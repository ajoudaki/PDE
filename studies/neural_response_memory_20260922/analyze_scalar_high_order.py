"""Read-only raw-array analysis of the frozen orders-five/six campaign.

No coefficient generation, training integration or dense-network evaluation.
Training probes are transported through archived segments to recompute gaps.
"""

import argparse
import csv
import json
from pathlib import Path
import re
import shutil
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from analyze_scalar_long_time import digest, nested, rms, scalar, spatial_metrics
from analyze_scalar_wide import SavedInputs, analyze_case as wide_case, verdict
from scalar_high_order_engine import ScalarHierarchy, recenter_coefficients


HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/"data/generated/neural_response_memory_20260922"
SEEDS = (20260920, 20260927)
TARGET = 1e-6
COLORS = {"dense":"#171717", "order2":"#81858b", "order4":"#7135a8",
          "order5":"#007f85", "order6":"#da7b2e"}
LABELS = {"dense":"Dense GPU", "order2":"Frozen kernel", "order4":"Order four",
          "order5":"Order five", "order6":"Order six"}


class Reader(SavedInputs):
    def selected(self, path, names):
        with np.load(self.track(path), allow_pickle=False) as data:
            return {name:data[name] for name in names if name in data.files}

    def training_probes(self, path):
        """Decompress one tensor at a time and retain only its last eight rows."""
        with np.load(self.track(path), allow_pickle=False) as data:
            names = [key for key in data.files if re.fullmatch(r"T[1-6]", key)]
            return {key:np.array(data[key][-8:], copy=True) for key in names}


def archive_manifest(reader,folder):
    path=folder/"manifest.json"
    if not path.exists():
        return dict(passed=False,reason="missing manifest")
    manifest=reader.json(path)
    checks={}
    def matches(path,expected):
        if not path.is_file():
            return False
        reader.track(path)
        return reader.hashes[str(path.resolve())]==expected
    for group,prefix in (("outputs",folder),("sources",folder/"sources")):
        checks[group]={name:matches(prefix/name,expected)
                       for name,expected in manifest.get(group,{}).items()}
    command=manifest.get("command",[])
    cap=float(command[command.index("--seconds")+1]) if "--seconds" in command else 600.
    return dict(passed=bool(checks["outputs"] and checks["sources"]
                           and all(value for group in checks.values() for value in group.values())),
                checks=checks,wall_cap_seconds=cap,inputs=manifest.get("inputs",{}))


def tensor_comparison(reader, first, second, order=6):
    checks = {}
    with np.load(reader.track(first), allow_pickle=False) as a, np.load(reader.track(second), allow_pickle=False) as b:
        for j in range(1, order+1):
            key = "T"+str(j)
            if key not in a.files or key not in b.files:
                checks[key] = dict(passed=False, reason="missing coefficient")
                continue
            x, y = a[key], b[key]
            if x.shape != y.shape:
                checks[key] = dict(passed=False, reason="shape mismatch")
                continue
            difference = float(np.max(abs(x-y)))
            bound = 1e-11+1e-9*float(np.max(abs(x)))
            checks[key] = dict(maximum_difference=difference, bound=bound,
                               bitwise_equal=bool(np.array_equal(x,y)), passed=difference<=bound)
            del x, y
    return dict(tensors=checks, passed=all(value["passed"] for value in checks.values()))


def legacy_comparison(initial, old):
    result = {}
    for j, name in enumerate(("f", "Theta", "C", "Q"), 1):
        key = "T"+str(j)
        difference = float(np.max(abs(initial[key]-old[name])))
        bound = 1e-11+1e-9*float(np.max(abs(old[name])))
        result[key] = dict(maximum_difference=difference, bound=bound, passed=difference<=bound)
    return dict(tensors=result, passed=all(value["passed"] for value in result.values()))


def initialization_check(record, old_hash):
    config = record.get("configuration", {})
    result = dict(status=record.get("status"), width=record.get("width", config.get("width")),
                  device=record.get("device",config.get("device")), dtype=record.get("dtype"),
                  initialization_hash_matches=record.get("initialization_hash")==old_hash,
                  deterministic_algorithms=record.get("deterministic_algorithms"),tf32=record.get("tf32"),
                  whole_action_limits_satisfied=record.get("whole_action_limits_satisfied",False))
    result["passed"] = (result["status"]=="complete" and result["width"]==2048
        and str(result["device"]).startswith("cuda") and result["dtype"]=="float64"
        and result["initialization_hash_matches"] and result["deterministic_algorithms"] is True
        and result["tf32"] is False and result["whole_action_limits_satisfied"])
    return result


def rates_at_boundaries(arrays, labels):
    m = len(labels)
    records = []
    for time, state in zip(arrays["segment_times"], arrays["segment_states"]):
        residual = state[:m]-labels
        kernel = state[m:m+m*m].reshape(m,m)
        square = float(residual@residual)
        rate = float(residual@kernel@residual/square) if square else 0.
        records.append(dict(time=float(time),loss=square/m,effective_rate=rate,
                            relative_loss_derivative=-4/m*rate,
                            minimum_kernel_eigenvalue=float(np.linalg.eigvalsh((kernel+kernel.T)/2)[0])))
    losses = arrays["losses"]
    increases = np.diff(losses)>np.maximum(1e-12,1e-9*losses[:-1])
    return dict(boundaries=records,negative_sampled_rates=[item for item in records if item["effective_rate"]<0],
                accepted_steps_with_resolved_loss_increase=int(np.count_nonzero(increases)),
                maximum_saved_loss=float(np.max(losses)),
                time_at_maximum_saved_loss=float(arrays["times"][np.argmax(losses)]),
                interpretation="L'/L=-(4/M)rho. A negative sampled rho gives instantaneous loss growth.")


