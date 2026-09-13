# Scene Writer Full Semantic Validation Cost Report V0.1

All figures are estimates from the existing DeepSeek adapter's recorded token basis, not billing statements. A verification cost is `N/A` when Runtime rejected generation before semantic verification.

| Fixture | Generation tokens in/out | Generation latency | Generation CNY | Verification tokens in/out | Verification latency | Verification CNY | Total CNY |
|---|---:|---:|---:|---:|---:|---:|---:|
| F01 | 4,268 / 742 | 16,176 ms | 0.0081168 | 2,037 / 18 | 1,936 ms | 0.0039342 | 0.0120510 |
| F02 | 4,153 / 548 | 13,302 ms | 0.0066078 | 1,751 / 18 | 3,066 ms | 0.0030762 | 0.0096840 |
| F03 | 4,136 / 444 | 10,905 ms | 0.0055520 | 1,640 / 18 | 2,407 ms | 0.0027432 | 0.0082952 |
| F04 | 4,152 / 625 | 15,234 ms | 0.0066860 | 1,820 / 18 | 3,233 ms | 0.0032832 | 0.0099692 |
| F05 | 4,193 / 460 | 10,314 ms | 0.0058190 | 1,699 / 18 | 2,323 ms | 0.0029202 | 0.0087392 |
| F06 | 4,165 / 538 | 12,020 ms | 0.0062030 | N/A | N/A | N/A | 0.0062030 |
| F07 | 4,183 / 491 | 12,337 ms | 0.0059750 | 1,725 / 18 | 2,550 ms | 0.0029982 | 0.0089732 |
| F08 | 4,359 / 535 | 11,982 ms | 0.0067670 | 1,919 / 18 | 1,816 ms | 0.0035802 | 0.0103472 |
| F09 | 4,197 / 453 | 10,133 ms | 0.0057890 | 1,717 / 18 | 2,551 ms | 0.0029742 | 0.0087632 |
| F10 | 4,341 / 434 | 9,953 ms | 0.0061070 | 1,762 / 18 | 3,118 ms | 0.0031092 | 0.0092162 |
| F11 | 4,189 / 366 | 8,072 ms | 0.0052430 | N/A | N/A | N/A | 0.0052430 |
| F12 | 4,041 / 367 | 10,540 ms | 0.0048050 | N/A | N/A | N/A | 0.0048050 |
| F13-A | 3,768 / 273 | 8,419 ms | 0.0034220 | N/A | N/A | N/A | 0.0034220 |
| F13-B | 4,078 / 602 | 12,686 ms | 0.0063260 | N/A | N/A | N/A | 0.0063260 |
| F14 | 4,185 / 929 | 17,221 ms | 0.0086090 | 2,029 / 18 | 2,349 ms | 0.0039102 | 0.0125192 |

## Aggregate

- Formal executions: `15`; resamples: `0`; automatic retries: `0`.
- Generation: input `62,408`; output `7,807`; latency `179,294 ms`; estimated `CNY 0.0920276`.
- Verification: `10` calls; input `18,099`; output `180`; latency `25,349 ms`; estimated `CNY 0.0325290`.
- Full validation estimated cost: `CNY 0.1245566`.

Five generation calls incurred cost but did not reach verification because Runtime correctly rejected their malformed executor output.

The raw runner summary's `CNY 0.0985576` only sums fixtures whose combined generation-plus-verification field was non-null. This report recomputes the full cost from each recorded generation and verification usage record, including the five rejected generation calls; `CNY 0.1245566` is the complete validation estimate.
