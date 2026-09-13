# Repair24 R27 Recorded Replay

Replay source: `Minimal_E2E_Runtime_Validation_V0.1/evidence/E2E-RUN-27/artifacts/scene_writer_provider_response.json`

This was an offline, raw-first replay. The provider response, tool arguments, and R27 directory were not edited.

| Stage | Result |
| --- | --- |
| Recorded provider tool arguments parsed | PASS |
| Existing strict wire schema validation | PASS |
| Existing compact decode and canonical transport validation | PASS |
| Raw `state.reveal` tokens | `NOT_YET_REVEALED`, `NOT_YET_REVEALED`, `NOT_YET_REVEALED` |
| Corrected authoritative handoff validation | FAIL-CLOSED: `REQUIRED_REVEAL_EVENT` |

The source response SHA-256 remains `dda048a83ca434d3553d8835af9e4862f67ec8d4f707dd1cd26ebc446db493e8`.

R27 remains a historical failure. It was not converted to PASS, retried, semantically repaired, or used as a new Provider call.
