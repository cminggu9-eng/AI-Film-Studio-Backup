---
type: director-scene-writer-strict-construct-diff
status: completed-with-actionable-difference
version: 0.1
---

# Director vs Scene Writer Strict Construct Diff V0.1

Scene Writer remains a read-only known-working strict control. This comparison is construct-level only; a difference alone is not treated as root cause.

| Construct | Scene Writer control | Director projected wire schema | Status |
| --- | --- | --- | --- |
| Root/nested objects | complete required sets + `additionalProperties: false` | same after state-string projection | aligned |
| String enum | `type: string` + `enum` | regular enums typed; nine `ABSENT` nodes enum-only | exact failed difference |
| Arrays/items | typed array and typed items | same pattern | aligned |
| `anyOf` | typed branches | state-string branch typed; `ABSENT` branch enum-only | exact failed difference |
| `minLength`, `maxLength`, `minItems`, `maxItems` | absent | absent | aligned |
| `$ref` / `$defs` | not required by control | not required by Director | not causal |

The live error and captured Director wire payload, not the diff itself, establish the enum-only nodes as the remaining constraint.

