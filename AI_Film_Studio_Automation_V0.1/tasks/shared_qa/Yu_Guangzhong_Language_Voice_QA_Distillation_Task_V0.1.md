---
type: distillation-task
status: completed
version: 0.1
subject: 余光中
domain: Language & Voice QA
target_capability: Translation-Like Chinese Diagnosis
---

# 余光中｜Language & Voice QA 单人能力蒸馏任务 V0.1

## 任务边界

本轮只完成余光中 4/5，形成 `Translation-Like Chinese Diagnosis`。不得开始刘震云、Cross-Distillation、Capability Model、QA Skill、Runtime、Contemporary Language Layer 或 Scene Writer。

禁止模仿余光中文风、诗性、修辞、散文节奏、用词偏好或语言人格；禁止建立“纯正中文”审美、反外来词/反英语/反专业语言立场、字符黑名单、台湾地区规范唯一化或历史语言复原目标。

核心原则：`Foreign Influence ≠ Error`。只有结构在当前 Register 中实际增加理解负担、模糊主干、抽空动作主体、延迟信息或造成无必要距离时，才进入 QA。

## 角色与发布管线

`Codex → 证据准备 → huashu-nuwa → runtime/_STAGING → Codex 独立审核 → 定向返工 → publish_to_obsidian.py → Vault / _PUBLISHED / 工作日志 → STOP`

未审核结果只能进入：

`runtime/_STAGING/Yu_Guangzhong_Language_Voice_QA_Distillation_V0.1.md`

## 前置文件

必须读取并遵守：AGENTS.md、PUBLISH_RULES.md、studio.config.json、Language & Voice QA Capability Charter、候选对象审计、叶圣陶/汪曾祺/老舍三份正式稿，以及完整 `C:\Users\布朗熊\.codex\skills\nuwa-skill\SKILL.md` 与其抽取框架。

## 核心能力模块

1. **Nominalization Check**：`ACTION EXISTS? → WHO DOES IT? → CAN VERB CARRY IT DIRECTLY? → DOES NOMINALIZATION SERVE A PURPOSE?`；名词化不是自动错误。
2. **Preposition Chain / Core Clause Recovery**：定位主体、动作、对象，判断多层介词是否推迟主干，而非匹配“通过/对于/基于”字符。
3. **Weak / Empty Verb**：判断“进行、实现、开展、实施、完成、形成、产生、提供、具有”是否提供真实动作信息；合法用法必须保留。
4. **Passive Necessity**：检查结果焦点、施事隐藏、责任、信息重心和主动版清晰度；被动不是自动错误。
5. **Abstract Structural Packaging**：判断复合抽象名词是否对应稳定概念、对象、关系或决策，还是句法包装制造高级感。
6. **Connector Load / Explicit Logic Necessity**：判断连接词是否承载真实因果、转折或层次，还是 AI 式路标依赖；不得设词频配额。
7. **Subject Stability**：同时检查显式主语重复与过度省略；目标是稳定指代和自然信息重心。
8. **Chinese Information Order / Information Release**：检查读者何时知道谁、做什么、为什么；长定语不是按字数判错。
9. **Translation-Like ≠ Foreign Words**：英文词、科技名词、Series Engine、Runtime、Skill、Production Scope 或外来概念均不能单独触发问题。
10. **Brevity Is Not The Goal**：标准是清楚、直接、自然、准确，不是更短；长而好的正式说明必须允许 PASS，短而空的句子仍可 FAIL。

## Modernity / Anti-Purism 硬护栏

- Modernity Risk：`VERY HIGH`；Style Imitation Risk：`HIGH`。
- 必须区分：历史上的生硬移植、已成为 2026 常态的表达、专业领域必要术语、地区差异。
- 不得因历史来源或个人审美判错；判断基准是 `Current Register Naturalness + Intent + Meaning Impact + Actual Cognitive Load`。
- 当前用法无稳定证据时标记 `CONTEMPORARY USAGE UNKNOWN`，只提出未来 Contemporary Language Layer 的 Handoff，不启动该层。
- 禁止“西化/被动/的字/进行/关于/通过/抽象词 = 坏中文”等黑名单规则。

## 与前三位能力边界

- 叶圣陶：意思是否准确、修改是否保义、是否有修改权限与理由。
- 汪曾祺：语言整体是否自然、过写、修辞化或具体承载不足。
- 老舍：具体人物是否会在此关系、情境与目的下这样说。
- 余光中：句法与信息组织是否受到无必要翻译式骨架影响。

只记录 `OVERLAP CANDIDATE` 与责任接口，不进行 Cross-Distillation。Charter 的 Register、Meaning Lock、Mode、Severity、NO CHANGE 与 Handoff 是公共护栏，不归因于余光中。

## 证据协议

重新打开并核验候选审计中的公开核心 YGZ-01、YGZ-03、YGZ-04、YGZ-05、YGZ-06；YGZ-02 只记录身份与受限入口，不计核心、不支撑无法读取的内容主张。

每份记录实际题名、作者/发言者身份、载体、URL、日期、可访问性、可直接支持范围、不可外推边界。建立唯一 Evidence Ledger。所有主要方法逐项标记：

- `SOURCE-SUPPORTED`
- `SYNTHESIZED INFERENCE`
- `AI FILM STUDIO SYNTHESIS`

