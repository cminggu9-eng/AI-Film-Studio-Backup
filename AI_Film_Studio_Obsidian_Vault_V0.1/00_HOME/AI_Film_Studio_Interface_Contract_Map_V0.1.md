---
type: integration-phase-1-interface-contract-map
status: frozen-for-phase-1-review
version: 0.1
date: 2026-08-26
scope: static-interface-mapping-only
---

# AI Film Studio｜Interface Contract Map V0.1

## Mapping rule

This document maps existing role contracts. It does not rename a canonical Mode, Primary State, Flag, Handoff, or authority boundary. “Adapter” below means a small, explicit transport envelope that preserves the source artifact verbatim and labels its recipient; it is not a role, a rewrite, or an implementation.

## Minimal transport envelope required for a future E2E validator

Every handoff should carry, without inventing fields in the source output:

| Envelope field | Purpose |
| --- | --- |
| Source role, source record ID, version, and timestamp | Identifies the version being consumed. |
| Intended recipient and handoff reason | Prevents a general output from becoming an implied instruction. |
| Canon / assignment locks and prohibited changes | Makes protected facts explicit. |
| Source Mode, Primary State, Flags, and Handoffs exactly as emitted | Preserves canonical tokens without translation. |
| Required outcome and unresolved decision | Separates accepted decision from open authority. |
| Current state, proposed state, knowledge timing, relationship state, visual state, and evidence locator when present | Allows Continuity to compare instead of infer. |
| QA context, target language, and explicit rewrite instruction when Shared QA is used | Prevents default QA from becoming a creative rewrite. |

An absent item is reported as absent. The envelope must not manufacture it.

## Core-chain interfaces

| Link | Formal source output / handoff | Recipient minimum input | Mode / state handling | Compatibility note |
| --- | --- | --- | --- | --- |
| USER CONCEPT -> SHOWRUNNER | One original user concept plus any separately authorized canon. | Concept, user constraints, existing canon if supplied. | Showrunner has no canonical Mode protocol in the reviewed record. Its STATUS tokens remain INFO, WARNING, BLOCKED, PASS. | The fixture supplies only its one-line original concept. |
| SHOWRUNNER -> SCENE WRITER | Scene Purpose; Character Objective; Conflict; Required Information; Starting State; Required Ending State; Canon Constraints; Relationship State; What Must NOT Be Changed; Acceptance Check. | Scene assignment with explicit locks, required outcome, characters, state, and constraint source. | Scene Writer receives the assignment and selects only its own canonical Mode: CREATE, REVISE, or DIAGNOSE. Its Primary State remains exact. | A normalized assignment package is required; no story prose is pre-written by the adapter. |
| SCENE WRITER -> DIRECTOR | Scene content plus scene function, entry/exit, outcome, locks, state, and eligible handoff flags. | Canon, scene function/events/outcome, character constraints, useful continuity/production context. | Preserve Scene Writer Primary State and flags exactly. Director selects PLAN, REVISE, or DIAGNOSE and emits only its own Primary State. | Director receives dramatic constraints, not a mandate to preserve scene wording beyond stated locks. |
| DIRECTOR -> CHARACTER & ACTING | Directorial Intent; Staging/Blocking; Audience Information; Spatial Geography; Camera/Coverage Intent; Rhythm/Transition; Production Burden; Handoffs. | Character facts/knowledge, locked scene content, objective/resistance/turn/outcome, partner and relationship state, director constraints. | Preserve Director Mode and state exactly. Character & Acting selects INTERPRET, REVISE, or DIAGNOSE. | The packet must distinguish a director constraint from a performance instruction. |
| DIRECTOR + CHARACTER & ACTING -> ART DIRECTOR | Director visual/spatial/audience intent plus Character & Acting physical/behavioral requirements that affect environment, objects, costume, or usable space. | Canon/story/world, scene need, character facts, required objects, director intent, physical-performance implications. | Preserve both source states/tokens. Art Director selects Design, revise, or diagnose only under its own contract. | Merge only source-referenced needs. A combined packet must retain each source identity. |
| SCENE WRITER + DIRECTOR + CHARACTER & ACTING + ART DIRECTOR -> CONTINUITY | Versioned scene and role outputs plus explicit prior/current/proposed state, authority source, knowledge timing, relationship state, and visual state where supplied. | Material to compare, relevant prior fact/state, and authority evidence. | Continuity has NO CANONICAL MODE. Its six capability outcomes remain exact. | Existing handoffs are partial. There is no shared state-packet standard or persistent state store. |