def replay_training(initial, probe, arrays, order, endpoint=None):
    labels = initial["labels"]
    names = ["T"+str(j) for j in range(1,order+1)]
    model = ScalarHierarchy({name:initial[name] for name in names},labels,order)
    if probe is not None and not all(name in probe for name in names):
        probe=None
    passive = {name:np.array((initial if probe is None else probe)[name],copy=True) for name in names}
    previous = model.initial_state()[:model.training_size]
    gaps, anchor_changes = [], []
    tensor_gaps = {name:0. for name in names[:-1]}
    for index,state in enumerate(arrays["segment_states"]):
        anchor_changes.append(float(np.max(abs(arrays["segment_training"][index]-previous))))
        passive = recenter_coefficients(passive,model.signatures(state))
        current = model.tensors(state)
        for name in names[:-1]:
            tensor_gaps[name] = max(tensor_gaps[name],rms(passive[name]-current[name]))
        gaps.append(rms(passive["T1"]-state[:model.M]))
        previous = model.training_state(state)
    final_state_match = float(np.max(abs(arrays["state"][:model.training_size]-previous)))
    final_f_match = rms(arrays["state"][:model.M]-arrays["train_f"])
    result = dict(peak_training_probe_gap=max(gaps,default=0.),gaps=gaps,
                  maximum_anchor_discontinuity=max(anchor_changes,default=0.),
                  final_training_state_difference=final_state_match,final_f_difference=final_f_match,
                  tensor_gaps=tensor_gaps,original_probe_coefficients_used=probe is not None)
    if endpoint is not None:
        result["replay_vs_saved_probe"] = rms(passive["T1"]-endpoint["train_probe"])
        result["saved_gap_difference"] = float(np.max(abs(np.asarray(gaps)-endpoint["segment_training_gaps"]))) if gaps else 0.
        result["endpoint_training_difference"] = rms(endpoint["train_f"]-arrays["train_f"])
    result["passed"] = (result["peak_training_probe_gap"]<=1e-4 and result["maximum_anchor_discontinuity"]==0.
        and final_state_match==0. and final_f_match==0.
        and result.get("replay_vs_saved_probe",0.)<=1e-10
        and result.get("saved_gap_difference",0.)<=1e-10
        and result.get("endpoint_training_difference",0.)==0.)
    return result


def read_high_run(reader, folder, initial, probes, order):
    record = reader.json(folder/"result.json")
    arrays = reader.arrays(folder/"trajectory.npz")
    endpoint_folder = folder.with_name(folder.name+"_readout")
    endpoint = None
    readout_record = None
    if (endpoint_folder/"endpoint.npz").exists():
        endpoint = reader.arrays(endpoint_folder/"endpoint.npz")
        readout_record = reader.json(endpoint_folder/"result.json")
        arrays.update({key:value for key,value in endpoint.items() if key in ("grid","off_grid","train_probe")})
    raw_loss = rms(arrays["train_f"]-initial["labels"])**2
    probe = replay_training(initial,probes,arrays,order,endpoint)
    manifest=archive_manifest(reader,folder)
    resource_pass=record["seconds"]<=manifest.get("wall_cap_seconds",0.) and record["peak_rss_bytes"]<8*1024**3 and record["accepted_steps"]<=100000
    bracket=record.get("crossing_bracket")
    fitted_event=(record["status"]!="fitted" or bool(bracket and bracket["left_time"]<=float(arrays["time"])<=bracket["right_time"]
        and bracket["left_loss"]>TARGET and bracket["right_loss"]<=TARGET
        and np.all(arrays["losses"][:-1]>TARGET) and abs(raw_loss-TARGET)<=1e-6*TARGET))
    readout_manifest=archive_manifest(reader,endpoint_folder) if endpoint is not None else None
    readout_match=(endpoint is None or (Path(readout_record["run"]).resolve()==folder.resolve()
        and readout_record["status"]==record["status"] and readout_record["order"]==order
        and readout_record["replay_seconds"]<=readout_manifest.get("wall_cap_seconds",0.)
        and readout_record["peak_rss_bytes"]<8*1024**3 and readout_manifest["passed"]))
    archive = dict(record_loss_difference=abs(raw_loss-record["loss"]),
                   record_time_difference=abs(float(arrays["time"])-record["time"]),
                   saved_final_loss_difference=abs(float(arrays["losses"][-1])-raw_loss),
                   strictly_increasing_times=bool(np.all(np.diff(arrays["times"])>0)),
                   from_original_time=bool(arrays["times"][0]==0.),
                   endpoint_time_difference=abs(float(endpoint["time"])-float(arrays["time"])) if endpoint is not None else 0.,
                   segment_count_matches=len(arrays["segment_times"])==len(arrays["segment_states"])==len(arrays["segment_training"])==record["segments"],
                   last_segment_time_matches=bool(len(arrays["segment_times"]) and arrays["segment_times"][-1]==arrays["time"]),
                   finite_arrays=bool(all(np.isfinite(value).all() for value in arrays.values())),
                   fitted_event_consistent=fitted_event,resource_limits_pass=resource_pass,
                   readout_provenance_pass=readout_match,manifest=manifest,readout_manifest=readout_manifest)
    archive["passed"] = (archive["record_loss_difference"]<=1e-10*max(1.,raw_loss)
        and archive["record_time_difference"]==0. and archive["saved_final_loss_difference"]<=1e-10*max(1.,raw_loss)
        and archive["strictly_increasing_times"] and archive["from_original_time"] and archive["endpoint_time_difference"]==0.
        and archive["segment_count_matches"] and archive["last_segment_time_matches"] and archive["finite_arrays"]
        and fitted_event and resource_pass and readout_match and manifest["passed"])
    return dict(folder=folder,record=record,arrays=arrays,endpoint=endpoint,readout_record=readout_record,
                raw_loss=raw_loss,probe=probe,archive=archive,rates=rates_at_boundaries(arrays,initial["labels"]))


