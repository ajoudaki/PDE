"""Independent p4/p5 raw-state audit; no producer or analyzer import.

Expected dictionaries are derived from P45_DERIVATION_ROUTE.md. The already
reviewed comparison helper supplies only I/O, raw-state prediction, metrics,
and snapshot audit. GPU execution requires an explicitly supplied device.
"""

import time
WORKER_START = time.monotonic()
import os
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

import comparison_independent_check as helper

ROOT, HERE, GENERATED, ARCHIVE = helper.ROOT, helper.HERE, helper.GENERATED, helper.ARCHIVE
CASES = helper.CASES
DIMS = {"new_p4": (6,12), "new_p5": (14,24)}


def shifted(poly, axis, count=1):
    """Multiply a homogeneous binary polynomial by y_axis**count.

    Index k is the exponent of y2; its y1 exponent is degree-k.
    """
    out = torch.zeros((len(poly)+count,)+poly.shape[1:], device=poly.device, dtype=poly.dtype)
    offset = axis*count
    out[offset:offset+len(poly)] = poly
    return out


def product(left,right):
    out = torch.zeros((len(left)+len(right)-1,)+left.shape[1:],device=left.device,dtype=left.dtype)
    for i in range(len(left)):
        for j in range(len(right)):
            out[i+j] += left[i]*right[j]
    return out


def gaussian_moments(order,v):
    nodes,weights = np.polynomial.hermite.hermgauss(order)
    lower = np.tanh(np.sqrt(2)*nodes)
    upper = np.tanh(np.sqrt(2*v)*nodes)
    ell,d = 1-lower*lower,1-upper*upper
    def mean(value):
        return float(np.dot(weights,value)/np.sqrt(np.pi))
    return dict(v=mean(lower*lower),tau=mean(upper*upper),ed=mean(d),
                ed2=mean(d*d),eh2d=mean(upper*upper*d),eh2d2=mean(upper*upper*d*d),
                el2=mean(ell*ell),eh2l2=mean(lower*lower*ell*ell),
                ed2_hsecond=mean(d*d-2*upper*upper*d))


