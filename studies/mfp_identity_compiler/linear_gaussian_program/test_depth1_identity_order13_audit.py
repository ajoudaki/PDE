from __future__ import annotations

import unittest
from fractions import Fraction

from .depth1_identity_order13_audit import (
    build_audit,
    catalan_scaled,
    depth1_derivatives,
)


class Depth1IdentityOrder13AuditTests(unittest.TestCase):
    def test_derivative_jet(self) -> None:
        self.assertEqual(
            depth1_derivatives(13),
            [0, 2, 0, 8, 0, 32, 0, 128, 0, 512, 0, 2048, 0, 8192],
        )

    def test_moments_and_minors(self) -> None:
        result = build_audit()
        moments = tuple(
            Fraction(record["exact"])
            for record in result["moments"].values()
        )
        self.assertEqual(
            moments,
            (
                Fraction(1),
                Fraction(1, 4),
                Fraction(1, 8),
                Fraction(5, 64),
                Fraction(7, 128),
                Fraction(21, 512),
            ),
        )
        self.assertEqual(result["unique_minor_counts"], {1: 6, 2: 13, 3: 4})
        self.assertTrue(result["all_23_accessible_minors_positive"])
        self.assertEqual(
            Fraction(
                result["new_shifted_H_2_plus"]["principal_minors"]["0,1,2"]["exact"]
            ),
            Fraction(1, 262144),
        )

    def test_beta_moment_recurrence(self) -> None:
        # The density's beta moments obey m_(r+1)/m_r=(2r+1)/(2r+4).
        moment = Fraction(1)
        for index in range(20):
            self.assertEqual(moment, catalan_scaled(index))
            moment *= Fraction(2 * index + 1, 2 * index + 4)


if __name__ == "__main__":
    unittest.main()

