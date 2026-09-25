"""Bounded single-passive-input experiment; see SCALAR_POINT_PROTOCOL.md."""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import hashlib
import json
import pickle
import platform
import sys
import time
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scalar_fourier_reference import DenseReference, PopulationReference, initialize

ANGLES = np.deg2rad([10., 125.])
U = np.stack([np.cos(ANGLES), np.sin(ANGLES)])
LABELS = np.array([1., -1.])
TEST = np.array([np.cos(np.pi/3), np.sin(np.pi/3)])
CONFIG = dict(width=16, seed=20260920, hidden_layers=3, activation="tanh", P=1,
              train_angles_degrees=[10,125], labels=[1,-1], test_angle_degrees=60,
              test_training_weight=0, training_denominator=2, cutoffs=[5,7],
              max_patterns=6000, max_terms=2000000, compile_seconds=120,
              solve_seconds=120, total_numerical_budget_seconds=600,
              horizon=40, target_mse=.001, rtol=1e-7, atol=1e-9)


def dump(path, value):
    with Path(path).open("x") as f:
        json.dump(value, f, indent=2, allow_nan=False)
        f.write("\n")


def fit(rhs, initial, output, *, rtol, atol, stop_at_target, horizon=40.):
    started=time.monotonic()
    last=[0.,initial.copy()]
    def checked(t,z):
        if time.monotonic()-started>CONFIG["solve_seconds"]:
            raise TimeoutError("Per-solve wall budget exceeded")
        if not np.all(np.isfinite(z)) or np.max(np.abs(z))>1e8:
            raise FloatingPointError("Nonfinite/excessive state")
        value=rhs(t,z)
        if not np.all(np.isfinite(value)):
            raise FloatingPointError("Nonfinite derivative")
        last[:]=[float(t),z.copy()]
        return value
    def target(t,z):
        return float(np.mean((output(z)-LABELS)**2)-CONFIG["target_mse"])
    target.direction=-1
    target.terminal=stop_at_target
    try:
        sol=solve_ivp(checked,(0.,horizon),initial,method="DOP853",rtol=rtol,
                      atol=atol,events=target,dense_output=True)
        hit=len(sol.t_events[0])>0
        t=float(sol.t_events[0][0]) if hit else float(sol.t[-1])
        final=sol.sol(t)
        record=dict(success=bool(sol.success),message=sol.message,reached_target=hit,
                    fit_time=t,integrated_to=float(sol.t[-1]),nfev=int(sol.nfev),
                    accepted_steps=len(sol.t)-1,solver_seconds=time.monotonic()-started,
                    training_output=output(final).tolist(),
                    training_rms=float(np.sqrt(np.mean((output(final)-LABELS)**2))))
        return sol,final,record
    except (TimeoutError,FloatingPointError,ValueError) as exc:
        return None,last[1],dict(success=False,reached_target=False,error=repr(exc),
            last_rhs_time=last[0],last_state_is_accepted=False,
            solver_seconds=time.monotonic()-started)


def hashes():
    folder=Path(__file__).parent
    return {name:hashlib.sha256((folder/name).read_bytes()).hexdigest()
            for name in ["run_scalar_point.py","scalar_point_engine.py",
                         "scalar_fourier_engine.py","scalar_fourier_reference.py",
                         "SCALAR_POINT_PROTOCOL.md"]
            if (folder/name).exists()}


def consumed(out):
    return sum(sum(json.loads(p.read_text()).get(k,0.) for k in
                   ("compile_seconds","initialization_seconds","solver_seconds"))
               for p in out.glob("*/result.json"))


def quota(out, reserve=120):
    used=consumed(out)
    if used+reserve>CONFIG["total_numerical_budget_seconds"]:
        raise RuntimeError(f"Campaign budget reached: {used:.3f}s recorded")


