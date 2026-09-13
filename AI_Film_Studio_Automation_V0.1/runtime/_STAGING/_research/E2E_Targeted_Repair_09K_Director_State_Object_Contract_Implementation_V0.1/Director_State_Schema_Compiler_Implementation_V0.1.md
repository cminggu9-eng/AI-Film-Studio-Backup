# Director State Schema Compiler Implementation V0.1

Compiler ID: `DIRECTOR_STATE_OBJECT_SCHEMA_COMPILER_V0.1`.

Inputs are the versioned compiled run contract, validated upstream carry-in records, committed run-local Ledger records, authorized locks, and transition authority records. The compiler loads and hashes eight frozen Repair 09J contracts; no Probe, R13, R14, or model response provides schema authority.

Prior selection is deterministic: previous committed scene snapshot, then explicit same-scene upstream carry-in, then compiled initial enum value only for the first scene. Current selection requires a committed Scene Writer record for every compiled scene and chooses the highest valid lifecycle/sequence winner inside the canonical ownership chain. Conflict or missing source fails compilation.

Scene IDs, dimension keys, types, requiredness, enums, and transitions are cloned from the compiled run contract. Compiler source contains none of the Fixture01–03 IDs, characters, props, dimensions, enum values, or transition tokens tested by `DIR-OBJ-NEG-01`.

The bundle includes authority, input, schema, trace, lock, transition, and bundle hashes. Identical inputs produced structurally identical output and identical bundle hashes.
