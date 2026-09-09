import math

import numpy as np
import pytest

from proxy.curves import (
    feature_hitting_time,
    output_at_time,
    physical_hitting_time,
    sample_hitting_curve,
    sample_time_curve,
)
from proxy.hierarchy import build_kernel_hierarchy


def test_constant_kernel_has_closed_form_hitting_times_and_output():
    a = 7.0

    def kernel(_y):
        return a

    for y in (0.0, 0.2, 0.8):
        assert feature_hitting_time(kernel, y) == pytest.approx(y / a)
        assert physical_hitting_time(kernel, y) == pytest.approx(-math.log1p(-y) / (2 * a))
    for time in (0.0, 0.01, 0.1):
        assert output_at_time(kernel, time) == pytest.approx(1 - math.exp(-2 * a * time))


def test_kernel_order_propagates_to_output_order_and_loss_reverse_order():
    levels = build_kernel_hierarchy(36, [6, "7/18"])
    lower, upper = levels[0], levels[1]
    times = np.linspace(0.0, 0.02, 8)
    low_curve = sample_time_curve(lower.kernel, times)
    up_curve = sample_time_curve(upper.kernel, times)
    assert all(lo <= up for lo, up in zip(low_curve.output, up_curve.output))
    assert all(lo >= up for lo, up in zip(low_curve.loss, up_curve.loss))


def test_common_output_grid_and_hard_cap():
    curve = sample_hitting_curve(lambda y: 3.0, [0.0, 0.2, 0.4])
    assert curve.output == (0.0, 0.2, 0.4)
    assert curve.loss == pytest.approx((1.0, 0.64, 0.36))
    with pytest.raises(ValueError, match="hard point cap"):
        sample_hitting_curve(lambda y: 3.0, np.linspace(0, 0.9, 5), max_grid_points=4)
