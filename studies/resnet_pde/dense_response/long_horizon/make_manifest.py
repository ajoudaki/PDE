#!/usr/bin/env python3
"""Write checksums after tests, experiments, and analysis have completed."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXCLUDED_PARTS = {"__pycache__", ".mplcache"}
EXCLUDED_NAMES = {"SHA256SUMS", "manifest.json"}


def main() -> None:
    records = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.name in EXCLUDED_NAMES:
            continue
        data = path.read_bytes()
        records.append(
            {
                "path": str(path.relative_to(ROOT)),
                "size_bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    metadata = ROOT / "metadata"
    metadata.mkdir(parents=True, exist_ok=True)
    (metadata / "manifest.json").write_text(
        json.dumps(records, indent=2), encoding="utf-8"
    )
    (metadata / "SHA256SUMS").write_text(
        "".join(f"{x['sha256']}  {x['path']}\n" for x in records),
        encoding="utf-8",
    )
    print(f"wrote checksums for {len(records)} files")


if __name__ == "__main__":
    main()
