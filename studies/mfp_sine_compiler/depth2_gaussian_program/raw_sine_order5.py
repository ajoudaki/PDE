#!/usr/bin/env python3
"""Closed-Fourier evaluation of the raw-sine depth-2 jet through order five."""

from __future__ import annotations

import hashlib
import json
import re
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from numpy.polynomial.hermite import hermgauss


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PROTOCOL = HERE / "PROTOCOL.md"
PRIMARY = (
    REPO
    / "studies/mean_field_peeling/generic_first_stieltjes/order5/compiler"
    / "LAYER_SEPARATED_ABC_NORMAL_FORM.txt"
)
INDEPENDENT = (
    REPO
    / "studies/mean_field_peeling/generic_first_stieltjes/order5/independent"
    / "independent_layer_tagged_coefficient_map.json"
)

EXPECTED_SHA256 = {
    "protocol": "27843d8916167fabfbf59f8412f904a11282ebee2ea23424e4aa0512c7d78f4e",
    "primary": "5219b3558aec52a2065b93ba7d6ce0e350ee930c2048518fcd012ba61f605ec9",
    "independent": "52832afc4f9e1cf27f5b8465f2f5373bcb3e9f5c56b0686c9366162da2e17c11",
}

PRIMARY_ATOM = re.compile(r"([XYM])_\{([0-9]{6})\}")
INDEPENDENT_ATOM = re.compile(r"([XYM])_([0-9]{6})")
ComplexFraction = tuple[Fraction, Fraction]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_add(
    left: ComplexFraction, right: ComplexFraction
) -> ComplexFraction:
    return left[0] + right[0], left[1] + right[1]


def complex_multiply(
    left: ComplexFraction, right: ComplexFraction
) -> ComplexFraction:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def derivative_fourier_factor(
    derivative: int,
) -> dict[int, ComplexFraction]:
    """Fourier coefficients of ``sin(x + derivative*pi/2)`` exactly."""

    phases: tuple[ComplexFraction, ...] = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    phase = phases[derivative % 4]
    conjugate = (phase[0], -phase[1])
    minus_i_over_two = (Fraction(0), Fraction(-1, 2))
    plus_i_over_two = (Fraction(0), Fraction(1, 2))
    return {
        1: complex_multiply(phase, minus_i_over_two),
        -1: complex_multiply(conjugate, plus_i_over_two),
    }


def product_fourier_coefficients(
    exponent: tuple[int, ...],
) -> dict[int, ComplexFraction]:
    coefficients: dict[int, ComplexFraction] = {
        0: (Fraction(1), Fraction(0))
    }
    for derivative, multiplicity in enumerate(exponent):
        factor = derivative_fourier_factor(derivative)
        for _ in range(multiplicity):
            product: dict[int, ComplexFraction] = {}
            for left_frequency, left_value in coefficients.items():
                for right_frequency, right_value in factor.items():
                    frequency = left_frequency + right_frequency
                    value = complex_multiply(left_value, right_value)
                    product[frequency] = complex_add(
                        product.get(
                            frequency, (Fraction(0), Fraction(0))
                        ),
                        value,
                    )
            coefficients = {
                frequency: value
                for frequency, value in product.items()
                if value != (0, 0)
            }
    return coefficients


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


class ClosedFourierMoments:
    """High-precision Gaussian sine/cosine product moments."""

    def __init__(self, dps: int) -> None:
        mp.mp.dps = dps
        self.dps = dps
        self.q0 = mp.mpf(1)
        self.q1 = (1 - mp.exp(-2)) / 2
        self.cache: dict[tuple[str, tuple[int, ...]], mp.mpf] = {}

    def __call__(self, layer: str, exponent: tuple[int, ...]) -> mp.mpf:
        key = (layer, exponent)
        if key in self.cache:
            return self.cache[key]
        variance = self.q0 if layer in {"X", "M"} else self.q1
        value = mp.mpc(0)
        for frequency, coefficient in product_fourier_coefficients(
            exponent
        ).items():
            coefficient_mp = mp.mpc(
                mp_fraction(coefficient[0]), mp_fraction(coefficient[1])
            )
            value += coefficient_mp * mp.exp(
                -mp.mpf(frequency * frequency) * variance / 2
            )
        imaginary_tolerance = mp.power(10, -self.dps + 15)
        if abs(mp.im(value)) > imaginary_tolerance:
            raise ArithmeticError(
                f"sine-product moment retained imaginary part {mp.im(value)}"
            )
        answer = mp.re(value)
        self.cache[key] = answer
        return answer


class QuadratureMoments:
    """Independent double-precision Gauss--Hermite atom evaluator."""

    def __init__(self, order: int) -> None:
        nodes, weights = hermgauss(order)
        self.nodes = nodes
        self.weights = weights / np.sqrt(np.pi)
        self.q0 = 1.0
        self.q1 = (1.0 - np.exp(-2.0)) / 2.0
        self.cache: dict[tuple[str, tuple[int, ...]], float] = {}

    def __call__(self, layer: str, exponent: tuple[int, ...]) -> float:
        key = (layer, exponent)
        if key in self.cache:
            return self.cache[key]
        variance = self.q0 if layer in {"X", "M"} else self.q1
        gaussian = np.sqrt(2.0 * variance) * self.nodes
        integrand = np.ones_like(gaussian)
        for derivative, multiplicity in enumerate(exponent):
            if multiplicity:
                integrand *= np.sin(
                    gaussian + derivative * np.pi / 2.0
                ) ** multiplicity
        value = float(self.weights @ integrand)
        self.cache[key] = value
        return value


