#!/usr/bin/env python3
"""Closed-Fourier evaluation of the unit-variance sine depth-2 order-five jet."""

from __future__ import annotations

import hashlib
import json
import re
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp

from raw_sine_order5 import (
    ClosedFourierMoments,
    QuadratureMoments,
    mp_fraction,
    relative_error,
    value_strings,
)


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PROTOCOL = HERE / "NORMALIZED_PROTOCOL.md"
PRIMARY = (
    REPO
    / "studies/mean_field_peeling/generic_first_stieltjes/order5/compiler"
    / "UNIT_GRAM_ABC_NORMAL_FORM.txt"
)
INDEPENDENT = (
    REPO
    / "studies/mean_field_peeling/generic_first_stieltjes/order5/independent"
    / "independent_coefficient_map.json"
)

EXPECTED_SHA256 = {
    "protocol": "2e26e1ab6caeea06b304e05cb9c805bdf8dd55b150f3a11780930a3056ac4971",
    "primary": "3be176963679c40127ac4f94305eeb7e4ef684a06910ae99a68a0f3528333214",
    "independent": "fa3b4a6f7dc665e63e2c02355a14122f89f56bdfd34f0fe7402be4cab0ff2878",
}

PRIMARY_ATOM = re.compile(r"M_\{([0-9]{6})\}")
INDEPENDENT_ATOM = re.compile(r"M_([0-9]{6})")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class UnitFourierMoments:
    def __init__(self, dps: int) -> None:
        self.raw = ClosedFourierMoments(dps)
        self.scale_denominator = mp.sqrt(self.raw.q1)

    def __call__(self, exponent: tuple[int, ...]) -> mp.mpf:
        return self.raw("X", exponent) / self.scale_denominator ** sum(exponent)


class UnitQuadratureMoments:
    def __init__(self, order: int) -> None:
        self.raw = QuadratureMoments(order)
        self.scale_denominator = self.raw.q1**0.5

    def __call__(self, exponent: tuple[int, ...]) -> float:
        return self.raw("X", exponent) / self.scale_denominator ** sum(exponent)


def evaluate_primary(moment_oracle) -> dict[str, object]:
    values: dict[str, object] = {}
    atom_cache: dict[tuple[int, ...], object] = {}

    def factor_value(token: str):
        token = token.strip()
        if token in values:
            return values[token]
        match = PRIMARY_ATOM.fullmatch(token)
        if match:
            exponent = tuple(int(digit) for digit in match.group(1))
            if exponent not in atom_cache:
                atom_cache[exponent] = moment_oracle(exponent)
            return atom_cache[exponent]
        rational = Fraction(token)
        if isinstance(moment_oracle, UnitFourierMoments):
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


def evaluate_independent(moment_oracle: UnitFourierMoments) -> dict[str, mp.mpf]:
    terms = json.loads(INDEPENDENT.read_text())["unit_gram"]
    output: dict[str, mp.mpf] = {}
    atom_cache: dict[tuple[int, ...], mp.mpf] = {}
    for name in ("A", "B", "C"):
        total = mp.mpf(0)
        for term in terms[name]:
            value = mp_fraction(Fraction(term["coefficient"]))
            for atom_text in term["atoms"]:
                match = INDEPENDENT_ATOM.fullmatch(atom_text)
                if match is None:
                    raise ValueError(f"unrecognized atom {atom_text}")
                exponent = tuple(int(digit) for digit in match.group(1))
                if exponent not in atom_cache:
                    atom_cache[exponent] = moment_oracle(exponent)
                value *= atom_cache[exponent]
            total += value
        output[name] = total
    return output


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

    primary_runs: dict[int, dict[str, mp.mpf]] = {}
    independent_runs: dict[int, dict[str, mp.mpf]] = {}
    scales: dict[int, mp.mpf] = {}
    for dps in (80, 120):
        oracle = UnitFourierMoments(dps)
        primary_runs[dps] = evaluate_primary(oracle)
        independent_runs[dps] = evaluate_independent(oracle)
        scales[dps] = oracle.scale_denominator

    primary = primary_runs[120]
    independent = independent_runs[120]
    route_errors = {
        name: relative_error(primary[name], independent[name])
        for name in ("A", "B", "C")
    }
    precision_errors = {
        name: relative_error(primary_runs[80][name], primary[name])
        for name in ("A", "B", "C")
    }
    if any(error > mp.mpf("1e-60") for error in route_errors.values()):
        raise AssertionError("primary and independent unit maps disagree")
    if any(error > mp.mpf("1e-60") for error in precision_errors.values()):
        raise AssertionError("80- and 120-digit unit evaluations disagree")

    frozen = {
        "A": mp.mpf("4.037096946465644"),
        "B": mp.mpf("-103.25733114677422"),
        "C": mp.mpf("29944.432342937285"),
    }
    gate_tolerances = {
        "A": mp.mpf("1e-14"),
        "B": mp.mpf("1e-12"),
        "C": mp.mpf("1e-9"),
    }
    for name in ("A", "B", "C"):
        if abs(primary[name] - frozen[name]) > gate_tolerances[name]:
            raise AssertionError(
                f"normalized-sine {name} frozen gate failed: {primary[name]}"
            )

    quadrature: dict[int, dict[str, float]] = {}
    for order in (64, 96):
        quadrature[order] = evaluate_primary(UnitQuadratureMoments(order))
    quadrature_tolerances = {"A": 1.0e-10, "B": 1.0e-10, "C": 1.0e-7}
    for order, values in quadrature.items():
        for name, tolerance in quadrature_tolerances.items():
            if abs(values[name] - float(primary[name])) > tolerance:
                raise AssertionError(
                    f"unit quadrature-{order} {name} gate failed: "
                    f"got {values[name]}, expected {primary[name]}"
                )

    payload = {
        "model": "unit-variance-sine-equal-width-two-hidden-layer",
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "normalization_denominator": mp.nstr(scales[120], 70),
        "max_order": 5,
        "derivatives": [
            "0",
            mp.nstr(primary["A"], 70),
            "0",
            mp.nstr(primary["B"], 70),
            "0",
            mp.nstr(primary["C"], 70),
        ],
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
