---
type: director-mocked-payload-validation-report
status: pass
version: 0.1
---

# Director Mocked Payload Validation Report V0.1

A valid 15-field Director payload passes. The five JSON-object-string values are decoded locally only after their string type and object parse are verified.

The following fail closed: any added field, `scene_packages`, `canon_assignment_locks`, `prohibited_changes`, direct object state values, malformed encoded-object strings, missing required fields, and canonical-token mutation.

No post-hoc field deletion, object-to-string coercion, missing-field insertion, or semantic auto-fill exists.

