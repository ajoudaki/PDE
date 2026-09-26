"""Prerecorded scalar-model comparison. See SCALAR_VARIANTS_PROTOCOL.md."""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse
import hashlib
import json
import pickle
import platform
import resource
import signal
import sys
import time
from pathlib import Path
import numpy as np
import scipy
from scalar_fourier_reference import DenseReference, PopulationReference, initialize
from run_scalar_point import fit

TRAIN_DEGREES=np.array([10.,125.])
LABELS=np.array([1.,-1.])
PRIMARY_DEGREES=np.array([30.,60.,90.])
ADDITIONAL_DEGREES=np.array([0.,150.,210.,270.,330.])
VARIANTS={
    "tail_frozen_K3":dict(family="tail",mode="frozen",K=3),
    "tail_frozen_K5":dict(family="tail",mode="frozen",K=5),
    "tail_tangent_K3":dict(family="tail",mode="tangent",K=3),
    "tail_tangent_K5":dict(family="tail",mode="tangent",K=5),
    **{f"basis_r{r}":dict(family="basis",rank=r) for r in (4,8,12,16)},
    "potential_g_d1":dict(family="potential",rank_mode="gradient",degree=1),
    "potential_g_d2":dict(family="potential",rank_mode="gradient",degree=2),
    "potential_h_d2":dict(family="potential",rank_mode="curvature",degree=2),
    "potential_h_d3":dict(family="potential",rank_mode="curvature",degree=3),
}


def circle(degrees):
    theta=np.deg2rad(degrees)
    return np.stack([np.cos(theta),np.sin(theta)])


def write_json(path,record):
    with Path(path).open("x") as handle:
        json.dump(record,handle,indent=2,allow_nan=False)
        handle.write("\n")


def hashes():
    folder=Path(__file__).parent
    names=["run_scalar_variants.py","run_scalar_point.py","scalar_fourier_engine.py",
           "scalar_point_engine.py","scalar_fourier_reference.py","scalar_tail_engine.py",
           "scalar_response_basis.py","scalar_polynomial_potential.py","SCALAR_VARIANTS_PROTOCOL.md"]
    return {name:hashlib.sha256((folder/name).read_bytes()).hexdigest() for name in names if (folder/name).exists()}


def rms(values):
    return float(np.sqrt(np.mean(np.asarray(values)**2)))


def physical_outputs(weights,inputs):
    h=np.tanh(weights["w"]@inputs)
    h=np.tanh(weights["W2"]@h)
    h=np.tanh(weights["W3"]@h)
    return weights["c"]@h/len(weights["c"])


def consumed(out):
    total=0.
    for path in out.glob("*/result.json"):
        rec=json.loads(path.read_text())
        total+=rec.get("preparation_seconds",0)+rec.get("solver_seconds",0)
    return total


def check_budget(out,reserve=0):
    config=json.loads((out/"config.json").read_text())
    if time.time()-config["campaign_start_unix"]>1800 or consumed(out)+reserve>1800:
        raise RuntimeError("Declared campaign budget exhausted")


def save_solution(folder,sol,initial,final,record,outputs):
    np.savez_compressed(folder/"checkpoint.npz",initial=initial,final=final)
    if sol is not None:
        times=np.unique(np.r_[np.linspace(0,sol.t[-1],121),record["fit_time"]])
        states=sol.sol(times)
        values=np.array([outputs(states[:,i]) for i in range(len(times))])
        np.savez_compressed(folder/"trajectory.npz",times=times,states=states,outputs=values)
        with (folder/"solution.pkl").open("xb") as handle:
            pickle.dump(sol,handle)
    record["source_hashes"]=hashes()
    write_json(folder/"result.json",record)
    print(json.dumps({"cell":folder.name,**record}),flush=True)


def references(out,width=16,refined=False,all_angles=False):
    angles=np.r_[PRIMARY_DEGREES,ADDITIONAL_DEGREES] if all_angles else PRIMARY_DEGREES
    init=initialize(width,20260920)
    U=circle(TRAIN_DEGREES)
    query=circle(np.r_[TRAIN_DEGREES,angles])
    for name,cls in [("dense",DenseReference),("parent_P1",PopulationReference)]:
        check_budget(out,120)
        suffix=(f"_n{width}" if width!=16 else "")+("_refined" if refined else "")+("_extended" if all_angles else "")
        folder=out/(name+suffix)
        folder.mkdir()
        started=time.monotonic()
        model=cls(U.T,LABELS,init)
        prep=time.monotonic()-started
        train=lambda z:model.predict(z,U.T)
        outputs=lambda z:model.predict(z,query.T)
        rt,at=(1e-9,1e-11) if refined else (1e-7,1e-9)
        sol,final,record=fit(model.rhs,model.initial,train,rtol=rt,atol=at,stop_at_target=False)
        record.update(width=width,refined=refined,passive_angles=angles.tolist(),
                      preparation_seconds=prep,state_count=len(model.initial),
                      outputs=outputs(final).tolist(),rtol=rt,atol=at)
        np.savez_compressed(folder/"physical_final.npz",**model.physical(final))
        save_solution(folder,sol,model.initial,final,record,outputs)


