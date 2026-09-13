---
type: director-final-wire-payload-evidence-contract
status: completed
version: 0.1
---

# Director Final Wire Payload Evidence Contract V0.1

## Before-send invariant

For every structured Director invocation, the runner calls `DeepSeekProviderAdapter.build_provider_payload()` and persists the exact redacted object returned by that builder before network send. This is the actual beta chat-completions wire representation, not a provider-neutral contract.

## Captured fields

The evidence includes endpoint, model, messages, thinking/request options, max tokens, stream setting, tools, function name, `strict`, final `parameters`, and `tool_choice`. Deterministic JSON serialization (`sort_keys=True`, compact separators, UTF-8) produces the wire hash.

## Hash lineage

Probe 03 persisted all four hashes:

| Stage | SHA-256 |
| --- | --- |
| Provider-neutral Director contract | `3adbf243cc99866251c09091f35c62820322c1b85072c3b5c34f2bce8ac5f8f8` |
| DeepSeek compatibility projection | `a5d063d2a455e6dca09935b07828b4d538589909bae5584991ea63e94d4ac11e` |
| Final function parameters | `a5d063d2a455e6dca09935b07828b4d538589909bae5584991ea63e94d4ac11e` |
| Final wire payload | `08b61fb7ffedf4bd0d7402d528defed63bfa9afebeaef3a5e1e7a0fee8b4fc5f` |

## Evidence location

`../E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1/evidence/DIRECTOR-COMPATIBILITY-PROBE-03/artifacts/director_final_wire_payload.json`

The artifact contains no secret request headers or environment values.

