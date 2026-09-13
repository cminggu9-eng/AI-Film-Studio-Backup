# Scene Writer Scene-ID Negative Test Report V0.1

Result: 15/15 PASS.

The suite rejected: Fixture01-in-Fixture02, Fixture03-in-Fixture02, wrong order, duplicate, missing, extra, suffix-only, and previous-run IDs. It also proved no stale Fixture01 prompt/schema/validator acceptance, retained fail-closed behavior for R20's foreign third ID, preserved the recorded response, made no unsupported provider-violation claim, and found zero fixture scene-ID literals in active generic sources.

Calls: provider 0; executor 0; role 0. Replay only: true.

Command: `python -X utf8 tests/run_scene_writer_scene_id_negative_tests.py`.
