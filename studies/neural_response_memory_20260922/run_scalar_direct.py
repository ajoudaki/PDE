"""Bounded no-Fourier scalar experiment. See SCALAR_DIRECT_PROTOCOL.md."""
from __future__ import annotations
import os
for variable in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[variable] = "1"
import argparse
import hashlib
import json
import pickle
import platform
import subprocess
import sys
import time
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp

from scalar_population_reference import initialize, PopulationReference

FOLDER = Path(__file__).resolve().parent
TASKS = {
    "broad_pair": ([10., 125.], [1., -1.]),
    "close_pair": ([10., 45.], [1., -1.]),
    "triple": ([10., 75., 145.], [1., -1., 1.]),
}
QUERY_ANGLES = [55., 205., 310.]
T = 12.
TIMES = np.linspace(0, T, 121)
SEEDS = [20260920, 20260921]
WIDTHS = [16, 64]
LIMIT = 1800.
SOURCES = ["scalar_direct.py", "scalar_population_reference.py",
           "scalar_fourier_engine.py", "run_scalar_direct.py",
           "SCALAR_DIRECT_PROTOCOL.md"]


def inputs(angles):
    a = np.deg2rad(angles)
    return np.column_stack((np.cos(a), np.sin(a)))


def write_json(path, obj):
    path = Path(path)
    with path.open("x") as f:
        json.dump(obj, f, indent=2, allow_nan=False)
        f.write("\n")


def hashes():
    return {s:hashlib.sha256((FOLDER/s).read_bytes()).hexdigest() for s in SOURCES}


def model(args):
    angles, y = TASKS[args.task]
    X, Q = inputs(angles), inputs(QUERY_ANGLES)
    parent = PopulationReference(X, y, initialize(args.width, args.seed), order=args.order)
    return X, np.asarray(y), Q, parent


def compile_worker(args):
    from scalar_direct import ScalarCompiler
    X, y, Q, _ = model(args)
    started = time.monotonic()
    try:
        compiler = ScalarCompiler(X, y, Q, args.cutoff, order=args.order)
        with (args.cell/"compiler.pkl").open("xb") as f:
            pickle.dump(compiler, f, protocol=5)
        result = dict(success=True, phase="compile", statistics=compiler.statistics(),
                      table_bytes=sum(a.nbytes for a in compiler.train_table.values()),
                      scalar_count=compiler.dimension)
    except Exception as exc:
        result = dict(success=False, phase="compile", error=repr(exc),
                      statistics=getattr(exc, "stats", {}))
    result.update(wall_seconds=time.monotonic()-started, source_hashes=hashes())
    write_json(args.cell/"result.json", result)
    print(json.dumps(result), flush=True)


def parent_observables(parent, z, Q):
    train = parent.query_fields(z, parent.inputs)
    test = parent.query_fields(z, Q)["f"]
    return dict(train=train["f"], test=test,
                grams=np.array([h.T@h/parent.n for h in train["h"]]),
                clock=float(parent.unpack(z)["L"]))


def integrate(rhs, initial, observe, labels, refined=False):
    started = time.monotonic()
    count = 0
    def checked(t, z):
        nonlocal count
        count += 1
        if time.monotonic()-started > 45:
            raise TimeoutError(f"45 second solve cap at RHS t={t:.9g}")
        if not np.isfinite(z).all() or np.max(abs(z))>1e14 or z[-1]<0.99:
            raise FloatingPointError(f"state/clock numerical gate at RHS t={t:.9g}")
        value = rhs(t, z)
        if not np.isfinite(value).all():
            raise FloatingPointError(f"nonfinite RHS at t={t:.9g}")
        return value
    def fit_event(t, z):
        return np.mean((observe(z)["train"]-labels)**2)-.05**2
    fit_event.direction, fit_event.terminal = -1, False
    tol = (2e-9, 2e-11) if refined else (2e-7, 2e-9)
    try:
        sol = solve_ivp(checked, (0., T), initial, method="DOP853",
                        rtol=tol[0], atol=tol[1], dense_output=True, events=fit_event)
        if not sol.success:
            raise RuntimeError(sol.message)
        states = sol.sol(TIMES)
        observed = [observe(states[:, i]) for i in range(len(TIMES))]
        arrays = {k:np.array([o[k] for o in observed]) for k in observed[0]}
        arrays["times"] = TIMES
        arrays["initial"], arrays["final"] = initial, sol.y[:, -1]
        arrays["fit_times"] = sol.t_events[0]
        if len(sol.t_events[0]):
            fit = observe(sol.sol(sol.t_events[0][0]))
            for key, value in fit.items():
                arrays["own_fit_"+key] = np.asarray(value)
        rec = dict(success=True, nfev=count, accepted_steps=len(sol.t)-1,
                   solver_seconds=time.monotonic()-started, rtol=tol[0], atol=tol[1],
                   fit_time=float(sol.t_events[0][0]) if len(sol.t_events[0]) else None,
                   final_training_rms=float(np.sqrt(np.mean((arrays["train"][-1]-labels)**2))))
        return sol, arrays, rec
    except Exception as exc:
        return None, None, dict(success=False, error=repr(exc), nfev=count,
                               solver_seconds=time.monotonic()-started,
                               rtol=tol[0], atol=tol[1])


