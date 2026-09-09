"""Post-freeze rational-Q0 spot comparisons without mutating frozen maps."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

from ..compiler.coefficient_map import expand_coefficient_map
from ..compiler.factored_expression import compile_factored
from .independent_compiler import _atom_text, compile_layer_tagged


HERE = Path(__file__).resolve().parent


def independent_map(q0: Fraction):
    result = compile_layer_tagged(q0=q0)
    return {
        name: {
            tuple(sorted(_atom_text(atom) for atom in monomial)): coefficient
            for monomial, coefficient in getattr(result, name).items()
        }
        for name in "ABC"
    }


def primary_map(q0: Fraction):
    result = compile_factored(5, arbitrary_q0=True)
    answer = {}
    for name, root in {"A": result.A, "B": result.B3, "C": result.C}.items():
        specialized: dict[tuple[str, ...], Fraction] = {}
        for monomial, coefficient in expand_coefficient_map(root).items():
            power = monomial.count("Q0")
            reduced = tuple(value for value in monomial if value != "Q0")
            specialized[reduced] = specialized.get(reduced, Fraction(0)) + coefficient * q0**power
        answer[name] = {key: value for key, value in specialized.items() if value}
    return answer


def main() -> None:
    report = {
        "status": "post-freeze bounded spot check; frozen coefficient artifacts unchanged",
        "points": {},
    }
    for q0 in (Fraction(1, 2), Fraction(2)):
        left = primary_map(q0)
        right = independent_map(q0)
        point = {}
        for name in "ABC":
            mismatch = [
                monomial
                for monomial in sorted(set(left[name]) | set(right[name]))
                if left[name].get(monomial, 0) != right[name].get(monomial, 0)
            ]
            point[name] = {
                "primary_terms": len(left[name]),
                "independent_terms": len(right[name]),
                "discrepancy_count": len(mismatch),
            }
        report["points"][str(q0)] = point
    report["pass"] = not any(
        values[name]["discrepancy_count"]
        for values in report["points"].values()
        for name in "ABC"
    )
    path = HERE / "Q0_SPOT_COMPARISON.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(path.read_text())
    if not report["pass"]:
        raise SystemExit("rational-Q0 comparison failed")


if __name__ == "__main__":
    main()
