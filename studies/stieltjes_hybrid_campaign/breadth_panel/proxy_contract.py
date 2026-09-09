#!/usr/bin/env python3
"""Exact existing-MFP proxy points for the bounded breadth campaign.

This module contains no simulation and performs no parameter search.  It
maps the already-audited rational hierarchies into the physical coordinates
used by the six frozen breadth-panel configurations.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable

from scipy.integrate import quad


HERE = Path(__file__).resolve().parent
PROXY_CAMPAIGN = HERE.parents[1] / "global_proxy_campaign"
if str(PROXY_CAMPAIGN) not in sys.path:
    sys.path.insert(0, str(PROXY_CAMPAIGN))

from proxy.hierarchy import KernelApproximation, build_kernel_hierarchy  # noqa: E402
from proxy.inventory import EvaluatedFamily, evaluate_family  # noqa: E402


PHYSICAL_NODES = (0.5, 0.75, 0.9, 0.95)


@dataclass(frozen=True)
class FrozenProxyPoint:
    key: str
    family: EvaluatedFamily
    physical_scale: Fraction = Fraction(1)

    @property
    def hierarchy(self) -> tuple[KernelApproximation, ...]:
        return build_kernel_hierarchy(self.family.baseline, self.family.moments)

    def kernel(self, level: int, physical_output: float) -> float:
        if not 0.0 <= physical_output <= 0.95:
            raise ValueError("breadth inference is frozen to 0 <= y <= .95")
        scale = float(self.physical_scale)
        return scale * self.hierarchy[level].kernel(physical_output / scale)

    def kernels(self, physical_output: float) -> tuple[float, ...]:
        return tuple(
            self.kernel(index, physical_output)
            for index in range(len(self.hierarchy))
        )

    def hitting_time(self, level: int, physical_output: float) -> float:
        if not 0.0 <= physical_output < 1.0:
            raise ValueError("physical label-one output must lie in [0,1)")
        integrand: Callable[[float], float] = lambda value: 1.0 / (
            2.0 * (1.0 - value) * self.kernel(level, value)
        )
        return float(quad(integrand, 0.0, physical_output, epsabs=1e-12)[0])

    def q1(self, level: int, physical_output: float, *, metric: float) -> float:
        """First-hidden squared RMS inherited from the output kernel."""

        integrand: Callable[[float], float] = lambda value: (
            8.0 * metric * value / self.kernel(level, value)
        )
        return 1.0 + float(
            quad(integrand, 0.0, physical_output, epsabs=1e-12)[0]
        )


def frozen_proxy_points() -> dict[str, FrozenProxyPoint]:
    return {
        "C": FrozenProxyPoint("C", evaluate_family("canonical")),
        "A": FrozenProxyPoint(
            "A", evaluate_family("centered_activation", c=1)
        ),
        "M": FrozenProxyPoint(
            "M", evaluate_family("relative_metric_output", **{"lambda": 2})
        ),
        "V": FrozenProxyPoint(
            "V",
            evaluate_family("variance_homotopy", alpha=Fraction(1, 2)),
            Fraction(1, 2),
        ),
        "T+": FrozenProxyPoint(
            "T+", evaluate_family("two_input_equal", t=Fraction(1, 2))
        ),
        "T-": FrozenProxyPoint(
            "T-", evaluate_family("two_input_opposite", t=Fraction(1, 2))
        ),
        "Q2": FrozenProxyPoint(
            "Q2", evaluate_family("relative_metric_q2", **{"lambda": 2})
        ),
    }


def symmetric_relative_gap(lower: float, upper: float) -> float:
    denominator = 0.5 * (abs(lower) + abs(upper))
    if denominator == 0.0:
        return 0.0 if lower == upper else math.inf
    return abs(upper - lower) / denominator


def exact_contract_record() -> dict[str, object]:
    """Return a compact JSON-serializable proxy/provenance record."""

    points = frozen_proxy_points()
    records: dict[str, object] = {}
    for key, point in points.items():
        node_records = {
            format(node, ".2f"): list(point.kernels(node))
            for node in PHYSICAL_NODES
        }
        levels = point.kernels(0.9)
        records[key] = {
            "family": point.family.exact_record(),
            "physical_scale": str(point.physical_scale),
            "level_names": [level.name for level in point.hierarchy],
            "physical_node_kernels": node_records,
            "m1_m2_symmetric_gap_y_0_9": symmetric_relative_gap(
                levels[2], levels[1]
            ),
        }
    return {"physical_nodes": list(PHYSICAL_NODES), "points": records}
