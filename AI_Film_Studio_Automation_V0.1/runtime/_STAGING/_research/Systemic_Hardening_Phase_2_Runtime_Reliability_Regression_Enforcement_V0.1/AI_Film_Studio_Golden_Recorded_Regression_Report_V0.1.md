---
type: golden-recorded-regression-report
status: pass
version: 0.1
run_id: E2E-RUN-05
---

# AI Film Studio Golden Recorded Regression Report V0.1

## Result

`PASS` using the original Rerun 05 evidence root only:

`E:\AI_Film_Studio\AI_Film_Studio_Automation_V0.1\runtime\_STAGING\_research\Minimal_E2E_Runtime_Validation_V0.1\evidence\E2E-RUN-05`

| Check | Recorded result |
| --- | --- |
| Seven role outputs parseable | `7/7` |
| Recorded outcomes preserved | Showrunner `PASS`; Scene Writer `SCENE_CREATED`; Director `DIRECTION_PLAN_PRODUCED`; Character & Acting `PERFORMANCE_INTERPRETATION_READY`; Art Director `DESIGN_RESPONSE_READY`; Continuity `CONTINUITY PRESERVED`; Shared QA `PASS / NO CHANGE` |
| Canonical transport tokens | exact `ABSENT` flags/handoffs preserved for every role |
| Invocation custody | `7` unique run-local invocation IDs; raw/parsed/invocation/persistence paths all in root |
| Handoffs / ledger | `6` / `3`, with append-only ledger true |
| Strict transport | exactly one Beta strict call, Scene Writer only |
| Acceptance evidence | `E2E-INT 18/18 PASS` |
| Retry / fallback / auto-repair | `0 / 0 / 0` |

No historical evidence was moved or changed. `Provider Calls 0`; `Executor Calls 0`; `Real E2E Runs 0` for this replay.

