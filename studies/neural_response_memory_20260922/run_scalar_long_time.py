"""Long physical-time continuation of the unchanged scalar closure."""
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
from scipy.integrate import BDF, Radau
from scipy.optimize import brentq

from scalar_aggregate_run import write_json, file_hash
from scalar_circle_probe_engine import fit_fourier, evaluate_fourier, initialize_probe_coefficients, forward_only
from scalar_aggregate_engine import initialize_network, unflatten_network
from run_scalar_circle_endpoints import deadline_call
from scalar_long_time_engine import StiffSignatureHierarchy, recenter_coefficients, frozen_kernel_endpoint

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1]/"data/generated/neural_response_memory_20260922/scalar_circle_endpoint_primary01"
TARGET, END = 1e-6, 1e9
NAMES = ("f","Theta","C","Q")
MILESTONES = np.array([2048.*4**k for k in range(10) if 2048.*4**k < END]+[END])


def rms(x):
    return float(np.sqrt(np.mean(np.asarray(x,dtype=np.longdouble)**2)))


def read_npz(path):
    with np.load(path,allow_pickle=False) as data:
        return {key:data[key] for key in data.files}


def transport(probe, model, state):
    return recenter_coefficients(probe,model.signatures(state))


def loss(model,state):
    return float(np.mean((state[:model.M]-model.labels)**2))


def boundary(model,state):
    sig=model.signatures(state)
    return max(float(np.max(np.abs(sig["z"]))/64),
               float(np.max(np.abs(sig["I"]))/64**2),
               float(np.max(np.abs(sig["J"]))/64**3))-1.


def initialize_run(source,level,from_zero):
    original=read_npz(source/"initial_coefficients.npz")
    probe=read_npz(source/"probe_coefficients.npz")
    coefficients={key:original[key] for key in NAMES}
    model=StiffSignatureHierarchy(coefficients,original["labels"],order=4)
    passive={key:probe[key] for key in NAMES}
    if from_zero:
        return original,probe,coefficients,passive,0.
    archive=read_npz(source/("order4_resolution"+str(level)+".npz"))
    state=archive["state"]
    current=model.training.tensors(model.training_state(state))
    coefficients={key:np.array(current[key],copy=True) for key in NAMES}
    passive=transport(passive,model,state)
    return original,probe,coefficients,passive,float(archive["time"])


