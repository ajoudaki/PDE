"""Frozen, offline analysis for the successor-02 canonical pilot.

The module is deliberately data-oblivious until the analysis/config/protocol
and unlock hashes have been checked.  It never writes arrays or selects a
scientific branch; its only output is a compact JSON certificate.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

try:
    from ..proxy.inventory import evaluate_family
except ImportError:  # campaign root on PYTHONPATH
    from proxy.inventory import evaluate_family

from .bootstrap import PointBootstrap, bootstrap_point
from .comparison import compare_proxy_hierarchy
from .reference_data import (
    ReferencePoint,
    estimate_curve,
    load_reference_run,
    pair_level_node_kernel,
    sha256,
)
from .verdict import decide_protocol_bracket
from .width import (
    WidthEstimate,
    extrapolate_widths,
    self_averaging_width_summary,
    union_width_estimates,
    width_sensitivity_summary,
)


class PilotAnalysisInvalid(RuntimeError):
    """A frozen-input or mandatory numerical condition cannot be evaluated."""


HERE = Path(__file__).resolve().parent
SOURCE_FILES = (
    Path(__file__),
    HERE / "run_frozen_pilot.py",
    HERE / "bootstrap.py",
    HERE / "comparison.py",
    HERE / "reference_data.py",
    HERE / "verdict.py",
    HERE / "width.py",
    HERE.parent / "proxy" / "exact_series.py",
    HERE.parent / "proxy" / "hierarchy.py",
    HERE.parent / "proxy" / "inventory.py",
)


def _bundle_hash(hashes: Mapping[str, str]) -> str:
    payload = "".join(f"{key}\0{hashes[key]}\n" for key in sorted(hashes))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise PilotAnalysisInvalid(f"JSON root is not an object: {path}")
    return value


def _point_map(points: Sequence[ReferencePoint]) -> dict[str, ReferencePoint]:
    result = {point.point_id: point for point in points}
    if len(result) != len(points):
        raise PilotAnalysisInvalid("loaded reference point ids are not unique")
    return result


def _frozen_metadata(
    summary_path: Path, config_path: Path, analysis_path: Path
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], Path, Path]:
    """Verify every small immutable input before any NPZ is opened."""

    summary_path = summary_path.resolve()
    config_path = config_path.resolve()
    analysis_path = analysis_path.resolve()
    summary, config, analysis = map(_json, (summary_path, config_path, analysis_path))
    if analysis.get("schema_version") != 1:
        raise PilotAnalysisInvalid("unsupported frozen analysis schema")
    if analysis.get("status") != "frozen_before_successor_02_execution":
        raise PilotAnalysisInvalid("analysis choices were not frozen pre-execution")
    if analysis.get("production_config") != config_path.name:
        raise PilotAnalysisInvalid("analysis document names a different production config")
    if config.get("purpose") != "scientific_production":
        raise PilotAnalysisInvalid("reference config is not scientific production")
    if config.get("analysis", {}).get("analysis_config") != analysis_path.name:
        raise PilotAnalysisInvalid("production config names a different analysis document")
    if summary.get("config_name") != config_path.name:
        raise PilotAnalysisInvalid("summary names a different production config")
    config_hash = sha256(config_path)
    if summary.get("config_sha256") != config_hash:
        raise PilotAnalysisInvalid("summary/config SHA-256 mismatch")

    reference_root = config_path.parent.parent
    recorded_source_hashes = summary.get("source_sha256")
    if not isinstance(recorded_source_hashes, Mapping) or not recorded_source_hashes:
        raise PilotAnalysisInvalid("summary lacks the reference source hash map")
    actual_source_hashes: dict[str, str] = {}
    for filename, expected_hash in recorded_source_hashes.items():
        source_path = reference_root / str(filename)
        if source_path.parent != reference_root or not source_path.is_file():
            raise PilotAnalysisInvalid(f"reference source is absent: {filename}")
        actual_source_hashes[str(filename)] = sha256(source_path)
        if actual_source_hashes[str(filename)] != expected_hash:
            raise PilotAnalysisInvalid(f"reference source hash changed: {filename}")
    if _bundle_hash(actual_source_hashes) != summary.get("source_bundle_sha256"):
        raise PilotAnalysisInvalid("reference source-bundle hash is inconsistent")

    # Successor naming is part of the lock contract used by the producer.
    name = config_path.name
    prefix, suffix = "FROZEN_SUCCESSOR_", ".json"
    if not (name.startswith(prefix) and name.endswith(suffix)):
        raise PilotAnalysisInvalid("analysis accepts only a frozen successor config")
    identifier = name[len(prefix) : -len(suffix)]
    if not identifier.isdigit():
        raise PilotAnalysisInvalid("successor identifier is malformed")
    campaign_root = config_path.parent.parent.parent
    protocol_path = campaign_root / f"SUCCESSOR_{identifier}_PROTOCOL.md"
    unlock_path = config_path.parent.parent / "PRODUCTION_UNLOCK.json"
    if not protocol_path.is_file() or not unlock_path.is_file():
        raise PilotAnalysisInvalid("protocol or production unlock is absent")
    unlock = _json(unlock_path)
    expected_unlock = {
        "status": "protocol_frozen_and_execution_authorized",
        "config_name": config_path.name,
        "config_sha256": config_hash,
        "protocol_name": protocol_path.name,
        "protocol_sha256": sha256(protocol_path),
        "analysis_config_name": analysis_path.name,
        "analysis_config_sha256": sha256(analysis_path),
        "source_bundle_sha256": summary.get("source_bundle_sha256"),
    }
    mismatches = {
        key: (unlock.get(key), expected)
        for key, expected in expected_unlock.items()
        if unlock.get(key) != expected
    }
    if mismatches:
        raise PilotAnalysisInvalid(f"production unlock hash mismatch: {mismatches}")
    return summary, config, analysis, unlock, protocol_path, unlock_path


def _validate_exact_point_contract(
    summary: Mapping[str, Any], config: Mapping[str, Any], analysis: Mapping[str, Any]
) -> tuple[str, ...]:
    seeds = analysis["bootstrap"]["seeds_by_point_id"]
    expected = tuple(seeds)
    if len(set(seeds.values())) != len(seeds):
        raise PilotAnalysisInvalid("point-bootstrap seeds are not distinct")
    trend_seeds = analysis["two_width_trend_bootstrap"]["seeds"]
    all_seeds = list(seeds.values()) + list(trend_seeds.values())
    if len(set(all_seeds)) != len(all_seeds):
        raise PilotAnalysisInvalid("point and trend bootstrap streams share a seed")
    config_ids = tuple(str(point["id"]) for point in config["points"])
    summary_ids = tuple(str(point["id"]) for point in summary.get("points", ()))
    if set(config_ids) != set(expected) or set(summary_ids) != set(expected):
        raise PilotAnalysisInvalid("config/summary/analysis point sets differ")
    if len(config_ids) != len(expected) or len(summary_ids) != len(expected):
        raise PilotAnalysisInvalid("duplicate registered point id")
    if summary.get("status") != "complete_scientific_run":
        raise PilotAnalysisInvalid("scientific run is incomplete")
    if not bool(summary.get("scientific_evidence_admissible", False)):
        raise PilotAnalysisInvalid("producer did not admit the run as scientific evidence")
    for record in summary["points"]:
        if record.get("status") != "complete_scientific_point":
            raise PilotAnalysisInvalid(f"incomplete registered point: {record['id']}")
        if not bool(record.get("scientific_evidence_admissible", False)):
            raise PilotAnalysisInvalid(f"inadmissible registered point: {record['id']}")
    return expected


def _group_points(
    points: Mapping[str, ReferencePoint], analysis: Mapping[str, Any]
) -> dict[str, tuple[ReferencePoint, ...]]:
    width = analysis["width_analysis"]
    required_widths = tuple(int(value) for value in width["required_widths"])
    if required_widths != (256, 512):
        raise PilotAnalysisInvalid("successor-02 width ladder changed")
    result: dict[str, tuple[ReferencePoint, ...]] = {}
    for group, ids in width["groups"].items():
        chosen = tuple(sorted((points[str(i)] for i in ids), key=lambda p: p.width))
        if tuple(point.width for point in chosen) != required_widths:
            raise PilotAnalysisInvalid(f"wrong registered widths in {group}")
        if any(point.group != group for point in chosen):
            raise PilotAnalysisInvalid(f"point metadata disagrees with group {group}")
        if any(point.family_key != analysis["family_key"] for point in chosen):
            raise PilotAnalysisInvalid(f"proxy family metadata changed in {group}")
        expected_parameters = tuple(
            sorted(
                (str(key), str(value))
                for key, value in analysis["family_parameters"].items()
            )
        )
        if any(point.family_parameters != expected_parameters for point in chosen):
            raise PilotAnalysisInvalid(f"proxy parameter metadata changed in {group}")
        result[group] = chosen
    scientific = str(width["scientific_comparison_group"])
    sensitivity = str(width["sensitivity_only_group"])
    if any(point.mode != "physical" for point in result[scientific]):
        raise PilotAnalysisInvalid("ordinary comparison group is not physical flow")
    if any(point.mode != "output_clock" for point in result[sensitivity]):
        raise PilotAnalysisInvalid("sensitivity group is not output-clock flow")
    return result


def _bootstrap_points(
    points: Mapping[str, ReferencePoint], analysis: Mapping[str, Any]
) -> dict[str, PointBootstrap]:
    spec = analysis["bootstrap"]
    if (
        spec["resampling_unit"] != "whole_antithetic_pair_lineage"
        or int(spec["resamples"]) != 2_000
        or float(spec["confidence"]) != 0.99
        or float(spec["minimum_valid_fraction"]) != 0.95
        or spec["quantile_method"] != "higher"
    ):
        raise PilotAnalysisInvalid("successor-02 bootstrap constants were changed")
    nodes = np.asarray(analysis["common_output_nodes"], dtype=np.float64)
    result: dict[str, PointBootstrap] = {}
    for point_id, seed in spec["seeds_by_point_id"].items():
        point = points[point_id]
        if not np.array_equal(point.output_nodes, nodes):
            raise PilotAnalysisInvalid(f"output grid changed at {point_id}")
        result[point_id] = bootstrap_point(
            point,
            output_nodes=nodes,
            replicates=2_000,
            seed=int(seed),
            confidence=0.99,
            minimum_valid_fraction=0.95,
        )
    return result


def _width_products(
    groups: Mapping[str, tuple[ReferencePoint, ...]],
    bootstraps: Mapping[str, PointBootstrap],
    analysis: Mapping[str, Any],
) -> tuple[dict[str, tuple[WidthEstimate, ...]], dict[str, Any]]:
    spec = analysis["width_analysis"]
    models = tuple(spec["model_union"])
    if models != (
        "inv_n_all",
        "inv_sqrt_n_all",
        "inv_n_leave_smallest",
        "top_width_direct",
    ):
        raise PilotAnalysisInvalid("frozen width-model union changed")
    estimates: dict[str, tuple[WidthEstimate, ...]] = {}
    unions: dict[str, Any] = {}
    for group, points in groups.items():
        point_bootstraps = tuple(bootstraps[point.point_id] for point in points)
        current = tuple(
            extrapolate_widths(point_bootstraps, model=model) for model in models
        )
        estimates[group] = current
        unions[group] = union_width_estimates(
            current, primary_model=str(spec["primary_model"])
        )
    return estimates, unions


def paired_step_halving(
    points: Mapping[str, ReferencePoint], spec: Mapping[str, Any]
) -> dict[str, Any]:
    coarse = points[str(spec["coarse_point_id"])]
    fine = points[str(spec["fine_point_id"])]
    indices = np.asarray(spec["coarse_lineage_indices"], dtype=np.int64)
    if (
        indices.ndim != 1
        or len(np.unique(indices)) != len(indices)
        or np.any(indices < 0)
        or np.any(indices >= coarse.antithetic_pairs)
    ):
        raise PilotAnalysisInvalid("paired coarse lineage indices are invalid")
    coarse_columns = np.ravel(np.column_stack((2 * indices, 2 * indices + 1)))
    subset_arrays: dict[str, np.ndarray] = {}
    for key, value in coarse.arrays.items():
        array = np.asarray(value)
        if key.startswith("raw_trajectory_") or key.startswith("node_raw_"):
            subset_arrays[key] = array[:, coarse_columns]
        elif key.startswith("node_pair_"):
            subset_arrays[key] = array[:, indices]
        else:
            subset_arrays[key] = array
    subset_config = dict(coarse.config)
    subset_config["antithetic_pairs"] = len(indices)
    coarse_subset = ReferencePoint(
        point_id=coarse.point_id + "__paired_subset",
        group=coarse.group,
        mode=coarse.mode,
        width=coarse.width,
        antithetic_pairs=len(indices),
        target=coarse.target,
        family_key=coarse.family_key,
        family_parameters=coarse.family_parameters,
        config=subset_config,
        diagnostics=coarse.diagnostics,
        arrays=subset_arrays,
        evidence_admissible=coarse.evidence_admissible,
        arrays_path=coarse.arrays_path,
        arrays_sha256=coarse.arrays_sha256,
    )
    coarse_curve = estimate_curve(coarse_subset)
    fine_curve = estimate_curve(fine)
    nodes = coarse_curve["output"]
    if not np.array_equal(nodes, fine_curve["output"]):
        raise PilotAnalysisInvalid("paired step runs use different output grids")
    initial_fields = ("raw_trajectory_output", "raw_trajectory_kernel")
    bitwise = all(
        np.array_equal(
            np.asarray(coarse.arrays[key])[0, coarse_columns],
            np.asarray(fine.arrays[key])[0],
        )
        for key in initial_fields
    )
    seed_equal = int(coarse.config["seed_base"]) == int(fine.config["seed_base"])
    structural = (
        coarse.width == fine.width
        and fine.antithetic_pairs == len(indices)
        and float(coarse.config["step"]) == 2.0 * float(fine.config["step"])
        and coarse.mode == fine.mode == "physical"
        and coarse.target == fine.target
        and float(coarse.config["max_time"]) == float(fine.config["max_time"])
        and coarse.config.get("integrator") == fine.config.get("integrator") == "rk4"
        and not bool(coarse.config.get("microcanonical_readout", False))
        and not bool(fine.config.get("microcanonical_readout", False))
        and fine.config.get("analysis", {}).get("paired_coarse_point_id")
        == coarse.point_id
        and tuple(
            fine.config.get("analysis", {}).get("paired_lineage_indices", ())
        )
        == tuple(int(value) for value in indices)
        and seed_equal
        and bitwise
    )
    relative = np.abs(coarse_curve["kernel"] - fine_curve["kernel"]) / np.abs(
        fine_curve["kernel"]
    )
    through = float(np.max(relative[nodes <= 0.95]))
    index_099 = np.flatnonzero(nodes == 0.99)
    at_099 = float(relative[index_099[0]]) if len(index_099) == 1 else math.inf
    gate = bool(
        structural
        and np.all(np.isfinite(relative))
        and through <= float(spec["maximum_relative_change_through_y_0_95"])
        and at_099 <= float(spec["maximum_relative_change_at_y_0_99"])
    )
    return {
        "passed": gate,
        "seed_base_equal": seed_equal,
        "initial_output_and_kernel_bitwise_equal": bitwise,
        "structural_pairing_valid": structural,
        "coarse_lineage_indices": indices.tolist(),
        "relative_change_by_node": relative.tolist(),
        "maximum_relative_change_through_y_0_95": through,
        "relative_change_at_y_0_99": at_099,
    }


def interval_overlap(physical: Any, clock: Any) -> dict[str, Any]:
    if not np.array_equal(physical.output, clock.output):
        raise PilotAnalysisInvalid("ordinary and output-clock union grids differ")
    overlap = np.maximum(physical.band.lower, clock.band.lower) <= np.minimum(
        physical.band.upper, clock.band.upper
    )
    separation = np.maximum(
        physical.band.lower - clock.band.upper,
        clock.band.lower - physical.band.upper,
    )
    return {
        "passed": bool(np.all(overlap)),
        "overlap_by_node": overlap.tolist(),
        "maximum_definite_separation": float(np.max(separation)),
    }


def projection_trend(
    points: Mapping[str, ReferencePoint], spec: Mapping[str, Any]
) -> dict[str, Any]:
    low = points[str(spec["point_256"])]
    high = points[str(spec["point_512"])]
    p_low = float(low.diagnostics.get(spec["statistic"], math.nan))
    p_high = float(high.diagnostics.get(spec["statistic"], math.nan))
    finite_nonnegative = bool(
        np.all(np.isfinite([p_low, p_high])) and min(p_low, p_high) >= 0.0
    )
    scaled = (
        math.sqrt(high.width) * p_high / (math.sqrt(low.width) * p_low)
        if p_low > 0.0
        else math.inf
    )
    passed = bool(
        finite_nonnegative
        and p_high < p_low
        and scaled <= float(spec["maximum_scaled_rate_ratio"])
    )
    return {
        "passed": passed,
        "p256": p_low,
        "p512": p_high,
        "finite_nonnegative": finite_nonnegative,
        "strict_decrease": p_high < p_low,
        "scaled_rate_ratio": scaled,
    }


def _jensen_statistic(point: ReferencePoint, indices: np.ndarray | None = None) -> float:
    curve = estimate_curve(point, pair_indices=indices)
    value = (
        np.asarray(curve["mean_loss"]) - np.asarray(curve["loss_of_mean_output"])
    ) / np.asarray(curve["mean_loss"])
    return float(np.max(np.abs(value)))


def _self_averaging_statistic(
    point: ReferencePoint, indices: np.ndarray | None = None
) -> float:
    values = pair_level_node_kernel(point)
    if indices is not None:
        values = values[:, indices]
    finite = np.isfinite(values)
    counts = finite.sum(axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        mean = np.nanmean(values, axis=1)
        sd = np.nanstd(values, axis=1, ddof=1)
        statistic = sd / (np.abs(mean) * np.sqrt(counts))
    return float(np.nanmax(statistic))


def _draw(point: ReferencePoint, rng: np.random.Generator) -> np.ndarray:
    return rng.integers(0, point.antithetic_pairs, size=point.antithetic_pairs)


def _difference_interval(
    low: ReferencePoint,
    high: ReferencePoint,
    *,
    metric: Any,
    seed: int,
    resamples: int,
    minimum_valid_fraction: float,
    lower_quantile: float,
    upper_quantile: float,
) -> dict[str, Any]:
    central_low, central_high = metric(low), metric(high)
    rng = np.random.default_rng(seed)
    differences: list[float] = []
    for _ in range(resamples):
        try:
            value = metric(high, _draw(high, rng)) - metric(low, _draw(low, rng))
            if not np.isfinite(value):
                raise FloatingPointError
            differences.append(float(value))
        except FloatingPointError:
            pass
    valid_fraction = len(differences) / resamples
    if valid_fraction < minimum_valid_fraction:
        raise PilotAnalysisInvalid("too few valid two-width trend resamples")
    samples = np.asarray(differences)
    lower = float(np.quantile(samples, lower_quantile, method="higher"))
    upper = float(np.quantile(samples, upper_quantile, method="higher"))
    return {
        "passed": lower <= 0.0,
        "seed": int(seed),
        "attempted_resamples": int(resamples),
        "valid_resamples": len(differences),
        "valid_fraction": valid_fraction,
        "value_256": central_low,
        "value_512": central_high,
        "central_difference_512_minus_256": central_high - central_low,
        "equal_tail_interval": [lower, upper],
    }


def _clock_gap_metric(
    physical: ReferencePoint,
    clock: ReferencePoint,
    physical_indices: np.ndarray | None = None,
    clock_indices: np.ndarray | None = None,
) -> float:
    p = estimate_curve(physical, pair_indices=physical_indices)["kernel"]
    c = estimate_curve(clock, pair_indices=clock_indices)["kernel"]
    return float(np.max(np.abs(np.log(p / c))))


def _clock_gap_interval(
    groups: Mapping[str, tuple[ReferencePoint, ...]],
    analysis: Mapping[str, Any],
) -> dict[str, Any]:
    width_spec = analysis["width_analysis"]
    physical = groups[width_spec["scientific_comparison_group"]]
    clock = groups[width_spec["sensitivity_only_group"]]
    by_width_p = {point.width: point for point in physical}
    by_width_c = {point.width: point for point in clock}
    low_p, high_p = by_width_p[256], by_width_p[512]
    low_c, high_c = by_width_c[256], by_width_c[512]
    trend = analysis["two_width_trend_bootstrap"]
    count = int(trend["resamples"])
    rng = np.random.default_rng(
        int(trend["seeds"]["ordinary_output_clock_log_gap_difference"])
    )
    samples: list[float] = []
    for _ in range(count):
        try:
            high = _clock_gap_metric(
                high_p, high_c, _draw(high_p, rng), _draw(high_c, rng)
            )
            low = _clock_gap_metric(
                low_p, low_c, _draw(low_p, rng), _draw(low_c, rng)
            )
            value = high - low
            if not np.isfinite(value):
                raise FloatingPointError
            samples.append(float(value))
        except FloatingPointError:
            pass
    fraction = len(samples) / count
    minimum = float(analysis["bootstrap"]["minimum_valid_fraction"])
    if fraction < minimum:
        raise PilotAnalysisInvalid("too few valid ordinary/clock trend resamples")
    values = np.asarray(samples)
    qlo = float(trend["lower_quantile"])
    qhi = float(trend["upper_quantile"])
    lower = float(np.quantile(values, qlo, method="higher"))
    upper = float(np.quantile(values, qhi, method="higher"))
    central_low = _clock_gap_metric(low_p, low_c)
    central_high = _clock_gap_metric(high_p, high_c)
    return {
        "passed": lower <= 0.0,
        "seed": int(trend["seeds"]["ordinary_output_clock_log_gap_difference"]),
        "attempted_resamples": count,
        "valid_resamples": len(samples),
        "valid_fraction": fraction,
        "value_256": central_low,
        "value_512": central_high,
        "central_difference_512_minus_256": central_high - central_low,
        "equal_tail_interval": [lower, upper],
    }


def trend_bootstraps(
    groups: Mapping[str, tuple[ReferencePoint, ...]],
    analysis: Mapping[str, Any],
) -> dict[str, Any]:
    trend = analysis["two_width_trend_bootstrap"]
    if (
        int(trend["resamples"]) != 2_000
        or float(trend["confidence"]) != 0.99
        or float(trend["lower_quantile"]) != 0.005
        or float(trend["upper_quantile"]) != 0.995
        or trend["quantile_method"] != "higher"
    ):
        raise PilotAnalysisInvalid("two-width trend bootstrap constants changed")
    ordinary_name = analysis["width_analysis"]["scientific_comparison_group"]
    low, high = groups[ordinary_name]
    common = {
        "resamples": 2_000,
        "minimum_valid_fraction": float(analysis["bootstrap"]["minimum_valid_fraction"]),
        "lower_quantile": 0.005,
        "upper_quantile": 0.995,
    }
    jensen = _difference_interval(
        low,
        high,
        metric=_jensen_statistic,
        seed=int(trend["seeds"]["jensen_relative_gap_difference"]),
        **common,
    )
    self_averaging = _difference_interval(
        low,
        high,
        metric=_self_averaging_statistic,
        seed=int(trend["seeds"]["self_averaging_relative_se_difference"]),
        **common,
    )
    clock_gap = _clock_gap_interval(groups, analysis)
    return {
        "passed": bool(
            jensen["passed"] and self_averaging["passed"] and clock_gap["passed"]
        ),
        "jensen_relative_gap_difference": jensen,
        "self_averaging_relative_se_difference": self_averaging,
        "ordinary_output_clock_log_gap_difference": clock_gap,
    }


def _direct_validity(
    points: Mapping[str, ReferencePoint],
    bootstraps: Mapping[str, PointBootstrap],
    spec: Mapping[str, Any],
) -> dict[str, bool]:
    eps = np.finfo(np.float64).eps
    cancellation = True
    dynamics = True
    clock = True
    positive = True
    rse = True
    jensen_range = True
    for point_id, point in points.items():
        diagnostics = point.diagnostics
        allowed = 64.0 * eps * max(
            1.0, float(diagnostics.get("max_abs_initial_output", math.inf))
        )
        cancellation &= (
            float(diagnostics.get("max_abs_antithetic_initial_output_sum", math.inf))
            <= allowed
        )
        if point.mode == "physical":
            dynamics &= (
                float(diagnostics.get("minimum_mean_output_increment", -math.inf))
                >= float(spec["physical_minimum_mean_output_increment"])
                and float(diagnostics.get("maximum_mean_loss_increment", math.inf))
                <= float(spec["physical_maximum_mean_loss_increment"])
            )
        else:
            clock &= (
                float(diagnostics.get("maximum_absolute_output_clock_defect", math.inf))
                <= float(spec["output_clock_maximum_absolute_defect"])
            )
        band = bootstraps[point_id].band
        positive &= bool(
            np.all(np.isfinite(band.estimate)) and np.all(band.estimate > 0.0)
        )
        pd = bootstraps[point_id].diagnostics
        rse &= (
            float(pd["maximum_relative_standard_error"])
            <= float(spec["maximum_self_averaging_relative_se"])
        )
        curve = estimate_curve(point)
        signed_jensen = (
            np.asarray(curve["mean_loss"])
            - np.asarray(curve["loss_of_mean_output"])
        ) / np.asarray(curve["mean_loss"])
        jensen_range &= bool(
            np.all(signed_jensen >= float(spec["jensen_relative_gap_minimum"]))
            and np.all(signed_jensen <= float(spec["jensen_relative_gap_maximum"]))
        )
    bootstrap_valid = all(
        value.band.attempted_replicates == 2_000
        and value.band.valid_replicates >= 1_900
        for value in bootstraps.values()
    )
    return {
        "all_registered_points_complete_and_hash_bound": True,
        "all_registered_pair_lineages_present": True,
        "no_forbidden_trajectory_repair_or_seed_substitution": True,
        "bootstrap_2000_and_minimum_95_percent_valid": bootstrap_valid,
        "finite_positive_kernels": positive,
        "antithetic_cancellation": bool(cancellation),
        "physical_monotone_output_and_loss": bool(dynamics),
        "output_clock_identity": bool(clock),
        "maximum_self_averaging_relative_se": bool(rse),
        "jensen_relative_gap_range": bool(jensen_range),
    }


def _node_index(nodes: np.ndarray, target: float) -> int:
    found = np.flatnonzero(nodes == target)
    if len(found) != 1:
        raise PilotAnalysisInvalid(f"registered node {target} is absent or duplicated")
    return int(found[0])


def _classifications(
    physical_union: Any,
    physical_points: Sequence[PointBootstrap],
    family: Any,
    gates: Mapping[str, bool],
) -> tuple[list[dict[str, Any]], str, str]:
    union_comparison = compare_proxy_hierarchy(
        physical_union, family, reference_model="ordinary_width_sensitivity_union"
    )
    finite = [
        compare_proxy_hierarchy(
            point, family, reference_model=f"ordinary_finite_width_n{point.width}"
        )
        for point in sorted(physical_points, key=lambda value: value.width)
    ]
    records: list[dict[str, Any]] = []
    statuses: list[str] = []
    for bracket in union_comparison.brackets:
        directions = tuple(
            next(
                item.definite_escape_direction
                for item in comparison.brackets
                if item.information_moments == bracket.information_moments
            )
            for comparison in finite
        )
        decision = decide_protocol_bracket(
            bracket,
            validity_gates=gates,
            two_largest_escape_directions=(directions[0], directions[1]),
        )
        status = {
            "pass": "compatible",
            "fail": "contrary",
            "inconclusive": "inconclusive",
        }[decision.status]
        statuses.append(status)
        records.append(
            {
                "information_moments": bracket.information_moments,
                "classification": status,
                "reason": decision.reason,
                "union_bracket": asdict(bracket),
                "finite_width_escape_directions": list(directions),
            }
        )
    if "contrary" in statuses:
        overall = "contrary"
        reason = "at least one valid rational-prefix escape repeats at both widths"
    elif statuses and all(value == "compatible" for value in statuses):
        overall = "compatible"
        reason = "every registered canonical rational bracket contains the ordinary union"
    else:
        overall = "inconclusive"
        reason = "no valid contrary prefix, but at least one prefix is unresolved"
    return records, overall, reason


def analyze_pilot(
    summary_path: str | Path,
    config_path: str | Path,
    analysis_path: str | Path,
) -> dict[str, Any]:
    summary_path, config_path, analysis_path = map(
        lambda value: Path(value).resolve(),
        (summary_path, config_path, analysis_path),
    )
    summary, config, analysis, unlock, protocol_path, unlock_path = _frozen_metadata(
        summary_path, config_path, analysis_path
    )
    expected_ids = _validate_exact_point_contract(summary, config, analysis)

    # This is the first operation that opens NPZs.
    run = load_reference_run(
        summary_path,
        config_path=config_path,
        verify_hashes=True,
        require_scientific=True,
    )
    points = _point_map(run.points)
    if set(points) != set(expected_ids):
        raise PilotAnalysisInvalid("hash-verified NPZ point set is incomplete")
    groups = _group_points(points, analysis)
    bootstraps = _bootstrap_points(points, analysis)
    estimates, unions = _width_products(groups, bootstraps, analysis)

    width_spec = analysis["width_analysis"]
    physical_name = str(width_spec["scientific_comparison_group"])
    clock_name = str(width_spec["sensitivity_only_group"])
    physical_union, clock_union = unions[physical_name], unions[clock_name]
    step = paired_step_halving(points, analysis["paired_step_halving"])
    agreement = interval_overlap(physical_union, clock_union)
    projection = projection_trend(points, analysis["projection_trend"])
    trends = trend_bootstraps(groups, analysis)
    direct = _direct_validity(points, bootstraps, analysis["direct_validity_gates"])

    resolution = analysis["stage2_resolution_gate"]
    index = _node_index(physical_union.output, float(resolution["node"]))
    resolution_width = float(
        np.log(physical_union.band.upper[index] / physical_union.band.lower[index])
    )
    resolution_record = {
        "passed": resolution_width <= float(resolution["maximum_full_log_band_width"]),
        "node": float(resolution["node"]),
        "full_log_band_width": resolution_width,
        "maximum_full_log_band_width": float(
            resolution["maximum_full_log_band_width"]
        ),
    }
    gates = {
        **direct,
        "paired_step_halving": bool(step["passed"]),
        "ordinary_output_clock_union_overlap": bool(agreement["passed"]),
        "projection_trend": bool(projection["passed"]),
        "two_width_diagnostic_trends": bool(trends["passed"]),
        "stage2_resolution": bool(resolution_record["passed"]),
    }

    family = evaluate_family(
        str(analysis["family_key"]), **dict(analysis["family_parameters"])
    )
    physical_comparison = compare_proxy_hierarchy(
        physical_union, family, reference_model="ordinary_width_sensitivity_union"
    )
    clock_comparison = compare_proxy_hierarchy(
        clock_union, family, reference_model="output_clock_width_sensitivity_union"
    )
    physical_bootstraps = tuple(
        bootstraps[point.point_id] for point in groups[physical_name]
    )
    prefix, overall, reason = _classifications(
        physical_union, physical_bootstraps, family, gates
    )

    analysis_sources = {
        str(path.relative_to(HERE.parent)): sha256(path) for path in SOURCE_FILES
    }
    npz_hashes = {point_id: points[point_id].arrays_sha256 for point_id in expected_ids}
    return {
        "schema_version": 1,
        "status": "complete_offline_analysis",
        "protocol_result": overall,
        "protocol_result_reason": reason,
        "stage3_branch_authorized": bool(all(gates.values()) and overall != "contrary"),
        "input_hashes": {
            "summary_sha256": sha256(summary_path),
            "production_config_sha256": sha256(config_path),
            "analysis_config_sha256": sha256(analysis_path),
            "protocol_sha256": sha256(protocol_path),
            "production_unlock_sha256": sha256(unlock_path),
            "reference_source_bundle_sha256": summary["source_bundle_sha256"],
            "npz_sha256_by_point_id": npz_hashes,
        },
        "analysis_source_sha256": analysis_sources,
        "analysis_source_bundle_sha256": _bundle_hash(analysis_sources),
        "family": family.exact_record(),
        "validity_gates": gates,
        "stage2_resolution": resolution_record,
        "paired_step_halving": step,
        "ordinary_output_clock_agreement": agreement,
        "projection_trend": projection,
        "two_width_trend_bootstraps": trends,
        "point_bootstraps": {
            key: value.compact_record() for key, value in bootstraps.items()
        },
        "width_analysis": {
            group: {
                "components": [value.compact_record() for value in estimates[group]],
                "union": unions[group].compact_record(),
                "sensitivity": width_sensitivity_summary(estimates[group]),
                "self_averaging": self_averaging_width_summary(
                    tuple(bootstraps[p.point_id] for p in groups[group])
                ),
            }
            for group in groups
        },
        "ordinary_proxy_comparison": physical_comparison.record(),
        "output_clock_proxy_comparison": clock_comparison.record(),
        "prefix_classifications": prefix,
        "classification_text": dict(analysis["classification"]),
        "producer_unlock": unlock,
    }


def write_json_atomic(path: str | Path, payload: Mapping[str, Any]) -> None:
    path = Path(path).resolve()
    if path.exists():
        raise FileExistsError(f"refusing to overwrite analysis result: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)
