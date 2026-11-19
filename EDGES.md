# Model vs. market

Scanned 2026-11-19 15:37 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXAAAGASD-26NOV20-3.6900 | Above 3.6900 | YES | 71¢ | 88% | 81% | $100 |  |
| +9¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 44¢ | 37% | 47% | $100 |  |
| +9¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 11¢ | 72% | 80% | $100 |  |
| +7¢ | KXHIGHCHI-26NOV20-B68.5 | 68° to 69° | NO | 55¢ | 27% | 38% | $100 | center 67.1, market mean 68.02, lead 1d |
| +5¢ | KXHIGHTBOS-26NOV20-B68.5 | 68° to 69° | NO | 78¢ | 8% | 17% | $100 | center 64.25, market mean 66.61, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXHIGHTBOS-26NOV19-B65.5 | 65° to 66° | NO | 56¢ | 22% | 34% | $0 | center 63.25, market mean 64.47, lead 0d |
| +10¢ | KXAAAGASD-26NOV20-3.6950 | Above 3.6950 | YES | 4¢ | 47% | 14% | $0 |  |
| +10¢ | KXHIGHCHI-26NOV19-B62.5 | 62° to 63° | YES | 6¢ | 27% | 16% | $0 | center 64.25, market mean 65.71, lead 0d |
| +10¢ | KXHIGHNY-26NOV19-B61.5 | 61° to 62° | YES | 14¢ | 34% | 24% | $0 | center 62.1, market mean 64.17, lead 0d |
| +9¢ | KXHIGHTSEA-26NOV19-B47.5 | 47° to 48° | YES | 4¢ | 23% | 13% | $0 | center 49.5, market mean 50.39, lead 0d |
| +9¢ | KXHIGHPHIL-26NOV19-B67.5 | 67° to 68° | NO | 32¢ | 21% | 59% | $0 | center 65.2, market mean 67.38, lead 0d |
| +9¢ | KXHIGHTPHX-26NOV20-T70 | 69° or below | YES | 12¢ | 51% | 21% | $0 | center 69.4, market mean 71.52, lead 1d |
| +9¢ | KXAAAGASW-26NOV23-3.6200 | Above 3.6200 | NO | 7¢ | 56% | 84% | $0 |  |
| +9¢ | KXHIGHTMIN-26NOV19-B55.5 | 55° to 56° | NO | 25¢ | 39% | 66% | $0 | center 55.85, market mean 55.93, lead 0d |
| +8¢ | KXHIGHMIA-26NOV19-B80.5 | 80° to 81° | YES | 31¢ | 49% | 40% | $0 | center 80.7, market mean 81.95, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV19-T56 | 55° or below | YES | 9¢ | 27% | 18% | $0 | center 56.65, market mean 57.61, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV19-B58.5 | 58° to 59° | NO | 56¢ | 27% | 36% | $0 | center 56.65, market mean 57.61, lead 0d |
| +8¢ | KXHIGHTDC-26NOV19-B68.5 | 68° to 69° | NO | 56¢ | 27% | 36% | $0 | center 66.7, market mean 67.42, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV19-B75.5 | 75° to 76° | NO | 28¢ | 38% | 64% | $0 | center 75.45, market mean 75.62, lead 0d |
| +8¢ | KXHIGHTMIN-26NOV19-T55 | 54° or below | YES | 6¢ | 22% | 14% | $0 | center 55.85, market mean 55.93, lead 0d |
| +8¢ | KXHIGHTBOS-26NOV20-B66.5 | 66° to 67° | NO | 45¢ | 21% | 47% | $0 | center 64.25, market mean 66.61, lead 1d |
| +7¢ | KXHIGHNY-26NOV19-B65.5 | 65° to 66° | NO | 56¢ | 12% | 37% | $0 | center 62.1, market mean 64.17, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV19-T70 | 69° or below | YES | 3¢ | 18% | 10% | $0 | center 71.25, market mean 72.12, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV19-B72.5 | 72° to 73° | NO | 40¢ | 28% | 53% | $0 | center 71.25, market mean 72.12, lead 0d |
| +7¢ | KXHIGHCHI-26NOV19-B66.5 | 66° to 67° | NO | 46¢ | 21% | 47% | $0 | center 64.25, market mean 65.71, lead 0d |
| +7¢ | KXHIGHLAX-26NOV20-B66.5 | 66° to 67° | NO | 40¢ | 24% | 53% | $0 | center 64.9, market mean 66.45, lead 1d |
| +7¢ | KXHIGHNY-26NOV19-B63.5 | 63° to 64° | NO | 57¢ | 28% | 36% | $0 | center 62.1, market mean 64.17, lead 0d |
| +7¢ | KXHIGHPHIL-26NOV19-B65.5 | 65° to 66° | YES | 19¢ | 34% | 26% | $0 | center 65.2, market mean 67.38, lead 0d |
| +7¢ | KXHIGHTHOU-26NOV19-B75.5 | 75° to 76° | NO | 33¢ | 39% | 60% | $0 | center 75.4, market mean 75.37, lead 0d |
| +7¢ | KXHIGHTATL-26NOV19-T69 | 70° or above | NO | 55¢ | 17% | 38% | $0 | center 67.65, market mean 69.18, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV19-B74.5 | 74° to 75° | NO | 54¢ | 19% | 40% | $0 | center 72.1, market mean 73.39, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV19-B66.5 | 66° to 67° | YES | 7¢ | 34% | 14% | $0 | center 67.55, market mean 69.15, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV19-T63 | 62° or below | YES | 10¢ | 37% | 16% | $0 | center 63.25, market mean 64.47, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV19-B68.5 | 68° to 69° | NO | 52¢ | 34% | 42% | $0 | center 67.55, market mean 69.15, lead 0d |
| +6¢ | KXHIGHTPHX-26NOV19-B73.5 | 73° to 74° | YES | 11¢ | 25% | 17% | $0 | center 75.45, market mean 75.62, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV19-B70.5 | 70° to 71° | YES | 4¢ | 30% | 10% | $0 | center 72.1, market mean 73.39, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV19-B70.5 | 70° to 71° | NO | 60¢ | 14% | 34% | $0 | center 67.55, market mean 69.15, lead 0d |
| +6¢ | KXHIGHTSATX-26NOV19-B70.5 | 70° to 71° | YES | 27¢ | 40% | 33% | $0 | center 71.25, market mean 72.12, lead 0d |
| +6¢ | KXHIGHTDC-26NOV19-B64.5 | 64° to 65° | YES | 9¢ | 22% | 15% | $0 | center 66.7, market mean 67.42, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV19-B72.5 | 72° to 73° | NO | 49¢ | 26% | 45% | $0 | center 70.7, market mean 71.53, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV19-B68.5 | 68° to 69° | YES | 8¢ | 21% | 14% | $0 | center 70.7, market mean 71.53, lead 0d |
| +6¢ | KXHIGHTLV-26NOV19-B61.5 | 61° to 62° | NO | 72¢ | 16% | 22% | $0 | center 59.75, market mean 61.57, lead 0d |
| +6¢ | KXHIGHTATL-26NOV19-B66.5 | 66° to 67° | YES | 6¢ | 31% | 12% | $0 | center 67.65, market mean 69.18, lead 0d |
| +5¢ | KXHIGHTDAL-26NOV19-B72.5 | 72° to 73° | NO | 52¢ | 37% | 43% | $0 | center 72.1, market mean 73.39, lead 0d |
| +5¢ | KXHIGHTOKC-26NOV19-B64.5 | 64° to 65° | YES | 2¢ | 13% | 7% | $0 | center 67.55, market mean 69.15, lead 0d |
