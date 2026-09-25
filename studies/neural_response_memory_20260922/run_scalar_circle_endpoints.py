"""Matched-training-loss, full-circle test of the frozen derivative closure."""
import argparse
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import signal
import sys
import time

import numpy as np
import scipy
from scipy.integrate import DOP853
from scipy.optimize import brentq

from scalar_aggregate_engine import initialize_network, initialize_coefficients
from scalar_aggregate_run import DenseReference, task_data, write_json, file_hash, array_hash
from scalar_circle_probe_engine import (SignatureHierarchy, initialize_probe_coefficients,
    forward_only, fit_fourier_coefficients, evaluate_fourier)

HERE = Path(__file__).resolve().parent
CASES = ("equal_mixed_odd", "quadrant_alternating")
TARGET = 1e-6
END = 2048.
RTOLS = (1e-7, 1e-9, 1e-11)


def circle(angles):
    """U=x/sqrt(2)=(cos(angle),sin(angle)), exactly as the original campaign."""
    return np.column_stack((np.cos(angles), np.sin(angles)))


def rms(values):
    return float(np.sqrt(np.mean(np.abs(values)**2)))


def deadline_call(call, seconds):
    if seconds <= 0:
        raise TimeoutError("global budget exhausted")
    def expired(signum, frame):
        raise TimeoutError("initializer wall cap")
    previous = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        return call()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def integrate_endpoint(rhs, initial, predictions, labels, rtol, seconds):
    """Stream accepted steps and use local dense interpolation at the loss event."""
    started = time.perf_counter()
    loss = lambda state: float(np.mean((predictions(state)-labels)**2))
    solver = DOP853(rhs, 0., initial.copy(), END, rtol=rtol, atol=rtol/100, max_step=2.)
    times, losses = [0.], [loss(initial)]
    status, message = "time_cap", ""
    state, final_time = initial.copy(), 0.
    if losses[0] <= TARGET:
        return dict(state=state,time=0.,train_f=predictions(state),times=np.array(times),losses=np.array(losses)), dict(
            status="fitted",message="initial state meets target",time=0.,loss=losses[0],
            rtol=rtol,atol=rtol/100,max_step=2.,nfev=solver.nfev,seconds=time.perf_counter()-started)
    while solver.status == "running":
        if time.perf_counter()-started >= seconds:
            status = "wall_cap"; break
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024 >= 2*1024**3:
            status = "memory_cap"; break
        old_time, old_loss = solver.t, losses[-1]
        message = solver.step() or ""
        if solver.status == "failed":
            status = "solver_failure"; break
        if not np.isfinite(solver.y).all():
            status = "nonfinite"; break
        state, final_time = solver.y.copy(), float(solver.t)
        current = loss(state)
        if old_loss > TARGET and current <= TARGET:
            interpolate = solver.dense_output()
            final_time = float(brentq(lambda t: loss(interpolate(t))-TARGET,
                                     old_time, solver.t, xtol=1e-12, rtol=1e-14))
            state = interpolate(final_time)
            current, status = loss(state), "fitted"
        times.append(final_time); losses.append(current)
        if status == "fitted":
            break
    return dict(state=state, time=final_time, train_f=predictions(state),
                times=np.array(times), losses=np.array(losses)), dict(
        status=status, message=message, time=final_time, loss=loss(state),
        rtol=rtol, atol=rtol/100, max_step=2., nfev=solver.nfev,
        seconds=time.perf_counter()-started)


def numerical_gate(first, second, error):
    change = rms(first["grid"]-second["grid"])
    return dict(change=change, passed=bool(change <= .002 and change <= .1*max(error, 1e-6)))


