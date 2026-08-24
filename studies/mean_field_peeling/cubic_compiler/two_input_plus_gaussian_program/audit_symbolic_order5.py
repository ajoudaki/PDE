#!/usr/bin/env python3
"""Reproduce and audit the accepted symbolic two-input cubic jet."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path
from types import ModuleType


Q = Fraction
Polynomial = tuple[Fraction, ...]
HERE = Path(__file__).resolve().parent
CUBIC = HERE.parent
MEAN_FIELD = CUBIC.parent

FILES = {
    "result": HERE / "results_symbolic_order5.json",
    "base_protocol": HERE / "PROTOCOL.md",
    "order3_result": HERE / "results_order3.json",
    "gaussian_program": HERE / "two_input_cubic_plus_jet.py",
    "fixed_rho_order9_protocol": HERE / "ORDER9_FIXED_RHO_PROTOCOL.md",
    "symbolic_order9_protocol": HERE / "ORDER9_SYMBOLIC_RHO_PROTOCOL.md",
    "connected_protocol": HERE / "ORDER9_CONNECTED_PROTOCOL.md",
    "color_quotient_amendment": (
        HERE / "ORDER9_CONNECTED_COLOR_QUOTIENT_AMENDMENT.md"
    ),
    "fixed_connected_amendment": (
        HERE / "ORDER9_FIXED_RHO_CONNECTED_AMENDMENT.md"
    ),
    "connected_polynomial_program": HERE / "two_input_cubic_connected.cpp",
    "connected_fixed_program": HERE / "two_input_cubic_connected_fixed.cpp",
    "fixed_gaussian_program": HERE / "two_input_cubic_plus_fixed_rho_jet.py",
    "connected_quadratic_parent": (
        MEAN_FIELD / "quadratic_compiler/campaign2/two_input_connected.cpp"
    ),
    "one_input_order9_result": (
        CUBIC / "depth2_gaussian_program/results_order9.json"
    ),
    "one_input_cubic_program": (
        CUBIC / "depth2_gaussian_program/depth2_cubic_exact_jet.py"
    ),
}

EXPECTED_SHA256 = {
    "result": "ac948d64b979f226424e1ff745512f0f97e78e164708f4313c41a48d41591023",
    "base_protocol": "6742675cb0c40dcfb2652edab05ce078b00506bfdef4bfd25157a22b0dbea956",
    "order3_result": "6d5178f1d044974712ad6be705c9231d1ec4a3c6454c0ad8aa5ea932b27f093b",
    "gaussian_program": "ec3c195f500fc09c22a7cfcbe72a9f2a3c2312fcb7835ab885fa21746b157426",
    "fixed_rho_order9_protocol": "8c4e7e51c19fdffaaf3d0afdbf73ba2bc2081c14c205a0271617e63a50a02320",
    "symbolic_order9_protocol": "85889d28417f7b04b4e69d578a843c554de450e30715fc239da0262c6bdca8bf",
    "connected_protocol": "8dff6184c215df1e4b6b8c4d7ed958c012e2f88054c1ab70becee666bb0e4534",
    "color_quotient_amendment": "1100031dcdcb768faa524efedc83ba61343d5c67795adc24b407e193751e3205",
    "fixed_connected_amendment": "ff8cb6c856daede0e8f78444792f756f4326abdacd001f43a68935a93a715895",
    "connected_polynomial_program": "5ba7709c9a7066ea475b7ebe2e26a5e18d575eb5ba8f81f92a59772b2ceb80f4",
    "connected_fixed_program": "56a9cbe297c8ab39ae3ce4d1167c3c69b73395ed46a35666791ed104a64c42ee",
    "fixed_gaussian_program": "198ed57cef8bcd1b1f8c970237a793f234d190dfc82d80c9101e7b3a690df922",
    "connected_quadratic_parent": "85c5c47c92bf926d4835120eac2be2f7d9ee70df12d3cd60359ea78ecacaed8e",
    "one_input_order9_result": "6ef10c12960929bc95437eb44407b8e84c6b4e4f3b10b4e8416ad8666bd56979",
    "one_input_cubic_program": "edb16223deb34586019a936809eec8cd7553c9eeea10e1cc957a6984a122af72",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(polynomial: tuple[Fraction, ...] | list[Fraction]) -> Polynomial:
    result = list(polynomial)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result) if result else (Q(0),)


def parse_polynomial(values: list[str]) -> Polynomial:
    return trim([Q(value) for value in values])


def evaluate(polynomial: Polynomial, rho: Fraction) -> Fraction:
    value = Q(0)
    for coefficient in reversed(polynomial):
        value = value * rho + coefficient
    return value


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def actual_hashes() -> dict[str, str]:
    return {name: sha256(path) for name, path in FILES.items()}


def load_document() -> dict[str, object]:
    return json.loads(FILES["result"].read_text())


def derivative_polynomials(document: dict[str, object]) -> list[Polynomial]:
    derivatives = document["derivatives"]
    if not isinstance(derivatives, dict):
        raise TypeError("derivatives must be a JSON object")
    return [
        parse_polynomial(derivatives[f"F_{order}"])
        for order in range(6)
    ]


def static_audit(document: dict[str, object]) -> dict[str, str]:
    hashes = actual_hashes()
    if hashes != EXPECTED_SHA256:
        raise AssertionError(
            f"SHA-256 gate failed: actual={hashes}, expected={EXPECTED_SHA256}"
        )

    stored_source_hashes = document["source_sha256"]
    if not isinstance(stored_source_hashes, dict):
        raise TypeError("source_sha256 must be a JSON object")
    if stored_source_hashes != {
        name: digest for name, digest in hashes.items() if name != "result"
    }:
        raise AssertionError("embedded source hashes do not match audited files")

    derivatives = derivative_polynomials(document)
    for order in (0, 2, 4):
        if derivatives[order] != (Q(0),):
            raise AssertionError(f"parity gate failed at order {order}")

    order3 = json.loads(FILES["order3_result"].read_text())
    for order in range(4):
        old = parse_polynomial(order3["derivatives"][f"F_{order}"])
        if derivatives[order] != old:
            raise AssertionError(f"order-three regression failed at {order}")

    specializations = document["exact_specializations"]
    if not isinstance(specializations, dict):
        raise TypeError("exact_specializations must be a JSON object")
    for record in specializations.values():
        if not isinstance(record, dict):
            raise TypeError("specialization record must be a JSON object")
        rho = Q(record["rho"])
        for order, polynomial in enumerate(derivatives):
            if evaluate(polynomial, rho) != Q(record[f"F_{order}"]):
                raise AssertionError(
                    f"stored specialization failed at rho={rho}, order={order}"
                )

    one_input = json.loads(FILES["one_input_order9_result"].read_text())
    for order, polynomial in enumerate(derivatives):
        if evaluate(polynomial, Q(1)) != Q(one_input["derivatives"][order]):
            raise AssertionError(
                f"one-input endpoint failed at derivative order {order}"
            )
    return hashes


def compile_cpp(source: Path, executable: Path) -> None:
    compiler = shutil.which("g++")
    if compiler is None:
        raise RuntimeError("g++ is required for the connected-tree audit")
    subprocess.run(
        [
            compiler,
            "-O3",
            "-std=c++17",
            "-Wall",
            "-Wextra",
            "-pedantic",
            str(source),
            "-o",
            str(executable),
        ],
        check=True,
        text=True,
        capture_output=True,
    )


def run_json(command: list[str], timeout: int = 300) -> dict[str, object]:
    completed = subprocess.run(
        command,
        check=True,
        text=True,
        capture_output=True,
        timeout=timeout,
    )
    return json.loads(completed.stdout)


def normalized_connected_polynomials(payload: dict[str, object]) -> list[Polynomial]:
    raw = payload["raw_theta"]
    if not isinstance(raw, list):
        raise TypeError("raw_theta must be a JSON array")
    result: list[Polynomial] = []
    for order, coefficients in enumerate(raw):
        if not isinstance(coefficients, list):
            raise TypeError("raw polynomial must be a JSON array")
        scale = Q(1, 2 ** (order + 1))
        result.append(trim([Q(value) * scale for value in coefficients]))
    return result


def connected_audit(
    document: dict[str, object], temporary: Path
) -> dict[str, object]:
    expected = derivative_polynomials(document)
    polynomial_executable = temporary / "two_input_cubic_connected"
    fixed_executable = temporary / "two_input_cubic_connected_fixed"
    compile_cpp(FILES["connected_polynomial_program"], polynomial_executable)
    compile_cpp(FILES["connected_fixed_program"], fixed_executable)

    polynomial_payload = run_json(
        [str(polynomial_executable), "plus", "5", "audit"]
    )
    if polynomial_payload["terminal_audit"] is not True:
        raise AssertionError("both terminal evaluators were not enabled")
    connected = normalized_connected_polynomials(polynomial_payload)
    if connected != expected:
        raise AssertionError("connected and Gaussian-program polynomials disagree")

    fixed_records: dict[str, dict[str, object]] = {}
    for rho_text in ("0", "1/2", "1"):
        payload = run_json(
            [str(fixed_executable), "plus", "5", rho_text]
        )
        raw_values = payload["raw_values"]
        if not isinstance(raw_values, list):
            raise TypeError("raw_values must be a JSON array")
        values = [
            Q(raw_value) / 2 ** (order + 1)
            for order, raw_value in enumerate(raw_values)
        ]
        rho = Q(rho_text)
        exact_evaluations = [evaluate(polynomial, rho) for polynomial in expected]
        if values != exact_evaluations:
            raise AssertionError(f"fixed connected gate failed at rho={rho_text}")
        fixed_records[rho_text] = {
            "derivatives": [fraction_string(value) for value in values],
            "value_cache": payload["value_cache"],
            "wick_cache": payload["wick_cache"],
            "base_evaluations": payload["base_evaluations"],
        }

    return {
        "polynomial_terminal_audit": True,
        "value_cache": polynomial_payload["value_cache"],
        "wick_cache": polynomial_payload["wick_cache"],
        "base_evaluations": polynomial_payload["base_evaluations"],
        "fixed_correlations": fixed_records,
    }


def load_gaussian_engine() -> ModuleType:
    specification = importlib.util.spec_from_file_location(
        "symbolic_order5_gaussian_program", FILES["gaussian_program"]
    )
    if specification is None or specification.loader is None:
        raise ImportError("cannot load the Gaussian-program source")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def full_gaussian_audit(document: dict[str, object]) -> dict[str, object]:
    engine = load_gaussian_engine()
    taylor = engine.taylor_jet(5)
    derivative = engine.derivative_jet(5)
    engine.validate_results((taylor, derivative), 5)
    expected = derivative_polynomials(document)
    if list(taylor.derivatives) != expected:
        raise AssertionError("Taylor Gaussian program disagrees with storage")
    if list(derivative.derivatives) != expected:
        raise AssertionError("derivative-normalized program disagrees with storage")
    return {
        "ordinary_taylor_seconds": taylor.elapsed_seconds,
        "derivative_normalized_seconds": derivative.elapsed_seconds,
        "exact_route_agreement": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--full-gaussian",
        action="store_true",
        help="also rerun both slow exact Gaussian-program order-five routes",
    )
    args = parser.parse_args()

    document = load_document()
    hashes = static_audit(document)
    with tempfile.TemporaryDirectory(prefix="cubic-order5-audit-") as name:
        connected = connected_audit(document, Path(name))

    gaussian: dict[str, object] | str
    if args.full_gaussian:
        gaussian = full_gaussian_audit(document)
    else:
        gaussian = (
            "not rerun; use --full-gaussian for the two approximately "
            "seven-to-eight-minute routes"
        )

    payload = {
        "model": document["model"],
        "accepted_max_order": 5,
        "validation": "passed",
        "sha256": hashes,
        "static_exact_gates": True,
        "connected_tree_reproduction": connected,
        "gaussian_program_reproduction": gaussian,
        "claim_boundary": document["claim_boundary"],
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
