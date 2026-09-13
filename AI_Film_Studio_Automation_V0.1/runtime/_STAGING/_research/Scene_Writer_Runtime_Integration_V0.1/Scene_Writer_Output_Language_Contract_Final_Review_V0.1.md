---
type: output-language-contract-final-review
status: complete-awaiting-user-review
---

# Scene Writer Output Language Contract Repair + Smoke Rerun Final Review V0.1

## Contract result

`output_language` is now an explicit Runtime execution constraint. It is carried from Assignment to Runtime, canonical executor prompt/metadata, shared `ModelExecutor`, provider request, output validator, and Runtime Result Envelope. The deterministic fallback is `INHERIT_ASSIGNMENT_LANGUAGE`; absent both explicit fields is a contract error, never a language guess.

## Test result

`OL-SW-01–08 = 8 / 8 PASS`; existing Runtime `30 / 30`, Executor Binding `10 / 10`, and Synthetic E2E remain passing. Canonical tokens remain exact English.

## Smoke rerun result

Exactly one real rerun of the original Assignment was performed, adding only `output_language = zh-CN`. Technical status is `Runtime SUCCESS`; creative and normal control text returned in Chinese; `SCENE_CREATED` is exact; model/provider are real `deepseek` / `deepseek-v4-pro`.

## Human-review observation

The language repair is technically successful. However, the rerun adds `他那边临时有状况` despite the lock that the reason is unknown, and changes the broad tonight condition into `十二点前` / `一小时内`. This is recorded as `OLR-SMOKE-01`, not auto-repaired and not attributed to the Runtime language layer.

## Integrity and lifecycle

- canonical Skill SHA-256 unchanged: `93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb`.
- Frozen asset mutations / dramatic semantic mutation: `0`.
- Runtime remains `INTEGRATED / CONTRACT VALIDATED / STAGING`; Executor remains `BOUND / REAL`.
- Full Semantic Validation and Human Acceptance: `NOT STARTED`.
- Scene Writer Production Ready: `NO`.

## Recommendation

`OUTPUT LANGUAGE CONTRACT TECHNICAL PASS — HUMAN REVIEW REQUIRED FOR OLR-SMOKE-01`.

No full validation, Runtime publish, semantic repair, resampling, or downstream role activation is authorized by this review.