def construct(config,U,y,Utest):
    args={k:v for k,v in config.items() if k!="family"}
    if config["family"]=="tail":
        from scalar_tail_engine import ScalarTailSystem
        return ScalarTailSystem(U,y,Utest,**args,max_patterns=12000,max_boundary=50000,
                                max_terms=5000000,compile_seconds=180,max_memory_bytes=3*1024**3)
    if config["family"]=="basis":
        from scalar_response_basis import ResponseBasisSystem
        return ResponseBasisSystem(U,y,Utest,**args)
    from scalar_polynomial_potential import PolynomialPotentialSystem
    return PolynomialPotentialSystem(U,y,Utest,**args)


def guard_alarm(signum,frame):
    raise TimeoutError("Preparation exceeded180s")


def cell(out,name,refined=False,width=16,extended=False):
    check_budget(out,300)
    config=VARIANTS[name]
    angles=np.r_[PRIMARY_DEGREES,ADDITIONAL_DEGREES] if extended else PRIMARY_DEGREES
    suffix=(f"_n{width}" if width!=16 else "")+("_refined" if refined else "")+("_extended" if extended else "")
    folder=out/(name+suffix)
    folder.mkdir()
    init=initialize(width,20260920)
    U=circle(TRAIN_DEGREES)
    started=time.monotonic()
    old_handler=signal.signal(signal.SIGALRM,guard_alarm)
    signal.alarm(180)
    try:
        model=construct(config,U,LABELS,circle(angles))
        initial=model.initialize(init.w,init.W20,init.W30,init.c)
        decoder=model.__dict__.pop("decoder",None)
        initial_velocity=model.rhs(0.,initial)
        if not np.all(np.isfinite(initial_velocity)):
            raise FloatingPointError("Initial velocity is nonfinite")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024>3*1024**3:
            raise MemoryError("Preparation exceeded3GiB RSS")
        prep=time.monotonic()-started
    except Exception as exc:
        record=dict(success=False,phase="preparation",error=repr(exc),variant=config,
                    preparation_seconds=time.monotonic()-started,source_hashes=hashes())
        if hasattr(exc,"stats"): record["statistics"]=exc.stats
        write_json(folder/"result.json",record)
        print(json.dumps({"cell":folder.name,**record}),flush=True)
        return
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM,old_handler)
    rt,at=(1e-9,1e-11) if refined else (1e-7,1e-9)
    sol,final,record=fit(model.rhs,initial,model.training_output,rtol=rt,atol=at,stop_at_target=True)
    record.update(variant=config,width=width,refined=refined,passive_angles=angles.tolist(),
                  phase="integration",preparation_seconds=prep,state_count=len(initial),
                  rtol=rt,atol=at,statistics=model.statistics())
    if sol is not None:
        record["outputs"]=model.outputs(final).tolist()
        record["initial_outputs"]=model.outputs(initial).tolist()
        if decoder is not None:
            if config["family"]=="basis":
                from scalar_response_basis import decode
                physical=decode(final,decoder)
            else:
                physical=model.decode(final,decoder)
            decoded=physical_outputs(physical,circle(np.r_[TRAIN_DEGREES,angles]))
            record["decoded_outputs"]=decoded.tolist()
            record["decoded_training_rms"]=rms(decoded[:2]-LABELS)
            record["internal_vs_decoded_rms"]=rms(decoded-model.outputs(final))
            np.savez_compressed(folder/"decoded_physical.npz",**physical)
            with (folder/"decoder.pkl").open("xb") as handle: pickle.dump(decoder,handle)
    with (folder/"runtime.pkl").open("xb") as handle: pickle.dump(model,handle)
    save_solution(folder,sol,initial,final,record,model.outputs)


