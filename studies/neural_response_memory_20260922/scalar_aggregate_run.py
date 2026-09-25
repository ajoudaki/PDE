"""Bounded matched-time dense versus scalar-only aggregate experiment."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import shutil
import sys
import time

import numpy as np
import scipy
from scipy.integrate import DOP853

from scalar_aggregate_engine import (
    ScalarHierarchy, initialize_coefficients, initialize_network, network_fields,
)

HERE = Path(__file__).resolve().parent
CASES = ("equal_mixed_odd", "quadrant_alternating")
SEEDS = (20260920, 20260927)
WIDTHS = (128, 256)
RTOLS = (1e-7, 1e-9)


def clean(value):
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, np.ndarray):
        return clean(value.tolist())
    if isinstance(value, (np.integer, np.floating)):
        return clean(value.item())
    if isinstance(value, float) and not np.isfinite(value):
        return None
    return value


def write_json(path, value):
    Path(path).write_text(json.dumps(clean(value), indent=2, sort_keys=True)+"\n")


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_hash(arrays):
    result = hashlib.sha256()
    for a in arrays:
        a = np.ascontiguousarray(a)
        result.update(str(a.shape).encode())
        result.update(a.tobytes())
    return result.hexdigest()


def task_data(name):
    case = json.loads((HERE / "deep_circle_cases.json").read_text())[name]
    angle = np.deg2rad(case["angles_degrees"])
    return np.column_stack((np.cos(angle), np.sin(angle))), np.array(case["labels"], dtype=float)


def sample_times(end):
    special = np.array([0., .01, .025, .05, .1, .25, .5, 1., 2., 4., 8., 16., 32., 64., 128.])
    return np.unique(np.concatenate((special[special <= end], np.linspace(0., end, 257))))


class DenseReference:
    def __init__(self, params, inputs, labels):
        self.shapes = [p.shape for p in params]
        self.ends = np.cumsum([0]+[p.size for p in params])
        self.inputs, self.labels = inputs.copy(), labels.copy()
        self.n, self.M = params[0].shape[0], len(labels)
        self.initial = self.pack(params)
        self.h0 = [h.copy() for h in network_fields(params, inputs)["h"]]

    def pack(self, params):
        return np.concatenate([p.ravel() for p in params])

    def unpack(self, state):
        return tuple(state[a:b].reshape(shape) for a, b, shape in zip(self.ends[:-1], self.ends[1:], self.shapes))

    def rhs(self, t, state):
        params = self.unpack(state)
        fields = network_fields(params, self.inputs)
        h, delta = fields["h"], fields["delta"]
        r = fields["f"]-self.labels
        velocity = [(-2/self.M)*(delta[0]*r) @ self.inputs]
        velocity.extend((-2/(self.M*self.n))*(delta[k]*r) @ h[k-1].T for k in range(1, len(h)))
        velocity.append((-2/self.M)*(h[-1] @ r))
        return self.pack(velocity)

    def observe(self, state):
        fields = network_fields(self.unpack(state), self.inputs)
        theta = fields["Theta"]
        return dict(f=fields["f"], loss=np.mean((fields["f"]-self.labels)**2),
                    eigenmin=np.linalg.eigvalsh((theta+theta.T)/2)[0],
                    motion=[np.sqrt(np.mean((h-h0)**2)) for h, h0 in zip(fields["h"], self.h0)],
                    kernel=theta)


def scalar_observer(model, labels):
    def observe(state):
        parts = model.unpack(state)
        f = parts["f"]
        theta = parts.get("Theta", model.terminal)
        return dict(f=f, loss=np.mean((f-labels)**2),
                    eigenmin=np.linalg.eigvalsh((theta+theta.T)/2)[0],
                    motion=[np.nan]*3, kernel=theta)
    return observe


def integrate(rhs, initial, observer, times, rtol, *, scalar=False, seconds=120., start=0.):
    """Stream observations; do not retain dense parameter states at all times."""
    begin = time.perf_counter()
    times = np.asarray(times)
    times = times[times >= start]
    state = np.asarray(initial, dtype=float).copy()
    solver = DOP853(rhs, start, state, float(times[-1]), rtol=rtol,
                    atol=rtol/100, max_step=2.)
    ts, fs, losses, eigenmins, motions, kernels, scalar_states = [], [], [], [], [], [], []
    checkpoints = {}
    j, steps, status, message = 0, 0, "complete", ""

    def capture(t, y):
        obs = observer(y)
        ts.append(float(t)); fs.append(np.array(obs["f"], copy=True)); losses.append(obs["loss"])
        eigenmins.append(obs["eigenmin"]); motions.append(obs["motion"]); kernels.append(obs["kernel"])
        if scalar:
            scalar_states.append(np.array(y, copy=True))
        if float(t) in (0., 1., 8., 32., 128., 512.):
            checkpoints["checkpoint_"+str(float(t)).replace(".", "_")] = np.array(y, copy=True)

    if len(times) and times[0] == start:
        capture(start, state); j += 1
    while solver.status == "running":
        if time.perf_counter()-begin > seconds:
            status, message = "wall_cap", "per-trajectory computation-wall cap"; break
        result = solver.step(); steps += 1
        if solver.status == "failed":
            status, message = "solver_failure", str(result); break
        interpolation = None
        while j < len(times) and times[j] <= solver.t:
            if interpolation is None:
                interpolation = solver.dense_output()
            y = interpolation(times[j])
            if not np.isfinite(y).all():
                status, message = "nonfinite", "nonfinite interpolated state"; break
            capture(times[j], y); j += 1
        if status != "complete":
            break
        if not np.isfinite(solver.y).all():
            status, message = "nonfinite", "nonfinite state"; break
        if scalar and (np.max(np.abs(solver.y[:len(fs[0])])) >= 10 or np.max(np.abs(solver.y)) >= 1e12):
            status, message = "state_escape", "predeclared scalar escape threshold"; break
    arrays = dict(times=np.array(ts), f=np.array(fs), loss=np.array(losses),
                  eigenmin=np.array(eigenmins), motion=np.array(motions), kernel=np.array(kernels),
                  final_state=solver.y, **checkpoints)
    if scalar:
        arrays["states"] = np.array(scalar_states)
    return arrays, dict(status=status, message=message, final_time=solver.t,
                        observations=len(ts), accepted_steps=steps, nfev=solver.nfev,
                        compute_seconds=time.perf_counter()-begin, rtol=rtol, atol=rtol/100,
                        max_step=2., scalar=scalar)


def tolerance_gate(coarse, fine, error):
    count = min(len(coarse["times"]), len(fine["times"]))
    if not count or not np.array_equal(coarse["times"][:count], fine["times"][:count]):
        return dict(pass_gate=False, reason="no matching sampled-time prefix")
    change = np.sqrt(np.mean((coarse["f"][:count]-fine["f"][:count])**2, axis=1)).max()
    loss_change = np.max(np.abs(coarse["loss"][:count]-fine["loss"][:count]))
    return dict(pass_gate=bool(change <= .002 and change <= .1*max(error, 1e-6) and loss_change <= .002),
                prediction_change=change, loss_change=loss_change, paired_error=error)


def paired_error(scalar, dense, end=None):
    count = min(len(scalar["times"]), len(dense["times"]))
    if end is not None:
        count = min(count, int(np.searchsorted(dense["times"][:count], end, side="right")))
    if not count:
        return np.inf, np.inf
    if not np.array_equal(scalar["times"][:count], dense["times"][:count]):
        raise ValueError("comparison times differ")
    prediction = np.sqrt(np.mean((scalar["f"][:count]-dense["f"][:count])**2, axis=1)).max()
    loss = np.max(np.abs(scalar["loss"][:count]-dense["loss"][:count]))
    return float(prediction), float(loss)


def initialize_with_timeout(params, inputs, seconds):
    def expired(signum, frame):
        raise TimeoutError("coefficient-initialization wall cap")
    previous = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        return initialize_coefficients(params, inputs, order=4)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def run_configuration(directory, case, width, seed, *, end=128., budget=3600., pilot=False):
    directory.mkdir(parents=True, exist_ok=False)
    begin = time.perf_counter()
    inputs, labels = task_data(case)
    params = initialize_network(width, 2, depth=3, seed=seed)
    reference = DenseReference(params, inputs, labels)
    init_begin = time.perf_counter()
    coefficients = initialize_with_timeout(params, inputs, min(120., budget))
    init_seconds = time.perf_counter()-init_begin
    np.savez_compressed(directory / "coefficients.npz", **coefficients, inputs=inputs, labels=labels)
    meta = dict(case=case, width=width, seed=seed, depth=3, M=len(labels), end=end, pilot=pilot,
                initialization_hash=array_hash(params), coefficients_hash=array_hash(list(coefficients.values())),
                initialization_seconds=init_seconds, dense_parameter_count=len(reference.initial),
                source_hashes={p.name: file_hash(p) for p in (
                    HERE / "scalar_aggregate_engine.py", Path(__file__), HERE / "SCALAR_AGGREGATE_PROTOCOL.md",
                    HERE / "SCALAR_AGGREGATE_CANDIDATE_THEORY.md", HERE / "deep_circle_cases.json")},
                environment=dict(python=sys.version, executable=sys.executable, numpy=np.__version__,
                                 scipy=scipy.__version__, platform=platform.platform(),
                                 threads={k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")}))
    write_json(directory / "configuration.json", meta)
    times = sample_times(end)
    records, runs = {}, {}

    def run(name, level):
        if time.perf_counter()-begin >= budget:
            raise TimeoutError("configuration exhausted remaining campaign budget")
        rtol = (1e-7, 1e-9, 1e-11)[level]
        model = None if name == "dense" else ScalarHierarchy(coefficients, labels, order=int(name[-1]))
        rhs = reference.rhs if model is None else model.rhs
        initial = reference.initial if model is None else model.initial_state()
        observer = reference.observe if model is None else scalar_observer(model, labels)
        arrays, record = integrate(rhs, initial, observer, times, rtol, scalar=model is not None,
                                   seconds=min(120., budget-(time.perf_counter()-begin)))
        if model is not None:
            record["storage"] = model.counts()
        record.update(model=name, level=level)
        target = directory / (name+"_resolution"+str(level))
        target.mkdir()
        np.savez_compressed(target / "trajectory.npz", **arrays)
        write_json(target / "result.json", record)
        records[name,level], runs[name,level] = record, arrays
        print(json.dumps(dict(event="run",case=case,width=width,seed=seed,**record)), flush=True)

    for name in ("dense", "order2", "order3", "order4"):
        for level in ((1,) if pilot else (0,1)):
            run(name,level)
    latest = {name:1 for name in ("dense","order2","order3","order4")}
    if not pilot:
        refine = set()
        for name in ("order2","order3","order4"):
            error,_ = paired_error(runs[name,1],runs["dense",1])
            if not tolerance_gate(runs[name,0],runs[name,1],error)["pass_gate"]:
                refine.add(name)
            if not tolerance_gate(runs["dense",0],runs["dense",1],error)["pass_gate"]:
                refine.add("dense")
        for name in ("dense","order2","order3","order4"):
            if name in refine:
                run(name,2); latest[name]=2
    dense = runs["dense",latest["dense"]]
    summary = dict(configuration=meta, latest_resolution=latest,
                   dense_complete=records["dense",latest["dense"]]["status"]=="complete",
                   dense_motion_max=np.max(dense["motion"],axis=0), orders={})
    for name in ("order2","order3","order4"):
        level = latest[name]; trajectory=runs[name,level]
        prediction,loss = paired_error(trajectory,dense)
        complete=records[name,level]["status"]=="complete" and summary["dense_complete"]
        if pilot:
            scalar_gate=dense_gate={"pass_gate":False,"reason":"feasibility pilot"}
        else:
            scalar_gate=tolerance_gate(runs[name,level-1],trajectory,prediction)
            dl=latest["dense"]
            dense_gate=tolerance_gate(runs["dense",dl-1],dense,prediction)
        valid=scalar_gate["pass_gate"] and dense_gate["pass_gate"]
        failures = {"state_escape", "nonfinite", "solver_failure"}
        repeated_failure=not complete and not pilot and all(records[name,k]["status"] in failures for k in (0,1))
        verdict=("adverse" if repeated_failure else "inconclusive")
        if complete and valid:
            verdict="practical_agreement" if prediction<=.1 and loss<=.05 else ("adverse" if prediction>.2 or loss>.1 else "inconclusive")
        summary["orders"][name]=dict(prediction_error=prediction, loss_error=loss, full_horizon_complete=complete,
            validity_pass=valid, verdict=verdict, scalar_gate=scalar_gate, dense_gate=dense_gate,
            status=records[name,level]["status"], final_time=records[name,level]["final_time"],
            prefixes={str(t):dict(**dict(zip(("prediction_error","loss_error"),paired_error(trajectory,dense,t))),
                prefix_complete=bool(trajectory["times"][-1]>=t and dense["times"][-1]>=t),
                last_compared_time=float(min(t,trajectory["times"][-1],dense["times"][-1])))
                for t in (1,8,32,128) if t<=end},
            min_kernel_eigenvalue=np.min(trajectory["eigenmin"]),
            nonlinear_gate=bool(np.max(summary["dense_motion_max"])>=.1))
    frozen=summary["orders"]["order2"]["prediction_error"]
    q4=summary["orders"]["order4"]
    q4["nonlinear_improvement"]=bool(q4["full_horizon_complete"] and q4["validity_pass"] and q4["prediction_error"]<=frozen/2 and frozen>=.05 and q4["nonlinear_gate"])
    summary["total_seconds"]=time.perf_counter()-begin
    summary["peak_process_rss_bytes"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
    write_json(directory / "summary.json",summary)
    return summary


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=("pilot","campaign"),required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--budget",type=float,default=3600.)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    sources=args.output/"sources"
    sources.mkdir()
    for name in ("scalar_aggregate_engine.py", "scalar_aggregate_run.py", "SCALAR_AGGREGATE_PROTOCOL.md",
                 "SCALAR_AGGREGATE_CANDIDATE_THEORY.md", "deep_circle_cases.json"):
        shutil.copy2(HERE/name,sources/name)
    started=time.perf_counter(); summaries=[]
    configurations=[("equal_mixed_odd",32,20260920)] if args.mode=="pilot" else [
        (case,width,seed) for width in WIDTHS for case in CASES for seed in SEEDS]
    for case,width,seed in configurations:
        remaining=args.budget-(time.perf_counter()-started)
        if remaining<=0:
            break
        name=case+"_n"+str(width)+"_seed"+str(seed)
        try:
            summaries.append(run_configuration(args.output/name,case,width,seed,
                end=.25 if args.mode=="pilot" else 128.,budget=remaining,pilot=args.mode=="pilot"))
        except Exception as exc:
            write_json(args.output/(name+"_failure.json"),dict(error=repr(exc),seconds=time.perf_counter()-started))
            raise
        write_json(args.output/"campaign.json",dict(mode=args.mode,configurations=summaries,seconds=time.perf_counter()-started))
    print(json.dumps(dict(event="finished",mode=args.mode,configurations=len(summaries),seconds=time.perf_counter()-started)),flush=True)


if __name__=="__main__":
    main()
