#!/usr/bin/env python3
"""Reproduce the preregistered sparse PDE/dense experiment grid."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, os.fspath(ROOT / "src"))

import numpy as np  # noqa: E402
from study_cases import load_case  # noqa: E402

PROTOCOL = json.loads(
    (ROOT / "protocol" / "generalization_protocol.json").read_text()
)
REGISTRY = ROOT / "protocol" / "cases.json"
RESULTS = ROOT / "results" / "generalization"
PYTHON = sys.executable


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_frozen() -> str:
    manifest_path = ROOT / "protocol" / "FROZEN_DYNAMICS_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text())
    for relative, expected in manifest["files"].items():
        observed = _sha256(ROOT / relative)
        if observed != expected:
            raise RuntimeError(f"frozen source mismatch: {relative}")
    aggregate = hashlib.sha256(
        json.dumps(
            manifest["files"], sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    if aggregate != manifest.get("aggregate_sha256"):
        raise RuntimeError("frozen source aggregate mismatch")
    return manifest["aggregate_sha256"]


def _run(command: list[str], label: str, env: dict[str, str]) -> str:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode:
        raise RuntimeError(
            f"{label} failed with code {completed.returncode}\n"
            f"{completed.stdout}"
        )
    last = completed.stdout.strip().splitlines()
    return f"{label}: {last[-1] if last else 'complete'}"


def _parallel(
    jobs: list[tuple[list[str], str]],
    parallel_jobs: int,
) -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = os.fspath(ROOT / "src")
    env["OPENBLAS_NUM_THREADS"] = "1"
    env["OMP_NUM_THREADS"] = "1"
    with ThreadPoolExecutor(max_workers=parallel_jobs) as pool:
        futures = {
            pool.submit(_run, command, label, env): label
            for command, label in jobs
        }
        for future in as_completed(futures):
            print(future.result(), flush=True)


def _pde_base(case_id: str, output: Path) -> list[str]:
    fixed = PROTOCOL["fixed_pde"]
    return [
        PYTHON,
        "run_pde.py",
        "--case-registry",
        os.fspath(REGISTRY),
        "--case-id",
        case_id,
        "--quadrature",
        fixed["quadrature"],
        "--P",
        str(fixed["basis_size_P"]),
        "--N",
        str(fixed["depth_nodes_N"]),
        "--base-order",
        str(fixed["base_order"]),
        "--R",
        str(fixed["fast_points_R"]),
        "--dt",
        str(fixed["dt"]),
        "--sample-dt",
        str(fixed["sample_dt"]),
        "--integrator",
        fixed["integrator"],
        "--output-dir",
        os.fspath(output),
    ]


def pde_primary(parallel_jobs: int) -> None:
    output = RESULTS / "pde_primary"
    jobs = []
    for case_id in PROTOCOL["active_case_ids"]:
        command = _pde_base(case_id, output)
        command += [
            "--seed",
            str(PROTOCOL["fixed_pde"]["primary_seed"]),
            "--duration",
            str(PROTOCOL["fixed_pde"]["initial_horizon"]),
        ]
        jobs.append((command, f"primary {case_id}"))
    _parallel(jobs, parallel_jobs)


def pde_scramble(parallel_jobs: int) -> None:
    output = RESULTS / "pde_scramble"
    jobs = []
    for case_id in PROTOCOL["active_case_ids"]:
        command = _pde_base(case_id, output)
        command += [
            "--seed",
            str(PROTOCOL["fixed_pde"]["second_scramble_seed"]),
            "--duration",
            str(PROTOCOL["fixed_pde"]["initial_horizon"]),
        ]
        jobs.append((command, f"scramble {case_id}"))
    _parallel(jobs, parallel_jobs)


def _single_match(pattern: str) -> Path:
    matches = sorted(ROOT.glob(pattern))
    if len(matches) != 1:
        raise RuntimeError(f"expected one match for {pattern}, got {len(matches)}")
    return matches[0]


def _metadata(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as archive:
        return json.loads(str(archive["metadata_json"]))


def _find_pde(
    directory: Path,
    case_id: str,
    *,
    start_time: float,
    end_time: float,
    seed: int,
    quadrature: str = "hybrid",
    N: int = 16,
    R: int = 128,
    dt: float = 0.02,
) -> Path:
    matches = []
    for path in sorted(directory.glob(f"pde_{case_id}_*.npz")):
        meta = _metadata(path)
        if (
            meta.get("case_id") == case_id
            and meta.get("start_time") == start_time
            and meta.get("end_time") == end_time
            and meta.get("quadrature_seed") == seed
            and meta.get("quadrature") == quadrature
            and meta.get("depth_nodes_N") == N
            and meta.get("fast_quadrature_R") == R
            and meta.get("dt") == dt
        ):
            matches.append(path)
    if len(matches) != 1:
        raise RuntimeError(
            f"expected one PDE archive for {case_id} "
            f"{start_time}->{end_time}, got {len(matches)}"
        )
    return matches[0]


def pde_continue(parallel_jobs: int) -> None:
    output = RESULTS / "pde_primary"
    fixed = PROTOCOL["fixed_pde"]
    continuation = (
        fixed["plateau_confirmation_horizon"] - fixed["initial_horizon"]
    )
    jobs = []
    for case_id in PROTOCOL["active_case_ids"]:
        source = _find_pde(
            output,
            case_id,
            start_time=0.0,
            end_time=fixed["initial_horizon"],
            seed=fixed["primary_seed"],
        )
        command = _pde_base(case_id, output)
        command += [
            "--seed",
            str(fixed["primary_seed"]),
            "--duration",
            str(continuation),
            "--restart-from",
            os.fspath(source),
        ]
        jobs.append((command, f"continuation {case_id}"))
    _parallel(jobs, parallel_jobs)


def pde_audits(parallel_jobs: int) -> None:
    output = RESULTS / "pde_audits"
    fixed = PROTOCOL["fixed_pde"]
    jobs: list[tuple[list[str], str]] = []
    for case_id in PROTOCOL["numerical_audits"]["qmc_crosscheck_cases"]:
        command = [
            PYTHON,
            "run_pde.py",
            "--case-registry",
            os.fspath(REGISTRY),
            "--case-id",
            case_id,
            "--quadrature",
            "sobol",
            "--P",
            "5",
            "--N",
            "16",
            "--M",
            "256",
            "--R",
            "128",
            "--seed",
            str(fixed["primary_seed"]),
            "--duration",
            "8",
            "--dt",
            "0.02",
            "--sample-dt",
            "0.04",
            "--output-dir",
            os.fspath(output),
        ]
        jobs.append((command, f"QMC {case_id}"))
    for case_id in PROTOCOL["numerical_audits"]["N32_cases"]:
        command = _pde_base(case_id, output)
        n_index = command.index("--N") + 1
        command[n_index] = "32"
        command += [
            "--seed",
            str(fixed["primary_seed"]),
            "--duration",
            "8",
        ]
        jobs.append((command, f"N32 {case_id}"))
    for case_id in PROTOCOL["numerical_audits"]["dt001_cases"]:
        command = _pde_base(case_id, output)
        dt_index = command.index("--dt") + 1
        command[dt_index] = "0.01"
        command += [
            "--seed",
            str(fixed["primary_seed"]),
            "--duration",
            "8",
        ]
        jobs.append((command, f"dt001 {case_id}"))
    _parallel(jobs, parallel_jobs)


def pde_r256(case_ids: list[str], parallel_jobs: int) -> None:
    unknown = sorted(set(case_ids).difference(PROTOCOL["active_case_ids"]))
    if unknown:
        raise ValueError(f"unknown fallback case IDs: {unknown}")
    output = RESULTS / "pde_fallback"
    fixed = PROTOCOL["fixed_pde"]
    jobs = []
    for case_id in case_ids:
        command = _pde_base(case_id, output)
        r_index = command.index("--R") + 1
        command[r_index] = str(
            PROTOCOL["numerical_audits"]["fallback_fast_points_R"]
        )
        command += [
            "--seed",
            str(fixed["primary_seed"]),
            "--duration",
            str(fixed["initial_horizon"]),
        ]
        jobs.append((command, f"R256 {case_id}"))
    _parallel(jobs, parallel_jobs)


def _dense_jobs(
    case_ids: list[str],
    tier: dict,
    output_name: str,
    dense_workers: int,
) -> list[tuple[list[str], str]]:
    jobs = []
    blocks = tier.get("seed_blocks")
    if blocks is None:
        blocks = [[tier["seed_start"], tier["ensemble_members"]]]
    for case_id in case_ids:
        for block_index, (seed_start, seeds) in enumerate(blocks):
            command = [
                PYTHON,
                "run_exact_reference.py",
                "--case-registry",
                os.fspath(REGISTRY),
                "--case-id",
                case_id,
                "--n",
                str(tier["width_n"]),
                "--depth",
                str(tier["depth_L"]),
                "--seeds",
                str(seeds),
                "--seed-start",
                str(seed_start),
                "--workers",
                str(dense_workers),
                "--duration",
                str(tier["horizon"]),
                "--dt",
                str(tier["dt"]),
                "--sample-dt",
                str(tier["sample_dt"]),
                "--output-dir",
                os.fspath(RESULTS / output_name),
                "--pde-seal",
                os.fspath(RESULTS / "PDE_STAGE_SEAL.json"),
            ]
            jobs.append((command, f"{output_name} {case_id} block{block_index}"))
    return jobs


def _require_pde_seal() -> None:
    seal = RESULTS / "PDE_STAGE_SEAL.json"
    if not seal.exists():
        raise RuntimeError("dense stages require protocol/run_grid.py seal-pde")
    record = json.loads(seal.read_text())
    if record["dynamics_sha256"] != verify_frozen():
        raise RuntimeError("PDE seal belongs to different frozen dynamics")
    if record["run_grid_sha256"] != _sha256(Path(__file__)):
        raise RuntimeError("PDE seal belongs to a different execution runner")
    for relative, expected in record["files"].items():
        path = ROOT / relative
        if not path.exists() or _sha256(path) != expected:
            raise RuntimeError(f"sealed PDE file mismatch: {relative}")


def dense_stage(mode: str, parallel_jobs: int, dense_workers: int) -> None:
    _require_pde_seal()
    if mode == "dense-screen":
        tier = PROTOCOL["screening_reference"]
        cases = PROTOCOL["active_case_ids"]
        output = "dense_screen"
    elif mode == "dense-confirm":
        tier = PROTOCOL["heldout_confirmation"]
        cases = tier["case_ids"]
        output = "dense_confirm"
    else:
        tier = PROTOCOL["depth_diagnostic"]
        cases = tier["case_ids"]
        output = "dense_depth"
    _parallel(
        _dense_jobs(cases, tier, output, dense_workers),
        parallel_jobs,
    )


def _find_dense(
    directory: Path,
    case_id: str,
    *,
    n: int,
    depth: int,
    seeds: int,
    seed_start: int,
    duration: float,
) -> Path:
    matches = []
    for path in sorted(directory.glob(f"exact_{case_id}_*.npz")):
        meta = _metadata(path)
        if (
            meta.get("case_id") == case_id
            and meta.get("n") == n
            and meta.get("depth") == depth
            and meta.get("seeds") == seeds
            and meta.get("seed_start") == seed_start
            and meta.get("duration") == duration
        ):
            matches.append(path)
    if len(matches) != 1:
        raise RuntimeError(
            f"expected one dense archive for {directory.name}/{case_id}/"
            f"n{n}/L{depth}/S{seeds}/seed{seed_start}, got {len(matches)}"
        )
    return matches[0]


def _validate_dense_archive(
    path: Path,
    case_id: str,
    tier: dict,
    seed_start: int,
    seeds: int,
    pde_seal_sha256: str,
    dynamics_sha256: str,
) -> None:
    case = load_case(REGISTRY, case_id)
    with np.load(path, allow_pickle=False) as archive:
        required = {"times", "seeds", "f", "grams", "theta", "metadata_json"}
        if not required.issubset(archive.files):
            raise RuntimeError(f"incomplete dense schema: {path}")
        meta = json.loads(str(archive["metadata_json"]))
        expected = {
            "case_id": case_id,
            "case_sha256": case.case_sha256,
            "registry_sha256": case.registry_sha256,
            "X": case.X.tolist(),
            "y": case.y.tolist(),
            "activation": case.activation,
            "sigma_w": case.sigma_w,
            "A": case.A,
            "gamma": case.gamma,
            "n": tier["width_n"],
            "depth": tier["depth_L"],
            "seeds": seeds,
            "seed_start": seed_start,
            "duration": tier["horizon"],
            "dt": tier["dt"],
            "sample_dt": tier["sample_dt"],
            "pde_seal_sha256": pde_seal_sha256,
            "dynamics_sha256": dynamics_sha256,
        }
        for key, value in expected.items():
            if meta.get(key) != value:
                raise RuntimeError(
                    f"{path.name}: dense metadata mismatch for {key}"
                )
        expected_seeds = np.arange(seed_start, seed_start + seeds)
        if not np.array_equal(archive["seeds"], expected_seeds):
            raise RuntimeError(f"{path.name}: exact seed vector mismatch")
        scientific_config = {
            "case_sha256": case.case_sha256,
            "registry_sha256": case.registry_sha256,
            "n": tier["width_n"],
            "depth": tier["depth_L"],
            "seed_start": seed_start,
            "seeds": seeds,
            "seed_ids": expected_seeds.tolist(),
            "duration": tier["horizon"],
            "dt": tier["dt"],
            "sample_dt": tier["sample_dt"],
            "sigma_w": case.sigma_w,
            "A": case.A,
            "gamma": case.gamma,
            "activation": case.activation,
            "X": case.X.tolist(),
            "y": case.y.tolist(),
            "pde_seal_sha256": pde_seal_sha256,
            "dynamics_sha256": dynamics_sha256,
        }
        scientific_hash = hashlib.sha256(
            json.dumps(
                scientific_config,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
        if meta.get("scientific_config_sha256") != scientific_hash:
            raise RuntimeError(
                f"{path.name}: scientific configuration hash mismatch"
            )
        times = archive["times"]
        expected_times = (
            np.arange(int(round(tier["horizon"] / tier["sample_dt"])) + 1)
            * tier["sample_dt"]
        )
        if not np.array_equal(times, expected_times):
            raise RuntimeError(f"{path.name}: time grid mismatch")
        m = case.y.size
        if archive["f"].shape != (seeds, times.size, m):
            raise RuntimeError(f"{path.name}: output shape mismatch")
        if archive["grams"].shape != (
            seeds,
            times.size,
            tier["depth_L"] + 1,
            m,
            m,
        ):
            raise RuntimeError(f"{path.name}: Gram shape mismatch")
        if archive["theta"].shape != (seeds, times.size, m, m):
            raise RuntimeError(f"{path.name}: theta shape mismatch")
        for key in ("times", "f", "grams", "theta"):
            if not np.all(np.isfinite(archive[key])):
                raise RuntimeError(f"{path.name}: nonfinite values in {key}")


def seal_dense() -> None:
    _require_pde_seal()
    pde_seal_path = RESULTS / "PDE_STAGE_SEAL.json"
    pde_seal_sha256 = _sha256(pde_seal_path)
    dynamics = verify_frozen()
    records: list[tuple[Path, str, dict, int, int]] = []
    tiers = (
        (
            "dense_screen",
            PROTOCOL["active_case_ids"],
            PROTOCOL["screening_reference"],
        ),
        (
            "dense_confirm",
            PROTOCOL["heldout_confirmation"]["case_ids"],
            PROTOCOL["heldout_confirmation"],
        ),
        (
            "dense_depth",
            PROTOCOL["depth_diagnostic"]["case_ids"],
            PROTOCOL["depth_diagnostic"],
        ),
    )
    for directory_name, case_ids, tier in tiers:
        blocks = tier.get(
            "seed_blocks",
            [[tier["seed_start"], tier["ensemble_members"]]],
        )
        for case_id in case_ids:
            for seed_start, seeds in blocks:
                path = _find_dense(
                    RESULTS / directory_name,
                    case_id,
                    n=tier["width_n"],
                    depth=tier["depth_L"],
                    seeds=seeds,
                    seed_start=seed_start,
                    duration=tier["horizon"],
                )
                records.append(
                    (path, case_id, tier, seed_start, seeds)
                )
    for path, case_id, tier, seed_start, seeds in records:
        _validate_dense_archive(
            path,
            case_id,
            tier,
            seed_start,
            seeds,
            pde_seal_sha256,
            dynamics,
        )
    actual = {
        path
        for directory in ("dense_screen", "dense_confirm", "dense_depth")
        for path in (RESULTS / directory).glob("*.npz")
    }
    expected = {record[0] for record in records}
    if actual != expected:
        raise RuntimeError("dense archive set contains missing or extra files")
    record = {
        "dynamics_sha256": dynamics,
        "run_grid_sha256": _sha256(Path(__file__)),
        "pde_seal_sha256": pde_seal_sha256,
        "files": {
            os.fspath(path.relative_to(ROOT)): _sha256(path)
            for path in sorted(expected)
        },
        "file_count": len(expected),
    }
    encoded = json.dumps(record, indent=2, sort_keys=True) + "\n"
    seal = RESULTS / "DENSE_STAGE_SEAL.json"
    if seal.exists() and seal.read_text() != encoded:
        raise RuntimeError("refusing to overwrite a different dense stage seal")
    seal.write_text(encoded)
    print(encoded, end="")


def _validate_pde_archive(path: Path, expected: dict) -> None:
    case = load_case(REGISTRY, expected["case_id"])
    with np.load(path, allow_pickle=False) as archive:
        required = {
            "times",
            "f",
            "loss",
            "grams",
            "theta",
            "theta_min",
            "residual_norm",
            "loss_dot",
            "projected_energy",
            "final_B",
            "final_a",
            "final_c",
            "metadata_json",
        }
        if not required.issubset(archive.files):
            raise RuntimeError(f"incomplete PDE schema: {path}")
        meta = json.loads(str(archive["metadata_json"]))
        for key, value in expected.items():
            if meta.get(key) != value:
                raise RuntimeError(
                    f"{path.name}: {key}={meta.get(key)!r}, expected {value!r}"
                )
        for key, value in (
            ("case_sha256", case.case_sha256),
            ("registry_sha256", case.registry_sha256),
            ("activation", case.activation),
            ("X", case.X.tolist()),
            ("y", case.y.tolist()),
            ("sigma_w", case.sigma_w),
            ("A", case.A),
            ("gamma", case.gamma),
            ("basis_size_P", 5),
            ("integrator", "rk4"),
            (
                "duration",
                expected["end_time"] - expected["start_time"],
            ),
        ):
            if meta.get(key) != value:
                raise RuntimeError(f"{path.name}: case provenance mismatch for {key}")
        times = archive["times"]
        sample_count = int(
            round(
                (expected["end_time"] - expected["start_time"])
                / expected["sample_dt"]
            )
        ) + 1
        expected_times = (
            expected["start_time"]
            + np.arange(sample_count) * expected["sample_dt"]
        )
        if not np.array_equal(times, expected_times):
            raise RuntimeError(f"{path.name}: stored time grid mismatch")
        scientific_config = {
            "static_compiler_sha256": meta["static_compiler_sha256"],
            "integrator": "rk4",
            "duration": expected["end_time"] - expected["start_time"],
            "start_time": expected["start_time"],
            "end_time": expected["end_time"],
            "dt": expected["dt"],
            "sample_dt": expected["sample_dt"],
            "restart_source_sha256": meta.get("restart_source_sha256"),
        }
        scientific_hash = hashlib.sha256(
            json.dumps(
                scientific_config,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
        if meta.get("scientific_config_sha256") != scientific_hash:
            raise RuntimeError(
                f"{path.name}: scientific configuration hash mismatch"
            )
        if archive["f"].shape != (times.size, case.y.size):
            raise RuntimeError(f"{path.name}: output shape mismatch")
        if archive["grams"].shape != (
            times.size,
            expected["depth_nodes_N"] + 1,
            case.y.size,
            case.y.size,
        ):
            raise RuntimeError(f"{path.name}: Gram shape mismatch")
        scalar_shapes = {
            "loss": (times.size,),
            "theta_min": (times.size,),
            "residual_norm": (times.size,),
            "loss_dot": (times.size,),
        }
        for key, shape in scalar_shapes.items():
            if archive[key].shape != shape:
                raise RuntimeError(f"{path.name}: {key} shape mismatch")
        if archive["theta"].shape != (
            times.size,
            case.y.size,
            case.y.size,
        ):
            raise RuntimeError(f"{path.name}: theta shape mismatch")
        if archive["projected_energy"].shape != (
            times.size,
            expected["depth_nodes_N"],
            case.y.size,
        ):
            raise RuntimeError(
                f"{path.name}: projected-energy shape mismatch"
            )
        base_points = expected["base_quadrature_M"]
        fast_points = expected["fast_quadrature_R"]
        if archive["final_B"].shape != (base_points, case.X.shape[0]):
            raise RuntimeError(f"{path.name}: final_B shape mismatch")
        if archive["final_a"].shape != (base_points,):
            raise RuntimeError(f"{path.name}: final_a shape mismatch")
        if archive["final_c"].shape != (
            expected["depth_nodes_N"],
            base_points,
            fast_points,
            5,
        ):
            raise RuntimeError(f"{path.name}: final_c shape mismatch")
        for key in required.difference({"metadata_json"}):
            if not np.all(np.isfinite(archive[key])):
                raise RuntimeError(f"{path.name}: nonfinite values in {key}")


def seal_pde() -> None:
    dynamics = verify_frozen()
    fixed = PROTOCOL["fixed_pde"]
    files: dict[str, str] = {}
    seen: set[tuple] = set()
    expected_records: list[tuple[Path, dict]] = []
    primary_dir = RESULTS / "pde_primary"
    for case_id in PROTOCOL["active_case_ids"]:
        first = _find_pde(
            primary_dir,
            case_id,
            start_time=0.0,
            end_time=8.0,
            seed=fixed["primary_seed"],
        )
        second = _find_pde(
            primary_dir,
            case_id,
            start_time=8.0,
            end_time=fixed["plateau_confirmation_horizon"],
            seed=fixed["primary_seed"],
        )
        expected_records.extend(
            [
                (
                    first,
                    {
                        "case_id": case_id,
                        "start_time": 0.0,
                        "end_time": 8.0,
                        "quadrature_seed": fixed["primary_seed"],
                        "quadrature": "hybrid",
                        "depth_nodes_N": 16,
                        "base_quadrature_M": 81,
                        "fast_quadrature_R": 128,
                        "dt": 0.02,
                        "sample_dt": 0.04,
                    },
                ),
                (
                    second,
                    {
                        "case_id": case_id,
                        "start_time": 8.0,
                        "end_time": fixed["plateau_confirmation_horizon"],
                        "quadrature_seed": fixed["primary_seed"],
                        "quadrature": "hybrid",
                        "depth_nodes_N": 16,
                        "base_quadrature_M": 81,
                        "fast_quadrature_R": 128,
                        "dt": 0.02,
                        "sample_dt": 0.04,
                    },
                ),
            ]
        )
        if _metadata(second)["restart_source_sha256"] != _sha256(first):
            raise RuntimeError(f"{case_id}: continuation source hash mismatch")
    for case_id in PROTOCOL["active_case_ids"]:
        path = _find_pde(
            RESULTS / "pde_scramble",
            case_id,
            start_time=0.0,
            end_time=8.0,
            seed=fixed["second_scramble_seed"],
        )
        expected_records.append(
            (
                path,
                {
                    "case_id": case_id,
                    "start_time": 0.0,
                    "end_time": 8.0,
                    "quadrature_seed": fixed["second_scramble_seed"],
                    "quadrature": "hybrid",
                    "depth_nodes_N": 16,
                    "base_quadrature_M": 81,
                    "fast_quadrature_R": 128,
                    "dt": 0.02,
                    "sample_dt": 0.04,
                },
            )
        )
    numerical_decision_path = RESULTS / "pde_numerical_decision.json"
    if not numerical_decision_path.exists():
        raise RuntimeError(
            "seal-pde requires the preregistered PDE-only numerical decision"
        )
    numerical_decision = json.loads(numerical_decision_path.read_text())
    if numerical_decision.get("dynamics_sha256") != dynamics:
        raise RuntimeError("PDE numerical decision has the wrong source hash")
    if numerical_decision.get("analysis_source_sha256") != _sha256(
        ROOT / "pde_precheck.py"
    ):
        raise RuntimeError("PDE numerical decision uses the wrong precheck source")
    recorded_inputs = numerical_decision.get("input_files")
    if not isinstance(recorded_inputs, dict):
        raise RuntimeError("PDE numerical decision lacks input-file hashes")
    for relative, expected_sha in recorded_inputs.items():
        input_path = ROOT / relative
        if not input_path.is_file() or _sha256(input_path) != expected_sha:
            raise RuntimeError(
                f"PDE numerical decision input mismatch: {relative}"
            )
    with tempfile.TemporaryDirectory(
        prefix="pde-precheck-", dir=RESULTS
    ) as temporary:
        recomputed_path = Path(temporary) / "decision.json"
        environment = os.environ.copy()
        environment["PYTHONPATH"] = os.fspath(ROOT / "src")
        completed = subprocess.run(
            [
                PYTHON,
                "pde_precheck.py",
                "--output",
                os.fspath(recomputed_path),
            ],
            cwd=ROOT,
            env=environment,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if completed.returncode:
            raise RuntimeError(
                "independent PDE precheck recomputation failed\n"
                + completed.stdout
            )
        recomputed = json.loads(recomputed_path.read_text())
    if recomputed != numerical_decision:
        raise RuntimeError(
            "stored PDE numerical decision differs from clean recomputation"
        )
    fallback_cases = numerical_decision.get("r256_required", [])
    if len(fallback_cases) != len(set(fallback_cases)):
        raise RuntimeError("duplicate R256 fallback case")
    for case_id in fallback_cases:
        path = _find_pde(
            RESULTS / "pde_fallback",
            case_id,
            start_time=0.0,
            end_time=8.0,
            seed=fixed["primary_seed"],
            quadrature="hybrid",
            N=16,
            R=256,
            dt=0.02,
        )
        expected_records.append(
            (
                path,
                {
                    "case_id": case_id,
                    "start_time": 0.0,
                    "end_time": 8.0,
                    "quadrature_seed": fixed["primary_seed"],
                    "quadrature": "hybrid",
                    "depth_nodes_N": 16,
                    "base_quadrature_M": 81,
                    "fast_quadrature_R": 256,
                    "dt": 0.02,
                    "sample_dt": 0.04,
                },
            )
        )
    audit_dir = RESULTS / "pde_audits"
    for case_id in PROTOCOL["numerical_audits"]["qmc_crosscheck_cases"]:
        path = _find_pde(
            audit_dir,
            case_id,
            start_time=0.0,
            end_time=8.0,
            seed=fixed["primary_seed"],
            quadrature="sobol",
            N=16,
            R=128,
            dt=0.02,
        )
        expected_records.append(
            (
                path,
                {
                    "case_id": case_id,
                    "start_time": 0.0,
                    "end_time": 8.0,
                    "quadrature_seed": fixed["primary_seed"],
                    "quadrature": "sobol",
                    "depth_nodes_N": 16,
                    "base_quadrature_M": 256,
                    "fast_quadrature_R": 128,
                    "dt": 0.02,
                    "sample_dt": 0.04,
                },
            )
        )
    for case_id in PROTOCOL["numerical_audits"]["N32_cases"]:
        path = _find_pde(
            audit_dir,
            case_id,
            start_time=0.0,
            end_time=8.0,
            seed=fixed["primary_seed"],
            quadrature="hybrid",
            N=32,
            R=128,
            dt=0.02,
        )
        expected_records.append(
            (
                path,
                {
                    "case_id": case_id,
                    "start_time": 0.0,
                    "end_time": 8.0,
                    "quadrature_seed": fixed["primary_seed"],
                    "quadrature": "hybrid",
                    "depth_nodes_N": 32,
                    "base_quadrature_M": 81,
                    "fast_quadrature_R": 128,
                    "dt": 0.02,
                    "sample_dt": 0.04,
                },
            )
        )
    for case_id in PROTOCOL["numerical_audits"]["dt001_cases"]:
        path = _find_pde(
            audit_dir,
            case_id,
            start_time=0.0,
            end_time=8.0,
            seed=fixed["primary_seed"],
            quadrature="hybrid",
            N=16,
            R=128,
            dt=0.01,
        )
        expected_records.append(
            (
                path,
                {
                    "case_id": case_id,
                    "start_time": 0.0,
                    "end_time": 8.0,
                    "quadrature_seed": fixed["primary_seed"],
                    "quadrature": "hybrid",
                    "depth_nodes_N": 16,
                    "base_quadrature_M": 81,
                    "fast_quadrature_R": 128,
                    "dt": 0.01,
                    "sample_dt": 0.04,
                },
            )
        )
    for path, expected in expected_records:
        key = (
            expected["case_id"],
            expected["start_time"],
            expected["end_time"],
            expected["quadrature_seed"],
            expected["quadrature"],
            expected["depth_nodes_N"],
            expected["fast_quadrature_R"],
            expected["dt"],
        )
        if key in seen:
            raise RuntimeError(f"duplicate expected PDE configuration: {key}")
        seen.add(key)
        _validate_pde_archive(path, expected)
        files[os.fspath(path.relative_to(ROOT))] = _sha256(path)
    actual_directories = [
        "pde_primary",
        "pde_scramble",
        "pde_audits",
        "pde_fallback",
    ]
    actual = {
        path
        for directory in actual_directories
        for path in (RESULTS / directory).glob("*.npz")
    }
    expected_paths = {path for path, _ in expected_records}
    if actual != expected_paths:
        extras = sorted(os.fspath(p) for p in actual - expected_paths)
        missing = sorted(os.fspath(p) for p in expected_paths - actual)
        raise RuntimeError(f"PDE archive set mismatch extras={extras} missing={missing}")
    files[
        os.fspath(numerical_decision_path.relative_to(ROOT))
    ] = _sha256(numerical_decision_path)
    record = {
        "dynamics_sha256": dynamics,
        "run_grid_sha256": _sha256(Path(__file__)),
        "pde_numerical_decision_sha256": _sha256(numerical_decision_path),
        "files": files,
        "file_count": len(files),
    }
    encoded = json.dumps(record, indent=2, sort_keys=True) + "\n"
    seal = RESULTS / "PDE_STAGE_SEAL.json"
    seal.parent.mkdir(parents=True, exist_ok=True)
    if seal.exists() and seal.read_text() != encoded:
        raise RuntimeError("refusing to overwrite a different PDE stage seal")
    seal.write_text(encoded)
    print(encoded, end="")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        choices=(
            "pde-primary",
            "pde-scramble",
            "pde-continue",
            "pde-audits",
            "pde-r256",
            "seal-pde",
            "dense-screen",
            "dense-confirm",
            "dense-depth",
            "seal-dense",
        ),
    )
    parser.add_argument("--parallel-jobs", type=int, default=1)
    parser.add_argument("--dense-workers", type=int, default=4)
    parser.add_argument("--case-ids", nargs="*", default=[])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dynamics_hash = verify_frozen()
    print(f"verified frozen dynamics {dynamics_hash}", flush=True)
    if args.mode == "pde-primary":
        pde_primary(args.parallel_jobs)
    elif args.mode == "pde-scramble":
        pde_scramble(args.parallel_jobs)
    elif args.mode == "pde-continue":
        pde_continue(args.parallel_jobs)
    elif args.mode == "pde-audits":
        pde_audits(args.parallel_jobs)
    elif args.mode == "pde-r256":
        pde_r256(args.case_ids, args.parallel_jobs)
    elif args.mode == "seal-pde":
        seal_pde()
    elif args.mode == "seal-dense":
        seal_dense()
    else:
        dense_stage(args.mode, args.parallel_jobs, args.dense_workers)


if __name__ == "__main__":
    main()
