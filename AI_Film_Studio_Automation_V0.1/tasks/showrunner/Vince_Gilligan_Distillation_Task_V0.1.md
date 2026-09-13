# Vince Gilligan｜Showrunner 能力蒸馏任务书 V0.1

## 任务性质

AI Film Studio V0.1 的第二份 Showrunner 单人能力方法论蒸馏。沿用既有受控管线，不修改管线架构。

## 目标

从可验证的一手材料中提取 Vince Gilligan 可复用的 **Character Consequence Engine（人物选择—后果—升级发动机）**：

1. 人物欲望如何产生剧情；
2. 人物主动选择如何产生后果；
3. 后果如何成为下一阶段剧情的原因；
4. 如何形成 Choice → Consequence → Escalation 因果链；
5. 如何让人物自己把局势推向更困难的状态；
6. 如何避免依赖随机事件或作者强行制造危机；
7. writers' room 如何 story breaking；
8. 如何从人物状态推导下一步，而非先规定“需要一个反转”；
9. 如何管理既意外又符合人物与因果的升级；
10. 如何判断剧情链已失去人物驱动力。

## 不要提取

- *Breaking Bad* 或 *Better Call Saul* 的具体剧情、角色模板、反英雄套路或犯罪题材表面元素；
- 具体对白、视觉风格、镜头风格或可识别表达；
- “模仿 Vince Gilligan”的写作人格或文风。

## 证据要求

优先使用 Vince Gilligan 本人的长访谈、writers' room 讨论、讲座、播客、编剧过程访谈和可核验公开文字。二手资料仅可辅助定位或交叉检查，不能单独支撑核心方法。

每个重要结论必须标为：

- **直接来源支持**：可回溯到一手材料；或
- **综合推断**：明确列出多个依据，不伪装为原话。

## 方法分类要求

最终产物必须把方法明确标为以下之一：

1. **硬约束**：缺失即导致人物因果链不可验证的条件；
2. **默认启发式**：通常有效、但应可被项目条件推翻的偏好；
3. **条件适用方法**：仅在满足指明前提时采用；
4. **可选工具**：辅助思考或协作，不取代人物判断。

不得把创作者方法改写成“每一场/每一集必须如此”的绝对公式。

## 执行流程

1. 读取本任务书、`AGENTS.md`、`PUBLISH_RULES.md`、`studio.config.json` 和已安装的 `huashu-nuwa`。
2. 在 `runtime/_STAGING/` 建立本次证据工作区并准备来源—主张对应关系。
3. 依女娲 Skill 执行单人能力蒸馏；首稿只能写入：
   `runtime/_STAGING/Vince_Gilligan_Showrunner_Distillation_V0.1.md`。
4. Codex 独立审核：证据边界、人物因果发动机、story breaking、反随机危机、反“为了反转而反转”、可执行性与方法分类。
5. 用一个不涉及上述作品的原创简单故事干跑；若发现机械化、因果断裂、人物服务剧情、强制升级、错误禁止随机事件或证据不足，定向返工。
6. 审核通过后将 frontmatter 设为 `approved/passed`，仅通过下列脚本发布：

```powershell
python scripts/publish_to_obsidian.py `
  --source "runtime/_STAGING/Vince_Gilligan_Showrunner_Distillation_V0.1.md" `
  --dest "02_DISTILLATION/编剧研究/Vince Gilligan｜Showrunner能力蒸馏 V0.1.md" `
  --title "Vince Gilligan Showrunner 能力蒸馏 V0.1"
```

## 完成标准

- 实际遵循 `huashu-nuwa`；
- 核心方法有可验证的一手证据；
- 形成 Choice → Consequence → Escalation 的人物因果发动机；
- 形成可用于 writers' room 的 story-breaking 输入、判断、决策与输出；
- 清楚区分硬约束、默认启发式、条件方法和可选工具；
- 包含诊断问题、失败模式、修正方法、禁止继承与可 Skill 化规则；
- 可执行性干跑与 Codex 审核均通过；
- 发布脚本成功，Vault 档案与工作日志均真实存在。
