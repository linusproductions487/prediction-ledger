# Model vs. market

Scanned 2026-11-28 07:39 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +12¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 2¢ | 75% | 87% | $100 |  |
| +7¢ | KXAAAGASW-26NOV30-3.5200 | Above 3.5200 | YES | 9¢ | 23% | 16% | $100 |  |
| +6¢ | KXHIGHLAX-26NOV28-B75.5 | 75° to 76° | NO | 50¢ | 34% | 43% | $100 | center 76.0, market mean 75.45, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXHIGHTDAL-26NOV28-B72.5 | 72° to 73° | NO | 39¢ | 38% | 50% | $0 | center 72.6, market mean 72.23, lead 0d |
| +11¢ | KXHIGHTMIN-26NOV28-B46.5 | 46° to 47° | YES | 3¢ | 26% | 14% | $0 | center 48.45, market mean 50.69, lead 0d |
| +11¢ | KXHIGHTDC-26NOV28-B56.5 | 56° to 57° | YES | 8¢ | 31% | 19% | $0 | center 57.85, market mean 59.27, lead 0d |
| +11¢ | KXHIGHTATL-26NOV28-B58.5 | 58° to 59° | YES | 2¢ | 24% | 13% | $0 | center 60.4, market mean 62.1, lead 0d |
| +10¢ | KXHIGHTATL-26NOV28-B62.5 | 62° to 63° | NO | 34¢ | 23% | 56% | $0 | center 60.4, market mean 62.1, lead 0d |
| +10¢ | KXHIGHPHIL-26NOV28-T52 | 51° or below | YES | 2¢ | 23% | 12% | $0 | center 53.0, market mean 54.58, lead 0d |
| +10¢ | KXHIGHMIA-26NOV28-B71.5 | 71° to 72° | YES | 9¢ | 29% | 19% | $0 | center 72.75, market mean 73.92, lead 0d |
| +9¢ | KXHIGHTSATX-26NOV28-B70.5 | 70° to 71° | YES | 9¢ | 30% | 18% | $0 | center 72.15, market mean 72.98, lead 0d |
| +9¢ | KXHIGHMIA-26NOV28-B73.5 | 73° to 74° | NO | 34¢ | 30% | 57% | $0 | center 72.75, market mean 73.92, lead 0d |
| +8¢ | KXHIGHCHI-26NOV28-B52.5 | 52° to 53° | NO | 48¢ | 36% | 44% | $0 | center 51.75, market mean 53.2, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV28-T51 | 52° or above | NO | 74¢ | 7% | 18% | $0 | center 48.45, market mean 50.69, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV28-B73.5 | 73° to 74° | YES | 10¢ | 26% | 18% | $0 | center 75.35, market mean 75.82, lead 0d |
| +7¢ | KXHIGHPHIL-26NOV28-B52.5 | 52° to 53° | YES | 20¢ | 37% | 27% | $0 | center 53.0, market mean 54.58, lead 0d |
| +7¢ | KXHIGHTNOLA-26NOV28-T70 | 71° or above | YES | 3¢ | 19% | 10% | $0 | center 67.15, market mean 67.19, lead 0d |
| +7¢ | KXHIGHAUS-26NOV28-B75.5 | 75° to 76° | NO | 51¢ | 19% | 42% | $0 | center 73.15, market mean 74.52, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV28-B61.5 | 61° to 62° | YES | 7¢ | 22% | 14% | $0 | center 63.75, market mean 64.81, lead 0d |
| +7¢ | KXHIGHTHOU-26NOV28-B75.5 | 75° to 76° | NO | 45¢ | 38% | 48% | $0 | center 75.65, market mean 75.28, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV28-T51 | 50° or below | YES | 11¢ | 42% | 18% | $0 | center 50.85, market mean 51.86, lead 0d |
| +7¢ | KXHIGHTSEA-26NOV28-B50.5 | 50° to 51° | NO | 42¢ | 29% | 51% | $0 | center 49.15, market mean 50.33, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV28-B75.5 | 75° to 76° | NO | 33¢ | 38% | 60% | $0 | center 75.35, market mean 75.82, lead 0d |
| +6¢ | KXHIGHAUS-26NOV28-B71.5 | 71° to 72° | YES | 2¢ | 30% | 9% | $0 | center 73.15, market mean 74.52, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV28-B48.5 | 48° to 49° | YES | 10¢ | 37% | 16% | $0 | center 48.45, market mean 50.69, lead 0d |
| +6¢ | KXHIGHCHI-26NOV28-B50.5 | 50° to 51° | YES | 7¢ | 32% | 13% | $0 | center 51.75, market mean 53.2, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV28-B50.5 | 50° to 51° | NO | 46¢ | 23% | 48% | $0 | center 48.45, market mean 50.69, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV28-B54.5 | 54° to 55° | NO | 43¢ | 30% | 51% | $0 | center 53.0, market mean 54.58, lead 0d |
| +5¢ | KXHIGHTNOLA-26NOV28-B67.5 | 67° to 68° | NO | 50¢ | 19% | 45% | $0 | center 67.15, market mean 67.19, lead 0d |
| +3¢ | KXHIGHTSFO-26NOV28-B64.5 | 64° to 65° | NO | 70¢ | 18% | 27% | $100 | center 65.8, market mean 64.01, lead 1d |
| +3¢ | KXHIGHTSEA-26NOV28-B46.5 | 46° to 47° | YES | 7¢ | 18% | 10% | $100 | center 49.15, market mean 50.33, lead 1d |
| +2¢ | KXHIGHTLV-26NOV28-B67.5 | 67° to 68° | NO | 64¢ | 28% | 34% | $100 | center 68.9, market mean 68.42, lead 1d |
| +1¢ | KXHIGHTLV-26NOV28-B71.5 | 71° to 72° | YES | 10¢ | 19% | 11% | $100 | center 68.9, market mean 68.42, lead 1d |