def compare_runs(first, second, discrepancy):
    fitted = first["record"]["status"]==second["record"]["status"]=="fitted"
    readouts = "grid" in first["arrays"] and "grid" in second["arrays"]
    change = rms(np.subtract(*nested(first["arrays"]["grid"],second["arrays"]["grid"]))) if readouts else None
    dt = abs(float(first["arrays"]["time"])-float(second["arrays"]["time"]))/max(1.,float(second["arrays"]["time"]))
    result = dict(fitted_statuses=fitted,endpoint_readouts_present=readouts,numerical_change=change,time_relative_change=dt,
                  raw_loss_target_pass=max(first["raw_loss"],second["raw_loss"])<=TARGET*(1+1e-6),
                  probe_pass=first["probe"]["passed"] and second["probe"]["passed"],
                  archive_pass=first["archive"]["passed"] and second["archive"]["passed"])
    result["passed"] = bool(fitted and readouts and result["raw_loss_target_pass"] and result["probe_pass"]
        and result["archive_pass"] and change<=.002 and change<=.1*max(discrepancy,1e-6) and dt<=.001)
    return result


def resolution_folders(directory,order):
    pattern = re.compile(r"order"+str(order)+r"_resolution([0-9]+)")
    return sorted((p for p in directory.iterdir() if p.is_dir() and pattern.fullmatch(p.name)
                   and (p/"result.json").exists()),key=lambda p:int(pattern.fullmatch(p.name).group(1)))


def improvement(lower, higher, dense_change):
    if "spatial" not in lower or "spatial" not in higher:
        return dict(status="no_matched_endpoint",resolved_improvement=False)
    a,b = lower["spatial"]["circle_rms"],higher["spatial"]["circle_rms"]
    ca = lower.get("refinement",{}).get("numerical_change")
    cb = higher.get("refinement",{}).get("numerical_change")
    numeric = None if ca is None or cb is None else 10*(ca+cb+dense_change)
    valid = lower.get("direct_grid_qualified",False) and higher.get("direct_grid_qualified",False)
    resolved = valid and numeric is not None and a-b>.01*a and a-b>numeric
    return dict(lower_error=a,higher_error=b,ratio=b/a if a else None,reduction=a-b,
                one_percent_threshold=.01*a,numerical_threshold=numeric,
                direct_grid_valid=bool(valid),resolved_improvement=bool(resolved),
                status="resolved_improvement" if resolved else "unqualified" if not valid else
                       "worse" if b>a else "unresolved_improvement")


