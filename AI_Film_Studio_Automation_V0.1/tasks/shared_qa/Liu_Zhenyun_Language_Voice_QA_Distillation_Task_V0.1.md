---
type: distillation-task
status: completed
version: 0.1
subject: 刘震云
domain: Language & Voice QA
target_capability: Everyday Social Communication Judgment
---

# 刘震云｜Language & Voice QA 单人能力蒸馏任务 V0.1

## 任务边界

本轮只完成五人单人蒸馏 5/5：刘震云，目标是 `Everyday Social Communication Judgment`。完成后立即停止；不得开始五人 Cross-Distillation、Capability Model、Language & Voice QA Skill、Runtime、Contemporary Language Layer 或 Scene Writer。

禁止模仿刘震云文风、幽默、地域语言、特定小说对白、人物或作品表达；禁止把错位、沉默、答非所问、生活小事、低沟通效率或荒诞感做成跨场景配额。

## 管线与前置

严格执行：

`Codex → 证据准备 → huashu-nuwa → runtime/_STAGING → Codex 独立审核 → 必要的定向返工 → publish_to_obsidian.py → Vault / _PUBLISHED / 工作日志 → STOP`

必须读取并遵守：`AGENTS.md`、`PUBLISH_RULES.md`、`studio.config.json`、Language & Voice QA Capability Charter、蒸馏对象选择审计，以及叶圣陶、汪曾祺、老舍、余光中四份已批准正式档。必须完整读取并实际调用 `C:\Users\布朗熊\.codex\skills\nuwa-skill\SKILL.md`（Skill：`huashu-nuwa`）。

未审核结果只能写入：

`runtime/_STAGING/Liu_Zhenyun_Language_Voice_QA_Distillation_V0.1.md`

## 核心能力模块

1. **Receiver Matters**：`SPEAKER → RECEIVER → RELATIONSHIP → PURPOSE → SPEECH FORM`；判断接收者如何改变信息量、直接度、解释、回避、隐瞒或沉默，而非建立固定话术。
2. **Communication Is Not Transmission**：`INTENDED MESSAGE → SPOKEN MESSAGE → RECEIVED MESSAGE → RESPONSE` 四层允许不同；不得强制误解。
3. **Misalignment**：检查利益、信息、注意点、面子、恐惧、社会位置、不愿承认与解释差异；识别 AI 式过度配合，但答非所问不是自动错误。
4. **Silence as Response**：不回应、转题、结束谈话、动作代答只在人物有理由时成立；属于 `CONDITIONAL METHOD`，不是高级技巧配额。
5. **Speech and Social Position**：判断关系权力、风险和所求如何改变沟通策略；不得从职业/身份直接生成语言模板。
6. **Ordinary Motives**：检查现场是否有小而具体的沟通动机；小动机不天然比理想、自省或大目标真实。
7. **Everyday Detail Anchoring**：检查关系是否通过实际事情、东西、时间、地点、钱、工作等发生；不得设置物件或日常细节配额。
8. **Self-Interpretation Gap**：`ACTUAL STATE ≠ SELF-EXPLANATION` 可条件成立；不得强迫人物永远不了解自己，或由 QA 把“真实心理”写进台词。
9. **Conversation Memory / State**：检查前文拒绝、回避、情绪、控制权和未回答问题是否影响后文；这是 QA，不是场景设计。
10. **Social Plausibility**：判断是否像有各自注意力、关系历史与社会风险的人在交流，而非两个模型协作传输信息。

## 与其他能力边界

- 老舍：`SPEAKER FIT`——这个人物在此情境下会不会这样说。
- 刘震云：`INTERACTION FIT`——这两个人是否真的会这样交流。
- 叶圣陶：Meaning / Accuracy / Editing。
- 汪曾祺：Naturalness / Anti-Overwriting。
- 余光中：Translation-like Structure。

只记录接口，不提前融合。Register、Meaning Lock、QA/Rewrite、Severity、NO CHANGE、Handoff、Conversation State 与完整运行协议如属 Charter 或项目扩展，必须标 `AI FILM STUDIO SYNTHESIS`。

## Contemporary Language 边界

本模块只能判断某个网络表达是否符合人物、关系、场景和沟通目的，不判断其在 2026 的实时流行度。需要流行度、平台或地区语料时，输出 `HANDOFF: Contemporary Language Layer`，不得启动该层或凭直觉裁决。

## 证据协议

重新打开候选审计中的 LZY-01、LZY-02、LZY-03；允许补充高质量、公开可核验的本人访谈、演讲或创作谈。每份记录题名、本人身份、载体、日期、URL、访问状态、可直接支持范围和不可外推边界。

所有主要主张逐项标记：

- `SOURCE-SUPPORTED`
- `SYNTHESIZED INFERENCE`
- `AI FILM STUDIO SYNTHESIS`

不得把刘震云未提出的 Receiver 五段式、Transmission 四段式、Self-Interpretation Gap、Conversation State、R1–R8、状态码、QA/Rewrite 或 Runtime 规则写成其原始方法。核心结论不得由二手材料单独承载。

