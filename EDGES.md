# Model vs. market

Scanned 2026-11-19 20:29 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXHIGHNY-26NOV20-B66.5 | 66° to 67° | NO | 52¢ | 29% | 39% | $100 | center 65.45, market mean 67.18, lead 1d |
| +9¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 9¢ | 72% | 82% | $100 |  |
| +8¢ | KXHIGHPHIL-26NOV20-B68.5 | 68° to 69° | NO | 52¢ | 28% | 40% | $100 | center 67.6, market mean 68.99, lead 1d |
| +7¢ | KXAAAGASW-26NOV23-3.6400 | Above 3.6400 | YES | 6¢ | 21% | 13% | $100 |  |
| +6¢ | KXHIGHTSEA-26NOV20-B48.5 | 48° to 49° | NO | 57¢ | 27% | 37% | $100 | center 47.1, market mean 47.91, lead 1d |
| +6¢ | KXHIGHNY-26NOV20-B64.5 | 64° to 65° | YES | 12¢ | 29% | 18% | $100 | center 65.45, market mean 67.18, lead 1d |
| +6¢ | KXHIGHCHI-26NOV20-T66 | 65° or below | YES | 9¢ | 27% | 15% | $100 | center 67.0, market mean 68.17, lead 1d |
| +5¢ | KXHIGHTSFO-26NOV20-B59.5 | 59° to 60° | NO | 63¢ | 20% | 32% | $100 | center 57.0, market mean 58.49, lead 1d |
| +5¢ | KXHIGHTDAL-26NOV20-B76.5 | 76° to 77° | NO | 64¢ | 21% | 31% | $100 | center 74.4, market mean 75.38, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +17¢ | KXAAAGASD-26NOV20-3.6900 | Above 3.6900 | YES | 20¢ | 88% | 37% | $0 |  |
| +13¢ | KXHIGHTSATX-26NOV19-B70.5 | 70° to 71° | NO | 12¢ | 35% | 75% | $0 | center 71.65, market mean 70.81, lead 0d |
| +13¢ | KXHIGHTNOLA-26NOV19-B70.5 | 70° to 71° | NO | 17¢ | 23% | 70% | $0 | center 71.6, market mean 70.68, lead 0d |
| +13¢ | KXHIGHTMIN-26NOV19-B55.5 | 55° to 56° | NO | 3¢ | 45% | 84% | $0 | center 55.9, market mean 55.61, lead 0d |
| +11¢ | KXHIGHTPHX-26NOV19-B75.5 | 75° to 76° | NO | 16¢ | 38% | 73% | $0 | center 75.25, market mean 75.57, lead 0d |
| +11¢ | KXHIGHCHI-26NOV19-B66.5 | 66° to 67° | NO | 5¢ | 47% | 84% | $0 | center 66.2, market mean 66.54, lead 0d |
| +11¢ | KXHIGHTDC-26NOV19-B66.5 | 66° to 67° | NO | 10¢ | 44% | 79% | $0 | center 67.0, market mean 66.75, lead 0d |
| +11¢ | KXHIGHNY-26NOV19-B63.5 | 63° to 64° | NO | 9¢ | 45% | 80% | $0 | center 63.0, market mean 63.65, lead 0d |
| +11¢ | KXHIGHTBOS-26NOV19-B63.5 | 63° to 64° | NO | 2¢ | 54% | 87% | $0 | center 62.6, market mean 63.61, lead 0d |
| +11¢ | KXHIGHTBOS-26NOV20-B66.5 | 66° to 67° | NO | 43¢ | 13% | 46% | $0 | center 63.1, market mean 66.91, lead 1d |
| +10¢ | KXHIGHPHIL-26NOV19-B67.5 | 67° to 68° | NO | 10¢ | 43% | 80% | $0 | center 68.0, market mean 67.65, lead 0d |
| +10¢ | KXHIGHTPHX-26NOV19-B73.5 | 73° to 74° | YES | 6¢ | 27% | 16% | $0 | center 75.25, market mean 75.57, lead 0d |
| +10¢ | KXHIGHTHOU-26NOV19-B75.5 | 75° to 76° | NO | 5¢ | 50% | 85% | $0 | center 75.2, market mean 75.58, lead 0d |
| +10¢ | KXHIGHTLV-26NOV20-B58.5 | 58° to 59° | NO | 31¢ | 27% | 59% | $0 | center 58.05, market mean 58.52, lead 1d |
| +10¢ | KXHIGHLAX-26NOV20-B66.5 | 66° to 67° | NO | 34¢ | 25% | 56% | $0 | center 64.9, market mean 66.26, lead 1d |
| +10¢ | KXHIGHTSATX-26NOV19-B72.5 | 72° to 73° | YES | 11¢ | 32% | 21% | $0 | center 71.65, market mean 70.81, lead 0d |
| +10¢ | KXHIGHCHI-26NOV19-B68.5 | 68° to 69° | YES | 5¢ | 26% | 15% | $0 | center 66.2, market mean 66.54, lead 0d |
| +9¢ | KXHIGHTLV-26NOV19-B57.5 | 57° to 58° | NO | 31¢ | 18% | 60% | $0 | center 60.05, market mean 58.02, lead 0d |
| +9¢ | KXHIGHAUS-26NOV19-B74.5 | 74° to 75° | YES | 16¢ | 34% | 25% | $0 | center 73.5, market mean 72.75, lead 0d |
| +9¢ | KXHIGHTPHX-26NOV20-T70 | 69° or below | YES | 9¢ | 45% | 18% | $0 | center 69.8, market mean 71.49, lead 1d |
| +8¢ | KXHIGHLAX-26NOV19-B66.5 | 66° to 67° | NO | 19¢ | 42% | 73% | $0 | center 66.0, market mean 66.87, lead 0d |
| +8¢ | KXHIGHCHI-26NOV20-B68.5 | 68° to 69° | NO | 39¢ | 26% | 53% | $0 | center 67.0, market mean 68.17, lead 1d |
| +8¢ | KXHIGHTHOU-26NOV19-B77.5 | 77° to 78° | YES | 4¢ | 21% | 12% | $0 | center 75.2, market mean 75.58, lead 0d |
| +8¢ | KXHIGHTDC-26NOV20-B70.5 | 70° to 71° | NO | 39¢ | 25% | 53% | $0 | center 68.85, market mean 70.08, lead 1d |
| +7¢ | KXHIGHTSATX-26NOV20-B73.5 | 73° to 74° | NO | 38¢ | 31% | 55% | $0 | center 73.4, market mean 73.86, lead 1d |
| +7¢ | KXHIGHTSATX-26NOV19-B74.5 | 74° to 75° | YES | 2¢ | 17% | 9% | $0 | center 71.65, market mean 70.81, lead 0d |
| +7¢ | KXHIGHTMIN-26NOV19-B57.5 | 57° to 58° | YES | 2¢ | 32% | 9% | $0 | center 55.9, market mean 55.61, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV20-B68.5 | 68° to 69° | NO | 67¢ | 3% | 26% | $0 | center 63.1, market mean 66.91, lead 1d |
| +7¢ | KXHIGHAUS-26NOV20-B76.5 | 76° to 77° | NO | 40¢ | 30% | 53% | $0 | center 75.85, market mean 75.98, lead 1d |
| +7¢ | KXHIGHDEN-26NOV19-B54.5 | 54° to 55° | YES | 34¢ | 52% | 41% | $0 | center 54.6, market mean 55.87, lead 0d |
| +7¢ | KXHIGHTATL-26NOV20-B69.5 | 69° to 70° | NO | 38¢ | 33% | 55% | $0 | center 69.1, market mean 69.97, lead 1d |
| +7¢ | KXHIGHTSEA-26NOV19-B49.5 | 49° to 50° | NO | 30¢ | 38% | 63% | $0 | center 49.25, market mean 49.52, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV20-B72.5 | 72° to 73° | NO | 53¢ | 18% | 40% | $0 | center 69.8, market mean 71.49, lead 1d |
| +7¢ | KXHIGHTBOS-26NOV20-B62.5 | 62° to 63° | YES | 2¢ | 30% | 9% | $0 | center 63.1, market mean 66.91, lead 1d |
| +7¢ | KXHIGHNY-26NOV19-B65.5 | 65° to 66° | YES | 11¢ | 25% | 18% | $0 | center 63.0, market mean 63.65, lead 0d |
| +7¢ | KXHIGHTNOLA-26NOV19-B72.5 | 72° to 73° | YES | 9¢ | 40% | 16% | $0 | center 71.6, market mean 70.68, lead 0d |
| +6¢ | KXHIGHDEN-26NOV20-B63.5 | 63° to 64° | NO | 51¢ | 22% | 43% | $0 | center 61.25, market mean 62.97, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV19-B72.5 | 72° to 73° | NO | 38¢ | 46% | 56% | $0 | center 73.4, market mean 73.15, lead 0d |
| +6¢ | KXHIGHAUS-26NOV19-B72.5 | 72° to 73° | NO | 22¢ | 42% | 72% | $0 | center 73.5, market mean 72.75, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV20-B69.5 | 69° to 70° | NO | 38¢ | 30% | 56% | $0 | center 69.0, market mean 69.79, lead 1d |
