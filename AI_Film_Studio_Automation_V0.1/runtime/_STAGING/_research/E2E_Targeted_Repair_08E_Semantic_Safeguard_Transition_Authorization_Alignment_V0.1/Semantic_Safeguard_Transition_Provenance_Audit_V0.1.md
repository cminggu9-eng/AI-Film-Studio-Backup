# Safeguard Transition Provenance Audit

`UNAUTHORIZED_STATE_CHANGE` came from `build_scene_assertions`: it inspected only the final scene, although the actual authorized transition was in Scene 3. The authority source is now one binding-derived projection, not a hardcoded final-scene assertion.
