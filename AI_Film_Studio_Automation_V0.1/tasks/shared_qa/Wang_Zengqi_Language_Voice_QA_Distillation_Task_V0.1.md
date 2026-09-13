---
type: distillation-task
status: completed
version: 0.1
subject: 汪曾祺
domain: Language & Voice QA
target_capability: Natural Chinese Judgment
sequence: 2/5
---

# 汪曾祺｜Language & Voice QA 能力蒸馏任务 V0.1

## 任务边界

本轮只抽取 `Natural Chinese Judgment`：判断语法正确、意思基本明确、事实无误的表达，为什么仍可能不像当前语境中的人会这样说或写。

不得模仿汪曾祺文风、清淡散文、生活化描写、句长、节奏、词汇、地域口语或“烟火气”；不得把所有中文改成朴素短句。不得启动老舍、余光中、刘震云、Cross-Distillation、Capability Model、QA Skill、Runtime 或 Scene Writer。

## 角色与发布管线

- Codex：证据准备、调度、独立审核、测试与发布控制。
- `huashu-nuwa`：能力方法论正式蒸馏执行器。
- 首稿只能写入 `runtime/_STAGING/Wang_Zengqi_Language_Voice_QA_Distillation_V0.1.md`。
- 审核失败不得发布；通过后只能由 `scripts/publish_to_obsidian.py` 发布。
- 目标：`02_DISTILLATION/语言与表达研究/汪曾祺｜Language & Voice QA 能力蒸馏 V0.1.md`。

## 能力模块

1. `Language as Meaning`：`MEANING + LANGUAGE FORM + REGISTER → ACTUAL EFFECT`；形式不是无影响的包装，也不是越漂亮越好。
2. `Natural Flow`：检查意思承接、真实重心、强行转折、追加总结和概念超载；长短不是判定式。
3. `Anti-Overwriting`：比较原始事实与新增抽象层，识别为高级感、完整感、概念感额外搭出的包装。
4. `Anti-Rhetoric`：对仗、排比、哲学句、口号、海报句与预告式总结按 `Frequency + Context + Register + Necessity` 判断，不设禁句。
5. `Concrete Before Abstract`：抽象总结应能回指人物、事件、动作、关系与结果；这是默认启发式，不是禁止抽象。
6. `Restraint`：表达已完成时停止；教学、复杂诊断、技术说明可保留必要解释。
7. `Whole-Context Judgment`：同时检查单句与段落模式，避免词语/句型黑名单。
8. `Ordinary Words`：普通词可以够用；专业词也可以必要。只判断当前用途中的必要性。

## 与叶圣陶边界

- 叶圣陶：Meaning Before Wording、Expression Accuracy、Clarity、Revision With Reasons、Meaning Preservation。
- 汪曾祺：语言形式造成的实际效果、整体流动、具体锚点、停止解释、反额外包装与整段自然度。
- 结论只能是 `COMPLEMENTARY CANDIDATE`，不得在本轮融合为 Cross-Distillation。

## 伪术语有限边界

汪曾祺模块可指出“任务事故现场”是否生硬、做作或普通说法已足够，但完整 `TERM PLAUSIBILITY` 仍属于 Charter/未来综合 QA。新词不自动等于不自然。

## 证据协议

必须重新打开候选审计的三份一手材料：

- WZQ-01：《小说里边最重要的是什么？》
- WZQ-02：《“揉面”——谈语言》
- WZQ-03：《我的作品所包涵的是什么样的感情？》

允许补充高质量一手材料；二手评论不得单独支撑核心方法。建立 canonical Evidence Ledger，记录来源、身份、可访问性、原文锚、直接支持范围、不可外推范围与主稿映射。

每条主要方法必须标注：

- `SOURCE-SUPPORTED`
- `SYNTHESIZED INFERENCE`
- `AI FILM STUDIO SYNTHESIS`

并归入：

- `HARD CONSTRAINT`
- `DEFAULT HEURISTIC`
- `CONDITIONAL METHOD`
- `OPTIONAL TOOL`

## 女娲调用约束

完整读取并实际使用 `C:\Users\布朗熊\.codex\skills\nuwa-skill\SKILL.md` 及 `references/extraction-framework.md`。采用主题/能力方法论变体：证据优先、来源分级、三重验证、诚实边界、原创测试与独立审核。

不得生成身份卡、人物角色扮演、表达 DNA、个人语气或 Perspective Skill。保存 Skill 名称、实际路径、SHA-256、读取状态、调用时间、采用阶段及省略项的正式回执。

