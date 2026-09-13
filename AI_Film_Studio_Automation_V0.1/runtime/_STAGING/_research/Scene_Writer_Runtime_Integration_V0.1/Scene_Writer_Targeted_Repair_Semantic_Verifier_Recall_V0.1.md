# Semantic Verifier Recall Repair V0.1

## Implemented approach

- Added `CHARACTER_KNOWLEDGE_TIMING_DRIFT` to the verifier-only integrity category set.
- Reframed verification as claim-to-ledger comparison across creative and relevant control text: causal, temporal, relationship/history, capability, knowledge/timing, authority, resource, obligation, and existing-fact claims.
- Preserved the public Runtime envelope exactly as `integrity_result` plus `violations`; no rewrite or artistic-quality assessment is permitted.
- Added an internal structured claim-audit and an independent adjudication call through the same shared `ModelExecutor`. These are detector evidence only, not a new Scene Writer or public creative output.
- The final staging iteration additionally uses punctuation/line segmentation to require audit coverage of every supplied candidate span. It is structural segmentation only; it contains no semantic keyword list, synonym catalogue, regex semantic gate, or deterministic pass/fail classifier.

## Observed result

The repair did not meet the acceptance gate. Before exhaustive candidate coverage, F03 was repeatedly returned as `PASS`; audit evidence from attempt 4 showed the verifier omitted the exact unsupported prior-work clause rather than classifying it. With exhaustive candidate coverage enabled, the provider returned non-JSON verifier responses for F03 and the first clean replay case. Therefore the final verifier transport is not sufficiently reliable for the authorised rerun gate.

## Decision

`VERIFIER RECALL / RESPONSE-RELIABILITY REMAINS UNRESOLVED.` No lexical arms race was introduced, and no further replay sampling was performed after the final failed attempt.
