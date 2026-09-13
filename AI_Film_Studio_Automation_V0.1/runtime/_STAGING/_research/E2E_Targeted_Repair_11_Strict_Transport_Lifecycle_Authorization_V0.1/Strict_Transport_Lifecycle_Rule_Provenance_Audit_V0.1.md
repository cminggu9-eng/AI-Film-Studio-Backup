# Strict Transport Lifecycle Rule Provenance Audit V0.1

## Historical rule

Systemic Phase 2 originally required DeepSeek Beta strict transport to be isolated to the one Scene Writer invocation. This was valid when `submit_scene_writer_package` was the sole authorized strict path.

## Drift evidence

`E2E-RUN-13` recorded two lawful strict invocations: Scene Writer with `submit_scene_writer_package`, and Director with `submit_director_package`. Both completed raw-first persistence, exact tool-call parsing, schema validation, and role-contract validation. E2E-INT-01 through E2E-INT-18 were 18/18 PASS.

The old count/ownership assertion therefore safe-stopped only because it was stale lifecycle metadata. It was not a Provider, role, semantic, schema, or evidence failure. The immutable R13 failure attribution remains unchanged.

## Repair conclusion

Lifecycle admission must authorize exact role/function pairs, not count one historical role. Provider-specific strict mechanics remain adapter-scoped.
