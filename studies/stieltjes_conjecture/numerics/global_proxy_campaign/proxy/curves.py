"""Hitting-time construction of feature, output, and loss proxy curves."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


MAX_GRID_POINTS = 10_001


def _validate_y(y: float, target: float | None = None) -> float:
    y = float(y)
    if y < 0:
        raise ValueError("output coordinate must be nonnegative")
    if target is not None and y >= target:
        raise ValueError("physical hitting time is finite only below the target")
    return y


def feature_hitting_time(
    kernel: Callable[[float], float],
    y: float,
    *,
    epsabs: float = 1e-11,
    epsrel: float = 1e-11,
) -> float:
    """Return ``int_0^y du/K(u)`` for feature-ascent time."""
    y = _validate_y(y)
    value, error = quad(lambda u: 1.0 / kernel(u), 0.0, y,
                        epsabs=epsabs, epsrel=epsrel, limit=200)
    if not np.isfinite(value) or error > 20 * max(epsabs, epsrel * abs(value)):
        raise ArithmeticError("feature hitting-time quadrature did not meet tolerance")
    return float(value)


def physical_hitting_time(
    kernel: Callable[[float], float],
    y: float,
    *,
    target: float = 1.0,
    epsabs: float = 1e-11,
    epsrel: float = 1e-11,
) -> float:
    """Return ``int_0^y du/[2(target-u)K(u)]`` for squared-loss flow."""
    y = _validate_y(y, target)
    value, error = quad(lambda u: 1.0 / (2.0 * (target - u) * kernel(u)),
                        0.0, y, epsabs=epsabs, epsrel=epsrel, limit=300)
    if not np.isfinite(value) or error > 20 * max(epsabs, epsrel * abs(value)):
        raise ArithmeticError("physical hitting-time quadrature did not meet tolerance")
    return float(value)


def output_at_time(
    kernel: Callable[[float], float],
    time: float,
    *,
    target: float = 1.0,
    y_cap: float = 0.999999,
    epsabs: float = 1e-11,
    epsrel: float = 1e-11,
) -> float:
    """Invert the physical hitting-time map without integrating an ODE."""
    if time < 0:
        raise ValueError("time must be nonnegative")
    if time == 0:
        return 0.0
    upper = target * y_cap
    maximum_time = physical_hitting_time(
        kernel, upper, target=target, epsabs=epsabs, epsrel=epsrel
    )
    if time > maximum_time:
        raise ValueError("requested time exceeds the precommitted output cap")
    return float(brentq(
        lambda y: physical_hitting_time(
            kernel, y, target=target, epsabs=epsabs, epsrel=epsrel
        ) - time,
        0.0,
        upper,
        xtol=max(epsabs, 1e-14),
        rtol=max(epsrel, 4 * np.finfo(float).eps),
        maxiter=100,
    ))


@dataclass(frozen=True)
class HittingCurve:
    output: tuple[float, ...]
    kernel: tuple[float, ...]
    feature_time: tuple[float, ...]
    physical_time: tuple[float, ...]
    loss: tuple[float, ...]


def sample_hitting_curve(
    kernel: Callable[[float], float],
    outputs: Iterable[float],
    *,
    target: float = 1.0,
    max_grid_points: int = MAX_GRID_POINTS,
    epsabs: float = 1e-11,
    epsrel: float = 1e-11,
) -> HittingCurve:
    """Sample a curve on a common output grid, the campaign's primary clock."""
    ys = tuple(float(value) for value in outputs)
    if not ys:
        raise ValueError("output grid must be nonempty")
    if len(ys) > max_grid_points:
        raise ValueError("output grid exceeds the hard point cap")
    if any(right <= left for left, right in zip(ys, ys[1:])):
        raise ValueError("output grid must be strictly increasing")
    for y in ys:
        _validate_y(y, target)
    kernels = tuple(float(kernel(y)) for y in ys)
    if any(value <= 0 or not np.isfinite(value) for value in kernels):
        raise ArithmeticError("kernel curve must remain finite and positive")
    feature = tuple(feature_hitting_time(kernel, y, epsabs=epsabs, epsrel=epsrel)
                    for y in ys)
    physical = tuple(physical_hitting_time(
        kernel, y, target=target, epsabs=epsabs, epsrel=epsrel
    ) for y in ys)
    return HittingCurve(
        output=ys,
        kernel=kernels,
        feature_time=feature,
        physical_time=physical,
        loss=tuple((target - y) ** 2 for y in ys),
    )


@dataclass(frozen=True)
class TimeCurve:
    time: tuple[float, ...]
    output: tuple[float, ...]
    loss: tuple[float, ...]


def sample_time_curve(
    kernel: Callable[[float], float],
    times: Iterable[float],
    *,
    target: float = 1.0,
    y_cap: float = 0.999999,
    max_grid_points: int = MAX_GRID_POINTS,
) -> TimeCurve:
    times_q = tuple(float(value) for value in times)
    if not times_q:
        raise ValueError("time grid must be nonempty")
    if len(times_q) > max_grid_points:
        raise ValueError("time grid exceeds the hard point cap")
    if any(value < 0 for value in times_q):
        raise ValueError("time grid must be nonnegative")
    if any(right <= left for left, right in zip(times_q, times_q[1:])):
        raise ValueError("time grid must be strictly increasing")
    outputs = tuple(output_at_time(
        kernel, time, target=target, y_cap=y_cap
    ) for time in times_q)
    return TimeCurve(
        time=times_q,
        output=outputs,
        loss=tuple((target - y) ** 2 for y in outputs),
    )
