---
type: distillation
status: approved
review_result: passed
version: 0.1
subject: 汪曾祺
domain: Language & Voice QA
capability: Natural Chinese Judgment
module: Natural Chinese Judgment
skill_executor: huashu-nuwa
source_count: 3
firsthand_ratio: 100%
---

# 汪曾祺｜Language & Voice QA 能力蒸馏 V0.1

> 本稿只蒸馏“自然中文判断”能力，不继承汪曾祺的个人文风、时代措辞、地域腔调、文学人格或作品表面风格。

## 蒸馏目标

建立一个可执行的 Natural Chinese Judgment：判断一段中文在指定 Register、上下文与生产任务中，是否让意义自然抵达读者，是否出现过写、空泛修辞、抽象跳跃、假口语或局部漂亮但整体失真的问题。

输入：文本、上下文、Register、模式（QA / REWRITE）、必须保留的意义与事实。  
判断：意义是否成立，形式是否服务意义，实际效果是否符合任务。  
决策：先定 `LEVEL 0–5`，再给对应 Gate Decision：`KEEP / PASS / PASS WITH NOTES / RETURN FOR LANGUAGE REVISION / ROLE HANDOFF / BLOCKED`。  
输出：问题位置、实际效果、证据、LEVEL 0–5 与最小修正方向；只有 REWRITE MODE 才给改写稿。

## 核心判断原则

1. **语言即意义的一部分**  
   `HARD CONSTRAINT｜SOURCE-SUPPORTED：WZQ-01、WZQ-02`  
   不把语言当作可任意替换的包装。修改词序、抽象度、语气或节奏前，先判断它们是否正在承载事实、关系、人物态度或叙事压力。

2. **先判 Register 与上下文，再判“自然”**  
   `HARD CONSTRAINT｜SOURCE-SUPPORTED：WZQ-02；运行转译为 AI FILM STUDIO SYNTHESIS`  
   同一句话在 R1 Creative Discussion 与 R8 Marketing Copy 中可能有不同结论。不得把“像日常聊天”设成全局自然度标准。

3. **整体关系高于孤句漂亮**  
   `DEFAULT HEURISTIC｜SOURCE-SUPPORTED：WZQ-01、WZQ-02`  
   先看句子在段落中的任务和前后关系，再看单句。一个孤立句普通，并不等于整段无力；一个孤立句漂亮，也不等于整段有效。

4. **具体承载抽象，但不禁绝抽象**  
   `DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE：WZQ-02、WZQ-03`  
   当抽象判断没有事实、行动、关系或可验证对象承载时，要求补锚；当抽象术语正准确完成 Project Brief 或 Production Note，则保留。

