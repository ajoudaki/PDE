#!/usr/bin/env python3
"""Regression tests for raw and unit-variance sine order-five evaluations."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import mpmath as mp

from normalized_sine_order5 import (
    UnitFourierMoments,
    evaluate_independent as evaluate_unit_independent,
    evaluate_primary as evaluate_unit_primary,
)
from raw_sine_order5 import (
    ClosedFourierMoments,
    evaluate_independent as evaluate_raw_independent,
    evaluate_primary as evaluate_raw_primary,
)


HERE = Path(__file__).resolve().parent


class SineOrderFiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mp.mp.dps = 80
        cls.raw_oracle = ClosedFourierMoments(80)
        cls.raw = evaluate_raw_primary(cls.raw_oracle)
        cls.raw_independent = evaluate_raw_independent(cls.raw_oracle)
        cls.unit_oracle = UnitFourierMoments(80)
        cls.unit = evaluate_unit_primary(cls.unit_oracle)
        cls.unit_independent = evaluate_unit_independent(cls.unit_oracle)

    def assertClose(self, left, right, tolerance="1e-60") -> None:
        self.assertLess(abs(left - mp.mpf(right)), mp.mpf(tolerance))

    def test_raw_derivatives(self) -> None:
        self.assertClose(self.raw["A"], "1")
        self.assertClose(
            self.raw["B"],
            "-1.886999827305931100883737327378247266466322061040333546307940021536186",
        )
        self.assertClose(
            self.raw["C"],
            "79.41498981614465305749487667598359722832666710865177953401263030229069",
        )

    def test_unit_variance_derivatives(self) -> None:
        self.assertClose(
            self.unit["A"],
            "4.037096946465641770044150036061438410171402282463690230320786544802301",
        )
        self.assertClose(
            self.unit["B"],
            "-103.2573311467741889140412475573025922826622454848942874837843393529655",
        )
        self.assertClose(
            self.unit["C"],
            "29944.43234293728236390344108299615290639013823097744233193199439481046",
        )

    def test_independent_maps_agree(self) -> None:
        for name in ("A", "B", "C"):
            self.assertLess(
                abs(self.raw[name] - self.raw_independent[name]),
                mp.mpf("1e-70"),
            )
            self.assertLess(
                abs(self.unit[name] - self.unit_independent[name]),
                mp.mpf("1e-70"),
            )

    def test_normalization_is_exact(self) -> None:
        exponent = (2, 0, 0, 0, 0, 0)
        raw_variance = self.raw_oracle("X", exponent)
        self.assertClose(raw_variance, (1 - mp.exp(-2)) / 2)
        self.assertClose(self.unit_oracle(exponent), "1")

    def test_frozen_maps_have_exact_even_parity(self) -> None:
        raw_map = json.loads(
            (
                HERE.parents[1]
                / "generic_first_stieltjes"
                / "order5"
                / "independent"
                / "independent_layer_tagged_coefficient_map.json"
            ).read_text()
        )
        unit_map = json.loads(
            (
                HERE.parents[1]
                / "generic_first_stieltjes"
                / "order5"
                / "independent"
                / "independent_coefficient_map.json"
            ).read_text()
        )
        self.assertTrue(all(not value for value in raw_map["parity"].values()))
        self.assertTrue(all(not value for value in unit_map["parity"].values()))


if __name__ == "__main__":
    unittest.main()
