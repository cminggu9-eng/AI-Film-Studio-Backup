# Character & Acting Raw Role Output Contract V0.1

Date: 2026-08-31  
Contract: `CHARACTER-ACTING-TRANSPORT-V0.1`

The non-strict Provider response contains exactly these nine role-owned fields:

1. `primary_state_or_outcome`
2. `flags`
3. `handoffs`
4. `canon_assignment_locks`
5. `prohibited_changes`
6. `required_outcome`
7. `unresolved_decisions`
8. `state_evidence`
9. `content`

`scene_packages` is prohibited from the raw Character & Acting payload. The prompt projects only this nine-field schema and does not ask the model to emit, echo, copy, summarize, reconstruct, rewrite, translate, or sentinel-fill upstream scene packages.

Raw validation checks the exact field set, lawful types, six exact state dimensions, exact canonical outcome, `flags=ABSENT`, `handoffs=ABSENT`, JSON safety, and non-empty content. It performs no prose extraction or semantic hydration.

