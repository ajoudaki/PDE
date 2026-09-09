from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import bivariate_reference as reference


@pytest.fixture(scope="module")
def binary(tmp_path_factory) -> Path:
    output = tmp_path_factory.mktemp("campaign4_build")/"sector_wrapper"
    subprocess.run([
        "g++", "-std=c++17", "-O2", "-DNDEBUG",
        str(HERE/"sector_wrapper.cpp"), "-o", str(output),
    ], check=True)
    return output


def production_polynomial(binary: Path, order: int) -> dict[tuple[int, int], int]:
    out = {}
    for w_hits in range(order+1):
        for a_hits in range(order-w_hits+1):
            completed = subprocess.run([
                str(binary), "f", str(order), str(w_hits), str(a_hits),
            ], check=True, stdout=subprocess.PIPE, text=True)
            record = json.loads(completed.stdout)
            assert record["order"] == order
            assert record["w_hits"] == w_hits
            assert record["a_hits"] == a_hits
            monomial = (order-w_hits-a_hits, w_hits)
            value = int(record["value"])
            if value:
                assert monomial not in out
                out[monomial] = value
    return out


def test_every_bivariate_coefficient_matches_independent_oracle(binary):
    oracle = reference.run(5)
    for order in range(6):
        expected = reference.parse_records(oracle["jets"][order])
        if order % 2 == 0:
            # The production parity rule kills every sector exactly.
            obtained = production_polynomial(binary, order)
        else:
            obtained = production_polynomial(binary, order)
        assert obtained == expected


def test_off_diagonal_points_from_production(binary):
    expected = {
        (2, 3): (231, 14_798_496, 2_845_728_662_304),
        (3, 1): (207, 14_883_264, 3_149_523_754_272),
        (0, 1): (63, 77_760, 274_547_232),
        (1, 0): (75, 666_240, 17_576_484_864),
    }
    polynomials = {order: production_polynomial(binary, order)
                   for order in (1, 3, 5)}
    for point, values in expected.items():
        assert tuple(reference.evaluate(polynomials[order], *point)
                     for order in (1, 3, 5)) == values
