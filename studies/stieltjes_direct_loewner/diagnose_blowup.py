#!/usr/bin/env python3
"""Post-failure numerical validity diagnostic; not a replacement primary test."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np

import simulate_loewner as base


HERE = Path(__file__).resolve().parent
THRESHOLDS = np.array([10.0, 1.0e2, 1.0e4, 1.0e8, 1.0e12])
ESCAPE_CEILING = float(THRESHOLDS[-1])


def initial_quantities(state: base.State) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = state.a.shape[1]
    u2 = state.u * state.u
    z = np.einsum("bij,bj->bi", state.W, u2, optimize=True) / math.sqrt(n)
    f = np.mean(state.a * z * z, axis=1)
    q = (
        np.sum(state.a * state.a, axis=1)
        + np.sum(state.W * state.W, axis=(1, 2))
        + np.sum(state.u * state.u, axis=1)
    )
    k0, _ = base.observable_and_derivative(state)
    return f, q, k0


def max_component(state: base.State) -> np.ndarray:
    return np.maximum.reduce(
        (
            np.max(np.abs(state.a), axis=1),
            np.max(np.abs(state.W), axis=(1, 2)),
            np.max(np.abs(state.u), axis=1),
        )
    )


def zero_inactive(state: base.State, inactive: np.ndarray) -> None:
    state.a[inactive] = 0.0
    state.W[inactive] = 0.0
    state.u[inactive] = 0.0


def run_escape(width: int, pair_count: int, step: float) -> dict[str, np.ndarray]:
    state = base.generate_state(width, pair_count)
    f0, q0, k0 = initial_quantities(state)
    trajectories = 2 * pair_count
    crossing = np.full((trajectories, len(THRESHOLDS)), np.nan)
    alive = np.ones(trajectories, dtype=bool)
    alive_at_nodes = np.zeros((trajectories, len(base.Y_NODES)), dtype=bool)
    k_at_nodes = np.full((trajectories, len(base.Y_NODES)), np.nan)
    target_steps = np.rint(base.Y_NODES / step).astype(int)
    target_map = {int(s): j for j, s in enumerate(target_steps)}

    for s in range(1, int(target_steps[-1]) + 1):
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            state = base.rk4_step(state, step)
        amplitude = max_component(state)
        for j, threshold in enumerate(THRESHOLDS):
            hit = alive & np.isnan(crossing[:, j]) & (
                (~np.isfinite(amplitude)) | (amplitude >= threshold)
            )
            crossing[hit, j] = s * step
        escaped = alive & ((~np.isfinite(amplitude)) | (amplitude >= ESCAPE_CEILING))
        alive[escaped] = False
        if np.any(~alive):
            zero_inactive(state, ~alive)

        if s in target_map:
            j = target_map[s]
            alive_at_nodes[:, j] = alive
            kval, _ = base.observable_and_derivative(state)
            kval[~alive] = np.nan
            k_at_nodes[:, j] = kval

    return {
        "f0": f0,
        "q0": q0,
        "k0": k0,
        "crossing": crossing,
        "alive_at_nodes": alive_at_nodes,
        "k_at_nodes": k_at_nodes,
    }


def paired_alive(alive: np.ndarray) -> np.ndarray:
    return alive.reshape(alive.shape[0] // 2, 2, alive.shape[1]).all(axis=1)


def nan_quantiles(values: np.ndarray) -> dict[str, float | None]:
    finite = values[np.isfinite(values)]
    if len(finite) == 0:
        return {"min": None, "q25": None, "median": None, "q75": None, "max": None}
    return {
        "min": float(np.min(finite)),
        "q25": float(np.quantile(finite, 0.25)),
        "median": float(np.median(finite)),
        "q75": float(np.quantile(finite, 0.75)),
        "max": float(np.max(finite)),
    }


def summarize(data: dict[str, np.ndarray]) -> dict:
    positive = data["f0"] > 0
    pair_alive = paired_alive(data["alive_at_nodes"])
    return {
        "trajectory_alive_counts_by_y": data["alive_at_nodes"].sum(axis=0).tolist(),
        "pair_alive_counts_by_y": pair_alive.sum(axis=0).tolist(),
        "positive_f0_trajectory_count": int(positive.sum()),
        "escape_time_quantiles_all": nan_quantiles(data["crossing"][:, -1]),
        "escape_time_quantiles_positive_f0": nan_quantiles(
            data["crossing"][positive, -1]
        ),
        "threshold_crossing_counts": np.isfinite(data["crossing"]).sum(axis=0).tolist(),
        "thresholds": THRESHOLDS.tolist(),
    }


def write_rows(
    writer: csv.DictWriter, width: int, step: float, data: dict[str, np.ndarray]
) -> None:
    for trajectory in range(len(data["f0"])):
        row: dict[str, object] = {
            "width": width,
            "step": step,
            "pair": trajectory // 2,
            "a_sign": "+" if trajectory % 2 == 0 else "-",
            "f0": data["f0"][trajectory],
            "q0": data["q0"][trajectory],
            "k0": data["k0"][trajectory],
        }
        for j, threshold in enumerate(THRESHOLDS):
            row[f"cross_{threshold:g}"] = data["crossing"][trajectory, j]
        for j, y in enumerate(base.Y_NODES):
            row[f"alive_y{y:g}"] = int(data["alive_at_nodes"][trajectory, j])
            row[f"k_y{y:g}"] = data["k_at_nodes"][trajectory, j]
        writer.writerow(row)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=HERE / "runs/failure_diagnostic")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    command = " ".join(sys.argv)
    summary: dict[str, object] = {
        "status": "post_failure_numerical_diagnostic_not_primary_test",
        "command": command,
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
        "thresholds": THRESHOLDS.tolist(),
        "x_nodes": base.X_NODES.tolist(),
        "y_nodes": base.Y_NODES.tolist(),
        "main": {},
        "half_step_first_eight": {},
        "controls": {
            "two_atom": base.exact_atomic_control((10.0, 100.0), (0.6, 0.4)),
            "three_atom": base.exact_atomic_control(
                (5.0, 40.0, 160.0), (0.5, 0.3, 0.2)
            ),
        },
    }
    log_lines = [f"command: {command}"]
    fields = ["width", "step", "pair", "a_sign", "f0", "q0", "k0"]
    fields += [f"cross_{threshold:g}" for threshold in THRESHOLDS]
    for y in base.Y_NODES:
        fields += [f"alive_y{y:g}", f"k_y{y:g}"]

    csv_path = args.output / "trajectory_escape.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for width in base.WIDTHS:
            count = base.PAIR_COUNTS[width]
            print(f"START main width={width} pairs={count}", flush=True)
            main_data = run_escape(width, count, base.MAIN_STEP)
            main_summary = summarize(main_data)
            summary["main"][str(width)] = main_summary
            write_rows(writer, width, base.MAIN_STEP, main_data)
            np.savez_compressed(args.output / f"escape_main_width_{width}.npz", **main_data)
            line = f"main width={width} {json.dumps(main_summary, sort_keys=True)}"
            print(line, flush=True)
            log_lines.append(line)

            print(f"START half width={width} pairs={base.VALIDATION_PAIRS}", flush=True)
            half_data = run_escape(width, base.VALIDATION_PAIRS, base.HALF_STEP)
            half_summary = summarize(half_data)
            summary["half_step_first_eight"][str(width)] = half_summary
            write_rows(writer, width, base.HALF_STEP, half_data)
            np.savez_compressed(args.output / f"escape_half_width_{width}.npz", **half_data)
            line = f"half width={width} {json.dumps(half_summary, sort_keys=True)}"
            print(line, flush=True)
            log_lines.append(line)

    summary_path = args.output / "failure_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    log_path = args.output / "failure_run.log"
    log_path.write_text("\n".join(log_lines) + "\n")
    artifacts = [csv_path, summary_path, log_path]
    artifacts += sorted(args.output.glob("escape_*.npz"))
    manifest = {
        path.name: {"sha256": file_sha256(path), "bytes": path.stat().st_size}
        for path in artifacts
    }
    for source in (Path(__file__), Path(base.__file__), HERE / "protocol.md"):
        manifest["source/" + source.name] = {
            "sha256": file_sha256(source), "bytes": source.stat().st_size
        }
    (args.output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )
    print("COMPLETE", flush=True)


if __name__ == "__main__":
    main()
