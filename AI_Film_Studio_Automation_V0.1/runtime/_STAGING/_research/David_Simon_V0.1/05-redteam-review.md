# David Simon｜WORLD-SYSTEM ENGINE 红队复审

审计对象：`runtime/_STAGING/David_Simon_Showrunner_Distillation_V0.1.md`

复审范围：证据归因、DS-01..DS-08 最终账本、研究子集编号、三层标签与四类方法分类、表层误蒸馏边界、10 个必需章节、Input → Judgment → Decision → Output、原创干跑与发布前状态。

## 复审结论

**红队 substantive checks：PASS。研究包最终发布门：BLOCKED（两项文档一致性修复待完成）。**

主稿已修复上一轮红队发现的三项问题：

- 工作流 9/9 行均有逐行证据层和方法分类；
- 原创干跑已记录，8/8 测试 PASS，机械化禁区 9/9 PASS；
- `01-primary-research.md` 与 `02-world-system.md` 已改用 `PI-*`／`WS-*` 本地编号，不再直接复用 `DS-*`。

当前仍有两项必须在发布前修复的文档一致性问题：

1. `01-primary-research.md` 顶部写“唯一 PI-01 至 PI-08 映射以 04-evidence-audit.md 为准”，但该文件实际只有 PI-01 至 PI-06，且 `04-evidence-audit.md` 的最终编号是 DS-01 至 DS-08，不是 PI 编号。
2. `02-world-system.md` 顶部写“唯一 WS-01 至 WS-08 映射以 04-evidence-audit.md 为准”，但该文件实际只有 WS-01 至 WS-05，且 04 文件不提供 WS 编号映射。

另有一份旧审查文件 `06-task-review.md` 仍保留修复前的 `FAIL / BLOCKED`、`待记录` 和旧行号。它必须更新为本轮复审结果，或明确标记为“superseded / 历史审查，不代表当前状态”，否则研究包内会同时存在通过和失败的最终审查结论。

## 主稿通过项

### 必需章节与结构

10/10 必需章节存在：

1. `## 蒸馏目标`
2. `## 核心判断原则`
3. `## 工作流程`
4. `## 诊断问题`
5. `## 失败模式`
6. `## 修正方法`
7. `## 禁止继承`
8. `## 可 Skill 化规则`
9. `## 证据与来源`
10. `## Codex 审核结论`

`## 工作流程` 使用 `阶段 | 输入 | 判断 | 决策 | 输出` 五列表格，9/9 行均有逐行证据层和方法分类：

- Research Triage：`SYNTHESIZED INFERENCE｜默认启发式 + AI FILM STUDIO SYNTHESIS｜可选工具`
- Institution Map：`SYNTHESIZED INFERENCE｜默认启发式 + AI FILM STUDIO SYNTHESIS｜可选工具`
- Incentive Pass：`SYNTHESIZED INFERENCE｜条件适用方法 + AI FILM STUDIO SYNTHESIS｜可选工具`
- World Without Protagonist：`SYNTHESIZED INFERENCE｜条件适用方法 + AI FILM STUDIO SYNTHESIS｜可选工具`
- Multi-Sided / Ensemble Break：`SYNTHESIZED INFERENCE｜默认启发式 + AI FILM STUDIO SYNTHESIS｜可选工具`
- Distributed Causality：`SYNTHESIZED INFERENCE｜默认启发式 + AI FILM STUDIO SYNTHESIS｜条件适用方法`
- System State / Consequence：`SYNTHESIZED INFERENCE｜硬约束 + AI FILM STUDIO SYNTHESIS｜可选工具`
- Research-to-Drama Pass：`SYNTHESIZED INFERENCE｜默认启发式 + AI FILM STUDIO SYNTHESIS｜硬约束`
- Room / Feedback Review：`SYNTHESIZED INFERENCE｜默认启发式 + AI FILM STUDIO SYNTHESIS｜可选工具`

核心判断原则、修正方法、可 Skill 化规则中的执行性条目同样具备 `SOURCE-SUPPORTED`、`SYNTHESIZED INFERENCE` 或 `AI FILM STUDIO SYNTHESIS` 标签，并对应硬约束、默认启发式、条件适用方法或可选工具。没有发现把 Studio 工具写成 Simon 固定术语的情况。

### 原创干跑

