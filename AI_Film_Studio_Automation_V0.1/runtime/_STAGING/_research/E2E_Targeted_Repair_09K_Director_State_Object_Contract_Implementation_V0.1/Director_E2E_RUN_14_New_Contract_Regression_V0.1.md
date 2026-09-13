# Director E2E-RUN-14 New Contract Regression V0.1

Recorded conformance result: **NON-CONFORMING — FAIL CLOSED**.

The immutable R14 Director raw artifact was read only. Its `proposed_state`, `knowledge_timing`, and `visual_state` are objects, while the Repair 09J/09K contract requires exact `ABSENT`. Its prior/current objects also do not match the compiled scene-keyed schema. The new local validator rejected the payload without coercion or fallback (`DIR-OBJ-17`).

R14 historical status remains BLOCKED and was not modified. Raw artifact SHA-256 remains `b6f0481da8c2eae4bff3baaf60abfbaba4308b422a8e03263dd12b4287d7ad18`. Provider Calls: 0.
