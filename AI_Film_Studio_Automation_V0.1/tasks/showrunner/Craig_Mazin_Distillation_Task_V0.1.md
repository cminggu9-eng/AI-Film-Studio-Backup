# Craig Mazin｜Showrunner 能力蒸馏任务书 V0.1

## 任务性质

这是 AI Film Studio 的第一份端到端蒸馏任务，也是自动发布管线的正式试运行。

## 目标

从可验证材料中提取 Craig Mazin 在以下方面可复用的决策方法：

1. 主题 / central dramatic argument 如何参与故事设计
2. 人物错误认知、目标、选择与变化如何形成结构
3. 情节如何由人物行动和因果关系推进
4. 如何诊断“机械套结构”而非人物驱动的故事
5. 如何把方法转化为 Showrunner 可执行的检查问题与流程

## 不要提取

- 具体作品情节
- 具体人物设计
- 签名式对白
- 视觉风格
- 可识别的表达模仿
- “像 Craig Mazin 一样写”的人格模拟

## 证据要求

优先使用：
- 本人公开课程、讲座、播客、访谈
- 本人参与的 Scriptnotes 等第一手创作讨论
- 可核验的本人公开文字材料

二手总结只能辅助，不能成为关键方法论唯一依据。

## 执行流程

1. Codex 读取本任务书。
2. Codex 定位并读取现有女娲 Skill。
3. Codex 准备证据材料与来源清单。
4. 女娲执行单人能力蒸馏。
5. 结果写入：
   `runtime/_STAGING/Craig_Mazin_Showrunner_Distillation_V0.1.md`
6. Codex 按 `PUBLISH_RULES.md` 审核。
7. 不通过：返工，不发布。
8. 通过后，将 frontmatter 改为：
   `status: approved`
   `review_result: passed`
9. 执行发布：

```powershell
python scripts/publish_to_obsidian.py `
  --source "runtime/_STAGING/Craig_Mazin_Showrunner_Distillation_V0.1.md" `
  --dest "02_DISTILLATION/编剧研究/Craig Mazin｜Showrunner能力蒸馏 V0.1.md" `
  --title "Craig Mazin Showrunner 能力蒸馏 V0.1"
```

## 完成标准

只有以下条件全部满足才算完成：

- 女娲 Skill 确实被调用 / 遵循
- 有可核验来源
- 输出不是人物介绍
- 输出不是风格模仿
- 形成判断原则
- 形成工作流程
- 形成诊断问题
- 形成失败模式与修正方法
- 形成可 Skill 化规则
- Codex 审核通过
- 发布脚本成功
- Obsidian 中出现正式档案
- 工作日志生成
