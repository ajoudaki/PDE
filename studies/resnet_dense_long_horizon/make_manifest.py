#!/usr/bin/env python3
"""Write checksums after tests, experiments, and analysis have completed."""

from __future__ import annotations

import hashlib
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from studies._output_paths import reject_output_links

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
    reject_output_links(path)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    parser.add_argument("--verify", action="store_true",
                        help="Read and verify the selected schema-2 manifest; never rewrite it.")
    args = parser.parse_args()
    output_root = validate_output_root(args.output_root)
    if not output_root.is_dir():
        raise SystemExit("No fresh run directory; run the selected workflow first.")
    if args.verify:
        verify_manifest(output_root / "metadata" / "manifest.json")
        return
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
    validate_output_root(output_root)
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


def verify_manifest(path: Path) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("schema") != 2 or set(manifest.get("roots", {})) != {"source", "run"}:
        raise ValueError("Expected a schema-2 source/run manifest, not a historical seal.")
    roots = {key: Path(value).resolve() for key, value in manifest["roots"].items()}
    if roots["run"] != path.resolve().parents[1]:
        raise ValueError("Manifest run root differs from the selected run directory.")
    records = manifest["files"]
    seen = set()
    for row in records:
        key = (row["root"], row["path"])
        if key in seen or key[0] not in roots:
            raise ValueError("Duplicate entry or unknown manifest root.")
        seen.add(key)
        relative = Path(key[1])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Manifest entries must remain within their declared root.")
        target = (roots[key[0]] / relative).resolve()
        if not target.is_relative_to(roots[key[0]]):
            raise ValueError("Manifest entry escapes its declared root.")
        content = target.read_bytes()
        if len(content) != row["size_bytes"] or hashlib.sha256(content).hexdigest() != row["sha256"]:
            raise ValueError(f"Checksum mismatch: {key[0]}/{key[1]}")
    expected = "".join(f"{row['sha256']}  {row['root']}/{row['path']}\n" for row in records)
    if path.with_name("SHA256SUMS").read_text(encoding="utf-8") != expected:
        raise ValueError("SHA256SUMS disagrees with the schema-2 manifest.")
    print(f"verified {len(records)} source/run checksums (read-only)")


if __name__ == "__main__":
    main()
