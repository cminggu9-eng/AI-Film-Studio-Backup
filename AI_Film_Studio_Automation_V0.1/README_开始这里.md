# AI Film Studio 自动化层 V0.1

这套文件不会替换你的 Obsidian Vault。

它负责：

**Codex → 女娲 Skill → _STAGING → Codex 审核 → 发布脚本 → Obsidian**

---

## 第一步｜放到固定位置

推荐解压到：

`E:\AI-Film-Studio-Automation\`

不要解压进 Obsidian Vault 内部。

---

## 第二步｜配置你的 Vault 路径

在这个文件夹空白处打开 PowerShell，然后运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_windows.ps1
```

脚本会让你粘贴 Obsidian Vault 的完整文件夹路径。

成功后会生成：

`studio.config.json`

---

## 第三步｜确认女娲 Skill

Codex 必须使用你已经拥有的女娲蒸馏 Skill。

如果它是 Codex 已安装 Skill，不需要复制到这里。

如果 Codex 找不到它，请不要让 Codex用通用提示词代替；先解决 Skill 可见性问题。

---

## 第四步｜用 Codex 打开这个文件夹

在 Codex 中把本文件夹作为本地项目打开。

第一条命令建议发送：

> 读取 AGENTS.md 和 PUBLISH_RULES.md。先运行自动化管线自检，不要开始人物蒸馏。检查 studio.config.json、Python、Vault 路径和发布脚本是否正常。自检通过后停止并报告结果。

---

## 第五步｜自检通过后

再发送：

> 按 tasks/showrunner/Craig_Mazin_Distillation_Task_V0.1.md 执行第一份 Showrunner 蒸馏任务。必须调用现有女娲 Skill。先写入 _STAGING，Codex 审核通过后才允许发布到 Obsidian。

---

## 当前安全原则

- 临时结果不直接进入 Obsidian
- `status: locked` 永不自动覆盖
- 发布前必须 `status: approved`
- 发布前必须 `review_result: passed`
- 成功发布后自动写工作日志
