# Semantic Safeguard Transition Authority Provenance Audit

Result: PASS.

Authority is compiled from the current binding's `state_dimensions` and `authorized_transitions`. The shared projection carries transition ID, state dimension, exact from/to states, fixture authority, allowed scene window, decision locks, prohibited outcomes, and the `adjacent_validated_machine_state` evidence requirement.

No transition relationship is inferred from token text. Ambiguous transition-to-dimension association fails closed.

