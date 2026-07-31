#!/usr/bin/env python3
"""Write the release SHA-256 manifest in stable path order."""

from __future__ import annotations

import hashlib
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
ARCHIVE_ROOT = PROJECT.parent
OUTPUT = ARCHIVE_ROOT / "MANIFEST.sha256"
INCLUDE = (PROJECT, ARCHIVE_ROOT / "agent_outputs")


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(2**20), b""):
            result.update(chunk)
    return result.hexdigest()


def eligible(path: Path) -> bool:
    relative_parts = path.relative_to(ARCHIVE_ROOT).parts
    return (
        "__pycache__" not in relative_parts
        and path.suffix not in {".pyc", ".pyo"}
        and path != OUTPUT
    )


def main() -> None:
    paths = sorted(
        path
        for root in INCLUDE
        for path in root.rglob("*")
        if path.is_file() and eligible(path)
    )
    lines = [
        f"{digest(path)}  {path.relative_to(ARCHIVE_ROOT)}"
        for path in paths
    ]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT} with {len(lines)} files")


if __name__ == "__main__":
    main()
