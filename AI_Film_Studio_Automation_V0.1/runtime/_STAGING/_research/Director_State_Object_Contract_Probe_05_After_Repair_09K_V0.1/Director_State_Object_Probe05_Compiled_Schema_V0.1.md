# Director State Object Probe05 Compiled Schema V0.1

## Compiler

DIRECTOR_STATE_OBJECT_SCHEMA_COMPILER_V0.1

## Fixture

E2E-FIX-01

## Five schemas

```json
{
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
}
```

## Hash chain

```json
{
  "repair09j_authority": "0cf9224f7b32f0b75d792ebccd3ac34c4382cd74cb1a9a69c1e4bc123949e070",
  "compiled_run_contract": "181975fa44f96d389bd5470db756f5471e0b88bf2e95e9215dfc5df2c337d6aa",
  "state_schema": "ed0baf41818b4aff532594483113c8b81a781175843081fcd5f15617ac88032d",
  "source_trace": "69b5d4b90e136cd8c1b7108fcfd21f11f1575b75369a33fd11bf4a1f5bf23001",
  "provider_neutral_contract": "2494a854cf3593a83d6c506c461bfa0427254477a7e9f0c434eeed4498645d36",
  "deepseek_projection": "53786f950536bc2c74a18064d5d4df6f39b6c6de69f6eed0b3334854196c6f80",
  "final_function_parameters": "53786f950536bc2c74a18064d5d4df6f39b6c6de69f6eed0b3334854196c6f80",
  "final_wire_payload": "158a6e756cb34ba113a5879e7940c2549dc700ad5cb08cfee229cfc194e7d4c8",
  "system_prompt": "64a04f389b3bfff6e419fd4ddd947585a8bf5edd97329da4cb477c934ff4542e"
}
```
