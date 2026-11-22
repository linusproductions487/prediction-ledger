# Model vs. market

Scanned 2026-11-22 19:31 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXAAAGASM-26NOV30-3.55 | Above 3.55 | YES | 7¢ | 25% | 16% | $100 |  |
| +7¢ | KXHIGHCHI-26NOV23-B40.5 | 40° to 41° | NO | 64¢ | 18% | 29% | $100 | center 43.07, market mean 41.77, lead 1d |
| +7¢ | KXHIGHTBOS-26NOV23-B68.5 | 68° to 69° | NO | 70¢ | 11% | 23% | $100 | center 65.17, market mean 66.83, lead 1d |
| +5¢ | KXHIGHTPHX-26NOV23-B68.5 | 68° to 69° | NO | 47¢ | 36% | 48% | $100 | center 68.58, market mean 69.36, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +15¢ | KXHIGHTHOU-26NOV23-T68 | 67° or below | NO | 9¢ | 27% | 76% | $0 | center 69.17, market mean 67.01, lead 1d |
| +13¢ | KXHIGHTDC-26NOV22-B64.5 | 64° to 65° | NO | 12¢ | 25% | 75% | $0 | center 65.92, market mean 64.69, lead 0d |
| +13¢ | KXHIGHLAX-26NOV22-B67.5 | 67° to 68° | NO | 7¢ | 41% | 80% | $0 | center 67.42, market mean 67.66, lead 0d |
| +12¢ | KXHIGHNY-26NOV22-T61 | 60° or below | NO | 13¢ | 38% | 76% | $0 | center 60.97, market mean 59.95, lead 0d |
| +10¢ | KXHIGHMIA-26NOV22-B83.5 | 83° to 84° | NO | 18¢ | 34% | 72% | $0 | center 84.67, market mean 83.87, lead 0d |
| +10¢ | KXHIGHDEN-26NOV23-T40 | 39° or below | NO | 32¢ | 28% | 58% | $0 | center 41.32, market mean 39.4, lead 1d |
| +10¢ | KXHIGHTATL-26NOV22-T65 | 64° or below | NO | 3¢ | 56% | 88% | $0 | center 63.72, market mean 63.65, lead 0d |
| +9¢ | KXHIGHNY-26NOV22-B63.5 | 63° to 64° | YES | 3¢ | 22% | 12% | $0 | center 60.97, market mean 59.95, lead 0d |
| +9¢ | KXHIGHTSFO-26NOV22-B57.5 | 57° to 58° | YES | 9¢ | 29% | 18% | $0 | center 55.83, market mean 55.02, lead 0d |
| +9¢ | KXHIGHAUS-26NOV22-B73.5 | 73° to 74° | NO | 8¢ | 54% | 83% | $0 | center 72.92, market mean 73.74, lead 0d |
| +9¢ | KXHIGHTPHX-26NOV22-B71.5 | 71° to 72° | YES | 13¢ | 31% | 22% | $0 | center 72.77, market mean 73.62, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV22-B73.5 | 73° to 74° | NO | 28¢ | 35% | 63% | $0 | center 72.77, market mean 73.62, lead 0d |
| +8¢ | KXHIGHTLV-26NOV23-B61.5 | 61° to 62° | NO | 25¢ | 35% | 67% | $0 | center 61.17, market mean 61.57, lead 1d |
| +8¢ | KXHIGHTSFO-26NOV22-B55.5 | 55° to 56° | NO | 42¢ | 39% | 50% | $0 | center 55.83, market mean 55.02, lead 0d |
| +8¢ | KXHIGHLAX-26NOV22-B69.5 | 69° to 70° | YES | 8¢ | 25% | 16% | $0 | center 67.42, market mean 67.66, lead 0d |
| +8¢ | KXHIGHPHIL-26NOV22-B69.5 | 69° to 70° | YES | 2¢ | 19% | 10% | $0 | center 66.2, market mean 66.32, lead 0d |
| +8¢ | KXAAAGASW-26NOV23-3.6350 | Above 3.6350 | NO | 66¢ | 1% | 26% | $0 |  |
| +8¢ | KXHIGHNY-26NOV22-B61.5 | 61° to 62° | YES | 14¢ | 31% | 22% | $0 | center 60.97, market mean 59.95, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV22-B71.5 | 71° to 72° | NO | 29¢ | 30% | 64% | $0 | center 72.17, market mean 72.07, lead 0d |
| +7¢ | KXHIGHDEN-26NOV22-B45.5 | 45° to 46° | NO | 46¢ | 25% | 47% | $0 | center 47.17, market mean 46.33, lead 0d |
| +7¢ | KXAAAGASD-26NOV23-3.6350 | Above 3.6350 | NO | 69¢ | 1% | 24% | $0 |  |
| +7¢ | KXHIGHTLV-26NOV22-B58.5 | 58° to 59° | NO | 48¢ | 35% | 45% | $0 | center 57.92, market mean 57.64, lead 0d |
| +6¢ | KXHIGHTPHX-26NOV23-T68 | 67° or below | YES | 3¢ | 31% | 10% | $0 | center 68.58, market mean 69.36, lead 1d |
| +6¢ | KXHIGHLAX-26NOV23-B69.5 | 69° to 70° | NO | 43¢ | 30% | 51% | $0 | center 68.17, market mean 69.02, lead 1d |
| +6¢ | KXHIGHMIA-26NOV23-B79.5 | 79° to 80° | NO | 48¢ | 25% | 46% | $0 | center 79.67, market mean 79.54, lead 1d |
| +6¢ | KXHIGHTSEA-26NOV23-B51.5 | 51° to 52° | NO | 43¢ | 30% | 51% | $0 | center 50.17, market mean 51.31, lead 1d |
| +6¢ | KXHIGHTSEA-26NOV22-T47 | 46° or below | YES | 8¢ | 40% | 14% | $0 | center 46.38, market mean 47.97, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV22-B73.5 | 73° to 74° | YES | 26¢ | 44% | 32% | $0 | center 72.17, market mean 72.07, lead 0d |
| +6¢ | KXHIGHDEN-26NOV22-T48 | 49° or above | YES | 4¢ | 30% | 10% | $0 | center 47.17, market mean 46.33, lead 0d |
| +6¢ | KXHIGHTSEA-26NOV22-B47.5 | 47° to 48° | NO | 32¢ | 35% | 62% | $0 | center 46.38, market mean 47.97, lead 0d |
| +6¢ | KXHIGHTLV-26NOV22-B56.5 | 56° to 57° | NO | 57¢ | 30% | 37% | $0 | center 57.92, market mean 57.64, lead 0d |
| +6¢ | KXHIGHAUS-26NOV22-B75.5 | 75° to 76° | YES | 10¢ | 23% | 16% | $0 | center 72.92, market mean 73.74, lead 0d |
| +6¢ | KXHIGHAUS-26NOV23-B61.5 | 61° to 62° | NO | 49¢ | 26% | 45% | $0 | center 60.97, market mean 61.24, lead 1d |
| +6¢ | KXHIGHTHOU-26NOV22-B83.5 | 83° to 84° | YES | 9¢ | 23% | 15% | $0 | center 81.17, market mean 81.22, lead 0d |
| +6¢ | KXHIGHNY-26NOV23-B66.5 | 66° to 67° | NO | 47¢ | 27% | 47% | $0 | center 67.02, market mean 66.63, lead 1d |
| +5¢ | KXHIGHTDC-26NOV23-T66 | 65° or below | YES | 8¢ | 32% | 13% | $0 | center 67.12, market mean 68.2, lead 1d |
| +5¢ | KXHIGHTMIN-26NOV23-B32.5 | 32° to 33° | NO | 39¢ | 35% | 56% | $0 | center 32.17, market mean 32.23, lead 1d |
| +5¢ | KXHIGHMIA-26NOV22-B85.5 | 85° to 86° | YES | 23¢ | 38% | 28% | $0 | center 84.67, market mean 83.87, lead 0d |
| +5¢ | KXHIGHCHI-26NOV23-B44.5 | 44° to 45° | YES | 14¢ | 29% | 19% | $100 | center 43.07, market mean 41.77, lead 1d |
| +4¢ | KXHIGHTHOU-26NOV23-B68.5 | 68° to 69° | YES | 12¢ | 28% | 16% | $100 | center 69.17, market mean 67.01, lead 1d |
