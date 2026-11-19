# Model vs. market

Scanned 2026-11-19 15:41 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 42¢ | 37% | 47% | $100 |  |
| +9¢ | KXAAAGASD-26NOV20-3.6900 | Above 3.6900 | YES | 70¢ | 88% | 79% | $100 |  |
| +8¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 12¢ | 72% | 80% | $100 |  |
| +7¢ | KXHIGHCHI-26NOV20-B68.5 | 68° to 69° | NO | 55¢ | 27% | 38% | $100 | center 67.1, market mean 68.0, lead 1d |
| +6¢ | KXHIGHNY-26NOV20-B68.5 | 68° to 69° | NO | 70¢ | 14% | 24% | $100 | center 65.25, market mean 66.67, lead 1d |
| +5¢ | KXHIGHTBOS-26NOV20-B68.5 | 68° to 69° | NO | 78¢ | 8% | 17% | $100 | center 64.25, market mean 66.61, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXHIGHTBOS-26NOV19-B65.5 | 65° to 66° | NO | 55¢ | 22% | 34% | $0 | center 63.25, market mean 64.49, lead 0d |
| +11¢ | KXHIGHPHIL-26NOV19-B67.5 | 67° to 68° | NO | 32¢ | 21% | 57% | $0 | center 65.2, market mean 67.38, lead 0d |
| +10¢ | KXAAAGASD-26NOV20-3.6950 | Above 3.6950 | YES | 4¢ | 47% | 14% | $0 |  |
| +10¢ | KXHIGHNY-26NOV19-B61.5 | 61° to 62° | YES | 13¢ | 34% | 23% | $0 | center 62.1, market mean 64.21, lead 0d |
| +10¢ | KXHIGHCHI-26NOV19-B62.5 | 62° to 63° | YES | 6¢ | 27% | 16% | $0 | center 64.25, market mean 65.78, lead 0d |
| +10¢ | KXHIGHMIA-26NOV19-B80.5 | 80° to 81° | YES | 26¢ | 49% | 36% | $0 | center 80.7, market mean 82.09, lead 0d |
| +9¢ | KXHIGHTPHX-26NOV20-T70 | 69° or below | YES | 12¢ | 51% | 21% | $0 | center 69.4, market mean 71.51, lead 1d |
| +9¢ | KXHIGHCHI-26NOV19-B66.5 | 66° to 67° | NO | 40¢ | 21% | 51% | $0 | center 64.25, market mean 65.78, lead 0d |
| +9¢ | KXAAAGASW-26NOV23-3.6200 | Above 3.6200 | NO | 7¢ | 56% | 84% | $0 |  |
| +8¢ | KXHIGHTSFO-26NOV19-T56 | 55° or below | YES | 9¢ | 27% | 18% | $0 | center 56.65, market mean 57.62, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV19-B58.5 | 58° to 59° | NO | 56¢ | 27% | 36% | $0 | center 56.65, market mean 57.62, lead 0d |
| +8¢ | KXHIGHTDC-26NOV19-B68.5 | 68° to 69° | NO | 56¢ | 27% | 36% | $0 | center 66.7, market mean 67.41, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV19-T55 | 54° or below | YES | 5¢ | 22% | 13% | $0 | center 55.85, market mean 55.96, lead 0d |
| +8¢ | KXHIGHTSEA-26NOV19-B47.5 | 47° to 48° | YES | 6¢ | 23% | 14% | $0 | center 49.5, market mean 50.34, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV19-B75.5 | 75° to 76° | NO | 28¢ | 38% | 64% | $0 | center 75.45, market mean 75.63, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV19-B55.5 | 55° to 56° | NO | 26¢ | 39% | 66% | $0 | center 55.85, market mean 55.96, lead 0d |
| +8¢ | KXHIGHTSATX-26NOV19-B72.5 | 72° to 73° | NO | 39¢ | 28% | 53% | $0 | center 71.25, market mean 72.17, lead 0d |
| +8¢ | KXHIGHNY-26NOV19-B65.5 | 65° to 66° | NO | 54¢ | 12% | 38% | $0 | center 62.1, market mean 64.21, lead 0d |
| +8¢ | KXHIGHLAX-26NOV19-B66.5 | 66° to 67° | NO | 45¢ | 39% | 47% | $0 | center 66.0, market mean 66.24, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV20-B66.5 | 66° to 67° | NO | 45¢ | 21% | 47% | $0 | center 64.25, market mean 66.61, lead 1d |
| +7¢ | KXHIGHTSATX-26NOV19-T70 | 69° or below | YES | 3¢ | 18% | 10% | $0 | center 71.25, market mean 72.17, lead 0d |
| +7¢ | KXHIGHMIA-26NOV19-B82.5 | 82° to 83° | NO | 33¢ | 37% | 60% | $0 | center 80.7, market mean 82.09, lead 0d |
| +7¢ | KXHIGHNY-26NOV19-B63.5 | 63° to 64° | NO | 57¢ | 28% | 36% | $0 | center 62.1, market mean 64.21, lead 0d |
| +7¢ | KXHIGHLAX-26NOV20-B66.5 | 66° to 67° | NO | 40¢ | 24% | 53% | $0 | center 64.9, market mean 66.45, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV19-B73.5 | 73° to 74° | YES | 10¢ | 25% | 17% | $0 | center 75.45, market mean 75.63, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV19-B68.5 | 68° to 69° | NO | 51¢ | 34% | 42% | $0 | center 67.55, market mean 69.16, lead 0d |
| +7¢ | KXHIGHTDC-26NOV20-B70.5 | 70° to 71° | NO | 45¢ | 25% | 48% | $0 | center 68.85, market mean 70.09, lead 1d |
| +7¢ | KXHIGHPHIL-26NOV19-B65.5 | 65° to 66° | YES | 19¢ | 34% | 26% | $0 | center 65.2, market mean 67.38, lead 0d |
| +7¢ | KXHIGHTATL-26NOV19-T69 | 70° or above | NO | 55¢ | 17% | 38% | $0 | center 67.65, market mean 69.18, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV19-B74.5 | 74° to 75° | NO | 54¢ | 19% | 40% | $0 | center 72.1, market mean 73.42, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV19-B66.5 | 66° to 67° | YES | 7¢ | 34% | 14% | $0 | center 67.55, market mean 69.16, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV19-B70.5 | 70° to 71° | NO | 59¢ | 14% | 35% | $0 | center 67.55, market mean 69.16, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV19-T63 | 62° or below | YES | 10¢ | 37% | 16% | $0 | center 63.25, market mean 64.49, lead 0d |
| +6¢ | KXHIGHTLV-26NOV19-B61.5 | 61° to 62° | NO | 71¢ | 16% | 23% | $0 | center 59.75, market mean 61.54, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV19-B70.5 | 70° to 71° | YES | 4¢ | 30% | 10% | $0 | center 72.1, market mean 73.42, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV19-B68.5 | 68° to 69° | YES | 8¢ | 21% | 14% | $0 | center 70.7, market mean 71.5, lead 0d |
| +6¢ | KXHIGHTHOU-26NOV19-B75.5 | 75° to 76° | NO | 34¢ | 39% | 60% | $0 | center 75.4, market mean 75.37, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV19-B72.5 | 72° to 73° | NO | 49¢ | 26% | 45% | $0 | center 70.7, market mean 71.5, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV19-B70.5 | 70° to 71° | YES | 27¢ | 40% | 33% | $0 | center 71.25, market mean 72.17, lead 0d |
| +6¢ | KXHIGHTATL-26NOV19-B66.5 | 66° to 67° | YES | 6¢ | 31% | 12% | $0 | center 67.65, market mean 69.18, lead 0d |
