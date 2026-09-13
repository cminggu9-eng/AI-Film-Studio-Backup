---
type: distillation-task
status: completed
version: 0.1
subject: 老舍
domain: Language & Voice QA
target_capability: Situation-Specific Spoken Language Judgment
---

# 老舍｜Language & Voice QA 单人能力蒸馏任务 V0.1

## 任务边界

本轮只完成老舍 3/5，形成 `Situation-Specific Spoken Language Judgment`。不得开始余光中、刘震云、Cross-Distillation、Capability Model、QA Skill、Runtime 或 Scene Writer。

禁止模仿老舍文风、北京话、幽默、曲艺节奏、时代口语、旧社会称谓、固定句式与人物模板。只抽取：

`WHO → TO WHOM → WHY NOW → WANT → KNOW / BELIEVE / ADMIT → ACTUAL SPEECH POSSIBILITY`

## 角色与发布管线

`Codex → 证据准备 → huashu-nuwa → runtime/_STAGING → Codex 审核 → 定向返工 → publish_to_obsidian.py → Vault / _PUBLISHED / 工作日志 → STOP`

未审核结果只能进入：

`runtime/_STAGING/Lao_She_Language_Voice_QA_Distillation_V0.1.md`

## 前置文件

必须读取并遵守：AGENTS.md、PUBLISH_RULES.md、studio.config.json、Language & Voice QA Capability Charter、候选对象审计、叶圣陶正式稿、汪曾祺正式稿，以及完整 `C:\Users\布朗熊\.codex\skills\nuwa-skill\SKILL.md`。

## 核心能力模块

1. Character-Specific Speech：年龄、职业、教育、社会位置、性格、关系、经验、习惯和理解程度共同形成可能说法；禁止角色词库。
2. Situation-Specific Speech：`PERSON + RELATIONSHIP + PRESSURE + GOAL → SPEECH POSSIBILITY`；同一人物随对象和压力变化。
3. Speech Purpose：说话首先服务人物当前沟通动作，不以“观众需要知道”为唯一目的。
4. Information Ownership：人物只能自然表达其知道、相信、怀疑、愿意承认且有权说出的内容。
5. Natural Incompleteness：省略、中断、绕开、不答或动作代答必须有具体理由；禁止机械添加口语填充词。
6. Subtext Awareness：识别表层语言与目标/关系的合理差异；不替 Scene Writer 或 Character & Acting 设计整套潜台词。
7. Anti-Exposition Dialogue：共享知识只是一个条件；还要检查为何现在说、对谁说、要造成什么效果。解释型对白允许真实确认、争辩、回忆或信息差。
8. Perfectly Articulate Emotion：检查人物是否已理解、愿承认、能表达且此刻有必要完整表达；不得机械要求“不善表达”。
9. Occupation / Social Position：检查具体权力、权限和风险，不使用职业刻板印象。
10. Address Check：每句对白必须有 Receiver，并试图让对方知道、相信、做、停止或误解什么。

## 与前两位能力边界

- 叶圣陶：Meaning Preservation、准确、修改理由与权限。
- 汪曾祺：Natural Flow、Anti-Overwriting、Anti-Rhetoric、Concrete Anchor、Restraint。
- 老舍：谁对谁、为何现在说、在什么关系和压力下说、为了什么目的说、人物会不会这样说。

只记录接口，不进行 Cross-Distillation；Charter 的 Register、Meaning Lock、Mode、Severity 与 Handoff 是公共护栏，不归因于老舍。

## 时代、地域与网络语言护栏

- Style Imitation Risk：HIGH。
- Modernity Risk：HIGH。
- 具体历史词语、北京地域语言、儿化、称谓、社会交往方式、幽默与节奏全部禁止继承。
- 方法必须适用于 2026 普通话、网络聊天、职场、家庭、年轻人关系、城市日常和 AI 漫剧对白。
- 本轮不建立网络梗数据库。网络词的角色/关系/场景/目的适配归本模块；2026 流行度归未来 Contemporary Language Layer。

## 证据协议

重新打开候选审计中的 4 份核心本人材料：

- LS-01《我怎样写小说》；
- LS-02《我的“话”》；
- LS-03《我怎样学习语言》；
- LS-04《谈一谈文学语言的问题》。

每份记录实际题名、作者身份、载体、URL、日期、可访问性、可直接支持范围和不可外推边界。建立唯一 Evidence Ledger。所有主要方法逐项标记：

- `SOURCE-SUPPORTED`
- `SYNTHESIZED INFERENCE`
- `AI FILM STUDIO SYNTHESIS`

