"""Evaluate the frozen unit-Gram normal forms for normalized sine."""

from __future__ import annotations

import json
from fractions import Fraction
from math import exp, pi, sqrt
from pathlib import Path
import re

import numpy as np
from numpy.polynomial.hermite import hermgauss


ATOM = re.compile(r"M_\{([0-9]{6})\}")
HERE = Path(__file__).resolve().parent
PRIMARY = HERE.parent / "primary"


def evaluate_unit_artifact(path: Path, quadrature_order: int) -> dict[str, float]:
    nodes, weights = hermgauss(quadrature_order)
    gaussian = sqrt(2.0) * nodes
    weights = weights / sqrt(pi)
    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)
    values: dict[str, float] = {}
    moments: dict[str, float] = {}

    def factor(token: str) -> float:
        token = token.strip()
        if token in values:
            return values[token]
        match = ATOM.fullmatch(token)
        if match:
            key = match.group(1)
            if key not in moments:
                integrand = np.ones_like(gaussian)
                for derivative, multiplicity_text in enumerate(key):
                    multiplicity = int(multiplicity_text)
                    if multiplicity:
                        derivative_value = (
                            np.sin(gaussian + derivative * pi / 2.0)
                            / normalization
                        )
                        integrand *= derivative_value**multiplicity
                moments[key] = float(weights @ integrand)
            return moments[key]
        return float(Fraction(token))

    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        name, right_hand_side = (
            part.strip() for part in line.split("=", 1)
        )
        total = 0.0
        for summand in right_hand_side.split(" + "):
            product = 1.0
            for token in summand.split(" * "):
                product *= factor(token)
            total += product
        values[name] = total
    return {name: values[name] for name in ("A", "B", "C")}


def prediction(quadrature_order: int = 96) -> dict[str, object]:
    depths: dict[str, dict[str, float]] = {}
    for hidden_layers in (3, 4):
        values = evaluate_unit_artifact(
            PRIMARY / f"H{hidden_layers}_UNIT_ABC.cse.txt",
            quadrature_order,
        )
        a, b, c = values["A"], values["B"], values["C"]
        values["mu0"] = b / (2.0 * a * a)
        values["mu1"] = (
            4.0 * b * b - a * c
        ) / (24.0 * a**5)
        depths[str(hidden_layers)] = values
    return {
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "quadrature_order": quadrature_order,
        "source_manifest_sha256": (
            "f4838437c1fb70b14713d39e8438d703434c49ffd72001beeb6fee8d53366b30"
        ),
        "depths": depths,
    }


def main() -> None:
    outputs = {
        str(order): prediction(order)
        for order in (64, 96, 128)
    }
    target = HERE / "NORMALIZED_SINE_FROZEN_PREDICTION.json"
    target.write_text(json.dumps(outputs, indent=2, sort_keys=True) + "\n")
    print(json.dumps(outputs, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
