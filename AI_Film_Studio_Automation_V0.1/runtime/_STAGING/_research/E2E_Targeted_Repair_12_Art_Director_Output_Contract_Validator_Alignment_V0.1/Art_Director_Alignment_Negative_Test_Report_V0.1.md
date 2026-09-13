# Art Director Alignment Negative Test Report V0.1

Date: 2026-08-31  
Result: 12 / 12 PASS

| Test | Protected failure mode | Result |
|---|---|---:|
| AD-ALIGN-NEG-01 | lawful `ABSENT` rejected as object-only | PASS |
| AD-ALIGN-NEG-02 | invalid `visual_state` accepted | PASS |
| AD-ALIGN-NEG-03 | cross-field auto-fill of `visual_state` | PASS |
| AD-ALIGN-NEG-04 | production keyword heuristic present | PASS |
| AD-ALIGN-NEG-05 | keyword-rich prose substitutes invalid machine field | PASS |
| AD-ALIGN-NEG-06 | validator requires content absent from prompt/schema | PASS |
| AD-ALIGN-NEG-07 | prompt requires content absent from contract | PASS |
| AD-ALIGN-NEG-08 | fixed heading requirement returns | PASS |
| AD-ALIGN-NEG-09 | conditional content treated mandatory | PASS |
| AD-ALIGN-NEG-10 | integration mismatch classified role semantic | PASS |
| AD-ALIGN-NEG-11 | canonical outcome mutation | PASS |
| AD-ALIGN-NEG-12 | Art Director authority takeover | PASS |

Counters: Provider 0; Executor 0; Role 0; Probe 0; real E2E 0.

