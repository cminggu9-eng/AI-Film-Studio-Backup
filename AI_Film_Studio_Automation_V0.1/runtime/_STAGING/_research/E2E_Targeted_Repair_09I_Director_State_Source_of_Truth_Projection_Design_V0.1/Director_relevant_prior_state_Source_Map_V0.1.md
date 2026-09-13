# Director relevant_prior_state Source Map V0.1

| Map element | Source-backed finding |
|---|---|
| Primary authority source | State Evidence record / State Ledger snapshot, when a prior entry is explicitly selected |
| Secondary carried source | source envelope `source_record_id`, `version`, authority source, locks/prohibitions |
| Projection owner | Integration |
| Projected keys | **OPEN**: no approved rule selects a prior entry or defines a minimal relevant projection |
| Requiredness / type | outer field must be object or exact `ABSENT`; inner properties OPEN |
| Token source | any carried machine values must retain the selected compiled contract domains; mapping OPEN |
| Forbidden-key source | Director Authority Lock plus exact outer contract; no model-added facts |
| ABSENT rule | lawful only when an approved input declares no prior record; not for unknown/missing projection |
| Director writable dimensions | none for upstream facts |
| Failure route | missing selection/schema -> `STATE SOURCE CONFLICT` / `CONTRACT DESIGN REQUIRED` |

`AUTHORITY OPEN`: State Ledger is append-only but has no canonical “relevant prior record” selection rule for a Director invocation. Choosing one by recency or model relevance would violate 09I.

