# AI Film Studio V0.1 — Language & Voice QA Capability Charter 任务书

## 任务定位

本任务在 Scene Writer 启动前，为 AI Film Studio 建立跨岗位共用的 `Shared QA Layer` 章程。交付物是能力边界、判断协议、未来能力槽与测试计划，不是最终 QA Skill，也不是第七个创作岗位。

本轮由 Codex 负责范围控制、章程编写与独立审核。禁止调用 `huashu-nuwa`，禁止选择或蒸馏人物，禁止建立交叉蒸馏、能力模型或运行时实现。

## 已知状态与冻结边界

- Showrunner：`PRODUCTION READY / LOCKED`，不得修改 canonical、installed Skill、Capability Model、Runtime 或 hash。
- Scene Writer：`NOT STARTED`，本任务不得启动其研究、蒸馏、Skill 或正式剧本开发。
- Obsidian Vault：只允许新增本任务指定的 Shared QA 章程；不得修改既有正史。
- Automation：只允许新增本任务书；不得修改现有管线架构或 runtime。

## 必须交付

### Obsidian 正式章程

`AI_Film_Studio_Obsidian_Vault_V0.1/01_SKILLS/Shared_QA/Language & Voice QA｜Capability Charter V0.1.md`

章程必须明确：

1. Shared QA 的层级位置、职责与非职责。
2. “语境适配的自然中文”目标，以及 `Natural ≠ Colloquial / Short / Casual / No Abstraction`。
3. 八类 `TEXT REGISTER` 及差异化判断。
4. 至少十八类 AI-pattern 问题，但不得形成词语黑名单。
5. `MEANING PRESERVATION CHECK` 的八类受保护信息。
6. 默认 `QA MODE` 与显式授权才启用的 `REWRITE MODE`。
7. `LEVEL 0–5` 严重度及处置门槛。
8. `Naturalness Judgment`、`TERM PLAUSIBILITY CHECK`、`THEME LANGUAGE CHECK`。
9. Character Dialogue、Scene Writer、Character & Acting 的边界。
10. 未来 Runtime 接口及内容问题回传机制。
11. 至少六个 `DISTILLATION CAPABILITY SLOTS`。
12. 未来 4–5 位互补对象的选人标准，但本轮不得列出候选人。
13. TEST A–J 十类原创测试的目的和通过条件。
14. 可执行输入、判断、输出、Warning、Block/Handoff 协议。

### Automation 任务书

`AI_Film_Studio_Automation_V0.1/tasks/shared_qa/Language_Voice_QA_Capability_Charter_Task_V0.1.md`

本文件即为任务书。它只定义本轮范围、交付物、审核门与停止条件，不创建运行时实现。

## 核心判断原则

### 语境优先

语言是否自然必须结合：`WHO + TO WHOM + WHY + REGISTER + INFORMATION NEED + ABSTRACTION LEVEL + SOCIAL PLAUSIBILITY`。同一句式在一种 Register 中可能合理，在另一种 Register 中可能过度。

### 意义优先

任何自然化建议或改写不得静默改变 Story Fact、Character Intent、Canon、Causal Relationship、Theme Direction、Information Reveal、Power Relationship 或 Emotional State。存在改变风险时必须 Warning；无法确认时不得生成确定性改写。

### 诊断先于改写

默认只报告问题、严重度、理由和建议。只有用户明确请求自然化、去 AI 味或改写时，才可进入 Rewrite Mode；改写后必须逐项复核意义。

### 非机械化

问题判断依赖 `Frequency + Context + Register + Intent`。不得根据单个词、句式或抽象程度自动判错，不得把全部文本强制改成口语、短句或低修辞。

### 岗位边界

Shared QA 只判断语言呈现质量。它不得重做故事结构、人物弧、镜头、表演、制作规模或 Canon；发现内容层问题时，标记并回传对应创作岗位。

## 审核门

Codex 必须逐项确认：

1. 未把 QA 错误定义为文学润色器。
2. 未把 QA 错误等同于语法检查器。
3. 八类 Register 均有不同判断边界。
4. Meaning Preservation 可执行且优先级足够高。
5. QA / Rewrite 双模式与触发条件明确。
6. AI-pattern 分类至少十八类并可诊断。
7. 无简单黑名单或固定数值规则。
8. 伪术语具有社会使用合理性检查。
9. 主题表达允许早期不确定与隐性探索。
10. Trailer Copy 依 Register 判断，不被一概禁止。
11. 能检测不自然对白，同时保护正常对白。
12. 不替代 Scene Writer。
13. 不替代 Character & Acting。
14. 不修改 Story Logic 或 Canon。
15. 能反向定义未来蒸馏对象所需的互补能力与证据门槛。

任何一项失败，章程保持 `draft/pending`，不得报告 PASS。全部通过后可将章程 frontmatter 设置为：

```yaml
type: capability-charter
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA
```

## 完成与停止条件

完成两个指定文件、十五项审核、数量校验及冻结边界复核后立即停止。本轮不得自动：

- 选择蒸馏人物；
- 调用 `huashu-nuwa`；
- 创建 Cross-Distillation、Capability Model 或 QA Skill；
- 修改 Runtime；
- 开始 Scene Writer 或正式剧本开发。

