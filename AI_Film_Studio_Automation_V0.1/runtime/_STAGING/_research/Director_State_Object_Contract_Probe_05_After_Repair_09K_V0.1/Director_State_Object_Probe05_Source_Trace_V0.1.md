# Director State Object Probe05 Source Trace V0.1

## Result

PASS

## Source artifacts

```json
{
  "fixture_binding": {
    "path": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\E2E_Targeted_Repair_07_Fixture_Generalization_Runtime_Parameterization_V0.1\\fixtures\\E2E_FIX_01_Runtime_Binding_V0.1.json",
    "sha256": "89d019a64e371c050fe8df25645875b8772d1a91ddd521a80af3dc2b97c5871f",
    "read_only": true
  },
  "showrunner_output": {
    "path": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\Minimal_E2E_Runtime_Validation_V0.1\\evidence\\E2E-RUN-12\\artifacts\\showrunner_output.json",
    "sha256": "87d8d02af8fa253e096e01f000f506553ac1968a8f93f9f753d9c1f958cda74a",
    "read_only": true
  },
  "scene_writer_output": {
    "path": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\Minimal_E2E_Runtime_Validation_V0.1\\evidence\\E2E-RUN-12\\artifacts\\scene_writer_output.json",
    "sha256": "4ac62a155ea6752e060643a173acef4081885940a86eba66207a109a14223b97",
    "read_only": true
  },
  "showrunner_envelope": {
    "path": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\Minimal_E2E_Runtime_Validation_V0.1\\evidence\\E2E-RUN-12\\envelopes\\01_showrunner_to_scene_writer.json",
    "sha256": "589cf112524472df64663a8d4874558174f4fc73530352151bdde905096456a8",
    "read_only": true
  },
  "scene_writer_envelope": {
    "path": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\Minimal_E2E_Runtime_Validation_V0.1\\evidence\\E2E-RUN-12\\envelopes\\02_scene_writer_to_director.json",
    "sha256": "9219e5db16c2b74e4fb6f7b2887e214002a654191d2ebe21cc747a3f6d4f2925",
    "read_only": true
  },
  "state_ledger": {
    "path": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\Minimal_E2E_Runtime_Validation_V0.1\\evidence\\E2E-RUN-12\\state_ledger.json",
    "sha256": "aae6fb8ed1a0f0961ac761c2162bba85aa4db8e2e51952fa451b1b1f5f3bfbf1",
    "read_only": true
  },
  "semantic_safeguard": {
    "path": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\Minimal_E2E_Runtime_Validation_V0.1\\evidence\\E2E-RUN-12\\semantic_safeguard.json",
    "sha256": "4f50069fcfc4b69d7d77944b7347b751488c5e927fb943874455fb574694bd20",
    "read_only": true
  }
}
```

## Source trace