## Staging 必备章节

- `## 蒸馏目标`
- `## 核心判断原则`
- `## Language as Meaning`
- `## Natural Flow`
- `## Anti-Overwriting`
- `## Anti-Rhetoric`
- `## Concrete Before Abstract`
- `## Restraint`
- `## Whole-Context Judgment`
- `## Ordinary Words`
- `## 与叶圣陶能力边界`
- `## QA MODE 应用`
- `## REWRITE MODE 应用`
- `## 工作流程`
- `## 诊断问题`
- `## 失败模式`
- `## 修正方法`
- `## 禁止继承`
- `## 可 Skill 化规则`
- `## 证据与来源`
- `## Codex 审核结论`

## TEST A｜主题宣言 AI 腔

输入：`当一切善意都必须被系统计分，一个人还会不会去帮助那些没有奖励价值的人？`

语境：R1 Showrunner 创作讨论；QA Mode。检查 Abstract Density、Rhetorical Structure、Overwriting、Concrete Anchor、Register、Theme Prematurity。不得直接改写。

## TEST B｜人工二元

输入：`他必须在服从规则和保住一个具体的人之间选择。`

检查 Binary Symmetry、Abstract Nouns 与真实因果。Rewrite Mode 先锁 Meaning，分别给普通讨论版与保留概括版，并验证意义。

## TEST C｜Trailer Copy Register 差异

输入：`寻找那个已经被全城遗忘、却仍存在于男主记忆中的人。`

分别按 R1 Creative Discussion 与 R8 Marketing Copy 判断；若结论完全相同则失败。

## TEST D｜过度总结

输入：`男主第二天去上班，发现同事不认识昨天出现的女孩。监控里也没有她。他开始怀疑自己的记忆。真正重要的是，这不仅是一次记忆异常，更是他对于真实、自我和系统定义之间关系的重新认识。`

检查前半信息是否已经完成，后半是否总结过早、抽象跳跃、口号化或意义膨胀。

## TEST E｜正常抽象语言

输入：`这一季的核心冲突是男主逐渐失去系统权限。`  
语境：R2 Project Brief。期望 `PASS / NO CHANGE`。

## TEST F｜正常专业词

输入：`本轮先验证 Series Engine 和 Character Engine，暂不进入 Scene Writer。`  
语境：R7 AI Film Studio Production Note。期望 `PASS / NO CHANGE`。

## TEST G｜伪高级 Project Brief

输入：`本阶段将通过对人物关系、系统机制以及世界结构的多维度重构，进一步强化项目在持续叙事层面的核心驱动力。`

检查 Empty High-Level Wording、Abstract Noun Stacking、Nominalization 与 Overwriting；不得提前把问题归因于尚未蒸馏的余光中或“西化中文”。

## TEST H｜NO CHANGE

输入：`这个人第二天没有来上班。`  
语境：R1 Creative Discussion。期望 `NO CHANGE`，不得文学化。

## TEST I｜Fake Casualness

输入：`说白了吧，其实这个故事就是怎么说呢，一个男的嘛，他反正就是发现系统不太对劲。`

检查 Fake Casualness 与信息组织失败；自然不等于口语、短句或随意。

## TEST J｜Modernity

构造同一意义的两版：A 为 2026 项目讨论中的自然普通话；B 为刻意历史文学表达。方法不得偏好 B，只按当前 Register 判断。

## Codex 审核门

1. Natural Flow；2. Anti-Overwriting；3. Anti-Rhetoric；4. Concrete Before Abstract；5. Restraint；6. Whole-context Judgment；7. 专业词保护；8. NO CHANGE；9. Natural ≠ Short；10. Natural ≠ Colloquial；11. 无文风模仿；12. Modernity 受控；13. 与叶圣陶独立；14. TEST A–J 全通过；15. 具备后续 Cross-Distillation 价值。

任一门失败：定位问题，定向补证据或返工，重跑受影响测试，再审核；最多两轮，仍失败则保持 staging 并报告 `BLOCKED`。

## 发布条件

审核 PASS 后才可设置：

```yaml
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 汪曾祺
domain: Language & Voice QA
```

必须先由发布脚本 dry-run，再正式发布。成功后确认 Vault 文件、`_PUBLISHED/<YYYY-MM-DD>/` 归档、工作日志和零阻塞，随后立即停止。
