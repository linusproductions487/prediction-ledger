# Model vs. market

Scanned 2026-11-21 06:59 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXHIGHLAX-26NOV21-B65.5 | 65° to 66° | YES | 5¢ | 25% | 14% | $100 | center 67.25, market mean 69.1, lead 1d |
| +7¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 52¢ | 33% | 41% | $100 |  |
| +7¢ | KXHIGHDEN-26NOV21-B46.5 | 46° to 47° | NO | 64¢ | 20% | 29% | $100 | center 44.95, market mean 45.93, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +20¢ | KXAAAGASW-26NOV23-3.6250 | Above 3.6250 | NO | 2¢ | 19% | 79% | $0 |  |
| +13¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 36¢ | 11% | 51% | $0 |  |
| +10¢ | KXHIGHMIA-26NOV21-B84.5 | 84° to 85° | NO | 60¢ | 19% | 30% | $0 | center 82.75, market mean 83.3, lead 0d |
| +10¢ | KXHIGHTNOLA-26NOV21-B73.5 | 73° to 74° | NO | 39¢ | 18% | 51% | $0 | center 74.0, market mean 74.02, lead 0d |
| +10¢ | KXHIGHTDAL-26NOV21-B75.5 | 75° to 76° | NO | 43¢ | 37% | 47% | $0 | center 75.0, market mean 74.88, lead 0d |
| +10¢ | KXHIGHCHI-26NOV21-B66.5 | 66° to 67° | YES | 6¢ | 26% | 16% | $0 | center 68.35, market mean 69.61, lead 0d |
| +9¢ | KXHIGHMIA-26NOV21-T80 | 79° or below | YES | 2¢ | 20% | 11% | $0 | center 82.75, market mean 83.3, lead 0d |
| +8¢ | KXHIGHLAX-26NOV21-B69.5 | 69° to 70° | NO | 45¢ | 21% | 47% | $0 | center 67.25, market mean 69.1, lead 1d |
| +8¢ | KXHIGHTSATX-26NOV21-B72.5 | 72° to 73° | NO | 52¢ | 31% | 40% | $0 | center 73.85, market mean 72.91, lead 0d |
| +8¢ | KXHIGHTOKC-26NOV21-T68 | 67° or below | NO | 63¢ | 19% | 29% | $0 | center 69.25, market mean 68.33, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV21-T67 | 66° or below | YES | 2¢ | 34% | 10% | $0 | center 67.55, market mean 68.58, lead 1d |
| +8¢ | KXHIGHTNOLA-26NOV21-B75.5 | 75° to 76° | NO | 73¢ | 8% | 19% | $0 | center 74.0, market mean 74.02, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV21-B62.5 | 62° to 63° | NO | 9¢ | 57% | 84% | $0 | center 61.9, market mean 62.67, lead 0d |
| +7¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 8¢ | 63% | 85% | $0 |  |
| +7¢ | KXHIGHCHI-26NOV21-B70.5 | 70° to 71° | NO | 47¢ | 22% | 46% | $0 | center 68.35, market mean 69.61, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV21-B76.5 | 76° to 77° | YES | 3¢ | 17% | 10% | $0 | center 73.85, market mean 72.91, lead 0d |
| +7¢ | KXHIGHTSFO-26NOV21-B57.5 | 57° to 58° | NO | 38¢ | 31% | 55% | $0 | center 57.9, market mean 57.91, lead 1d |
| +6¢ | KXHIGHTATL-26NOV21-B65.5 | 65° to 66° | YES | 6¢ | 19% | 12% | $0 | center 61.65, market mean 63.78, lead 0d |
| +6¢ | KXHIGHTLV-26NOV21-B58.5 | 58° to 59° | NO | 46¢ | 27% | 48% | $0 | center 57.15, market mean 57.61, lead 1d |
| +6¢ | KXHIGHTATL-26NOV21-T65 | 64° or below | NO | 7¢ | 65% | 87% | $0 | center 61.65, market mean 63.78, lead 0d |
| +6¢ | KXHIGHTPHX-26NOV21-B69.5 | 69° to 70° | NO | 50¢ | 23% | 44% | $0 | center 67.55, market mean 68.58, lead 1d |
| +6¢ | KXHIGHPHIL-26NOV21-B67.5 | 67° to 68° | NO | 42¢ | 30% | 52% | $0 | center 66.0, market mean 66.94, lead 0d |
| +6¢ | KXHIGHNY-26NOV21-T65 | 66° or above | YES | 7¢ | 21% | 13% | $0 | center 63.85, market mean 63.56, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV21-T71 | 70° or below | YES | 2¢ | 15% | 8% | $0 | center 74.0, market mean 74.02, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV21-B63.5 | 63° to 64° | YES | 6¢ | 18% | 12% | $0 | center 66.0, market mean 66.94, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV21-B70.5 | 70° to 71° | YES | 19¢ | 31% | 25% | $0 | center 69.25, market mean 68.33, lead 0d |
| +6¢ | KXHIGHTDC-26NOV21-B65.5 | 65° to 66° | NO | 50¢ | 36% | 44% | $0 | center 66.0, market mean 66.09, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV21-B65.5 | 65° to 66° | YES | 25¢ | 37% | 31% | $0 | center 66.0, market mean 66.94, lead 0d |
| +6¢ | KXHIGHTHOU-26NOV21-B77.5 | 77° to 78° | NO | 37¢ | 37% | 57% | $0 | center 77.9, market mean 77.82, lead 0d |
| +5¢ | KXHIGHTNOLA-26NOV21-B71.5 | 71° to 72° | YES | 7¢ | 32% | 12% | $0 | center 74.0, market mean 74.02, lead 0d |
| +5¢ | KXHIGHTSEA-26NOV21-B48.5 | 48° to 49° | NO | 58¢ | 28% | 37% | $100 | center 49.7, market mean 48.6, lead 1d |
| +4¢ | KXHIGHTPHX-26NOV21-B67.5 | 67° to 68° | NO | 56¢ | 31% | 40% | $100 | center 67.55, market mean 68.58, lead 1d |
| +2¢ | KXHIGHTLV-26NOV21-B56.5 | 56° to 57° | NO | 60¢ | 30% | 38% | $100 | center 57.15, market mean 57.61, lead 1d |
| +2¢ | KXHIGHDEN-26NOV21-B42.5 | 42° to 43° | YES | 12¢ | 22% | 14% | $100 | center 44.95, market mean 45.93, lead 1d |
| +1¢ | KXHIGHTLV-26NOV21-B54.5 | 54° to 55° | YES | 9¢ | 18% | 10% | $100 | center 57.15, market mean 57.61, lead 1d |
| -1¢ | KXHIGHTSFO-26NOV21-B55.5 | 55° to 56° | YES | 15¢ | 20% | 14% | $100 | center 57.9, market mean 57.91, lead 1d |
| -6¢ | KXHIGHTSEA-26NOV21-B52.5 | 52° to 53° | YES | 16¢ | 17% | 10% | $100 | center 49.7, market mean 48.6, lead 1d |
