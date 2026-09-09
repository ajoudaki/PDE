"""Regressions for the exact positive-alpha interval postprocessor."""

from fractions import Fraction

from alpha_interval_tools import (
    bernstein_coefficients_on_interval,
    certify_negative_by_bernstein,
    elementary_negative_interval,
    output_kernel_moments_from_jets,
    peval,
    poly,
    primitive_integer_polynomial,
    shifted_h2_from_jets,
)


AXIS_ODD_DERIVATIVES = [
    63,
    77760,
    274547232,
    2141006515200,
    31149221916487680,
    759035131220036321280,
    28719223368439752070594560,
]


def test_axis_moments_and_negative_determinant() -> None:
    jets = [poly([value]) for value in AXIS_ODD_DERIVATIVES]
    moments = output_kernel_moments_from_jets(jets)
    assert [moment.evaluate(0) for moment in moments] == [
        Fraction(480, 49),
        Fraction(43756, 151263),
        Fraction(7214528, 200120949),
        Fraction(12545175968, 2402451992745),
        Fraction(171752915595136, 200241971143303005),
        Fraction(2199776554157960896, 14570607030242443158825),
    ]
    determinant = shifted_h2_from_jets(jets)
    assert determinant.evaluate(0) == Fraction(
        -86245462994269879146938487857152,
        200150589172828762588730609071155193161975,
    )


def test_nonconstant_baseline_has_structural_power_33() -> None:
    # This deliberately artificial family checks denominator bookkeeping;
    # the physical family will replace every higher constant by a polynomial.
    jets = [poly([AXIS_ODD_DERIVATIVES[0], 48])] + [
        poly([value]) for value in AXIS_ODD_DERIVATIVES[1:]
    ]
    determinant = shifted_h2_from_jets(jets)
    assert determinant.c == poly([63, 48])
    assert determinant.c_power == 33
    assert determinant.evaluate(0) == Fraction(
        -86245462994269879146938487857152,
        200150589172828762588730609071155193161975,
    )


def test_elementary_and_bernstein_certificates_are_exact() -> None:
    # P(x)=-3+2x+100x^2 is negative on the certified interval.
    coefficients = (-3, 2, 100)
    automatic = elementary_negative_interval(coefficients)
    assert automatic == Fraction(3, 204)
    assert peval(poly(coefficients), automatic) < 0

    epsilon = Fraction(1, 10)
    bernstein = certify_negative_by_bernstein(coefficients, epsilon)
    assert bernstein == bernstein_coefficients_on_interval(coefficients, epsilon)
    assert all(value < 0 for value in bernstein)


def test_primitive_integer_polynomial_clears_rational_content() -> None:
    assert primitive_integer_polynomial(
        poly([Fraction(-2, 3), Fraction(4, 9), Fraction(2, 3)])
    ) == (-3, 2, 3)

