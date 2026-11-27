# Model vs. market

Scanned 2026-11-27 21:41 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 3¢ | 75% | 87% | $100 |  |
| +8¢ | KXHIGHPHIL-26NOV28-B56.5 | 56° to 57° | NO | 73¢ | 6% | 19% | $100 | center 52.15, market mean 54.97, lead 1d |
| +8¢ | KXAAAGASW-26NOV30-3.5200 | Above 3.5200 | YES | 6¢ | 23% | 14% | $100 |  |
| +8¢ | KXHIGHNY-26NOV28-B52.5 | 52° to 53° | NO | 64¢ | 19% | 28% | $100 | center 49.95, market mean 51.5, lead 1d |
| +6¢ | KXHIGHTBOS-26NOV28-B53.5 | 53° to 54° | NO | 60¢ | 22% | 34% | $100 | center 51.3, market mean 52.52, lead 1d |
| +6¢ | KXHIGHLAX-26NOV28-B73.5 | 73° to 74° | NO | 57¢ | 29% | 37% | $100 | center 75.2, market mean 74.51, lead 1d |
| +6¢ | KXHIGHTATL-26NOV28-B58.5 | 58° to 59° | YES | 10¢ | 27% | 16% | $100 | center 60.0, market mean 61.47, lead 1d |
| +5¢ | KXHIGHNY-26NOV28-T52 | 51° or below | YES | 63¢ | 75% | 68% | $100 | center 49.95, market mean 51.5, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +16¢ | KXHIGHTHOU-26NOV27-B64.5 | 64° to 65° | NO | 2¢ | 31% | 82% | $0 | center 65.0, market mean 64.5, lead 0d |
| +16¢ | KXHIGHLAX-26NOV27-B81.5 | 81° to 82° | NO | 7¢ | 27% | 77% | $0 | center 83.35, market mean 81.61, lead 0d |
| +15¢ | KXHIGHTPHX-26NOV27-B77.5 | 77° to 78° | NO | 5¢ | 32% | 80% | $0 | center 77.15, market mean 77.61, lead 0d |
| +15¢ | KXHIGHTNOLA-26NOV27-B56.5 | 56° to 57° | NO | 3¢ | 36% | 82% | $0 | center 56.15, market mean 56.57, lead 0d |
| +13¢ | KXHIGHTSATX-26NOV27-B67.5 | 67° to 68° | NO | 2¢ | 44% | 85% | $0 | center 67.15, market mean 67.39, lead 0d |
| +13¢ | KXHIGHAUS-26NOV27-B68.5 | 68° to 69° | NO | 13¢ | 30% | 74% | $0 | center 69.8, market mean 68.68, lead 0d |
| +12¢ | KXHIGHTNOLA-26NOV27-B58.5 | 58° to 59° | YES | 3¢ | 27% | 15% | $0 | center 56.15, market mean 56.57, lead 0d |
| +12¢ | KXHIGHAUS-26NOV27-B70.5 | 70° to 71° | YES | 11¢ | 60% | 23% | $0 | center 69.8, market mean 68.68, lead 0d |
| +10¢ | KXHIGHTDAL-26NOV27-B69.5 | 69° to 70° | NO | 2¢ | 55% | 88% | $0 | center 69.8, market mean 69.44, lead 0d |
| +10¢ | KXHIGHTPHX-26NOV27-B79.5 | 79° to 80° | YES | 5¢ | 26% | 15% | $0 | center 77.15, market mean 77.61, lead 0d |
| +10¢ | KXHIGHTATL-26NOV27-B51.5 | 51° to 52° | NO | 5¢ | 50% | 85% | $0 | center 51.8, market mean 51.51, lead 0d |
| +10¢ | KXHIGHTDAL-26NOV27-T70 | 71° or above | YES | 3¢ | 45% | 13% | $0 | center 69.8, market mean 69.44, lead 0d |
| +10¢ | KXAAAGASD-26NOV28-3.5350 | Above 3.5350 | YES | 2¢ | 43% | 12% | $0 |  |
| +10¢ | KXHIGHLAX-26NOV27-B83.5 | 83° to 84° | YES | 8¢ | 28% | 18% | $0 | center 83.35, market mean 81.61, lead 0d |
| +9¢ | KXHIGHPHIL-26NOV28-B54.5 | 54° to 55° | NO | 42¢ | 21% | 49% | $0 | center 52.15, market mean 54.97, lead 1d |
| +9¢ | KXAAAGASD-26NOV28-3.5300 | Above 3.5300 | YES | 47¢ | 86% | 56% | $0 |  |
| +9¢ | KXHIGHPHIL-26NOV28-T52 | 51° or below | YES | 2¢ | 39% | 11% | $0 | center 52.15, market mean 54.97, lead 1d |
| +8¢ | KXHIGHTPHX-26NOV28-B75.5 | 75° to 76° | NO | 34¢ | 32% | 58% | $0 | center 75.95, market mean 75.7, lead 1d |
| +8¢ | KXHIGHTBOS-26NOV28-T51 | 50° or below | YES | 3¢ | 36% | 11% | $0 | center 51.3, market mean 52.52, lead 1d |
| +8¢ | KXHIGHMIA-26NOV28-B73.5 | 73° to 74° | NO | 33¢ | 31% | 59% | $0 | center 72.55, market mean 73.79, lead 1d |
| +8¢ | KXHIGHDEN-26NOV27-B64.5 | 64° to 65° | YES | 3¢ | 36% | 11% | $0 | center 62.6, market mean 62.53, lead 0d |
| +8¢ | KXHIGHTATL-26NOV27-B53.5 | 53° to 54° | YES | 4¢ | 39% | 12% | $0 | center 51.8, market mean 51.51, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV27-B42.5 | 42° to 43° | NO | 10¢ | 51% | 82% | $0 | center 43.15, market mean 42.63, lead 0d |
| +7¢ | KXHIGHTNOLA-26NOV28-B67.5 | 67° to 68° | NO | 54¢ | 15% | 39% | $0 | center 66.55, market mean 68.02, lead 1d |
| +7¢ | KXHIGHDEN-26NOV27-B62.5 | 62° to 63° | NO | 5¢ | 60% | 88% | $0 | center 62.6, market mean 62.53, lead 0d |
| +7¢ | KXHIGHTSEA-26NOV27-B52.5 | 52° to 53° | YES | 3¢ | 18% | 10% | $0 | center 49.7, market mean 49.17, lead 0d |
| +7¢ | KXHIGHCHI-26NOV28-B54.5 | 54° to 55° | NO | 57¢ | 13% | 36% | $0 | center 51.2, market mean 53.1, lead 1d |
| +7¢ | KXHIGHTSFO-26NOV27-B66.5 | 66° to 67° | YES | 5¢ | 19% | 12% | $0 | center 63.85, market mean 62.8, lead 0d |
| +7¢ | KXHIGHTMIN-26NOV28-B50.5 | 50° to 51° | NO | 52¢ | 18% | 41% | $0 | center 47.8, market mean 49.52, lead 1d |
| +6¢ | KXHIGHTSATX-26NOV27-B65.5 | 65° to 66° | YES | 3¢ | 32% | 9% | $0 | center 67.15, market mean 67.39, lead 0d |
| +6¢ | KXHIGHAUS-26NOV28-B75.5 | 75° to 76° | NO | 44¢ | 28% | 50% | $0 | center 74.5, market mean 74.8, lead 1d |
| +6¢ | KXHIGHTATL-26NOV28-B62.5 | 62° to 63° | NO | 50¢ | 19% | 44% | $0 | center 60.0, market mean 61.47, lead 1d |
| +6¢ | KXHIGHPHIL-26NOV28-B52.5 | 52° to 53° | YES | 9¢ | 34% | 15% | $0 | center 52.15, market mean 54.97, lead 1d |
| +6¢ | KXHIGHTSFO-26NOV27-B62.5 | 62° to 63° | NO | 41¢ | 31% | 53% | $0 | center 63.85, market mean 62.8, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV27-B44.5 | 44° to 45° | YES | 8¢ | 37% | 13% | $0 | center 43.15, market mean 42.63, lead 0d |
| +5¢ | KXHIGHTHOU-26NOV27-B66.5 | 66° to 67° | YES | 3¢ | 28% | 8% | $0 | center 65.0, market mean 64.5, lead 0d |
| +5¢ | KXHIGHTSEA-26NOV28-B50.5 | 50° to 51° | NO | 56¢ | 29% | 39% | $100 | center 49.2, market mean 49.84, lead 1d |
| +4¢ | KXHIGHMIA-26NOV28-B71.5 | 71° to 72° | YES | 16¢ | 31% | 20% | $100 | center 72.55, market mean 73.79, lead 1d |
| +4¢ | KXHIGHMIA-26NOV28-T71 | 70° or below | YES | 6¢ | 18% | 10% | $100 | center 72.55, market mean 73.79, lead 1d |
| +4¢ | KXHIGHCHI-26NOV28-B50.5 | 50° to 51° | YES | 19¢ | 32% | 23% | $100 | center 51.2, market mean 53.1, lead 1d |
