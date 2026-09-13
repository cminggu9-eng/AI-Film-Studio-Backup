# Director State Object Probe05 Execution Manifest V0.1

## Probe

DIRECTOR-STATE-OBJECT-CONTRACT-PROBE-05

## Result

PASS

## Execution

```json
{
  "result": "PASS",
  "probe_id": "DIRECTOR-STATE-OBJECT-CONTRACT-PROBE-05",
  "timestamp": "2026-08-30T08:07:08.546002+00:00",
  "invocation_id": "DIRECTOR-STATE-OBJECT-CONTRACT-PROBE-05:director:1",
  "model": "deepseek-v4-pro",
  "endpoint": "https://api.deepseek.com/beta/chat/completions",
  "token_budget": 3500,
  "compiled_run_contract_id": "E2E-FIX-01",
  "compiled_run_contract": {
    "fixture": {
      "fixture_id": "E2E-FIX-01",
      "concept": "暴雨夜，夜班管理员许宁把一把刻有“A-17”的黄铜钥匙交给久未联系的姐姐许曼；许曼承认这是母亲留给两人一起打开储物间的钥匙，要求许宁先换下湿透的制服、等天亮再开门。",
      "scene_count": 3,
      "characters": [
        "许宁",
        "许曼"
      ],
      "tracked_entities": [
        {
          "entity_id": "A-17",
          "identity_lock": "A-17",
          "custody_required": true,
          "condition_lock": "brass_key"
        }
      ],
      "knowledge_events": [
        {
          "event_id": "shared_storage_reveal",
          "holder": "许曼",
          "not_before_scene": 3
        }
      ],
      "relationship_constraints": [
        "不得自动升级为完全和解"
      ],
      "state_dimensions": [
        {
          "dimension": "clothing_visual_state_code",
          "allowed_tokens": [
            "soaked_uniform",
            "changed_clothes"
          ]
        }
      ],
      "authorized_transitions": [
        "change_from_soaked_uniform"
      ],
      "time_conditions": [
        "天亮前后"
      ],
      "decision_locks": [
        "storage_room_opening"
      ],
      "prohibited_outcomes": [
        "完全和解"
      ],
      "acceptance_evidence": {
        "identity": "A-17",
        "reveal": "shared_storage_reveal",
        "state_dimension": "clothing_visual_state_code"
      }
    },
    "scene_ids": [
      "E2E-FIX-01-S01",
      "E2E-FIX-01-S02",
      "E2E-FIX-01-S03"
    ],
    "tracked_entity_ids": [
      "A-17"
    ],
    "state_enums": {
      "clothing_visual_state_code": [
        "soaked_uniform",
        "changed_clothes"
      ]
    },
    "strict_schema": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "scene_packages": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "scene_id": {
                "type": "string",
                "enum": [
                  "E2E-FIX-01-S01",
                  "E2E-FIX-01-S02",
                  "E2E-FIX-01-S03"
                ]
              },
              "tracked_entity_id": {
                "type": "string",
                "enum": [
                  "A-17"
                ]
              },
              "state": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "authorized_transitions": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": [
                    "change_from_soaked_uniform"
                  ]
                }
              }
            },
            "required": [
              "scene_id",
              "tracked_entity_id",
              "state",
              "authorized_transitions"
            ]
          }
        }
      },
      "required": [
        "scene_packages"
      ]
    },
    "semantic_safeguard_config": {
      "tracked_entities": [
        {
          "entity_id": "A-17",
          "identity_lock": "A-17",
          "custody_required": true,
          "condition_lock": "brass_key"
        }
      ],
      "knowledge_events": [
        {
          "event_id": "shared_storage_reveal",
          "holder": "许曼",
          "not_before_scene": 3
        }
      ],
      "relationship_constraints": [
        "不得自动升级为完全和解"
      ],
      "state_dimensions": [
        {
          "dimension": "clothing_visual_state_code",
          "allowed_tokens": [
            "soaked_uniform",
            "changed_clothes"
          ]
        }
      ],
      "authorized_transitions": [
        "change_from_soaked_uniform"
      ],
      "time_conditions": [
        "天亮前后"
      ],
      "prohibited_outcomes": [
        "完全和解"
      ],
      "decision_locks": [
        "storage_room_opening"
      ]
    },
    "ledger_tracking": {
      "entity_ids": [
        "A-17"
      ],
      "state_dimensions": [
        "clothing_visual_state_code"
      ],
      "state_enums": {
        "clothing_visual_state_code": [
          "soaked_uniform",
          "changed_clothes"
        ]
      },
      "authorized_transitions": [
        "change_from_soaked_uniform"
      ],
      "time_conditions": [
        "天亮前后"
      ]
    },
    "acceptance_evidence_map": {
      "identity": "A-17",
      "reveal": "shared_storage_reveal",
      "state_dimension": "clothing_visual_state_code"
    }
  },
  "state_schema_compiler_version": "DIRECTOR_STATE_OBJECT_SCHEMA_COMPILER_V0.1",
  "state_contract": {
    "compiler_id": "DIRECTOR_STATE_OBJECT_SCHEMA_COMPILER_V0.1",
    "authority": {
      "authority_id": "REPAIR_09J_DIRECTOR_STATE_PROJECTION_AUTHORITY_V0.1",
      "contract_root": "E:\\AI_Film_Studio\\AI_Film_Studio_Automation_V0.1\\runtime\\_STAGING\\_research\\E2E_Targeted_Repair_09J_Director_State_Projection_Authority_Closure_V0.1",
      "contract_hashes": {
        "Director_State_Projection_Authority_Decisions_V0.1.md": "10b61164784fb2f6ce04beef7ea2d9e5dd86b2f93c158c8394c4807649771ba7",
        "Director_relevant_prior_state_Selection_Contract_V0.1.md": "56c37c6b5e7f213c0c5335847973e19d5386526b895cb946a783ce4c5a670d04",
        "Director_current_state_Selection_Contract_V0.1.md": "cbf862657677242bffdf3d77929c938c849495e337e48b16570f06185089035a",
        "Director_proposed_state_Selection_Contract_V0.1.md": "42aa3fce65b6ac00b823d570b3249225bad05d049f5d3be1129d4d7f6b8951e9",
        "Director_knowledge_timing_Selection_Contract_V0.1.md": "f228b8195f07189255cd859a9c576a280a4ab7b478fac0e28e395d31fc161a68",
        "Director_visual_state_Selection_Contract_V0.1.md": "a789558747e1c21aac353128f6e23a12f12f9fb375e9da8c838572ca1f32124f",
        "Director_State_Source_Winner_Contract_V0.1.md": "eaa7a57920c7c98120f254a585fadb51beb9790c905266d863ee785749586d47",
        "Director_State_ABSENT_Closure_Contract_V0.1.md": "67ef2c60d5b34c5e70cc951dc622c36b67115048ac73fa20f1d90a47c41a5dc9"
      },
      "authority_bundle_hash": "0cf9224f7b32f0b75d792ebccd3ac34c4382cd74cb1a9a69c1e4bc123949e070"
    },
    "compiled_contract_hash": "181975fa44f96d389bd5470db756f5471e0b88bf2e95e9215dfc5df2c337d6aa",
    "validated_upstream_records_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "run_local_ledger_records_hash": "c3e44ebb712a108b28a2c3b4a28c3babb98cfb86f2e7588d08652af54ae0e802",
    "fixture_id": "E2E-FIX-01",
    "scene_ids": [
      "E2E-FIX-01-S01",
      "E2E-FIX-01-S02",
      "E2E-FIX-01-S03"
    ],
    "state_dimensions": [
      "clothing_visual_state_code"
    ],
    "state_schemas": {
      "relevant_prior_state": {
        "type": "object",
        "properties": {
          "E2E-FIX-01-S01": {
            "type": "object",
            "properties": {
              "clothing_visual_state_code": {
                "type": "string",
                "enum": [
                  "soaked_uniform",
                  "changed_clothes"
                ]
              }
            },
            "required": [
              "clothing_visual_state_code"
            ],
            "additionalProperties": false
          },
          "E2E-FIX-01-S02": {
            "type": "object",
            "properties": {
              "clothing_visual_state_code": {
                "type": "string",
                "enum": [
                  "soaked_uniform",
                  "changed_clothes"
                ]
              }
            },
            "required": [
              "clothing_visual_state_code"
            ],
            "additionalProperties": false
          },
          "E2E-FIX-01-S03": {
            "type": "object",
            "properties": {
              "clothing_visual_state_code": {
                "type": "string",
                "enum": [
                  "soaked_uniform",
                  "changed_clothes"
                ]
              }
            },
            "required": [
              "clothing_visual_state_code"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "E2E-FIX-01-S01",
          "E2E-FIX-01-S02",
          "E2E-FIX-01-S03"
        ],
        "additionalProperties": false
      },
      "current_state": {
        "type": "object",
        "properties": {
          "E2E-FIX-01-S01": {
            "type": "object",
            "properties": {
              "clothing_visual_state_code": {
                "type": "string",
                "enum": [
                  "soaked_uniform",
                  "changed_clothes"
                ]
              }
            },
            "required": [
              "clothing_visual_state_code"
            ],
            "additionalProperties": false
          },
          "E2E-FIX-01-S02": {
            "type": "object",
            "properties": {
              "clothing_visual_state_code": {
                "type": "string",
                "enum": [
                  "soaked_uniform",
                  "changed_clothes"
                ]
              }
            },
            "required": [
              "clothing_visual_state_code"
            ],
            "additionalProperties": false
          },
          "E2E-FIX-01-S03": {
            "type": "object",
            "properties": {
              "clothing_visual_state_code": {
                "type": "string",
                "enum": [
                  "soaked_uniform",
                  "changed_clothes"
                ]
              }
            },
            "required": [
              "clothing_visual_state_code"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "E2E-FIX-01-S01",
          "E2E-FIX-01-S02",
          "E2E-FIX-01-S03"
        ],
        "additionalProperties": false
      },
      "proposed_state": {
        "const": "ABSENT"
      },
      "knowledge_timing": {
        "const": "ABSENT"
      },
      "visual_state": {
        "const": "ABSENT"
      }
    },
    "expected_state_values": {
      "relevant_prior_state": {
        "E2E-FIX-01-S01": {
          "clothing_visual_state_code": "soaked_uniform"
        },
        "E2E-FIX-01-S02": {
          "clothing_visual_state_code": "soaked_uniform"
        },
        "E2E-FIX-01-S03": {
          "clothing_visual_state_code": "changed_clothes"
        }
      },
      "current_state": {
        "E2E-FIX-01-S01": {
          "clothing_visual_state_code": "soaked_uniform"
        },
        "E2E-FIX-01-S02": {
          "clothing_visual_state_code": "changed_clothes"
        },
        "E2E-FIX-01-S03": {
          "clothing_visual_state_code": "changed_clothes"
        }
      },
      "proposed_state": "ABSENT",
      "knowledge_timing": "ABSENT",
      "visual_state": "ABSENT"
    },
    "source_trace": [
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
    ],
    "required_locks_hash": "376e980b7568c66df66627c13086d7d91ec0041bfc0e844086adb2d9a8bf2b40",
    "transition_authority_hash": "f78c4aba7c5597799d0d31c474b9a2fefcdba432130ce72da0befd8d1f0f75a0",
    "downstream_representation": "JSON_OBJECT_OR_EXACT_ABSENT",
    "legacy_string_path": "UNREACHABLE",
    "state_schema_hash": "ed0baf41818b4aff532594483113c8b81a781175843081fcd5f15617ac88032d",
    "source_trace_hash": "69b5d4b90e136cd8c1b7108fcfd21f11f1575b75369a33fd11bf4a1f5bf23001",
    "bundle_hash": "512417519d4eae2b58d6aa490c26f3c86a30f1e8eb866d4ce416b1bba6d9a4bc"
  },
  "five_compiled_field_schemas": {
    "relevant_prior_state": {
      "type": "object",
      "properties": {
        "E2E-FIX-01-S01": {
          "type": "object",
          "properties": {
            "clothing_visual_state_code": {
              "type": "string",
              "enum": [
                "soaked_uniform",
                "changed_clothes"
              ]
            }
          },
          "required": [
            "clothing_visual_state_code"
          ],
          "additionalProperties": false
        },
        "E2E-FIX-01-S02": {
          "type": "object",
          "properties": {
            "clothing_visual_state_code": {
              "type": "string",
              "enum": [
                "soaked_uniform",
                "changed_clothes"
              ]
            }
          },
          "required": [
            "clothing_visual_state_code"
          ],
          "additionalProperties": false
        },
        "E2E-FIX-01-S03": {
          "type": "object",
          "properties": {
            "clothing_visual_state_code": {
              "type": "string",
              "enum": [
                "soaked_uniform",
                "changed_clothes"
              ]
            }
          },
          "required": [
            "clothing_visual_state_code"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "E2E-FIX-01-S01",
        "E2E-FIX-01-S02",
        "E2E-FIX-01-S03"
      ],
      "additionalProperties": false
    },
    "current_state": {
      "type": "object",
      "properties": {
        "E2E-FIX-01-S01": {
          "type": "object",
          "properties": {
            "clothing_visual_state_code": {
              "type": "string",
              "enum": [
                "soaked_uniform",
                "changed_clothes"
              ]
            }
          },
          "required": [
            "clothing_visual_state_code"
          ],
          "additionalProperties": false
        },
        "E2E-FIX-01-S02": {
          "type": "object",
          "properties": {
            "clothing_visual_state_code": {
              "type": "string",
              "enum": [
                "soaked_uniform",
                "changed_clothes"
              ]
            }
          },
          "required": [
            "clothing_visual_state_code"
          ],
          "additionalProperties": false
        },
        "E2E-FIX-01-S03": {
          "type": "object",
          "properties": {
            "clothing_visual_state_code": {
              "type": "string",
              "enum": [
                "soaked_uniform",
                "changed_clothes"
              ]
            }
          },
          "required": [
            "clothing_visual_state_code"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "E2E-FIX-01-S01",
        "E2E-FIX-01-S02",
        "E2E-FIX-01-S03"
      ],
      "additionalProperties": false
    },
    "proposed_state": {
      "const": "ABSENT"
    },
    "knowledge_timing": {
      "const": "ABSENT"
    },
    "visual_state": {
      "const": "ABSENT"
    }
  },
  "source_trace_manifest": [
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
  ],
  "source_records": [
    {
      "scene_id": "E2E-FIX-01-S01",
      "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S01",
      "source_version": "1.0",
      "canonical_owner": "Scene Writer",
      "lifecycle_state": "STATE_LEDGER_COMMITTED",
      "ledger_sequence": 1,
      "state_snapshot": {
        "clothing_visual_state_code": "soaked_uniform"
      }
    },
    {
      "scene_id": "E2E-FIX-01-S02",
      "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S02",
      "source_version": "1.0",
      "canonical_owner": "Scene Writer",
      "lifecycle_state": "STATE_LEDGER_COMMITTED",
      "ledger_sequence": 2,
      "state_snapshot": {
        "clothing_visual_state_code": "changed_clothes"
      }
    },
    {
      "scene_id": "E2E-FIX-01-S03",
      "source_record_id": "E2E-RUN-12/scene_writer/E2E-FIX-01-S03",
      "source_version": "1.0",
      "canonical_owner": "Scene Writer",
      "lifecycle_state": "STATE_LEDGER_COMMITTED",
      "ledger_sequence": 3,
      "state_snapshot": {
        "clothing_visual_state_code": "changed_clothes"
      }
    }
  ],
  "source_artifacts": {
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
  },
  "neutral_schema": {
    "type": "object",
    "additionalProperties": false,
    "required": [
      "selected_mode",
      "primary_state_or_outcome",
      "flags",
      "handoffs",
      "required_outcome",
      "unresolved_decisions",
      "state_evidence",
      "directorial_intent",
      "staging_blocking",
      "audience_information",
      "spatial_geography",
      "camera_coverage_intent",
      "rhythm_transition_intent",
      "production_burden",
      "handoffs_unresolved_issues"
    ],
    "properties": {
      "selected_mode": {
        "type": "string",
        "enum": [
          "PLAN",
          "REVISE",
          "DIAGNOSE"
        ]
      },
      "primary_state_or_outcome": {
        "type": "string",
        "enum": [
          "DIRECTION_PLAN_PRODUCED",
          "DIRECTION_PLAN_REVISED",
          "NO_MATERIAL_DIRECTION_CHANGE",
          "NEEDS_CONTEXT",
          "UPSTREAM_DECISION_REQUIRED",
          "OUT_OF_SCOPE_HANDOFF"
        ]
      },
      "flags": {
        "const": "ABSENT"
      },
      "handoffs": {
        "const": "ABSENT"
      },
      "required_outcome": {
        "type": "string",
        "minLength": 1
      },
      "unresolved_decisions": {
        "anyOf": [
          {
            "const": "ABSENT"
          },
          {
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            }
          }
        ]
      },
      "state_evidence": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "relevant_prior_state",
          "current_state",
          "proposed_state",
          "knowledge_timing",
          "relationship_state",
          "visual_state"
        ],
        "properties": {
          "relevant_prior_state": {
            "type": "object",
            "properties": {
              "E2E-FIX-01-S01": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S02": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S03": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              }
            },
            "required": [
              "E2E-FIX-01-S01",
              "E2E-FIX-01-S02",
              "E2E-FIX-01-S03"
            ],
            "additionalProperties": false
          },
          "current_state": {
            "type": "object",
            "properties": {
              "E2E-FIX-01-S01": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S02": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S03": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              }
            },
            "required": [
              "E2E-FIX-01-S01",
              "E2E-FIX-01-S02",
              "E2E-FIX-01-S03"
            ],
            "additionalProperties": false
          },
          "proposed_state": {
            "const": "ABSENT"
          },
          "knowledge_timing": {
            "const": "ABSENT"
          },
          "visual_state": {
            "const": "ABSENT"
          },
          "relationship_state": {
            "anyOf": [
              {
                "const": "ABSENT"
              },
              {
                "type": "string",
                "minLength": 1
              }
            ]
          }
        }
      },
      "directorial_intent": {
        "type": "string",
        "minLength": 1
      },
      "staging_blocking": {
        "type": "string",
        "minLength": 1
      },
      "audience_information": {
        "type": "string",
        "minLength": 1
      },
      "spatial_geography": {
        "type": "string",
        "minLength": 1
      },
      "camera_coverage_intent": {
        "type": "string",
        "minLength": 1
      },
      "rhythm_transition_intent": {
        "type": "string",
        "minLength": 1
      },
      "production_burden": {
        "type": "string",
        "minLength": 1
      },
      "handoffs_unresolved_issues": {
        "type": "string",
        "minLength": 1
      }
    }
  },
  "strict_schema": {
    "type": "object",
    "additionalProperties": false,
    "required": [
      "selected_mode",
      "primary_state_or_outcome",
      "flags",
      "handoffs",
      "required_outcome",
      "unresolved_decisions",
      "state_evidence",
      "directorial_intent",
      "staging_blocking",
      "audience_information",
      "spatial_geography",
      "camera_coverage_intent",
      "rhythm_transition_intent",
      "production_burden",
      "handoffs_unresolved_issues"
    ],
    "properties": {
      "selected_mode": {
        "type": "string",
        "enum": [
          "PLAN",
          "REVISE",
          "DIAGNOSE"
        ]
      },
      "primary_state_or_outcome": {
        "type": "string",
        "enum": [
          "DIRECTION_PLAN_PRODUCED",
          "DIRECTION_PLAN_REVISED",
          "NO_MATERIAL_DIRECTION_CHANGE",
          "NEEDS_CONTEXT",
          "UPSTREAM_DECISION_REQUIRED",
          "OUT_OF_SCOPE_HANDOFF"
        ]
      },
      "flags": {
        "type": "string",
        "enum": [
          "ABSENT"
        ]
      },
      "handoffs": {
        "type": "string",
        "enum": [
          "ABSENT"
        ]
      },
      "required_outcome": {
        "type": "string"
      },
      "unresolved_decisions": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "ABSENT"
            ]
          },
          {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        ]
      },
      "state_evidence": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "relevant_prior_state",
          "current_state",
          "proposed_state",
          "knowledge_timing",
          "relationship_state",
          "visual_state"
        ],
        "properties": {
          "relevant_prior_state": {
            "type": "object",
            "properties": {
              "E2E-FIX-01-S01": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S02": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S03": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              }
            },
            "required": [
              "E2E-FIX-01-S01",
              "E2E-FIX-01-S02",
              "E2E-FIX-01-S03"
            ],
            "additionalProperties": false
          },
          "current_state": {
            "type": "object",
            "properties": {
              "E2E-FIX-01-S01": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S02": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              },
              "E2E-FIX-01-S03": {
                "type": "object",
                "properties": {
                  "clothing_visual_state_code": {
                    "type": "string",
                    "enum": [
                      "soaked_uniform",
                      "changed_clothes"
                    ]
                  }
                },
                "required": [
                  "clothing_visual_state_code"
                ],
                "additionalProperties": false
              }
            },
            "required": [
              "E2E-FIX-01-S01",
              "E2E-FIX-01-S02",
              "E2E-FIX-01-S03"
            ],
            "additionalProperties": false
          },
          "proposed_state": {
            "type": "string",
            "enum": [
              "ABSENT"
            ]
          },
          "knowledge_timing": {
            "type": "string",
            "enum": [
              "ABSENT"
            ]
          },
          "visual_state": {
            "type": "string",
            "enum": [
              "ABSENT"
            ]
          },
          "relationship_state": {
            "anyOf": [
              {
                "type": "string",
                "enum": [
                  "ABSENT"
                ]
              },
              {
                "type": "string"
              }
            ]
          }
        }
      },
      "directorial_intent": {
        "type": "string"
      },
      "staging_blocking": {
        "type": "string"
      },
      "audience_information": {
        "type": "string"
      },
      "spatial_geography": {
        "type": "string"
      },
      "camera_coverage_intent": {
        "type": "string"
      },
      "rhythm_transition_intent": {
        "type": "string"
      },
      "production_burden": {
        "type": "string"
      },
      "handoffs_unresolved_issues": {
        "type": "string"
      }
    }
  },
  "identity": {
    "result": "PASS",
    "manifest_hash": "eaa15d403996068e2cbb9e877122f16285efc16fe81150014dff26aeff59a2a3",
    "outer_field_count": 15
  },
  "strict_lint": {
    "result": "PASS",
    "unsupported_paths": [],
    "invalid_paths": [],
    "schema_hash": "53786f950536bc2c74a18064d5d4df6f39b6c6de69f6eed0b3334854196c6f80"
  },
  "hash_chain": {
    "repair09j_authority": "0cf9224f7b32f0b75d792ebccd3ac34c4382cd74cb1a9a69c1e4bc123949e070",
    "compiled_run_contract": "181975fa44f96d389bd5470db756f5471e0b88bf2e95e9215dfc5df2c337d6aa",
    "state_schema": "ed0baf41818b4aff532594483113c8b81a781175843081fcd5f15617ac88032d",
    "source_trace": "69b5d4b90e136cd8c1b7108fcfd21f11f1575b75369a33fd11bf4a1f5bf23001",
    "provider_neutral_contract": "2494a854cf3593a83d6c506c461bfa0427254477a7e9f0c434eeed4498645d36",
    "deepseek_projection": "53786f950536bc2c74a18064d5d4df6f39b6c6de69f6eed0b3334854196c6f80",
    "final_function_parameters": "53786f950536bc2c74a18064d5d4df6f39b6c6de69f6eed0b3334854196c6f80",
    "final_wire_payload": "158a6e756cb34ba113a5879e7940c2549dc700ad5cb08cfee229cfc194e7d4c8",
    "system_prompt": "64a04f389b3bfff6e419fd4ddd947585a8bf5edd97329da4cb477c934ff4542e"
  },
  "canonical_skill_hashes": {
    "showrunner": "0847EE3521A915936E97FA1F72D081F0788876F003E071918F517B0A46AE999C",
    "scene_writer": "93E1BE12988F8CAA6CDD76ACB5E6C1BF6AD3CA0DFF5806A2EA93511E66052DFB",
    "director": "807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781",
    "character_acting": "CD96A794D37371B855552C23A2670EBD78A9F2E2D3218152CE568C3B4356B09F",
    "art_director": "8C8DB2370D69863BBA71138A5BBC123B5BC9BBA73E5CCF2F02D8764FFE933C75",
    "continuity": "C64475BD0578BE6C159DF5A0FA0D90A96636160215B00E17AA3C5CC8E7F0B64C",
    "shared_qa": "2F2E0F241766AB0354E471FC4BA0BF4854363622FB87AE013AB56DDDD270476D"
  },
  "legacy_string_path": "UNREACHABLE",
  "provider_calls": 0,
  "executor_calls": 0,
  "role_calls": 0,
  "retries": 0,
  "fallbacks": 0
}
```

## Call integrity

```json
{
  "provider_calls": 1,
  "retries": 0,
  "fallbacks": 0,
  "other_role_calls": 0,
  "e2e_runs": 0
}
```
