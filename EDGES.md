# Model vs. market

Scanned 2026-11-27 21:38 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 3¢ | 75% | 87% | $100 |  |
| +8¢ | KXHIGHPHIL-26NOV28-B56.5 | 56° to 57° | NO | 73¢ | 6% | 19% | $100 | center 52.15, market mean 54.97, lead 1d |
| +8¢ | KXAAAGASW-26NOV30-3.5200 | Above 3.5200 | YES | 6¢ | 23% | 14% | $100 |  |
| +6¢ | KXHIGHAUS-26NOV28-B75.5 | 75° to 76° | NO | 49¢ | 32% | 45% | $100 | center 75.15, market mean 74.8, lead 1d |
| +5¢ | KXHIGHTSEA-26NOV28-B50.5 | 50° to 51° | NO | 56¢ | 28% | 39% | $100 | center 49.15, market mean 49.84, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +16¢ | KXHIGHTHOU-26NOV27-B64.5 | 64° to 65° | NO | 2¢ | 31% | 82% | $0 | center 65.15, market mean 64.5, lead 0d |
| +15¢ | KXHIGHTNOLA-26NOV27-B56.5 | 56° to 57° | NO | 3¢ | 35% | 82% | $0 | center 56.15, market mean 56.57, lead 0d |
| +13¢ | KXHIGHLAX-26NOV27-B81.5 | 81° to 82° | NO | 9¢ | 34% | 78% | $0 | center 82.15, market mean 81.58, lead 0d |
| +13¢ | KXHIGHAUS-26NOV27-B68.5 | 68° to 69° | NO | 14¢ | 27% | 73% | $0 | center 69.8, market mean 68.71, lead 0d |
| +13¢ | KXHIGHTPHX-26NOV27-B77.5 | 77° to 78° | NO | 13¢ | 32% | 74% | $0 | center 77.15, market mean 77.68, lead 0d |
| +13¢ | KXHIGHTSATX-26NOV27-B67.5 | 67° to 68° | NO | 2¢ | 46% | 85% | $0 | center 67.15, market mean 67.39, lead 0d |
| +12¢ | KXHIGHTNOLA-26NOV27-B58.5 | 58° to 59° | YES | 3¢ | 27% | 15% | $0 | center 56.15, market mean 56.57, lead 0d |
| +11¢ | KXHIGHTDAL-26NOV27-B69.5 | 69° to 70° | NO | 2¢ | 53% | 87% | $0 | center 69.8, market mean 69.44, lead 0d |
| +10¢ | KXHIGHTDAL-26NOV27-T70 | 71° or above | YES | 3¢ | 47% | 13% | $0 | center 69.8, market mean 69.44, lead 0d |
| +10¢ | KXAAAGASD-26NOV28-3.5350 | Above 3.5350 | YES | 2¢ | 43% | 12% | $0 |  |
| +10¢ | KXHIGHTPHX-26NOV28-B75.5 | 75° to 76° | NO | 34¢ | 26% | 56% | $0 | center 77.15, market mean 75.71, lead 1d |
| +10¢ | KXHIGHTATL-26NOV27-B51.5 | 51° to 52° | NO | 5¢ | 51% | 86% | $0 | center 51.8, market mean 51.51, lead 0d |
| +9¢ | KXHIGHTMIN-26NOV28-B50.5 | 50° to 51° | NO | 52¢ | 7% | 39% | $0 | center 46.15, market mean 49.5, lead 1d |
| +9¢ | KXHIGHPHIL-26NOV28-B54.5 | 54° to 55° | NO | 42¢ | 21% | 49% | $0 | center 52.15, market mean 54.97, lead 1d |
| +9¢ | KXHIGHDEN-26NOV27-B62.5 | 62° to 63° | NO | 5¢ | 54% | 86% | $0 | center 62.6, market mean 62.53, lead 0d |
| +9¢ | KXHIGHPHIL-26NOV28-T52 | 51° or below | YES | 2¢ | 39% | 11% | $0 | center 52.15, market mean 54.97, lead 1d |
| +8¢ | KXAAAGASD-26NOV28-3.5300 | Above 3.5300 | YES | 47¢ | 86% | 56% | $0 |  |
| +8¢ | KXHIGHAUS-26NOV27-B70.5 | 70° to 71° | YES | 14¢ | 53% | 22% | $0 | center 69.8, market mean 68.71, lead 0d |
| +8¢ | KXHIGHDEN-26NOV27-B64.5 | 64° to 65° | YES | 3¢ | 37% | 11% | $0 | center 62.6, market mean 62.53, lead 0d |
| +8¢ | KXHIGHMIA-26NOV28-B73.5 | 73° to 74° | NO | 32¢ | 33% | 60% | $0 | center 73.15, market mean 73.82, lead 1d |
| +8¢ | KXHIGHTNOLA-26NOV28-B67.5 | 67° to 68° | NO | 54¢ | 13% | 38% | $0 | center 66.15, market mean 68.02, lead 1d |
| +8¢ | KXHIGHTMIN-26NOV27-B42.5 | 42° to 43° | NO | 10¢ | 50% | 82% | $0 | center 43.15, market mean 42.63, lead 0d |
| +8¢ | KXHIGHTATL-26NOV27-B53.5 | 53° to 54° | YES | 4¢ | 39% | 12% | $0 | center 51.8, market mean 51.51, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV27-B66.5 | 66° to 67° | YES | 5¢ | 21% | 13% | $0 | center 64.15, market mean 62.56, lead 0d |
| +8¢ | KXHIGHDEN-26NOV28-T50 | 51° or above | NO | 8¢ | 60% | 84% | $0 | center 51.15, market mean 51.21, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV27-B79.5 | 79° to 80° | YES | 9¢ | 24% | 16% | $0 | center 77.15, market mean 77.68, lead 0d |
| +6¢ | KXHIGHLAX-26NOV28-B73.5 | 73° to 74° | NO | 55¢ | 18% | 39% | $0 | center 76.15, market mean 74.51, lead 1d |
| +6¢ | KXHIGHTSATX-26NOV27-B65.5 | 65° to 66° | YES | 3¢ | 32% | 9% | $0 | center 67.15, market mean 67.39, lead 0d |
| +6¢ | KXHIGHCHI-26NOV28-B54.5 | 54° to 55° | NO | 58¢ | 12% | 36% | $0 | center 51.15, market mean 53.09, lead 1d |
| +6¢ | KXHIGHTSFO-26NOV28-T64 | 63° or below | NO | 48¢ | 17% | 46% | $0 | center 67.15, market mean 63.85, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV28-B72.5 | 72° to 73° | NO | 39¢ | 35% | 55% | $0 | center 72.15, market mean 72.27, lead 1d |
| +6¢ | KXHIGHTSFO-26NOV27-B64.5 | 64° to 65° | YES | 16¢ | 31% | 22% | $0 | center 64.15, market mean 62.56, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV28-B52.5 | 52° to 53° | YES | 9¢ | 34% | 15% | $0 | center 52.15, market mean 54.97, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV28-B63.5 | 63° to 64° | NO | 47¢ | 24% | 47% | $0 | center 62.15, market mean 63.56, lead 1d |
| +6¢ | KXHIGHLAX-26NOV27-B83.5 | 83° to 84° | YES | 7¢ | 32% | 13% | $0 | center 82.15, market mean 81.58, lead 0d |
| +6¢ | KXHIGHTHOU-26NOV27-B66.5 | 66° to 67° | YES | 3¢ | 28% | 8% | $0 | center 65.15, market mean 64.5, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV27-B44.5 | 44° to 45° | YES | 8¢ | 38% | 14% | $0 | center 43.15, market mean 42.63, lead 0d |
| +5¢ | KXHIGHCHI-26NOV27-B45.5 | 45° to 46° | NO | 44¢ | 40% | 51% | $0 | center 46.4, market mean 46.26, lead 0d |
| +5¢ | KXHIGHTMIN-26NOV28-B46.5 | 46° to 47° | YES | 15¢ | 32% | 20% | $100 | center 46.15, market mean 49.5, lead 1d |
| +4¢ | KXHIGHTBOS-26NOV28-B51.5 | 51° to 52° | NO | 57¢ | 27% | 39% | $100 | center 53.15, market mean 52.52, lead 1d |
