# Model vs. market

Scanned 2026-11-24 22:20 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 9¢ | 72% | 82% | $100 |  |
| +8¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 33¢ | 50% | 59% | $100 |  |
| +7¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 33¢ | 50% | 60% | $100 |  |
| +7¢ | KXHIGHNY-26NOV25-T47 | 46° or below | NO | 38¢ | 44% | 55% | $100 | center 47.1, market mean 46.39, lead 1d |
| +6¢ | KXHIGHLAX-26NOV25-B74.5 | 74° to 75° | NO | 47¢ | 35% | 47% | $100 | center 74.3, market mean 74.71, lead 1d |
| +6¢ | KXHIGHAUS-26NOV25-B56.5 | 56° to 57° | YES | 9¢ | 27% | 15% | $100 | center 57.9, market mean 59.18, lead 1d |
| +6¢ | KXHIGHTMIN-26NOV25-B39.5 | 39° to 40° | NO | 55¢ | 31% | 40% | $100 | center 38.15, market mean 39.0, lead 1d |
| +6¢ | KXHIGHTSFO-26NOV25-B62.5 | 62° to 63° | NO | 60¢ | 27% | 35% | $100 | center 64.15, market mean 63.72, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +17¢ | KXAAAGASD-26NOV25-3.5900 | Above 3.5900 | YES | 9¢ | 79% | 26% | $0 |  |
| +15¢ | KXHIGHTDAL-26NOV24-B46.5 | 46° to 47° | NO | 5¢ | 28% | 80% | $0 | center 48.9, market mean 46.63, lead 0d |
| +14¢ | KXHIGHTPHX-26NOV24-B74.5 | 74° to 75° | NO | 3¢ | 38% | 83% | $0 | center 74.7, market mean 74.54, lead 0d |
| +14¢ | KXHIGHTDAL-26NOV25-T53 | 52° or below | YES | 3¢ | 60% | 17% | $0 | center 52.25, market mean 54.91, lead 1d |
| +12¢ | KXHIGHPHIL-26NOV25-T50 | 49° or below | NO | 23¢ | 23% | 65% | $0 | center 51.6, market mean 49.27, lead 1d |
| +11¢ | KXHIGHNY-26NOV24-B51.5 | 51° to 52° | NO | 3¢ | 53% | 86% | $0 | center 50.6, market mean 51.48, lead 0d |
| +10¢ | KXHIGHTPHX-26NOV24-B72.5 | 72° to 73° | YES | 3¢ | 25% | 14% | $0 | center 74.7, market mean 74.54, lead 0d |
| +10¢ | KXHIGHTDAL-26NOV25-B55.5 | 55° to 56° | NO | 46¢ | 10% | 44% | $0 | center 52.25, market mean 54.91, lead 1d |
| +10¢ | KXHIGHTSATX-26NOV25-B61.5 | 61° to 62° | NO | 44¢ | 13% | 46% | $0 | center 58.5, market mean 60.54, lead 1d |
| +10¢ | KXHIGHTSFO-26NOV24-B64.5 | 64° to 65° | YES | 4¢ | 44% | 14% | $0 | center 63.5, market mean 59.96, lead 0d |
| +10¢ | KXHIGHNY-26NOV24-B49.5 | 49° to 50° | YES | 4¢ | 45% | 14% | $0 | center 50.6, market mean 51.48, lead 0d |
| +9¢ | KXHIGHTSFO-26NOV24-B62.5 | 62° to 63° | YES | 6¢ | 46% | 15% | $0 | center 63.5, market mean 59.96, lead 0d |
| +9¢ | KXHIGHDEN-26NOV25-B49.5 | 49° to 50° | NO | 45¢ | 18% | 46% | $0 | center 48.25, market mean 49.66, lead 1d |
| +8¢ | KXHIGHTDC-26NOV25-T53 | 52° or below | NO | 12¢ | 53% | 80% | $0 | center 52.35, market mean 51.93, lead 1d |
| +8¢ | KXHIGHTMIN-26NOV24-B34.5 | 34° to 35° | NO | 3¢ | 61% | 89% | $0 | center 34.0, market mean 34.55, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV25-B44.5 | 44° to 45° | NO | 31¢ | 35% | 61% | $0 | center 44.5, market mean 44.31, lead 1d |
| +8¢ | KXHIGHTHOU-26NOV25-B61.5 | 61° to 62° | NO | 56¢ | 9% | 36% | $0 | center 58.1, market mean 60.3, lead 1d |
| +8¢ | KXHIGHTOKC-26NOV25-T45 | 44° or below | YES | 2¢ | 35% | 10% | $0 | center 45.45, market mean 46.6, lead 1d |
| +8¢ | KXHIGHDEN-26NOV25-T49 | 48° or below | YES | 25¢ | 57% | 33% | $0 | center 48.25, market mean 49.66, lead 1d |
| +7¢ | KXHIGHTHOU-26NOV25-B57.5 | 57° to 58° | YES | 6¢ | 40% | 13% | $0 | center 58.1, market mean 60.3, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV25-B76.5 | 76° to 77° | NO | 57¢ | 14% | 36% | $0 | center 76.65, market mean 77.63, lead 1d |
| +6¢ | KXHIGHTHOU-26NOV25-B59.5 | 59° to 60° | NO | 48¢ | 26% | 46% | $0 | center 58.1, market mean 60.3, lead 1d |
| +6¢ | KXHIGHCHI-26NOV25-B43.5 | 43° to 44° | NO | 38¢ | 35% | 56% | $0 | center 44.1, market mean 43.6, lead 1d |
| +6¢ | KXHIGHTNOLA-26NOV25-B55.5 | 55° to 56° | NO | 41¢ | 26% | 53% | $0 | center 57.1, market mean 56.03, lead 1d |
| +6¢ | KXHIGHTATL-26NOV25-B54.5 | 54° to 55° | NO | 56¢ | 15% | 38% | $0 | center 51.65, market mean 53.06, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV24-B48.5 | 48° to 49° | YES | 4¢ | 32% | 10% | $0 | center 48.9, market mean 46.63, lead 0d |
| +6¢ | KXHIGHTLV-26NOV25-B63.5 | 63° to 64° | NO | 38¢ | 30% | 56% | $0 | center 62.25, market mean 63.2, lead 1d |
| +6¢ | KXHIGHTSATX-26NOV25-B57.5 | 57° to 58° | YES | 6¢ | 33% | 12% | $0 | center 58.5, market mean 60.54, lead 1d |
| +6¢ | KXHIGHTSFO-26NOV24-B60.5 | 60° to 61° | NO | 58¢ | 5% | 36% | $0 | center 63.5, market mean 59.96, lead 0d |
| +6¢ | KXHIGHTSFO-26NOV24-T60 | 59° or below | NO | 63¢ | 0% | 32% | $0 | center 63.5, market mean 59.96, lead 0d |
| +5¢ | KXHIGHTMIN-26NOV24-B36.5 | 36° to 37° | YES | 2¢ | 13% | 7% | $0 | center 34.0, market mean 34.55, lead 0d |
| +5¢ | KXHIGHTPHX-26NOV24-B76.5 | 76° to 77° | YES | 4¢ | 30% | 9% | $0 | center 74.7, market mean 74.54, lead 0d |
| +5¢ | KXHIGHTSEA-26NOV25-B59.5 | 59° to 60° | NO | 73¢ | 13% | 22% | $100 | center 55.8, market mean 58.04, lead 1d |
| +4¢ | KXHIGHTATL-26NOV25-B50.5 | 50° to 51° | YES | 16¢ | 30% | 20% | $100 | center 51.65, market mean 53.06, lead 1d |
| +4¢ | KXHIGHAUS-26NOV25-B60.5 | 60° to 61° | NO | 71¢ | 15% | 25% | $100 | center 57.9, market mean 59.18, lead 1d |
| +4¢ | KXHIGHMIA-26NOV25-B75.5 | 75° to 76° | NO | 60¢ | 30% | 36% | $100 | center 76.45, market mean 75.75, lead 1d |
| +3¢ | KXHIGHTSEA-26NOV25-B57.5 | 57° to 58° | NO | 65¢ | 22% | 32% | $100 | center 55.8, market mean 58.04, lead 1d |
| +3¢ | KXHIGHTSEA-26NOV25-B55.5 | 55° to 56° | YES | 18¢ | 29% | 21% | $100 | center 55.8, market mean 58.04, lead 1d |
| +3¢ | KXHIGHLAX-26NOV25-B72.5 | 72° to 73° | YES | 15¢ | 25% | 18% | $100 | center 74.3, market mean 74.71, lead 1d |
| +3¢ | KXHIGHTOKC-26NOV25-B47.5 | 47° to 48° | NO | 66¢ | 19% | 31% | $100 | center 45.45, market mean 46.6, lead 1d |
