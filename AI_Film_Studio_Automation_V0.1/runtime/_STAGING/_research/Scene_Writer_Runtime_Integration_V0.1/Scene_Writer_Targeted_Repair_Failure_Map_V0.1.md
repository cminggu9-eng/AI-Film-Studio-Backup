# Scene Writer Targeted Repair Failure Map V0.1

## Scope and evidence boundary

- Classification: `TARGETED REPAIR / STAGING / SYNTHETIC / NON-CANON`.
- Canonical Skill is read-only. Re-verified SHA-256: `93e1be12988f8caa6cdd76acb5e6c1bf6ad3ca0dff5806a2ea93511e66052dfb`.
- Evidence reread before implementation: `F03`, `F06`, `F09`, `F10`, `F11`, `F12`, `F13-A`, `F13-B`, and `F14` raw results; the Full Semantic Validation human reviews and failure-ownership matrix.
- The frozen raw-result format retains accepted Runtime outputs but intentionally does not retain malformed executor packets. For F06/F11/F12/F13-A/F13-B, the exact failed provider JSON cannot be reconstructed from evidence; only the Runtime's precise schema rejection is asserted below.
- No canonical semantic absence is evidenced. This map authorizes only execution-layer, constraint-presentation, and verifier-recall repairs.

## Failure map

### F03 — Unsupported shared prior-work fact

1. **Exact failure:** `内容我们反复对过` asserted unprovided shared prior work on the proposal.
2. **Expected behavior:** Preserve the unsigned/unsubmitted proposal and let the submission request, co-sign condition, and immediate action carry the scene without adding history.
3. **Observed model behavior:** Produced an otherwise playable dialogue scene, but added a pre-existing collaborative-review history.
4. **Runtime disposition:** Accepted. Its deterministic fact guard did not classify this semantic history assertion as a violation.
5. **Verifier disposition:** Returned `PASS`. Its former instruction mentioned unsupported facts but did not require exhaustive claim-to-ledger comparison of dialogue history claims.
6. **Primary ownership:** `PROVIDER BEHAVIOR`.
7. **Contributing ownership:** `SEMANTIC VERIFIER`; generation-side ledger presentation was insufficiently explicit as a binding fact ceiling.
8. **Minimal repair:** Inject the structured ledger as binding generation authority; state that open creativity cannot create pre-existing history. Require verifier claim-to-ledger classification for history/relationship claims. Do not alter dialogue, objective, resistance, turn, or canonical Skill semantics.

### F06 — Subtext packet rejected for an empty optional control field

1. **Exact failure:** `MALFORMED_EXECUTOR_OUTPUT`: `control_data.diagnosis_summary` failed the output-language validator because it was empty/non-text.
2. **Expected behavior:** Return a normal `SCENE_CREATED` scene with only applicable, language-valid control text; optional fields must be omitted or `null`, never empty placeholders.
3. **Observed model behavior:** Provider call succeeded, but emitted a packet whose optional normal-control field was unusable. The retained evidence cannot recover the rejected JSON.
4. **Runtime disposition:** Correctly rejected it: if an optional language-checked field is present and non-null, it must be non-empty, readable text.
5. **Verifier disposition:** Not invoked because Runtime rejected the packet before semantic verification.
6. **Primary ownership:** `EXECUTOR PROMPT CONSTRUCTION`.
7. **Contributing ownership:** `RUNTIME` only insofar as its universal optional-field transport exposed the prompt/schema mismatch; its rejection is correct.
8. **Minimal repair:** Replace the universal output instruction with a state-aware projection that marks `diagnosis_summary` optional for normal creation and explicitly prohibits empty-string placeholders. No Subtext-capability change.

### F09 — Information timing sequence is internally incoherent

1. **Exact failure:** 岳临 opens and reads the notice, then says `先让我看看`; the request occurs after the requested action.
2. **Expected behavior:** He must request or receive the notice before opening it; the rejection becomes known only at the lawful in-scene disclosure moment, while its reason remains unknown.
3. **Observed model behavior:** Preserved the world-fact/knowledge boundary and unknown reason, but inverted the event order in the final beat.
4. **Runtime disposition:** Accepted. Output shape and deterministic fact locks were valid; they do not model a scene's information-state transition ordering.
5. **Verifier disposition:** Returned `PASS`. It checked fact authority but did not require a knowledge-timing claim comparison or detect that generated action contradicted its own timing/state claim.
6. **Primary ownership:** `PROVIDER BEHAVIOR`.
7. **Contributing ownership:** Generation constraint presentation lacked an explicit entry-knowledge/discovered-during-scene projection; verifier lacked a knowledge-timing-drift category and claim check.
8. **Minimal repair:** Present world facts, per-character entry knowledge, explicit not-yet-known information, and permitted discovery timing in the generation ledger. Add verifier claim-to-ledger review for knowledge timing without judging prose quality.

