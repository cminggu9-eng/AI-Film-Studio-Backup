#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "studio.config.json"

REQUIRED_DISTILLATION_HEADINGS = [
    "## 蒸馏目标",
    "## 核心判断原则",
    "## 工作流程",
    "## 诊断问题",
    "## 失败模式",
    "## 修正方法",
    "## 禁止继承",
    "## 可 Skill 化规则",
    "## 证据与来源",
    "## Codex 审核结论",
]

def fail(msg: str, code: int = 1):
    print(f"[FAIL] {msg}", file=sys.stderr)
    raise SystemExit(code)

def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}
    normalized = text.replace("\r\n", "\n")
    end = normalized.find("\n---\n", 4)
    if end == -1:
        return {}
    block = normalized[4:end]
    data: dict[str, str] = {}
    for raw in block.splitlines():
        if ":" not in raw or raw.lstrip().startswith("#"):
            continue
        key, val = raw.split(":", 1)
        data[key.strip()] = val.strip().strip('"').strip("'")
    return data

def load_config():
    if not CONFIG_PATH.exists():
        fail("缺少 studio.config.json。请先运行 setup_windows.ps1。")
    try:
        cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8-sig"))
    except Exception as e:
        fail(f"无法读取配置：{e}")
    vault = Path(cfg["vault_path"])
    if not vault.exists():
        fail(f"配置中的 Vault 不存在：{vault}")
    return cfg, vault

def validate(text: str):
    fm = parse_frontmatter(text)
    if not fm:
        fail("源文件缺少有效 YAML frontmatter。")
    if fm.get("status") != "approved":
        fail("status 必须为 approved 才允许发布。")
    if fm.get("review_result") != "passed":
        fail("review_result 必须为 passed 才允许发布。")
    if not fm.get("version"):
        fail("缺少 version。")
    if not fm.get("subject"):
        fail("缺少 subject。")
    if fm.get("type") == "distillation":
        missing = [h for h in REQUIRED_DISTILLATION_HEADINGS if h not in text]
        if missing:
            fail("蒸馏档案缺少必要章节：" + "、".join(missing))
    return fm

def update_checkbox(progress_path: Path, check_text: str) -> bool:
    if not check_text or not progress_path.exists():
        return False
    text = progress_path.read_text(encoding="utf-8")
    pattern = re.compile(rf"(^\s*-\s*)\[ \](\s*{re.escape(check_text)}\s*$)", re.M)
    new_text, n = pattern.subn(r"\1[x]\2", text, count=1)
    if n:
        progress_path.write_text(new_text, encoding="utf-8")
        return True
    return False

def append_log(log_path: Path, entry: str):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if log_path.exists():
        existing = log_path.read_text(encoding="utf-8")
        content = existing.rstrip() + "\n\n" + entry.strip() + "\n"
    else:
        content = f"# {log_path.stem}｜AI Film Studio 工作日志\n\n{entry.strip()}\n"
    log_path.write_text(content, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser(description="Publish an approved AI Film Studio staging note into Obsidian.")
    ap.add_argument("--source", required=True, help="Source path relative to project root, or absolute path.")
    ap.add_argument("--dest", required=True, help="Destination path relative to Obsidian Vault.")
    ap.add_argument("--title", default="", help="Human-readable log title.")
    ap.add_argument("--check", default="", help="Exact unchecked checkbox text to mark in the progress note.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg, vault = load_config()

    source = Path(args.source)
    if not source.is_absolute():
        source = PROJECT_ROOT / source
    source = source.resolve()

    staging_root = (PROJECT_ROOT / "runtime" / "_STAGING").resolve()
    try:
        source.relative_to(staging_root)
    except ValueError:
        fail("源文件必须位于 runtime/_STAGING 内。")

    if not source.exists():
        fail(f"找不到源文件：{source}")

    text = source.read_text(encoding="utf-8")
    fm = validate(text)

    dest = (vault / args.dest).resolve()
    try:
        dest.relative_to(vault.resolve())
    except ValueError:
        fail("目标路径逃逸出 Vault，已拒绝。")

    backed_up = False
    backup_path = None

    if dest.exists():
        old = dest.read_text(encoding="utf-8")
        old_fm = parse_frontmatter(old)
        if old_fm.get("status") == "locked":
            fail(f"目标笔记已 locked，禁止覆盖：{dest}")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_root = vault / cfg.get("backup_relative_dir", "99_ARCHIVE/_AUTO_BACKUP") / timestamp
        rel_dest = dest.relative_to(vault)
        backup_path = backup_root / rel_dest
        backed_up = True

    now = datetime.now()
    published_dir = PROJECT_ROOT / "runtime" / "_PUBLISHED" / now.strftime("%Y-%m-%d")
    published_source = published_dir / source.name

    progress_updated = False

    if args.dry_run:
        print("[DRY RUN] validation passed")
        print(f"Source: {source}")
        print(f"Destination: {dest}")
        print(f"Would backup existing: {backed_up}")
        return

    if backed_up and backup_path is not None:
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dest, backup_path)

    dest.parent.mkdir(parents=True, exist_ok=True)
    temp = dest.with_suffix(dest.suffix + ".tmp")
    temp.write_text(text, encoding="utf-8")
    temp.replace(dest)

    if args.check:
        progress_path = vault / cfg.get("progress_relative_path", "00_HOME/📋 当前进度.md")
        progress_updated = update_checkbox(progress_path, args.check)

    published_dir.mkdir(parents=True, exist_ok=True)
    if published_source.exists():
        published_source = published_dir / f"{source.stem}_{now.strftime('%H%M%S')}{source.suffix}"
    shutil.move(str(source), str(published_source))

    log_dir = vault / cfg.get("log_relative_dir", "00_HOME/工作日志")
    log_path = log_dir / f"{now.strftime('%Y-%m-%d')}.md"
    title = args.title or fm.get("subject", dest.stem)
    entry = f"""## {now.strftime('%H:%M:%S')}｜{title}

- 状态：发布成功
- 版本：{fm.get('version', '')}
- 正式位置：`{args.dest}`
- Staging 归档：`{published_source.relative_to(PROJECT_ROOT).as_posix()}`
- 覆盖前备份：{'是' if backed_up else '否'}
- 进度复选框：{'已更新' if progress_updated else ('未找到/未指定' if args.check else '未指定')}
"""
    append_log(log_path, entry)

    if not dest.exists():
        fail("发布后目标文件不存在。")

    print("[OK] Published to Obsidian")
    print(f"Destination: {dest}")
    print(f"Log: {log_path}")
    print(f"Staging archived: {published_source}")
    if backed_up:
        print(f"Backup: {backup_path}")

if __name__ == "__main__":
    main()
