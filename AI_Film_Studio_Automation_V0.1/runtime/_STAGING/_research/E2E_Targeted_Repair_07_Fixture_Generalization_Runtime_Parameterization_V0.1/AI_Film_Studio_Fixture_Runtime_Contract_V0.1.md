# AI Film Studio Fixture Runtime Contract V0.1

The generic contract requires exactly: `fixture_id`, `concept`, `scene_count`, `characters`, `tracked_entities`, `knowledge_events`, `relationship_constraints`, `state_dimensions`, `authorized_transitions`, `time_conditions`, `decision_locks`, `prohibited_outcomes`, and `acceptance_evidence`.

Structural subfields carry the required categories without naming a story: each `tracked_entities` item carries identity/condition/custody locks; `knowledge_events` carries holder and timing; `state_dimensions` carries physical or visual machine-state enums; and the remaining generic lists carry relationship, transition, time, decision, prohibited-outcome, and acceptance constraints.

It defines structure only. Story values are legal only in a per-fixture binding. Missing required fields fail closed; the compiler has no LLM, provider, inference, repair, or cross-fixture merge behavior.
