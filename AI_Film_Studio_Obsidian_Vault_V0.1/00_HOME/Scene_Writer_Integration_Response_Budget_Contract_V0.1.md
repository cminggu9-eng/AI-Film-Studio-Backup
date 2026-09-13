# Scene Writer Integration Response Budget Contract V0.1

## Classification

The fixed three-scene Scene Writer package is a `LARGE_STRUCTURED_DELIVERABLE`: it must carry three readable scenes, six structural fields per scene, machine state codes, display prose, source/version attribution, evidence locators, and immutable assignment locks.

## Policy

| Field | Value |
| --- | --- |
| Selected completion budget | 5,000 tokens |
| Local policy ceiling | 6,000 tokens |
| Prior failed cap | 3,500 tokens |
| Added headroom | 1,500 tokens / 42.9% |
| Provider/model | DeepSeek / `deepseek-v4-pro` |
| Provider documented maximum | 384,000 tokens |
| Retry / fallback | 0 / 0 |

The policy is explicit per invocation, recorded in provider evidence, finite, and validated before a Provider request. It is not a global unlimited setting.

## Selection Basis

Probe 01 reached 3,500 completion tokens with incomplete JSON. Repair 02 pairs a 5,000-token budget with compact transport serialization: the offline equivalent shrank from 3,366 to 1,879 characters while preserving all semantic-bearing values. The additional 1,500 tokens supply bounded completion headroom without selecting an extreme maximum.

## Safe Stop

If selected budget is non-positive, exceeds the local ceiling, does not exceed the historical cap, or cannot be shown below the documented provider ceiling, preflight returns `SINGLE-CALL SERIALIZATION NOT VIABLE` before any Provider call. No multi-call replacement is authorized.