主稿已写入 8/8 独立干跑结果，并链接到 [03-original-dryrun.md](<E:/AI_Film_Studio/AI_Film_Studio_Automation_V0.1/runtime/_STAGING/_research/David_Simon_V0.1/03-original-dryrun.md>)：

- World Without Protagonist：PASS
- Institution Map：PASS
- Multi-Sided Conflict：PASS
- Character + Incentive：PASS
- Distributed Causality：PASS
- Research → Drama：PASS
- Ensemble Function：PASS
- Long-Term Consequence：PASS

机械化边界 9/9 PASS：未强制完整社会模拟、未把人物化为制度函数、未压成好人／坏人二元、未禁止明确恶意节点、未要求 15 人／长期跨度为配额、未把研究写成百科对白，也未蒸馏政治、慢节奏、犬儒、社会写实或具体作品表层。

### 表层与交叉边界

主稿明确排除 *The Wire*、Baltimore、警察、毒品、新闻、港口、学校及具体机构／城市／角色模板；排除 Simon 的政治立场、悲观主义、犬儒主义、慢节奏、社会写实气质、对白风格和人格；不把“大群像越大越好”或“系统必胜个人”写成规则。

Tony Gilroy 只作为 `OVERLAP CANDIDATE`，主稿明确禁止用 Tony 的 Scene State／Production Check 回填 Simon，也未发现提前融合。

## DS-01..DS-08 最终账本核对

`04-evidence-audit.md` 与主稿最终账本均为 8 条、8/8 第一手（100%），ID、来源、URL、可直接支持范围一致：

| ID | 来源 | URL／映射 | 结果 |
|---|---|---|---|
| DS-01 | *The Wire Series Wrap-Up / Just Words* | S3 官方 PDF，一致 | PASS |
| DS-02 | Salon 访谈 | 一致 | PASS |
| DS-03 | WIRED 访谈 | 一致 | PASS |
| DS-04 | PBS *Bill Moyers Journal* transcript | 一致 | PASS |
| DS-05 | Museum of the Moving Image panel transcript | 一致 | PASS |
| DS-06 | WGA East *OnWriting* Episode 79 | 一致 | PASS |
| DS-07 | Maximum Fun *Bullseye* transcript | 一致 | PASS |
| DS-08 | NPR/VPM TV-writer interview transcript | 已规范化为尾斜杠 URL，一致 | PASS |

8 个来源 URL 在本轮检查中可访问；DS-08 浏览器可正常解析并显示正文。

## 研究子集编号复核

本地编号已经从冲突的 DS 编号改为 PI／WS 前缀，方向正确，但顶部声明仍不准确：

- `01-primary-research.md` 实际有 PI-01 至 PI-06（6 份子集），不能写 PI-01 至 PI-08；最终口径应明确指向 `04-evidence-audit.md` 的 DS-01 至 DS-08。
- `02-world-system.md` 实际有 WS-01 至 WS-05（5 份子集），不能写 WS-01 至 WS-08；同样应明确 WS 是本文件局部编号，最终账本仍是 DS-01 至 DS-08。
- `02-world-system.md` 的“5 份核心一手材料”随后又说明其中 4 份为 Simon 直接访谈／现场记录、1 份为官方辅助报道；建议改为“5 份研究子集材料（4 份直接材料 + 1 份辅助报道）”，避免把辅助报道称为核心一手。

## 精确修复要求

1. 将 `01-primary-research.md` 顶部改为：`本文件使用 PI-01 至 PI-06 的局部子集编号；最终核心账本为 04-evidence-audit.md 中的 DS-01 至 DS-08。`
2. 将 `02-world-system.md` 顶部改为：`本文件使用 WS-01 至 WS-05 的局部子集编号；最终核心账本为 04-evidence-audit.md 中的 DS-01 至 DS-08。`
3. 将 02 文件的“5 份核心一手材料”改为“5 份研究子集材料（4 份直接一手材料 + 1 份官方辅助报道）”。
4. 更新 `06-task-review.md` 为本轮复审结果，或明确标记为 superseded；不能让旧 FAIL 审查与主稿 PASS 并存而不解释。
5. 完成以上修复后，再进行一次最终一致性扫描；修复前不得改 frontmatter 为 `approved/passed`，不得调用发布脚本。

## 安全状态

本次复审只读检查 staging、研究文件和 URL；未修改正式 Obsidian Vault，未执行发布。
