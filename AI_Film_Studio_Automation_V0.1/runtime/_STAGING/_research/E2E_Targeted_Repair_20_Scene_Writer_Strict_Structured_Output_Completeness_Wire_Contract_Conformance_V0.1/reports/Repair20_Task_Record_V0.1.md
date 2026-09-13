# Repair20 task record

- Authorization: E2E Targeted Repair 20, Scene Writer strict structured-output completeness and wire contract conformance.
- Root cause: provider omitted role-owned required fields in later scenes despite a correct strict wire schema.
- Repair: dynamically derive an independent-per-scene completeness instruction from the final strict schema; persist and enforce a pre-send five-way schema identity manifest.
- Offline validation: positive 20/20, negative 15/15, Mandatory Preflight 15/15, GEN 18/18, Unified Phase2 25/25.
- Live validation: exactly one new F03 Scene Writer-only strict probe, PASS, no retry.
- Next state: Repair20 complete, awaiting review.