5. **修正收益必须大于意义与语域风险**  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`  
   只有问题真实存在、修正针对该问题、保护项仍被保留、改后不更假且收益大于风险时，才进入改写。

6. **非机械化**  
   `HARD CONSTRAINT｜SOURCE-SUPPORTED 基础：WZQ-01（非固定句长）、WZQ-03（地方语言非机械绑定、作品不可任意扩缩）；运行护栏为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`  
   不设置句长、短句、口语词、修辞、地方词或抽象词的固定配额；不因“文学感”自动偏好历史表达。后两项是现代项目护栏，不伪写成作者原规则。

## Language as Meaning

`HARD CONSTRAINT｜SOURCE-SUPPORTED 原则：WZQ-01、WZQ-02；下列现代意义维度为 AI FILM STUDIO SYNTHESIS`

检查语言形式是否正在改变以下任一项：

- 事实边界；
- 因果强度；
- 谁承担选择或责任；
- 人物与组织之间的权力关系；
- 语气、距离和可信度；
- 主题被读者发现的时机。

若删掉“看起来多余”的形式会改变上述任一项，它就不是纯装饰。反之，若形式只重复已知结论、抬高意义或模拟深刻，则进入 Anti-Overwriting 检查。

## Natural Flow

`DEFAULT HEURISTIC｜SOURCE-SUPPORTED：WZQ-01、WZQ-02；检查流程为 SYNTHESIZED INFERENCE`

自然流动不是统一短句，而是信息、动作、关系和语气之间有连续的接力：

1. 每句是否接住前句已经建立的对象；
2. 新概念是否有进入句，不突然跨层；
3. 句长变化是否服从信息负载；
4. 转折词是否对应真实转折；
5. 段末结论是否由段内材料推出。

口头感可用，但未经组织的停顿词、兜圈和含混不因“像人在说话”而自动自然。

## Anti-Overwriting

`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE：WZQ-01、WZQ-02`

命中下列现象时，先标记实际损失，不立即删改：

- 已经说清的事实又被抽象总结一次；
- 一个局部动作被升级为宏大价值判断；
- 同义名词连续叠加，却没有新增对象、因果或决策；
- 为显得完整而补入没有证据的心理、主题或后果；
- 句子比当前任务承担了更多意义。

**收益门**（五项同向检查）：

1. 原文是否存在可定位的问题？
2. 修正是否确实解决该问题？
3. 必须保留的意义、事实、语气和 Register 是否仍在？
4. 改后是否避免更假、更空或更像模板？
5. 修正收益是否大于意义漂移与声音损失风险？

五项不能同时成立时，输出 `NO CHANGE`、注释或多个候选，不强改。

## Anti-Rhetoric

`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE：WZQ-02`

修辞不是错误。只有当修辞替代了需要交付的事实、因果、选择或动作时才告警。先执行 `Frequency + Context + Register + Intent / Necessity` 四因子门：出现频率是否造成累积效果、上下文是否已完成同一任务、当前 Register 是否容纳该修辞、它在此处是否有必要且符合表达意图。再检查：

- 对偶是否制造了原本不存在的二元对立；
- 反问是否把未论证的结论伪装成共识；
- 排比是否重复同一空义；
- “真正重要的是”“这不仅是”是否提前替读者宣布主题；
- 华丽形容是否遮蔽人物、对象或任务。

Marketing Copy 可以容纳压缩和张力，但仍需事实可兑现；Project Brief 可以抽象，但必须指向实际决策。

## Concrete Before Abstract

`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE：WZQ-02、WZQ-03`

当句子提出主题、价值、系统性判断或人物认识时，追问它由什么承载：

- 可观察事实；
- 人物行动与选择；
- 关系变化；
- 制度规则及其后果；
- 具体对象、地点或时间；
- 可执行的项目决策。

若当前文本只是标题、Brief、日志或营销文案，允许压缩；若正文正在建立戏剧事实，不用总结句替代具体推进。

## Restraint

`DEFAULT HEURISTIC｜SOURCE-SUPPORTED 基础：WZQ-02（态度/意义宜进入叙述关系）；下列编辑优先次序与收益门为 AI FILM STUDIO SYNTHESIS`

克制不是冷淡、短句或留白配额，而是让已有事实承担其应有重量。优先次序：

1. 保留已经工作的原句；
2. 删除重复解释，而不是删除核心事实；
3. 降低无证据的意义强度；
4. 必须改时做最小改动；
5. 只有用户授权 REWRITE 且局部修正不足，才做结构性重写。

## Whole-Context Judgment

`HARD CONSTRAINT｜SOURCE-SUPPORTED：WZQ-01、WZQ-02；运行流程为 SYNTHESIZED INFERENCE`

不得只截取“金句”判断。每次至少确认：

- 这段在当前文档中的任务；
- 前文已经建立什么；
- 后文需要接收什么；
- 说话者/文档所有者是谁；
- 当前 Register；
- 若移除或改写，局部与整体各改变什么。

上下文不足时可以指出局部风险，但不得把条件性判断写成确定结论。

## Ordinary Words

`CONDITIONAL METHOD｜SOURCE-SUPPORTED 基础：WZQ-02（普通词可在准确关系与生活印象中产生新意）；下列适用条件为 SYNTHESIZED INFERENCE / AI FILM STUDIO SYNTHESIS`

普通词的价值来自准确关系和具体经验，不来自“普通”本身。适用条件：

- 用户需要降低无效装饰；
- 现有专业词没有承担精确任务；
- 普通说法能保留全部必要意义；
- 改后仍符合 Register。

不适用：术语本身是项目协议、Production Note 需要精确名词、Marketing Copy 需要可识别命名，或简化会损失责任/因果边界。

## 与叶圣陶能力边界

- **叶圣陶模块**：意义锁定、修改理由、多案比较、读者与用途、修改权限；回答“能不能改、改后是否仍是原意”。
- **汪曾祺模块**：语言形式的实际效果、整体流动、具体承载、过写与克制；回答“这句话在这里是否自然地工作”。
- **未来组合接口**：汪模块可提出问题与候选方向，叶模块可复核意义保全与修改理由；两者不构成当前运行的强制依赖。
- **公共护栏**：Meaning Lock、Mode、Register、Severity 属于 Language & Voice QA Charter / AI Film Studio 的公共运行协议，不归因于任一候选人。
- **禁止融合**：本稿不重述叶圣陶完整框架，不把 `NO CHANGE`、R1-R8、QA/REWRITE 状态码归因于汪曾祺。

## QA MODE 应用

`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

