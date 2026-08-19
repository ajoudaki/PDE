"""Exact six-point proof of the primary explicit-Q0 coefficient powers.

The independent compiler accepts exact rational Q0 but does not serialize it
symbolically.  Both routes have explicit Q0 degree at most k in D^k f when
layer moments are treated as formal atoms.  Equality at six distinct points
therefore proves the complete A/B/C coefficient polynomials (bounds 1/3/5).
"""

from __future__ import annotations

from fractions import Fraction
import gc
import json
from pathlib import Path

from ..independent.depth_factored import compile_depth_factored, expand_expression


HERE = Path(__file__).resolve().parent
PRIMARY = HERE.parent / "primary"
INDEPENDENT = HERE.parent / "independent"
POINTS = tuple(Fraction(value, 2) for value in (1, 2, 3, 4, 5, 6))
HOLDOUT = Fraction(7, 2)
DEGREE_BOUNDS = {"A": 1, "B": 3, "C": 5}


def primary_graded(depth: int):
    path = PRIMARY / f"H{depth}_LAYER_TAGGED_COEFFICIENTS.json"
    payload = json.loads(path.read_text())
    answer = {}
    observed = {}
    for root in "ABC":
        mapping = {}
        maximum = 0
        for atoms, coefficient_text in payload["roots"][root]:
            degree = atoms.count("Q0")
            activation = tuple(sorted(atom for atom in atoms if atom != "Q0"))
            key = (activation, degree)
            mapping[key] = mapping.get(key, Fraction(0)) + Fraction(coefficient_text)
            maximum = max(maximum, degree)
        mapping = {key: value for key, value in mapping.items() if value}
        if maximum > DEGREE_BOUNDS[root]:
            raise AssertionError((depth, root, maximum, DEGREE_BOUNDS[root]))
        answer[root] = mapping
        observed[root] = maximum
    return answer, observed


def specialize(graded, point: Fraction):
    answer = {}
    for root in "ABC":
        mapping = {}
        for (atoms, degree), coefficient in graded[root].items():
            mapping[atoms] = mapping.get(atoms, Fraction(0)) + coefficient * point**degree
        answer[root] = {key: value for key, value in mapping.items() if value}
    return answer


def independent_map(depth: int, point: Fraction):
    # Reuse the separately frozen Q0=1 map; compile every other point afresh.
    if point == 1:
        payload = json.loads(
            (INDEPENDENT / f"H{depth}_TAGGED_COEFFICIENT_MAP.json").read_text()
        )
        return {
            root: {
                tuple(sorted(record["atoms"])): Fraction(record["coefficient"])
                for record in payload[root]
            }
            for root in "ABC"
        }
    result = compile_depth_factored(depth, q0=point, unit_gram=False)
    return {
        "A": expand_expression(result.A),
        "B": expand_expression(result.B),
        "C": expand_expression(result.C),
    }


def compare(left, right):
    report = {}
    for root in "ABC":
        mismatch_count = 0
        first = []
        for atoms in set(left[root]) | set(right[root]):
            if left[root].get(atoms, 0) != right[root].get(atoms, 0):
                mismatch_count += 1
                if len(first) < 10:
                    first.append(
                        {
                            "atoms": list(atoms),
                            "primary": str(left[root].get(atoms, 0)),
                            "independent": str(right[root].get(atoms, 0)),
                        }
                    )
        report[root] = {
            "primary_terms": len(left[root]),
            "independent_terms": len(right[root]),
            "discrepancy_count": mismatch_count,
            "first_discrepancies": first,
        }
    return report


def main() -> None:
    full_report = {
        "method": (
            "exact rational specialization at six distinct points; explicit "
            "degree bounds A/B/C<=1/3/5; seventh point unused holdout"
        ),
        "degree_proof": (
            "With layer moments formal, explicit Q0 occurs only in zdot1=Q0*b1. "
            "Each directional/time derivative inserts at most one vector-field "
            "factor, so deg_Q0 D^k f<=k. Wick, Stein, expectation, and equality "
            "partitioning preserve total Taylor order and cannot raise the bound."
        ),
        "degree_bounds": DEGREE_BOUNDS,
        "interpolation_points": [str(point) for point in POINTS],
        "holdout_point": str(HOLDOUT),
        "depths": {},
    }
    passed = True
    for depth in (3, 4):
        graded, observed = primary_graded(depth)
        depth_report = {"primary_observed_degrees": observed, "points": {}}
        for point in POINTS + (HOLDOUT,):
            primary = specialize(graded, point)
            independent = independent_map(depth, point)
            point_report = compare(primary, independent)
            depth_report["points"][str(point)] = point_report
            discrepancies = {root: point_report[root]["discrepancy_count"] for root in "ABC"}
            print(f"H={depth} Q0={point}: {discrepancies}", flush=True)
            if any(discrepancies.values()):
                passed = False
            del primary, independent
            gc.collect()
        full_report["depths"][str(depth)] = depth_report
        del graded
        gc.collect()
    full_report["pass"] = passed
    output = HERE / "SYMBOLIC_Q0_AUDIT.json"
    output.write_text(json.dumps(full_report, indent=2, sort_keys=True) + "\n")
    print(output)
    if not passed:
        raise SystemExit("symbolic Q0 audit failed")


if __name__ == "__main__":
    main()

