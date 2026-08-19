"""High-precision analytic-Fourier evaluation of the normalized-sine atoms."""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb
from pathlib import Path

from .depth_population_jet import compile_depth, specialize_unit_gram


HERE = Path(__file__).resolve().parent


def decimal_fraction(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def sine_atom(exponent: tuple[int, ...], normalization: Decimal) -> Decimal:
    sine_power = sum(
        exponent[order] for order in range(len(exponent)) if order % 4 in (0, 2)
    )
    cosine_power = sum(
        exponent[order] for order in range(len(exponent)) if order % 4 in (1, 3)
    )
    derivative_sign = -1 if sum(
        exponent[order] for order in range(len(exponent)) if order % 4 in (2, 3)
    ) % 2 else 1
    if sine_power % 2:
        return Decimal(0)
    fourier_sign = (-1) ** (sine_power // 2)
    denominator = 2 ** (sine_power + cosine_power)
    answer = Decimal(0)
    for j in range(sine_power + 1):
        for k in range(cosine_power + 1):
            frequency = sine_power + cosine_power - 2 * (j + k)
            coefficient = Fraction(
                fourier_sign * (-1) ** j * comb(sine_power, j) * comb(cosine_power, k),
                denominator,
            )
            answer += decimal_fraction(coefficient) * (
                -Decimal(frequency * frequency) / 2
            ).exp()
    return Decimal(derivative_sign) * answer / normalization ** (
        sine_power + cosine_power
    )


def evaluate(root, normalization: Decimal) -> Decimal:
    memo = {}

    def visit(node):
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = decimal_fraction(node.node[1])
        elif kind == "symbol":
            value = Decimal(1)
        elif kind == "atom":
            value = sine_atom(node.node[2], normalization)
        elif kind == "add":
            value = sum((visit(child) for child in node.node[1]), Decimal(0))
        elif kind == "mul":
            value = Decimal(1)
            for child in node.node[1]:
                value *= visit(child)
        else:
            raise ValueError(kind)
        memo[node] = value
        return value

    return visit(root)


def main() -> None:
    getcontext().prec = 80
    normalization = ((Decimal(1) - Decimal(-2).exp()) / 2).sqrt()
    records = {}
    for depth in (2, 3, 4):
        result = compile_depth(depth)
        A, B, C = (
            evaluate(specialize_unit_gram(root), normalization)
            for root in (result.A, result.B, result.C)
        )
        mu0 = B / (2 * A * A)
        mu1 = (4 * B * B - A * C) / (24 * A**5)
        records[str(depth)] = {
            "A": str(A),
            "B": str(B),
            "C": str(C),
            "mu0": str(mu0),
            "mu1": str(mu1),
            "mu0_sign": "positive" if mu0 > 0 else "negative" if mu0 < 0 else "zero",
            "mu1_sign": "positive" if mu1 > 0 else "negative" if mu1 < 0 else "zero",
        }
    payload = {
        "schema": "route-s-normalized-sine-control-v1",
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "method": "80-digit exact finite Fourier expansion of each Gaussian atom",
        "forward_grams": "Q^ell=1 for every ell",
        "records_by_hidden_depth": records,
    }
    output = HERE / "NORMALIZED_SINE_CONTROL.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("sha256", digest)


if __name__ == "__main__":
    main()

