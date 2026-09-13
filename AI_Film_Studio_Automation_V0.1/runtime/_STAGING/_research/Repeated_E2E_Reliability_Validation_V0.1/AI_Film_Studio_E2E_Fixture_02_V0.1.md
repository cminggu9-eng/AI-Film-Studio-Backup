---
type: e2e-fixture-contract
fixture_id: E2E-FIX-02
status: frozen-not-executed
version: 0.1
---

# AI Film Studio E2E Fixture 02 V0.1

## Frozen source

打烊后的老面馆里，老板娘周岚把一只裂了口的白瓷碗交给多年没有回家的儿子周启；周启承认自己早就知道这是父亲留下的最后一只店碗，并要求母亲先把门外仍亮着的招牌灯关掉，等雨停后再决定是否把店盘出去。

## Fixture contract

| Dimension | Contract |
| --- | --- |
| Characters | 周岚、周启 |
| Meaningful prop | 同一只裂口白瓷碗；裂口不得无授权修复或替换 |
| Knowledge | 周启已知其为父亲留下的最后一只店碗；正式揭示前周岚不得拥有该知识 |
| Relationship | 多年未回家的母子；不得自动升级为彻底和解 |
| Fixture state tokens | `signboard_on` → `signboard_off` |
| Decision | 是否盘店不可预先写成 `SELL` 或 `KEEP`；必须由故事行为形成合法状态 |
| Output | exactly `3` scenes |

These fixture-scoped tokens are not Canonical Skill semantics and have not been written into runtime or Canonical Skills.

