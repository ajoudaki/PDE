"""Exact finite-depth deep-linear sequence and candidate-recurrence audit.

This is a bounded check, not a proof that the candidate recurrence holds at
uncomputed depths. The output records that claim boundary explicitly.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

from .controls import evaluate_polynomial
from .depth_factored import compile_depth_factored


HERE = Path(__file__).resolve().parent


def candidate(hidden_depth: int) -> dict[str, Fraction]:
    m = Fraction(hidden_depth + 1)
    return {
        "A": m,
        "B": Fraction(2, 3) * m**2 * (m**2 - 1),
        "C": Fraction(1, 15)
        * m**2
        * (m**2 - 1)
        * (17 * m**3 - 4 * m**2 - 38 * m - 4),
    }


def increment(m: int) -> dict[str, Fraction]:
    q = Fraction(m)
    return {
        "A": Fraction(1),
        "B": Fraction(4, 3) * q * (q - 1) * (2 * q - 1),
        "C": Fraction(1, 15)
        * q
        * (q - 1)
        * (119 * q**4 - 262 * q**3 + 118 * q**2 - 7 * q - 26),
    }


def serial(values: dict[str, Fraction]) -> dict[str, str]:
    return {name: str(value) for name, value in values.items()}


def main() -> None:
    # H=1 is the exact two-factor calculation.
    values: dict[int, dict[str, Fraction]] = {
        1: {"A": Fraction(2), "B": Fraction(8), "C": Fraction(32)}
    }
    for depth in range(2, 11):
        result = compile_depth_factored(depth, unit_gram=True)
        values[depth] = evaluate_polynomial(result, (0, 1))
        print(depth, serial(values[depth]), flush=True)

    rows = {}
    all_value_checks = True
    all_increment_checks = True
    for depth, actual in values.items():
        expected = candidate(depth)
        value_pass = actual == expected
        all_value_checks &= value_pass
        record: dict[str, object] = {
            "m": depth + 1,
            "actual": serial(actual),
            "candidate": serial(expected),
            "candidate_value_pass": value_pass,
        }
        if depth > 1:
            observed = {
                name: actual[name] - values[depth - 1][name] for name in "ABC"
            }
            expected_increment = increment(depth + 1)
            increment_pass = observed == expected_increment
            all_increment_checks &= increment_pass
            record["observed_increment"] = serial(observed)
            record["candidate_increment"] = serial(expected_increment)
            record["candidate_increment_pass"] = increment_pass
        rows[str(depth)] = record

    report = {
        "format": "independent-deep-linear-finite-sequence-v1",
        "scope": "exact H=1,...,10; Q0=1; phi(x)=x",
        "arbitrary_depth_status": (
            "A=m is proved; the displayed B,C formulas and increments remain "
            "finite-range conjectures because no symbolic depth-transfer "
            "induction or degree bound is supplied"
        ),
        "candidate_formulas": {
            "m": "H+1",
            "A": "m",
            "B": "2*m^2*(m^2-1)/3",
            "C": "m^2*(m^2-1)*(17*m^3-4*m^2-38*m-4)/15",
        },
        "candidate_increments": {
            "A(m)-A(m-1)": "1",
            "B(m)-B(m-1)": "4*m*(m-1)*(2*m-1)/3",
            "C(m)-C(m-1)": (
                "m*(m-1)*(119*m^4-262*m^3+118*m^2-7*m-26)/15"
            ),
        },
        "depths": rows,
        "all_finite_value_checks_pass": all_value_checks,
        "all_finite_increment_checks_pass": all_increment_checks,
    }
    output = HERE / "DEEP_LINEAR_SEQUENCE_AUDIT.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    if not (all_value_checks and all_increment_checks):
        raise SystemExit("finite deep-linear candidate check failed")


if __name__ == "__main__":
    main()
