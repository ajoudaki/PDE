#!/usr/bin/env python3
"""Static and compact-artifact checks that do not require raw trajectories."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / "dense_mup_pde_repro"
AGENTS = ROOT / "agent_outputs"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_layout(include_snapshot: bool) -> None:
    required = [
        ROOT / "FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT.md",
        PROJECT / "src" / "dense_pde" / "operator_galerkin.py",
        PROJECT / "src" / "dense_reference" / "core.py",
        PROJECT / "protocol" / "reproduce_full.sh",
        PROJECT / "protocol" / "protocol.json",
        AGENTS / "numerics" / "operator_hermite_pde.py",
        AGENTS / "final_adversarial_pde_audit.md",
    ]
    if include_snapshot:
        required.extend(
            [
                PROJECT / "results" / "processed" / "summary.json",
                AGENTS / "statistical_audit" / "ordered_limit_summary.json",
            ]
        )
    for path in required:
        check(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")


def verify_no_raw_arrays() -> None:
    archives = list(ROOT.rglob("*.npz"))
    if archives:
        raise AssertionError(
            f"compact bundle unexpectedly contains NPZ: {archives[0]}"
        )
    total = sum(path.stat().st_size for path in ROOT.rglob("*") if path.is_file())
    check(total < 5 * 1024 * 1024, "uncompressed compact bundle exceeds 5 MiB")


def verify_python_syntax() -> None:
    for path in sorted(ROOT.rglob("*.py")):
        source = path.read_text(encoding="utf-8")
        ast.parse(source, filename=str(path))


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


def verify_compact_results() -> None:
    summary = json.loads(
        (PROJECT / "results" / "processed" / "summary.json").read_text(
            encoding="utf-8"
        )
    )
    check(
        summary["primary_pde"]["actual_width_independent_pde_run"] is True,
        "primary summary does not identify a genuine PDE run",
    )
    check(
        summary["primary_pde"]["contains_dense_network_weight_matrix"] is False,
        "primary summary claims a dense matrix",
    )
    gap = summary["reference_comparisons"]["n256_L32_S128"][
        "max_gram_increment_gap"
    ]
    check(abs(gap - 0.007243343266500024) < 1e-15, "snapshot headline gap changed")
    check(
        summary["plateau"]["max_all_depth_gram_drift"] < 1e-10,
        "snapshot plateau check failed",
    )

    for name in ("pde_vs_dense_curves.png", "pde_plateau_tail.png"):
        path = PROJECT / "figures" / name
        check(path.is_file(), f"missing figure: {name}")
        check(path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n", f"invalid PNG: {name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--snapshot",
        action="store_true",
        help="also check compact result files, figures, size, and absence of NPZs",
    )
    args = parser.parse_args()
    verify_layout(include_snapshot=args.snapshot)
    verify_python_syntax()
    verify_no_reference_oracle()
    if args.snapshot:
        verify_no_raw_arrays()
        verify_compact_results()
        print("Static compact-snapshot checks passed.")
    else:
        print("Static source checks passed.")


if __name__ == "__main__":
    main()
