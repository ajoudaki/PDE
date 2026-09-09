#!/usr/bin/env python3

import json
from pathlib import Path
import tempfile
import unittest

import sympy as sp

import postprocess


HERE = Path(__file__).resolve().parent


class PostprocessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plus = postprocess.load_jets(HERE / "frozen/plus_order7_raw.json")
        cls.minus_raw = postprocess.load_jets(
            HERE / "frozen/minus_order7_raw.json"
        )
        cls.minus = postprocess.divide_minus_endpoint(cls.minus_raw)

    def test_plus_canonical_endpoint_all_orders(self):
        expected = (111, 1685184, 77400633120, 7315868433079296)
        self.assertEqual(
            tuple(self.plus[k].eval(1) for k in (1, 3, 5, 7)), expected
        )

    def test_minus_forced_factors(self):
        for order in (1, 3, 5, 7):
            reconstructed = self.minus[order].as_expr() * (
                1 - postprocess.t
            ) ** ((order + 1) // 2)
            self.assertEqual(
                sp.expand(reconstructed - self.minus_raw[order].as_expr()), 0
            )

    def test_all_moments_and_hankels_positive(self):
        for jets in (self.plus, self.minus):
            for expression in postprocess.certificates(jets).values():
                certificate = postprocess.sign_certificate(expression)
                self.assertTrue(
                    certificate["strictly_positive_on_closed_unit_interval"]
                )

    def test_universal_formulas_at_single_input(self):
        values = postprocess.certificates(self.plus)
        # Accepted canonical moments through mu2.
        expected = (
            sp.Rational(280864, 4107),
            sp.Rational(38443196932, 5616860517),
            sp.Rational(37578479127292096, 12802987609542045),
        )
        self.assertEqual(
            tuple(sp.cancel(values[f"mu{i}"].subs(postprocess.t, 1))
                  for i in range(3)),
            expected,
        )


if __name__ == "__main__":
    unittest.main()

