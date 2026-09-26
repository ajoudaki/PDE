"""Independent CUDA replay of the frozen two-case comparison.

No producer, dictionary builder, engine, or analyzer is imported. CPU work is
limited to I/O, metadata, and the protocol's scalar Gaussian quadrature.
All predictions, dictionary construction and scientific metrics use CUDA f64.
"""
import os
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import time
import zipfile

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
GENERATED = ROOT / "data/generated/gradient_flow_probe_dictionary_20260921"
ARCHIVE = ROOT / "data/generated/random_dictionary_learned_circle_20260920"
CASES = {
    "quadrant_pairs": ([10,20,30,40,50,60,70,80], [1,1,-1,-1,1,1,-1,-1]),
    "two_outliers_alternating": ([15,27,39,51,63,75,165,285], [1,-1,1,-1,1,-1,1,-1]),
}
DIMS = {"new_p1": (2,4), "new_p2": (2,4), "new_p3": (6,12),
        "old_p1": (5,3), "old_p2": (15,6), "old_p3": (35,10)}
ALLOWED_SOURCE = [
    "studies/gradient_flow_probe_dictionary_20260921/COMPARISON_PROTOCOL.md",
    "studies/gradient_flow_probe_dictionary_20260921/comparison_run.py",
    "studies/gradient_flow_probe_dictionary_20260921/new_dictionary.py",
    *["studies/random_dictionary_learned_circle_20260920/"+x for x in (
        "benchmark.py", "diverse_benchmark.py", "diverse_cases.py",
        "diverse_dictionary.py", "scaling_dictionary.py")],
    *["code/pde/"+x for x in ("observable_torch_p1.py", "finite_torch.py",
                             "observable_initialization.py", "observable_words.py")],
]


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(8*1024*1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def save_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")


def snapshots(path, key):
    """Stream one leading-axis snapshot, never materializing a dense history."""
    with zipfile.ZipFile(path) as archive, archive.open(key+".npy") as handle:
        version = np.lib.format.read_magic(handle)
        reader = (np.lib.format.read_array_header_1_0 if version == (1,0)
                  else np.lib.format.read_array_header_2_0)
        shape, fortran, dtype = reader(handle)
        if fortran or dtype != np.dtype("float64"):
            raise ValueError("Snapshot format changed")
        count = math.prod(shape[1:])
        for _ in range(shape[0]):
            raw = handle.read(count*dtype.itemsize)
            if len(raw) != count*dtype.itemsize:
                raise ValueError("Truncated snapshot")
            yield np.frombuffer(raw, dtype=dtype).reshape(shape[1:]).copy()


def tensor(value, device):
    return torch.as_tensor(value, dtype=torch.float64, device=device)


def maximum(value):
    return float(value.abs().max())


def norms(value):
    return dict(rms=float(value.square().mean().sqrt()), l1=float(value.abs().mean()),
                maximum=maximum(value))


@torch.no_grad()
def predict(state, inputs, bases=None):
    """Independent association, batched by input, with no engine import."""
    w, c, middle = state
    n = len(c)
    # Folding the upper linear product differs from the producer association.
    upper_map = middle if bases is None else bases[1] @ middle
    pieces = []
    for x in inputs.split(256):
        hidden = torch.tanh(w @ x.T)
        if bases is not None:
            hidden = (bases[0].T @ hidden) / n
        pieces.append((c @ torch.tanh(upper_map @ hidden))/n)
    return torch.cat(pieces)


def chebyshev_table(coordinates, p):
    # Enumerate independently using Cartesian products, then the contract sort.
    exponents = [x for x in itertools.product(range(p+1), repeat=coordinates.shape[1])
                 if sum(x) <= p]
    exponents.sort(key=lambda x: (sum(x), tuple(-a for a in x)))
    one = torch.ones_like(coordinates)
    terms = [one, coordinates]
    for degree in range(2,p+1):
        terms.append(2*coordinates*terms[-1]-terms[-2])
    return torch.stack([torch.stack([terms[d][:,j] for j,d in enumerate(e)],1).prod(1)
                        for e in exponents],1)


@torch.no_grad()
def independent_dictionaries(initial):
    w, _, W = initial
    h = torch.tanh(w)
    H = torch.tanh(W @ h)
    d = 1-H*H
    U = torch.stack([d[:,a]*H[:,b] for a in range(2) for b in range(2)],1)
    L = torch.stack([(1-h[:,a].square()).square()*(W.T @ U[:,2*a+b])
                     for a in range(2) for b in range(2)],1)
    values = []
    for order in (128,256):
        nodes, weights = np.polynomial.hermite.hermgauss(order)
        values.append(float(np.dot(weights, np.tanh(np.sqrt(2)*nodes)**2)/np.sqrt(np.pi)))
    F = values[-1]*U + W@L
    def A(a,b,c):
        return d[:,a]*d[:,b]*F[:,2*b+c]
    def B(a,b,c):
        return -2*H[:,c]*H[:,a]*d[:,a]*F[:,2*a+b]
    quartic = torch.stack([
        A(0,0,0)+3*B(0,0,0), A(0,0,1)+3*(B(0,0,1)+B(0,1,0)),
        A(0,1,0)+3*B(0,1,1), A(0,1,1), A(1,0,0),
        A(1,0,1)+3*B(1,0,0), A(1,1,0)+3*(B(1,0,1)+B(1,1,0)),
        A(1,1,1)+3*B(1,1,1)],1)
    old_coordinates = (torch.cat([h,torch.tanh(W.T@H)],1),H)
    result = {}
    for method, dimensions in DIMS.items():
        p = int(method[-1]); eta=1/(1024*(p+1)**2)
        if method.startswith("old"):
            raw = [chebyshev_table(c,p) for c in old_coordinates]
        elif p == 3:
            raw = [torch.cat([h,L],1), torch.cat([U,quartic],1)]
        else:
            raw = [h,U]
        bases, diagnostics = [], []
        for field, count in zip(raw,dimensions):
            assert field.shape == (4096,count)
            gram = field.T@field/len(w)
            gram = (gram+gram.T)/2
            regularized = gram+eta*torch.eye(count,device=w.device,dtype=w.dtype)
            factor = torch.linalg.cholesky(regularized)
            basis = torch.linalg.solve_triangular(factor,field.T,upper=False).T.contiguous()
            eigenvalues = torch.linalg.eigvalsh(gram)
            effective = torch.linalg.eigvalsh(basis.T@basis/len(w))
            residual = float((basis@factor.T-field).norm()/field.norm())
            condition = float(torch.linalg.cond(regularized))
            diagnostic = dict(raw_eigenvalues=eigenvalues.cpu().tolist(),
                normalized_eigenvalues=effective.cpu().tolist(), ridge_condition=condition,
                triangular_relative_residual=residual,
                raw_rank_epsilon=int((eigenvalues>max(field.shape)*torch.finfo(w.dtype).eps*eigenvalues[-1]).sum()),
                raw_rank_1e_10=int((eigenvalues>1e-10*eigenvalues[-1]).sum()),
                normalized_rank_1e_10=int((effective>1e-10*effective[-1]).sum()),
                finite=bool(torch.isfinite(field).all() and torch.isfinite(basis).all()))
            diagnostic["passed"] = diagnostic["finite"] and condition<=1e10 and residual<=1e-8
            diagnostics.append(diagnostic); bases.append(basis)
        projected = bases[1].T@(W@bases[0])/len(w)
        result[method] = dict(bases=bases, projected=projected, diagnostics=diagnostics,
                              eta=eta, dimensions=dimensions)
    return result, dict(v_128=values[0],v_256=values[1],absolute_discrepancy=abs(values[1]-values[0]))


class Audit:
    def __init__(self):
        self.failures=[]; self.count=0
    def check(self, condition, name, observed=None):
        self.count+=1
        if not bool(condition):
            self.failures.append(dict(check=name,observed=observed))
    def close(self, observed, expected, name, tolerance=1e-10):
        delta=abs(float(observed)-float(expected))
        self.check(math.isfinite(delta) and delta<=tolerance,name,delta)
        return delta


def source_config_checks(audit, configurations):
    current={name:sha(ROOT/name) for name in ALLOWED_SOURCE}
    checked={}; manifests={}
    for tag,config in configurations:
        manifests[tag]=config["source_hashes"]
        scope_hashes={name:digest for name,digest in config["source_hashes"].items() if name in current}
        for name,digest in scope_hashes.items():
            audit.check(current[name]==digest,tag+" source "+name)
        for name,expected in (("width",4096),("network_seed",20260920),
                              ("threshold",1e-3),("dtype","float64"),("max_time",10000),
                              ("max_steps",30000),("max_step",2),("per_trajectory_limit_seconds",180)):
            audit.check(config.get(name)==expected,tag+" config "+name,config.get(name))
        audit.check(str(config.get("device","")).startswith("cuda"),tag+" CUDA")
        for case,(angles,labels) in CASES.items():
            audit.check(config["cases"][case]["angles_degrees"]==angles,tag+" angles "+case)
            audit.check(config["cases"][case]["labels"]==labels,tag+" labels "+case)
        checked[tag]=scope_hashes
    return dict(checked_current_sources=current,configuration_source_checks=checked,
                note="Actual file hashes checked only for assigned producer/engine/dictionary sources; unrelated manifest entries were not opened.")


def compare_analysis(independent_directory, analysis_directory):
    """Compare already frozen, independently computed scientific scalars.

    This metadata-only stage imports no analyzer and evaluates no raw model.
    It runs after independent_results.json exists, preserving discovery order.
    """
    independent_directory=independent_directory.resolve()
    analysis_directory=analysis_directory.resolve()
    independent=read_json(independent_directory/"independent_results.json")
    records=read_json(independent_directory/"replay_checks.json")
    metrics=read_json(analysis_directory/"metrics.json")
    validation=read_json(analysis_directory/"validation.json")
    comparisons=read_json(analysis_directory/"comparisons.json")
    audit=Audit();deltas=[]
    for item in metrics:
        case,method=item["case"],item["method"]
        own_ref=next(x for x in independent["refinement"] if x["case"]==case and x["method"]==method)
        full_ref=next(x for x in independent["refinement"] if x["case"]==case and x["method"]=="full")
        audit.check(item["valid"]==(own_ref["passed"] and full_ref["passed"]),case+method+" validity")
        audit.close(item["refinement_max"],own_ref["maximum"],case+method+" refinement")
        audit.close(item["full_refinement_max"],full_ref["maximum"],case+method+" full refinement")
        audit.check((item["K1"],item["K2"])==DIMS[method],case+method+" dimensions")
        for slot,tag in enumerate(("primary","refined")):
            own=next(x for x in independent["metrics"] if x["case"]==case and x["method"]==method
                     and (x.get("slot")==slot or ("slot" not in x and x["level"]==slot)))
            record=next(x for x in records if x["case"]==case and x["method"]==method and x["level"]==own["level"])
            audit.check(Path(item[tag+"_path"])==ROOT/record["path"],case+method+tag+" selected path")
            audit.close(item[tag+"_loss"],record["loss"],case+method+tag+" loss")
            audit.close(item[tag+"_time"],record["time"],case+method+tag+" time")
            audit.check(item[tag+"_status"]==record["status"],case+method+tag+" status")
            for key,author_key in (("rms","rms"),("l1","l1"),("maximum","max_abs")):
                delta=audit.close(item[tag+"_"+author_key],own[key],case+method+tag+key)
                deltas.append(delta)
                audit.close(item[tag+"_"+author_key+"_grid4096"],own["grid4096"][key],case+method+tag+key+" grid4096")
                audit.close(item[tag+"_"+author_key+"_grid_change"],own["grid8192_vs4096"][key],case+method+tag+key+" grid difference")
    for entry in validation.values():
        own_ref=next(x for x in independent["refinement"] if x["case"]==entry["case"] and x["method"]==entry["method"])
        audit.check(entry["valid"]==own_ref["passed"],entry["case"]+entry["method"]+" validation")
        for attempt in entry["attempts"]:
            own=next(x for x in records if ROOT/x["path"]==Path(attempt["path"]))
            audit.check(attempt["arrays_sha256"]==own["source_arrays_sha256"],own["path"]+" raw file digest")
            audit.close(attempt["recomputed_loss"],own["loss"],own["path"]+" independently replayed loss")
            audit.check(attempt["first_crossing"]==own["first_recorded_crossing"],own["path"]+" first crossing")
    for entry in comparisons:
        own=next(x for x in independent["comparisons"] if x["case"]==entry["case"] and x["p"]==entry["p"])
        audit.check(entry["ordering_agrees"]==own["stable_ordering"],entry["case"]+str(entry["p"])+" ordering")
        valid=all(next(x["passed"] for x in independent["refinement"] if x["case"]==entry["case"] and x["method"]==method)
                  for method in ("full",f"new_p{entry['p']}",f"old_p{entry['p']}"))
        audit.check(entry["valid"]==valid,entry["case"]+str(entry["p"])+" comparison validity")
        for tag,pair in zip(("primary","refined"),own["levels"]):
            audit.close(entry[tag+"_new_rms"],pair["new"]["rms"],entry["case"]+tag+" comparison new RMS")
            audit.close(entry[tag+"_old_rms"],pair["old"]["rms"],entry["case"]+tag+" comparison old RMS")
            audit.close(entry[tag+"_old_over_new_rms"],1/pair["ratio"],entry["case"]+tag+" ratio")
            audit.check(entry[tag+"_winner"]==("new" if pair["new_lower"] else "old"),entry["case"]+tag+" winner")
        verdict=("new" if own["levels"][-1]["new_lower"] else "old") if valid and own["stable_ordering"] else "inconclusive"
        audit.check(entry["verdict"]==verdict,entry["case"]+str(entry["p"])+" verdict")
    agreement=dict(passed=not audit.failures,checks=audit.count,failures=audit.failures,
        maximum_metric_absolute_difference=max(deltas),
        independent_results_sha256=sha(independent_directory/"independent_results.json"),
        analysis_directory=str(analysis_directory.relative_to(ROOT)),
        compared_files_sha256={name:sha(analysis_directory/(name+".json")) for name in ("metrics","validation","comparisons")})
    save_json(independent_directory/(analysis_directory.name+"_agreement.json"),agreement)
    print(json.dumps(agreement),flush=True)


@torch.no_grad()
def audit_cell(audit, path, method, case, level, initial, dictionaries, device):
    name=f"{case}/{method}/level{level}"
    summary=read_json(path/"summary.json")
    with np.load(path/"arrays.npz",allow_pickle=False) as file:
        saved={key:tensor(file[key],device) for key in file.files if key not in ("M",)}
    bases=None if method=="full" else (saved["b1"],saved["b2"])
    expected_angles=tensor(CASES[case][0],device)*(math.pi/180)
    train=torch.stack([expected_angles.cos(),expected_angles.sin()],1)
    audit.close(maximum(saved["training_inputs"]-train),0,name+" training grid")
    audit.close(maximum(saved["labels"]-tensor(CASES[case][1],device)),0,name+" labels",0)
    grid_deltas={}
    for stem,count in (("circle",2048),("endpoint",8192)):
        theta=torch.arange(count,dtype=torch.float64,device=device)*(2*math.pi/count)
        grid=torch.stack([theta.cos(),theta.sin()],1)
        grid_deltas[stem]=max(maximum(saved[stem+"_angles"]-theta),maximum(saved[stem+"_inputs"]-grid))
        audit.close(grid_deltas[stem],0,name+" "+stem+" grid")
    audit.close(maximum(saved["w"][0]-initial[0]),0,name+" initial w",0)
    audit.close(maximum(saved["c"][0]-initial[1]),0,name+" initial c",0)
    dictionary_delta=0
    if bases is not None:
        expected=dictionaries[method]
        for layer,(basis,reference) in enumerate(zip(bases,expected["bases"]),1):
            audit.check(tuple(basis.shape)==(4096,expected["dimensions"][layer-1]),name+f" dimensions {layer}")
            delta=maximum(basis-reference)
            dictionary_delta=max(dictionary_delta,delta)
            audit.close(delta,0,name+f" independent basis {layer}")
        audit.close(maximum(saved["g"]-initial[0]),0,name+" frozen g",0)
        for p in ("p1","p2"):
            audit.close(maximum(saved[p]-1/4096),0,name+" population "+p,0)
        audit.close(maximum(saved["D"]-expected["projected"]),0,name+" projected D")
    endpoint=None; prediction_delta=0; loss_delta=0; snapshot_losses=[]
    times, losses = saved["times"],saved["losses"]
    audit.check(bool(torch.isfinite(losses).all()),name+" finite loss history")
    audit.check(bool((times[1:]>times[:-1]).all()),name+" increasing times")
    audit.close(maximum(times[1:]-times[:-1]-saved["accepted_steps"]),0,name+" accepted step times")
    audit.check(bool((saved["local_error_ratios"]<=1).all()),name+" accepted embedded errors")
    audit.check(bool((losses[1:]<=losses[:-1]*(1+1e-8)+1e-12).all()),name+" decreasing-loss acceptance")
    audit.check(len(times)==summary["steps"]+1,name+" steps")
    audit.close(float(times[-1]),summary["time"],name+" final time")
    audit.close(float(losses[-1]),summary["loss"],name+" stored final loss")
    audit.close(summary["rtol"],6.25e-5/4**level,name+" rtol",1e-20)
    audit.close(summary["atol"],6.25e-7/4**level,name+" atol",1e-20)
    audit.check(float(times[-1])<=10000 and summary["steps"]<=30000,name+" trajectory bounds")
    first_crossing=bool((losses[:-1]>1e-3).all() and losses[-1]<=1e-3)
    audit.check(summary["status"]=="fitted" and first_crossing,name+" first recorded fitting crossing",summary["status"])
    count=0
    for i,middle_cpu in enumerate(snapshots(path/"arrays.npz","M")):
        middle=tensor(middle_cpu,device)
        state=(saved["w"][i],saved["c"][i],middle)
        audit.check(all(bool(torch.isfinite(x).all()) for x in state),name+f" finite snapshot {i}")
        if i==0:
            expected=initial[2] if method=="full" else dictionaries[method]["projected"]
            audit.close(maximum(middle-expected),0,name+" common/projected middle initialization")
        replay=predict(state,saved["circle_inputs"],bases)
        delta=maximum(replay-saved["circle_predictions"][i]);prediction_delta=max(prediction_delta,delta)
        audit.close(delta,0,name+f" snapshot prediction {i}")
        fitted_loss=float((predict(state,train,bases)-saved["labels"]).square().mean())
        closest=int((times-saved["snapshot_times"][i]).abs().argmin())
        audit.close(float(times[closest]),float(saved["snapshot_times"][i]),name+f" snapshot time {i}")
        delta=audit.close(fitted_loss,float(losses[closest]),name+f" snapshot loss {i}")
        loss_delta=max(loss_delta,delta);snapshot_losses.append(fitted_loss)
        if i==len(saved["snapshot_times"])-1:
            endpoint=predict(state,saved["endpoint_inputs"],bases)
        count+=1
    audit.check(count==len(saved["snapshot_times"]),name+" snapshot count")
    audit.close(float(saved["snapshot_times"][-1]),summary["time"],name+" endpoint state time")
    end_delta=maximum(endpoint-saved["endpoint_prediction"])
    audit.close(end_delta,0,name+" endpoint replay")
    record=dict(case=case,method=method,level=level,path=str(path.relative_to(ROOT)),
        status=summary["status"],loss=snapshot_losses[-1],time=summary["time"],
        first_recorded_crossing=first_crossing,steps=summary["steps"],snapshots=count,
        snapshot_prediction_max_delta=prediction_delta,endpoint_prediction_max_delta=end_delta,
        snapshot_loss_max_delta=loss_delta,independent_basis_max_delta=dictionary_delta,
        grid_max_deltas=grid_deltas,source_arrays_sha256=sha(path/"arrays.npz"),
        source_summary_sha256=sha(path/"summary.json"))
    print(json.dumps(dict(checked=name,status=record["status"],replay_delta=max(prediction_delta,end_delta))),flush=True)
    return record,endpoint


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--device")
    parser.add_argument("--out",type=Path,default=GENERATED/"comparison_independent01")
    parser.add_argument("--analysis",type=Path)
    parser.add_argument("--compare-only",action="store_true")
    args=parser.parse_args()
    if args.compare_only:
        if args.analysis is None:
            parser.error("--compare-only requires --analysis")
        compare_analysis(args.out,args.analysis)
        return
    if args.device is None:
        parser.error("CUDA replay requires --device")
    args.out.mkdir(parents=True,exist_ok=False)
    if not torch.cuda.is_available() or not args.device.startswith("cuda"):
        raise RuntimeError("Protocol requires CUDA; CPU replay is forbidden")
    torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False;torch.set_float32_matmul_precision("highest")
    torch.cuda.set_device(args.device)
    start=time.monotonic(); audit=Audit()
    initial_path=ARCHIVE/"scaling_width4096_refined01/quadrant_pairs_full/arrays.npz"
    initial_cpu=[next(snapshots(initial_path,k)) for k in ("w","c","M")]
    initial=[tensor(value,args.device) for value in initial_cpu]
    initial_hashes={key:hashlib.sha256(value.tobytes()).hexdigest() for key,value in zip(("w","c","M"),initial_cpu)}
    dictionaries,quadrature=independent_dictionaries(initial)
    save_json(args.out/"dictionary_checks.json",dict(quadrature=quadrature,
        methods={k:{a:b for a,b in v.items() if a not in ("bases","projected")} for k,v in dictionaries.items()}))
    for method,value in dictionaries.items():
        for index,diagnostic in enumerate(value["diagnostics"]):
            audit.check(diagnostic["passed"],method+f" dictionary gate {index}",diagnostic)
    configurations=[]
    preflight=GENERATED/"comparison_preflight02"
    configurations.append(("preflight",read_json(preflight/"config_worker0.json")))
    audit.check(read_json(preflight/"validation.json")["passed"],"recorded preflight pass")
    cells=[]
    for level,tag in enumerate(("primary01","refined01")):
        for worker,case in enumerate(CASES):
            new_root=GENERATED/("comparison_"+tag)
            old_root=ARCHIVE/("scaling_width4096_"+tag)
            for root,prefix in ((new_root,"config_worker"),(old_root,"config_user_width4096_worker")):
                config=read_json(root/f"{prefix}{worker}.json")
                configurations.append((root.name+f"/worker{worker}",config))
                audit.close(config["rtol"],6.25e-5/4**level,root.name+" config rtol",1e-20)
                audit.close(config["atol"],6.25e-7/4**level,root.name+" config atol",1e-20)
                if root==new_root:
                    audit.check(config["initial_array_sha256"]==initial_hashes,root.name+" initial array hashes")
                    audit.check(config["initial_archive_sha256"]==sha(initial_path),root.name+" initial archive hash")
                    completion=read_json(root/f"completion_worker{worker}.json")
                    audit.check(completion["total"]==completion["expected"]==4,root.name+f" worker{worker} complete")
                    audit.check(completion["fitted"]==4,root.name+f" worker{worker} all fitted")
            for method in ("full",*DIMS):
                archived=method in ("full","old_p1","old_p3")
                path=(old_root if archived else new_root)/(case+"_"+method.replace("old_","ours_") if archived else case+"_"+method)
                cells.append((path,method,case,level))
    extra_root=GENERATED/"comparison_extra01"
    if extra_root.exists():
        for config_path in sorted(extra_root.glob("config_worker*.json")):
            config=read_json(config_path); worker=config["worker"];case=list(CASES)[worker]
            configurations.append(("extra/worker"+str(worker),config))
            audit.check(config["level"]==2,"extra level")
            audit.check(config["initial_array_sha256"]==initial_hashes,"extra initial array hashes")
            audit.check(config["worker_limit_seconds"]<=200,"extra worker budget")
            audit.close(config["rtol"],6.25e-5/16,"extra config rtol",1e-20)
            audit.close(config["atol"],6.25e-7/16,"extra config atol",1e-20)
            completion=read_json(extra_root/f"completion_worker{worker}.json")
            audit.check(completion["total"]==completion["expected"]==len(config["methods"]),"extra completion")
            audit.check(completion["fitted"]==len(config["methods"]),"extra fit status")
            for method in config["methods"]:
                cells.append((extra_root/(case+"_"+method),method,case,2))
    sources=source_config_checks(audit,configurations)
    save_json(args.out/"source_checks.json",sources)
    records=[];predictions={}
    for path,method,case,level in cells:
        record,prediction=audit_cell(audit,path,method,case,level,initial,dictionaries,args.device)
        records.append(record);predictions[(case,method,level)]=prediction
        save_json(args.out/"replay_checks.json",records)
    metrics=[];refinement=[];comparisons=[]
    for case in CASES:
        for method in ("full",*DIMS):
            available=sorted(level for c,m,level in predictions if c==case and m==method)
            selected=available[-2:]
            coarse,fine=[predictions[(case,method,k)] for k in selected]
            result=norms(fine-coarse)
            refinement.append(dict(case=case,method=method,selected_levels=selected,**result,passed=result["maximum"]<=.01))
            audit.check(result["maximum"]<=.01,f"{case}/{method} endpoint refinement",result["maximum"])
            if 2 in available:
                previous=norms(predictions[(case,method,1)]-predictions[(case,method,0)])
                audit.check(previous["maximum"]>.01,f"{case}/{method} allowed extra trigger",previous["maximum"])
                audit.check(method in ("new_p1","new_p2","new_p3","old_p2"),"extra method eligibility")
            if method=="full":
                continue
            for slot,level in enumerate(selected):
                reference_level=slot
                delta=predictions[(case,method,level)]-predictions[(case,"full",reference_level)]
                full=norms(delta);half=norms(delta[::2])
                metrics.append(dict(case=case,method=method,level=level,slot=slot,reference_level=reference_level,
                    selected=level in selected,**full,grid4096=half,
                    grid8192_vs4096={key:abs(full[key]-half[key]) for key in full}))
        for p in (1,2,3):
            new_method=f"new_p{p}";old_method=f"old_p{p}"
            nlevels=next(x["selected_levels"] for x in refinement if x["case"]==case and x["method"]==new_method)
            olevels=next(x["selected_levels"] for x in refinement if x["case"]==case and x["method"]==old_method)
            pair=[]
            # Latest two attempts for each cell. When an extra is used, pair
            # coarse/fine slots; every comparison uses the SAME reference.
            for slot in (0,1):
                nl,ol=nlevels[slot],olevels[slot]
                rl=slot
                reference=predictions[(case,"full",rl)]
                new=norms(predictions[(case,new_method,nl)]-reference)
                old=norms(predictions[(case,old_method,ol)]-reference)
                pair.append(dict(slot=slot,new_level=nl,old_level=ol,reference_level=rl,
                    new=new,old=old,ratio=new["rms"]/old["rms"],new_lower=new["rms"]<old["rms"]))
            stable=pair[0]["new_lower"]==pair[1]["new_lower"]
            valid=all(next(x["passed"] for x in refinement if x["case"]==case and x["method"]==m)
                      for m in ("full",new_method,old_method))
            comparisons.append(dict(case=case,p=p,levels=pair,stable_ordering=stable,
                valid=valid,conclusion=(("new_lower" if pair[1]["new_lower"] else "new_higher")
                    if stable else "unresolved_reversal") if valid else "unresolved_gate"))
    output=dict(schema="independent-comparison-v1",gpu=torch.cuda.get_device_name(args.device),
        device=args.device,dtype="float64",seconds=time.monotonic()-start,
        checked_assertions=audit.count,failures=audit.failures,passed=not audit.failures,
        metrics=metrics,refinement=refinement,comparisons=comparisons,
        checker_sha256=sha(__file__),protocol_sha256=sha(HERE/"COMPARISON_PROTOCOL.md"),
        limitations=["No rerun of training or every accepted intermediate state; all saved snapshots replayed.",
            "First crossing means the recorded accepted-step/chord interpolation rule, not a certified exact-flow first crossing.",
            "Sampled circle norms and refinement are numerical diagnostics, not continuum error bounds."])
    save_json(args.out/"independent_results.json",output)
    print(json.dumps(dict(passed=output["passed"],assertions=audit.count,failures=audit.failures,
                          seconds=output["seconds"])),flush=True)
    if args.analysis is not None:
        compare_analysis(args.out,args.analysis)


if __name__=="__main__":
    main()
