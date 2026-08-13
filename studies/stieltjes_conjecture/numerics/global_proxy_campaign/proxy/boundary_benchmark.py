"""No-width calibration of the proxy hierarchy against the exact boundary.

The functions are deterministic and side-effect free.  The module intentionally
does not execute a production grid on import; the campaign protocol controls
the eventual point count and cutoffs.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import log

import numpy as np

from .curves import feature_hitting_time, physical_hitting_time
from .hierarchy import (
    KernelApproximation,
    build_kernel_brackets,
    build_kernel_hierarchy,
    build_taylor_controls,
)
from .variance_boundary import BOUNDARY_MOMENTS, boundary_kernel


MAX_BOUNDARY_POINTS = 2_001


@dataclass(frozen=True)
class ApproximationMetrics:
    name: str
    information_moments: int
    ordering: str
    sup_log_kernel_error: float
    sup_feature_hitting_time_error: float
    sup_physical_hitting_time_error: float
    maximum_side_violation: float | None


@dataclass(frozen=True)
class BracketMetrics:
    information_moments: int
    lower_name: str
    upper_name: str
    sup_log_width: float
    maximum_reference_escape: float


@dataclass(frozen=True)
class BoundaryBenchmark:
    grid_points: int
    y_max: float
    exact_baseline: float
    rational_levels: tuple[ApproximationMetrics, ...]
    taylor_controls: tuple[ApproximationMetrics, ...]
    brackets: tuple[BracketMetrics, ...]

    def record(self) -> dict:
        return asdict(self)


def _metrics(
    name: str,
    information_moments: int,
    ordering: str,
    kernel,
    ys: np.ndarray,
    exact_kernel: np.ndarray,
    exact_feature_time: np.ndarray,
    exact_physical_time: np.ndarray,
    side: str | None,
) -> ApproximationMetrics:
    values = np.array([kernel(float(y)) for y in ys])
    feature = np.array([feature_hitting_time(kernel, float(y)) for y in ys])
    physical = np.array([physical_hitting_time(kernel, float(y)) for y in ys])
    if side == "lower":
        violation = float(np.max(values - exact_kernel))
    elif side == "upper":
        violation = float(np.max(exact_kernel - values))
    else:
        violation = None
    return ApproximationMetrics(
        name=name,
        information_moments=information_moments,
        ordering=ordering,
        sup_log_kernel_error=float(np.max(np.abs(np.log(values / exact_kernel)))),
        sup_feature_hitting_time_error=float(np.max(np.abs(feature - exact_feature_time))),
        sup_physical_hitting_time_error=float(np.max(np.abs(physical - exact_physical_time))),
        maximum_side_violation=violation,
    )


def benchmark_boundary(
    *,
    grid_points: int = 101,
    y_max: float = 0.99,
) -> BoundaryBenchmark:
    """Evaluate a bounded deterministic calibration grid.

    This is a calibration utility, not evidence about finite-width convergence.
    The hard point cap prevents accidental conversion into a broad production
    search before the parent protocol has been frozen.
    """
    if not 3 <= grid_points <= MAX_BOUNDARY_POINTS:
        raise ValueError(f"grid_points must lie in [3,{MAX_BOUNDARY_POINTS}]")
    if not 0 < y_max < 1:
        raise ValueError("y_max must lie strictly between zero and one")
    ys = np.linspace(0.0, float(y_max), int(grid_points))
    exact_kernel = np.array([boundary_kernel(float(y)) for y in ys])
    exact_feature = np.array([
        feature_hitting_time(boundary_kernel, float(y)) for y in ys
    ])
    exact_physical = np.array([
        physical_hitting_time(boundary_kernel, float(y)) for y in ys
    ])

    hierarchy = build_kernel_hierarchy(36, BOUNDARY_MOMENTS)
    rational = tuple(_metrics(
        level.name,
        level.information_moments,
        level.side,
        level.kernel,
        ys,
        exact_kernel,
        exact_feature,
        exact_physical,
        level.side,
    ) for level in hierarchy)

    taylor = tuple(_metrics(
        control.name,
        control.information_moments,
        "unordered",
        control.kernel,
        ys,
        exact_kernel,
        exact_feature,
        exact_physical,
        None,
    ) for control in build_taylor_controls(36, BOUNDARY_MOMENTS))

    brackets: list[BracketMetrics] = []
    for bracket in build_kernel_brackets(36, BOUNDARY_MOMENTS):
        lower = np.array([bracket.lower.kernel(float(y)) for y in ys])
        upper = np.array([bracket.upper.kernel(float(y)) for y in ys])
        escape = np.maximum(lower - exact_kernel, exact_kernel - upper)
        brackets.append(BracketMetrics(
            information_moments=bracket.information_moments,
            lower_name=bracket.lower.name,
            upper_name=bracket.upper.name,
            sup_log_width=float(np.max(np.log(upper / lower))),
            maximum_reference_escape=float(np.max(escape)),
        ))
    return BoundaryBenchmark(
        grid_points=grid_points,
        y_max=float(y_max),
        exact_baseline=36.0,
        rational_levels=rational,
        taylor_controls=taylor,
        brackets=tuple(brackets),
    )
