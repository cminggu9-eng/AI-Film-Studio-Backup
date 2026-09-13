# Scene Writer Full Semantic Validation Plan V0.1

Status: `AUTHORIZED / STAGING ONLY / NO REPAIR DURING VALIDATION`

## Scope

- Validate the frozen canonical `scene-writer` through SceneWriterRuntime, the shared ModelExecutor, the bound DeepSeek development provider, and the already-bound semantic verifier.
- Every case is synthetic, non-Canon, and requests `output_language: zh-CN`.
- `F01–F12`, `F14` execute once each. Required boundary Fixture `F13` has two mutually exclusive state subcases, `F13-A` and `F13-B`; each is a separate one-time formal execution. Total planned formal executions: `15`; planned resamples: `0`.

## Freeze

From the preflight baseline through final review, do not modify canonical Skill, Capability Model, Runtime contracts, Output Language Contract, Fact / Knowledge Gate, semantic verifier contract, executor binding, provider configuration, or Fixture Pack. Findings are recorded only.

## Review Method

Each raw result records input, Runtime output, verifier result, generation/verification usage, latency, and estimated CNY cost. Human review uses PASS / PASS WITH OBSERVATION / FAIL with a separate unsupported-fact and character-knowledge assessment. Verifier performance is recorded only for integrity-targeted cases and any observed integrity violation.

## Fixture Coverage

| Fixture | Primary validation |
|---|---|
| F01 | Normal CREATE and complete Scene construction |
| F02 | Action / object / spatial construction |
| F03 | Dialogue as dramatic action |
| F04 | Silence, reaction, choice, and object use |
| F05 | Internal state to observable playable behavior |
| F06 | Subtext |
| F07 | Exposition through discovery / resistance |
| F08 | Assignment Fact Integrity |
| F09 | Character Knowledge Integrity |
| F10 | Local REVISE ceiling |
| F11 | NO_MATERIAL_CHANGE |
| F12 | DIAGNOSE without replacement Scene |
| F13-A | Truly missing material context |
| F13-B | Upstream Canon / Showrunner decision |
| F14 | Production and role boundary |

No Full Semantic Validation finding authorizes repair, publish, Human Acceptance, or downstream-role activation.
