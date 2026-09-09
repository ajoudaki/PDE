#!/usr/bin/env python3
"""Exact interval certificate for beta=1 and 0<=alpha<=1/100.

The jet polynomials below are supplied by the independent tensor-program
recurrence.  This file performs only the algebraically separate formal
inversion, Hankel determinant, and interval-sign certification.
"""

from __future__ import annotations

import json
from fractions import Fraction

from alpha_interval_tools import (
    build_interval_certificate,
    fraction_string,
    peval,
    poly,
    shifted_h2_from_jets,
)


Q = Fraction
EPSILON = Q(1, 100)

# Ascending alpha coefficients of F_alpha^(2r+1)(0), r=0,...,6.
ODD_JET_COEFFICIENTS = [
    [63, 48],
    [77760, 625536, 754560, 227328],
    [
        274547232,
        4596735744,
        21436337664,
        31088738304,
        17024090112,
        2980184064,
    ],
    [
        2141006515200,
        51717526548480,
        443633644707840,
        1617194490200064,
        2564438160015360,
        1911736087216128,
        647577990070272,
        77429527805952,
    ],
    [
        31149221916487680,
        926397280733921280,
        11228797008295759872,
        68120013107843407872,
        216157343459495804928,
        360293373996617170944,
        325383748411160788992,
        157873329654523232256,
        37777979806259871744,
        3369009878554116096,
    ],
    [
        759035131220036321280,
        25594965804374979379200,
        383019483677094369755136,
        3183862200286963804176384,
        15561308094860120107253760,
        45191839708552427406360576,
        77732833310661790408900608,
        80037321953103213886439424,
        49156411552814847636799488,
        17330750388205451118379008,
        3157236628947852268142592,
        221895065540516313563136,
    ],
    [
        28719223368439752070594560,
        1049927070983648807603404800,
        17931688202114583797612298240,
        182535682557908834998152560640,
        1185389301689487145264541073408,
        4995568087297667723007295488000,
        13644399097739494223476842037248,
        23988792318732344423548176039936,
        27175238485927648131807568723968,
        19766556153143784452713000992768,
        9044046194292861476093351165952,
        2471574150367421186553069699072,
        359712824603649166641664622592,
        20689648397930917159577321472,
    ],
]

OLD_AXIS_DETERMINANT = Q(
    -86245462994269879146938487857152,
    200150589172828762588730609071155193161975,
)


def build_certificate() -> dict[str, object]:
    jets = [poly(coefficients) for coefficients in ODD_JET_COEFFICIENTS]
    record = build_interval_certificate(jets, EPSILON)
    determinant = shifted_h2_from_jets(jets)
    primitive = tuple(int(value) for value in record["primitive_numerator_ascending"])

    if determinant.evaluate(0) != OLD_AXIS_DETERMINANT:
        raise AssertionError("alpha=0 determinant regression failed")
    if determinant.c != poly([63, 48]) or determinant.c_power != 33:
        raise AssertionError("determinant denominator regression failed")
    if record["positive_primitive_scale"] != "55296/2358125":
        raise AssertionError("primitive scale regression failed")
    if not (primitive[0] < 0 and primitive[1] < 0):
        raise AssertionError("constant/linear numerator signs changed")
    if not all(value > 0 for value in primitive[2:]):
        raise AssertionError("strict convexity coefficient gate failed")

    second_derivative = tuple(
        degree * (degree - 1) * primitive[degree]
        for degree in range(2, len(primitive))
    )
    if not all(value > 0 for value in second_derivative):
        raise AssertionError("P'' is not coefficientwise positive")

    # A compact integer endpoint check equivalent to P(1/100)<0.
    scaled_endpoint = sum(
        coefficient * 100 ** (len(primitive) - 1 - degree)
        for degree, coefficient in enumerate(primitive)
    )
    if scaled_endpoint >= 0:
        raise AssertionError("right endpoint is not negative")
    if peval(poly(primitive), EPSILON) != Q(
        scaled_endpoint, 100 ** (len(primitive) - 1)
    ):
        raise AssertionError("endpoint scaling identity failed")

    record.update(
        {
            "schema": "positive_alpha_shifted_H2_interval_v1",
            "beta": 1,
            "odd_feature_derivative_polynomials_ascending": {
                str(2 * index + 1): [str(value) for value in coefficients]
                for index, coefficients in enumerate(ODD_JET_COEFFICIENTS)
            },
            "even_feature_derivatives_through_12": "identically_zero",
            "determinant_formula": (
                "Delta(alpha)=55296*P(alpha)/"
                "(2358125*(63+48*alpha)^33)"
            ),
            "denominator_positive_lower_bound_on_interval": (
                "2358125*63^33"
            ),
            "Delta_at_zero": fraction_string(determinant.evaluate(0)),
            "strictly_positive_second_derivative_coefficients": True,
            "second_derivative_coefficient_count": len(second_derivative),
            "scaled_endpoint_identity": "100^36*P(1/100)",
            "scaled_endpoint_integer": str(scaled_endpoint),
            "decision": "Delta(alpha)<0 for every 0<=alpha<=1/100",
        }
    )
    return record


def main() -> None:
    print(json.dumps(build_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

