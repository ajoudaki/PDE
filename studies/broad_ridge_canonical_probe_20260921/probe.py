#!/usr/bin/env python3
"""Study-only canonical tanh GF and fixed-dictionary Galerkin probe.

Inputs to forward/rhs are normalized U=X/sqrt(d); stored data include both.
No training happens on import. CLI: make-data, benchmark, run.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.integrate import DOP853
from scipy.linalg import solve_triangular

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.finite_network import initialize

MODELS = ("closure1024", "width244", "width492", "width1024")
SEEDS = dict(target=2026092101, calibration=2026092102, train=2026092103,
             passive=2026092104, initialization=20260921)
CHECKPOINTS = (0, 1, 3, 10, 30, 100, 300, 1000, 3000, 5000)


def json_write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def manifest():
    paths = [Path(__file__), ROOT / "code/pde/finite_network.py",
             ROOT / "docs/NOTATION.md", Path(__file__).with_name("PROTOCOL.md")]
    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except subprocess.SubprocessError:
        head = "unavailable"
    return {"git_head": head, "source_sha256": {str(p.relative_to(ROOT)): sha256(p)
            for p in paths if p.exists()}, "python": platform.python_version(),
            "numpy": np.__version__, "scipy": scipy.__version__,
            "threads": {k: os.environ[k] for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}}


def target(X, V, a, C=1.0):
    """Raw Gaussian inputs, unit directions; 1/sqrt(K) is absorbed by calibration."""
    return C * (a @ np.tanh(V.T @ X)) / np.sqrt(a.size)


def make_data(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    d, K, m, mcal = 64, 768, 2048, 32768
    rng = np.random.default_rng(SEEDS["target"])
    V = rng.standard_normal((d, K))
    V /= np.linalg.norm(V, axis=0)
    signs = rng.choice(np.array([-1.0, 1.0]), size=K)
    a = signs - V.T @ np.linalg.solve(V @ V.T, V @ signs)
    a *= np.sqrt(K) / np.linalg.norm(a)
    Xcal = np.random.default_rng(SEEDS["calibration"]).standard_normal((d, mcal))
    rawcal = np.concatenate([target(Xcal[:, j:j+2048], V, a) for j in range(0, mcal, 2048)])
    calibration_rms = float(np.sqrt(np.mean(rawcal**2)))
    C = 1.0 / calibration_rms
    arrays = dict(V=V, a=a, signs=signs, C=np.array(C), calibration_rms=np.array(calibration_rms),
                  X_calibration=Xcal, y_calibration=C*rawcal)
    for split in ("train", "passive"):
        X = np.random.default_rng(SEEDS[split]).standard_normal((d, m))
        arrays.update({f"X_{split}": X, f"U_{split}": X/np.sqrt(d), f"y_{split}": target(X,V,a,C)})
    np.savez(output / "data.npz", **arrays)
    info = dict(d=d, K=K, samples_train=m, samples_passive=m, samples_calibration=mcal,
                seeds=SEEDS, C=C, calibration_rms_before_C=calibration_rms,
                target_formula="C/sqrt(K) * a @ tanh(V.T @ X_raw)",
                linear_cancellation_norm=float(np.linalg.norm(V@a)),
                a_norm=float(np.linalg.norm(a)), provenance=manifest())
    info["data_sha256"] = sha256(output / "data.npz")
    json_write(output / "data.json", info)
    print(json.dumps(info), flush=True)
    return arrays


def pack(*blocks):
    return np.concatenate([np.ravel(block) for block in blocks])


def unpack(state, model):
    blocks, start = [], 0
    for shape in model["shapes"]:
        size = int(np.prod(shape))
        blocks.append(state[start:start+size].reshape(shape))
        start += size
    if start != state.size:
        raise ValueError("state size differs from model shapes")
    return tuple(blocks)


def build_model(name, data=None, d=64, seed=20260921):
    if data is not None:
        d = data["U_train"].shape[0]
    if name not in MODELS:
        raise ValueError(f"unknown model {name}")
    n = 1024 if name.startswith("closure") else int(name[5:])
    p = initialize(n, 2, d, seed=seed)
    W, A, c = p.weights[0], p.weights[1], p.readout
    model = dict(name=name, kind="closure" if name.startswith("closure") else "dense",
                 n=n, d=d, W0=W.copy(), A0=A.copy(), c0=c.copy())
    middle = A
    if model["kind"] == "closure":
        H = np.tanh(W)
        U = np.tanh(A@H)
        R = np.tanh(A.T@U)
        F1, F2 = np.column_stack((np.ones(n),H,R)), np.column_stack((np.ones(n),U))
        for index, F in ((1,F1),(2,F2)):
            gram = F.T@F/n
            chol = np.linalg.cholesky(gram+np.eye(F.shape[1])/4096)
            model[f"B{index}"] = solve_triangular(chol, F.T, lower=True).T
            model[f"F{index}"] = F
            model[f"L{index}"] = chol
        middle = model["B2"].T@A@model["B1"]/n
        model["M0"] = middle.copy()
    model["shapes"] = (W.shape, middle.shape, c.shape)
    model["initial_state"] = pack(W,middle,c)
    model["state0"] = model["initial_state"]
    return model


def fields(state, model, U):
    W, middle, c = unpack(state, model)
    z1 = W@U
    h = np.tanh(z1)
    if model["kind"] == "closure":
        q = model["B1"].T@h/model["n"]
        z = model["B2"]@(middle@q)
    else:
        q, z = h, middle@h
    g = np.tanh(z)
    return h, q, g, c@g/model["n"], z1, z


def forward(state, model, U):
    return fields(state,model,U)[3]


def sech2(z):
    u = np.exp(-np.abs(z))
    return (2*u/(1+u*u))**2


def rhs(t, state, model, U, y, *, with_loss=False):
    """Physical -D grad(unhalved mean square), D=(n,1,n)."""
    W, middle, c = unpack(state,model)
    h, q, g, pred, z1, z2 = fields(state,model,U)
    r = pred-y
    e = (c[:,None]*sech2(z2))*r[None,:]
    n, m = model["n"], y.size
    if model["kind"] == "closure":
        e2 = model["B2"].T@e
        back = model["B1"]@(middle.T@e2)/n
        dm = -2*(e2@q.T)/(m*n)
    else:
        back = middle.T@e
        dm = -2*(e@h.T)/(m*n)
    dw = -2*(sech2(z1)*back)@U.T/m
    dc = -2*(g@r)/m
    velocity = pack(dw,dm,dc)
    return (velocity,float(np.mean(r*r))) if with_loss else velocity


def state_metrics(state, model, data):
    blocks = unpack(state,model)
    initial = unpack(model["initial_state"],model)
    pred = {s:forward(state,model,data[f"U_{s}"]) for s in ("train","passive")}
    norms = np.linalg.norm(blocks[0],axis=1)
    norm0 = np.linalg.norm(initial[0],axis=1)
    names = ("W","M" if model["kind"] == "closure" else "A","c")
    metrics = {f"mse_{s}":float(np.mean((pred[s]-data[f"y_{s}"])**2)) for s in pred}
    metrics["block_rms_motion"] = {k:float(np.sqrt(np.mean((b-b0)**2))) for k,b,b0 in zip(names,blocks,initial)}
    metrics["block_relative_frobenius_motion"] = {k:float(np.linalg.norm(b-b0)/np.linalg.norm(b0)) for k,b,b0 in zip(names,blocks,initial)}
    metrics["W_row_norms"] = dict(median=float(np.median(norms)), maximum=float(norms.max()),
        median_ratio_to_initial=float(np.median(norms/norm0)), maximum_ratio_to_initial=float(np.max(norms/norm0)),
        median_statistic_ratio=float(np.median(norms)/np.median(norm0)), maximum_statistic_ratio=float(norms.max()/norm0.max()))
    return metrics,pred


class WallTimeout(RuntimeError):
    pass


def run(args):
    started = time.monotonic()
    output = Path(args.output)
    output.mkdir(parents=True,exist_ok=False)
    data_path = Path(args.data)
    if data_path.is_dir():
        data_path /= "data.npz"
    with np.load(data_path) as archive:
        data = {k:archive[k] for k in archive.files}
    model = build_model(args.model)
    y = model["initial_state"].copy()
    rtol,atol,max_step = (1e-5,1e-8,500.0) if args.level == "primary" else (1e-7,1e-10,250.0)
    config = dict(model=args.model,level=args.level,horizon=args.horizon,wall_seconds=args.wall_seconds,
        export_reserve_seconds=10,rtol=rtol,atol=atol,max_step=max_step,solver="DOP853",loss="unhalved MSE",
        mobilities=[model["n"],1,model["n"]],state_shapes=model["shapes"],state_scalars=y.size,
        data_path=str(data_path.resolve()),data_sha256=sha256(data_path),seeds=SEEDS,provenance=manifest(),argv=sys.argv)
    json_write(output/"config.json",config)
    np.savez(output/"source.npz",**{k:v for k,v in model.items() if isinstance(v,np.ndarray)})
    deadline = started+max(0,args.wall_seconds-10)
    nfev,steps,t,final_rhs,last_eval_loss = 0,0,0.0,None,None
    rows,step_rows,checkpoint_states,checkpoint_predictions = [],[],[],[]
    status,message = "complete","horizon reached"

    def timed_rhs(ti,yi):
        nonlocal nfev,last_eval_loss
        if time.monotonic() >= deadline:
            raise WallTimeout("wall allowance reached; exporting last accepted state")
        velocity,last_eval_loss = rhs(ti,yi,model,data["U_train"],data["y_train"],with_loss=True)
        nfev += 1
        if not np.all(np.isfinite(velocity)):
            raise FloatingPointError("nonfinite RHS")
        return velocity

    def save_state(label,ti,yi,velocity):
        metrics,preds = state_metrics(yi,model,data)
        if label == "final":
            np.savez(output/"final.npz",time=np.array(ti),state=yi,rhs=velocity,
                     train_prediction=preds["train"],passive_prediction=preds["passive"])
        else:
            checkpoint_states.append(yi.copy())
            checkpoint_predictions.append(preds)
        row = dict(t=ti,nfev=nfev,accepted_steps=steps,wall_seconds=time.monotonic()-started,**metrics)
        print(json.dumps(dict(event=label,**row)),flush=True)
        return row

    try:
        final_rhs = timed_rhs(t,y)
        rows.append(save_state("checkpoint_0",t,y,final_rhs))
        previous_loss = rows[-1]["mse_train"]
        bounds = sorted({float(v) for v in CHECKPOINTS if 0<v<=args.horizon} | {float(args.horizon)})
        next_step = None
        with (output/"accepted.csv").open("w") as log:
            log.write("time,loss\n")
            log.write(f"{t:.17g},{previous_loss:.17g}\n")
            for bound in bounds:
                if bound <= t:
                    continue
                first_step = None if next_step is None else min(next_step,bound-t,max_step)
                solver = DOP853(timed_rhs,t,y,bound,rtol=rtol,atol=atol,max_step=max_step,first_step=first_step)
                while solver.status == "running":
                    solver.step()
                    if solver.status == "failed":
                        raise RuntimeError("DOP853 step failed")
                    t,y,final_rhs = float(solver.t),solver.y,solver.f
                    steps += 1
                    # DOP853's final function evaluation is at the accepted state.
                    loss = float(last_eval_loss)
                    step = dict(t=t,mse_train=loss,loss_increase=loss-previous_loss,nfev=nfev,
                                wall_seconds=time.monotonic()-started)
                    log.write(f"{t:.17g},{loss:.17g}\n")
                    log.flush()
                    step_rows.append(step)
                    previous_loss = loss
                    next_step = solver.h_abs
                rows.append(save_state(f"checkpoint_{bound:g}",t,y,final_rhs))
    except WallTimeout as error:
        status,message = "wall_censored",str(error)
    except Exception as error:
        status,message = "failed",f"{type(error).__name__}: {error}"
    if final_rhs is None:
        final_rhs = rhs(t,y,model,data["U_train"],data["y_train"])
    final = save_state("final",t,y,final_rhs)
    np.savez(output/"checkpoints.npz",times=np.array([r["t"] for r in rows]),
             states=np.array(checkpoint_states),
             train_prediction=np.array([p["train"] for p in checkpoint_predictions]),
             passive_prediction=np.array([p["passive"] for p in checkpoint_predictions]),
             train_loss=np.array([r["mse_train"] for r in rows]),
             passive_loss=np.array([r["mse_passive"] for r in rows]))
    result = dict(config=config,status=status,message=message,checkpoints=rows,final=final,
        nfev=nfev,accepted_steps=steps,wall_seconds=time.monotonic()-started,
        maximum_accepted_loss_increase=max([r["loss_increase"] for r in step_rows]+[0.0]),
        accepted_step_diagnostics=step_rows,
        checkpoint_provenance="solver accepted states; no dense output; restarted only at prescribed checkpoint bounds")
    json_write(output/"result.json",result)
    return result


def benchmark(args):
    with np.load(args.data) as archive:
        U,y = archive["U_train"],archive["y_train"]
    records = []
    for name in MODELS:
        start = time.monotonic()
        model = build_model(name)
        setup = time.monotonic()-start
        start = time.monotonic()
        velocity = rhs(0,model["initial_state"],model,U,y)
        records.append(dict(model=name,setup_seconds=setup,rhs_seconds=time.monotonic()-start,
                            scalars=model["initial_state"].size,rhs_rms=float(np.sqrt(np.mean(velocity**2)))))
    print(json.dumps(records,indent=2),flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command",required=True)
    data = commands.add_parser("make-data")
    data.add_argument("--output",required=True)
    bench = commands.add_parser("benchmark")
    bench.add_argument("--data",required=True)
    train = commands.add_parser("run")
    train.add_argument("--data",required=True)
    train.add_argument("--model",choices=MODELS,required=True)
    train.add_argument("--output",required=True)
    train.add_argument("--level",choices=("primary","fine"),required=True)
    train.add_argument("--horizon",type=float,default=5000)
    train.add_argument("--wall-seconds",type=float,default=120)
    args = parser.parse_args()
    if args.command == "make-data":
        make_data(args.output)
    elif args.command == "benchmark":
        benchmark(args)
    elif args.horizon < 0 or args.wall_seconds < 10:
        parser.error("horizon must be nonnegative and wall allowance at least ten seconds")
    else:
        run(args)


if __name__ == "__main__":
    main()
