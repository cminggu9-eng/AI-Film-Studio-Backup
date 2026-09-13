# Scene Writer Strict Structured Output Contract V0.1

## Scope

This is an Integration-only response transport contract for the frozen `E2E-FIX-01` Scene Writer probe. It is not a new Scene Writer capability contract and does not alter Canon, authority, creative rules, modes, or canonical tokens.

## Provider-neutral contract

| Field | Value |
| --- | --- |
| Transport | forced structured function response |
| Function | `submit_scene_writer_package` |
| Formal result channel | one function-call `arguments` object only |
| Ordinary assistant prose | rejected as a formal result |
| Standard `json_object` parallel route | prohibited |
| Auto-repair / tolerant parse / continuation | prohibited |

The provider-neutral request carries a function name, description, and parameter schema. The Provider Adapter exclusively maps those values to the chosen provider API.

## Contract source and coverage

The schema is a constrained representation of the already accepted:

- `Scene_Writer_Integration_Output_Contract_V0.1`
- `Scene_Writer_Integration_State_Contract_V0.1`
- `Scene_Writer_Compact_Serialization_Contract_V0.1`

It requires the compact top-level `format`, `control`, `state`, and `scenes`; the frozen three scene IDs; the six structural fields `目标`, `阻力`, `对白行动`, `转折`, `入场`, `出场`; `A-17`; reveal and clothing machine codes; display prose; knowledge timing; custody; and authorized clothing transition data.

## Validation order

`Provider response → raw response / usage persistence → required tool call → strict argument parse → schema validation → existing compact hydration → existing Structural Contract Gate → existing State Token Gate → Semantic Safeguard → downstream eligibility`

No generated content is rewritten in this route. Hydration only restores the pre-existing integration shape and immutable run metadata.

## Human text safety

Chinese dialogue, quotes, line breaks, and control characters travel as provider/SDK JSON function arguments. The creative role is not asked to hand-escape JSON.
