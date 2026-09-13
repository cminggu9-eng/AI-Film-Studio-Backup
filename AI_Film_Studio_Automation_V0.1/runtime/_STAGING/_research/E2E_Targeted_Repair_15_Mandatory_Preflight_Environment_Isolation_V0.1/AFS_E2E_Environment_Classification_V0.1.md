# AFS_E2E Environment Classification V0.1

| Class | Variables | Child policy |
|---|---|---|
| LIVE-RUN-SCOPED | `AFS_E2E_RUN_ID`, `AFS_E2E_EVIDENCE_ROOT`, `AFS_E2E_RECOVERY_OF`, `AFS_E2E_AUTHORIZATION_LABEL`, `AFS_E2E_FIXTURE_BINDING` | Remove from every offline child; only a suite manifest may inject a fixture binding. |
| SUITE-SCOPED | Manifest-declared fixture binding | Inject only for that child suite. |
| SAFE GLOBAL / NON-FIXTURE | Explicit operating-system and Python runtime allowlist | Preserve by name only. |
| UNKNOWN | Any other `AFS_E2E_*` name | Remove; never inherit by default. |

No environment value classified as a secret is emitted in provenance evidence.

