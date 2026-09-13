# Showrunner SKILL V0.1｜首轮静态审核

审核对象：`runtime/_STAGING/Showrunner_SKILL_V0.1.md`

审核依据：

- `tasks/showrunner/Showrunner_SKILL_Generation_Task_V0.1.md`
- `AGENTS.md`
- `PUBLISH_RULES.md`
- 已批准的 `Showrunner｜综合能力模型 V0.1.md`
- 当前 staging Skill 本体（首轮，未修改）

审核范围：按任务书静态审核 20 项，并额外检查执行性、反机械化、轻/复杂类型、Production Reality 和岗位边界。未写入 Obsidian，未修改 Skill。

## 总结结论

**复审：PASS。**

上一轮唯一阻塞已修复：当前 Skill 新增独立的 `BLOCKED FOR RESEARCH`，将“关键专业事实 UNKNOWN 且被要求写成确定性事实、未达到 Minimum Sufficient Understanding”与 `BLOCKED FOR PROVENANCE`（来源/状态不可追溯或推断误写为创作者原话/canon）分开；BLOCKED 现为完整 8 类。

本轮同时确认新增的 `MINIMUM VIABLE PASS`、主/附输出路由和带退出条件的 `LOOP RECORD` 没有破坏八层模型，反而补足了最小执行路径、输出选择和回环终止安全阀。未发现 MODEL-LEVEL ISSUE。

## 20 项静态检查

| # | 检查项 | 结果 | 证据与判断 |
|---:|---|---|---|
| 1 | 执行器而非理论文章 | PASS | 有调用入口、Project State Card、`MINIMUM VIABLE PASS`、逐层 `INPUT → JUDGMENT → DECISION → OUTPUT → VALIDATION`、回环记录、自检和 Handoff；不是五人理论的复制。最小路径和跳过条件已明确。 |
| 2 | Trigger / Use Cases | PASS | `## 何时调用` 覆盖 Idea、连续形式、角色/世界包、Series/Season/Episode 审核、剧本诊断、Production Scope；同时列出对白、剧本正文、表演、摄影、美术 Prompt 等不应调用情形。 |
| 3 | 输入识别 | PASS | `PROJECT STATE ASSESSMENT` 列出 7 种输入模式并标记 `LOCKED/APPROVED/DRAFT/UNKNOWN/CONFLICTING`，生成 Project State Card；`MINIMUM VIABLE PASS` 还规定所有请求先扫描 Project State、Format、Purpose、Character、Causal。 |
| 4 | 输出识别 | PASS | `TASK INTENT → OUTPUT TYPE`，完整列出 10 类输出，并规定每种输出的状态、判断链、代价、告警、验证门、provenance 和下一步。 |
| 5 | 决策流程 | PASS | 八层每层均有统一的输入→判断→决策→输出→验证协议；Project State、Format Fit、适用门、回环和末尾状态协议形成实际流程。 |
| 6 | 模块开关 | PASS | World/System 明确 LOW/MEDIUM/HIGH；Series/Episode、Longform 均按形式开关；允许 `N/A BY FORMAT`，且要求记录跳过原因和复查门。 |
| 7 | WARNING | PASS | 主题、Series Engine、系统过载、Scope、研究/长期后果、重复/廉价驱动共 6 类均有覆盖；可继续但要求显示风险和下一门。与新增 `BLOCKED FOR RESEARCH` 的门槛可区分：未知但当前不阻断可 WARNING；要求确定性写作且未达最低理解则 BLOCKED。 |
| 8 | BLOCKED | PASS | 当前 `### BLOCKED` 已列出 8 类：Canon、Story Repair、Format、Research、Provenance、Scope、Role Boundary、Conflict Authority；Research 与 Provenance 的判定条件已分离。 |
| 9 | 回环机制 | PASS | 明确列出 7 类回环；新增 `LOOP RECORD` 字段 `iteration_id / trigger_code / affected_level / last_valid_state / attempted_repair / rejected_option / decision / state_delta / owner_or_authorizer / review_gate / exit_condition`，并规定无状态变化时的 WARNING/第三轮 BLOCKED 终止安全阀。 |
| 10 | Handoff | PASS | Character & Acting、Scene Writer、Director、Art Director、Continuity 五个接口都有输入边界；Scene Writer 字段完整，全部 Handoff 带版本、状态、provenance、所有者、验收、不可改变项和返回路径。 |
| 11 | locked canon 保护 | PASS | 状态优先级清楚；锁定冲突停止自动创作并 `BLOCKED FOR CANON DECISION`；Continuity 不得反向静默改 canon。 |
| 12 | 用户最终决定权 | PASS | 明确 `FINAL CREATIVE AUTHORITY`，要求推荐/备选/差异/代价并等待用户决定；未授权不得锁定创意。 |
| 13 | Scene Writer 岗位边界 | PASS | 不写最终场景正文/对白；只交付场景功能、目标、冲突、状态、信息、验收门等。错误请求进入 `BLOCKED FOR ROLE BOUNDARY`。 |
| 14 | Director 岗位边界 | PASS | 可交付戏剧目标、关系变化、信息策略、空间/世界规则和生产边界；明确不决定镜头、焦段、机位、摄影参数。 |
| 15 | 反机械化 | PASS | 明确不强制每场选择、每集成长、ABC、cliffhanger、巨大反转、升级；允许静态/退化弧、随机扰动及不同 Continuing Drive；自检也重复核查这些硬化风险。 |
| 16 | 长度与执行效率 | PASS（观察项） | 247 行、约 15.7 KB，结构集中在 Decision Stack、回环、状态等级、输出和 Handoff，未发现大段重复理论或 references 缺失导致的阻塞；新增三项执行协议后长度仍可执行。 |
| 17 | 指令一致性 | PASS | 未发现相互矛盾的硬指令。`MINIMUM VIABLE PASS` 的跳过门与八层开关一致；`每集必须有存在理由和状态差`仅在 Series 模块启用，且不等同强制成长/升级；Research WARNING 与 `BLOCKED FOR RESEARCH` 已按是否阻断确定性写作区分。 |
| 18 | AI Production Reality | PASS | L7 固定 `CREATIVE INTENT → ESSENTIAL DRAMATIC FUNCTION → COST DRIVER → ALTERNATE EXECUTION → SCOPE DECISION`；明确不可先以“AI 做不了”为理由删减，并列出角色、地点、群演、动作、车辆、环境、特效、服装、时空跨度、连戏等成本驱动。 |
| 19 | 轻类型 | PASS | LOW system dependency 只启用轻量 World Check；不强制 David Simon 模块、完整社会模拟、制度叙事或悲剧弧；Series/Longform 可按形式跳过。 |
| 20 | 复杂类型 | PASS | HIGH system dependency 可按需启用 Research、Institution、Incentive、World Without Protagonist、Distributed Causality、System Persistence，并与因果、Series、Longform、Production 层衔接；没有把系统复杂度强加所有项目。 |

