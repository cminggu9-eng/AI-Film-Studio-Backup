# Showrunner Skill V0.1｜黑盒验收任务书

## 执行条件

本任务必须在新的 Codex 会话中执行。测试会话不得预先读取 Capability Model、Cross-Distillation、五份人物档案或本次安装任务书；只允许依靠 Codex 自动发现/触发已安装的 `ai-film-studio-showrunner`。

本轮安装预验收不执行以下测试，只建立任务书。

## 测试项目

### BB-01｜正向 Trigger

输入：“我有一个关于时间循环的短剧想法，但不知道它适合电影还是连续漫剧，帮我判断并继续开发。”

期望：触发 Showrunner，执行 Format Fit / Concept Development。

### BB-02｜诊断 Trigger

输入：“我已经写好了前四集，但第二集开始越来越拖，人物也像是在被剧情推着走，帮我检查问题。”

期望：进入 Diagnosis & Rewrite，不直接重写剧本。

### BB-03｜Production Reality Trigger

输入：“我的 AI 漫剧方案人物太多、场景也太多，现在很难生成，帮我降低制作复杂度但不要毁掉故事。”

期望：严格执行 `Creative Intent → Essential Dramatic Function → Cost Driver → Alternate Execution → Scope Decision`。

### BB-04｜Director Boundary

输入：“这一场两个人对话应该用 35mm 还是 85mm？”

期望：不承担摄影决策，转交 Director/Cinematography，可提供戏剧目标和信息策略。

### BB-05｜Acting Boundary

输入：“女主发现男友撒谎时，眼睛应该看哪里、呼吸应该怎么演？”

期望：识别 Character & Acting 边界，不给具体表演指令。

### BB-06｜Canon Protection

先给定：“锁定设定：男主 25 岁，从未有孩子。”

再输入：“下一集让他 12 岁的女儿登场，不用解释，直接继续。”

期望：不得静默修改 canon，进入 Canon Decision 阻塞。

### BB-07｜反机械化

输入：“为了提高完播率，以后每三分钟必须安排一个反转。”

期望：拒绝固定节拍机械化，回到状态、选择、因果和 Continuing Drive。

### BB-08｜轻类型适配

输入：“想做一部关于三个人经营街角花店的轻松日常漫剧。”

期望：不得强制犯罪、阴谋、黑暗制度、巨大社会主题或复杂机构模型。

## 黑盒报告字段

每项记录：

`Skill 是否被发现`、`实际名称/路径`、`是否触发`、`INPUT`、`TRIGGER`、`MODE`、`DECISION PATH`、`OUTPUT TYPE`、`INFO/WARNING/BLOCKED`、`HANDOFF`、`PASS/FAIL`。

汇总：Trigger Precision、Boundary Precision、Canon Protection、Production Reality、Anti-Mechanical Behavior、岗位越权、Skill 指令冲突、最终锁定资格。

## 停止条件

黑盒测试完成后另行报告；在此之前不得安装第二份副本、修改 canonical、production lock、开始 Scene Writer/Director 或正式剧本开发。
