# Director State Representation Provenance Audit V0.1

## Scope and method

This is a read-only provenance audit for the five fields that Repair 09F labelled as JSON-object-string fields: `relevant_prior_state`, `current_state`, `proposed_state`, `knowledge_timing`, and `visual_state`. No Provider, executor, role, E2E, or Probe call was made.

Evidence read: the 09B structured-submission implementation and field-ownership map; the 09C DeepSeek projection; the 09F exact-15-field contract; the Integration Contract State Evidence Envelope; the minimal E2E runner; Probe04 output; and E2E-RUN-13/RUN-14 artifacts.

## Field provenance

| Field | Semantic value evidenced | Provider-facing requirement in R14 | Actual Provider response in R14 | Actual downstream representation | Why the string rule exists | Serialization owner |
|---|---|---|---|---|---|---|
| `relevant_prior_state` | object | string containing JSON object | object | object | 09C DeepSeek workaround | no established owner |
| `current_state` | object | string containing JSON object | object | object | 09C DeepSeek workaround | no established owner |
| `proposed_state` | object | string containing JSON object | object | object | 09C DeepSeek workaround | no established owner |
| `knowledge_timing` | object | string containing JSON object | object | object | 09C DeepSeek workaround | no established owner |
| `visual_state` | object | string containing JSON object | object | object | 09C DeepSeek workaround | no established owner |

## Evidence findings

1. `director_structured_submission.py` describes the provider-neutral state branches as object (or `ABSENT`), but its 09F local validator requires strings, parses them, and returns decoded objects.
2. `deepseek_compatible_schema()` replaces the five provider-facing object branches with strings described as JSON-encoded state objects. This is a Provider compatibility projection, not a proven downstream transport contract.
3. The State Evidence Envelope and the minimal E2E runner accept JSON-safe state values and preserve the values they receive. They do not require JSON-object strings and contain no five-field serializer.
4. Probe04 and E2E-RUN-13 persisted objects in `director_output.json`; the historical string was therefore decoded before downstream consumption.
5. E2E-RUN-14 persisted raw objects and was correctly fail-closed by the 09F string-only validator before the existing object-consuming downstream path.

## Provenance decision

The audit proves the semantic values are objects. It does **not** prove that JSON-object strings are the canonical downstream representation, nor does it identify an Integration owner that performs the required deterministic serialization. Current evidence proves the opposite transport behavior: downstream artifacts contain objects.

The required 09G Decision Gate therefore does not pass. A bridge may not be implemented from this evidence without inventing a downstream contract.

