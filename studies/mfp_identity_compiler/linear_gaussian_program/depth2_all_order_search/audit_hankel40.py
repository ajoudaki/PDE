#!/usr/bin/env python3
"""Exact H_0,...,H_19 and shifted-Hankel audit for depth-two identity."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
INPUT = HERE / "RESULTS.json"
Q = Fraction


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def ldl_leading_determinants(matrix: list[list[Fraction]]) -> tuple[list[Fraction], list[Fraction]]:
    size = len(matrix)
    lower = [[Q(0) for _ in range(size)] for _ in range(size)]
    diagonal = [Q(0) for _ in range(size)]
    determinants: list[Fraction] = []
    running = Q(1)
    for i in range(size):
        lower[i][i] = Q(1)
        diagonal[i] = matrix[i][i] - sum(
            lower[i][k] * lower[i][k] * diagonal[k]
            for k in range(i)
        )
        if not diagonal[i]:
            raise ArithmeticError(f"zero LDL pivot at {i}")
        for j in range(i + 1, size):
            numerator = matrix[j][i] - sum(
                lower[j][k] * lower[i][k] * diagonal[k]
                for k in range(i)
            )
            lower[j][i] = numerator / diagonal[i]
        running *= diagonal[i]
        determinants.append(running)
    return diagonal, determinants


def sympy_determinant(matrix: list[list[Fraction]], size: int) -> Fraction:
    submatrix = [
        [sp.Rational(value.numerator, value.denominator) for value in row[:size]]
        for row in matrix[:size]
    ]
    value = sp.Matrix(submatrix).det(method="domain-ge")
    return Q(int(value.p), int(value.q))


def audit_family(moments: list[Fraction], shift: int) -> dict[str, object]:
    size = 20
    matrix = [
        [moments[row + column + shift] for column in range(size)]
        for row in range(size)
    ]
    pivots, determinants = ldl_leading_determinants(matrix)
    checked_sizes = list(range(1, 7)) + [20]
    independent = {
        str(check_size): sympy_determinant(matrix, check_size)
        for check_size in checked_sizes
    }
    for check_size, value in independent.items():
        if value != determinants[int(check_size) - 1]:
            raise AssertionError(f"determinant routes disagree at size {check_size}")
    return {
        "shift": shift,
        "matrices": [f"H_{degree}" + ("_plus" if shift else "") for degree in range(20)],
        "ldl_pivots": [fraction_string(value) for value in pivots],
        "leading_determinants": [fraction_string(value) for value in determinants],
        "leading_determinant_signs": [
            "positive" if value > 0 else "zero" if value == 0 else "negative"
            for value in determinants
        ],
        "all_positive_definite": all(value > 0 for value in determinants),
        "independent_symbolic_checks": {
            f"size_{check_size}": fraction_string(value)
            for check_size, value in independent.items()
        },
        "independent_checks_agree": True,
    }


def main() -> int:
    document = json.loads(INPUT.read_text())
    moments = [Q(value) for value in document["moments"]]
    if len(moments) != 40:
        raise AssertionError("expected exactly forty moments")
    ordinary = audit_family(moments, 0)
    shifted = audit_family(moments, 1)
    payload = {
        "format": "identity-depth2-hankel40-v1",
        "input_moments": ["mu_0", "...", "mu_39"],
        "moment_signs_all_positive": all(value > 0 for value in moments),
        "ordinary": ordinary,
        "shifted": shifted,
        "verdict": (
            "H_0_through_H_19_and_shifted_partners_are_all_positive_definite"
            if ordinary["all_positive_definite"] and shifted["all_positive_definite"]
            else "at_least_one_accessible_Hankel_matrix_is_not_positive_definite"
        ),
        "claim_boundary": (
            "Exact finite forty-moment compatibility only; no all-order sequence, "
            "measure, or convergence claim."
        ),
        "sha256": {
            "input": sha256(INPUT),
            "protocol": sha256(HERE / "HANKEL40_PROTOCOL.md"),
            "source": sha256(Path(__file__)),
        },
    }
    output = HERE / "HANKEL40_RESULTS.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "output": str(output),
        "verdict": payload["verdict"],
        "ordinary_terminal_sign": ordinary["leading_determinant_signs"][-1],
        "shifted_terminal_sign": shifted["leading_determinant_signs"][-1],
        "ordinary_terminal_digits": len(ordinary["leading_determinants"][-1]),
        "shifted_terminal_digits": len(shifted["leading_determinants"][-1]),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

