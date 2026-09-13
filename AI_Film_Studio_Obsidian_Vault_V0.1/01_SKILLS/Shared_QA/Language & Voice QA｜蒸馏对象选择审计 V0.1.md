---
type: candidate-suitability-audit
status: approved
review_result: passed
version: 0.1
subject: Language & Voice QA Distillation Candidates
candidate_count: 7
recommended_count: 5
core_first_hand_sources: 27
---

# AI Film Studio｜Language & Voice QA 蒸馏对象选择审计 V0.1

## 审计定位

本档案依据已批准的 `Language & Voice QA｜Capability Charter V0.1`，审核 7 位候选是否能为六个能力槽提供可执行、可核验、非模仿式的方法材料，并形成未来正式蒸馏的 4–5 人组合。

本轮不是人物蒸馏。未调用 `huashu-nuwa`，未创建人物 Distillation、Cross-Distillation、Capability Model、Language & Voice QA Skill 或 Runtime 实现；Showrunner 保持锁定，Scene Writer 保持 `NOT STARTED`。

## Charter 对齐

本次选择服务六槽：

- A Natural Modern Chinese
- B Spoken Dialogue
- C Restraint
- D Editing & Syntax
- E Everyday Observation
- F Anti-Rhetoric

选择同时考虑 Charter 的 18 类 AI-pattern、Meaning Preservation、Text Register、Naturalness Judgment、Term Plausibility、Theme Language 和 Character Dialogue 边界。文学地位、作品知名度与个人文风均不构成通过理由。

## Evidence Protocol

核心一手材料限定为：本人署名文章/自序/创作谈、本人演讲或访谈记录、机构页面中能明确归属本人的直接发言。二手评论只用于导航和交叉核验，不计数量、不独立支撑候选结论。

研究总账：

`AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/Language_Voice_QA_Candidate_Audit_V0.1/00-canonical-evidence-ledger.md`

核验日期：2026-08-22。

## Evidence Readiness

|Candidate|公开可访问核心一手|主要类型|来源稳定性|正式蒸馏适配|
|---|---:|---|---|---|
|汪曾祺|3|创作谈、语言论、自序|HIGH / MEDIUM-HIGH|READY|
|老舍|4|小说创作谈、语言复盘、对白论、文学语言论|HIGH / MEDIUM-HIGH|READY|
|叶圣陶|2|写作论文章组、公开报告与本人修订附记|HIGH|READY；两份均为长材料且方法密度高|
|余光中|5|长文、长访谈、大学访谈、演讲、电话访谈|HIGH / MEDIUM|READY WITH GUARDRAILS；另有 1 份受限访谈元数据未计数|
|刘震云|3|长期访谈、大学 Q&A、2025 长访谈|HIGH|READY|
|余华|6|创作复盘、长访谈、演讲、公开对谈|HIGH|READY AS ALTERNATE|
|吕叔湘|4|本人序文、修订说明、语法修辞方法引言|HIGH / MEDIUM|READY AS ALTERNATE；1 份为合著|
|**总计**|**27**|**27/27 核心为本人材料或明确直接发言**|二手核心 0|足够支持候选选择|

代表性一手入口：