QA MODE 只诊断，不替用户重写。固定输出顺序：

1. `Mode: QA`；
2. `Register`；
3. `Context Confidence`；
4. `Original`；
5. `Problem Type`；
6. `Severity: LEVEL 0–5`；
7. `Why`；
8. `Meaning Warning: NONE / DETAILS`；
9. `Recommendation`（不用完整替代文本）；
10. `Role Handoff: NONE / ROLE + REASON`。

Severity 映射：`LEVEL 0 = KEEP`；`LEVEL 1 = 可选建议`；`LEVEL 2 = PASS WITH NOTES / 定向修改建议`；`LEVEL 3 = RETURN FOR LANGUAGE REVISION`；`LEVEL 4 = ROLE HANDOFF / WARNING`；`LEVEL 5 = BLOCKED`。Severity 不按词数或命中数量机械累加。

如果原文已经满足任务，明确输出 `PASS / NO CHANGE`，不得为了展示能力而制造修改。

## REWRITE MODE 应用

`HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`

先完成 Meaning Lock，再给改写：

- 保留事实、因果、责任主体、人物关系、语气与 Register；
- 标明无法从输入确认的假设；
- 优先最小改写；
- 需要不同抽象度时并列候选，并说明差异；
- 改写后逐项回查是否增添、删除或强化原意。

## 工作流程

`DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE；模式与权限为 AI FILM STUDIO SYNTHESIS`

1. **Context Intake**：识别文档类型、上下文、R1-R8、QA/REWRITE、保护项。
2. **Meaning Lock**：列出事实、因果、主体、关系、语气和不可添加内容。
3. **Whole Check**：判断该段的任务、信息接力和段末落点。
4. **Effect Check**：依次检查 Overwriting、Rhetoric、Abstract Jump、Concrete Anchor、Fake Casualness、Register。
5. **Severity**：依据 `LEVEL 0–5` 判断，再映射为 `KEEP / PASS / PASS WITH NOTES / RETURN FOR LANGUAGE REVISION / ROLE HANDOFF / BLOCKED`；不按问题数量机械判级。
6. **Decision**：QA 只给诊断；REWRITE 通过收益门后给最小候选。
7. **Regression Check**：回查意义、事实、语气、现代性和上下文连续性。

## 诊断问题

`OPTIONAL TOOL｜SYNTHESIZED INFERENCE`

1. 这句话在当前文档里具体要完成什么？
2. 删除形容、总结或修辞后，事实与因果是否更清楚，还是意义被削弱？
3. 抽象概念由哪个事实、行动、关系或决策承载？
4. 这是真转折，还是连接词制造的转折？
5. 句子是否替人物/读者过早说出了主题？
6. 口语词是在传递人物状态，还是掩盖信息不足？
7. 专业词能否指出明确对象、动作、负责人或验收标准？若不能，是否为伪术语/空壳词？
8. 单句修改会不会破坏段落的接力、距离或声音？
9. 改写是否只是更像某位作家，而非更适合当前项目？
10. 原文是否已经工作，最正确的决定是否是 `NO CHANGE`？

## 失败模式