## Shared QA horizontal interfaces

| Source text | Required QA packet | Existing QA outcome / handling | Boundary |
| --- | --- | --- | --- |
| Showrunner, Scene Writer, Director, Character & Acting, Art Director, or Continuity textual artifact | Original text; source role/record; relevant locks/context; target language where applicable; explicit rewrite instruction only if rewrite is requested. | QA MODE is default. REWRITE MODE requires explicit instruction and applicable locks/protection. QA decision states remain exact: PASS / NO CHANGE; PASS WITH NOTES; RETURN FOR LANGUAGE REVISION; NEEDS CONTEXT; ROLE HANDOFF / WARNING; REWRITE DELIVERED; BLOCKED. | QA does not change canon, role authority, or creative decision. |

## Outcome and stop rules

| Situation | Required outcome |
| --- | --- |
| A recipient lacks locked facts, authoritative state, or context | Preserve the source state and emit the recipient’s canonical context/upstream outcome. Do not infer. |
| A source asks the wrong role to decide | Emit a bounded handoff to the lawful owner; retain the original source record. |
| Continuity finds a possible or confirmed contradiction | Flag and route; do not correct. A recheck requires a new version and authority evidence. |
| Shared QA lacks semantics/context or sees a protected semantic risk | Use NEEDS CONTEXT, ROLE HANDOFF / WARNING, or BLOCKED; do not silently rewrite. |
| An external department is needed | Record the external owner and stop the seven-role path at that boundary. |

## Canonical Mode and Primary State index

| Role | Canonical Mode(s) / protocol | Primary State / outcome tokens |
| --- | --- | --- |
| Showrunner | NO CANONICAL MODE | STATUS: INFO, WARNING, BLOCKED, PASS. |
| Scene Writer | CREATE, REVISE, DIAGNOSE | SCENE_CREATED; SCENE_REVISED; NO_MATERIAL_CHANGE; NEEDS_CONTEXT; UPSTREAM_DECISION_REQUIRED; REQUEST_OUT_OF_SCOPE. |
| Director | PLAN, REVISE, DIAGNOSE | DIRECTION_PLAN_PRODUCED; DIRECTION_PLAN_REVISED; NO_MATERIAL_DIRECTION_CHANGE; NEEDS_CONTEXT; UPSTREAM_DECISION_REQUIRED; OUT_OF_SCOPE_HANDOFF. |
| Character & Acting | INTERPRET, REVISE, DIAGNOSE | PERFORMANCE_INTERPRETATION_READY; PERFORMANCE_INTERPRETATION_REVISED; NO_PERFORMANCE_CHANGE; CONTEXT_REQUIRED; UPSTREAM_DECISION_REQUIRED; OUT_OF_SCOPE. |
| Art Director | Design, revise, diagnose | CONTEXT_RESOLUTION_REQUIRED; CROSS_ROLE_DECISION_REQUIRED; RESEARCH_DECISION_REQUIRED; PRODUCTION_FEASIBILITY_DECISION_REQUIRED; PARTIAL_OR_DEFERRED_CAPABILITY_LIMIT; DESIGN_RESPONSE_READY. |
| Continuity | NO CANONICAL MODE | CONTINUITY PRESERVED; AUTHORIZED OR SUPPORTED CHANGE; INTENTIONAL DISCONTINUITY; CONTEXT INSUFFICIENT; POTENTIAL CONTRADICTION; CONFIRMED CONTRADICTION. |
| Shared QA | QA MODE; REWRITE MODE only by explicit instruction | PASS / NO CHANGE; PASS WITH NOTES; RETURN FOR LANGUAGE REVISION; NEEDS CONTEXT; ROLE HANDOFF / WARNING; REWRITE DELIVERED; BLOCKED. |

This map defines no runtime schema and performs no data transformation.
