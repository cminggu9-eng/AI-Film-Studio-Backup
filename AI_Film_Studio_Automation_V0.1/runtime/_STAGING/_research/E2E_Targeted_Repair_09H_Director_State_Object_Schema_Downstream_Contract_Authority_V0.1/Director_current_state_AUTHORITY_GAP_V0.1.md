# Director current_state Authority Gap V0.1

## Lawful purpose

This field is the present state that the Director may observe and use for directorial choices. It must remain bounded by upstream locks and cannot become a free-form narrative summary.

## Missing authority

The runtime's Scene Writer snapshot has nine fixture-local keys, while the 09B Director contract declares only an unrestricted object. No authority states that Director `current_state` is that Scene Writer snapshot, a filtered view, or a newly authored Director object. No key/value domain is common and authoritative across fixtures.

## Decision required

Approve whether `current_state` is (a) a carried Scene Writer snapshot with its compiled schema, (b) a deterministic, named projection, or (c) a separate Director-owned state type. Define that source before strict Provider schema work.