1. **自然 = 口语化**：把严谨 Brief 改成聊天语气。
2. **自然 = 短句化**：把复杂因果拆碎，失去责任关系。
3. **具体 = 堆细节**：添加没有来源的场景或心理。
4. **克制 = 删意义**：删掉必要限定、风险或人物态度。
5. **反修辞 = 禁修辞**：忽略 Marketing Copy 或人物语言的正当功能。
6. **普通词 = 反专业**：把精确项目术语改成含混日常词。
7. **烟火气 = 地域腔调**：复制方言、生活趣味或时代气息。
8. **整体判断 = 不做局部定位**：只说“整体不自然”，不给证据。
9. **QA 越权**：未获授权便直接重写。
10. **伪术语泛化**：因自己不熟悉就把合法专业词判为伪术语。

## 修正方法

1. 对假口语：删停顿填充词，恢复明确主体、动作和因果；不必改成书面腔。  
   `DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
2. 对抽象跳跃：补回已有事实锚，或把总结延后；不虚构新细节。  
   `DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
3. 对名词堆叠：追问每个名词对应的对象、动作、负责人或结果，删除无新增信息者。  
   `CONDITIONAL METHOD｜AI FILM STUDIO SYNTHESIS`
4. 对过早主题：保留事实/行动，把主题改为待验证问题或移至适合的总结层。  
   `DEFAULT HEURISTIC｜SYNTHESIZED INFERENCE`
5. 对局部漂亮、整体断裂：恢复指代与信息接力，不追求单句独立成章。  
   `DEFAULT HEURISTIC｜SOURCE-SUPPORTED：WZQ-01、WZQ-02`
6. 对合法专业表达：若对象、边界和决策清楚，输出 `NO CHANGE`。  
   `HARD CONSTRAINT｜AI FILM STUDIO SYNTHESIS`
7. 对疑似伪术语：只指出“当前无法对应任务/对象/检验方式”，请求定义；不承担全局术语治理。  
   `CONDITIONAL METHOD｜AI FILM STUDIO SYNTHESIS`

## 禁止继承

以下内容不得进入未来 Language & Voice QA Skill：

- 汪曾祺的个人写作腔调、句法节奏、作品语言与文学人格；
- 其时代措辞、历史表达、乡土气质、地域词汇和生活趣味；
- “烟火气”“淡”“雅”“有味道”等不可执行风格标签；
- 固定短句、固定长短交替、固定留白或固定口语比例；
- 把古典/民间表达当作现代 2026 项目的优先形式；
- 用文学文本标准覆盖 Project Brief、Production Note、Marketing Copy 等专业 Register；
- 用作者权威代替当前项目的事实、用户意图与 Canon。

## 可 Skill 化规则

1. `HARD`：任何改写先锁定意义、Register、模式和保护项。
2. `HARD`：QA MODE 不输出替代全文；原文已工作时必须允许 `NO CHANGE`。
3. `HARD`：不得用固定句长、固定口语、固定修辞或历史文风衡量自然度。
4. `DEFAULT`：先看段落任务和信息接力，再处理孤句。
5. `DEFAULT`：抽象判断优先寻找事实、行动、关系或决策锚。
6. `DEFAULT`：过写判断必须说明它造成的实际损失。
7. `CONDITIONAL`：普通词替换只在意义无损、Register 合适且确实更准确时使用。
8. `CONDITIONAL`：疑似伪术语只做局部可解释性检查，不越权重建术语系统。
9. `OPTIONAL`：朗读可用于发现不调顺，但不能成为所有 Register 的硬门槛。
10. `OUTPUT`：Context → Meaning Lock → Whole Check → Effect Check → Decision → Regression Check。

## 证据与来源

本稿主动依赖 3 份核心材料，第一手内容 3/3（100%），二手材料不承载核心主张。完整 ID、载体边界、主张映射与不可外推项见研究目录 `00-canonical-evidence-ledger.md`。

