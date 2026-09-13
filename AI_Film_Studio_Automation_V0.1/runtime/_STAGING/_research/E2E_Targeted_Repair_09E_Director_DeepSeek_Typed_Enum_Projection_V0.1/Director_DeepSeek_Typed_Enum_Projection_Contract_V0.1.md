---
type: director-deepseek-typed-enum-projection-contract
status: complete
version: 0.1
---

# Director DeepSeek Typed-Enum Projection Contract V0.1

## Deterministic projection rule

Within `director_provider_compatibility.py`, a provider-neutral fixed string constant now projects as:

```json
{ "type": "string", "enum": ["ABSENT"] }
```

The projector rejects non-string constants and refuses to overwrite a pre-existing non-string type. It does not add a value, remove a value, change an `anyOf`, alter an object shape, or modify Director's provider-neutral schema.

## Contract preservation

- Required top-level fields: unchanged.
- Eight Director machine semantic fields: unchanged.
- Canonical mode and primary-state domains: unchanged.
- Locks, prohibitions, handoff semantics, and state dimensions: unchanged.
- `strict: true`, function name `submit_director_package`, and forced tool choice: unchanged.

Only the DeepSeek wire representation of a fixed string value changed.

