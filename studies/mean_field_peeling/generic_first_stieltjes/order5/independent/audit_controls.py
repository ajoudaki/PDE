"""Exact polynomial controls for the independent coefficient maps."""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import json
from pathlib import Path

from .independent_compiler import MPoly, compile_layer_tagged, compile_unit_gram


Polynomial = list[Fraction]


def _multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def _derivative(poly: Polynomial, order: int) -> Polynomial:
    out = list(poly)
    for _ in range(order):
        out = [Fraction(k) * out[k] for k in range(1, len(out))] or [Fraction(0)]
    return out


def _gaussian_power(power: int, variance: Fraction) -> Fraction:
    if power % 2:
        return Fraction(0)
    return Fraction(factorial(power), 2 ** (power // 2) * factorial(power // 2)) * variance ** (power // 2)


def activation_atom(counts: tuple[int, ...], activation: Polynomial, variance: Fraction) -> Fraction:
    integrand = [Fraction(1)]
    for order, multiplicity in enumerate(counts):
        factor = _derivative(activation, order)
        for _ in range(multiplicity):
            integrand = _multiply(integrand, factor)
    return sum(
        (coefficient * _gaussian_power(power, variance) for power, coefficient in enumerate(integrand)),
        Fraction(0),
    )


def evaluate(mapping: MPoly, activation: Polynomial, *, tagged: bool) -> Fraction:
    q1 = activation_atom((2,), activation, Fraction(1))
    answer = Fraction(0)
    for monomial, coefficient in mapping.items():
        value = coefficient
        for atom in monomial:
            if tagged:
                layer, counts = atom[0], atom[1:]
                value *= activation_atom(counts, activation, Fraction(1) if layer == -1 else q1)
            else:
                value *= activation_atom(atom, activation, Fraction(1))
        answer += value
    return answer


def main() -> None:
    unit = compile_unit_gram()
    tagged = compile_layer_tagged(q0=1)
    controls = {
        "constant_1_unit": (unit, [Fraction(1)], False, (1, 0, 0)),
        "linear_unit": (unit, [Fraction(0), Fraction(1)], False, (3, 48, 1464)),
        "affine_1_plus_x_tagged": (tagged, [Fraction(1), Fraction(1)], True, (6, 112, 4400)),
        "quadratic_tagged": (tagged, [Fraction(0), Fraction(0), Fraction(1)], True, (111, 1685184, 77400633120)),
    }
    report: dict[str, object] = {}
    for name, (result, activation, is_tagged, expected) in controls.items():
        actual = tuple(evaluate(getattr(result, key), activation, tagged=is_tagged) for key in "ABC")
        report[name] = {
            "actual": [str(value) for value in actual],
            "expected": [str(value) for value in expected],
            "pass": actual == expected,
        }
    parity = {
        "unit": [len(unit.f_coefficients[k]) for k in (0, 2, 4)],
        "tagged": [len(tagged.f_coefficients[k]) for k in (0, 2, 4)],
    }
    report["parity_term_counts"] = parity
    report["pass"] = all(item.get("pass", True) for item in report.values() if isinstance(item, dict)) and parity == {"unit": [0, 0, 0], "tagged": [0, 0, 0]}
    path = Path(__file__).resolve().parent / "CONTROL_AUDIT.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(path.read_text())
    if not report["pass"]:
        raise SystemExit("control audit failed")


if __name__ == "__main__":
    main()
