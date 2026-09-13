# Director State Source Conflict Rules V0.1

1. Use a source only when its record identity, version, authority source, and applicable compiled binding are explicit.
2. Retain the source's canonical owner; never merge values by heuristic or ask the Director/Provider to choose.
3. Existing State Ledger order is append-only evidence order, not an approved Director “winner” rule.
4. If a specific existing contract supplies a version authority or named record reference, use that exact rule.
5. Otherwise, conflicting or multiply eligible sources produce `STATE SOURCE CONFLICT -> FAIL CLOSED -> UPSTREAM_DECISION_REQUIRED`.

This prevents “latest blindly” selection and keeps source selection an explicit authority decision.

