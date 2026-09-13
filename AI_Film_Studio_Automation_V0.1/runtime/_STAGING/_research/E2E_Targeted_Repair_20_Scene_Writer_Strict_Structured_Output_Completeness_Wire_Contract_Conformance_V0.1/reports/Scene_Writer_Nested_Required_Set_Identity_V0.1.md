# Scene Writer nested required-set identity

The schema-identity manifest records every nested object required-set for compiled, final strict, adapter-projected, wire, and local-validator forms. All five maps are equal.

- Root: format, control, state, scenes.
- Control: outcome, flags, handoffs, required_outcome, unresolved_decisions.
- State: prior, current, proposed, knowledge_timing, relationship, visual.
- Each scenes item: id, content, structural, state.
- Structural: the six frozen structural field names.
- State: nine F03 role-owned state fields, including the compiled camera_battery_state field.

This is an identity audit only. It cannot manufacture a value where a provider omitted a required field.
