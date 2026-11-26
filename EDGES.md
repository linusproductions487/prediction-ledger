# Model vs. market

Scanned 2026-11-26 21:37 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +6¢ | KXHIGHTATL-26NOV27-B51.5 | 51° to 52° | NO | 64¢ | 19% | 30% | $100 | center 50.14, market mean 50.87, lead 1d |
| +6¢ | KXHIGHCHI-26NOV27-B47.5 | 47° to 48° | NO | 51¢ | 31% | 43% | $100 | center 46.14, market mean 47.31, lead 1d |
| +5¢ | KXHIGHNY-26NOV27-T57 | 56° or below | NO | 33¢ | 50% | 62% | $100 | center 57.19, market mean 56.25, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +24¢ | KXAAAGASD-26NOV27-3.5400 | Above 3.5400 | NO | 3¢ | 0% | 73% | $0 |  |
| +20¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 2¢ | 15% | 78% | $0 |  |
| +18¢ | KXHIGHTPHX-26NOV26-B78.5 | 78° to 79° | NO | 5¢ | 22% | 77% | $0 | center 78.99, market mean 78.62, lead 0d |
| +15¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 35¢ | 2% | 50% | $0 |  |
| +15¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 37¢ | 2% | 48% | $0 |  |
| +14¢ | KXHIGHAUS-26NOV26-B60.5 | 60° to 61° | NO | 2¢ | 38% | 83% | $0 | center 59.0, market mean 60.49, lead 0d |
| +14¢ | KXAAAGASD-26NOV27-3.5450 | Above 3.5450 | NO | 43¢ | 0% | 44% | $0 |  |
| +13¢ | KXHIGHTNOLA-26NOV26-B57.5 | 57° to 58° | NO | 3¢ | 42% | 84% | $0 | center 57.2, market mean 57.5, lead 0d |
| +12¢ | KXHIGHDEN-26NOV26-B58.5 | 58° to 59° | NO | 5¢ | 45% | 83% | $0 | center 58.64, market mean 58.53, lead 0d |
| +11¢ | KXHIGHTPHX-26NOV26-B80.5 | 80° to 81° | YES | 6¢ | 30% | 17% | $0 | center 78.99, market mean 78.62, lead 0d |
| +11¢ | KXHIGHTSATX-26NOV26-B63.5 | 63° to 64° | NO | 2¢ | 52% | 87% | $0 | center 62.6, market mean 63.37, lead 0d |
| +10¢ | KXHIGHCHI-26NOV26-B44.5 | 44° to 45° | NO | 6¢ | 47% | 84% | $0 | center 45.54, market mean 44.61, lead 0d |
| +9¢ | KXHIGHTBOS-26NOV26-B51.5 | 51° to 52° | YES | 4¢ | 24% | 13% | $0 | center 50.14, market mean 48.37, lead 0d |
| +9¢ | KXHIGHTSFO-26NOV26-B65.5 | 65° to 66° | YES | 7¢ | 26% | 16% | $0 | center 64.14, market mean 63.24, lead 0d |
| +9¢ | KXHIGHTSEA-26NOV27-B50.5 | 50° to 51° | NO | 33¢ | 29% | 58% | $0 | center 49.19, market mean 50.76, lead 1d |
| +9¢ | KXHIGHCHI-26NOV26-B46.5 | 46° to 47° | YES | 6¢ | 46% | 15% | $0 | center 45.54, market mean 44.61, lead 0d |
| +9¢ | KXHIGHTSATX-26NOV27-B67.5 | 67° to 68° | NO | 39¢ | 25% | 52% | $0 | center 65.79, market mean 66.66, lead 1d |
| +8¢ | KXHIGHTPHX-26NOV27-B77.5 | 77° to 78° | NO | 41¢ | 26% | 51% | $0 | center 76.89, market mean 78.29, lead 1d |
| +8¢ | KXHIGHTOKC-26NOV27-B62.5 | 62° to 63° | NO | 49¢ | 16% | 43% | $0 | center 59.89, market mean 62.63, lead 1d |
| +8¢ | KXHIGHTHOU-26NOV26-B59.5 | 59° to 60° | NO | 31¢ | 27% | 61% | $0 | center 60.8, market mean 60.08, lead 0d |
| +7¢ | KXHIGHNY-26NOV26-T56 | 55° or below | NO | 4¢ | 65% | 89% | $0 | center 52.64, market mean 54.71, lead 0d |
| +7¢ | KXHIGHTSEA-26NOV26-B54.5 | 54° to 55° | NO | 26¢ | 44% | 67% | $0 | center 54.59, market mean 54.97, lead 0d |
| +7¢ | KXHIGHTHOU-26NOV27-B66.5 | 66° to 67° | NO | 53¢ | 14% | 40% | $0 | center 63.44, market mean 65.68, lead 1d |
| +7¢ | KXHIGHTSFO-26NOV26-B63.5 | 63° to 64° | NO | 33¢ | 34% | 60% | $0 | center 64.14, market mean 63.24, lead 0d |
| +7¢ | KXHIGHMIA-26NOV27-B74.5 | 74° to 75° | NO | 41¢ | 29% | 52% | $0 | center 73.44, market mean 74.64, lead 1d |
| +7¢ | KXHIGHLAX-26NOV27-B83.5 | 83° to 84° | NO | 55¢ | 15% | 38% | $0 | center 83.69, market mean 82.9, lead 1d |
| +7¢ | KXHIGHTBOS-26NOV27-T58 | 57° or below | NO | 45¢ | 20% | 48% | $0 | center 59.14, market mean 57.61, lead 1d |
| +7¢ | KXHIGHTBOS-26NOV26-T49 | 48° or below | NO | 38¢ | 28% | 55% | $0 | center 50.14, market mean 48.37, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV26-T57 | 56° or below | NO | 21¢ | 52% | 73% | $0 | center 56.74, market mean 56.05, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV27-B60.5 | 60° to 61° | YES | 7¢ | 35% | 14% | $0 | center 59.14, market mean 57.61, lead 1d |
| +6¢ | KXHIGHAUS-26NOV27-B68.5 | 68° to 69° | NO | 39¢ | 34% | 55% | $0 | center 67.94, market mean 68.92, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV27-B65.5 | 65° to 66° | YES | 4¢ | 31% | 10% | $0 | center 66.54, market mean 68.66, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV27-B58.5 | 58° to 59° | YES | 4¢ | 32% | 10% | $0 | center 59.89, market mean 62.63, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV26-B56.5 | 56° to 57° | YES | 2¢ | 15% | 8% | $0 | center 53.6, market mean 54.55, lead 0d |
| +6¢ | KXHIGHLAX-26NOV27-T84 | 85° or above | YES | 19¢ | 45% | 25% | $0 | center 83.69, market mean 82.9, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV27-B69.5 | 69° to 70° | NO | 51¢ | 15% | 43% | $0 | center 66.54, market mean 68.66, lead 1d |
| +6¢ | KXHIGHTSATX-26NOV26-B61.5 | 61° to 62° | YES | 3¢ | 28% | 9% | $0 | center 62.6, market mean 63.37, lead 0d |
| +6¢ | KXHIGHTSFO-26NOV26-B67.5 | 67° to 68° | YES | 2¢ | 14% | 8% | $0 | center 64.14, market mean 63.24, lead 0d |
| +6¢ | KXHIGHTDC-26NOV26-B61.5 | 61° to 62° | YES | 2¢ | 14% | 8% | $0 | center 57.94, market mean 56.42, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV26-B53.5 | 53° to 54° | YES | 2¢ | 14% | 8% | $0 | center 50.14, market mean 48.37, lead 0d |
