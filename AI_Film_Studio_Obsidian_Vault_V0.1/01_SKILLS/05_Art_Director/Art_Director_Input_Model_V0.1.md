---
type: input-model
role: art-director
status: phase-4-capability-model-complete-awaiting-user-review
version: 0.1
---

# Art Director Input Model V0.1

This is a capability input taxonomy, not a Runtime JSON schema.

| Category | Inputs | Handling rule |
| --- | --- | --- |
| REQUIRED | Canon/world facts; story/scene material; location/period facts; character identities; required objects/environments; locked dramatic functions. | Validate authority and contradictions before design. Missing or conflicting material facts may block. |
| USEFUL | Showrunner tone/thematic intent; Director visual/spatial intent; Character & Acting physical-performance needs; production constraints; prior visual decisions; research references; current visual-state information. | Use when relevant and retain the owner boundary. Their absence does not automatically block. |
| OPTIONAL | Moodboard; look-book; image references; implementation constraints; future external AI production constraints. | May inform an evidence-supported creative opportunity; their absence must never cause context hunger or a block. |

## Input acceptance and limits

- Distinguish an input fact from a reference, interpretation, request, preference, or production constraint.
- Do not convert a style name, reference image, or optional visual preference into a Canon or research fact.
- Authorized external visual-production constraints may be received only as a future interface boundary. This model does not define model IDs, prompts, sampling, image generation, ComfyUI, GPU, seed, or resolution behavior.
- If useful context conflicts with required higher authority, follow the Authority Model and hand off the unresolved conflict.

