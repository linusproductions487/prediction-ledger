# Model vs. market

Scanned 2026-11-27 08:19 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| – | none this scan | | | | | | | |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +20¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 2¢ | 15% | 78% | $0 |  |
| +16¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 31¢ | 2% | 53% | $0 |  |
| +16¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 30¢ | 2% | 54% | $0 |  |
| +12¢ | KXHIGHTDC-26NOV27-B54.5 | 54° to 55° | NO | 30¢ | 21% | 58% | $0 | center 56.69, market mean 55.2, lead 0d |
| +11¢ | KXHIGHTSEA-26NOV27-B48.5 | 48° to 49° | YES | 11¢ | 33% | 22% | $0 | center 49.74, market mean 50.7, lead 0d |
| +11¢ | KXHIGHTATL-26NOV27-B49.5 | 49° to 50° | NO | 56¢ | 22% | 33% | $0 | center 51.14, market mean 49.99, lead 0d |
| +10¢ | KXHIGHAUS-26NOV27-B70.5 | 70° to 71° | NO | 52¢ | 27% | 38% | $0 | center 68.69, market mean 69.47, lead 0d |
| +10¢ | KXHIGHTBOS-26NOV27-B60.5 | 60° to 61° | YES | 12¢ | 32% | 22% | $0 | center 59.24, market mean 58.12, lead 0d |
| +10¢ | KXHIGHTSATX-26NOV27-T68 | 69° or above | YES | 5¢ | 25% | 15% | $0 | center 67.14, market mean 66.94, lead 0d |
| +10¢ | KXHIGHTHOU-26NOV27-B62.5 | 62° to 63° | YES | 4¢ | 24% | 14% | $0 | center 63.84, market mean 65.83, lead 0d |
| +10¢ | KXHIGHTOKC-26NOV27-B60.5 | 60° to 61° | YES | 14¢ | 36% | 24% | $0 | center 60.04, market mean 62.83, lead 0d |
| +9¢ | KXHIGHTDAL-26NOV27-B69.5 | 69° to 70° | NO | 43¢ | 18% | 48% | $0 | center 66.94, market mean 68.89, lead 0d |
| +9¢ | KXHIGHTLV-26NOV27-B70.5 | 70° to 71° | NO | 52¢ | 29% | 39% | $0 | center 69.14, market mean 69.55, lead 0d |
| +9¢ | KXHIGHCHI-26NOV27-B47.5 | 47° to 48° | NO | 52¢ | 29% | 39% | $0 | center 46.14, market mean 46.85, lead 0d |
| +9¢ | KXHIGHAUS-26NOV27-B66.5 | 66° to 67° | YES | 3¢ | 21% | 12% | $0 | center 68.69, market mean 69.47, lead 0d |
| +9¢ | KXHIGHTMIN-26NOV27-B40.5 | 40° to 41° | YES | 10¢ | 29% | 19% | $0 | center 42.04, market mean 43.12, lead 0d |
| +8¢ | KXHIGHLAX-26NOV27-B83.5 | 83° to 84° | NO | 64¢ | 19% | 28% | $0 | center 83.34, market mean 82.77, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV27-T58 | 57° or below | NO | 64¢ | 19% | 28% | $0 | center 59.24, market mean 58.12, lead 0d |
| +8¢ | KXHIGHTNOLA-26NOV27-B58.5 | 58° to 59° | NO | 58¢ | 25% | 34% | $0 | center 56.89, market mean 57.37, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV27-B77.5 | 77° to 78° | NO | 33¢ | 33% | 59% | $0 | center 77.09, market mean 78.08, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV27-B42.5 | 42° to 43° | NO | 46¢ | 37% | 46% | $0 | center 42.04, market mean 43.12, lead 0d |
| +8¢ | KXHIGHLAX-26NOV27-T84 | 85° or above | YES | 22¢ | 39% | 30% | $0 | center 83.34, market mean 82.77, lead 0d |
| +8¢ | KXHIGHTSEA-26NOV27-B50.5 | 50° to 51° | NO | 31¢ | 35% | 61% | $0 | center 49.74, market mean 50.7, lead 0d |
| +8¢ | KXHIGHNY-26NOV27-B57.5 | 57° to 58° | NO | 31¢ | 37% | 61% | $0 | center 57.54, market mean 57.06, lead 0d |
| +8¢ | KXHIGHTOKC-26NOV27-B62.5 | 62° to 63° | NO | 50¢ | 18% | 42% | $0 | center 60.04, market mean 62.83, lead 0d |
| +7¢ | KXHIGHPHIL-26NOV27-B59.5 | 59° to 60° | NO | 11¢ | 49% | 82% | $0 | center 58.19, market mean 59.59, lead 0d |
| +7¢ | KXHIGHMIA-26NOV27-B74.5 | 74° to 75° | NO | 39¢ | 32% | 54% | $0 | center 73.99, market mean 74.62, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV27-B58.5 | 58° to 59° | YES | 3¢ | 32% | 10% | $0 | center 60.04, market mean 62.83, lead 0d |
| +7¢ | KXHIGHTLV-26NOV27-B66.5 | 66° to 67° | YES | 4¢ | 18% | 11% | $0 | center 69.14, market mean 69.55, lead 0d |
| +7¢ | KXHIGHTDC-26NOV27-B58.5 | 58° to 59° | YES | 3¢ | 31% | 10% | $0 | center 56.69, market mean 55.2, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV27-B61.5 | 61° to 62° | YES | 4¢ | 17% | 10% | $0 | center 58.19, market mean 59.59, lead 0d |
| +6¢ | KXHIGHLAX-26NOV27-B81.5 | 81° to 82° | NO | 69¢ | 18% | 25% | $0 | center 83.34, market mean 82.77, lead 0d |
| +6¢ | KXHIGHTHOU-26NOV27-B60.5 | 60° to 61° | YES | 2¢ | 15% | 8% | $0 | center 63.84, market mean 65.83, lead 0d |
| +6¢ | KXHIGHTPHX-26NOV27-B75.5 | 75° to 76° | YES | 3¢ | 30% | 9% | $0 | center 77.09, market mean 78.08, lead 0d |
| +6¢ | KXHIGHMIA-26NOV27-B72.5 | 72° to 73° | YES | 15¢ | 28% | 21% | $0 | center 73.99, market mean 74.62, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV27-B54.5 | 54° to 55° | YES | 7¢ | 20% | 13% | $0 | center 56.89, market mean 57.37, lead 0d |
| +6¢ | KXHIGHNY-26NOV27-B59.5 | 59° to 60° | YES | 2¢ | 28% | 8% | $0 | center 57.54, market mean 57.06, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV27-B65.5 | 65° to 66° | YES | 3¢ | 30% | 9% | $0 | center 66.94, market mean 68.89, lead 0d |
| +6¢ | KXHIGHCHI-26NOV27-B43.5 | 43° to 44° | YES | 5¢ | 18% | 11% | $0 | center 46.14, market mean 46.85, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV27-B67.5 | 67° to 68° | NO | 31¢ | 38% | 63% | $0 | center 67.14, market mean 66.94, lead 0d |
