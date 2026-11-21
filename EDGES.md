# Model vs. market

Scanned 2026-11-21 19:09 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXAAAGASD-26NOV22-3.6450 | Above 3.6450 | NO | 81¢ | 0% | 10% | $100 |  |
| +8¢ | KXAAAGASW-26NOV23-3.6350 | Above 3.6350 | NO | 83¢ | 0% | 9% | $100 |  |
| +6¢ | KXHIGHNY-26NOV22-T61 | 60° or below | NO | 52¢ | 32% | 42% | $100 | center 61.74, market mean 60.77, lead 1d |
| +5¢ | KXHIGHTSFO-26NOV22-B55.5 | 55° to 56° | NO | 49¢ | 33% | 46% | $100 | center 56.4, market mean 56.19, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +18¢ | KXHIGHMIA-26NOV21-B82.5 | 82° to 83° | NO | 4¢ | 23% | 78% | $0 | center 83.74, market mean 82.59, lead 0d |
| +16¢ | KXHIGHTBOS-26NOV21-B58.5 | 58° to 59° | NO | 6¢ | 29% | 78% | $0 | center 60.45, market mean 58.72, lead 0d |
| +15¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 23¢ | 0% | 62% | $0 |  |
| +13¢ | KXHIGHTNOLA-26NOV21-B75.5 | 75° to 76° | NO | 28¢ | 11% | 59% | $0 | center 74.54, market mean 75.23, lead 0d |
| +13¢ | KXHIGHTDC-26NOV21-B67.5 | 67° to 68° | NO | 4¢ | 43% | 83% | $0 | center 66.2, market mean 67.54, lead 0d |
| +11¢ | KXHIGHTSFO-26NOV21-B57.5 | 57° to 58° | NO | 39¢ | 38% | 50% | $0 | center 57.9, market mean 57.16, lead 0d |
| +11¢ | KXHIGHTATL-26NOV21-T65 | 64° or below | NO | 3¢ | 75% | 86% | $0 | center 62.6, market mean 63.65, lead 0d |
| +10¢ | KXHIGHTSATX-26NOV22-T71 | 70° or below | YES | 9¢ | 59% | 20% | $0 | center 69.64, market mean 73.49, lead 1d |
| +10¢ | KXHIGHTBOS-26NOV21-B62.5 | 62° to 63° | YES | 3¢ | 25% | 13% | $0 | center 60.45, market mean 58.72, lead 0d |
| +10¢ | KXHIGHTSEA-26NOV21-B50.5 | 50° to 51° | YES | 9¢ | 31% | 19% | $0 | center 49.6, market mean 47.75, lead 0d |
| +10¢ | KXHIGHTOKC-26NOV21-B72.5 | 72° to 73° | YES | 2¢ | 23% | 12% | $0 | center 70.44, market mean 67.76, lead 0d |
| +10¢ | KXHIGHMIA-26NOV21-B84.5 | 84° to 85° | YES | 4¢ | 24% | 14% | $0 | center 83.74, market mean 82.59, lead 0d |
| +10¢ | KXHIGHTATL-26NOV22-T65 | 64° or below | NO | 22¢ | 37% | 68% | $0 | center 66.59, market mean 64.29, lead 1d |
| +10¢ | KXHIGHTSFO-26NOV21-B59.5 | 59° to 60° | YES | 9¢ | 29% | 19% | $0 | center 57.9, market mean 57.16, lead 0d |
| +10¢ | KXHIGHTSEA-26NOV21-B46.5 | 46° to 47° | NO | 66¢ | 15% | 25% | $0 | center 49.6, market mean 47.75, lead 0d |
| +9¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 3¢ | 58% | 88% | $0 |  |
| +8¢ | KXHIGHNY-26NOV21-T65 | 66° or above | YES | 18¢ | 37% | 26% | $0 | center 64.44, market mean 64.7, lead 0d |
| +8¢ | KXHIGHCHI-26NOV21-B68.5 | 68° to 69° | NO | 39¢ | 42% | 53% | $0 | center 68.89, market mean 69.22, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV21-B77.5 | 77° to 78° | YES | 2¢ | 19% | 10% | $0 | center 75.04, market mean 73.23, lead 0d |
| +8¢ | KXHIGHNY-26NOV21-B64.5 | 64° to 65° | NO | 17¢ | 45% | 75% | $0 | center 64.44, market mean 64.7, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV21-B76.5 | 76° to 77° | YES | 2¢ | 19% | 10% | $0 | center 73.94, market mean 72.14, lead 0d |
| +8¢ | KXHIGHLAX-26NOV21-B67.5 | 67° to 68° | NO | 45¢ | 37% | 47% | $0 | center 68.0, market mean 68.23, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV22-B73.5 | 73° to 74° | NO | 52¢ | 12% | 40% | $0 | center 69.64, market mean 73.49, lead 1d |
| +8¢ | KXHIGHTDAL-26NOV21-B75.5 | 75° to 76° | YES | 5¢ | 37% | 13% | $0 | center 75.04, market mean 73.23, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV22-B73.5 | 73° to 74° | NO | 32¢ | 34% | 60% | $0 | center 73.0, market mean 73.3, lead 1d |
| +8¢ | KXHIGHTBOS-26NOV22-T62 | 61° or below | NO | 8¢ | 61% | 85% | $0 | center 60.65, market mean 60.97, lead 1d |
| +7¢ | KXHIGHAUS-26NOV21-B76.5 | 76° to 77° | NO | 56¢ | 28% | 37% | $0 | center 75.44, market mean 75.49, lead 0d |
| +7¢ | KXHIGHLAX-26NOV21-B65.5 | 65° to 66° | YES | 4¢ | 19% | 11% | $0 | center 68.0, market mean 68.23, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV21-B60.5 | 60° to 61° | YES | 5¢ | 36% | 12% | $0 | center 60.45, market mean 58.72, lead 0d |
| +7¢ | KXHIGHAUS-26NOV21-T74 | 73° or below | YES | 4¢ | 18% | 11% | $0 | center 75.44, market mean 75.49, lead 0d |
| +7¢ | KXHIGHAUS-26NOV21-B78.5 | 78° to 79° | YES | 2¢ | 16% | 9% | $0 | center 75.44, market mean 75.49, lead 0d |
| +7¢ | KXHIGHLAX-26NOV22-B67.5 | 67° to 68° | NO | 36¢ | 35% | 57% | $0 | center 67.34, market mean 67.82, lead 1d |
| +7¢ | KXHIGHDEN-26NOV21-B44.5 | 44° to 45° | NO | 37¢ | 33% | 56% | $0 | center 45.34, market mean 44.4, lead 0d |
| +7¢ | KXHIGHTNOLA-26NOV21-B73.5 | 73° to 74° | YES | 21¢ | 40% | 28% | $0 | center 74.54, market mean 75.23, lead 0d |
| +7¢ | KXHIGHTNOLA-26NOV21-B77.5 | 77° to 78° | YES | 5¢ | 19% | 12% | $0 | center 74.54, market mean 75.23, lead 0d |
| +7¢ | KXHIGHDEN-26NOV21-B48.5 | 48° to 49° | YES | 2¢ | 16% | 9% | $0 | center 45.34, market mean 44.4, lead 0d |
| +7¢ | KXHIGHTSEA-26NOV21-B52.5 | 52° to 53° | YES | 2¢ | 16% | 9% | $0 | center 49.6, market mean 47.75, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV22-T66 | 65° or below | YES | 16¢ | 44% | 23% | $0 | center 66.29, market mean 67.18, lead 1d |
| +6¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 47¢ | 26% | 46% | $0 |  |
| +6¢ | KXHIGHTSATX-26NOV21-B72.5 | 72° to 73° | NO | 42¢ | 29% | 52% | $0 | center 73.94, market mean 72.14, lead 0d |
