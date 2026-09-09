"""Reconstruct the independent symbolic-Q0 map by exact interpolation.

The six interpolation points are fixed before any primary symbolic map is
loaded.  A seventh point is an independent exact holdout.  Only after the
interpolated map is serialized and hashed is the primary compiler imported
for a literal graded coefficient comparison.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Mapping

from .independent_compiler import _atom_text, compile_layer_tagged


HERE = Path(__file__).resolve().parent
POINTS = tuple(Fraction(value, 2) for value in (1, 2, 3, 4, 5, 6))
HOLDOUT = Fraction(7, 2)
DEGREE_BOUNDS = {"A": 1, "B": 3, "C": 5}

ActivationMonomial = tuple[str, ...]
NumericMap = dict[ActivationMonomial, Fraction]
GradedMap = dict[tuple[ActivationMonomial, int], Fraction]


def _numeric_map(result, name: str) -> NumericMap:
    return {
        tuple(sorted(_atom_text(atom) for atom in monomial)): coefficient
        for monomial, coefficient in getattr(result, name).items()
    }


def _poly_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(left), len(right))
    for index, coefficient in enumerate(left):
        out[index] += coefficient
    for index, coefficient in enumerate(right):
        out[index] += coefficient
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def _poly_scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * coefficient for coefficient in poly]


def _poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def interpolate(values: list[Fraction]) -> list[Fraction]:
    if len(values) != len(POINTS):
        raise ValueError("one value is required at every frozen interpolation point")
    answer = [Fraction(0)]
    for i, (xi, yi) in enumerate(zip(POINTS, values)):
        basis = [Fraction(1)]
        denominator = Fraction(1)
        for j, xj in enumerate(POINTS):
            if i == j:
                continue
            basis = _poly_mul(basis, [-xj, Fraction(1)])
            denominator *= xi - xj
        answer = _poly_add(answer, _poly_scale(basis, yi / denominator))
    return answer


def evaluate_graded(mapping: GradedMap, q0: Fraction) -> NumericMap:
    answer: dict[ActivationMonomial, Fraction] = {}
    for (monomial, degree), coefficient in mapping.items():
        answer[monomial] = answer.get(monomial, Fraction(0)) + coefficient * q0**degree
    return {key: value for key, value in answer.items() if value}


def serialize(mapping: GradedMap) -> list[dict[str, object]]:
    return [
        {
            "atoms": list(monomial),
            "q0_degree": degree,
            "coefficient": str(coefficient),
        }
        for (monomial, degree), coefficient in sorted(mapping.items())
    ]


def compare(left: Mapping[str, GradedMap], right: Mapping[str, GradedMap]):
    report = {}
    for name in "ABC":
        discrepancies = []
        for key in sorted(set(left[name]) | set(right[name])):
            if left[name].get(key, 0) != right[name].get(key, 0):
                monomial, degree = key
                discrepancies.append(
                    {
                        "atoms": list(monomial),
                        "q0_degree": degree,
                        "primary": str(left[name].get(key, 0)),
                        "independent": str(right[name].get(key, 0)),
                    }
                )
        report[name] = {
            "primary_graded_terms": len(left[name]),
            "independent_graded_terms": len(right[name]),
            "discrepancy_count": len(discrepancies),
            "discrepancies": discrepancies,
        }
    return report


def main() -> None:
    samples: dict[Fraction, dict[str, NumericMap]] = {}
    for point in POINTS:
        result = compile_layer_tagged(q0=point)
        samples[point] = {name: _numeric_map(result, name) for name in "ABC"}
        print(f"compiled interpolation point Q0={point}", flush=True)

    reconstructed: dict[str, GradedMap] = {}
    observed_degrees = {}
    for name in "ABC":
        monomials = set().union(*(samples[point][name] for point in POINTS))
        graded: GradedMap = {}
        maximum = 0
        for monomial in sorted(monomials):
            polynomial = interpolate([samples[point][name].get(monomial, 0) for point in POINTS])
            for degree, coefficient in enumerate(polynomial):
                if coefficient:
                    graded[(monomial, degree)] = coefficient
                    maximum = max(maximum, degree)
        if maximum > DEGREE_BOUNDS[name]:
            raise AssertionError(
                f"interpolation exceeds proved degree bound for {name}: {maximum}"
            )
        reconstructed[name] = graded
        observed_degrees[name] = maximum

    # Exact seventh-point holdout, not used by interpolation.
    holdout_result = compile_layer_tagged(q0=HOLDOUT)
    holdout = {name: _numeric_map(holdout_result, name) for name in "ABC"}
    holdout_discrepancies = {}
    for name in "ABC":
        predicted = evaluate_graded(reconstructed[name], HOLDOUT)
        mismatch = [
            monomial
            for monomial in sorted(set(predicted) | set(holdout[name]))
            if predicted.get(monomial, 0) != holdout[name].get(monomial, 0)
        ]
        holdout_discrepancies[name] = len(mismatch)
    if any(holdout_discrepancies.values()):
        raise AssertionError(f"independent Q0 holdout failed: {holdout_discrepancies}")

    payload = {
        "format": "independent-H2-B1-symbolic-Q0-graded-Mpoly-v1",
        "construction": "exact Fraction interpolation before primary comparison",
        "degree_proof": (
            "Treat X_nu and Y_nu as formal degree-zero atoms. Explicit Q0 enters only "
            "through udot=Q0*phi'(u)*r. An order-k feature directional derivative has "
            "at most k velocity insertions, hence explicit Q0 degree <=k."
        ),
        "degree_bounds": DEGREE_BOUNDS,
        "interpolation_points": [str(value) for value in POINTS],
        "holdout_point": str(HOLDOUT),
        "holdout_discrepancy_counts": holdout_discrepancies,
        "observed_maximum_degrees": observed_degrees,
        "maps": {name: serialize(reconstructed[name]) for name in "ABC"},
        "counts": {
            name: {
                "activation_monomials": len({monomial for monomial, _ in reconstructed[name]}),
                "graded_terms": len(reconstructed[name]),
            }
            for name in "ABC"
        },
    }
    exact = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode() + b"\n"
    map_path = HERE / "independent_symbolic_q0_coefficient_map.json"
    map_path.write_bytes(exact)
    digest = hashlib.sha256(exact).hexdigest()
    (HERE / "SYMBOLIC_Q0_FROZEN_SHA256.txt").write_text(
        f"{digest}  {map_path.name}\n"
    )
    print(f"froze independent symbolic-Q0 map {digest}", flush=True)

    # Delayed primary import/comparison: the independent artifact is frozen.
    from ..compiler.coefficient_map import expand_coefficient_map
    from ..compiler.factored_expression import compile_factored

    primary_result = compile_factored(5, arbitrary_q0=True)
    primary: dict[str, GradedMap] = {}
    for name, root in {
        "A": primary_result.A,
        "B": primary_result.B3,
        "C": primary_result.C,
    }.items():
        graded: GradedMap = {}
        for monomial, coefficient in expand_coefficient_map(root).items():
            degree = monomial.count("Q0")
            activation = tuple(sorted(atom for atom in monomial if atom != "Q0"))
            key = (activation, degree)
            graded[key] = graded.get(key, Fraction(0)) + coefficient
        primary[name] = {key: value for key, value in graded.items() if value}

    comparison = compare(primary, reconstructed)
    primary_degrees = {
        name: max((degree for (_, degree) in primary[name]), default=0)
        for name in "ABC"
    }
    report = {
        "comparison_time": "after independent interpolation artifact freeze",
        "independent_exact_file_sha256": digest,
        "degree_bounds": DEGREE_BOUNDS,
        "independent_observed_degrees": observed_degrees,
        "primary_observed_degrees": primary_degrees,
        "interpolation_points": [str(value) for value in POINTS],
        "holdout_point": str(HOLDOUT),
        "holdout_discrepancy_counts": holdout_discrepancies,
        "coefficients": comparison,
        "pass": not any(comparison[name]["discrepancy_count"] for name in "ABC"),
    }
    report_path = HERE / "SYMBOLIC_Q0_PRIMARY_COMPARISON.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report_path.read_text())
    if not report["pass"]:
        raise SystemExit("symbolic-Q0 atomwise comparison failed")


if __name__ == "__main__":
    main()
