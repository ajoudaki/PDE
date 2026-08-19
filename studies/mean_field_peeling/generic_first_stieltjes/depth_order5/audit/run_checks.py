"""Lightweight replay of every frozen hostile promotion gate.

The expensive literal diff and seven-point symbolic-Q0 compilation have
already emitted deterministic exact-rational certificates.  This script
validates those certificates, all frozen hashes, numerical decision rules,
and the byte-reconstructed final report.  ``compare_frozen.py`` is the full
literal replay when a coefficient artifact changes.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ..primary.build_self_contained_report import check as check_report


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def verify_primary_freeze() -> None:
    path = ROOT / "primary" / "PRIMARY_FREEZE_MANIFEST.json"
    require(
        digest(path) == "f4838437c1fb70b14713d39e8438d703434c49ffd72001beeb6fee8d53366b30",
        "primary manifest hash",
    )
    manifest = json.loads(path.read_text())
    for name, record in manifest["artifacts"].items():
        artifact = path.parent / name
        require(artifact.stat().st_size == record["bytes"], f"primary bytes {name}")
        require(digest(artifact) == record["sha256"], f"primary hash {name}")


def verify_independent_freeze() -> None:
    path = ROOT / "independent" / "FROZEN_MANIFEST.json"
    require(
        digest(path) == "dee0198e119864a90195101466f29f3ab2f248495c6e6a3494f35cafd3f2502b",
        "independent manifest hash",
    )
    manifest = json.loads(path.read_text())
    for formula in manifest["artifacts"].values():
        for kind in ("dag", "expanded", "text"):
            record = formula[kind]
            artifact = path.parent / record["file"]
            require(digest(artifact) == record["sha256"], f"independent hash {artifact.name}")


def verify_exact_certificates() -> None:
    comparison = json.loads((HERE / "FROZEN_MAP_COMPARISON.json").read_text())
    require(comparison["pass"], "literal map certificate")
    for formula in comparison["comparisons"].values():
        for root in formula.values():
            require(root["discrepancy_count"] == 0, "literal discrepancy")
            require(root["primary_maximum_derivative"] <= 5, "primary derivative ceiling")
            require(root["independent_maximum_derivative"] <= 5, "independent derivative ceiling")

    q0 = json.loads((HERE / "SYMBOLIC_Q0_AUDIT.json").read_text())
    require(q0["pass"], "symbolic Q0 certificate")
    require(q0["degree_bounds"] == {"A": 1, "B": 3, "C": 5}, "Q0 degree bounds")
    for depth in q0["depths"].values():
        require(depth["primary_observed_degrees"] == {"A": 1, "B": 3, "C": 5}, "Q0 observed degree")
        for point in depth["points"].values():
            require(all(point[root]["discrepancy_count"] == 0 for root in "ABC"), "Q0 discrepancy")

    linear = json.loads((HERE / "DEEP_LINEAR_AUDIT.json").read_text())
    require(linear["depths"]["3"]["large_width_A_B_C"] == [4, 160, 13888], "H3 linear")
    require(linear["depths"]["4"]["large_width_A_B_C"] == [5, 400, 73240], "H4 linear")
    for name, expected in linear["source_sha256"].items():
        require(digest(HERE / name) == expected, f"linear source hash {name}")


def verify_numerical_certificates() -> None:
    gate = json.loads((HERE / "TWO_ORACLE_GATE.json").read_text())
    require(gate["pass"] and gate["worst_scaled_discrepancy"] <= gate["threshold"], "two-oracle gate")

    experiment = json.loads((HERE / "NORMALIZED_SINE_EXPERIMENT.json").read_text())
    require(experiment["total_networks"] == 7700, "network budget")
    require(experiment["decision"] == "pass", "nonpolynomial decision")
    require(sum(cell["count"] for cells in experiment["cells"].values() for cell in cells) == 7700, "cell counts")
    for cells in experiment["cells"].values():
        require(all(cell["valid"] and cell["finite"] and cell["heavy_tail_batch_gate"] for cell in cells), "cell validity")
    for fit in experiment["fits"].values():
        require(fit["valid"] and fit["chi_square_p_value"] >= 0.01 and abs(fit["z"]) <= 3, "fit gate")


def main() -> None:
    verify_primary_freeze()
    verify_independent_freeze()
    print("PASS both producer freezes and every frozen artifact hash")
    verify_exact_certificates()
    print("PASS literal maps, symbolic Q0, derivative grammar, and deep-linear certificate")
    verify_numerical_certificates()
    print("PASS two-oracle and preregistered 7,700-network discriminator")
    check_report()
    print("PASS final report byte reconstruction and embedded audit hashes")


if __name__ == "__main__":
    main()
