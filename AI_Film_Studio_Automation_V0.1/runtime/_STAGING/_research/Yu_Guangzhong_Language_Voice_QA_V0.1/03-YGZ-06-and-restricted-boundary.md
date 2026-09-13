# YGZ-06 与 YGZ-02 受限入口核验及边界审计

核验日期：2026-08-22  
任务范围：只核验 YGZ-06 的“重改旧译／目标语组织复审”证据，以及 YGZ-02 的公开元数据与访问边界。本文件不从受限全文推测观点，不建立完整余光中方法论。

## Provenance 标签

- `SOURCE-SUPPORTED`：页面正文、公开书目字段或公开摘要可以直接支持的窄主张。
- `SYNTHESIZED INFERENCE`：把一项或多项直接证据转成可执行判断时所作的有限归纳；不得写成余光中的原话或固定术语。
- `AI FILM STUDIO SYNTHESIS`：为 2026 生产环境、Anti-Purism、现代用法和职责边界设置的 Studio 自有护栏；不得归因于余光中。

## YGZ-06｜2017 电话访谈

### 页面与元数据核验

|字段|逐页核验结果|Provenance|
|---|---|---|
|实际题名|《最后的声音！余光中9月接受环球时报记者采访音频记录》；“2017 最后一次完整电话访谈”是证据台账的描述性标签，不是页面原题。|`SOURCE-SUPPORTED`|
|URL|https://news.sina.cn/gn/2017-12-14/detail-ifyptfcn0304938.d.html|`SOURCE-SUPPORTED`|
|发言者|答问者：余光中；提问方在正文中标为“环球时报”；报道署名记者吴薇。|`SOURCE-SUPPORTED`|
|载体|《环球时报》—环球网独家电话专访的文字全记录；手机新浪网转载，页面作者/来源标为“环球网”。页面称原文刊于 9 月 29 日《环球时报》13 版。|`SOURCE-SUPPORTED`|
|采访日期|2017-09-28。|`SOURCE-SUPPORTED`|
|网页刊出时间|2017-12-14 14:55。|`SOURCE-SUPPORTED`|
|可访问性|全文可直接读取；页面明确写“以下是访谈全纪录”，HTML 正文含连续问答。未遇登录或付费门。|`SOURCE-SUPPORTED`|
|来源稳定性|媒体转载且正文完整，身份与日期可核；但不是余光中本人托管页，故作为 `MEDIUM-HIGH`，重要方法须与其他一手材料交叉。|`SYNTHESIZED INFERENCE`|

### 可直接使用的窄证据

定位：正文第二个提问组，余光中回忆童年古文阅读之后、进入下一条“如何看待传统文化”问题之前。

1. `SOURCE-SUPPORTED｜YGZ-06-R1`：余光中明确复盘《梵古传》出版约十年后曾再改一次。
2. `SOURCE-SUPPORTED｜YGZ-06-R2`：他明确区分了两种问题：重改并不是因为早年的英文理解能力不足，而是后来不满意当年“用中文的方式”。
3. `SOURCE-SUPPORTED｜YGZ-06-R3`：他把该次修订的用意说成纠正自己认为偏于西化的中文。

为避免不必要的长引，以上只保留可核对的短识别语和释义，不复制访谈段落。

### 可进入蒸馏的有限归纳

|可执行归纳|标签|证据限度|
|---|---|---|
|源语理解无明显错误，仍不代表目标语表达已经成立；应允许单独复审中文如何组织意义。|`SYNTHESIZED INFERENCE`，基础为 YGZ-06-R1/R2|“源语理解检查 → 目标语组织检查”的两层接口是方法化转译，不是访谈中提出的流程名称。|
|旧译可以在时间拉开后重审；复审应问中文结构是否自然承载原意，而不只问字义是否对应。|`SYNTHESIZED INFERENCE`，基础为 YGZ-06-R1/R2|只支持复审的必要性与目标语维度；不支持固定等待年限、每次必改或某一种唯一中文句法。|
|Translation-like Chinese 可是一种目标语组织问题，而非源语能力不足的同义词。|`SYNTHESIZED INFERENCE`，基础为 YGZ-06-R2/R3|访谈使用“偏于西化”的历史性自评；“Translation-like Chinese”是本项目的现代诊断接口。|

