# Protocol

These rules exist so the scorecard measures reality, not spin.

## Making a prediction
1. **Domain:** technology and AI developments (releases, benchmarks, product and policy changes).
2. **Confidence** is the probability (1–99%) that the claim resolves TRUE. 0% and 100% are not allowed.
3. **Resolution criteria** are written before the outcome and must be objective enough that a stranger would reach the same verdict.
4. **Source of truth** names where the answer will be checked (an official blog, a leaderboard, a changelog).
5. **Deadline** is fixed when the prediction is made, and the database rejects any deadline in the past.
6. **Rationale** is pre-registered: the reasoning is written down and hashed with the claim, so a miss can be traced to the assumption that failed, and the reasoning can't be rewritten afterward.
7. **Baseline:** every prediction also records what a naive rule would say (e.g. "status quo holds", "announced dates slip") and its confidence. The scorecard shows whether the forecaster beats that dumb rule; a good score on easy questions proves nothing.
8. **Anyone can play.** The `made_by` field records the forecaster. Human entries follow exactly the same rules and appear on the same public scorecard.
9. Once inserted, a prediction can never be edited or deleted. A changed view becomes a **new** prediction; the old one still gets scored.

## Reviewing drafts
Drafts may be dropped before locking **only** for being ambiguous or unverifiable, never because they look likely to be wrong.

## Resolving
1. A prediction is resolved once, with a public **evidence URL**.
2. Outcomes: `true`, `false`, or `void`. **Void** is only for questions that became impossible to resolve (e.g. the source of truth disappeared), and the reason must be written in the notes. Voids are counted and shown on the scorecard.
3. Claude resolves its own predictions, which is a conflict of interest. That's why criteria are fixed in advance and evidence is public: anyone can check a verdict and dispute it by opening an issue.

## Learning
Misses are reviewed for patterns and written to the `lessons` table (also append-only). Lessons are revised by superseding, never by editing.
