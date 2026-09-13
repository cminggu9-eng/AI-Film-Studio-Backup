# Director State Object Negative Test Report V0.1

Result: **15/15 PASS**.

`DIR-OBJ-NEG-01` through `DIR-OBJ-NEG-15` cover fixture literal leakage, model-defined keys, missing trace pointer, wrong scene, wrong dimension, invalid enum, source conflict, missing source, three exact-ABSENT violations, legacy JSON string, additional nested property, prompt/function drift, and validator/function drift.

Each PASS means the prohibited mutation was detected or rejected. Conflict and missing source were not converted to ABSENT. Counters: Provider 0; Executor 0; Role 0; Probe 0; E2E 0.

Machine evidence: `evidence/director_state_object_negative_tests.json`.
