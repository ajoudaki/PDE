"""Frozen higher-order campaign: original coefficients, scalar ODE, passive replay.

GPU is used only by initialization. Training and endpoint replay use exclusively
sample-indexed scalar tensors. Each action creates a fresh output directory.
"""
import argparse
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import sys
import time

import numpy as np
import scipy
from scipy.optimize import brentq

from scalar_aggregate_run import write_json, file_hash
from scalar_aggregate_engine import initialize_network
from run_scalar_long_time import read_npz, rms, spatial_check

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/"data/generated/neural_response_memory_20260922"
SOURCES = ("run_scalar_high_order.py", "scalar_high_order_initialization.py",
           "scalar_high_order_oracle.py", "scalar_high_order_engine.py",
           "SCALAR_HIGH_ORDER_PROTOCOL.md", "SCALAR_HIGH_ORDER_INITIALIZATION.md",
           "scalar_aggregate_engine.py", "scalar_aggregate_run.py",
           "scalar_circle_probe_engine.py", "run_scalar_long_time.py",
           "scalar_long_time_engine.py", "deep_circle_cases.json")
TARGET, END = 1e-6, 1e9


def start_output(output, inputs=()):
    output.mkdir(parents=True, exist_ok=False)
    (output/"sources").mkdir()
    hashes = {}
    for name in SOURCES:
        shutil.copy2(HERE/name, output/"sources"/name)
        hashes[name] = file_hash(HERE/name)
    record = dict(command=sys.argv, cwd=os.getcwd(), sources=hashes,
                  inputs={str(p.resolve()):file_hash(p) for p in inputs},
                  python=sys.version, numpy=np.__version__, scipy=scipy.__version__,
                  platform=platform.platform(), threads={name:os.environ.get(name) for name in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")})
    write_json(output/"manifest.json", record)
    return record


def finish_output(output, manifest):
    if any(file_hash(HERE/name) != digest for name,digest in manifest["sources"].items()):
        raise RuntimeError("used source changed during execution; retain this run as unqualified")
    manifest["outputs"] = {p.name:file_hash(p) for p in output.iterdir()
                           if p.is_file() and p.name != "manifest.json"}
    write_json(output/"manifest.json", manifest)


def case_data(seed):
    name = "quadrant_alternating_n2048_seed"+str(seed)
    source = DATA/"scalar_wide_source01"/name
    return name, source, read_npz(source/"initial_coefficients.npz")


def prepare(args):
    import torch
    from scalar_high_order_initialization import initialize_probe_coefficients, InitializationLimit
    name, source, old = case_data(args.seed)
    manifest = start_output(args.output, (source/"initial_coefficients.npz",source/"initialization.json"))
    started = time.perf_counter()
    torch.set_num_threads(1)
    params = initialize_network(2048,2,depth=3,seed=args.seed)
    angles = 2*np.pi*np.arange(args.grid)/args.grid
    off = 2*np.pi*(np.arange(32)+np.sqrt(2)/10)/32
    circle = lambda theta:np.column_stack((np.cos(theta),np.sin(theta)))
    if args.panel == "training":
        points = old["inputs"]
    elif args.panel == "pilot":
        points = circle(2*np.pi*np.arange(32)/32)
    else:
        # Only passive queries exploit exact oddness; all eight training inputs remain.
        points = np.vstack((circle(angles[:args.grid//2]),circle(off[:16]),old["inputs"]))
    config = dict(seed=args.seed, width=2048, case="quadrant_alternating", panel=args.panel,
                  order=args.order, grid=args.grid, device=args.device, seconds=args.seconds,
                  batch_size=32,word_chunk_size=16)
    write_json(args.output/"configuration.json",config)
    try:
        values, record = initialize_probe_coefficients(params,old["inputs"],points,order=args.order,
            device=args.device,batch_size=32,word_chunk_size=16,max_wall_seconds=args.seconds,
            return_metadata=True)
    except InitializationLimit as exc:
        write_json(args.output/"result.json",dict(exc.metadata,configuration=config))
        finish_output(args.output,manifest)
        print(json.dumps(exc.metadata),flush=True)
        return
    record.update(configuration=config,device_name=torch.cuda.get_device_name(torch.device(args.device)),
                  torch=torch.__version__,cuda=torch.version.cuda)
    reference_hash=json.loads((source/"initialization.json").read_text())["initialization_hash"]
    if record["initialization_hash"] != reference_hash:
        raise RuntimeError("parameters differ from common dense reference")
    if args.panel == "training":
        checks={}
        for p,key in enumerate(("f","Theta","C","Q"),1):
            diff=float(np.max(abs(values["T"+str(p)]-old[key])))
            bound=1e-11+1e-9*float(np.max(abs(old[key])))
            checks[key]=dict(maximum_difference=diff,bound=bound,passed=diff<=bound)
        record["legacy_checks"]=checks
        if not all(c["passed"] for c in checks.values()):
            raise RuntimeError("wide legacy coefficient comparison failed")
        np.savez_compressed(args.output/"coefficients.npz",**values,inputs=old["inputs"],labels=old["labels"])
    elif args.panel == "pilot":
        np.savez_compressed(args.output/"coefficients.npz",**values,probe_inputs=points)
    else:
        half=args.grid//2
        expanded={key:np.concatenate((v[:half],-v[:half],v[half:half+16],-v[half:half+16],v[-8:]),axis=0)
                  for key,v in values.items()}
        fullpoints=np.vstack((points[:half],-points[:half],points[half:half+16],-points[half:half+16],old["inputs"]))
        record.update(antipodal_reconstruction=True,computed_queries=len(points),queries=len(fullpoints))
        np.savez_compressed(args.output/"coefficients.npz",**expanded,angles=angles,off_angles=off,
                            probe_inputs=fullpoints,inputs=old["inputs"],labels=old["labels"])
    record["total_seconds"]=time.perf_counter()-started
    record["peak_rss_bytes"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
    record["whole_action_limits_satisfied"]=(record["total_seconds"]<args.seconds
                                               and record["peak_rss_bytes"]<8*1024**3)
    if not record["whole_action_limits_satisfied"]:
        record["status"]="resource_limit"
    write_json(args.output/"result.json",record)
    finish_output(args.output,manifest)
    print(json.dumps(record),flush=True)


def fit_loss(model,state):
    return float(np.mean((state[:model.M]-model.labels)**2))


def boundary(model,state):
    return max(float(np.max(abs(value)))/64**k for k,value in
               enumerate(model.signatures(state).values(),1))-1.


def integrate(args):
    from scalar_high_order_engine import ScalarHierarchy, StructuredBDF
    manifest=start_output(args.output,(args.source/"coefficients.npz",args.source/"result.json"))
    started=time.perf_counter()
    if json.loads((args.source/"result.json").read_text())["status"]!="complete":
        raise ValueError("training coefficients did not complete within resource limits")
    initial=read_npz(args.source/"coefficients.npz")
    names=["T"+str(p) for p in range(1,args.order+1)]
    coefficients={name:initial[name] for name in names}
    labels=initial["labels"]
    model=ScalarHierarchy(coefficients,labels,order=args.order,with_signatures=True)
    state=model.initial_state(); t=0.
    times,losses=[t],[fit_loss(model,state)]
    segment_times,segment_states,segment_training=[],[],[]
    nfev=njev=nlu=steps=0
    status,message="time_cap",""
    crossing_bracket=None
    while t<END and status=="time_cap":
        if time.perf_counter()-started>=args.seconds:
            status="wall_cap"; break
        solver=StructuredBDF(model,t,state,END,rtol=args.rtol,atol=args.rtol/100,max_step=np.inf)
        segment_start=t; anchor=model.training_state(state).copy(); do_recenter=False
        while solver.status=="running":
            if time.perf_counter()-started>=args.seconds:
                status="wall_cap"; break
            if steps>=100000:
                status="step_cap"; break
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024>=8*1024**3:
                status="memory_cap"; break
            old_time,old_loss,old_boundary=solver.t,fit_loss(model,solver.y),boundary(model,solver.y)
            message=solver.step() or ""; steps+=1
            if solver.status=="failed":
                status="solver_failure"; break
            if not np.isfinite(solver.y).all():
                status="nonfinite"; break
            events=[]; interpolation=None
            if fit_loss(model,solver.y)<=TARGET and old_loss>TARGET:
                interpolation=solver.dense_output()
                event=float(brentq(lambda x:fit_loss(model,interpolation(x))-TARGET,
                    old_time,solver.t,xtol=1e-12,rtol=1e-14))
                events.append((event,"fitted"))
            if boundary(model,solver.y)>=0 and old_boundary<0:
                interpolation=solver.dense_output() if interpolation is None else interpolation
                event=float(brentq(lambda x:boundary(model,interpolation(x)),
                    old_time,solver.t,xtol=1e-12,rtol=1e-14))
                events.append((event,"recenter"))
            if events:
                t,event=min(events,key=lambda x:x[0]); state=interpolation(t)
                if event=="fitted":
                    status="fitted"
                    crossing_bracket=dict(left_time=float(old_time),right_time=float(solver.t),
                        left_loss=old_loss,right_loss=fit_loss(model,solver.y))
                else: do_recenter=True
            else:
                t=float(solver.t); state=solver.y.copy()
            times.append(t); losses.append(fit_loss(model,state))
            if status=="fitted" or do_recenter: break
        nfev+=solver.nfev; njev+=solver.njev; nlu+=solver.nlu
        segment_times.append(t); segment_states.append(state.copy()); segment_training.append(anchor)
        coefficients={key:np.array(value,copy=True) for key,value in model.tensors(state).items()}
        model=ScalarHierarchy(coefficients,labels,order=args.order,with_signatures=True)
        state=model.initial_state()
        if not do_recenter or status!="time_cap": break
        if t<=segment_start:
            status,message="solver_failure","nonadvancing recenter"; break
    np.savez_compressed(args.output/"trajectory.npz",state=state,train_f=state[:len(labels)],
        time=t,times=np.array(times),losses=np.array(losses),segment_times=np.array(segment_times),
        segment_states=np.array(segment_states),segment_training=np.array(segment_training))
    fields=model.tensors(state); residual=fields["T1"]-labels; kernel=fields["T2"]
    record=dict(status=status,message=message,order=args.order,rtol=args.rtol,atol=args.rtol/100,
        time=t,loss=fit_loss(model,state),seconds=time.perf_counter()-started,segments=len(segment_times),
        accepted_steps=steps,nfev=nfev,njev=njev,nlu=nlu,initialization=str(args.source.resolve()),
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
        endpoint_kernel_minimum_eigenvalue=float(np.linalg.eigvalsh((kernel+kernel.T)/2)[0]),
        endpoint_effective_rate=float(residual@kernel@residual/(residual@residual)),
        maximum_saved_loss=float(max(losses)),minimum_saved_loss=float(min(losses)),
        crossing_bracket=crossing_bracket)
    write_json(args.output/"result.json",record); finish_output(args.output,manifest)
    print(json.dumps(record),flush=True)


def replay(args):
    from scalar_high_order_engine import ScalarHierarchy, recenter_coefficients
    manifest=start_output(args.output,(args.source/"coefficients.npz",args.run/"trajectory.npz",args.run/"result.json"))
    started=time.perf_counter()
    if json.loads((args.source/"result.json").read_text())["status"]!="complete":
        raise ValueError("passive coefficients did not complete within resource limits")
    probe=read_npz(args.source/"coefficients.npz")
    trajectory=read_npz(args.run/"trajectory.npz")
    runrecord=json.loads((args.run/"result.json").read_text())
    order=runrecord["order"]; names=["T"+str(p) for p in range(1,order+1)]
    passive={key:probe[key] for key in names}
    training={key:probe[key][-8:] for key in names}
    model=ScalarHierarchy(training,probe["labels"],order=order,with_signatures=True)
    gaps=[]
    for index,state in enumerate(trajectory["segment_states"]):
        if time.perf_counter()-started>=args.seconds:
            raise TimeoutError("passive replay exceeded declared wall cap")
        passive=recenter_coefficients(passive,model.signatures(state))
        gap=rms(passive["T1"][-8:]-state[:8]); gaps.append(gap)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024>=8*1024**3:
            raise MemoryError("passive replay exceeded memory cap")
    ngrid=len(probe["angles"]); prediction=passive["T1"]
    np.savez_compressed(args.output/"endpoint.npz",grid=np.asarray(prediction[:ngrid],dtype=float),
        off_grid=np.asarray(prediction[ngrid:ngrid+32],dtype=float),train_probe=np.asarray(prediction[-8:],dtype=float),
        train_f=trajectory["train_f"],time=trajectory["time"],segment_training_gaps=np.array(gaps))
    record=dict(status=runrecord["status"],order=order,training_probe_gap=max(gaps,default=0.),
        replay_seconds=time.perf_counter()-started,segments=len(gaps),run=str(args.run.resolve()),
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
    write_json(args.output/"result.json",record); finish_output(args.output,manifest)
    print(json.dumps(record),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="action",required=True)
    init=sub.add_parser("prepare"); init.add_argument("--seed",type=int,required=True)
    init.add_argument("--panel",choices=("training","pilot","probes"),required=True)
    init.add_argument("--order",type=int,choices=(5,6),default=6)
    init.add_argument("--device",default="cuda:1"); init.add_argument("--grid",type=int,choices=(1024,2048),default=1024)
    flow=sub.add_parser("integrate"); flow.add_argument("--source",type=Path,required=True)
    flow.add_argument("--order",type=int,choices=(4,5,6),required=True); flow.add_argument("--rtol",type=float,required=True)
    passive=sub.add_parser("replay"); passive.add_argument("--source",type=Path,required=True)
    passive.add_argument("--run",type=Path,required=True)
    for command in (init,flow,passive):
        command.add_argument("--output",type=Path,required=True); command.add_argument("--seconds",type=float,default=600.)
    args=parser.parse_args()
    globals()[{"prepare":"prepare","integrate":"integrate","replay":"replay"}[args.action]](args)


if __name__=="__main__":
    main()
