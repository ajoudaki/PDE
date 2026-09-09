#!/usr/bin/env python3
"""Write checksums after tests, experiments, and analysis have completed."""

from __future__ import annotations

import hashlib
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_ROOT = ROOT.parents[1] / "data" / "generated" / ROOT.name
EXCLUDED_PARTS = {"__pycache__", ".mplcache"}
EXCLUDED_NAMES = {"SHA256SUMS", "manifest.json"}


def validate_output_root(path: Path) -> Path:
    output = path.expanduser().resolve()
    repository = Path(__file__).resolve().parents[2]
    for protected in (repository / name for name in (
        "studies", "docs", "code", ".git", "data/historical",
        "data/original_backups", "data/runtime_cache",
    )):
        if output == protected or protected in output.parents or output in protected.parents:
            raise ValueError("Select fresh output, not source or retained evidence.")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    args = parser.parse_args()
    output_root = validate_output_root(args.output_root)
    if not output_root.is_dir():
        raise SystemExit("No fresh run directory; run the selected workflow first.")
    records = []
    for kind, base in (("source", ROOT), ("run", output_root)):
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            if any(part in EXCLUDED_PARTS for part in path.parts):
                continue
            if path.name in EXCLUDED_NAMES:
                continue
            data = path.read_bytes()
            records.append({
                "root": kind,
                "path": str(path.relative_to(base)),
                "size_bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            })
    metadata = output_root / "metadata"
    metadata.mkdir(parents=True, exist_ok=True)
    (metadata / "manifest.json").write_text(
        json.dumps({"schema": 2, "roots": {"source": str(ROOT), "run": str(output_root)},
                    "files": records}, indent=2), encoding="utf-8"
    )
    (metadata / "SHA256SUMS").write_text(
        "".join(f"{x['sha256']}  {x['root']}/{x['path']}\n" for x in records),
        encoding="utf-8",
    )
    print(f"wrote checksums for {len(records)} files")


if __name__ == "__main__":
    main()