def simulation_worker(args):
    X, y, Q, parent = model(args)
    started = time.monotonic()
    kind = args.phase
    info = dict(kind=kind, task=args.task, P=args.order, K=args.cutoff,
                width=args.width, seed=args.seed, refined=args.refined,
                clip=not args.no_clip, source_hashes=hashes())
    runtime = None
    if kind == "scalar":
        with args.compiler.open("rb") as f:
            compiler = pickle.load(f)
        begin = time.monotonic()
        runtime, bounds = compiler.initialize(parent, T, clip=not args.no_clip)
        info.update(initialization_seconds=time.monotonic()-begin,
                    scalar_count=runtime.dimension, runtime_array_bytes=runtime.array_bytes(),
                    table_bytes=sum(a.nbytes for a in runtime.table.values()),
                    bounds=bounds)
        rhs, initial, observe = runtime.rhs, runtime.initial, runtime.observables
        # Algebraic passive nonfeedback must be true even after arbitrary
        # perturbation; structure is checked separately in check_scalar_direct.
    else:
        rhs, initial = parent.rhs, parent.initial
        observe = lambda z:parent_observables(parent, z, Q)
        info.update(population_state_count=parent.dimension,
                    initialized_matrix_count=sum(W.size for W in parent.initialization.W0),
                    population_total_array_bytes=8*(parent.dimension+sum(W.size for W in parent.initialization.W0)))
    sol, arrays, rec = integrate(rhs, initial, observe, y, args.refined)
    info.update(rec)
    if sol is not None:
        eigen = np.linalg.eigvalsh(arrays["grams"])
        info["gram_min_eigenvalue"] = float(eigen.min())
        info["gram_max_abs_entry"] = float(abs(arrays["grams"]).max())
        info["gram_motion_rms"] = np.sqrt(np.mean(
            (arrays["grams"][-1]-arrays["grams"][0])**2, axis=(1, 2))).tolist()
        if runtime is not None:
            sampled = sol.sol(TIMES)
            ratio = abs(sampled[:-1])/runtime.caps[:, None]
            info["clipped_coordinate_time_fraction"] = float(np.mean(ratio>1))
            info["clipped_coordinate_count"] = int(np.sum(np.any(ratio>1, axis=1)))
            info["max_cap_ratio"] = float(ratio.max())
            arrays["caps"] = runtime.caps
            # Compare at the independently saved parent's first fit time.
            ref = json.loads((args.parent/"result.json").read_text())
            fit = ref.get("fit_time")
            if fit is not None:
                for key, value in observe(sol.sol(fit)).items():
                    arrays["parent_fit_"+key] = np.asarray(value)
            # Genuine instantaneous truncation defect on the parent, for
            # diagnosis only; this is not supplied to the scalar solver.
            from scalar_direct import parent_fields
            snapshot = np.load(args.parent/"parent_snapshots.npz")
            defects = []
            for t, state in zip(snapshot["times"], snapshot["states"]):
                evaluator = parent_fields(parent, state, Q)
                z = np.r_[[evaluator.tree(tree) for tree in compiler.training_patterns],
                          float(parent.unpack(state)["L"])]
                truncated = runtime.rhs(t, z)
                full = parent.query_field_velocity(state, np.concatenate((X, Q)))["f"]
                selected = np.r_[runtime.output_indices, runtime.query_indices]
                defects.append(truncated[selected]-full)
            arrays["velocity_defect_times"] = snapshot["times"]
            arrays["velocity_defects"] = np.array(defects)
        else:
            snapshots = np.array([0., 1., 4., T])
            np.savez_compressed(args.cell/"parent_snapshots.npz",
                                times=snapshots, states=sol.sol(snapshots).T)
        np.savez_compressed(args.cell/"trajectory.npz", **arrays)
    info["wall_seconds"] = time.monotonic()-started
    write_json(args.cell/"result.json", info)
    print(json.dumps(info), flush=True)


