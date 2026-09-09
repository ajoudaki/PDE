#!/usr/bin/env python3
"""Freeze the proof-obligation study before any scientific trajectory exists."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import tempfile

import numpy as np
import scipy


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
PROTOCOL = ROOT / "protocol" / "preregistered_protocol.json"
SEAL = ROOT / "results" / "seals" / "FROZEN_INPUTS.json"
SCIENTIFIC_SUFFIXES = {".npz", ".npy", ".csv", ".parquet"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode()


def reject_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key in protocol: {key}")
        result[key] = value
    return result


def source_inventory() -> list[Path]:
    canonical = [
        WORKSPACE
        / "activation_linearity_smoking_gun"
        / "source"
        / "src"
        / "dense_reference"
        / "core.py",
        WORKSPACE
        / "activation_linearity_smoking_gun"
        / "source"
        / "src"
        / "dense_pde"
        / "operator_galerkin.py",
        WORKSPACE
        / "activation_linearity_smoking_gun"
        / "source"
        / "src"
        / "activations.py",
    ]
    local = [PROTOCOL]
    for directory in (ROOT / "protocol", ROOT / "source", ROOT / "tests"):
        if directory.exists():
            local.extend(sorted(directory.glob("*.py")))
    paths = canonical + list(dict.fromkeys(local))
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"freeze input is missing: {missing}")
    return paths


def relative_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path.relative_to(WORKSPACE))


def assert_no_evidence() -> None:
    results = ROOT / "results"
    if not results.exists():
        return
    offenders = [
        path
        for path in results.rglob("*")
        if path.is_file()
        and path != SEAL
        and (
            path.suffix.lower() in SCIENTIFIC_SUFFIXES
            or path.name.endswith(".partial")
        )
    ]
    if offenders:
        raise RuntimeError(
            "scientific evidence exists before the first freeze: "
            + ", ".join(str(path) for path in offenders)
        )


def atomic_write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".partial",
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(canonical_json(value))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def main() -> None:
    if SEAL.exists():
        raise RuntimeError(f"freeze already exists: {SEAL}")
    assert_no_evidence()
    protocol = json.loads(
        PROTOCOL.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_pairs,
    )
    status = str(protocol.get("status", ""))
    if status != "preregistered_before_new_scientific_trajectories":
        raise RuntimeError(
            "protocol status must be "
            "'preregistered_before_new_scientific_trajectories'"
        )
    files = []
    seen_labels: set[str] = set()
    for path in source_inventory():
        label = relative_label(path)
        relative = Path(label)
        if (
            not label
            or relative.is_absolute()
            or ".." in relative.parts
            or "." in relative.parts
            or label in seen_labels
        ):
            raise RuntimeError(f"unsafe or duplicate freeze label: {label!r}")
        seen_labels.add(label)
        files.append(
            {
                "path": label,
                "sha256": sha256(path),
                "size_bytes": path.stat().st_size,
            }
        )
    tree_hash = hashlib.sha256(
        b"".join(
            item["path"].encode()
            + b"\0"
            + item["sha256"].encode()
            + b"\0"
            for item in files
        )
    ).hexdigest()
    manifest = {
        "schema_version": 1,
        "status": "frozen_before_new_scientific_trajectories",
        "protocol_sha256": sha256(PROTOCOL),
        "source_tree_sha256": tree_hash,
        "files": files,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "scientific_evidence_count_at_freeze": 0,
        "notes": [
            "Existing parent-study archives are prior evidence and are outside this sibling study's results directory.",
            "No wall-clock timestamp is part of the scientific identity.",
        ],
    }
    atomic_write_json(SEAL, manifest)
    print(
        json.dumps(
            {
                "seal": str(SEAL),
                "protocol_sha256": manifest["protocol_sha256"],
                "source_tree_sha256": tree_hash,
                "file_count": len(files),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
