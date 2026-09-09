from __future__ import annotations

from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import bivariate_reference as reference


FROZEN = {
    1: [27, 84],
    3: [0, 123120, 699408, 862656],
    5: [0, 0, 1730898720, 14214258432, 35456350464, 25999125504],
}


def diagonal(poly: dict[tuple[int, int], int], order: int) -> list[int]:
    out = [0]*(order+1)
    for (a, b), value in poly.items():
        out[a+b] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def test_reference_diagonal_and_canonical_through_five():
    result = reference.run(5)
    accepted = {1: 111, 3: 1_685_184, 5: 77_400_633_120}
    for order in (1, 3, 5):
        poly = reference.parse_records(result["jets"][order])
        assert diagonal(poly, order) == FROZEN[order]
        assert reference.evaluate(poly, 1, 1) == accepted[order]


def test_reference_even_parity():
    result = reference.run(5)
    for order in (0, 2, 4):
        assert result["jets"][order] == []


def test_exact_first_jet_and_off_diagonal_values():
    result = reference.run(5)
    first = reference.parse_records(result["jets"][1])
    assert first == {(0, 0): 27, (1, 0): 48, (0, 1): 36}
    expected = {
        (2, 3): (231, 14_798_496, 2_845_728_662_304),
        (3, 1): (207, 14_883_264, 3_149_523_754_272),
        (0, 1): (63, 77_760, 274_547_232),
        (1, 0): (75, 666_240, 17_576_484_864),
    }
    for point, values in expected.items():
        obtained = tuple(reference.evaluate(
            reference.parse_records(result["jets"][order]), *point
        ) for order in (1, 3, 5))
        assert obtained == values


def test_selected_exact_sector_coefficients():
    result = reference.run(5)
    third = reference.parse_records(result["jets"][3])
    fifth = reference.parse_records(result["jets"][5])
    assert third[(3, 0)] == 227_328
    assert third[(0, 3)] == 15_552
    assert third[(1, 1)] == 321_408
    assert fifth[(2, 0)] == 1_214_300_160
    assert fifth[(0, 5)] == 11_197_440
    assert fifth[(2, 2)] == 9_805_307_904
