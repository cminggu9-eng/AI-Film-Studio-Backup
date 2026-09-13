---
type: director-strict-compatibility-probe-03-validation-report
status: failed-at-local-structured-validator
version: 0.1
---

# Director Strict Compatibility Probe 03 — Validation Report V0.1

| Required gate | Result | Evidence |
| --- | --- | --- |
| Provider strict request accepted | PASS | successful tool-call response |
| Required function exists | PASS | exactly one `submit_director_package` call |
| Tool arguments parse | PASS | JSON arguments parsed |
| Truncation check | PASS | `NOT_TRUNCATED` |
| Final function-schema validation | FAIL | `Director payload did not match exact required field set` |
| Eight machine fields / control / locks / envelope / display | NOT REACHED | fail-closed at schema-validation gate |
| Semantic auto-fill / prose extraction | PASS | `0 / 0` |

The fail-closed validator stopped before role-contract validation or envelope assembly. This prevents an invalid provider payload from being normalized into a formal Director output.