### 不可由 YGZ-06 推出的结论

- 不能推出名词化、介词、被动、代词、连接词或外来词一出现就错。
- 不能推出所有翻译都必须重写，或必须改成文言、短句、对仗、诗性中文。
- 不能把个人对“西化”、文言教育、政治或传统文化的价值判断升级为 Shared QA 的跨项目硬规则。
- 不能用这一个自述个案独立证明完整的 `Nominalization / Preposition Chain / Connector Load / Passive Necessity` 模块；这些模块必须由 YGZ-01、03–05 等材料交叉，并保留现代护栏。
- 不能把“目标语组织复审”写成余光中的原始术语；它是 `SYNTHESIZED INFERENCE`。

## YGZ-02｜《翻译面面观》受限入口

### 详情页元数据核验

|字段|逐页核验结果|Provenance|
|---|---|---|
|实际题名|《余光中教授訪談：翻譯面面觀》|`SOURCE-SUPPORTED`（公开书目字段）|
|并列题名|*Aspects of Translation: An Interview with Kwang-chung Yu*|`SOURCE-SUPPORTED`（公开书目字段）|
|URL|https://ericdata.com/tw/detail.aspx?no=215135|`SOURCE-SUPPORTED`|
|访谈者/署名作者|單德興。|`SOURCE-SUPPORTED`（`citation_author` 与页面“作者”字段）|
|受访者|余光中教授。|`SOURCE-SUPPORTED`（题名及公开摘要）|
|载体|《編譯論叢》6 卷 2 期，165–205 页；出版单位为國家教育研究院；ERICDATA 高等教育知识库提供索引。|`SOURCE-SUPPORTED`|
|出版日期|2013-09-01；页面期次写作 `201309 (6:2期)`。|`SOURCE-SUPPORTED`（`citation_publication_date` 与期次字段）|
|制作信息|公开摘要称访谈在国立中山大学文学研究室进行，约三小时；录音由黃碧儀謄打，之后送余光中过目。|`SOURCE-SUPPORTED`（仅限公开摘要的版本/身份信息）|
|公开可读范围|题名、作者、摘要、页码、关键词、刊名、期次与出版单位可读。|`SOURCE-SUPPORTED`|
|全文可访问性|受限。详情页“阅读全文”指向 `note.aspx?no=215135&code=00518493`；打开后明确说明本站只提供索引，阅读全文需年费会员登录或购买。|`SOURCE-SUPPORTED`|
|来源稳定性|书目身份 `HIGH`；正文访问 `LIMITED`。|`SYNTHESIZED INFERENCE`|

### 为什么不计入公开核心

1. `SOURCE-SUPPORTED`：当前能核验的是书目、摘要与版本过程；未取得 165–205 页访谈全文。
2. `SYNTHESIZED INFERENCE`：摘要可证明这是一份由單德興访谈余光中、录音转写并送本人过目的可靠补证入口，但不能证明任何具体问答、措辞或方法规则。
3. `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：由于无法逐段核对正文，YGZ-02 不计入“公开可访问核心一手”数量，不给主稿任何 `SOURCE-SUPPORTED` 方法条目编号，也不用于填补证据缺口。未来若依法取得全文，应另建版本记录并重新审核，不能用摘要代替全文。

### 严禁从公开摘要虚构的内容

- 不虚构访谈中关于名词化、被动、介词、连接词、目标语顺序或“英式中文”的具体回答。
- 不把摘要所列“成果与经验、批评与论述、教学与提倡”等主题范围写成余光中的方法结论。
- 不生成不存在于公开页的引语、页码定位、问答次序或课程内容。
- 不因摘要称“本人过目”就假定所有文字逐字代表其口语原貌；只能确认这是经本人审阅的转写版本入口。

## Modernity Risk 审计

风险等级：`VERY HIGH`。

1. `SOURCE-SUPPORTED`：YGZ-06 是余光中对自己旧译和个人语言取向的历史复盘；它确实表明他后来不满意早年的中文表达方式。
2. `SYNTHESIZED INFERENCE`：这支持“目标语仍需独立复审”，不自动支持他对所有“西化”现象的历史判断在 2026 仍然有效。
3. `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：`Foreign Influence ≠ Error`。只能在结构造成当下中文的理解、因果、主语、信息释放、语域或行动可执行性负担时发出 Translation-like 诊断。
4. `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：现代已规范化的表达、专业术语、行业惯用语与地区差异不得仅凭历史来源判错；须按当前受众、Register、Intent 和实际认知负担判断。
5. `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：当前用法无法确认时标记 `CONTEMPORARY USAGE UNKNOWN`，留给未来 Contemporary Language Layer；本轮不得自建该层，也不得假装已有现代语料结论。
6. `AI FILM STUDIO SYNTHESIS`：YGZ-02 的 2013 元数据与 YGZ-06 的 2017 自述都不能单独证明 2026 的通行用法。

