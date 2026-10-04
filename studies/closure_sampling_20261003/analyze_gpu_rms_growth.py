"""Recompute the preregistered RMS growth metrics from saved GPU observations.

No training or sampler imports. Calibration selection is separate from holdout
acceptance. Missing prescribed refinement checks leave validation provisional.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import sys

import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def metrics(predictions):
    error = predictions - predictions[:, :1, :]
    return {
        "rms_time_sup": np.sqrt(np.mean(np.max(np.abs(error), axis=0) ** 2, axis=1)),
        "max_time_rms": np.sqrt(np.mean(error ** 2, axis=2)).max(axis=0),
        "endpoint_rms": np.sqrt(np.mean(error[-1] ** 2, axis=1)),
        "sup_panel_time": np.max(np.abs(error), axis=(0, 2)),
        "endpoint_sup": np.max(np.abs(error[-1]), axis=1),
    }


def metric_oracle():
    predictions = np.zeros((2, 2, 2))
    predictions[0, 1, 0] = predictions[1, 1, 1] = 1.
    got = metrics(predictions)
    assert got["rms_time_sup"][1] == 1.
    assert np.isclose(got["max_time_rms"][1], 1 / np.sqrt(2))
    assert np.isclose(got["endpoint_rms"][1], 1 / np.sqrt(2))
    return {key: float(value[1]) for key, value in got.items()}


def write_csv(path, rows):
    if not rows:
        Path(path).write_text("")
        return
    with Path(path).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def case_key(record):
    return tuple(record[k] for k in ("n", "seed", "angle", "sign"))


def expected_cases(stage):
    if stage == "calibration":
        widths, seeds = (512, 1024, 2048), (8411,)
    elif stage == "validation":
        widths, seeds = (512, 1024, 2048, 4096), range(8511, 8516)
    else:
        widths, seeds = (8192,), (8611,)
    return {(n, seed, angle, sign) for n in widths for seed in seeds
            for angle in (60., 90.) for sign in (-1, 1)}


def load_case(folder):
    folder = Path(folder)
    record = json.loads((folder / "record.json").read_text())
    for filename in ("observations.npz", "reduced_restart.npz"):
        expected = record.get(filename + "_sha256")
        if expected is None or digest(folder / filename) != expected:
            raise ValueError("Missing or mismatched archive hash: " + str(folder / filename))
    with np.load(folder / "observations.npz", allow_pickle=False) as archive:
        data = {key: archive[key] for key in archive.files}
    required = ("times", "panel", "predictions", "residual_rms", "feature_motion")
    for key in required:
        if key not in data or not np.isfinite(data[key]).all():
            raise ValueError("Missing/nonfinite " + key + " in " + str(folder))
    prediction = data["predictions"]
    if prediction.ndim != 3 or prediction.shape[0] != len(data["times"]):
        raise ValueError("Prediction/time shape mismatch in " + str(folder))
    if len(record["model_names"]) != prediction.shape[1]:
        raise ValueError("Model-name shape mismatch in " + str(folder))
    if not np.all(np.diff(data["times"]) > 0):
        raise ValueError("Observation times must increase strictly")
    if data["panel"].shape != (prediction.shape[2], 2):
        raise ValueError("Query-panel shape mismatch")
    if "training_predictions" in data:
        residual = np.sqrt(np.mean((data["training_predictions"] - data["labels"]) ** 2, axis=2))
        if not np.allclose(residual, data["residual_rms"], atol=1e-12, rtol=1e-10):
            raise ValueError("Stored residuals disagree with signed training predictions")
    return record, data


def core_gate(root):
    path = root / "core_validation.json"
    if not path.exists():
        return False, {"missing": str(path)}
    record = json.loads(path.read_text())
    # Required established equation/restart oracles. Other diagnostics may be
    # nested or non-error values, so do not interpret every number as an error.
    required = ("rhs_public", "heun_public", "uniform_weighted_rhs",
                "uniform_weighted_heun", "weighted_autograd", "restart")
    dynamics = record.get("dynamics", record)
    ok = all(key in dynamics and np.isfinite(dynamics[key]) and
             abs(dynamics[key]) < 2e-12 for key in required)
    metric_checks = record.get("metrics", {})
    ok = ok and all(metric_checks.get(key) is True for key in
                    ("noncommuting_metric_oracle", "root_scaling", "zero_baseline"))
    return bool(ok), record


def extract(roots, stage):
    rows, controls, cases, failures, provenance = [], [], [], [], []
    seen = set()
    for root in roots:
        root = Path(root)
        core_ok, core = core_gate(root)
        status_path = root / "status.json"
        status = json.loads(status_path.read_text()) if status_path.exists() else {}
        failures.extend(dict(root=str(root), **failure) for failure in status.get("failures", []))
        provenance.append({"root": str(root), "core_pass": core_ok, "core_checks": core,
                           "status": status, "status_present": status_path.exists(),
                           "metadata_hashes": {name: digest(root / name) for name in
                              ("core_validation.json", "provenance.json", "config.input.json", "config.resolved.json")
                              if (root / name).exists()}})
        for record_path in sorted(root.glob("*/record.json")):
            folder = record_path.parent
            record, data = load_case(folder)
            value = metrics(data["predictions"])
            if "metrics" in record:
                names = {"rms_time_sup": "rms_of_time_sup", "max_time_rms": "sup_of_time_rms",
                         "endpoint_rms": "endpoint_rms", "sup_panel_time": "sup_panel_time"}
                for ours, stored in names.items():
                    if not np.allclose(value[ours], [r[stored] for r in record["metrics"]], atol=1e-14, rtol=1e-12):
                        raise ValueError("Archived metric mismatch: " + stored + " at " + str(folder))
            tail_indices = data["times"] >= data["times"][-1] - 10 - 1e-10
            tail = np.max(np.abs(data["predictions"][tail_indices] - data["predictions"][-1]), axis=(0, 2))
            residual = data["residual_rms"][-1]
            settled = (residual <= 1e-6) & (tail <= 1e-5) & (data["times"][-1] >= 10)
            base = {key: record[key] for key in ("n", "seed", "angle", "sign")}
            base.update(phase=stage, case_path=str(folder))
            root_n = np.sqrt(record["n"])
            control_indices = [1]
            if "frozen_dense_hidden" in record["model_names"]:
                control_indices.append(record["model_names"].index("frozen_dense_hidden"))
            moving_indices = [j for j, name in enumerate(record["model_names"]) if name != "frozen_dense_hidden"]
            for j in control_indices:
                controls.append(dict(base, model=record["model_names"][j],
                    **{key: float(v[j]) for key, v in value.items()},
                    scaled_rms=float(root_n * value["rms_time_sup"][j]),
                    scaled_endpoint_rms=float(root_n * value["endpoint_rms"][j]),
                    fit_rms=float(residual[j]), tail_change=float(tail[j]), settled=bool(settled[j])))
            for specification in record["schedule"]:
                j = int(specification["model_index"])
                n_selected = int(specification["width"])
                rank = int(specification["rank"])
                total = n_selected ** 2 + 5 * n_selected + 6
                if total != int(specification["total"]):
                    raise ValueError("State-count mismatch: " + str(folder))
                p = specification.get("p", "")
                if stage != "calibration" and p not in (0, 1, 2, 4):
                    raise ValueError("A validation/extrapolation schedule requires explicit p in {0,1,2,4}")
                budget = specification.get("budget")
                if budget is not None and not (total <= budget + 1e-8 and
                        (n_selected + 1) ** 2 + 5 * (n_selected + 1) + 6 > budget - 1e-8):
                    raise ValueError("Selected width is not maximal within its stated budget")
                identity = (case_key(record), p, n_selected, rank)
                if identity in seen:
                    raise ValueError("Duplicate comparison across inputs: " + str(identity))
                seen.add(identity)
                diag = record["sampler_diagnostics"][j - 2]
                final_optimizer = all(diag[layer]["fits"][-1]["success"] for layer in ("cubature1", "cubature2"))
                warnings = sum(not fit["success"] for layer in ("cubature1", "cubature2")
                               for fit in diag[layer]["fits"][:-1])
                discarded = sum(diag[layer]["discarded_directions"] for layer in ("frame1", "frame2"))
                valid = bool(core_ok and settled[0] and settled[1] and settled[j]
                             and final_optimizer and discarded == 0)
                primary = float(value["rms_time_sup"][j])
                dense = float(value["rms_time_sup"][1])
                rows.append(dict(base, model=record["model_names"][j], p=p,
                    N=n_selected, rank=rank, P=total, moving=n_selected ** 2 + 3 * n_selected,
                    fixed=2 * n_selected + 6,
                    **{key: float(v[j]) for key, v in value.items()},
                    scaled_rms=float(root_n * primary),
                    scaled_max_time_rms=float(root_n * value["max_time_rms"][j]),
                    scaled_endpoint_rms=float(root_n * value["endpoint_rms"][j]),
                    dense_rms=dense, dense_scaled_rms=float(root_n * dense),
                    paired_rms_ratio=primary / dense if dense else None,
                    fit_rms=float(residual[j]), tail_change=float(tail[j]), settled=bool(settled[j]),
                    dense_settled=bool(settled[0] and settled[1]),
                    core_pass=core_ok, final_optimizer_pass=bool(final_optimizer),
                    intermediate_optimizer_warnings=int(warnings), discarded_frame_modes=int(discarded),
                    valid_model=valid, feature1=float(data["feature_motion"][-1, j, 0]),
                    feature2=float(data["feature_motion"][-1, j, 1]),
                    dense_feature1=float(data["feature_motion"][-1, 0, 0]),
                    dense_feature2=float(data["feature_motion"][-1, 0, 1]),
                    cubature_gram1=float(diag["cubature1"]["gram_operator_error"]),
                    cubature_gram2=float(diag["cubature2"]["gram_operator_error"]),
                    source_h0=float(diag["basis1"]["source_residuals"]["h0"]["relative_frobenius"]),
                    source_g0=float(diag["basis2"]["source_residuals"]["g0"]["relative_frobenius"]),
                    forward_error=float(diag["forward_initial"]["mean_weighted_rms"]),
                    reverse_error=float(diag["reverse_initial_jet"]["mean_weighted_rms"]),
                    last_time=float(data["times"][-1]), dt=float(record["dt"])))
            cases.append(dict(base, all_moving_settled=bool(np.all(settled[moving_indices])),
                max_moving_residual=float(np.max(residual[moving_indices])),
                max_moving_tail_change=float(np.max(tail[moving_indices])), last_time=float(data["times"][-1]),
                core_pass=core_ok, record_sha256=digest(record_path),
                observations_sha256=record["observations.npz_sha256"],
                reduced_restart_sha256=record["reduced_restart.npz_sha256"]))
    return rows, controls, cases, failures, provenance


def group_id(row, stage):
    return (row["N"], row["rank"]) if stage == "calibration" else (row["p"],)


def aggregate(rows, stage, bootstrap_samples=2000):
    groups = []
    seeds = sorted({r["seed"] for r in rows})
    rng = np.random.default_rng(90210)
    draws = rng.integers(0, len(seeds), (bootstrap_samples, len(seeds))) if len(seeds) > 1 else None
    keys = sorted({(group_id(r, stage), r["n"], r["angle"], r["sign"]) for r in rows})
    for identity, n, angle, sign in keys:
        selected = [r for r in rows if (group_id(r, stage), r["n"], r["angle"], r["sign"]) == (identity, n, angle, sign)]
        first = selected[0]
        group = dict(phase=stage, p=first["p"], N=first["N"], rank=first["rank"], P=first["P"],
                     n=n, angle=angle, sign=sign, count=len(selected), all_valid=all(r["valid_model"] for r in selected))
        for metric in ("rms_time_sup", "scaled_rms", "max_time_rms", "endpoint_rms", "scaled_endpoint_rms", "paired_rms_ratio"):
            values = [r[metric] for r in selected if r[metric] is not None]
            group[metric + "_median"] = float(np.median(values)) if values else None
            group[metric + "_max"] = max(values) if values else None
        median_dense = float(np.median([r["dense_rms"] for r in selected]))
        group["ratio_of_medians"] = (float(np.median([r["rms_time_sup"] for r in selected])) /
                                     median_dense if median_dense > 0 else None)
        group["bootstrap_scaled_median_low"] = group["bootstrap_scaled_median_high"] = None
        if draws is not None and len(selected) == len(seeds) and {r["seed"] for r in selected} == set(seeds):
            values = np.array([next(r["scaled_rms"] for r in selected if r["seed"] == seed) for seed in seeds])
            lo, hi = np.quantile(np.median(values[draws], axis=1), [.025, .975])
            group["bootstrap_scaled_median_low"], group["bootstrap_scaled_median_high"] = float(lo), float(hi)
        groups.append(group)
    return groups, seeds, draws


def decisions(rows, stage, seeds, draws):
    expected = expected_cases(stage)
    result = []
    for identity in sorted({group_id(r, stage) for r in rows}):
        selected = [r for r in rows if group_id(r, stage) == identity]
        actual = {case_key(r) for r in selected}
        complete = actual == expected and len(selected) == len(expected)
        valid = all(r["valid_model"] for r in selected)
        maximum = max(r["scaled_rms"] for r in selected)
        ceiling = .10 if stage == "calibration" else .15
        growth = []
        if stage == "validation":
            for angle in (60., 90.):
                for sign in (-1, 1):
                    low = [r for r in selected if (r["n"], r["angle"], r["sign"]) == (512, angle, sign)]
                    high = [r for r in selected if (r["n"], r["angle"], r["sign"]) == (4096, angle, sign)]
                    if low and high:
                        factor = float(np.median([r["scaled_rms"] for r in high]) / np.median([r["scaled_rms"] for r in low]))
                        item = dict(angle=angle, sign=sign, median_scaled_growth=factor,
                                    bootstrap_low=None, bootstrap_high=None)
                        if draws is not None and {r["seed"] for r in low} == set(seeds) and {r["seed"] for r in high} == set(seeds):
                            a = np.array([next(r["scaled_rms"] for r in low if r["seed"] == seed) for seed in seeds])
                            b = np.array([next(r["scaled_rms"] for r in high if r["seed"] == seed) for seed in seeds])
                            ratios = np.median(b[draws], axis=1) / np.median(a[draws], axis=1)
                            item["bootstrap_low"], item["bootstrap_high"] = map(float, np.quantile(ratios, [.025, .975]))
                        growth.append(item)
        growth_ok = stage != "validation" or (len(growth) == 4 and all(g["median_scaled_growth"] <= 1.5 for g in growth))
        criterion_pass = bool(complete and valid and maximum <= ceiling and growth_ok)
        status = ("incomplete" if not complete else "invalid_or_unsettled" if not valid else
                  "performance_pass" if criterion_pass else "criterion_fail")
        result.append(dict(identity=list(identity), p=selected[0]["p"], N=selected[0]["N"], rank=selected[0]["rank"],
            complete=complete, missing_cases=[list(k) for k in sorted(expected - actual)],
            extra_cases=[list(k) for k in sorted(actual - expected)], count=len(selected), all_models_valid=valid,
            maximum_scaled_rms=maximum, median_scaled_rms=float(np.median([r["scaled_rms"] for r in selected])),
            count_below_primary=sum(r["scaled_rms"] <= ceiling for r in selected),
            count_below_secondary=sum(r["scaled_rms"] <= .10 for r in selected),
            growth=growth, growth_pass=growth_ok, performance_pass=criterion_pass, status=status,
            worst_case={k: max(selected, key=lambda r: r["scaled_rms"])[k] for k in ("n", "seed", "angle", "sign", "case_path", "model", "scaled_rms")}))
    return result


def refinement(coarse, fine):
    rc, c = load_case(coarse)
    rf, f = load_case(fine)
    if case_key(rc) != case_key(rf):
        raise ValueError("Refinement pairs must use identical width, seed, geometry and labels")
    if rc["model_names"] != rf["model_names"]:
        raise ValueError("Refinement pairs must retain the same model names/order")
    if not np.isclose(c["times"][-1], f["times"][-1], atol=1e-10):
        raise ValueError("Refinement metrics need identical observation horizons")
    indices = np.searchsorted(f["times"], c["times"])
    if np.any(indices >= len(f["times"])) or not np.allclose(f["times"][indices], c["times"], atol=1e-10, rtol=0):
        raise ValueError("Fine times do not contain coarse observation times")
    distance = np.max(np.abs(c["panel"][:, None] - f["panel"][None]), axis=2)
    columns = np.argmin(distance, axis=1)
    if distance[np.arange(len(columns)), columns].max() > 1e-12:
        raise ValueError("Fine panel is not nested with coarse panel")
    shared = f["predictions"][indices][:, :, columns]
    gap = np.max(np.abs(c["predictions"] - shared), axis=(0, 2))
    cm, fm = metrics(c["predictions"]), metrics(f["predictions"])
    change = np.abs(cm["rms_time_sup"] - fm["rms_time_sup"])
    threshold = min(1e-4, .05 * float(cm["rms_time_sup"][1]))
    allowed_step = np.isclose(rf["dt"] * 2, rc["dt"]) or np.isclose(rf["dt"] * 4, rc["dt"])
    proper_refinement = bool(allowed_step and
                             len(f["panel"]) >= 2 * len(c["panel"]) and
                             np.max(np.diff(f["times"])) <= .5 * np.max(np.diff(c["times"])) + 1e-10)
    return dict(case=list(case_key(rc)), coarse=str(coarse), fine=str(fine),
                models=rc["model_names"], threshold=threshold,
                same_point_prediction_change=gap.tolist(), primary_metric_change=change.tolist(),
                dt_pass=bool(gap.max() <= threshold), metric_pass=bool(change.max() <= threshold),
                proper_refinement=proper_refinement,
                passed=bool(proper_refinement and gap.max() <= threshold and change.max() <= threshold))


def plot(rows, controls, groups, stage, out):
    os.environ.setdefault("MPLCONFIGDIR", str((out / "matplotlib_cache").resolve()))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    if stage == "calibration":
        fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), sharey=True, layout="constrained")
        ranks = sorted({r["rank"] for r in rows})
        rank_colors = {rank: plt.get_cmap("tab10")(index) for index, rank in enumerate(ranks)}
        for ax, n in zip(axes, (512, 1024, 2048)):
            for rank in ranks:
                x, y = [], []
                for count in sorted({r["N"] for r in rows if r["rank"] == rank and r["n"] == n}):
                    values = [r["scaled_rms"] for r in rows if (r["n"], r["rank"], r["N"]) == (n, rank, count)]
                    ax.scatter(np.full(len(values), count), values, alpha=.35, s=18, color=rank_colors[rank])
                    x.append(count); y.append(max(values))
                if x: ax.plot(x, y, marker="o", label=f"rank {rank}", color=rank_colors[rank])
            ax.axhline(.10, color="black", linestyle="--", label="selection ceiling" if n == 512 else None)
            ax.set_title(f"Dense width {n}"); ax.set_xlabel("Selected neurons N")
            ax.set_xscale("log", base=2); ax.set_yscale("log"); ax.grid(alpha=.2)
        axes[0].set_ylabel("sqrt(n) × RMS of time maximum")
        axes[0].legend(fontsize=8)
        fig.suptitle("Calibration: individual configurations and worst-case envelopes")
        fig.savefig(out / "calibration_rank_count.png", dpi=180)
        fig.savefig(out / "calibration_rank_count.pdf")
        plt.close(fig)
        return
    ps = sorted({r["p"] for r in rows})
    colors = {p: color for p, color in zip(ps, ("#0072B2", "#D55E00", "#009E73", "#CC79A7"))}
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.4), sharex=True, layout="constrained")
    for ax, (angle, sign) in zip(axes.flat, ((90., 1), (90., -1), (60., 1), (60., -1))):
        for p in ps:
            group = sorted([g for g in groups if (g["p"], g["angle"], g["sign"]) == (p, angle, sign)], key=lambda g: g["n"])
            ax.plot([g["n"] for g in group], [g["scaled_rms_median"] for g in group], marker="o", color=colors[p], label=f"p={p}")
            points = [r for r in rows if (r["p"], r["angle"], r["sign"]) == (p, angle, sign)]
            ax.scatter([r["n"] for r in points], [r["scaled_rms"] for r in points], color=colors[p], alpha=.4, s=13)
        for model, style, label in (("dense_independent", "--", "dense copy"), ("frozen_dense_hidden", ":", "frozen features")):
            subset = [r for r in controls if (r["model"], r["angle"], r["sign"]) == (model, angle, sign)]
            widths = sorted({r["n"] for r in subset})
            ax.plot(widths, [np.median([r["scaled_rms"] for r in subset if r["n"] == n]) for n in widths], style, color="0.35", label=label)
        ax.axhline(.15, color="black", linewidth=.8, label="C=0.15")
        ax.axhline(.10, color="black", linewidth=.6, linestyle=":", label="C=0.10")
        ax.set_title(f"{angle:g}°; " + ("same-sign labels" if sign == 1 else "opposite-sign labels"))
        ax.set_xscale("log", base=2); ax.set_yscale("log"); ax.grid(alpha=.2)
        ax.set_xlabel("Dense width n"); ax.set_ylabel("sqrt(n) × RMS of time maximum")
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=4, fontsize=9)
    fig.suptitle(stage.capitalize() + ": seed medians and every individual trajectory")
    fig.savefig(out / "rms_width_scaling.png", dpi=180)
    fig.savefig(out / "rms_width_scaling.pdf")
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(6.5, 4.2), layout="constrained")
    for p in ps:
        pairs = sorted({(r["n"], r["P"]) for r in rows if r["p"] == p})
        ax.plot([a for a, b in pairs], [b for a, b in pairs], marker="o", label=f"p={p}", color=colors[p])
    ax.set_xscale("log", base=2); ax.set_yscale("log"); ax.grid(alpha=.2)
    ax.set_xlabel("Dense width n"); ax.set_ylabel("Retained scalars P=N²+5N+6"); ax.legend()
    fig.savefig(out / "state_width_scaling.png", dpi=180)
    fig.savefig(out / "state_width_scaling.pdf")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", nargs="+")
    parser.add_argument("--output")
    parser.add_argument("--stage", choices=("calibration", "validation", "extrapolation"))
    parser.add_argument("--refinement-pair", nargs=2, action="append", default=[], metavar=("COARSE_CASE", "FINE_CASE"))
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    oracle = metric_oracle()
    if args.self_test:
        print(json.dumps({"metric_oracle": oracle, "passed": True}, indent=2)); return
    if not args.inputs or not args.output or not args.stage:
        parser.error("--inputs, --output and --stage are required")
    if args.bootstrap_samples < 1:
        parser.error("--bootstrap-samples must be positive")
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    rows, controls, cases, failures, provenance = extract(args.inputs, args.stage)
    if not rows:
        raise ValueError("No completed model comparisons found")
    groups, seeds, draws = aggregate(rows, args.stage, args.bootstrap_samples)
    results = decisions(rows, args.stage, seeds, draws)
    checks = [refinement(*pair) for pair in args.refinement_pair]
    summary = dict(stage=args.stage, case_records=len(cases), distinct_cases=len({case_key(r) for r in cases}),
                   comparison_count=len(rows), failures=failures, decisions=results, metric_oracle=oracle,
                   primary_ceiling=.10 if args.stage == "calibration" else .15,
                   bootstrap=dict(samples=args.bootstrap_samples, seed=90210, cluster_seeds=seeds,
                                  interpretation="descriptive seed-cluster resampling, not a population guarantee"),
                   refinement_checks=checks, inputs=provenance)
    passing = [r for r in results if r["performance_pass"]]
    if args.stage == "calibration":
        choice = min(passing, key=lambda r: (r["N"], r["maximum_scaled_rms"], r["rank"])) if passing else None
        summary["selected_candidate"] = None if choice is None else {key: choice[key] for key in ("N", "rank", "maximum_scaled_rms")}
        summary["selection_status"] = "candidate_available_freeze_selection_before_holdout" if choice else "no_passing_candidate"
    elif args.stage == "validation":
        p = min(r["p"] for r in passing) if passing else 4
        candidate_rows = [r for r in rows if r["p"] == p]
        worst = max(candidate_rows, key=lambda r: r["scaled_rms"]) if candidate_rows else None
        required = {(4096, 8511, 60., -1)}
        if worst is not None: required.add(case_key(worst))
        passed_cases = {tuple(check["case"]) for check in checks if check["passed"]}
        numerical_complete = required <= passed_cases
        summary["smallest_performance_passing_p"] = min(r["p"] for r in passing) if passing else None
        summary["required_refinement_cases"] = [list(k) for k in sorted(required)]
        summary["numerical_validity_complete"] = numerical_complete
        summary["numerical_validity_status"] = "pass" if numerical_complete else "pending_or_failed"
        summary["empirically_sufficient_p"] = sorted(r["p"] for r in passing) if numerical_complete else []
        for result in results:
            if result["performance_pass"]:
                result["status"] = "empirically_sufficient_on_tested_grid" if numerical_complete else "performance_pass_numerics_pending"
    else:
        summary["stress_passing_p"] = sorted(r["p"] for r in passing)
        summary["interpretation"] = "Four-case extrapolation stress, conditional on validation numerical gates"
    write_csv(out / "all_comparisons.csv", rows)
    write_csv(out / "controls.csv", controls)
    write_csv(out / "cases.csv", cases)
    write_csv(out / "cell_summary.csv", groups)
    (out / "summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n")
    protocol = Path(__file__).with_name("GPU_RMS_GROWTH_PROTOCOL.md")
    (out / "analysis_provenance.json").write_text(json.dumps(dict(argv=sys.argv, python=sys.version,
        numpy=np.__version__, analysis_sha256=digest(__file__), protocol_sha256=digest(protocol),
        input_record_hashes={r["case_path"]: r["record_sha256"] for r in cases}), indent=2) + "\n")
    (out / "analysis_source.py").write_bytes(Path(__file__).read_bytes())
    plot(rows, controls, groups, args.stage, out)
    print(json.dumps({key: summary[key] for key in ("stage", "case_records", "comparison_count", "decisions")}, indent=2))
    if args.stage == "calibration": print(json.dumps({"selected_candidate": summary["selected_candidate"]}))


if __name__ == "__main__":
    main()
