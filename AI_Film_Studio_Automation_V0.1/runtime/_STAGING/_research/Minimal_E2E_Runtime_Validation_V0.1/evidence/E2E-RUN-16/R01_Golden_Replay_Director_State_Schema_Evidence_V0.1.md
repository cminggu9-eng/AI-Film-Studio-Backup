# R01 Golden Replay Director State Schema Evidence V0.1

Result: PASS

The live Director request used the per-run Fixture01 state-object compiler, exact 15-field contract, deterministic prompt projection, and DeepSeek-compatible strict projection. The source-exact object representation was preserved for `relevant_prior_state` and `current_state`; `proposed_state`, `knowledge_timing`, and `visual_state` remained exact `ABSENT` where required.

- Legacy JSON-object-string path: UNREACHABLE
- Compiled schema identity: verified before network send
- Local state-object validation: PASS
- Evidence: `artifacts/director_final_wire_payload.json`, `artifacts/director_output.json`

