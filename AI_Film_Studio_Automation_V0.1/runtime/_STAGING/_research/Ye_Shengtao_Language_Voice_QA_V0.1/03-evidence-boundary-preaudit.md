# 叶圣陶｜Language & Voice QA 证据边界预审

## 预审范围

本预审只核对以下材料，不对蒸馏主稿或 Vault 做任何修改：

- `Language & Voice QA｜Capability Charter V0.1.md`
- `Language & Voice QA｜蒸馏对象选择审计 V0.1.md`
- `Ye_Shengtao_Language_Voice_QA_Distillation_Task_V0.1.md`
- 候选审计中的 `03-叶圣陶-evidence.md` 与 `00-canonical-evidence-ledger.md`
- YST-01：中国作家网《怎样写作》选文
- YST-02：叶圣陶研究会《端正文风——在新华社国内记者训练班的讲话》及本人附记

核验结果：YST-01 正文可直接打开；YST-02 的网页抓取接口超时，但同一官方 URL 经 HTTP 直接访问可读取全文，身份、正文、1978 年讲话日期与 1979 年附记日期均可核验。

## 两份一手材料能够直接支持的最小方法集合

1. `SOURCE-SUPPORTED`：先问作者实际要表达什么，并检查文字是否与思想、事实、目的相合。YST-01 把“想得认真”和“用相当的语言文字表达”分成两层，也明确说修改文章同时是在修正思想；YST-02 要求动笔前先考虑“告诉读者什么”以及如何避免误会。
2. `SOURCE-SUPPORTED`：语法或表面通顺不等于表达准确。YST-01 区分“通”与“好”，并以思想未明、词义不确、事实不合及句法关系错误说明表达仍可能失败。
3. `SOURCE-SUPPORTED`：修改必须说明理由。YST-02 明列事实不符、说得不准确、可能使人误会，反对只说“这个地方写得不大好”。
4. `SOURCE-SUPPORTED`：可提出两三个修改办法，经过比较再选择。YST-02 直接给出这一流程；YST-01 也说“唯一适当”未免言过其实，支持多案而非唯一答案。
5. `SOURCE-SUPPORTED`：初稿应复看，若原想法不到家，或写出的话没有针对所想，就应修改；如果“想对了，写对了”，可以一字不易。这个原则支持克制修改，但不等同于项目状态码 `NO CHANGE`。
6. `SOURCE-SUPPORTED`：朗读可用于发现不调顺、别扭或难懂之处。YST-02 还明确区分书面文章与聊天：书面文本须独立承担理解，不能依靠表情和手势。

## 拟议规则的来源边界