| ID | 来源 | 用途 |
|---|---|---|
| WZQ-01 | 汪曾祺本人文本，中国作家网当前网页题名《小说里边最重要的是什么？》（注明原载 1991《写作》第 4 期） | 语言—内容不可剥离；字句段全篇关系；非机械流动 |
| WZQ-02 | 汪曾祺《“揉面”——谈语言》，高教社教材 PDF（注明选自 1993《汪曾祺文集·文论卷》） | 文学语言实际效果；整体统筹；普通词；人物/题材/Register；态度溶入叙述 |
| WZQ-03 | 汪曾祺本人自序，中国作家网当前网页题名《我的作品所包涵的是什么样的感情？》 | 具体生活锚；地域与现代性边界；形式不可机械扩缩 |

### 证据声明

- `SOURCE-SUPPORTED`：可由上述本人文本在限定范围内直接支持。
- `SYNTHESIZED INFERENCE`：Codex / 女娲基于多份材料形成的能力归纳，不是汪曾祺原话。
- `AI FILM STUDIO SYNTHESIS`：为本项目生产流程建立的模式、状态码、Register、Severity、Meaning Lock 与测试协议。
- 未使用二手总结单独支撑任何核心方法；转载和节选的载体边界已保留。

## Codex 审核结论

最终状态：`PASS`。

- 证据红队：PASS。3/3 第一手内容口径、载体边界、来源实际题名及直接支持/综合推断/项目合成分层均通过。
- 内容边界审核：PASS。21 个必备章节、Natural Chinese Judgment 定位、与叶圣陶独立性、风格禁继承、现代性与 Charter 输出契约均通过。
- 可执行性干跑：TEST A-J 全部 PASS；E/F/H 正确输出 `LEVEL 0 / NO CHANGE`，C 形成跨 Register 不同结论，B 保留 Meaning Warning 与 Role Handoff，J 不偏好历史文学表达。
- 返工：2 轮定向返工。第一轮修正证据元数据/分层、QA 固定字段、规则分类与测试精度；第二轮统一 LEVEL 0–5 与 Gate Decision。
- 未解决阻塞：0。
- 发布决定：允许通过现有 `publish_to_obsidian.py` 受控发布。

## Codex 可执行性测试 A-J（首轮）

### TEST A｜抽象密度与过早主题

输入：“当一切善意都必须被系统计分，一个人还会不会去帮助那些没有奖励价值的人？”  
Register：R1 Creative Discussion；Mode：QA。

- 判定：`LEVEL 2 / PASS WITH NOTES`。
- 抽象密度：善意、系统计分、奖励价值连续出现，但问题对象仍可识别。
- 修辞：主题式设问内嵌“善意被系统计分”的价值前提，可能过早规定项目的道德问题；它不是天然错误。
- 具体锚：缺少谁被计分、帮助会付出什么、系统如何作用。
- Register：作为早期讨论问题可用，不宜直接当作已成立的主题结论。
- QA 权限：只建议用人物行动/制度后果验证，不提供改写稿。

### TEST B｜人工二元与两种抽象度

输入：“他必须在服从规则和保住一个具体的人之间选择。”  
Mode：先 QA，后 REWRITE。

- QA：`LEVEL 4 / MEANING WARNING + ROLE HANDOFF TO SHOWRUNNER`。句子声称二者互斥，但输入没有说明规则为何会伤害此人，也没有证明不存在第三路径。语言层不能替上游降强度或修故事逻辑，需要补足实际因果。
- Meaning Lock：主体是“他”；两个方向是遵守规则 / 保护具体的人；原句断言二者必须选择；不得添加人物身份、制度内容、代价或结局。
- 改写前提：只有项目 Canon 已经证明二者确实不可兼得，才进入下列 REWRITE；否则停在 QA 并请求补因果。
- 普通讨论版：“按规则办，就保不住这个人；要保住他，就不能服从规则。他必须选一边。”
- 保留一定抽象版：“他必须在遵守规则与保住这个人之间作出选择，两者不可兼得。”
- 回查：两版都保留主体、两个选项和“必须二选一”的强度，没有添加人物身份、制度内容或结局；自然度修正不替代因果核验。

### TEST C｜同句跨 Register

输入：“寻找那个已经被全城遗忘、却仍存在于男主记忆中的人。”

