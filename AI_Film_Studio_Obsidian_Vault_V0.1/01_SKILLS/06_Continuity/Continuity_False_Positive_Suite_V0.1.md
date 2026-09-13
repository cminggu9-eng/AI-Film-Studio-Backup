---
type: synthetic-policy-suite
role: continuity
phase: 3-verified-nuwa-cross-distillation
status: pass
version: 0.1
---

# Continuity False Positive Suite V0.1

Synthetic architecture tests only; no real screenplay continuity audit was run.

| ID | Case | Expected Continuity result | Evidence / rule basis | Result |
| --- | --- | --- | --- | --- |
| FP-01 | Character lies about a known fact | Treat the line as a character statement, not an automatic Canon contradiction; flag only a separately evidenced conflict. | RL-10; DR-01, DR-03, DR-12 | PASS |
| FP-02 | Audience knows a secret before the character | Preserve audience/character knowledge separation; no character leak unless character action relies on supported-unavailable information. | RL-10; DR-03 | PASS |
| FP-03 | Character merely suspects unrevealed truth | Suspicion is not confirmed knowledge and not a leak. | DR-03, DR-12 | PASS |
| FP-04 | Legal time jump changes costume | Treat explicit elapsed time/support as context before comparing appearance. | RL-02, RL-08; DR-04, DR-10 | PASS |
| FP-05 | Prop transfers off-screen with authorized support | Treat supported off-screen transition as legal change; do not force earlier possession. | RL-03, RL-11; DR-10, DR-12 | PASS |
| FP-06 | Flashback reverses chronological order | Separate story chronology from presentation order. | RL-02, RL-08; DR-05, DR-10 | PASS |
| FP-07 | Montage compresses time | Preserve marked montage as a conditional formal exception. | RL-08, RL-11; DR-04, DR-10 | PASS |
| FP-08 | Character is calmer after meaningful time passage | Do not impose emotional sameness; compare only evidenced carry and context. | RL-03; DR-06, DR-10 | PASS |
| FP-09 | Sparse prior state leaves current state unknown | Retain UNKNOWN and route a question rather than filling the state or declaring error. | RL-03, RL-11; DR-12 | PASS |
| FP-10 | Two similar props are different entities | Do not collapse similar entities; exact designation/evidence is required. | RL-06; DR-01, DR-07 | PASS |
| FP-11 | Intentional continuity break for authorized stylization | Preserve supported stylization as an exception context, not an automatic defect. | RL-08, RL-11; DR-04 | PASS |
| FP-12 | Relationship behavior changes after a new scene event | Allow evidenced qualitative change; do not create a relationship score/meter or demand sameness. | RL-03, RL-09; DR-06, DR-12 | PASS |

Result: False Positive 12 / 12 PASS.

