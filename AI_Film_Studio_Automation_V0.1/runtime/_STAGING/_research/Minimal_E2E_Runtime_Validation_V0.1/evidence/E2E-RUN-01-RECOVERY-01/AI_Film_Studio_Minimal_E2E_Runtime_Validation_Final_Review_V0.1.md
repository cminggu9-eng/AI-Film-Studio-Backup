# AI Film Studio｜Minimal E2E Runtime Validation V0.1

## Execution

| Item | Result |
| --- | --- |
| Fixture / scenes | E2E-FIX-01 / exactly 3 generated scenes |
| Roles actually called in bounded recovery | Showrunner, Scene Writer |
| Provider / model | DeepSeek / deepseek-v4-pro |
| Provider calls | 3 actual across authorization: 1 initial technical attempt + 2 recovery calls |
| Retries / fallback | 0 / 0 |
| Known recovery cost | CNY 0.054336 for 14,384 known tokens; initial call telemetry unavailable and not fabricated |

## Role Results

| Role | Result |
| --- | --- |
| Showrunner | PASS in recovery; Story / Canon Package and State & Evidence Envelope produced. |
| Scene Writer | Provider / structural contract PASS; semantic gate BLOCK. |
| Director | NOT REACHED. |
| Character & Acting | NOT REACHED. |
| Art Director | NOT REACHED. |
| Continuity | NOT REACHED. |
| Shared QA | NOT REACHED. |

## State Integrity

| State | Result |
| --- | --- |
| A-17 identity / custody | Retained in all three generated scene packages. |
| Knowledge timing | Shared-use reveal recorded as `REVEALED_WITH_EVENT`; storage-room content remains unrevealed. |
| Relationship state | No full reconciliation declared. |
| Soaked-uniform exact state | FAIL — `湿透制服` supplied where `soaked_uniform` was required. |
| Clothing change | Final authorized `change_from_soaked_uniform` retained. |
| Chronology / visual carryover | Not eligible for full Continuity validation; no ledger entry was appended. |

## Semantic Safeguard

The gate BLOCKED `SOAKED-UNIFORM` as `REQUIRED_STATE_MISMATCH`. It reported no unsupported micro-fact or knowledge-leakage finding. Legacy verification stayed supplemental, and the gate did not rewrite creative output.

## Handoffs

Showrunner → Scene Writer passed with exact tokens intact. The Scene Writer → Director envelope was retained as evidence but was not delivered after the BLOCK. No adapter invented state.

## E2E Acceptance

`E2E-INT-01–18`: **8 PASS / 4 FAIL / 6 NOT REACHED**. The authoritative detailed table is `AI_Film_Studio_E2E_Run_01_Acceptance_Test_Report_V0.1.md`.

## Failures

1. Initial technical post-response persistence/role-contract defect: one bounded recovery used, no retry or fallback.
2. Scene Writer exact machine-state mismatch: recommended future repair is schema/enum enforcement distinct from Chinese human-readable prose.
3. Scene Writer required six structural headings absent: recommended future repair is a validated structured deliverable contract.

No semantic repair was run.

## Integrity

| Counter | Value |
| --- | --- |
| Canonical Skill Mutation | 0; seven post-run canonical hashes match the frozen preflight hashes. |
| Production Lock Mutation | 0 |
| Nuwa Calls | 0 |
| Database / RAG Work | 0 |
| Image / Video / ComfyUI | 0 |
| Automatic Provider Fallback | 0 |
| Silent Semantic Repair | 0 |

## Recommendation

MINIMAL E2E VALIDATION FAILED — TARGETED REPAIR REQUIRED
