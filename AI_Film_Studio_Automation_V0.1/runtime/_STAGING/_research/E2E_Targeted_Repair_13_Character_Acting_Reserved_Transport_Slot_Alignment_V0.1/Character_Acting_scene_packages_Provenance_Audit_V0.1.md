# Character & Acting scene_packages Provenance Audit V0.1

Date: 2026-08-31  
Result: PASS  
Decision: `C. INTEGRATION-OWNED RESERVED TRANSPORT SLOT`

## Sources audited

- Canonical Character & Acting `SKILL.md`, Output Model, Handoff Model, and Authority Model.
- `AI_Film_Studio_Interface_Contract_Map_V0.1.md`.
- `AI_Film_Studio_State_Evidence_Envelope_V0.1.md`.
- `Scene_Writer_Integration_Output_Contract_V0.1.md`.
- Showrunner Repair04 transport-ownership contract and implementation.
- Current non-strict prompt, raw parser, generic ten-field role-result validator, envelope assembly, and failure path.
- Relevant Scene Writer, Director, and Art Director integration implementations.
- Immutable E2E-RUN-16 Character raw response, decoded JSON, failure record, Director-to-Character envelope, Character input, and Scene Writer output.

## Ownership decision

| Question | Decision |
|---|---|
| Who owns `scene_packages` semantics? | Scene Writer only. |
| Does Character & Acting own or produce them? | No. It owns playable performance interpretation only. |
| Does Character raw role output require the slot? | No. Raw role output has nine Character-owned fields. |
| Why does the generic final role transport have the slot? | It is a closed integration schema shared across roles. |
| Character-stage representation | Exact existing integration sentinel `ABSENT`. |
| Upstream Scene Writer package representation | Independent validated source artifact plus exact identity metadata; never model echo. |

This is not deterministic carry-forward inside the Character field. The upstream package remains independently available to downstream assembly, while Character's own reserved slot expresses lawful non-ownership. A missing upstream Scene Writer source fails closed and cannot be hidden by `ABSENT`.

