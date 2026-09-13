---
type: integration-phase-1-asset-inventory
status: frozen-for-phase-1-review
version: 0.1
date: 2026-08-26
scope: static-contract-inventory-only
---

# AI Film Studio｜Canonical Asset Inventory V0.1

## Scope and reading rule

This is a read-only inventory for Integration Validation Phase 1. It reports Vault artifacts as found on 2026-08-26. It does not select a replacement source of truth where lifecycle records conflict, and it does not change a canonical Skill, Production Lock, Runtime asset, executor, provider, or acceptance record.

“Production Ready” means an explicit ready declaration in the cited role record. It is not inferred from publication, freezing, or a successful static check.

## Role inventory

| Role | Canonical identity and Vault path | Lifecycle / Production Skill | Runtime / Executor | Semantic validation | Human acceptance | Production Ready | Known limitation relevant to integration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Showrunner | ai-film-studio-showrunner. 01_SKILLS/01_Showrunner/SKILL.md | COMPLETE / LOCKED. Production Lock V0.1 records production-ready publication and the explicit router binding. | Runtime V0.2 RC2; explicit role router and Runtime Compliance Gate recorded. Internal, gate, router, recovery, and regression evidence are recorded as passed. | Runtime regression evidence: 10/10 pass; this is the role’s recorded compliance/semantic evidence. | No separate Human Acceptance field found in the reviewed Production Lock. User retains final authority. | YES, explicitly recorded in Production Lock. | No formal cross-role canonical envelope; Showrunner handoffs are rich but downstream packaging/version rules are not centralized. |
| Scene Writer | scene-writer. 01_SKILLS/02_Scene_Writer/scene-writer/SKILL.md | Capability model complete/frozen; Production Skill PUBLISHED / FROZEN. Development Checkpoint records a staged runtime posture. | INTEGRATED / CONTRACT VALIDATED / STAGING; executor BOUND / REAL; provider-neutral contract with real DeepSeek evidence recorded. Production Lock predates this and says executor binding not started. | Full Semantic Validation COMPLETE; Targeted Repair 18/20, with formal rerun 0/13. | Deferred. | NO. | Unsupported micro-fact additions, knowledge-timing drift, unreliable non-CREATE states, unreliable verifier, and a smoke-runner import that can reach a provider. |
| Director | director. 01_SKILLS/03_Director/director/SKILL.md | PUBLISHED / FROZEN, V0.1. | Deferred. | Deferred. | Deferred. | NO. | Entry/exit evidence gap; external production constraints deferred; all Runtime, Executor, semantic, and cross-role validation remain deferred. |
| Character & Acting | character-acting. 01_SKILLS/04_Character_Acting/character-acting/SKILL.md | PUBLISHED / FROZEN, V0.1. | Deferred. | Deferred. | Deferred. | NO. | No safe formal microexpression treatment; current-scene handoff is structurally limited; future interface remains deferred. |
| Art Director | art-director. 01_SKILLS/05_Art_Director/art-director/SKILL.md | PUBLISHED / FROZEN, V0.1. | Deferred. | Deferred. | Deferred. | NO. | Several material/design and production-feasibility limits are partial or deferred; Runtime and cross-role validation are not started. |
| Continuity | continuity. 01_SKILLS/06_Continuity/continuity/SKILL.md | PUBLISHED / FROZEN, V0.1. | Deferred. | Deferred. | Deferred. | NO. | Continuity can observe, compare, classify, flag, and route, but persistent state storage/retrieval, database memory, Runtime, and cross-role validation are deferred. |
| Shared QA | language-voice-qa. 01_SKILLS/Shared_QA/SKILL.md | Production Skill FROZEN; Contemporary Layer and Validation Pack FROZEN; Rewrite Gate ACTIVE. | Runtime Integration FROZEN; Model Executor Binding ACTIVE; DeepSeek listed as active development provider. No execution was performed in this phase. | Validation Pack FROZEN; Rewrite consistency gate active. | ACCEPT WITH KNOWN LIMITATIONS — HUMAN ACCEPTED. | Not separately declared in the Shared QA Hub. | KL-01 and KL-02 are retained known-limitations references; default QA is non-rewriting and an explicit rewrite path requires semantic protection. |

## Canonical-state and metadata observations

1. The Showrunner Production Lock is the only reviewed record that explicitly declares Production Ready.
2. Scene Writer has the most advanced recorded execution evidence, but its older Production Lock conflicts with its newer Development Checkpoint on executor status. This is an unresolved lifecycle-record discrepancy, not a finding that either record is false.
3. The Director, Character & Acting, Art Director, and Continuity canonical SKILL frontmatter remains in a staging-oriented status while their role checkpoints/locks record PUBLISHED / FROZEN. This is a discovery/automation metadata debt and has not been repaired here.
4. Shared QA is accepted and frozen for its declared QA scope. That does not authorize it to rewrite story, canon, or other role decisions.

## Canonical paths and integrity snapshot

| Asset | SHA-256 observed before Phase 1 documentation |
| --- | --- |
| 01_Showrunner/SKILL.md | 0847EE3521A915936E97FA1F72D081F0788876F003E071918F517B0A46AE999C |
| 02_Scene_Writer/scene-writer/SKILL.md | 93E1BE12988F8CAA6CDD76ACB5E6C1BF6AD3CA0DFF5806A2EA93511E66052DFB |
| 03_Director/director/SKILL.md | 807D5B398A247A69C3F54FB58F256E8E87AE3B245540071A8B3F6832B49A7781 |
| 04_Character_Acting/character-acting/SKILL.md | CD96A794D37371B855552C23A2670EBD78A9F2E2D3218152CE568C3B4356B09F |
| 05_Art_Director/art-director/SKILL.md | 8C8DB2370D69863BBA71138A5BBC123B5BC9BBA73E5CCF2F02D8764FFE933C75 |
| 06_Continuity/continuity/SKILL.md | C64475BD0578BE6C159DF5A0D90A96636160215B00E17AA3C5CC8E7F0B64C |
| Shared_QA/SKILL.md | 2F2E0F241766AB0354E471FC4BA0BF4854363622FB87AE013AB56DDDD270476D |

## Evidence consulted

- Each role’s canonical SKILL.md, Production Lock or controlled-publish/checkpoint record, and its Deferred Hardening Register where present.
- Shared QA Hub and its frozen/runtime/executor status records.
- AI Film Studio Distillation Process Hardening Register V0.1 and Nuwa Distillation Provenance Audit V0.1.

No inventory row is permission to invoke a role, provider, executor, or QA rewrite.
