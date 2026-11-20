# Model vs. market

Scanned 2026-11-20 15:37 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +8¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 51¢ | 33% | 41% | $100 |  |
| +5¢ | KXHIGHTPHX-26NOV21-T67 | 66° or below | YES | 17¢ | 34% | 22% | $100 | center 67.5, market mean 68.21, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +17¢ | KXAAAGASW-26NOV23-3.6200 | Above 3.6200 | NO | 2¢ | 29% | 81% | $0 |  |
| +11¢ | KXHIGHTMIN-26NOV20-B66.5 | 66° to 67° | NO | 49¢ | 28% | 40% | $0 | center 64.85, market mean 66.39, lead 0d |
| +11¢ | KXHIGHTLV-26NOV20-B56.5 | 56° to 57° | YES | 5¢ | 27% | 16% | $0 | center 58.15, market mean 59.02, lead 0d |
| +10¢ | KXHIGHTNOLA-26NOV20-B72.5 | 72° to 73° | NO | 53¢ | 26% | 37% | $0 | center 71.95, market mean 72.69, lead 0d |
| +10¢ | KXAAAGASD-26NOV21-3.6600 | Above 3.6600 | YES | 25¢ | 74% | 35% | $0 |  |
| +10¢ | KXHIGHCHI-26NOV20-B66.5 | 66° to 67° | YES | 7¢ | 28% | 17% | $0 | center 68.15, market mean 68.77, lead 0d |
| +10¢ | KXAAAGASW-26NOV23-3.6250 | Above 3.6250 | NO | 19¢ | 19% | 71% | $0 |  |
| +10¢ | KXHIGHAUS-26NOV20-T74 | 73° or below | YES | 2¢ | 23% | 12% | $0 | center 75.0, market mean 76.08, lead 0d |
| +10¢ | KXHIGHLAX-26NOV20-B66.5 | 66° to 67° | NO | 33¢ | 27% | 57% | $0 | center 65.0, market mean 66.32, lead 0d |
| +10¢ | KXHIGHTBOS-26NOV20-B68.5 | 68° to 69° | NO | 50¢ | 10% | 40% | $0 | center 65.05, market mean 67.51, lead 0d |
| +10¢ | KXHIGHTDC-26NOV20-B68.5 | 68° to 69° | YES | 15¢ | 36% | 25% | $0 | center 69.0, market mean 70.75, lead 0d |
| +10¢ | KXHIGHTSFO-26NOV20-B55.5 | 55° to 56° | YES | 5¢ | 25% | 15% | $0 | center 57.45, market mean 58.11, lead 0d |
| +10¢ | KXHIGHAUS-26NOV20-B76.5 | 76° to 77° | NO | 33¢ | 26% | 57% | $0 | center 75.0, market mean 76.08, lead 0d |
| +9¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 50¢ | 11% | 41% | $0 |  |
| +9¢ | KXHIGHPHIL-26NOV20-B70.5 | 70° to 71° | NO | 38¢ | 20% | 53% | $0 | center 68.1, market mean 70.13, lead 0d |
| +9¢ | KXHIGHTDAL-26NOV20-B72.5 | 72° to 73° | YES | 7¢ | 26% | 16% | $0 | center 74.4, market mean 74.89, lead 0d |
| +9¢ | KXHIGHTMIN-26NOV20-B64.5 | 64° to 65° | YES | 19¢ | 38% | 28% | $0 | center 64.85, market mean 66.39, lead 0d |
| +9¢ | KXHIGHTDC-26NOV20-B72.5 | 72° to 73° | NO | 71¢ | 10% | 20% | $0 | center 69.0, market mean 70.75, lead 0d |
| +9¢ | KXHIGHTPHX-26NOV20-B72.5 | 72° to 73° | NO | 38¢ | 26% | 53% | $0 | center 70.65, market mean 71.95, lead 0d |
| +9¢ | KXHIGHTNOLA-26NOV21-B73.5 | 73° to 74° | NO | 45¢ | 19% | 46% | $0 | center 73.4, market mean 73.76, lead 1d |
| +8¢ | KXHIGHMIA-26NOV20-B82.5 | 82° to 83° | NO | 48¢ | 32% | 43% | $0 | center 83.2, market mean 82.07, lead 0d |
| +8¢ | KXHIGHTLV-26NOV20-B58.5 | 58° to 59° | NO | 32¢ | 33% | 60% | $0 | center 58.15, market mean 59.02, lead 0d |
| +8¢ | KXHIGHTOKC-26NOV20-B69.5 | 69° to 70° | NO | 45¢ | 38% | 47% | $0 | center 69.75, market mean 70.21, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV20-B73.5 | 73° to 74° | NO | 31¢ | 35% | 61% | $0 | center 73.05, market mean 73.75, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV20-B57.5 | 57° to 58° | NO | 43¢ | 38% | 49% | $0 | center 57.45, market mean 58.11, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV20-B62.5 | 62° to 63° | YES | 2¢ | 18% | 10% | $0 | center 65.05, market mean 67.51, lead 0d |
| +8¢ | KXHIGHMIA-26NOV20-B84.5 | 84° to 85° | YES | 14¢ | 30% | 22% | $0 | center 83.2, market mean 82.07, lead 0d |
| +8¢ | KXHIGHTOKC-26NOV20-B67.5 | 67° to 68° | YES | 6¢ | 22% | 14% | $0 | center 69.75, market mean 70.21, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV20-T73 | 72° or below | YES | 11¢ | 43% | 19% | $0 | center 73.05, market mean 73.75, lead 0d |
| +8¢ | KXHIGHTHOU-26NOV20-B73.5 | 73° to 74° | YES | 13¢ | 29% | 21% | $0 | center 75.4, market mean 75.57, lead 0d |
| +8¢ | KXHIGHTDC-26NOV20-B66.5 | 66° to 67° | YES | 3¢ | 19% | 11% | $0 | center 69.0, market mean 70.75, lead 0d |
| +7¢ | KXHIGHTHOU-26NOV20-B75.5 | 75° to 76° | NO | 32¢ | 37% | 61% | $0 | center 75.4, market mean 75.57, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV20-B64.5 | 64° to 65° | YES | 5¢ | 37% | 12% | $0 | center 65.05, market mean 67.51, lead 0d |
| +7¢ | KXHIGHTMIN-26NOV20-B68.5 | 68° to 69° | NO | 77¢ | 8% | 16% | $0 | center 64.85, market mean 66.39, lead 0d |
| +7¢ | KXHIGHNY-26NOV20-B68.5 | 68° to 69° | NO | 35¢ | 36% | 58% | $0 | center 67.7, market mean 68.0, lead 0d |
| +7¢ | KXHIGHDEN-26NOV20-B59.5 | 59° to 60° | YES | 3¢ | 18% | 10% | $0 | center 62.1, market mean 63.98, lead 0d |
| +7¢ | KXHIGHCHI-26NOV20-B68.5 | 68° to 69° | NO | 33¢ | 38% | 60% | $0 | center 68.15, market mean 68.77, lead 0d |
| +7¢ | KXHIGHTDC-26NOV20-B70.5 | 70° to 71° | NO | 42¢ | 29% | 51% | $0 | center 69.0, market mean 70.75, lead 0d |
| +7¢ | KXHIGHLAX-26NOV21-B69.5 | 69° to 70° | NO | 54¢ | 15% | 39% | $0 | center 66.25, market mean 68.49, lead 1d |
| +7¢ | KXHIGHTDAL-26NOV20-B74.5 | 74° to 75° | NO | 34¢ | 38% | 59% | $0 | center 74.4, market mean 74.89, lead 0d |
