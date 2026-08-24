#!/usr/bin/env python3
"""Regression tests for the independent depth-two spectral closure."""

from __future__ import annotations

import json
import math
import unittest
from fractions import Fraction
from pathlib import Path

from spectral_closure import initial_spectral_moments, spectral_fixed_point


Q = Fraction
HERE = Path(__file__).resolve().parent


class SpectralClosureTests(unittest.TestCase):
    def test_initial_measures(self) -> None:
        rho_x, rho_v = initial_spectral_moments(7)
        self.assertEqual(rho_x, [Q(x) for x in (1, 0, 1, 2, 6, 18, 57, 186)])
        self.assertEqual(rho_v, [Q(x) for x in (1, 2, 5, 14, 42, 132, 429, 1430)])

    def test_independent_order13_prefix(self) -> None:
        r, _, _ = spectral_fixed_point(14)
        derivatives = [
            Q(math.factorial(order + 1), 2) * r[order + 1]
            for order in range(14)
        ]
        expected = [
            0, 3, 0, 48, 0, 1464, 0, 76800, 0, 6193152, 0,
            708341760, 0, 109038689280,
        ]
        self.assertEqual(derivatives, [Q(value) for value in expected])

    def test_production_artifacts(self) -> None:
        search = json.loads((HERE / "RESULTS.json").read_text())
        self.assertEqual(len(search["moments"]), 40)
        self.assertEqual(search["algebraic_ogf_candidates"], [])
        self.assertEqual(search["p_recursive_candidates"], [])
        closure = json.loads((HERE / "SPECTRAL_CLOSURE_RESULTS.json").read_text())
        self.assertTrue(
            closure["validation"]["derivatives_match_independent_gaussian_program_through_81"]
        )
        self.assertTrue(closure["validation"]["moments_mu_0_through_39_match"])
        hankel = json.loads((HERE / "HANKEL40_RESULTS.json").read_text())
        self.assertTrue(hankel["ordinary"]["all_positive_definite"])
        self.assertTrue(hankel["shifted"]["all_positive_definite"])


if __name__ == "__main__":
    unittest.main()

