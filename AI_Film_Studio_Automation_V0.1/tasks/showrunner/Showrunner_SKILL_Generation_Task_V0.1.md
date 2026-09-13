# AI Film Studio V0.1 — Showrunner Production Skill 生成任务书

## 授权与边界

本轮已获用户授权，将已批准的 `Showrunner｜综合能力模型 V0.1.md` 转译为可被 Codex 实际调用的 canonical `Showrunner SKILL.md`。不重新研究五位创作者，不重做理论，不安装到 `C:\Users\布朗熊\.codex\skills`，不标记 production locked，不启动 Scene Writer、Director 或正式剧本开发。

Codex 负责编排、审核、测试和发布；女娲 `huashu-nuwa` 负责 Capability Model → Production Skill 转译；用户保留最终创作决定权。

## 核心输入

- 主要：`AI_Film_Studio_Obsidian_Vault_V0.1/01_SKILLS/01_Showrunner/Showrunner｜综合能力模型 V0.1.md`
- 辅助：`AI_Film_Studio_Obsidian_Vault_V0.1/02_DISTILLATION/方法论/Showrunner｜五人交叉蒸馏 V0.1.md`
- 必要时仅回查五份单人档案 provenance，不重新蒸馏。

## Skill 必须具备

Trigger/use cases 与“不应调用”边界；PROJECT STATE ASSESSMENT；Format Fit；完整 8 层 Decision Stack；World/System 与 Series 模块开关；因果检查器；Series Engine；Production Reality 五段顺序；13 类诊断码；INFO/WARNING/BLOCKED；Conflict Resolver；7 类回环；10 类输出；五类 Downstream Handoff；用户最终决定权；内部 provenance。

Skill 必须是执行器而非理论复制，能够说明读取什么、按何顺序判断、何时跳过、何时回环、何时 WARNING/BLOCKED、输出什么、如何自检和交接。

## 首轮产物

首轮仅写入：`runtime/_STAGING/Showrunner_SKILL_V0.1.md`。允许建立 `tests/showrunner/` 和 `runtime/_STAGING/_research/Showrunner_SKILL_V0.1/skill-test-report.md`，不得直接写入 Vault 或全局 Skill 目录。

## 测试门

必须完成 8 项功能测试：Idea Development、轻喜剧、复杂都市悬疑、已有剧本诊断、Canon Conflict、Production Scope、错误导演请求、错误表演请求；并完成反机械化攻击测试：强制反转、每集成长、固定三线、删角色、禁止反派、随机杀人、硬加社会议题、锁结局即锁过程。

每项记录 `INPUT / TRIGGER / MODE / DECISION PATH / OUTPUT TYPE / WARNING或BLOCK / HANDOFF / PASS或FAIL`。任何核心测试失败必须执行 `FAILURE → ROOT CAUSE → SKILL INSTRUCTION → REVISION → RETEST`；若是模型级问题，停止并报告 `MODEL-LEVEL ISSUE`。

## 发布

通过静态审核、8 项测试、反机械化、Canon、Production、岗位边界和用户决定权审核后，设置：

```yaml
type: skill
status: approved
review_result: passed
version: 0.1
subject: AI Film Studio Showrunner
installation_status: not-installed
```

使用 `scripts/publish_to_obsidian.py` 发布 canonical source 至 `01_SKILLS/01_Showrunner/SKILL.md`，同时以相同 staging→review→publish 原则发布 `CHANGELOG.md`。不复制到 `.codex/skills`，不锁定。发布成功后立即停止。
