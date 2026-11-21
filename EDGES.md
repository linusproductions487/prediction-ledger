# Model vs. market

Scanned 2026-11-21 22:58 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXAAAGASW-26NOV23-3.6350 | Above 3.6350 | NO | 79¢ | 0% | 12% | $100 |  |
| +9¢ | KXHIGHMIA-26NOV22-B85.5 | 85° to 86° | NO | 49¢ | 31% | 42% | $100 | center 85.34, market mean 85.09, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV22-B59.5 | 59° to 60° | NO | 57¢ | 25% | 37% | $100 | center 60.49, market mean 60.1, lead 1d |
| +6¢ | KXHIGHPHIL-26NOV22-B65.5 | 65° to 66° | NO | 62¢ | 22% | 32% | $100 | center 64.44, market mean 64.24, lead 1d |
| +5¢ | KXAAAGASD-26NOV22-3.6450 | Above 3.6450 | NO | 87¢ | 0% | 8% | $100 |  |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +24¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 4¢ | 0% | 72% | $0 |  |
| +16¢ | KXHIGHTSEA-26NOV21-T46 | 45° or below | NO | 21¢ | 2% | 63% | $0 | center 49.6, market mean 44.99, lead 0d |
| +12¢ | KXHIGHLAX-26NOV21-B67.5 | 67° to 68° | NO | 3¢ | 44% | 84% | $0 | center 68.25, market mean 67.48, lead 0d |
| +11¢ | KXHIGHTSFO-26NOV21-B57.5 | 57° to 58° | NO | 8¢ | 47% | 81% | $0 | center 57.74, market mean 57.67, lead 0d |
| +10¢ | KXHIGHTSFO-26NOV21-B59.5 | 59° to 60° | YES | 8¢ | 28% | 18% | $0 | center 57.74, market mean 57.67, lead 0d |
| +9¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 3¢ | 58% | 88% | $0 |  |
| +8¢ | KXHIGHTSEA-26NOV21-B50.5 | 50° to 51° | YES | 2¢ | 36% | 10% | $0 | center 49.6, market mean 44.99, lead 0d |
| +7¢ | KXHIGHLAX-26NOV22-B67.5 | 67° to 68° | NO | 31¢ | 35% | 62% | $0 | center 67.44, market mean 67.8, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV22-B73.5 | 73° to 74° | NO | 31¢ | 34% | 62% | $0 | center 72.99, market mean 73.32, lead 1d |
| +7¢ | KXHIGHTSEA-26NOV21-B48.5 | 48° to 49° | YES | 3¢ | 34% | 10% | $0 | center 49.6, market mean 44.99, lead 0d |
| +7¢ | KXHIGHTDAL-26NOV22-T66 | 65° or below | YES | 14¢ | 42% | 21% | $0 | center 66.54, market mean 67.12, lead 1d |
| +6¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 47¢ | 26% | 46% | $0 |  |
| +6¢ | KXHIGHNY-26NOV22-T61 | 60° or below | NO | 47¢ | 27% | 47% | $0 | center 62.2, market mean 60.83, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV22-B66.5 | 66° to 67° | NO | 51¢ | 19% | 43% | $0 | center 66.54, market mean 67.12, lead 1d |
| +6¢ | KXHIGHTSFO-26NOV22-B55.5 | 55° to 56° | NO | 39¢ | 35% | 55% | $0 | center 56.2, market mean 55.92, lead 1d |
| +5¢ | KXHIGHTBOS-26NOV22-T62 | 61° or below | NO | 9¢ | 67% | 86% | $0 | center 60.2, market mean 60.89, lead 1d |
| +5¢ | KXHIGHTSEA-26NOV22-T47 | 46° or below | YES | 18¢ | 35% | 23% | $100 | center 47.45, market mean 48.43, lead 1d |
| +4¢ | KXHIGHTHOU-26NOV22-B81.5 | 81° to 82° | NO | 56¢ | 28% | 40% | $100 | center 80.44, market mean 81.23, lead 1d |
| +4¢ | KXHIGHTSEA-26NOV22-B49.5 | 49° to 50° | NO | 66¢ | 23% | 30% | $100 | center 47.45, market mean 48.43, lead 1d |
| +3¢ | KXHIGHLAX-26NOV22-B65.5 | 65° to 66° | YES | 13¢ | 24% | 16% | $100 | center 67.44, market mean 67.8, lead 1d |
| +3¢ | KXHIGHTATL-26NOV22-T65 | 64° or below | NO | 28¢ | 60% | 69% | $100 | center 63.3, market mean 64.18, lead 1d |
| +2¢ | KXHIGHCHI-26NOV22-B62.5 | 62° to 63° | YES | 9¢ | 19% | 11% | $100 | center 60.05, market mean 59.48, lead 1d |
| +2¢ | KXHIGHTBOS-26NOV22-B62.5 | 62° to 63° | YES | 11¢ | 21% | 13% | $100 | center 60.2, market mean 60.89, lead 1d |
| +2¢ | KXHIGHTSEA-26NOV22-B47.5 | 47° to 48° | NO | 60¢ | 31% | 38% | $100 | center 47.45, market mean 48.43, lead 1d |
| +2¢ | KXHIGHNY-26NOV22-B63.5 | 63° to 64° | YES | 17¢ | 26% | 19% | $100 | center 62.2, market mean 60.83, lead 1d |
| +2¢ | KXHIGHTLV-26NOV22-B56.5 | 56° to 57° | NO | 59¢ | 29% | 39% | $100 | center 57.95, market mean 57.63, lead 1d |
| +1¢ | KXHIGHAUS-26NOV22-B73.5 | 73° to 74° | NO | 60¢ | 31% | 39% | $100 | center 73.09, market mean 73.62, lead 1d |
| +1¢ | KXHIGHTDAL-26NOV22-B68.5 | 68° to 69° | NO | 76¢ | 16% | 23% | $100 | center 66.54, market mean 67.12, lead 1d |
| +1¢ | KXHIGHCHI-26NOV22-B60.5 | 60° to 61° | NO | 59¢ | 34% | 40% | $100 | center 60.05, market mean 59.48, lead 1d |
| +1¢ | KXHIGHTSATX-26NOV22-T71 | 70° or below | YES | 20¢ | 32% | 21% | $100 | center 71.59, market mean 73.43, lead 1d |
| +1¢ | KXHIGHDEN-26NOV22-B45.5 | 45° to 46° | NO | 65¢ | 28% | 34% | $100 | center 46.45, market mean 45.66, lead 1d |
| +0¢ | KXHIGHDEN-26NOV22-T48 | 49° or above | YES | 15¢ | 22% | 16% | $100 | center 46.45, market mean 45.66, lead 1d |
| -0¢ | KXHIGHTDC-26NOV22-B66.5 | 66° to 67° | NO | 74¢ | 20% | 26% | $100 | center 64.99, market mean 65.25, lead 1d |
| -0¢ | KXHIGHTMIN-26NOV22-B41.5 | 41° to 42° | YES | 12¢ | 19% | 12% | $100 | center 44.1, market mean 44.28, lead 1d |
| -0¢ | KXHIGHNY-26NOV22-B65.5 | 65° to 66° | YES | 8¢ | 14% | 8% | $100 | center 62.2, market mean 60.83, lead 1d |
| -0¢ | KXHIGHTSATX-26NOV22-B73.5 | 73° to 74° | NO | 67¢ | 25% | 33% | $100 | center 71.59, market mean 73.43, lead 1d |
| -0¢ | KXHIGHTPHX-26NOV22-B75.5 | 75° to 76° | YES | 15¢ | 21% | 15% | $100 | center 72.99, market mean 73.32, lead 1d |
| -0¢ | KXHIGHTDC-26NOV22-T62 | 61° or below | YES | 12¢ | 18% | 12% | $100 | center 64.99, market mean 65.25, lead 1d |
| -0¢ | KXHIGHTLV-26NOV22-B60.5 | 60° to 61° | YES | 12¢ | 19% | 12% | $100 | center 57.95, market mean 57.63, lead 1d |
| -0¢ | KXHIGHTNOLA-26NOV22-B76.5 | 76° to 77° | NO | 68¢ | 22% | 32% | $100 | center 77.09, market mean 76.07, lead 1d |