|拟议规则|应使用的最高证据标签|边界结论|
|---|---|---|
|`Intended Meaning → Current Expression → Mismatch`|`SOURCE-SUPPORTED`|“所想/目的”与“所写”是否切合，可由 YST-01/02 直接支持。|
|`Repair Options → Meaning Check` 的完整五段流水线|`SYNTHESIZED INFERENCE`|比较多个改法、改后复看分别有依据；把它们组装成固定五段工作流是本次蒸馏归纳，不是叶圣陶原列流程。|
|语法正确与意义准确必须分开|`SOURCE-SUPPORTED`|YST-01 的“通”与“好”、思想与表达两层直接支持。|
|指代、主体、因果、范围、程度、抽象对应、越证据断言的完整清单|`SYNTHESIZED INFERENCE`|主体误置、词义、连接关系、事实和空洞抽象有实例；七项完整检查表并非原文目录。特别是影视因果、范围/程度与越证据断言，不得逐项宣称为本人规则。|
|主干、信息顺序、修饰范围、句间关系|`SYNTHESIZED INFERENCE`|YST-01 支持词是否适合、篇章是否调顺、关系词是否称职；现代诊断字段是从这些原则抽象出来。|
|名词化、抽象名词链、翻译式中文、AI 连接词过密|`AI FILM STUDIO SYNTHESIS`|两份材料没有建立这些现代专项分类。不可借叶圣陶名义支撑；其中“空洞抽象”和连接关系不当只能提供邻近证据。|
|修改必须给理由、多案比较|`SOURCE-SUPPORTED`|YST-02 直接支持。|
|没有唯一正确改法|`SOURCE-SUPPORTED`（限原则）|YST-01 反驳“唯一适当”的绝对性，YST-02 允许两三个办法比较；仍不能推成“所有改法等价”。|
|`NO CHANGE / LEVEL 0 / KEEP`|`AI FILM STUDIO SYNTHESIS`|叶圣陶“想对了，写对了，才可以一字不易”提供相容依据；但状态码、等级和“没有收益就保持”的运行规则来自 Charter（尤其 Charter 141、161、343 行）。主稿应写“项目制度受来源原则支持”，不能标成叶氏术语。|
|Over-Editing Protection|`SYNTHESIZED INFERENCE`|来源支持有理由才改、正确则可不改、多案比较；“修改收益必须高于风险”的显式门槛是现代编辑系统归纳。|
|Read-Aloud 是一种检查工具|`SOURCE-SUPPORTED`|YST-01/02 均直接支持诵读/念读发现不调顺和听不明白。|
|Read-Aloud 必须非机械、Register-aware、卡顿不自动判错|`AI FILM STUDIO SYNTHESIS`|来源没有八类 Register，也没有“卡顿不自动失败”的规则。其“最好念一两遍”与书面/口头差异，支持把朗读降为辅助检查；但“OPTIONAL TOOL”分类和专业 Brief 豁免是项目护栏。|
|八类 Register（R1–R8）|`AI FILM STUDIO SYNTHESIS`|YST-02 只直接区分书面/口头并强调目的、读者；R1–R8 的枚举、名称、容忍度和边界全部来自 Charter（62–69 行）。|
|先判 Register 再判自然度|`AI FILM STUDIO SYNTHESIS`|与“目的/读者/书面与口头有别”相容，但顺序门与八类路由是项目能力模型。|
|Meaning Preservation 一般原则|`SOURCE-SUPPORTED`|思想、目的、事实、准确性、误解风险与表达切合均有直接材料。|
|`Meaning Lock` 八项：Story Fact / Character Intent / Canon / Causal Relationship / Theme Direction / Information Reveal / Power Relationship / Emotional State|`AI FILM STUDIO SYNTHESIS`|叶圣陶材料可直接覆盖事实、一般意图和避免误解；影视 Canon、揭示时机、权力关系、情绪状态等精细项来自 Charter 110–126 行。不得把八项说成叶圣陶提出。|
|QA Mode / Rewrite Mode 的权限分离与输出格式|`AI FILM STUDIO SYNTHESIS`|来源讨论写作与修改，不讨论 AI 系统权限、默认 QA、显式改写授权、Severity 或 Role Handoff。|
|现代自然中文与 2026 使用感|`AI FILM STUDIO SYNTHESIS`|YST-02 所谓“现代话/普通话”属于 1978 语境；本人也强调时代变化，但不能证明 2026 平台、行业、网络和跨地区实际用法。具体当代判断须靠 Charter 与后续现代语料校准。|
|AI 腔诊断总类|`AI FILM STUDIO SYNTHESIS`|“AI 腔”及 AP-01–AP-18 均不可能由历史来源直接支持。|

## 四类 AI 模式的专项边界

|现代问题|叶圣陶材料能提供的邻近证据|最终规则应如何标注|
|---|---|---|
|Abstract Thesis|YST-01 批评作者没有真正理解“人生、意义、空虚”等概念却先写成结论；YST-02 反对空话、套话|“概念未懂清、没有事实依傍时不应装成确定表达”可 `SOURCE-SUPPORTED`；“AP-01、主题总结时机、Concrete Situation → Choice → Consequence 链”均为 `AI FILM STUDIO SYNTHESIS`。|
|Artificial Binary|两份材料没有专门讨论“不是 A 而是 B”或二元选择模板|必须 `AI FILM STUDIO SYNTHESIS`；最多借“逻辑与实际意思相合”作一般背景，不得伪称来源支持二元诊断。|
|Trailer Copy by Register|两份材料强调目的与读者，但没有宣传文案 Register 或 Trailer Copy 分类|必须 `AI FILM STUDIO SYNTHESIS`；R8 允许高压缩、R1/R2 防止压掉开发信息均来自 Charter。|
|Pseudo-term|YST-01 的“聊寞”例只说明不了解词义而拼造会妨碍理解；YST-02 批评不懂专业内容却照写|“词义未知或读者无法理解时要核验”可 `SOURCE-SUPPORTED`；Social Proof、使用群体、世界观命名权和 `TERM PLAUSIBILITY WARNING` 是 `AI FILM STUDIO SYNTHESIS`。|

