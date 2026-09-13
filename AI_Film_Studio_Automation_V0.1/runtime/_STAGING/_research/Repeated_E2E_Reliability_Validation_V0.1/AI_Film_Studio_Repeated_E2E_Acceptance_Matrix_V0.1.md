---
type: repeated-e2e-acceptance-matrix
status: not-reached
version: 0.1
---

# AI Film Studio Repeated E2E Acceptance Matrix V0.1

| Run | Fixture | Provider calls | E2E-INT | Integrity | Status |
| --- | --- | --- | --- | --- | --- |
| RUN-R01 | E2E-FIX-01 Golden replay (`E2E-RUN-06`) | `2` | `0/18 NOT REACHED` | FAIL | BLOCKED at Scene Writer schema validation |
| RUN-R02 | E2E-FIX-02 | `0` | NOT RUN | NOT RUN | NOT REACHED |
| RUN-R03 | E2E-FIX-03 | `0` | NOT RUN | NOT RUN | NOT REACHED |

No rows may be averaged. R02/R03 remain unstarted because R01 produced a blocking Scene Writer transport/schema failure.
