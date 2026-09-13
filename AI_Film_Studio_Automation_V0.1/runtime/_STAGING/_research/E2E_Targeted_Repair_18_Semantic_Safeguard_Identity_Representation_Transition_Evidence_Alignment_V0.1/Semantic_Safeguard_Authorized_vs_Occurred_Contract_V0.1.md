# Semantic Safeguard Authorized vs Occurred Contract

- AUTHORIZED: present in the current compiled transition authority.
- OCCURRED: exactly one adjacent validated machine-state change from `from_state` to `to_state`.
- OBSERVED: that occurrence has an attributable scene-local evidence locator.
- HANDED_OFF: an explicit downstream handoff fact; it is never inferred from authorization or occurrence.

An allowed/planned/future token, final-scene position, or `authorized_transitions` membership cannot establish OCCURRED. Missing occurrence remains `OCCURRED=false` and is not auto-repaired.

