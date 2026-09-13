# Scene Writer Compact Serialization Contract V0.1

## Transport Shape

The Provider emits exactly four top-level fields:

`format`, `control`, `state`, `scenes`.

`format` is the exact token `scene-writer-integration-compact-v0.1`. `scenes` retains all three scene IDs, normal scene content, the six frozen structural fields, and all state values. The compact field aliases are transport-only.

## Lossless Runtime Hydration

The runtime deterministically restores the existing integration shape before the frozen state-token and structural gates execute:

- `场景 1`–`场景 3` aggregate content is assembled from untouched per-scene content.
- Assignment locks and prohibited changes are copied exactly from the immutable passed-in assignment.
- `source_role`, `version`, `source_record_id`, and the scene-local `evidence_locator` are derived only from the authorized run ID and scene ID.
- No creative sentence, structural value, state value, knowledge holder, display prose, or transition token is summarized, translated, or altered.

## Bounds

- Per-scene content: at most 420 characters.
- Each structural value: at most 96 characters.
- Each state text value: at most 160 characters.
- Each top-level state dimension: at most 360 serialized characters.

Exceeding a bound is a compact serialization failure; it never triggers truncation, auto-repair, or a second call.

## Semantic Preservation

The compact form does not modify the machine-state contract, six-field structural contract, Semantic Safeguard, Scene Writer creative semantics, Canon, knowledge timing, or authorized transitions. `Semantic Mutation = 0`.

