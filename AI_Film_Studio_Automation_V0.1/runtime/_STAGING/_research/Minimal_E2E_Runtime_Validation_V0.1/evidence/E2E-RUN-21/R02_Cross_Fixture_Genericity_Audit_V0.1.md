# R02 Cross-Fixture Genericity Audit V0.1

Result: FAIL.

- Fixture01 scene IDs in R02 prompt/schema: 0 — PASS
- Fixture03 scene IDs in R02 prompt/schema: 0 — PASS
- Fixture02 scene-ID and state-token domains from compiled contract — PASS
- Generic scene-ID literal leak — 0, PASS
- Generic story literal leak — FAIL: prompt transport schema contains `A-17` once
- Function-description provenance — FAIL: description still says `frozen E2E-FIX-01 probe`
- Dynamic state-field isolation — FAIL: hydration emits `clothing_visual_state_code`, validator reads `signboard_state`

Machine evidence: `r02_cross_fixture_genericity_diagnostic.json`.
