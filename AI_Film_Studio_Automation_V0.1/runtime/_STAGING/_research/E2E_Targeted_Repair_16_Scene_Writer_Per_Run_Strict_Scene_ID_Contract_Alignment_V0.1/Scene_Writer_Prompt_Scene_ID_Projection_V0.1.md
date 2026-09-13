# Scene Writer Prompt Scene-ID Projection V0.1

Result: PASS.

The Scene Writer system prompt now embeds the current run's machine projection and explicitly requires the exact full-token order in `scenes[*].id`. Each current-run ID appears once; IDs from the other two fixture bindings appear zero times.

The prompt assembly order is: role constraints, transport instruction, current-run scene-ID contract, run contract, then one canonical Skill block. A duplicated canonical Skill concatenation found during final inspection was removed and the file was recompiled before the final 20/20 run.