def save_fit(folder, sol, final, record, initial, training, point=None):
    np.savez_compressed(folder/"checkpoint.npz", initial=initial, final=final)
    if sol is not None:
        times=np.unique(np.r_[np.linspace(0,sol.t[-1],121),record["fit_time"]])
        states=sol.sol(times)
        training_values=np.array([training(states[:,i]) for i in range(len(times))])
        point_values=np.array([point(states[:,i]) for i in range(len(times))]) if point else np.full(len(times),np.nan)
        np.savez_compressed(folder/"trajectory.npz",times=times,states=states,
                            training=training_values,point=point_values)
        if point:
            record["point_prediction"]=float(point(final))
        with (folder/"solution.pkl").open("xb") as f:
            pickle.dump(sol,f)
    record["source_hashes"]=hashes()
    dump(folder/"result.json",record)
    print(json.dumps({"cell":folder.name,**record}),flush=True)


def references(out, refined=False):
    init=initialize(CONFIG["width"],CONFIG["seed"])
    for name,cls in [("dense",DenseReference),("parent_P1",PopulationReference)]:
        quota(out)
        folder=out/(name+("_refined" if refined else ""))
        folder.mkdir()
        model=cls(U.T,LABELS,init)
        training=lambda z:model.predict(z,U.T)
        point=lambda z:float(model.predict(z,TEST[None])[0])
        rt,at=(1e-9,1e-11) if refined else (1e-7,1e-9)
        sol,final,record=fit(model.rhs,model.initial,training,rtol=rt,atol=at,stop_at_target=False)
        record.update(rtol=rt,atol=at,state_count=model.dimension)
        save_fit(folder,sol,final,record,model.initial,training,point)


def scalar(out,K,refined=False,training_only=False):
    from scalar_point_engine import ScalarPointSystem
    quota(out,reserve=240)
    name=f"scalar_K{K}"+("_refined" if refined else "")+("_training_only" if training_only else "")
    folder=out/name
    folder.mkdir()
    started=time.monotonic()
    try:
        model=ScalarPointSystem(U,LABELS,None if training_only else TEST,K,
                                max_patterns=CONFIG["max_patterns"],max_terms=CONFIG["max_terms"],
                                compile_seconds=CONFIG["compile_seconds"])
    except Exception as exc:
        record=dict(success=False,phase="compilation",error=repr(exc),K=K,
                    compile_seconds=time.monotonic()-started,source_hashes=hashes())
        if hasattr(exc,"stats"):
            record["statistics"]=exc.stats
        dump(folder/"result.json",record)
        print(json.dumps({"cell":name,**record}),flush=True)
        return False,False
    compile_seconds=time.monotonic()-started
    init=initialize(CONFIG["width"],CONFIG["seed"])
    started=time.monotonic()
    initial=model.initialize(init.w,init.W20,init.W30,init.c)
    initialization_seconds=time.monotonic()-started
    rt,at=(1e-9,1e-11) if refined else (1e-7,1e-9)
    horizon=CONFIG["horizon"]
    if training_only:
        point_result=json.loads((out/"scalar_K5/result.json").read_text())
        if not point_result.get("success"):
            raise RuntimeError("No valid point stopping time for training-only control")
        horizon=point_result["fit_time"]
    sol,final,record=fit(model.rhs,initial,model.training_output,rtol=rt,atol=at,
                         stop_at_target=not training_only,horizon=horizon)
    record.update(phase="integration",K=K,refined=refined,training_only=training_only,
                  compile_seconds=compile_seconds,initialization_seconds=initialization_seconds,
                  rtol=rt,atol=at,state_count=len(initial),statistics=model.statistics())
    save_fit(folder,sol,final,record,initial,model.training_output,
              None if training_only else model.point_output)
    with (folder/"runtime.pkl").open("xb") as f:
        pickle.dump(model,f)
    return True, bool(record.get("reached_target"))


def load_solution(folder):
    with (folder/"solution.pkl").open("rb") as f:
        return pickle.load(f)


