---
type: executor-binding-test-report
status: passed
classification: NON-NETWORK BINDING TEST
---

# Scene Writer Executor Binding Test Report V0.1

Key status: `DEEPSEEK_API_KEY: AVAILABLE` (value neither read into this report nor logged).

| Test | Result | Evidence |
|---|---|---|
| EB-SW-01 | PASS | exact canonical identity `scene-writer` |
| EB-SW-02 | PASS | exact canonical version `V0.1` |
| EB-SW-03 | PASS | published canonical SHA-256 matches expected hash |
| EB-SW-04 | PASS | shared provider-neutral `ModelExecutor` resolved |
| EB-SW-05 | PASS | shared `DeepSeekProviderAdapter` resolved for `deepseek-v4-pro` |
| EB-SW-06 | PASS | Phase 5 Staging Skill path rejected by exact registry |
| EB-SW-07 | PASS | version mismatch rejected |
| EB-SW-08 | PASS | hash mismatch rejected |
| EB-SW-09 | PASS | malformed structured output reaches Runtime `FAIL_SAFE` |
| EB-SW-10 | PASS | canonical executor only loads Skill, transports the request, and returns JSON to Runtime validation |

`EB-SW-01–10 = 10 / 10 PASS`.

These gates construct the binding but do not call the provider. The single provider call occurred only after this report's gates passed, in `SMOKE-SW-EXEC-01`.
