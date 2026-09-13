# Art Director Output Contract / Validator Provenance Audit V0.1

Date: 2026-08-31  
Classification: AUTHORITATIVE PROVENANCE AUDIT  
Result: PASS

## Sources audited

- Canonical Art Director `SKILL.md`
- Frozen `Art_Director_Capability_Model_V0.1.md`
- `AI_Film_Studio_Interface_Contract_Map_V0.1.md`
- Repair 06 Art Director integration-contract implementation, tests, and evidence
- Current provider-facing output schema and system-prompt construction
- Current local validation and failure-classification path
- Immutable E2E-RUN-15 Art Director raw response, parsed payload, failure attribution, provider manifest, execution manifest, and acceptance report
- E2E-INT-11 acceptance contract and relevant Phase 2 regression suites

## Provenance decisions

| Item | Classification | Authoritative decision |
|---|---|---|
| Canonical Art Director outcomes | CANONICAL ROLE REQUIREMENT | Exact, case-sensitive frozen tokens; no aliases or translations. |
| Minimum-sufficient response | CANONICAL ROLE REQUIREMENT | Output is minimum sufficient and untamplated. Fixed display sections are not canonical. |
| Ten top-level transport fields | INTEGRATION MACHINE REQUIREMENT | All ten fields are required and no additional top-level field is accepted. |
| `state_evidence` six dimensions | INTEGRATION MACHINE REQUIREMENT | Exact six-field object; each child is independently validated. |
| `state_evidence.visual_state` | INTEGRATION MACHINE REQUIREMENT | JSON object or exact `ABSENT`. |
| `unresolved_decisions` | INTEGRATION MACHINE REQUIREMENT | Required machine slot; array of strings or exact `ABSENT`; empty array is lawful. |
| Production-feasibility discussion | OPTIONAL / CONDITIONAL CONTENT | Required only when evidence establishes an actual burden or a Production decision. |
| Unresolved-issue prose | OPTIONAL / CONDITIONAL CONTENT | Required only when a real unresolved owner decision exists. |
| Natural-language headings and section names | DISPLAY CONTENT | No fixed heading identity and no mandatory English labels. |
| Object-only `visual_state` assertion | VALIDATOR-INVENTED ASSERTION | Unauthorized drift; removed. |
| Non-empty unresolved issue or production-keyword assertion | VALIDATOR-INVENTED ASSERTION | Unauthorized drift; removed. |

## Governing conclusion

`PROMPT = PROVIDER CONTRACT = VALIDATOR`, while canonical Art Director creative authority remains read-only. Absence of irrelevant content is not a failure.

