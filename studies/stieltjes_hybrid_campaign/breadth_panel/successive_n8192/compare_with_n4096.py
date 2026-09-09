#!/usr/bin/env python3
"""Paired, read-only comparison of the retained n=4096 and n=8192 campaigns.

Both widths use the same nested antithetic lineages.  Every bootstrap draw
therefore resamples the same lineage indices at both widths and reconstructs
both ensemble-mean output clocks before taking any width difference.  Raw
campaign inputs are hash-checked by the retained analyzers and are never
modified by this script.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import types
from typing import Any

import numpy as np


HERE = Path(__file__).resolve().parent
PANEL = HERE.parent
REPO = HERE.parents[5]
N4096_DIR = PANEL / "successive_n4096"
N8192_DIR = HERE
CONFIGURATION_ORDER = ("C", "A", "M", "V")
OUTPUT_FILES = {
    "results_json": "WIDTH_COMPARISON.json",
    "nodewise_csv": "width_nodewise.csv",
    "aggregate_csv": "width_aggregate.csv",
    "transitions_csv": "width_transitions.csv",
    "best_levels_csv": "width_best_levels.csv",
    "reference_plot": "width_reference_log_ratio.png",
    "nodewise_plot": "width_proxy_error_change.png",
    "aggregate_plot": "width_aggregate_change.png",
}


class ComparisonInvalid(RuntimeError):
    """Raised when the paired comparison contract is not satisfied."""


@dataclass(frozen=True)
class Campaign:
    width: int
    directory: Path
    analyzer: types.ModuleType
    config: dict[str, Any]
    retained_result: dict[str, Any]
    data: dict[str, Any]
    neural_reference: dict[str, np.ndarray]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ComparisonInvalid(message)


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ComparisonInvalid(f"required file is missing: {path}") from exc
    if not isinstance(value, dict):
        raise ComparisonInvalid(f"JSON document is not an object: {path}")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
    except FileNotFoundError as exc:
        raise ComparisonInvalid(f"required file is missing: {path}") from exc
    return digest.hexdigest()


def load_module(path: Path, name: str) -> types.ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_analyzers() -> tuple[types.ModuleType, types.ModuleType]:
    analyzer_4096 = load_module(
        N4096_DIR / "analyze.py", "breadth_successive_n4096_for_width_comparison"
    )
    wrapper_8192 = load_module(
        N8192_DIR / "analyze.py", "breadth_successive_n8192_wrapper_for_comparison"
    )
    analyzer_8192 = wrapper_8192.load_analyzer()
    return analyzer_4096, analyzer_8192


def close_array(left: Any, right: Any, message: str, atol: float = 1e-12) -> None:
    require(
        np.allclose(
            np.asarray(left, dtype=np.float64),
            np.asarray(right, dtype=np.float64),
            rtol=0.0,
            atol=atol,
        ),
        message,
    )


def validate_retained_result(
    width: int,
    directory: Path,
    analyzer: types.ModuleType,
    config: dict[str, Any],
    data: dict[str, Any],
    neural: dict[str, np.ndarray],
) -> dict[str, Any]:
    path = directory / "RESULTS.json"
    result = read_json(path)
    require(
        result.get("schema") == f"breadth-successive-n{width}-analysis-result-v1",
        f"wrong retained result schema at n={width}",
    )
    require(result.get("status") == "complete", f"n={width} analysis is incomplete")
    require(
        result.get("configuration_sha256") == sha256_file(directory / "CONFIG.json"),
        f"n={width} retained configuration digest mismatch",
    )
    require(
        result.get("analysis_source_sha256") == sha256_file(directory / "analyze.py"),
        f"n={width} retained analysis-source digest mismatch",
    )
    records = result.get("configurations", {})
    require(set(records) == set(CONFIGURATION_ORDER), f"n={width} result membership changed")
    nodes = np.asarray(config["nodes"], dtype=np.float64)
    for key in CONFIGURATION_ORDER:
        record = records[key]
        require(int(record.get("width", 0)) == width, f"wrong {key} result width")
        require(
            record.get("lineage_ids") == data[key].lineage_ids.tolist(),
            f"n={width} {key} retained lineage IDs mismatch",
        )
        close_array(record.get("physical_nodes"), nodes, f"n={width} {key} node mismatch", 0.0)
        close_array(
            record.get("neural_reference"),
            neural[key],
            f"n={width} {key} retained neural reference disagrees with raw arrays",
        )
        retained_blocks = record.get("block_provenance", [])
        require(
            len(retained_blocks) == len(data[key].manifests),
            f"n={width} {key} retained block count mismatch",
        )
        for retained, loaded in zip(retained_blocks, data[key].manifests, strict=True):
            require(
                retained.get("manifest_sha256") == loaded.get("manifest_sha256")
                and retained.get("arrays_sha256") == loaded.get("arrays_sha256"),
                f"n={width} {key} retained block provenance mismatch",
            )
    return result


def load_campaign(
    width: int, directory: Path, analyzer: types.ModuleType
) -> Campaign:
    config = analyzer.read_json(analyzer.CONFIG_PATH)
    analyzer.validate_campaign_config(config)
    require(int(config.get("width", 0)) == width, f"wrong campaign width at {directory}")
    data: dict[str, Any] = {}
    neural: dict[str, np.ndarray] = {}
    for key in CONFIGURATION_ORDER:
        blocks = [
            analyzer.load_block(config, key, int(start), int(stop))
            for start, stop in config["lineage_blocks"]
        ]
        merged = analyzer.merge_blocks(blocks, key)
        data[key] = merged
        _, reference = analyzer.central_common_clock(
            merged, np.asarray(config["nodes"], dtype=np.float64)
        )
        neural[key] = reference
    retained = validate_retained_result(
        width, directory, analyzer, config, data, neural
    )
    return Campaign(width, directory, analyzer, config, retained, data, neural)


def validate_matched_contract(c4096: Campaign, c8192: Campaign) -> None:
    require(c4096.width == 4096 and c8192.width == 8192, "wrong compared widths")
    for field in (
        "seed",
        "step",
        "nodes",
        "lineage_blocks",
        "configurations",
        "bootstrap",
    ):
        require(
            c4096.config.get(field) == c8192.config.get(field),
            f"cross-width scientific contract differs at {field}",
        )
    caps_4096 = c4096.config["point_caps"]
    caps_8192 = c8192.config["point_caps"]
    for field in ("gpu_memory_gib", "host_rss_gib", "kernel_ceiling", "state_ceiling"):
        require(caps_4096[field] == caps_8192[field], f"cap differs at {field}")
    require(
        float(caps_8192["wall_seconds_per_8_lineage_block"])
        >= float(caps_4096["wall_seconds_per_8_lineage_block"]),
        "n=8192 wall cap is smaller than the n=4096 cap",
    )


def lineage_diagnostics(campaign: Campaign, key: str) -> dict[int, dict[str, Any]]:
    records: dict[int, dict[str, Any]] = {}
    for start, stop in campaign.config["lineage_blocks"]:
        manifest_path = (
            campaign.directory
            / "runs"
            / f"{key}_n{campaign.width}_L{start}_{stop}"
            / "MANIFEST.json"
        )
        manifest = read_json(manifest_path)
        require(
            int(manifest.get("seed", -1)) == int(campaign.config["seed"]),
            f"n={campaign.width} {key} manifest seed mismatch",
        )
        for record in manifest.get("diagnostics", {}).get("lineages", []):
            lineage = int(record.get("lineage", -1))
            require(lineage not in records, f"duplicate n={campaign.width} {key} lineage {lineage}")
            records[lineage] = record
    require(
        sorted(records) == list(range(16)),
        f"n={campaign.width} {key} diagnostic lineages are not 0 through 15",
    )
    return records


def audit_nested_pairing(c4096: Campaign, c8192: Campaign) -> dict[str, Any]:
    audit: dict[str, Any] = {
        "campaign_seed": int(c4096.config["seed"]),
        "campaign_seed_match": True,
        "bootstrap_contract_match": True,
        "lineage_ids_match": True,
        "required_shared_prefix_sizes": [2048, 4096],
        "configurations": {},
    }
    for key in CONFIGURATION_ORDER:
        require(
            np.array_equal(c4096.data[key].lineage_ids, c8192.data[key].lineage_ids),
            f"{key} lineage IDs are not paired across widths",
        )
        records_4096 = lineage_diagnostics(c4096, key)
        records_8192 = lineage_diagnostics(c8192, key)
        lineage_audit: list[dict[str, Any]] = []
        for lineage in range(16):
            left = records_4096[lineage]
            right = records_8192[lineage]
            require(left.get("configuration") == right.get("configuration"), f"{key} lineage {lineage} configuration mismatch")
            init_left = left.get("initialization", {})
            init_right = right.get("initialization", {})
            require(
                init_left.get("initialization_bytes") == init_right.get("initialization_bytes")
                and init_left.get("dynamics_dtype") == init_right.get("dynamics_dtype"),
                f"{key} lineage {lineage} initialization contract mismatch",
            )
            digest_record: dict[str, Any] = {"lineage": lineage}
            for digest_kind in ("base_prefix_sha256", "physical_prefix_sha256"):
                left_map = init_left.get(digest_kind, {})
                right_map = init_right.get(digest_kind, {})
                require(
                    isinstance(left_map, dict) and isinstance(right_map, dict),
                    f"{key} lineage {lineage} lacks {digest_kind}",
                )
                matched: dict[str, str] = {}
                for size in ("2048", "4096"):
                    require(
                        size in left_map and size in right_map and left_map[size] == right_map[size],
                        f"{key} lineage {lineage} nested {digest_kind} mismatch at n={size}",
                    )
                    matched[size] = str(left_map[size])
                digest_record[digest_kind] = matched
                digest_record[f"n8192_{digest_kind}"] = right_map.get("8192")
            monitor_left = left.get("monitor_sha256")
            monitor_right = right.get("monitor_sha256")
            if monitor_left is not None or monitor_right is not None:
                require(
                    monitor_left == monitor_right,
                    f"{key} lineage {lineage} monitor digest mismatch",
                )
            digest_record["monitor_sha256"] = monitor_left
            lineage_audit.append(digest_record)
        audit["configurations"][key] = {
            "lineage_count": 16,
            "all_shared_prefix_digests_match": True,
            "all_available_monitor_digests_match": True,
            "lineages": lineage_audit,
        }
    return audit


def reference_from_counts(
    data: Any, counts: np.ndarray, nodes: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    lineage_count = counts.shape[1]
    mean_output = counts @ np.ascontiguousarray(data.pair_output.T)
    mean_output /= float(lineage_count)
    valid = (
        np.all(np.isfinite(mean_output), axis=1)
        & (mean_output[:, 0] <= nodes[0])
        & (mean_output[:, -1] >= nodes[-1])
    )
    references = np.full((counts.shape[0], len(nodes)), np.nan, dtype=np.float64)
    for node_index, node in enumerate(nodes):
        crossing = np.argmax(mean_output >= node, axis=1)
        selected = np.flatnonzero(valid & (crossing > 0))
        if selected.size == 0:
            continue
        upper = crossing[selected]
        lower = upper - 1
        output_lower = mean_output[selected, lower]
        denominator = mean_output[selected, upper] - output_lower
        positive = denominator > 0.0
        if not np.all(positive):
            valid[selected[~positive]] = False
            selected = selected[positive]
            upper = upper[positive]
            lower = lower[positive]
            output_lower = output_lower[positive]
            denominator = denominator[positive]
        if selected.size == 0:
            continue
        alpha = (node - output_lower) / denominator
        weighted_lower = np.einsum(
            "br,br->b",
            counts[selected],
            data.pair_weighted_kernel[lower, :],
            optimize=True,
        ) / float(lineage_count)
        weighted_upper = np.einsum(
            "br,br->b",
            counts[selected],
            data.pair_weighted_kernel[upper, :],
            optimize=True,
        ) / float(lineage_count)
        values = (weighted_lower + alpha * (weighted_upper - weighted_lower)) / (1.0 - node)
        finite_positive = np.isfinite(values) & (values > 0.0)
        references[selected[finite_positive], node_index] = values[finite_positive]
        valid[selected[~finite_positive]] = False
    valid &= np.all(np.isfinite(references), axis=1)
    return references, valid


def paired_bootstrap(
    data_4096: Any,
    data_8192: Any,
    nodes: np.ndarray,
    *,
    replicates: int,
    seed: int,
    minimum_valid_fraction: float,
    chunk_size: int = 256,
) -> tuple[np.ndarray, np.ndarray, dict[str, Any]]:
    require(
        np.array_equal(data_4096.lineage_ids, np.arange(16, dtype=np.int64))
        and np.array_equal(data_8192.lineage_ids, data_4096.lineage_ids),
        "paired bootstrap requires the same registered lineages 0 through 15",
    )
    rng = np.random.default_rng(seed)
    references_4096 = np.full((replicates, len(nodes)), np.nan, dtype=np.float64)
    references_8192 = np.full_like(references_4096, np.nan)
    valid_4096 = np.zeros(replicates, dtype=bool)
    valid_8192 = np.zeros(replicates, dtype=bool)
    for first in range(0, replicates, chunk_size):
        last = min(first + chunk_size, replicates)
        size = last - first
        draws = rng.integers(0, 16, size=(size, 16))
        counts = np.zeros((size, 16), dtype=np.float64)
        rows = np.repeat(np.arange(size, dtype=np.int64), 16)
        np.add.at(counts, (rows, draws.reshape(-1)), 1.0)
        ref_4096, good_4096 = reference_from_counts(data_4096, counts, nodes)
        ref_8192, good_8192 = reference_from_counts(data_8192, counts, nodes)
        references_4096[first:last] = ref_4096
        references_8192[first:last] = ref_8192
        valid_4096[first:last] = good_4096
        valid_8192[first:last] = good_8192
    joint = valid_4096 & valid_8192
    valid_fraction = float(np.mean(joint))
    require(
        valid_fraction >= minimum_valid_fraction,
        f"paired valid bootstrap fraction {valid_fraction:.6f} is below the minimum",
    )
    diagnostics = {
        "seed": seed,
        "requested_replicates": replicates,
        "valid_n4096": int(np.count_nonzero(valid_4096)),
        "valid_n8192": int(np.count_nonzero(valid_8192)),
        "joint_valid_replicates": int(np.count_nonzero(joint)),
        "joint_valid_fraction": valid_fraction,
        "draw_pairing": "identical whole-antithetic-lineage index draw at both widths",
        "clock_rule": "recompute each width's primitive-first ensemble-mean output clock in every paired draw",
    }
    return references_4096[joint], references_8192[joint], diagnostics


def quantile_interval(values: np.ndarray, confidence: float) -> tuple[np.ndarray, np.ndarray]:
    alpha = 0.5 * (1.0 - confidence)
    return (
        np.quantile(values, alpha, axis=0, method="linear"),
        np.quantile(values, 1.0 - alpha, axis=0, method="linear"),
    )


def sign_label(value: float) -> str:
    if value > 0.0:
        return "improves"
    if value < 0.0:
        return "worsens"
    return "tie"


def analyze_configuration(
    key: str, c4096: Campaign, c8192: Campaign
) -> tuple[
    dict[str, Any],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    nodes = np.asarray(c4096.config["nodes"], dtype=np.float64)
    bootstrap_contract = c4096.config["bootstrap"]
    confidence = float(bootstrap_contract["confidence"])
    ref_4096 = c4096.neural_reference[key]
    ref_8192 = c8192.neural_reference[key]
    boot_4096, boot_8192, bootstrap_diagnostics = paired_bootstrap(
        c4096.data[key],
        c8192.data[key],
        nodes,
        replicates=int(bootstrap_contract["replicates"]),
        seed=int(bootstrap_contract["seed_by_configuration"][key]),
        minimum_valid_fraction=float(bootstrap_contract["minimum_valid_fraction"]),
    )

    proxy_point = c4096.analyzer.frozen_proxy_points()[key]
    hierarchy = proxy_point.hierarchy
    proxy = np.asarray(
        [[proxy_point.kernel(level, node) for node in nodes] for level in range(len(hierarchy))],
        dtype=np.float64,
    )
    result_4096 = c4096.retained_result["configurations"][key]
    result_8192 = c8192.retained_result["configurations"][key]
    for level in range(len(hierarchy)):
        close_array(
            result_4096["levels"][level]["proxy_kernel"],
            proxy[level],
            f"n=4096 {key} proxy M{level} changed",
            0.0,
        )
        close_array(
            result_8192["levels"][level]["proxy_kernel"],
            proxy[level],
            f"n=8192 {key} proxy M{level} changed",
            0.0,
        )

    log_width_ratio = np.log(ref_8192 / ref_4096)
    bootstrap_log_width_ratio = np.log(boot_8192 / boot_4096)
    ratio_lower, ratio_upper = quantile_interval(bootstrap_log_width_ratio, confidence)

    error_4096 = np.abs(np.log(proxy / ref_4096[None, :]))
    error_8192 = np.abs(np.log(proxy / ref_8192[None, :]))
    bootstrap_error_4096 = np.abs(np.log(proxy[None, :, :] / boot_4096[:, None, :]))
    bootstrap_error_8192 = np.abs(np.log(proxy[None, :, :] / boot_8192[:, None, :]))
    error_change = error_8192 - error_4096
    bootstrap_error_change = bootstrap_error_8192 - bootstrap_error_4096
    node_error_4096_lower, node_error_4096_upper = quantile_interval(
        bootstrap_error_4096, confidence
    )
    node_error_8192_lower, node_error_8192_upper = quantile_interval(
        bootstrap_error_8192, confidence
    )
    node_change_lower, node_change_upper = quantile_interval(
        bootstrap_error_change, confidence
    )

    neural_records: list[dict[str, Any]] = []
    level_records: list[dict[str, Any]] = []
    nodewise_rows: list[dict[str, Any]] = []
    for node_index, node in enumerate(nodes):
        neural_records.append(
            {
                "node": float(node),
                "neural_reference_n4096": float(ref_4096[node_index]),
                "neural_reference_n8192": float(ref_8192[node_index]),
                "log_k8192_over_k4096": float(log_width_ratio[node_index]),
                "log_ratio_ci99": [
                    float(ratio_lower[node_index]),
                    float(ratio_upper[node_index]),
                ],
                "bootstrap_probability_log_ratio_gt_zero": float(
                    np.mean(bootstrap_log_width_ratio[:, node_index] > 0.0)
                ),
            }
        )
    for level, approximation in enumerate(hierarchy):
        nodes_for_level: list[dict[str, Any]] = []
        for node_index, node in enumerate(nodes):
            record = {
                "configuration": key,
                "node": float(node),
                "level_index": level,
                "level_label": f"M{level}",
                "level_name": approximation.name,
                "proxy_kernel": float(proxy[level, node_index]),
                "neural_reference_n4096": float(ref_4096[node_index]),
                "neural_reference_n8192": float(ref_8192[node_index]),
                "log_k8192_over_k4096": float(log_width_ratio[node_index]),
                "log_ratio_ci99_lower": float(ratio_lower[node_index]),
                "log_ratio_ci99_upper": float(ratio_upper[node_index]),
                "absolute_log_error_n4096": float(error_4096[level, node_index]),
                "absolute_log_error_n4096_ci99_lower": float(
                    node_error_4096_lower[level, node_index]
                ),
                "absolute_log_error_n4096_ci99_upper": float(
                    node_error_4096_upper[level, node_index]
                ),
                "absolute_log_error_n8192": float(error_8192[level, node_index]),
                "absolute_log_error_n8192_ci99_lower": float(
                    node_error_8192_lower[level, node_index]
                ),
                "absolute_log_error_n8192_ci99_upper": float(
                    node_error_8192_upper[level, node_index]
                ),
                "error_change_n8192_minus_n4096": float(error_change[level, node_index]),
                "error_change_ci99_lower": float(node_change_lower[level, node_index]),
                "error_change_ci99_upper": float(node_change_upper[level, node_index]),
                "bootstrap_probability_error_decreases": float(
                    np.mean(bootstrap_error_change[:, level, node_index] < 0.0)
                ),
            }
            nodewise_rows.append(record)
            nodes_for_level.append(
                {k: v for k, v in record.items() if k not in {"configuration", "level_index", "level_label", "level_name"}}
            )
        level_records.append(
            {
                "level_index": level,
                "level_label": f"M{level}",
                "level_name": approximation.name,
                "side": approximation.side,
                "information_moments": approximation.information_moments,
                "nodes": nodes_for_level,
            }
        )

    aggregate_rows: list[dict[str, Any]] = []
    transition_rows: list[dict[str, Any]] = []
    best_rows: list[dict[str, Any]] = []
    aggregate_records: list[dict[str, Any]] = []
    transition_records: list[dict[str, Any]] = []
    best_records: list[dict[str, Any]] = []
    for metric, reduce_axis in (("sup_absolute_log_error", np.max), ("mean_absolute_log_error", np.mean)):
        aggregate_4096 = reduce_axis(error_4096, axis=1)
        aggregate_8192 = reduce_axis(error_8192, axis=1)
        bootstrap_aggregate_4096 = reduce_axis(bootstrap_error_4096, axis=2)
        bootstrap_aggregate_8192 = reduce_axis(bootstrap_error_8192, axis=2)
        aggregate_change = aggregate_8192 - aggregate_4096
        bootstrap_aggregate_change = bootstrap_aggregate_8192 - bootstrap_aggregate_4096
        aggregate_4096_lower, aggregate_4096_upper = quantile_interval(
            bootstrap_aggregate_4096, confidence
        )
        aggregate_8192_lower, aggregate_8192_upper = quantile_interval(
            bootstrap_aggregate_8192, confidence
        )
        aggregate_lower, aggregate_upper = quantile_interval(
            bootstrap_aggregate_change, confidence
        )
        best_4096 = int(np.argmin(aggregate_4096))
        best_8192 = int(np.argmin(aggregate_8192))
        bootstrap_best_4096 = np.argmin(bootstrap_aggregate_4096, axis=1)
        bootstrap_best_8192 = np.argmin(bootstrap_aggregate_8192, axis=1)
        best_record = {
            "metric": metric,
            "central_best_level_n4096": f"M{best_4096}",
            "central_best_level_n8192": f"M{best_8192}",
            "central_best_level_changed": bool(best_4096 != best_8192),
            "bootstrap_probability_same_best_level": float(
                np.mean(bootstrap_best_4096 == bootstrap_best_8192)
            ),
            "level_probabilities": [],
        }
        for level in range(len(hierarchy)):
            level_probability = {
                "configuration": key,
                "metric": metric,
                "level_index": level,
                "level_label": f"M{level}",
                "central_best_n4096": bool(level == best_4096),
                "central_best_n8192": bool(level == best_8192),
                "bootstrap_probability_best_n4096": float(np.mean(bootstrap_best_4096 == level)),
                "bootstrap_probability_best_n8192": float(np.mean(bootstrap_best_8192 == level)),
            }
            best_rows.append(level_probability)
            best_record["level_probabilities"].append(
                {k: v for k, v in level_probability.items() if k not in {"configuration", "metric"}}
            )
            aggregate_record = {
                "configuration": key,
                "metric": metric,
                "level_index": level,
                "level_label": f"M{level}",
                "error_n4096": float(aggregate_4096[level]),
                "error_n4096_ci99_lower": float(aggregate_4096_lower[level]),
                "error_n4096_ci99_upper": float(aggregate_4096_upper[level]),
                "error_n8192": float(aggregate_8192[level]),
                "error_n8192_ci99_lower": float(aggregate_8192_lower[level]),
                "error_n8192_ci99_upper": float(aggregate_8192_upper[level]),
                "error_change_n8192_minus_n4096": float(aggregate_change[level]),
                "error_change_ci99_lower": float(aggregate_lower[level]),
                "error_change_ci99_upper": float(aggregate_upper[level]),
                "bootstrap_probability_error_decreases": float(
                    np.mean(bootstrap_aggregate_change[:, level] < 0.0)
                ),
                "central_best_n4096": bool(level == best_4096),
                "central_best_n8192": bool(level == best_8192),
            }
            aggregate_rows.append(aggregate_record)
            aggregate_records.append(
                {k: v for k, v in aggregate_record.items() if k != "configuration"}
            )
        best_records.append(best_record)

        margin_4096 = aggregate_4096[:-1] - aggregate_4096[1:]
        margin_8192 = aggregate_8192[:-1] - aggregate_8192[1:]
        bootstrap_margin_4096 = bootstrap_aggregate_4096[:, :-1] - bootstrap_aggregate_4096[:, 1:]
        bootstrap_margin_8192 = bootstrap_aggregate_8192[:, :-1] - bootstrap_aggregate_8192[:, 1:]
        margin_change = margin_8192 - margin_4096
        bootstrap_margin_change = bootstrap_margin_8192 - bootstrap_margin_4096
        margin_4096_lower, margin_4096_upper = quantile_interval(
            bootstrap_margin_4096, confidence
        )
        margin_8192_lower, margin_8192_upper = quantile_interval(
            bootstrap_margin_8192, confidence
        )
        margin_change_lower, margin_change_upper = quantile_interval(
            bootstrap_margin_change, confidence
        )
        for level in range(1, len(hierarchy)):
            record = {
                "configuration": key,
                "metric": metric,
                "from_level": f"M{level - 1}",
                "to_level": f"M{level}",
                "margin_n4096": float(margin_4096[level - 1]),
                "margin_n4096_ci99_lower": float(margin_4096_lower[level - 1]),
                "margin_n4096_ci99_upper": float(margin_4096_upper[level - 1]),
                "margin_n8192": float(margin_8192[level - 1]),
                "margin_n8192_ci99_lower": float(margin_8192_lower[level - 1]),
                "margin_n8192_ci99_upper": float(margin_8192_upper[level - 1]),
                "sign_n4096": sign_label(float(margin_4096[level - 1])),
                "sign_n8192": sign_label(float(margin_8192[level - 1])),
                "central_sign_changed": bool(
                    np.sign(margin_4096[level - 1]) != np.sign(margin_8192[level - 1])
                ),
                "margin_change_n8192_minus_n4096": float(margin_change[level - 1]),
                "margin_change_ci99_lower": float(margin_change_lower[level - 1]),
                "margin_change_ci99_upper": float(margin_change_upper[level - 1]),
                "bootstrap_probability_margin_positive_n4096": float(
                    np.mean(bootstrap_margin_4096[:, level - 1] > 0.0)
                ),
                "bootstrap_probability_margin_positive_n8192": float(
                    np.mean(bootstrap_margin_8192[:, level - 1] > 0.0)
                ),
            }
            transition_rows.append(record)
            transition_records.append(
                {k: v for k, v in record.items() if k != "configuration"}
            )

    result = {
        "configuration": key,
        "physical_nodes": nodes.tolist(),
        "paired_bootstrap": bootstrap_diagnostics,
        "neural_width_change": neural_records,
        "levels": level_records,
        "aggregate_changes": aggregate_records,
        "best_levels": best_records,
        "transition_signs": transition_records,
    }
    return result, nodewise_rows, aggregate_rows, transition_rows, best_rows


def write_csv_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    require(bool(rows), f"refusing to write empty CSV: {path}")
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def import_plotting():
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise ComparisonInvalid("matplotlib is required for width-comparison plots") from exc
    return matplotlib, plt


def save_figure(figure: Any, path: Path, plt: Any) -> None:
    temporary = path.with_name(path.name + ".tmp.png")
    figure.savefig(temporary, dpi=180)
    plt.close(figure)
    os.replace(temporary, path)


def plot_reference(results: dict[str, dict[str, Any]], path: Path) -> str:
    matplotlib, plt = import_plotting()
    figure, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    for axis, key in zip(axes.flat, CONFIGURATION_ORDER, strict=True):
        records = results[key]["neural_width_change"]
        x = np.asarray([record["node"] for record in records])
        y = np.asarray([record["log_k8192_over_k4096"] for record in records])
        intervals = np.asarray([record["log_ratio_ci99"] for record in records])
        error = np.maximum(np.vstack((y - intervals[:, 0], intervals[:, 1] - y)), 0.0)
        axis.errorbar(x, y, yerr=error, marker="o", capsize=4, color="tab:blue")
        axis.axhline(0.0, color="black", linewidth=1.0)
        axis.set_title(key)
        axis.set_xlabel("physical output y")
        axis.set_ylabel("log(K8192 / K4096)")
        axis.grid(alpha=0.25)
    save_figure(figure, path, plt)
    return matplotlib.__version__


def plot_nodewise_change(results: dict[str, dict[str, Any]], path: Path) -> None:
    _, plt = import_plotting()
    figure, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    for axis, key in zip(axes.flat, CONFIGURATION_ORDER, strict=True):
        levels = results[key]["levels"]
        colors = plt.cm.viridis(np.linspace(0.08, 0.92, len(levels)))
        for color, level in zip(colors, levels, strict=True):
            nodes = level["nodes"]
            x = np.asarray([record["node"] for record in nodes])
            y = np.asarray([record["error_change_n8192_minus_n4096"] for record in nodes])
            lower = np.asarray([record["error_change_ci99_lower"] for record in nodes])
            upper = np.asarray([record["error_change_ci99_upper"] for record in nodes])
            error = np.maximum(np.vstack((y - lower, upper - y)), 0.0)
            axis.errorbar(x, y, yerr=error, marker="o", capsize=2, color=color, label=level["level_label"])
        axis.axhline(0.0, color="black", linewidth=1.0)
        axis.set_title(key)
        axis.set_xlabel("physical output y")
        axis.set_ylabel("|log error|8192 - |log error|4096")
        axis.grid(alpha=0.25)
        axis.legend(fontsize=8, ncol=2)
    save_figure(figure, path, plt)


def plot_aggregate_change(results: dict[str, dict[str, Any]], path: Path) -> None:
    _, plt = import_plotting()
    figure, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    for axis, key in zip(axes.flat, CONFIGURATION_ORDER, strict=True):
        records = results[key]["aggregate_changes"]
        for offset, metric, label, color, marker in (
            (-0.08, "sup_absolute_log_error", "sup", "tab:blue", "o"),
            (0.08, "mean_absolute_log_error", "mean", "tab:orange", "s"),
        ):
            subset = [record for record in records if record["metric"] == metric]
            x = np.arange(len(subset), dtype=np.float64)
            y = np.asarray([record["error_change_n8192_minus_n4096"] for record in subset])
            lower = np.asarray([record["error_change_ci99_lower"] for record in subset])
            upper = np.asarray([record["error_change_ci99_upper"] for record in subset])
            error = np.maximum(np.vstack((y - lower, upper - y)), 0.0)
            axis.errorbar(x + offset, y, yerr=error, marker=marker, capsize=3, color=color, label=label)
        axis.axhline(0.0, color="black", linewidth=1.0)
        axis.set_xticks(np.arange(len(subset)), [record["level_label"] for record in subset])
        axis.set_title(key)
        axis.set_xlabel("accepted approximation level")
        axis.set_ylabel("aggregate error8192 - error4096")
        axis.grid(alpha=0.25)
        axis.legend(fontsize=8)
    save_figure(figure, path, plt)


def campaign_provenance(campaign: Campaign) -> dict[str, Any]:
    return {
        "width": campaign.width,
        "config_path": str((campaign.directory / "CONFIG.json").relative_to(REPO)),
        "config_sha256": sha256_file(campaign.directory / "CONFIG.json"),
        "analysis_path": str((campaign.directory / "analyze.py").relative_to(REPO)),
        "analysis_sha256": sha256_file(campaign.directory / "analyze.py"),
        "retained_result_path": str((campaign.directory / "RESULTS.json").relative_to(REPO)),
        "retained_result_sha256": sha256_file(campaign.directory / "RESULTS.json"),
        "blocks": {
            key: list(campaign.data[key].manifests) for key in CONFIGURATION_ORDER
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=HERE)
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    analyzer_4096, analyzer_8192 = load_analyzers()
    campaign_4096 = load_campaign(4096, N4096_DIR, analyzer_4096)
    campaign_8192 = load_campaign(8192, N8192_DIR, analyzer_8192)
    validate_matched_contract(campaign_4096, campaign_8192)
    pairing_audit = audit_nested_pairing(campaign_4096, campaign_8192)

    results: dict[str, dict[str, Any]] = {}
    nodewise_rows: list[dict[str, Any]] = []
    aggregate_rows: list[dict[str, Any]] = []
    transition_rows: list[dict[str, Any]] = []
    best_rows: list[dict[str, Any]] = []
    for key in CONFIGURATION_ORDER:
        result, nodewise, aggregate, transitions, best = analyze_configuration(
            key, campaign_4096, campaign_8192
        )
        results[key] = result
        nodewise_rows.extend(nodewise)
        aggregate_rows.extend(aggregate)
        transition_rows.extend(transitions)
        best_rows.extend(best)

    write_csv_atomic(output_dir / OUTPUT_FILES["nodewise_csv"], nodewise_rows)
    write_csv_atomic(output_dir / OUTPUT_FILES["aggregate_csv"], aggregate_rows)
    write_csv_atomic(output_dir / OUTPUT_FILES["transitions_csv"], transition_rows)
    write_csv_atomic(output_dir / OUTPUT_FILES["best_levels_csv"], best_rows)
    matplotlib_version = plot_reference(results, output_dir / OUTPUT_FILES["reference_plot"])
    plot_nodewise_change(results, output_dir / OUTPUT_FILES["nodewise_plot"])
    plot_aggregate_change(results, output_dir / OUTPUT_FILES["aggregate_plot"])

    payload = {
        "schema": "breadth-successive-width-comparison-n4096-n8192-v1",
        "status": "complete",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "paired fixed-width movement from n=4096 to n=8192; no width-limit extrapolation",
        "comparison_source_sha256": sha256_file(Path(__file__)),
        "numpy_version": np.__version__,
        "matplotlib_version": matplotlib_version,
        "confidence": float(campaign_4096.config["bootstrap"]["confidence"]),
        "uncertainty_scope": "99% paired whole-lineage bootstrap percentile intervals; every draw uses identical lineage multiplicities at both widths and recomputes both common output clocks",
        "sign_conventions": {
            "neural_width_log_ratio": "log(K8192/K4096); positive means the neural effective kernel increased",
            "proxy_error_change": "absolute-log-error(n8192) minus absolute-log-error(n4096); negative means the proxy moved closer",
            "transition_margin": "previous-level error minus next-level error; positive means the adjacent order improves",
            "transition_margin_change": "n8192 margin minus n4096 margin",
        },
        "input_provenance": {
            "n4096": campaign_provenance(campaign_4096),
            "n8192": campaign_provenance(campaign_8192),
        },
        "nested_pairing_audit": pairing_audit,
        "configurations": results,
        "outputs": OUTPUT_FILES,
    }
    write_json_atomic(output_dir / OUTPUT_FILES["results_json"], payload)
    print(
        json.dumps(
            {
                "status": "complete",
                "results": str(output_dir / OUTPUT_FILES["results_json"]),
                "central_best_levels": {
                    key: {
                        record["metric"]: {
                            "n4096": record["central_best_level_n4096"],
                            "n8192": record["central_best_level_n8192"],
                        }
                        for record in results[key]["best_levels"]
                    }
                    for key in CONFIGURATION_ORDER
                },
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
