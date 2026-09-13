---
type: director-post-09e-final-wire-capture
status: intercepted-before-network
version: 0.1
---

# Director Post-09E Final Wire Capture V0.1

The real adapter's `build_provider_payload()` path was executed offline and stopped before send.

| Item | Value |
| --- | --- |
| Endpoint base | `https://api.deepseek.com/beta` |
| Function | `submit_director_package` |
| Strict flag | `true` |
| Tool choice | forced `submit_director_package` |
| Provider-neutral contract hash | `3adbf243cc99866251c09091f35c62820322c1b85072c3b5c34f2bce8ac5f8f8` |
| Compatibility projection hash | `06b1bd545b87c70452072f8c3aae3d1e417b87b041f8046b50ed538ca512a1a0` |
| Final parameters hash | `06b1bd545b87c70452072f8c3aae3d1e417b87b041f8046b50ed538ca512a1a0` |
| Final wire payload hash | `070e51eb5baaaeb3fc1b54c4b48e59663e68b8ec7d19a79cb6c1195b41c567c2` |

Projection and final `tools[0].function.parameters` hashes are identical. All nine repaired nodes are typed string enums. Provider calls: `0`.
