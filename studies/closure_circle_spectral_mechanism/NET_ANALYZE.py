"""Compare actual finite networks with frozen study-owned closure predictions.

The raw network is always the reference. Templates describe saved outputs;
they never replace a comparator. Outputs must occupy a fresh campaign child.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CLOSURES = ROOT / "data/generated/closure_circle_spectral_mechanism/campaign_001/analysis_final"
ORDERS = (1, 3, 5)
SEEDS = (1729, 2718, 3141)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def rms(value):
    return float(np.sqrt(np.mean(np.asarray(value, dtype=float) ** 2)))


def distance(candidate, reference):
    a, b = np.asarray(candidate, float), np.asarray(reference, float)
    if a.shape != b.shape or not np.all(np.isfinite(a + b)):
        raise ValueError("incompatible or nonfinite comparison arrays")
    ra, rb = rms(a), rms(b)
    if min(ra, rb) <= 1e-15:
        raise ValueError("zero output does not define a normalized shape")
    return dict(rms=rms(a - b), mse=rms(a - b) ** 2,
                max=float(np.max(abs(a - b))), relative_rms=rms(a - b) / rb,
                reference_rms=rb, candidate_rms=ra,
                normalized_shape_rms=rms(a / ra - b / rb))


def template(theta, delta, rotation, amplitude, kappa):
    mid, half = np.deg2rad([rotation, delta / 2])
    return amplitude * np.tanh(kappa * np.sin(theta - mid)) / np.tanh(kappa * np.sin(half))


def fit_template(f, theta, config):
    """Fixed amplitude/midpoint; the only parameter is kappa in [.02,30]."""
    f = np.asarray(f, float)
    train, held = np.arange(0, len(f), 2), np.arange(1, len(f), 2)
    def curve(k):
        return template(theta, config["delta"], config["rotation"], config["amplitude"], k)
    def objective(log_k):
        return float(np.mean((curve(np.exp(log_k))[train] - f[train]) ** 2))
    grid = np.linspace(np.log(.02), np.log(30.), 101)
    values = np.array([objective(x) for x in grid])
    candidates = [(values[0], grid[0]), (values[-1], grid[-1])]
    for j in range(1, len(grid) - 1):
        if values[j] <= values[j-1] and values[j] <= values[j+1]:
            fitted = minimize_scalar(objective, bounds=(grid[j-1], grid[j+1]),
                                     method="bounded", options={"xatol": 1e-10})
            candidates.append((float(fitted.fun), float(fitted.x)))
    _, selected = min(candidates)
    kappa = float(np.exp(selected))
    fitted = curve(kappa)
    result = dict(kappa=kappa, at_boundary=bool(kappa <= .02001 or kappa >= 29.999),
                  whole=distance(fitted, f), fit=distance(fitted[train], f[train]),
                  heldout=distance(fitted[held], f[held]))
    # Reflection preserves both interleaved panels for the declared midpoint.
    coordinate = (2 * np.deg2rad(config["rotation"]) - theta) * len(theta) / (2*np.pi)
    rounded = np.rint(coordinate)
    if np.max(abs(coordinate - rounded)) > 1e-9:
        raise ValueError("reflection is not aligned with the observation panel")
    reflected = f[rounded.astype(int) % len(f)]
    even, odd = (f + reflected) / 2, (f - reflected) / 2
    residual_energy = float(np.mean((f - fitted) ** 2))
    reflection_energy = float(np.mean(even ** 2))
    symmetric_residual_energy = float(np.mean((odd - fitted) ** 2))
    result["reflection"] = dict(even_rms=rms(even), even_relative_rms=rms(even)/rms(f),
        symmetric_residual_relative_rms=rms(odd-fitted)/rms(f),
        residual_energy_fraction=reflection_energy/residual_energy if residual_energy > 1e-28 else 0.,
        decomposition_absolute_error=abs(residual_energy-reflection_energy-symmetric_residual_energy))
    return result, fitted


def spectral(f):
    f = np.asarray(f, float)
    coeff = np.fft.rfft(f) / len(f)
    power = abs(coeff) ** 2
    power[1:] *= 2
    if len(f) % 2 == 0:
        power[-1] /= 2
    mode = np.arange(len(power))
    total = float(power.sum())
    return dict(rms=np.sqrt(total), k_rms=float(np.sqrt((mode**2 @ power) / total)),
                mode1_fraction=float(power[1]/total), tail_ge3=float(power[3:].sum()/total),
                tail_ge5=float(power[5:].sum()/total), even_fraction=float(power[2::2].sum()/total),
                mean_fraction=float(power[0]/total), max_abs=float(np.max(abs(f))))


def paired_gain(low, high):
    low, high = np.asarray(low, float), np.asarray(high, float)
    gain = low - high
    se = float(np.std(gain, ddof=1) / np.sqrt(len(gain))) if len(gain) > 1 else None
    return dict(low_mean_mse=float(low.mean()), high_mean_mse=float(high.mean()),
                per_seed_gain=gain.tolist(), mean_gain=float(gain.mean()), standard_error=se,
                fractional_reduction=float(gain.mean()/low.mean()) if low.mean() > 0 else None,
                all_seeds_improve=bool(np.all(gain > 0)),
                positive_seed_count=int(np.count_nonzero(gain > 0)))


def gain_gate(gain, numerical_effect):
    return bool(gain["standard_error"] is not None
                and gain["fractional_reduction"] is not None
                and gain["fractional_reduction"] >= .1
                and gain["mean_gain"] > 2 * gain["standard_error"]
                and gain["mean_gain"] > 2 * numerical_effect)


def _load_npz(path):
    with np.load(path, allow_pickle=False) as source:
        return {k: source[k] for k in source.files}


def load_closures(deltas):
    summary_path = CLOSURES / "summary.json"
    summary = json.loads(summary_path.read_text())
    records, arrays = {}, {}
    for key, item in summary["records"].items():
        config = item["config"]
        if (config["kind"] != "pair" or config["rotation"] != 45
                or config["amplitude"] != 1 or config["delta"] not in deltas
                or config["order"] not in ORDERS):
            continue
        path = CLOSURES / item["derived_file"]
        if sha(path) != item["derived_sha256"]:
            raise ValueError("closure-derived hash mismatch: " + key)
        arrays[key] = _load_npz(path)
        records[key] = item
    return summary, records, arrays, sha(summary_path)


def closure_id(delta, order, variant="main"):
    return f"pair_d{delta}_r45_N{order}_{variant}"


def load_networks(campaign, manifest):
    records, arrays, failures, missing = {}, {}, {}, []
    for source, expected in manifest["source_hashes"].items():
        archived = campaign / "producer_sources" / Path(source).name
        if sha(archived) != expected:
            raise ValueError("archived producer source hash mismatch: " + source)
    configs = list(manifest["configs"])
    configs += [c for c in manifest.get("conditional_wide", [])
                if ((campaign/c["id"]/"record.json").exists()
                    or (campaign/c["id"]/"failure.json").exists())]
    for config in configs:
        key = config["id"]
        directory = campaign / key
        path = directory / "record.json"
        if not path.exists():
            missing.append(key)
            failure = directory / "failure.json"
            if failure.exists():
                failures[key] = json.loads(failure.read_text())
            continue
        record = json.loads(path.read_text())
        if record["status"] != "complete":
            failures[key] = record
            continue
        if record["config"] != config:
            raise ValueError("network configuration mismatch: " + key)
        if record["source_hashes"] != manifest["source_hashes"]:
            raise ValueError("network producer source identity mismatch: " + key)
        for filename, expected in record["outputs"].items():
            candidate = (directory / filename).resolve()
            if not candidate.is_relative_to(directory.resolve()) or sha(candidate) != expected:
                raise ValueError("network output hash mismatch: " + key + "/" + filename)
        raw = _load_npz(directory / "observations.npz")
        if any(not np.all(np.isfinite(value)) for value in raw.values()):
            raise ValueError("nonfinite network arrays: " + key)
        theta = raw["theta"]
        target = np.arange(1440) * 2*np.pi/1440
        if theta.shape != (1440,) or np.max(abs(theta-target)) > 1e-12:
            raise ValueError("wrong network panel: " + key)
        if raw["dense_predictions"].shape != (1440,) or raw["common_T100"].shape != (1440,):
            raise ValueError("wrong dense predictions shape: " + key)
        loss = np.mean((raw["train_predictions"]-np.asarray(config["labels"]))**2, axis=1)
        if (np.max(abs(loss-raw["loss"])) > 2e-6
                or abs(float(raw["times"][-1])-record["final_time"]) > 1e-8
                or abs(loss[-1]-record["final_loss"]) > 2e-6):
            raise ValueError("network loss/clock mismatch: " + key)
        if np.count_nonzero(np.isclose(raw["times"],100,rtol=0,atol=1e-8)) != 1:
            raise ValueError("missing unique T100 observation: " + key)
        if (config["kind"] != "pair" or config["rotation"] != 45 or config["amplitude"] != 1
                or config["angles_degrees"] != [45-config["delta"]/2,45+config["delta"]/2]
                or config["labels"] != [-1,1]):
            raise ValueError("network data mismatch: " + key)
        valid_failures = []
        if len(loss)>1 and float(np.max(np.diff(loss))) > 1e-6:
            valid_failures.append("saved_loss_increase")
        if record["checks"].get("max_loss_increase", 0.) > 1e-6:
            valid_failures.append("producer_step_loss_increase")
        replay = record["checks"].get("disk_replay")
        if replay is not None and replay > 2e-5:
            valid_failures.append("producer_disk_replay")
        oddness = float(np.max(abs(raw["dense_predictions"]+np.roll(raw["dense_predictions"],720))))
        if oddness > (1e-10 if config["dtype"] == "float64" else 2e-5):
            valid_failures.append("antipodal_oddness")
        dense_spectrum, half_spectrum = spectral(raw["dense_predictions"]), spectral(raw["dense_predictions"][::2])
        grid_difference = abs(dense_spectrum["k_rms"]-half_spectrum["k_rms"])/dense_spectrum["k_rms"]
        if grid_difference > .005:
            valid_failures.append("Fourier_grid")
        fit, fitted = fit_template(raw["dense_predictions"],theta,config)
        item = dict(id=key, config=config, final_time=record["final_time"],
                    final_loss=float(loss[-1]), settled=record["settled"],
                    matched_fit=bool(loss[-1] <= 1e-4), stop_reason=record["stop_reason"],
                    checks=record["checks"], source_hashes=record["source_hashes"],
                    record_sha256=sha(path), outputs=record["outputs"],
                    validity_failures=valid_failures, valid=not valid_failures,
                    antipodal_oddness_max=oddness, grid_k_rms_relative_difference=grid_difference,
                    spectrum=dense_spectrum, template=fit,
                    final_to_T100=distance(raw["dense_predictions"],raw["common_T100"]),
                    hidden={k:raw[k].tolist() for k in raw if k.startswith(("gram", "motion"))})
        raw["template_final"] = fitted
        records[key], arrays[key] = item, raw
    return records, arrays, failures, missing


def run(campaign, out, plots=True):
    start = time.perf_counter()
    campaign, out = Path(campaign).resolve(), Path(out).resolve()
    if not out.is_relative_to(campaign) or out == campaign:
        raise ValueError("analysis output must be a fresh child of the network campaign")
    out.mkdir(exist_ok=False)
    manifest_path = campaign / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    deltas = sorted({c["delta"] for c in manifest["configs"]})
    cs, cr, ca, closure_summary_hash = load_closures(deltas)
    nr, na, failures, missing = load_networks(campaign,manifest)
    derived = {}
    for key, raw in na.items():
        derived[key + "__final"] = raw["dense_predictions"]
        derived[key + "__T100"] = raw["common_T100"]
        derived[key + "__template"] = raw["template_final"]
    closure_descriptions = {}
    for key, item in cr.items():
        derived[key + "__final"] = ca[key]["learned_final"]
        closure_descriptions[key] = dict(config=item["config"], final_time=item["final_time"],
            valid=item["valid"], matched_fit=item["matched_fit"], settled=item["settled"],
            template=item["templates"]["normalized_tanh_sine"], spectrum=item["spectra"]["final"],
            available_controls=item.get("available_controls", []), derived_sha256=item["derived_sha256"])
    controls = []
    for key, item in nr.items():
        cfg = item["config"]
        if cfg["variant"] == "main":
            continue
        main_key = f"pair_d{cfg['delta']}_n{cfg['width']}_s{cfg['seed']}_main"
        if main_key not in nr:
            continue
        control = dict(control=key, main=main_key, delta=cfg["delta"], variant=cfg["variant"],
            final=distance(na[key]["dense_predictions"],na[main_key]["dense_predictions"]),
            common_T100=distance(na[key]["common_T100"],na[main_key]["common_T100"]),
            both_settled=bool(item["settled"] and nr[main_key]["settled"]),
            both_valid=bool(item["valid"] and nr[main_key]["valid"]),
            paired_gain_effects={})
        control["passes_curve_tolerance"] = bool(max(control["final"]["relative_rms"],
            control["common_T100"]["relative_rms"]) <= .002 and control["both_settled"] and control["both_valid"])
        for lo, hi in zip(ORDERS[:-1],ORDERS[1:]):
            candidate_lo, candidate_hi = [ca[closure_id(cfg["delta"],n)]["learned_final"] for n in (lo,hi)]
            gains = []
            for reference in [na[key]["dense_predictions"],na[main_key]["dense_predictions"]]:
                gains.append(float(np.mean((candidate_lo-reference)**2)-np.mean((candidate_hi-reference)**2)))
            control["paired_gain_effects"][f"{lo}_to_{hi}"] = abs(gains[0]-gains[1])
        controls.append(control)
    numerical_effects = {f"{lo}_to_{hi}": max([c["paired_gain_effects"][f"{lo}_to_{hi}"] for c in controls]+[0.])
                         for lo,hi in zip(ORDERS[:-1],ORDERS[1:])}
    required_controls_complete = {c["variant"] for c in controls} >= {"half","precision"}
    numerical_controls_pass = bool(required_controls_complete and all(c["passes_curve_tolerance"] for c in controls))
    groups = {}
    group_keys = sorted({(r["config"]["delta"],r["config"]["width"]) for r in nr.values()
                         if r["config"]["variant"] == "main"})
    for delta, width in group_keys:
        ids = sorted([k for k,r in nr.items() if r["config"]["variant"] == "main"
                      and r["config"]["delta"] == delta and r["config"]["width"] == width],
                     key=lambda k:nr[k]["config"]["seed"])
        seed_values = [nr[k]["config"]["seed"] for k in ids]
        stack = np.stack([na[k]["dense_predictions"] for k in ids])
        mean = stack.mean(axis=0)
        sd = np.std(stack,axis=0,ddof=1) if len(ids)>1 else np.zeros_like(mean)
        f100 = np.stack([na[k]["common_T100"] for k in ids])
        mean100 = f100.mean(axis=0)
        fit, fitted = fit_template(mean,na[ids[0]]["theta"],nr[ids[0]]["config"])
        group_key = f"pair_d{delta}_n{width}"
        derived[group_key+"__mean"] = mean
        derived[group_key+"__sd"] = sd
        derived[group_key+"__template"] = fitted
        group = dict(delta=delta,width=width,ids=ids,seeds=seed_values,seed_count=len(ids),
            complete_seed_panel=seed_values == list(SEEDS),
            all_settled=all(nr[k]["settled"] for k in ids),
            all_matched_fit=all(nr[k]["matched_fit"] for k in ids),
            all_valid=all(nr[k]["valid"] for k in ids),
            final_time_range=[min(nr[k]["final_time"] for k in ids),max(nr[k]["final_time"] for k in ids)],
            ensemble_template=fit, ensemble_spectrum=spectral(mean),
            seed_kappas=[nr[k]["template"]["kappa"] for k in ids],
            seed_heldout_errors=[nr[k]["template"]["heldout"]["relative_rms"] for k in ids],
            template_supported_all_seeds=bool(all(nr[k]["template"]["heldout"]["relative_rms"]<=.05 for k in ids)),
            uncertainty=dict(pointwise_sd_rms=rms(sd),relative_sd_rms=rms(sd)/rms(mean),
                estimated_mean_se_rms=rms(sd)/np.sqrt(len(ids)),
                estimated_relative_mean_se_rms=rms(sd)/np.sqrt(len(ids))/rms(mean),
                seed_scatter_mse=float(np.mean((stack-mean)**2)),
                meaning="Sample SD and estimated mean-SE over available seeds; neither bounds infinite-width bias."),
            comparisons={},hierarchy=[])
        errors = {}
        for order in ORDERS:
            cid = closure_id(delta,order)
            candidate = ca[cid]["learned_final"]
            per_seed = [distance(candidate,reference) for reference in stack]
            errors[order] = np.array([v["mse"] for v in per_seed])
            ensemble_comparison = distance(candidate,mean)
            absolute_identity_error = abs(float(errors[order].mean())-ensemble_comparison["mse"]-group["uncertainty"]["seed_scatter_mse"])
            kclosure = cr[cid]["templates"]["normalized_tanh_sine"]["kappa"]
            group["comparisons"][str(order)] = dict(closure_id=cid,ensemble=ensemble_comparison,
                per_seed=per_seed,mean_seed_mse=float(errors[order].mean()),
                pooled_relative_rms=float(np.sqrt(errors[order].mean()/np.mean(stack**2))),
                mean_seed_relative_rms=float(np.mean([v["relative_rms"] for v in per_seed])),
                relative_rms_range=[min(v["relative_rms"] for v in per_seed),max(v["relative_rms"] for v in per_seed)],
                common_T100_ensemble=distance(ca[cid]["learned_T100"],mean100[::2]),
                common_T100_per_seed=[distance(ca[cid]["learned_T100"],f[::2]) for f in f100],
                bias_variance_identity_absolute_error=absolute_identity_error,
                closure_kappa=kclosure,kappa_difference_to_ensemble=kclosure-fit["kappa"],
                per_seed_kappa_differences=[kclosure-v for v in group["seed_kappas"]])
        for lo,hi in zip(ORDERS[:-1],ORDERS[1:]):
            gain = paired_gain(errors[lo],errors[hi])
            key = f"{lo}_to_{hi}"
            gain.update(low_order=lo,high_order=hi,numerical_control_effect=numerical_effects[key],
                numerical_controls_matched_geometry=delta == 30,
                predeclared_gain_gate_pass=gain_gate(gain,numerical_effects[key]),
                control_effects={})
            effects=[]
            for variant in ["fine","half"]:
                ids_control=[closure_id(delta,n,variant) for n in [lo,hi]]
                if not all(k in ca for k in ids_control):
                    continue
                controlled_errors=[np.mean((ca[k]["learned_final"][None,:]-stack)**2,axis=1) for k in ids_control]
                controlled_gain=paired_gain(*controlled_errors)
                effect_bound=float(abs(controlled_errors[0].mean()-errors[lo].mean())
                                   +abs(controlled_errors[1].mean()-errors[hi].mean()))
                gain["control_effects"][variant]=dict(paired_gain=controlled_gain,
                    absolute_gain_change=abs(controlled_gain["mean_gain"]-gain["mean_gain"]),
                    sum_individual_mse_effects=effect_bound)
                effects.append(effect_bound)
            gain["closure_control_effect_bound"] = max(effects+[0.])
            gain["closure_complete_controls"] = set(gain["control_effects"]) == {"fine","half"}
            gain["above_twice_measured_closure_effect"] = bool(gain["mean_gain"] > 2*gain["closure_control_effect_bound"])
            gain["fully_controlled_improvement"] = bool(gain["predeclared_gain_gate_pass"]
                and numerical_controls_pass and gain["numerical_controls_matched_geometry"]
                and gain["closure_complete_controls"] and gain["above_twice_measured_closure_effect"]
                and group["all_settled"] and group["all_matched_fit"] and group["all_valid"]
                and group["complete_seed_panel"])
            gain["classification"] = ("controlled_empirical_improvement" if gain["fully_controlled_improvement"]
                else "gain_gate_pass_with_control_qualifications" if gain["predeclared_gain_gate_pass"]
                else "inconclusive_or_no_improvement")
            group["hierarchy"].append(gain)
        groups[group_key]=group
    width_comparisons=[]
    for delta in deltas:
        widths=sorted([w for d,w in group_keys if d==delta])
        for low,high in zip(widths[:-1],widths[1:]):
            g0,g1=groups[f"pair_d{delta}_n{low}"],groups[f"pair_d{delta}_n{high}"]
            key0,key1=f"pair_d{delta}_n{low}",f"pair_d{delta}_n{high}"
            ordering=[np.sign(x["mean_gain"])!=np.sign(y["mean_gain"]) for x,y in zip(g0["hierarchy"],g1["hierarchy"])]
            width_comparisons.append(dict(delta=delta,low_width=low,high_width=high,
                ensemble=distance(derived[key0+"__mean"],derived[key1+"__mean"]),
                complete_seed_panels=g0["complete_seed_panel"] and g1["complete_seed_panel"],
                hierarchy_ordering_reversed=[bool(v) for v in ordering],width_sensitive=bool(any(ordering)),
                kappa_ensemble_shift=g1["ensemble_template"]["kappa"]-g0["ensemble_template"]["kappa"]))
    branch_width=next((v for v in width_comparisons if v["delta"]==30 and v["low_width"]==1024 and v["high_width"]==4096),None)
    branch_group=groups.get("pair_d30_n4096")
    branch_ready=bool(branch_width and branch_group and branch_width["complete_seed_panels"] and required_controls_complete)
    branch=dict(ready=branch_ready, based_only_on_widths=[1024,4096],
        relative_width_shift=branch_width["ensemble"]["relative_rms"] if branch_width else None,
        width_shift_over_001=bool(branch_width and branch_width["ensemble"]["relative_rms"]>.01),
        unresolved_transitions=[f"{t['low_order']}_to_{t['high_order']}" for t in branch_group["hierarchy"]
                               if not t["predeclared_gain_gate_pass"]] if branch_group else None)
    widest={str(delta):groups[f"pair_d{delta}_n{max(w for d,w in group_keys if d==delta)}"] for delta in deltas
            if any(d==delta for d,w in group_keys)}
    summary=dict(network_records=nr,network_groups=groups,network_controls=controls,
        closure_records=closure_descriptions,closure_controls=[c for c in cs["controls"] if c["left"] in cr],
        width_comparisons=width_comparisons,prebranch=branch,
        widen_recommended=bool(branch_ready and (branch["width_shift_over_001"] or branch["unresolved_transitions"])),
        numerical_controls_complete=required_controls_complete,numerical_controls_pass=numerical_controls_pass,
        widest_widths={d:g["width"] for d,g in widest.items()},
        template_supported_at_all_widest_seeds=bool(len(widest)==len(deltas) and all(g["complete_seed_panel"]
            and g["all_valid"] and g["all_settled"] and g["all_matched_fit"] and g["template_supported_all_seeds"] for g in widest.values())),
        failures=failures,missing=missing,completed_records=len(nr),
        normalization="Relative RMS divides by the unmodified network reference RMS. Shape RMS normalizes each curve separately; no gain/phase/clock fitted.",
        clocks="Final compares each mildly settled saved endpoint; common_T100 compares at physical T100 on the aligned720-point panel.",
        finite_width_scope="Seed SD/SE and differences of width means are empirical diagnostics, not infinite-width confidence bounds. Cross-width same-number seeds are not asserted to be paired realizations.",
        provenance=dict(campaign=str(campaign),manifest_sha256=sha(manifest_path),
            closure_summary=str(CLOSURES/"summary.json"),closure_summary_sha256=closure_summary_hash,
            source_sha256={str(path):sha(path) for path in [HERE/"NET_ANALYZE.py",HERE/"NET_PLAN.md",HERE/"ANALYZE.py"]}),
        environment=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),
            threads={k:os.environ.get(k) for k in ["OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"]}),
        command=[sys.executable,*sys.argv])
    branch_path=campaign/"wide_decision.json"
    if branch_path.exists():
        summary["actual_wide_branch_decision"]=json.loads(branch_path.read_text())
        summary["provenance"]["wide_decision_sha256"]=sha(branch_path)
    np.savez_compressed(out/"curves.npz",**derived)
    summary["curves_sha256"]=sha(out/"curves.npz")
    if plots and groups:
        make_plots(summary,derived,out)
    summary["elapsed_seconds"]=time.perf_counter()-start
    with (out/"summary.json").open("x") as stream:
        json.dump(summary,stream,indent=2,allow_nan=False)
    print(json.dumps(dict(output=str(out),completed=len(nr),missing=len(missing),
        widen_recommended=summary["widen_recommended"],elapsed_seconds=summary["elapsed_seconds"])),flush=True)
    return summary


def make_plots(summary,arrays,out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
    colors={1:"#377eb8",3:"#e68613",5:"#984ea3"}
    theta=np.arange(1440)*2*np.pi/1440
    angle=(np.rad2deg(theta)-45+180)%360-180
    sort=np.argsort(angle)
    groups=summary["network_groups"]
    deltas=sorted(map(int,summary["widest_widths"]))
    with PdfPages(out/"network_comparison_report.pdf") as pdf:
        fig,axes=plt.subplots(len(deltas),2,figsize=(13,3.2*len(deltas)),squeeze=False)
        for row,delta in enumerate(deltas):
            width=summary["widest_widths"][str(delta)]
            key=f"pair_d{delta}_n{width}"
            mean,sd=arrays[key+"__mean"],arrays[key+"__sd"]
            ax,er=axes[row]
            ax.fill_between(angle[sort],(mean-sd)[sort],(mean+sd)[sort],color=".8",label="Network seed ±1 SD")
            ax.plot(angle[sort],mean[sort],color="k",lw=2,label=f"Network mean, n={width}")
            for n in ORDERS:
                f=arrays[closure_id(delta,n)+"__final"]
                ax.plot(angle[sort],f[sort],color=colors[n],ls={1:"--",3:"-.",5:":"}[n],lw=1.7,label=f"Closure N={n}")
                er.plot(angle[sort],(f-mean)[sort],color=colors[n],label=f"N={n}")
            er.fill_between(angle[sort],-sd[sort],sd[sort],color=".85",label="Network seed SD")
            er.axhline(0,color="k",lw=.6)
            ax.scatter([-delta/2,delta/2],[-1,1],marker="x",color="k",zorder=5)
            ax.set_title(f"Separation {delta}°: unmodified outputs")
            er.set_title("Closure minus network mean")
            ax.set_ylabel("Prediction")
            for a in [ax,er]:
                a.set_xlabel("Angle relative to pair midpoint (degrees)")
                a.set_xlim(-180,180)
                a.grid(alpha=.2)
            if row==0:
                ax.legend(fontsize=8,ncol=2)
                er.legend(fontsize=8,ncol=2)
        fig.suptitle("Actual dense networks and closure predictions",fontsize=15)
        fig.tight_layout(rect=[0,0,1,.96]); fig.savefig(out/"network_closure_curves.png",dpi=160)
        pdf.savefig(fig);plt.close(fig)

        fig,axes=plt.subplots(1,len(deltas),figsize=(13,4.8),subplot_kw={"projection":"polar"},squeeze=False)
        for ax,delta in zip(axes[0],deltas):
            width=summary["widest_widths"][str(delta)];key=f"pair_d{delta}_n{width}"
            curves=[arrays[key+"__mean"]]+[arrays[closure_id(delta,n)+"__final"] for n in ORDERS]
            scale=max(np.max(abs(v)) for v in curves)*1.1
            for f,color,label,style in [(curves[0],"k",f"Network n={width}","-")]+[
                (curves[j+1],colors[n],f"N={n}",{1:"--",3:"-.",5:":"}[n]) for j,n in enumerate(ORDERS)]:
                # Radius encodes signed prediction around the explicitly labelled zero ring.
                ax.plot(theta,scale+f,color=color,label=label,ls=style,lw=1.8)
            ax.plot(theta,np.full(1440,scale),color=".6",lw=.6)
            data_angles=np.deg2rad([45-delta/2,45+delta/2])
            ax.scatter(data_angles,[scale,scale],facecolors="none",edgecolors="k",s=35,
                       zorder=5,label="Training directions")
            ax.scatter(data_angles,scale+np.array([-1,1]),color="k",s=20,zorder=5,
                       label="Targets −1, +1")
            ticks=np.array([-1.,0.,1.]);ax.set_rticks(scale+ticks,labels=["−1","0","+1"])
            ax.set_ylim(0,2*scale);ax.set_title(f"δ={delta}°",pad=20)
        axes[0,0].legend(loc="lower left",bbox_to_anchor=(-.2,-.23),fontsize=8)
        fig.suptitle("Circle view: signed prediction is radial displacement from the zero ring",fontsize=12)
        fig.tight_layout(rect=[0,.05,1,.93]);fig.savefig(out/"network_closure_radial.png",dpi=160)
        pdf.savefig(fig);plt.close(fig)

        fig,axes=plt.subplots(2,len(deltas),figsize=(13,7.5),squeeze=False)
        for j,delta in enumerate(deltas):
            width=summary["widest_widths"][str(delta)];key=f"pair_d{delta}_n{width}";g=groups[key]
            ax=axes[0,j]
            ax.plot(angle[sort],arrays[key+"__mean"][sort],color="k",label="Network mean")
            ax.plot(angle[sort],arrays[key+"__template"][sort],color="#009e73",ls="--",label="Tanh–sine fit")
            ax.set_title(f"δ={delta}°, κ={g['ensemble_template']['kappa']:.3f}\nHeldout RMS {100*g['ensemble_template']['heldout']['relative_rms']:.2f}%")
            ax.set_xlabel("Angle relative to midpoint (degrees)");ax.set_ylabel("Prediction")
            ax.grid(alpha=.2)
            if j==0:ax.legend(fontsize=8)
            ax=axes[1,j]
            widths=sorted({gg["width"] for gg in groups.values() if gg["delta"]==delta})
            labels=[]
            for position,w in enumerate(widths):
                gg=groups[f"pair_d{delta}_n{w}"]
                ax.scatter(np.full(gg["seed_count"],position)+np.linspace(-.08,.08,gg["seed_count"]),gg["seed_kappas"],color=".45",s=25)
                ax.scatter(position,gg["ensemble_template"]["kappa"],color="k",marker="D",s=35)
                labels.append(f"n={w}")
            for q,n in enumerate(ORDERS):
                ax.scatter(len(widths)+q,summary["closure_records"][closure_id(delta,n)]["template"]["kappa"],color=colors[n],s=40)
                labels.append(f"N={n}")
            ax.set_xticks(range(len(labels)),labels,rotation=25);ax.set_ylabel("Fitted κ")
            ax.set_title("Individual seeds • and fitted mean ◆")
            ax.grid(axis="y",alpha=.2)
        fig.suptitle("One-parameter reconstruction: κ is separate from closure order",fontsize=14)
        fig.tight_layout(rect=[0,0,1,.94]);fig.savefig(out/"network_template_fits.png",dpi=160)
        pdf.savefig(fig);plt.close(fig)

        fig,axes=plt.subplots(2,len(deltas),figsize=(13,7.5),squeeze=False)
        width_colors={1024:"#999999",4096:"#111111",8192:"#009e73"}
        for j,delta in enumerate(deltas):
            widths=sorted({gg["width"] for gg in groups.values() if gg["delta"]==delta})
            for wi,w in enumerate(widths):
                gg=groups[f"pair_d{delta}_n{w}"]
                offset=(wi-(len(widths)-1)/2)*.12
                x=np.arange(3)+offset
                for row,metric in [(0,"relative_rms"),(1,"normalized_shape_rms")]:
                    ax=axes[row,j]
                    ys=[100*gg["comparisons"][str(n)]["ensemble"][metric] for n in ORDERS]
                    ax.plot(x,ys,color=width_colors.get(w,"#444444"),marker="D",label=f"Network n={w}")
                    for index,n in enumerate(ORDERS):
                        points=[100*v[metric] for v in gg["comparisons"][str(n)]["per_seed"]]
                        ax.scatter(x[index]+np.linspace(-.04,.04,len(points)),points,color=width_colors.get(w,"#444444"),s=18,alpha=.6)
                    ax.set_xticks(range(3),["N=1","N=3","N=5"]);ax.grid(axis="y",alpha=.2)
                    ax.set_title(f"δ={delta}°");ax.set_ylabel("Relative RMS (%)" if row==0 else "Unit-RMS shape distance (%)")
            if j==0:axes[0,j].legend(fontsize=8)
        fig.suptitle("Full-function error: ensemble means ◆ and individual seeds •",fontsize=14)
        fig.tight_layout(rect=[0,0,1,.94]);fig.savefig(out/"closure_network_errors.png",dpi=160)
        pdf.savefig(fig);plt.close(fig)


def selftest():
    theta=np.arange(1440)*2*np.pi/1440
    config=dict(delta=30,rotation=45,amplitude=1)
    checks=[]
    for k in [.02,.3,2.,6.,30.]:
        f=template(theta,30,45,1,k)
        result,_=fit_template(f,theta,config)
        error=abs(result["kappa"]-k)/k
        assert error<1e-5,(k,error)
        assert result["heldout"]["relative_rms"]<1e-6
        checks.append(dict(name=f"exact_template_kappa_{k}",relative_kappa_error=error))
    f=template(theta,30,45,1,4.)+.1*np.cos(theta-np.pi/4)
    result,_=fit_template(f,theta,config)
    assert abs(result["kappa"]-4)<1e-6
    assert result["reflection"]["decomposition_absolute_error"]<1e-14
    checks.append(dict(name="reflection_even_residual_is_orthogonal",decomposition_error=result["reflection"]["decomposition_absolute_error"]))
    f=np.sin(theta)
    metric=distance(2*f,f)
    assert abs(metric["relative_rms"]-1)<1e-14 and metric["normalized_shape_rms"]<1e-14
    checks.append(dict(name="raw_gain_and_shape_are_distinct"))
    stack=np.stack([f+.1*np.cos(theta),f-.2*np.cos(theta),f+.3*np.cos(theta)])
    candidate=.9*f
    lhs=float(np.mean((candidate-stack)**2))
    rhs=float(np.mean((candidate-stack.mean(0))**2)+np.mean((stack-stack.mean(0))**2))
    assert abs(lhs-rhs)<1e-14
    checks.append(dict(name="ensemble_error_decomposition",absolute_error=abs(lhs-rhs)))
    gain=paired_gain([1,1.1,.9],[.5,.6,.4])
    assert gain_gate(gain,.1) and not gain_gate(gain,.3)
    assert not gain_gate(paired_gain([1,1,1],[.95,.95,.95]),0)
    checks.append(dict(name="paired_gain_thresholds_and_control_floor"))
    assert abs(spectral(np.sin(3*theta))["k_rms"]-3)<1e-14
    checks.append(dict(name="single_harmonic_spectral_oracle"))
    return dict(status="pass",checks=checks,source_sha256=sha(__file__))


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign");parser.add_argument("--output")
    parser.add_argument("--no-plots",action="store_true")
    parser.add_argument("--selftest",action="store_true")
    args=parser.parse_args()
    if args.selftest:
        result=selftest()
        if args.output:
            path=Path(args.output)
            with path.open("x") as stream:json.dump(result,stream,indent=2,allow_nan=False)
        print(json.dumps(result,indent=2))
    else:
        if not args.campaign or not args.output:parser.error("--campaign and --output are required")
        run(args.campaign,args.output,plots=not args.no_plots)
