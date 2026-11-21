# Model vs. market

Scanned 2026-11-21 21:41 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +8¢ | KXHIGHMIA-26NOV22-B85.5 | 85° to 86° | NO | 48¢ | 32% | 44% | $100 | center 85.34, market mean 85.08, lead 1d |
| +7¢ | KXHIGHNY-26NOV22-T61 | 60° or below | NO | 48¢ | 34% | 45% | $100 | center 61.7, market mean 60.76, lead 1d |
| +5¢ | KXHIGHTATL-26NOV22-T65 | 64° or below | NO | 29¢ | 55% | 66% | $100 | center 64.0, market mean 64.22, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +23¢ | KXHIGHTOKC-26NOV21-T68 | 67° or below | NO | 2¢ | 4% | 75% | $0 | center 70.29, market mean 66.67, lead 0d |
| +16¢ | KXHIGHCHI-26NOV21-B68.5 | 68° to 69° | NO | 6¢ | 25% | 78% | $0 | center 69.8, market mean 68.58, lead 0d |
| +14¢ | KXHIGHDEN-26NOV21-B46.5 | 46° to 47° | NO | 3¢ | 38% | 83% | $0 | center 46.4, market mean 46.51, lead 0d |
| +14¢ | KXHIGHLAX-26NOV21-B67.5 | 67° to 68° | NO | 3¢ | 42% | 84% | $0 | center 68.0, market mean 67.53, lead 0d |
| +12¢ | KXHIGHDEN-26NOV21-B48.5 | 48° to 49° | YES | 3¢ | 27% | 15% | $0 | center 46.4, market mean 46.51, lead 0d |
| +11¢ | KXHIGHTSFO-26NOV21-B57.5 | 57° to 58° | YES | 15¢ | 38% | 26% | $0 | center 57.95, market mean 55.79, lead 0d |
| +10¢ | KXHIGHCHI-26NOV21-B70.5 | 70° to 71° | YES | 4¢ | 49% | 15% | $0 | center 69.8, market mean 68.58, lead 0d |
| +10¢ | KXHIGHTPHX-26NOV21-B67.5 | 67° to 68° | NO | 12¢ | 39% | 78% | $0 | center 68.09, market mean 67.72, lead 0d |
| +10¢ | KXHIGHTSFO-26NOV21-B55.5 | 55° to 56° | NO | 30¢ | 19% | 60% | $0 | center 57.95, market mean 55.79, lead 0d |
| +9¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 4¢ | 58% | 87% | $0 |  |
| +9¢ | KXAAAGASW-26NOV23-3.6350 | Above 3.6350 | NO | 64¢ | 0% | 27% | $0 |  |
| +8¢ | KXHIGHTSEA-26NOV21-B48.5 | 48° to 49° | YES | 11¢ | 30% | 19% | $0 | center 49.6, market mean 45.83, lead 0d |
| +8¢ | KXHIGHTLV-26NOV21-B56.5 | 56° to 57° | NO | 49¢ | 32% | 43% | $0 | center 57.49, market mean 57.4, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV21-B74.5 | 74° to 75° | YES | 6¢ | 41% | 14% | $0 | center 73.84, market mean 72.03, lead 0d |
| +7¢ | KXHIGHLAX-26NOV22-B67.5 | 67° to 68° | NO | 33¢ | 35% | 60% | $0 | center 67.44, market mean 67.78, lead 1d |
| +7¢ | KXHIGHTDAL-26NOV22-T66 | 65° or below | YES | 14¢ | 44% | 21% | $0 | center 66.19, market mean 67.17, lead 1d |
| +7¢ | KXHIGHLAX-26NOV21-B69.5 | 69° to 70° | YES | 4¢ | 33% | 11% | $0 | center 68.0, market mean 67.53, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV22-T71 | 70° or below | YES | 12¢ | 41% | 19% | $0 | center 71.04, market mean 73.31, lead 1d |
| +7¢ | KXHIGHTSATX-26NOV21-B76.5 | 76° to 77° | YES | 2¢ | 16% | 9% | $0 | center 73.84, market mean 72.03, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV22-B73.5 | 73° to 74° | NO | 33¢ | 34% | 60% | $0 | center 72.99, market mean 73.3, lead 1d |
| +7¢ | KXAAAGASD-26NOV22-3.6450 | Above 3.6450 | NO | 66¢ | 0% | 27% | $0 |  |
| +6¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 47¢ | 26% | 46% | $0 |  |
| +6¢ | KXHIGHTSFO-26NOV22-B55.5 | 55° to 56° | NO | 39¢ | 34% | 55% | $0 | center 56.2, market mean 55.96, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV21-B68.5 | 68° to 69° | YES | 2¢ | 28% | 8% | $0 | center 70.29, market mean 66.67, lead 0d |
| +6¢ | KXHIGHTSFO-26NOV21-B59.5 | 59° to 60° | YES | 3¢ | 29% | 9% | $0 | center 57.95, market mean 55.79, lead 0d |
| +6¢ | KXHIGHTSEA-26NOV21-B46.5 | 46° to 47° | NO | 69¢ | 15% | 25% | $0 | center 49.6, market mean 45.83, lead 0d |
| +6¢ | KXHIGHTSEA-26NOV21-B50.5 | 50° to 51° | YES | 4¢ | 31% | 10% | $0 | center 49.6, market mean 45.83, lead 0d |
| +6¢ | KXHIGHTSEA-26NOV21-T46 | 45° or below | NO | 55¢ | 4% | 39% | $0 | center 49.6, market mean 45.83, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV22-T62 | 61° or below | NO | 9¢ | 66% | 85% | $0 | center 60.2, market mean 60.89, lead 1d |
| +5¢ | KXHIGHTDAL-26NOV22-B66.5 | 66° to 67° | NO | 51¢ | 21% | 44% | $0 | center 66.19, market mean 67.17, lead 1d |
| +5¢ | KXHIGHTPHX-26NOV21-B69.5 | 69° to 70° | YES | 9¢ | 35% | 14% | $0 | center 68.09, market mean 67.72, lead 0d |
| +4¢ | KXHIGHTSEA-26NOV22-T47 | 46° or below | YES | 18¢ | 33% | 22% | $100 | center 47.45, market mean 48.43, lead 1d |
| +3¢ | KXHIGHTLV-26NOV22-B56.5 | 56° to 57° | NO | 58¢ | 27% | 39% | $100 | center 57.95, market mean 57.55, lead 1d |
| +3¢ | KXHIGHCHI-26NOV22-B60.5 | 60° to 61° | NO | 55¢ | 34% | 42% | $100 | center 60.05, market mean 59.56, lead 1d |
| +2¢ | KXHIGHLAX-26NOV22-B65.5 | 65° to 66° | YES | 15¢ | 24% | 17% | $100 | center 67.44, market mean 67.78, lead 1d |
| +2¢ | KXHIGHTSEA-26NOV22-B47.5 | 47° to 48° | NO | 59¢ | 33% | 39% | $100 | center 47.45, market mean 48.43, lead 1d |
| +2¢ | KXHIGHAUS-26NOV22-B73.5 | 73° to 74° | NO | 60¢ | 30% | 38% | $100 | center 73.59, market mean 73.68, lead 1d |
| +1¢ | KXHIGHCHI-26NOV22-B62.5 | 62° to 63° | YES | 11¢ | 20% | 12% | $100 | center 60.05, market mean 59.56, lead 1d |
| +1¢ | KXHIGHTHOU-26NOV22-B79.5 | 79° to 80° | YES | 25¢ | 35% | 26% | $100 | center 80.44, market mean 81.44, lead 1d |
| +1¢ | KXHIGHTNOLA-26NOV22-B76.5 | 76° to 77° | NO | 66¢ | 22% | 33% | $100 | center 77.29, market mean 75.89, lead 1d |
