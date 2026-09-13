# Art Director visual_state Contract Alignment V0.1

Date: 2026-08-31  
Decision: `OBJECT OR exact ABSENT`  
Result: ALIGNED

## Contract

`state_evidence.visual_state` is a required machine field whose lawful representations are:

1. A JSON-safe object with string keys; or
2. The exact case-sensitive token `ABSENT`.

The field is validated independently. Visual information in `current_state`, `proposed_state`, or prose does not fill, replace, or strengthen `visual_state`. Conversely, a lawful `ABSENT` is not rejected merely because another field contains visual information.

## Recorded cases

| Case | Expected | Result |
|---|---:|---:|
| lawful exact `ABSENT` | PASS | PASS |
| valid object | PASS | PASS |
| invalid object / non-JSON-safe value | FAIL | FAIL-CLOSED |
| illegal scalar or array type | FAIL | FAIL-CLOSED |
| missing required `visual_state` field | FAIL | FAIL-CLOSED |

No semantic synthesis, cross-field substitution, or post-hoc prose extraction is performed.

