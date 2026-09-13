---
type: e2e-run-04-execution-manifest
status: blocked-awaiting-user-review
version: 0.1
date: 2026-08-28
---

# AI Film Studio E2E Run 04 Execution Manifest V0.1

| Item | Actual value |
| --- | --- |
| Run ID | `E2E-RUN-04` |
| Authorization | `Minimal E2E Runtime Validation Rerun 04 V0.1` |
| Fixture | `E2E-FIX-01` |
| Provider / Model | DeepSeek / `deepseek-v4-pro` |
| Primary-call budget / used | `7 / 5` |
| Retries / fallbacks / recovery budget | `0 / 0 / 0` |
| Result | `BLOCKED` at Art Director local contract validation |

## Actual evidence root

`E:\AI_Film_Studio\AI_Film_Studio_Automation_V0.1\runtime\_STAGING\_research\Minimal_E2E_Runtime_Validation_V0.1\runtime\_STAGING\_research\Minimal_E2E_Runtime_Validation_V0.1\evidence\E2E-RUN-04`

The root is nonstandard because the execution environment received a stage-relative evidence path while already running from the Minimal E2E stage. No evidence was moved or overwritten after the run. The runtime `execution_manifest.json` correctly records the Rerun 04 ID and authorization, but does not contain an explicit evidence-root or invocation-ID field; this document is an additive metadata disclosure, not a mutation of the immutable run proof.

## Invocation IDs

`E2E-RUN-04:showrunner:1` · `E2E-RUN-04:scene_writer:1` · `E2E-RUN-04:director:1` · `E2E-RUN-04:character_acting:1` · `E2E-RUN-04:art_director:1`

Continuity and Shared QA were not invoked.
