#!/usr/bin/env python3
"""Compare repository files against a JSON SHA-256 manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    expected = json.loads(args.manifest.read_text(encoding="utf-8"))
    rows = []
    for name, want in sorted(expected.items()):
        path = Path(name)
        got = digest(path) if path.is_file() else None
        rows.append({"path": name, "expected": want, "actual": got, "match": got == want})
    print(json.dumps({"checked": len(rows), "matched": sum(row["match"] for row in rows), "mismatches": [row for row in rows if not row["match"]]}, indent=2))
    return 0 if all(row["match"] for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