def analyze(out,filename="scores.json"):
    base=json.loads((out/"dense/result.json").read_text())
    if not(base.get("success") and base.get("reached_target")):
        raise RuntimeError("Dense reference did not fit")
    with (out/"dense/solution.pkl").open("rb") as handle: dense_sol=pickle.load(handle)
    dense=DenseReference(circle(TRAIN_DEGREES).T,LABELS,initialize(16,20260920))
    results={"reference":base,"cells":{},"numerical_seconds":consumed(out)}
    for folder in sorted(out.iterdir()):
        if not folder.is_dir() or not (folder/"result.json").exists() or folder.name.startswith(("dense","parent")):
            continue
        rec=json.loads((folder/"result.json").read_text())
        if rec.get("success") and "outputs" in rec:
            width=rec.get("width",16)
            angles=np.array(rec["passive_angles"])
            query=circle(np.r_[TRAIN_DEGREES,angles])
            if width==16:
                dense_fit=dense.predict(dense_sol.sol(base["fit_time"]),query.T)
                refsol=dense_sol; refmodel=dense
            else:
                refname=f"dense_n{width}"+("_extended" if len(angles)>3 else "")
                refrec=json.loads((out/refname/"result.json").read_text())
                if not(refrec.get("success") and refrec.get("reached_target")):
                    raise RuntimeError("Additional-width reference did not fit")
                with (out/refname/"solution.pkl").open("rb") as handle: refsol=pickle.load(handle)
                refmodel=DenseReference(circle(TRAIN_DEGREES).T,LABELS,initialize(width,20260920))
                dense_fit=refmodel.predict(refsol.sol(refrec["fit_time"]),query.T)
            values=np.array(rec["outputs"])
            error=values[2:]-dense_fit[2:]
            rec.update(reference_outputs=dense_fit.tolist(),passive_error=error.tolist(),
                       passive_rms=rms(error),passive_max=float(np.max(np.abs(error))))
            rec["primary_panel_rms"]=rms(error[:3])
            rec["primary_panel_max"]=float(np.max(np.abs(error[:3])))
            t=rec["fit_time"]
            if not(refsol.t[0]<=t<=refsol.t[-1]): raise RuntimeError("Reference extrapolation refused")
            same=refmodel.predict(refsol.sol(t),query.T)
            rec["same_time_passive_rms"]=rms(values[2:]-same[2:])
            rec["internal_pass"]=bool(rec.get("reached_target") and rec["primary_panel_rms"]<=.05 and rec["primary_panel_max"]<=.1)
            if "decoded_outputs" in rec:
                decoded=np.array(rec["decoded_outputs"])
                rec["decoded_passive_rms"]=rms(decoded[2:]-dense_fit[2:])
                rec["decoded_passive_max"]=float(np.max(np.abs(decoded[2:]-dense_fit[2:])))
                rec["decoded_primary_panel_rms"]=rms(decoded[2:5]-dense_fit[2:5])
                rec["decoded_primary_panel_max"]=float(np.max(np.abs(decoded[2:5]-dense_fit[2:5])))
                rec["decoder_pass"]=bool(rec["decoded_training_rms"]<=.05 and rec["decoded_primary_panel_rms"]<=.05 and rec["decoded_primary_panel_max"]<=.1)
            if len(angles)>3:
                rec["additional_panel_rms"]=rms(error[3:])
                rec["additional_panel_max"]=float(np.max(np.abs(error[3:])))
                if "decoded_outputs" in rec:
                    rec["decoded_additional_panel_rms"]=rms(decoded[5:]-dense_fit[5:])
                    rec["decoded_additional_panel_max"]=float(np.max(np.abs(decoded[5:]-dense_fit[5:])))
        results["cells"][folder.name]=rec
    results["analysis_source_hashes"]=hashes()
    write_json(out/filename,results)
    concise={name:{k:r.get(k) for k in ["success","reached_target","state_count","passive_rms","passive_max","decoded_training_rms","decoded_passive_rms","internal_pass","decoder_pass","error"]}
             for name,r in results["cells"].items()}
    print(json.dumps(concise,indent=2),flush=True)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--phase",choices=["references","family","cell","analyze"],required=True)
    p.add_argument("--family",choices=["tail","basis","potential"])
    p.add_argument("--variant",choices=list(VARIANTS))
    p.add_argument("--refined",action="store_true")
    p.add_argument("--width",type=int,default=16)
    p.add_argument("--extended",action="store_true")
    p.add_argument("--score-file",default="scores.json")
    a=p.parse_args()
    if a.phase=="references":
        if not (a.out/"config.json").exists():
            a.out.mkdir(parents=True,exist_ok=True)
            write_json(a.out/"config.json",dict(seed=20260920,width=16,train=TRAIN_DEGREES.tolist(),
              primary=PRIMARY_DEGREES.tolist(),additional=ADDITIONAL_DEGREES.tolist(),variants=VARIANTS,
              campaign_start_unix=time.time(),python=sys.version,numpy=np.__version__,scipy=scipy.__version__,
              platform=platform.platform(),source_hashes=hashes(),command=sys.argv,cwd=os.getcwd()))
        references(a.out,a.width,a.refined,a.extended)
    elif a.phase=="family":
        if a.family is None:p.error("--family required")
        for name,config in VARIANTS.items():
            if config["family"]==a.family:cell(a.out,name)
    elif a.phase=="cell":
        if a.variant is None:p.error("--variant required")
        cell(a.out,a.variant,a.refined,a.width,a.extended)
    else: analyze(a.out,a.score_file)


if __name__=="__main__":main()
