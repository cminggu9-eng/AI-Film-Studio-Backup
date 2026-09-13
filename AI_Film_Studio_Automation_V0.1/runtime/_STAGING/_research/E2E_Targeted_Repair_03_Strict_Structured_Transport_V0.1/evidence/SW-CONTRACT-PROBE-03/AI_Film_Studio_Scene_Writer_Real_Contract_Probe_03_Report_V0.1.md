# AI Film Studio Scene Writer Real Contract Probe 03 Report V0.1

| Item | Result |
| --- | --- |
| Run ID | SW-CONTRACT-PROBE-03 |
| Status | PASS |
| Provider / model | DeepSeek / deepseek-v4-pro |
| Transport | strict function `submit_scene_writer_package` |
| Beta feature | YES; isolated adapter path |
| Provider calls | 1 |
| Retries / fallback | 0 / 0 |
| Showrunner calls | 0 |
| Downstream calls | 0 |

## Probe Acceptance

| Test | Result | Detail |
| --- | --- | --- |
| PROBE-03-01 | PASS | one required strict function call received |
| PROBE-03-02 | PASS | arguments parsed without tolerant parsing |
| PROBE-03-03 | PASS | arguments pass the strict function schema |
| PROBE-03-04 | PASS | three scenes complete |
| PROBE-03-05 | PASS | six structural fields complete per scene |
| PROBE-03-06 | PASS | machine state codes valid |
| PROBE-03-07 | PASS | soaked_uniform exact |
| PROBE-03-08 | PASS | A-17 retained |
| PROBE-03-09 | PASS | custody retained |
| PROBE-03-10 | PASS | knowledge timing retained |
| PROBE-03-11 | PASS | authorized clothing transition retained |
| PROBE-03-12 | PASS | no unauthorized reconciliation |
| PROBE-03-13 | PASS | Structural Contract Gate PASS |
| PROBE-03-14 | PASS | State Token Gate PASS |
| PROBE-03-15 | PASS | Semantic Safeguard PASS |
| PROBE-03-16 | PASS | raw response and usage persisted before validation |
| PROBE-03-17 | PASS | no transport auto-repair |
