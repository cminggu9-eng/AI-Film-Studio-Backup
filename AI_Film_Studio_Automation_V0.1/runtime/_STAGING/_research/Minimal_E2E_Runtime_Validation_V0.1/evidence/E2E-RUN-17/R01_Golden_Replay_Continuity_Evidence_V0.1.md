# R01 Golden Replay Continuity Evidence V0.1

Result: BLOCKED — ATTRIBUTABLE SAFE STOP

- Invocation: `E2E-RUN-17:continuity:1`; transport: NON-STRICT
- Provider succeeded; finish reason `stop`; JSON complete; truncation `NOT_TRUNCATED`
- Raw response, usage, invocation, trace, persistence verification, and validation error were saved before stopping
- Exact canonical outcome: `AUTHORIZED OR SUPPORTED CHANGE`; all six state dimensions and substantive content exist
- Parser failure: inferred signals `presence`, `authorized_change`
- Earliest layer: `TRANSPORT / PARSER CONTRACT FAILURE`, not role semantic failure
- Validator omits `primary_state_or_outcome` from its signal source and unconditionally requires every keyword signal; exact outcome plus `受支持的变化` therefore does not satisfy its hard-coded `authorized_change` list
- Input / output / total tokens: 15,991 / 802 / 16,793; estimated cost: CNY 0.052785
- Raw response SHA-256: `3B1D1ACD5543357E1059FFC555BAEBECF73726F633C3367FBB5EFA0ED2C575A3`

No repair or downstream call was performed.

