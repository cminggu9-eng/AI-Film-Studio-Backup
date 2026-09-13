# Scene Writer Response Truncation Detection Audit V0.1

## Detection Contract

`TRUNCATED_RESPONSE` is detected without repairing content by combining:

1. provider `finish_reason` when supplied;
2. completion-token contact with the requested cap;
3. JSON completeness; and
4. durable raw-response, usage, invocation, and persistence-verification evidence.

A `finish_reason: length` response, or incomplete JSON that exactly contacts the completion cap, is an `EXECUTOR / RESPONSE-BUDGET FAILURE`. It is never a role semantic failure and never triggers JSON repair, continuation, or a second call.

## Offline Result

TRUNC-01 through TRUNC-04: **4/4 PASS**. The detector distinguishes provider length, incomplete-at-cap, malformed-below-cap, and complete `stop` output.

## Probe Comparison

| Run | Signal | Classification |
| --- | --- | --- |
| Probe 01 | 3,500 completion tokens, incomplete JSON | Response-budget truncation baseline. |
| Probe 02 | `finish_reason: stop`, 1,756/5,000 tokens, invalid JSON | `NOT_TRUNCATED`; executor serialization failure. |

Probe 02 therefore demonstrates that response-budget and malformed-serialization failures are not conflated.