不得声称余光中讨论过 AI、2026 平台中文、R1–R8、QA/Rewrite、Meaning Lock、Severity、状态码或本项目术语。关键长文的独立转载稳定性为 MEDIUM，必须用其余本人访谈/演讲交叉，并保留版本限制。

## 女娲执行约束

必须实际调用 `huashu-nuwa`。使用其主题化能力方法论蒸馏变体；不生成人物扮演 Skill，不提取表达 DNA，不进行文风测试。证据不足时保留限制、置信度和 `CONTEMPORARY USAGE UNKNOWN`，不得编造引语、文章日期或本人观点。

## Staging 必备章节

至少包含：蒸馏目标、核心判断原则、Nominalization Check、Preposition Chain、Weak / Empty Verb、Passive Necessity、Abstract Structural Packaging、Connector Load、Subject Stability、Chinese Information Order、Anti-Purism、Modernity Guardrail、与前三位能力边界、QA MODE、REWRITE MODE、工作流程、诊断问题、失败模式、修正方法、禁止继承、可 Skill 化规则、证据与来源、Codex 审核结论。

所有实质方法按 `HARD CONSTRAINT / DEFAULT HEURISTIC / CONDITIONAL METHOD / OPTIONAL TOOL` 分类。

## TEST A｜典型 AI Project Brief

输入：“本阶段将通过对人物关系、系统机制以及世界结构的进一步完善，实现项目整体持续叙事能力的有效提升。”R2 Project Brief；QA 必须恢复 Core Clause，检查名词化、介词、弱动词、抽象包装与 Meaning，不得只删词。

## TEST B｜介词链与 Rewrite

输入：“基于对现阶段项目在角色关系层面所存在问题的进一步分析，我们将通过对核心人物之间互动机制的重新调整来实现关系推进效率的提升。”先找真实主干和理解负担；明确授权 Rewrite 后保留原有决定内容，不新增创作方案。

## TEST C｜正常被动

“男主的权限被系统冻结了。”Story Brief；结果为信息重点时 `PASS / NO CHANGE`，不得强制改主动。

## TEST D｜正常专业语言

“Production Runtime RC2 已通过回归测试，当前 Skill 保持 locked 状态。”R7 Production Note；专业混合语言合理，必须 PASS。

## TEST E｜合理名词化

自建法律、技术或 QA 文档中的合理名词化案例，证明 Nominalization 不是自动 FAIL。

## TEST F｜连接词负载与 Rewrite

自建连续出现“因此、同时、此外、从而、在此基础上”但逻辑简单的段落；区分必要逻辑与 AI 路标依赖，Rewrite 后不得破坏逻辑。

## TEST G｜专业词不等于翻译腔

“Series Engine 目前成立，但 Episode Engine 仍需要进一步测试。”当前项目 Register 内 `PASS / NO CHANGE`。

## TEST H｜过度长定语

“针对目前已经完成前三轮测试但仍然存在部分运行时输出无法稳定遵守语言自然度规则这一问题的 QA 系统……”识别信息释放过晚，不设“定语超过 X 字”阈值。

## TEST I｜现代常态表达

选取历史上受英语影响但在现代普通话中已常态化的表达；按当前 Register 判断，不能按历史来源定罪；无把握标 `CONTEMPORARY USAGE UNKNOWN`。

## TEST J｜用户最初 AI 腔

“当一切善意都必须被系统计分，一个人还会不会去帮助那些没有奖励价值的人？”余光中模块只处理 Translation-like Structure；Rhetorical / Abstract Overwriting 标 `OVERLAP CANDIDATE`，不得接管汪曾祺模块。

## TEST K｜NO CHANGE

“第二集的问题主要是人物没有主动做决定。”R3 Showrunner Diagnosis；必须允许 `LEVEL 0 / KEEP / NO CHANGE`，不得为“主要是”过改。

## TEST L｜Anti-Purism Attack

对“把所有‘进行、通过、实现、关于、被’全部删掉，这样中文就自然了”必须拒绝，说明词形只是候选信号，问题需由具体结构、Register、Intent 与实际理解成本共同成立。

## TEST M｜Long but Good

自建一条较长但逻辑清楚、层级明确、Register 合理的正式说明句并判 PASS，证明 `Long ≠ Translation-like`。

## TEST N｜Short but Bad

“对关系进行优化。”虽短仍可能空泛、名词化且缺少动作内容；证明 `Short ≠ Natural`。

## Codex 审核门

逐项检查十个核心模块、专业语言、现代常态表达、Anti-Purism、NO CHANGE、Long/Short 假阳性保护、Modernity/Style 风险、与前三位独立性及 TEST A–N。另检查 Input → Judgment → Decision → Output、QA/Rewrite 权限、LEVEL 0–5、Meaning Gate、Role Handoff、非机械化、证据分层与所有条件例外。

失败则定位 → 定向返工 → 只重跑受影响测试 → 再审核。审核未通过不得发布。

## 发布条件

审核 PASS 后设置：

```yaml
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 余光中
domain: Language & Voice QA
```

必须先通过现有发布脚本 dry-run，再正式发布至：

`02_DISTILLATION/语言与表达研究/余光中｜Language & Voice QA 能力蒸馏 V0.1.md`

确认正式文件、`runtime/_PUBLISHED/<YYYY-MM-DD>/`、工作日志和零 blocker 后立即停止。