def analyze_seed(reader,args,seed):
    name = "quadrant_alternating_n2048_seed"+str(seed)
    old_source = DATA/"scalar_wide_source01"/name
    old_primary = DATA/"scalar_wide_primary01"/name
    reference,plot = wide_case(reader,old_source,old_primary,
        DATA/"scalar_wide_source_reproduction01"/name if seed==SEEDS[0] else None,
        DATA/"scalar_wide_reproduction01"/name if seed==SEEDS[0] else None)
    old_initial = reader.arrays(old_source/"initial_coefficients.npz")
    old_receipt = reader.json(old_source/"initialization.json")
    source = args.training/("seed"+str(seed))
    initial = reader.arrays(source/"coefficients.npz")
    init_record = reader.json(source/"result.json")
    init_gate = initialization_check(init_record,old_receipt["initialization_hash"])
    init_gate["manifest"]=archive_manifest(reader,source)
    init_gate["inputs_match"]=bool(np.array_equal(initial["inputs"],old_initial["inputs"]))
    init_gate["labels_match"]=bool(np.array_equal(initial["labels"],old_initial["labels"]))
    init_gate["passed"]=bool(init_gate["passed"] and init_gate["manifest"]["passed"] and init_gate["inputs_match"] and init_gate["labels_match"])
    legacy = legacy_comparison(initial,old_initial)
    probes_folder = args.probes/("seed"+str(seed))
    probe_path = probes_folder/"coefficients.npz"
    probes = reader.training_probes(probe_path) if probe_path.exists() else None
    probe_meta = reader.selected(probe_path,("angles","off_angles","inputs","labels","probe_inputs")) if probes is not None else None
    probe_receipt = reader.json(probes_folder/"result.json") if (probes_folder/"result.json").exists() else None
    probe_gate = initialization_check(probe_receipt,old_receipt["initialization_hash"]) if probe_receipt else dict(passed=False,status="missing")
    if probes is not None:
        probe_gate["manifest"]=archive_manifest(reader,probes_folder)
        probe_gate["inputs_match"]=bool(np.array_equal(probe_meta["inputs"],initial["inputs"]))
        probe_gate["labels_match"]=bool(np.array_equal(probe_meta["labels"],initial["labels"]))
        probe_gate["training_queries_match"]=bool(np.array_equal(probe_meta["probe_inputs"][-8:],initial["inputs"]))
        ngrid=len(probe_meta["angles"])
        circle=lambda angles:np.column_stack((np.cos(angles),np.sin(angles)))
        expected_grid=2*np.pi*np.arange(ngrid)/ngrid
        expected_off=2*np.pi*(np.arange(32)+np.sqrt(2)/10)/32
        expected_points=np.vstack((circle(expected_grid),circle(expected_off),initial["inputs"]))
        probe_gate["query_order_matches"]=bool(np.array_equal(probe_meta["angles"],expected_grid)
            and np.array_equal(probe_meta["off_angles"],expected_off)
            and probe_meta["probe_inputs"].shape==expected_points.shape
            and np.max(abs(probe_meta["probe_inputs"]-expected_points))<2e-15)
        probe_gate["training_coefficients"]={key:dict(maximum_difference=float(np.max(abs(value-initial[key]))),
            passed=bool(np.max(abs(value-initial[key]))<=1e-11+1e-9*np.max(abs(initial[key])))) for key,value in probes.items()}
        probe_gate["passed"]=bool(probe_gate["passed"] and probe_gate["manifest"]["passed"] and probe_gate["inputs_match"]
            and probe_gate["labels_match"] and probe_gate["training_queries_match"] and probe_gate["query_order_matches"]
            and all(value["passed"] for value in probe_gate["training_coefficients"].values()))
    record = dict(seed=seed,width=2048,samples=8,case="quadrant_alternating",initialization=init_record,
                  initialization_gate=init_gate,legacy_coefficients=legacy,probe_initialization=probe_receipt,
                  probe_initialization_gate=probe_gate,dense=reference["dense"],
                  order2=reference["order2"],order4=reference["order4"],dense_checks=reference["dense_device_checks"])
    record["order4"]["refinement"] = reference["refinement"]["order4"]
    record["order2"]["refinement"] = dict(numerical_change=0.,passed=record["order2"]["spectral"]["passed"])
    record["order2"]["direct_grid_qualified"] = record["order2"]["verdict"] in ("agreement","inconclusive","adverse")
    record["dense_refinement"] = reference["refinement"]["dense"]
    fresh_training = args.reproduction_training/("seed"+str(seed))
    fresh_probes = args.reproduction_probes/("seed"+str(seed))
    reproduction_coefficients = {}
    fresh_initial = fresh_probe_values = None
    if seed==SEEDS[0] and (fresh_training/"coefficients.npz").exists():
        fresh_initial = reader.arrays(fresh_training/"coefficients.npz")
        reproduction_coefficients["training"] = tensor_comparison(reader,source/"coefficients.npz",fresh_training/"coefficients.npz")
        reproduction_coefficients["training_initialization"] = initialization_check(reader.json(fresh_training/"result.json"),old_receipt["initialization_hash"])
        reproduction_coefficients["training_initialization"]["manifest"]=archive_manifest(reader,fresh_training)
        reproduction_coefficients["training_initialization"]["passed"] &= bool(
            reproduction_coefficients["training_initialization"]["manifest"]["passed"]
            and np.array_equal(fresh_initial["inputs"],initial["inputs"])
            and np.array_equal(fresh_initial["labels"],initial["labels"]))
        if (fresh_probes/"coefficients.npz").exists():
            fresh_probe_values = reader.training_probes(fresh_probes/"coefficients.npz")
            fresh_max = max(int(key[1:]) for key in fresh_probe_values)
            reproduction_coefficients["probes"] = tensor_comparison(reader,probe_path,fresh_probes/"coefficients.npz",fresh_max)
            reproduction_coefficients["probe_initialization"] = initialization_check(reader.json(fresh_probes/"result.json"),old_receipt["initialization_hash"])
            reproduction_coefficients["probe_initialization"]["manifest"]=archive_manifest(reader,fresh_probes)
            reproduction_coefficients["probe_initialization"]["passed"] &= reproduction_coefficients["probe_initialization"]["manifest"]["passed"]
    record["coefficient_reproduction"] = reproduction_coefficients
    for order in (5,6):
        key = "order"+str(order)
        directory = args.campaign/("seed"+str(seed))
        folders = resolution_folders(directory,order)
        if len(folders)<2:
            raise RuntimeError("wait for both declared resolutions: "+str(directory)+"/"+key)
        runs = [read_high_run(reader,path,initial,probes,order) for path in folders]
        fine = runs[-1]
        arrays,run_record = fine["arrays"],fine["record"]
        spatial = spatial_metrics(arrays,probe_meta,plot["dense"]) if "grid" in arrays else None
        discrepancy = spatial["circle_rms"] if spatial else float("inf")
        refine = compare_runs(*runs[-2:],discrepancy)
        dense_change = record["dense_refinement"]["numerical_change"]
        dense_gate = (record["dense_refinement"]["passed"] and dense_change<=.1*max(discrepancy,1e-6))
        reproduction = dict(required=seed==SEEDS[0],passed=seed!=SEEDS[0])
        fresh_run = args.reproduction/("seed"+str(seed))/key
        if seed==SEEDS[0] and (fresh_run/"result.json").exists() and fresh_initial is not None:
            other = read_high_run(reader,fresh_run,fresh_initial,fresh_probe_values,order)
            comparison = compare_runs(fine,other,discrepancy)
            settings_match=(other["record"]["rtol"]==run_record["rtol"] and other["record"]["atol"]==run_record["atol"]
                            and other["record"]["order"]==order)
            training_reproduced=all(reproduction_coefficients.get(name,{}).get("passed",False)
                                   for name in ("training","training_initialization"))
            exact_archives={name:bool(np.array_equal(arrays[name],other["arrays"][name]))
                            for name in ("time","times","losses","state","train_f","segment_times","segment_states","segment_training")}
            nonfit_agreement=bool(run_record["status"]!="fitted" and run_record["status"]==other["record"]["status"]
                and run_record["message"]==other["record"]["message"] and settings_match and training_reproduced
                and fine["archive"]["passed"] and other["archive"]["passed"] and all(exact_archives.values()))
            reproduction.update(status=other["record"]["status"],loss=other["raw_loss"],time=float(other["arrays"]["time"]),
                comparison=comparison,probe=other["probe"],archive=other["archive"],
                same_terminal_status=run_record["status"]==other["record"]["status"],
                selected_tolerance_matches=settings_match,
                same_message=run_record["message"]==other["record"]["message"],
                exact_array_agreement=exact_archives,nonfit_reproduction_agreement=nonfit_agreement,
                nonfit_reproduction_rule="Same status, message and settings; fresh coefficients pass; both archives pass; saved trajectories bitwise equal.",
                relative_terminal_loss_difference=abs(other["raw_loss"]-fine["raw_loss"])/max(1e-300,fine["raw_loss"]),
                passed=bool(comparison["passed"] and settings_match and len(reproduction_coefficients)==4
                            and all(value["passed"] for value in reproduction_coefficients.values())))
        direct = bool(spatial and refine["passed"] and dense_gate and spatial["quadrature_pass"]
                      and init_gate["passed"] and legacy["passed"] and probe_gate["passed"] and reproduction["passed"])
        encoded = bool(direct and spatial["fourier_pass"])
        fitted = run_record["status"]=="fitted"
        failed_gates=[name for name,passed in (("fitted_status",fitted),("passive_endpoint",spatial is not None),
            ("scalar_refinement",refine["passed"]),("training_probe_consistency",fine["probe"]["passed"]),
            ("dense_refinement",dense_gate),("training_initialization",init_gate["passed"]),
            ("legacy_coefficients",legacy["passed"]),("probe_initialization",probe_gate["passed"]),
            ("matched_endpoint_reproduction",reproduction["passed"]),("spatial_quadrature",bool(spatial and spatial["quadrature_pass"]))) if not passed]
        item = dict(status=run_record["status"],loss=fine["raw_loss"],time=float(arrays["time"]),
            outcome_kind=("fitted" if fitted else "resource_limited" if run_record["status"] in ("wall_cap","memory_cap","step_cap")
                          else "physical_time_cap" if run_record["status"]=="time_cap" else "numerical_failure"),
            time_ratio_to_dense=float(arrays["time"])/record["dense"]["time"],
            wall_seconds=run_record["seconds"],replay_seconds=fine["readout_record"]["replay_seconds"] if fine["readout_record"] else None,
            wall_scope="CPU scalar integration/run including loading and saving; excludes initialization and passive replay. Runs can have different terminal outcomes.",
            rtol=run_record["rtol"],accepted_steps=run_record["accepted_steps"],nfev=run_record["nfev"],
            njev=run_record["njev"],nlu=run_record["nlu"],segments=run_record["segments"],
            peak_rss_bytes=run_record["peak_rss_bytes"],moving_state_scalars=2*sum(8**j for j in range(1,order)),
            initialized_training_scalars=sum(8**j for j in range(1,order+1)),
            probe=fine["probe"],archive=fine["archive"],rates=fine["rates"],refinement=refine,
            dense_refinement_pass=bool(dense_gate),reproduction=reproduction,
            direct_grid_qualified=direct,encoded_qualified=encoded,
            failed_direct_grid_gates=failed_gates,
            direct_grid_verdict=verdict(fitted,direct,discrepancy),verdict=verdict(fitted,encoded,discrepancy),
            resolution_records=[run["record"] for run in runs],resolution_rates=[run["rates"] for run in runs],
            resolution_checks=[dict(probe=run["probe"],archive=run["archive"]) for run in runs])
        if spatial is not None:
            item["spatial"] = spatial
        record[key] = item
        plot[key] = arrays
        plot[key+"_resolutions"]=[{name:run["arrays"][name] for name in ("times","losses")} for run in runs]
    record["comparisons"] = {higher+"_over_"+lower:improvement(record[lower],record[higher],record["dense_refinement"]["numerical_change"])
                             for lower,higher in (("order4","order5"),("order4","order6"),("order5","order6"))}
    return record,plot


