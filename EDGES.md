# Model vs. market

Scanned 2026-11-19 21:38 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXHIGHMIA-26NOV20-B82.5 | 82° to 83° | NO | 47¢ | 31% | 43% | $100 | center 83.0, market mean 83.25, lead 1d |
| +10¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 8¢ | 72% | 82% | $100 |  |
| +8¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 45¢ | 37% | 47% | $100 |  |
| +8¢ | KXHIGHNY-26NOV20-B68.5 | 68° to 69° | NO | 64¢ | 16% | 28% | $100 | center 65.6, market mean 67.06, lead 1d |
| +7¢ | KXHIGHNY-26NOV20-B66.5 | 66° to 67° | NO | 54¢ | 29% | 39% | $100 | center 65.6, market mean 67.06, lead 1d |
| +7¢ | KXAAAGASW-26NOV23-3.6400 | Above 3.6400 | YES | 5¢ | 21% | 12% | $100 |  |
| +6¢ | KXHIGHCHI-26NOV20-T66 | 65° or below | YES | 8¢ | 26% | 14% | $100 | center 67.1, market mean 68.16, lead 1d |
| +6¢ | KXHIGHNY-26NOV20-B64.5 | 64° to 65° | YES | 14¢ | 28% | 20% | $100 | center 65.6, market mean 67.06, lead 1d |
| +5¢ | KXHIGHTDAL-26NOV20-B76.5 | 76° to 77° | NO | 63¢ | 21% | 32% | $100 | center 74.4, market mean 75.39, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +17¢ | KXHIGHTLV-26NOV19-B57.5 | 57° to 58° | NO | 11¢ | 15% | 72% | $0 | center 61.0, market mean 57.75, lead 0d |
| +16¢ | KXHIGHTOKC-26NOV19-B68.5 | 68° to 69° | NO | 3¢ | 31% | 81% | $0 | center 69.8, market mean 68.53, lead 0d |
| +16¢ | KXHIGHTSATX-26NOV19-B72.5 | 72° to 73° | NO | 2¢ | 33% | 82% | $0 | center 71.75, market mean 72.57, lead 0d |
| +13¢ | KXHIGHDEN-26NOV19-B54.5 | 54° to 55° | NO | 6¢ | 39% | 81% | $0 | center 55.4, market mean 54.58, lead 0d |
| +13¢ | KXHIGHTPHX-26NOV19-B75.5 | 75° to 76° | NO | 4¢ | 42% | 83% | $0 | center 75.3, market mean 75.49, lead 0d |
| +12¢ | KXHIGHTMIN-26NOV19-B55.5 | 55° to 56° | NO | 3¢ | 45% | 85% | $0 | center 55.75, market mean 55.62, lead 0d |
| +12¢ | KXHIGHTOKC-26NOV19-B70.5 | 70° to 71° | YES | 4¢ | 54% | 16% | $0 | center 69.8, market mean 68.53, lead 0d |
| +12¢ | KXHIGHTSEA-26NOV19-B47.5 | 47° to 48° | YES | 3¢ | 27% | 15% | $0 | center 49.35, market mean 49.76, lead 0d |
| +12¢ | KXHIGHTDAL-26NOV19-B72.5 | 72° to 73° | NO | 6¢ | 46% | 82% | $0 | center 73.4, market mean 72.65, lead 0d |
| +11¢ | KXHIGHLAX-26NOV19-B66.5 | 66° to 67° | NO | 4¢ | 48% | 85% | $0 | center 66.05, market mean 66.56, lead 0d |
| +11¢ | KXHIGHTPHX-26NOV19-B73.5 | 73° to 74° | YES | 4¢ | 27% | 15% | $0 | center 75.3, market mean 75.49, lead 0d |
| +11¢ | KXAAAGASD-26NOV20-3.6900 | Above 3.6900 | YES | 37¢ | 88% | 48% | $0 |  |
| +11¢ | KXAAAGASD-26NOV20-3.6950 | Above 3.6950 | YES | 2¢ | 47% | 13% | $0 |  |
| +11¢ | KXHIGHTHOU-26NOV19-B75.5 | 75° to 76° | NO | 3¢ | 50% | 86% | $0 | center 75.2, market mean 75.56, lead 0d |
| +10¢ | KXHIGHLAX-26NOV19-B68.5 | 68° to 69° | YES | 3¢ | 25% | 13% | $0 | center 66.05, market mean 66.56, lead 0d |
| +10¢ | KXHIGHTSEA-26NOV19-B49.5 | 49° to 50° | NO | 16¢ | 42% | 74% | $0 | center 49.35, market mean 49.76, lead 0d |
| +10¢ | KXHIGHTBOS-26NOV20-B66.5 | 66° to 67° | NO | 45¢ | 13% | 45% | $0 | center 63.1, market mean 67.01, lead 1d |
| +10¢ | KXHIGHTPHX-26NOV19-B77.5 | 77° to 78° | YES | 2¢ | 22% | 12% | $0 | center 75.3, market mean 75.49, lead 0d |
| +9¢ | KXHIGHLAX-26NOV20-B66.5 | 66° to 67° | NO | 33¢ | 25% | 58% | $0 | center 64.9, market mean 66.43, lead 1d |
| +9¢ | KXHIGHTDC-26NOV20-B70.5 | 70° to 71° | NO | 38¢ | 25% | 53% | $0 | center 68.85, market mean 70.1, lead 1d |
| +9¢ | KXHIGHTPHX-26NOV20-T70 | 69° or below | YES | 9¢ | 45% | 18% | $0 | center 69.8, market mean 71.51, lead 1d |
| +8¢ | KXHIGHTHOU-26NOV19-B77.5 | 77° to 78° | YES | 3¢ | 21% | 11% | $0 | center 75.2, market mean 75.56, lead 0d |
| +8¢ | KXAAAGASW-26NOV23-3.6200 | Above 3.6200 | NO | 9¢ | 56% | 83% | $0 |  |
| +8¢ | KXHIGHCHI-26NOV20-B68.5 | 68° to 69° | NO | 39¢ | 27% | 53% | $0 | center 67.1, market mean 68.16, lead 1d |
| +8¢ | KXHIGHAUS-26NOV19-B72.5 | 72° to 73° | NO | 19¢ | 44% | 73% | $0 | center 73.45, market mean 72.88, lead 0d |
| +7¢ | KXHIGHTSFO-26NOV19-B56.5 | 56° to 57° | NO | 26¢ | 41% | 67% | $0 | center 56.25, market mean 57.23, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV20-B73.5 | 73° to 74° | NO | 38¢ | 31% | 55% | $0 | center 73.6, market mean 73.77, lead 1d |
| +7¢ | KXHIGHTLV-26NOV19-B61.5 | 61° to 62° | YES | 3¢ | 18% | 10% | $0 | center 61.0, market mean 57.75, lead 0d |
| +7¢ | KXHIGHAUS-26NOV20-B76.5 | 76° to 77° | NO | 39¢ | 30% | 54% | $0 | center 75.85, market mean 76.0, lead 1d |
| +7¢ | KXHIGHTLV-26NOV20-B58.5 | 58° to 59° | NO | 34¢ | 27% | 59% | $0 | center 58.05, market mean 58.44, lead 1d |
| +7¢ | KXHIGHTBOS-26NOV20-B68.5 | 68° to 69° | NO | 64¢ | 3% | 29% | $0 | center 63.1, market mean 67.01, lead 1d |
| +7¢ | KXHIGHTOKC-26NOV20-B69.5 | 69° to 70° | NO | 39¢ | 30% | 54% | $0 | center 69.0, market mean 69.91, lead 1d |
| +7¢ | KXHIGHTSATX-26NOV19-B74.5 | 74° to 75° | YES | 3¢ | 17% | 10% | $0 | center 71.75, market mean 72.57, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV20-B62.5 | 62° to 63° | YES | 2¢ | 30% | 9% | $0 | center 63.1, market mean 67.01, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV19-B74.5 | 74° to 75° | YES | 7¢ | 35% | 14% | $0 | center 73.4, market mean 72.65, lead 0d |
| +6¢ | KXHIGHTPHX-26NOV20-B72.5 | 72° to 73° | NO | 53¢ | 18% | 41% | $0 | center 69.8, market mean 71.51, lead 1d |
| +6¢ | KXHIGHTATL-26NOV20-B69.5 | 69° to 70° | NO | 40¢ | 33% | 54% | $0 | center 69.1, market mean 70.05, lead 1d |
| +6¢ | KXHIGHTMIN-26NOV20-B66.5 | 66° to 67° | NO | 50¢ | 19% | 44% | $0 | center 64.0, market mean 65.64, lead 1d |
| +6¢ | KXHIGHDEN-26NOV19-B56.5 | 56° to 57° | YES | 8¢ | 37% | 14% | $0 | center 55.4, market mean 54.58, lead 0d |
| +6¢ | KXHIGHDEN-26NOV20-B63.5 | 63° to 64° | NO | 52¢ | 22% | 42% | $0 | center 61.25, market mean 63.0, lead 1d |
