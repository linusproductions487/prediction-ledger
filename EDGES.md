# Model vs. market

Scanned 2026-11-20 07:06 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 5¢ | 72% | 84% | $100 |  |
| +9¢ | KXHIGHTSFO-26NOV20-B57.5 | 57° to 58° | NO | 51¢ | 31% | 40% | $100 | center 57.55, market mean 58.36, lead 1d |
| +6¢ | KXHIGHLAX-26NOV20-B62.5 | 62° to 63° | YES | 4¢ | 19% | 10% | $100 | center 65.0, market mean 66.41, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +12¢ | KXHIGHCHI-26NOV20-B68.5 | 68° to 69° | NO | 38¢ | 38% | 50% | $0 | center 68.45, market mean 68.78, lead 0d |
| +11¢ | KXHIGHTPHX-26NOV20-T70 | 69° or below | YES | 3¢ | 26% | 14% | $0 | center 70.75, market mean 71.47, lead 0d |
| +11¢ | KXHIGHTOKC-26NOV20-B69.5 | 69° to 70° | NO | 40¢ | 38% | 49% | $0 | center 69.7, market mean 70.08, lead 0d |
| +10¢ | KXHIGHTHOU-26NOV20-B75.5 | 75° to 76° | NO | 40¢ | 39% | 50% | $0 | center 75.8, market mean 75.94, lead 0d |
| +10¢ | KXHIGHTLV-26NOV20-B58.5 | 58° to 59° | NO | 28¢ | 29% | 62% | $0 | center 58.05, market mean 58.69, lead 1d |
| +10¢ | KXHIGHNY-26NOV20-B64.5 | 64° to 65° | YES | 7¢ | 28% | 17% | $0 | center 66.15, market mean 67.36, lead 0d |
| +10¢ | KXAAAGASW-26NOV23-3.6200 | Above 3.6200 | NO | 2¢ | 56% | 88% | $0 |  |
| +10¢ | KXHIGHDEN-26NOV20-B63.5 | 63° to 64° | NO | 53¢ | 26% | 37% | $0 | center 61.65, market mean 63.44, lead 0d |
| +10¢ | KXHIGHTDC-26NOV20-B70.5 | 70° to 71° | NO | 52¢ | 28% | 38% | $0 | center 68.85, market mean 70.32, lead 0d |
| +9¢ | KXHIGHDEN-26NOV20-B59.5 | 59° to 60° | YES | 3¢ | 22% | 12% | $0 | center 61.65, market mean 63.44, lead 0d |
| +9¢ | KXHIGHPHIL-26NOV20-B70.5 | 70° to 71° | NO | 39¢ | 17% | 52% | $0 | center 67.8, market mean 69.75, lead 0d |
| +9¢ | KXHIGHDEN-26NOV20-T64 | 65° or above | NO | 72¢ | 8% | 19% | $0 | center 61.65, market mean 63.44, lead 0d |
| +9¢ | KXHIGHLAX-26NOV20-B66.5 | 66° to 67° | NO | 36¢ | 26% | 55% | $0 | center 65.0, market mean 66.41, lead 1d |
| +9¢ | KXHIGHTPHX-26NOV20-B72.5 | 72° to 73° | NO | 53¢ | 28% | 38% | $0 | center 70.75, market mean 71.47, lead 0d |
| +9¢ | KXHIGHTBOS-26NOV20-B68.5 | 68° to 69° | NO | 59¢ | 2% | 32% | $0 | center 63.55, market mean 67.2, lead 0d |
| +9¢ | KXHIGHTMIN-26NOV20-B62.5 | 62° to 63° | YES | 4¢ | 22% | 13% | $0 | center 64.65, market mean 66.07, lead 0d |
| +9¢ | KXHIGHTDAL-26NOV20-B72.5 | 72° to 73° | YES | 6¢ | 24% | 15% | $0 | center 74.6, market mean 74.95, lead 0d |
| +8¢ | KXHIGHTDC-26NOV20-B66.5 | 66° to 67° | YES | 3¢ | 20% | 11% | $0 | center 68.85, market mean 70.32, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV20-B66.5 | 66° to 67° | NO | 37¢ | 26% | 55% | $0 | center 64.65, market mean 66.07, lead 0d |
| +8¢ | KXHIGHTATL-26NOV20-B69.5 | 69° to 70° | NO | 47¢ | 36% | 45% | $0 | center 70.0, market mean 70.27, lead 0d |
| +8¢ | KXHIGHTOKC-26NOV20-B67.5 | 67° to 68° | YES | 6¢ | 22% | 14% | $0 | center 69.7, market mean 70.08, lead 0d |
| +8¢ | KXHIGHDEN-26NOV20-B61.5 | 61° to 62° | YES | 22¢ | 38% | 30% | $0 | center 61.65, market mean 63.44, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV20-B62.5 | 62° to 63° | YES | 2¢ | 34% | 10% | $0 | center 63.55, market mean 67.2, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV20-B64.5 | 64° to 65° | YES | 22¢ | 38% | 30% | $0 | center 64.65, market mean 66.07, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV20-B70.5 | 70° to 71° | NO | 47¢ | 38% | 46% | $0 | center 70.75, market mean 71.47, lead 0d |
| +7¢ | KXHIGHTDAL-26NOV20-B74.5 | 74° to 75° | NO | 31¢ | 38% | 62% | $0 | center 74.6, market mean 74.95, lead 0d |
| +7¢ | KXHIGHTNOLA-26NOV20-B72.5 | 72° to 73° | NO | 41¢ | 30% | 52% | $0 | center 71.7, market mean 72.25, lead 0d |
| +7¢ | KXHIGHTDC-26NOV20-B68.5 | 68° to 69° | YES | 23¢ | 37% | 30% | $0 | center 68.85, market mean 70.32, lead 0d |
| +7¢ | KXHIGHMIA-26NOV20-B86.5 | 86° to 87° | YES | 3¢ | 17% | 10% | $0 | center 83.65, market mean 82.74, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV20-B64.5 | 64° to 65° | YES | 6¢ | 34% | 13% | $0 | center 63.55, market mean 67.2, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV20-B66.5 | 66° to 67° | NO | 53¢ | 14% | 40% | $0 | center 63.55, market mean 67.2, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV20-B73.5 | 73° to 74° | NO | 32¢ | 39% | 62% | $0 | center 73.6, market mean 73.47, lead 0d |
| +6¢ | KXHIGHNY-26NOV20-B68.5 | 68° to 69° | NO | 54¢ | 20% | 40% | $0 | center 66.15, market mean 67.36, lead 0d |
| +6¢ | KXHIGHCHI-26NOV20-B66.5 | 66° to 67° | YES | 11¢ | 25% | 17% | $0 | center 68.45, market mean 68.78, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV20-B66.5 | 66° to 67° | YES | 4¢ | 30% | 10% | $0 | center 67.8, market mean 69.75, lead 0d |
| +6¢ | KXHIGHTSEA-26NOV20-B46.5 | 46° to 47° | NO | 44¢ | 31% | 50% | $0 | center 46.75, market mean 46.9, lead 1d |
| +6¢ | KXHIGHAUS-26NOV20-B76.5 | 76° to 77° | NO | 41¢ | 32% | 53% | $0 | center 75.65, market mean 75.95, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV20-B68.5 | 68° to 69° | YES | 3¢ | 14% | 8% | $0 | center 71.7, market mean 72.25, lead 0d |
| +6¢ | KXHIGHTDC-26NOV20-B72.5 | 72° to 73° | NO | 80¢ | 8% | 14% | $0 | center 68.85, market mean 70.32, lead 0d |
| +5¢ | KXHIGHTATL-26NOV20-B67.5 | 67° to 68° | YES | 6¢ | 17% | 11% | $0 | center 70.0, market mean 70.27, lead 0d |
