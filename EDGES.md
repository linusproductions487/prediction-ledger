# Model vs. market

Scanned 2026-11-24 09:48 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 5¢ | 72% | 84% | $100 |  |
| +11¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 27¢ | 50% | 62% | $100 |  |
| +11¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 28¢ | 50% | 61% | $100 |  |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXHIGHPHIL-26NOV24-B53.5 | 53° to 54° | NO | 4¢ | 50% | 85% | $0 | center 53.88, market mean 53.51, lead 0d |
| +10¢ | KXHIGHTPHX-26NOV24-B74.5 | 74° to 75° | NO | 43¢ | 37% | 47% | $0 | center 74.28, market mean 74.4, lead 0d |
| +9¢ | KXHIGHLAX-26NOV24-B74.5 | 74° to 75° | NO | 52¢ | 29% | 39% | $0 | center 72.93, market mean 73.65, lead 0d |
| +9¢ | KXHIGHTLV-26NOV24-B59.5 | 59° to 60° | YES | 7¢ | 26% | 16% | $0 | center 61.28, market mean 61.82, lead 0d |
| +9¢ | KXHIGHDEN-26NOV24-B50.5 | 50° to 51° | NO | 45¢ | 37% | 46% | $0 | center 51.13, market mean 50.97, lead 0d |
| +9¢ | KXHIGHTHOU-26NOV24-T59 | 58° or below | NO | 27¢ | 36% | 64% | $0 | center 59.13, market mean 58.29, lead 0d |
| +9¢ | KXHIGHCHI-26NOV24-T40 | 39° or below | YES | 8¢ | 26% | 17% | $0 | center 40.78, market mean 41.29, lead 0d |
| +9¢ | KXHIGHMIA-26NOV24-B81.5 | 81° to 82° | NO | 55¢ | 27% | 36% | $0 | center 81.13, market mean 80.38, lead 0d |
| +9¢ | KXHIGHTSFO-26NOV24-B62.5 | 62° to 63° | NO | 50¢ | 30% | 41% | $0 | center 63.93, market mean 61.97, lead 0d |
| +8¢ | KXHIGHTSEA-26NOV24-B50.5 | 50° to 51° | YES | 7¢ | 24% | 15% | $0 | center 52.13, market mean 53.92, lead 0d |
| +8¢ | KXHIGHPHIL-26NOV24-B55.5 | 55° to 56° | YES | 3¢ | 37% | 11% | $0 | center 53.88, market mean 53.51, lead 0d |
| +8¢ | KXHIGHTOKC-26NOV24-B45.5 | 45° to 46° | YES | 2¢ | 19% | 10% | $0 | center 43.13, market mean 42.12, lead 0d |
| +8¢ | KXHIGHTLV-26NOV24-B61.5 | 61° to 62° | NO | 28¢ | 38% | 64% | $0 | center 61.28, market mean 61.82, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV24-B51.5 | 51° to 52° | YES | 4¢ | 21% | 12% | $0 | center 54.13, market mean 54.72, lead 0d |
| +8¢ | KXHIGHAUS-26NOV24-B53.5 | 53° to 54° | NO | 44¢ | 39% | 48% | $0 | center 53.88, market mean 53.83, lead 0d |
| +8¢ | KXHIGHTHOU-26NOV24-B61.5 | 61° to 62° | YES | 4¢ | 21% | 12% | $0 | center 59.13, market mean 58.29, lead 0d |
| +8¢ | KXHIGHTNOLA-26NOV24-T62 | 61° or below | NO | 6¢ | 57% | 86% | $0 | center 61.28, market mean 60.78, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV24-B66.5 | 66° to 67° | YES | 2¢ | 18% | 10% | $0 | center 63.93, market mean 61.97, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV24-B48.5 | 48° to 49° | NO | 50¢ | 33% | 42% | $0 | center 49.93, market mean 48.95, lead 0d |
| +7¢ | KXHIGHCHI-26NOV24-B40.5 | 40° to 41° | NO | 46¢ | 38% | 47% | $0 | center 40.78, market mean 41.29, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV24-T50 | 51° or above | YES | 2¢ | 17% | 9% | $0 | center 46.43, market mean 48.38, lead 0d |
| +7¢ | KXHIGHTSEA-26NOV24-B54.5 | 54° to 55° | NO | 48¢ | 21% | 45% | $0 | center 52.13, market mean 53.92, lead 0d |
| +7¢ | KXHIGHMIA-26NOV24-B83.5 | 83° to 84° | YES | 5¢ | 20% | 12% | $0 | center 81.13, market mean 80.38, lead 0d |
| +7¢ | KXHIGHTATL-26NOV24-T61 | 60° or below | YES | 31¢ | 61% | 38% | $0 | center 60.13, market mean 61.35, lead 0d |
| +7¢ | KXHIGHNY-26NOV24-B53.5 | 53° to 54° | YES | 2¢ | 17% | 9% | $0 | center 50.48, market mean 50.69, lead 0d |
| +7¢ | KXHIGHTMIN-26NOV24-B32.5 | 32° to 33° | NO | 44¢ | 27% | 49% | $0 | center 34.13, market mean 33.47, lead 0d |
| +7¢ | KXHIGHMIA-26NOV24-B79.5 | 79° to 80° | NO | 62¢ | 22% | 31% | $0 | center 81.13, market mean 80.38, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV24-B55.5 | 55° to 56° | NO | 53¢ | 33% | 40% | $0 | center 54.13, market mean 54.72, lead 0d |
| +7¢ | KXHIGHTSFO-26NOV24-B64.5 | 64° to 65° | YES | 9¢ | 37% | 16% | $0 | center 63.93, market mean 61.97, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV24-B36.5 | 36° to 37° | YES | 7¢ | 20% | 14% | $0 | center 34.13, market mean 33.47, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV24-B62.5 | 62° to 63° | YES | 2¢ | 29% | 8% | $0 | center 61.28, market mean 60.78, lead 0d |
| +6¢ | KXHIGHLAX-26NOV24-B70.5 | 70° to 71° | YES | 7¢ | 20% | 13% | $0 | center 72.93, market mean 73.65, lead 0d |
| +6¢ | KXHIGHTHOU-26NOV24-B59.5 | 59° to 60° | YES | 26¢ | 39% | 32% | $0 | center 59.13, market mean 58.29, lead 0d |
| +6¢ | KXHIGHTSFO-26NOV24-B60.5 | 60° to 61° | NO | 64¢ | 10% | 30% | $0 | center 63.93, market mean 61.97, lead 0d |
| +6¢ | KXHIGHTDC-26NOV24-B52.5 | 52° to 53° | NO | 26¢ | 45% | 68% | $0 | center 52.53, market mean 52.82, lead 0d |
| +6¢ | KXHIGHNY-26NOV24-B51.5 | 51° to 52° | NO | 47¢ | 41% | 47% | $0 | center 50.48, market mean 50.69, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV24-B41.5 | 41° to 42° | NO | 47¢ | 28% | 47% | $0 | center 43.13, market mean 42.12, lead 0d |
| +6¢ | KXHIGHTATL-26NOV24-B61.5 | 61° to 62° | NO | 50¢ | 24% | 44% | $0 | center 60.13, market mean 61.35, lead 0d |
| +5¢ | KXHIGHTDAL-26NOV24-B50.5 | 50° to 51° | YES | 27¢ | 38% | 32% | $0 | center 49.93, market mean 48.95, lead 0d |