## Anti-Purism 审计

1. `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：不得建立“的／其／被／通过／进行／实现／关于”等字符、词项或句式黑名单；出现只是检查信号，不是错误证明。
2. `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：外来词、英文项目名、Production/QA 术语或技术接口名本身不等于翻译腔；只检查它们是否妨碍当前目标受众理解与工作交接。
3. `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`：被动句有信息焦点、受事状态或责任隐藏等实际功能时可以保留；专业文本中的名词化、连接词和介词结构也可以合理成立。
4. `AI FILM STUDIO SYNTHESIS｜DEFAULT HEURISTIC`：先恢复核心命题和信息关系，再判断现有包装是否造成不必要负担；修正目标是意义更可读、可判断、可执行，不是更“纯”、更古或更短。
5. `SYNTHESIZED INFERENCE`：YGZ-06 的“重改旧译”适合作为复审许可，不适合作为净化配额；`NO CHANGE` 必须保留为合法结果。

## Style Imitation Risk 审计

风险等级：`HIGH`。

- `AI FILM STUDIO SYNTHESIS｜禁止继承`：余光中的诗性节奏、对仗、古典引语、文言偏好、散文音调与个人修辞配方。
- `AI FILM STUDIO SYNTHESIS｜禁止继承`：YGZ-06 中关于政治、国文教育和文化正统的立场；这些不属于 Language & Voice QA 的 Translation-like Chinese 能力。
- `AI FILM STUDIO SYNTHESIS｜禁止继承`：把“反西化”塑造成回答人格、审美身份或普遍语言纯化使命。
- `SYNTHESIZED INFERENCE｜允许迁移`：只迁移“源语理解与目标语表达可分开复核”“旧表达允许重新检查中文组织”的窄判断能力。

## 对主蒸馏稿的证据接口

|接口|可用性|允许写法|禁止写法|
|---|---|---|---|
|Revision / Target-language Review|可用；YGZ-06 直接基础，方法化部分需标 `SYNTHESIZED INFERENCE`|“即使源语理解无误，也要复核中文组织是否自然承载原意。”|“余光中提出了固定的两阶段 QA 流程。”|
|Translation-like ≠ source misunderstanding|可用；YGZ-06 强支持区别|“问题可能位于目标语组织，而非源语理解。”|“所有西式结构都是翻译错误。”|
|Modernity / Foreign Influence ≠ Error|只能作为 `AI FILM STUDIO SYNTHESIS` 护栏|按 2026 Register、Intent、受众与认知负担复核。|归因于余光中，或用其历史偏好直接裁定当代用法。|
|YGZ-02 方法论|当前不可用|只列为受限补证入口和版本身份。|由摘要反推具体观点、规则、引语或页码。|

## 子任务结论

- YGZ-06：`PASS AS CORE FIRST-HAND EVIDENCE`。全文可读；只支持重改旧译、源语理解与目标语中文方式可分开复审，以及目标语组织仍需独立判断。政治、文言和个人风格内容全部排除。
- YGZ-02：`VERIFIED RESTRICTED METADATA / NOT COUNTED AS CORE`。身份、载体、日期、页码、访谈/转写/本人过目流程均可核；正文受会员门限制，未作任何内容性推断。
- Modernity：`GUARDRAIL REQUIRED`。历史自评不可直接等同 2026 规范。
- Anti-Purism：`GUARDRAIL REQUIRED`。不得生成字符/词项黑名单，必须保留功能判断和 `NO CHANGE`。
- Style：`GUARDRAIL REQUIRED`。不得模仿余光中或把文化立场转成 QA 人格。

