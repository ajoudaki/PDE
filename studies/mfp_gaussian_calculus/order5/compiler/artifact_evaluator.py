"""Independent evaluator for the emitted arithmetic-DAG normal-form files."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
from typing import Iterable

from .population_jet import MAX_DERIV, activation_product_moment


ATOM = re.compile(r"([XYM])_\{([0-9]{6})\}")


def evaluate_artifact_polynomial(
    path: str | Path,
    coefficients: Iterable[int | Fraction],
    *,
    q0: int | Fraction = 1,
) -> dict[str, Fraction]:
    """Parse and evaluate a generated file without importing its compiler IR."""

    coefficients = tuple(Fraction(value) for value in coefficients)
    q0 = Fraction(q0)
    exponent20 = (2,) + (0,) * MAX_DERIV
    q1 = activation_product_moment(exponent20, coefficients, q0)
    values: dict[str, Fraction] = {"Q0": q0}
    atom_cache: dict[tuple[str, tuple[int, ...]], Fraction] = {}

    def factor_value(token: str) -> Fraction:
        token = token.strip()
        if token in values:
            return values[token]
        match = ATOM.fullmatch(token)
        if match:
            layer = match.group(1)
            short = tuple(int(digit) for digit in match.group(2))
            exponent = short + (0,) * (MAX_DERIV + 1 - len(short))
            key = (layer, exponent)
            if key not in atom_cache:
                variance = q0 if layer in {"X", "M"} else q1
                atom_cache[key] = activation_product_moment(exponent, coefficients, variance)
            return atom_cache[key]
        return Fraction(token)

    for raw_line in Path(path).read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        name, rhs = (part.strip() for part in line.split("=", 1))
        total = Fraction(0)
        for summand in rhs.split(" + "):
            product = Fraction(1)
            for factor in summand.split(" * "):
                product *= factor_value(factor)
            total += product
        values[name] = total
    return {name: values[name] for name in ("A", "B", "C")}
