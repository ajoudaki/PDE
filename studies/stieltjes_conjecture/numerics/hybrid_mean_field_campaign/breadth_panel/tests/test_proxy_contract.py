from __future__ import annotations

import math
from pathlib import Path
import sys

import pytest


PANEL = Path(__file__).resolve().parents[1]
if str(PANEL) not in sys.path:
    sys.path.insert(0, str(PANEL))

import proxy_contract as contract  # noqa: E402


EXPECTED_Y09 = {
    "C": (111.0, 166.39319211102995, 162.2394107876611),
    "A": (60.0, 132.2304, 120.17723702172705),
    "M": (195.0, 300.9243550295858, 292.10356971765805),
    "V": (36.75, 98.29695543523533, 85.16921835639502),
    "T+": (80.0, 124.8972875, 121.49930397317853),
    "T-": (31.0, 62.93304890738814, 58.08026168116393),
    "Q2": (3.0, 3.4649751479289943, 3.3843226254650736),
}


@pytest.mark.parametrize("key", tuple(EXPECTED_Y09))
def test_exact_existing_mfp_levels_and_first_bracket(key):
    point = contract.frozen_proxy_points()[key]
    values = point.kernels(0.9)
    assert values[:3] == pytest.approx(EXPECTED_Y09[key], rel=2e-14, abs=2e-14)
    assert values[0] <= values[2] <= values[1]


def test_variance_mapping_uses_physical_output_not_normalized_node():
    point = contract.frozen_proxy_points()["V"]
    normalized = point.hierarchy
    for level in range(3):
        assert point.kernel(level, 0.9) == pytest.approx(
            0.5 * normalized[level].kernel(1.8), rel=0.0, abs=1e-13
        )
    # The old wrong mapping at z=.9 is separated by far more than numerical
    # tolerances and cannot silently pass this regression.
    assert abs(point.kernel(2, 0.9) - 0.5 * normalized[2].kernel(0.9)) > 30.0


def test_hitting_times_and_q1_are_positive_and_ordered():
    points = contract.frozen_proxy_points()
    for key in ("C", "A", "M", "V", "T+", "T-"):
        times = [points[key].hitting_time(level, 0.95) for level in range(3)]
        assert all(math.isfinite(value) and value > 0.0 for value in times)
        # M1 is the upper kernel and therefore the earliest trajectory; NTK
        # is the lower kernel and therefore the latest.
        assert times[1] <= times[2] <= times[0]
    q1 = [points["M"].q1(level, 0.9, metric=2.0) for level in range(3)]
    assert all(value > 1.0 for value in q1)
    assert q1[1] <= q1[2] <= q1[0]


def test_contract_record_is_complete_and_source_hashed():
    record = contract.exact_contract_record()
    assert tuple(record["physical_nodes"]) == contract.PHYSICAL_NODES
    assert set(record["points"]) == set(EXPECTED_Y09)
    for point in record["points"].values():
        family = point["family"]
        assert len(family["source_paths"]) == len(family["source_sha256"])
        assert all(len(digest) == 64 for digest in family["source_sha256"])
