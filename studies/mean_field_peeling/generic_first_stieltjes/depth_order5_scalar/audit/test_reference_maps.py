from fractions import Fraction

from .exact_controls import control_table
from .reference_maps import EXPECTED_COUNTS, difference, load_reference


def test_frozen_reference_hashes_and_counts() -> None:
    for depth, expected in EXPECTED_COUNTS.items():
        roots = load_reference(depth)
        assert {name: len(poly) for name, poly in roots.items()} == expected
        for poly in roots.values():
            assert all(value != 0 for value in poly.values())
            assert all(tuple(sorted(key)) == key for key in poly)


def test_difference_is_exact() -> None:
    reference = {(): Fraction(1), ("M_020000",): Fraction(2)}
    same = difference(reference, reference)
    assert same["discrepancy_count"] == 0
    changed = difference({(): Fraction(2), ("M_101000",): Fraction(3)}, reference)
    assert changed["missing_count"] == 1
    assert changed["extra_count"] == 1
    assert changed["unequal_count"] == 1


def test_model_consistent_unit_controls() -> None:
    table = control_table()
    for depth in (2, 3, 4):
        assert table["constant_1"][depth] == {"A": "1", "B": "0", "C": "0"}
    assert table["linear"][3] == {"A": "4", "B": "160", "C": "13888"}
    assert table["linear"][4] == {"A": "5", "B": "400", "C": "73240"}
    assert table["unit_affine_3_4"][3] == {
        "A": "36121/15625",
        "B": "6667077184/244140625",
        "C": "3167910851940352/3814697265625",
    }


def test_unnormalized_quadratic_is_not_a_unit_quotient_control() -> None:
    table = control_table()
    # These formal quotient values deliberately differ from the accepted
    # arbitrary-Gram quadratic model, whose H=2 A is 111.
    assert table["formal_unit_quotient_x2"][2]["A"] == "21"
    assert table["formal_unit_quotient_x2"][2]["A"] != "111"
