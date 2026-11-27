# Model vs. market

Scanned 2026-11-27 21:11 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 5¢ | 75% | 86% | $100 |  |
| +8¢ | KXAAAGASW-26NOV30-3.5200 | Above 3.5200 | YES | 6¢ | 23% | 14% | $100 |  |
| +8¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 7¢ | 75% | 85% | $100 |  |
| +6¢ | KXHIGHNY-26NOV28-B52.5 | 52° to 53° | NO | 66¢ | 19% | 28% | $100 | center 49.95, market mean 51.49, lead 1d |
| +6¢ | KXHIGHPHIL-26NOV28-B52.5 | 52° to 53° | YES | 15¢ | 33% | 21% | $100 | center 52.0, market mean 54.97, lead 1d |
| +6¢ | KXHIGHLAX-26NOV28-B73.5 | 73° to 74° | NO | 58¢ | 28% | 36% | $100 | center 75.2, market mean 74.52, lead 1d |
| +6¢ | KXHIGHTSEA-26NOV28-B50.5 | 50° to 51° | NO | 56¢ | 28% | 38% | $100 | center 49.15, market mean 49.85, lead 1d |
| +6¢ | KXHIGHTBOS-26NOV28-B53.5 | 53° to 54° | NO | 60¢ | 23% | 35% | $100 | center 51.45, market mean 52.51, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +15¢ | KXHIGHLAX-26NOV27-B81.5 | 81° to 82° | NO | 8¢ | 30% | 77% | $0 | center 82.9, market mean 81.58, lead 0d |
| +15¢ | KXHIGHTDC-26NOV27-B54.5 | 54° to 55° | NO | 11¢ | 27% | 74% | $0 | center 56.4, market mean 54.77, lead 0d |
| +15¢ | KXHIGHTNOLA-26NOV27-B56.5 | 56° to 57° | NO | 3¢ | 35% | 82% | $0 | center 56.15, market mean 56.56, lead 0d |
| +12¢ | KXHIGHTATL-26NOV27-B51.5 | 51° to 52° | NO | 5¢ | 42% | 83% | $0 | center 50.9, market mean 51.51, lead 0d |
| +11¢ | KXHIGHTSFO-26NOV27-B62.5 | 62° to 63° | NO | 46¢ | 31% | 43% | $0 | center 63.85, market mean 62.83, lead 0d |
| +10¢ | KXHIGHTHOU-26NOV27-B62.5 | 62° to 63° | NO | 26¢ | 21% | 63% | $0 | center 65.1, market mean 63.04, lead 0d |
| +10¢ | KXHIGHLAX-26NOV27-B83.5 | 83° to 84° | YES | 7¢ | 29% | 17% | $0 | center 82.9, market mean 81.58, lead 0d |
| +10¢ | KXHIGHTPHX-26NOV27-B79.5 | 79° to 80° | YES | 4¢ | 25% | 14% | $0 | center 77.15, market mean 77.17, lead 0d |
| +10¢ | KXHIGHAUS-26NOV27-B68.5 | 68° to 69° | NO | 22¢ | 30% | 68% | $0 | center 69.8, market mean 68.91, lead 0d |
| +10¢ | KXHIGHTSATX-26NOV27-B67.5 | 67° to 68° | NO | 9¢ | 44% | 81% | $0 | center 67.15, market mean 67.34, lead 0d |
| +9¢ | KXHIGHPHIL-26NOV28-T52 | 51° or below | YES | 2¢ | 41% | 11% | $0 | center 52.0, market mean 54.97, lead 1d |
| +9¢ | KXHIGHDEN-26NOV27-B62.5 | 62° to 63° | NO | 2¢ | 60% | 89% | $0 | center 62.6, market mean 62.54, lead 0d |
| +9¢ | KXAAAGASD-26NOV28-3.5300 | Above 3.5300 | YES | 47¢ | 86% | 56% | $0 |  |
| +9¢ | KXHIGHPHIL-26NOV28-B54.5 | 54° to 55° | NO | 43¢ | 19% | 48% | $0 | center 52.0, market mean 54.97, lead 1d |
| +9¢ | KXHIGHTMIN-26NOV28-B50.5 | 50° to 51° | NO | 53¢ | 8% | 38% | $0 | center 46.4, market mean 49.49, lead 1d |
| +8¢ | KXHIGHCHI-26NOV27-B47.5 | 47° to 48° | YES | 25¢ | 43% | 33% | $0 | center 46.4, market mean 45.99, lead 0d |
| +8¢ | KXHIGHMIA-26NOV28-B73.5 | 73° to 74° | NO | 33¢ | 31% | 59% | $0 | center 72.6, market mean 73.81, lead 1d |
| +8¢ | KXHIGHTATL-26NOV27-B53.5 | 53° to 54° | YES | 4¢ | 22% | 12% | $0 | center 50.9, market mean 51.51, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV27-B42.5 | 42° to 43° | NO | 7¢ | 56% | 85% | $0 | center 42.8, market mean 42.59, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV27-B69.5 | 69° to 70° | NO | 6¢ | 57% | 86% | $0 | center 69.8, market mean 69.47, lead 0d |
| +8¢ | KXHIGHDEN-26NOV27-B64.5 | 64° to 65° | YES | 3¢ | 36% | 11% | $0 | center 62.6, market mean 62.54, lead 0d |
| +7¢ | KXHIGHTDAL-26NOV27-T70 | 71° or above | YES | 6¢ | 43% | 13% | $0 | center 69.8, market mean 69.47, lead 0d |
| +7¢ | KXHIGHTSEA-26NOV27-B52.5 | 52° to 53° | YES | 3¢ | 18% | 10% | $0 | center 49.7, market mean 49.13, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV27-B77.5 | 77° to 78° | NO | 28¢ | 31% | 65% | $0 | center 77.15, market mean 77.17, lead 0d |
| +7¢ | KXHIGHCHI-26NOV28-B54.5 | 54° to 55° | NO | 58¢ | 11% | 35% | $0 | center 50.9, market mean 53.09, lead 1d |
| +7¢ | KXHIGHTBOS-26NOV28-T51 | 50° or below | YES | 4¢ | 34% | 11% | $0 | center 51.45, market mean 52.51, lead 1d |
| +7¢ | KXHIGHTSFO-26NOV27-B66.5 | 66° to 67° | YES | 5¢ | 19% | 12% | $0 | center 63.85, market mean 62.83, lead 0d |
| +7¢ | KXHIGHTDC-26NOV27-B56.5 | 56° to 57° | YES | 11¢ | 43% | 18% | $0 | center 56.4, market mean 54.77, lead 0d |
| +7¢ | KXHIGHAUS-26NOV28-B75.5 | 75° to 76° | NO | 44¢ | 28% | 49% | $0 | center 74.5, market mean 74.79, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV28-B75.5 | 75° to 76° | NO | 37¢ | 32% | 56% | $0 | center 75.95, market mean 75.66, lead 1d |
| +6¢ | KXHIGHAUS-26NOV27-B70.5 | 70° to 71° | YES | 24¢ | 60% | 30% | $0 | center 69.8, market mean 68.91, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV27-B65.5 | 65° to 66° | YES | 5¢ | 32% | 11% | $0 | center 67.15, market mean 67.34, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV27-B44.5 | 44° to 45° | YES | 5¢ | 35% | 11% | $0 | center 42.8, market mean 42.59, lead 0d |
| +6¢ | KXHIGHTDC-26NOV28-B60.5 | 60° to 61° | NO | 59¢ | 15% | 35% | $0 | center 57.5, market mean 59.3, lead 1d |
| +6¢ | KXHIGHTMIN-26NOV28-B46.5 | 46° to 47° | YES | 8¢ | 34% | 14% | $0 | center 46.4, market mean 49.49, lead 1d |
| +5¢ | KXHIGHTNOLA-26NOV27-B58.5 | 58° to 59° | YES | 3¢ | 27% | 8% | $0 | center 56.15, market mean 56.56, lead 0d |
| +5¢ | KXHIGHCHI-26NOV28-B50.5 | 50° to 51° | YES | 18¢ | 33% | 23% | $100 | center 50.9, market mean 53.09, lead 1d |
| +5¢ | KXHIGHTDC-26NOV28-B56.5 | 56° to 57° | YES | 15¢ | 31% | 20% | $100 | center 57.5, market mean 59.3, lead 1d |
| +5¢ | KXHIGHTATL-26NOV28-B58.5 | 58° to 59° | YES | 11¢ | 27% | 16% | $100 | center 60.0, market mean 61.44, lead 1d |
| +4¢ | KXHIGHNY-26NOV28-T52 | 51° or below | YES | 64¢ | 75% | 68% | $100 | center 49.95, market mean 51.49, lead 1d |
