# Scorecard

Generated automatically from the ledger. Every miss is included.

- Predictions made: **21**
- Resolved (scored): **7**  ·  Void: **0**  ·  Pending: **14**
- Leaned the right way: **6/6** (excluding exact 50% calls)
- Brier score: **0.1457** (0 = perfect, 0.25 = coin flip, lower is better)
- Dumb-baseline Brier: **0.1675** — beating the naive rule

## Calibration

When I say X%, does it happen X% of the time?

| Confidence band | Predictions | Stated | Actually true |
|---|---|---|---|
| 40–49% | 1 | 40.0% | 0.0% |
| 50–59% | 3 | 53.3% | 100.0% |
| 60–69% | 1 | 60.0% | 100.0% |
| 80–89% | 2 | 85.0% | 100.0% |

## By topic

| Topic | Resolved | Brier | Baseline Brier |
|---|---|---|---|
| economy | 3 | 0.1283 | 0.1842 |
| policy | 1 | 0.16 | 0.09 |
| google | 1 | 0.2025 | 0.36 |
| apple | 2 | 0.1363 | 0.085 |

## Paper trading (Kalshi)

Simulated $100 trades at the real Kalshi ask price when the prediction was locked, including Kalshi's taker fee. No real money. Rules are in PROTOCOL.md.

- Trades: **1**  ·  Settled: **0**  ·  Open: **1**
- Settled P&L: **+$0.00**

| # | Market | Side | Price | Contracts | Fee | Cost | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 18 | [KXCPIYOY-26NOV Above 3.7%](https://kalshi.com/markets/kxcpiyoy/inflation/kxcpiyoy-26nov) | YES | 38¢ | 263 | $4.34 | $104.28 | open | — |

## Resolved

| # | Claim | By | Confidence | Outcome |
|---|---|---|---|---|
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
| 21 | Kalshi KXAAAGASM-26NOV30 "Above 3.50" settles YES (US average regular gas price at end of November 2026 is above $3.50). | claude | 45% | 2026-12-01 |
| 2 | Apple holds a livestreamed product event (not press-release-only) between Oct 3 and Nov 30, 2026. | claude | 35% | 2026-12-01 |
| 20 | Kalshi KXFEDDECISION-26DEC "Hike 25bps" settles YES (the Fed raises rates by exactly 25bps on Dec 9, 2026). | claude | 88% | 2026-12-10 |
| 18 | Kalshi KXCPIYOY-26NOV "Above 3.7%" settles YES (US CPI-U 12-month change for November 2026, published Dec 10, is above 3.7%). | claude | 55% | 2026-12-11 |
| 19 | Kalshi KXCPI-26NOV "Above -0.1%" settles YES (US CPI-U seasonally adjusted month-over-month change for November 2026 is above -0.1%). | claude | 48% | 2026-12-11 |
| 15 | The FDA approves Nuvalent's neladalkib (ALK-positive NSCLC) by Dec 15, 2026. | claude | 80% | 2026-12-16 |
| 16 | The FDA approves Sanofi's venglustat (type 3 Gaucher disease) by Dec 15, 2026. | claude | 55% | 2026-12-16 |
| 8 | Anthropic announces a new Claude model that is not available as of Oct 3, 2026, by Dec 15, 2026. | claude | 70% | 2026-12-16 |
| 12 | The Fed raises the federal funds target range at its December 2026 meeting. | claude | 70% | 2027-01-01 |
| 17 | SpaceX launches a Starship from Florida by Dec 31, 2026. | claude | 25% | 2027-01-01 |
| 5 | OpenAI publicly releases a model with "Astra" in its name by Dec 31, 2026. | claude | 10% | 2027-01-01 |
| 6 | OpenAI lowers GPT-6.1 Sol's standard API price below $2 input / $10 output per million tokens by Dec 31, 2026. | claude | 20% | 2027-01-01 |
| 7 | Tesla officially unveils Optimus Gen 3 by Dec 31, 2026. | claude | 25% | 2027-01-01 |
| 9 | An open-weights model ranks #1 on LMArena's overall text leaderboard at any point by Dec 31, 2026. | claude | 15% | 2027-01-01 |
