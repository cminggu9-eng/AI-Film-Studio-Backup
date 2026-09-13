# Scene Writer State Validator Alignment V0.1

Result: PASS.

Provider schema, strict argument validator, compact hydrator, structural gate, and state-token gate now share one projection. Validation distinguishes field identity from token identity:

- legal token in wrong field: rejected;
- illegal token in correct field: rejected;
- foreign entity or transition: rejected;
- unknown state dimension: rejected.

Bridge failures are attributable integration/state-contract failures, not role-semantic failures. No value is repaired.
