# Director current_state Selection Contract V0.1

`current_state` is the latest validated scene-local snapshot at Director handoff, retained separately for every compiled scene.

Candidate records must be validated Scene Writer scene packages accepted by the semantic safeguard and committed to the run-local Ledger. For the same `scene_id` and dimension, the winner order is: canonical owner, validated lifecycle position, then highest valid Ledger `sequence` within the same ownership chain. Timestamp and Provider order never decide.

Same-authority records at the same lifecycle position with incompatible values produce `STATE SOURCE CONFLICT` and fail closed. The output schema is the same fully closed scene-keyed dynamic object used for prior state, with property names and enums inherited from the compiled strict state schema.

Status: **AUTHORITY CLOSED**.

