#!/usr/bin/env python3
"""Execute the frozen conditional fitting protocol with two bounded GPU workers."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
SEEDS = (20260921, 20260922, 20260923)
SAMPLES = (30, 62, 126, 254)
CAP = 2500.0
RESERVATION = 75.0


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")
    temporary.replace(path)


def load_summary(path):
    record = json.loads((path / "record.json").read_text())
    return record


def summary_metrics(record):
    return dict(record["diagnostics"]["best"], fit=record["fit"])


def execute_job(job):
    output = Path(job["output"])
    config_path = output.parent / (output.name + "_config.json")
    config = dict(model=job["model"], width=job["width"], m=job["samples"],
                  seed=job["seed"], gain="primary" if job["input_gain"] == 1 else "rescue",
                  device=job["device"], max_seconds=60)
    write_json(config_path, config)
    command = [sys.executable, "-B", str(STUDY / "fit_benchmark.py"), "attempt",
               "--config", str(config_path), "--output", str(output),
               "--freeze", str(STUDY / "README.md")]
    environment = os.environ.copy()
    environment.update(PYTHONPATH=str(ROOT / "code"), PYTHONDONTWRITEBYTECODE="1",
                       OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    start = time.perf_counter()
    with (output.parent / (output.name + ".log")).open("w") as log:
        try:
            completed = subprocess.run(command, cwd=ROOT, env=environment,
                                       stdout=log, stderr=subprocess.STDOUT, timeout=74)
            returncode, failure = completed.returncode, None
        except subprocess.TimeoutExpired:
            returncode, failure = -9, "supervisor_timeout_74s"
    result = dict(job, command=command, cwd=str(ROOT), returncode=returncode,
                  process_wall_seconds=time.perf_counter()-start, supervisor_failure=failure)
    if (output / "record.json").exists():
        result["summary"] = load_summary(output)
        result["metrics"] = summary_metrics(result["summary"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--adjudications", type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if args.resume:
        record = json.loads((output/"run_record.json").read_text())
        if record["status"] != "stopped_with_error":
            raise RuntimeError("resume requires a retained stopped campaign")
        for p in (STUDY/"README.md", STUDY/"fit_benchmark.py"):
            if digest(p) != record["source_hashes"][str(p.relative_to(ROOT))]:
                raise RuntimeError("frozen scientific source changed")
        snapshot = output/f"interruption_{len(record.get('resumes', []))+1:02d}.json"
        write_json(snapshot, record)
        record.setdefault("resumes", []).append(dict(
            interrupted_record=str(snapshot), runner_sha256=digest(__file__),
            command=sys.argv, unix_seconds=time.time()))
        record["status"] = "running"
        record.pop("error", None)
    else:
        output.mkdir(parents=True, exist_ok=False)
        record = dict(status="running", worker_wall_cap=CAP, spent_worker_seconds=0.0,
                      reservations=0.0, selected_samples=None, jobs=[], gates=[],
                      source_hashes={str(p.relative_to(ROOT)): digest(p) for p in
                                     (STUDY/"README.md", STUDY/"fit_benchmark.py", Path(__file__))})
        (output/"frozen_protocol.md").write_bytes((STUDY/"README.md").read_bytes())
    write_json(output/"run_record.json", record)

    def accept(result):
        if result["returncode"] == 0:
            return result
        path = Path(result["output"])
        if not (path/"record.json").exists():
            raise RuntimeError("producer failure without record; cannot adjudicate")
        summary = load_summary(path)
        # Only the predeclared cancellation diagnostic can resolve this stop.
        if (not summary.get("budget_respected") or summary.get("oracle_pass")
                or summary.get("status") in ("error", "nonfinite")):
            raise RuntimeError("producer failure is not eligible for precision adjudication")
        decisions = (json.loads(args.adjudications.read_text())
                     if args.adjudications and args.adjudications.exists() else {})
        decision = decisions.get(str(path))
        if not decision and args.adjudications:
            # This is replay of saved weights only, never another training run.
            # Reserve 100 of the 300 CPU-check seconds for prior/final checks.
            remaining = 200 - record.get("automatic_precision_seconds", 0.0)
            if remaining < 1:
                raise RuntimeError("automatic precision replay allowance exhausted")
            command = [sys.executable, "-B", str(STUDY/"fit_check.py"), "adjudicate",
                       str(path), "--output", str(args.adjudications.resolve())]
            start = time.perf_counter()
            try:
                with (output/(path.name+"_precision.log")).open("w") as log:
                    checked = subprocess.run(command, cwd=ROOT, stdout=log,
                                             stderr=subprocess.STDOUT, timeout=min(60, remaining))
                if checked.returncode:
                    raise RuntimeError("independent precision replay failed")
            finally:
                elapsed = time.perf_counter()-start
                record["automatic_precision_seconds"] = record.get("automatic_precision_seconds", 0.0)+elapsed
                record.setdefault("precision_commands", []).append(dict(
                    command=command, process_wall_seconds=elapsed,
                    checker_sha256=digest(STUDY/"fit_check.py")))
            decisions = json.loads(args.adjudications.read_text())
            decision = decisions.get(str(path))
        if not decision or not decision.get("resolved"):
            raise RuntimeError(f"independent precision adjudication pending: {path}")
        if decision["record_sha256"] != digest(path/"record.json"):
            raise RuntimeError("precision adjudication record hash mismatch")
        result["summary"] = summary
        result["metrics"] = summary_metrics(summary)
        result["metrics"].update({k: decision[k] for k in
                                  ("fit", "mse", "sign_errors", "max_abs_error")})
        result["precision_adjudication"] = decision
        return result

    def batch(jobs):
        results = []
        existing = {job["output"]: job for job in record["jobs"]}
        pending = []
        for job in jobs:
            if job["output"] in existing:
                old = existing[job["output"]]
                for key in ("model", "width", "samples", "seed", "input_gain", "stage", "device"):
                    if old[key] != job[key]:
                        raise RuntimeError("resume job configuration mismatch")
                accept(old)
            else:
                pending.append(job)
        for begin in range(0, len(pending), 2):
            group = pending[begin:begin+2]
            if record["spent_worker_seconds"] + RESERVATION*len(group) > CAP:
                raise RuntimeError("insufficient remaining worker budget for next reservation")
            record["reservations"] = RESERVATION*len(group)
            write_json(output/"run_record.json", record)
            with ThreadPoolExecutor(max_workers=len(group)) as pool:
                completed = list(pool.map(execute_job, group))
            record["reservations"] = 0.0
            for result in completed:
                record["spent_worker_seconds"] += result["process_wall_seconds"]
                record["jobs"].append(result)
                existing[result["output"]] = result
                display = {k: result[k] for k in
                           ("stage", "model", "width", "samples", "seed", "input_gain", "returncode")}
                display["metrics"] = {k: result.get("metrics", {}).get(k) for k in
                                      ("fit", "mse", "sign_errors", "max_abs_error")}
                print(json.dumps(display), flush=True)
            write_json(output/"run_record.json", record)
            for result in completed:
                accept(result)
        return [existing[job["output"]] for job in jobs]

    def group(model, width, samples, gain, stage):
        jobs = []
        for index, seed in enumerate(SEEDS):
            name = f"{stage}_{model}_n{width}_m{samples}_seed{seed}_gain{gain:g}"
            jobs.append(dict(model=model, width=width, samples=samples, seed=seed,
                             input_gain=gain, stage=stage, device=f"cuda:{index%2}",
                             output=str(output/name)))
        return batch(jobs)

    def suite(model, width, samples, stage):
        canonical = group(model, width, samples, 1.0, stage+"_canonical")
        results = list(canonical)
        canonical_fits = sum(bool(job["metrics"]["fit"]) for job in canonical)
        if canonical_fits == 0:
            results.extend(group(model, width, samples, samples/2, stage+"_rescue"))
        gate = dict(model=model, width=width, samples=samples,
                    canonical_fits=canonical_fits, all_fits=sum(bool(j["metrics"]["fit"]) for j in results),
                    attempted=len(results), rescue_run=(canonical_fits == 0))
        record["gates"] = [g for g in record["gates"] if
                           (g["model"], g["width"], g["samples"]) != (model, width, samples)] + [gate]
        write_json(output/"run_record.json", record)
        print(json.dumps({"gate": gate}), flush=True)
        return results

    try:
        stage_a = {m: suite("network", 55, m, "A") for m in SAMPLES}
        failed = [m for m in SAMPLES if m > 55 and not any(j["metrics"]["fit"] for j in stage_a[m])]
        selected = failed[0] if failed else None
        record["selected_samples"] = selected
        write_json(output/"run_record.json", record)
        if selected is not None:
            selected_groups = [stage_a[selected], suite("closure", 1024, selected, "B"),
                               suite("network", 105, selected, "B")]
        else:
            selected_groups = [stage_a[254]]
        for jobs in selected_groups:
            original = min(jobs, key=lambda job: job["metrics"]["mse"])
            repeat = {key: original[key] for key in
                      ("model", "width", "samples", "seed", "input_gain", "device")}
            repeat.update(stage="reproduction", original_output=original["output"],
                          output=str(output/("reproduction_"+Path(original["output"]).name)))
            reproduced = batch([repeat])[0]
            comparison = dict(original_output=original["output"], reproduction_output=reproduced["output"],
                              mse_difference=abs(original["metrics"]["mse"]-reproduced["metrics"]["mse"]),
                              same_fit=bool(original["metrics"]["fit"] == reproduced["metrics"]["fit"]))
            comparison["passed"] = comparison["same_fit"] and comparison["mse_difference"] <= 1e-6
            record["reproductions"] = [r for r in record.get("reproductions", []) if
                                      r["original_output"] != comparison["original_output"]] + [comparison]
            write_json(output/"run_record.json", record)
        record["status"] = "complete"
    except Exception as exc:
        record["status"] = "stopped_with_error"
        record["error"] = repr(exc)
        raise
    finally:
        record["reservations"] = 0.0
        write_json(output/"run_record.json", record)


if __name__ == "__main__":
    main()
