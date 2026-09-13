# Scene Writer Targeted Repair Architecture Audit V0.1

## Audited execution path

`Assignment → SceneWriterRuntime normalization → Assignment Constraint Ledger → CanonicalSceneWriterExecutor → Runtime output validation → deterministic fact precheck → SemanticAssignmentIntegrityVerifier → Runtime result`

The canonical `scene-writer/SKILL.md` is read only and remains outside this repair surface. The bound executor and verifier use one shared `ModelExecutor`; provider, model, retry policy, and Runtime publication are not changed.

## Observed architecture defects

1. The executor sends one universal schema whose creative field says `scene or revision`. Its prose favours `SCENE_CREATED` for CREATE, but it does not project the six Runtime states into lawful state-specific packets. This directly explains the malformed packet cluster F06/F11/F12/F13-A/F13-B.
2. Runtime already enforces several state invariants correctly, but only `NO_MATERIAL_CHANGE` explicitly forbids creative content. The other non-creative boundary states need the same explicit invariant to ensure the matrix is enforceable rather than prompt-only.
3. A complete `assignment_constraint_ledger` is technically included in the executor user request, but the generation system prompt does not establish it as the binding, structured claim authority. Knowledge entry state and discovery timing are not separately projected.
4. The deterministic fact guard is intentionally narrow and regex-based. It remains a cheap precheck only; expanding it would be a lexical-arms-race response and is excluded from this repair.
5. The semantic verifier has a bounded schema and correct no-rewrite boundary, but its prompt does not require a systematic inventory/classification of story-state claims across the scene and relevant control text. Its original categories have no dedicated knowledge-timing drift classification.

## Approved state-aware execution projection

This is a Runtime execution projection, not a replacement Scene Writer or a semantic change to the frozen canonical Skill. All responses retain exactly two top-level keys: `creative_deliverable` and `control_data`.

| Primary state | Valid modes | Required | Optional | Forbidden |
|---|---|---|---|---|
| `SCENE_CREATED` | `CREATE` | creative `{kind: scene, content}`, `primary_state`, `flags`, `handoffs` | scene-function/control summaries only when meaningful | revision creative, empty control placeholders |
| `SCENE_REVISED` | `REVISE` | creative `{kind: revision, content}`, `primary_state`, `flags`, `handoffs` | compact repair/scene summaries | scene creative, empty placeholders, fact expansion beyond assignment |
| `NO_MATERIAL_CHANGE` | `REVISE`, `DIAGNOSE` | creative `null`, `primary_state`, `flags`, `handoffs`, `material_rewrite_claimed: false`; DIAGNOSE also requires `diagnosis_summary` | concise non-creative rationale | scene/revision/replacement content, true/missing rewrite claim |
| `NEEDS_CONTEXT` | `CREATE`, `REVISE`, `DIAGNOSE` | creative `null`, `primary_state`, `flags`, `handoffs`, `material_missing_context.{missing, why_material, target_owner}` | concise lawful rationale | guessed people, story facts, or creative scene/revision |
| `UPSTREAM_DECISION_REQUIRED` | `CREATE`, `REVISE`, `DIAGNOSE` | creative `null`, `primary_state`, `flags` containing `UPSTREAM_HANDOFF_REQUIRED`, at least one handoff, `upstream_decision_needed` | concise authority rationale | an upstream decision made by Scene Writer, scene/revision |
| `REQUEST_OUT_OF_SCOPE` | `CREATE`, `REVISE`, `DIAGNOSE` | creative `null`, `primary_state`, `flags`, `handoffs`, `out_of_scope_boundary` | concise boundary rationale | scene/revision or role-substitution work |

All normal user-facing/audit prose follows the resolved output language. Canonical mode, state, flag, and handoff-owner tokens remain exact English tokens.

## Approved generation authority projection

The generation request will retain the existing named ledger fields and make them binding:

`LOCKED_FACTS`, `EXPLICIT_UNKNOWNS`, `CHARACTER_KNOWLEDGE_LIMITS`, `TEMPORAL_CONSTRAINTS`, `RELATIONSHIP_CONSTRAINTS`, `CAPABILITY_CONSTRAINTS`, `REQUIRED_EVENTS`, `REQUIRED_INFORMATION`, `REQUIRED_OUTCOME`, and `OPEN_CREATIVE_SPACE`.

It will also present a derived, source-preserving `KNOWLEDGE_TIMING` view:

- world facts and locked state;
- what each named participant knows at scene entry;
- explicit not-yet-known/unknown statements, preserved without inference;
- a rule that a fact may become known only through the assigned in-scene event and only after that event occurs.

This is transport metadata, not an inference engine or a new Canon source. It may copy input statements but never add a story fact.

## Approved verifier-recall projection

The verifier will remain a detector/classifier/reporter. Before producing its strict existing public JSON schema, it must compare each generated state-bearing claim with the ledger and classify it internally as:

1. ledger-supported;
2. lawful scene-local proposal/action/explicit uncertainty;
3. neutral behavior; or
4. unauthorized.

Claim classes must cover causal, temporal, relationship/history, capability, knowledge/timing, authority, resource, and obligation claims in creative and relevant control text. The repair may add a narrow verifier category for knowledge-timing drift, but cannot add rewriting, evaluation of artistic quality, lexical synonym catalogues, or regex-based semantic gate expansion.

## Minimal change set and non-goals

- Change executor prompt construction and expose the projection as inspectable data for contract tests.
- Strengthen Runtime state validation only where it enforces the matrix's non-creative state semantics.
- Enrich ledger transport with source-preserving knowledge timing.
- Update verifier prompt/category validation for claim-to-ledger recall.
- Add a dedicated Targeted Repair test/replay/rerun runner and evidence reports.

Not changed: canonical Skill, Capability Model, dramatic rules, Objective/Resistance/Turn semantics, shootability, entry/exit rules, production-burden authority boundaries, canonical tokens, Showrunner, Shared QA, provider, model, or Runtime publication state.
