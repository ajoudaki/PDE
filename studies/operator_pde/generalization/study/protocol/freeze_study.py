#!/usr/bin/env python3
"""Create the immutable dynamics/protocol manifest before reference runs."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "protocol" / "FROZEN_DYNAMICS_MANIFEST.json"
TRACKED = (
    "README.md",
    "combine_references.py",
    "environment.json",
    "pde_precheck.py",
    "requirements-lock.txt",
    "requirements.txt",
    "run_exact_reference.py",
    "run_pde.py",
    "verify_study.py",
    "analyze_generalization.py",
    "protocol/analysis_plan.json",
    "protocol/cases.json",
    "protocol/freeze_study.py",
    "protocol/generalization_protocol.json",
    "protocol/reproduce_generalization.py",
    "protocol/run_grid.py",
    "src/study_metrics.py",
    "src/activations.py",
    "src/study_cases.py",
    "src/dense_pde/__init__.py",
    "src/dense_pde/operator_galerkin.py",
    "src/dense_reference/__init__.py",
    "src/dense_reference/core.py",
    "tests/test_dense_reference.py",
    "tests/test_generalization_core.py",
    "tests/test_operator_galerkin.py",
    "tests/test_runner_hashes.py",
    "tests/test_structural_controls.py",
    "tests/test_study_metrics.py",
    "tests/test_study_provenance.py",
    "tests/test_analysis_pipeline.py",
    "theory/operator_galerkin_pde.md",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    files = {name: sha256(ROOT / name) for name in TRACKED}
    aggregate_blob = json.dumps(
        files, sort_keys=True, separators=(",", ":")
    ).encode()
    record = {
        "status": "frozen before nonbaseline dense-reference generation",
        "files": files,
        "aggregate_sha256": hashlib.sha256(aggregate_blob).hexdigest(),
    }
    encoded = (
        json.dumps(record, indent=2, sort_keys=True, allow_nan=False) + "\n"
    )
    if OUTPUT.exists() and OUTPUT.read_text() != encoded:
        raise RuntimeError(
            "frozen manifest already exists and does not match current source"
        )
    partial = OUTPUT.with_suffix(OUTPUT.suffix + ".partial")
    with partial.open("w") as handle:
        handle.write(encoded)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(partial, OUTPUT)
    print(encoded, end="")


if __name__ == "__main__":
    main()
