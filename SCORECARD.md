# Scorecard

Generated automatically from the ledger. Every miss is included.

- Predictions made: **47**
- Resolved (scored): **22**  ·  Void: **0**  ·  Pending: **25**
- Leaned the right way: **15/21** (excluding exact 50% calls)
- Brier score: **0.2201** (0 = perfect, 0.25 = coin flip, lower is better)
- Dumb-baseline Brier: **0.2066** — NOT beating the naive rule

## Calibration

When I say X%, does it happen X% of the time?

| Confidence band | Predictions | Stated | Actually true |
|---|---|---|---|
| 10–19% | 2 | 15.0% | 50.0% |
| 20–29% | 2 | 27.0% | 50.0% |
| 30–39% | 5 | 35.4% | 20.0% |
| 40–49% | 3 | 41.3% | 66.7% |
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
| market:weather | 11 | 0.2577 | 0.2373 |
| apple | 2 | 0.1363 | 0.085 |

## Paper trading (Kalshi)

Simulated $100 trades at the real Kalshi ask price when the prediction was locked, including Kalshi's taker fee. No real money. Rules are in PROTOCOL.md.

- Trades: **11**  ·  Settled: **3**  ·  Open: **8**
- Settled P&L: **-$305.79** on $305.79 risked (-100.0%)

