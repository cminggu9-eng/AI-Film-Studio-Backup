# Showrunner SKILL V0.1｜huashu-nuwa Phase 5 Optimizer Review

## 审查范围

只读审查 `runtime/_STAGING/Showrunner_SKILL_V0.1.md`，按 huashu-nuwa Phase 5 的 optimizer 视角检查：指令冗余、可操作性、触发路由、边界条件、回环安全、输出字段和执行效率。未修改 Skill，未修改 Obsidian Vault，未安装或锁定 Skill。

## 总体结论

**优化审查：PASS（无阻塞项，建议合并以下 3 项文本修复后再发布）。**

现有 Skill 已通过 8 项功能干跑、8 项反机械化攻击测试、Canon/Production/岗位边界检查；以下是生产化前的低风险优化，不改变其创作原则、Decision Stack、用户最终决定权或下游边界。

## 优化项 1｜增加“最小充分运行”与层级启用门

**位置：** `SHOWRUNNER DECISION STACK`（当前约第 71 行）。

**观察：** Skill 要求八层都做 `INPUT → JUDGMENT → DECISION → OUTPUT → VALIDATION`，同时允许 `N/A BY FORMAT`，但没有规定小任务的最小扫描顺序，也没有明确什么条件才启动 L3、L5、L6、L7。实际调用时可能重复输出不适用的制度、连续剧、长篇或制作分析。

**建议加入的文本：**

> 先运行 `MINIMUM VIABLE PASS`：PROJECT STATE、FORMAT FIT、STORY PURPOSE、CHARACTER ENGINE、CAUSAL STORY ENGINE 是默认最低扫描；只有触发对应门时才展开 WORLD/SYSTEM、SERIES/EPISODE、LONGFORM 或 PRODUCTION。触发门分别为：独立机构/激励/系统持续改变选择成本 → L3；存在连续形式且需要解释下一集供给 → L5；存在多阶段/有限季/长篇交接 → L6；用户请求制作范围审查或已发现规模风险 → L7。未触发的层标记 `N/A BY FORMAT/INTENT`，写明跳过原因、复查条件和最小输出，不得把跳过当作未知。任一层出现 BLOCKED 时停止该路径，不为填满八层继续生成。

**收益：** 保留完整决策覆盖，同时减少轻量 Idea、单场景或越权请求的无关分析，令“按需启用”可执行、可审计。

**优先级：** P1（可操作性/效率）；不属于模型级问题。

## 优化项 2｜明确触发路由的主输出与附加输出规则

**位置：** `何时调用`、`输出路由`（当前约第 24、173–188 行）。

**观察：** 当前允许输出一个或多个类型，但当用户同时提出“判断 Idea、开发整季并审查制作范围”时，没有明确主输出如何选择、附加输出如何受控，容易把 10 类输出全部展开，或让输出类型与任务意图不一致。

**建议加入的文本：**

> 先选一个 `PRIMARY OUTPUT TYPE`，再按决策结果选择零个或多个 `SECONDARY OUTPUT TYPE`；路由优先级为：明确用户交付物/格式请求 > 当前阻塞或诊断症状 > 项目阶段 > 默认推荐。没有明确交付物时，`TASK INTENT` 决定主类型：Idea/Concept → Concept Diagnosis 或 Project Development Brief；角色包 → Character Engine Brief；Series/Season/Episode 结构 → 对应 Engine/Architecture/Brief；已有问题 → Story Repair Report；制作规模请求 → Production Scope Review；跨岗位交付 → Downstream Handoff Package。每个附加类型必须注明“触发它的判断”和最小必要范围；不得仅因某层被扫描就自动生成对应完整报告。

**收益：** 将“先声明 TASK INTENT/OUTPUT TYPE”转成确定的路由算法，降低过度生产、交付物漂移和输出重复。

**优先级：** P1（触发路由/输出效率）；不改变现有 10 类输出定义。

