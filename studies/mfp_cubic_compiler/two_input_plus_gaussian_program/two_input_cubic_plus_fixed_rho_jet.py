#!/usr/bin/env python3
"""Exact fixed-correlation specialization of the two-input cubic plus jet."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable


Q = Fraction
Progress = Callable[[str], None]
HERE = Path(__file__).resolve().parent
ORDER9_PROTOCOL = HERE / "ORDER9_FIXED_RHO_PROTOCOL.md"
BASE_ENGINE = HERE / "two_input_cubic_plus_jet.py"
ORDER3_RESULTS = HERE / "results_order3.json"
ONE_INPUT_RESULTS = (
    HERE.parent / "depth2_gaussian_program" / "results_order9.json"
)

EXPECTED_SHA256 = {
    "order9_protocol": (
        "8c4e7e51c19fdffaaf3d0afdbf73ba2bc2081c14c205a0271617e63a50a02320"
    ),
    "base_engine": (
        "ec3c195f500fc09c22a7cfcbe72a9f2a3c2312fcb7835ab885fa21746b157426"
    ),
    "order3_results": (
        "6d5178f1d044974712ad6be705c9231d1ec4a3c6454c0ad8aa5ea932b27f093b"
    ),
    "one_input_results": (
        "6ef10c12960929bc95437eb44407b8e84c6b4e4f3b10b4e8416ad8666bd56979"
    ),
}
ALLOWED_RHOS = (Q(0), Q(1, 2), Q(1))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    return {
        "order9_protocol": sha256(ORDER9_PROTOCOL),
        "base_engine": sha256(BASE_ENGINE),
        "order3_results": sha256(ORDER3_RESULTS),
        "one_input_results": sha256(ONE_INPUT_RESULTS),
    }


def assert_source_hashes() -> dict[str, str]:
    actual = source_hashes()
    if actual != EXPECTED_SHA256:
        raise AssertionError(
            f"source SHA-256 gate failed: actual={actual}, "
            f"expected={EXPECTED_SHA256}"
        )
    return actual


def load_base_engine() -> Any:
    specification = importlib.util.spec_from_file_location(
        "fixed_rho_two_input_base_engine", BASE_ENGINE
    )
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load {BASE_ENGINE}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def serialize_fraction(value: Fraction) -> int | str:
    if value.denominator == 1:
        return value.numerator
    return fraction_string(value)


def parse_fraction(value: int | str) -> Fraction:
    return Q(value)


def constant_value(polynomial: tuple[Fraction, ...]) -> Fraction:
    if len(polynomial) != 1:
        raise AssertionError(
            "fixed-correlation run retained a symbolic rho dependence: "
            f"{polynomial}"
        )
    return polynomial[0]


def evaluate_stored_polynomial(
    coefficient_strings: Iterable[str], rho: Fraction
) -> Fraction:
    value = Q(0)
    for coefficient in reversed(tuple(coefficient_strings)):
        value = value * rho + Q(coefficient)
    return value


@dataclass
class FixedJetResult:
    rho: Fraction
    route: str
    derivatives: list[Fraction]
    sample_derivatives: list[list[Fraction]]
    analytic_initial_kernel: Fraction
    elapsed_seconds: float
    state_counts: list[dict[str, int]]
    wick_cache_sizes: dict[str, int]


def run_fixed_rho(
    engine: Any,
    rho: Fraction,
    route: str,
    max_order: int,
    progress: Progress | None = None,
) -> FixedJetResult:
    """Run one exact assembler after specializing rho in the coefficient ring."""

    rho = Q(rho)
    if rho not in ALLOWED_RHOS:
        raise ValueError(f"rho must be one of {ALLOWED_RHOS}, got {rho}")
    if route not in ("taylor", "derivative"):
        raise ValueError("route must be taylor or derivative")
    if not 0 <= max_order <= 9:
        raise ValueError("max_order must lie between zero and nine")

    previous = engine.RHO_VARIABLE
    engine.RHO_VARIABLE = engine.rho_constant(rho)
    try:
        assembler = (
            engine.taylor_jet if route == "taylor" else engine.derivative_jet
        )
        raw = assembler(max_order, progress)
        analytic_initial = constant_value(engine.analytic_initial_kernel())
    finally:
        engine.RHO_VARIABLE = previous

    return FixedJetResult(
        rho=rho,
        route=route,
        derivatives=[constant_value(value) for value in raw.derivatives],
        sample_derivatives=[
            [constant_value(value) for value in sample]
            for sample in raw.sample_derivatives
        ],
        analytic_initial_kernel=analytic_initial,
        elapsed_seconds=raw.elapsed_seconds,
        state_counts=raw.state_counts,
        wick_cache_sizes=raw.wick_cache_sizes,
    )


def validate_single(
    result: FixedJetResult,
    max_order: int,
    order3_document: dict[str, Any],
    one_input_document: dict[str, Any],
) -> None:
    for order in range(0, max_order + 1, 2):
        if result.derivatives[order] != 0:
            raise AssertionError(
                f"{result.route}, rho={result.rho}: parity gate F^{order}"
            )

    for sample in result.sample_derivatives:
        if sample != result.derivatives:
            raise AssertionError(
                f"{result.route}, rho={result.rho}: sample-exchange gate"
            )

    for order in (1, 3):
        if order > max_order:
            continue
        expected = evaluate_stored_polynomial(
            order3_document["derivatives"][f"F_{order}"], result.rho
        )
        if result.derivatives[order] != expected:
            raise AssertionError(
                f"{result.route}, rho={result.rho}: "
                f"symbolic order-{order} gate"
            )

    if max_order >= 1 and result.derivatives[1] != result.analytic_initial_kernel:
        raise AssertionError(
            f"{result.route}, rho={result.rho}: direct-gradient F^1 gate"
        )

    if result.rho == 1:
        expected = [
            parse_fraction(value)
            for value in one_input_document["derivatives"][: max_order + 1]
        ]
        if result.derivatives != expected:
            raise AssertionError(
                f"{result.route}: rho=1 one-input endpoint gate"
            )


def validate_pair(results: list[FixedJetResult]) -> None:
    if len(results) == 2 and results[0].derivatives != results[1].derivatives:
        raise AssertionError(
            f"exact route disagreement at rho={results[0].rho}"
        )


def result_payload(result: FixedJetResult) -> dict[str, Any]:
    return {
        "route": result.route,
        "derivatives": [
            serialize_fraction(value) for value in result.derivatives
        ],
        "elapsed_seconds": result.elapsed_seconds,
        "order9_state_counts": (
            result.state_counts[-1] if result.state_counts else {}
        ),
        "wick_cache_sizes": result.wick_cache_sizes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rho", required=True)
    parser.add_argument("--max-order", type=int, default=9)
    parser.add_argument(
        "--route",
        choices=("taylor", "derivative", "both"),
        default="both",
    )
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    rho = Q(args.rho)
    if rho not in ALLOWED_RHOS:
        parser.error("rho must be 0, 1/2, or 1")

    hashes = assert_source_hashes()
    engine = load_base_engine()
    order3_document = json.loads(ORDER3_RESULTS.read_text())
    one_input_document = json.loads(ONE_INPUT_RESULTS.read_text())
    progress: Progress | None = None if args.quiet else print

    routes = (
        ("taylor", "derivative")
        if args.route == "both"
        else (args.route,)
    )
    results: list[FixedJetResult] = []
    for route in routes:
        result = run_fixed_rho(
            engine, rho, route, args.max_order, progress
        )
        validate_single(
            result, args.max_order, order3_document, one_input_document
        )
        results.append(result)
    validate_pair(results)

    angle = {Q(0): "90 degrees", Q(1, 2): "60 degrees", Q(1): "0 degrees"}[rho]
    payload = {
        "model": "two-input-equal-label-raw-cubic-depth2-plus-channel",
        "rho": fraction_string(rho),
        "rho_interpretation": f"cosine similarity; angle={angle}",
        "max_order": args.max_order,
        "source_sha256": hashes,
        "validation": {
            "status": "passed",
            "exact_route_agreement": (
                True if len(results) == 2 else "checked in paired audit"
            ),
            "even_order_parity": True,
            "sample_exchange_symmetry": True,
            "symbolic_lower_orders": True,
            "direct_initial_gradient_block": True,
            "rho_1_one_input_endpoint": rho == 1,
            "fixed_rational_specialization": True,
        },
        "results": [result_payload(result) for result in results],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for result in results:
            derivatives = ", ".join(
                f"F^{order}={fraction_string(value)}"
                for order, value in enumerate(result.derivatives)
            )
            print(f"{result.route}: {derivatives}")
        print("validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
