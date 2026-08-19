#!/usr/bin/env python3
"""Regression tests for the depth-3 order-nine Stieltjes audit."""

from __future__ import annotations

import unittest
from fractions import Fraction

from depth3_stieltjes_audit import audit_hankels, moments_from_triangular_identity


ODD_DERIVATIVES = {
    1: 14_175,
    3: 139_445_032_896,
    5: 4_298_284_752_832_899_360,
    7: 272_967_464_957_028_310_013_451_264,
    9: 29_466_555_372_596_241_677_766_026_853_605_376,
}

EXPECTED_MOMENTS = (
    Fraction(95_641_312, 275_625),
    Fraction(3_963_629_647_049_188, 3_230_587_705_078_125),
    Fraction(
        12_164_741_271_894_434_633_792,
        601_040_746_943_206_787_109_375,
    ),
    Fraction(
        4_206_861_574_840_394_358_968_837_051_264,
        9_862_678_589_590_839_304_447_174_072_265_625,
    ),
)


class Depth3StieltjesAuditTests(unittest.TestCase):
    def test_triangular_moment_route(self) -> None:
        baseline, moments = moments_from_triangular_identity(ODD_DERIVATIVES)
        self.assertEqual(baseline, 14_175)
        self.assertEqual(moments, EXPECTED_MOMENTS)

    def test_all_accessible_hankels_are_positive_definite(self) -> None:
        audit = audit_hankels(EXPECTED_MOMENTS)
        self.assertEqual(audit["accessible_matrix_count"], 4)
        self.assertTrue(audit["all_accessible_matrices_positive_semidefinite"])
        self.assertTrue(audit["all_accessible_matrices_positive_definite"])

    def test_nontrivial_determinants(self) -> None:
        ordinary = EXPECTED_MOMENTS[0] * EXPECTED_MOMENTS[2] - EXPECTED_MOMENTS[1] ** 2
        shifted = EXPECTED_MOMENTS[1] * EXPECTED_MOMENTS[3] - EXPECTED_MOMENTS[2] ** 2
        self.assertGreater(ordinary, 0)
        self.assertGreater(shifted, 0)


if __name__ == "__main__":
    unittest.main()