## 特别风险结论

### Register 8 类

R1–R8 是已批准 Charter 的项目分类，不是叶圣陶一手方法。叶圣陶只能为“目的、读者和书面/口头差异会改变表达判断”提供原则性先例。主稿若写“叶圣陶提出八类 Register”或给八类逐项挂 `SOURCE-SUPPORTED`，证据越界。

### NO CHANGE

`NO CHANGE` 作为 QA 输出决定属于 AI Film Studio。它与“想对了，写对了，才可以一字不易”及“修改要讲理由”一致，因此可以写成：`AI FILM STUDIO SYNTHESIS — source-compatible`。不能写成叶圣陶的固定输出或把“不改”当成他唯一偏好。

### 现代性

不得把 1978 年的“普通话”“群众观点”、成语取舍、广播可懂度、报刊篇幅和“尽可能短”原样变成 2026 硬规则。可迁移的是目的、读者、准确、误解、方案比较与复核。专业 Brief、行业术语、Marketing Copy、网络语言及当代社会使用感必须由 Charter、当代语料或其他蒸馏对象校准。

### Read-Aloud 非机械化

来源直接支持“念一两遍”这一检查，但没有支持：所有文本必须朗读、朗读卡顿即错误、书面专业文本必须改成日常口语。相反，YST-02 明确说书面与口头有不同，且书面文本要脱离表情手势独立成立。因此最稳妥的转译是：`OPTIONAL TOOL / CONDITIONAL METHOD`；先根据 Register 与用途决定朗读测试检查什么，绝不把口语顺滑设为唯一门槛。

### Meaning Lock

一般“原意—表达—误差—复核”可以由来源支撑；八项影视意义锁与 Canon 决策门必须标 `AI FILM STUDIO SYNTHESIS`。尤其 Character Intent、Information Reveal、Power Relationship、Emotional State 和 locked canon 都不是两份材料覆盖的术语或判断系统。

## 主稿的最低标注护栏

1. 只把“目的/读者、思想与表达、事实/准确/误解、修改理由、多案比较、书面/口头差异、朗读复核”标为 `SOURCE-SUPPORTED`。
2. 把完整五段工作流、表达准确检查表、Over-Editing 收益门和非唯一答案的运行化标为 `SYNTHESIZED INFERENCE`；如直接采用 Charter 状态码或字段，则升级为 `AI FILM STUDIO SYNTHESIS`。
3. 把 R1–R8、Meaning Lock 八项、QA/Rewrite 权限、Severity、AI-pattern、Term Plausibility、Role Handoff 和 2026 现代性全部标为 `AI FILM STUDIO SYNTHESIS`。
4. 每条历史材料的“短、普通话、群众、上口、顺耳”都必须附现代性护栏，不得进入 `HARD CONSTRAINT`。其中朗读最多为 `OPTIONAL TOOL`；“短”最多为受内容与用途限制的 `CONDITIONAL METHOD`。
5. 不得以叶圣陶名义判断 Trailer Copy、AI 腔、Series Engine、Canon 或影视角色信息控制；这些是 Charter/项目应用。

## 预审结论

`PASS WITH EVIDENCE BOUNDARY WARNINGS`。

两份一手材料足以支撑 Meaning-Preserving Editing Judgment 的核心：先澄清意义，定位表达错位，给出可说明的修改理由，比较多个方案并复核是否更准确。但它们不足以直接支撑八类 Register、完整 Meaning Lock、现代 AI-pattern 诊断、`NO CHANGE` 状态码或 2026 现代性标准。只要主稿严格按上述三种来源标签拆分，并切断历史规范与风格继承，当前证据可继续进入正式蒸馏与原创干跑。
