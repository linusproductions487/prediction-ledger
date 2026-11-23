# Model vs. market

Scanned 2026-11-23 07:28 UTC.

**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus
the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.

## Tradeable candidates

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +7¢ | KXHIGHLAX-26NOV23-B69.5 | 69° to 70° | NO | 52¢ | 30% | 41% | $100 | center 68.17, market mean 68.58, lead 1d |
| +7¢ | KXHIGHTSEA-26NOV23-B51.5 | 51° to 52° | NO | 44¢ | 38% | 49% | $100 | center 51.17, market mean 51.85, lead 1d |
| +6¢ | KXHIGHLAX-26NOV23-B65.5 | 65° to 66° | YES | 3¢ | 17% | 9% | $100 | center 68.17, market mean 68.58, lead 1d |
| +5¢ | KXAAAGASM-26NOV30-3.55 | Above 3.55 | YES | 14¢ | 25% | 19% | $100 |  |

## Not tradeable (gap too large to trust, or the book cannot fill $100)

| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |
|---|---|---|---|---|---|---|---|---|
| +14¢ | KXHIGHTHOU-26NOV23-T68 | 67° or below | NO | 14¢ | 25% | 72% | $0 | center 69.27, market mean 67.04, lead 0d |
| +12¢ | KXHIGHTSATX-26NOV23-B63.5 | 63° to 64° | NO | 34¢ | 43% | 55% | $0 | center 62.97, market mean 64.06, lead 0d |
| +11¢ | KXHIGHAUS-26NOV23-B61.5 | 61° to 62° | NO | 39¢ | 38% | 50% | $0 | center 61.17, market mean 61.66, lead 0d |
| +11¢ | KXHIGHMIA-26NOV23-B79.5 | 79° to 80° | NO | 49¢ | 28% | 40% | $0 | center 79.62, market mean 79.98, lead 0d |
| +10¢ | KXHIGHTLV-26NOV23-B61.5 | 61° to 62° | NO | 21¢ | 33% | 69% | $0 | center 60.72, market mean 61.54, lead 1d |
| +10¢ | KXHIGHTHOU-26NOV23-B68.5 | 68° to 69° | YES | 10¢ | 31% | 20% | $0 | center 69.27, market mean 67.04, lead 0d |
| +10¢ | KXHIGHTHOU-26NOV23-B70.5 | 70° to 71° | YES | 5¢ | 26% | 15% | $0 | center 69.27, market mean 67.04, lead 0d |
| +10¢ | KXHIGHDEN-26NOV23-B42.5 | 42° to 43° | YES | 5¢ | 25% | 15% | $0 | center 40.67, market mean 39.62, lead 0d |
| +9¢ | KXHIGHTATL-26NOV23-T68 | 67° or below | NO | 68¢ | 13% | 23% | $0 | center 69.77, market mean 68.65, lead 0d |
| +9¢ | KXHIGHTSATX-26NOV23-B61.5 | 61° to 62° | YES | 6¢ | 26% | 15% | $0 | center 62.97, market mean 64.06, lead 0d |
| +9¢ | KXHIGHTDC-26NOV23-B68.5 | 68° to 69° | NO | 51¢ | 31% | 40% | $0 | center 68.02, market mean 68.79, lead 0d |
| +9¢ | KXHIGHTNOLA-26NOV23-B70.5 | 70° to 71° | NO | 55¢ | 26% | 36% | $0 | center 72.12, market mean 70.74, lead 0d |
| +9¢ | KXHIGHNY-26NOV23-B66.5 | 66° to 67° | NO | 51¢ | 31% | 40% | $0 | center 67.38, market mean 67.14, lead 0d |
| +9¢ | KXHIGHTPHX-26NOV23-B68.5 | 68° to 69° | NO | 44¢ | 38% | 47% | $0 | center 68.27, market mean 69.39, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV23-B55.5 | 55° to 56° | YES | 10¢ | 28% | 18% | $0 | center 57.17, market mean 57.69, lead 0d |
| +8¢ | KXHIGHDEN-26NOV23-T40 | 39° or below | NO | 49¢ | 31% | 43% | $0 | center 40.67, market mean 39.62, lead 0d |
| +8¢ | KXHIGHTPHX-26NOV23-B70.5 | 70° to 71° | NO | 61¢ | 22% | 31% | $0 | center 68.27, market mean 69.39, lead 0d |
| +8¢ | KXHIGHTOKC-26NOV23-T48 | 47° or below | YES | 2¢ | 37% | 10% | $0 | center 48.17, market mean 49.7, lead 0d |
| +8¢ | KXHIGHCHI-26NOV23-B44.5 | 44° to 45° | YES | 8¢ | 25% | 16% | $0 | center 42.52, market mean 41.94, lead 0d |
| +8¢ | KXHIGHTSFO-26NOV23-B57.5 | 57° to 58° | NO | 33¢ | 33% | 59% | $0 | center 57.52, market mean 57.83, lead 1d |
| +8¢ | KXHIGHTPHX-26NOV23-T68 | 67° or below | YES | 2¢ | 35% | 10% | $0 | center 68.27, market mean 69.39, lead 0d |
| +8¢ | KXHIGHTDAL-26NOV23-B57.5 | 57° to 58° | NO | 28¢ | 38% | 64% | $0 | center 57.17, market mean 57.69, lead 0d |
| +8¢ | KXHIGHAUS-26NOV23-T61 | 60° or below | YES | 21¢ | 37% | 29% | $0 | center 61.17, market mean 61.66, lead 0d |
| +7¢ | KXHIGHTMIN-26NOV23-B32.5 | 32° to 33° | NO | 31¢ | 39% | 62% | $0 | center 32.17, market mean 32.13, lead 0d |
| +7¢ | KXHIGHCHI-26NOV23-B42.5 | 42° to 43° | NO | 47¢ | 38% | 46% | $0 | center 42.52, market mean 41.94, lead 0d |
| +7¢ | KXHIGHTMIN-26NOV23-B34.5 | 34° to 35° | YES | 6¢ | 21% | 13% | $0 | center 32.17, market mean 32.13, lead 0d |
| +7¢ | KXHIGHPHIL-26NOV23-B71.5 | 71° to 72° | YES | 2¢ | 16% | 9% | $0 | center 68.58, market mean 68.67, lead 0d |
| +7¢ | KXHIGHMIA-26NOV23-B81.5 | 81° to 82° | NO | 64¢ | 22% | 29% | $0 | center 79.62, market mean 79.98, lead 0d |
| +6¢ | KXHIGHTBOS-26NOV23-B64.5 | 64° to 65° | YES | 11¢ | 25% | 17% | $0 | center 66.33, market mean 66.86, lead 0d |
| +6¢ | KXHIGHTATL-26NOV23-B70.5 | 70° to 71° | YES | 25¢ | 37% | 31% | $0 | center 69.77, market mean 68.65, lead 0d |
| +6¢ | KXHIGHTATL-26NOV23-B72.5 | 72° to 73° | YES | 5¢ | 17% | 11% | $0 | center 69.77, market mean 68.65, lead 0d |
| +6¢ | KXHIGHTOKC-26NOV23-B50.5 | 50° to 51° | NO | 53¢ | 21% | 41% | $0 | center 48.17, market mean 49.7, lead 0d |
| +6¢ | KXHIGHTDC-26NOV23-T66 | 65° or below | YES | 2¢ | 14% | 8% | $0 | center 68.02, market mean 68.79, lead 0d |
| +6¢ | KXHIGHTDC-26NOV23-B66.5 | 66° to 67° | YES | 17¢ | 29% | 23% | $0 | center 68.02, market mean 68.79, lead 0d |
| +5¢ | KXHIGHMIA-26NOV23-T77 | 76° or below | YES | 2¢ | 13% | 7% | $0 | center 79.62, market mean 79.98, lead 0d |
| +5¢ | KXHIGHTNOLA-26NOV23-B76.5 | 76° to 77° | YES | 2¢ | 13% | 7% | $0 | center 72.12, market mean 70.74, lead 0d |
| +3¢ | KXHIGHTLV-26NOV23-B59.5 | 59° to 60° | YES | 17¢ | 31% | 20% | $100 | center 60.72, market mean 61.54, lead 1d |
| +1¢ | KXHIGHTSEA-26NOV23-B49.5 | 49° to 50° | YES | 15¢ | 25% | 16% | $100 | center 51.17, market mean 51.85, lead 1d |
| +1¢ | KXHIGHTSFO-26NOV23-B55.5 | 55° to 56° | YES | 16¢ | 26% | 17% | $100 | center 57.52, market mean 57.83, lead 1d |
