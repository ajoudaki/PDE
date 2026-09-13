"""One predeclared solver-validation configuration, producing fresh evidence.

Run a supervisor for hard wall/RSS/total budgets. Each worker additionally
sets a CPU limit and writes its own failure record. No parameter search.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time
import traceback

import numpy as np
from pde import observable_fixed, observable_arithmetic, observable_compiler, observable_initialization, observable_solver
from pde.observable_solver import (initialize, ArcLaw, evolve, predict, circle_inputs,
    paired_observations, loss, save_restart, load_restart, state_bytes)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scalar(x):
    return float(x)


def run(plan_path, run_id, output):
    plan = json.loads(Path(plan_path).read_text())
    config = next(c for c in plan["configurations"] if c["id"] == run_id)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    resource.setrlimit(resource.RLIMIT_CPU, (plan["budget"]["cpu_seconds_per_configuration"],)*2)
    modules = (observable_fixed, observable_arithmetic, observable_compiler, observable_initialization, observable_solver)
    record = dict(id=run_id, configuration=config, plan_sha256=digest(plan_path),
                  plan_version=plan["version"], status="running", command=sys.argv,
                  cwd=str(Path.cwd()), source_hashes={Path(m.__file__).name: digest(m.__file__) for m in modules},
                  producer_sha256=digest(__file__), python=sys.version, numpy=np.__version__, platform=platform.platform(),
                  processor=platform.processor(), thread_environment={k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")})
    record_path = output/"record.json"
    record_path.write_text(json.dumps(record, indent=2)+"\n")
    wall_start, cpu_start = time.perf_counter(), time.process_time()
    try:
        init_wall, init_cpu = time.perf_counter(), time.process_time()
        state = initialize(config["order"], initialization_nodes=config["initialization_nodes"],
                           population_nodes=config["population_nodes"], digits=config["digits"], backend=config["backend"],
                           epsilon_cov=plan["common"]["epsilon_cov"])
        record["initialization_seconds"] = dict(wall=time.perf_counter()-init_wall, cpu=time.process_time()-init_cpu)
        ar = state.arithmetic
        data = ArcLaw(**plan["law_parameters"][config["law"]]).quadrature(config["nodes_per_arc"], ar)
        record["state_bytes_initial"] = state_bytes(state)
        record["initialization_metadata"] = state.metadata
        record["dimensions"] = dict(first_features=state.b1.shape[1], second_features=state.b2.shape[1],
                                    first_nodes=len(state.b1), second_nodes=len(state.b2), input_nodes=len(data.inputs),
                                    action_matrix=list(state.M.shape))
        record["loss_initial"] = scalar(loss(state, data))
        steps = config["steps"]
        if steps % 2:
            raise ValueError("restart plan requires an even number of steps")
        h = Fraction(plan["horizon"])/steps
        timing, cpu = time.perf_counter(), time.process_time()
        midpoint = evolve(state, data, steps=steps//2, step_size=h, block_size=plan["common"]["block_size"])
        final = evolve(midpoint, data, steps=steps//2, step_size=h, block_size=plan["common"]["block_size"])
        record["evolution_seconds"] = dict(wall=time.perf_counter()-timing, cpu=time.process_time()-cpu)
        save_restart(output/"midpoint_restart.json", midpoint, data)
        restored, restored_data = load_restart(output/"midpoint_restart.json")
        timing, cpu = time.perf_counter(), time.process_time()
        resumed = evolve(restored, restored_data, steps=steps//2, step_size=h, block_size=plan["common"]["block_size"])
        record["restart_seconds"] = dict(wall=time.perf_counter()-timing, cpu=time.process_time()-cpu)
        record["restart_exact"] = all(np.array_equal(getattr(final, k), getattr(resumed, k))
                                      for k in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D"))
        if not record["restart_exact"]:
            raise AssertionError("own-state restart differed at the same arithmetic and steps")
        timing, cpu = time.perf_counter(), time.process_time()
        circle = circle_inputs(plan["common"]["circle_directions"], ar)
        prediction = predict(final, circle, block_size=plan["common"]["block_size"])
        pairs = paired_observations(final, data, block_size=plan["common"]["block_size"])
        record["observation_seconds"] = dict(wall=time.perf_counter()-timing, cpu=time.process_time()-cpu)
        record["loss_final"] = scalar(loss(final, data))
        record["rms1"], record["rms2"] = scalar(pairs["rms1"]), scalar(pairs["rms2"])
        record["prediction_max_abs"] = float(np.max(np.abs(np.asarray(prediction, float))))
        with ar.context():
            record["dynamic_changes"] = dict(row_max_abs=float(np.max(np.abs(np.asarray(final.w-state.w, float)))),
                                              readout_max_abs=float(np.max(np.abs(np.asarray(final.c, float)))),
                                              matrix_frobenius=float(np.linalg.norm(np.asarray(final.M-state.M, float))))
        record["state_bytes_final"] = state_bytes(final)
        record["checkpoint_bytes"] = (output/"midpoint_restart.json").stat().st_size
        np.savez_compressed(output/"observations.npz", circle=np.asarray(circle, float), prediction=np.asarray(prediction, float),
                            **{k: np.asarray(v, float) for k, v in pairs.items()})
        # Exact working values are retained separately, without float conversion.
        save_restart(output/"final_restart.json", final, data)
        record["observation_storage"] = "NPZ diagnostics rounded to float64; restart JSON retains exact working scalar values"
        record["status"] = "operational_pass"
    except Exception as exc:
        record.update(status="failure", error=repr(exc), traceback=traceback.format_exc())
    finally:
        record["total_seconds"] = dict(wall=time.perf_counter()-wall_start, cpu=time.process_time()-cpu_start)
        record["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
        record["outputs"] = {p.name: digest(p) for p in output.iterdir() if p.is_file() and p.name != "record.json"}
        record_path.write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k: record.get(k) for k in ("id", "status", "total_seconds", "peak_rss_bytes", "error")}))
    return 0 if record["status"] == "operational_pass" else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.plan, args.id, args.output))
