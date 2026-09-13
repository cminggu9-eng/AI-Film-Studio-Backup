# Scene Writer Live Schema Path Audit V0.1

Live runner calls `build_structured_output_contract(compiled_run_contract()["strict_schema"])`. The neutral contract is passed through `ModelExecutor`; the DeepSeek adapter alone maps it to beta `tools[].function.parameters`, forced `tool_choice`, and `strict:true`. No live default or Fixture-specific schema is selected.
