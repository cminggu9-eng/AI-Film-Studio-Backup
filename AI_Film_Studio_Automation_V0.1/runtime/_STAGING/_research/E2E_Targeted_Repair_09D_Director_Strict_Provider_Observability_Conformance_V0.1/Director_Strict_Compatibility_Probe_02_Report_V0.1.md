---
type: director-strict-compatibility-probe-report
status: failed-with-exact-constraint
version: 0.1
---

# Director Strict Compatibility Probe 02 Report V0.1

## Execution

- Runtime evidence ID: `DIRECTOR-COMPATIBILITY-PROBE-03` (the second new compatibility attempt across Repair 09C/09D; this document retains the requested 09D deliverable name).
- Provider calls: `1`
- Retries: `0`
- Fallbacks: `0`
- Upstream roles executed: `0`
- E2E reruns: `0`
- Endpoint: `https://api.deepseek.com/beta/chat/completions`
- Model: `deepseek-v4-pro`

## Before-send proof

The redacted final payload and all four lineage hashes were persisted before send. See `director_final_wire_payload.json` under the Probe 03 artifact root.

## After-response proof

HTTP status was `400`. The response body parsed successfully and reports `invalid_request_error`; trace ID is `eb5b97b249e1c8810ebd214c9bb4cf90`.

## Result

The server rejected a schema node lacking `type`, `anyOf`, and `$ref`. Payload inspection identifies the nine enum-only `ABSENT` nodes listed in the lint report. No retry or additional probe was executed.

## Historical integrity

E2E-RUN-12 and the historical Repair 09C evidence were not rewritten. Probe 03 is new evidence created under the existing compatibility probe evidence convention.