### F10 — Revision expands facts beyond the repair ceiling

1. **Exact failure:** `午休前我得去趟行政那边` plus possible lateness and a twenty-minute cover created an external plan, temporal obligation, and work arrangement absent from the Assignment.
2. **Expected behavior:** Return a local `SCENE_REVISED` deliverable that adds resistance/conditional consent without adding reason, schedule, authority, resource commitment, history, or relationship context.
3. **Observed model behavior:** Achieved local resistance and turn, then supplied unsupported administrative and time/coverage micro-facts as the condition.
4. **Runtime disposition:** Accepted. The deterministic guard did not interpret those connected micro-facts as unsupported story/obligation claims.
5. **Verifier disposition:** Returned `PASS`. Its former prompt allowed conditional dialogue but did not force distinction between a scene-local proposed condition and an asserted pre-existing external duty.
6. **Primary ownership:** `PROVIDER BEHAVIOR`.
7. **Contributing ownership:** `SEMANTIC VERIFIER`; generation prompt did not make the REVISE fact-expansion ceiling explicit enough.
8. **Minimal repair:** Make the repair target and ledger a binding revision ceiling, explicitly prohibiting added schedules, work arrangements, obligations, and authority facts. Teach generation and verifier the lawful proposal-versus-pre-existing-fact distinction.

### F11 — `NO_MATERIAL_CHANGE` malformed

1. **Exact failure:** `MALFORMED_EXECUTOR_OUTPUT`: `NO_MATERIAL_CHANGE` carried creative material and/or did not provide `material_rewrite_claimed: false`.
2. **Expected behavior:** For no material benefit, return `primary_state: NO_MATERIAL_CHANGE`, `creative_deliverable: null`, and `material_rewrite_claimed: false`; do not manufacture a revision.
3. **Observed model behavior:** Selected or attempted the no-change decision but did not produce its valid state packet. Frozen evidence retains only the Runtime error.
4. **Runtime disposition:** Correctly rejected a state that claimed no material change while sending a creative rewrite or omitting the mandatory false boolean.
5. **Verifier disposition:** Not invoked after Runtime rejection.
6. **Primary ownership:** `EXECUTOR PROMPT CONSTRUCTION`.
7. **Contributing ownership:** `RUNTIME` is a correct enforcement layer, not a semantic defect.
8. **Minimal repair:** Add a REVISE/`NO_MATERIAL_CHANGE` projection and field matrix that make the null creative field and exact false boolean required and prohibit revision content.

### F12 — DIAGNOSE emitted an invalid creative kind

1. **Exact failure:** `MALFORMED_EXECUTOR_OUTPUT`: `creative_deliverable.kind` was not `scene` or `revision`.
2. **Expected behavior:** Perform a bounded diagnosis of Scene Function, Resistance, and Turn without a replacement scene or revision. A diagnosis is control text, not a new creative kind.
3. **Observed model behavior:** Provider call succeeded but attempted to encode diagnostic content in an invalid creative deliverable. Frozen evidence does not retain that rejected packet.
4. **Runtime disposition:** Correctly rejected a creative object outside the strict `scene|revision` vocabulary.
5. **Verifier disposition:** Not invoked after Runtime rejection.
6. **Primary ownership:** `EXECUTOR PROMPT CONSTRUCTION`.
7. **Contributing ownership:** `RUNTIME` correctly prevents an undeclared creative type.
8. **Minimal repair:** Add a DIAGNOSE projection: non-creative output, lawful `NO_MATERIAL_CHANGE` state packet, and `diagnosis_summary`; prohibit any replacement scene/revision. Do not add a second writer or change the Skill's diagnostic semantics.

### F13-A — missing-material context packet malformed

