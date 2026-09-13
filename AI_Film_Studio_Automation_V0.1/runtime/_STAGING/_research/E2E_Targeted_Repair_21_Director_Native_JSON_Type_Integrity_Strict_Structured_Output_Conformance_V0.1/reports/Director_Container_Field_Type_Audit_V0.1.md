# Director Container Field Type Audit V0.1

The type reminder and audit are generated from the final schema rather than a hand-maintained alias table.

| Field | Allowed contract domain |
| --- | --- |
| `unresolved_decisions` | exact `ABSENT` or native array of strings |
| `state_evidence` | native object |
| `state_evidence.relevant_prior_state` | native object |
| `state_evidence.current_state` | native object |
| `state_evidence.proposed_state` | exact `ABSENT` |
| `state_evidence.knowledge_timing` | exact `ABSENT` |
| `state_evidence.relationship_state` | exact `ABSENT` or text |
| `state_evidence.visual_state` | exact `ABSENT` |
| `flags`, `handoffs` | exact `ABSENT` |

`relevant_prior_state` and `current_state` remain source-exact objects or lawful `ABSENT`; no legacy object-as-JSON-string path is reachable.

