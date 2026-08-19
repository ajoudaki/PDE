"""Exact control evaluator independent of all order-five producer code."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache, reduce
from typing import Iterable

from .reference_maps import Polynomial, load_reference


Poly = tuple[Fraction, ...]


def _trim(values: Iterable[Fraction]) -> Poly:
    values = list(values)
    while values and values[-1] == 0:
        values.pop()
    return tuple(values)


def derivative(poly: Poly, order: int) -> Poly:
    answer = poly
    for _ in range(order):
        answer = _trim((index * value for index, value in enumerate(answer[1:], 1)))
    return answer


def multiply(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return ()
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    return _trim(answer)


def power(poly: Poly, exponent: int) -> Poly:
    answer = (Fraction(1),)
    factor = poly
    while exponent:
        if exponent & 1:
            answer = multiply(answer, factor)
        exponent >>= 1
        if exponent:
            factor = multiply(factor, factor)
    return answer


def gaussian_moment(power_: int) -> int:
    if power_ & 1:
        return 0
    answer = 1
    for odd in range(1, power_, 2):
        answer *= odd
    return answer


def activation_atom(name: str, activation: Poly) -> Fraction:
    tag, encoded = name.split("_")
    if tag != "M" or len(encoded) != 6 or not encoded.isdigit():
        raise ValueError(name)
    value = (Fraction(1),)
    for order, count in enumerate(map(int, encoded)):
        value = multiply(value, power(derivative(activation, order), count))
    return sum(coefficient * gaussian_moment(degree) for degree, coefficient in enumerate(value))


def evaluate(poly: Polynomial, activation: Iterable[int | Fraction]) -> Fraction:
    activation = tuple(Fraction(value) for value in activation)

    @lru_cache(maxsize=None)
    def atom_value(name: str) -> Fraction:
        return activation_atom(name, activation)

    answer = Fraction(0)
    for atoms, coefficient in poly.items():
        answer += coefficient * reduce(
            lambda product, name: product * atom_value(name),
            atoms,
            Fraction(1),
        )
    return answer


def control_table() -> dict[str, dict[int, dict[str, str]]]:
    activations = {
        "constant_1": (1,),
        # E[(3/5+4G/5)^2]=1, so this is a genuine shared unit-Gram control.
        "unit_affine_3_4": (Fraction(3, 5), Fraction(4, 5)),
        "linear": (0, 1),
        # This is only a formal evaluation of the M_200000=1 quotient; x^2
        # itself has E[x^4]=3 and is not a unit-Gram shared activation.
        "formal_unit_quotient_x2": (0, 0, 1),
    }
    result: dict[str, dict[int, dict[str, str]]] = {}
    for label, activation in activations.items():
        result[label] = {}
        for depth in (2, 3, 4):
            maps = load_reference(depth)
            result[label][depth] = {
                root: str(evaluate(poly, activation)) for root, poly in maps.items()
            }
    return result


if __name__ == "__main__":
    import json

    print(json.dumps(control_table(), indent=2, sort_keys=True))
