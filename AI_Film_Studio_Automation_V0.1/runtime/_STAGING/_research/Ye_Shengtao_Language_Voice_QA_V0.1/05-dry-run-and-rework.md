# 原创干跑与定向返工记录 V0.1

## 首轮结果

|测试|首轮|
|---|---|
|TEST A｜主题总结 QA|PASS|
|TEST B｜人工二元|PASS WITH MEANING WARNING|
|TEST C｜名词化与空泛|PASS|
|TEST D｜自然句 NO CHANGE|PASS|
|TEST E｜Project Brief|PASS|
|TEST F｜伪术语|首稿遗漏|
|Rewrite Mode｜Trailer Copy 转创作讨论|PASS|
|Read-Aloud 非机械化|PASS|
|Over-Editing Benefit Test|FAIL|

## 发现的问题

首稿 Over-Editing 的五问混用正反极性：既询问“原句是否已经清楚”和“改后是否丢失信息”，又统一要求所有问题回答“是”才允许修改。该门无法稳定执行，并可能把已经工作中的文本误送入修改。

分类：`SKILLIZATION LOGIC ISSUE`，不属于证据不足。

同轮红队还发现：任务要求的伪术语案例未进入正式干跑；`NO CHANGE` 的运行状态一处为默认启发式、一处为硬门，分类不一致。

## 定向返工 1

只把 Benefit Test 改为同向验收：

1. 原句存在可指认问题；
2. 修改确实解决问题；
3. 修改保留语气、含混、专业精度、节奏与角色状态；
4. 修改没有更假或更偏离原意；
5. 收益大于 Meaning / Voice 风险。

五项全为“是”才修改；任何“否/不确定”进入 `KEEP / NO CHANGE` 或请求上下文。

## 定向复测

- Over-Editing Benefit Test：`PASS`。
- TEST D：`PASS`；原句不存在可指认问题，第一门即停止修改。
- TEST E：`PASS`；R2 Project Brief 的目标、范围、阶段限制和术语均适配用途，保持原文。
- TEST F：`PASS`；不因陌生删除，也不因类似专业词放行；上下文不足进入 `TERM PLAUSIBILITY WARNING`。
- `NO CHANGE`：统一为 `AI FILM STUDIO SYNTHESIS｜HARD CONSTRAINT`；叶圣陶材料只作为“正确时可不改”的来源基础。
- 其他干跑未受改动影响，无需重跑。

返工次数：`1`。
