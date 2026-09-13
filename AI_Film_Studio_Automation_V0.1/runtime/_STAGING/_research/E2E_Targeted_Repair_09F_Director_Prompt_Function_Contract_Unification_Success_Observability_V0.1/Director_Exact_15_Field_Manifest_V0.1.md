---
type: director-exact-15-field-manifest
status: pass
version: 0.1
---

# Director Exact 15-Field Manifest V0.1

The only allowed and required structured Director fields are:

`selected_mode`, `primary_state_or_outcome`, `flags`, `handoffs`, `required_outcome`, `unresolved_decisions`, `state_evidence`, `directorial_intent`, `staging_blocking`, `audience_information`, `spatial_geography`, `camera_coverage_intent`, `rhythm_transition_intent`, `production_burden`, `handoffs_unresolved_issues`.

`canon_assignment_locks`, `prohibited_changes`, `scene_packages`, and generic `content` are runtime/envelope slots, not function arguments. Any occurrence in function arguments fails closed.

