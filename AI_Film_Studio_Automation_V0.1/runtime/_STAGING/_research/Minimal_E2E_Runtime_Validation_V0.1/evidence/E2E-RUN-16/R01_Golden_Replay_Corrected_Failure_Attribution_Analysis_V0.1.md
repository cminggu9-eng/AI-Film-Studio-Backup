# R01 Golden Replay Corrected Failure Attribution Analysis V0.1

This is an additive analysis. `failure_attribution.json` and the raw evidence remain immutable.

## Earliest failure layer

`CHARACTER & ACTING INTEGRATION MACHINE-CONTRACT FAILURE — MISSING REQUIRED TRANSPORT FIELD scene_packages`

## Layer separation

| Layer | Decision | Evidence |
|---|---|---|
| Provider / HTTP | PASS | HTTP 200, provider invocation ID present |
| Completion / truncation | PASS | `finish_reason=stop`, `NOT_TRUNCATED`, complete JSON |
| JSON parse | PASS | nine-field JSON object parsed successfully |
| Raw-first persistence | PASS | raw, usage, invocation, finish reason, trace and verification persisted |
| Integration machine contract | FAIL | required tenth field `scene_packages` absent |
| Canonical semantic failure | NOT ESTABLISHED | valid canonical outcome and non-empty semantic content existed; validation stopped at structure |
| Handoff to Art Director | NOT REACHED | no Character & Acting output artifact or envelope was assembled |

The runner's frozen failure record uses the broader label `EXECUTOR FAILURE`. The more precise evidence-backed attribution is a missing required transport field, not Provider failure, HTTP failure, truncation, JSON parse failure, or proven canonical semantic failure.

## Next exact repair boundary

Character & Acting non-strict integration output contract / reserved transport-slot compliance only. A future authorized repair must establish the authority for `scene_packages=ABSENT` and align prompt, transport representation, and validator without semantic auto-fill. No repair is performed in this run.

