#!/usr/bin/env python3
from pathlib import Path
import sys


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("CLAUDE.md")
    if not path.exists():
        print(f"ERROR: {path} not found")
        return 1

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    long_lines = [i + 1 for i, line in enumerate(lines) if len(line) > 120]
    todo_hits = [i + 1 for i, line in enumerate(lines) if "TODO" in line]

    print(f"File: {path}")
    print(f"Lines: {len(lines)}")
    print(f"Characters: {len(text)}")

    if len(lines) > 200:
        print("WARN: file exceeds 200 lines; consider splitting rules into .claude/rules/")
    if long_lines:
        print(f"WARN: long lines at: {', '.join(map(str, long_lines[:10]))}")
    if todo_hits:
        print(f"WARN: TODO markers at: {', '.join(map(str, todo_hits[:10]))}")

    if len(lines) <= 200 and not todo_hits:
        print("OK: CLAUDE.md is compact and has no TODO markers")
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
