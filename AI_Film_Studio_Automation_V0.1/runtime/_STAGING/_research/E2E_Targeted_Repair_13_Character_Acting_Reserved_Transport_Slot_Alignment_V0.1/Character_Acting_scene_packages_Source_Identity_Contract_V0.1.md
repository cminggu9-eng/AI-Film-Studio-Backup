# Character & Acting scene_packages Source Identity Contract V0.1

Date: 2026-08-31  
Semantic owner: Scene Writer

Integration records, without copying package semantics:

- `source_role = Scene Writer`
- Absolute source artifact path and SHA-256.
- `source_schema_identity = SCENE-WRITER-INTEGRATION-OUTPUT-CONTRACT-V0.1`
- Stable scene-package content SHA-256.
- Ordered scene package IDs.
- Ordered source record IDs.
- Source versions.
- Evidence locators.

For E2E-RUN-16 the source artifact hash is:

`2B6D81821B1FD9D7D4E56D41C7BAE2422CE5FDCB0A59E2D86A2AB6D0DF9A4441`

Scene IDs remain `E2E-FIX-01-S01`, `E2E-FIX-01-S02`, and `E2E-FIX-01-S03`; source record IDs remain the corresponding `E2E-RUN-16/scene_writer/...` identities. Any source mismatch, mutation, duplicate identity, missing attribution, or changed evidence locator fails closed.

