# Scene Entry Snapshot Contract

For S01, ENTRY is the first allowed token from the compiled state dimension. For every later scene, ENTRY is only the preceding scene's validated EXIT snapshot for the same dimension.

ENTRY may not be inferred from the current scene's EXIT evidence, a global latest ledger value, a persistent default, a planned transition, or an authorization-only transition. The source trace must be complete before the snapshot is consumable by the Safeguard.

R24 S01 example: `camera_battery_state` ENTRY is `battery_installed`, with source kind `COMPILED_INITIAL_STATE`.
