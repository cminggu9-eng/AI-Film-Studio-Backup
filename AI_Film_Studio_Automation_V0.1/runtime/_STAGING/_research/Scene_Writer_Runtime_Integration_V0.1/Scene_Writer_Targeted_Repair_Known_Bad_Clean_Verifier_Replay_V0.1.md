# Known Bad / Clean Verifier Replay Report V0.1

## Frozen evidence set

Known human-fail outputs: F03, F09, F10, F14, and `SMOKE-SW-EXEC-01` (no regeneration). Known clean outputs: F04, F05, F07, F08.

## Results

- First two attempts: all four clean outputs returned `PASS`; F03 returned `PASS` despite the confirmed unsupported prior-work claim. The remaining four known-bad cases were not reached because the atomic known-bad group correctly stopped on the failed F03 assertion.
- Claim-audit attempt: F03 still returned `PASS`; its retained audit did not include the exact prior-work clause. The independent adjudicator also returned `PASS`.
- Exhaustive-candidate attempt: F03 and the first clean replay failed at provider JSON transport. No semantic PASS/FAIL can be claimed for that attempt.

## Acceptance

Known Bad detection is not `100%`; Clean Replay reliability is not demonstrably stable under the final verifier structure. The replay acceptance gate therefore fails.
