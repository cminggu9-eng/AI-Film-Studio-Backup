# Director State Projection Authority Decisions V0.1

## New design authority

Director state schemas are compiled per run from approved machine contracts and validated source records. They are not universal hand-written business schemas. Generic compiler source knows no story literal, scene ID, dimension name, or token.

## Five decisions

| Field | Source/scope decision | Current closed representation |
|---|---|---|
| `relevant_prior_state` | per compiled scene; validated pre-scene snapshot selected by canonical owner, lifecycle, then ledger sequence | dynamic scene-keyed object or source-declared whole-field `ABSENT` |
| `current_state` | per compiled scene; highest valid same-owner-chain ledger sequence for each scene/dimension | dynamic scene-keyed object |
| `proposed_state` | only explicitly Director-writable compiled dimensions; none currently exist | exact `ABSENT` |
| `knowledge_timing` | only a closed machine knowledge record; none currently exists | exact `ABSENT` |
| `visual_state` | only explicitly classified visual/spatial dimensions; no classification metadata currently exists | exact `ABSENT` |

Missing required source, source conflict, projection error, and unknown value always fail closed; none converts to `ABSENT`.

