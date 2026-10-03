# Prediction Ledger

A public, tamper-evident record of Claude's predictions about technology and AI.
Every forecast is locked **before** its outcome is known, and every miss stays on the record.

**→ [SCORECARD.md](SCORECARD.md)** for current results  ·  **[PROTOCOL.md](PROTOCOL.md)** for the rules

## Why
An AI model usually gives an answer and never learns whether it was right. This ledger closes that loop:
predictions are scored against reality, calibration is measured ("when I say 70%, does it happen 70% of the time?"),
and lessons from misses are fed back into future sessions.

## How integrity works
- **Append-only database.** Triggers block every update, delete and truncate on predictions and resolutions.
- **Hash chain.** Each entry's SHA-256 hash covers its content *and* the previous entry's hash, so changing anything breaks every hash after it.
- **Server timestamps.** The database sets creation time itself; entries can't be backdated.
- **External anchor.** Every 6 hours a GitHub Action exports the full ledger to [`ledger.json`](ledger.json), verifies it, and appends the chain heads to [`ANCHORS.md`](ANCHORS.md). Removing or rewriting an entry that was ever anchored is detectable.

## Verify it yourself
No trust in the database, this repo's automation, or Claude required:

```
python3 verify.py ledger.json
```

The script uses only Python's standard library and recomputes every hash from the raw fields.

## Honest limits
- The repo owner could force-push to rewrite Git history. Forks and clones made by anyone else preserve the old history, which is why public visibility matters.
- Database `id` values can have gaps (from rolled-back test transactions). `seq` is the gapless chain order.
- Claude resolves its own predictions. Criteria are fixed in advance and evidence is linked so verdicts can be audited and disputed.
