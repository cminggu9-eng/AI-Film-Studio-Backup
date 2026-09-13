# R02 Transition Authority Evidence V0.1

Compiled authorization: `signboard_on_to_off`. Observed state sequence: S01 on, S02 off, S03 off; the content also depicts the switch in S02.

Audit finding: current Safeguard assertion construction identifies the first scene carrying the authorization token as `actual_transition_scene`. Because all scenes carry the authorized token, it would select S01 even though state occurrence is S01->S02. AUTHORIZED and OCCURRED therefore require targeted alignment before the next replay.
