# Director Strict Schema Compatibility Audit

Semantic requirements remain provider-neutral. Projection converts only `const: ABSENT` to `enum: [ABSENT]` and removes `minLength`, whose non-empty enforcement remains in the local Director validator. The one allowed probe still returned 400, so a remaining Provider constraint is unresolved.
