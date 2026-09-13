---
type: assignment-fact-knowledge-lock-architecture-audit
status: semantic-validation-failure-awaiting-user-decision
scope: staging runtime enforcement only
---

# Scene Writer Assignment Fact & Character Knowledge Lock Architecture Audit V0.1

## Ownership conclusion

Canonical `scene-writer` already instructs the executor not to invent Canon/story facts and to protect relevant character constraints. No Skill semantic change is justified or authorized. The repair therefore belongs to execution enforcement: explicit prompt presentation plus Runtime post-checking of Assignment fact/knowledge constraints.

## Implemented enforcement

- Runtime contract now distinguishes locked fact preservation, explicit-unknown preservation, unspecified-fact prohibition, creative expression space, coarse temporal specificity, and world-fact-to-character-knowledge protection.
- The executor prompt explicitly prohibits reasoning/category labels for an unknown reason, deadline expansion of coarse time, invented knowledge sources, capability rankings, relationship history, authority, commitment, and unsupported world facts.
- The Runtime derives a narrow guard profile from existing Assignment fields. It does not build a Canon database, knowledge graph, continuity system, or character memory engine.
- The Runtime validates output after structure/language validation and returns `ASSIGNMENT_FACT_LOCK_VIOLATION` for detected violations.

## Smoke limitation discovered

The guard detected the required synthetic cases, but the final real Smoke used an equivalent phrase outside the initial lexical coverage: `最熟悉整体内容的人之一`. It therefore returned Runtime `SUCCESS` while still adding an unauthorized capability comparison. This is a Runtime semantic-validator coverage gap, with provider adherence as a contributing execution behavior; it is not evidence that frozen Skill semantics must change.

## Frozen boundaries

No canonical Skill, Capability Model, Showrunner, Shared QA, Canon, published archive, or Runtime publish path changed.
