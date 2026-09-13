---
type: runtime-test-report
status: passed
classification: SYNTHETIC / NON-CANON / NON-SEMANTIC
---

# Scene Writer Runtime Test Report V0.1

## Execution

Command:

```powershell
$env:PYTHONPATH = '<Stage>;E:\AI_Film_Studio\AI_Film_Studio_Automation_V0.1'
python -X utf8 -B <Stage>\tests\test_scene_writer_runtime.py
```

Result: `30 / 30 PASS`.

## RT-SW matrix

| Tests | Result | Evidence |
|---|---|---|
| RT-SW-01–03 | PASS | canonical identity, V0.1, and hash-lock fail-safe |
| RT-SW-04–10 | PASS | CREATE, REVISE, DIAGNOSE, six primary-state transports |
| RT-SW-11–16 | PASS | multiple flags; Production, Shared QA, Director, Character & Acting, Deferred contracts |
| RT-SW-17–20 | PASS | illegal mode, malformed/unknown state, unknown flag, display-suffix rejection |
| RT-SW-21–25 | PASS | executor-unbound fail-safe, no fallback, duplicate safety, creative/control separation, no private reasoning field |
| RT-SW-26–30 | PASS | revision/no-change consistency, handoff schema, frozen integrity, synthetic isolation |

## Malformed output matrix

| Case | Condition | Result |
|---|---|---|
| RT-MAL-01 | missing primary state | `REJECT / FAIL_SAFE` |
| RT-MAL-02 | two primary states | `REJECT / FAIL_SAFE` |
| RT-MAL-03 | unknown primary state | `REJECT / FAIL_SAFE` |
| RT-MAL-04 | unknown flag | `REJECT / FAIL_SAFE` |
| RT-MAL-05 | display suffix appended to token | `REJECT / FAIL_SAFE` |
| RT-MAL-06 | `SCENE_REVISED` without revision | `REJECT / FAIL_SAFE` |
| RT-MAL-07 | contradictory rewrite claim on `NO_MATERIAL_CHANGE` | `REJECT / FAIL_SAFE` |
| RT-MAL-08 | malformed handoff packet | `REJECT / FAIL_SAFE` |

## Scope of result

These tests validate only transport, canonical binding, exact-token parsing, contract consistency, routing representation, fail-safe behavior, and test-executor isolation. They make no claim about scene-writing quality or real semantic execution.
