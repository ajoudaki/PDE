"""Execute exactly CH3_VALIDATION_PLAN.md, one independent worker per case."""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time
import traceback

import numpy as np

CONFIGS = [dict(id=k, order=n, Q=q, P=p, steps=j, arc_nodes=m)
           for k, n, q, p, j, m in (
               ("a", 1, 64, 32, 8, 4), ("b", 3, 64, 32, 8, 4),
               ("c", 5, 64, 32, 8, 4), ("d", 3, 128, 64, 16, 8),
               ("e", 1, 64, 32, 16, 4))]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def worker(config, directory):
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    from depth_closure import (initialize, DataLaw, evolve, predict,
                               paired_observations, state_bytes,
                               save_restart, load_restart)
    from pde.observable_compiler import CompilerLimits
    from pde.observable_solver import ArcLaw
    directory.mkdir()
    started, cpu_start = time.perf_counter(), time.process_time()
    report = dict(config=config, status="started", environment=dict(
        python=sys.version, numpy=np.__version__, platform=platform.platform(),
        threads={k: os.environ[k] for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}))
    try:
        limits = CompilerLimits(max_nodes=20000, max_sources=2048, max_points=1024,
                                max_working_bytes=1024**3, max_work_units=100000000000)
        at = time.perf_counter()
        state = initialize(config["order"], depth=3, dimension=2,
                           initialization_nodes=config["Q"], population_nodes=config["P"],
                           epsilon_cov=Fraction(1, 10000), limits=limits)
        report["initialization_seconds"] = time.perf_counter()-at
        raw = ArcLaw().quadrature(config["arc_nodes"], state.arithmetic)
        law = DataLaw(raw.inputs, raw.labels, raw.probabilities,
                      {"exact_law": raw.metadata, "scope": "depth-three operational validation; no finite-resolution error certificate"})
        step = Fraction(1, 200*config["steps"])
        at = time.perf_counter()
        middle = evolve(state, law, steps=config["steps"]//2, step_size=step)
        save_restart(directory/"halfway.json", middle, law)
        final = evolve(middle, law, steps=config["steps"]//2, step_size=step)
        report["evolution_seconds"] = time.perf_counter()-at
        save_restart(directory/"final.json", final, law)
        at = time.perf_counter()
        restored, restored_law = load_restart(directory/"halfway.json")
        resumed = evolve(restored, restored_law, steps=config["steps"]//2, step_size=step)
        save_restart(directory/"resumed.json", resumed, restored_law)
        report["restart_seconds"] = time.perf_counter()-at
        report["exact_restart"] = json.loads((directory/"final.json").read_text()) == json.loads((directory/"resumed.json").read_text())
        if not report["exact_restart"]:
            raise AssertionError("complete working-state restart differs")
        panel = []
        for k in range(-8, 8):
            s = Fraction(k, 8)
            panel.append(((1-s*s)/(1+s*s), 2*s/(1+s*s)))
        panel = final.arithmetic.array(panel)
        predictions = predict(final, panel)
        paired = paired_observations(final, law)
        arrays = dict(panel=np.asarray(panel, float), predictions=np.asarray(predictions, float),
                      inputs=np.asarray(law.inputs, float), labels=np.asarray(law.labels, float),
                      input_weights=np.asarray(law.probabilities, float))
        for l, values in enumerate(paired["pairs"]):
            arrays["pairs_"+str(l+1)] = np.asarray(values, float)
            arrays["population_weights_"+str(l+1)] = np.asarray(final.pi[l], float)
        arrays["training_prediction"] = np.asarray(predict(final, law.inputs), float)
        arrays["rms"] = np.asarray(paired["rms"], float)
        if not all(np.all(np.isfinite(a)) for a in arrays.values()):
            raise AssertionError("nonfinite operational observation")
        np.savez(directory/"observations.npz", **arrays)
        report["loss"] = float(np.sum(arrays["input_weights"]*(arrays["training_prediction"]-arrays["labels"])**2))
        report["rms"] = arrays["rms"].tolist()
        report["retained_state_bytes"] = state_bytes(final)
        report["feature_counts"] = [a.shape[1] for a in final.b]
        report["initialized_gram_condition"] = final.metadata["initialized_gram_condition"]
        report["population_gram_condition"] = []
        for b, pi in zip(final.b, final.pi):
            gram = np.asarray(b, float).T @ (np.asarray(pi, float)[:, None]*np.asarray(b, float))
            condition = float(np.linalg.cond(gram))
            report["population_gram_condition"].append(condition if np.isfinite(condition) else None)
        report["initializer_metadata"] = final.metadata
        report["status"] = "pass"
    except Exception:
        report["status"] = "fail"
        report["traceback"] = traceback.format_exc()
    report["wall_seconds"] = time.perf_counter()-started
    report["cpu_seconds"] = time.process_time()-cpu_start
    report["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
    report["output_hashes"] = {p.name: digest(p) for p in directory.iterdir() if p.is_file()}
    (directory/"report.json").write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: report[k] for k in ("config", "status", "wall_seconds", "cpu_seconds", "peak_rss_bytes")}))
    if report["status"] != "pass":
        print(report["traceback"])
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--worker", choices=[c["id"] for c in CONFIGS])
    args = parser.parse_args()
    if args.worker:
        return worker(next(c for c in CONFIGS if c["id"] == args.worker), args.output)
    args.output.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).resolve().parent
    repo = source.parents[1]
    files = list(source.glob("*.py"))+[source/"CH3_VALIDATION_PLAN.md"]
    files += [repo/"code/pde"/name for name in (
        "observable_arithmetic.py", "observable_fixed.py", "observable_compiler.py",
        "observable_words.py", "observable_solver.py", "observable_initialization.py")]
    (args.output/"provenance.json").write_text(json.dumps(dict(
        configs=CONFIGS, command=sys.argv, cwd=str(Path.cwd()),
        sources={str(p.relative_to(repo)): digest(p) for p in files}), indent=2)+"\n")
    results, total_cpu = [], 0.0
    for config in CONFIGS:
        command = [sys.executable, "-B", str(Path(__file__).resolve()),
                   "--output", str(args.output/config["id"]), "--worker", config["id"]]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=120)
            (args.output/(config["id"]+".log")).write_text(result.stdout+result.stderr)
            print(result.stdout, flush=True)
            report_path = args.output/config["id"]/"report.json"
            if report_path.exists():
                report = json.loads(report_path.read_text())
                total_cpu += report["cpu_seconds"]
                results.append(report)
            if result.returncode != 0:
                break
        except subprocess.TimeoutExpired as exc:
            (args.output/(config["id"]+".failure.txt")).write_text(str(exc))
            break
        if total_cpu >= 600:
            break
    summary = dict(passed=sum(r["status"] == "pass" for r in results), required=len(CONFIGS),
                   cpu_seconds=total_cpu, reports=[r["config"]["id"] for r in results])
    (args.output/"summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(summary))
    return int(summary["passed"] != len(CONFIGS))


if __name__ == "__main__":
    raise SystemExit(main())