```json
[
  {
    "field": "relevant_prior_state",
    "scene": "E2E-FIX-01-S01",
    "property": "clothing_visual_state_code",
    "source_contract_pointer": "compiled_run_contract#/state_enums/clothing_visual_state_code",
    "source_version": "181975fa44f96d389bd5470db756f5471e0b88bf2e95e9215dfc5df2c337d6aa",
    "canonical_owner": "Compiled Run Contract",
    "source_record_id": "E2E-FIX-01/compiled-initial-state",
    "ledger_sequence": 0,
    "type_source": "compiled_run_contract#/strict_schema/scene_packages/state/properties/clothing_visual_state_code/type",
    "enum_source": "compiled_run_contract#/state_enums/clothing_visual_state_code",
    "requiredness_source": "Repair09J relevant_prior_state per-scene closure",
    "projection_rule": "COMPILED_INITIAL_OR_PREVIOUS_VALIDATED_SCENE"
  },
  {
    "field": "current_state",
    "scene": "E2E-FIX-01-S01",
    "property": "clothing_visual_state_code",
    "source_contract_pointer": "run_local_state_ledger_records#/E2E-FIX-01-S01/state_snapshot/clothing_visual_state_code",
    "source_version": "1.0",
    "canonical_owner": "Scene Writer",
    "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S01",
    "ledger_sequence": 1,
    "type_source": "compiled_run_contract#/strict_schema/scene_packages/state/properties/clothing_visual_state_code/type",
    "enum_source": "compiled_run_contract#/state_enums/clothing_visual_state_code",
    "requiredness_source": "Repair09J current_state per-scene closure",
    "projection_rule": "OWNER_LIFECYCLE_LEDGER_SEQUENCE_WINNER"
  },
  {
    "field": "relevant_prior_state",
    "scene": "E2E-FIX-01-S02",
    "property": "clothing_visual_state_code",
    "source_contract_pointer": "run_local_state_ledger_records#/E2E-FIX-01-S01/state_snapshot/clothing_visual_state_code",
    "source_version": "1.0",
    "canonical_owner": "Scene Writer",
    "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S01",
    "ledger_sequence": 1,
    "type_source": "compiled_run_contract#/strict_schema/scene_packages/state/properties/clothing_visual_state_code/type",
    "enum_source": "compiled_run_contract#/state_enums/clothing_visual_state_code",
    "requiredness_source": "Repair09J relevant_prior_state per-scene closure",
    "projection_rule": "COMPILED_INITIAL_OR_PREVIOUS_VALIDATED_SCENE"
  },
  {
    "field": "current_state",
    "scene": "E2E-FIX-01-S02",
    "property": "clothing_visual_state_code",
    "source_contract_pointer": "run_local_state_ledger_records#/E2E-FIX-01-S02/state_snapshot/clothing_visual_state_code",
    "source_version": "1.0",
    "canonical_owner": "Scene Writer",
    "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S02",
    "ledger_sequence": 2,
    "type_source": "compiled_run_contract#/strict_schema/scene_packages/state/properties/clothing_visual_state_code/type",
    "enum_source": "compiled_run_contract#/state_enums/clothing_visual_state_code",
    "requiredness_source": "Repair09J current_state per-scene closure",
    "projection_rule": "OWNER_LIFECYCLE_LEDGER_SEQUENCE_WINNER"
  },
  {
    "field": "relevant_prior_state",
    "scene": "E2E-FIX-01-S03",
    "property": "clothing_visual_state_code",
    "source_contract_pointer": "run_local_state_ledger_records#/E2E-FIX-01-S02/state_snapshot/clothing_visual_state_code",
    "source_version": "1.0",
    "canonical_owner": "Scene Writer",
    "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S02",
    "ledger_sequence": 2,
    "type_source": "compiled_run_contract#/strict_schema/scene_packages/state/properties/clothing_visual_state_code/type",
    "enum_source": "compiled_run_contract#/state_enums/clothing_visual_state_code",
    "requiredness_source": "Repair09J relevant_prior_state per-scene closure",
    "projection_rule": "COMPILED_INITIAL_OR_PREVIOUS_VALIDATED_SCENE"
  },
  {
    "field": "current_state",
    "scene": "E2E-FIX-01-S03",
    "property": "clothing_visual_state_code",
    "source_contract_pointer": "run_local_state_ledger_records#/E2E-FIX-01-S03/state_snapshot/clothing_visual_state_code",
    "source_version": "1.0",
    "canonical_owner": "Scene Writer",
    "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S03",
    "ledger_sequence": 3,
    "type_source": "compiled_run_contract#/strict_schema/scene_packages/state/properties/clothing_visual_state_code/type",
    "enum_source": "compiled_run_contract#/state_enums/clothing_visual_state_code",
    "requiredness_source": "Repair09J current_state per-scene closure",
    "projection_rule": "OWNER_LIFECYCLE_LEDGER_SEQUENCE_WINNER"
  },
  {
    "field": "proposed_state",
    "scene": "ABSENT",
    "property": "ABSENT",
    "source_contract_pointer": "Repair09J#/proposed_state/exact_absent",
    "source_version": "0cf9224f7b32f0b75d792ebccd3ac34c4382cd74cb1a9a69c1e4bc123949e070",
    "canonical_owner": "Repair 09J Authority",
    "source_record_id": "ABSENT",
    "ledger_sequence": 0,
    "type_source": "State Evidence ABSENT",
    "enum_source": "State Evidence ABSENT",
    "requiredness_source": "Repair09J proposed_state closure",
    "projection_rule": "NO_AUTHORIZED_PROJECTABLE_CONTENT"
  },
  {
    "field": "knowledge_timing",
    "scene": "ABSENT",
    "property": "ABSENT",
    "source_contract_pointer": "Repair09J#/knowledge_timing/exact_absent",
    "source_version": "0cf9224f7b32f0b75d792ebccd3ac34c4382cd74cb1a9a69c1e4bc123949e070",
    "canonical_owner": "Repair 09J Authority",
    "source_record_id": "ABSENT",
    "ledger_sequence": 0,
    "type_source": "State Evidence ABSENT",
    "enum_source": "State Evidence ABSENT",
    "requiredness_source": "Repair09J knowledge_timing closure",
    "projection_rule": "NO_AUTHORIZED_PROJECTABLE_CONTENT"
  },
  {
    "field": "visual_state",
    "scene": "ABSENT",
    "property": "ABSENT",
    "source_contract_pointer": "Repair09J#/visual_state/exact_absent",
    "source_version": "0cf9224f7b32f0b75d792ebccd3ac34c4382cd74cb1a9a69c1e4bc123949e070",
    "canonical_owner": "Repair 09J Authority",
    "source_record_id": "ABSENT",
    "ledger_sequence": 0,
    "type_source": "State Evidence ABSENT",
    "enum_source": "State Evidence ABSENT",
    "requiredness_source": "Repair09J visual_state closure",
    "projection_rule": "NO_AUTHORIZED_PROJECTABLE_CONTENT"
  }
]
```
