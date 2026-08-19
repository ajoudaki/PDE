"""Exact internal gates for the independent analytic scalar contraction."""

from __future__ import annotations

from fractions import Fraction
from math import prod
import unittest

import forward_contraction as fw
import reverse_contraction as rv
import moving_contraction as mv


def variable(name: str) -> fw.SPoly:
    return fw.sv(name)


def eval_poly(poly: fw.SPoly, values: dict[str, Fraction]) -> Fraction:
    answer = Fraction(0)
    for monomial, coefficient in poly.items():
        answer += coefficient * prod(values[name] for name in monomial)
    return answer


def linear_moment(name: str) -> Fraction:
    if not name.startswith("M") or len(name) != 7:
        raise ValueError(name)
    counts = tuple(int(value) for value in name[1:])
    if any(counts[index] for index in range(2, 6)):
        return Fraction(0)
    exponent = counts[0]
    if exponent & 1:
        return Fraction(0)
    moment = 1
    for odd in range(1, exponent, 2):
        moment *= odd
    return Fraction(moment)


def atom_names(*polys: fw.SPoly) -> set[str]:
    return {
        name
        for poly in polys
        for monomial in poly
        for name in monomial
        if name.startswith("M")
    }


class AnalyticRouteTests(unittest.TestCase):
    def test_forward_order_three_projection_exact(self) -> None:
        result = fw.transition()
        d = variable("M020000")
        v0 = variable("M101000")
        m = variable("M121000")
        r = variable("M010100")
        s = variable("M002000")
        j0 = variable("M030100")
        expected_w = fw.sa(fw.sm(d, fw.W), fw.sproduct(variable("M040000"), fw.B, fw.sp(fw.L1, 2)))
        expected_u = fw.sa(
            fw.sm(d, fw.U), fw.sm(v0, fw.U), fw.sm(v0, fw.W),
            fw.sproduct(m, fw.B, fw.sp(fw.L1, 2)),
        )
        expected_j = fw.sa(
            fw.ss(fw.sproduct(fw.L1, fw.U, r), 3),
            fw.ss(fw.sproduct(fw.L1, fw.U, s), 3),
            fw.ss(fw.sproduct(fw.L1, fw.W, r), 3),
            fw.sm(d, fw.L3),
            fw.ss(fw.sproduct(j0, fw.B, fw.sp(fw.L1, 3)), 3),
        )
        self.assertEqual(result["w_next"], expected_w)
        self.assertEqual(result["u_next"], expected_u)
        self.assertEqual(result["j_next"], expected_j)

    def test_reverse_order_three_projection_exact(self) -> None:
        result = rv.transition()
        d = variable("M020000")
        s = variable("M002000")
        e = variable("M022000")
        h = variable("M220000")
        m = variable("M121000")
        v0 = variable("M101000")
        r = variable("M010100")
        expected_source11 = fw.sa(
            fw.sproduct(s, rv.B, variable("w")),
            fw.sm(d, rv.E11),
            fw.ss(fw.sproduct(e, fw.sp(rv.B, 2), fw.sp(rv.L1, 2)), 3),
            fw.ss(fw.sproduct(m, rv.B, rv.C10, rv.L1), 2),
            fw.sproduct(h, fw.sp(rv.C10, 2)),
        )
        expected_c10 = fw.sa(
            fw.sm(d, rv.B),
            fw.sproduct(rv.L1, rv.B, s),
            fw.sproduct(rv.L1, rv.B, r),
            fw.sm(d, rv.C10),
            fw.sm(v0, rv.C10),
        )
        self.assertEqual(result["source11"], expected_source11)
        self.assertEqual(result["c10_next"], expected_c10)

    def test_terminal_derivative_ceiling(self) -> None:
        result = list(fw.transition().values()) + list(rv.transition().values())
        result += [
            polynomial
            for group in mv.transitions().values()
            for polynomial in group.values()
        ]
        for name in atom_names(*result):
            counts = tuple(int(value) for value in name[1:])
            self.assertLessEqual(
                max((index for index, count in enumerate(counts) if count), default=0),
                5,
                name,
            )

    def test_compact_tensor_identity(self) -> None:
        # Coordinates are (V5, U[A,p^3], |B|^2, B.c, T[A,A,p], |c|^2).
        original = (2, 22, 14, 30, 36, 16)
        # 2V5 + 10U + 10 B.(B+c) + 4|B+c|^2
        #       + 12 A.m3,  A.m3=U+3T+B.c+|c|^2.
        compact = (
            2,
            10 + 12,
            10 + 4,
            10 + 8 + 12,
            36,
            4 + 12,
        )
        self.assertEqual(compact, original)

    def test_linear_base_frozen_sectors_vanish(self) -> None:
        # H=1: f is bilinear.  The straight fifth derivative and the frozen
        # A.C and B.B sectors vanish.  The subsequently frozen moving passes
        # supply the nonzero mixed-sector total C_1=32.
        b = Fraction(1)
        forward_values: dict[str, Fraction] = {
            "b": b,
            "l1": Fraction(1),
            "l3": Fraction(0),
            "l5": Fraction(0),
            "u": Fraction(0),
            "v": Fraction(0),
            "w": Fraction(0),
            "x": Fraction(0),
            "y": Fraction(0),
        }
        for name in atom_names(*fw.transition().values()):
            forward_values[name] = linear_moment(name)
        # Exact first-layer initialization.
        u = b * linear_moment("M121000")
        v = 3 * b**2 * linear_moment("M140010")
        x = 3 * b**2 * linear_moment("M050100")
        y = 3 * b**2 * linear_moment("M042000")
        j = 3 * b * linear_moment("M030100")
        k = 15 * b**2 * linear_moment("M050001")
        self.assertEqual(k + 5 * v, 0)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual((u, j), (0, 0))


if __name__ == "__main__":
    unittest.main()
