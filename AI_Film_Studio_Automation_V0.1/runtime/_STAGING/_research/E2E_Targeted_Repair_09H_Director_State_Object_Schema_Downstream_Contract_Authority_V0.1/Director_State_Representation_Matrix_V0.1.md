# Director State Representation Matrix V0.1

| Boundary | Semantic type | Current/authorized representation | Validator | Owner | Status |
|---|---|---|---|---|---|
| Director semantics | state value | object or `ABSENT` | authority-bound future exact schema | Director / Integration boundary | object type proven; shape gap |
| provider-neutral 09B | state value | object or `ABSENT` | generic object branch | Integration contract | insufficiently strict |
| DeepSeek 09C | same value | JSON-object string or `ABSENT` | legacy function projection | provider adapter | legacy compatibility only |
| 09F local validator | same value | accepts string then decodes object | string parse plus mapping check | Integration | legacy mismatch source |
| State Evidence Envelope | carried value | JSON-safe object or `ABSENT` | no-null / JSON-safe | transport | canonical object carriage |
| State Ledger | carried value | copied object or `ABSENT` | supplied-envelope validation | ledger | canonical object carriage |
| Handoff / display | carried/displayed value | copied object / lossless projection | source attribution / display only | transport | no string bridge |

The matrix resolves downstream representation and ownership but deliberately does not invent the missing strict object schemas.

