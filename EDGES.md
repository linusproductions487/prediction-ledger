# Model vs. market

Scanned 2026-11-26 21:26 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +6¢ | KXHIGHTATL-26NOV27-B51.5 | 51° to 52° | NO | 64¢ | 19% | 30% | $100 | center 50.14, market mean 50.89, lead 1d |
| +6¢ | KXHIGHCHI-26NOV27-B47.5 | 47° to 48° | NO | 51¢ | 31% | 43% | $100 | center 46.14, market mean 47.32, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +24¢ | KXAAAGASD-26NOV27-3.5400 | Above 3.5400 | NO | 4¢ | 0% | 72% | $0 |  |
| +20¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 2¢ | 15% | 78% | $0 |  |
| +17¢ | KXHIGHTOKC-26NOV26-B47.5 | 47° to 48° | NO | 3¢ | 27% | 80% | $0 | center 46.84, market mean 47.56, lead 0d |
| +16¢ | KXHIGHTPHX-26NOV26-B78.5 | 78° to 79° | NO | 8¢ | 22% | 76% | $0 | center 78.99, market mean 78.61, lead 0d |
| +15¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 38¢ | 2% | 47% | $0 |  |
| +14¢ | KXHIGHAUS-26NOV26-B60.5 | 60° to 61° | NO | 2¢ | 38% | 83% | $0 | center 59.0, market mean 60.5, lead 0d |
| +14¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 38¢ | 2% | 48% | $0 |  |
| +13¢ | KXHIGHTNOLA-26NOV26-B57.5 | 57° to 58° | NO | 3¢ | 42% | 84% | $0 | center 57.2, market mean 57.5, lead 0d |
| +13¢ | KXAAAGASD-26NOV27-3.5450 | Above 3.5450 | NO | 46¢ | 0% | 41% | $0 |  |
| +12¢ | KXHIGHDEN-26NOV26-B58.5 | 58° to 59° | NO | 5¢ | 45% | 83% | $0 | center 58.64, market mean 58.56, lead 0d |
| +12¢ | KXHIGHTDAL-26NOV26-B54.5 | 54° to 55° | NO | 2¢ | 49% | 86% | $0 | center 53.6, market mean 54.55, lead 0d |
| +11¢ | KXHIGHCHI-26NOV26-B44.5 | 44° to 45° | NO | 5¢ | 47% | 84% | $0 | center 45.54, market mean 44.61, lead 0d |
| +11¢ | KXHIGHTSATX-26NOV26-B63.5 | 63° to 64° | NO | 2¢ | 52% | 87% | $0 | center 62.6, market mean 63.38, lead 0d |
| +11¢ | KXHIGHDEN-26NOV26-B60.5 | 60° to 61° | YES | 6¢ | 29% | 17% | $0 | center 58.64, market mean 58.56, lead 0d |
| +9¢ | KXHIGHCHI-26NOV26-B46.5 | 46° to 47° | YES | 6¢ | 46% | 15% | $0 | center 45.54, market mean 44.61, lead 0d |
| +9¢ | KXHIGHTBOS-26NOV26-B51.5 | 51° to 52° | YES | 5¢ | 24% | 14% | $0 | center 50.14, market mean 48.35, lead 0d |
| +9¢ | KXHIGHTHOU-26NOV26-B59.5 | 59° to 60° | NO | 31¢ | 27% | 60% | $0 | center 60.8, market mean 60.09, lead 0d |
| +9¢ | KXHIGHTSEA-26NOV27-B50.5 | 50° to 51° | NO | 34¢ | 29% | 57% | $0 | center 49.19, market mean 50.74, lead 1d |
| +8¢ | KXHIGHTSATX-26NOV27-B67.5 | 67° to 68° | NO | 40¢ | 25% | 52% | $0 | center 65.79, market mean 66.64, lead 1d |
| +8¢ | KXHIGHTPHX-26NOV27-B77.5 | 77° to 78° | NO | 41¢ | 26% | 51% | $0 | center 76.89, market mean 78.29, lead 1d |
| +8¢ | KXHIGHTOKC-26NOV27-B62.5 | 62° to 63° | NO | 49¢ | 16% | 43% | $0 | center 59.89, market mean 62.6, lead 1d |
| +8¢ | KXHIGHNY-26NOV26-T56 | 55° or below | NO | 4¢ | 64% | 88% | $0 | center 52.79, market mean 54.71, lead 0d |
| +7¢ | KXHIGHLAX-26NOV27-B83.5 | 83° to 84° | NO | 54¢ | 15% | 39% | $0 | center 83.69, market mean 82.99, lead 1d |
| +7¢ | KXHIGHTHOU-26NOV27-B66.5 | 66° to 67° | NO | 53¢ | 14% | 40% | $0 | center 63.44, market mean 65.66, lead 1d |
| +7¢ | KXHIGHMIA-26NOV27-B74.5 | 74° to 75° | NO | 41¢ | 29% | 52% | $0 | center 73.44, market mean 74.64, lead 1d |
| +7¢ | KXHIGHTBOS-26NOV27-T58 | 57° or below | NO | 45¢ | 20% | 48% | $0 | center 59.14, market mean 57.61, lead 1d |
| +7¢ | KXHIGHTOKC-26NOV26-B49.5 | 49° to 50° | YES | 3¢ | 18% | 10% | $0 | center 46.84, market mean 47.56, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV26-T49 | 48° or below | NO | 36¢ | 28% | 57% | $0 | center 50.14, market mean 48.35, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV27-B60.5 | 60° to 61° | YES | 7¢ | 35% | 14% | $0 | center 59.14, market mean 57.61, lead 1d |
| +6¢ | KXHIGHAUS-26NOV27-B68.5 | 68° to 69° | NO | 39¢ | 34% | 55% | $0 | center 67.94, market mean 68.92, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV27-B65.5 | 65° to 66° | YES | 4¢ | 31% | 10% | $0 | center 66.54, market mean 68.62, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV27-B58.5 | 58° to 59° | YES | 4¢ | 32% | 10% | $0 | center 59.89, market mean 62.6, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV26-B56.5 | 56° to 57° | YES | 2¢ | 15% | 8% | $0 | center 53.6, market mean 54.55, lead 0d |
| +6¢ | KXHIGHLAX-26NOV27-T84 | 85° or above | YES | 19¢ | 45% | 25% | $0 | center 83.69, market mean 82.99, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV27-B69.5 | 69° to 70° | NO | 52¢ | 15% | 42% | $0 | center 66.54, market mean 68.62, lead 1d |
| +6¢ | KXHIGHTPHX-26NOV26-B80.5 | 80° to 81° | YES | 5¢ | 30% | 11% | $0 | center 78.99, market mean 78.61, lead 0d |
| +6¢ | KXHIGHTSFO-26NOV26-B65.5 | 65° to 66° | YES | 13¢ | 26% | 19% | $0 | center 64.14, market mean 63.28, lead 0d |
| +6¢ | KXHIGHTSFO-26NOV26-B67.5 | 67° to 68° | YES | 2¢ | 14% | 8% | $0 | center 64.14, market mean 63.28, lead 0d |
| +6¢ | KXHIGHTDC-26NOV26-B61.5 | 61° to 62° | YES | 2¢ | 14% | 8% | $0 | center 57.94, market mean 56.34, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV26-B53.5 | 53° to 54° | YES | 2¢ | 14% | 8% | $0 | center 50.14, market mean 48.35, lead 0d |
