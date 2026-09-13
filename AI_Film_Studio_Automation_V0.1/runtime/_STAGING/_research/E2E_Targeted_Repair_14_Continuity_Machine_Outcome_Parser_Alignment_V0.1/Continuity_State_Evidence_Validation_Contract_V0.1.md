# Continuity State Evidence Validation Contract V0.1

`state_evidence` must be a JSON object with exactly:

- `relevant_prior_state`
- `current_state`
- `proposed_state`
- `knowledge_timing`
- `relationship_state`
- `visual_state`

Each dimension is a JSON object or exact `ABSENT`. Missing/extra keys, lists/scalars, null, or non-JSON values fail as `STATE TRANSPORT FAILURE`. Keyword-rich prose cannot repair invalid structure. The validator does not infer missing state or require all optional dimensions to be populated.

