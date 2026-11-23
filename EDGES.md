# Model vs. market

Scanned 2026-11-23 23:48 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +7¢ | KXAAAGASW-26NOV30-3.5800 | Above 3.5800 | YES | 3¢ | 18% | 10% | $100 |  |
| +6¢ | KXHIGHNY-26NOV24-T49 | 48° or below | YES | 13¢ | 30% | 19% | $100 | center 49.63, market mean 50.31, lead 1d |
| +6¢ | KXHIGHLAX-26NOV24-B74.5 | 74° to 75° | NO | 61¢ | 23% | 33% | $100 | center 72.38, market mean 73.2, lead 1d |
| +6¢ | KXHIGHTDC-26NOV24-B54.5 | 54° to 55° | NO | 63¢ | 23% | 31% | $100 | center 52.43, market mean 53.44, lead 1d |
| +6¢ | KXHIGHTATL-26NOV24-T61 | 60° or below | YES | 31¢ | 48% | 37% | $100 | center 60.68, market mean 61.66, lead 1d |
| +6¢ | KXHIGHMIA-26NOV24-B79.5 | 79° to 80° | NO | 57¢ | 27% | 37% | $100 | center 80.48, market mean 79.65, lead 1d |
| +6¢ | KXHIGHLAX-26NOV24-B70.5 | 70° to 71° | YES | 10¢ | 25% | 16% | $100 | center 72.38, market mean 73.2, lead 1d |
| +5¢ | KXHIGHTPHX-26NOV24-B72.5 | 72° to 73° | YES | 12¢ | 28% | 17% | $100 | center 74.03, market mean 74.82, lead 1d |
| +5¢ | KXHIGHNY-26NOV24-B51.5 | 51° to 52° | NO | 62¢ | 24% | 33% | $100 | center 49.63, market mean 50.31, lead 1d |
| +5¢ | KXHIGHTOKC-26NOV24-B41.5 | 41° to 42° | NO | 53¢ | 30% | 42% | $100 | center 42.93, market mean 42.15, lead 1d |
| +5¢ | KXHIGHTMIN-26NOV24-B32.5 | 32° to 33° | NO | 56¢ | 28% | 39% | $100 | center 34.13, market mean 33.61, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +14¢ | KXAAAGASD-26NOV24-3.6200 | Above 3.6200 | YES | 2¢ | 58% | 16% | $0 |  |
| +13¢ | KXAAAGASD-26NOV24-3.6150 | Above 3.6150 | YES | 35¢ | 93% | 48% | $0 |  |
| +11¢ | KXHIGHTSFO-26NOV23-B55.5 | 55° to 56° | NO | 22¢ | 21% | 67% | $0 | center 57.88, market mean 55.91, lead 0d |
| +10¢ | KXHIGHTBOS-26NOV24-B49.5 | 49° to 50° | NO | 46¢ | 14% | 44% | $0 | center 46.28, market mean 48.75, lead 1d |
| +9¢ | KXHIGHTPHX-26NOV24-B74.5 | 74° to 75° | NO | 28¢ | 35% | 63% | $0 | center 74.03, market mean 74.82, lead 1d |
| +9¢ | KXHIGHTLV-26NOV24-B61.5 | 61° to 62° | NO | 22¢ | 36% | 69% | $0 | center 61.13, market mean 61.84, lead 1d |
| +9¢ | KXHIGHTNOLA-26NOV24-T62 | 61° or below | NO | 20¢ | 43% | 71% | $0 | center 62.23, market mean 61.17, lead 1d |
| +8¢ | KXHIGHTSEA-26NOV23-B53.5 | 53° to 54° | NO | 2¢ | 64% | 90% | $0 | center 53.6, market mean 53.42, lead 0d |
| +8¢ | KXAAAGASW-26NOV30-3.5400 | Above 3.5400 | YES | 19¢ | 51% | 27% | $0 |  |
| +8¢ | KXHIGHPHIL-26NOV24-B53.5 | 53° to 54° | NO | 39¢ | 29% | 53% | $0 | center 52.18, market mean 53.22, lead 1d |
| +8¢ | KXHIGHTSFO-26NOV23-B57.5 | 57° to 58° | YES | 18¢ | 37% | 26% | $0 | center 57.88, market mean 55.91, lead 0d |
| +7¢ | KXAAAGASM-26NOV30-3.55 | Above 3.55 | YES | 13¢ | 42% | 20% | $0 |  |
| +7¢ | KXAAAGASW-26NOV30-3.5200 | Above 3.5200 | YES | 41¢ | 69% | 48% | $0 |  |
| +6¢ | KXHIGHTSEA-26NOV24-B54.5 | 54° to 55° | NO | 57¢ | 16% | 37% | $0 | center 51.13, market mean 53.43, lead 1d |
| +6¢ | KXAAAGASW-26NOV30-3.5600 | Above 3.5600 | YES | 6¢ | 33% | 12% | $0 |  |
| +6¢ | KXHIGHTSFO-26NOV23-B59.5 | 59° to 60° | YES | 2¢ | 28% | 8% | $0 | center 57.88, market mean 55.91, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV24-B55.5 | 55° to 56° | NO | 46¢ | 27% | 48% | $0 | center 54.43, market mean 54.85, lead 1d |
| +6¢ | KXHIGHTDC-26NOV24-T52 | 51° or below | YES | 6¢ | 33% | 12% | $0 | center 52.43, market mean 53.44, lead 1d |
| +5¢ | KXHIGHTHOU-26NOV24-T59 | 58° or below | NO | 30¢ | 44% | 65% | $0 | center 59.08, market mean 58.37, lead 1d |
| +5¢ | KXHIGHNY-26NOV24-B49.5 | 49° to 50° | NO | 52¢ | 36% | 43% | $100 | center 49.63, market mean 50.31, lead 1d |
| +4¢ | KXHIGHTLV-26NOV24-B59.5 | 59° to 60° | YES | 11¢ | 28% | 15% | $100 | center 61.13, market mean 61.84, lead 1d |
| +4¢ | KXHIGHTBOS-26NOV24-B45.5 | 45° to 46° | YES | 12¢ | 28% | 16% | $100 | center 46.28, market mean 48.75, lead 1d |
| +4¢ | KXHIGHDEN-26NOV24-B50.5 | 50° to 51° | NO | 49¢ | 37% | 47% | $100 | center 50.68, market mean 50.91, lead 1d |
| +4¢ | KXHIGHLAX-26NOV24-B72.5 | 72° to 73° | NO | 53¢ | 37% | 44% | $100 | center 72.38, market mean 73.2, lead 1d |
| +3¢ | KXHIGHAUS-26NOV24-B53.5 | 53° to 54° | NO | 49¢ | 38% | 48% | $100 | center 53.13, market mean 53.47, lead 1d |
| +3¢ | KXHIGHCHI-26NOV24-B42.5 | 42° to 43° | NO | 58¢ | 32% | 39% | $100 | center 41.23, market mean 41.57, lead 1d |
| +3¢ | KXHIGHTSFO-26NOV24-B60.5 | 60° to 61° | NO | 72¢ | 18% | 25% | $100 | center 63.08, market mean 62.21, lead 1d |
| +3¢ | KXHIGHTATL-26NOV24-B61.5 | 61° to 62° | NO | 58¢ | 31% | 39% | $100 | center 60.68, market mean 61.66, lead 1d |
| +2¢ | KXHIGHTSFO-26NOV24-B64.5 | 64° to 65° | YES | 19¢ | 30% | 21% | $100 | center 63.08, market mean 62.21, lead 1d |
| +2¢ | KXHIGHTDC-26NOV24-B52.5 | 52° to 53° | NO | 53¢ | 38% | 45% | $100 | center 52.43, market mean 53.44, lead 1d |
| +2¢ | KXHIGHCHI-26NOV24-T40 | 39° or below | YES | 11¢ | 20% | 13% | $100 | center 41.23, market mean 41.57, lead 1d |
| +1¢ | KXHIGHCHI-26NOV24-B40.5 | 40° to 41° | NO | 58¢ | 35% | 41% | $100 | center 41.23, market mean 41.57, lead 1d |
| +1¢ | KXHIGHTBOS-26NOV24-B43.5 | 43° to 44° | YES | 9¢ | 18% | 10% | $100 | center 46.28, market mean 48.75, lead 1d |
| +1¢ | KXHIGHTSFO-26NOV24-B62.5 | 62° to 63° | NO | 56¢ | 35% | 43% | $100 | center 63.08, market mean 62.21, lead 1d |
| +0¢ | KXHIGHTDAL-26NOV24-B48.5 | 48° to 49° | NO | 59¢ | 35% | 41% | $100 | center 49.63, market mean 49.42, lead 1d |
| +0¢ | KXHIGHPHIL-26NOV24-B49.5 | 49° to 50° | YES | 10¢ | 18% | 10% | $100 | center 52.18, market mean 53.22, lead 1d |
| +0¢ | KXHIGHMIA-26NOV24-B83.5 | 83° to 84° | YES | 11¢ | 17% | 11% | $100 | center 80.48, market mean 79.65, lead 1d |
| -0¢ | KXHIGHTSEA-26NOV24-B50.5 | 50° to 51° | YES | 16¢ | 24% | 16% | $100 | center 51.13, market mean 53.43, lead 1d |
| -0¢ | KXHIGHAUS-26NOV24-B51.5 | 51° to 52° | YES | 24¢ | 30% | 24% | $100 | center 53.13, market mean 53.47, lead 1d |
| -1¢ | KXHIGHTSEA-26NOV24-B48.5 | 48° to 49° | YES | 10¢ | 16% | 9% | $100 | center 51.13, market mean 53.43, lead 1d |
