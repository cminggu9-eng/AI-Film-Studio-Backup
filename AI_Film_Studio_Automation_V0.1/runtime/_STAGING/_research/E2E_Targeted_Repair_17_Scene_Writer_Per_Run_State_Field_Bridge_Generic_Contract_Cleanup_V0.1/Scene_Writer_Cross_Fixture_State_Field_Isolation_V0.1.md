# Scene Writer Cross-Fixture State-Field Isolation V0.1

Result: PASS.

Both compile orders passed: F01 -> F02 -> F03 and F03 -> F02 -> F01. Each run produced a distinct projection hash and contained only its own field, tokens, entities, and transitions. No module-level fixture cache or previous-run fallback is used.
