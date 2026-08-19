"""Exact polynomial and smooth nonpolynomial controls for H=3,4 maps."""

from __future__ import annotations

from fractions import Fraction
from math import exp, factorial, pi, sqrt
import json
from pathlib import Path

import numpy as np
from scipy.special import roots_hermitenorm

from .depth_factored import Expr, FactoredDepthResult, compile_depth_factored


HERE = Path(__file__).resolve().parent


def _poly_mul(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def _poly_derivative(poly, order):
    out = list(poly)
    for _ in range(order):
        out = [Fraction(index) * out[index] for index in range(1, len(out))] or [Fraction(0)]
    return out


def _gaussian_power(power: int, variance: Fraction) -> Fraction:
    if power % 2:
        return Fraction(0)
    return Fraction(factorial(power), 2 ** (power // 2) * factorial(power // 2)) * variance ** (power // 2)


def polynomial_atom(exponent, coefficients, variance):
    integrand = [Fraction(1)]
    for derivative, multiplicity in enumerate(exponent):
        factor = _poly_derivative(coefficients, derivative)
        for _ in range(multiplicity):
            integrand = _poly_mul(integrand, factor)
    return sum(
        (coefficient * _gaussian_power(power, variance) for power, coefficient in enumerate(integrand)),
        Fraction(0),
    )


def evaluate_polynomial(result: FactoredDepthResult, coefficients) -> dict[str, Fraction]:
    coefficients = tuple(Fraction(value) for value in coefficients)
    variances = [Fraction(result.q0)]
    for _ in range(result.hidden_layers - 1):
        variances.append(polynomial_atom((2,), coefficients, variances[-1]))
    memo: dict[Expr, Fraction] = {}

    def visit(node: Expr) -> Fraction:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = node.node[1]
        elif kind == "atom":
            tag, exponent = node.node[1], node.node[2]
            variance = Fraction(1) if tag == "M" else variances[int(tag[1:]) - 1]
            value = polynomial_atom(exponent, coefficients, variance)
        elif kind == "add":
            value = sum((visit(child) for child in node.node[1]), Fraction(0))
        else:
            value = Fraction(1)
            for child in node.node[1]:
                value *= visit(child)
        memo[node] = value
        return value

    return {name: visit(getattr(result, name)) for name in "ABC"}


def evaluate_sine(result: FactoredDepthResult, order: int = 96) -> dict[str, float]:
    if not result.unit_gram:
        raise ValueError("normalized sine oracle uses the unit map")
    nodes, weights = roots_hermitenorm(order)
    weights = weights / sqrt(2 * pi)
    scale = sqrt(2 / (1 - exp(-2)))
    jets = (
        scale * np.sin(nodes), scale * np.cos(nodes), -scale * np.sin(nodes),
        -scale * np.cos(nodes), scale * np.sin(nodes), scale * np.cos(nodes),
    )
    atom_cache: dict[tuple[int, ...], float] = {}
    memo: dict[Expr, float] = {}

    def atom(exponent):
        if exponent not in atom_cache:
            integrand = np.ones_like(nodes)
            for derivative, multiplicity in enumerate(exponent):
                integrand *= jets[derivative] ** multiplicity
            atom_cache[exponent] = float(weights @ integrand)
        return atom_cache[exponent]

    def visit(node):
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = float(node.node[1])
        elif kind == "atom":
            value = atom(node.node[2])
        elif kind == "add":
            value = sum(visit(child) for child in node.node[1])
        else:
            value = 1.0
            for child in node.node[1]:
                value *= visit(child)
        memo[node] = value
        return value

    return {name: visit(getattr(result, name)) for name in "ABC"}


def linear_formula(hidden_layers: int) -> dict[str, Fraction]:
    h = Fraction(hidden_layers)
    return {
        "A": h + 1,
        "B": Fraction(2, 3) * h * (h + 1) ** 2 * (h + 2),
        "C": Fraction(1, 15)
        * h
        * (h + 1) ** 2
        * (h + 2)
        * (17 * h**3 + 47 * h**2 + 5 * h - 29),
    }


def main() -> None:
    report = {
        "linear_arbitrary_depth_candidate": {
            "parameter_block_count": "m=H+1",
            "A": "m",
            "B": "2*m^2*(m^2-1)/3",
            "C": "m^2*(m^2-1)*(17*m^3-4*m^2-38*m-4)/15",
            "status": (
                "A is proved by gradient-energy counting; B and C are exact "
                "finite-difference candidates, not promoted without a symbolic "
                "depth-transfer induction"
            ),
        },
        "depths": {},
    }
    for depth in (3, 4):
        tagged = compile_depth_factored(depth, unit_gram=False)
        unit = compile_depth_factored(depth, unit_gram=True)
        linear = evaluate_polynomial(unit, (0, 1))
        formula = linear_formula(depth)
        constant = evaluate_polynomial(unit, (1,))
        affine = evaluate_polynomial(tagged, (1, 1))
        quadratic = evaluate_polynomial(tagged, (0, 0, 1))
        quadratic_variances = [Fraction(1)]
        for _ in range(depth):
            quadratic_variances.append(3 * quadratic_variances[-1] ** 2)
        sine64 = evaluate_sine(unit, 64)
        sine96 = evaluate_sine(unit, 96)
        report["depths"][str(depth)] = {
            "linear": {"actual": {k: str(v) for k, v in linear.items()}, "formula": {k: str(v) for k, v in formula.items()}, "pass": linear == formula},
            "constant_1": {k: str(v) for k, v in constant.items()},
            "affine_1_plus_x": {k: str(v) for k, v in affine.items()},
            "quadratic": {k: str(v) for k, v in quadratic.items()},
            "quadratic_forward_gram_chain": [str(value) for value in quadratic_variances],
            "normalized_sine_order64": sine64,
            "normalized_sine_order96": sine96,
            "sine_max_abs_change": max(abs(sine96[k] - sine64[k]) for k in "ABC"),
        }
    report["pass"] = all(item["linear"]["pass"] for item in report["depths"].values())
    path = HERE / "CONTROL_AUDIT.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(path.read_text())
    if not report["pass"]:
        raise SystemExit("deep linear control failed")


if __name__ == "__main__":
    main()
