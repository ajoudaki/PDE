#!/usr/bin/env python3
"""Regression tests for the raw-cubic four-moment Stieltjes audit."""

from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from depth2_cubic_stieltjes_audit import (
    audit_hankels,
    load_series_reversion_route,
    moments_from_triangular_identity,
)


Q = Fraction
HERE = Path(__file__).resolve().parent
EXPECTED_MOMENTS = (
    Q(93_960_072, 114_005),
    Q(5_787_193_487_251, 147_192_610_783_125),
    Q(
        8_262_390_512_438_071_457_518,
        25_655_582_915_973_781_969_921_875,
    ),
    Q(
        2_636_622_646_388_500_249_440_493_088_029,
        5_564_847_635_936_495_462_248_842_835_546_875_000,
    ),
)
EXPECTED_ORDINARY_DETERMINANT = Q(
    85_757_048_922_094_359_666_566_525_129,
    324_984_970_037_287_890_386_771_484_375,
)
EXPECTED_SHIFTED_DETERMINANT = -Q(
    3_136_318_387_543_181_669_964_663_532_850_762_952_758_515_589,
    36_859_700_346_470_723_980_544_924_489_290_665_938_162_841_796_875_000,
)


class Depth2CubicStieltjesAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        document = json.loads((HERE / "results_order9.json").read_text())
        odd = {
            order: int(document["derivatives"][order])
            for order in range(1, 10, 2)
        }
        cls.baseline_a, cls.moments_a = load_series_reversion_route()(odd)
        cls.baseline_b, cls.moments_b = moments_from_triangular_identity(odd)
        cls.hankels = audit_hankels(cls.moments_a)

    def test_two_exact_moment_routes_agree(self) -> None:
        self.assertEqual(self.baseline_a, self.baseline_b)
        self.assertEqual(self.moments_a, self.moments_b)

    def test_exact_moments(self) -> None:
        self.assertEqual(self.baseline_a, 305_775)
        self.assertEqual(self.moments_a, EXPECTED_MOMENTS)

    def test_all_four_moments_are_positive(self) -> None:
        self.assertTrue(all(moment > 0 for moment in self.moments_a))

    def test_ordinary_hankel_is_positive_definite(self) -> None:
        record = self.hankels["ordinary"]["H_1"]
        self.assertTrue(record["positive_definite"])
        self.assertEqual(
            self.moments_a[0] * self.moments_a[2]
            - self.moments_a[1] ** 2,
            EXPECTED_ORDINARY_DETERMINANT,
        )

    def test_shifted_hankel_has_exact_negative_determinant(self) -> None:
        record = self.hankels["shifted"]["H_1_plus"]
        self.assertFalse(record["positive_semidefinite"])
        self.assertEqual(
            self.moments_a[1] * self.moments_a[3]
            - self.moments_a[2] ** 2,
            EXPECTED_SHIFTED_DETERMINANT,
        )

    def test_redundant_cross_minor_remains_positive(self) -> None:
        cross = (
            self.moments_a[0] * self.moments_a[3]
            - self.moments_a[1] * self.moments_a[2]
        )
        self.assertGreater(cross, 0)


if __name__ == "__main__":
    unittest.main()