## 优化项 3｜给回环增加可终止记录格式

**位置：** `CONFLICT RESOLVER`、`回环机制`、`每次回环记录`（当前约第 127–147 行）。

**观察：** 当前已要求记录原因、受影响层、未选方案、状态变更、授权者和复查门，但缺少迭代编号、最后有效状态、当前尝试的修复和退出条件。若相同根因反复回环，执行器可能重复生成相同方案，难以判断何时升级为阻塞。

**建议加入的文本：**

> 每次回环使用 `LOOP RECORD`：`iteration_id / trigger_code / affected_level / last_valid_state / attempted_repair / rejected_option / decision / state_delta / owner_or_authorizer / review_gate / exit_condition`。只有 `state_delta` 改善目标或减少未知时才进入下一轮；若同一 `trigger_code + last_valid_state` 连续两轮没有新的可行修复，输出 `WARNING｜REPEATED LOOP`；若第三轮仍无状态变化，或所有修复都损坏 Essential Dramatic Function，则升级为相应 `BLOCKED FOR ...`，停止该路径并等待用户决定。此为执行安全阀，不是每个项目必须经历的重试次数。

**收益：** 防止回环失控和静默重复改写，使诊断、修正、复查、阻塞之间有可追踪的终止条件。

**优先级：** P1（回环安全/可审计性）；不把创作过程机械化为固定重试配额。

## 其它检查结果

- **冗余：** 八层、回环、状态等级和自检清单存在有意重复，分别承担决策、返工、停止和验收职责；未发现必须删除的重复段落。
- **边界：** Role Boundary、Canon、UNKNOWN、Production Reality 和用户最终决定权均有明确保护；无需扩大 Skill 职责。
- **触发：** 已覆盖 Idea、Concept、Character/World、Series、Season、Episode、Diagnosis 与 Production；建议项 2 只补主/附输出优先级。
- **效率：** 主要风险是小项目的层级过扫与失败回环的重复；建议项 1、3 分别处理。
- **来源边界：** 未新增创作者事实；建议文本属于 `AI FILM STUDIO SYNTHESIS` 执行优化，不应归因于任一创作者。

## 最终判定

**PASS。** 三项均为局部文本优化，无阻塞性缺陷；在合并后应重跑现有功能/反机械化测试，并额外检查一次性短片、无机构关系剧和多触发任务的主输出路由。

## 合并后复审｜2026-08-21

已核对当前 `Showrunner_SKILL_V0.1.md`：三项建议均已写入，字段和终止条件完整，未破坏用户决定权、Canon 保护、角色/制作边界或反机械化约束。

- `MINIMUM VIABLE PASS`：已写入，并明确 L3/L5/L6/L7 的触发门、`N/A BY FORMAT/INTENT`、复查条件和 BLOCKED 停止条件。**非阻塞微调建议：** 当前 L3 触发文字偏向“独立机构/激励/系统持续”，可能让轻量项目跳过原本仍有价值的 `LOW` 级规则/空间/资源检查；可改为“相关规则/空间/资源会改变选择成本时至少启用 L3 LOW，只有独立机构或跨阶段系统持续时才展开 MEDIUM/HIGH 模块”。
- `PRIMARY/SECONDARY OUTPUT`：已写入优先级和附加输出最小范围。**非阻塞微调建议：** 默认路由仍写作 `Concept Diagnosis 或 Project Development Brief`；若要求完全确定路由，可补充“仅有 Idea/Concept 且未指定交付物时默认 Concept Diagnosis；用户明确要求开发包时才选 Project Development Brief”。
- `LOOP RECORD`：已完整写入 `iteration_id`、`last_valid_state`、`state_delta`、`review_gate`、`exit_condition`，并提供 `WARNING｜REPEATED LOOP` 与升级 BLOCKED 条件；审查通过。

**复审结论：PASS（两项为 P2 清晰度微调，不构成阻塞；修正后可标记最终 PASS）。**