- 汪曾祺：[《小说里边最重要的是什么？》](https://www.chinawriter.com.cn/n1/2021/1024/c404032-32262629.html)、[《“揉面”——谈语言》](https://oss0.changxianggu.com/book/chapter/269_9787040514674.pdf)。
- 老舍：[《我怎样写小说》](https://www.chinawriter.com.cn/n1/2019/0521/c404032-31095340.html)、[《我怎样学习语言》](https://zh.wikisource.org/zh-hans/%E6%88%91%E6%80%8E%E6%A8%A3%E5%AD%B8%E7%BF%92%E8%AA%9E%E8%A8%80)。
- 叶圣陶：[《怎样写作》选文](https://www.chinawriter.com.cn/n1/2021/0201/c404032-32018755.html)、[1978 写作报告及修改附记](https://www.mj.org.cn/zsjg/ystyjh/yjlw/202201/t20220117_248050.htm)。
- 余光中：[《中文的常态与变态》完整转载](https://clonewith.github.io/translation/ref/improve-EC/)、[香港中文大学访谈](https://www.iso.cuhk.edu.hk/chinese/publications/newsletter/article.aspx?articleid=61461)、[中山大学演讲记录](https://news.nsysu.edu.tw/p/16-1120-141127.php?Lang=zh-tw)。
- 刘震云：[《写作向彼岸靠近》](https://www.chinawriter.com.cn/n1/2022/1118/c405057-32569482.html)、[北大师生公开对话](https://www.chinawriter.com.cn/2015/2015-06-15/245638.html)。
- 余华：[对话障碍复盘](https://www.chinawriter.com.cn/n1/2018/0813/c405057-30224176.html)、[日常语言与书面语言访谈](https://www.chinawriter.com.cn/n1/2018/0903/c405057-30268217.html)、[长期创作访谈](https://www.chinawriter.com.cn/n1/2022/1125/c405057-32574066.html)。
- 吕叔湘：[《语文常谈》序](https://www.cp.com.cn/book/7-100-01291-0_32.html)、[文集自序及修订说明](https://www.cp.com.cn/book/7-100-00860-3_41.html)、[《语法修辞讲话》引言](https://www.diancangwang.cn/xueshuzaji/4e63210e027b/6019d479757c.html)。

## Capability Coverage Matrix

等级只表示本任务证据适配，不评价文学或学术地位。

|Candidate|A|B|C|D|E|F|主要证据理由|
|---|---|---|---|---|---|---|---|
|汪曾祺|PRIMARY|LIMITED|PRIMARY|SECONDARY|SECONDARY|PRIMARY|字—句—段流动、加工口语、暗示与整体关系；防止 QA 退化为孤立换词|
|老舍|SECONDARY|PRIMARY|SECONDARY|LIMITED|PRIMARY|SECONDARY|人物、情境、职业、文化、目的与效果形成最明确的对白判断|
|叶圣陶|PRIMARY|LIMITED|SECONDARY|PRIMARY|SECONDARY|SECONDARY|目的—读者—初稿—理由—多案—朗读—意义复核的编辑流程|
|余光中|SECONDARY|LIMITED|SECONDARY|PRIMARY|LIMITED|PRIMARY|翻译骨架、名词化、代词/介词/连接与目标语重组的专项证据|
|刘震云|PRIMARY|SECONDARY|SECONDARY|LIMITED|PRIMARY|SECONDARY|现代生活联结、话语权、接收者、沉默、言外之意与细节适配|
|余华|SECONDARY|SECONDARY|PRIMARY|LIMITED|SECONDARY|SECONDARY|准确优先、语言随项目变化、对话失败时用叙述替代的修复方法|
|吕叔湘|SECONDARY|LIMITED|LIMITED|PRIMARY|LIMITED|SECONDARY|口/书面分层、语法诊断、标准谨慎与规则置信度|

完整逐格理由见：

`runtime/_STAGING/_research/Language_Voice_QA_Candidate_Audit_V0.1/08-capability-coverage-matrix.md`

## Individual Conclusions

### 汪曾祺｜FINAL RECOMMENDED

- Primary：A Natural Modern Chinese。
- Secondary：C Restraint、F Anti-Rhetoric。
- Needed：建立语言整体关联、加工口语和自然不等于原样口语的判断。
- Not Redundant：叶圣陶负责编辑过程，不负责语言整体流动与暗示。
- Risk：Style HIGH；Modernity MEDIUM。
- Guardrail：禁止清淡、短句、水意、乡土/饮食意象和个人语调模仿；声律与文气不能成为现代中文硬门。

### 老舍｜FINAL RECOMMENDED

- Primary：B Spoken Dialogue。
- Secondary：E Everyday Observation、F Anti-Rhetoric。
- Needed：7 人中最完整的 WHO/WHEN/WHERE/职业/文化/效果式对白判断。
- Not Redundant：刘震云补现代关系和话语权，不替代对白框架。
- Risk：Style HIGH；Modernity MEDIUM-HIGH。
- Guardrail：禁止北京话、地域词、曲艺节奏、幽默和角色模板继承；具体当代语料重新取证。

### 叶圣陶｜FINAL RECOMMENDED

- Primary：D Editing & Syntax / Meaning Preservation。
- Secondary：A Natural Modern Chinese、C Restraint。
- Needed：提供可解释的修改工作流与改前/改后意义复核。
- Not Redundant：余光中处理 Translation-like 专项，不承担完整 Meaning Gate。
- Risk：Style LOW-MEDIUM；Modernity MEDIUM。
- Guardrail：朗读是可选检查，不把专业 Brief、诊断或制作说明强制口语化、浅白化。

### 余光中｜FINAL RECOMMENDED WITH GUARDRAILS

- Primary：D Translation-like Chinese。
- Secondary：F Anti-Rhetoric、A Natural Modern Chinese。
- Needed：直接覆盖 AP-05、AP-06、AP-17，并提供跨语结构重组机制。
- Not Redundant：叶圣陶是通用编辑；余光中是跨语句法专项。
- Risk：Style HIGH；Modernity HIGH。
- Guardrail：不得建立代词、被动、介词、名词化或连接词黑名单；先检查 2026 当前用法、Register、Intent 与实际认知负担。

### 刘震云｜FINAL RECOMMENDED

- Primary：E Everyday Observation。
- Secondary：B Spoken Dialogue、A Natural Modern Chinese。
- Needed：为组合提供 2025 现代锚、谁说/谁听、沉默、言外之意与日常细节适配。
- Not Redundant：老舍给出对白机制，刘震云负责现代社会联结校准。
- Risk：Style HIGH；Modernity LOW-MEDIUM。
- Guardrail：禁止家常短句、分号、延津语言、标志性幽默或作品人格模仿。

### 余华｜ALTERNATE 1

- Primary Fit：C Restraint。
- Secondary Fit：B Spoken Dialogue、A Natural Modern Chinese。
- Strength：一手证据最多；明确复盘对白失败、叙述替代执行、准确优先和语言随项目变化。
- Why Alternate：当前 A/B/C 已由汪曾祺、老舍、刘震云覆盖；加入会增加重叠而非补空槽。
- Activation：对白失败修复、Anti-Mechanical 或语言随项目变化在正式蒸馏/测试中不足时启用。
- Risk：Style HIGH；Modernity LOW。

### 吕叔湘｜ALTERNATE 2

- Primary Fit：D Editing & Syntax（系统语法）。
- Secondary Fit：A Natural Modern Chinese。
- Strength：7 人中语言学分类、口/书面分层、规则谨慎和证据门槛最系统。
- Why Alternate：D 已由叶圣陶的编辑流程与余光中的翻译专项覆盖；第三位会造成能力过度集中。
- Activation：未来出现句法分类冲突、语法与自然度混同、规则碎片或置信度不足时启用。
- Risk：Style LOW；Modernity MEDIUM；额外风险是把 QA 降为语法检查器。

## Overlap Decisions

|Pair|结论|职责切分|
|---|---|---|
|汪曾祺 × 叶圣陶|COMPLEMENTARY|艺术语言整体判断 vs 可解释编辑检查|
|老舍 × 刘震云|CONTROLLED OVERLAP / BOTH NEEDED|人物情境对白框架 vs 现代话语权与关系联结|
|叶圣陶 × 余光中|COMPLEMENTARY|Meaning-preserving 通用修改 vs Translation-like 专项|
|余光中 × 吕叔湘|HIGH OVERLAP AT D|跨语症状更直接；系统语言学留作 Alternate|
|老舍 × 余华|OLD SHE PRIMARY / YU HUA ALTERNATE|完整对白 QA 框架 vs 对话失败替代执行|

## Style Imitation Risk Summary

|Candidate|Risk|必须切断|
|---|---|---|
|汪曾祺|HIGH|清淡文风、短句、水意、乡土/饮食意象|
|老舍|HIGH|北京口语、幽默、曲艺节奏、角色模板|
|叶圣陶|LOW-MEDIUM|所有文本浅白化、朗读/精简机械化|
|余光中|HIGH|语言纯化、反西化、文言优越、诗性配方|
|刘震云|HIGH|家常短句、分号、地域话语、标志性幽默|
|余华|HIGH|余华式简洁、冷静与苦难叙述人格|
|吕叔湘|LOW|语法正确等同自然、规范硬门|

## Modernity Risk Summary

|Candidate|Risk|2026 迁移原则|
|---|---|---|
|汪曾祺|MEDIUM|保留整体关系与社会来源，不固化声律/古典偏好|
|老舍|MEDIUM-HIGH|只迁移人物/情境/群体机制，具体词语全部当代取证|
|叶圣陶|MEDIUM|保留目的、读者、误解、朗读流程，允许专业 Register|
|余光中|HIGH|当前用法 + Register + Intent + 认知负担四门共同判断|
|刘震云|LOW-MEDIUM|以 2025 证据作现代锚，不固化个人短句审美|
|余华|LOW|只防个人创作选择泛化|
|吕叔湘|MEDIUM|当代语料复核旧规范，保留其不武断原则|

## Final Recommended Combination

1. 汪曾祺 — A/C/F：语言整体、自然中文、克制与反孤立修辞。
2. 老舍 — B/E：人物与情境驱动的真实对白。
3. 叶圣陶 — D/A：Meaning-preserving 编辑、修改理由与朗读检查。
4. 余光中 — D/F：Translation-like Chinese 与结构污染专项。
5. 刘震云 — E/B/A：现代生活语言、话语权、关系联结与社会真实感。

### Slot ownership

|Slot|Primary owner(s)|Secondary|
|---|---|---|
|A Natural Modern Chinese|汪曾祺、刘震云|叶圣陶、老舍、余光中|
|B Spoken Dialogue|老舍|刘震云|
|C Restraint|汪曾祺|叶圣陶、刘震云|
|D Editing & Syntax|叶圣陶、余光中|汪曾祺|
|E Everyday Observation|刘震云、老舍|汪曾祺、叶圣陶|
|F Anti-Rhetoric|汪曾祺、余光中|老舍、叶圣陶、刘震云|

Coverage：`6 / 6 SLOTS COVERED`。没有无主责任人的能力槽。

## Known Limits

- 公开链接稳定性不同；正式蒸馏前需重新打开并保存必要证据摘录。
- 余光中关键长文来自独立完整转载，虽有多份本人访谈交叉，正式蒸馏仍应优先补权威版本或正版文本页码。
- 叶圣陶公开核心只有 2 份，但两份均为长材料且覆盖完整修改流程；若正式蒸馏拆不出足够失败模式，再定向补本人著作。
- 现代网络中文、平台文案、行业术语与方言仍需未来原创测试和当代语料校准，不能由历史候选自动代表。
- 本审计只证明“适合进入蒸馏”，不证明未来蒸馏结果必然通过。

## Codex Audit Conclusion

Codex 最终审核：`PASS`。

|审核门|结论|核验结果|
|---|---|---|
|7 位候选同标审核|PASS|Primary 与 Alternate 均按相同一手证据、覆盖、风险和非冗余标准审核|
|核心一手数量可复算|PASS|3 + 4 + 2 + 5 + 3 + 6 + 4 = 27；受限 YGZ-02 未计入|
|来源—主张可追溯|PASS|canonical ledger 含 URL、类型、日期、槽位、主张、可访问性、可靠性与备注|
|Coverage Matrix 含理由|PASS|每格均含 PRIMARY/SECONDARY/LIMITED 与证据原因|
|五组指定重叠|PASS|全部完成，且区分互补、受控重叠和高重叠|
|Style Imitation Risk|PASS|7/7 有等级、误读与硬护栏|
|Modernity Risk|PASS|7/7 有等级与 2026 迁移门|
|最终推荐人数|PASS|5 人，符合 4–5 人要求|
|六槽覆盖|PASS|A–F 为 6/6，每槽至少一位主责任人|
|最终候选字段|PASS|均含 Primary/Secondary、Needed、Not Redundant、Readiness 与 Risk|
|Alternate 启用条件|PASS|余华与吕叔湘均有明确触发条件|
|阶段与冻结边界|PASS|未调用女娲、未创建人物蒸馏/后续模型/Skill/Runtime；Showrunner hash 未变，Scene Writer 未启动|

最终推荐：`汪曾祺 / 老舍 / 叶圣陶 / 余光中 / 刘震云`。

Alternates：`余华 / 吕叔湘`。

本审计已具备进入“用户锁定蒸馏对象”决策的条件。它不构成开始正式人物蒸馏的授权；必须等待用户明确指令：“锁定蒸馏对象并开始第一位人物蒸馏。”
