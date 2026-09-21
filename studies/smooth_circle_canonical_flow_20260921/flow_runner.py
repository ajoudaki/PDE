#!/usr/bin/env python3
"""Bounded supervisor for the frozen smooth-circle physical-flow experiment."""
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SEEDS = (20260921, 20260922, 20260923)
MODELS = ("width55", "closure1024", "width105")
TIMES = np.array([0, .01, .03, .1, .3, 1, 3, 5, 10, 20, 40, 60,
                  100, 160, 250, 400, 630, 800, 1000.], dtype=np.float64)
BUDGET = 4200.
RESERVE = 430.


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def frozen_sources():
    paths = [HERE / "PROTOCOL.md", HERE / "flow_benchmark.py",
             HERE / "flow_check.py", HERE / "flow_runner.py",
             HERE / "flow_analyze.py",
             ROOT / "code/pde/finite_network.py"]
    return {str(p.relative_to(ROOT)): sha(p) for p in paths}


def assert_sources(expected):
    for relative, value in expected.items():
        if sha(ROOT / relative) != value:
            raise RuntimeError("Frozen source changed: " + relative)


def labels(count, midpoint=False):
    theta = 2*np.pi*(np.arange(count) + (0.5 if midpoint else 0.))/count
    return np.sqrt(32/21)*(np.cos(theta)+.5*np.sin(3*theta)+.25*np.cos(5*theta))


