# Director Historical State Output Conformance Audit V0.1

## Read-only sources

- Probe04 `director_output.json`
- E2E-RUN-13 `director_output.json`
- E2E-RUN-14 `director_provider_response.json` tool arguments

| Artifact | Observed status | Non-authoritative observations |
|---|---|---|
| Probe04 | NOT ASSESSABLE | prior/current/proposed each include `relationship_state`, `knowledge_state`, `visual_state`, `key_custody`; visual has `clothing_visual_state_code`, `authorized_transition` |
| E2E-RUN-13 | NOT ASSESSABLE | prior/current/proposed each have three state names; visual has `scene_1`, `scene_2`, `scene_3` |
| E2E-RUN-14 | NOT ASSESSABLE; raw Provider object mismatch retained | `relevant_prior_state.source` is an **UNSUPPORTED KEY** because no independent authority supports it; other key names remain observed only |

No artifact is marked CONFORMS because no lawful exact Director schema exists. No schema was loosened to pass a historical example, and no historical file was modified.

