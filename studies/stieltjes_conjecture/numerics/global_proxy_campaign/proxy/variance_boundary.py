"""Exactly solvable Lambert-W variance-boundary reference."""

from __future__ import annotations

from fractions import Fraction
from math import exp, sqrt

from scipy.special import lambertw

from .curves import physical_hitting_time


BOUNDARY_MOMENTS = (
    Fraction(6),
    Fraction(7, 18),
    Fraction(55, 972),
    Fraction(245, 23328),
    Fraction(19, 8640),
)


def q_of_output(y: float) -> float:
    """Return the principal ``q=W(y^2/9)`` for real ``y``."""
    if y < 0:
        raise ValueError("the calibration campaign uses y >= 0")
    return float(lambertw(y * y / 9.0, k=0).real)


def boundary_kernel(y: float) -> float:
    """Return ``kappa_0(y)=36 exp(q/2)(1+q)``."""
    q = q_of_output(float(y))
    return 36.0 * exp(0.5 * q) * (1.0 + q)


def boundary_resolvent(x: float) -> float:
    """Return ``(kappa_0(sqrt(x))-36)/x`` with its exact limit at zero."""
    if x < 0:
        raise ValueError("the Stieltjes resolvent is restricted to x >= 0")
    if x == 0:
        return 6.0
    return (boundary_kernel(sqrt(x)) - 36.0) / x


def boundary_feature_time(y: float) -> float:
    """Exact inverse feature coordinate ``f_0^{-1}(y)``."""
    return sqrt(q_of_output(float(y)) / 144.0)


def boundary_physical_time(y: float) -> float:
    return physical_hitting_time(boundary_kernel, y)


def boundary_feature_output(s: float) -> float:
    """Exact feature-ascent output ``f_0(s)=36s exp(72s^2)``."""
    return 36.0 * s * exp(72.0 * s * s)
