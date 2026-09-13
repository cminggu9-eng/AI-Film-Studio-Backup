---
type: systemic-hardening-golden-baseline
status: frozen-validation-baseline
version: 0.1
scope: E2E-RUN-05 evidence only
---

# AI Film Studio Golden E2E Baseline V0.1

## Baseline declaration

`E2E-RUN-05` is frozen as the Golden E2E Baseline for runtime-validation regression comparison. It is a validation baseline, not story Canon, not a creative reference, and not permission to reuse or rewrite its creative material.

| Field | Frozen value |
| --- | --- |
| Run / fixture | `E2E-RUN-05` / `E2E-FIX-01` |
| Status | `PASS` |
| Provider / model | `deepseek` / `deepseek-v4-pro` |
| Invocation count | `7` exactly; recovery budget `0`; retries `0`; fallback `0` |
| Role chain | Showrunner → Scene Writer → Director → Character & Acting → Art Director → Continuity → Shared QA |
| Acceptance | `E2E-INT-01`–`E2E-INT-18`: `18/18 PASS` |
| Evidence root | `E:\AI_Film_Studio\AI_Film_Studio_Automation_V0.1\runtime\_STAGING\_research\Minimal_E2E_Runtime_Validation_V0.1\evidence\E2E-RUN-05` |

## Frozen role outcomes

| Role | Recorded outcome | Provider / persistence / contract |
| --- | --- | --- |
| Showrunner | `PASS` | `true / true / true` |
| Scene Writer | `SCENE_CREATED` | `true / true / true` |
| Director | `DIRECTION_PLAN_PRODUCED` | `true / true / true` |
| Character & Acting | `PERFORMANCE_INTERPRETATION_READY` | `true / true / true` |
| Art Director | `DESIGN_RESPONSE_READY` | `true / true / true` |
| Continuity | `CONTINUITY PRESERVED` | `true / true / true` |
| Shared QA | `PASS / NO CHANGE` | `true / true / true` |

## Integrity baseline

- Six handoffs are recorded in order, with one envelope for each adjacent pair in the role chain.
- The append-only state ledger contains three ordered Scene Writer state records (`001`–`003`).
- Raw provider evidence was persisted and verified for every call before contract evaluation; all calls are marked `NOT_TRUNCATED`.
- Scene Writer alone used the recorded strict function transport; its arguments were parsed and schema-validated with no transport auto-repair.
- Semantic safeguard decision: `PASS`; creative-output rewrite: `PROHIBITED`; legacy verifier remains `SUPPLEMENTAL_SIGNAL_ONLY`.

| Usage / integrity counter | Frozen value |
| --- | --- |
| Input / completion / total tokens | `80621 / 10888 / 91509` |
| Estimated cost | `CNY 0.2698726` |
| Canonical Skill hash change | `0` (`7/7 unchanged`) |
| Production Lock change | `0` |
| Semantic auto-repair | `0` |
| Nuwa / DB-RAG / image-video-ComfyUI calls | `0 / 0 / 0` |

## Canonical hash baseline

| Canonical Skill | SHA-256 recorded by E2E-RUN-05 |
| --- | --- |
| Showrunner | `0847EE3521A915936E97FA1F72D081F0788876F003E071918F517B0A46AE999C` |
| Scene Writer | `93E1BE12988F8CAA6CDD76ACB5E6C1BF6AD3CA0DFF5806A2EA93511E66052DFB` |
| Director | `807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781` |
| Character & Acting | `CD96A794D37371B855552C23A2670EBD78A9F2E2D3218152CE568C3B4356B09F` |
| Art Director | `8C8DB2370D69863BBA71138A5BBC123B5BC9BBA73E5CCF2F02D8764FFE933C75` |
| Continuity | `C64475BD0578BE6C159DF5A0FA0D90A96636160215B00E17AA3C5CC8E7F0B64C` |
| Shared QA | `2F2E0F241766AB0354E471FC4BA0BF4854363622FB87AE013AB56DDDD270476D` |

The hash values, manifests, raw records, and envelopes remain at their original evidence root. This document is an index and does not relocate, normalize, or overwrite them.

## Baseline use rule

Compare future runtime changes against this baseline at the appropriate regression tier. A matching `PASS` does not make the system Production Ready; it demonstrates only the bounded runtime-validation contract captured here.
