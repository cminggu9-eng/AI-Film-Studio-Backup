---
type: director-strict-compatibility-probe-03-provider-response
status: provider-success-local-validation-failed
version: 0.1
---

# Director Strict Compatibility Probe 03 — Provider Response V0.1

DeepSeek accepted the strict request and returned one `submit_director_package` tool call with empty assistant prose. The raw response, invocation metadata, usage, and persistence verification were written before local validation.

| Item | Value |
| --- | --- |
| Provider invocation ID | `fd504697-3928-4e30-9a75-72d27e784a36` |
| Finish reason | `tool_calls` |
| Prompt / completion / total tokens | `13752 / 2474 / 16226` |
| Latency | `48668 ms` |
| Truncation | `NOT_TRUNCATED` |
| Raw response SHA-256 | `7dd4497930bca1397b64b3c416ca2cb406b12754f75899c6b3e50ba3c094beae` |

The response persistence artifact proves durable raw evidence. However, the successful-response artifact does not separately persist HTTP status or response tracing headers; this is an observability gap recorded in the final review.

