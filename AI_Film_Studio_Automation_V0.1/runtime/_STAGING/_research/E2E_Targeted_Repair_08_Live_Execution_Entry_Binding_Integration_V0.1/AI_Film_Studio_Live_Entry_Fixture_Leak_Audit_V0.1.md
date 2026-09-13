# Live Entry Fixture Leak Audit V0.1

The prior 28 occurrences were in `run_minimal_e2e.py`: role prompts, fixture construction, Continuity signals, scene IDs, Provider fixture projection, assertions, acceptance, and manifest rendering. Each is now sourced from `compiled_run_contract()` (binding `fixture`, `scene_ids`, `state_enums`, safeguard, ledger, or acceptance fields). No literal replacement changed Fixture binding data.
