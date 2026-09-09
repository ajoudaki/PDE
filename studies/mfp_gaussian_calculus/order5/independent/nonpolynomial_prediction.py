"""Preregistered normalized-sine prediction from the frozen unit map.

Gauss--Hermite is used only as Gaussian quadrature for already-declared
moment atoms.  The activation is never approximated by a Hermite series.
"""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.special import roots_hermitenorm


HERE = Path(__file__).resolve().parent


def evaluate(order: int) -> dict[str, float]:
    document = json.loads((HERE / "independent_coefficient_map.json").read_text())["unit_gram"]
    nodes, weights = roots_hermitenorm(order)
    weights = weights / sqrt(2 * pi)
    scale = sqrt(2 / (1 - exp(-2)))
    jets = (
        scale * np.sin(nodes),
        scale * np.cos(nodes),
        -scale * np.sin(nodes),
        -scale * np.cos(nodes),
        scale * np.sin(nodes),
        scale * np.cos(nodes),
    )
    cache: dict[str, float] = {}

    def atom(name: str) -> float:
        if name not in cache:
            counts = tuple(int(value) for value in name.split("_", 1)[1])
            integrand = np.ones_like(nodes)
            for derivative, multiplicity in enumerate(counts):
                integrand *= jets[derivative] ** multiplicity
            cache[name] = float(weights @ integrand)
        return cache[name]

    answer = {}
    for coefficient in "ABC":
        value = 0.0
        for term in document[coefficient]:
            summand = float(term["coefficient"])
            for name in term["atoms"]:
                summand *= atom(name)
            value += summand
        answer[coefficient] = value
    return answer


def main() -> None:
    orders = (32, 48, 64, 96, 128)
    convergence = {str(order): evaluate(order) for order in orders}
    final = convergence[str(orders[-1])]
    A, B, C = (final[key] for key in "ABC")
    report = {
        "activation": "sin(x)/sqrt(E sin(G)^2)",
        "normalization": sqrt(2 / (1 - exp(-2))),
        "method": "direct Gaussian quadrature of frozen M_nu atoms; no Hermite activation approximation",
        "quadrature_convergence": convergence,
        "prediction": final,
        "mu0": B / (2 * A * A),
        "mu1": (4 * B * B - A * C) / (24 * A**5),
    }
    path = HERE / "NORMALIZED_SINE_PREDICTION.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(path.read_text())


if __name__ == "__main__":
    main()
