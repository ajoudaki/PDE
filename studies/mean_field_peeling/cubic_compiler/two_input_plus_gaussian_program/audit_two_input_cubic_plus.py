#!/usr/bin/env python3
"""Independent audit and kernel postprocessing for the cubic plus channel."""

from __future__ import annotations

import hashlib
import importlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


Q = Fraction
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO))
gnf_module = importlib.import_module(
    "studies.mean_field_peeling.generic_first_stieltjes.b2."
    "contracted_gnf_polynomial_reference"
)
normal_form_module = importlib.import_module(
    "studies.mean_field_peeling.generic_first_stieltjes.compiler.normal_form"
)
evaluate_contracted_directional_gnf = (
    gnf_module.evaluate_contracted_directional_gnf
)
PolynomialActivation = normal_form_module.PolynomialActivation
INPUT = HERE / "results_order3.json"
PROTOCOL = HERE / "PROTOCOL.md"
ENGINE = HERE / "two_input_cubic_plus_jet.py"
GNF_REFERENCE = (
    HERE.parents[1]
    / "generic_first_stieltjes/b2/contracted_gnf_polynomial_reference.py"
)
NORMAL_FORM = HERE.parents[1] / "generic_first_stieltjes/compiler/normal_form.py"

EXPECTED_SHA256 = {
    "input": "6d5178f1d044974712ad6be705c9231d1ec4a3c6454c0ad8aa5ea932b27f093b",
    "protocol": "6742675cb0c40dcfb2652edab05ce078b00506bfdef4bfd25157a22b0dbea956",
    "engine": "ec3c195f500fc09c22a7cfcbe72a9f2a3c2312fcb7835ab885fa21746b157426",
    "gnf_reference": "c9d12ddbe1101d14a61af85f2d350dea41c30ad5a8b918171085121daec548eb",
    "normal_form": "b81febfb840d3cc7a0e7c36c83e0a3187223994d29a50cdc4d63dbf30315f8c9",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_engine():
    specification = importlib.util.spec_from_file_location(
        "audited_two_input_cubic_plus", ENGINE
    )
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load {ENGINE}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def parse_polynomial(values: list[str]) -> tuple[Fraction, ...]:
    return tuple(Q(value) for value in values)


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> int:
    actual_hashes = {
        "input": sha256(INPUT),
        "protocol": sha256(PROTOCOL),
        "engine": sha256(ENGINE),
        "gnf_reference": sha256(GNF_REFERENCE),
        "normal_form": sha256(NORMAL_FORM),
    }
    if actual_hashes != EXPECTED_SHA256:
        raise AssertionError(
            f"SHA-256 gate failed: actual={actual_hashes}, "
            f"expected={EXPECTED_SHA256}"
        )

    engine = load_engine()
    document = json.loads(INPUT.read_text())
    derivatives = {
        order: parse_polynomial(document["derivatives"][f"F_{order}"])
        for order in range(4)
    }

    taylor = engine.taylor_jet(3)
    derivative = engine.derivative_jet(3)
    engine.validate_results((taylor, derivative), 3)
    if taylor.derivatives != derivative.derivatives:
        raise AssertionError("the two Gaussian-program routes disagree")
    if any(taylor.derivatives[order] != derivatives[order] for order in range(4)):
        raise AssertionError("stored derivative polynomials do not match the engine")

    a = parse_polynomial(
        document["factored_derivatives"]["A_coefficients"]
    )
    p = parse_polynomial(
        document["factored_derivatives"]["P_coefficients"]
    )
    expected_f1 = engine.rho_scale(
        engine.rho_multiply((Q(1), Q(1)), a), Q(81, 2)
    )
    expected_f3 = engine.rho_scale(
        engine.rho_multiply(
            engine.rho_power((Q(1), Q(1)), 2), p
        ),
        39_366,
    )
    if derivatives[1] != expected_f1 or derivatives[3] != expected_f3:
        raise AssertionError("stored factorization does not reproduce the jets")

    holdouts = (Q(-3, 4), Q(-1, 3), Q(0), Q(2, 5), Q(3, 4))
    activation = PolynomialActivation([0, 0, 0, 1])
    holdout_records: list[dict[str, object]] = []
    for rho in holdouts:
        independent = evaluate_contracted_directional_gnf(
            [[1, rho], [rho, 1]], [Q(1, 2), Q(1, 2)], activation
        )
        f1 = engine.rho_evaluate(derivatives[1], rho)
        f3 = engine.rho_evaluate(derivatives[3], rho)
        if independent.ntk != f1 or independent.correction != f3:
            raise AssertionError(f"independent GNF holdout failed at rho={rho}")
        holdout_records.append({
            "rho": fraction_string(rho),
            "F_1": fraction_string(f1),
            "F_3": fraction_string(f3),
            "exact_match": True,
        })

    rho_symbol = sp.symbols("rho")
    a_symbolic = sum(
        sp.Rational(value.numerator, value.denominator) * rho_symbol**degree
        for degree, value in enumerate(a)
    )
    p_symbolic = sum(
        sp.Rational(value.numerator, value.denominator) * rho_symbol**degree
        for degree, value in enumerate(p)
    )
    a_roots = sp.count_roots(sp.Poly(a_symbolic, rho_symbol), -1, 1)
    p_roots = sp.count_roots(sp.Poly(p_symbolic, rho_symbol), -1, 1)
    if a_roots != 0 or p_roots != 0:
        raise AssertionError("A or P has an unexpected root on [-1,1]")
    if min(a_symbolic.subs(rho_symbol, endpoint) for endpoint in (-1, 1)) <= 0:
        raise AssertionError("A endpoint sign gate failed")
    if min(p_symbolic.subs(rho_symbol, endpoint) for endpoint in (-1, 1)) <= 0:
        raise AssertionError("P endpoint sign gate failed")

    f1_at_zero = engine.rho_evaluate(derivatives[1], 0)
    f3_at_zero = engine.rho_evaluate(derivatives[3], 0)
    f1_at_one = engine.rho_evaluate(derivatives[1], 1)
    f3_at_one = engine.rho_evaluate(derivatives[3], 1)
    kpp_zero = f3_at_zero / f1_at_zero**2
    kpp_one = f3_at_one / f1_at_one**2

    cross_kernel = engine.rho_add(
        engine.rho_scale(derivatives[1], 2),
        engine.rho_constant(-305_775),
    )
    expected_cross = (
        Q(0),
        Q(54_675),
        Q(0),
        Q(91_368),
        Q(0),
        Q(78_732),
        Q(0),
        Q(64_152),
        Q(0),
        Q(16_848),
    )
    if cross_kernel != expected_cross:
        raise AssertionError("initial full-kernel reconstruction failed")

    payload = {
        "model": document["model"],
        "validation": "passed",
        "sha256": actual_hashes,
        "gaussian_program_routes_agree_exactly": True,
        "independent_contracted_gnf_holdouts": holdout_records,
        "factorization": {
            "F_1": "81*(rho+1)*A(rho)/2",
            "F_3": "39366*(rho+1)^2*P(rho)",
            "K_double_prime_0": "24*P(rho)/A(rho)^2",
        },
        "interval_certificate": {
            "A_real_roots_on_closed_interval": int(a_roots),
            "P_real_roots_on_closed_interval": int(p_roots),
            "A_minus_1": str(a_symbolic.subs(rho_symbol, -1)),
            "A_plus_1": str(a_symbolic.subs(rho_symbol, 1)),
            "P_minus_1": str(p_symbolic.subs(rho_symbol, -1)),
            "P_plus_1": str(p_symbolic.subs(rho_symbol, 1)),
            "conclusion": (
                "K_+(0;rho)>0 for -1<rho<=1 and "
                "K_+''(0;rho)>0 throughout the nondegenerate interval"
            ),
        },
        "representative_values": {
            "rho_0": {
                "K_0": fraction_string(f1_at_zero),
                "F_3": fraction_string(f3_at_zero),
                "K_double_prime_0": fraction_string(kpp_zero),
            },
            "rho_1": {
                "K_0": fraction_string(f1_at_one),
                "F_3": fraction_string(f3_at_one),
                "K_double_prime_0": fraction_string(kpp_one),
            },
        },
        "full_initial_kernel": {
            "Theta_11_equals_Theta_22": "305775",
            "Theta_12_equals_Theta_21": engine.rho_expression(cross_kernel),
            "plus_eigenvalue": "2*K_+(0;rho)",
        },
        "loss_mapping": {
            "loss": "L=((f_1-1)^2+(f_2-1)^2)/2=(1-g)^2",
            "symmetric_flow": "g_dot=2*eta*(1-g)*K_+(g;rho)",
            "loss_flow": "L_dot=-4*eta*K_+(g;rho)*L",
            "initial_loss_slope": "L_dot(0)=-4*eta*K_+(0;rho)",
            "initial_loss_curvature": "L_ddot(0)=16*eta^2*K_+(0;rho)^2",
            "initial_loss_third_derivative": (
                "L'''(0)=-16*eta^3*(4*K_+(0;rho)^3+F_+'''(0;rho))"
            ),
        },
        "claim_boundary": (
            "The scalar loss equation is exact for the exchange-symmetric "
            "width-first/formal trajectory, not for a generic finite-width "
            "realization or an asymmetric two-output state."
        ),
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
