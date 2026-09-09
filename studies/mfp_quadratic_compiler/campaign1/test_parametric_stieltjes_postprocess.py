#!/usr/bin/env python3
"""Exact unit and regression gates for Campaign 1 postprocessing."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

import sympy as sp


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import parametric_stieltjes_postprocess as pp


def campaign1_order6_fixture() -> dict:
    """The checked low-order runner output, stripped to the required jets."""
    return {
        "jets": {
            "f": [
                [0],
                [27, 84],
                [0],
                [0, 123120, 699408, 862656],
                [0],
                [0, 0, 1730898720, 14214258432, 35456350464,
                 25999125504],
                [0],
            ],
            "q2": [
                [3],
                [0],
                [0, 2916, 9456],
                [0],
                [0, 0, 20751552, 123392448, 167175936],
                [0],
                [0, 0, 0, 390147331968, 3343277514240,
                 8933475492864, 7317629343744],
            ],
        }
    }


class FormalSeriesTests(unittest.TestCase):
    def test_reverse_r_a_squared(self) -> None:
        # x = r(2+3r)^2 = 4r+12r^2+9r^3.
        reverse = pp.reverse_r_times_a_squared(
            [sp.Integer(2), sp.Integer(3)], 4
        )
        forward = [sp.Integer(0), sp.Integer(4), sp.Integer(12), sp.Integer(9)]
        composed = pp._series_compose(forward, reverse, 4)
        self.assertEqual(composed, [0, 1, 0, 0, 0])

    def test_output_regression_through_order_eleven(self) -> None:
        accepted = [
            111,
            1_685_184,
            77_400_633_120,
            7_315_868_433_079_296,
            1_181_161_141_825_400_561_664,
            291_982_832_387_585_872_335_470_592,
        ]
        f = [[0] for _ in range(12)]
        for index, derivative in enumerate(accepted):
            f[2 * index + 1] = [derivative]
        q2 = [[0] for _ in range(12)]
        q2[0] = [3]
        result = pp.compute({"jets": {"f": f, "q2": q2}})
        self.assertEqual(
            result["output_kernel"]["moments_mu"],
            [
                "280864/4107",
                "38443196932/5616860517",
                "37578479127292096/12802987609542045",
                "21749547365571716077696/13618704359108797313085",
                (
                    "2463577914969508668234788122624/"
                    "2514423905282563683042386470725"
                ),
            ],
        )

    def test_checked_cpp_schema_is_consumed_directly(self) -> None:
        compact = campaign1_order6_fixture()["jets"]
        production = {
            "observables": {
                root: {
                    "jets": [
                        {"order": order, "lambda_coefficients": coefficients}
                        for order, coefficients in enumerate(compact[root])
                    ]
                }
                for root in ("f", "q2")
            }
        }
        self.assertEqual(
            pp.compute(production)["second_hidden_norm"]["moments_nu"],
            pp.compute({"jets": compact})["second_hidden_norm"]["moments_nu"],
        )


class ExactRaySignTests(unittest.TestCase):
    def setUp(self) -> None:
        self.parameter = sp.Symbol("lambda", real=True, nonnegative=True)

    def test_coefficientwise_positive_certificate(self) -> None:
        result = pp.certify_rational_nonnegative(
            self.parameter * (1 + 2 * self.parameter)
            / (3 + self.parameter)**2,
            self.parameter,
        )
        self.assertEqual(result["status"], "nonnegative")
        self.assertEqual(
            result["numerator_sign"]["method"],
            "coefficientwise_nonnegative",
        )

    def test_root_isolation_finds_exact_negative_witness(self) -> None:
        result = pp.certify_rational_nonnegative(
            (self.parameter - 1) * (self.parameter - 2),
            self.parameter,
        )
        self.assertEqual(result["status"], "falsified")
        self.assertIn(
            "negative",
            result["numerator_sign"]["rational_witnesses"],
        )

    def test_even_root_is_certified_nonnegative(self) -> None:
        result = pp.certify_rational_nonnegative(
            (self.parameter - 1)**2,
            self.parameter,
        )
        self.assertEqual(result["status"], "nonnegative")


class CampaignOnePilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = pp.compute(campaign1_order6_fixture())

    def test_forced_scaling_is_exact(self) -> None:
        self.assertTrue(
            self.result["output_kernel"]["forced_scaling"]
            ["exact_expected_valuation"]
        )
        self.assertTrue(
            self.result["second_hidden_norm"]["forced_scaling"]
            ["exact_expected_valuation"]
        )
        self.assertEqual(
            self.result["second_hidden_norm"]["forced_scaling"]
            ["valuations_at_zero"],
            [1, 2, 3],
        )

    def test_hidden_moments_are_exact(self) -> None:
        self.assertEqual(
            self.result["second_hidden_norm"]["moments_nu"][0],
            "2*lambda*(788*lambda + 243)/(3*(28*lambda + 9)**2)",
        )
        self.assertEqual(
            self.result["second_hidden_norm"]["moments_nu"][1],
            (
                "8*lambda**2*(32267920*lambda**3 + 37565472*lambda**2 + "
                "13437603*lambda + 1520451)/(81*(28*lambda + 9)**5)"
            ),
        )

    def test_first_hidden_hankel_family_is_strict_after_normalization(self) -> None:
        certificates = self.result["second_hidden_norm"][
            "normalized_sign_certificates"
        ]["ordinary"]
        self.assertEqual(len(certificates), 2)
        self.assertTrue(all(
            certificate["status"] == "strictly_positive"
            for certificate in certificates
        ))
        determinant = self.result["second_hidden_norm"][
            "normalized_hankel_determinants"
        ]["ordinary"][1]
        numerator = determinant.split("/", 1)[0]
        # The proof is especially transparent: every numerator coefficient is
        # strictly positive on the whole nonnegative parameter ray.
        parameter = sp.Symbol("lam")
        polynomial = sp.Poly(
            sp.sympify(numerator.replace("lambda", "lam")),
            parameter,
        )
        self.assertTrue(all(coefficient > 0 for coefficient in polynomial.all_coeffs()))


if __name__ == "__main__":
    unittest.main()
