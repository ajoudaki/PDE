from fractions import Fraction

import pytest

from proxy.exact_series import companion_moments, output_kernel_moments
from proxy.inventory import evaluate_family


CANONICAL_MOMENTS = (
    Fraction(280864, 4107),
    Fraction(38443196932, 5616860517),
    Fraction(37578479127292096, 12802987609542045),
    Fraction(21749547365571716077696, 13618704359108797313085),
    Fraction(
        2463577914969508668234788122624,
        2514423905282563683042386470725,
    ),
)


def test_canonical_regression_from_accepted_certificate():
    family = evaluate_family("canonical")
    assert family.baseline == 111
    assert family.moments == CANONICAL_MOMENTS


def test_variance_endpoints_reproduce_boundary_and_canonical():
    boundary = evaluate_family("variance_homotopy", alpha=0)
    canonical = evaluate_family("variance_homotopy", alpha=1)
    assert boundary.baseline == 36
    assert boundary.moments == (
        Fraction(6), Fraction(7, 18), Fraction(55, 972),
        Fraction(245, 23328), Fraction(19, 8640),
    )
    assert canonical.baseline == 111
    assert canonical.moments == CANONICAL_MOMENTS


def test_relative_metric_canonical_output_and_hidden_regressions():
    output = evaluate_family("relative_metric_output", **{"lambda": 1})
    hidden = evaluate_family("relative_metric_q2", **{"lambda": 1})
    assert output.baseline == 111
    assert output.moments == CANONICAL_MOMENTS[:4]
    assert hidden.baseline == 3
    assert hidden.moments == (
        Fraction(2062, 4107),
        Fraction(678331568, 5616860517),
        Fraction(2090752728035608, 38408962828626135),
        Fraction(137586915791251406192, 4539568119702932437695),
    )


def test_other_canonical_intersections_match():
    assert evaluate_family("two_input_equal", t=1).moments == CANONICAL_MOMENTS[:3]
    assert evaluate_family("centered_activation", c=0).moments == CANONICAL_MOMENTS[:3]
    assert evaluate_family(
        "independent_block_metric", alpha=1, beta=1
    ).moments == CANONICAL_MOMENTS[:4]


def test_opposite_singular_endpoint_is_not_relabelled_physical():
    with pytest.raises(ValueError, match="collapses"):
        evaluate_family("two_input_opposite", t=1)


def test_generic_transform_formulas_at_order_five():
    # F(s)=a*s+b*s^3+c*s^5, where b,c are ordinary Taylor coefficients.
    a, b, c = Fraction(7), Fraction(11), Fraction(13)
    baseline, moments = output_kernel_moments({1: a, 3: 6 * b, 5: 120 * c})
    assert baseline == a
    assert moments[0] == 3 * b / a**2
    assert moments[1] == (6 * b**2 - 5 * a * c) / a**5


def test_companion_transform_toy_example():
    # F(s)=2s and Q(s)=3+5s^2-7s^4.  Substitution s=y/2 is immediate.
    baseline, moments = companion_moments(
        {1: 2, 3: 0, 5: 0},
        {0: 3, 2: 10, 4: -168},
    )
    assert baseline == 3
    assert moments == (Fraction(5, 4), Fraction(7, 16))
