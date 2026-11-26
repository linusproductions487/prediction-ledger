# Model vs. market

Scanned 2026-11-26 08:08 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +8¢ | KXAAAGASW-26NOV30-3.5000 | Above 3.5000 | NO | 64¢ | 19% | 28% | $100 |  |
| +7¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 66¢ | 19% | 27% | $100 |  |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXHIGHTSEA-26NOV26-B52.5 | 52° to 53° | YES | 2¢ | 25% | 13% | $0 | center 54.42, market mean 56.74, lead 0d |
| +11¢ | KXAAAGASW-26NOV30-3.4800 | Above 3.4800 | NO | 9¢ | 44% | 80% | $0 |  |
| +10¢ | KXHIGHTLV-26NOV26-T66 | 65° or below | YES | 2¢ | 24% | 13% | $0 | center 67.17, market mean 67.98, lead 0d |
| +10¢ | KXHIGHTBOS-26NOV26-B51.5 | 51° to 52° | YES | 4¢ | 25% | 14% | $0 | center 50.17, market mean 48.49, lead 0d |
| +10¢ | KXHIGHAUS-26NOV26-B60.5 | 60° to 61° | NO | 35¢ | 15% | 55% | $0 | center 58.22, market mean 60.08, lead 0d |
| +10¢ | KXHIGHTDAL-26NOV26-B54.5 | 54° to 55° | NO | 29¢ | 24% | 61% | $0 | center 52.72, market mean 54.31, lead 0d |
| +9¢ | KXHIGHTSATX-26NOV26-B59.5 | 59° to 60° | YES | 2¢ | 38% | 11% | $0 | center 60.58, market mean 62.56, lead 0d |
| +9¢ | KXHIGHTHOU-26NOV26-B57.5 | 57° to 58° | YES | 2¢ | 38% | 11% | $0 | center 58.92, market mean 60.04, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV26-B52.5 | 52° to 53° | YES | 20¢ | 40% | 28% | $0 | center 52.72, market mean 54.31, lead 0d |
| +8¢ | KXHIGHMIA-26NOV26-B78.5 | 78° to 79° | NO | 53¢ | 29% | 39% | $0 | center 79.12, market mean 79.03, lead 0d |
| +8¢ | KXHIGHDEN-26NOV26-B56.5 | 56° to 57° | YES | 3¢ | 20% | 11% | $0 | center 58.92, market mean 60.08, lead 0d |
| +8¢ | KXHIGHTLV-26NOV26-B68.5 | 68° to 69° | NO | 35¢ | 29% | 57% | $0 | center 67.17, market mean 67.98, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV26-B49.5 | 49° to 50° | NO | 66¢ | 16% | 27% | $0 | center 46.97, market mean 48.22, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV26-B45.5 | 45° to 46° | YES | 6¢ | 36% | 13% | $0 | center 46.97, market mean 48.22, lead 0d |
| +7¢ | KXHIGHTHOU-26NOV26-B59.5 | 59° to 60° | NO | 35¢ | 26% | 58% | $0 | center 58.92, market mean 60.04, lead 0d |
| +7¢ | KXHIGHAUS-26NOV26-B58.5 | 58° to 59° | YES | 24¢ | 39% | 31% | $0 | center 58.22, market mean 60.08, lead 0d |
| +7¢ | KXHIGHAUS-26NOV26-B56.5 | 56° to 57° | YES | 3¢ | 32% | 10% | $0 | center 58.22, market mean 60.08, lead 0d |
| +7¢ | KXHIGHNY-26NOV26-T56 | 55° or below | NO | 18¢ | 52% | 75% | $0 | center 55.38, market mean 55.12, lead 0d |
| +7¢ | KXHIGHCHI-26NOV26-B42.5 | 42° to 43° | YES | 3¢ | 17% | 10% | $0 | center 45.17, market mean 45.27, lead 0d |
| +7¢ | KXHIGHCHI-26NOV26-B44.5 | 44° to 45° | NO | 45¢ | 36% | 48% | $0 | center 45.17, market mean 45.27, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV26-B59.5 | 59° to 60° | YES | 4¢ | 17% | 10% | $0 | center 57.62, market mean 56.21, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV26-B53.5 | 53° to 54° | YES | 4¢ | 32% | 10% | $0 | center 55.17, market mean 55.96, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV26-T38 | 37° or below | YES | 8¢ | 21% | 14% | $0 | center 39.07, market mean 39.2, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV26-T52 | 51° or below | YES | 2¢ | 28% | 8% | $0 | center 52.72, market mean 54.31, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV26-B61.5 | 61° to 62° | YES | 3¢ | 16% | 9% | $0 | center 57.62, market mean 56.21, lead 0d |
| +6¢ | KXHIGHMIA-26NOV26-B82.5 | 82° to 83° | YES | 2¢ | 14% | 8% | $0 | center 79.12, market mean 79.03, lead 0d |
| +6¢ | KXHIGHTATL-26NOV26-B53.5 | 53° to 54° | YES | 3¢ | 14% | 8% | $0 | center 50.62, market mean 50.33, lead 0d |
| +5¢ | KXHIGHTBOS-26NOV26-B53.5 | 53° to 54° | YES | 2¢ | 13% | 7% | $0 | center 50.17, market mean 48.49, lead 0d |
| +5¢ | KXHIGHTHOU-26NOV26-T57 | 56° or below | YES | 2¢ | 13% | 7% | $0 | center 58.92, market mean 60.04, lead 0d |
| +5¢ | KXHIGHTATL-26NOV26-T49 | 48° or below | YES | 3¢ | 14% | 8% | $0 | center 50.62, market mean 50.33, lead 0d |
| +5¢ | KXHIGHTPHX-26NOV26-B78.5 | 78° to 79° | NO | 52¢ | 17% | 43% | $0 | center 78.92, market mean 78.91, lead 0d |
| +5¢ | KXHIGHTNOLA-26NOV26-T53 | 52° or below | YES | 2¢ | 13% | 7% | $0 | center 55.17, market mean 55.96, lead 0d |
| +5¢ | KXHIGHTOKC-26NOV26-B47.5 | 47° to 48° | NO | 42¢ | 33% | 53% | $0 | center 46.97, market mean 48.22, lead 0d |
