# Cross-Fixture Parent Environment Matrix V0.1

| Historical suite | Parent fixture | Effective child fixture | Result |
|---|---|---|---|
| SW-INT Fixture01 | Unset | Fixture01 manifest | PASS |
| SW-INT Fixture01 | Fixture01 | Fixture01 manifest | PASS |
| SW-INT Fixture01 | Fixture02 | Fixture01 manifest | PASS |
| SW-INT Fixture01 | Fixture03 | Fixture01 manifest | PASS |

Fixture02 dry-run was also executed with all four parent contexts and always compiled `E2E-FIX-02` with its own manifest-owned Fixture02 binding.

