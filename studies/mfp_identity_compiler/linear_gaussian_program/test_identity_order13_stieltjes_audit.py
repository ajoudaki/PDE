from __future__ import annotations

import unittest
from fractions import Fraction

from .identity_order13_stieltjes_audit import (
    audit_depth_order13,
    load_reversion_route,
)


class IdentityOrder13StieltjesAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.route = staticmethod(load_reversion_route())

    def test_depth_two_new_endpoint(self) -> None:
        derivatives = [
            0, 3, 0, 48, 0, 1464, 0, 76800, 0, 6193152, 0, 708341760,
            0, 109038689280,
        ]
        result = audit_depth_order13(2, derivatives, self.route)
        self.assertEqual(
            Fraction(result["new_moment_mu_5"]["exact"]),
            Fraction(63196828537, 82864937925),
        )
        self.assertEqual(
            Fraction(
                result["new_shifted_H_2_plus"]["principal_minors"]["0,1,2"]["exact"]
            ),
            Fraction(4662092676191348, 2157853448314196325),
        )
        self.assertEqual(result["unique_minor_counts"], {1: 6, 2: 13, 3: 4})
        self.assertTrue(result["all_23_accessible_minors_positive"])

    def test_depth_three_new_endpoint(self) -> None:
        derivatives = [
            0, 4, 0, 160, 0, 13888, 0, 2222592, 0, 571082752, 0,
            214935699456, 0, 111466749771776,
        ]
        result = audit_depth_order13(3, derivatives, self.route)
        self.assertEqual(
            Fraction(result["new_moment_mu_5"]["exact"]),
            Fraction(314669435827, 54499737600),
        )
        self.assertEqual(
            Fraction(
                result["new_shifted_H_2_plus"]["principal_minors"]["0,1,2"]["exact"]
            ),
            Fraction(114573182642874004393, 708802833725521920000),
        )
        self.assertEqual(result["unique_minor_counts"], {1: 6, 2: 13, 3: 4})
        self.assertTrue(result["all_23_accessible_minors_positive"])


if __name__ == "__main__":
    unittest.main()

