# Character & Acting Reserved Transport Slot Contract V0.1

Date: 2026-08-31  
Result: ALIGNED

The final closed role-result transport retains ten fields. For Character & Acting:

`scene_packages = exact ABSENT`

Field origin: `INTEGRATION_TRANSPORT_ABSENCE_SENTINEL`.

The sentinel is lawful only after Integration confirms:

- A validated upstream Scene Writer output exists.
- Its source artifact exists and is readable.
- The supplied package object matches the persisted artifact.
- Every package retains exact Scene Writer ownership, record ID, version, scene ID, and evidence locator.

`ABSENT` means Character & Acting does not own or emit scene-package semantics. It must never mask a missing upstream source. Integration inserts only the reserved slot; semantic mutation, canonical-token mutation, and scene-package semantic copy are all 0.