@torch.no_grad()
def expected_dictionaries(initial):
    w,_,W = initial
    h = torch.tanh(w)
    upper = torch.tanh(W @ h)
    ell,d = 1-h*h,1-upper*upper
    lower_second,upper_second = -2*h*ell,-2*upper*d
    upper_third = 2*d*(3*upper*upper-1)
    nodes,weights = np.polynomial.hermite.hermgauss(256)
    v = float(np.dot(weights,np.tanh(np.sqrt(2)*nodes)**2)/np.sqrt(np.pi))
    moments = gaussian_moments(256,v)
    coarse = gaussian_moments(128,v)
    discrepancy = max(abs(moments[key]-coarse[key]) for key in moments)
    if discrepancy > 1e-9:
        raise ValueError("Independent Gaussian moment discrepancy exceeds protocol")
    S = upper.T.contiguous()
    q,V,R = [],[],[]
    for a in range(2):
        reverse = (W.T @ (S*d[:,a]).T).T
        qa = shifted(reverse*ell[:,a]/2,a)
        va = qa*ell[:,a]
        ra = v*shifted(S*d[:,a],a)/2+(W @ va.T).T
        q.append(qa);V.append(va);R.append(ra)
    J = sum(shifted(R[a]*d[:,a],a) for a in range(2))
    K = [J*d[:,a]/3+product(S,R[a])*upper_second[:,a] for a in range(2)]
    old_lower = torch.cat((h,
        torch.stack([2*V[a][a+b] for a in range(2) for b in range(2)],1)),1)
    U = torch.stack([d[:,a]*upper[:,b] for a in range(2) for b in range(2)],1)
    old_upper = torch.cat((U,6*torch.cat(K,0).T),1)
    lam = np.array([[moments["eh2l2"]*moments["ed2_hsecond"],
                     v*moments["el2"]*moments["ed"]**2],
                    [v*moments["el2"]*moments["ed"]**2,
                     moments["eh2l2"]*moments["ed2_hsecond"]]])
    T = []
    for a in range(2):
        b2_adjoint = torch.zeros_like(K[a])
        for b in range(2):
            for k in range(2):
                gamma = (moments["eh2d2"] if a==b==k else
                         moments["tau"]*moments["ed2"] if a==b else
                         moments["eh2d"]*moments["ed"])
                b2_adjoint[b+2*k] += gamma*h[:,b]/2
        actual_adjoint = (W.T @ K[a].T).T
        ta = (shifted(actual_adjoint,a)*ell[:,a]**2/4
              +shifted(b2_adjoint,a)*ell[:,a]**2/4
              +product(q[a],q[a])*lower_second[:,a])
        T.append(ta)
    E = []
    for a in range(2):
        scalar_part = sum(lam[a,b]*shifted(S*d[:,b],b,2) for b in range(2))
        E.append((W @ T[a].T).T+v*shifted(K[a],a)/4+3*shifted(scalar_part,a)/8)
    N = sum(shifted(E[a]*d[:,a]+product(R[a],R[a])*upper_second[:,a]/2,a)
            for a in range(2))
    K5 = [N*d[:,a]/5+product(J,R[a])*upper_second[:,a]/3
          +product(S,E[a])*upper_second[:,a]
          +product(S,product(R[a],R[a]))*upper_third[:,a]/2 for a in range(2)]
    lower_extra = 24*torch.cat((T[0][:4],T[1][1:]),0).T
    upper_extra = 120*torch.cat(K5,0).T
    result = {}
    for method,p in (("new_p4",4),("new_p5",5)):
        raw = ((old_lower,old_upper) if p==4 else
               (torch.cat((old_lower,lower_extra),1),torch.cat((old_upper,upper_extra),1)))
        eta = 1/(1024*(p+1)**2)
        bases,diagnostics = [],[]
        for field,count in zip(raw,DIMS[method]):
            if tuple(field.shape)!=(4096,count):
                raise ValueError("Incorrect independent dictionary dimensions")
            gram = field.T @ field/len(w)
            gram = (gram+gram.T)/2
            regularized = gram+eta*torch.eye(count,device=w.device,dtype=w.dtype)
            chol = torch.linalg.cholesky(regularized)
            basis = torch.linalg.solve_triangular(chol,field.T,upper=False).T.contiguous()
            eigenvalues = torch.linalg.eigvalsh(gram)
            effective = torch.linalg.eigvalsh(basis.T @ basis/len(w))
            residual = float((basis @ chol.T-field).norm()/field.norm())
            condition = float(torch.linalg.cond(regularized))
            finite = bool(torch.isfinite(field).all() and torch.isfinite(basis).all())
            diagnostics.append(dict(raw_eigenvalues=eigenvalues.cpu().tolist(),
                normalized_eigenvalues=effective.cpu().tolist(),ridge_condition=condition,
                triangular_relative_residual=residual,finite=finite,
                passed=finite and condition<=1e10 and residual<=1e-8))
            bases.append(basis)
        projected = bases[1].T @ (W @ bases[0])/len(w)
        result[method] = dict(bases=bases,projected=projected,diagnostics=diagnostics,
                              dimensions=DIMS[method],eta=eta)
    return result,dict(order256=moments,order128=coarse,maximum_discrepancy=discrepancy,
                       divisibility_zero_checks=dict(T1_y2_power4=helper.maximum(T[0][4]),
                                                     T2_y1_power4=helper.maximum(T[1][0])))


def source_checks(audit,configurations):
    """Manifest provenance only; old-study source files are never imported."""
    allowed_roots = (HERE,ROOT/"code",ROOT/"studies/random_dictionary_learned_circle_20260920")
    current,checked,skipped = {},{},{}
    for tag,config in configurations:
        checked[tag],skipped[tag] = {},{}
        for name,digest in config["source_hashes"].items():
            path = (ROOT/name).resolve()
            if not any(path==base or base in path.parents for base in allowed_roots):
                skipped[tag][name] = digest
                continue
            if name not in current:
                current[name] = helper.sha(path)
            audit.check(current[name]==digest,tag+" source "+name,
                        dict(recorded=digest,current=current[name]))
            checked[tag][name] = digest
    return dict(current=current,checked=checked,skipped_outside_authorized_scope=skipped,
                note="Original circle-study sources are hash-only provenance inputs")


