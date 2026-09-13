# Scene Writer Semantic Assignment Integrity Test Report V0.1

Status: `VERIFIER CONTRACT PASS / FINAL SMOKE HUMAN REVIEW FAIL`

## Non-network gates

- `SI-STRUCT-01–10 = 10 / 10 PASS`: assignment-only ledger, real-verifier binding requirement, fail-safe enforcement, no rewrite/resample, malformed verifier rejection, strict schema, provider neutrality, no lexical capability catalogue, and frozen Skill hash.
- Existing regressions remained green: Runtime `30 / 30`, Output Language `8 / 8`, Assignment Fact / Knowledge `10 / 10`, and Executor Binding `10 / 10`.

## Real provider verifier-only matrix

Provider: `deepseek`; model: `deepseek-v4-pro`; classification: `REAL PROVIDER VERIFIER-ONLY TEST; NO SCENE GENERATION`.

- Initial evidence run: `11 / 17 PASS`; it revealed an insufficient semantic definition for explicit-unknown preservation and implicit-speaker comparative capability claims. No Scene was generated.
- One minimal verifier-contract clarification was made. No deterministic pattern or synonym list was added.
- Final evidence run: `SI-SW-01–10 = 10 / 10 PASS`; capability paraphrases `SI-PARA-01–05 = 5 / 5 PASS`; false-positive protection `SI-FP-01–02 = 2 / 2 PASS`; total `17 / 17 PASS`.
- Final matrix tokens: input `24,428`; output `1,665`; total latency `57,481 ms`; estimated cost `CNY 0.026154`.

Raw evidence:

- `Scene_Writer_Semantic_Assignment_Integrity_Provider_Test_Raw_Result_V0.1.json` — initial failing definition evidence.
- `Scene_Writer_Semantic_Assignment_Integrity_Provider_Test_Round2_Raw_Result_V0.1.json` — final `17 / 17` passing matrix.

These verifier-only results qualify the Runtime gate but do not override the required independent human review of the one real generated Smoke.