不得把 Studio 扩展、现代情境清单、R1–R8、QA/Rewrite、Meaning Lock、Severity、网络流行度或 2026 语料归因于老舍。

## 女娲执行约束

必须实际调用 `huashu-nuwa`。本轮使用其“主题化能力方法论蒸馏”变体，不生成人物扮演 Skill，不提取表达 DNA，不进行文风测试。证据不足时保留限制，不编造引语或创作观点。

## Staging 必备章节

至少包含：蒸馏目标、核心判断原则、Character-Specific Speech、Situation-Specific Speech、Speech Purpose、Information Ownership、Natural Incompleteness、Subtext Awareness、Anti-Exposition Dialogue、Perfectly Articulate Emotion、Occupation / Social Position、Address Check、与叶圣陶 / 汪曾祺边界、QA MODE、REWRITE MODE、工作流程、诊断问题、失败模式、修正方法、禁止继承、可 Skill 化规则、证据与来源、Codex 审核结论。

所有实质方法按 `HARD CONSTRAINT / DEFAULT HEURISTIC / CONDITIONAL METHOD / OPTIONAL TOOL` 分类。

## TEST A｜作者借人物说话

22 岁便利店夜班员工对同事说：“这个城市的本质，是通过消费和劳动不断重新定义普通人的价值。”QA MODE；检查 Character / Relationship / Situation / Purpose、Abstract Density 与 Author Voice Leakage；有思想不自动通过。

## TEST B｜熟人百科解释

一起长大的兄妹。哥哥说：“你还记得吗？我们十年前父亲去世以后，母亲独自把我们养大，所以你一直特别依赖她。”检查共享知识、当前目的、为何现在重提及真实沟通动作，不能只说“双方都知道”。

## TEST C｜Perfect Emotion

女主刚发现恋人长期撒谎：“我现在的愤怒其实不是因为你骗我，而是因为你的行为触发了我过去被抛弃的恐惧。”检查高压时刻的自知、承认意愿、语言能力和必要性；保留特定人物可能合格的条件。

## TEST D｜职业刻板印象

急诊医生：A 使用大量专业术语，B 对朋友说普通话。不得默认 A 更符合职业；按 Receiver、Purpose、Context 判断。

## TEST E｜关系改变语言

同一意思“你今天别去了”分别由朋友、直属上司、刚分手恋人说。分析语言行为与隐含目的差异，但不机械生成固定模板。

## TEST F｜自然不完整

吵架后：“我不是那个意思。算了，你先走吧。”允许 `LEVEL 0 / KEEP / NO CHANGE`；不得强制补全解释。

## TEST G｜假口语

“就是吧，我其实怎么说呢，就是感觉吧，我们这个关系它其实有一种结构性的问题。”不得因填充词判自然；检查信息骨架和 AI 式抽象。

## TEST H｜正常高表达角色

心理咨询专业研究生，平时强自我分析，平静时说：“我觉得我可能不是生气，是害怕你以后也会突然离开。”Character Fit + Context Fit 成立时允许 PASS。

## TEST I｜网络用语角色适配

20 岁游戏主播与 61 岁严肃企业高管均说“这波真的绷不住了”。只判断 Character / Register / Relationship / Situation / Purpose Fit；不判断 2026 流行度。

## TEST J｜作者主题泄漏

“我们所有人都以为自己在做选择，其实只是系统提前规定了我们可以选择什么。”检查人物的知识、动机、语言能力、Receiver 与当前谈话目的。

## TEST K｜同义不同人物

同一事实“我知道你昨天没回家”由母亲、同事、恋人、警察表达。验证关系、权限与目的如何改变语言策略；不以生成精彩对白为目标。

## TEST L｜NO CHANGE

合理关系与语境中的“你昨晚去哪了？”必须允许 `LEVEL 0 / KEEP / NO CHANGE`，不得为了人物性格硬改花哨。

## Codex 审核门

逐项检查 10 个核心模块、网络语言边界、NO CHANGE、非地域/非时代模仿、与前两位独立性和 TEST A–L。另检查输入→判断→决策→输出、QA/Rewrite 权限、LEVEL 0–5、Role Handoff、非机械化、证据分层和所有条件例外。

失败则定位 → 定向返工 → 只重跑受影响测试 → 再审核。审核未通过不得发布。

## 发布条件

审核 PASS 后设置：

```yaml
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 老舍
domain: Language & Voice QA
```

必须先通过现有发布脚本 dry-run，再正式发布至：

`02_DISTILLATION/语言与表达研究/老舍｜Language & Voice QA 能力蒸馏 V0.1.md`

确认正式文件、`runtime/_PUBLISHED/<YYYY-MM-DD>/`、工作日志和零 blocker 后立即停止。
