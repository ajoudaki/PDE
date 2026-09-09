#!/usr/bin/env python3
"""Fast regression gates for the exact depth-3 Gaussian program."""

from __future__ import annotations

import unittest

from depth3_exact_jet import derivative_jet, taylor_jet


EXPECTED_THROUGH_FIVE = [
    0,
    14_175,
    0,
    139_445_032_896,
    0,
    4_298_284_752_832_899_360,
]


class Depth3ExactJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.taylor = taylor_jet(5)
        cls.derivative = derivative_jet(5)

    def test_accepted_raw_quadratic_controls(self) -> None:
        self.assertEqual(self.taylor.derivatives, EXPECTED_THROUGH_FIVE)

    def test_independent_normalizations_agree(self) -> None:
        self.assertEqual(
            self.derivative.derivatives,
            self.taylor.derivatives,
        )

    def test_sparse_state_is_nonempty(self) -> None:
        for route in (self.taylor, self.derivative):
            for order in route.monomial_counts:
                for name, count in order.items():
                    if name != "degree":
                        self.assertGreater(count, 0)


if __name__ == "__main__":
    unittest.main()
