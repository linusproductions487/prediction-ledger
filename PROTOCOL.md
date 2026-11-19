# Protocol

These rules exist so the scorecard measures reality, not spin.

## Making a prediction
1. **Domain:** objectively resolvable questions across technology, AI, economics, business, science and health, and space.
2. **Confidence** is the probability (1–99%) that the claim resolves TRUE. 0% and 100% are not allowed.
3. **Resolution criteria** are written before the outcome and must be objective enough that a stranger would reach the same verdict.
4. **Source of truth** names where the answer will be checked (an official blog, a government release, a market's settlement).
5. **Deadline** is fixed when the prediction is made, and the database rejects any deadline in the past.
6. **Rationale** is pre-registered: the reasoning is written down and hashed with the claim, so a miss can be traced to the assumption that failed, and the reasoning can't be rewritten afterward.
7. **Baseline:** every prediction also records what a naive rule would say (e.g. "status quo holds", "announced dates slip") and its confidence. For market predictions the baseline is the market's own price. The scorecard shows whether the forecaster beats that baseline; a good score on easy questions proves nothing.
8. **Anyone can play.** The `made_by` field records the forecaster. Human entries follow exactly the same rules and appear on the same public scorecard.
9. Once inserted, a prediction can never be edited or deleted. A changed view becomes a **new** prediction; the old one still gets scored.

## Paper trading
Market predictions (topic `market:*`) are tied to a real, open contract on **Kalshi**, a CFTC-regulated US exchange, so every trade is one that could actually have been placed. No real money is used.

1. **Real prices only.** Prices come from the public scanner (`scan.py`, run by GitHub Actions), which reads Kalshi's live order book and commits it to this repo. The entry price is what buying $100 would really cost walking that book, from a scan no more than 20 minutes old. The scan's commit is the proof. (Trade #1 predates the scanner and used the ask shown on the market page.)
2. **The claim is the contract.** A market prediction resolves TRUE exactly when Kalshi settles that contract YES.
3. **Trade rule:** buy only when my probability beats the fill price by **at least 5 cents**. Otherwise the prediction is still logged (for calibration) with "no trade."
   - **Blend rule:** for model-driven markets my probability is the model averaged 50/50 with the market's own price, until that model has 50+ settled trades. A raw model-vs-market gap above 25 points is treated as a model error and is never traded.
   - **No same-day weather trades:** those markets move on live readings the scanner lags.
4. **Fixed size:** $100 per trade, as many whole contracts as $100 buys at the ask.
5. **Real fees:** Kalshi's taker fee, `ceil(0.07 × contracts × price × (1 − price))`, is charged on every trade.
6. **One trade per underlying event.** Several contracts that hinge on the same data release count as one bet, so only one of them may be traded.
7. **Locked together.** A trade must be logged within 10 minutes of its prediction, and trades are append-only like everything else.
8. **The real test is P&L, not hit rate.** Buying a likely outcome at a high price can win often and still lose money. A strategy shows an edge only if it profits after fees over many trades; anything under ~100 settled trades is mostly noise.

Known issue: trade #1 (prediction 18) recorded a fee of $0.44 instead of the correct $4.34 because of a bug that was fixed the same day. The row can't be edited, so the scorecard recomputes the fee from the formula above.

## Reviewing drafts
Drafts may be dropped before locking **only** for being ambiguous or unverifiable, never because they look likely to be wrong.

## Resolving
1. A prediction is resolved once, with a public **evidence URL**.
2. Outcomes: `true`, `false`, or `void`. **Void** is only for questions that became impossible to resolve (e.g. the source of truth disappeared), and the reason must be written in the notes. Voids are counted and shown on the scorecard.
3. Claude resolves its own predictions, which is a conflict of interest. That's why criteria are fixed in advance and evidence is public: anyone can check a verdict and dispute it by opening an issue.

## Learning
Misses are reviewed for patterns and written to the `lessons` table (also append-only). Lessons are revised by superseding, never by editing.
