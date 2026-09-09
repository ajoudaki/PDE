#!/usr/bin/env python3
"""Fast regression gates for the accepted depth-3 six-moment result."""

from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path

from depth3_stieltjes_audit import (
    audit_hankels,
    load_existing_moment_transform,
    moments_from_triangular_identity,
)


HERE = Path(__file__).resolve().parent
RESULT = HERE / "results_order13.json"

EXPECTED_MU4 = Fraction(
    52_706_019_439_078_857_802_390_858_812_108_565_605_376,
    5_201_999_704_599_090_318_757_481_910_288_333_892_822_265_625,
)
EXPECTED_MU5 = Fraction(
    101_941_467_717_521_925_959_195_647_155_186_172_639_980_128_272,
    394_295_321_359_534_174_004_571_011_668_886_058_032_512_664_794_921_875,
)
EXPECTED_DET_H2 = Fraction(
    307_594_062_486_287_708_470_348_618_146_958_047_797_145_928_662_386_034_696_990_888_626_634_752,
    54_291_694_295_880_760_637_974_956_015_823_843_147_891_242_466_585_026_704_706_251_621_246_337_890_625,
)
EXPECTED_DET_H2_PLUS = Fraction(
    149_727_900_958_810_667_809_124_859_762_487_199_827_666_057_549_067_484_722_050_515_755_971_792_446_448_013_698_208_883_236_864,
    192_329_039_679_037_943_937_909_881_893_529_487_162_630_437_749_805_012_254_101_434_124_135_827_641_310_925_173_456_780_612_468_719_482_421_875,
)


class Depth3Order13StieltjesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        document = json.loads(RESULT.read_text())
        derivatives = {
            int(key): int(value) for key, value in document["derivatives"].items()
        }
        cls.odd = {
            order: value for order, value in derivatives.items() if order % 2
        }
        cls.baseline, cls.moments = moments_from_triangular_identity(cls.odd)

    def test_two_moment_routes_agree(self) -> None:
        self.assertEqual(
            (self.baseline, self.moments),
            load_existing_moment_transform()(self.odd),
        )

    def test_new_moments(self) -> None:
        self.assertEqual(self.moments[4], EXPECTED_MU4)
        self.assertEqual(self.moments[5], EXPECTED_MU5)

    def test_all_six_moment_hankels_are_positive_definite(self) -> None:
        audit = audit_hankels(self.moments)
        self.assertEqual(audit["accessible_matrix_count"], 6)
        self.assertTrue(audit["all_accessible_matrices_positive_semidefinite"])
        self.assertTrue(audit["all_accessible_matrices_positive_definite"])
        self.assertEqual(len(audit["ordinary"]["H_2"]["principal_minors"]), 7)
        self.assertEqual(len(audit["shifted"]["H_2_plus"]["principal_minors"]), 7)

    def test_new_full_determinants(self) -> None:
        audit = audit_hankels(self.moments)
        self.assertEqual(
            Fraction(audit["ordinary"]["H_2"]["principal_minors"]["0,1,2"]),
            EXPECTED_DET_H2,
        )
        self.assertEqual(
            Fraction(audit["shifted"]["H_2_plus"]["principal_minors"]["0,1,2"]),
            EXPECTED_DET_H2_PLUS,
        )


if __name__ == "__main__":
    unittest.main()