1. **Exact failure:** `MALFORMED_EXECUTOR_OUTPUT`: `creative_deliverable.content` was empty though a creative object was supplied.
2. **Expected behavior:** Return `NEEDS_CONTEXT` with `creative_deliverable: null` and a complete `material_missing_context` packet explaining what is missing, why it is material, and the target owner; do not invent people, relationship, location, event, or result.
3. **Observed model behavior:** Appears to have recognized a non-creative boundary but encoded it as an empty creative packet. Exact rejected JSON is not retained.
4. **Runtime disposition:** Correctly rejected an empty creative content field.
5. **Verifier disposition:** Not invoked after Runtime rejection.
6. **Primary ownership:** `EXECUTOR PROMPT CONSTRUCTION`.
7. **Contributing ownership:** `RUNTIME` correctly enforces the creative-object schema.
8. **Minimal repair:** Add a CREATE/`NEEDS_CONTEXT` projection and field matrix: creative is forbidden; material context summary is required and language-valid. No fact guessing.

### F13-B — upstream-decision packet omitted its required decision

1. **Exact failure:** `MALFORMED_EXECUTOR_OUTPUT`: `UPSTREAM_DECISION_REQUIRED` omitted non-empty `upstream_decision_needed`.
2. **Expected behavior:** Return no creative deliverable, exact `UPSTREAM_DECISION_REQUIRED`, `UPSTREAM_HANDOFF_REQUIRED`, a specific upstream decision, and a lawful handoff packet; never decide whether the protected name may be disclosed.
3. **Observed model behavior:** The Runtime error indicates the high-level upstream state was selected but the decision-description packet was incomplete.
4. **Runtime disposition:** Correctly rejected it because the necessary upstream decision was missing.
5. **Verifier disposition:** Not invoked after Runtime rejection.
6. **Primary ownership:** `EXECUTOR PROMPT CONSTRUCTION`.
7. **Contributing ownership:** `RUNTIME` correctly enforces the canonical boundary packet.
8. **Minimal repair:** Add a CREATE/`UPSTREAM_DECISION_REQUIRED` projection and field matrix: creative is forbidden; decision description, canonical flag, and handoff are required. Do not modify Canon, Showrunner, or the frozen Skill.

### F14 — wet ground became a causal danger claim

1. **Exact failure:** Control data said wet ground `可能增加进入风险`, turning a supplied production condition into an unsupported in-world causal/safety fact.
2. **Expected behavior:** Preserve the wet ground as an observed condition and production-burden handoff context, but do not infer a cause, danger, crime, accident, or entering-risk fact.
3. **Observed model behavior:** Otherwise respected role boundaries and issued lawful Director, Character & Acting, and Production handoffs, but added the unsupported causal claim in `control_data.resistance`.
4. **Runtime disposition:** Accepted. The deterministic fact guard cannot reliably distinguish an inferred causal story fact from an allowed physical observation.
5. **Verifier disposition:** Returned `PASS`. Its former broad causal rule was not operationalized as mandatory claim-to-ledger comparison across control text.
6. **Primary ownership:** `PROVIDER BEHAVIOR`.
7. **Contributing ownership:** `SEMANTIC VERIFIER`; generation-side fact ceiling lacked explicit treatment of observational conditions versus causal interpretation.
8. **Minimal repair:** State in generation constraints that observable supplied conditions are not authority to infer causality/risk. Require verifier to inspect creative and all relevant control claims against the ledger and classify unauthorized causal claims.

## Repair ownership summary

| Track | Fixtures | Minimum approved intervention |
|---|---|---|
| A. Executor Prompt Construction | F06, F11, F12, F13-A, F13-B | Mode/state-aware execution projection with six-state required/optional/forbidden field matrix. |
| B. Generation-side Assignment / Fact / Knowledge Fidelity | F03, F09, F10, F14 | Binding structured-ledger injection, fact-expansion ceiling, proposal distinction, and knowledge-timing presentation. |
| C. Semantic Verifier Recall | F03, F09, F10, F14 and frozen bad replay set | Claim-to-ledger detection/classification only; no rewrite, no lexical synonym catalogue, no artistic assessment. |

## Phase-0 decision

`PHASE 0 COMPLETE — NO CANONICAL SKILL SEMANTIC CHANGE REQUIRED.`

The permitted repair surface is sufficient: Executor prompt construction, Runtime execution projection/validation where needed, generation constraint presentation, and semantic-verifier prompt/schema. No code was modified before this map was completed.
