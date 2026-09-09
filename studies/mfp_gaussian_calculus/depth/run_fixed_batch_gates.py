"""Run the independent joint fixed-depth/fixed-batch exact gates."""

from __future__ import annotations

from .test_fixed_batch_polynomial_reference import (
    test_b1_reduces_to_independently_contracted_depth_recurrence,
    test_deep_linear_closed_form_at_arbitrary_batch,
    test_h2_reduces_blockwise_to_accepted_fixed_batch_gnf,
    test_h3_b2_nonlinear_exact_fixture_and_singular_b1_collapse,
)


def main() -> None:
    checks = (
        test_h2_reduces_blockwise_to_accepted_fixed_batch_gnf,
        test_b1_reduces_to_independently_contracted_depth_recurrence,
        test_h3_b2_nonlinear_exact_fixture_and_singular_b1_collapse,
        test_deep_linear_closed_form_at_arbitrary_batch,
    )
    for check in checks:
        check()
    print(f"PASS: {len(checks)} joint fixed-depth/fixed-batch GNF gates")


if __name__ == "__main__":
    main()

