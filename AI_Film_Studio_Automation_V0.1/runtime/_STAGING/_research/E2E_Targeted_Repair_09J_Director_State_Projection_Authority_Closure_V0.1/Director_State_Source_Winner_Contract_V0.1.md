# Director State Source Winner Contract V0.1

Winner ordering is:

1. canonical state owner;
2. validated lifecycle state;
3. applicable version/ownership chain;
4. highest valid run-local Ledger `sequence`.

Source authority beats recency. Timestamps, file modification time, Provider order, model preference, and last-write-wins are prohibited.

Every candidate must have an explicit compiled `scene_id` association and source identity. Missing association fails closed; the compiler must not parse prose or guess from record order. Incompatible candidates at the same authority and lifecycle position yield `STATE SOURCE CONFLICT`.

