# Director Unresolved Decisions Type Contract V0.1

Authoritative source: final strict function parameters.

- Requiredness: required top-level field, one of 15 exact fields.
- Allowed native JSON forms: exact JSON string `ABSENT`, or a native JSON array.
- Array item type: string; the provider-neutral schema requires non-empty item text.
- Array size: no `minItems` or `maxItems` is declared. Therefore `[]` is a lawful native array and must remain distinct from `ABSENT`.
- Forbidden substitutions: JSON-stringified arrays, `null`, empty string, object, scalar wrapping, and conversion between `[]` and `ABSENT`.

This report records the existing contract; Repair21 does not tighten or reinterpret its decision semantics.

