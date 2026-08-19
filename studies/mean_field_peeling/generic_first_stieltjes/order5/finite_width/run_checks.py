"""Dependency-free entry point for all exact finite-width order-five gates."""

from . import test_order5


def run() -> None:
    checks = (
        test_order5.test_two_independent_routes_seedwise,
        test_order5.test_constant_and_affine_exact_width_one_controls,
        test_order5.test_linear_exact_controls,
        test_order5.test_quadratic_width_one_exact_wick_control,
        test_order5.test_generic_quadratic_matches_accepted_finite_width_compiler,
        test_order5.test_quadratic_exact_frozen_large_width_endpoint,
        test_order5.test_preregistered_sine_exact_pre_gate_only,
    )
    for check in checks:
        check()
        print(f"PASS {check.__name__}")


if __name__ == "__main__":
    run()
