"""Numerical evaluation of the frozen M-only head for normalized sine."""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss

from ...order5.compiler.factored_expression import FactoredMomentExpression as Expr
from .assemble_gamma04 import assemble_head


HERE = Path(__file__).resolve().parent
NORMALIZATION = sqrt((1.0 - exp(-2.0)) / 2.0)


def evaluate(root: Expr, quadrature_order: int) -> float:
    nodes, weights = hermgauss(quadrature_order)
    gaussian = sqrt(2.0) * nodes
    weights = weights / sqrt(pi)
    moments: dict[tuple[int, ...], float] = {}
    memo: dict[Expr, float] = {}

    def visit(node: Expr) -> float:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = float(node.node[1])
        elif kind == "atom":
            if node.node[1] != "M":
                raise KeyError(node.node[1])
            exponent = tuple(node.node[2])
            if exponent not in moments:
                integrand = np.ones_like(gaussian)
                for derivative, multiplicity in enumerate(exponent):
                    if multiplicity:
                        integrand *= (
                            np.sin(gaussian + derivative * pi / 2.0)
                            / NORMALIZATION
                        ) ** multiplicity
                moments[exponent] = float(weights @ integrand)
            value = moments[exponent]
        elif kind == "add":
            value = sum(visit(child) for child in node.node[1])
        elif kind == "mul":
            value = 1.0
            for child in node.node[1]:
                value *= visit(child)
        else:
            raise ValueError(node.node)
        memo[node] = value
        return value

    return visit(root)


def prediction() -> dict[str, object]:
    result = assemble_head(2)
    roots = {
        "Gamma04_H2_layer2": result.head[2]["gamma04"],
        "Gamma13_H2_layer2": result.backbone.feature3[2]["q13"],
        "Gamma22_H2_layer2": result.backbone.feature2[2]["q22"],
    }
    orders: dict[str, object] = {}
    for quadrature_order in (64, 96, 128):
        values = {
            name: evaluate(root, quadrature_order) for name, root in roots.items()
        }
        values["Q4_H2_layer2"] = (
            2 * values["Gamma04_H2_layer2"]
            + 8 * values["Gamma13_H2_layer2"]
            + 6 * values["Gamma22_H2_layer2"]
        )
        orders[str(quadrature_order)] = values
    return {
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "head_freeze_sha256": "66449874726a3f424ec8cdcda27f90823c3317aa0b00fa7ebfbed9d1e88075b6",
        "hidden_depth": 2,
        "observed_layer": 2,
        "orders": orders,
        "quadrature_is_numerical_evaluation_not_an_activation_approximation": True,
    }


if __name__ == "__main__":
    payload = prediction()
    path = HERE / "NORMALIZED_SINE_PREDICTION.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