def integrate(source,target,level,rtol,method,from_zero,seconds):
    """Keep full physical aggregate fields and restart only local signatures."""
    target.mkdir(parents=True,exist_ok=False)
    started=time.perf_counter()
    original,probe,coefficients,passive,t=initialize_run(source,level,from_zero)
    labels=original["labels"]; m=len(labels); ngrid=len(probe["angles"])
    model=StiffSignatureHierarchy(coefficients,labels,order=4)
    state=model.initial_state()
    times,losses=[t],[loss(model,state)]
    segment_times,segment_states,segment_training=[],[],[]
    milestones=[]; milestone_grids=[]; milestone_states=[]; milestone_segments=[]
    nfev=njev=nlu=steps=0
    status,message="time_cap",""
    next_milestone=int(np.searchsorted(MILESTONES,t,side="right"))
    peak_gap=rms(passive["f"][-m:]-state[:m])
    solver_class=BDF if method=="BDF" else Radau
    while t < END and status=="time_cap":
        if time.perf_counter()-started >= seconds:
            status="wall_cap"; break
        solver=solver_class(model.rhs,t,state,END,rtol=rtol,atol=rtol/100,jac=model.jac,max_step=np.inf)
        segment_start=t
        do_recenter=False
        while solver.status=="running":
            if time.perf_counter()-started >= seconds:
                status="wall_cap"; break
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024 >= 2*1024**3:
                status="memory_cap"; break
            old_time,old_loss,old_boundary=solver.t,loss(model,solver.y),boundary(model,solver.y)
            message=solver.step() or ""; steps+=1
            if solver.status=="failed":
                status="solver_failure"; break
            if not np.isfinite(solver.y).all():
                status="nonfinite"; break
            interpolation=None
            events=[]
            if loss(model,solver.y)<=TARGET and old_loss>TARGET:
                interpolation=solver.dense_output()
                fit=float(brentq(lambda x:loss(model,interpolation(x))-TARGET,
                    old_time,solver.t,xtol=1e-12,rtol=1e-14))
                events.append((fit,"fitted"))
            if boundary(model,solver.y)>=0 and old_boundary<0:
                interpolation=solver.dense_output() if interpolation is None else interpolation
                edge=float(brentq(lambda x:boundary(model,interpolation(x)),
                    old_time,solver.t,xtol=1e-12,rtol=1e-14))
                events.append((edge,"recenter"))
            if events:
                t,event=min(events,key=lambda pair:pair[0]); state=interpolation(t)
                if event=="fitted": status="fitted"
                else: do_recenter=True
            else:
                t=float(solver.t); state=solver.y.copy()
            while next_milestone<len(MILESTONES) and MILESTONES[next_milestone]<=t:
                interpolation=solver.dense_output() if interpolation is None else interpolation
                mt=float(MILESTONES[next_milestone]); ms=interpolation(mt)
                pred=transport(passive,model,ms)["f"]
                fields=model.training.tensors(model.training_state(ms)); r=fields["f"]-labels
                kernel=fields["Theta"]; eig=np.linalg.eigvalsh((kernel+kernel.T)/2)
                milestones.append(dict(time=mt,loss=loss(model,ms),eigenmin=float(eig[0]),
                    effective_rate=float(r@kernel@r/(r@r)),training_probe_gap=rms(pred[-m:]-r-labels)))
                milestone_grids.append(np.asarray(pred[:ngrid],dtype=float))
                milestone_states.append(ms.copy()); milestone_segments.append(len(segment_states))
                next_milestone+=1
            times.append(t); losses.append(loss(model,state))
            if status=="fitted" or do_recenter: break
        nfev+=solver.nfev; njev+=solver.njev; nlu+=solver.nlu
        # The local signature is now fully accounted for, including a partial
        # segment at a resource cap. This is a state change, never a dense refresh.
        passive=transport(passive,model,state)
        peak_gap=max(peak_gap,rms(passive["f"][-m:]-state[:m]))
        segment_times.append(t); segment_states.append(state.copy())
        segment_training.append(model.training.initial_state())
        fields=model.training.tensors(model.training_state(state))
        coefficients={key:np.array(fields[key],copy=True) for key in NAMES}
        model=StiffSignatureHierarchy(coefficients,labels,order=4)
        state=model.initial_state()
        if not do_recenter or status!="time_cap": break
        if t<=segment_start:
            status,message="solver_failure","nonadvancing recenter"; break
    arrays=dict(state=state,train_f=state[:m],grid=np.asarray(passive["f"][:ngrid],dtype=float),
        off_grid=np.asarray(passive["f"][ngrid:ngrid+32],dtype=float),
        train_probe=np.asarray(passive["f"][-m:],dtype=float),time=np.array(t),
        times=np.array(times),losses=np.array(losses),segment_times=np.array(segment_times),
        segment_states=np.array(segment_states),segment_training=np.array(segment_training))
    arrays["milestone_grids"]=np.array(milestone_grids)
    arrays["milestone_states"]=np.array(milestone_states)
    arrays["milestone_segments"]=np.array(milestone_segments,dtype=int)
    np.savez_compressed(target/"trajectory.npz",**arrays)
    np.savez_compressed(target/"passive_endpoint.npz",**passive)
    write_json(target/"milestones.json",milestones)
    record=dict(status=status,message=message,time=t,loss=loss(model,state),rtol=rtol,atol=rtol/100,
        method=method,from_zero=from_zero,start_level=level,segments=len(segment_times),
        accepted_steps=steps,nfev=nfev,njev=njev,nlu=nlu,training_probe_gap=peak_gap,
        seconds=time.perf_counter()-started,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
    write_json(target/"result.json",record)
    print(json.dumps(dict(event="run",configuration=source.name,run=target.name,**record)),flush=True)
    return arrays,record


def check_pair(coarse,fine,coarse_rec,fine_rec,reference):
    count=min(len(coarse["grid"]),len(fine["grid"]),len(reference["grid"]))
    if any(len(a["grid"])%count for a in (coarse,fine,reference)):
        raise ValueError("non-nested comparison grids")
    first,second,ref=(a["grid"][::len(a["grid"])//count] for a in (coarse,fine,reference))
    error=rms(second-ref)
    change=rms(first-second)
    time_change=abs(float(coarse["time"])-float(fine["time"]))/max(1.,float(fine["time"]))
    passed=(coarse_rec["status"]==fine_rec["status"]=="fitted" and change<=.002
            and change<=.1*max(error,1e-6) and time_change<=.001
            and max(coarse_rec["training_probe_gap"],fine_rec["training_probe_gap"])<=1e-4)
    return dict(circle_rms=error,numerical_change=change,time_relative_change=time_change,passed=bool(passed))


def spatial_check(values,probe,reference):
    angles,off=probe["angles"],probe["off_angles"]
    difference=values["grid"]-reference["grid"]; error=rms(difference)
    change=abs(error-rms(difference[::2]))
    checks=[]
    for degree in (64,128,256):
        fc=fit_fourier(values["grid"],degree)
        gd=evaluate_fourier(fc,angles)-values["grid"]
        od=evaluate_fourier(fc,off)-values["off_grid"]
        entry=dict(mode=degree,grid_rms=rms(gd),off_grid_rms=rms(od),maximum=float(max(np.max(abs(gd)),np.max(abs(od)))))
        entry["passed"]=max(entry["grid_rms"],entry["off_grid_rms"])<=1e-5 and entry["maximum"]<=1e-4
        checks.append(entry)
        if entry["passed"]: break
    return dict(circle_rms=error,relative_rms=error/rms(reference["grid"]),
        maximum_error=float(np.max(abs(difference))),quadrature_change=change,
        quadrature_pass=bool(change<=.001 and change<=.01*max(error,1e-6)),
        fourier=checks,fourier_pass=checks[-1]["passed"]),fc


def refined_probes(source,target,runs,records,reference,seconds):
    """Refine only passive circle evaluation by replaying archived scalar segments."""
    metadata=json.loads((source/"configuration.json").read_text())
    initial=read_npz(source/"initial_coefficients.npz")
    angles=2*np.pi*np.arange(2048)/2048
    off=2*np.pi*(np.arange(32)+np.sqrt(2)/10)/32
    circle=lambda theta:np.column_stack((np.cos(theta),np.sin(theta)))
    points=np.vstack((circle(angles),circle(off),initial["inputs"]))
    params=initialize_network(metadata["width"],2,depth=3,seed=metadata["seed"])
    original=deadline_call(lambda:initialize_probe_coefficients(params,initial["inputs"],points,order=4),min(60.,seconds))
    probe=dict(**original,angles=angles,off_angles=off,probe_inputs=points)
    np.savez_compressed(target/"probe_coefficients_refined.npz",**probe)
    model=StiffSignatureHierarchy(initial,initial["labels"],order=4)
    for level,(run,record) in enumerate(zip(runs,records)):
        passive={key:probe[key] for key in NAMES}
        if not record["from_zero"]:
            prefix=read_npz(source/("order4_resolution"+str(record["start_level"])+".npz"))
            passive=transport(passive,model,prefix["state"])
        for state in run["segment_states"]:
            passive=transport(passive,model,state)
        values=passive["f"]
        run.update(grid=np.asarray(values[:2048],dtype=float),off_grid=np.asarray(values[2048:2080],dtype=float),
                   train_probe=np.asarray(values[2080:],dtype=float))
        np.savez_compressed(target/("order4_resolution"+str(level))/"trajectory_spatial_refined.npz",**run)
    n=metadata["width"]
    dense_params=unflatten_network(reference["state"],((n,2),(n,n),(n,n),(n,)))
    reference=dict(reference,grid=forward_only(dense_params,points[:2048]))
    np.savez_compressed(target/"dense_reference_refined.npz",**reference)
    return probe,reference


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source",type=Path,default=SOURCE)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--budget",type=float,default=1800.)
    args=parser.parse_args(); args.output.mkdir(parents=True,exist_ok=False)
    source_dir=args.output/"sources"; source_dir.mkdir()
    names=(Path(__file__).name,"scalar_long_time_engine.py","scalar_circle_probe_engine.py","run_scalar_circle_endpoints.py",
           "scalar_aggregate_engine.py","scalar_aggregate_run.py","SCALAR_LONG_TIME_PROTOCOL.md")
    for name in names: shutil.copy2(HERE/name,source_dir/name)
    source_inputs={str(p):file_hash(p) for d in sorted(args.source.glob('quadrant_alternating_*'))
                   for p in d.glob('*') if p.is_file()}
    write_json(args.output/"manifest.json",dict(command=sys.argv,inputs=source_inputs,
        sources={name:file_hash(HERE/name) for name in names},
        environment=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),
            longdouble_epsilon=float(np.finfo(np.longdouble).eps),
            threads={key:os.environ.get(key) for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")})))
    started=time.perf_counter(); summaries=[]
    for index,source in enumerate(sorted(args.source.glob("quadrant_alternating_*"))):
        target=args.output/source.name; target.mkdir()
        runs=[]; records=[]
        reference=read_npz(source/"dense_resolution1.npz")
        initial=read_npz(source/"initial_coefficients.npz"); probe=read_npz(source/"probe_coefficients.npz")
        for level,rtol in enumerate((1e-7,1e-9)):
            remaining=args.budget-(time.perf_counter()-started)
            if remaining<=0: break
            a,r=integrate(source,target/("order4_resolution"+str(level)),level,rtol,"BDF",False,min(180.,remaining))
            runs.append(a);records.append(r)
        if len(runs)<2: break
        gate=check_pair(*runs,*records,reference)
        if not gate["passed"]:
            remaining=args.budget-(time.perf_counter()-started)
            if remaining>0:
                a,r=integrate(source,target/"order4_resolution2",1,1e-11,"BDF",True,min(180.,remaining))
                runs.append(a);records.append(r)
                gate=check_pair(runs[-2],runs[-1],records[-2],records[-1],reference)
        spatial,fc=spatial_check(runs[-1],probe,reference)
        if not spatial["quadrature_pass"]:
            probe,reference=refined_probes(source,target,runs,records,reference,args.budget-(time.perf_counter()-started))
            gate=check_pair(runs[-2],runs[-1],records[-2],records[-1],reference)
            spatial,fc=spatial_check(runs[-1],probe,reference)
        np.savez_compressed(target/"order4_fourier.npz",endpoint=fc,angles=probe["angles"])
        baseline=frozen_kernel_endpoint(initial,initial["labels"],target=TARGET,time_cap=END)
        pred=np.asarray(probe["f"],dtype=np.longdouble)+np.asarray(probe["Theta"],dtype=np.longdouble)@np.asarray(baseline["z"],dtype=np.longdouble)
        count=len(probe["angles"])
        ba=dict(grid=np.asarray(pred[:count],dtype=float),off_grid=np.asarray(pred[count:count+32],dtype=float),
                train_probe=np.asarray(pred[-8:],dtype=float),**baseline)
        np.savez_compressed(target/"order2_spectral.npz",**ba)
        bs,bfc=spatial_check(ba,probe,reference)
        np.savez_compressed(target/"order2_fourier.npz",endpoint=bfc,angles=probe["angles"])
        extra={}
        if index==0:
            for label,method,from_zero in (("radau_crosscheck","Radau",False),("fresh_reproduction","BDF",True)):
                remaining=args.budget-(time.perf_counter()-started)
                if remaining<=0: break
                a,r=integrate(source,target/label,1,1e-9,method,from_zero,min(180.,remaining))
                extra[label]=dict(record=r,comparison=check_pair(runs[-1],a,records[-1],r,reference))
        fitted=records[-1]["status"]=="fitted"
        valid=gate["passed"] and spatial["quadrature_pass"] and spatial["fourier_pass"]
        if index==0:
            valid=valid and len(extra)==2 and all(item["comparison"]["passed"] for item in extra.values())
        verdict="no_matched_endpoint" if not fitted else "numerically_inconclusive" if not valid else (
            "agreement" if spatial["circle_rms"]<=.1 else "adverse" if spatial["circle_rms"]>.2 else "inconclusive")
        summary=dict(configuration=source.name,records=records,latest=len(records)-1,gate=gate,
            spatial=spatial,verdict=verdict,order2=dict(spatial=bs,time=float(baseline["time"]),
                loss=float(baseline["loss"]),status=str(baseline["status"])),checks=extra,
            dense_time=float(reference["time"]))
        write_json(target/"summary.json",summary);summaries.append(summary)
        write_json(args.output/"campaign.json",dict(configurations=summaries,seconds=time.perf_counter()-started))
        print(json.dumps(dict(event="configuration",configuration=source.name,verdict=verdict,
             time=records[-1]["time"],loss=records[-1]["loss"],circle_rms=spatial["circle_rms"])),flush=True)
    print(json.dumps(dict(event="finished",configurations=len(summaries),seconds=time.perf_counter()-started)),flush=True)


if __name__=="__main__": main()