| # | Market | Side | Price | Contracts | Fee | Cost | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 18 | [KXCPIYOY-26NOV Above 3.7%](https://kalshi.com/markets/kxcpiyoy/inflation/kxcpiyoy-26nov) | YES | 38¢ | 263 | $4.34 | $104.28 | open | — |
| 22 | [KXAAAGASD-26NOV20 Above 3.6900](https://kalshi.com/markets/kxaaagasd) | YES | 74¢ | 135 | $1.82 | $101.72 | false | -$101.72 |
| 23 | [KXAAAGASW-26NOV23 Above 3.6300](https://kalshi.com/markets/kxaaagasw) | NO | 44¢ | 227 | $3.92 | $103.80 | open | — |
| 25 | [KXHIGHCHI-26NOV20 68° to 69°](https://kalshi.com/markets/kxhighchi) | NO | 55¢ | 181 | $3.14 | $102.69 | true | -$102.69 |
| 26 | [KXHIGHTBOS-26NOV20 68° to 69°](https://kalshi.com/markets/kxhightbos) | NO | 78¢ | 128 | $1.54 | $101.38 | true | -$101.38 |
| 39 | [KXHIGHMIA-26NOV22 85° to 86°](https://kalshi.com/markets/kxhighmia) | NO | 49¢ | 204 | $3.57 | $103.53 | open | — |
| 40 | [KXHIGHPHIL-26NOV22 65° to 66°](https://kalshi.com/markets/kxhighphil) | NO | 62¢ | 161 | $2.66 | $102.48 | open | — |
| 41 | [KXHIGHLAX-26NOV23 69° to 70°](https://kalshi.com/markets/kxhighlax) | NO | 53¢ | 188 | $3.28 | $102.92 | open | — |
| 42 | [KXHIGHTBOS-26NOV23 68° to 69°](https://kalshi.com/markets/kxhightbos) | NO | 72¢ | 138 | $1.95 | $101.31 | open | — |
| 43 | [KXHIGHPHIL-26NOV23 67° to 68°](https://kalshi.com/markets/kxhighphil) | NO | 55¢ | 181 | $3.14 | $102.69 | open | — |
| 44 | [KXAAAGASM-26NOV30 Above 3.55](https://kalshi.com/markets/kxaaagasm) | YES | 7¢ | 1428 | $6.51 | $106.47 | open | — |

## Resolved

| # | Claim | By | Confidence | Outcome |
|---|---|---|---|---|
| 34 | Kalshi KXHIGHTSFO-26NOV21-B57.5 "57° to 58°" settles YES (official high for San Francisco (SFO) on Nov 21, 2026 is 57 or 58F). | claude | 41% | ❌ true |
| 35 | Kalshi KXHIGHTSEA-26NOV21-B48.5 "48° to 49°" settles YES (official high for Seattle (Sea-Tac) on Nov 21, 2026 is 48 or 49F). | claude | 33% | ✅ false |
| 33 | Kalshi KXHIGHTBOS-26NOV21-B60.5 "60° to 61°" settles YES (official high for Boston on Nov 21, 2026 is 60 or 61F). | claude | 36% | ✅ false |
| 31 | Kalshi KXHIGHAUS-26NOV20-B74.5 "74° to 75°" settles YES (official high for Austin on Nov 20, 2026 is 74 or 75F). | claude | 28% | ❌ true |
| 32 | Kalshi KXHIGHLAX-26NOV20-B68.5 "68° to 69°" settles YES (official high for Los Angeles (LAX) on Nov 20, 2026 is 68 or 69F). | claude | 13% | ✅ false |
| 25 | Kalshi KXHIGHCHI-26NOV20-B68.5 "68° to 69°" settles YES (official high for Chicago (Midway) on Nov 20, 2026 is 68 or 69F). | claude | 38% | ❌ true |
| 27 | Kalshi KXHIGHNY-26NOV20-B66.5 "66° to 67°" settles YES (official high for New York City (Central Park) on Nov 20, 2026 is 66 or 67F). | claude | 38% | ✅ false |
| 28 | Kalshi KXHIGHDEN-26NOV20-B61.5 "61° to 62°" settles YES (official high for Denver on Nov 20, 2026 is 61 or 62F). | claude | 32% | ✅ false |
| 29 | Kalshi KXHIGHMIA-26NOV20-B82.5 "82° to 83°" settles YES (official high for Miami on Nov 20, 2026 is 82 or 83F). | claude | 43% | ❌ true |
| 30 | Kalshi KXHIGHTNOLA-26NOV20-B70.5 "70° to 71°" settles YES (official high for New Orleans on Nov 20, 2026 is 70 or 71F). | claude | 26% | ✅ false |
| 26 | Kalshi KXHIGHTBOS-26NOV20-B68.5 "68° to 69°" settles YES (official high for Boston on Nov 20, 2026 is 68 or 69F). | claude | 17% | ❌ true |
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
| 36 | Kalshi KXHIGHCHI-26NOV22-B60.5 "60° to 61°" settles YES (official high for Chicago (Midway) on Nov 22, 2026 is 60 or 61F). | claude | 42% | 2026-11-24 |
| 37 | Kalshi KXHIGHAUS-26NOV22-B73.5 "73° to 74°" settles YES (official high for Austin on Nov 22, 2026 is 73 or 74F). | claude | 38% | 2026-11-24 |
| 38 | Kalshi KXHIGHTNOLA-26NOV22-B76.5 "76° to 77°" settles YES (official high for New Orleans on Nov 22, 2026 is 76 or 77F). | claude | 33% | 2026-11-24 |
| 39 | Kalshi KXHIGHMIA-26NOV22-B85.5 "85° to 86°" settles YES (official high for Miami on Nov 22, 2026 is 85 or 86F). | claude | 42% | 2026-11-24 |
| 40 | Kalshi KXHIGHPHIL-26NOV22-B65.5 "65° to 66°" settles YES (official high for Philadelphia on Nov 22, 2026 is 65 or 66F). | claude | 32% | 2026-11-24 |
| 23 | Kalshi KXAAAGASW-26NOV23-3.6300 "Above 3.6300" settles YES (AAA national average regular gas price on Nov 23, 2026 is strictly above $3.6300). | claude | 47% | 2026-11-25 |
| 41 | Kalshi KXHIGHLAX-26NOV23-B69.5 "69° to 70°" settles YES (official high for Los Angeles (LAX) on Nov 23, 2026 is 69 or 70F). | claude | 40% | 2026-11-25 |
| 42 | Kalshi KXHIGHTBOS-26NOV23-B68.5 "68° to 69°" settles YES (official high for Boston on Nov 23, 2026 is 68 or 69F). | claude | 22% | 2026-11-25 |
| 43 | Kalshi KXHIGHPHIL-26NOV23-B67.5 "67° to 68°" settles YES (official high for Philadelphia on Nov 23, 2026 is 67 or 68F). | claude | 40% | 2026-11-25 |
| 45 | Kalshi KXHIGHTMIN-26NOV23-B30.5 "30° to 31°" settles YES (official high for Minneapolis on Nov 23, 2026 is 30 or 31F). | claude | 30% | 2026-11-25 |
| 46 | Kalshi KXHIGHTSFO-26NOV23-B59.5 "59° to 60°" settles YES (official high for San Francisco (SFO) on Nov 23, 2026 is 59 or 60F). | claude | 26% | 2026-11-25 |
| 47 | Kalshi KXHIGHTDAL-26NOV23-B59.5 "59° to 60°" settles YES (official high for Dallas (DFW) on Nov 23, 2026 is 59 or 60F). | claude | 25% | 2026-11-25 |
| 21 | Kalshi KXAAAGASM-26NOV30 "Above 3.50" settles YES (US average regular gas price at end of November 2026 is above $3.50). | claude | 45% | 2026-12-01 |
| 2 | Apple holds a livestreamed product event (not press-release-only) between Oct 3 and Nov 30, 2026. | claude | 35% | 2026-12-01 |
| 24 | Kalshi KXAAAGASM-26NOV30-3.45 "Above 3.45" settles YES (AAA national average regular gas price on Nov 30, 2026 is strictly above $3.45). | claude | 80% | 2026-12-02 |
| 44 | Kalshi KXAAAGASM-26NOV30-3.55 "Above 3.55" settles YES (AAA national average regular gas price on Nov 30, 2026 is strictly above $3.55). | claude | 16% | 2026-12-02 |
| 20 | Kalshi KXFEDDECISION-26DEC "Hike 25bps" settles YES (the Fed raises rates by exactly 25bps on Dec 9, 2026). | claude | 88% | 2026-12-10 |
| 18 | Kalshi KXCPIYOY-26NOV "Above 3.7%" settles YES (US CPI-U 12-month change for November 2026, published Dec 10, is above 3.7%). | claude | 55% | 2026-12-11 |
| 19 | Kalshi KXCPI-26NOV "Above -0.1%" settles YES (US CPI-U seasonally adjusted month-over-month change for November 2026 is above -0.1%). | claude | 48% | 2026-12-11 |
| 12 | The Fed raises the federal funds target range at its December 2026 meeting. | claude | 70% | 2027-01-01 |
| 17 | SpaceX launches a Starship from Florida by Dec 31, 2026. | claude | 25% | 2027-01-01 |
| 5 | OpenAI publicly releases a model with "Astra" in its name by Dec 31, 2026. | claude | 10% | 2027-01-01 |
| 6 | OpenAI lowers GPT-6.1 Sol's standard API price below $2 input / $10 output per million tokens by Dec 31, 2026. | claude | 20% | 2027-01-01 |
| 7 | Tesla officially unveils Optimus Gen 3 by Dec 31, 2026. | claude | 25% | 2027-01-01 |
| 9 | An open-weights model ranks #1 on LMArena's overall text leaderboard at any point by Dec 31, 2026. | claude | 15% | 2027-01-01 |
