"""Unfitted six-case closure/network comparison; no scientific training.

Primary: common physical T100, exact aligned 720-angle panel.
Secondary: network T120 versus each closure's saved T100--120 endpoint.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CLOSURES = ROOT / "data/generated/closure_circle_spectral_mechanism/campaign_001"
CASES = ("triple_d20", "triple_d40", "triple_d60", "quad_d15", "quad_d30", "quad_d45")
ORDERS, SEEDS, WIDTHS = (1, 3, 5), (1729, 2718, 3141), (1024, 4096)
CLOCKS = ("common_T100", "final")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def load(path):
    with np.load(path, allow_pickle=False) as source:
        return {k: source[k] for k in source.files}


def require(value, message):
    if not value:
        raise AssertionError(message)


def rms(x):
    return float(np.sqrt(np.mean(np.asarray(x, float) ** 2)))


def distance(candidate, reference):
    a, b = np.asarray(candidate, float), np.asarray(reference, float)
    require(a.shape == b.shape and np.all(np.isfinite(a + b)), "invalid comparison arrays")
    ra, rb = rms(a), rms(b)
    require(min(ra, rb) > 1e-15, "zero RMS cannot define shape")
    return dict(rms=rms(a-b), mse=float(np.mean((a-b)**2)), max=float(np.max(abs(a-b))),
                relative_rms=rms(a-b)/rb, reference_rms=rb, candidate_rms=ra,
                normalized_shape_rms=rms(a/ra-b/rb))


def spectral(f):
    f = np.asarray(f, float)
    p = abs(np.fft.rfft(f)/len(f))**2
    p[1:] *= 2
    if len(f) % 2 == 0:
        p[-1] /= 2
    k = np.arange(len(p))
    return dict(rms=float(np.sqrt(p.sum())), k_rms=float(np.sqrt(k*k@p/p.sum())),
                tail_ge3=float(p[3:].sum()/p.sum()), even_fraction=float(p[2::2].sum()/p.sum()))


def paired_gain(low, high):
    low, high = np.asarray(low, float), np.asarray(high, float)
    g = low-high
    return dict(low_mean_mse=float(low.mean()), high_mean_mse=float(high.mean()),
                per_seed_gain=g.tolist(), mean_gain=float(g.mean()),
                standard_error=float(np.std(g, ddof=1)/np.sqrt(len(g))) if len(g)>1 else None,
                fractional_reduction=float(g.mean()/low.mean()) if low.mean()>0 else None,
                all_seeds_improve=bool(np.all(g>0)))


def gain_gate(g, effect):
    return bool(g["standard_error"] is not None and g["fractional_reduction"] is not None
                and g["fractional_reduction"] >= .1 and g["mean_gain"] > 2*g["standard_error"]
                and effect is not None and g["mean_gain"] > 2*effect)


def closure_id(case, order, variant="main"):
    return f"{case}_N{order}_{variant}"


def network_id(case, width, seed, variant="main"):
    return f"{case}_n{width}_s{seed}_{variant}"


def closures():
    summary = read(CLOSURES/"analysis_final/summary.json")
    records, curves = {}, {}
    for name, item in summary["records"].items():
        cfg = item["config"]
        if cfg["name"] not in CASES or cfg["order"] not in ORDERS:
            continue
        derived_path = CLOSURES/"analysis_final"/item["derived_file"]
        require(sha(derived_path) == item["derived_sha256"], name+": closure derived hash")
        directory = CLOSURES/name
        record_path = directory/"record.json"
        raw_record = read(record_path)
        require(sha(record_path) == summary["input_hashes"][name]["record"], name+": raw record hash")
        require(raw_record["config"] == cfg, name+": closure config")
        for filename in ("observations.npz", "config.json"):
            require(sha(directory/filename) == raw_record["outputs"][filename]
                    == summary["input_hashes"][name][filename], name+": raw input hash")
        derived, raw = load(derived_path), load(directory/"observations.npz")
        require(np.array_equal(derived["learned_final"], raw["dense_predictions"]), name+": final raw/derived")
        index = np.flatnonzero(np.isclose(raw["times"], 100, atol=1e-10, rtol=0))
        require(len(index) == 1 and np.array_equal(derived["learned_T100"], raw["predictions"][index[0]]),
                name+": T100 raw/derived")
        require(derived["learned_T100"].shape == (720,) and derived["learned_final"].shape == (1440,),
                name+": closure panel shapes")
        require(np.array_equal(derived["angles1440"], 2*np.pi*np.arange(1440)/1440), name+": closure grid")
        curves[name] = dict(common_T100=derived["learned_T100"], final=raw["dense_predictions"])
        records[name] = {k:item[k] for k in ("config", "final_time", "final_loss", "settled", "matched_fit",
                                          "valid", "validity_failures", "derived_sha256")}
        records[name]["available_controls"] = item.get("available_controls", [])
        records[name].update(record_sha256=sha(record_path), observations_sha256=sha(directory/"observations.npz"),
                             relative_T100_loss=item["relative_T100_loss"])
    return records, curves, [c for c in summary["controls"] if c["left"] in records]


def networks(campaign, manifest):
    records, curves = {}, {}
    for cfg in manifest["configs"]:
        name, directory = cfg["id"], campaign/cfg["id"]
        record, raw = read(directory/"record.json"), load(directory/"observations.npz")
        require(record["status"] == "complete" and record["config"] == cfg == read(directory/"config.json"),
                name+": network identity")
        require(record["source_hashes"] == manifest["source_hashes"], name+": producer identity")
        # Full weight/hash validation is independently performed by MULTI_NET_VERIFY.
        for filename in ("config.json", "observations.npz"):
            require(sha(directory/filename) == record["outputs"][filename], name+": input hash")
        require(all(np.all(np.isfinite(v)) for v in raw.values()), name+": nonfinite observations")
        require(np.array_equal(raw["theta"], 2*np.pi*np.arange(1440)/1440), name+": circle panel")
        require(raw["dense_predictions"].shape == raw["common_T100"].shape == (1440,), name+": shape")
        require(np.array_equal(raw["times"], np.arange(13)*10.), name+": fixed T120 clock")
        loss = np.mean((raw["train_predictions"]-np.asarray(cfg["labels"]))**2, axis=1)
        require(np.max(abs(loss-raw["loss"])) < 1e-13, name+": loss")
        tolerance = 1e-10 if cfg["dtype"] == "float64" else 2e-5
        oddness = max(float(np.max(abs(raw[k][:720]+raw[k][720:]))) for k in ("dense_predictions", "common_T100"))
        grid = {clock:abs(spectral(raw[k])["k_rms"]/spectral(raw[k][::2])["k_rms"]-1)
                for clock,k in (("final", "dense_predictions"),("common_T100", "common_T100"))}
        valid = bool(np.max(np.diff(loss)) <= 1e-6 and oddness <= tolerance and max(grid.values()) <= .005)
        records[name] = dict(config=cfg, record_sha256=sha(directory/"record.json"), outputs=record["outputs"],
            final_time=record["final_time"], final_loss=float(loss[-1]), T100_loss=float(loss[10]),
            settled=record["settled"], stop_reason=record["stop_reason"], valid=valid,
            matched_fit=bool(loss[-1] <= 1e-4), common_T100_matched_fit=bool(loss[10] <= 1e-4),
            antipodal_oddness_max=oddness, grid_k_rms_relative_difference=grid,
            final_to_T100=distance(raw["dense_predictions"], raw["common_T100"]),
            hidden={k:raw[k].tolist() for k in raw if k.startswith(("gram", "motion"))})
        curves[name] = dict(common_T100=raw["common_T100"][::2], final=raw["dense_predictions"],
                            common_T100_dense=raw["common_T100"])
    return records, curves


def run(campaign, output):
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    begun_cpu, begun = time.process_time(), time.monotonic()
    require(output.is_relative_to(campaign) and output != campaign, "output must be a fresh campaign child")
    output.mkdir(exist_ok=False)
    manifest = read(campaign/"manifest.json")
    cr, ca, cc = closures()
    nr, na = networks(campaign, manifest)
    require(len(nr) == 48, "all 48 networks required")
    derived = {}
    for name,a in na.items():
        derived[name+"__final"], derived[name+"__T100"] = a["final"], a["common_T100_dense"]
    for name,a in ca.items():
        derived[name+"__final"], derived[name+"__T100"] = a["final"], a["common_T100"]
    controls = []
    for name,r in nr.items():
        cfg = r["config"]
        if cfg["variant"] == "main":
            continue
        case = cfg["name"]
        main = network_id(case, cfg["width"], cfg["seed"])
        control = dict(case=case, control=name, main=main, variant=cfg["variant"],
                       width=cfg["width"], both_valid=r["valid"] and nr[main]["valid"],
                       both_settled=r["settled"] and nr[main]["settled"], clocks={})
        for clock in CLOCKS:
            d = distance(na[name][clock], na[main][clock])
            effects = {}
            for lo,hi in zip(ORDERS[:-1],ORDERS[1:]):
                g = []
                for key in (name, main):
                    g.append(float(np.mean((ca[closure_id(case,lo)][clock]-na[key][clock])**2)
                                   - np.mean((ca[closure_id(case,hi)][clock]-na[key][clock])**2)))
                effects[f"{lo}_to_{hi}"] = abs(g[0]-g[1])
            control["clocks"][clock] = dict(distance=d, paired_gain_effects=effects,
                passes_curve_tolerance=bool(d["relative_rms"] <= .002 and control["both_valid"]))
        controls.append(control)
    groups = {}
    for case in CASES:
        local_controls = [v for v in controls if v["case"] == case]
        for width in WIDTHS:
            ids = [network_id(case,width,s) for s in SEEDS]
            group = dict(case=case, width=width, ids=ids, seeds=list(SEEDS), seed_count=3,
                         all_valid=all(nr[k]["valid"] for k in ids),
                         all_settled=all(nr[k]["settled"] for k in ids), clocks={})
            for clock in CLOCKS:
                stack = np.stack([na[k][clock] for k in ids])
                mean, sd = stack.mean(0), stack.std(0,ddof=1)
                stem = f"{case}_n{width}__{clock}"
                derived[stem+"_mean"], derived[stem+"_sd"] = mean, sd
                scatter = float(np.mean((stack-mean)**2))
                panel = dict(panel_size=len(mean), network_time=100 if clock=="common_T100" else 120,
                    mean_reference_rms=rms(mean), mean_seed_reference_rms=float(np.mean([rms(f) for f in stack])),
                    seed_sd_rms=rms(sd), relative_seed_sd_rms=rms(sd)/rms(mean),
                    estimated_mean_se_rms=rms(sd)/np.sqrt(3), seed_scatter_mse=scatter,
                    matched_fit=all(nr[k]["common_T100_matched_fit" if clock=="common_T100" else "matched_fit"] for k in ids),
                    comparisons={}, hierarchy=[])
                errors = {}
                for n in ORDERS:
                    cid = closure_id(case,n)
                    seed_metrics = [dict(seed=s,**distance(ca[cid][clock],f)) for s,f in zip(SEEDS,stack)]
                    errors[n] = np.array([m["mse"] for m in seed_metrics])
                    ensemble = distance(ca[cid][clock],mean)
                    controls_for_order = [c for c in cc if c["right"] == cid]
                    valid_key = "common_T100_valid" if clock == "common_T100" else "settled_endpoint_valid"
                    panel["comparisons"][str(n)] = dict(closure_id=cid, ensemble=ensemble, per_seed=seed_metrics,
                        mean_seed_mse=float(errors[n].mean()), pooled_relative_rms=float(np.sqrt(errors[n].mean()/np.mean(stack**2))),
                        mean_seed_relative_rms=float(np.mean([m["relative_rms"] for m in seed_metrics])),
                        closure_time=100 if clock=="common_T100" else cr[cid]["final_time"],
                        closure_numerical_controls_complete={c["control"] for c in controls_for_order} == {"half","fine"},
                        closure_numerical_controls_pass=bool(len(controls_for_order)==2 and all(c[valid_key] for c in controls_for_order)),
                        bias_variance_identity_absolute_error=abs(errors[n].mean()-ensemble["mse"]-scatter))
                for lo,hi in zip(ORDERS[:-1],ORDERS[1:]):
                    key = f"{lo}_to_{hi}"
                    gain = paired_gain(errors[lo],errors[hi])
                    net_effect = max([c["clocks"][clock]["paired_gain_effects"][key] for c in local_controls], default=None)
                    net_pass = bool({c["variant"] for c in local_controls} == {"half","precision"}
                                    and all(c["clocks"][clock]["passes_curve_tolerance"] for c in local_controls))
                    closure_effects = {}
                    for variant in ("fine", "half"):
                        pair = [closure_id(case,n,variant) for n in (lo,hi)]
                        if not all(k in ca for k in pair):
                            continue
                        changed = [np.mean((ca[k][clock][None,:]-stack)**2,axis=1) for k in pair]
                        changed_gain = paired_gain(*changed)
                        closure_effects[variant] = dict(paired_gain=changed_gain,
                            absolute_gain_change=abs(changed_gain["mean_gain"]-gain["mean_gain"]),
                            sum_individual_mse_effects=float(abs(changed[0].mean()-errors[lo].mean())
                                                           +abs(changed[1].mean()-errors[hi].mean())))
                    closure_effect = max([v["sum_individual_mse_effects"] for v in closure_effects.values()], default=None)
                    closure_pass = all(panel["comparisons"][str(n)]["closure_numerical_controls_pass"] for n in (lo,hi))
                    raw_gate = gain_gate(gain, net_effect)
                    fully = bool(raw_gate and net_pass and closure_pass and closure_effect is not None
                                 and gain["mean_gain"] > 2*closure_effect and group["all_valid"]
                                 and all(cr[closure_id(case,n)]["valid"] for n in (lo,hi)))
                    if clock == "final":
                        fully = fully and group["all_settled"] and panel["matched_fit"]
                    gain.update(low_order=lo, high_order=hi, numerical_control_effect=net_effect,
                        numerical_controls_pass=net_pass,
                        numerical_control_widths={c["variant"]:c["width"] for c in local_controls},
                        controls_at_both_widths=False, raw_gain_gate_pass=raw_gate,
                        closure_control_effect_bound=closure_effect, closure_control_effects=closure_effects,
                        closure_controls_pass=closure_pass, fully_controlled_improvement=fully,
                        measured_direction="improvement" if gain["mean_gain"]>0 else "deterioration" if gain["mean_gain"]<0 else "tie",
                        classification="controlled_empirical_improvement" if fully else
                            "gain_with_control_qualifications" if raw_gate else
                            "measured_deterioration_with_uncertainty_qualifications" if gain["mean_gain"]<0 else
                            "inconclusive_small_improvement_or_tie")
                    panel["hierarchy"].append(gain)
                panel["smallest_measured_error_order"] = min(ORDERS,key=lambda n:panel["comparisons"][str(n)]["ensemble"]["relative_rms"])
                group["clocks"][clock] = panel
            groups[f"{case}_n{width}"] = group
    widths = []
    for case in CASES:
        row = dict(case=case, low_width=1024, high_width=4096, clocks={})
        for clock in CLOCKS:
            low,high = [groups[f"{case}_n{w}"]["clocks"][clock] for w in WIDTHS]
            reversals = [bool(np.sign(a["mean_gain"]) != np.sign(b["mean_gain"]))
                         for a,b in zip(low["hierarchy"], high["hierarchy"])]
            row["clocks"][clock] = dict(ensemble=distance(derived[f"{case}_n1024__{clock}_mean"],derived[f"{case}_n4096__{clock}_mean"]),
                hierarchy_ordering_reversed=reversals, width_sensitive=any(reversals))
        widths.append(row)
    np.savez_compressed(output/"curves.npz", **derived)
    result = dict(schema_version=1, network_records=nr, network_groups=groups, network_controls=controls,
        closure_records=cr, closure_controls=cc, width_comparisons=widths, completed_records=len(nr),
        primary_clock="common_T100", secondary_clock="final", cases=list(CASES),
        normalization="Relative RMS divides by the actual network reference RMS; ensemble uses the three-seed mean. No fitted clock, gain, phase or teacher labels.",
        clocks="Primary common_T100 uses closure/network T100 on the exact 720-point subset. Secondary final compares network T120 with each closure's saved mildly settled T100--120 endpoint; these are different clocks when the closure stopped at T100.",
        limitations=["Three seeds and two widths do not bound infinite-width bias or prove closure-order convergence.",
            "Network step controls use width4096 and precision controls width1024; their effects are applied within the same geometry, but both axes are not tested at both widths.",
            "Existing closure quadrature controls occur only at triple_d40 and quad_d30. Triple_d40 N1 and N5 fail their 2% tolerance; no fresh high-precision closure campaign was requested.",
            "Settling is a finite diagnostic. Any unmet gate remains unsettled at fixed T120.",
            "Off-training angles have no teacher labels; measured accuracy means agreement with actual finite networks."],
        provenance=dict(manifest_sha256=sha(campaign/"manifest.json"),
            closure_summary_sha256=sha(CLOSURES/"analysis_final/summary.json"),
            analyzer_sha256=sha(__file__), curves_sha256=sha(output/"curves.npz")),
        cpu_seconds=time.process_time()-begun_cpu, wall_seconds=time.monotonic()-begun,
        environment=dict(numpy=np.__version__, threads={k:os.environ[k] for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")}),
        command=[sys.executable,*sys.argv])
    (output/"summary.json").write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    (output/"comparison.md").write_text(report(result))
    print(json.dumps(dict(completed=len(nr),cpu_seconds=result["cpu_seconds"],wall_seconds=result["wall_seconds"])))
    return result


def report(s):
    lines = ["# Actual networks for the six three-/four-point circle cases", "",
        "Primary errors below compare each unfitted closure at physical T100 against the mean of three actual width4096 networks at T100. Relative RMS is normalized by that network mean's RMS. Lower is closer; off-training angles have no teacher labels.", "",
        "| Case | N1 error | N3 error | N5 error | Smallest measured error | 1024→4096 mean drift | Settled at T120 |",
        "|---|---:|---:|---:|---|---:|---:|"]
    for case in CASES:
        g = s["network_groups"][f"{case}_n4096"]; p = g["clocks"]["common_T100"]
        w = next(x for x in s["width_comparisons"] if x["case"]==case)["clocks"]["common_T100"]
        values = [100*p["comparisons"][str(n)]["ensemble"]["relative_rms"] for n in ORDERS]
        count = sum(s["network_records"][k]["settled"] for k in g["ids"])
        lines.append(f"| {case} | {values[0]:.2f}% | {values[1]:.2f}% | {values[2]:.2f}% | N{p['smallest_measured_error_order']} | {100*w['ensemble']['relative_rms']:.2f}% | {count}/3 |")
    lines += ["", "The smallest measured error is descriptive. A hierarchy claim requires each paired squared-error gain to be at least10%, exceed twice its seed standard error and twice the measured network and closure numerical effects, and pass the numerical controls. A missing control is unknown, not zero error.", "",
        "| Case (width4096, T100) | N1→N3 squared-error change | N3→N5 squared-error change |",
        "|---|---|---|"]
    for case in CASES:
        p = s["network_groups"][f"{case}_n4096"]["clocks"]["common_T100"]
        cells = [f"{100*h['fractional_reduction']:+.1f}% reduction; {h['classification'].replace('_',' ')}" for h in p["hierarchy"]]
        lines.append(f"| {case} | {cells[0]} | {cells[1]} |")
    lines += ["", "Negative reduction means the higher order has larger average squared error. Numerical control effects are same-geometry controls: half-step at4096 and float64 at1024, both seed1729. Width drift and seed spread remain separate uncertainties.", "",
        "Existing closure quadrature checks cover only triple_d40 and quad_d30. At triple_d40, doubled quadrature changes N1 by4.18% and N5 by2.57%, failing the2% tolerance; N3 changes1.51%. Quad_d30 changes about0.50–0.53% and passes. The other four geometries have no matched closure quadrature/step controls. No new high-precision closure runs were requested.", "",
        "Secondary endpoint comparisons (network T120 versus the saved closure endpoint at T100–120) are in summary.json. Those clocks are explicitly different when the closure stopped at T100. Network T120 is a fixed cap, and unmet settling gates remain marked unsettled.", "",
        "All per-seed RMS/max/shape errors, mean-reference RMS, seed SD/SE, paired gains, both clock comparisons, and provenance hashes are retained in summary.json; exact unmodified curves are in curves.npz. Independent saved-state verification is recorded separately in verification_final/verification.json.", "",
        "This is empirical accuracy of these finite networks and numerical closures. It establishes neither an infinite-width limit nor convergence as closure order increases.", ""]
    return "\n".join(lines)


def selftest():
    theta = 2*np.pi*np.arange(1440)/1440
    f = np.sin(theta)
    require(abs(distance(2*f,f)["relative_rms"]-1) < 1e-14, "raw gain metric")
    require(distance(2*f,f)["normalized_shape_rms"] < 1e-14, "shape metric")
    require(abs(spectral(np.sin(3*theta))["k_rms"]-3) < 1e-14, "spectral oracle")
    good = paired_gain([1,1.1,.9],[.5,.6,.4])
    require(gain_gate(good,.1) and not gain_gate(good,.3) and not gain_gate(good,None), "control floor")
    require(not gain_gate(paired_gain([1,1,1],[.95,.95,.95]),0), "10% threshold")
    stack = np.stack([f+.1*np.cos(theta),f-.2*np.cos(theta),f+.3*np.cos(theta)])
    require(abs(np.mean((.9*f-stack)**2)-np.mean((.9*f-stack.mean(0))**2)-np.mean((stack-stack.mean(0))**2))<1e-14,
            "ensemble decomposition")
    return dict(passed=True, checks=["raw_gain_vs_shape", "spectral_oracle", "paired_seed_gain", "unknown_control_is_not_zero", "ensemble_decomposition"], source_sha256=sha(__file__))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        print(json.dumps(selftest()))
    else:
        require(args.campaign is not None and args.output is not None, "campaign/output required")
        run(args.campaign.resolve(), args.output.resolve())