- R1 Creative Discussion：`LEVEL 2 / PASS WITH NOTES`。它压缩出方向，却没有说明“遗忘”是事实、机制还是比喻，也没有给人物为何行动的因果；适合作为待展开 seed，不足以作为可执行 story decision。
- R8 Marketing Copy：`LEVEL 0 / KEEP WITH FACT CHECK`。句式具目标、反差和记忆点；若“全城遗忘”能由正片兑现，可以保留。
- 结论：相同形式的实际效果随任务不同而变化，不能给统一“自然/不自然”判词。

### TEST D｜总结跳跃

输入：“男主第二天去上班，发现同事不认识昨天出现的女孩。监控里也没有她。他开始怀疑自己的记忆。真正重要的是，这不仅是一次记忆异常，更是他对于真实、自我和系统定义之间关系的重新认识。”

- 判定：`LEVEL 2 / PASS WITH NOTES`。
- 前半判断：前三句已完成事实递进与当前 beat——异常被第二份证据加强，并推动男主怀疑自己的记忆。
- 问题：末句突然从“异常”跨到“真实、自我、系统定义”，出现总结先行、名词堆叠和意义膨胀。
- 实际效果：替人物与读者提前宣布认识，削弱前文事实承担主题的空间。
- 最小方向：若这是 R1 讨论，先标为待验证主题假设；若是正文，优先让人物下一步选择承载认识。QA 不直接重写。

### TEST E｜合法 Project Brief

输入：“这一季的核心冲突是男主逐渐失去系统权限。”  
Register：R2 Project Brief。

- 判定：`LEVEL 0 / PASS / NO CHANGE`。
- 理由：对象、时间尺度、变化方向和冲突载体都明确；抽象度符合 Brief，不因“系统权限”是专业概念而降级。

### TEST F｜合法 Production Note

输入：“本轮先验证 Series Engine 和 Character Engine，暂不进入 Scene Writer。”  
Register：R7 Production Note。

- 判定：`LEVEL 0 / PASS / NO CHANGE`。
- 理由：范围、动作与禁止进入的阶段明确；项目术语承担流程控制功能。

### TEST G｜空泛专业腔

输入：“本阶段将通过对人物关系、系统机制以及世界结构的多维度重构，进一步强化项目在持续叙事层面的核心驱动力。”

- 判定：`LEVEL 2 / PASS WITH NOTES`。
- 问题：名词堆叠、名词化和高层动作词没有说明改什么、由谁判断、如何验收；“多维度重构”“核心驱动力”当前无法对应具体决策。
- 边界：不预先命名为翻译腔或其他候选人的专属问题；这里只判断任务可解释性。
- QA 方向：要求列出本阶段实际修改对象和验收信号，不提供替代全文。

### TEST H｜普通句保持

输入：“这个人第二天没有来上班。”  
Register：R1 Creative Discussion。

- 判定：`LEVEL 0 / PASS / NO CHANGE`。
- 理由：事实、主体与时间清楚。没有上下文证明需要更生动、更多解释或文学化。

### TEST I｜假口语

输入：“说白了吧，其实这个故事就是怎么说呢，一个男的嘛，他反正就是发现系统不太对劲。”

- 判定：`LEVEL 2 / PASS WITH NOTES`。
- 问题：“说白了吧、其实、就是、怎么说呢、嘛、反正”模拟随口表达，却没有补充人物身份、发现内容、因果或行动；自然感以信息塌缩为代价。
- 方向：先要求恢复最小信息骨架（谁、发现了什么、因此做什么），不是简单把语气改得更正式。

### TEST J｜现代性护栏

同一意义：本轮先理清人物关系，再决定是否补充世界设定。

- A（2026 项目中文）：“这一轮先把人物关系理清，再决定要不要补世界设定。”
- B（刻意历史文学表达）：“此番当先厘清人物彼此之关系，继而酌定是否增补世界设定。”
- R1 / R7 判定：A `LEVEL 0 / KEEP`；B `LEVEL 3 / RETURN FOR LANGUAGE REVISION`，除非说话者设定或项目语域明确要求历史表达。
- 结论：本方法不因 B 更像旧文学表达就偏好 B；现代项目的实际用途优先于作者风格联想。