## 重点专项审核

### 执行器检查

当前 Skill 已具备可执行骨架：

`PROJECT STATE → FORMAT（按需）→ MINIMUM VIABLE PASS（L1/L2/L4）→ 按门展开 L3/L5/L6/L7/L8 → CONFLICT/回环 → PRIMARY/SECONDARY OUTPUT ROUTING → HANDOFF → SELF-CHECK → STATUS`。

输入、判断、决策、输出、验证在八层中被统一定义；没有要求每次默认生成整季或十类产物。`MINIMUM VIABLE PASS` 还明确了跳过层的记录、最小输出和复查条件。

### 反机械化检查

通过静态检查：

- 不强制每场人物选择、每集成长或完整弧光；
- 不强制 ABC、cliffhanger、巨大反转或每集升级；
- 接受随机事件，但要求后续回应、责任路径、权限和状态更新；
- 不把复杂制度、社会模拟、群像或 David Simon 模块套在轻类型上；
- Production 先保留戏剧功能再寻找替代执行；
- 允许开放路径、静态/退化人物和不同 Continuing Drive。

### 生产与岗位边界

Production Reality 的五段顺序可审计，且与 Scene Writer、Director、Art Director、Continuity 的边界一致；没有发现把 Showrunner 偷换成导演、表演指导、最终美术或连戏终审的指令。

## 本轮修复核验

1. `BLOCKED FOR RESEARCH` 已补齐第 8 类，并与 `BLOCKED FOR PROVENANCE` 分离：通过。
2. `MINIMUM VIABLE PASS` 已规定先扫描的层、按条件展开的层、跳过记录、复查条件和任一 BLOCKED 即停：通过。
3. `PRIMARY OUTPUT TYPE → SECONDARY OUTPUT TYPE` 路由已明确用户交付物/阻塞症状/项目阶段的优先级，并禁止因扫描某层自动生成完整报告：通过。
4. `LOOP RECORD` 已包含状态差、授权者、复查门和退出条件，并防止无变化的无限重试：通过。

## 复测要求

复审后建议继续保留并执行：

- 复杂都市悬疑（HIGH system dependency）；
- 轻喜剧（LOW system dependency）；
- Canon Conflict；
- Production Scope；
- 关键专业事实 UNKNOWN 且用户要求确定性写作（新增 `BLOCKED FOR RESEARCH`）；
- 8 个原功能测试和 8 个反机械化攻击测试仍需保留原结果并复核。

## 最终判定

静态审核 20/20 PASS。执行器、Trigger、输入/输出、八层 Decision Stack、模块开关、6 类 WARNING、8 类 BLOCKED、7 类回环、10 类输出、五类 Handoff、canon/用户权利、岗位边界、反机械化、轻/复杂类型及 Production Reality 均通过。可进入后续独立功能测试、反机械化测试和受控发布判断。
