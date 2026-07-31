#!/usr/bin/env python3
"""Read-only verification of frozen source and regenerated study evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results" / "generalization"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_source(run_tests: bool) -> str:
    manifest_path = ROOT / "protocol" / "FROZEN_DYNAMICS_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    for relative, expected in manifest["files"].items():
        path = ROOT / relative
        if not path.exists() or sha256(path) != expected:
            raise RuntimeError(f"frozen source mismatch: {relative}")
    aggregate = hashlib.sha256(
        json.dumps(
            manifest["files"], sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    if aggregate != manifest["aggregate_sha256"]:
        raise RuntimeError("frozen source aggregate mismatch")
    if run_tests:
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(ROOT / "src")
        subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                "tests",
                "-v",
            ],
            cwd=ROOT,
            env=environment,
            check=True,
        )
    return aggregate


def verify_seal(path: Path) -> dict:
    record = json.loads(path.read_text())
    for relative, expected in record["files"].items():
        target = ROOT / relative
        if not target.exists() or sha256(target) != expected:
            raise RuntimeError(f"sealed evidence mismatch: {relative}")
    if len(record["files"]) != record["file_count"]:
        raise RuntimeError(f"{path.name}: file count mismatch")
    return record


def verify_evidence(run_tests: bool) -> None:
    aggregate = verify_source(run_tests)
    pde_path = RESULTS / "PDE_STAGE_SEAL.json"
    dense_path = RESULTS / "DENSE_STAGE_SEAL.json"
    processed_path = RESULTS / "PROCESSED_STAGE_SEAL.json"
    pde = verify_seal(pde_path)
    dense = verify_seal(dense_path)
    processed = verify_seal(processed_path)
    sealed_pde_archives = {
        (ROOT / relative).resolve()
        for relative in pde["files"]
        if relative.endswith(".npz")
    }
    actual_pde_archives = {
        path.resolve()
        for name in (
            "pde_primary",
            "pde_scramble",
            "pde_audits",
            "pde_fallback",
        )
        for path in (RESULTS / name).glob("*.npz")
    }
    if sealed_pde_archives != actual_pde_archives:
        raise RuntimeError("current PDE archive inventory differs from its seal")
    sealed_dense_archives = {
        (ROOT / relative).resolve()
        for relative in dense["files"]
        if relative.endswith(".npz")
    }
    actual_dense_archives = {
        path.resolve()
        for name in ("dense_screen", "dense_confirm", "dense_depth")
        for path in (RESULTS / name).glob("*.npz")
    }
    if sealed_dense_archives != actual_dense_archives:
        raise RuntimeError(
            "current dense archive inventory differs from its seal"
        )
    runner_sha256 = sha256(ROOT / "protocol" / "run_grid.py")
    if pde["dynamics_sha256"] != aggregate:
        raise RuntimeError("PDE evidence uses the wrong frozen source")
    if dense["dynamics_sha256"] != aggregate:
        raise RuntimeError("dense evidence uses the wrong frozen source")
    if processed["dynamics_sha256"] != aggregate:
        raise RuntimeError("processed evidence uses the wrong frozen source")
    if pde["run_grid_sha256"] != runner_sha256:
        raise RuntimeError("PDE seal uses the wrong execution runner")
    if dense["run_grid_sha256"] != runner_sha256:
        raise RuntimeError("dense seal uses the wrong execution runner")
    decision_path = RESULTS / "pde_numerical_decision.json"
    if pde["pde_numerical_decision_sha256"] != sha256(decision_path):
        raise RuntimeError("PDE seal uses the wrong numerical decision")
    if dense["pde_seal_sha256"] != sha256(pde_path):
        raise RuntimeError("dense evidence does not point to this PDE seal")
    if processed["pde_seal_sha256"] != sha256(pde_path):
        raise RuntimeError("processed evidence uses the wrong PDE seal")
    if processed["dense_seal_sha256"] != sha256(dense_path):
        raise RuntimeError("processed evidence uses the wrong dense seal")
    if processed["analysis_source_sha256"] != sha256(
        ROOT / "analyze_generalization.py"
    ):
        raise RuntimeError("processed evidence uses the wrong analyzer source")
    if processed.get("bootstrap_replicates") != 2000:
        raise RuntimeError("processed evidence is not the preregistered bootstrap")
    if processed.get("bootstrap_test_override"):
        raise RuntimeError("processed evidence is marked test-only")
    required = (
        "results/generalization/processed/summary.json",
        "results/generalization/processed/case_metrics.csv",
        "results/generalization/processed/numerical_metrics.csv",
        "results/generalization/processed/plateau_metrics.csv",
        "results/generalization/figures/all_case_errors.png",
        "results/generalization/figures/loss_curves.png",
        "results/generalization/figures/gram_motion_curves.png",
        "REPORT.md",
    )
    if set(processed["files"]) != set(required):
        raise RuntimeError(
            "processed seal inventory differs from required deliverables"
        )
    for relative in required:
        if not (ROOT / relative).is_file():
            raise RuntimeError(f"missing processed deliverable: {relative}")
        if relative not in processed["files"]:
            raise RuntimeError(
                f"processed seal omits required deliverable: {relative}"
            )
    actual_processed = {
        os.fspath(path.relative_to(ROOT))
        for directory in (
            RESULTS / "processed",
            RESULTS / "figures",
        )
        for path in directory.iterdir()
        if path.is_file()
    }
    actual_processed.add("REPORT.md")
    if actual_processed != set(required):
        raise RuntimeError(
            "processed output directories contain missing or extra files"
        )
    summary = json.loads(
        (RESULTS / "processed" / "summary.json").read_text()
    )
    provenance = summary["provenance"]
    if provenance["dynamics_sha256"] != aggregate:
        raise RuntimeError("processed summary uses the wrong source")
    if provenance["pde_seal_sha256"] != sha256(pde_path):
        raise RuntimeError("processed summary uses the wrong PDE evidence")
    if provenance["dense_seal_sha256"] != sha256(dense_path):
        raise RuntimeError("processed summary uses the wrong dense evidence")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("source", "evidence"))
    parser.add_argument("--skip-tests", action="store_true")
    args = parser.parse_args()
    if args.mode == "source":
        aggregate = verify_source(not args.skip_tests)
        print(f"source verification passed: {aggregate}")
    else:
        verify_evidence(not args.skip_tests)
        print("full evidence verification passed")


if __name__ == "__main__":
    main()
