# Generation Authority Enforcement Repair V0.1

## Implemented transport changes

The generation request now explicitly states that `assignment_constraint_ledger` is binding current-assignment authority and structurally transports all required domains:

- `LOCKED_FACTS`
- `EXPLICIT_UNKNOWNS`
- `CHARACTER_KNOWLEDGE_LIMITS`
- `TEMPORAL_CONSTRAINTS`
- `RELATIONSHIP_CONSTRAINTS`
- `CAPABILITY_CONSTRAINTS`
- `REQUIRED_EVENTS`
- `REQUIRED_INFORMATION`
- `REQUIRED_OUTCOME`
- `OPEN_CREATIVE_SPACE`

`KNOWLEDGE_TIMING` was added as source-preserving transport metadata: world facts, entry knowledge, explicit unknown/not-yet-known statements, and Assignment-authorized discovery during scene. It does not infer or create any new fact.

## Generation rules added

- Open creative space permits immediate actions, pauses, silence, object interaction, dialogue tactics, and present scene-local choices; it does not permit new facts.
- A new in-scene request/question/conditional proposal is distinct from an asserted pre-existing policy, deadline, commitment, schedule, relationship history, authority, resource, or work arrangement.
- REVISE has an explicit fact-expansion ceiling: the repair may not manufacture an outside plan, obligation, schedule, authority, relationship context, or cause to create resistance.
- Knowledge state must change only after an Assignment-authorized disclosure/action; a request or reaction may not appear after its prerequisite action.

## Evidence and scope

`TR-SW-10–16 = 7 / 7 PASS` in the latest attempt; these are non-network contract checks. This repair does not change dramatic capability semantics, Objective/Resistance/Turn, shootability, Entry/Exit, Production Burden, or authority boundaries. Its real generation validation is blocked pending verifier-gate completion.