def compare(out):
    records = []
    for cell in sorted(out.glob("scalar_*")):
        if not (cell/"result.json").exists():
            continue
        result = json.loads((cell/"result.json").read_text())
        if not result.get("success"):
            records.append(dict(cell=cell.name, **result))
            continue
        tag = f'{result["task"]}_P{result["P"]}_n{result["width"]}_s{result["seed"]}'
        parent_path = out/("parent_"+tag)
        ref_result = json.loads((parent_path/"result.json").read_text())
        a, b = np.load(cell/"trajectory.npz"), np.load(parent_path/"trajectory.npz")
        for name in ("train", "test"):
            error = np.sqrt(np.mean((a[name]-b[name])**2, axis=1))
            result[name+"_max_rms_error"] = float(error.max())
            result[name+"_final_rms_error"] = float(error[-1])
            if "parent_fit_"+name in a.files:
                result[name+"_at_parent_fit_rms_error"] = float(np.sqrt(np.mean(
                    (a["parent_fit_"+name]-b["own_fit_"+name])**2)))
        gram_error = np.sqrt(np.mean((a["grams"]-b["grams"])**2, axis=(2, 3)))
        result["gram_max_rms_errors"] = gram_error.max(axis=0).tolist()
        result["gram_final_rms_errors"] = gram_error[-1].tolist()
        result["clock_max_error"] = float(abs(a["clock"]-b["clock"]).max())
        labels = np.asarray(TASKS[result["task"]][1])
        loss_a, loss_b = np.mean((a["train"]-labels)**2, axis=1), np.mean((b["train"]-labels)**2, axis=1)
        result["loss_max_error"] = float(abs(loss_a-loss_b).max())
        result["parent_final_training_rms"] = ref_result["final_training_rms"]
        result["parent_gram_motion_rms"] = ref_result["gram_motion_rms"]
        result["parent_fit_time"] = ref_result["fit_time"]
        worst = max(result["train_max_rms_error"], result["test_max_rms_error"],
                    *result["gram_max_rms_errors"])
        result["accuracy_gate"] = "pass" if worst<=.02 else "fail" if worst>.1 else "intermediate"
        result["numerically_refined"] = False
        records.append(dict(cell=cell.name, **result))
    # Refined/reference ablations are transparently additional records.
    by_name = {r["cell"]:r for r in records}
    for r in records:
        if r["cell"].endswith("_refined") and r.get("success"):
            base = r["cell"].removesuffix("_refined")
            if base in by_name and by_name[base].get("success"):
                a,b=np.load(out/r["cell"]/"trajectory.npz"),np.load(out/base/"trajectory.npz")
                diffs = {key:float(np.max(abs(a[key]-b[key]))) for key in ("train","test","grams")}
                r["refinement_max_abs_changes"] = diffs
                by_name[base]["refinement_max_abs_changes"] = diffs
                by_name[base]["numerically_refined"] = max(diffs.values())<=1e-4
    summary = dict(records=records, source_hashes=hashes(),
                   budget=json.loads((out/"budget.json").read_text()) if (out/"budget.json").exists() else {})
    write_json(out/"scores.json", summary)
    import csv
    columns=["cell","P","K","width","seed","success","accuracy_gate","final_training_rms",
             "parent_final_training_rms","train_max_rms_error","test_max_rms_error",
             "test_final_rms_error","gram_max_rms_errors","scalar_count","solver_seconds",
             "clipped_coordinate_count"]
    with (out/"comparison.csv").open("x") as f:
        writer=csv.DictWriter(f,fieldnames=columns,extrasaction="ignore")
        writer.writeheader()
        for r in records: writer.writerow(r)
    print(json.dumps(dict(successful=sum(r.get("success",False) for r in records),
                         total=len(records), passes=sum(r.get("accuracy_gate")=="pass" for r in records))))


