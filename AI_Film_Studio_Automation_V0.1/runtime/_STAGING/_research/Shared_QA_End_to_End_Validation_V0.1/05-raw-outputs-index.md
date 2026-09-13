---
type: validation-raw-output-index
status: approved
review_result: passed
version: 0.1
subject: Shared QA End-to-End Validation
---

# Shared QA End-to-End Validation V0.1｜Raw Outputs Index

## Runtime invocation record

Runner：`python -X utf8 scripts/run_shared_qa_e2e_validation.py`  
Caller marker：`VALIDATION / SYNTHETIC / NON-CANON`  
Fixture source：`runtime/_TEST_SANDBOX/validation/fixtures/shared_qa/v0.1/`  
Raw output directory：`runtime/_TEST_SANDBOX/validation/results/shared_qa/v0.1/`

每个 F01–F08、C01、C02 都经实际 `LanguageVoiceQARuntime.invoke()` 进入 canonical integrity / input contract / invoker stage。因为项目没有注册 canonical QA executor，十次调用均返回：

```text
runtime_status: FAIL_SAFE
failure_code: F3
failure_message: Skill executor failed: CanonicalExecutorBindingUnavailable
original_preserved: true
```

这是真实 formal adapter 的 fail-safe output，不是 QA state，也不是 fixture expected answer。下列语义步骤因此没有发生：Detection、Severity、Rewrite、Meaning Regression、initial Handoff、Contemporary Evidence Return、final QA callback。

|Fixture|Raw record|Formal Runtime result|Semantic result|
|---|---|---|---|
|F01–F08|`F01.json` … `F08.json`|F3 / FAIL_SAFE|NOT EVALUABLE|
|C01–C02|`C01.json`、`C02.json`|F3 / FAIL_SAFE|Handoff NOT REACHED|

## Full Passage

F08 (`1,536` Chinese characters) was formally created and executed through the same Adapter. It returned the same F3 fail-safe result before canonical QA output. Therefore Full Passage status is `CREATED / EXECUTED — SEMANTIC EVALUATION BLOCKED BY EXECUTION BINDING` rather than the former fixture-unavailable skip.

