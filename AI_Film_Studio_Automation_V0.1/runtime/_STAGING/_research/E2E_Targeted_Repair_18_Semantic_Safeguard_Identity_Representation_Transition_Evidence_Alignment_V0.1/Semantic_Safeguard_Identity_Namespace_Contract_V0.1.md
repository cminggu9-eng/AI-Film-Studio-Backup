# Semantic Safeguard Identity Namespace Contract

Invariant: token equality is not entity identity across machine namespaces.

- `transport.entity_id` identifies the provider/transport entity token.
- `assertion.identity_lock` identifies the protected identity lock token.
- Equality is decided only after both exact tokens resolve through the current projection to one `binding_entity_node` with the same binding ID and projection hash.
- Same-namespace typed comparisons, missing fields, unknown tokens, ambiguity, similarity, suffix matching, and automatic aliases are rejected.

No global alias registry exists.

