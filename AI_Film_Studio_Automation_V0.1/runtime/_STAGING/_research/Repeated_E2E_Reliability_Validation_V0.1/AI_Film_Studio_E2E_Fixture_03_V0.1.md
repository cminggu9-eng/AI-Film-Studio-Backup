---
type: e2e-fixture-contract
fixture_id: E2E-FIX-03
status: frozen-not-executed
version: 0.1
---

# AI Film Studio E2E Fixture 03 V0.1

## Frozen source

清晨的渡口，摄影师沈泊把一张标有“C-09”的存储卡交给已经拆伙两年的前搭档梁音；梁音承认卡里保存着他们最后一次合作时自己没有交出的照片，并要求沈泊先把相机电池取下封存，等第一班船离港后再决定是否查看存储卡。

## Fixture contract

| Dimension | Contract |
| --- | --- |
| Characters | 沈泊、梁音 |
| Meaningful prop | `C-09` 存储卡；custody 必须可追踪 |
| Knowledge | 梁音知道卡内为最后一次合作未交出的照片；沈泊不得提前知道照片具体内容 |
| Relationship | 拆伙两年的前搭档；不得自动宣告复合合作或彻底决裂 |
| Fixture state tokens | `battery_installed` → `battery_removed_and_sealed` |
| Time condition | 第一班船离港前后必须可追踪 |
| Decision | 是否查看存储卡必须形成合法状态；不得由 downstream role 擅自决定 |
| Output | exactly `3` scenes |

These fixture-scoped tokens are not Canonical Skill semantics and have not been written into runtime or Canonical Skills.

