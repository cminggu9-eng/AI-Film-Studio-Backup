---
type: director-success-response-observability-contract
status: implemented-and-mocked
version: 0.1
---

# Director Success Response Observability Contract V0.1

Before tool parsing or local validation, a successful adapter response now carries HTTP status and a minimal trace-header record through `ModelExecutor` into the existing raw-first persistence artifacts.

Persisted success evidence includes status, raw body, trace headers, Provider request ID, usage, finish reason, invocation ID, and timestamp. The trace policy permits only:

`x-ds-trace-id`, `x-request-id`, `request-id`, `traceparent`, `x-amzn-trace-id`.

Each absent trace header is recorded as `ABSENT`. Authorization/cookie headers and credentials are never persisted. Mocked success verification confirms both raw-response and invocation-metadata artifacts contain status and trace evidence before structured-tool parsing.

