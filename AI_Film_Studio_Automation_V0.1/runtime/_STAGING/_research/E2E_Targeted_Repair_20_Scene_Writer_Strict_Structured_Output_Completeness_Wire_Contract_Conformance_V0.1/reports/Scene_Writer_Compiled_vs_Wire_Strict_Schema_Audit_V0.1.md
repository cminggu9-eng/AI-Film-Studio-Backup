# Scene Writer compiled-to-wire strict schema audit

## Schema identity

The F03 compiled schema, final StructuredOutputContract, adapter-projected schema, actual tool-wire schema, and local validator schema all have SHA-256:

ddcf597eeeb18253bddb832039e36d9642e144c9ad7720ffc35c912d142408e0

Byte equivalence and semantic equivalence are true across all five representations. This excludes a projection, serialization, or validator-divergence root cause.

## Actual wire mechanics

- Endpoint family: DeepSeek strict beta.
- Function: submit_scene_writer_package.
- function.strict: true.
- Exact tool choice: type function, function name submit_scene_writer_package.
- R25 persisted wire payload SHA-256: 9aeb185bb3099997c911a996d01c99eca6d402e6e73773b6361719a87acd7c0b.

## Scenes-item contract

- Required: id, content, structural, state.
- Structural required: 目标, 阻力, 对白行动, 转折, 入场, 出场.
- F03 state required: entity_id, custody, holders, reveal, relationship, camera_battery_state, state_display, location, transitions.
- Every strict-schema object, including scenes items, structural, and state, uses additionalProperties false.
- No provider minItems or maxItems are emitted because that documented strict subset excludes them. The local scene-ID contract independently requires the exact ordered three F03 IDs.

The runtime now persists a scene_writer_schema_identity_manifest.json before every Scene Writer strict send and fails before provider dispatch if this identity or strict mechanics diverge.
