# SW-INT-01 Environment Contamination Reproduction V0.1

Provider calls: 0.

With the old inherited subprocess environment and parent `AFS_E2E_FIXTURE_BINDING=E2E-FIX-02`, the Fixture01 SW-INT suite reproduced the recorded result: 14/15, with `SW-INT-01` failing `Scene package IDs are not exact and ordered`.

The producer used Fixture01 historical IDs while the imported runner validated against inherited Fixture02 IDs. This proves the original failure was a preflight environment contamination, not a role semantic failure.

