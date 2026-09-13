# Director E2E-RUN-12 Provider 400 Evidence Audit

Director input and invocation identity were persisted, but the final wire payload and HTTP 400 error body were not. Recorded fact: DeepSeek Beta strict endpoint returned HTTP 400 before a Director payload. `PROVIDER ERROR BODY NOT PERSISTED`; no rejected keyword is asserted.
