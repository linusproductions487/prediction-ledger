# Model vs. market

Scanned 2026-11-22 06:39 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +9¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 55¢ | 26% | 36% | $100 |  |
| +7¢ | KXHIGHTPHX-26NOV22-B73.5 | 73° to 74° | NO | 48¢ | 33% | 45% | $100 | center 73.44, market mean 73.98, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +24¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 2¢ | 0% | 74% | $0 |  |
| +24¢ | KXAAAGASW-26NOV23-3.6250 | Above 3.6250 | NO | 2¢ | 2% | 74% | $0 |  |
| +20¢ | KXHIGHTOKC-26NOV22-B59.5 | 59° to 60° | NO | 5¢ | 13% | 75% | $0 | center 50.45, market mean 59.63, lead 0d |
| +18¢ | KXHIGHTBOS-26NOV22-T62 | 61° or below | NO | 4¢ | 19% | 77% | $0 | center 63.45, market mean 60.79, lead 0d |
| +11¢ | KXHIGHAUS-26NOV22-B73.5 | 73° to 74° | NO | 48¢ | 30% | 41% | $0 | center 74.44, market mean 73.68, lead 0d |
| +10¢ | KXHIGHTMIN-26NOV22-B43.5 | 43° to 44° | NO | 9¢ | 48% | 81% | $0 | center 41.45, market mean 43.71, lead 0d |
| +9¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 4¢ | 58% | 87% | $0 |  |
| +8¢ | KXHIGHMIA-26NOV22-B85.5 | 85° to 86° | NO | 44¢ | 38% | 47% | $0 | center 85.44, market mean 85.16, lead 0d |
| +8¢ | KXHIGHTLV-26NOV22-B56.5 | 56° to 57° | NO | 40¢ | 25% | 52% | $0 | center 58.45, market mean 57.39, lead 1d |
| +8¢ | KXHIGHCHI-26NOV22-B60.5 | 60° to 61° | NO | 26¢ | 39% | 66% | $0 | center 59.45, market mean 61.12, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV22-B68.5 | 68° to 69° | NO | 55¢ | 28% | 37% | $0 | center 63.45, market mean 67.65, lead 0d |
| +8¢ | KXHIGHNY-26NOV22-B63.5 | 63° to 64° | YES | 14¢ | 31% | 22% | $0 | center 62.45, market mean 60.93, lead 0d |
| +8¢ | KXHIGHLAX-26NOV22-B67.5 | 67° to 68° | NO | 31¢ | 35% | 61% | $0 | center 67.44, market mean 67.77, lead 1d |
| +8¢ | KXHIGHTBOS-26NOV22-B64.5 | 64° to 65° | YES | 2¢ | 34% | 10% | $0 | center 63.45, market mean 60.79, lead 0d |
| +8¢ | KXHIGHNY-26NOV22-B65.5 | 65° to 66° | YES | 2¢ | 18% | 10% | $0 | center 62.45, market mean 60.93, lead 0d |
| +8¢ | KXHIGHTATL-26NOV22-T65 | 64° or below | NO | 16¢ | 53% | 77% | $0 | center 64.44, market mean 64.1, lead 0d |
| +7¢ | KXHIGHTSFO-26NOV22-B55.5 | 55° to 56° | NO | 35¢ | 32% | 58% | $0 | center 56.45, market mean 55.61, lead 1d |
| +7¢ | KXAAAGASW-26NOV23-3.6350 | Above 3.6350 | NO | 69¢ | 0% | 24% | $0 |  |
| +7¢ | KXHIGHPHIL-26NOV22-B65.5 | 65° to 66° | NO | 58¢ | 26% | 35% | $0 | center 64.44, market mean 64.49, lead 0d |
| +7¢ | KXHIGHPHIL-26NOV22-B63.5 | 63° to 64° | NO | 63¢ | 22% | 30% | $0 | center 64.44, market mean 64.49, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV22-B76.5 | 76° to 77° | NO | 56¢ | 31% | 38% | $0 | center 77.44, market mean 76.31, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV22-B66.5 | 66° to 67° | YES | 2¢ | 15% | 8% | $0 | center 63.45, market mean 60.79, lead 0d |
| +6¢ | KXHIGHAUS-26NOV22-B77.5 | 77° to 78° | YES | 2¢ | 15% | 8% | $0 | center 74.44, market mean 73.68, lead 0d |
| +6¢ | KXHIGHNY-26NOV22-T61 | 60° or below | NO | 51¢ | 22% | 43% | $0 | center 62.45, market mean 60.93, lead 0d |
| +6¢ | KXHIGHTDC-26NOV22-T69 | 70° or above | YES | 2¢ | 14% | 8% | $0 | center 66.44, market mean 65.85, lead 0d |
| +6¢ | KXHIGHTATL-26NOV22-B65.5 | 65° to 66° | YES | 11¢ | 23% | 17% | $0 | center 64.44, market mean 64.1, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV22-B62.5 | 62° to 63° | YES | 4¢ | 30% | 10% | $0 | center 63.45, market mean 60.79, lead 0d |
| +6¢ | KXHIGHNY-26NOV22-B61.5 | 61° to 62° | NO | 62¢ | 26% | 32% | $0 | center 62.45, market mean 60.93, lead 0d |
| +5¢ | KXHIGHPHIL-26NOV22-T63 | 62° or below | YES | 14¢ | 25% | 19% | $0 | center 64.44, market mean 64.49, lead 0d |
| +5¢ | KXHIGHPHIL-26NOV22-B67.5 | 67° to 68° | YES | 8¢ | 19% | 13% | $0 | center 64.44, market mean 64.49, lead 0d |
| +5¢ | KXHIGHTSEA-26NOV22-B47.5 | 47° to 48° | NO | 50¢ | 25% | 45% | $0 | center 49.45, market mean 48.3, lead 1d |
| +5¢ | KXHIGHTSATX-26NOV22-B73.5 | 73° to 74° | NO | 57¢ | 32% | 38% | $0 | center 72.44, market mean 73.37, lead 0d |
| +5¢ | KXHIGHTNOLA-26NOV22-B80.5 | 80° to 81° | YES | 3¢ | 13% | 8% | $0 | center 77.44, market mean 76.31, lead 0d |
| +3¢ | KXHIGHLAX-26NOV22-B65.5 | 65° to 66° | YES | 14¢ | 24% | 17% | $100 | center 67.44, market mean 67.77, lead 1d |
| +3¢ | KXHIGHTPHX-26NOV22-B71.5 | 71° to 72° | YES | 14¢ | 24% | 17% | $100 | center 73.44, market mean 73.98, lead 1d |
| +1¢ | KXHIGHTSFO-26NOV22-B57.5 | 57° to 58° | YES | 22¢ | 31% | 23% | $100 | center 56.45, market mean 55.61, lead 1d |
| -1¢ | KXHIGHTLV-26NOV22-B60.5 | 60° to 61° | YES | 13¢ | 23% | 12% | $100 | center 58.45, market mean 57.39, lead 1d |
| -1¢ | KXHIGHTSEA-26NOV22-B51.5 | 51° to 52° | YES | 14¢ | 23% | 13% | $100 | center 49.45, market mean 48.3, lead 1d |
| -3¢ | KXHIGHTSFO-26NOV22-B59.5 | 59° to 60° | YES | 11¢ | 14% | 8% | $100 | center 56.45, market mean 55.61, lead 1d |
