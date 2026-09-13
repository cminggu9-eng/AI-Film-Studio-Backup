#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "studio.config.json"

def ok(msg): print(f"[OK] {msg}")
def warn(msg): print(f"[WARN] {msg}")
def fail(msg):
    print(f"[FAIL] {msg}")
    raise SystemExit(1)

if not CONFIG.exists():
    fail("studio.config.json 不存在；先运行 setup_windows.ps1。")

try:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8-sig"))
except Exception as e:
    fail(f"配置读取失败：{e}")

vault = Path(cfg.get("vault_path", ""))
if not vault.exists():
    fail(f"Vault 路径不存在：{vault}")
ok(f"Vault 路径存在：{vault}")

if not (vault / "00_HOME").exists():
    fail("Vault 缺少 00_HOME。")
ok("Vault 结构检查通过")

publisher = ROOT / "scripts" / "publish_to_obsidian.py"
if not publisher.exists():
    fail("缺少发布脚本。")
ok("发布脚本存在")

staging = ROOT / "runtime" / "_STAGING"
staging.mkdir(parents=True, exist_ok=True)
test_note = staging / "__pipeline_self_test__.md"
test_note.write_text("""---
type: distillation
status: approved
review_result: passed
version: 0.0-test
subject: pipeline-self-test
---

# Pipeline Self Test

## 蒸馏目标
test
## 核心判断原则
test
## 工作流程
test
## 诊断问题
test
## 失败模式
test
## 修正方法
test
## 禁止继承
test
## 可 Skill 化规则
test
## 证据与来源
test
## Codex 审核结论
test
""", encoding="utf-8")

cmd = [
    sys.executable, str(publisher),
    "--source", str(test_note),
    "--dest", "99_ARCHIVE/__PIPELINE_DRY_RUN__.md",
    "--title", "Pipeline Self Test",
    "--dry-run",
]
proc = subprocess.run(cmd, capture_output=True, text=True)
try:
    test_note.unlink(missing_ok=True)
except Exception:
    pass

if proc.returncode != 0:
    print(proc.stdout)
    print(proc.stderr)
    fail("发布脚本 dry-run 失败。")

ok("发布脚本 dry-run 通过")
print()
print("=== SELF TEST PASSED ===")
print("注意：这是 dry-run，没有向 Vault 写入测试笔记。")
