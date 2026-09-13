# Director E2E-RUN-14 Recorded Response Regression V0.1

## Immutable baseline

E2E-RUN-14 remains `BLOCKED`. Its Director request reached HTTP 200 with the correct `submit_director_package` call, but the five state fields were raw objects where the 09C projection and 09F local validator demanded JSON-object strings. Local validation failed closed; retries and fallbacks were zero.

## Read-only replay assessment

The raw response is suitable evidence that the provider emitted objects. It is not suitable for a 09G positive recorded-response regression because:

1. no exact semantic object schema exists to validate the response, and
2. no downstream canonical string boundary exists to receive a serialized result.

No replay code ran, no artifact was overwritten, and the historical status was not changed.

