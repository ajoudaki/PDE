#!/usr/bin/env python3
"""Low-order exact gates for the Campaign 1 reference compiler."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import parametric_multiroot_reference as pm
import independent_checks as independent
import exact_graph_wick as eg


class PolynomialTests(unittest.TestCase):
    def test_dense_polynomial_operations(self) -> None:
        self.assertEqual(pm.poly_add((1, 2), (3, 0, 4)), (4, 2, 4))
        self.assertEqual(pm.poly_scale_shift((1, 2), 3, 1), (0, 3, 6))
        self.assertEqual(pm.evaluate_polynomial((1, 2, 3), 1), 6)


class ExactCompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = pm.run(5, verify_parent_rewrites=True)

    def poly(self, root: str, order: int) -> tuple[int, ...]:
        return tuple(self.result["jets"][root][order])

    def test_initial_values(self) -> None:
        self.assertEqual(self.poly("f", 0), (0,))
        self.assertEqual(self.poly("q1", 0), (1,))
        self.assertEqual(self.poly("q2", 0), (3,))

    def test_lambda_one_matches_accepted_output_jet(self) -> None:
        accepted = (0, 111, 0, 1_685_184, 0, 77_400_633_120)
        obtained = tuple(
            pm.evaluate_polynomial(self.poly("f", order), 1)
            for order in range(6)
        )
        self.assertEqual(obtained, accepted)

    def test_parity_holds_coefficientwise(self) -> None:
        for order in (0, 2, 4):
            self.assertEqual(self.poly("f", order), (0,))
        for order in (1, 3, 5):
            self.assertEqual(self.poly("q1", order), (0,))
            self.assertEqual(self.poly("q2", order), (0,))

    def test_first_norm_euler_identity(self) -> None:
        # For D_lambda = D_a + lambda(D_u+D_W),
        # D_lambda^k Q1 = 8 lambda D_lambda^(k-1) f.
        for order in (2, 4):
            expected = pm.poly_scale_shift(self.poly("f", order - 1), 8, 1)
            self.assertEqual(self.poly("q1", order), expected)

    def test_connected_component_cache_is_actually_shared(self) -> None:
        # Full forests remain root-distinct at these orders, but their exact
        # connected subproblems already overlap.
        census = self.result["component_cache_census"][2]
        self.assertGreater(census["shared_by_at_least_two_roots"], 0)
        self.assertGreater(census["duplicate_evaluations_avoided"], 0)

    def test_default_metric_line_is_not_variance_boundary(self) -> None:
        # At lambda=0 only the readout moves.  The feature curve is exactly
        # linear: D f = E[z^4] = 27 and D^3 f=0.  The normalized
        # middle-weight-variance boundary is 36*s*exp(72*s^2), whose third
        # derivative is 15552.  No nonsingular linear output/time rescaling
        # can identify a linear curve with that nonlinear boundary.
        self.assertEqual(pm.evaluate_polynomial(self.poly("f", 1), 0), 27)
        self.assertEqual(pm.evaluate_polynomial(self.poly("f", 3), 0), 0)

    def test_new_roots_against_independent_direct_wick_pairing(self) -> None:
        polynomial = pm.initial_observables()
        metric = {"a": 0, "u": 1, "w": 1}
        for _order in range(3):
            for root in pm.ROOTS:
                scalar = pm.project_root_at_integer(polynomial, root, 1)
                self.assertEqual(
                    eg.expected_large_n(scalar),
                    independent.direct_large_n(scalar),
                )
            polynomial = pm.differentiate(polynomial, metric)


if __name__ == "__main__":
    unittest.main()
