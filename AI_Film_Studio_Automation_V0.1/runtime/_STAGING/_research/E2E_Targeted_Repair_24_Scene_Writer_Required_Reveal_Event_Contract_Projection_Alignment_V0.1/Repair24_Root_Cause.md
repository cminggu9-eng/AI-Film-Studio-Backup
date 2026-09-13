# Repair24 Root Cause

## Classification

`SCENE WRITER REVEAL-EVENT CONTRACT PROJECTION FAILURE`

Fixture03 is authoritative through `acceptance_evidence.reveal = withheld_photo_reveal`, matched to its sole `knowledge_events` record with `not_before_scene = 2`. The same binding shape exists for Fixtures01 and 02.

Before Repair24, the compiled run contract preserved `knowledge_events` only inside the semantic-safeguard input. Scene Writer's provider prompt received neither the accepted event nor its eligible scene range. The strict transport schema correctly limited `state.reveal` to `NOT_YET_REVEALED` and `REVEALED_WITH_EVENT`, but could not express the cross-scene requirement. Separately, the handoff validator unconditionally required one reveal token without deriving the condition or timing from compiled authority.

Therefore R27 cannot be attributed to provider conformance: its provider-facing contract was incomplete. No prose was read or used as reveal evidence.

## Corrected Authority Path

`fixture.acceptance_evidence.reveal -> fixture.knowledge_events[event_id] -> compiled_run_contract.reveal_event_contract -> Scene Writer prompt and final-wire evidence -> handoff validator`

The projection carries event identity, holder, `not_before_scene`, ordered eligible scene IDs, the two allowed status codes, required status, source pointers, and a deterministic hash. The validator verifies that projection against the same compiled fixture before it evaluates only `state_evidence.reveal_status`.
