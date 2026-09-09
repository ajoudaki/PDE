"""Regression tests for the exact two-input raw-cubic plus-channel jet."""

from __future__ import annotations

import importlib
import sys
import unittest
from fractions import Fraction
from pathlib import Path


Q = Fraction
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO))

engine = importlib.import_module("two_input_cubic_plus_jet")
gnf_module = importlib.import_module(
    "studies.mean_field_peeling.generic_first_stieltjes.b2."
    "contracted_gnf_polynomial_reference"
)
normal_form_module = importlib.import_module(
    "studies.mean_field_peeling.generic_first_stieltjes.compiler.normal_form"
)


EXPECTED_F1 = (
    Q(305_775, 2),
    Q(54_675, 2),
    Q(0),
    Q(45_684),
    Q(0),
    Q(39_366),
    Q(0),
    Q(32_076),
    Q(0),
    Q(8_424),
)
EXPECTED_F3 = (
    Q(19_310_071_119_750),
    Q(6_082_858_923_750),
    Q(4_950_930_928_050),
    Q(16_553_736_233_190),
    Q(14_601_768_753_564),
    Q(21_566_517_052_140),
    Q(10_179_565_523_964),
    Q(24_773_966_615_700),
    Q(10_747_229_306_328),
    Q(8_081_925_224_220),
    Q(9_565_735_816_224),
    Q(0),
    Q(5_163_082_687_008),
    Q(0),
    Q(1_993_411_099_008),
    Q(0),
    Q(502_141_358_592),
    Q(0),
    Q(45_067_456_512),
)


class TwoInputCubicPlusTests(unittest.TestCase):
    """Exercise both coefficient conventions and the independent holdout."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.taylor = engine.taylor_jet(3)
        cls.derivative = engine.derivative_jet(3)

    def test_two_routes_and_precommitted_gates(self) -> None:
        engine.validate_results((self.taylor, self.derivative), 3)
        self.assertEqual(self.taylor.derivatives, self.derivative.derivatives)
        self.assertEqual(self.taylor.derivatives[0], engine.RHO_ZERO)
        self.assertEqual(self.taylor.derivatives[1], EXPECTED_F1)
        self.assertEqual(self.taylor.derivatives[2], engine.RHO_ZERO)
        self.assertEqual(self.taylor.derivatives[3], EXPECTED_F3)

    def test_initial_full_kernel_reconstruction(self) -> None:
        cross = engine.rho_add(
            engine.rho_scale(EXPECTED_F1, 2),
            engine.rho_constant(-305_775),
        )
        self.assertEqual(
            cross,
            (
                Q(0), Q(54_675), Q(0), Q(91_368), Q(0),
                Q(78_732), Q(0), Q(64_152), Q(0), Q(16_848),
            ),
        )
        for rho in (Q(-3, 4), Q(0), Q(2, 5), Q(1)):
            diagonal = Q(305_775)
            plus_projection = (diagonal + engine.rho_evaluate(cross, rho)) / 2
            self.assertEqual(plus_projection, engine.rho_evaluate(EXPECTED_F1, rho))

    def test_representative_kernel_curvatures(self) -> None:
        for rho, expected in (
            (Q(0), Q(94_181_112, 114_005)),
            (Q(1), Q(187_920_144, 114_005)),
        ):
            f1 = engine.rho_evaluate(EXPECTED_F1, rho)
            f3 = engine.rho_evaluate(EXPECTED_F3, rho)
            self.assertEqual(f3 / f1**2, expected)

    def test_independent_contracted_gnf_holdouts(self) -> None:
        activation = normal_form_module.PolynomialActivation([0, 0, 0, 1])
        evaluate = gnf_module.evaluate_contracted_directional_gnf
        for rho in (Q(-3, 4), Q(-1, 3), Q(0), Q(2, 5), Q(3, 4)):
            with self.subTest(rho=rho):
                independent = evaluate(
                    [[1, rho], [rho, 1]],
                    [Q(1, 2), Q(1, 2)],
                    activation,
                )
                self.assertEqual(
                    independent.ntk,
                    engine.rho_evaluate(EXPECTED_F1, rho),
                )
                self.assertEqual(
                    independent.correction,
                    engine.rho_evaluate(EXPECTED_F3, rho),
                )


if __name__ == "__main__":
    unittest.main()
