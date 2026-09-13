---
type: director-probe-03-contract-drift-audit
status: audited
version: 0.1
---

# Director Probe 03 Contract Drift Audit V0.1

| Contract layer | Expected | Probe 03 actual | Result |
| --- | --- | --- | --- |
| Prompt field set | Legacy generic 10-field transport description | Model followed both prompt and function context | drift confirmed |
| Function parameters | exact 15 Director structured fields | 15 required fields present | Provider accepted request |
| Model output | no additional fields; 5 object-state values encoded as strings | added `canon_assignment_locks`, `prohibited_changes`, `scene_packages`; five values were JSON objects | local fail-closed rejection |
| Local validator | exact 15 fields and 5 JSON-object strings | rejected at exact-field gate | correct safe stop |

Probe 03 raw wire evidence proves the generic prompt advertised `scene_packages`, locks/prohibitions, and `object or ABSENT` state values, while the final function schema did not. This repair treats that as a transport-composition failure, not a semantic failure.

