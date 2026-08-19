"""Unified low-cost integrity/status checks for the depth-order-five result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .build_self_contained_report import check as check_report


HERE = Path(__file__).resolve().parent
DEPTH_ROOT = HERE.parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    freeze = json.loads((HERE / "PRIMARY_FREEZE_MANIFEST.json").read_text())
    recorded = (HERE / "PRIMARY_FREEZE_SHA256.txt").read_text().split()[0]
    require(recorded == sha256(HERE / "PRIMARY_FREEZE_MANIFEST.json"), "primary freeze manifest drift")
    for name, record in freeze["artifacts"].items():
        require(sha256(HERE / name) == record["sha256"], f"frozen artifact drift: {name}")
    print("PASS primary freeze and all formula/map hashes")

    for depth in (3, 4):
        stats = json.loads((HERE / f"H{depth}_ARTIFACT_STATS.json").read_text())
        require(all(stats["parity"].values()), f"parity failed at H={depth}")
        require(
            stats["maximum_terminal_derivative"] == {"A": 1, "B": 3, "C": 5},
            f"derivative ceiling failed at H={depth}",
        )
        for quotient in ("TAGGED", "UNIT"):
            comparison = json.loads(
                (HERE / f"H{depth}_{quotient}_FROZEN_COMPARISON.json").read_text()
            )
            require(comparison["pass"], f"frozen route diff failed: H{depth} {quotient}")
    print("PASS parity, derivative ceilings, and four exact route comparisons")

    hostile = DEPTH_ROOT / "audit"
    independent = DEPTH_ROOT / "independent"
    require(json.loads((hostile / "FROZEN_MAP_COMPARISON.json").read_text())["pass"], "hostile map comparison")
    require(json.loads((hostile / "SYMBOLIC_Q0_AUDIT.json").read_text())["pass"], "symbolic Q0 audit")
    require(json.loads((hostile / "TWO_ORACLE_GATE.json").read_text())["pass"], "two-oracle gate")
    experiment = json.loads((hostile / "NORMALIZED_SINE_EXPERIMENT.json").read_text())
    require(experiment["decision"] == "pass", "normalized-sine regression")
    require(json.loads((independent / "CONTROL_AUDIT.json").read_text())["pass"], "independent controls")
    print("PASS hostile Q0/oracle/regression gates and independent controls")

    sine = json.loads((HERE / "NORMALIZED_SINE_CONTROL.json").read_text())
    for depth in (3, 4):
        record = sine["records_by_hidden_depth"][str(depth)]
        require(record["mu0_sign"] == "negative", f"sine mu0 sign H={depth}")
        require(record["mu1_sign"] == "negative", f"sine mu1 sign H={depth}")
    print("PASS normalized-sine analytic atom evaluation/sign audit")

    for depth in (3, 4):
        for quotient in ("LAYER_TAGGED", "UNIT"):
            path = HERE / f"H{depth}_{quotient}_ABC.cse.txt"
            text = path.read_text()
            require(text.endswith("\n"), f"missing terminal LF: {path.name}")
            require("\nA = " in text and "\nB = " in text and "\nC = " in text, f"missing roots: {path.name}")
            for forbidden in ("alpha", "beta", "pseudoinverse", "F^", "R^", "covariance"):
                require(forbidden not in text, f"auxiliary token {forbidden}: {path.name}")
    print("PASS terminal CSE leaf/roots scan")

    check_report()


if __name__ == "__main__":
    main()