def trace_increase(run):
    with (Path(run) / "accepted_steps.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    losses = np.array([float(row["loss"]) for row in rows])
    if len(losses) < 2:
        return 0.
    return float(np.max(np.maximum(np.diff(losses), 0)/np.maximum(1, losses[:-1])))


def compare_pair(coarse_dir, fine_dir, model):
    """Independently recompute the prespecified observable and state gates."""
    coarse_dir, fine_dir = Path(coarse_dir), Path(fine_dir)
    out = {"coarse": str(coarse_dir), "fine": str(fine_dir), "passed": False}
    try:
        records = [json.loads((p / "result.json").read_text()) for p in (coarse_dir, fine_dir)]
        if any(r["status"] != "completed" for r in records):
            return {**out, "reason": "incomplete integration"}
        with np.load(coarse_dir / "checkpoints.npz", allow_pickle=False) as left, \
                np.load(fine_dir / "checkpoints.npz", allow_pickle=False) as right:
            if not np.array_equal(left["times"], TIMES) or not np.array_equal(right["times"], TIMES):
                return {**out, "reason": "common observation times missing"}
            prediction_difference = 0.
            rmse_difference = 0.
            finite = True
            for key, target in (("train_prediction", labels(126)),
                                ("passive_prediction", labels(1024, True))):
                a, b = left[key], right[key]
                finite &= bool(np.isfinite(a).all() and np.isfinite(b).all())
                if not finite:
                    return {**out, "reason": "nonfinite saved predictions"}
                prediction_difference = max(prediction_difference, float(np.max(np.abs(a-b))))
                aa = np.sqrt(np.mean((a-target)**2, axis=1))
                bb = np.sqrt(np.mean((b-target)**2, axis=1))
                rmse_difference = max(rmse_difference, float(np.max(np.abs(aa-bb))))
            n = 1024 if model == "closure1024" else int(model.removeprefix("width"))
            k = 15 if model == "closure1024" else n*n
            slices = (slice(0, 2*n), slice(2*n, 2*n+k), slice(2*n+k, 3*n+k))
            a, b = left["states"], right["states"]
            if a.shape != (len(TIMES), 3*n+k) or b.shape != a.shape:
                return {**out, "reason": "state shape mismatch"}
            finite &= bool(np.isfinite(a).all() and np.isfinite(b).all())
            if not finite:
                return {**out, "reason": "nonfinite saved states"}
            block_ratios = []
            for part in slices:
                difference = np.sqrt(np.mean((a[:, part]-b[:, part])**2, axis=1))
                scale = 1+np.sqrt(np.mean(b[:, part]**2, axis=1))
                block_ratios.append(float(np.max(difference/scale)))
            fits = [bool(np.mean((arr["train_prediction"][-1]-labels(126))**2) <= .001)
                    for arr in (left, right)]
        monotone = trace_increase(fine_dir)
        passed = (finite and prediction_difference <= 2e-4 and rmse_difference <= 5e-5
                  and max(block_ratios) <= 2e-4 and fits[0] == fits[1] and monotone <= 5e-7)
        return {**out, "passed": bool(passed), "finite": bool(finite),
                "max_prediction_difference": prediction_difference,
                "max_rmse_difference": rmse_difference,
                "max_block_scaled_rms_difference": block_ratios,
                "fits": fits, "max_relative_loss_increase": monotone,
                "reason": "passed" if passed else "refinement gate failed"}
    except (OSError, ValueError, KeyError) as error:
        return {**out, "reason": str(error)}


def compare_reproduction(original, repeat):
    out = {"original": str(original), "repeat": str(repeat), "passed": False}
    try:
        records = [json.loads((Path(p) / "result.json").read_text()) for p in (original, repeat)]
        if any(r["status"] != "completed" for r in records):
            return {**out, "reason": "incomplete integration"}
        with np.load(Path(original)/"checkpoints.npz", allow_pickle=False) as a, \
                np.load(Path(repeat)/"checkpoints.npz", allow_pickle=False) as b:
            if not np.array_equal(a["times"], TIMES) or not np.array_equal(b["times"], TIMES):
                return {**out, "reason": "missing common observations"}
            differences = {key: float(np.max(np.abs(a[key]-b[key])))
                           for key in ("states", "train_prediction", "passive_prediction")}
            fits = [bool(np.mean((arr["train_prediction"][-1]-labels(126))**2) <= .001)
                    for arr in (a, b)]
        passed = all(np.isfinite(v) and v <= 1e-10 for v in differences.values()) and fits[0] == fits[1]
        return {**out, "passed": bool(passed), "max_differences": differences, "fits": fits}
    except (OSError, ValueError, KeyError) as error:
        return {**out, "reason": str(error)}


def worker(job, runroot, frozen):
    assert_sources(frozen)
    directory = runroot / job["id"]
    if directory.exists():
        raise RuntimeError("Refusing existing attempt: " + str(directory))
    command = [sys.executable, "-B", str(HERE/"flow_benchmark.py"),
               "--model", job["model"], "--seed", str(job["seed"]),
               "--level", job["level"], "--output", str(directory),
               "--wall-seconds", "400"]
    environment = os.environ.copy()
    environment.update(PYTHONPATH=str(ROOT/"code"), PYTHONDONTWRITEBYTECODE="1",
                       OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1",
                       NUMEXPR_NUM_THREADS="1")
    environment["FLOW_GIT_HEAD"] = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    log = runroot / (job["id"] + ".log")
    start = time.monotonic()
    with log.open("x") as stream:
        process = subprocess.Popen(command, cwd=ROOT, env=environment, stdout=stream,
                                   stderr=subprocess.STDOUT, start_new_session=True)
        killed = False
        try:
            exit_code = process.wait(timeout=429)
        except subprocess.TimeoutExpired:
            killed = True
            os.killpg(process.pid, signal.SIGKILL)
            exit_code = process.wait()
    elapsed = time.monotonic()-start
    result = {**job, "directory": str(directory), "command": command,
              "worker_process_wall_seconds": elapsed, "exit_code": exit_code,
              "supervisor_killed": killed, "log_sha256": sha(log)}
    artifact = directory / "result.json"
    if artifact.exists():
        record = json.loads(artifact.read_text())
        result.update(result_sha256=sha(artifact), status=record.get("status"),
                      physical_time=record.get("physical_time"), final_loss=record.get("final_loss"))
    else:
        result["status"] = "no_result"
    assert_sources(frozen)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--preflight", type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    if out.exists():
        raise SystemExit("Refusing existing campaign directory")
    preflight = json.loads(args.preflight.read_text())
    if not preflight.get("passed", False):
        raise SystemExit("Independent preflight must pass before training")
    frozen = frozen_sources()
    if preflight.get("producer_sha256") != frozen[str((HERE/"flow_benchmark.py").relative_to(ROOT))]:
        raise SystemExit("Preflight producer hash mismatch")
    if preflight.get("protocol_sha256") != frozen[str((HERE/"PROTOCOL.md").relative_to(ROOT))]:
        raise SystemExit("Preflight protocol hash mismatch")
    if preflight.get("checker_sha256") != frozen[str((HERE/"flow_check.py").relative_to(ROOT))]:
        raise SystemExit("Preflight checker hash mismatch")
    out.mkdir(parents=True)
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    manifest = {"study": HERE.name, "protocol_sha256": sha(HERE/"PROTOCOL.md"),
                "frozen_sources": frozen, "head": head, "cwd": str(ROOT),
                "command": sys.argv, "preflight": str(args.preflight.resolve()),
                "preflight_sha256": sha(args.preflight), "attempts": [], "comparisons": [],
                "reproductions": [], "selected": [], "batches": [], "status": "running",
                "worker_process_wall_seconds": 0., "worker_budget_seconds": BUDGET,
                "maximum_concurrency": 2}
    manifest_path = out / "run_record.json"

    def save():
        write_json(manifest_path, manifest)

    def batches(jobs):
        for offset in range(0, len(jobs), 2):
            batch = jobs[offset:offset+2]
            if manifest["worker_process_wall_seconds"] + len(batch)*RESERVE > BUDGET:
                manifest["budget_limited"] = True
                save()
                return
            manifest["pending"] = batch
            batch_record = {"jobs": [item["id"] for item in batch],
                            "prior_wall_seconds": manifest["worker_process_wall_seconds"],
                            "reserved_seconds": len(batch)*RESERVE, "status": "running"}
            manifest["batches"].append(batch_record)
            save()
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                futures = [executor.submit(worker, job, out, frozen) for job in batch]
                for future in futures:
                    attempt = future.result()
                    manifest["attempts"].append(attempt)
                    manifest["worker_process_wall_seconds"] += attempt["worker_process_wall_seconds"]
                    print(json.dumps(attempt, allow_nan=False), flush=True)
                    save()
            manifest["pending"] = []
            batch_record["status"] = "complete"
            batch_record["after_wall_seconds"] = manifest["worker_process_wall_seconds"]
            save()

    def job(model, seed, level, kind="original"):
        name = f"{model}_seed{seed}_{level}" + ("_reproduction" if kind == "reproduction" else "")
        return {"id": name, "model": model, "seed": seed, "level": level, "kind": kind}

    try:
        jobs = [job(model, seed, level) for seed in SEEDS for model in MODELS
                for level in ("primary", "fine")]
        batches(jobs)
        conditional = []
        for seed in SEEDS:
            for model in MODELS:
                a = out / job(model, seed, "primary")["id"]
                b = out / job(model, seed, "fine")["id"]
                comparison = compare_pair(a, b, model)
                manifest["comparisons"].append({"model": model, "seed": seed, **comparison})
                if comparison["passed"]:
                    manifest["selected"].append({"model": model, "seed": seed, "level": "fine", "directory": str(b)})
                elif comparison["reason"] == "refinement gate failed":
                    conditional.append(job(model, seed, "finer"))
        save()
        batches(conditional)
        for specification in conditional:
            model, seed = specification["model"], specification["seed"]
            a = out / job(model, seed, "fine")["id"]
            b = out / specification["id"]
            comparison = compare_pair(a, b, model)
            manifest["comparisons"].append({"model": model, "seed": seed, **comparison})
            if comparison["passed"]:
                manifest["selected"].append({"model": model, "seed": seed, "level": "finer", "directory": str(b)})
        save()
        reproduction_jobs = [job(item["model"], item["seed"], item["level"], "reproduction")
                             for item in manifest["selected"] if item["seed"] == SEEDS[0]]
        batches(reproduction_jobs)
        for specification in reproduction_jobs:
            original = out / job(specification["model"], specification["seed"], specification["level"])["id"]
            repeat = out / specification["id"]
            manifest["reproductions"].append({"model": specification["model"],
                "seed": specification["seed"], "level": specification["level"],
                **compare_reproduction(original, repeat)})
        manifest["status"] = "budget_limited" if manifest.get("budget_limited") else "complete"
        manifest["numerically_resolved"] = (len(manifest["selected"]) == 9
            and len(manifest["reproductions"]) == 3
            and all(item["passed"] for item in manifest["reproductions"]))
        assert_sources(frozen)
        save()
    except BaseException as error:
        manifest["status"] = "supervisor_failure"
        manifest["error"] = repr(error)
        save()
        raise
    print(json.dumps({k: manifest[k] for k in ("status", "numerically_resolved",
                     "worker_process_wall_seconds")}), flush=True)


if __name__ == "__main__":
    main()
