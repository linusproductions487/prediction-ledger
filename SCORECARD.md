# Scorecard

Generated automatically from the ledger. Every miss is included.

- Predictions made: **35**
- Resolved (scored): **11**  ·  Void: **0**  ·  Pending: **24**
- Leaned the right way: **9/10** (excluding exact 50% calls)
- Brier score: **0.1826** (0 = perfect, 0.25 = coin flip, lower is better)
- Dumb-baseline Brier: **0.1759** — NOT beating the naive rule

## Calibration

When I say X%, does it happen X% of the time?

| Confidence band | Predictions | Stated | Actually true |
|---|---|---|---|
| 40–49% | 1 | 40.0% | 0.0% |
| 50–59% | 4 | 53.8% | 100.0% |
| 60–69% | 1 | 60.0% | 100.0% |
| 70–79% | 1 | 70.0% | 100.0% |
| 80–89% | 4 | 82.8% | 75.0% |

## By topic

| Topic | Resolved | Brier | Baseline Brier |
|---|---|---|---|
| economy | 3 | 0.1283 | 0.1842 |
| policy | 1 | 0.16 | 0.09 |
| google | 1 | 0.2025 | 0.36 |
| health | 2 | 0.1213 | 0.0625 |
| anthropic | 1 | 0.09 | 0.09 |
| market:gas | 1 | 0.6561 | 0.5476 |
| apple | 2 | 0.1363 | 0.085 |

## Paper trading (Kalshi)

Simulated $100 trades at the real Kalshi ask price when the prediction was locked, including Kalshi's taker fee. No real money. Rules are in PROTOCOL.md.

- Trades: **5**  ·  Settled: **1**  ·  Open: **4**
- Settled P&L: **-$101.72** on $101.72 risked (-100.0%)

