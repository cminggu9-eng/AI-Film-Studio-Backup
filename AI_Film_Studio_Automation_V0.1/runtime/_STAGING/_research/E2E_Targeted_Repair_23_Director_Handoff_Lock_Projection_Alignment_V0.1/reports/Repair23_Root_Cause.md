# Repair23 Root Cause

## Authoritative source

Production Director handoff locks are authoritative only from the current Scene Writer role result. The exact fields are canon_assignment_locks and prohibited_changes, preserved as ordered native lists.

## Probe22 construction audit

- Sent/handoff expectation: immutable R26 scene_writer_output.json, containing six locks in source order.
- Director input snapshot: the embedded Scene Writer result contains the same six locks in the same order.
- Provider raw arguments: contain no lock field because locks are integration transport, not Director provider-owned output.
- Old received-lock construction: Repair22 test helper independently created the canonical validator with only view_memory_card_decision.
- Post-validation expectation: Probe22 passed the six-lock R26 list to CanonicalRoleExecutor.invoke.

The canonical validator therefore injected a one-lock received list, which was compared with the six-lock authoritative sent list and failed with Received locks changed in transit.

## Classification

- Different authority source: **YES** — received locks came from an independently rebuilt fixture list.
- Probe independently rebuilt locks: **YES**.
- Ordering difference in authoritative evidence: **NO**.
- Hash or serialization identity mismatch: **NO** — validation compares native ordered lists directly.
- Real transit mutation: **NO** — the Provider contract and raw arguments do not transport locks.

Probe22 remains historically FAIL; Repair23 does not rewrite or reclassify it.