def evaluate_primary(moment_oracle) -> dict[str, object]:
    values: dict[str, object] = {"Q0": 1}
    atom_cache: dict[tuple[str, tuple[int, ...]], object] = {}

    def factor_value(token: str):
        token = token.strip()
        if token in values:
            return values[token]
        match = PRIMARY_ATOM.fullmatch(token)
        if match:
            layer = match.group(1)
            exponent = tuple(int(digit) for digit in match.group(2))
            key = (layer, exponent)
            if key not in atom_cache:
                atom_cache[key] = moment_oracle(layer, exponent)
            return atom_cache[key]
        rational = Fraction(token)
        if isinstance(moment_oracle, ClosedFourierMoments):
            return mp_fraction(rational)
        return float(rational)

    for raw_line in PRIMARY.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        name, right_hand_side = (
            part.strip() for part in line.split("=", 1)
        )
        total = 0
        for summand in right_hand_side.split(" + "):
            product = 1
            for factor in summand.split(" * "):
                product *= factor_value(factor)
            total += product
        values[name] = total
    return {name: values[name] for name in ("A", "B", "C")}


def evaluate_independent(moment_oracle: ClosedFourierMoments) -> dict[str, mp.mpf]:
    document = json.loads(INDEPENDENT.read_text())
    output: dict[str, mp.mpf] = {}
    atom_cache: dict[tuple[str, tuple[int, ...]], mp.mpf] = {}
    for name in ("A", "B", "C"):
        total = mp.mpf(0)
        for term in document[name]:
            value = mp_fraction(Fraction(term["coefficient"]))
            for atom_text in term["atoms"]:
                match = INDEPENDENT_ATOM.fullmatch(atom_text)
                if match is None:
                    raise ValueError(f"unrecognized atom {atom_text}")
                layer = match.group(1)
                exponent = tuple(int(digit) for digit in match.group(2))
                key = (layer, exponent)
                if key not in atom_cache:
                    atom_cache[key] = moment_oracle(layer, exponent)
                value *= atom_cache[key]
            total += value
        output[name] = total
    return output


def relative_error(left, right) -> mp.mpf:
    return abs(left - right) / max(mp.mpf(1), abs(left), abs(right))


def value_strings(values: dict[str, mp.mpf], digits: int = 70) -> dict[str, str]:
    return {name: mp.nstr(value, digits) for name, value in values.items()}


def main() -> int:
    started = time.perf_counter()
    actual_hashes = {
        "protocol": sha256(PROTOCOL),
        "primary": sha256(PRIMARY),
        "independent": sha256(INDEPENDENT),
    }
    if actual_hashes != EXPECTED_SHA256:
        raise AssertionError(
            f"SHA-256 gate failed: actual={actual_hashes}, "
            f"expected={EXPECTED_SHA256}"
        )

    closed_runs: dict[int, dict[str, mp.mpf]] = {}
    independent_runs: dict[int, dict[str, mp.mpf]] = {}
    q1_runs: dict[int, mp.mpf] = {}
    for dps in (80, 120):
        oracle = ClosedFourierMoments(dps)
        closed_runs[dps] = evaluate_primary(oracle)
        independent_runs[dps] = evaluate_independent(oracle)
        q1_runs[dps] = oracle.q1

    primary = closed_runs[120]
    independent = independent_runs[120]
    route_errors = {
        name: relative_error(primary[name], independent[name])
        for name in ("A", "B", "C")
    }
    precision_errors = {
        name: relative_error(closed_runs[80][name], primary[name])
        for name in ("A", "B", "C")
    }
    if any(error > mp.mpf("1e-60") for error in route_errors.values()):
        raise AssertionError("primary and independent maps disagree")
    if any(error > mp.mpf("1e-60") for error in precision_errors.values()):
        raise AssertionError("80- and 120-digit Fourier evaluations disagree")
    if abs(primary["A"] - 1) > mp.mpf("1e-60"):
        raise AssertionError(f"raw-sine F1 gate failed: {primary['A']}")
    if abs(primary["B"] - mp.mpf("-1.88699982730593")) > mp.mpf("1e-13"):
        raise AssertionError(f"raw-sine F3 gate failed: {primary['B']}")

    quadrature: dict[int, dict[str, float]] = {}
    for order in (64, 96):
        quadrature[order] = evaluate_primary(QuadratureMoments(order))
    tolerances = {"A": 1.0e-10, "B": 1.0e-10, "C": 1.0e-7}
    for order, values in quadrature.items():
        for name, tolerance in tolerances.items():
            if abs(values[name] - float(primary[name])) > tolerance:
                raise AssertionError(
                    f"quadrature-{order} {name} gate failed: "
                    f"got {values[name]}, expected {primary[name]}"
                )

    jet = [
        "0",
        mp.nstr(primary["A"], 70),
        "0",
        mp.nstr(primary["B"], 70),
        "0",
        mp.nstr(primary["C"], 70),
    ]
    payload = {
        "model": "raw-sine-equal-width-two-hidden-layer",
        "activation": "sin(x)",
        "max_order": 5,
        "derivatives": jet,
        "forward_variance_q1": mp.nstr(q1_runs[120], 70),
        "closed_fourier_primary_120dps": value_strings(primary),
        "closed_fourier_independent_120dps": value_strings(independent),
        "primary_independent_relative_errors": {
            name: mp.nstr(value, 8) for name, value in route_errors.items()
        },
        "primary_80dps_vs_120dps_relative_errors": {
            name: mp.nstr(value, 8) for name, value in precision_errors.items()
        },
        "gauss_hermite_controls": {
            str(order): values for order, values in quadrature.items()
        },
        "parity": "F^(0), F^(2), and F^(4) vanish exactly",
        "validation": "passed",
        "elapsed_seconds": time.perf_counter() - started,
        "sha256": actual_hashes,
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
