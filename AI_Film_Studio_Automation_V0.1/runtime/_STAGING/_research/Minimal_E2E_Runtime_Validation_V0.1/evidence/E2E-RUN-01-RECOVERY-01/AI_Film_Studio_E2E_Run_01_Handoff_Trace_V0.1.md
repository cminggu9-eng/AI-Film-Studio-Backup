# AI Film Studio E2E Run 01 Handoff Trace V0.1

| Sequence | Handoff | Status | Evidence |
| --- | --- | --- | --- |
| 01 | Showrunner → Scene Writer | PASS — envelope produced and consumed | `envelopes/01_showrunner_to_scene_writer.json` |
| 02 | Scene Writer → Director | BLOCKED BEFORE DELIVERY — envelope was materialized for attribution, but Director was not invoked after the semantic gate BLOCK | `envelopes/02_scene_writer_to_director.json`; `semantic_safeguard.json` |
| 03 | Director → Character & Acting | NOT REACHED | `artifacts/character_acting_not_reached.json` |
| 04 | Character & Acting → Art Director | NOT REACHED | `artifacts/art_director_not_reached.json` |
| 05 | Art Director → Continuity | NOT REACHED | `artifacts/continuity_not_reached.json` |
| 06 | Continuity → Shared QA | NOT REACHED | `artifacts/shared_qa_not_reached.json` |

For both produced envelopes, source role, version, locks, exact canonical tokens, assignment state, knowledge timing, relationship state, required outcome, unresolved decisions, and evidence locator are preserved. No adapter supplied missing facts.
