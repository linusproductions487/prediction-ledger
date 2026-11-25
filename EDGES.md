# Model vs. market

Scanned 2026-11-25 08:23 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +8¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 2¢ | 82% | 90% | $100 |  |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +12¢ | KXHIGHTDAL-26NOV25-T53 | 52° or below | YES | 13¢ | 65% | 25% | $0 | center 52.15, market mean 53.88, lead 0d |
| +12¢ | KXHIGHNY-26NOV25-T47 | 46° or below | NO | 35¢ | 41% | 53% | $0 | center 47.1, market mean 46.42, lead 0d |
| +11¢ | KXHIGHTBOS-26NOV25-B44.5 | 44° to 45° | NO | 39¢ | 38% | 50% | $0 | center 44.35, market mean 44.0, lead 0d |
| +11¢ | KXHIGHTNOLA-26NOV25-B55.5 | 55° to 56° | NO | 21¢ | 33% | 68% | $0 | center 56.85, market mean 56.07, lead 0d |
| +11¢ | KXHIGHLAX-26NOV25-B74.5 | 74° to 75° | NO | 41¢ | 37% | 48% | $0 | center 75.1, market mean 74.74, lead 0d |
| +11¢ | KXHIGHTPHX-26NOV25-B76.5 | 76° to 77° | NO | 38¢ | 17% | 51% | $0 | center 76.85, market mean 76.99, lead 0d |
| +11¢ | KXHIGHDEN-26NOV25-B49.5 | 49° to 50° | NO | 46¢ | 32% | 43% | $0 | center 48.7, market mean 50.06, lead 0d |
| +11¢ | KXHIGHTLV-26NOV25-T61 | 60° or below | YES | 2¢ | 24% | 13% | $0 | center 62.0, market mean 63.36, lead 0d |
| +10¢ | KXHIGHTLV-26NOV25-B63.5 | 63° to 64° | NO | 28¢ | 29% | 62% | $0 | center 62.0, market mean 63.36, lead 0d |
| +10¢ | KXHIGHTHOU-26NOV25-B59.5 | 59° to 60° | NO | 34¢ | 23% | 56% | $0 | center 58.1, market mean 59.89, lead 0d |
| +10¢ | KXHIGHTATL-26NOV25-B56.5 | 56° to 57° | YES | 7¢ | 28% | 17% | $0 | center 52.25, market mean 54.57, lead 0d |
| +9¢ | KXHIGHTSATX-26NOV25-B59.5 | 59° to 60° | NO | 46¢ | 34% | 45% | $0 | center 58.25, market mean 60.18, lead 0d |
| +9¢ | KXHIGHTHOU-26NOV25-T57 | 56° or below | YES | 2¢ | 21% | 11% | $0 | center 58.1, market mean 59.89, lead 0d |
| +9¢ | KXHIGHTDC-26NOV25-T53 | 52° or below | NO | 12¢ | 49% | 79% | $0 | center 52.5, market mean 51.85, lead 0d |
| +9¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 17¢ | 44% | 74% | $0 |  |
| +9¢ | KXHIGHTSFO-26NOV25-B66.5 | 66° to 67° | YES | 8¢ | 27% | 17% | $0 | center 64.7, market mean 63.64, lead 0d |
| +9¢ | KXHIGHTSEA-26NOV25-T60 | 61° or above | NO | 75¢ | 7% | 16% | $0 | center 56.0, market mean 59.11, lead 0d |
| +9¢ | KXHIGHTDAL-26NOV25-B53.5 | 53° to 54° | NO | 38¢ | 21% | 53% | $0 | center 52.15, market mean 53.88, lead 0d |
| +9¢ | KXHIGHTOKC-26NOV25-T45 | 44° or below | YES | 3¢ | 41% | 12% | $0 | center 45.15, market mean 46.21, lead 0d |
| +8¢ | KXHIGHPHIL-26NOV25-T50 | 49° or below | NO | 27¢ | 31% | 65% | $0 | center 50.9, market mean 49.2, lead 0d |
| +8¢ | KXHIGHNY-26NOV25-B49.5 | 49° to 50° | YES | 4¢ | 21% | 12% | $0 | center 47.1, market mean 46.42, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV25-B39.5 | 39° to 40° | NO | 51¢ | 32% | 41% | $0 | center 38.2, market mean 38.74, lead 0d |
| +8¢ | KXHIGHDEN-26NOV25-T49 | 48° or below | YES | 13¢ | 47% | 21% | $0 | center 48.7, market mean 50.06, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV25-B46.5 | 46° to 47° | YES | 5¢ | 22% | 13% | $0 | center 44.35, market mean 44.0, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV25-B62.5 | 62° to 63° | NO | 60¢ | 23% | 32% | $0 | center 64.7, market mean 63.64, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV25-T37 | 36° or below | YES | 3¢ | 20% | 11% | $0 | center 38.2, market mean 38.74, lead 0d |
| +8¢ | KXHIGHCHI-26NOV25-B41.5 | 41° to 42° | YES | 13¢ | 30% | 21% | $0 | center 43.0, market mean 43.61, lead 0d |
| +8¢ | KXHIGHAUS-26NOV25-T56 | 55° or below | YES | 2¢ | 18% | 10% | $0 | center 57.1, market mean 58.64, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV25-B80.5 | 80° to 81° | YES | 2¢ | 18% | 10% | $0 | center 76.85, market mean 76.99, lead 0d |
| +8¢ | KXHIGHAUS-26NOV25-B56.5 | 56° to 57° | YES | 10¢ | 42% | 18% | $0 | center 57.1, market mean 58.64, lead 0d |
| +7¢ | KXHIGHPHIL-26NOV25-B52.5 | 52° to 53° | YES | 7¢ | 23% | 14% | $0 | center 50.9, market mean 49.2, lead 0d |
| +7¢ | KXHIGHTDAL-26NOV25-B55.5 | 55° to 56° | NO | 75¢ | 10% | 18% | $0 | center 52.15, market mean 53.88, lead 0d |
| +7¢ | KXHIGHTLV-26NOV25-B61.5 | 61° to 62° | YES | 20¢ | 35% | 27% | $0 | center 62.0, market mean 63.36, lead 0d |
| +7¢ | KXHIGHAUS-26NOV25-B58.5 | 58° to 59° | NO | 32¢ | 30% | 61% | $0 | center 57.1, market mean 58.64, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV25-B45.5 | 45° to 46° | NO | 33¢ | 37% | 60% | $0 | center 45.15, market mean 46.21, lead 0d |
| +7¢ | KXHIGHTHOU-26NOV25-B57.5 | 57° to 58° | YES | 9¢ | 42% | 16% | $0 | center 58.1, market mean 59.89, lead 0d |
| +7¢ | KXHIGHTHOU-26NOV25-B61.5 | 61° to 62° | NO | 75¢ | 11% | 18% | $0 | center 58.1, market mean 59.89, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV25-B57.5 | 57° to 58° | YES | 7¢ | 40% | 14% | $0 | center 58.25, market mean 60.18, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV25-B61.5 | 61° to 62° | NO | 62¢ | 10% | 31% | $0 | center 58.25, market mean 60.18, lead 0d |
| +6¢ | KXHIGHDEN-26NOV25-B51.5 | 51° to 52° | NO | 70¢ | 16% | 23% | $0 | center 48.7, market mean 50.06, lead 0d |
