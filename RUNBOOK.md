# Daily runbook

How a Claude session runs the ledger each day. PROTOCOL.md has the rules; this file is the procedure.

**Database:** Supabase project `werawuijbdvqgwpxvciu`, schema `ledger` (use the Supabase tools).
**Repo:** `linusproductions487/prediction-ledger` (use the GitHub tools, or attach and clone it).

## 1. Get a fresh scan
The GitHub Action runs `scan.py` every 6 hours and on every push to `main`. It writes:
- `markets.json`: live Kalshi prices, model probabilities and every model input, with `scanned_at`
- `EDGES.md`: tradeable candidates, already checked against the real order book
- `data/settled.json`: Kalshi's own settlement results (`result`, `expiration_value`)
- `data/wx_history.jsonl`, `data/gas_history.jsonl`: forecast history used for calibration

A session cannot reach Kalshi directly, so the scan is the only price source. To get a fresh one,
commit the current UTC time to `scan_request.txt` on `main`, wait for the next
`ledger-anchor[bot]` commit (2 to 6 minutes), then read `markets.json`.
**Never lock a trade on a scan older than 20 minutes.** The scan's commit is the public proof of the price.

Check `markets.json → log` for errors before trusting a scan.

## 2. Settle what is due
```sql
select seq, claim, deadline from ledger.pending order by deadline;
```
For each market prediction whose ticker is in `data/settled.json` with `result` yes or no:
```sql
select ledger.settle_market('<market ticker>', '<yes|no>',
  'https://kalshi.com/markets/<series lowercase>', 'Kalshi settled <result>; reported value <expiration_value>');
```
Predictions 18 to 21 were logged by event, so settle them with the event ticker
(`KXCPIYOY-26NOV`, `KXCPI-26NOV`, `KXFEDDECISION-26DEC`, `KXAAAGASM-26NOV30`).
Non-market predictions are resolved by hand: web search, then
`insert into ledger.resolutions (prediction_id, outcome, evidence_url, notes)`.

## 3. Pick trades
Take them from the **Tradeable candidates** table in `EDGES.md`. The scanner has already applied:
- **Blend rule:** confidence is the model averaged 50/50 with the market's own price. The market is a
  strong forecaster and the models are unproven. A raw gap over 25 points is treated as a model or
  data error and is never tradeable.
- **Tomorrow only:** same-day weather markets trade on live thermometer readings we lag. Not tradeable.
- **Real fills:** the price is what $100 actually costs walking the order book, not the top quote.

Then check each candidate by hand in `markets.json`:
- `prob_sum` near 1.0, `lo`/`hi` match the label, 4+ forecast `models`, 50+ `ens_members`
- Anything odd in the inputs (a stale `nws_updated`, one model far from the rest) means skip it
- One trade per event (enforced by the database): take the largest edge
- Weather markets for tomorrow are thin until early afternoon Eastern. Trade them after 3 pm ET.
- No quota. Zero trades is a fine day.

Also log two or three no-edge markets a day with `p_allow_trade => false`, so calibration data
does not come only from disagreements.

## 4. Lock them in
```sql
select ledger.log_market_call(
  p_topic => 'market:weather',                     -- or market:gas, market:economy
  p_market_ticker => 'KXHIGHNY-26NOV20-B66.5',
  p_event_ticker => 'KXHIGHNY-26NOV20',
  p_label => '66° to 67°',
  p_description => 'official high for New York City on Nov 20, 2026 is 66 or 67F',
  p_confidence => 38,                              -- blend_p as a whole percent; change it only with a stated reason
  p_yes_ask => 50, p_no_ask => 59,                 -- traded side: fill.fill_price. Other side: its ask, rounded up
  p_deadline => '2026-11-22 12:00-05',             -- two days after the event date
  p_rationale => 'Model 28% (center 65.3: NWS 64, NBM 65.3, HRRR 67.8, ECMWF 63.1; 82 ensemble members, sd 0.5), market mid 48%, blend 38%. ...',
  p_price_source => 'scan 2026-11-19T15:33Z, $100 order-book fill');
```
The function applies the 5-cent rule, the one-trade-per-event rule, sizing and fees, and returns the
decision. Put all of a day's calls in one SQL statement. Rationales must name the model inputs.

## 5. Keep the models honest
- `markets.json → calibration` shows each city's day-ahead bias and error once days settle; the
  scanner applies it automatically after 8 settled days per city.
- Every 25 settled trades, compare P&L and Brier by topic against the market baseline:
  `select * from ledger.scorecard_by_topic;` and `select topic, count(*), sum(pnl_cents) from ledger.paper_pnl join ledger.predictions using (seq) where pnl_cents is not null group by 1;`
- If a model loses after fees over 50+ settled trades, stop trading it and write a lesson.
  If it wins over 50+, the blend weight may be raised, as a recorded protocol change.
- Any bug, bad input or surprise gets a lesson the same day (`insert into ledger.lessons (topic, lesson, evidence_prediction_ids)`).
- Model changes go in `scan.py` with a commit message that says why.

## 6. Report
End with: what settled and its P&L, what was traded and why, and running totals:
`select count(*) trades, count(pnl_cents) settled, sum(pnl_cents) pnl_cents from ledger.paper_pnl;`