def finish_figure(figure,axes,output,stem,title,subtitle):
    handles,labels=[],[]
    for axis in np.asarray(axes).flat:
        for handle,label in zip(*axis.get_legend_handles_labels()):
            if label not in labels:
                handles.append(handle); labels.append(label)
    short=figure.get_size_inches()[1]<6
    figure.suptitle(title,x=.07,y=.985,ha="left",fontsize=16,fontweight="bold")
    figure.text(.07,.925 if short else .947,subtitle,ha="left",fontsize=9.2,color="#444444")
    figure.subplots_adjust(left=.075,right=.985,top=.82 if short else .865,
                           bottom=.18 if short else .13,wspace=.26,hspace=.43)
    if handles:
        figure.legend(handles,labels,loc="lower center",ncol=min(4,len(labels)),frameon=False,fontsize=9)
    for suffix in ("png","pdf"):
        figure.savefig(output/(stem+"."+suffix),bbox_inches="tight")
    plt.close(figure)


def figures(output,records,plots):
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.spines.top":False,
                        "axes.spines.right":False,"savefig.dpi":220,"pdf.fonttype":42})
    loss_figure,loss_axes = plt.subplots(1,2,figsize=(12.4,5.6))
    circle_figure,circle_axes = plt.subplots(1,2,figsize=(12.4,5.6))
    compare_figure,compare_axes = plt.subplots(2,2,figsize=(12.4,8.6))
    failure_figure,failure_axes = plt.subplots(2,2,figsize=(12.4,8.6))
    models = ("dense","order2","order4","order5","order6")
    for index,(record,plot,axis,circle_axis) in enumerate(zip(records,plots,loss_axes,circle_axes)):
        seed = str(record["seed"])
        maximum_time = max(float(plot[key]["time"]) for key in models)
        maximum_loss = 1.
        for key in models:
            color,label = COLORS[key],LABELS[key]
            if key=="order2":
                times = np.concatenate(([0.],np.geomspace(.01,max(.02,float(plot[key]["time"])),600)))
                eig,components = plot["spectrum"]
                losses = np.exp(-.5*np.outer(times,eig))@(components**2)/8
            else:
                times,losses = plot[key]["times"],plot[key]["losses"]
            maximum_loss = max(maximum_loss,float(np.max(losses)))
            axis.plot(times,losses,color=color,label=label,linestyle="--" if key=="order2" else "-",linewidth=1.5)
            if record[key]["status"]!="fitted":
                axis.scatter(times[-1],losses[-1],marker="x",s=35,color=color,zorder=5)
        axis.axhline(TARGET,color="#b2652f",linestyle=":",linewidth=1.,label="Target MSE")
        axis.set_xscale("symlog",linthresh=1.); axis.set_yscale("log")
        axis.set_xlim(0.,maximum_time*1.15); axis.set_ylim(4e-7,maximum_loss*4)
        axis.set_xlabel("Physical training time"); axis.set_ylabel("Training mean squared error")
        axis.set_title("Eight inputs · seed "+seed); axis.grid(True,alpha=.14)
        text = "\n".join("P{}: {} · t={:.4g}".format(p,record["order"+str(p)]["status"].replace("_"," "),record["order"+str(p)]["time"]) for p in (5,6))
        axis.text(.97,.97,text,transform=axis.transAxes,ha="right",va="top",fontsize=8.3,
                  bbox=dict(facecolor="white",alpha=.88,edgecolor="none"))
        circle_axis.axvspan(10.,80.,color="#c9d9eb",alpha=.22,zorder=0)
        inset = circle_axis.inset_axes([.60,.08,.36,.25])
        for key in models:
            if record[key]["status"]!="fitted" or "grid" not in plot[key]:
                continue
            grid = plot[key]["grid"]
            angles = np.linspace(0.,360.,len(grid)+1)
            values = np.concatenate((grid,grid[:1]))
            label = LABELS[key]
            if key in ("order5","order6") and not record[key]["direct_grid_qualified"]:
                label += " (diagnostic)"
            for target,width in ((circle_axis,1.5),(inset,.9)):
                target.plot(angles,values,color=COLORS[key],label=label if target is circle_axis else None,
                            linewidth=width,linestyle="--" if key=="order2" else "-")
        angles = np.rad2deg(np.arctan2(plot["inputs"][:,1],plot["inputs"][:,0]))%360
        for target,size in ((circle_axis,23),(inset,9)):
            target.scatter(angles,plot["labels"],s=size,facecolor="white",edgecolor=COLORS["dense"],linewidth=.7,zorder=5,
                           label="Training labels" if target is circle_axis else None)
        inset.set_xlim(0.,90.); inset.set_ylim(-1.6,1.6); inset.set_xticks((0,45,90)); inset.set_yticks((-1,0,1))
        inset.tick_params(labelsize=6.5,length=2); inset.set_title("Training arc (expanded)",fontsize=7,pad=2)
        circle_axis.set_xlim(0.,360.); circle_axis.set_xticks((0,90,180,270,360)); circle_axis.margins(y=.2)
        circle_axis.set_xlabel("Circle angle (degrees)"); circle_axis.set_ylabel("Prediction")
        circle_axis.set_title("Eight inputs · seed "+seed); circle_axis.grid(True,alpha=.14)
        descriptions = []
        for p in (5,6):
            item=record["order"+str(p)]
            descriptions.append("P{}: RMS {:.4g} · {}".format(p,item["spatial"]["circle_rms"],item["direct_grid_verdict"].replace("_"," ")) if "spatial" in item else "P{}: no matched endpoint ({})".format(p,item["status"].replace("_"," ")))
        if not record["order5"]["probe"]["passed"]:
            descriptions.append("P5 training-probe gap {:.3g} > 1e−4".format(record["order5"]["probe"]["peak_training_probe_gap"]))
        elif "spatial" in record["order5"]:
            descriptions.append("P5 Fourier encoding: "+("passed" if record["order5"]["spatial"]["fourier_pass"] else "unresolved"))
        circle_axis.text(.03,.97,"\n".join(descriptions),transform=circle_axis.transAxes,va="top",fontsize=8,
                         bbox=dict(facecolor="white",alpha=.9,edgecolor="none"))
        error_axis,wall_axis = compare_axes[:,index]
        points=[]
        for p in (2,4,5,6):
            key="order"+str(p); item=record[key]
            if "spatial" in item and item["status"]=="fitted":
                error=item["spatial"]["circle_rms"]
                marker="o" if item.get("direct_grid_qualified",False) else "x"
                error_axis.scatter(p,error,color=COLORS[key],marker=marker,s=50,zorder=3,label=LABELS[key])
                points.append((p,error))
                error_axis.annotate("{:.4g}".format(error),(p,error),xytext=(0,8),textcoords="offset points",ha="center",fontsize=8)
            else:
                error_axis.text(p,.05,"No matched\nendpoint",transform=error_axis.get_xaxis_transform(),ha="center",fontsize=8,color=COLORS[key])
        if points:
            error_axis.plot(*np.asarray(points).T,color="#b9b9b9",linewidth=.8,zorder=1)
        error_axis.axhline(.1,color="#5b7959",linewidth=.8,linestyle=":",label="Agreement threshold")
        error_axis.set_yscale("log"); error_axis.set_xticks((2,4,5,6)); error_axis.set_xlim(1.7,6.3)
        error_axis.margins(y=.25); error_axis.set_xlabel("Scalar truncation order"); error_axis.set_ylabel("Circle RMS discrepancy")
        error_axis.set_title("Seed "+seed+" · matched loss"); error_axis.grid(True,alpha=.14)
        keys=("dense","order4","order5","order6")
        values=[record[key]["wall_seconds"] for key in keys]
        bars=wall_axis.bar(np.arange(4),values,color=[COLORS[key] for key in keys])
        wall_axis.bar_label(bars,labels=["{:.1f}".format(value) for value in values],padding=3,fontsize=8)
        wall_axis.set_xticks(np.arange(4),("Dense\nGPU","P4\nCPU","P5\nCPU","P6\nCPU"))
        wall_axis.set_ylim(0.,max(values)*1.16); wall_axis.set_ylabel("Selected run wall seconds")
        wall_axis.set_title("Seed "+seed+" · recorded integration / run")
        wall_axis.grid(True,axis="y",alpha=.14); wall_axis.set_axisbelow(True)
        failure_loss,failure_rate=failure_axes[:,index]
        resolution_colors=("#b7a291",COLORS["order6"],"#8e451d")
        all_rates=[]
        for resolution,(saved,run,rates) in enumerate(zip(plot["order6_resolutions"],record["order6"]["resolution_records"],record["order6"]["resolution_rates"])):
            color=resolution_colors[min(resolution,2)]
            tolerance="rtol={:.0e}".format(run["rtol"])
            failure_loss.plot(saved["times"],saved["losses"],color=color,linewidth=1.5,label="P6 "+tolerance)
            failure_loss.scatter(saved["times"][-1],saved["losses"][-1],color=color,marker="x",s=35)
            boundaries=rates["boundaries"]
            all_rates.extend(point[name] for point in boundaries for name in ("effective_rate","minimum_kernel_eigenvalue"))
            times=[point["time"] for point in boundaries]
            failure_rate.plot(times,[point["effective_rate"] for point in boundaries],color=color,linewidth=1.4,
                              marker=".",markersize=3,label="Effective rate · "+tolerance)
            failure_rate.plot(times,[point["minimum_kernel_eigenvalue"] for point in boundaries],color=color,
                              linestyle="--",linewidth=1.1,label="Minimum eigenvalue · "+tolerance)
        failure_loss.set_yscale("log"); failure_loss.set_title("Seed "+seed+" · order-six loss")
        failure_loss.set_xlabel("Physical training time"); failure_loss.set_ylabel("Mean squared error")
        failure_rate.axhline(0.,color="#777777",linewidth=.6)
        failure_rate.set_yscale("symlog",linthresh=1e-4)
        if all_rates:
            failure_rate.set_ylim(min(-1e-4,3*min(all_rates)),max(1e-4,3*max(all_rates)))
        failure_rate.yaxis.get_major_locator().set_params(numticks=11)
        failure_rate.set_title("Seed "+seed+" · archived segment boundaries")
        failure_rate.set_xlabel("Physical training time"); failure_rate.set_ylabel("Kernel rate / eigenvalue (signed scale)")
        for failure_axis in (failure_loss,failure_rate):
            failure_axis.grid(True,alpha=.14)
    finish_figure(loss_figure,loss_axes,output,"high_order_training_loss","Orders five and six: fitting and numerical stopping",
                  "Eight inputs, width 2048. Physical time differs from runtime; crosses mark endpoints that did not attain the target.")
    finish_figure(circle_figure,circle_axes,output,"high_order_matched_circle_functions","Circle functions at each model’s own fitted endpoint",
                  "Only fitted endpoints are drawn. Diagnostic curves fail a qualification gate; Fourier encoding is scored separately.")
    finish_figure(compare_figure,compare_axes,output,"high_order_error_and_runtime","Higher scalar order: accuracy and computation are separate questions",
                  "Dots require direct-grid validity; crosses are diagnostic. Runtime excludes initialization and can end at fitting or solver failure.")
    finish_figure(failure_figure,failure_axes,output,"high_order_failure_diagnostics","Order six: loss growth and changing kernel along the recorded runs",
                  "For eight inputs, L′/L = −effective rate / 2. Negative rates explain growth; terminal solver failure does not prove divergence.")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for argument,folder in (("training","scalar_high_order_training01"),("campaign","scalar_high_order_primary01"),
        ("probes","scalar_high_order_probes01"),("reproduction-training","scalar_high_order_training_reproduction01"),
        ("reproduction","scalar_high_order_reproduction01"),("reproduction-probes","scalar_high_order_probes_reproduction01"),
        ("output","scalar_high_order_analysis01")):
        parser.add_argument("--"+argument,type=Path,default=DATA/folder)
    parser.add_argument("--overwrite",action="store_true")
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=args.overwrite)
    reader=Reader(); records=[]; plots=[]
    for name in ("SCALAR_HIGH_ORDER_PROTOCOL.md","SCALAR_HIGH_ORDER_ENGINE.md","scalar_high_order_engine.py",
                 "run_scalar_high_order.py","analyze_scalar_wide.py","analyze_scalar_long_time.py"):
        reader.track(HERE/name)
    for seed in SEEDS:
        record,plot=analyze_seed(reader,args,seed); records.append(record); plots.append(plot)
    report=dict(width=2048,samples=8,target=TARGET,configurations=records,research_computation_performed=False,
        measurement_notes=["No new training, coefficient initialization or dense-network evaluation.",
            "Training-probe consistency is independently replayed from original scalar coefficients and archived signatures.",
            "Direct-grid validity and optional Fourier encoding validity are distinct.",
            "Physical fitting time differs from measured compute time. Dense runs and new initialization use GPU; scalar integration uses CPU.",
            "Training initialization through T6 is shared by orders five and six. Passive initialization serves the replayed fitted orders only; count each preparation once.",
            "A numerical or resource cap means no qualified matched endpoint, not a proof of permanent nonfitting or hierarchy divergence.",
            "Improvements at finitely many orders do not establish hierarchy convergence."])
    (args.output/"analysis.json").write_text(json.dumps(report,indent=2,default=scalar)+"\n")
    fields=("seed","width","samples","model","status","loss","time","time_ratio_to_dense","wall_seconds","replay_seconds",
            "circle_rms","relative_rms","maximum_error","direct_grid_verdict","verdict","fourier_pass","refinement_change",
            "training_probe_gap","moving_state_scalars","shared_training_initialization_seconds","shared_probe_initialization_seconds")
    with (args.output/"endpoints.csv").open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader()
        for record in records:
            for model in ("dense","order2","order4","order5","order6"):
                item=record[model]
                row={key:record[key] for key in ("seed","width","samples")}
                row.update(model=model,**{key:item.get(key,"") for key in fields if key in item})
                row.update({key:item.get("spatial",{}).get(key,"") for key in ("circle_rms","relative_rms","maximum_error","fourier_pass")})
                row["refinement_change"]=item.get("refinement",{}).get("numerical_change","")
                row["training_probe_gap"]=item.get("probe",{}).get("peak_training_probe_gap","")
                if model in ("order5","order6"):
                    row["shared_training_initialization_seconds"]=record["initialization"].get("total_seconds","")
                    if item.get("replay_seconds") is not None:
                        row["shared_probe_initialization_seconds"]=(record["probe_initialization"] or {}).get("total_seconds","")
                writer.writerow(row)
    figures(args.output,records,plots)
    shutil.copy2(Path(__file__),args.output/Path(__file__).name)
    manifest=dict(command=sys.argv,source_sha256=digest(Path(__file__)),inputs=reader.hashes,
                  outputs={path.name:digest(path) for path in sorted(args.output.iterdir()) if path.is_file() and path.name!="manifest.json"})
    (args.output/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps({str(record["seed"]):dict(comparisons=record["comparisons"],
        **{key:{field:record[key][field] for field in ("status","loss","time","direct_grid_verdict","verdict")}
           for key in ("order5","order6")}) for record in records},indent=2))


if __name__=="__main__":
    main()
