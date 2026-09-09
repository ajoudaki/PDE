"""Activation derivative oracles used by the finite-width audit."""

from __future__ import annotations

from math import exp, sqrt

import numpy as np


def polynomial_oracle(coefficients):
    """Return all derivatives of a polynomial in increasing-power form."""

    coefficients = tuple(float(value) for value in coefficients)

    def derivative(order: int, x: np.ndarray) -> np.ndarray:
        values = list(coefficients)
        for _ in range(order):
            values = [degree * values[degree] for degree in range(1, len(values))]
        out = np.zeros_like(x, dtype=np.float64)
        for coefficient in reversed(values):
            out = out * x + coefficient
        return out

    return derivative


def sine_oracle(order: int, x: np.ndarray) -> np.ndarray:
    """Derivatives of the preregistered unit-variance normalized sine."""

    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)
    phase = order % 4
    if phase == 0:
        value = np.sin(x)
    elif phase == 1:
        value = np.cos(x)
    elif phase == 2:
        value = -np.sin(x)
    else:
        value = -np.cos(x)
    return value / normalization


def tanh_oracle(order: int, x: np.ndarray) -> np.ndarray:
    """Tanh derivatives through order five, used only as an extra audit."""

    y = np.tanh(x)
    if order == 0:
        return y
    if order == 1:
        return 1.0 - y**2
    if order == 2:
        return -2.0 * y + 2.0 * y**3
    if order == 3:
        return -2.0 + 8.0 * y**2 - 6.0 * y**4
    if order == 4:
        return 16.0 * y - 40.0 * y**3 + 24.0 * y**5
    if order == 5:
        return 16.0 - 136.0 * y**2 + 240.0 * y**4 - 120.0 * y**6
    raise ValueError("tanh_oracle is implemented only through order five")
