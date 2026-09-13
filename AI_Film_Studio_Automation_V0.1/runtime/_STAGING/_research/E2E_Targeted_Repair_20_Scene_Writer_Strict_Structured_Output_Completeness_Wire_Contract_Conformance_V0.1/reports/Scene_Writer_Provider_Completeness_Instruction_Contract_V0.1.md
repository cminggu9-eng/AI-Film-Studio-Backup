# Scene Writer provider completeness instruction contract

The runtime now derives its Scene Writer completeness instruction directly from the final strict parameters schema. It states that each scenes item is independently complete and forbids:

- same-as-above;
- omitted repeated fields;
- implicit inheritance;
- references to another scene as a substitute for a required object;
- placeholder replacement for structural or state.

The instruction recursively prints the schema required sets at runtime. It has no C09, A17, F01, F02, F03 identity, character, prop, battery, or fixture literal hardcode. Structural and complete scene state remain role-owned; Integration validates and transports only.
