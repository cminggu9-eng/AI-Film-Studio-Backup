---
type: golden-e2e-evidence-manifest
status: frozen-index
version: 0.1
run_id: E2E-RUN-05
---

# AI Film Studio Golden E2E Evidence Manifest V0.1

## Source and custody

All entries below resolve inside the original immutable-in-practice staging evidence root:

`E:\AI_Film_Studio\AI_Film_Studio_Automation_V0.1\runtime\_STAGING\_research\Minimal_E2E_Runtime_Validation_V0.1\evidence\E2E-RUN-05`

No file has been copied, renamed, regenerated, or moved by this Phase 1 package.

| Evidence class | Original artifact | What it establishes |
| --- | --- | --- |
| Execution | `execution_manifest.json` | run identity, authorization, fixture, status, budgets, hashes, integrity counters |
| Provider | `provider_manifest.json` | seven calls, model, usage, raw/output/invocation/persistence paths, truncation and transport data |
| Handoff | `handoff_trace.json` | six adjacent-role envelopes |
| State | `state_ledger.json` | append-only state records and ordered snapshots |
| Safeguard | `semantic_safeguard.json` | evidence/contract decision, non-rewrite boundary |
| Acceptance | `acceptance_test_report.json` | `E2E-INT-01`–`18`, all `PASS` |
| Failure attribution | `failure_attribution.json` | no failure attribution recorded for this passing run |
| Gate / preflight | `preflight.json`, `authorization.json` | pre-run integrity and explicit execution boundary |
| Evidence bundle | `AI_Film_Studio_E2E_Run_05_Evidence_Bundle_V0.1.md` | human-readable evidence index |

## Role-artifact manifest

For each role key below, the evidence root contains `{key}_input.json`, `{key}_output.json`, `{key}_provider_response.json`, `{key}_invocation.json`, `{key}_persistence_verification.json`, and `{key}_truncation_detection.json`. The Character & Acting raw/invocation/persistence filenames use the recorded `character_&_acting` stem.

| Role | Key | Raw / parsed representation | Handoff envelope |
| --- | --- | --- | --- |
| Showrunner | `showrunner` | raw response + parsed output | `envelopes\01_showrunner_to_scene_writer.json` |
| Scene Writer | `scene_writer` | raw response + parsed structured output | `envelopes\02_scene_writer_to_director.json` |
| Director | `director` | raw response + parsed output | `envelopes\03_director_to_character_acting.json` |
| Character & Acting | `character_acting` | raw response + parsed output | `envelopes\04_character_acting_to_art_director.json` |
| Art Director | `art_director` | raw response + parsed output | `envelopes\05_art_director_to_continuity.json` |
| Continuity | `continuity` | raw response + parsed output | `envelopes\06_continuity_to_shared_qa.json` |
| Shared QA | `shared_qa` | raw response + parsed output | terminal role; no subsequent envelope |

## Deliverable records

The original root also contains the seven role Markdown deliveries, the final review, task record, work log, execution manifest, and evidence-bundle record. These are evidence references only; this manifest does not restate their creative content.

## Retrieval rule

Use an absolute path under the root above, then verify it remains under that exact root. Do not accept a nested stage root, an alias, or an unrecorded substitute as Golden evidence.

