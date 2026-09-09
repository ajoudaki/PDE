#!/usr/bin/env python3
"""Analyze the fixed n=4096 FP64 successive-proxy experiment.

The resampling unit is one whole antithetic lineage.  Every bootstrap draw
reconstructs its own ensemble-mean output curve, inverts that curve at the
four physical output nodes, and only then forms the effective neural kernel.
The accepted proxy inventory is evaluated read-only in physical coordinates.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import sys
from typing import Any, Iterable

import numpy as np


HERE = Path(__file__).resolve().parent
PANEL = HERE.parent
REPO = HERE.parents[5]
GLOBAL_PROXY_CAMPAIGN = (
    REPO / "studies/stieltjes_conjecture/numerics/global_proxy_campaign"
)
CONFIG_PATH = HERE / "CONFIG.json"
RUNNER_PATH = HERE / "run_block.py"
FP64_DIR = PANEL / "fp64_successor"
FP64_CONFIG_PATH = FP64_DIR / "FROZEN_LOCAL_QUALIFICATION.json"
FP64_LOCK_PATH = FP64_DIR / "FROZEN_LOCAL_QUALIFICATION_LOCK.json"

if str(PANEL) not in sys.path:
    sys.path.insert(0, str(PANEL))
if str(GLOBAL_PROXY_CAMPAIGN) not in sys.path:
    sys.path.insert(0, str(GLOBAL_PROXY_CAMPAIGN))

from proxy_contract import frozen_proxy_points  # noqa: E402
from analysis.bootstrap import simultaneous_log_band  # noqa: E402


CONFIGURATION_ORDER = ("C", "A", "M", "V")
RAW_FIELDS = (
    "raw_output",
    "raw_kernel",
    "raw_kernel_a",
    "raw_kernel_W",
    "raw_kernel_u",
    "raw_weighted_kernel",
    "raw_loss",
    "raw_q1",
    "raw_q2",
)
OUTPUT_FILES = {
    "results_json": "RESULTS.json",
    "nodewise_csv": "nodewise_errors.csv",
    "aggregate_csv": "aggregate_errors.csv",
    "transitions_csv": "transition_margins.csv",
    "curves_plot": "proxy_curves.png",
    "aggregate_plot": "aggregate_errors.png",
    "transitions_plot": "transition_margins.png",
}


class AnalysisInvalid(RuntimeError):
    """Raised when a retained block cannot support the fixed analysis."""


@dataclass(frozen=True)
class BlockData:
    configuration: str
    lineage_start: int
    lineage_stop: int
    time: np.ndarray
    lineage_ids: np.ndarray
    pair_output: np.ndarray
    pair_weighted_kernel: np.ndarray
    manifest_record: dict[str, Any]
    environment_record: dict[str, Any]


@dataclass(frozen=True)
class MergedData:
    configuration: str
    time: np.ndarray
    lineage_ids: np.ndarray
    pair_output: np.ndarray
    pair_weighted_kernel: np.ndarray
    manifests: tuple[dict[str, Any], ...]
    environment: dict[str, Any]


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AnalysisInvalid(f"required file is missing: {path}") from exc
    if not isinstance(value, dict):
        raise AnalysisInvalid(f"JSON document is not an object: {path}")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
    except FileNotFoundError as exc:
        raise AnalysisInvalid(f"required file is missing: {path}") from exc
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AnalysisInvalid(message)


def scalar_text(value: np.ndarray, name: str) -> str:
    require(value.shape == (), f"{name} is not a scalar array")
    item = value.item()
    if isinstance(item, bytes):
        return item.decode("ascii")
    if isinstance(item, str):
        return item
    raise AnalysisInvalid(f"{name} is not a string scalar")


def expected_point(
    config: dict[str, Any], configuration: str, start: int, stop: int
) -> dict[str, Any]:
    spec = config["configurations"][configuration]
    step = float(config["step"])
    steps = int(round(float(spec["max_time"]) / step))
    lineages = stop - start
    return {
        "key": f"{configuration}_n4096_L{start}_{stop}",
        "purpose": "width_screen",
        "configuration": spec["engine_key"],
        "width": int(config["width"]),
        "step": step,
        "max_time": float(spec["max_time"]),
        "lineage_start": start,
        "lineage_stop": stop,
        "prefix_sizes": [2048, 4096],
        "rng_row_block": 128,
        "w_monitor_size": 4096,
        "w_monitor_extent": 2048,
        "w_monitor_seed": int(spec["monitor_seed"]),
        "diagnostic_stride": 256,
        "wall_sync_stride": 32,
        "caps": {
            "wall_seconds": float(
                config["point_caps"]["wall_seconds_per_8_lineage_block"]
            ),
            "max_steps_all_lineages": steps * lineages,
            "gpu_memory_gib": float(config["point_caps"]["gpu_memory_gib"]),
            "host_rss_gib": float(config["point_caps"]["host_rss_gib"]),
            "kernel_ceiling": float(config["point_caps"]["kernel_ceiling"]),
            "state_ceiling": float(config["point_caps"]["state_ceiling"]),
        },
    }


def validate_campaign_config(config: dict[str, Any]) -> None:
    require(
        config.get("schema") == "breadth-successive-n4096-fp64-v1",
        "wrong successive-experiment configuration schema",
    )
    require(config.get("status") == "authorized-execution", "configuration is not active")
    require(int(config.get("width", 0)) == 4096, "analysis is restricted to n=4096")
    require(float(config.get("step", 0.0)) == 1e-5, "unexpected integration step")
    require(config.get("nodes") == [0.5, 0.75, 0.9, 0.95], "unexpected nodes")
    require(config.get("lineage_blocks") == [[0, 8], [8, 16]], "unexpected lineage blocks")
    require(
        tuple(config.get("configurations", {}).keys()) == CONFIGURATION_ORDER,
        "configuration order or membership changed",
    )
    bootstrap = config.get("bootstrap", {})
    require(int(bootstrap.get("replicates", 0)) == 20_000, "bootstrap count changed")
    require(float(bootstrap.get("confidence", 0.0)) == 0.99, "confidence level changed")
    require(
        0.0 < float(bootstrap.get("minimum_valid_fraction", 0.0)) <= 1.0,
        "invalid minimum bootstrap fraction",
    )
    require(
        set(bootstrap.get("seed_by_configuration", {})) == set(CONFIGURATION_ORDER),
        "bootstrap seed map is incomplete",
    )


def validate_block_manifest(
    config: dict[str, Any], configuration: str, start: int, stop: int, block_dir: Path
) -> tuple[dict[str, Any], Path]:
    manifest_path = block_dir / "MANIFEST.json"
    manifest = read_json(manifest_path)
    point = expected_point(config, configuration, start, stop)
    require(
        manifest.get("schema") == "breadth-successive-n4096-block-result-v1",
        f"wrong block schema: {manifest_path}",
    )
    require(manifest.get("status") == "complete", f"incomplete block: {manifest_path}")
    require(manifest.get("configuration") == configuration, f"wrong configuration: {manifest_path}")
    require(manifest.get("point") == point, f"point contract mismatch: {manifest_path}")
    require(manifest.get("seed") == config["seed"], f"seed mismatch: {manifest_path}")
    require(manifest.get("device") == "cuda:0", f"unvalidated device: {manifest_path}")
    require(manifest.get("deterministic_algorithms") is True, f"nondeterministic block: {manifest_path}")
    require(manifest.get("tf32_matmul") is False, f"TF32 matmul enabled: {manifest_path}")
    require(manifest.get("tf32_cudnn") is False, f"TF32 cuDNN enabled: {manifest_path}")
    require(
        manifest.get("cublas_workspace_config") == ":4096:8",
        f"wrong CUBLAS mode: {manifest_path}",
    )
    diagnostics = manifest.get("diagnostics", {})
    require(
        diagnostics.get("lineage_start") == start
        and diagnostics.get("lineage_stop") == stop,
        f"diagnostic lineage interval mismatch: {manifest_path}",
    )
    lineage_diagnostics = diagnostics.get("lineages")
    require(
        isinstance(lineage_diagnostics, list)
        and [entry.get("lineage") for entry in lineage_diagnostics]
        == list(range(start, stop)),
        f"diagnostic lineage identities mismatch: {manifest_path}",
    )
    require(
        float(diagnostics.get("max_gpu_allocated_gib", math.inf))
        <= float(point["caps"]["gpu_memory_gib"]),
        f"GPU cap exceeded: {manifest_path}",
    )
    require(
        float(diagnostics.get("max_host_rss_gib", math.inf))
        <= float(point["caps"]["host_rss_gib"]),
        f"host cap exceeded: {manifest_path}",
    )
    require(
        float(diagnostics.get("elapsed_seconds", math.inf))
        <= float(point["caps"]["wall_seconds"]),
        f"wall cap exceeded: {manifest_path}",
    )

    provenance = manifest.get("provenance", {})
    require(
        provenance.get("campaign_config_sha256") == sha256_file(CONFIG_PATH),
        f"configuration provenance mismatch: {manifest_path}",
    )
    require(
        provenance.get("run_script_sha256") == sha256_file(RUNNER_PATH),
        f"runner provenance mismatch: {manifest_path}",
    )
    require(
        provenance.get("validated_fp64_config_sha256")
        == sha256_file(FP64_CONFIG_PATH),
        f"FP64 configuration provenance mismatch: {manifest_path}",
    )
    require(
        provenance.get("validated_fp64_source_lock_sha256")
        == sha256_file(FP64_LOCK_PATH),
        f"FP64 source-lock provenance mismatch: {manifest_path}",
    )
    require(
        provenance.get("validated_fp64_source_bundle_sha256")
        == read_json(FP64_LOCK_PATH).get("bundle_sha256"),
        f"FP64 source-bundle provenance mismatch: {manifest_path}",
    )
    require(manifest.get("arrays_file") == "arrays.npz", f"wrong NPZ name: {manifest_path}")
    arrays_path = block_dir / "arrays.npz"
    require(
        manifest.get("arrays_sha256") == sha256_file(arrays_path),
        f"NPZ digest mismatch: {arrays_path}",
    )
    return manifest, arrays_path


def load_block(
    config: dict[str, Any], configuration: str, start: int, stop: int
) -> BlockData:
    point = expected_point(config, configuration, start, stop)
    block_dir = HERE / "runs" / point["key"]
    manifest, arrays_path = validate_block_manifest(
        config, configuration, start, stop, block_dir
    )
    steps = int(round(float(point["max_time"]) / float(point["step"])))
    expected_shape = (steps + 1, 2 * (stop - start))

    try:
        archive_context = np.load(arrays_path, allow_pickle=False)
    except (OSError, ValueError) as exc:
        raise AnalysisInvalid(f"cannot read NPZ: {arrays_path}") from exc
    with archive_context as archive:
        missing = {
            "time",
            "lineage_ids",
            "column_lineage_id",
            "antithetic_sign",
            "array_schema_version",
            "dynamics_dtype",
            "initialization_contract",
            *RAW_FIELDS,
        } - set(archive.files)
        require(not missing, f"NPZ misses arrays {sorted(missing)}: {arrays_path}")
        require(
            scalar_text(archive["array_schema_version"], "array_schema_version")
            == "breadth-successive-fp64-arrays-v1",
            f"wrong array schema: {arrays_path}",
        )
        require(
            scalar_text(archive["dynamics_dtype"], "dynamics_dtype") == "float64",
            f"wrong dynamics dtype: {arrays_path}",
        )
        require(
            scalar_text(archive["initialization_contract"], "initialization_contract")
            == "frozen-fp32-cast-exactly-to-fp64",
            f"wrong initialization contract: {arrays_path}",
        )
        time = np.asarray(archive["time"], dtype=np.float64)
        expected_time = np.arange(steps + 1, dtype=np.float64) * float(point["step"])
        require(np.array_equal(time, expected_time), f"wrong time grid: {arrays_path}")
        lineage_ids = np.asarray(archive["lineage_ids"], dtype=np.int64)
        require(
            np.array_equal(lineage_ids, np.arange(start, stop, dtype=np.int64)),
            f"wrong lineage IDs: {arrays_path}",
        )
        require(
            np.array_equal(
                np.asarray(archive["column_lineage_id"], dtype=np.int64),
                np.repeat(lineage_ids, 2),
            ),
            f"wrong column-lineage map: {arrays_path}",
        )
        require(
            np.array_equal(
                np.asarray(archive["antithetic_sign"], dtype=np.int8),
                np.tile(np.asarray((1, -1), dtype=np.int8), stop - start),
            ),
            f"wrong antithetic-sign map: {arrays_path}",
        )
        raw: dict[str, np.ndarray] = {}
        for field in RAW_FIELDS:
            value = np.asarray(archive[field])
            require(value.dtype == np.float64, f"{field} is not float64: {arrays_path}")
            require(value.shape == expected_shape, f"wrong {field} shape: {arrays_path}")
            require(np.all(np.isfinite(value)), f"nonfinite {field}: {arrays_path}")
            raw[field] = value.copy()

    require(
        np.all(np.diff(raw["raw_output"], axis=0) > 0.0),
        f"a raw output trajectory is not strictly increasing: {arrays_path}",
    )
    for field in ("raw_kernel", "raw_kernel_a", "raw_kernel_W", "raw_kernel_u", "raw_weighted_kernel", "raw_q1", "raw_q2"):
        require(np.all(raw[field] > 0.0), f"nonpositive {field}: {arrays_path}")
    require(np.all(raw["raw_loss"] >= 0.0), f"negative loss: {arrays_path}")
    require(
        np.max(np.abs(0.5 * (raw["raw_output"][0, 0::2] + raw["raw_output"][0, 1::2])))
        <= 1e-14,
        f"antithetic initial output does not cancel: {arrays_path}",
    )

    pair_output = 0.5 * (raw["raw_output"][:, 0::2] + raw["raw_output"][:, 1::2])
    pair_weighted = 0.5 * (
        raw["raw_weighted_kernel"][:, 0::2]
        + raw["raw_weighted_kernel"][:, 1::2]
    )
    manifest_record = {
        "manifest_path": str((block_dir / "MANIFEST.json").relative_to(REPO)),
        "manifest_sha256": sha256_file(block_dir / "MANIFEST.json"),
        "arrays_path": str(arrays_path.relative_to(REPO)),
        "arrays_sha256": manifest["arrays_sha256"],
        "lineage_start": start,
        "lineage_stop": stop,
        "elapsed_seconds": manifest["diagnostics"]["elapsed_seconds"],
        "max_gpu_allocated_gib": manifest["diagnostics"]["max_gpu_allocated_gib"],
        "max_host_rss_gib": manifest["diagnostics"]["max_host_rss_gib"],
    }
    environment = {
        key: manifest.get(key)
        for key in (
            "device",
            "gpu_identity",
            "torch_version",
            "cuda_version",
            "deterministic_algorithms",
            "tf32_matmul",
            "tf32_cudnn",
            "cublas_workspace_config",
        )
    }
    return BlockData(
        configuration=configuration,
        lineage_start=start,
        lineage_stop=stop,
        time=time,
        lineage_ids=lineage_ids,
        pair_output=pair_output,
        pair_weighted_kernel=pair_weighted,
        manifest_record=manifest_record,
        environment_record=environment,
    )


def merge_blocks(blocks: Iterable[BlockData], configuration: str) -> MergedData:
    pieces = list(blocks)
    require(len(pieces) == 2, f"{configuration} does not have exactly two blocks")
    pieces.sort(key=lambda block: block.lineage_start)
    require(
        all(block.configuration == configuration for block in pieces),
        f"configuration mismatch while merging {configuration}",
    )
    require(
        np.array_equal(pieces[0].time, pieces[1].time),
        f"time grids differ across {configuration} blocks",
    )
    require(
        pieces[0].environment_record == pieces[1].environment_record,
        f"execution environments differ across {configuration} blocks",
    )
    lineage_ids = np.concatenate([block.lineage_ids for block in pieces])
    require(
        np.array_equal(lineage_ids, np.arange(16, dtype=np.int64)),
        f"{configuration} lineages are not exactly 0 through 15",
    )
    pair_output = np.concatenate([block.pair_output for block in pieces], axis=1)
    pair_weighted = np.concatenate(
        [block.pair_weighted_kernel for block in pieces], axis=1
    )
    require(
        pair_output.shape[1] == pair_weighted.shape[1] == len(lineage_ids),
        f"pair count mismatch after merging {configuration}",
    )
    return MergedData(
        configuration=configuration,
        time=pieces[0].time,
        lineage_ids=lineage_ids,
        pair_output=pair_output,
        pair_weighted_kernel=pair_weighted,
        manifests=tuple(block.manifest_record for block in pieces),
        environment=pieces[0].environment_record,
    )


def central_common_clock(data: MergedData, nodes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mean_output = data.pair_output.mean(axis=1)
    mean_weighted = data.pair_weighted_kernel.mean(axis=1)
    require(np.all(np.diff(mean_output) > 0.0), f"{data.configuration} mean output is not increasing")
    require(
        mean_output[0] <= nodes[0] and mean_output[-1] >= nodes[-1],
        f"{data.configuration} mean output does not cover all nodes",
    )
    node_time = np.interp(nodes, mean_output, data.time)
    numerator = np.interp(node_time, data.time, mean_weighted)
    reference = numerator / (1.0 - nodes)
    require(np.all(np.isfinite(reference)) and np.all(reference > 0.0), f"invalid {data.configuration} reference")
    return node_time, reference


def bootstrap_common_clock(
    data: MergedData,
    nodes: np.ndarray,
    *,
    replicates: int,
    seed: int,
    chunk_size: int = 256,
) -> tuple[np.ndarray, int]:
    """Pair-bootstrap the neural reference, re-inverting every mean clock."""

    lineage_count = len(data.lineage_ids)
    require(lineage_count == 16, "bootstrap requires the registered 16 lineages")
    rng = np.random.default_rng(seed)
    references = np.full((replicates, len(nodes)), np.nan, dtype=np.float64)
    invalid = 0
    output_transpose = np.ascontiguousarray(data.pair_output.T)

    for first in range(0, replicates, chunk_size):
        last = min(replicates, first + chunk_size)
        size = last - first
        draws = rng.integers(0, lineage_count, size=(size, lineage_count))
        counts = np.zeros((size, lineage_count), dtype=np.float64)
        rows = np.repeat(np.arange(size, dtype=np.int64), lineage_count)
        np.add.at(counts, (rows, draws.reshape(-1)), 1.0)
        mean_output = (counts @ output_transpose) / float(lineage_count)
        valid = (
            np.all(np.isfinite(mean_output), axis=1)
            & (mean_output[:, 0] <= nodes[0])
            & (mean_output[:, -1] >= nodes[-1])
        )
        chunk_reference = np.full((size, len(nodes)), np.nan, dtype=np.float64)

        for node_index, node in enumerate(nodes):
            crossing = np.argmax(mean_output >= node, axis=1)
            node_valid = valid & (crossing > 0)
            selected = np.flatnonzero(node_valid)
            if selected.size == 0:
                continue
            upper = crossing[selected]
            lower = upper - 1
            output_lower = mean_output[selected, lower]
            output_upper = mean_output[selected, upper]
            denominator = output_upper - output_lower
            positive = denominator > 0.0
            if not np.all(positive):
                node_valid[selected[~positive]] = False
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
            numerator = weighted_lower + alpha * (weighted_upper - weighted_lower)
            values = numerator / (1.0 - node)
            finite_positive = np.isfinite(values) & (values > 0.0)
            chunk_reference[selected[finite_positive], node_index] = values[finite_positive]
            if not np.all(finite_positive):
                valid[selected[~finite_positive]] = False

        valid &= np.all(np.isfinite(chunk_reference), axis=1)
        references[first:last] = chunk_reference
        invalid += int(np.count_nonzero(~valid))

    return references, invalid


def quantile_interval(values: np.ndarray, confidence: float) -> tuple[np.ndarray, np.ndarray]:
    alpha = 0.5 * (1.0 - confidence)
    lower = np.quantile(values, alpha, axis=0, method="linear")
    upper = np.quantile(values, 1.0 - alpha, axis=0, method="linear")
    return lower, upper


def analyze_configuration(
    config: dict[str, Any], configuration: str
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    blocks = [
        load_block(config, configuration, int(start), int(stop))
        for start, stop in config["lineage_blocks"]
    ]
    data = merge_blocks(blocks, configuration)
    nodes = np.asarray(config["nodes"], dtype=np.float64)
    node_time, neural = central_common_clock(data, nodes)
    bootstrap_contract = config["bootstrap"]
    bootstrap_reference, invalid_count = bootstrap_common_clock(
        data,
        nodes,
        replicates=int(bootstrap_contract["replicates"]),
        seed=int(bootstrap_contract["seed_by_configuration"][configuration]),
    )
    valid_mask = np.all(np.isfinite(bootstrap_reference), axis=1)
    valid_reference = bootstrap_reference[valid_mask]
    valid_count = int(np.count_nonzero(valid_mask))
    valid_fraction = valid_count / int(bootstrap_contract["replicates"])
    require(
        invalid_count == int(bootstrap_contract["replicates"]) - valid_count,
        f"inconsistent invalid-bootstrap accounting for {configuration}",
    )
    require(
        valid_fraction >= float(bootstrap_contract["minimum_valid_fraction"]),
        f"{configuration} valid bootstrap fraction {valid_fraction:.6f} is below the minimum",
    )
    neural_band = simultaneous_log_band(
        neural,
        valid_reference,
        confidence=float(bootstrap_contract["confidence"]),
    )
    neural_lower = neural_band.lower
    neural_upper = neural_band.upper

    proxy_point = frozen_proxy_points()[configuration]
    hierarchy = proxy_point.hierarchy
    proxy = np.asarray(
        [[proxy_point.kernel(level, node) for node in nodes] for level in range(len(hierarchy))],
        dtype=np.float64,
    )
    require(np.all(np.isfinite(proxy)) and np.all(proxy > 0.0), f"invalid frozen proxy for {configuration}")
    signed = np.log(proxy / neural[None, :])
    absolute = np.abs(signed)
    bootstrap_signed = np.log(proxy[None, :, :] / valid_reference[:, None, :])
    bootstrap_absolute = np.abs(bootstrap_signed)
    signed_lower, signed_upper = quantile_interval(
        bootstrap_signed, float(bootstrap_contract["confidence"])
    )
    absolute_lower, absolute_upper = quantile_interval(
        bootstrap_absolute, float(bootstrap_contract["confidence"])
    )

    sup_error = absolute.max(axis=1)
    mean_error = absolute.mean(axis=1)
    bootstrap_sup = bootstrap_absolute.max(axis=2)
    bootstrap_mean = bootstrap_absolute.mean(axis=2)
    sup_lower, sup_upper = quantile_interval(
        bootstrap_sup, float(bootstrap_contract["confidence"])
    )
    mean_lower, mean_upper = quantile_interval(
        bootstrap_mean, float(bootstrap_contract["confidence"])
    )

    nodewise_rows: list[dict[str, Any]] = []
    nodewise_transitions_json: list[dict[str, Any]] = []
    aggregate_rows: list[dict[str, Any]] = []
    for level, approximation in enumerate(hierarchy):
        label = f"M{level}"
        aggregate_rows.append(
            {
                "configuration": configuration,
                "level_index": level,
                "level_label": label,
                "level_name": approximation.name,
                "sup_absolute_log_error": float(sup_error[level]),
                "sup_ci99_lower": float(sup_lower[level]),
                "sup_ci99_upper": float(sup_upper[level]),
                "mean_absolute_log_error": float(mean_error[level]),
                "mean_ci99_lower": float(mean_lower[level]),
                "mean_ci99_upper": float(mean_upper[level]),
            }
        )
        for node_index, node in enumerate(nodes):
            if level == 0:
                node_transition = {
                    "previous_level": None,
                    "transition_margin": None,
                    "transition_margin_ci99_lower": None,
                    "transition_margin_ci99_upper": None,
                    "bootstrap_probability_margin_gt_zero": None,
                    "central_improves_vs_previous": None,
                }
            else:
                node_margin = float(
                    absolute[level - 1, node_index] - absolute[level, node_index]
                )
                bootstrap_node_margin = (
                    bootstrap_absolute[:, level - 1, node_index]
                    - bootstrap_absolute[:, level, node_index]
                )
                node_margin_lower, node_margin_upper = quantile_interval(
                    bootstrap_node_margin, float(bootstrap_contract["confidence"])
                )
                node_transition = {
                    "previous_level": f"M{level - 1}",
                    "transition_margin": node_margin,
                    "transition_margin_ci99_lower": float(node_margin_lower),
                    "transition_margin_ci99_upper": float(node_margin_upper),
                    "bootstrap_probability_margin_gt_zero": float(
                        np.mean(bootstrap_node_margin > 0.0)
                    ),
                    "central_improves_vs_previous": bool(node_margin > 0.0),
                }
                nodewise_transitions_json.append(
                    {
                        "node": float(node),
                        "from_level": f"M{level - 1}",
                        "to_level": label,
                        **{
                            key: value
                            for key, value in node_transition.items()
                            if key != "previous_level"
                        },
                    }
                )
            nodewise_rows.append(
                {
                    "configuration": configuration,
                    "level_index": level,
                    "level_label": label,
                    "level_name": approximation.name,
                    "node": float(node),
                    "proxy_kernel": float(proxy[level, node_index]),
                    "neural_reference": float(neural[node_index]),
                    "neural_ci99_lower": float(neural_lower[node_index]),
                    "neural_ci99_upper": float(neural_upper[node_index]),
                    "signed_log_error": float(signed[level, node_index]),
                    "signed_log_error_ci99_lower": float(signed_lower[level, node_index]),
                    "signed_log_error_ci99_upper": float(signed_upper[level, node_index]),
                    "absolute_log_error": float(absolute[level, node_index]),
                    "absolute_log_error_ci99_lower": float(absolute_lower[level, node_index]),
                    "absolute_log_error_ci99_upper": float(absolute_upper[level, node_index]),
                    **node_transition,
                }
            )

    transition_rows: list[dict[str, Any]] = []
    transitions_json: list[dict[str, Any]] = []
    for metric, central_values, bootstrap_values in (
        ("sup_absolute_log_error", sup_error, bootstrap_sup),
        ("mean_absolute_log_error", mean_error, bootstrap_mean),
    ):
        for level in range(1, len(hierarchy)):
            margin = float(central_values[level - 1] - central_values[level])
            bootstrap_margin = bootstrap_values[:, level - 1] - bootstrap_values[:, level]
            lower, upper = quantile_interval(
                bootstrap_margin, float(bootstrap_contract["confidence"])
            )
            record = {
                "configuration": configuration,
                "metric": metric,
                "from_level": f"M{level - 1}",
                "to_level": f"M{level}",
                "from_error": float(central_values[level - 1]),
                "to_error": float(central_values[level]),
                "central_margin": margin,
                "margin_ci99_lower": float(lower),
                "margin_ci99_upper": float(upper),
                "bootstrap_probability_margin_gt_zero": float(
                    np.mean(bootstrap_margin > 0.0)
                ),
                "central_improves": bool(margin > 0.0),
            }
            transition_rows.append(record)
            transitions_json.append(record)

    level_records = []
    for level, approximation in enumerate(hierarchy):
        level_records.append(
            {
                "level_index": level,
                "level_label": f"M{level}",
                "level_name": approximation.name,
                "side": approximation.side,
                "information_moments": approximation.information_moments,
                "proxy_kernel": proxy[level].tolist(),
                "signed_log_error": signed[level].tolist(),
                "absolute_log_error": absolute[level].tolist(),
                "sup_absolute_log_error": float(sup_error[level]),
                "sup_ci99": [float(sup_lower[level]), float(sup_upper[level])],
                "mean_absolute_log_error": float(mean_error[level]),
                "mean_ci99": [float(mean_lower[level]), float(mean_upper[level])],
            }
        )

    result = {
        "configuration": configuration,
        "engine_key": config["configurations"][configuration]["engine_key"],
        "width": int(config["width"]),
        "lineage_ids": data.lineage_ids.tolist(),
        "antithetic_lineages": len(data.lineage_ids),
        "physical_nodes": nodes.tolist(),
        "node_time": node_time.tolist(),
        "neural_reference": neural.tolist(),
        "neural_reference_ci99": {
            "lower": neural_lower.tolist(),
            "upper": neural_upper.tolist(),
            "kind": "studentized max-absolute-t simultaneous log band",
            "pointwise_log_standard_error": neural_band.pointwise_log_standard_error.tolist(),
            "simultaneous_critical_value": neural_band.simultaneous_critical_value,
        },
        "bootstrap": {
            "seed": int(bootstrap_contract["seed_by_configuration"][configuration]),
            "requested_replicates": int(bootstrap_contract["replicates"]),
            "valid_replicates": valid_count,
            "invalid_replicates": invalid_count,
            "valid_fraction": valid_fraction,
            "confidence": float(bootstrap_contract["confidence"]),
            "quantile_method": "linear",
            "resampling_unit": "whole_antithetic_lineage",
            "clock_rule": "recompute primitive-first ensemble mean-output clock in every resample",
        },
        "proxy_provenance": {
            "family": proxy_point.family.exact_record(),
            "physical_scale": str(proxy_point.physical_scale),
            "evaluation": "frozen accepted hierarchy in physical output coordinates",
        },
        "levels": level_records,
        "nodewise_transitions": nodewise_transitions_json,
        "transitions": transitions_json,
        "successive_improvement": {
            "all_central_sup_margins_positive": bool(np.all(np.diff(sup_error) < 0.0)),
            "all_central_mean_margins_positive": bool(np.all(np.diff(mean_error) < 0.0)),
            "interpretation": "empirical fixed-width comparison only; bootstrap intervals quantify lineage uncertainty",
        },
        "block_provenance": list(data.manifests),
        "execution_environment": data.environment,
    }
    return result, nodewise_rows, aggregate_rows, transition_rows


def write_csv_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    require(bool(rows), f"refusing to write empty CSV: {path}")
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0].keys()),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(temporary, path)


def import_plotting():
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise AnalysisInvalid("matplotlib is required to emit the registered plots") from exc
    return matplotlib, plt


def plot_curves(results: dict[str, dict[str, Any]], path: Path) -> str:
    matplotlib, plt = import_plotting()
    figure, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    for axis, configuration in zip(axes.flat, CONFIGURATION_ORDER, strict=True):
        result = results[configuration]
        nodes = np.asarray(result["physical_nodes"])
        neural = np.asarray(result["neural_reference"])
        lower = np.asarray(result["neural_reference_ci99"]["lower"])
        upper = np.asarray(result["neural_reference_ci99"]["upper"])
        axis.fill_between(
            nodes,
            lower,
            upper,
            color="black",
            alpha=0.15,
            label="neural 99% simultaneous band",
        )
        axis.plot(nodes, neural, "o-k", linewidth=2.0, label="neural n=4096")
        colors = plt.cm.viridis(np.linspace(0.08, 0.92, len(result["levels"])))
        for color, level in zip(colors, result["levels"], strict=True):
            axis.plot(
                nodes,
                np.asarray(level["proxy_kernel"]),
                marker="o",
                linewidth=1.2,
                color=color,
                label=level["level_label"],
            )
        axis.set_title(configuration)
        axis.set_xlabel("physical output y")
        axis.set_ylabel("effective kernel")
        axis.grid(alpha=0.25)
        axis.legend(fontsize=8, ncol=2)
    temporary = path.with_name(path.name + ".tmp.png")
    figure.savefig(temporary, dpi=180)
    plt.close(figure)
    os.replace(temporary, path)
    return matplotlib.__version__


def plot_aggregate(results: dict[str, dict[str, Any]], path: Path) -> None:
    _, plt = import_plotting()
    figure, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    for axis, configuration in zip(axes.flat, CONFIGURATION_ORDER, strict=True):
        levels = results[configuration]["levels"]
        x = np.arange(len(levels))
        for key, ci_key, label, color, marker in (
            ("sup_absolute_log_error", "sup_ci99", "sup |log error|", "tab:blue", "o"),
            ("mean_absolute_log_error", "mean_ci99", "mean |log error|", "tab:orange", "s"),
        ):
            values = np.asarray([level[key] for level in levels])
            intervals = np.asarray([level[ci_key] for level in levels])
            error = np.vstack((values - intervals[:, 0], intervals[:, 1] - values))
            error = np.maximum(error, 0.0)
            axis.errorbar(x, values, yerr=error, color=color, marker=marker, capsize=3, label=label)
        axis.set_xticks(x, [level["level_label"] for level in levels])
        axis.set_yscale("log")
        axis.set_title(configuration)
        axis.set_xlabel("accepted approximation level")
        axis.set_ylabel("absolute log error")
        axis.grid(alpha=0.25, which="both")
        axis.legend(fontsize=8)
    temporary = path.with_name(path.name + ".tmp.png")
    figure.savefig(temporary, dpi=180)
    plt.close(figure)
    os.replace(temporary, path)


def plot_transitions(results: dict[str, dict[str, Any]], path: Path) -> None:
    _, plt = import_plotting()
    figure, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    for axis, configuration in zip(axes.flat, CONFIGURATION_ORDER, strict=True):
        records = results[configuration]["transitions"]
        sup = [record for record in records if record["metric"] == "sup_absolute_log_error"]
        mean = [record for record in records if record["metric"] == "mean_absolute_log_error"]
        x = np.arange(len(sup), dtype=np.float64)
        for offset, subset, label, color, marker in (
            (-0.08, sup, "sup margin", "tab:blue", "o"),
            (0.08, mean, "mean margin", "tab:orange", "s"),
        ):
            values = np.asarray([record["central_margin"] for record in subset])
            lower = np.asarray([record["margin_ci99_lower"] for record in subset])
            upper = np.asarray([record["margin_ci99_upper"] for record in subset])
            error = np.maximum(np.vstack((values - lower, upper - values)), 0.0)
            axis.errorbar(x + offset, values, yerr=error, color=color, marker=marker, capsize=3, label=label)
        axis.axhline(0.0, color="black", linewidth=1.0)
        axis.set_xticks(x, [f"M{i}→M{i+1}" for i in range(len(sup))])
        axis.set_title(configuration)
        axis.set_xlabel("adjacent transition")
        axis.set_ylabel("previous error − next error")
        axis.grid(alpha=0.25)
        axis.legend(fontsize=8)
        for index, record in enumerate(sup):
            axis.annotate(
                f"p={record['bootstrap_probability_margin_gt_zero']:.3f}",
                (index - 0.08, record["central_margin"]),
                xytext=(0, 7),
                textcoords="offset points",
                ha="center",
                fontsize=7,
            )
    temporary = path.with_name(path.name + ".tmp.png")
    figure.savefig(temporary, dpi=180)
    plt.close(figure)
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=HERE)
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    config = read_json(CONFIG_PATH)
    validate_campaign_config(config)
    results_by_configuration: dict[str, dict[str, Any]] = {}
    nodewise_rows: list[dict[str, Any]] = []
    aggregate_rows: list[dict[str, Any]] = []
    transition_rows: list[dict[str, Any]] = []
    for configuration in CONFIGURATION_ORDER:
        result, nodewise, aggregate, transitions = analyze_configuration(
            config, configuration
        )
        results_by_configuration[configuration] = result
        nodewise_rows.extend(nodewise)
        aggregate_rows.extend(aggregate)
        transition_rows.extend(transitions)

    write_csv_atomic(output_dir / OUTPUT_FILES["nodewise_csv"], nodewise_rows)
    write_csv_atomic(output_dir / OUTPUT_FILES["aggregate_csv"], aggregate_rows)
    write_csv_atomic(output_dir / OUTPUT_FILES["transitions_csv"], transition_rows)
    matplotlib_version = plot_curves(
        results_by_configuration, output_dir / OUTPUT_FILES["curves_plot"]
    )
    plot_aggregate(results_by_configuration, output_dir / OUTPUT_FILES["aggregate_plot"])
    plot_transitions(results_by_configuration, output_dir / OUTPUT_FILES["transitions_plot"])

    payload = {
        "schema": "breadth-successive-n4096-analysis-result-v1",
        "status": "complete",
        "scope": config["scope"],
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "configuration_sha256": sha256_file(CONFIG_PATH),
        "analysis_source_sha256": sha256_file(Path(__file__)),
        "validated_fp64_source_lock_sha256": sha256_file(FP64_LOCK_PATH),
        "numpy_version": np.__version__,
        "matplotlib_version": matplotlib_version,
        "uncertainty_scope": "neural reference: 99% studentized simultaneous log band; proxy errors and transition margins: 99% whole-lineage pair-bootstrap percentile intervals; numerical-step and width uncertainty are not included",
        "error_metrics": {
            "nodewise": "abs(log(proxy_kernel/neural_reference))",
            "aggregate_sup": "max over the four physical nodes of nodewise absolute log error",
            "aggregate_mean": "mean over the four physical nodes of nodewise absolute log error",
            "transition_margin": "previous-level aggregate error minus next-level aggregate error; positive means improvement",
        },
        "configurations": results_by_configuration,
        "outputs": OUTPUT_FILES,
    }
    write_json_atomic(output_dir / OUTPUT_FILES["results_json"], payload)
    print(
        json.dumps(
            {
                "status": "complete",
                "results": str(output_dir / OUTPUT_FILES["results_json"]),
                "central_successive_improvement": {
                    key: value["successive_improvement"]
                    for key, value in results_by_configuration.items()
                },
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
