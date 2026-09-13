# R02 Repair15 Preflight Provenance

Mandatory Preflight: 15/15 PASS. Environment policy: `PREFLIGHT-SUBPROCESS-ENV-ISOLATION-V0.1`.

Every historical/offline child removed the live-run variables `AFS_E2E_AUTHORIZATION_LABEL`, `AFS_E2E_EVIDENCE_ROOT`, `AFS_E2E_FIXTURE_BINDING`, and `AFS_E2E_RUN_ID`. Fixture-dependent suites received only their manifest-declared fixture binding. Provider credentials injected into preflight children: false.

The redacted per-suite provenance and environment hashes are stored in `preflight.json` under `required_suites.*.environment_provenance`.

