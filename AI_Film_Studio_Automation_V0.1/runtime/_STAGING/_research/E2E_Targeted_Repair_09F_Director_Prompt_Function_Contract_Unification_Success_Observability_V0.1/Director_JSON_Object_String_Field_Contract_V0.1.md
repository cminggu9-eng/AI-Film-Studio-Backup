---
type: director-json-object-string-field-contract
status: implemented
version: 0.1
---

# Director JSON Object String Field Contract V0.1

| Field | Semantic meaning | Function representation | Local rule | Downstream consumer |
| --- | --- | --- | --- | --- |
| `relevant_prior_state` | inherited prior facts | JSON-object string or `ABSENT` | parse and require object | State Evidence Envelope |
| `current_state` | present factual state | JSON-object string or `ABSENT` | parse and require object | State Evidence Envelope |
| `proposed_state` | lawful intended state | JSON-object string or `ABSENT` | parse and require object | State Evidence Envelope |
| `knowledge_timing` | reveal/knowledge timing | JSON-object string or `ABSENT` | parse and require object | State Evidence Envelope |
| `visual_state` | visual continuity state | JSON-object string or `ABSENT` | parse and require object | State Evidence Envelope |

`relationship_state` remains a text field or `ABSENT`; it is not one of the five object-string fields. No adapter coercion is permitted: direct objects fail locally.

