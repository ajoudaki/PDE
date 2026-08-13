from __future__ import annotations

from fractions import Fraction

import b3_reference as reference


def test_equicorrelated_triangle_moment():
    assert reference.equicorrelated_moment((2, 2, 2)) == (1, 0, 6, 8)


def test_two_color_campaign2_equal_label_control():
    _, desired, _ = reference.run(2, 3)
    assert desired[1] == tuple(map(Fraction, (63, 0, 20, 0, 28)))
    assert desired[3] == tuple(map(Fraction, (
        279680, 0, 423312, 0, 788336, 0, 143232, 0, 50624,
    )))


def test_three_color_first_derivative_and_parity():
    _, desired, _ = reference.run(3, 3)
    assert desired[0] == (Fraction(0),)
    assert desired[2] == (Fraction(0),)
    assert desired[1] == tuple(map(Fraction, (
        47, 0, Fraction(80, 3), 0, Fraction(112, 3),
    )))


def test_canonical_endpoint_through_order_three():
    _, desired, _ = reference.run(3, 3)
    assert sum(desired[1]) == 111
    assert sum(desired[3]) == 1_685_184


def test_explicit_triangle_sector_is_nonzero():
    _, _, stages = reference.run(3, 3)
    witness = reference.three_color_witness(stages[3])
    assert all(value > 0 for value in witness["color_totals"])
    triangle = witness["triangle_columns"]
    assert triangle
    assert all(value > 0 for value in triangle[0]["exponents"])
    assert any(triangle[0]["moment"][q]
               for q in range(1, len(triangle[0]["moment"]), 2))
