from __future__ import annotations

import unittest
from fractions import Fraction

from .identity_exact_jet import (
    depth2_derivative,
    depth2_taylor,
    depth3_derivative,
    depth3_taylor,
    validate,
)


class IdentityExactJetTests(unittest.TestCase):
    def test_order_thirteen_extension(self) -> None:
        expected = {
            2: (
                0, 3, 0, 48, 0, 1464, 0, 76800, 0, 6193152, 0,
                708341760, 0, 109038689280,
            ),
            3: (
                0, 4, 0, 160, 0, 13888, 0, 2222592, 0, 571082752, 0,
                214935699456, 0, 111466749771776,
            ),
        }
        routes = {
            2: (depth2_taylor, depth2_derivative),
            3: (depth3_taylor, depth3_derivative),
        }
        for depth, functions in routes.items():
            for function in functions:
                self.assertEqual(
                    tuple(function(13).derivatives),
                    tuple(Fraction(value) for value in expected[depth]),
                )

    def test_depth2_order_eleven(self) -> None:
        expected = tuple(
            Fraction(value)
            for value in (
                0,
                3,
                0,
                48,
                0,
                1464,
                0,
                76800,
                0,
                6193152,
                0,
                708341760,
            )
        )
        taylor = depth2_taylor(11)
        derivative = depth2_derivative(11)
        self.assertEqual(tuple(taylor.derivatives), expected)
        self.assertEqual(tuple(derivative.derivatives), expected)

    def test_depth3_order_eleven(self) -> None:
        expected = tuple(
            Fraction(value)
            for value in (
                0,
                4,
                0,
                160,
                0,
                13888,
                0,
                2222592,
                0,
                571082752,
                0,
                214935699456,
            )
        )
        taylor = depth3_taylor(11)
        derivative = depth3_derivative(11)
        self.assertEqual(tuple(taylor.derivatives), expected)
        self.assertEqual(tuple(derivative.derivatives), expected)

    def test_frozen_validation(self) -> None:
        results = [
            depth2_taylor(11),
            depth2_derivative(11),
            depth3_taylor(11),
            depth3_derivative(11),
        ]
        self.assertEqual(validate(results, 11)["status"], "passed")


if __name__ == "__main__":
    unittest.main()
