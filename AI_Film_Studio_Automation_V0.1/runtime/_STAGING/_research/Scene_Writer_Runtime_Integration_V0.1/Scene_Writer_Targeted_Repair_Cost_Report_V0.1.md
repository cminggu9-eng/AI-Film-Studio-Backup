# Scene Writer Targeted Repair Cost Report V0.1

All amounts are DeepSeek pricing estimates, not billing records.

| Category | Executions | Tokens / latency | Estimated CNY |
|---|---:|---|---:|
| Repair development and static tests | 0 model calls | — | 0 |
| Recorded verifier-only replay responses | 14 provider calls with retained usage | retained in attempt JSON evidence | 0.0718902 |
| Provider calls with invalid JSON response | 4 observed calls | provider usage unavailable from the failed transport | not estimable from retained telemetry |
| Unplanned Smoke generation caused by test-runner import side effect | 1 generation; Runtime FAIL_SAFE; verifier not invoked | input 5,712; output 614; latency 14,536 ms | 0.0208200 |
| Formal Targeted generation rerun | 0 / 13 | — | 0 |

Known recorded lower bound: `CNY 0.0927102`, plus four invalid-response calls whose provider usage was not retained. The unintended Smoke call was immediately stopped, did not overwrite historical raw evidence, and is explicitly excluded from the authorised 13-rerun count.
