#!/usr/bin/env python3
"""Regression checks for the single-source depth-two identity closure."""

from __future__ import annotations

import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPECTRAL_DIR = HERE.parent / "depth2_all_order_search"
sys.path.insert(0, str(SPECTRAL_DIR))

from spectral_closure import initial_spectral_moments, spectral_fixed_point  # noqa: E402


class AutonomousMSEClosureTests(unittest.TestCase):
    @staticmethod
    def rho_x_density(lam: float) -> float:
        return math.sqrt(lam * (4.0 - lam)) / (2.0 * math.pi * (1.0 + 2.0 * lam))

    @staticmethod
    def rho_v_density(lam: float) -> float:
        return math.sqrt(lam * (4.0 - lam)) / (2.0 * math.pi)

    @staticmethod
    def nu_density(lam: float) -> float:
        return (
            (1.0 + lam)
            * math.sqrt(lam * (4.0 - lam))
            / (math.pi * (1.0 + 2.0 * lam))
        )

    def test_single_scalar_source_decomposes_two_channels(self) -> None:
        for lam in (0.125, 0.5, 1.0, 2.0, 3.5):
            alpha_squared = 1.0 / (2.0 * (1.0 + lam))
            beta_squared = (1.0 + 2.0 * lam) / (2.0 * (1.0 + lam))
            self.assertAlmostEqual(
                alpha_squared * self.nu_density(lam), self.rho_x_density(lam)
            )
            self.assertAlmostEqual(
                beta_squared * self.nu_density(lam), self.rho_v_density(lam)
            )
            self.assertAlmostEqual(alpha_squared + beta_squared, 1.0)
        self.assertEqual(Fraction(3, 4) * 1**2, Fraction(3, 4))
        self.assertEqual(Fraction(3, 4) * 0**2, Fraction(0))

    def test_initial_readouts(self) -> None:
        rho_x, rho_v = initial_spectral_moments(2)
        r0 = rho_x[0]
        f0 = Fraction(0)
        k0 = rho_v[0] + rho_x[1] + 2 * r0 * r0
        self.assertEqual((r0, f0, k0), (Fraction(1), Fraction(0), Fraction(3)))

    def test_formal_jet_crosscheck(self) -> None:
        r, _, _ = spectral_fixed_point(14)
        derivatives = [
            Fraction(math.factorial(order + 1), 2) * r[order + 1]
            for order in range(14)
        ]
        expected = [
            0, 3, 0, 48, 0, 1464, 0, 76800, 0, 6193152, 0,
            708341760, 0, 109038689280,
        ]
        self.assertEqual(derivatives, [Fraction(value) for value in expected])


if __name__ == "__main__":
    unittest.main()
