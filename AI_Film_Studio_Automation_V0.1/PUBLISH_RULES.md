# AI Film Studio — Obsidian Publication Rules V0.1

## Purpose

This file defines when Codex is allowed to move a 女娲 distillation result from staging into the official Obsidian Vault.

## Required staging location

All unapproved outputs must live under:

`runtime/_STAGING/`

The official Vault is not a scratchpad.

## Required frontmatter

A publishable distillation note must begin with valid YAML frontmatter containing at least:

```yaml
---
type: distillation
status: approved
review_result: passed
version: 0.1
subject: <name or topic>
---
```

If either `status` is not `approved` or `review_result` is not `passed`, publication must fail.

## Required sections for `type: distillation`

The note must contain all of the following headings:

- `## 蒸馏目标`
- `## 核心判断原则`
- `## 工作流程`
- `## 诊断问题`
- `## 失败模式`
- `## 修正方法`
- `## 禁止继承`
- `## 可 Skill 化规则`
- `## 证据与来源`
- `## Codex 审核结论`

## Evidence rules

Each meaningful method claim should be traceable to source material or explicitly labelled as an inference.

Do not fabricate:
- interviews
- lectures
- course contents
- quotations
- source URLs
- production anecdotes

The goal is method extraction, not creator imitation.

## Locked note protection

Before writing a destination note:

- if it does not exist: create it
- if it exists and `status: locked`: abort
- if it exists and is not locked: create an automatic backup before replacing it

Backups go under:

`99_ARCHIVE/_AUTO_BACKUP/<timestamp>/...`

## Atomic publication

The publication script must write a temporary file first and then replace the destination atomically where possible.

## Staging lifecycle

After successful publication, move the staging file to:

`runtime/_PUBLISHED/<YYYY-MM-DD>/`

Do not delete it.

## Logging

Every successful publication must append an entry to:

`00_HOME/工作日志/<YYYY-MM-DD>.md`

The log should include:
- time
- subject
- destination
- version
- staging source
- whether an existing note was backed up

## Progress update

A checkbox may be updated only after publication succeeds.
If the exact checkbox text is not found, publication still succeeds but the log must record that progress was not updated.

## User authority

Codex may approve a methodology artifact for storage, but the user remains the final authority over:
- creative canon
- project direction
- whether a Skill becomes production-locked
