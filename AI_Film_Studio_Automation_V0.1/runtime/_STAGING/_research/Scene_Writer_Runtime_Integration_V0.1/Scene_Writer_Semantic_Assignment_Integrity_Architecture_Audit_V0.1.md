# Scene Writer Semantic Assignment Integrity Verification Gate V0.1

Status: `IMPLEMENTED / STAGING ONLY / PRE-VALIDATION REVIEW REQUIRED`

## Architecture

- The frozen canonical `scene-writer` Skill remains the sole source of Scene Writer authority.
- The existing deterministic Assignment Fact / Knowledge guard remains a cheap pre-check only. It was not expanded with capability synonym, substring, fuzzy, or regex-catalogue logic.
- `SemanticAssignmentIntegrityVerifier` is a bounded compliance component: it receives one Assignment Constraint Ledger, one generated creative deliverable, and relevant control data; it can only return `PASS` / `FAIL` plus classified violations. It cannot rewrite or resample a scene.
- `SceneWriterRuntime` owns the sequence `generate → deterministic pre-check → semantic verify → enforce`. A real executor without a verifier returns `SEMANTIC_VERIFIER_UNBOUND`; verifier failure returns `SEMANTIC_VERIFIER_FAILURE`; verifier `FAIL` returns `SEMANTIC_INTEGRITY_VIOLATION` and suppresses the Scene deliverable.
- Generation and verification share the same existing provider-neutral `ModelExecutor` instance. The verifier contains no DeepSeek-specific client, credentials, base URL, pricing, or retry logic. The existing shared adapter was not changed.

## Constraint Ledger

`build_assignment_constraint_ledger()` derives only from current Runtime input and represents:

- `LOCKED_FACTS`
- `EXPLICIT_UNKNOWNS`
- `CHARACTER_KNOWLEDGE_LIMITS`
- `TEMPORAL_CONSTRAINTS`
- `RELATIONSHIP_CONSTRAINTS`
- `CAPABILITY_CONSTRAINTS`
- `REQUIRED_EVENTS`, `REQUIRED_INFORMATION`, and `REQUIRED_OUTCOME`
- `OPEN_CREATIVE_SPACE`

It does not query or construct a global Canon database. Open creative space permits neutral immediate action, pause, silence, existing-object handling, scene-local movement, dialogue tactics, neutral phrasing, and pacing only when they do not assert a new story, knowledge, relationship, capability, causal, temporal-obligation, or resource fact.

## Scope and Integrity

- Modified only Staging Runtime adapter, canonical executor transport metadata, binding wiring, semantic verifier, tests, and reports.
- `scene-writer/SKILL.md`, Capability Model, Modes, Primary States, Flags/Handoffs, authority boundaries, Showrunner, Shared QA, and provider adapter remain unchanged.
- Canonical Skill SHA-256: `93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb`.
- Frozen-asset semantic mutation count: `0`.
