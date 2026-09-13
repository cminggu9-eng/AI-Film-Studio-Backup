# 汪曾祺 Language & Voice QA V0.1｜Canonical Evidence Ledger

## 口径

- 核心材料：3 份。
- 第一手内容：3/3（100%）。其中 WZQ-01、WZQ-03 是署名为汪曾祺的权威转载；WZQ-02 是收入教材 PDF、明确溯源至 1993 年《汪曾祺文集·文论卷》的本人文论节选。它们不等同于原刊扫描，因此保留载体与版本边界。
- 二手材料作为核心证据：0 份。
- `SOURCE-SUPPORTED` 只表示下列来源可直接支持限定范围内的主张；任何现代 QA 模式、状态码、Register、Severity、Meaning Lock 与测试流程均属于 `AI FILM STUDIO SYNTHESIS`。

## 唯一来源 ID

### WZQ-01｜当前网页题名《小说里边最重要的是什么？》

- 作者：汪曾祺。
- 当前载体：中国作家网转载，页面注明原载 1991 年《写作》第 4 期；“思想·语言·结构”仅是研究阶段主题标签，不是当前载体题名。
- URL：https://www.chinawriter.com.cn/n1/2021/1024/c404032-32262629.html
- 直接支持：语言与内容不可剥离；字、句、段和全篇互相制约；自然流动不等于固定短句；长短安排与“合适、准确”有关；复杂主题不应被压成唯一标准答案。
- 不可外推：固定句长、固定节奏配额、朗读硬规则、古典/民间腔调强制继承。

### WZQ-02｜《“揉面”——谈语言》

- 作者：汪曾祺。
- 当前载体：高等教育出版社教材章节 PDF；页尾注明选自 1993 年江苏文艺出版社《汪曾祺文集·文论卷》。
- URL：https://oss0.changxianggu.com/book/chapter/269_9787040514674.pdf
- 直接支持：文学语言本身参与艺术效果；书面语言不是未经加工的口语；整篇、整段、整句统筹；普通词在具体关系与生活印象中可以产生新鲜效果；不造难懂形容词；语言须贴近人物、题材与态度；意义/态度宜溶入叙述，不宜另行宣布。
- 不可外推：口语至上、普通词一律优先、漂亮句一律删除、历史表达优先、朗读适用于所有 Register。

### WZQ-03｜当前网页题名《我的作品所包涵的是什么样的感情？》

- 作者：汪曾祺。
- 当前载体：中国作家网转载的本人自序；“自报家门”仅是研究阶段来源别名/文本身份说明，不是当前网页题名。
- URL：https://www.chinawriter.com.cn/n1/2021/1015/c404032-32254662.html
- 直接支持：地方生活会影响语言但不机械绑定地方语言；人物从具体生活经验/原型出发并允许艺术加工；本人不从纯理念出发制造人物；地方书写与现代主义不构成必然对立；作品有自身形式，不能机械拉长或缩短。
- 不可外推：地方口语模仿、地域气质模板、普通词优先、现代项目应仿用其时代语言。

## 方法主张映射

| ID | 方法主张 | 证据性质 | 来源 |
|---|---|---|---|
| M1 | 语言不是附着在意义之外的装饰；改形式可能同时改意义与实际效果。 | SOURCE-SUPPORTED | WZQ-01, WZQ-02 |
| M2 | 流动感来自字—句—段—全篇的关系，而不是统一短句或固定节拍。 | SOURCE-SUPPORTED | WZQ-01, WZQ-02 |
| M3 | 自然不等于原样口语；文学/项目书面中文可以经过组织。 | SOURCE-SUPPORTED | WZQ-02 |
| M4 | 普通词可在准确关系与具体生活印象中产生新鲜效果。 | SOURCE-SUPPORTED | WZQ-02 |
| M5 | 语言效果必须结合人物、题材、态度与使用场景判断。 | SOURCE-SUPPORTED | WZQ-02 |
| M6 | 作者态度宜溶入叙述关系，而非脱离文本另行宣布。 | SOURCE-SUPPORTED | WZQ-02 |
| M7 | 地方生活影响语言，但地域语言与现代主义并非机械绑定或必然对立。 | SOURCE-SUPPORTED | WZQ-03 |
| M8 | 作品有自身形式，不宜任意拉长或缩短。 | SOURCE-SUPPORTED（限于作品形式） | WZQ-03 |
| S1 | 以“意义—形式—Register—上下文—实际效果”作为 Natural Chinese Judgment 主链。 | SYNTHESIZED INFERENCE | M1-M8 |
| S2 | 把 Anti-Overwriting、Anti-Rhetoric、Concrete Before Abstract 和 Restraint 组合为收益门。 | SYNTHESIZED INFERENCE | M1, M4-M6 |
| S3 | Whole-Context Judgment 先看段落任务，再判断单句是否需要修改。 | SYNTHESIZED INFERENCE | M2, M5 |
| S4 | 普通词原则不能升级为词汇配额或禁词表。 | SYNTHESIZED INFERENCE | M4 |
| S5 | 抽象判断优先寻找事实、行动、关系或决策锚。 | SYNTHESIZED INFERENCE | M6, M7 |
| S6 | 反机械边界可转译为不设置跨项目句长、修辞或口语数字配额。 | SYNTHESIZED INFERENCE | M2, M8 |
| AFS1 | R1-R8、QA/REWRITE 权限、Meaning Lock、Severity、NO CHANGE/PASS 等运行协议。 | AI FILM STUDIO SYNTHESIS | Charter/项目规则 |
| AFS2 | AI-pattern、伪术语有限诊断、现代性测试、测试 A-J 的输入输出结构。 | AI FILM STUDIO SYNTHESIS | 本任务书 |
| AFS3 | 不以地域腔调或历史文风复制代替 2026 项目判断。 | AI FILM STUDIO SYNTHESIS | Modernity Guardrail |

## 冲突与边界

1. “自然”不等于“更口语、更短、更随便”；假口语和信息塌缩同样可能不自然。
2. “普通词”不是硬约束；专业 Brief、术语、抽象讨论在 Register 合适且信息有效时可保持不动。
3. “具体在前”不是禁绝抽象；抽象必须有任务、证据与承载位置。
4. 不把汪曾祺的个人文风、时代措辞、地域经验、句法节奏或生活趣味继承到现代项目文本。
5. 伪术语检查只判断词是否遮蔽任务、对象或可验证含义，不扩张为完整术语治理系统。

## 审计结论

三份核心材料可支撑受限的方法论蒸馏；所有跨来源流程与现代 QA 机制必须显式标为推断或 AI Film Studio 合成，不能伪写成汪曾祺原话。
