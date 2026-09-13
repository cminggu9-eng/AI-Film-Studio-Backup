# Director R26 Immutable Replay V0.1

R26 was read only. Its raw, wire, invocation, persistence, truncation, and validation artifacts were hash-checked before and after replay.

- Raw Provider response still carries `unresolved_decisions` as a string.
- Diagnostic-only decoding confirms the inner text is an array, but local strict validation still fails.
- No R26 artifact was rewritten, appended, normalized, or retroactively passed.
- R26 status remains `BLOCKED`, with 3 provider calls, 0 retries, and 0 fallback.

This is an immutable replay proof, not an R26 retry.

