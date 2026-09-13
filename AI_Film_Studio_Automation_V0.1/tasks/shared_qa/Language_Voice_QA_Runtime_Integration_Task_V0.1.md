---
type: automation-task
status: completed
version: 0.1
subject: Language & Voice QA Runtime Integration
canonical_identity: language-voice-qa
runtime_integration_status: published
---

# AI Film Studio｜Language & Voice QA Runtime Integration V0.1 任务书

## 目标

将已发布的 canonical `language-voice-qa` Production Skill V0.1 以独立 Shared QA Runtime Adapter 接入 AI Film Studio，建立可由未来合法调用者使用的输入封装、契约验证、七状态处理、失败安全、幂等与审计接口。

## Source of Truth

1. Showrunner Production Lock / Vault Governance
2. `01_SKILLS/Shared_QA/SKILL.md`
3. `Language & Voice QA｜综合能力模型 V0.1.md`
4. `Language & Voice QA｜五人交叉蒸馏 V0.1.md`
5. 本任务的 Runtime Contract / Adapter

## 架构边界

- 使用 `runtime/shared_qa/` 独立 Adapter；不注册进、也不修改 locked Showrunner Runtime。
- canonical Skill 仍位于正式 Vault；本任务不安装、不改写、不复制替代其能力语义。
- Scene Writer 与 Contemporary Language Layer 不存在于本调用链；Synthetic Caller 仅用于非正史测试。
- 测试资产只进入 `runtime/_TEST_SANDBOX/`，研发与审核记录先进入 `runtime/_STAGING/`。

## 验收门

- TEST-RT01–RT20：20/20 PASS
- Production Safety Stress：10/10 PASS
- Seven-State Mapping：7/7 PASS
- Static Audit、Runtime Drift Audit、Hash Integrity、Codex Final Review：全部 PASS
- Full Passage Fixture 不存在时保持 `SKIP — FIXTURE NOT AVAILABLE`
- 受控发布不得覆盖既有 `_PUBLISHED` 快照

## Lifecycle

`active → completed` 仅可在 staging 测试通过、正式 Adapter 建立、受控发布快照存在、Hub / 当前进度 / 工作日志更新且冻结资产哈希复核通过后执行。

## Completion Receipt

- Architecture Audit：`PASS`
- Integration Pattern：`Parallel Shared QA Adapter`
- Formal Runtime：`runtime/shared_qa/`
- Seven-State Mapping：`7 / 7 PASS`
- TEST-RT01–RT20：`20 / 20 PASS`
- Production Safety Stress：`10 / 10 PASS`
- Static / Drift / Hash：`PASS`
- Published Snapshot：`runtime/_PUBLISHED/2026-08-24/Language_Voice_QA_Runtime_Integration_V0.1.zip`
- Contemporary Language Layer / Scene Writer：`NOT STARTED`
