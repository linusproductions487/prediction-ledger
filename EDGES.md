# Model vs. market

Scanned 2026-11-20 20:07 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXHIGHDEN-26NOV21-B46.5 | 46° to 47° | NO | 55¢ | 24% | 36% | $100 | center 45.0, market mean 46.17, lead 1d |
| +8¢ | KXHIGHCHI-26NOV21-B68.5 | 68° to 69° | NO | 52¢ | 30% | 40% | $100 | center 67.7, market mean 69.15, lead 1d |
| +8¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 51¢ | 33% | 41% | $100 |  |
| +7¢ | KXHIGHMIA-26NOV21-B82.5 | 82° to 83° | NO | 61¢ | 23% | 32% | $100 | center 83.15, market mean 83.4, lead 1d |
| +6¢ | KXHIGHCHI-26NOV21-B70.5 | 70° to 71° | NO | 66¢ | 17% | 28% | $100 | center 67.7, market mean 69.15, lead 1d |
| +6¢ | KXHIGHTPHX-26NOV21-B69.5 | 69° to 70° | NO | 58¢ | 24% | 36% | $100 | center 67.6, market mean 68.56, lead 1d |
| +5¢ | KXHIGHMIA-26NOV21-B84.5 | 84° to 85° | NO | 64¢ | 22% | 31% | $100 | center 83.15, market mean 83.4, lead 1d |
| +5¢ | KXHIGHNY-26NOV21-B62.5 | 62° to 63° | NO | 54¢ | 30% | 41% | $100 | center 63.3, market mean 62.91, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +17¢ | KXAAAGASW-26NOV23-3.6200 | Above 3.6200 | NO | 2¢ | 29% | 81% | $0 |  |
| +16¢ | KXAAAGASW-26NOV23-3.6250 | Above 3.6250 | NO | 13¢ | 19% | 71% | $0 |  |
| +15¢ | KXHIGHMIA-26NOV20-B82.5 | 82° to 83° | NO | 3¢ | 35% | 82% | $0 | center 83.35, market mean 82.57, lead 0d |
| +13¢ | KXHIGHNY-26NOV20-B68.5 | 68° to 69° | NO | 2¢ | 44% | 85% | $0 | center 67.5, market mean 68.43, lead 0d |
| +13¢ | KXHIGHTNOLA-26NOV20-B72.5 | 72° to 73° | NO | 8¢ | 37% | 79% | $0 | center 72.2, market mean 72.63, lead 0d |
| +13¢ | KXHIGHPHIL-26NOV20-B70.5 | 70° to 71° | NO | 4¢ | 42% | 83% | $0 | center 70.0, market mean 70.45, lead 0d |
| +13¢ | KXHIGHTPHX-26NOV20-B72.5 | 72° to 73° | NO | 13¢ | 32% | 74% | $0 | center 70.9, market mean 72.43, lead 0d |
| +13¢ | KXHIGHTSATX-26NOV20-B73.5 | 73° to 74° | NO | 6¢ | 42% | 81% | $0 | center 73.5, market mean 73.58, lead 0d |
| +13¢ | KXHIGHTDC-26NOV20-B70.5 | 70° to 71° | NO | 3¢ | 45% | 84% | $0 | center 69.8, market mean 70.52, lead 0d |
| +13¢ | KXHIGHTHOU-26NOV20-B75.5 | 75° to 76° | NO | 7¢ | 41% | 80% | $0 | center 75.45, market mean 75.52, lead 0d |
| +12¢ | KXHIGHDEN-26NOV20-T64 | 65° or above | NO | 9¢ | 40% | 79% | $0 | center 63.15, market mean 65.22, lead 0d |
| +12¢ | KXHIGHTNOLA-26NOV21-B73.5 | 73° to 74° | NO | 37¢ | 14% | 52% | $0 | center 73.45, market mean 73.91, lead 1d |
| +11¢ | KXHIGHDEN-26NOV20-B63.5 | 63° to 64° | YES | 10¢ | 60% | 21% | $0 | center 63.15, market mean 65.22, lead 0d |
| +10¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 46¢ | 11% | 44% | $0 |  |
| +10¢ | KXHIGHTDC-26NOV20-B72.5 | 72° to 73° | YES | 4¢ | 25% | 14% | $0 | center 69.8, market mean 70.52, lead 0d |
| +10¢ | KXHIGHTATL-26NOV20-B69.5 | 69° to 70° | NO | 4¢ | 55% | 86% | $0 | center 70.0, market mean 69.56, lead 0d |
| +10¢ | KXHIGHTHOU-26NOV20-B77.5 | 77° to 78° | YES | 3¢ | 23% | 13% | $0 | center 75.45, market mean 75.52, lead 0d |
| +9¢ | KXHIGHTSFO-26NOV20-B57.5 | 57° to 58° | NO | 41¢ | 38% | 50% | $0 | center 57.5, market mean 58.19, lead 0d |
| +9¢ | KXAAAGASD-26NOV21-3.6600 | Above 3.6600 | YES | 33¢ | 74% | 42% | $0 |  |
| +9¢ | KXHIGHTATL-26NOV20-B71.5 | 71° to 72° | YES | 3¢ | 41% | 12% | $0 | center 70.0, market mean 69.56, lead 0d |
| +9¢ | KXHIGHTSEA-26NOV20-T46 | 45° or below | NO | 8¢ | 56% | 83% | $0 | center 45.2, market mean 44.79, lead 0d |
| +8¢ | KXHIGHCHI-26NOV20-B68.5 | 68° to 69° | NO | 4¢ | 59% | 87% | $0 | center 68.0, market mean 68.59, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV20-B75.5 | 75° to 76° | YES | 4¢ | 21% | 12% | $0 | center 73.5, market mean 73.58, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV20-B55.5 | 55° to 56° | YES | 6¢ | 25% | 14% | $0 | center 57.5, market mean 58.19, lead 0d |
| +8¢ | KXHIGHTHOU-26NOV21-B77.5 | 77° to 78° | NO | 38¢ | 30% | 54% | $0 | center 77.0, market mean 77.81, lead 1d |
| +7¢ | KXHIGHLAX-26NOV21-B69.5 | 69° to 70° | NO | 48¢ | 22% | 45% | $0 | center 67.6, market mean 68.6, lead 1d |
| +7¢ | KXHIGHPHIL-26NOV20-T71 | 72° or above | YES | 4¢ | 37% | 11% | $0 | center 70.0, market mean 70.45, lead 0d |
| +7¢ | KXHIGHLAX-26NOV20-B64.5 | 64° to 65° | NO | 45¢ | 39% | 48% | $0 | center 65.0, market mean 65.45, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV20-B70.5 | 70° to 71° | YES | 10¢ | 43% | 17% | $0 | center 70.9, market mean 72.43, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV21-T67 | 66° or below | YES | 4¢ | 33% | 11% | $0 | center 67.6, market mean 68.56, lead 1d |
| +7¢ | KXHIGHTOKC-26NOV20-B69.5 | 69° to 70° | YES | 30¢ | 63% | 37% | $0 | center 69.85, market mean 70.91, lead 0d |
| +7¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 9¢ | 63% | 84% | $0 |  |
| +7¢ | KXHIGHTDAL-26NOV20-B76.5 | 76° to 77° | NO | 45¢ | 38% | 48% | $0 | center 75.2, market mean 75.67, lead 0d |
| +6¢ | KXHIGHMIA-26NOV20-B84.5 | 84° to 85° | YES | 4¢ | 34% | 10% | $0 | center 83.35, market mean 82.57, lead 0d |
| +6¢ | KXHIGHTLV-26NOV20-B60.5 | 60° to 61° | NO | 50¢ | 24% | 44% | $0 | center 58.2, market mean 59.51, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV21-B67.5 | 67° to 68° | NO | 48¢ | 27% | 46% | $0 | center 65.9, market mean 66.65, lead 1d |
| +6¢ | KXHIGHTMIN-26NOV21-T60 | 59° or below | YES | 6¢ | 31% | 12% | $0 | center 61.2, market mean 62.71, lead 1d |
| +6¢ | KXHIGHTMIN-26NOV21-B62.5 | 62° to 63° | NO | 53¢ | 21% | 41% | $0 | center 61.2, market mean 62.71, lead 1d |
| +5¢ | KXHIGHTNOLA-26NOV20-B74.5 | 74° to 75° | YES | 10¢ | 22% | 15% | $0 | center 72.2, market mean 72.63, lead 0d |
| +5¢ | KXHIGHTSATX-26NOV20-T73 | 72° or below | YES | 5¢ | 29% | 10% | $0 | center 73.5, market mean 73.58, lead 0d |
