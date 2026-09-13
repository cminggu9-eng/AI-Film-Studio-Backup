---
type: director-provider-error-observability-contract
status: completed-with-targeted-provider-constraint
version: 0.1
---

# Director Provider Error Observability Contract V0.1

## Scope and boundary

This repair adds raw-first evidence at the DeepSeek HTTP error boundary. It does not alter a canonical Skill, Director semantics, strict mode, upstream artifacts, or historical evidence.

## Implemented evidence order

1. The adapter catches `HTTPError`, reads the raw response bytes, and sanitizes response headers before raising `ProviderHTTPError`.
2. The runner persists the structured error evidence before it classifies or re-raises the failure.
3. The record contains invocation ID, endpoint, status, raw body, parsed JSON body when valid, provider code/type/param/message, safe trace headers, and UTC timestamp.
4. An empty response body is represented literally as `EMPTY ERROR BODY`.

## Sensitive-data rule

No request headers are persisted. `Authorization`, `Cookie`, `Set-Cookie`, and case variants are excluded from captured headers. The captured Probe 03 response contains only response metadata and `x-ds-trace-id`; it contains no credential material.

## Observed result

`DIRECTOR-COMPATIBILITY-PROBE-03` persisted its error record before classification at:

`../E2E_Targeted_Repair_09C_Director_Strict_Provider_Compatibility_V0.1/evidence/DIRECTOR-COMPATIBILITY-PROBE-03/artifacts/director_provider_http_error.json`

The real HTTP 400 message is preserved verbatim in that artifact and identified the exact structural requirement for the next repair.

