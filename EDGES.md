# Model vs. market

Scanned 2026-11-23 21:37 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +12¢ | KXAAAGASW-26NOV30-3.5600 | Above 3.5600 | YES | 9¢ | 33% | 21% | $100 |  |
| +9¢ | KXHIGHTATL-26NOV24-T61 | 60° or below | YES | 31¢ | 52% | 40% | $100 | center 60.68, market mean 61.59, lead 1d |
| +7¢ | KXAAAGASW-26NOV30-3.5800 | Above 3.5800 | YES | 3¢ | 18% | 10% | $100 |  |
| +6¢ | KXHIGHNY-26NOV24-B51.5 | 51° to 52° | NO | 62¢ | 24% | 32% | $100 | center 49.73, market mean 50.34, lead 1d |
| +5¢ | KXHIGHLAX-26NOV24-B70.5 | 70° to 71° | YES | 10¢ | 25% | 15% | $100 | center 72.38, market mean 73.18, lead 1d |
| +5¢ | KXHIGHLAX-26NOV24-B72.5 | 72° to 73° | NO | 51¢ | 37% | 44% | $100 | center 72.38, market mean 73.18, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +16¢ | KXHIGHTOKC-26NOV23-B50.5 | 50° to 51° | NO | 2¢ | 32% | 82% | $0 | center 51.8, market mean 50.56, lead 0d |
| +15¢ | KXHIGHTNOLA-26NOV23-T70 | 69° or below | NO | 2¢ | 35% | 83% | $0 | center 71.18, market mean 68.68, lead 0d |
| +15¢ | KXHIGHLAX-26NOV23-B67.5 | 67° to 68° | NO | 5¢ | 33% | 80% | $0 | center 68.83, market mean 67.59, lead 0d |
| +13¢ | KXHIGHTBOS-26NOV23-B68.5 | 68° to 69° | NO | 12¢ | 27% | 75% | $0 | center 69.8, market mean 68.57, lead 0d |
| +13¢ | KXAAAGASD-26NOV24-3.6200 | Above 3.6200 | YES | 5¢ | 58% | 18% | $0 |  |
| +12¢ | KXHIGHTBOS-26NOV23-T69 | 70° or above | YES | 12¢ | 73% | 25% | $0 | center 69.8, market mean 68.57, lead 0d |
| +12¢ | KXHIGHAUS-26NOV23-B61.5 | 61° to 62° | NO | 2¢ | 48% | 86% | $0 | center 61.63, market mean 61.62, lead 0d |
| +12¢ | KXHIGHTMIN-26NOV23-B30.5 | 30° to 31° | NO | 5¢ | 43% | 83% | $0 | center 31.38, market mean 30.65, lead 0d |
| +11¢ | KXHIGHTLV-26NOV23-B59.5 | 59° to 60° | YES | 2¢ | 25% | 13% | $0 | center 60.68, market mean 61.6, lead 0d |
| +11¢ | KXHIGHTOKC-26NOV23-B52.5 | 52° to 53° | YES | 3¢ | 49% | 14% | $0 | center 51.8, market mean 50.56, lead 0d |
| +11¢ | KXHIGHTNOLA-26NOV23-B70.5 | 70° to 71° | YES | 3¢ | 25% | 14% | $0 | center 71.18, market mean 68.68, lead 0d |
| +10¢ | KXHIGHAUS-26NOV23-B63.5 | 63° to 64° | YES | 3¢ | 25% | 14% | $0 | center 61.63, market mean 61.62, lead 0d |
| +10¢ | KXHIGHTSFO-26NOV23-B59.5 | 59° to 60° | YES | 7¢ | 27% | 17% | $0 | center 57.88, market mean 56.67, lead 0d |
| +10¢ | KXHIGHTLV-26NOV23-B61.5 | 61° to 62° | NO | 8¢ | 49% | 82% | $0 | center 60.68, market mean 61.6, lead 0d |
| +9¢ | KXHIGHCHI-26NOV23-B42.5 | 42° to 43° | NO | 3¢ | 58% | 88% | $0 | center 43.03, market mean 42.55, lead 0d |
| +9¢ | KXHIGHPHIL-26NOV24-B53.5 | 53° to 54° | NO | 37¢ | 24% | 54% | $0 | center 51.48, market mean 53.09, lead 1d |
| +9¢ | KXHIGHTNOLA-26NOV24-T62 | 61° or below | NO | 21¢ | 35% | 70% | $0 | center 62.78, market mean 61.16, lead 1d |
| +9¢ | KXHIGHTLV-26NOV24-B61.5 | 61° to 62° | NO | 28¢ | 36% | 63% | $0 | center 61.13, market mean 61.96, lead 1d |
| +8¢ | KXHIGHCHI-26NOV23-B44.5 | 44° to 45° | YES | 2¢ | 37% | 10% | $0 | center 43.03, market mean 42.55, lead 0d |
| +8¢ | KXHIGHLAX-26NOV23-B69.5 | 69° to 70° | YES | 4¢ | 38% | 12% | $0 | center 68.83, market mean 67.59, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV24-B74.5 | 74° to 75° | NO | 30¢ | 36% | 62% | $0 | center 74.13, market mean 74.81, lead 1d |
| +8¢ | KXHIGHTHOU-26NOV23-T68 | 67° or below | NO | 2¢ | 64% | 90% | $0 | center 66.18, market mean 66.65, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV24-B49.5 | 49° to 50° | NO | 52¢ | 14% | 40% | $0 | center 46.13, market mean 48.79, lead 1d |
| +7¢ | KXAAAGASW-26NOV30-3.5400 | Above 3.5400 | YES | 21¢ | 51% | 28% | $0 |  |
| +7¢ | KXHIGHTSEA-26NOV24-B54.5 | 54° to 55° | NO | 57¢ | 15% | 36% | $0 | center 51.13, market mean 53.54, lead 1d |
| +6¢ | KXHIGHTHOU-26NOV24-T59 | 58° or below | NO | 32¢ | 39% | 62% | $0 | center 59.28, market mean 58.48, lead 1d |
| +6¢ | KXHIGHTLV-26NOV23-B63.5 | 63° to 64° | YES | 7¢ | 22% | 13% | $0 | center 60.68, market mean 61.6, lead 0d |
| +6¢ | KXHIGHTATL-26NOV24-B61.5 | 61° to 62° | NO | 50¢ | 23% | 44% | $0 | center 60.68, market mean 61.59, lead 1d |
| +6¢ | KXAAAGASW-26NOV30-3.5200 | Above 3.5200 | YES | 43¢ | 69% | 49% | $0 |  |
| +6¢ | KXAAAGASM-26NOV30-3.55 | Above 3.55 | YES | 14¢ | 42% | 20% | $0 |  |
| +6¢ | KXHIGHTSFO-26NOV23-B55.5 | 55° to 56° | NO | 64¢ | 22% | 30% | $0 | center 57.88, market mean 56.67, lead 0d |
| +6¢ | KXHIGHDEN-26NOV23-B42.5 | 42° to 43° | YES | 2¢ | 14% | 8% | $0 | center 39.2, market mean 39.85, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV24-B41.5 | 41° to 42° | NO | 47¢ | 28% | 47% | $0 | center 42.93, market mean 42.1, lead 1d |
| +6¢ | KXHIGHTSATX-26NOV24-B55.5 | 55° to 56° | NO | 46¢ | 28% | 48% | $0 | center 54.48, market mean 54.89, lead 1d |
| +5¢ | KXHIGHMIA-26NOV24-B79.5 | 79° to 80° | NO | 54¢ | 21% | 41% | $0 | center 81.33, market mean 79.67, lead 1d |
| +5¢ | KXHIGHTMIN-26NOV23-B32.5 | 32° to 33° | YES | 5¢ | 30% | 10% | $0 | center 31.38, market mean 30.65, lead 0d |
| +5¢ | KXHIGHNY-26NOV24-T49 | 48° or below | YES | 13¢ | 29% | 18% | $100 | center 49.73, market mean 50.34, lead 1d |
| +5¢ | KXHIGHLAX-26NOV24-B74.5 | 74° to 75° | NO | 64¢ | 23% | 31% | $100 | center 72.38, market mean 73.18, lead 1d |
| +4¢ | KXHIGHCHI-26NOV24-T40 | 39° or below | YES | 12¢ | 27% | 16% | $100 | center 40.68, market mean 41.48, lead 1d |
| +4¢ | KXHIGHTMIN-26NOV24-B32.5 | 32° to 33° | NO | 57¢ | 28% | 39% | $100 | center 34.13, market mean 33.67, lead 1d |
