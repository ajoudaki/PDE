#!/usr/bin/env python3
"""Regression tests for the shallow normalized Hermite-2 certificate."""

from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from centered_h2_exact import (
    gaussian_expectation,
    lie_derivative,
    lie_jet,
    taylor_jet,
)


Q = Fraction
HERE = Path(__file__).resolve().parent


class CenteredHermite2Tests(unittest.TestCase):
    def test_two_exact_jet_routes(self) -> None:
        lie, _ = lie_jet(13)
        taylor, _ = taylor_jet(13)
        expected = [
            0, 3, 0, 192, 0, 38592, 0, 16882272, 0, 13710887424,
            0, 18618267830400, 0, 39219558574625280,
        ]
        self.assertEqual(lie, taylor)
        self.assertEqual(lie, [Q(value) for value in expected])

    def test_polynomial_invariant(self) -> None:
        # The polynomial part b^2-v has derivative -2b.  Since
        # d(log v)/dt=v'/v=2b, the full invariant has zero derivative.
        polynomial_part = {(2, 0): Q(1), (0, 1): Q(-1)}
        self.assertEqual(lie_derivative(polynomial_part), {(1, 0): Q(-2)})
        self.assertEqual(gaussian_expectation({(0, 0): Q(1)}), Q(1))

    def test_exact_violation_artifact(self) -> None:
        result = json.loads((HERE / "RESULTS.json").read_text())
        moments = [record["exact"] for record in result["moments_mu_0_through_5"]]
        self.assertEqual(
            moments,
            [
                "32/3", "440/81", "160738/10935", "30517412/688905",
                "85823505179/558013050", "13556868117611/23675696550",
            ],
        )
        audit = result["all_23_accessible_hankel_minors"]
        self.assertFalse(audit["all_nonnegative"])
        self.assertEqual(len(audit["negative_labels"]), 1)
        shifted = result["hankel_audit"]["shifted"]["H_2_plus"]
        self.assertEqual(
            shifted["leading_principal_determinants"][-1]["exact"],
            "-515758203187135106171912/485517025870694173125",
        )


if __name__ == "__main__":
    unittest.main()

