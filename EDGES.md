# Model vs. market

Scanned 2026-11-25 21:38 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +7¢ | KXHIGHDEN-26NOV26-B60.5 | 60° to 61° | NO | 57¢ | 24% | 36% | $100 | center 58.12, market mean 59.91, lead 1d |
| +6¢ | KXHIGHLAX-26NOV26-B80.5 | 80° to 81° | NO | 59¢ | 25% | 35% | $100 | center 82.17, market mean 81.27, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +20¢ | KXAAAGASD-26NOV26-3.5550 | Above 3.5550 | YES | 15¢ | 96% | 35% | $0 |  |
| +16¢ | KXHIGHTHOU-26NOV25-B59.5 | 59° to 60° | NO | 3¢ | 30% | 81% | $0 | center 60.8, market mean 59.61, lead 0d |
| +16¢ | KXHIGHMIA-26NOV25-T75 | 74° or below | NO | 8¢ | 24% | 76% | $0 | center 75.73, market mean 73.72, lead 0d |
| +16¢ | KXHIGHTPHX-26NOV25-B76.5 | 76° to 77° | NO | 14¢ | 20% | 70% | $0 | center 76.83, market mean 76.5, lead 0d |
| +14¢ | KXHIGHLAX-26NOV25-B74.5 | 74° to 75° | NO | 14¢ | 26% | 72% | $0 | center 76.42, market mean 74.63, lead 0d |
| +12¢ | KXHIGHTOKC-26NOV26-B47.5 | 47° to 48° | NO | 33¢ | 20% | 56% | $0 | center 46.17, market mean 47.78, lead 1d |
| +11¢ | KXHIGHTDAL-26NOV26-B54.5 | 54° to 55° | NO | 34¢ | 18% | 55% | $0 | center 52.17, market mean 54.26, lead 1d |
| +11¢ | KXHIGHPHIL-26NOV25-T50 | 49° or below | NO | 2¢ | 76% | 87% | $0 | center 47.38, market mean 48.68, lead 0d |
| +10¢ | KXHIGHTOKC-26NOV25-B45.5 | 45° to 46° | NO | 6¢ | 48% | 84% | $0 | center 46.4, market mean 45.67, lead 0d |
| +10¢ | KXHIGHTLV-26NOV26-B68.5 | 68° to 69° | NO | 33¢ | 27% | 57% | $0 | center 67.17, market mean 68.29, lead 1d |
| +10¢ | KXHIGHAUS-26NOV26-B60.5 | 60° to 61° | NO | 41¢ | 13% | 49% | $0 | center 57.72, market mean 59.9, lead 1d |
| +10¢ | KXHIGHTDAL-26NOV25-B55.5 | 55° to 56° | YES | 5¢ | 25% | 14% | $0 | center 53.6, market mean 53.65, lead 0d |
| +9¢ | KXHIGHTLV-26NOV25-B63.5 | 63° to 64° | NO | 45¢ | 34% | 46% | $0 | center 62.07, market mean 62.76, lead 0d |
| +9¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 18¢ | 44% | 73% | $0 |  |
| +9¢ | KXHIGHAUS-26NOV25-B56.5 | 56° to 57° | YES | 4¢ | 22% | 13% | $0 | center 58.52, market mean 58.5, lead 0d |
| +9¢ | KXHIGHNY-26NOV25-T47 | 46° or below | NO | 6¢ | 53% | 85% | $0 | center 46.38, market mean 45.7, lead 0d |
| +9¢ | KXHIGHAUS-26NOV25-B58.5 | 58° to 59° | NO | 7¢ | 53% | 84% | $0 | center 58.52, market mean 58.5, lead 0d |
| +8¢ | KXHIGHTSEA-26NOV26-B56.5 | 56° to 57° | NO | 36¢ | 29% | 56% | $0 | center 55.17, market mean 56.61, lead 1d |
| +8¢ | KXHIGHAUS-26NOV25-B60.5 | 60° to 61° | YES | 3¢ | 20% | 11% | $0 | center 58.52, market mean 58.5, lead 0d |
| +8¢ | KXHIGHTHOU-26NOV26-B59.5 | 59° to 60° | NO | 46¢ | 20% | 46% | $0 | center 58.17, market mean 60.19, lead 1d |
| +8¢ | KXHIGHTDAL-26NOV26-T52 | 51° or below | YES | 5¢ | 40% | 13% | $0 | center 52.17, market mean 54.26, lead 1d |
| +8¢ | KXHIGHTNOLA-26NOV26-B55.5 | 55° to 56° | NO | 40¢ | 26% | 52% | $0 | center 54.92, market mean 56.03, lead 1d |
| +8¢ | KXHIGHTMIN-26NOV25-B39.5 | 39° to 40° | NO | 3¢ | 63% | 89% | $0 | center 39.2, market mean 39.56, lead 0d |
| +8¢ | KXHIGHMIA-26NOV25-B75.5 | 75° to 76° | YES | 6¢ | 43% | 14% | $0 | center 75.73, market mean 73.72, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV26-B80.5 | 80° to 81° | NO | 40¢ | 23% | 52% | $0 | center 78.83, market mean 79.95, lead 1d |
| +8¢ | KXHIGHAUS-26NOV26-B56.5 | 56° to 57° | YES | 3¢ | 34% | 10% | $0 | center 57.72, market mean 59.9, lead 1d |
| +8¢ | KXHIGHPHIL-26NOV26-T57 | 56° or below | NO | 32¢ | 37% | 61% | $0 | center 57.92, market mean 56.8, lead 1d |
| +7¢ | KXHIGHNY-26NOV26-T56 | 55° or below | NO | 18¢ | 51% | 75% | $0 | center 55.42, market mean 55.02, lead 1d |
| +7¢ | KXHIGHTHOU-26NOV26-B57.5 | 57° to 58° | YES | 5¢ | 35% | 12% | $0 | center 58.17, market mean 60.19, lead 1d |
| +7¢ | KXHIGHTDAL-26NOV25-B53.5 | 53° to 54° | NO | 5¢ | 63% | 88% | $0 | center 53.6, market mean 53.65, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV26-B61.5 | 61° to 62° | NO | 51¢ | 19% | 42% | $0 | center 59.22, market mean 62.19, lead 1d |
| +7¢ | KXHIGHLAX-26NOV25-B76.5 | 76° to 77° | YES | 10¢ | 42% | 17% | $0 | center 76.42, market mean 74.63, lead 0d |
| +7¢ | KXHIGHPHIL-26NOV25-B50.5 | 50° to 51° | YES | 3¢ | 17% | 10% | $0 | center 47.38, market mean 48.68, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV26-B45.5 | 45° to 46° | YES | 12¢ | 40% | 19% | $0 | center 46.17, market mean 47.78, lead 1d |
| +6¢ | KXHIGHTHOU-26NOV25-B61.5 | 61° to 62° | YES | 7¢ | 40% | 13% | $0 | center 60.8, market mean 59.61, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV26-B59.5 | 59° to 60° | YES | 5¢ | 35% | 11% | $0 | center 59.22, market mean 62.19, lead 1d |
| +6¢ | KXHIGHMIA-26NOV26-B78.5 | 78° to 79° | NO | 47¢ | 27% | 47% | $0 | center 78.83, market mean 79.14, lead 1d |
| +6¢ | KXHIGHTSATX-26NOV26-B63.5 | 63° to 64° | NO | 59¢ | 6% | 35% | $0 | center 59.22, market mean 62.19, lead 1d |
| +6¢ | KXAAAGASW-26NOV30-3.4600 | Above 3.4600 | NO | 3¢ | 71% | 91% | $0 |  |
| +6¢ | KXHIGHTHOU-26NOV26-B61.5 | 61° to 62° | NO | 63¢ | 12% | 31% | $0 | center 58.17, market mean 60.19, lead 1d |
