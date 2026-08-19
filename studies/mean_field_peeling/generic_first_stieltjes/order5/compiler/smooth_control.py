"""Gaussian-quadrature evaluation of the preregistered normalized-sine control."""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss

from .factored_expression import FactoredMomentExpression, compile_factored


def normalized_sine_values(order: int = 64) -> dict[str, float]:
    result = compile_factored(5)
    roots = {
        "A": result.A.specialize_unit_gram(),
        "B": result.B3.specialize_unit_gram(),
        "C": result.C.specialize_unit_gram(),
    }
    nodes, weights = hermgauss(order)
    gaussian = sqrt(2.0) * nodes
    weights = weights / sqrt(pi)
    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)
    memo: dict[FactoredMomentExpression, float] = {}

    def evaluate(node: FactoredMomentExpression) -> float:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = float(node.node[1])
        elif kind == "atom":
            integrand = np.ones_like(gaussian)
            for derivative, multiplicity in enumerate(node.node[2]):
                if multiplicity:
                    derivative_value = np.sin(gaussian + derivative * pi / 2.0) / normalization
                    integrand *= derivative_value**multiplicity
            value = float(weights @ integrand)
        elif kind == "add":
            value = sum(evaluate(child) for child in node.node[1])
        elif kind == "mul":
            value = 1.0
            for child in node.node[1]:
                value *= evaluate(child)
        else:
            raise ValueError(kind)
        memo[node] = value
        return value

    values = {name: evaluate(root) for name, root in roots.items()}
    A, B, C = values["A"], values["B"], values["C"]
    values["mu0"] = B / (2.0 * A**2)
    values["mu1"] = (4.0 * B**2 - A * C) / (24.0 * A**5)
    values["mu1_over_mu0"] = values["mu1"] / values["mu0"]
    values["normalization"] = normalization
    values["quadrature_order"] = order
    return values


def main() -> None:
    values = normalized_sine_values()
    target = Path(__file__).with_name("NORMALIZED_SINE_CONTROL.json")
    target.write_text(json.dumps(values, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
