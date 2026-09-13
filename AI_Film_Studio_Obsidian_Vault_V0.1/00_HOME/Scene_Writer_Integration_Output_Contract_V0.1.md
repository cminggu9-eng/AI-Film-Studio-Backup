# Scene Writer Integration Output Contract V0.1

## Required Top-Level Contract

The Scene Writer response remains a JSON object with canonical output controls and `scene_packages`. The output contract is fixture-bound and requires three independently valid package items.

## Exact `scene_packages[]` Fields

`scene_id`, `content`, `structural_deliverable`, `state_evidence`, `source_attribution`, `evidence_locator`.

No supplemental or inferred fields are accepted inside a package by this integration contract.

## Exact Structural Deliverable

`structural_deliverable` contains these six Chinese keys, each populated independently from normal scene prose:

`目标`, `阻力`, `对白行动`, `转折`, `入场`, `出场`.

Normal `content` remains creative scene material. The six fields are explicit, machine-checkable delivery structure; parsing prose for labels is not an acceptable substitute.

## Source Attribution

`source_attribution` has exactly `source_role`, `source_record_id`, `version`, and `evidence_locator`. It identifies the run-local scene package and does not grant an authority override.

## No Semantic Mutation

This contract introduces output packaging only. It does not modify Objective, Resistance, Turn, Shootability, Entry/Exit rules, Production Burden, authority boundaries, canonical state tokens, or any canonical Skill prose.

