# Model vs. market

Scanned 2026-11-20 21:38 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXHIGHDEN-26NOV21-B46.5 | 46° to 47° | NO | 56¢ | 23% | 35% | $100 | center 45.0, market mean 46.18, lead 1d |
| +8¢ | KXHIGHCHI-26NOV21-B70.5 | 70° to 71° | NO | 63¢ | 17% | 29% | $100 | center 67.7, market mean 69.27, lead 1d |
| +8¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 51¢ | 33% | 41% | $100 |  |
| +8¢ | KXHIGHTPHX-26NOV21-B69.5 | 69° to 70° | NO | 58¢ | 24% | 35% | $100 | center 67.6, market mean 68.5, lead 1d |
| +6¢ | KXHIGHNY-26NOV21-B62.5 | 62° to 63° | NO | 55¢ | 30% | 39% | $100 | center 63.3, market mean 62.97, lead 1d |
| +6¢ | KXHIGHCHI-26NOV21-B68.5 | 68° to 69° | NO | 53¢ | 30% | 41% | $100 | center 67.7, market mean 69.27, lead 1d |
| +6¢ | KXHIGHCHI-26NOV21-B66.5 | 66° to 67° | YES | 11¢ | 28% | 17% | $100 | center 67.7, market mean 69.27, lead 1d |
| +6¢ | KXHIGHMIA-26NOV21-B82.5 | 82° to 83° | NO | 61¢ | 25% | 33% | $100 | center 83.15, market mean 83.4, lead 1d |
| +6¢ | KXHIGHTLV-26NOV21-B56.5 | 56° to 57° | NO | 54¢ | 30% | 40% | $100 | center 57.1, market mean 57.52, lead 1d |
| +6¢ | KXHIGHMIA-26NOV21-B84.5 | 84° to 85° | NO | 63¢ | 23% | 31% | $100 | center 83.15, market mean 83.4, lead 1d |
| +5¢ | KXHIGHTOKC-26NOV21-T68 | 67° or below | NO | 70¢ | 13% | 25% | $100 | center 70.25, market mean 68.44, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +18¢ | KXAAAGASW-26NOV23-3.6250 | Above 3.6250 | NO | 6¢ | 19% | 76% | $0 |  |
| +14¢ | KXAAAGASD-26NOV21-3.6600 | Above 3.6600 | YES | 14¢ | 74% | 28% | $0 |  |
| +14¢ | KXHIGHTHOU-26NOV20-B75.5 | 75° to 76° | NO | 2¢ | 41% | 84% | $0 | center 75.45, market mean 75.52, lead 0d |
| +12¢ | KXHIGHTNOLA-26NOV21-B73.5 | 73° to 74° | NO | 32¢ | 17% | 56% | $0 | center 73.65, market mean 73.93, lead 1d |
| +11¢ | KXHIGHTSATX-26NOV20-B75.5 | 75° to 76° | YES | 3¢ | 27% | 14% | $0 | center 73.9, market mean 73.62, lead 0d |
| +11¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 43¢ | 11% | 46% | $0 |  |
| +10¢ | KXHIGHTHOU-26NOV20-B77.5 | 77° to 78° | YES | 2¢ | 23% | 12% | $0 | center 75.45, market mean 75.52, lead 0d |
| +9¢ | KXHIGHTSEA-26NOV20-T46 | 45° or below | NO | 6¢ | 56% | 85% | $0 | center 45.2, market mean 44.79, lead 0d |
| +9¢ | KXHIGHTMIN-26NOV20-B64.5 | 64° to 65° | NO | 4¢ | 57% | 87% | $0 | center 65.0, market mean 64.6, lead 0d |
| +9¢ | KXHIGHAUS-26NOV20-B76.5 | 76° to 77° | NO | 19¢ | 39% | 72% | $0 | center 75.45, market mean 76.32, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV20-B74.5 | 74° to 75° | NO | 28¢ | 54% | 64% | $0 | center 75.2, market mean 74.99, lead 0d |
| +8¢ | KXHIGHTHOU-26NOV21-B77.5 | 77° to 78° | NO | 37¢ | 30% | 55% | $0 | center 77.0, market mean 77.85, lead 1d |
| +8¢ | KXHIGHTMIN-26NOV20-B66.5 | 66° to 67° | YES | 5¢ | 39% | 13% | $0 | center 65.0, market mean 64.6, lead 0d |
| +8¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 5¢ | 63% | 87% | $0 |  |
| +7¢ | KXHIGHLAX-26NOV20-B64.5 | 64° to 65° | NO | 25¢ | 37% | 68% | $0 | center 65.0, market mean 64.94, lead 0d |
| +7¢ | KXHIGHLAX-26NOV21-B69.5 | 69° to 70° | NO | 48¢ | 22% | 45% | $0 | center 67.6, market mean 68.62, lead 1d |
| +7¢ | KXHIGHTSFO-26NOV20-B57.5 | 57° to 58° | NO | 27¢ | 41% | 66% | $0 | center 57.95, market mean 58.04, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV20-B69.5 | 69° to 70° | NO | 6¢ | 61% | 87% | $0 | center 70.0, market mean 69.61, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV21-T67 | 66° or below | YES | 4¢ | 33% | 11% | $0 | center 67.6, market mean 68.5, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV20-B71.5 | 71° to 72° | YES | 6¢ | 35% | 12% | $0 | center 70.0, market mean 69.61, lead 0d |
| +6¢ | KXHIGHAUS-26NOV20-B74.5 | 74° to 75° | YES | 17¢ | 49% | 23% | $0 | center 75.45, market mean 76.32, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV21-B67.5 | 67° to 68° | NO | 48¢ | 26% | 46% | $0 | center 65.85, market mean 66.66, lead 1d |
| +6¢ | KXHIGHTPHX-26NOV20-B72.5 | 72° to 73° | NO | 13¢ | 53% | 81% | $0 | center 71.6, market mean 72.48, lead 0d |
| +6¢ | KXHIGHLAX-26NOV20-B68.5 | 68° to 69° | YES | 2¢ | 14% | 8% | $0 | center 65.0, market mean 64.94, lead 0d |
| +6¢ | KXHIGHTLV-26NOV20-B60.5 | 60° to 61° | NO | 54¢ | 30% | 40% | $0 | center 58.55, market mean 59.49, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV21-B62.5 | 62° to 63° | NO | 50¢ | 21% | 45% | $0 | center 61.7, market mean 62.63, lead 1d |
| +5¢ | KXHIGHTSEA-26NOV20-B46.5 | 46° to 47° | YES | 7¢ | 32% | 12% | $0 | center 45.2, market mean 44.79, lead 0d |
| +5¢ | KXHIGHDEN-26NOV20-B63.5 | 63° to 64° | YES | 21¢ | 48% | 26% | $0 | center 64.4, market mean 64.97, lead 0d |
| +5¢ | KXHIGHDEN-26NOV20-T64 | 65° or above | NO | 24¢ | 52% | 71% | $0 | center 64.4, market mean 64.97, lead 0d |
| +5¢ | KXHIGHTPHX-26NOV20-B74.5 | 74° to 75° | YES | 4¢ | 15% | 9% | $0 | center 71.6, market mean 72.48, lead 0d |
| +4¢ | KXHIGHTPHX-26NOV21-B67.5 | 67° to 68° | NO | 56¢ | 31% | 40% | $100 | center 67.6, market mean 68.5, lead 1d |
| +4¢ | KXHIGHTNOLA-26NOV21-B71.5 | 71° to 72° | YES | 16¢ | 31% | 20% | $100 | center 73.65, market mean 73.93, lead 1d |
| +4¢ | KXHIGHTSFO-26NOV21-B57.5 | 57° to 58° | NO | 55¢ | 31% | 41% | $100 | center 57.8, market mean 58.07, lead 1d |
| +4¢ | KXHIGHTSEA-26NOV21-B48.5 | 48° to 49° | NO | 63¢ | 26% | 33% | $100 | center 49.85, market mean 48.79, lead 1d |
| +3¢ | KXHIGHLAX-26NOV21-B65.5 | 65° to 66° | YES | 10¢ | 21% | 13% | $100 | center 67.6, market mean 68.62, lead 1d |
| +3¢ | KXHIGHTNOLA-26NOV21-B75.5 | 75° to 76° | NO | 80¢ | 9% | 17% | $100 | center 73.65, market mean 73.93, lead 1d |
| +3¢ | KXHIGHTBOS-26NOV21-B60.5 | 60° to 61° | NO | 61¢ | 28% | 36% | $100 | center 59.15, market mean 59.69, lead 1d |
| +2¢ | KXHIGHCHI-26NOV21-T66 | 65° or below | YES | 8¢ | 19% | 10% | $100 | center 67.7, market mean 69.27, lead 1d |
| +2¢ | KXHIGHNY-26NOV21-T65 | 66° or above | YES | 9¢ | 19% | 11% | $100 | center 63.3, market mean 62.97, lead 1d |
| +1¢ | KXHIGHTHOU-26NOV21-B75.5 | 75° to 76° | YES | 17¢ | 27% | 18% | $100 | center 77.0, market mean 77.85, lead 1d |