| # | Market | Side | Price | Contracts | Fee | Cost | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 18 | [KXCPIYOY-26NOV Above 3.7%](https://kalshi.com/markets/kxcpiyoy/inflation/kxcpiyoy-26nov) | YES | 38¢ | 263 | $4.34 | $104.28 | open | — |
| 22 | [KXAAAGASD-26NOV20 Above 3.6900](https://kalshi.com/markets/kxaaagasd) | YES | 74¢ | 135 | $1.82 | $101.72 | false | -$101.72 |
| 23 | [KXAAAGASW-26NOV23 Above 3.6300](https://kalshi.com/markets/kxaaagasw) | NO | 44¢ | 227 | $3.92 | $103.80 | open | — |
| 25 | [KXHIGHCHI-26NOV20 68° to 69°](https://kalshi.com/markets/kxhighchi) | NO | 55¢ | 181 | $3.14 | $102.69 | open | — |
| 26 | [KXHIGHTBOS-26NOV20 68° to 69°](https://kalshi.com/markets/kxhightbos) | NO | 78¢ | 128 | $1.54 | $101.38 | open | — |

## Resolved

| # | Claim | By | Confidence | Outcome |
|---|---|---|---|---|
| 22 | Kalshi KXAAAGASD-26NOV20-3.6900 "Above 3.6900" settles YES (AAA national average regular gas price on Nov 20, 2026 is strictly above $3.6900). | claude | 81% | ❌ false |
| 16 | The FDA approves Sanofi's venglustat (type 3 Gaucher disease) by Dec 15, 2026. | claude | 55% | ✅ true |
| 15 | The FDA approves Nuvalent's neladalkib (ALK-positive NSCLC) by Dec 15, 2026. | claude | 80% | ✅ true |
| 8 | Anthropic announces a new Claude model that is not available as of Oct 3, 2026, by Dec 15, 2026. | claude | 70% | ✅ true |
| 14 | The US unemployment rate for October 2026 is 4.3% or higher. | claude | 40% | ✅ false |
| 10 | Chegg or Penske Media files a notice of appeal of Judge Mehta's dismissal of their AI Overviews antitrust suits by Nov 15, 2026. | claude | 60% | ✅ true |
| 11 | The Fed holds the federal funds target range at 3.75%-4.00% at its Oct 27-28, 2026 meeting. | claude | 85% | ✅ true |
| 1 | Apple announces at least one new hardware product by Oct 31, 2026. | claude | 85% | ✅ true |
| 3 | Apple announces a smart display / "HomePad"-type home hub product by Dec 31, 2026. | claude | 50% | ➖ true |
| 4 | Gemini 4 Argon becomes available through Google's paid API by Nov 15, 2026. | claude | 55% | ✅ true |
| 13 | US CPI for September 2026 (released Oct 14) shows a 12-month all-items increase of 3.5% or higher. | claude | 55% | ✅ true |

## Pending

| # | Claim | By | Confidence | Deadline (UTC) |
|---|---|---|---|---|
| 25 | Kalshi KXHIGHCHI-26NOV20-B68.5 "68° to 69°" settles YES (official high for Chicago (Midway) on Nov 20, 2026 is 68 or 69F). | claude | 38% | 2026-11-22 |
| 26 | Kalshi KXHIGHTBOS-26NOV20-B68.5 "68° to 69°" settles YES (official high for Boston on Nov 20, 2026 is 68 or 69F). | claude | 17% | 2026-11-22 |
| 27 | Kalshi KXHIGHNY-26NOV20-B66.5 "66° to 67°" settles YES (official high for New York City (Central Park) on Nov 20, 2026 is 66 or 67F). | claude | 38% | 2026-11-22 |
| 28 | Kalshi KXHIGHDEN-26NOV20-B61.5 "61° to 62°" settles YES (official high for Denver on Nov 20, 2026 is 61 or 62F). | claude | 32% | 2026-11-22 |
| 29 | Kalshi KXHIGHMIA-26NOV20-B82.5 "82° to 83°" settles YES (official high for Miami on Nov 20, 2026 is 82 or 83F). | claude | 43% | 2026-11-22 |
| 30 | Kalshi KXHIGHTNOLA-26NOV20-B70.5 "70° to 71°" settles YES (official high for New Orleans on Nov 20, 2026 is 70 or 71F). | claude | 26% | 2026-11-22 |
| 31 | Kalshi KXHIGHAUS-26NOV20-B74.5 "74° to 75°" settles YES (official high for Austin on Nov 20, 2026 is 74 or 75F). | claude | 28% | 2026-11-22 |
| 32 | Kalshi KXHIGHLAX-26NOV20-B68.5 "68° to 69°" settles YES (official high for Los Angeles (LAX) on Nov 20, 2026 is 68 or 69F). | claude | 13% | 2026-11-22 |
| 33 | Kalshi KXHIGHTBOS-26NOV21-B60.5 "60° to 61°" settles YES (official high for Boston on Nov 21, 2026 is 60 or 61F). | claude | 36% | 2026-11-23 |
| 34 | Kalshi KXHIGHTSFO-26NOV21-B57.5 "57° to 58°" settles YES (official high for San Francisco (SFO) on Nov 21, 2026 is 57 or 58F). | claude | 41% | 2026-11-23 |
| 35 | Kalshi KXHIGHTSEA-26NOV21-B48.5 "48° to 49°" settles YES (official high for Seattle (Sea-Tac) on Nov 21, 2026 is 48 or 49F). | claude | 33% | 2026-11-23 |
| 23 | Kalshi KXAAAGASW-26NOV23-3.6300 "Above 3.6300" settles YES (AAA national average regular gas price on Nov 23, 2026 is strictly above $3.6300). | claude | 47% | 2026-11-25 |
| 21 | Kalshi KXAAAGASM-26NOV30 "Above 3.50" settles YES (US average regular gas price at end of November 2026 is above $3.50). | claude | 45% | 2026-12-01 |
| 2 | Apple holds a livestreamed product event (not press-release-only) between Oct 3 and Nov 30, 2026. | claude | 35% | 2026-12-01 |
| 24 | Kalshi KXAAAGASM-26NOV30-3.45 "Above 3.45" settles YES (AAA national average regular gas price on Nov 30, 2026 is strictly above $3.45). | claude | 80% | 2026-12-02 |
| 20 | Kalshi KXFEDDECISION-26DEC "Hike 25bps" settles YES (the Fed raises rates by exactly 25bps on Dec 9, 2026). | claude | 88% | 2026-12-10 |
| 18 | Kalshi KXCPIYOY-26NOV "Above 3.7%" settles YES (US CPI-U 12-month change for November 2026, published Dec 10, is above 3.7%). | claude | 55% | 2026-12-11 |
| 19 | Kalshi KXCPI-26NOV "Above -0.1%" settles YES (US CPI-U seasonally adjusted month-over-month change for November 2026 is above -0.1%). | claude | 48% | 2026-12-11 |
| 12 | The Fed raises the federal funds target range at its December 2026 meeting. | claude | 70% | 2027-01-01 |
| 17 | SpaceX launches a Starship from Florida by Dec 31, 2026. | claude | 25% | 2027-01-01 |
| 5 | OpenAI publicly releases a model with "Astra" in its name by Dec 31, 2026. | claude | 10% | 2027-01-01 |
| 6 | OpenAI lowers GPT-6.1 Sol's standard API price below $2 input / $10 output per million tokens by Dec 31, 2026. | claude | 20% | 2027-01-01 |
| 7 | Tesla officially unveils Optimus Gen 3 by Dec 31, 2026. | claude | 25% | 2027-01-01 |
| 9 | An open-weights model ranks #1 on LMArena's overall text leaderboard at any point by Dec 31, 2026. | claude | 15% | 2027-01-01 |
