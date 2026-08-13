"""Comparison of finite-width references with exact-moment proxy hierarchies."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping, Protocol

import numpy as np

try:  # Namespace-package import from the repository root.
    from ..proxy.hierarchy import (
        build_kernel_brackets,
        build_kernel_hierarchy,
        build_taylor_controls,
    )
    from ..proxy.inventory import EvaluatedFamily
except ImportError:  # Direct campaign-root execution, matching proxy tests.
    from proxy.hierarchy import (
        build_kernel_brackets,
        build_kernel_hierarchy,
        build_taylor_controls,
    )
    from proxy.inventory import EvaluatedFamily
from .bootstrap import BootstrapBand


class BandedReference(Protocol):
    output: np.ndarray
    band: BootstrapBand


@dataclass(frozen=True)
class ApproximationComparison:
    name: str
    information_moments: int
    ordering: str
    sup_log_kernel_error: float
    sup_physical_hitting_time_error: float | None
    sup_output_error_at_reference_times: float | None
    sup_loss_error_at_reference_times: float | None
    terminal_decay_rate_absolute_error: float | None
    side_status: str
    maximum_side_separation: float


@dataclass(frozen=True)
class BracketComparison:
    information_moments: int
    lower_name: str
    upper_name: str
    sup_log_width: float
    reference_sup_log_band_width: float
    reference_to_bracket_width_ratio: float
    containment_status: str
    definite_escape_direction: str
    maximum_definite_escape: float


@dataclass(frozen=True)
class ProxyComparison:
    family_key: str
    family_parameters: tuple[tuple[str, str], ...]
    observable: str
    output: np.ndarray
    reference_model: str
    rational_levels: tuple[ApproximationComparison, ...]
    taylor_controls: tuple[ApproximationComparison, ...]
    brackets: tuple[BracketComparison, ...]
    parity_improvement: Mapping[str, Any]

    def record(self) -> dict[str, Any]:
        return {
            "family_key": self.family_key,
            "family_parameters": dict(self.family_parameters),
            "observable": self.observable,
            "output": self.output.tolist(),
            "reference_model": self.reference_model,
            "rational_levels": [asdict(value) for value in self.rational_levels],
            "taylor_controls": [asdict(value) for value in self.taylor_controls],
            "brackets": [asdict(value) for value in self.brackets],
            "parity_improvement": dict(self.parity_improvement),
        }


def _cumulative_trapezoid(values: np.ndarray, x: np.ndarray) -> np.ndarray:
    result = np.zeros_like(values)
    result[1:] = np.cumsum(0.5 * np.diff(x) * (values[:-1] + values[1:]))
    return result


def _physical_time(kernel: np.ndarray, output: np.ndarray, target: float) -> np.ndarray:
    if np.any(output >= target):
        raise ValueError("physical proxy comparison requires output below target")
    return _cumulative_trapezoid(
        np.reciprocal(2.0 * (target - output) * kernel), output
    )


def _side_status(
    side: str | None,
    proxy: np.ndarray,
    band: BootstrapBand,
) -> tuple[str, float]:
    if side == "lower":
        if np.all(proxy <= band.lower):
            return "pass", float(np.max(proxy - band.lower))
        definite = proxy - band.upper
        if np.any(definite > 0.0):
            return "fail", float(np.max(definite))
        return "inconclusive", float(np.max(proxy - band.lower))
    if side == "upper":
        if np.all(proxy >= band.upper):
            return "pass", float(np.max(band.upper - proxy))
        definite = band.lower - proxy
        if np.any(definite > 0.0):
            return "fail", float(np.max(definite))
        return "inconclusive", float(np.max(band.upper - proxy))
    return "not_applicable", 0.0


def _metrics(
    *,
    name: str,
    information_moments: int,
    ordering: str,
    values: np.ndarray,
    reference_values: np.ndarray,
    band: BootstrapBand,
    output: np.ndarray,
    target: float | None,
    side: str | None,
) -> ApproximationComparison:
    if np.any(values <= 0.0):
        raise FloatingPointError(f"proxy {name} is nonpositive on the comparison grid")
    physical_error: float | None = None
    output_error: float | None = None
    loss_error: float | None = None
    terminal_rate_error: float | None = None
    if target is not None:
        reference_time = _physical_time(reference_values, output, target)
        proxy_time = _physical_time(values, output, target)
        physical_error = float(np.max(np.abs(proxy_time - reference_time)))
        terminal_rate_error = float(4.0 * abs(values[-1] - reference_values[-1]))
        common = reference_time <= proxy_time[-1]
        if np.count_nonzero(common) >= 2:
            proxy_output = np.interp(reference_time[common], proxy_time, output)
            output_error = float(np.max(np.abs(proxy_output - output[common])))
            loss_error = float(np.max(np.abs(
                np.square(target - proxy_output) - np.square(target - output[common])
            )))
    status, separation = _side_status(side, values, band)
    return ApproximationComparison(
        name=name,
        information_moments=information_moments,
        ordering=ordering,
        sup_log_kernel_error=float(np.max(np.abs(np.log(values / reference_values)))),
        sup_physical_hitting_time_error=physical_error,
        sup_output_error_at_reference_times=output_error,
        sup_loss_error_at_reference_times=loss_error,
        terminal_decay_rate_absolute_error=terminal_rate_error,
        side_status=status,
        maximum_side_separation=separation,
    )


def _parity_improvement(levels: tuple[ApproximationComparison, ...]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for side in ("lower", "upper"):
        errors = [
            level.sup_log_kernel_error for level in levels if level.ordering == side
        ]
        result[side] = {
            "errors": errors,
            "nonincreasing_within_side": all(
                right <= left + 32.0 * np.finfo(float).eps
                for left, right in zip(errors, errors[1:])
            ),
        }
    return result


def compare_proxy_hierarchy(
    reference: BandedReference,
    family: EvaluatedFamily,
    *,
    reference_model: str,
) -> ProxyComparison:
    """Compare every one-moment increment and equal-information Taylor control."""

    output = np.asarray(reference.output, dtype=np.float64)
    band = reference.band
    reference_values = np.asarray(band.estimate, dtype=np.float64)
    if np.any(reference_values <= 0.0):
        raise FloatingPointError("reference kernel must remain positive")
    hierarchy = build_kernel_hierarchy(family.baseline, family.moments)
    rational: list[ApproximationComparison] = []
    for level in hierarchy:
        values = np.asarray([level.kernel(float(y)) for y in output])
        rational.append(_metrics(
            name=level.name,
            information_moments=level.information_moments,
            ordering=level.side,
            values=values,
            reference_values=reference_values,
            band=band,
            output=output,
            target=None if family.training_target is None else float(family.training_target),
            side=level.side,
        ))

    taylors: list[ApproximationComparison] = []
    for control in build_taylor_controls(family.baseline, family.moments):
        values = np.asarray([control.kernel(float(y)) for y in output])
        taylors.append(_metrics(
            name=control.name,
            information_moments=control.information_moments,
            ordering="unordered",
            values=values,
            reference_values=reference_values,
            band=band,
            output=output,
            target=None if family.training_target is None else float(family.training_target),
            side=None,
        ))

    reference_band_width = float(np.max(np.log(band.upper / band.lower)))
    brackets: list[BracketComparison] = []
    for bracket in build_kernel_brackets(family.baseline, family.moments):
        lower = np.asarray([bracket.lower.kernel(float(y)) for y in output])
        upper = np.asarray([bracket.upper.kernel(float(y)) for y in output])
        proxy_width = float(np.max(np.log(upper / lower)))
        contained = np.all(lower <= band.lower) and np.all(band.upper <= upper)
        escape_below = lower - band.upper
        escape_above = band.lower - upper
        definite_escape = np.maximum(escape_below, escape_above)
        if contained:
            status = "pass"
            direction = "none"
        elif np.any(definite_escape > 0.0):
            status = "fail"
            below = bool(np.any(escape_below > 0.0))
            above = bool(np.any(escape_above > 0.0))
            direction = (
                "both" if below and above else "below" if below else "above"
            )
        else:
            status = "inconclusive"
            direction = "none"
        ratio = (
            reference_band_width / proxy_width
            if proxy_width > 0.0 else float("inf")
        )
        brackets.append(BracketComparison(
            information_moments=bracket.information_moments,
            lower_name=bracket.lower.name,
            upper_name=bracket.upper.name,
            sup_log_width=proxy_width,
            reference_sup_log_band_width=reference_band_width,
            reference_to_bracket_width_ratio=ratio,
            containment_status=status,
            definite_escape_direction=direction,
            maximum_definite_escape=float(np.max(definite_escape)),
        ))
    levels_tuple = tuple(rational)
    return ProxyComparison(
        family_key=family.key,
        family_parameters=tuple((key, str(value)) for key, value in family.parameters),
        observable=family.observable,
        output=output,
        reference_model=reference_model,
        rational_levels=levels_tuple,
        taylor_controls=tuple(taylors),
        brackets=tuple(brackets),
        parity_improvement=_parity_improvement(levels_tuple),
    )