def campaign(args):
    out = args.out
    out.mkdir(parents=True, exist_ok=False)
    sources = out/"source"
    sources.mkdir()
    for source in SOURCES:
        (sources/source).write_bytes((FOLDER/source).read_bytes())
    write_json(out/"config.json", dict(tasks=TASKS, queries=QUERY_ANGLES, widths=WIDTHS,
        seeds=SEEDS, horizon=T, times=TIMES.tolist(), cutoffs=[3,5,7], memory_orders=[1,2],
        budget_seconds=LIMIT, command=sys.argv, cwd=os.getcwd(), python=sys.version,
        numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform(),
        source_hashes=hashes()))
    used, calls = 0., []
    def run(phase, name, task, P, K=3, n=16, seed=SEEDS[0], extra=()):
        nonlocal used
        reserve=65 if phase=="compile" else 55
        if used+reserve > LIMIT:
            return None
        cell=out/name
        cell.mkdir()
        cmd=[sys.executable,"-B",str(Path(__file__).resolve()),"--phase",phase,
             "--cell",str(cell),"--task",task,"--order",str(P),"--cutoff",str(K),
             "--width",str(n),"--seed",str(seed),*map(str,extra)]
        start=time.monotonic()
        with (cell/"worker.log").open("x") as f:
            try:
                cp=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=110)
                status=cp.returncode
            except subprocess.TimeoutExpired:
                status="timeout"
        elapsed=time.monotonic()-start
        used+=elapsed
        calls.append(dict(name=name,command=cmd,exit_status=status,seconds=elapsed))
        result=cell/"result.json"
        if not result.exists():
            write_json(result,dict(success=False,error=f"worker exit {status}",wall_seconds=elapsed))
        record=json.loads(result.read_text())
        print(json.dumps(dict(cell=name,success=record.get("success"),seconds=round(elapsed,3),
                              scalar_count=record.get("scalar_count"),
                              final_rms=record.get("final_training_rms"),
                              error=record.get("error"))),flush=True)
        return record
    completed={}
    for task,P in [(task,1) for task in TASKS]+[("broad_pair",2)]:
        references={}
        for n in WIDTHS:
            for seed in SEEDS:
                tag=f"{task}_P{P}_n{n}_s{seed}"
                references[n,seed]=run("parent","parent_"+tag,task,P,n=n,seed=seed)
        for K in ([3,5,7,9] if task=="broad_pair" and P==1 else [3,5,7]):
            name=f"compile_{task}_P{P}_K{K}"
            record=run("compile",name,task,P,K)
            if record is None or not record["success"]:
                break
            completed[task,P]=K
            compiler=out/name/"compiler.pkl"
            for n in WIDTHS:
                for seed in SEEDS:
                    if not references[n,seed] or not references[n,seed]["success"]:
                        continue
                    tag=f"{task}_P{P}_n{n}_s{seed}"
                    run("scalar",f"scalar_{tag}_K{K}",task,P,K,n,seed,
                        ("--compiler",compiler,"--parent",out/("parent_"+tag)))
    if ("broad_pair",1) in completed:
        K=completed["broad_pair",1]
        tag=f"broad_pair_P1_n16_s{SEEDS[0]}"
        extra=("--compiler",out/f"compile_broad_pair_P1_K{K}"/"compiler.pkl",
               "--parent",out/("parent_"+tag))
        run("scalar",f"scalar_{tag}_K{K}_unclipped","broad_pair",1,K,extra=extra+("--no-clip",))
        run("scalar",f"scalar_{tag}_K{K}_refined","broad_pair",1,K,extra=extra+("--refined",))
        run("parent",f"parent_{tag}_refined","broad_pair",1,K,extra=("--refined",))
    write_json(out/"budget.json",dict(total_worker_wall_seconds=used,limit=LIMIT,calls=calls,
                                    completed_cutoffs={f"{k[0]}_P{k[1]}":v for k,v in completed.items()}))
    compare(out)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--phase",choices=["campaign","compile","parent","scalar","analyze"],default="campaign")
    p.add_argument("--out",type=Path)
    p.add_argument("--cell",type=Path)
    p.add_argument("--compiler",type=Path)
    p.add_argument("--parent",type=Path)
    p.add_argument("--task",choices=list(TASKS),default="broad_pair")
    p.add_argument("--order",type=int,default=1)
    p.add_argument("--cutoff",type=int,default=3)
    p.add_argument("--width",type=int,default=16)
    p.add_argument("--seed",type=int,default=SEEDS[0])
    p.add_argument("--refined",action="store_true")
    p.add_argument("--no-clip",action="store_true")
    args=p.parse_args()
    if args.phase=="campaign": campaign(args)
    elif args.phase=="compile": compile_worker(args)
    elif args.phase=="analyze": compare(args.out)
    else: simulation_worker(args)


if __name__=="__main__":
    main()
