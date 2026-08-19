"""Direct exact finite-width evaluation of ledger equation (3.10).

This module is deliberately independent of ``finite_width_jet.py``.  It does
not propagate a Taylor series or differentiate the feature-ascent ODE.  It
evaluates the fixed NETSOR-transpose-plus scalar program (3.1)--(3.10)
directly from the initialization arrays.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Callable

import numpy as np


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class ThirdDerivativeContraction:
    straight_line: float
    hessian_readout: float
    hessian_middle: float
    hessian_first: float

    @property
    def value(self) -> float:
        return 2.0 * self.straight_line + 4.0 * (
            self.hessian_readout + self.hessian_middle + self.hessian_first
        )


def third_derivative_contraction(
    width: int,
    q0: float,
    activation_derivative: DerivativeOracle,
    seed: int,
) -> ThirdDerivativeContraction:
    """Evaluate ``D_n^3 f_n`` using only the exact contraction program.

    The draw order ``u, W, a`` intentionally matches the independent feature
    jet oracle so a shared seed means a shared finite-width network.  The
    middle matrix below is ``A=W/sqrt(n)`` in the ledger notation.
    """

    if width < 1:
        raise ValueError("width must be positive")
    if q0 < 0:
        raise ValueError("q0 must be nonnegative")

    rng = np.random.default_rng(seed)
    n = width
    u = sqrt(q0) * rng.standard_normal(n)
    middle = rng.standard_normal((n, n)) / sqrt(n)
    readout = rng.standard_normal(n)

    x0 = activation_derivative(0, u)
    x1 = activation_derivative(1, u)
    x2 = activation_derivative(2, u)
    x3 = activation_derivative(3, u)

    z = middle @ x0
    y0 = activation_derivative(0, z)
    y1 = activation_derivative(1, z)
    y2 = activation_derivative(2, z)
    y3 = activation_derivative(3, z)

    b = readout * y1
    backward = middle.T @ b

    q_n = float(np.mean(x0**2))
    d_backward_n = float(np.mean(b**2))

    zeta = q_n * b + q0 * (middle @ (x1**2 * backward))

    c_n = float(np.mean(x0 * x1**2 * backward))
    sigma = (
        2.0 * q0 * c_n * b
        + q0**2 * (middle @ (x2 * x1**2 * backward**2))
    )

    m_n = float(np.mean(x0 * x2 * x1**2 * backward**2))
    tau = (
        3.0 * q0**2 * m_n * b
        + q0**3 * (middle @ (x3 * x1**3 * backward**3))
    )

    capital_b = y0 * y1 + readout * y2 * zeta
    backward_dot = d_backward_n * x0 + middle.T @ capital_b

    straight_line = float(
        np.mean(
            readout
            * (
                y3 * zeta**3
                + 3.0 * y2 * zeta * sigma
                + y1 * tau
            )
            + 3.0 * y0 * (y2 * zeta**2 + y1 * sigma)
        )
    )

    hessian_readout = float(np.mean((y1 * zeta) ** 2))
    hessian_middle = float(
        q_n * np.mean(capital_b**2)
        + q0**2 * np.mean(b**2) * np.mean(x1**4 * backward**2)
        + 2.0
        * q0
        * np.mean(b * capital_b)
        * np.mean(x0 * x1**2 * backward)
    )
    hessian_first = float(
        q0
        * np.mean(
            (
                q0 * x2 * x1 * backward**2
                + x1 * backward_dot
            )
            ** 2
        )
    )

    return ThirdDerivativeContraction(
        straight_line=straight_line,
        hessian_readout=hessian_readout,
        hessian_middle=hessian_middle,
        hessian_first=hessian_first,
    )
