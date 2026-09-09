from __future__ import annotations

from pathlib import Path
import math
import sys


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import centered_reference as module


def direct_centered_moment(power: int) -> int:
    total = 0
    for q in range(power+1):
        gaussian = 1 if q == 0 else math.prod(range(2*q-1, 0, -2))
        total += math.comb(power, q)*(-1)**(power-q)*gaussian
    return total


def test_centered_moment_recurrence_against_direct_binomial_expansion():
    for power in range(15):
        assert module.centered_moment(power) == direct_centered_moment(power)


def test_reference_exact_orders_through_three():
    result = module.run(3)
    assert result["jets_t"][0] == [0]
    assert result["jets_t"][1] == [60, 0, 44, 0, 7]
    assert result["jets_t"][2] == [0]
    assert result["jets_t"][3] == [
        642048, 163328, 566784, 111104, 163840,
        18816, 18304, 0, 960,
    ]


def test_canonical_and_centered_endpoints_through_three():
    jets = module.run(3)["jets_t"]
    assert sum(jets[1]) == 111
    assert sum(jets[3]) == 1_685_184
    assert jets[1][0] == 60
    assert jets[3][0] == 642_048
