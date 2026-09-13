# Director State Schema Compiler Design — Authority Gap V0.1

No compiler design is frozen because the required inputs are incomplete. A future compiler may be designed only after each map is closed and must accept: a versioned selected source record, compiled binding, named projection rule, and authority/lock context; it must emit the five exact object schemas with closed `properties`, `required`, `additionalProperties:false`, enums, and `ABSENT` branches.

Without winner/source-scope and knowledge/proposed-state closure, a compiler would encode unauthorized choices. No runtime/compiler code was written.

