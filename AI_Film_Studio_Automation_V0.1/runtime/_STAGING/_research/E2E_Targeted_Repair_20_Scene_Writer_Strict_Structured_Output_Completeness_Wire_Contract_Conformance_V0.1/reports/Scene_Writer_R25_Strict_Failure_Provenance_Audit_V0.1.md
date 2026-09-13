# R25 Scene Writer strict-failure provenance audit

## Decision

E2E-RUN-25 is a Provider Strict Structured Output Conformance Failure. It is not a truncation, Repair17 state-field bridge, Repair19 phase-aware safeguard, or adapter projection failure.

## Immutable raw evidence

- Raw response artifact: Minimal_E2E_Runtime_Validation_V0.1/evidence/E2E-RUN-25/artifacts/scene_writer_provider_response.json
- Raw provider-content SHA-256: 24de6a0571f203d751f1dc7ee55ef3c0e61b91369a603ea633e5d485f4eaae82
- Finish reason: tool_calls; requested maximum: 5000; truncation assessment: NOT_TRUNCATED.
- S01 supplied id, content, structural, and state.
- S02 supplied only id and content; S03 supplied only id and content.
- The official first failure remains scenes/1: structural is a required property.

## Attribution boundary

The persisted R25 wire payload contains the exact required structural and state fields for every scenes item. The local strict validator received the same schema and rejected the provider arguments without copying S01, inferring from text, hydrating missing role-owned values, changing required fields, or retrying.

R25 remains historical, read-only evidence. Repair20 does not alter its raw response, failure attribution, validation error, truncation record, or execution status.