def analyze(out):
    init=initialize(CONFIG["width"],CONFIG["seed"])
    models={"dense":DenseReference(U.T,LABELS,init),"parent_P1":PopulationReference(U.T,LABELS,init)}
    refs={name:json.loads((out/name/"result.json").read_text()) for name in models}
    if not all(r.get("success") and r.get("reached_target") for r in refs.values()):
        raise RuntimeError("A reference failed to fit; no fitted comparison is valid")
    solutions={name:load_solution(out/name) for name in models}
    summary={"references":refs,"scalars":{},"point_angle_degrees":60,
             "parent_vs_dense_abs_error":abs(refs["parent_P1"]["point_prediction"]-refs["dense"]["point_prediction"])}
    for folder in sorted(out.glob("scalar_K*")):
        rec=json.loads((folder/"result.json").read_text())
        if rec.get("success") and "point_prediction" in rec:
            t=rec["fit_time"]
            prefix="own_fit" if rec.get("reached_target") else "terminal_unfitted"
            rec["comparison_status"]="fitted" if rec.get("reached_target") else "did_not_fit"
            rec[prefix+"_vs_dense_abs_error"]=abs(rec["point_prediction"]-refs["dense"]["point_prediction"])
            rec[prefix+"_vs_parent_abs_error"]=abs(rec["point_prediction"]-refs["parent_P1"]["point_prediction"])
            for name,model in models.items():
                ref=solutions[name]
                if not (ref.t[0]<=t<=ref.t[-1]):
                    raise RuntimeError("Reference extrapolation refused")
                pred=float(model.predict(ref.sol(t),TEST[None])[0])
                rec[f"{name}_point_same_time"]=pred
                rec[f"same_time_vs_{name}_abs_error"]=abs(rec["point_prediction"]-pred)
            panel=np.load(folder/"trajectory.npz")
            for name,model in models.items():
                train=np.array([model.predict(solutions[name].sol(ti),U.T) for ti in panel["times"]])
                rec[f"max_training_trajectory_difference_{name}"]=float(np.max(np.abs(panel["training"]-train)))
        summary["scalars"][folder.name]=rec
    for name in models:
        path=out/(name+"_refined")/"result.json"
        if path.exists():
            summary[name+"_refinement_abs_change"]=abs(json.loads(path.read_text())["point_prediction"]-refs[name]["point_prediction"])
    for folder in out.glob("scalar_K*_refined"):
        r=json.loads((folder/"result.json").read_text())
        base=json.loads((out/folder.name.removesuffix("_refined")/"result.json").read_text())
        if r.get("success") and base.get("success"):
            summary[folder.name+"_point_change"]=abs(r["point_prediction"]-base["point_prediction"])
    if (out/"scalar_K5_training_only/solution.pkl").exists() and (out/"scalar_K5/solution.pkl").exists():
        point_sol=load_solution(out/"scalar_K5")
        train_sol=load_solution(out/"scalar_K5_training_only")
        with (out/"scalar_K5/runtime.pkl").open("rb") as f: point_model=pickle.load(f)
        with (out/"scalar_K5_training_only/runtime.pkl").open("rb") as f: train_model=pickle.load(f)
        times=np.linspace(0,min(point_sol.t[-1],train_sol.t[-1]),121)
        errors=[point_model.training_output(point_sol.sol(t))-train_model.training_output(train_sol.sol(t)) for t in times]
        summary["passive_vs_training_only_max_training_difference"]=float(np.max(np.abs(errors)))
    summary["total_recorded_numerical_seconds"]=consumed(out)
    summary["analysis_source_hashes"]=hashes()
    dump(out/"scores.json",summary)
    print(json.dumps(summary,indent=2),flush=True)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--phase",choices=["references","scalars","controls","refine-scalar","analyze"],required=True)
    p.add_argument("--refine-cutoff",type=int)
    args=p.parse_args()
    out=args.out
    if args.phase=="references":
        out.mkdir(parents=True,exist_ok=False)
        dump(out/"config.json",dict(CONFIG,source_hashes=hashes(),command=sys.argv,
                                  python=sys.version,numpy=np.__version__,scipy=scipy.__version__,
                                  platform=platform.platform(),cwd=os.getcwd()))
        references(out)
    elif args.phase=="scalars":
        for K in CONFIG["cutoffs"]:
            compiled,fitted=scalar(out,K)
            if not compiled: break
    elif args.phase=="controls":
        scalar(out,5,training_only=True)
        references(out,refined=True)
        if args.refine_cutoff is not None:
            scalar(out,args.refine_cutoff,refined=True)
    elif args.phase=="refine-scalar":
        if args.refine_cutoff is None:
            p.error("--refine-cutoff is required for refine-scalar")
        scalar(out,args.refine_cutoff,refined=True)
    else:
        analyze(out)


if __name__=="__main__":
    main()
