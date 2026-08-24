from __future__ import annotations

import unittest
from fractions import Fraction

from .identity_stieltjes_audit import audit_depth, load_reversion_route


class IdentityStieltjesAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.route = staticmethod(load_reversion_route())

    def test_depth_two(self) -> None:
        derivatives = [
            0, 3, 0, 48, 0, 1464, 0, 76800, 0, 6193152, 0, 708341760
        ]
        result = audit_depth(2, derivatives, self.route)
        moments = tuple(
            Fraction(record["exact"])
            for record in result["moments"].values()
        )
        self.assertEqual(
            moments,
            (
                Fraction(8, 3),
                Fraction(67, 81),
                Fraction(6832, 10935),
                Fraction(414716, 688905),
                Fraction(182387864, 279006525),
            ),
        )
        self.assertTrue(
            result["hankel_audit"]["all_accessible_matrices_positive_definite"]
        )
        self.assertTrue(result["all_accessible_total_positivity_minors_positive"])

    def test_depth_three(self) -> None:
        derivatives = [
            0, 4, 0, 160, 0, 13888, 0, 2222592, 0, 571082752, 0,
            214935699456,
        ]
        result = audit_depth(3, derivatives, self.route)
        moments = tuple(
            Fraction(record["exact"])
            for record in result["moments"].values()
        )
        self.assertEqual(
            moments,
            (
                Fraction(5),
                Fraction(61, 32),
                Fraction(11131, 5760),
                Fraction(3235483, 1290240),
                Fraction(852431627, 232243200),
            ),
        )
        self.assertTrue(
            result["hankel_audit"]["all_accessible_matrices_positive_definite"]
        )
        self.assertTrue(result["all_accessible_total_positivity_minors_positive"])


if __name__ == "__main__":
    unittest.main()