def config_checks(audit,tag,config,level,initial_hashes,initial_archive_hash,is_new):
    for key,value in (("width",4096),("network_seed",20260920),("threshold",1e-3),
                      ("dtype","float64"),("max_time",10000),("max_steps",30000),
                      ("max_step",2),("per_trajectory_limit_seconds",180)):
        audit.check(config.get(key)==value,tag+" setting "+key,config.get(key))
    audit.check(str(config.get("device","")).startswith("cuda"),tag+" CUDA")
    audit.close(config["rtol"],6.25e-5/4**level,tag+" rtol",1e-20)
    audit.close(config["atol"],6.25e-7/4**level,tag+" atol",1e-20)
    for case,(angles,labels) in CASES.items():
        audit.check(config["cases"][case]["angles_degrees"]==angles,tag+" angles "+case)
        audit.check(config["cases"][case]["labels"]==labels,tag+" labels "+case)
    if is_new:
        audit.check(config["initial_array_sha256"]==initial_hashes,tag+" initial array hashes")
        audit.check(config["initial_archive_sha256"]==initial_archive_hash,tag+" initial archive digest")
        audit.check(config["orders"]==[4,5],tag+" orders")
        audit.check(set(config["methods"])<=set(DIMS),tag+" methods")
        for key,value in (("initial_step",.05),("min_step",1e-7),("block_size",256),("level",level)):
            audit.check(config.get(key)==value,tag+" setting "+key,config.get(key))
        audit.check(config["worker_limit_seconds"]<=(200 if level==2 else 400),tag+" worker cap")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device",required=True)
    parser.add_argument("--out",type=Path,default=GENERATED/"p45_independent01")
    parser.add_argument("--primary",type=Path,default=GENERATED/"p45_primary01")
    parser.add_argument("--refined",type=Path,default=GENERATED/"p45_refined01")
    parser.add_argument("--extra",type=Path,action="append",default=[])
    parser.add_argument("--budget",type=float,default=58)
    args = parser.parse_args()
    if not args.device.startswith("cuda") or not torch.cuda.is_available():
        raise RuntimeError("CUDA float64 required; CPU scientific replay is forbidden")
    if not 0<args.budget<=60:
        raise ValueError("Audit budget must be in (0,60]")
    args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.set_float32_matmul_precision("highest")
    torch.cuda.set_device(args.device)
    audit = helper.Audit()
    def budget_check():
        if time.monotonic()-WORKER_START>=args.budget:
            raise TimeoutError("Independent GPU audit reached its wall-clock ceiling")
    original_predict = helper.predict
    def bounded_predict(*values,**keywords):
        budget_check()
        return original_predict(*values,**keywords)
    helper.predict = bounded_predict
    initial_path = ARCHIVE/"scaling_width4096_refined01/quadrant_pairs_full/arrays.npz"
    initial_cpu = [next(helper.snapshots(initial_path,key)) for key in ("w","c","M")]
    initial_hashes = {key:hashlib.sha256(value.tobytes()).hexdigest()
                      for key,value in zip(("w","c","M"),initial_cpu)}
    initial_hash = helper.sha(initial_path)
    initial = [helper.tensor(value,args.device) for value in initial_cpu]
    audit.check(bool((initial[1]!=0).any()),"archived finite random readout retained")
    dictionaries,quadrature = expected_dictionaries(initial)
    helper.save_json(args.out/"dictionary_checks.json",dict(quadrature=quadrature,
        methods={method:{key:value for key,value in item.items() if key not in ("bases","projected")}
                 for method,item in dictionaries.items()}))
    for method,item in dictionaries.items():
        for j,diagnostic in enumerate(item["diagnostics"]):
            audit.check(diagnostic["passed"],method+f" independent dictionary gate {j}",diagnostic)
    configurations,cells = [],[]
    for level,newroot in enumerate((args.primary,args.refined)):
        oldroot = ARCHIVE/("scaling_width4096_"+("primary01" if level==0 else "refined01"))
        for worker,case in enumerate(CASES):
            for root,stem,is_new in ((newroot,"config_worker",True),
                                     (oldroot,"config_user_width4096_worker",False)):
                config = helper.read_json(root/f"{stem}{worker}.json")
                tag = root.name+f"/worker{worker}"
                configurations.append((tag,config))
                config_checks(audit,tag,config,level,initial_hashes,initial_hash,is_new)
                if is_new:
                    completion = helper.read_json(root/f"completion_worker{worker}.json")
                    audit.check(completion["total"]==completion["expected"]==2,tag+" all declared trajectories")
                    audit.check(completion["fitted"]==2,tag+" both fitted")
            cells.append((oldroot/(case+"_full"),"full",case,level))
            cells.extend((newroot/(case+"_"+method),method,case,level) for method in DIMS)
    for root in args.extra:
        for config_path in sorted(root.glob("config_worker*.json")):
            config = helper.read_json(config_path)
            worker,level = config["worker"],config["level"]
            case = list(CASES)[worker]
            tag = root.name+f"/worker{worker}"
            configurations.append((tag,config))
            audit.check(level==2,tag+" permitted extra level")
            config_checks(audit,tag,config,level,initial_hashes,initial_hash,True)
            completion = helper.read_json(root/f"completion_worker{worker}.json")
            audit.check(completion["total"]==completion["expected"]==len(config["methods"]),tag+" all declared extras")
            audit.check(completion["fitted"]==len(config["methods"]),tag+" extras fitted")
            cells.extend((root/(case+"_"+method),method,case,level) for method in config["methods"])
    helper.save_json(args.out/"source_checks.json",source_checks(audit,configurations))
    records,predictions = [],{}
    for path,method,case,level in cells:
        budget_check()
        record,prediction = helper.audit_cell(audit,path,method,case,level,initial,dictionaries,args.device)
        records.append(record)
        predictions[(case,method,level)] = prediction
        helper.save_json(args.out/"replay_checks.json",records)
    metrics,refinement = [],[]
    for case in CASES:
        for method in ("full",*DIMS):
            available = sorted(level for c,m,level in predictions if c==case and m==method)
            chosen = available[-2:]
            audit.check(len(chosen)==2,case+method+" selected pair")
            diff = helper.norms(predictions[(case,method,chosen[1])]-predictions[(case,method,chosen[0])])
            passed = diff["maximum"]<=.01
            refinement.append(dict(case=case,method=method,selected_levels=chosen,**diff,passed=passed))
            audit.check(passed,case+method+" refinement maximum gate",diff["maximum"])
            if 2 in available:
                trigger = helper.norms(predictions[(case,method,1)]-predictions[(case,method,0)])
                audit.check(trigger["maximum"]>.01,case+method+" permitted extra trigger",trigger["maximum"])
                audit.check(method in DIMS,case+method+" permitted extra method")
            if method=="full":
                continue
            for slot,level in enumerate(chosen):
                delta = predictions[(case,method,level)]-predictions[(case,"full",slot)]
                full,half = helper.norms(delta),helper.norms(delta[::2])
                metrics.append(dict(case=case,method=method,level=level,slot=slot,reference_level=slot,
                    dimensions=DIMS[method],**full,grid4096=half,
                    grid8192_vs4096={key:abs(full[key]-half[key]) for key in full}))
    torch.cuda.synchronize(args.device)
    budget_check()
    result = dict(schema="independent-p45-raw-state-audit-v1",passed=not audit.failures,
                  checked_assertions=audit.count,failures=audit.failures,
                  seconds=time.monotonic()-WORKER_START,worker_limit_seconds=args.budget,
                  device=args.device,gpu=torch.cuda.get_device_name(args.device),dtype="float64",
                  metrics=metrics,refinement=refinement,
                  checker_sha256=helper.sha(__file__),helper_sha256=helper.sha(helper.__file__),
                  route_sha256=helper.sha(HERE/"P45_DERIVATION_ROUTE.md"),
                  protocol_sha256=helper.sha(HERE/"P45_PROTOCOL.md"),
                  limitations=["All saved snapshots replayed; unsaved accepted states were not reconstructed.",
                    "First crossing refers to the recorded accepted-step/interpolated endpoint rule.",
                    "Circle norms and refinement are sampled numerical diagnostics.",
                    "Independent metrics were frozen before reading producer analysis outputs."])
    helper.save_json(args.out/"independent_results.json",result)
    print(json.dumps(dict(passed=result["passed"],assertions=audit.count,
                          failures=audit.failures,seconds=result["seconds"])),flush=True)


if __name__=="__main__":
    main()
