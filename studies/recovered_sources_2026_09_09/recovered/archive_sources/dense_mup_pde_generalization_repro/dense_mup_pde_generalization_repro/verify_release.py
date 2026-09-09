#!/usr/bin/env python3
"""Verify every file in the compact source-first release."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"
PROVENANCE = ROOT / "RELEASE_PROVENANCE.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_bound_file(relative: str, expected: str) -> None:
    path = (ROOT / relative).resolve()
    if ROOT.resolve() not in path.parents:
        raise SystemExit(f"{relative}: provenance path escapes release root")
    if not path.is_file() or sha256(path) != expected:
        raise SystemExit(f"{relative}: provenance hash mismatch")


def main() -> None:
    if not MANIFEST.is_file():
        raise SystemExit("missing SHA256SUMS.txt")
    checked = 0
    for line_number, line in enumerate(MANIFEST.read_text().splitlines(), 1):
        if not line:
            continue
        try:
            expected, relative = line.split("  ", 1)
        except ValueError as error:
            raise SystemExit(
                f"SHA256SUMS.txt:{line_number}: malformed line"
            ) from error
        path = (ROOT / relative).resolve()
        if ROOT.resolve() not in path.parents:
            raise SystemExit(f"{relative}: path escapes release root")
        if not path.is_file():
            raise SystemExit(f"{relative}: missing")
        observed = sha256(path)
        if observed != expected:
            raise SystemExit(f"{relative}: checksum mismatch")
        checked += 1

    record = json.loads(PROVENANCE.read_text())
    frozen = record["frozen_scientific_source"]
    verify_bound_file(frozen["path"], frozen["file_sha256"])
    frozen_manifest = json.loads((ROOT / frozen["path"]).read_text())
    if frozen_manifest["aggregate_sha256"] != frozen["declared_aggregate_sha256"]:
        raise SystemExit("frozen scientific aggregate mismatch")
    if len(frozen_manifest["files"]) != frozen["file_count"]:
        raise SystemExit("frozen scientific file-count mismatch")

    execution = record["execution_amendment"]
    verify_bound_file(execution["record"], execution["record_sha256"])
    verify_bound_file(
        execution["historical_wrapper"],
        execution["historical_wrapper_sha256"],
    )
    verify_bound_file(
        execution["verified_reproduction_wrapper"],
        execution["verified_reproduction_wrapper_sha256"],
    )

    analysis = record["analysis_amendment"]
    verify_bound_file(analysis["record"], analysis["record_sha256"])
    verify_bound_file(analysis["wrapper"], analysis["wrapper_sha256"])

    for item in record["stage_seals"].values():
        verify_bound_file(item["path"], item["sha256"])
    verify_bound_file(
        record["processed_summary"]["path"],
        record["processed_summary"]["sha256"],
    )
    for item in record["release_documents"].values():
        verify_bound_file(item["path"], item["sha256"])

    print(
        f"release verification passed ({checked} files; "
        "provenance chain valid)"
    )


if __name__ == "__main__":
    main()
