# Model vs. market

Scanned 2026-11-22 21:37 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +11¢ | KXHIGHCHI-26NOV23-B40.5 | 40° to 41° | NO | 60¢ | 18% | 29% | $100 | center 43.17, market mean 41.82, lead 1d |
| +9¢ | KXAAAGASM-26NOV30-3.55 | Above 3.55 | YES | 7¢ | 25% | 16% | $100 |  |
| +7¢ | KXHIGHAUS-26NOV23-B61.5 | 61° to 62° | NO | 53¢ | 28% | 40% | $100 | center 61.22, market mean 61.4, lead 1d |
| +7¢ | KXHIGHLAX-26NOV23-B69.5 | 69° to 70° | NO | 53¢ | 29% | 40% | $100 | center 68.08, market mean 68.8, lead 1d |
| +6¢ | KXHIGHTBOS-26NOV23-B68.5 | 68° to 69° | NO | 72¢ | 10% | 22% | $100 | center 65.08, market mean 66.73, lead 1d |
| +5¢ | KXHIGHTPHX-26NOV23-B68.5 | 68° to 69° | NO | 47¢ | 36% | 48% | $100 | center 68.37, market mean 69.34, lead 1d |
| +5¢ | KXHIGHPHIL-26NOV23-B67.5 | 67° to 68° | NO | 55¢ | 30% | 40% | $100 | center 67.38, market mean 68.16, lead 1d |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +15¢ | KXHIGHNY-26NOV22-T61 | 60° or below | NO | 7¢ | 30% | 78% | $0 | center 61.42, market mean 59.76, lead 0d |
| +14¢ | KXHIGHDEN-26NOV22-B45.5 | 45° to 46° | NO | 14¢ | 27% | 72% | $0 | center 47.22, market mean 45.25, lead 0d |
| +13¢ | KXAAAGASW-26NOV23-3.6350 | Above 3.6350 | NO | 40¢ | 1% | 47% | $0 |  |
| +13¢ | KXAAAGASD-26NOV23-3.6350 | Above 3.6350 | NO | 38¢ | 1% | 49% | $0 |  |
| +13¢ | KXHIGHTHOU-26NOV23-T68 | 67° or below | NO | 11¢ | 35% | 76% | $0 | center 68.58, market mean 67.01, lead 1d |
| +12¢ | KXHIGHTSEA-26NOV22-B47.5 | 47° to 48° | NO | 8¢ | 44% | 80% | $0 | center 46.38, market mean 47.72, lead 0d |
| +12¢ | KXHIGHNY-26NOV22-B61.5 | 61° to 62° | YES | 7¢ | 30% | 18% | $0 | center 61.42, market mean 59.76, lead 0d |
| +11¢ | KXHIGHTSFO-26NOV22-B57.5 | 57° to 58° | YES | 2¢ | 25% | 13% | $0 | center 55.42, market mean 54.86, lead 0d |
| +10¢ | KXHIGHDEN-26NOV23-T40 | 39° or below | NO | 31¢ | 26% | 59% | $0 | center 41.32, market mean 39.35, lead 1d |
| +9¢ | KXHIGHTSFO-26NOV22-B55.5 | 55° to 56° | NO | 38¢ | 41% | 53% | $0 | center 55.42, market mean 54.86, lead 0d |
| +9¢ | KXHIGHLAX-26NOV22-B67.5 | 67° to 68° | NO | 4¢ | 56% | 87% | $0 | center 67.47, market mean 67.56, lead 0d |
| +9¢ | KXHIGHTLV-26NOV23-B61.5 | 61° to 62° | NO | 23¢ | 35% | 68% | $0 | center 61.17, market mean 61.49, lead 1d |
| +8¢ | KXHIGHDEN-26NOV22-B47.5 | 47° to 48° | YES | 2¢ | 38% | 10% | $0 | center 47.22, market mean 45.25, lead 0d |
| +7¢ | KXHIGHLAX-26NOV22-B69.5 | 69° to 70° | YES | 3¢ | 35% | 10% | $0 | center 67.47, market mean 67.56, lead 0d |
| +7¢ | KXHIGHTPHX-26NOV23-T68 | 67° or below | YES | 3¢ | 34% | 10% | $0 | center 68.37, market mean 69.34, lead 1d |
| +7¢ | KXHIGHTPHX-26NOV22-B73.5 | 73° to 74° | NO | 18¢ | 43% | 75% | $0 | center 72.62, market mean 73.73, lead 0d |
| +7¢ | KXHIGHMIA-26NOV23-B79.5 | 79° to 80° | NO | 46¢ | 25% | 47% | $0 | center 79.88, market mean 79.53, lead 1d |
| +6¢ | KXHIGHNY-26NOV23-B66.5 | 66° to 67° | NO | 47¢ | 26% | 47% | $0 | center 67.17, market mean 66.6, lead 1d |
| +6¢ | KXHIGHTDC-26NOV23-T66 | 65° or below | YES | 5¢ | 33% | 11% | $0 | center 67.02, market mean 68.28, lead 1d |
| +6¢ | KXHIGHTSEA-26NOV23-B51.5 | 51° to 52° | NO | 44¢ | 31% | 50% | $0 | center 50.17, market mean 51.28, lead 1d |
| +6¢ | KXHIGHAUS-26NOV22-B75.5 | 75° to 76° | YES | 3¢ | 30% | 9% | $0 | center 73.4, market mean 73.62, lead 0d |
| +6¢ | KXHIGHTLV-26NOV22-B58.5 | 58° to 59° | NO | 42¢ | 40% | 52% | $0 | center 57.88, market mean 57.81, lead 0d |
| +6¢ | KXHIGHTDC-26NOV23-B68.5 | 68° to 69° | NO | 54¢ | 21% | 40% | $0 | center 67.02, market mean 68.28, lead 1d |
| +5¢ | KXHIGHTHOU-26NOV22-B81.5 | 81° to 82° | NO | 23¢ | 44% | 72% | $0 | center 81.17, market mean 81.8, lead 0d |
| +5¢ | KXHIGHTATL-26NOV23-B68.5 | 68° to 69° | NO | 59¢ | 27% | 36% | $100 | center 70.02, market mean 68.69, lead 1d |
| +4¢ | KXHIGHTBOS-26NOV23-B64.5 | 64° to 65° | YES | 22¢ | 36% | 26% | $100 | center 65.08, market mean 66.73, lead 1d |
| +4¢ | KXHIGHCHI-26NOV23-B44.5 | 44° to 45° | YES | 15¢ | 30% | 19% | $100 | center 43.17, market mean 41.82, lead 1d |
| +4¢ | KXAAAGASM-26NOV30-3.50 | Above 3.50 | YES | 52¢ | 63% | 56% | $100 |  |
| +4¢ | KXHIGHLAX-26NOV23-B65.5 | 65° to 66° | YES | 6¢ | 18% | 10% | $100 | center 68.08, market mean 68.8, lead 1d |
| +4¢ | KXHIGHTSFO-26NOV23-B57.5 | 57° to 58° | NO | 51¢ | 35% | 45% | $100 | center 57.72, market mean 57.82, lead 1d |
| +3¢ | KXHIGHTHOU-26NOV23-B68.5 | 68° to 69° | YES | 13¢ | 29% | 16% | $100 | center 68.58, market mean 67.01, lead 1d |
| +3¢ | KXHIGHDEN-26NOV23-B42.5 | 42° to 43° | YES | 11¢ | 25% | 14% | $100 | center 41.32, market mean 39.35, lead 1d |
| +3¢ | KXHIGHCHI-26NOV23-B42.5 | 42° to 43° | NO | 56¢ | 34% | 41% | $100 | center 43.17, market mean 41.82, lead 1d |
| +3¢ | KXHIGHTMIN-26NOV23-B32.5 | 32° to 33° | NO | 50¢ | 35% | 47% | $100 | center 32.17, market mean 32.04, lead 1d |
| +2¢ | KXHIGHPHIL-26NOV23-B69.5 | 69° to 70° | NO | 68¢ | 24% | 30% | $100 | center 67.38, market mean 68.16, lead 1d |
| +2¢ | KXHIGHTHOU-26NOV23-B70.5 | 70° to 71° | YES | 11¢ | 22% | 13% | $100 | center 68.58, market mean 67.01, lead 1d |
| +2¢ | KXHIGHPHIL-26NOV23-B65.5 | 65° to 66° | YES | 14¢ | 22% | 16% | $100 | center 67.38, market mean 68.16, lead 1d |
| +2¢ | KXHIGHTATL-26NOV23-T68 | 67° or below | NO | 78¢ | 14% | 20% | $100 | center 70.02, market mean 68.69, lead 1d |
| +2¢ | KXHIGHTPHX-26NOV23-B70.5 | 70° to 71° | NO | 68¢ | 23% | 30% | $100 | center 68.37, market mean 69.34, lead 1d |
| +2¢ | KXHIGHTOKC-26NOV23-T48 | 47° or below | YES | 12¢ | 23% | 13% | $100 | center 48.82, market mean 49.55, lead 1d |
