---
type: director-strict-compatibility-probe-03-failure-attribution
status: exact-local-contract-composition-failure
version: 0.1
---

# Director Strict Compatibility Probe 03 — Failure Attribution V0.1

## Earliest failed layer

`Strict Function Schema Validation` — local Director Full Structured Submission validator.

DeepSeek did not reject the typed-enum schema. The returned function arguments have 18 top-level fields where the final function schema requires exactly 15.

| Difference | Exact fields / values |
| --- | --- |
| Unexpected top-level fields | `canon_assignment_locks`, `prohibited_changes`, `scene_packages` |
| Missing required function fields | none |
| Invalid state representation | five state dimensions are objects where the final function schema requires JSON-object strings or `ABSENT` |

## Causal evidence

The persisted system message contains an older generic `REQUIRED TRANSPORT SCHEMA` that advertises `canon_assignment_locks`, `prohibited_changes`, `content`, and `scene_packages`, while omitting the Director function's nine semantic fields and `selected_mode`. It also says state values are `object or ABSENT`, contradicting the final function schema's JSON-object-string representation.

This prompt/function contract divergence explains the observed extra fields and object values. It is a transport-composition failure, not a Director semantic failure and not a new DeepSeek schema rejection.

## Next exact repair boundary

1. In the structured Director path, derive or inject the prompt's required transport schema from the actual final function parameters; suppress the generic role-output schema when it conflicts.
2. Ensure structured-prompt state instructions match the JSON-object-string projection exactly.
3. Add successful-response persistence for HTTP status plus safe tracing headers, while preserving existing error-path capture.
4. Add a provider-free regression that compares prompt-advertised fields/state representation to final `tools[].function.parameters`.

No code or schema was changed in this probe-only task.

