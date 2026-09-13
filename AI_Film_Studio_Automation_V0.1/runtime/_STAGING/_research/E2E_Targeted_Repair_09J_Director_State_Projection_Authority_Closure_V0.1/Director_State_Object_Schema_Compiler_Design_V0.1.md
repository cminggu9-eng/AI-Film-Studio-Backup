# Director State Object Schema Compiler Design V0.1

## Inputs

- versioned `compiled_run_contract`;
- validated upstream scene records with explicit compiled `scene_id` association;
- run-local State Ledger entries and `sequence`;
- canonical owner/lifecycle metadata and locks/prohibitions;
- authorized transition registry;
- optional closed knowledge source and explicit dimension-classification metadata.

## Stages

1. Validate input identities, versions, scene associations, and source schemas.
2. Select prior/current records using the Source Winner Contract; fail on conflict or missing required source.
3. Clone scene IDs, state properties, types, and enums from compiled schema nodes; emit an authority-manifest pointer for each generated property.
4. Emit `proposed_state` only for explicitly Director-writable dimensions; otherwise typed `ABSENT`.
5. Emit knowledge/visual object schemas only from closed source schemas/classification; otherwise typed `ABSENT`.
6. Close every object with exact `required` and `additionalProperties:false`; validate typed `ABSENT` branches.
7. Output schema bundle, authority manifest, compiler-version/hash inputs, and failure attribution. Do not serialize objects to strings.

## Outputs

- five per-run schemas;
- property/token/source authority manifest;
- source-selection trace;
- deterministic schema hash inputs;
- fail-closed diagnostic without semantic repair.

No runtime compiler was implemented in 09J.

