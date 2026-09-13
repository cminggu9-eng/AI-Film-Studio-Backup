# Scene Writer Full Semantic Validation Failure Ownership Matrix V0.1

| Fixture | Failure | Primary ownership | Contributing ownership | Why |
|---|---|---|---|---|
| F03 | Unsupported shared prior-work fact | PROVIDER BEHAVIOR | SEMANTIC VERIFIER | Frozen Skill and Assignment prohibit invented history; generated dialogue introduced it and verifier missed it. |
| F06 | Empty/invalid normal control field rejected | EXECUTOR PROMPT CONSTRUCTION | RUNTIME | The strict Runtime rejection is correct; generation prompt/schema did not reliably produce a language-valid optional control value. |
| F09 | Request to inspect notice occurs after inspection | PROVIDER BEHAVIOR | — | Scene-level temporal / information sequencing is internally incoherent. |
| F10 | Local revision adds outside administrative plan and time obligation | PROVIDER BEHAVIOR | SEMANTIC VERIFIER | Core local repair works, but generated micro-facts exceed Assignment and verifier missed them. |
| F11 | `NO_MATERIAL_CHANGE` packet malformed | EXECUTOR PROMPT CONSTRUCTION | RUNTIME | Runtime correctly required no creative replacement plus `material_rewrite_claimed=false`; executor output did not meet it. |
| F12 | DIAGNOSE packet creative kind invalid | EXECUTOR PROMPT CONSTRUCTION | RUNTIME | Executor's generated shape did not meet the Runtime's diagnostic-only contract. |
| F13-A | `NEEDS_CONTEXT` packet malformed | EXECUTOR PROMPT CONSTRUCTION | RUNTIME | Required context packet was not emitted in a Runtime-valid form. |
| F13-B | Upstream decision packet omitted required field | EXECUTOR PROMPT CONSTRUCTION | RUNTIME | High-level boundary appears recognised, but structured control data was incomplete. |
| F14 | Wet ground becomes unsupported in-world risk | PROVIDER BEHAVIOR | SEMANTIC VERIFIER | Role handoffs are lawful; control data introduced a causal story fact and verifier missed it. |

No evidence in this pack establishes a Capability Model semantic absence or requires a canonical Skill change. No Fixture defect is assigned as primary ownership: each failing Fixture passed preflight shape review and was intentionally narrow.
