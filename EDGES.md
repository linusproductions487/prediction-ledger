# Model vs. market

Scanned 2026-11-19 15:33 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +10¢ | KXAAAGASW-26NOV23-3.6300 | Above 3.6300 | NO | 43¢ | 37% | 47% | $100 |  |
| +10¢ | KXHIGHMIA-26NOV19-B80.5 | 80° to 81° | YES | 41¢ | 62% | 51% | $100 | center 80.0, market mean 81.8, lead 0d |
| +9¢ | KXAAAGASM-26NOV30-3.45 | Above 3.45 | NO | 9¢ | 72% | 82% | $100 |  |
| +8¢ | KXHIGHAUS-26NOV19-B74.5 | 74° to 75° | NO | 65¢ | 16% | 27% | $100 | center 71.9, market mean 73.2, lead 0d |
| +8¢ | KXHIGHCHI-26NOV19-B66.5 | 66° to 67° | NO | 48¢ | 35% | 44% | $100 | center 66.0, market mean 65.61, lead 0d |
| +7¢ | KXAAAGASD-26NOV20-3.6900 | Above 3.6900 | YES | 74¢ | 88% | 81% | $100 |  |
| +6¢ | KXHIGHDEN-26NOV19-B52.5 | 52° to 53° | NO | 74¢ | 11% | 20% | $100 | center 55.8, market mean 53.87, lead 0d |
| +6¢ | KXHIGHTHOU-26NOV20-B77.5 | 77° to 78° | NO | 68¢ | 16% | 26% | $0 | center 74.8, market mean 76.32, lead 1d |
| +6¢ | KXHIGHNY-26NOV20-B62.5 | 62° to 63° | YES | 4¢ | 17% | 10% | $0 | center 65.3, market mean 66.68, lead 1d |
| +6¢ | KXHIGHNY-26NOV20-B64.5 | 64° to 65° | YES | 17¢ | 30% | 23% | $0 | center 65.3, market mean 66.68, lead 1d |
| +6¢ | KXHIGHDEN-26NOV19-T57 | 58° or above | YES | 7¢ | 20% | 13% | $0 | center 55.8, market mean 53.87, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV20-B64.5 | 64° to 65° | YES | 3¢ | 16% | 9% | $0 | center 67.5, market mean 68.85, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV19-B64.5 | 64° to 65° | YES | 2¢ | 15% | 8% | $0 | center 67.4, market mean 69.15, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV20-B64.5 | 64° to 65° | NO | 63¢ | 24% | 31% | $0 | center 62.7, market mean 65.44, lead 1d |
| +6¢ | KXHIGHTPHX-26NOV19-B77.5 | 77° to 78° | YES | 13¢ | 25% | 19% | $0 | center 75.6, market mean 75.61, lead 0d |
| +6¢ | KXHIGHTLV-26NOV20-B60.5 | 60° to 61° | YES | 13¢ | 25% | 19% | $0 | center 58.3, market mean 58.4, lead 1d |
| +6¢ | KXHIGHTNOLA-26NOV19-B70.5 | 70° to 71° | NO | 59¢ | 29% | 35% | $0 | center 70.8, market mean 71.5, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV20-B67.5 | 67° to 68° | YES | 16¢ | 30% | 22% | $0 | center 68.5, market mean 69.76, lead 1d |
| +6¢ | KXHIGHLAX-26NOV19-B66.5 | 66° to 67° | NO | 50¢ | 38% | 44% | $0 | center 65.9, market mean 66.27, lead 0d |
| +6¢ | KXHIGHTPHX-26NOV19-B73.5 | 73° to 74° | YES | 11¢ | 23% | 17% | $0 | center 75.6, market mean 75.61, lead 0d |
| +6¢ | KXHIGHPHIL-26NOV19-B69.5 | 69° to 70° | NO | 88¢ | 0% | 6% | $0 | center 63.2, market mean 67.35, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV20-T72 | 71° or below | YES | 2¢ | 14% | 8% | $0 | center 74.2, market mean 75.23, lead 1d |
| +6¢ | KXHIGHTLV-26NOV20-T56 | 55° or below | YES | 4¢ | 16% | 10% | $0 | center 58.3, market mean 58.4, lead 1d |
| +6¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | NO | 42¢ | 46% | 52% | $0 |  |
| +6¢ | KXHIGHAUS-26NOV19-B72.5 | 72° to 73° | NO | 52¢ | 36% | 43% | $0 | center 71.9, market mean 73.2, lead 0d |
| +5¢ | KXHIGHTLV-26NOV19-B57.5 | 57° to 58° | YES | 7¢ | 18% | 12% | $0 | center 61.0, market mean 61.68, lead 0d |
| +5¢ | KXHIGHPHIL-26NOV20-B66.5 | 66° to 67° | YES | 15¢ | 29% | 20% | $0 | center 67.5, market mean 68.85, lead 1d |
| +5¢ | KXHIGHTBOS-26NOV19-B65.5 | 65° to 66° | NO | 56¢ | 32% | 39% | $0 | center 64.4, market mean 64.47, lead 0d |
| +5¢ | KXHIGHTNOLA-26NOV19-B68.5 | 68° to 69° | YES | 8¢ | 20% | 13% | $0 | center 70.8, market mean 71.5, lead 0d |
| +5¢ | KXHIGHCHI-26NOV20-T66 | 65° or below | YES | 5¢ | 16% | 10% | $0 | center 68.0, market mean 67.99, lead 1d |
| +5¢ | KXHIGHTSFO-26NOV20-B59.5 | 59° to 60° | NO | 65¢ | 22% | 30% | $0 | center 57.4, market mean 58.36, lead 1d |
| +5¢ | KXHIGHTDAL-26NOV19-B72.5 | 72° to 73° | NO | 52¢ | 37% | 43% | $0 | center 72.2, market mean 73.39, lead 0d |
| +5¢ | KXHIGHTATL-26NOV19-B64.5 | 64° to 65° | YES | 2¢ | 12% | 7% | $0 | center 67.4, market mean 69.18, lead 0d |
| +5¢ | KXHIGHTATL-26NOV19-B68.5 | 68° to 69° | NO | 53¢ | 36% | 42% | $0 | center 67.4, market mean 69.18, lead 0d |
| +5¢ | KXHIGHTSEA-26NOV19-B51.5 | 51° to 52° | NO | 63¢ | 25% | 32% | $0 | center 49.5, market mean 50.38, lead 0d |
| +5¢ | KXHIGHTDAL-26NOV20-B72.5 | 72° to 73° | YES | 16¢ | 26% | 21% | $0 | center 74.2, market mean 75.23, lead 1d |
| +5¢ | KXHIGHTLV-26NOV19-T62 | 63° or above | NO | 55¢ | 33% | 40% | $0 | center 61.0, market mean 61.68, lead 0d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +16¢ | KXHIGHPHIL-26NOV19-B67.5 | 67° to 68° | NO | 31¢ | 4% | 53% | $0 | center 63.2, market mean 67.35, lead 0d |
| +11¢ | KXHIGHTPHX-26NOV20-T70 | 69° or below | YES | 12¢ | 61% | 23% | $0 | center 68.8, market mean 71.54, lead 1d |
| +10¢ | KXAAAGASD-26NOV20-3.6950 | Above 3.6950 | YES | 4¢ | 47% | 14% | $0 |  |
| +9¢ | KXHIGHMIA-26NOV20-T80 | 79° or below | YES | 3¢ | 40% | 12% | $0 | center 80.1, market mean 82.77, lead 1d |
| +9¢ | KXHIGHTSFO-26NOV19-T56 | 55° or below | YES | 9¢ | 48% | 18% | $0 | center 55.4, market mean 57.61, lead 0d |
| +9¢ | KXHIGHTDC-26NOV19-B68.5 | 68° to 69° | NO | 56¢ | 7% | 35% | $0 | center 64.6, market mean 67.42, lead 0d |
| +9¢ | KXAAAGASW-26NOV23-3.6200 | Above 3.6200 | NO | 7¢ | 56% | 84% | $0 |  |
| +8¢ | KXHIGHTMIN-26NOV19-B55.5 | 55° to 56° | NO | 25¢ | 40% | 67% | $0 | center 55.4, market mean 55.92, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV19-B75.5 | 75° to 76° | NO | 28¢ | 38% | 64% | $0 | center 75.6, market mean 75.61, lead 0d |
| +7¢ | KXHIGHLAX-26NOV20-B66.5 | 66° to 67° | NO | 38¢ | 25% | 55% | $0 | center 64.8, market mean 66.47, lead 1d |
| +7¢ | KXHIGHTATL-26NOV19-T69 | 70° or above | NO | 55¢ | 14% | 38% | $0 | center 67.4, market mean 69.18, lead 0d |
| +7¢ | KXHIGHTSFO-26NOV19-B58.5 | 58° to 59° | NO | 56¢ | 14% | 37% | $0 | center 55.4, market mean 57.61, lead 0d |
| +7¢ | KXHIGHTSATX-26NOV19-B72.5 | 72° to 73° | NO | 42¢ | 25% | 51% | $0 | center 71.0, market mean 72.07, lead 0d |
| +7¢ | KXHIGHTOKC-26NOV19-B66.5 | 66° to 67° | YES | 7¢ | 36% | 14% | $0 | center 67.4, market mean 69.15, lead 0d |
| +7¢ | KXHIGHTBOS-26NOV20-B66.5 | 66° to 67° | NO | 45¢ | 26% | 48% | $0 | center 64.9, market mean 66.53, lead 1d |
| +6¢ | KXHIGHMIA-26NOV20-B82.5 | 82° to 83° | NO | 45¢ | 20% | 49% | $0 | center 80.1, market mean 82.77, lead 1d |
| +6¢ | KXHIGHTHOU-26NOV19-B75.5 | 75° to 76° | NO | 34¢ | 38% | 59% | $0 | center 76.0, market mean 75.37, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV19-B70.5 | 70° to 71° | NO | 60¢ | 12% | 33% | $0 | center 67.4, market mean 69.15, lead 0d |
| +6¢ | KXHIGHTDC-26NOV19-B64.5 | 64° to 65° | YES | 10¢ | 38% | 16% | $0 | center 64.6, market mean 67.42, lead 0d |
| +6¢ | KXHIGHNY-26NOV19-B65.5 | 65° to 66° | NO | 57¢ | 13% | 37% | $0 | center 62.2, market mean 64.12, lead 0d |
| +6¢ | KXHIGHDEN-26NOV20-B63.5 | 63° to 64° | NO | 56¢ | 16% | 38% | $0 | center 60.5, market mean 62.39, lead 1d |
| +6¢ | KXHIGHTATL-26NOV19-B66.5 | 66° to 67° | YES | 6¢ | 34% | 12% | $0 | center 67.4, market mean 69.18, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV19-B74.5 | 74° to 75° | NO | 54¢ | 20% | 40% | $0 | center 72.2, market mean 73.39, lead 0d |
| +6¢ | KXHIGHTNOLA-26NOV19-B72.5 | 72° to 73° | NO | 50¢ | 25% | 44% | $0 | center 70.8, market mean 71.5, lead 0d |
| +6¢ | KXHIGHTDAL-26NOV19-B70.5 | 70° to 71° | YES | 4¢ | 29% | 10% | $0 | center 72.2, market mean 73.39, lead 0d |
| +6¢ | KXHIGHTMIN-26NOV20-T62 | 61° or below | YES | 4¢ | 32% | 10% | $0 | center 62.7, market mean 65.44, lead 1d |
| +6¢ | KXHIGHTOKC-26NOV20-B69.5 | 69° to 70° | NO | 46¢ | 28% | 48% | $0 | center 68.5, market mean 69.76, lead 1d |
| +5¢ | KXHIGHAUS-26NOV19-B70.5 | 70° to 71° | YES | 9¢ | 33% | 14% | $0 | center 71.9, market mean 73.2, lead 0d |
| +5¢ | KXHIGHTLV-26NOV20-B58.5 | 58° to 59° | NO | 40¢ | 25% | 55% | $0 | center 58.3, market mean 58.4, lead 1d |
| +5¢ | KXHIGHMIA-26NOV19-B82.5 | 82° to 83° | NO | 43¢ | 32% | 52% | $0 | center 80.0, market mean 81.8, lead 0d |
| +5¢ | KXHIGHNY-26NOV19-B63.5 | 63° to 64° | NO | 59¢ | 28% | 36% | $100 | center 62.2, market mean 64.12, lead 0d |
| +4¢ | KXHIGHNY-26NOV19-B61.5 | 61° to 62° | YES | 18¢ | 31% | 22% | $100 | center 62.2, market mean 64.12, lead 0d |
| +4¢ | KXHIGHTDC-26NOV19-B66.5 | 66° to 67° | NO | 61¢ | 26% | 34% | $100 | center 64.6, market mean 67.42, lead 0d |
| +4¢ | KXHIGHDEN-26NOV19-B56.5 | 56° to 57° | YES | 20¢ | 36% | 24% | $100 | center 55.8, market mean 53.87, lead 0d |
| +4¢ | KXHIGHTOKC-26NOV19-B68.5 | 68° to 69° | NO | 55¢ | 33% | 41% | $100 | center 67.4, market mean 69.15, lead 0d |
| +4¢ | KXHIGHTMIN-26NOV19-T55 | 54° or below | YES | 13¢ | 28% | 17% | $100 | center 55.4, market mean 55.92, lead 0d |
| +3¢ | KXHIGHTBOS-26NOV20-B68.5 | 68° to 69° | NO | 78¢ | 12% | 19% | $100 | center 64.9, market mean 66.53, lead 1d |
| +3¢ | KXHIGHNY-26NOV20-B66.5 | 66° to 67° | NO | 59¢ | 28% | 38% | $100 | center 65.3, market mean 66.68, lead 1d |
| +3¢ | KXHIGHNY-26NOV20-B68.5 | 68° to 69° | NO | 73¢ | 14% | 24% | $100 | center 65.3, market mean 66.68, lead 1d |
| +3¢ | KXHIGHDEN-26NOV20-B59.5 | 59° to 60° | YES | 15¢ | 28% | 18% | $100 | center 60.5, market mean 62.39, lead 1d |
