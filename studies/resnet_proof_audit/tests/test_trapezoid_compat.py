"""Tiny integration regression for the NumPy 1.x/2.x spelling change."""

from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "source"))
from pde_tangent import _trapezoid  # noqa: E402


class TrapezoidCompatibilityTests(unittest.TestCase):
    def test_affine_integral_on_irregular_grid_and_reversed_axis(self):
        x = np.array([0.0, 0.25, 1.5, 3.0])
        values = np.stack((2.0 * x + 3.0, -x + 2.0))
        # Exact antiderivatives: x^2+3x and -x^2/2+2x.
        np.testing.assert_allclose(_trapezoid(values, x, axis=1), [18.0, 1.5], rtol=0, atol=0)
        np.testing.assert_allclose(_trapezoid(values[:, ::-1], x[::-1], axis=1), [-18.0, -1.5], rtol=0, atol=0)
        np.testing.assert_array_equal(_trapezoid(values[:, :1], x[:1], axis=1), [0.0, 0.0])
