# Tony Gilroy｜Showrunner 能力蒸馏任务书 V0.1

## 任务性质

AI Film Studio V0.1 的第四份 Showrunner 单人能力方法论蒸馏。沿用既有受控管线；本轮只提取 **Reality-Constrained Longform Design（现实约束下的长篇设计）**，不创建 Showrunner Skill、不进行交叉蒸馏、不提前执行 David Simon。

## 目标

从 Tony Gilroy 本人的可核验公开访谈、编剧／showrunning 讨论、writers' room 或制作过程资料中，提取可复用的判断方法：

1. **Destination Awareness**：终点何时必须清晰，哪些路径可保持开放；终点清楚但过程允许发现；
2. **Reality State**：场景的 Entry State → Event → Exit State，以及信息、欲望、风险、权力和资源如何变化；不要求每场巨大变化；
3. **Causal Reality / Reality Check**：制度、权限、信息、资源、时间、组织反应与现实后果是否支持行为发生；现实逻辑不等于禁绝巧合与戏剧化；
4. **Complex Story Simplification**：复杂人物、机构、地点、政治／组织关系如何分层呈现；何时延迟信息，何时通过目标与行动表达；复杂不等于混乱；
5. **Modular Longform Structure**：block／chapter／phase／arc 的功能、局部闭环与模块交接；不得机械规定固定集数；
6. **Character Within Systems**：人物欲望如何与机构、等级、资源、法律、社会关系、时间、地理与权力摩擦；不得提前替代 David Simon 的 World-System 蒸馏；
7. **Production Reality Check**：仅在一手证据足够时归因给 Gilroy；否则标为 `AI FILM STUDIO SYNTHESIS`。以 Creative Intent → Production Cost Driver → 必须保留 → 可重新设计 → Alternate Execution 处理制作约束；不因成本直接删除创意；
8. **Scope Compression**：识别戏剧价值后压缩地点、角色、群演、动作、特效、时间跨度与连戏复杂度，保留权力关系、调查压力、危险升级和世界规模感。若无 Tony 一手依据，必须标 `AI FILM STUDIO SYNTHESIS`。

## 不要提取

- *Andor*、*Rogue One*、*Michael Clayton* 或其他作品的具体剧情、角色、世界观与组织模板；
- 帝国／反抗军、政治惊悚、复杂／阴暗／写实等表层元素；
- Tony Gilroy 的对白风格、视觉设计、写实审美或“像 Tony Gilroy 一样写”的人格；
- 把复杂性本身、低成本本身或制作困难本身当作方法论。

## 证据与标签要求

优先使用 Gilroy 本人的长访谈、编剧／showrunning 讨论、Writers Guild／Script Magazine／播客与制作过程公开讨论。二手资料只能定位或交叉核验，不能独自支撑核心方法。

每条重要结论必须标为三者之一：

- `SOURCE-SUPPORTED`：一手来源直接支持，主张不得超过原文；
- `SYNTHESIZED INFERENCE`：多个来源归纳出的可执行方法，不能伪装成 Gilroy 原话；
- `AI FILM STUDIO SYNTHESIS`：为 AI Film Studio 制作流程形成的 Studio 自有规则，不能归因给 Gilroy。

最终方法还必须标为：硬约束、默认启发式、条件适用方法或可选工具。

## 执行流程

1. 读取本任务书、`AGENTS.md`、`PUBLISH_RULES.md`、`studio.config.json` 与完整 `huashu-nuwa`。
2. 仅在 `runtime/_STAGING/_research/Tony_Gilroy_V0.1/` 建立来源—主张证据工作区和唯一核心账本。
3. 按女娲 Skill 的直接人物路径完成多源研究与提炼；首稿只能写入：
   `runtime/_STAGING/Tony_Gilroy_Showrunner_Distillation_V0.1.md`。
4. Codex 独立审核 Destination Awareness、Scene Entry／Exit State、Reality Check、复杂性管理、模块化长篇、人物—系统、制作可行性与 Scope Compression，并检查三层证据标签未混淆。
5. 使用原创测试概念干跑，不发展为正式项目：
   “一家沿海城市大型物流企业在一次常规系统升级后，发现部分旧货运记录被人为修改。一名普通内部审计员最初只负责确认财务异常；随着调查，她发现物流公司、地方承包商以及一个重要港口建设项目之间存在长期利益关系。”
6. 干跑必须覆盖：终点意识、审计员向主管询问异常记录的 Entry State → Event → Exit State、复杂信息分层、模块化第一阶段、现实因果与权限路径、18 角色／14 地点／两场大型港口行动／多个政府会议／车辆群众的 Production Reality Check 与 Scope Compression。
7. 若证据、因果、复杂度或制作规则不通过，定向补证据／返工／重跑；未通过不得发布。
8. 审核通过后设置 frontmatter `approved/passed`，仅调用：

```powershell
python scripts/publish_to_obsidian.py `
  --source "runtime/_STAGING/Tony_Gilroy_Showrunner_Distillation_V0.1.md" `
  --dest "02_DISTILLATION/编剧研究/Tony Gilroy｜Showrunner能力蒸馏 V0.1.md" `
  --title "Tony Gilroy Showrunner 能力蒸馏 V0.1"
```

## 机械化禁区

- 不得把“长篇必须知道全部结局和过程”写成硬规则；
- 不得要求每场都让所有人物状态巨大变化；
- 不得以大量解释代替复杂性管理；
- 不得把现实逻辑写成禁绝巧合、戏剧化或人物异常决定；
- 不得固定“三集一个 block”；
- 不得因制作困难直接删除创意；
- 不得把制作成本优先级置于戏剧价值之前；
- 不得让观众“不完全理解”成为复杂性的荣誉；
- 人物可以突破规则，但世界必须合理回应。

## 完成标准

- 实际遵循 `huashu-nuwa`；
- 核心方法具备可核验的一手证据且三层标签清晰；
- 形成输入 → 判断 → 决策 → 输出的 Reality-Constrained Longform Design；
- Production Reality Check 与 Scope Compression 未被错误归因；
- 原创干跑、Codex 独立审核与必要返工通过；
- 正式 Obsidian 文件、`_PUBLISHED` 归档与工作日志真实存在；
- 完成后立即停止，不自动执行 David Simon、交叉蒸馏、Showrunner 能力模型、Showrunner SKILL.md 或正式剧本开发。
