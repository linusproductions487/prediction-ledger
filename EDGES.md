# Model vs. market

Scanned 2026-11-24 21:38 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 30¢ | 50% | 61% | $100 |  |
| +9¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 30¢ | 50% | 61% | $100 |  |
| +9¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 9¢ | 72% | 82% | $100 |  |
| +7¢ | KXHIGHNY-26NOV25-T47 | 46° or below | NO | 37¢ | 44% | 56% | $100 | center 47.1, market mean 46.39, lead 1d |
| +7¢ | KXHIGHTSEA-26NOV25-B57.5 | 57° to 58° | NO | 59¢ | 22% | 34% | $100 | center 55.8, market mean 57.88, lead 1d |
| +6¢ | KXHIGHTPHX-26NOV25-B76.5 | 76° to 77° | NO | 67¢ | 15% | 26% | $100 | center 76.35, market mean 77.71, lead 1d |
| +5¢ | KXHIGHTSEA-26NOV25-B59.5 | 59° to 60° | NO | 73¢ | 13% | 22% | $100 | center 55.8, market mean 57.88, lead 1d |
| +5¢ | KXHIGHAUS-26NOV25-B60.5 | 60° to 61° | NO | 69¢ | 15% | 26% | $100 | center 57.9, market mean 59.19, lead 1d |
| +5¢ | KXHIGHTMIN-26NOV25-B39.5 | 39° to 40° | NO | 54¢ | 31% | 41% | $100 | center 38.15, market mean 39.09, lead 1d |
| +5¢ | KXHIGHTSFO-26NOV25-B62.5 | 62° to 63° | NO | 61¢ | 24% | 34% | $100 | center 64.45, market mean 63.78, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +18¢ | KXHIGHTDAL-26NOV24-B46.5 | 46° to 47° | NO | 3¢ | 25% | 79% | $0 | center 49.1, market mean 46.65, lead 0d |
| +17¢ | KXHIGHTSATX-26NOV24-B53.5 | 53° to 54° | NO | 2¢ | 28% | 81% | $0 | center 55.1, market mean 53.55, lead 0d |
| +15¢ | KXHIGHLAX-26NOV24-B74.5 | 74° to 75° | NO | 11¢ | 29% | 74% | $0 | center 72.35, market mean 74.27, lead 0d |
| +14¢ | KXHIGHPHIL-26NOV25-T50 | 49° or below | NO | 21¢ | 23% | 65% | $0 | center 51.6, market mean 49.31, lead 1d |
| +13¢ | KXHIGHTDAL-26NOV25-T53 | 52° or below | YES | 4¢ | 60% | 17% | $0 | center 52.25, market mean 54.88, lead 1d |
| +12¢ | KXAAAGASD-26NOV25-3.5900 | Above 3.5900 | YES | 25¢ | 79% | 37% | $0 |  |
| +12¢ | KXHIGHTOKC-26NOV24-B41.5 | 41° to 42° | NO | 10¢ | 40% | 78% | $0 | center 42.05, market mean 41.72, lead 0d |
| +11¢ | KXHIGHNY-26NOV24-B51.5 | 51° to 52° | NO | 5¢ | 48% | 84% | $0 | center 50.6, market mean 51.45, lead 0d |
| +10¢ | KXHIGHTOKC-26NOV24-B43.5 | 43° to 44° | YES | 8¢ | 30% | 19% | $0 | center 42.05, market mean 41.72, lead 0d |
| +10¢ | KXHIGHTDAL-26NOV25-B55.5 | 55° to 56° | NO | 47¢ | 10% | 43% | $0 | center 52.25, market mean 54.88, lead 1d |
| +10¢ | KXHIGHTSATX-26NOV25-B61.5 | 61° to 62° | NO | 44¢ | 13% | 46% | $0 | center 58.5, market mean 60.54, lead 1d |
| +10¢ | KXHIGHTSFO-26NOV24-B62.5 | 62° to 63° | YES | 14¢ | 35% | 24% | $0 | center 63.4, market mean 60.38, lead 0d |
| +10¢ | KXHIGHTSFO-26NOV24-T60 | 59° or below | NO | 76¢ | 2% | 14% | $0 | center 63.4, market mean 60.38, lead 0d |
| +9¢ | KXHIGHLAX-26NOV24-B72.5 | 72° to 73° | YES | 9¢ | 45% | 18% | $0 | center 72.35, market mean 74.27, lead 0d |
| +8¢ | KXHIGHTDC-26NOV25-T53 | 52° or below | NO | 12¢ | 53% | 80% | $0 | center 52.35, market mean 51.93, lead 1d |
| +8¢ | KXHIGHTHOU-26NOV25-B57.5 | 57° to 58° | YES | 4¢ | 40% | 12% | $0 | center 58.1, market mean 60.4, lead 1d |
| +8¢ | KXHIGHTHOU-26NOV25-B61.5 | 61° to 62° | NO | 54¢ | 9% | 38% | $0 | center 58.1, market mean 60.4, lead 1d |
| +8¢ | KXHIGHDEN-26NOV25-B49.5 | 49° to 50° | NO | 46¢ | 18% | 46% | $0 | center 48.25, market mean 49.66, lead 1d |
| +8¢ | KXHIGHTSATX-26NOV24-B55.5 | 55° to 56° | YES | 2¢ | 35% | 10% | $0 | center 55.1, market mean 53.55, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV24-B34.5 | 34° to 35° | NO | 4¢ | 61% | 88% | $0 | center 34.0, market mean 34.55, lead 0d |
| +8¢ | KXHIGHDEN-26NOV25-T49 | 48° or below | YES | 25¢ | 57% | 33% | $0 | center 48.25, market mean 49.66, lead 1d |
| +8¢ | KXHIGHTSFO-26NOV24-B60.5 | 60° to 61° | NO | 52¢ | 15% | 40% | $0 | center 63.4, market mean 60.38, lead 0d |
| +8¢ | KXHIGHNY-26NOV24-B49.5 | 49° to 50° | YES | 6¢ | 41% | 14% | $0 | center 50.6, market mean 51.45, lead 0d |
| +7¢ | KXAAAGASD-26NOV25-3.5950 | Above 3.5950 | YES | 2¢ | 33% | 9% | $0 |  |
| +7¢ | KXHIGHTBOS-26NOV25-B44.5 | 44° to 45° | NO | 33¢ | 35% | 60% | $0 | center 44.5, market mean 44.25, lead 1d |
| +7¢ | KXHIGHCHI-26NOV25-B43.5 | 43° to 44° | NO | 36¢ | 35% | 57% | $0 | center 44.1, market mean 43.55, lead 1d |
| +7¢ | KXHIGHTLV-26NOV24-B61.5 | 61° to 62° | YES | 25¢ | 42% | 32% | $0 | center 61.1, market mean 63.1, lead 0d |
| +7¢ | KXHIGHTLV-26NOV25-B63.5 | 63° to 64° | NO | 37¢ | 30% | 56% | $0 | center 62.25, market mean 63.22, lead 1d |
| +7¢ | KXHIGHTOKC-26NOV25-T45 | 44° or below | YES | 4¢ | 35% | 11% | $0 | center 45.45, market mean 46.6, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV24-B74.5 | 74° to 75° | NO | 19¢ | 38% | 74% | $0 | center 74.7, market mean 74.37, lead 0d |
| +6¢ | KXHIGHTATL-26NOV25-B54.5 | 54° to 55° | NO | 55¢ | 15% | 39% | $0 | center 51.65, market mean 53.11, lead 1d |
| +6¢ | KXHIGHTDAL-26NOV24-B48.5 | 48° to 49° | YES | 5¢ | 33% | 11% | $0 | center 49.1, market mean 46.65, lead 0d |
| +6¢ | KXHIGHTPHX-26NOV24-B76.5 | 76° to 77° | YES | 4¢ | 30% | 10% | $0 | center 74.7, market mean 74.37, lead 0d |
| +6¢ | KXHIGHTSFO-26NOV24-B64.5 | 64° to 65° | YES | 4¢ | 33% | 10% | $0 | center 63.4, market mean 60.38, lead 0d |
| +6¢ | KXHIGHLAX-26NOV25-B74.5 | 74° to 75° | NO | 40¢ | 35% | 54% | $0 | center 74.15, market mean 74.57, lead 1d |
| +6¢ | KXHIGHTSATX-26NOV25-B57.5 | 57° to 58° | YES | 6¢ | 33% | 12% | $0 | center 58.5, market mean 60.54, lead 1d |
| +5¢ | KXHIGHTMIN-26NOV24-B36.5 | 36° to 37° | YES | 2¢ | 13% | 7% | $0 | center 34.0, market mean 34.55, lead 0d |
| +5¢ | KXHIGHTPHX-26NOV25-B78.5 | 78° to 79° | NO | 54¢ | 22% | 41% | $0 | center 76.35, market mean 77.71, lead 1d |
| +5¢ | KXHIGHTOKC-26NOV25-B47.5 | 47° to 48° | NO | 64¢ | 19% | 31% | $100 | center 45.45, market mean 46.6, lead 1d |
| +4¢ | KXHIGHTDC-26NOV25-B53.5 | 53° to 54° | YES | 13¢ | 29% | 17% | $100 | center 52.35, market mean 51.93, lead 1d |
