#!/usr/bin/env python3
"""PDE-only numerical decision, run before any dense reference is generated."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results" / "generalization"
PROTOCOL = json.loads(
    (ROOT / "protocol" / "generalization_protocol.json").read_text()
)


def metadata(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as archive:
        return json.loads(str(archive["metadata_json"]))


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def find_one(directory: str, case_id: str, **conditions) -> Path:
    matches = []
    for path in sorted((RESULTS / directory).glob(f"pde_{case_id}_*.npz")):
        meta = metadata(path)
        if all(meta.get(key) == value for key, value in conditions.items()):
            matches.append(path)
    if len(matches) != 1:
        raise RuntimeError(
            f"{directory}/{case_id}/{conditions}: expected one, got {len(matches)}"
        )
    return matches[0]


def load(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as archive:
        return {key: archive[key].copy() for key in archive.files}


def align_depth(values: np.ndarray, target_nodes: int) -> np.ndarray:
    source_nodes = values.shape[1] - 1
    target_depth = np.linspace(0.0, 1.0, target_nodes + 1)
    source_depth = np.linspace(0.0, 1.0, source_nodes + 1)
    if source_nodes % target_nodes == 0:
        return values[:, :: source_nodes // target_nodes]
    flat = values.reshape(values.shape[0], source_nodes + 1, -1)
    result = np.empty((values.shape[0], target_nodes + 1, flat.shape[-1]))
    for time_index in range(values.shape[0]):
        for coordinate in range(flat.shape[-1]):
            result[time_index, :, coordinate] = np.interp(
                target_depth,
                source_depth,
                flat[time_index, :, coordinate],
            )
    return result.reshape(
        values.shape[0], target_nodes + 1, *values.shape[2:]
    )


def discrepancy(primary: dict, other: dict) -> dict:
    if not np.array_equal(primary["times"], other["times"]):
        raise RuntimeError("PDE audit time grids differ")
    target_nodes = primary["grams"].shape[1] - 1
    other_grams = align_depth(other["grams"], target_nodes)
    delta_gp = primary["grams"] - primary["grams"][0:1]
    delta_go = other_grams - other_grams[0:1]
    delta_fp = primary["f"] - primary["f"][0:1]
    delta_fo = other["f"] - other["f"][0:1]
    gp_norm = np.linalg.norm(delta_gp.reshape(*delta_gp.shape[:2], -1), axis=-1)
    go_norm = np.linalg.norm(delta_go.reshape(*delta_go.shape[:2], -1), axis=-1)
    gram_scale = max(float(np.max(gp_norm)), float(np.max(go_norm)), 0.05)
    fp_norm = np.linalg.norm(delta_fp, axis=-1)
    fo_norm = np.linalg.norm(delta_fo, axis=-1)
    y = np.asarray(json.loads(str(primary["metadata_json"]))["y"])
    output_scale = max(
        float(np.linalg.norm(y)),
        float(np.max(fp_norm)),
        float(np.max(fo_norm)),
        0.1,
    )
    gram_difference = np.linalg.norm(
        (delta_gp - delta_go).reshape(*delta_gp.shape[:2], -1),
        axis=-1,
    )
    output_difference = np.linalg.norm(delta_fp - delta_fo, axis=-1)
    return {
        "gram_error": float(np.max(gram_difference)),
        "gram_scale": gram_scale,
        "gram_normalized": float(np.max(gram_difference) / gram_scale),
        "output_error": float(np.max(output_difference)),
        "output_scale": output_scale,
        "output_normalized": float(np.max(output_difference) / output_scale),
    }


def identity_checks(primary: dict) -> dict:
    meta = json.loads(str(primary["metadata_json"]))
    y = np.asarray(meta["y"])
    e = primary["f"] - y
    energy = np.einsum("ti,tij,tj->t", e, primary["theta"], e)
    defect = np.max(np.abs(primary["loss_dot"] + energy))
    return {
        "finite": bool(
            all(
                np.all(np.isfinite(primary[key]))
                for key in (
                    "f",
                    "loss",
                    "grams",
                    "theta",
                    "theta_min",
                    "loss_dot",
                    "projected_energy",
                )
            )
        ),
        "loss_energy_identity_defect": float(defect),
        "minimum_theta_eigenvalue": float(np.min(primary["theta_min"])),
        "minimum_projected_energy": float(
            np.min(primary["projected_energy"])
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=RESULTS / "pde_numerical_decision.json")
    args = parser.parse_args()
    fixed = PROTOCOL["fixed_pde"]
    primary: dict[str, dict] = {}
    scramble: dict[str, dict] = {}
    identity: dict[str, dict] = {}
    input_files: dict[str, str] = {}

    def record_input(path: Path) -> None:
        input_files[os.fspath(path.relative_to(ROOT))] = file_sha256(path)

    for case_id in PROTOCOL["active_case_ids"]:
        primary_path = find_one(
            "pde_primary",
            case_id,
            start_time=0.0,
            end_time=8.0,
            quadrature_seed=fixed["primary_seed"],
            quadrature="hybrid",
            depth_nodes_N=16,
            fast_quadrature_R=128,
            dt=0.02,
        )
        scramble_path = find_one(
            "pde_scramble",
            case_id,
            start_time=0.0,
            end_time=8.0,
            quadrature_seed=fixed["second_scramble_seed"],
            quadrature="hybrid",
            depth_nodes_N=16,
            fast_quadrature_R=128,
            dt=0.02,
        )
        record_input(primary_path)
        record_input(scramble_path)
        primary[case_id] = load(primary_path)
        scramble[case_id] = discrepancy(
            primary[case_id], load(scramble_path)
        )
        identity[case_id] = identity_checks(primary[case_id])

    qmc = {}
    for case_id in PROTOCOL["numerical_audits"]["qmc_crosscheck_cases"]:
        path = find_one(
            "pde_audits",
            case_id,
            start_time=0.0,
            end_time=8.0,
            quadrature_seed=fixed["primary_seed"],
            quadrature="sobol",
            depth_nodes_N=16,
            base_quadrature_M=256,
            fast_quadrature_R=128,
            dt=0.02,
        )
        record_input(path)
        qmc[case_id] = discrepancy(primary[case_id], load(path))
    depth = {}
    for case_id in PROTOCOL["numerical_audits"]["N32_cases"]:
        path = find_one(
            "pde_audits",
            case_id,
            start_time=0.0,
            end_time=8.0,
            quadrature_seed=fixed["primary_seed"],
            quadrature="hybrid",
            depth_nodes_N=32,
            fast_quadrature_R=128,
            dt=0.02,
        )
        record_input(path)
        depth[case_id] = discrepancy(primary[case_id], load(path))
    time_step = {}
    for case_id in PROTOCOL["numerical_audits"]["dt001_cases"]:
        path = find_one(
            "pde_audits",
            case_id,
            start_time=0.0,
            end_time=8.0,
            quadrature_seed=fixed["primary_seed"],
            quadrature="hybrid",
            depth_nodes_N=16,
            fast_quadrature_R=128,
            dt=0.01,
        )
        record_input(path)
        time_step[case_id] = discrepancy(primary[case_id], load(path))

    scramble_tolerance = PROTOCOL["numerical_audits"][
        "scramble_tolerance_fraction_of_motion"
    ]
    r256_required = [
        case_id
        for case_id in PROTOCOL["active_case_ids"]
        if max(
            scramble[case_id]["gram_normalized"],
            scramble[case_id]["output_normalized"],
        )
        > scramble_tolerance
    ]
    dynamics = json.loads(
        (ROOT / "protocol" / "FROZEN_DYNAMICS_MANIFEST.json").read_text()
    )["aggregate_sha256"]
    result = {
        "status": "PDE-only decision made before dense-reference generation",
        "dynamics_sha256": dynamics,
        "analysis_source_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "input_files": dict(sorted(input_files.items())),
        "scramble_tolerance": scramble_tolerance,
        "r256_required": r256_required,
        "scramble": scramble,
        "qmc": qmc,
        "depth": depth,
        "time_step": time_step,
        "identity": identity,
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists() and args.output.read_text() != encoded:
        raise RuntimeError("refusing to overwrite a different PDE decision")
    args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
