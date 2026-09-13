# Repair23 Probe22 Corrected Replay

Immutable source: DIRECTOR-TAGGED-WIRE-PROBE-22-F03 raw provider response, SHA-256 d9f743c15c218624788639eaaa6d84c2c0dff239b24c2fbe9ac174649ab3a3d6.

Replay sequence:

1. Wire schema validation: **PASS**
2. Tagged-union lossless decode: **PASS**
3. Canonical 15-field validation: **PASS**
4. Corrected authoritative handoff validation: **PASS**

The corrected path uses project_authoritative_handoff_constraints on the R26 Scene Writer role result once and reuses that projection for canonical construction and handoff comparison. Received locks equal the six sent locks in exact source order; prohibitions also match exactly.

Provider / Executor / Role / Probe / Live E2E calls: 0 / 0 / 0 / 0 / 0.

Probe22 historical result remains FAIL and was not retroactively changed.
