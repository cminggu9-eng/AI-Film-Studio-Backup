# 叶圣陶｜Language & Voice QA Canonical Evidence Ledger V0.1

核验日期：`2026-08-22`  
核心来源：`2`  
第一手内容：`2 / 2 = 100%`  
二手核心：`0`

> “第一手”在本账本中指叶圣陶本人署名文章、讲话及本人附记。托管/转载机构不是主张作者。候选审计只用于导航，不承担本轮方法证据。

## Canonical sources

|ID|来源|材料性质|可访问性|直接支持范围|不得外推|
|---|---|---|---|---|---|
|YST-01|[中国作家网｜《怎样写作》选文](https://www.chinawriter.com.cn/n1/2021/0201/c404032-32018755.html)|叶圣陶本人写作论文章组；页面注明选自中华书局 2007 版|全文可读 / HIGH|词要与所想一致；语法/用词“通”不等于意思真实准确；“词适合、篇章调顺”；思想、语言、文字联动；修改可同时修思想与表达；诵读可暴露不调顺|不能据此规定 2026 中文词汇、句长、审美或人物对白；文中教学性硬语气不得原样成为跨 Register 硬门|
|YST-02|[叶圣陶研究会｜《端正文风——在新华社国内记者训练班的讲话》](https://www.mj.org.cn/zsjg/ystyjh/yjlw/202201/t20220117_248050.htm)|1978-04-20 讲话的修订文本；含 1979-06-21 本人附记。现行稿经友人代改并由叶圣陶细读认可，不是现场逐字稿|全文可读 / HIGH|先定目的和读者，再选材料/语言；完稿多次复查；区分原想法不到位与表达未对准；修改需说明事实、准确性或误解风险；比较两三种改法；书面表达须自足；改后可朗读检查上口、可懂|不能把友人具体措辞当叶圣陶表达 DNA；“尽可能短”、特定成语/政治语境、普通话/广播标准不能泛化为现代所有 Register；朗读不是唯一正确性测试|

## Source anchors and claim map

|Claim ID|主张|标签|证据锚|正文用途|
|---|---|---|---|---|
|M1|修改前先明确要表达的意思、目的与接收者。|SOURCE-SUPPORTED|YST-02“第八点，养成写作的好习惯”；YST-01“诚实/精密”与“谈文章的修改”|Meaning Before Wording|
|M2|需要区分想法尚未理清与语言没有对准想法。|SOURCE-SUPPORTED|YST-02“假如我原来的想法不到家，或者我写出来的话没有针对我所想的”；YST-01“谈文章的修改”|Mismatch classification|
|M3|语法/词句可以“通”，但意思仍可能不真实、不精密或超出实际理解。|SOURCE-SUPPORTED|YST-01“好与不好”“通与不通”|Expression Accuracy|
|M4|清楚度涉及词是否合适、句篇组织是否调顺、关系词是否真实承担关系。|SOURCE-SUPPORTED|YST-01“通与不通”|Clarity / 顺当|
|M5|修改必须能说出理由：事实不符、说法不准确、可能使人误会。|SOURCE-SUPPORTED|YST-02“第八点”作文修改段|Revision With Reasons|
|M6|对一个问题可提出两三种改法，通过比较选择，而非宣布唯一答案。|SOURCE-SUPPORTED|YST-02“还有一个办法，我倒是常用的，就是比较”|Revision options|
|M7|朗读可作为改后检查，发现别扭或听不明白之处。|SOURCE-SUPPORTED|YST-01“诵读几遍”；YST-02“文章改完之后最好是念一两遍”|Read-Aloud Check|
|M8|想对、写对时可以保持不改；修改本身不是价值。|SOURCE-SUPPORTED|YST-01“想对了，写对了，才可以一字不易”|NO CHANGE / Over-editing|
|M9|书面与口头既相通又不同；书面表达缺少表情手势，需自足，但不能等同聊天。|SOURCE-SUPPORTED|YST-02“写在纸上的文章，跟口头说的话，有同有不同”|Register-aware read-aloud boundary|
|S1|将 M1–M8 编排为 `Meaning → Expression → Mismatch → Options → Meaning Check`。|SYNTHESIZED INFERENCE|YST-01 + YST-02 跨材料综合|可执行 QA 工作流|
|S2|把不准确拆为指代、主体、因果、范围、程度、抽象对应与越证据断言。|SYNTHESIZED INFERENCE|M2–M5 的现代诊断化|Expression Accuracy checklist|
|S3|把“调顺”拆为主干、信息顺序、修饰范围、连接、句间关系、重复、名词化与抽象链。|SYNTHESIZED INFERENCE|M4、M7 的现代诊断化|Clarity checklist|
|AFS1|R1–R8、QA/Rewrite 双模式、Meaning Lock 与严重度属于 AI Film Studio 章程接口。|AI FILM STUDIO SYNTHESIS|已批准 Capability Charter，不归因于叶圣陶|Register / Mode / Output|
|AFS2|Read-Aloud 只作条件工具；Project Brief 不得强制口语化。|AI FILM STUDIO SYNTHESIS|M7/M9 + Charter R2/R7|反机械化护栏|
|AFS3|AI 腔、Trailer Copy、伪术语和人工二元测试属于现代迁移验证。|AI FILM STUDIO SYNTHESIS|任务书 + Charter AP 分类|原创测试|

## Evidence boundary decision

- 核心一手材料虽只有两份，但都是方法密度高、全文可访问的长材料，且共同覆盖“意图—表达—复查—说明理由—比较方案—朗读—复核”。
- 不新增低质量材料充数。两份来源之外的现代 Register、AI 模式与精确输出契约全部明确归入 `AI FILM STUDIO SYNTHESIS`。
- 任何“所有句子都应简短/口语化/朗朗上口”“某个改写是唯一正确答案”“叶圣陶会如何写”均不进入方法规则。