## 女娲执行约束

实际调用 `huashu-nuwa` 的主题化能力方法论蒸馏流程，不生成人物扮演 Skill，不提取表达 DNA，不做文风模仿。保留来源张力、反例、适用条件与置信度。输出方法必须形成 `Input → Judgment → Decision → Output`。

## Staging 必备章节

至少包含：蒸馏目标、核心判断原则、Receiver Matters、Communication Is Not Transmission、Misalignment、Silence as Response、Social Position、Ordinary Motives、Everyday Detail Anchoring、Self-Interpretation Gap、Conversation Memory、Social Plausibility、与老舍边界、与前三位能力边界、Contemporary Language 边界、QA MODE、REWRITE MODE、工作流程、诊断问题、失败模式、修正方法、禁止继承、可 Skill 化规则、证据与来源、Codex 审核结论。

所有实质方法按 `HARD CONSTRAINT / DEFAULT HEURISTIC / CONDITIONAL METHOD / OPTIONAL TOOL` 分类。

## 测试矩阵 A–O

- **A｜AI 高质量沟通**：三年恋爱争吵；A 说被忽视，B 给出过度准确的共情解释。检查关系状态、接收者、压力、回应精度与 AI Cooperation；专业训练/特殊人物是条件例外。
- **B｜现实错位**：A 问昨天为何没回来，B 问冰箱是否有菜。无上下文时 `NEEDS CONTEXT`；不得脑补逃避或自动判坏。
- **C｜沉默**：A 问是否早已知道，B 沉默并推回钥匙。判断动作是否构成回应，不解释完整内心。
- **D｜生活小事承载关系**：紧张夫妻的抽象信任句与“本周第三次晚回”比较；按人物、Register、目的判断，不默认后者优越。
- **E｜Self-Interpretation Gap**：嫉妒者说“我只是觉得他不靠谱”；允许有限自知，不把真实心理写进对白。
- **F｜正常明确沟通**：同事询问明天下午三点会议，回答“可以”；应 `LEVEL 0 / KEEP / NO CHANGE`。
- **G｜所有人都懂主题**：三人连续共同总结系统认可、身份与价值机制；识别 `AUTHORIAL COLLABORATION` 风险。
- **H｜社会位置**：普通员工指出领导数据错误；直接说与缓冲说法均非自动胜者，取决于关系、风险、性格、组织环境。
- **I｜网络用语**：年轻角色说“今天班味有点重”；只判人物/关系/场景适配，流行度 Handoff。
- **J｜Conversation Memory**：原创六轮对话，第 2 轮回避，第 5 轮重提；检查整段是否记住状态，不只逐句检查。
- **K｜普通小动机**：创伤式解释与“怕你知道又要吵”比较；不机械选择后者，检查自省能力与目的。
- **L｜接收者改变说法**：同一“我没钱了”分别面对母亲、一般同事、银行职员、亲近朋友；分析信息变化，不建立四套模板。
- **M｜真实但低效**：含重复、停顿、非直接回答但关系真实；不得以最大信息效率为目标。
- **N｜AI 假生活化**：47 岁严肃法务主管在正式会议使用高密网络口语；识别 Register/人物失配，不裁决梗新旧。
- **O｜NO CHANGE**：朋友问“你吃了吗？”答“还没。”在合理日常语境必须允许 `NO CHANGE`。

## 综合边界测试

输入：“他必须在服从规则和保住一个具体的人之间选择。”

- R1 Showrunner 创作讨论：刘震云模块只看是否存在现实沟通对象与互动任务，不接管主题/结构判断。
- R4 人物对白：重点检查现实人物是否会对当前 Receiver 如此完整地概括处境。

不得接管汪曾祺 Anti-Rhetoric、余光中 Syntax、叶圣陶 Meaning 或老舍 Speaker Fit 的全部职责。

## Codex 独立审核门

至少审核：Receiver 是否进入模型；Communication ≠ Transmission 是否成立；Misalignment / Silence / Everyday Detail 是否反机械化；Social Position、Ordinary Motive、Self-Interpretation Gap、Conversation Memory、Social Plausibility 是否可执行；与老舍及其他三位是否独立；是否误追求低效率或把生活化等同网络口语；是否支持 NO CHANGE；Contemporary Layer 边界；TEST A–O 与综合测试；证据分层；Input → Judgment → Decision → Output；QA/Rewrite 权限；Meaning 与 Role Handoff；Cross-Distillation 价值。

失败则：定位 → 定向返工 → 只重跑受影响测试 → 再审核。未通过不得发布。

## 发布条件

审核 PASS 后设置：

```yaml
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 刘震云
domain: Language & Voice QA
```

必须先用现有发布脚本 dry-run，再正式发布至：

`02_DISTILLATION/语言与表达研究/刘震云｜Language & Voice QA 能力蒸馏 V0.1.md`

确认正式文件、`runtime/_PUBLISHED/<YYYY-MM-DD>/`、工作日志和零 blocker 后立即停止。
