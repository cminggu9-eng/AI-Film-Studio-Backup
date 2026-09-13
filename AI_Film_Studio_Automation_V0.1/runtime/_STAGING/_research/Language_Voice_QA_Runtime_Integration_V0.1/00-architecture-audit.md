---
type: runtime-architecture-audit
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA Runtime Integration
audited_at: 2026-08-24T10:31:11+08:00
---

# Language & Voice QA Runtime Architecture Audit V0.1

## 审计范围

已在任何 Runtime 实现修改前读取并核对：Automation `AGENTS.md`、`PUBLISH_RULES.md`、`studio.config.json`、`runtime/` 目录、Showrunner Production Runtime RC2、Runtime Compliance Gate、Production Lock、Vault Rules、canonical `language-voice-qa/SKILL.md`、Capability Model、Cross-Distillation、Shared QA Hub、staging / published 结构、任务生命周期与 Vault Repair Recheck。

## 当前架构事实

- 现有生产执行代码只有 Showrunner 专属的 `runtime/compliance/` Adapter、显式 Showrunner Router 和 Gate；它不是通用 Runtime 总线。
- `runtime/` 是项目正式的运行层根目录；现有模式允许在其下以域为边界放置可审计 Adapter，并把测试隔离到 `_TEST_SANDBOX`、日志写入 `_COMPLIANCE_LOG`、研发证据写入 `_STAGING`。
- Showrunner Router 对对白润色只产生 `Non-Showrunner / Scene Writer Boundary` 交接；它不拥有 Language & Voice QA，也无需为本任务修改。
- 项目不存在通用 module registry、skill registry、hook、dispatcher、plugin interface 或第二个总 Router。
- canonical Language & Voice QA Skill 的身份、版本和七个互斥状态足以建立 transport contract；Skill 未安装不是阻塞，因为 Adapter 可显式绑定正式 Vault canonical 文件并由调用者提供执行器。

## RA-01｜是否存在正式 Runtime 扩展点

`YES`。合法扩展面是项目已采用的 `runtime/<domain>/` 显式 Adapter 包边界，而非中央插件注册表。本轮可新增 `runtime/shared_qa/`，不改变现有 Showrunner 专属包。

## RA-02｜能否不修改 locked Showrunner Runtime

`YES`。Shared QA Adapter 可作为独立可调用能力，由未来合法上游显式调用；不需要进入 `runtime/compliance/`、`showrunner_role_router.py` 或 Showrunner Gate。

## RA-03｜现有扩展机制清单

|机制|现状|
|---|---|
|module registry|不存在|
|skill registry|不存在|
|router|存在，但仅为 Showrunner 显式 Router，不作为本轮扩展点|
|adapter|存在正式先例：`runtime/compliance/runtime_pipeline.py`|
|hook|不存在|
|gate|存在，但仅为 locked Showrunner Compliance Gate|
|orchestration extension|存在显式 Orchestrator → domain Adapter 调用边界|
|dispatcher|不存在通用实现|
|plugin-like interface|不存在|

## RA-04｜采用的合法扩展点

`runtime/shared_qa/` 下的独立 `LanguageVoiceQARuntime` Adapter：

`Future Authorized Caller → Shared QA Adapter → Input Contract → caller-supplied language-voice-qa executor → Canonical Output Contract → Runtime Handler`

Adapter 只收集、规范化、验证、传递、接收、处理和记录；不执行 Severity、Rewrite 或审美判断。

## RA-05｜是否必须修改 locked Runtime

`NO`。不需要修改 locked Showrunner Skill、Showrunner Runtime、Runtime Compliance Gate、Production Lock 或 Canon。不存在 `NO AUTHORIZED RUNTIME EXTENSION POINT` 阻塞条件。

## 架构决定

`PASS` — 允许进入 staging 实现。正式模式为 `Parallel Shared QA Adapter`；禁止建立第二个总 Router、第二套 Showrunner Runtime 或未来层占位实现。

