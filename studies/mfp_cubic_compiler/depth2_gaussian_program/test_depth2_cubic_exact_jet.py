#!/usr/bin/env python3
"""Regression gates for the exact raw-cubic depth-2 Gaussian program."""

from __future__ import annotations

import unittest
from pathlib import Path
import sys

from depth2_cubic_exact_jet import derivative_jet, taylor_jet


PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from studies.mean_field_peeling.generic_first_stieltjes.order5.compiler.artifact_evaluator import (  # noqa: E402
    evaluate_artifact_polynomial,
)


EXPECTED_THROUGH_NINE = [
    0,
    305_775,
    0,
    154_118_008_098_000,
    0,
    302_467_842_967_104_331_335_000,
    0,
    1_412_600_607_141_756_021_360_853_290_900_000,
    0,
    12_844_661_809_234_735_951_068_178_383_554_688_801_750_000,
]


class Depth2CubicExactJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.taylor = taylor_jet(9)
        cls.derivative = derivative_jet(9)

    def test_independently_audited_lower_order_controls(self) -> None:
        self.assertEqual(
            self.taylor.derivatives[:6], EXPECTED_THROUGH_NINE[:6]
        )

    def test_fifth_order_gate_replays_frozen_general_activation_artifact(self) -> None:
        artifact = (
            Path(__file__).resolve().parents[2]
            / "generic_first_stieltjes"
            / "order5"
            / "compiler"
            / "LAYER_SEPARATED_ABC_NORMAL_FORM.txt"
        )
        evaluated = evaluate_artifact_polynomial(
            artifact, [0, 0, 0, 1], q0=1
        )
        self.assertEqual(evaluated["A"], EXPECTED_THROUGH_NINE[1])
        self.assertEqual(evaluated["B"], EXPECTED_THROUGH_NINE[3])
        self.assertEqual(evaluated["C"], EXPECTED_THROUGH_NINE[5])

    def test_exact_order_nine_jet(self) -> None:
        self.assertEqual(self.taylor.derivatives, EXPECTED_THROUGH_NINE)

    def test_independent_normalizations_agree(self) -> None:
        self.assertEqual(
            self.derivative.derivatives,
            self.taylor.derivatives,
        )

    def test_sparse_states_are_nonempty(self) -> None:
        for route in (self.taylor, self.derivative):
            for order in route.monomial_counts:
                for name, count in order.items():
                    if name != "degree":
                        self.assertGreater(count, 0)


if __name__ == "__main__":
    unittest.main()
