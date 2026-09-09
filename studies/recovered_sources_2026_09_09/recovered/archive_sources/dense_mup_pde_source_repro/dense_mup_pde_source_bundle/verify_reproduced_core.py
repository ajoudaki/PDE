#!/usr/bin/env python3
"""Verify a clean canonical regeneration without historical pilot archives."""

from __future__ import annotations

import ast
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / "dense_mup_pde_repro"
RAW = PROJECT / "results" / "raw"
PROCESSED = PROJECT / "results" / "processed"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(value: float, expected: float, tolerance: float, label: str) -> None:
    check(
        abs(value - expected) <= tolerance,
        f"{label}: observed {value:.12g}, expected {expected:.12g} ± {tolerance:g}",
    )


def verify_archives() -> int:
    paths = sorted([*RAW.glob("*.npz"), *PROCESSED.glob("*.npz")])
    check(len(paths) >= 36, f"expected at least 36 canonical NPZ files, found {len(paths)}")
    for path in paths:
        with np.load(path, allow_pickle=False) as archive:
            check(bool(archive.files), f"empty archive: {path.name}")
            for key in archive.files:
                array = archive[key]
                if np.issubdtype(array.dtype, np.number):
                    check(np.all(np.isfinite(array)), f"nonfinite {path.name}:{key}")
    return len(paths)


def verify_no_reference_oracle() -> None:
    path = PROJECT / "src" / "dense_pde" / "operator_galerkin.py"
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    imports: list[str] = []
    literals: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            literals.append(node.value)
    check(
        not any("dense_reference" in name for name in imports),
        "PDE source imports dense_reference",
    )
    forbidden = ("results/raw", "exact_ensemble", "reference_comparisons")
    check(
        not any(token in literal for token in forbidden for literal in literals),
        "PDE source contains a dense-reference result path",
    )
    check("np.load" not in source, "PDE vector-field module performs file loading")


def verify_metrics() -> None:
    summary = json.loads((PROCESSED / "summary.json").read_text(encoding="utf-8"))
    expected_metrics = json.loads(
        (PROJECT / "protocol" / "expected_metrics.json").read_text(
            encoding="utf-8"
        )
    )
    expected = expected_metrics["expected"]
    tolerances = expected_metrics["tolerances"]
    primary = summary["primary_pde"]
    check(primary["actual_width_independent_pde_run"] is True, "bad PDE label")
    check(primary["contains_dense_network_weight_matrix"] is False, "hidden matrix label")

    reference = summary["reference_comparisons"]["n256_L32_S128"]
    close(
        reference["max_gram_increment_gap"],
        expected["primary_gram_increment_gap"],
        tolerances["primary_gram_increment_gap"],
        "primary Gram-increment gap",
    )
    close(
        reference["pde_feature_motion"],
        expected["pde_feature_motion"],
        tolerances["pde_feature_motion"],
        "PDE feature motion",
    )
    close(
        reference["max_loss_of_mean_gap"],
        expected["loss_of_mean_gap"],
        tolerances["loss_of_mean_gap"],
        "loss-of-mean gap",
    )

    plateau = summary["plateau"]
    plateau_bound = tolerances["plateau_drift_upper_bound"]
    check(plateau["max_output_drift"] < plateau_bound, "output tail did not plateau")
    check(
        plateau["max_all_depth_gram_drift"] < plateau_bound,
        "Gram tail did not plateau",
    )

    levels = summary["compiler_level_reference_checks"]
    check(
        levels["QMC_P15_complete_quadratic"]["max_gram_increment_gap"]
        > levels["QMC_P5"]["max_gram_increment_gap"],
        "regenerated P=15 result no longer records the audited unfavorable step",
    )

    ordered = json.loads(
        (
            ROOT
            / "agent_outputs"
            / "statistical_audit"
            / "ordered_limit_summary.json"
        ).read_text(encoding="utf-8")
    )
    check(bool(ordered["cauchy_decisions"]), "ordered-limit decisions are missing")
    check(bool(ordered["pde_decisions"]), "PDE/reference decisions are missing")


def main() -> None:
    count = verify_archives()
    verify_no_reference_oracle()
    verify_metrics()
    print(f"Canonical regenerated evidence passed ({count} complete NPZ files).")


if __name__ == "__main__":
    main()