def run_configuration(directory, case, width, seed, deadline):
    directory.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    inputs, labels = task_data(case)
    params = initialize_network(width, 2, depth=3, seed=seed)
    reference = DenseReference(params, inputs, labels)
    angles = 2*np.pi*np.arange(1024)/1024
    off_angles = 2*np.pi*(np.arange(32)+np.sqrt(2)/10)/32
    probe_inputs = np.vstack((circle(angles), circle(off_angles), inputs))
    init_started = time.perf_counter()
    def initialize():
        return (initialize_coefficients(params, inputs, order=4),
                initialize_probe_coefficients(params, inputs, probe_inputs, order=4))
    coefficients, probe = deadline_call(initialize, min(60., deadline-time.perf_counter()))
    initial_seconds = time.perf_counter()-init_started
    np.savez_compressed(directory/"initial_coefficients.npz", **coefficients,
                        inputs=inputs, labels=labels)
    np.savez_compressed(directory/"probe_coefficients.npz", **probe,
                        angles=angles, off_angles=off_angles, probe_inputs=probe_inputs)
    training_probe_checks = {key: float(np.max(np.abs(probe[key][-len(labels):]-value)))
                             for key, value in coefficients.items()}
    if max(training_probe_checks.values()) > 1e-10:
        raise AssertionError("probe/training initializer mismatch")
    metadata = dict(case=case, width=width, seed=seed, M=len(labels), target=TARGET,
        time_cap=END, initial_seconds=initial_seconds, initialization_hash=array_hash(params),
        training_probe_checks=training_probe_checks, dense_parameter_count=reference.initial.size,
        input_convention="U=(cos(angle),sin(angle))=x/sqrt(2)",
        environment=dict(python=sys.version, executable=sys.executable, numpy=np.__version__,
            scipy=scipy.__version__, platform=platform.platform(),
            threads={key:os.environ.get(key) for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")}))
    write_json(directory/"configuration.json", metadata)
    models = {name: SignatureHierarchy(coefficients, labels, order=int(name[-1]))
              for name in ("order2", "order4")}
    records, runs = {}, {}

    def run(name, level):
        remaining = deadline-time.perf_counter()
        if remaining <= 0:
            raise TimeoutError("campaign budget exhausted")
        model = models.get(name)
        if model is None:
            rhs, initial = reference.rhs, reference.initial
            prediction = lambda state: forward_only(reference.unpack(state), inputs)
        else:
            rhs, initial = model.rhs, model.initial_state()
            prediction = lambda state: model.training.unpack(model.training_state(state))["f"]
        arrays, record = integrate_endpoint(rhs, initial, prediction, labels, RTOLS[level], min(60.,remaining))
        all_outputs = (forward_only(reference.unpack(arrays["state"]), probe_inputs) if model is None
                       else model.readout(probe, arrays["state"]))
        arrays.update(grid=all_outputs[:len(angles)], off_grid=all_outputs[len(angles):len(angles)+32],
                      train_probe=all_outputs[-len(labels):])
        record.update(model=name, level=level, training_readout_gap=rms(arrays["train_probe"]-arrays["train_f"]))
        np.savez_compressed(directory/(name+"_resolution"+str(level)+".npz"), **arrays)
        write_json(directory/(name+"_resolution"+str(level)+".json"), record)
        records[name,level], runs[name,level] = record, arrays
        print(json.dumps(dict(event="endpoint",case=case,width=width,seed=seed,**record)),flush=True)

    for name in ("dense", "order2", "order4"):
        for level in (0,1):
            run(name,level)
    latest = {name:1 for name in ("dense", "order2", "order4")}
    refine = set()
    for name in ("order2","order4"):
        if records[name,1]["status"] == records["dense",1]["status"] == "fitted":
            error = rms(runs[name,1]["grid"]-runs["dense",1]["grid"])
            for key in (name,"dense"):
                if not numerical_gate(runs[key,0],runs[key,1],error)["passed"] or records[key,0]["status"] != "fitted":
                    refine.add(key)
    for name in ("dense","order2","order4"):
        if name in refine:
            run(name,2); latest[name]=2

    # Probe-only spatial refinements do not change any training state.
    spatial = {}
    need_more_angles = False
    dense = runs["dense",latest["dense"]]
    for name in ("order2","order4"):
        diff = runs[name,latest[name]]["grid"]-dense["grid"]
        error, coarse = rms(diff), rms(diff[::2])
        change = abs(error-coarse)
        passed = change <= .001 and change <= .01*max(error,1e-6)
        spatial[name] = dict(grid_size=1024, change=change, passed=bool(passed))
        need_more_angles |= not passed
    if need_more_angles:
        angles = 2*np.pi*np.arange(2048)/2048
        probe_inputs = np.vstack((circle(angles),circle(off_angles),inputs))
        probe = deadline_call(lambda: initialize_probe_coefficients(params,inputs,probe_inputs,order=4),
                              min(60.,deadline-time.perf_counter()))
        np.savez_compressed(directory/"probe_coefficients_refined.npz", **probe,
                            angles=angles,off_angles=off_angles,probe_inputs=probe_inputs)
        for name,level in list(runs):
            a = runs[name,level]
            values = (forward_only(reference.unpack(a["state"]),probe_inputs) if name=="dense"
                      else models[name].readout(probe,a["state"]))
            a["grid"] = values[:len(angles)]
            np.savez_compressed(directory/(name+"_spatial_refined_resolution"+str(level)+".npz"), **a)
        dense = runs["dense",latest["dense"]]
        for name in ("order2","order4"):
            diff = runs[name,latest[name]]["grid"]-dense["grid"]
            error, coarse = rms(diff), rms(diff[::2]); change=abs(error-coarse)
            spatial[name] = dict(grid_size=2048, change=change,
                                passed=bool(change<=.001 and change<=.01*max(error,1e-6)))

    fourier, summaries = {}, {}
    for name in ("order2","order4"):
        level, model = latest[name], models[name]
        scalar = runs[name,level]
        checks = []
        for mode in (64,128,256):
            retained = ("f","Theta") if model.order==2 else ("f","Theta","C","Q")
            fc = fit_fourier_coefficients({key:probe[key][:len(angles)] for key in retained},mode)
            endpoint_fc = model.readout(fc,scalar["state"])
            fg = evaluate_fourier(endpoint_fc,angles)
            fo = evaluate_fourier(endpoint_fc,off_angles)
            grid_error, off_error = fg-scalar["grid"], fo-scalar["off_grid"]
            check = dict(mode=mode,grid_rms=rms(grid_error),off_grid_rms=rms(off_error),
                         maximum=float(max(np.max(np.abs(grid_error)),np.max(np.abs(off_error)))))
            check["rms"] = max(check["grid_rms"],check["off_grid_rms"])
            check["passed"] = check["rms"]<=1e-5 and check["maximum"]<=1e-4
            checks.append(check)
            if check["passed"]:
                break
        fourier[name] = dict(checks=checks,passed=checks[-1]["passed"],mode=mode,
                            real_coefficient_entries=sum(v.size*2 for v in fc.values()),
                            endpoint_real_entries=2*endpoint_fc.size)
        np.savez_compressed(directory/(name+"_fourier.npz"),**fc,endpoint=endpoint_fc,angles=angles,
                            endpoint_grid=fg,endpoint_off_grid=fo)
        fitted = records[name,level]["status"]==records["dense",latest["dense"]]["status"]=="fitted"
        error = rms(scalar["grid"]-dense["grid"])
        scalar_gate = numerical_gate(runs[name,level-1],scalar,error)
        dl=latest["dense"]
        dense_gate = numerical_gate(runs["dense",dl-1],dense,error)
        statuses_match = records[name,level-1]["status"]==records[name,level]["status"] and records["dense",dl-1]["status"]==records["dense",dl]["status"]
        valid = scalar_gate["passed"] and dense_gate["passed"] and spatial[name]["passed"] and fourier[name]["passed"] and statuses_match
        verdict = "no_matched_endpoint" if not fitted else ("numerically_inconclusive" if not valid else
            ("agreement" if error<=.1 else "adverse" if error>.2 else "inconclusive"))
        summaries[name] = dict(fitted_pair=fitted, circle_rms=error,
            relative_rms=error/max(rms(dense["grid"]),1e-30),dense_function_rms=rms(dense["grid"]),
            maximum_grid_error=float(np.max(np.abs(scalar["grid"]-dense["grid"]))),
            scalar_status=records[name,level]["status"],dense_status=records["dense",dl]["status"],
            scalar_time=records[name,level]["time"],dense_time=records["dense",dl]["time"],
            scalar_loss=records[name,level]["loss"],dense_loss=records["dense",dl]["loss"],
            scalar_gate=scalar_gate,dense_gate=dense_gate,quadrature=spatial[name],fourier=fourier[name],
            valid=bool(valid),verdict=verdict)
    summary = dict(configuration=metadata,latest=latest,models=summaries,
                   seconds=time.perf_counter()-started,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
    write_json(directory/"summary.json",summary)
    print(json.dumps(dict(event="configuration",case=case,width=width,seed=seed,
                          models={k:v["verdict"] for k,v in summaries.items()},seconds=summary["seconds"])),flush=True)
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--mode",choices=("campaign","reproduction"),default="campaign")
    parser.add_argument("--budget",type=float,default=780.)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    sources=args.output/"sources"; sources.mkdir()
    names=(Path(__file__).name,"scalar_circle_probe_engine.py","scalar_aggregate_engine.py",
           "scalar_aggregate_run.py","SCALAR_CIRCLE_ENDPOINT_PROTOCOL.md","deep_circle_cases.json")
    for name in names:
        shutil.copy2(HERE/name,sources/name)
    write_json(args.output/"manifest.json",dict(source_hashes={name:file_hash(HERE/name) for name in names},
              command=sys.argv,cwd=os.getcwd(),mode=args.mode,budget=args.budget))
    started=time.perf_counter(); deadline=started+args.budget
    configurations=[(case,width,seed) for case in CASES for width in (128,256) for seed in (20260920,20260927)]
    if args.mode=="reproduction":
        configurations=configurations[:1]
    summaries=[]
    for case,width,seed in configurations:
        key=case+"_n"+str(width)+"_seed"+str(seed)
        try:
            summaries.append(run_configuration(args.output/key,case,width,seed,deadline))
        except (TimeoutError,MemoryError) as exc:
            write_json(args.output/(key+"_incomplete.json"),dict(error=str(exc),seconds=time.perf_counter()-started))
            break
        write_json(args.output/"campaign.json",dict(configurations=summaries,seconds=time.perf_counter()-started))
    print(json.dumps(dict(event="finished",configurations=len(summaries),seconds=time.perf_counter()-started)),flush=True)


if __name__=="__main__":
    main()
