"""Analyze frozen MNIST moment runs without choosing seeds or fitting endpoints.

All predictions are paired by their own model's training-loss crossing.  They
are not a comparison at a common physical time.  The two original tolerances
determine primary endpoint eligibility, even when a third refinement exists.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np


LEVELS = (0.1, 0.03, 0.01, 0.003, 0.001)
BASE_RTOLS = (2e-4, 5e-5)
REFINED_RTOL = 1.25e-5
MODELS = ("dense", "P1", "P2", "P3")
COLORS = {"dense": "#222222", "P1": "#0072B2", "P2": "#D55E00", "P3": "#009E73"}


@dataclass(frozen=True)
class Protocol:
    training_count: int
    widths: tuple[int, ...]
    base_rtols: tuple[float, float]
    refined_rtol: float


PROTOCOLS = {
    "mnist1000": Protocol(1000, (512, 1024), BASE_RTOLS, REFINED_RTOL),
    "mnist100": Protocol(100, (4096,), (1.25e-5, 3.125e-6), 7.8125e-7),
}
DEFAULT_PROTOCOL = PROTOCOLS["mnist1000"]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rms(values):
    return float(np.sqrt(np.mean(np.square(values))))


def same(a, b):
    return bool(np.isclose(float(a), float(b), rtol=1e-9, atol=1e-14))


def loss_key(value):
    for level in LEVELS:
        if same(value, level):
            return level
    raise ValueError(f"unregistered training-loss endpoint {value}")


def accuracy(predictions, labels):
    return float(np.mean(np.where(predictions >= 0, 1., -1.) == labels))


@dataclass
class Endpoint:
    level: float
    physical_time: float
    train_mse: float
    validation: np.ndarray
    train_accuracy: float | None
    source: str


@dataclass
class Run:
    path: Path
    model: str
    rtol: float
    width: int
    seed: int
    data_sha256: str
    meta: dict
    endpoints: dict[float, Endpoint]
    trace_time: np.ndarray
    trace_loss: np.ndarray
    files: list[Path] = field(default_factory=list)


def run_at(runs, model, rtol):
    candidates = [run for run in runs if run.model == model and same(run.rtol, rtol)]
    if len(candidates) > 1:
        raise ValueError(f"duplicate runs for {model}, rtol={rtol:g}; no run selection is allowed")
    return candidates[0] if candidates else None


def cell_runs(runs, model, level):
    return sorted((run for run in runs if run.model == model and level in run.endpoints),
                  key=lambda run: run.rtol, reverse=True)


def refinement_record(runs, model, level):
    available = cell_runs(runs, model, level)
    pairs = []
    for coarse, fine in zip(available, available[1:]):
        pairs.append(dict(coarse_rtol=coarse.rtol, fine_rtol=fine.rtol,
                          validation_prediction_rms=rms(
                              coarse.endpoints[level].validation - fine.endpoints[level].validation),
                          coarse_time=coarse.endpoints[level].physical_time,
                          fine_time=fine.endpoints[level].physical_time))
    return dict(model=model, level=level,
                available_rtols=[run.rtol for run in available],
                finest_rtol=available[-1].rtol if available else None,
                adjacent_pairs=pairs,
                finest_pair_rms=pairs[-1]["validation_prediction_rms"] if pairs else None)


def compare_cell(runs, model, level, refinements):
    dense_runs = cell_runs(runs, "dense", level)
    closure_runs = cell_runs(runs, model, level)
    if not dense_runs or not closure_runs:
        return None
    dense, closure = dense_runs[-1], closure_runs[-1]
    de, ce = dense.endpoints[level], closure.endpoints[level]
    discrepancy = rms(ce.validation - de.validation)
    dd = refinements[("dense", level)]["finest_pair_rms"]
    cd = refinements[(model, level)]["finest_pair_rms"]
    threshold = min(.005, .1 * discrepancy)
    verified = dd is not None and cd is not None
    gate = verified and dd <= threshold and cd <= threshold
    margin = dd + cd if verified else None
    if not gate:
        agreement = "inconclusive_numerical_refinement"
    elif discrepancy + margin < .1:
        agreement = "below_0.1_with_observed_refinement_margin"
    elif discrepancy - margin >= .1:
        agreement = "above_or_equal_0.1_with_observed_refinement_margin"
    else:
        agreement = "threshold_unresolved_by_observed_refinement"
    same_tolerance_scores = []
    for rtol in sorted(set(run.rtol for run in dense_runs + closure_runs), reverse=True):
        d = run_at(runs, "dense", rtol)
        c = run_at(runs, model, rtol)
        if d is not None and c is not None and level in d.endpoints and level in c.endpoints:
            same_tolerance_scores.append(dict(rtol=rtol, rms=rms(
                c.endpoints[level].validation - d.endpoints[level].validation)))
    return dict(model=model, order=int(model[1:]), level=level,
                rms_difference=discrepancy, dense_rtol=dense.rtol, closure_rtol=closure.rtol,
                dense_physical_time=de.physical_time, closure_physical_time=ce.physical_time,
                dense_train_mse=de.train_mse, closure_train_mse=ce.train_mse,
                dense_refinement_rms=dd, closure_refinement_rms=cd,
                refinement_gate_threshold=threshold, numerical_gate_passed=bool(gate),
                observed_refinement_margin=margin, practical_agreement=agreement,
                same_tolerance_scores=same_tolerance_scores)


def compare_orders(cells):
    comparisons = []
    by_order = {cell["order"]: cell for cell in cells}
    for left, right in ((1, 2), (2, 3), (1, 3)):
        if left not in by_order or right not in by_order:
            continue
        a, b = by_order[left], by_order[right]
        improvement = a["rms_difference"] - b["rms_difference"]
        margins = (a["observed_refinement_margin"], b["observed_refinement_margin"])
        margin = sum(margins) if all(x is not None for x in margins) else None
        if not (a["numerical_gate_passed"] and b["numerical_gate_passed"]):
            verdict = "inconclusive_numerical_refinement"
        elif improvement > margin:
            verdict = "improvement_resolved_by_observed_refinement"
        elif improvement < -margin:
            verdict = "worsening_resolved_by_observed_refinement"
        else:
            verdict = "order_difference_unresolved_by_observed_refinement"
        comparisons.append(dict(from_order=left, to_order=right,
                                rms_improvement=improvement,
                                observed_refinement_margin=margin, verdict=verdict))
    return comparisons


def primary_level(runs, protocol=DEFAULT_PROTOCOL):
    eligible = [level for level in LEVELS if all(
        (run_at(runs, model, rtol) is not None and
         level in run_at(runs, model, rtol).endpoints)
        for model in MODELS for rtol in protocol.base_rtols)]
    return min(eligible) if eligible else None


def refinement_requests(runs, comparisons, protocol=DEFAULT_PROTOCOL):
    """Flag original-resolution gate failures; do not request a second extra run."""
    requests = {model: [] for model in MODELS}
    for cell in comparisons:
        level, model = cell["level"], cell["model"]
        d0, d1 = (run_at(runs, "dense", rtol) for rtol in protocol.base_rtols)
        c0, c1 = (run_at(runs, model, rtol) for rtol in protocol.base_rtols)
        if any(run is None or level not in run.endpoints for run in (d0, d1, c0, c1)):
            continue
        discrepancy = rms(c1.endpoints[level].validation - d1.endpoints[level].validation)
        for current, coarse, fine in (("dense", d0, d1), (model, c0, c1)):
            delta = rms(coarse.endpoints[level].validation - fine.endpoints[level].validation)
            if delta > .005 or delta > .1 * discrepancy:
                requests[current].append(dict(level=level, compared_closure=model,
                    base_refinement_rms=delta, base_closure_dense_rms=discrepancy,
                    exceeds_absolute_gate=delta > .005,
                    exceeds_relative_gate=delta > .1 * discrepancy))
    return [dict(model=model, requested_rtol=protocol.refined_rtol,
                 refinement_already_present=run_at(runs, model, protocol.refined_rtol) is not None,
                 reasons=reasons)
            for model, reasons in requests.items() if reasons]


def save_figure(fig, output, basename):
    fig.savefig(output / (basename + ".png"), dpi=180, bbox_inches="tight")
    fig.savefig(output / (basename + ".pdf"), bbox_inches="tight")


def make_plots(runs, rows, primary, labels, output, protocol=DEFAULT_PROTOCOL):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "pdf.fonttype": 42})
    figures = []
    for level in LEVELS:
        current = [row for row in rows if same(row["level"], level)]
        if not current:
            continue
        fig, axes = plt.subplots(1, 3, figsize=(12.3, 4), constrained_layout=True)
        for order, ax in enumerate(axes, start=1):
            row = next((r for r in current if r["order"] == order), None)
            if row is None:
                ax.text(.5, .5, f"P={order}: endpoint not reached", ha="center", va="center",
                        transform=ax.transAxes)
                ax.set_axis_off()
                continue
            dp = cell_runs(runs, "dense", level)[-1].endpoints[level].validation
            cp = cell_runs(runs, f"P{order}", level)[-1].endpoints[level].validation
            for label, digit, color in ((-1., 3, "#0072B2"), (1., 8, "#D55E00")):
                keep = labels == label
                ax.scatter(dp[keep], cp[keep], s=7, alpha=.5, color=color,
                           linewidths=0, label=f"Digit {digit}", rasterized=True)
            low, high = min(dp.min(), cp.min()), max(dp.max(), cp.max())
            pad = max((high - low) * .05, .05)
            low, high = low-pad, high+pad
            ax.plot([low, high], [low, high], color="#666666", linewidth=1)
            ax.set(xlim=(low, high), ylim=(low, high), xlabel="Dense prediction",
                   ylabel=f"P={order} prediction")
            ax.set_aspect("equal", adjustable="box")
            status = "" if row["numerical_gate_passed"] else "\nrefinement inconclusive"
            ax.set_title(f"P={order}   RMS={row['rms_difference']:.4f}{status}")
            if order == 1:
                ax.legend(frameon=False, markerscale=2, fontsize=9)
        tag = "Primary" if primary is not None and same(primary, level) else "Additional endpoint"
        fig.suptitle(f"{tag}: training MSE {level:g} · validation digits 3 and 8")
        name = "scatter_primary" if primary is not None and same(primary, level) else f"scatter_loss_{level:g}"
        save_figure(fig, output, name)
        figures.append(name)
        plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)
    for run in sorted(runs, key=lambda r: (MODELS.index(r.model), -r.rtol)):
        style = ":" if same(run.rtol, protocol.base_rtols[0]) else "--" if same(run.rtol, protocol.base_rtols[1]) else "-"
        ax.plot(run.trace_time, run.trace_loss, linestyle=style, color=COLORS[run.model],
                label=f"{run.model}, rtol={run.rtol:g}", linewidth=1.4)
    if primary is not None:
        ax.axhline(primary, color="#777777", linewidth=.7, label=f"Primary MSE {primary:g}")
    ax.set(xlabel="Physical time", ylabel="Training MSE", yscale="log",
           title="Training loss along each trajectory")
    ax.legend(frameon=False, ncol=2, fontsize=8)
    save_figure(fig, output, "train_loss_vs_time")
    figures.append("train_loss_vs_time")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)
    for level in LEVELS:
        current = sorted((row for row in rows if same(row["level"], level)), key=lambda r: r["order"])
        if not current:
            continue
        label = f"MSE {level:g}" + (" (primary)" if primary is not None and same(primary, level) else "")
        line, = ax.plot([row["order"] for row in current], [row["rms_difference"] for row in current],
                       "-", linewidth=1.6, label=label)
        for row in current:
            ax.plot(row["order"], row["rms_difference"], "o", color=line.get_color(),
                    markerfacecolor=line.get_color() if row["numerical_gate_passed"] else "white")
            if row["observed_refinement_margin"] is not None:
                ax.errorbar(row["order"], row["rms_difference"],
                            yerr=row["observed_refinement_margin"], fmt="none",
                            capsize=3, color=line.get_color(), linewidth=1)
    ax.axhline(.1, color="#777777", linestyle=":", linewidth=1, label="Coarse agreement: 0.1")
    ax.set(xlabel="Moment order P", ylabel="Validation RMS difference from dense",
           xticks=[1, 2, 3], xlim=(.8, 3.2), title="Prediction agreement at own-loss endpoints")
    ax.set_ylim(bottom=0)
    ax.legend(frameon=False, fontsize=8)
    fig.text(.5, -.035, "Bars: observed refinement margins, not confidence intervals. Open circles: numerical gate failed.",
             ha="center", fontsize=8)
    save_figure(fig, output, "rms_vs_order")
    figures.append("rms_vs_order")
    plt.close(fig)
    return figures


def discover_runs(paths):
    """Inspect only explicitly supplied directories and their immediate children."""
    folders = []
    for path in paths:
        if (path / "summary.json").is_file():
            folders.append(path.resolve())
        else:
            folders.extend(p.parent.resolve() for p in sorted(path.glob("*/summary.json")))
    if len(set(folders)) != len(folders):
        raise ValueError("the same run directory was supplied more than once")
    if not folders:
        raise ValueError("no completed run summary.json files in supplied directories")
    return folders


def load_run(folder, frozen, dataset_hash, protocol=DEFAULT_PROTOCOL):
    summary_path, arrays_path = folder / "summary.json", folder / "arrays.npz"
    meta = json.loads(summary_path.read_text())
    model = "dense" if meta["model"] == "dense" else f"P{meta['P']}"
    if meta["model"] not in ("dense", "moment") or model not in MODELS:
        raise ValueError(f"unrecognized model in {summary_path}")
    if meta["seed"] != 20260924 or meta["width"] not in protocol.widths:
        raise ValueError(f"non-protocol seed or width: {folder}")
    if meta["dataset_sha256"] != dataset_hash:
        raise ValueError(f"prepared dataset hash mismatch: {folder}")
    if meta["arrays_sha256"] != sha256(arrays_path):
        raise ValueError(f"arrays checksum mismatch: {folder}")
    if not any(same(meta["rtol"], rtol) for rtol in (*protocol.base_rtols, protocol.refined_rtol)):
        raise ValueError(f"non-protocol tolerance: {folder}")
    if not same(meta["atol"], meta["rtol"] / 100):
        raise ValueError(f"non-protocol absolute tolerance: {folder}")
    if not same(meta["target_loss"], LEVELS[-1]):
        raise ValueError(f"primary analysis cannot include throughput pilots: {folder}")
    if meta["dtype"] != "float64" or meta["status"] == "running":
        raise ValueError(f"invalid dtype or unfinished run: {folder}")
    if (meta["d"], meta["sample_count"], meta["validation_count"]) != (784, protocol.training_count, 1984):
        raise ValueError(f"non-protocol dataset dimensions: {folder}")
    with np.load(arrays_path, allow_pickle=False) as archive:
        names = ("times", "losses", "observation_times", "observation_training_mse",
                 "observation_labels", "validation_predictions", "train_predictions",
                 "validation_labels", "train_labels", "train_ids", "validation_ids")
        data = {name: archive[name].copy() for name in names}
    for name in ("train_labels", "validation_labels", "train_ids", "validation_ids"):
        if not np.array_equal(data[name], frozen[name]):
            raise ValueError(f"saved {name} differ from frozen data: {folder}")
    count = len(data["observation_labels"])
    for name, shape in (("validation_predictions", (count, len(frozen["validation_labels"]))),
                        ("train_predictions", (count, len(frozen["train_labels"]))),
                        ("observation_times", (count,)), ("observation_training_mse", (count,))):
        if data[name].shape != shape or not np.isfinite(data[name]).all():
            raise ValueError(f"invalid {name}: {folder}")
    if (data["times"].ndim != 1 or data["losses"].shape != data["times"].shape
            or not len(data["times"]) or np.any(np.diff(data["times"]) < 0)
            or not np.isfinite(data["times"]).all() or not np.isfinite(data["losses"]).all()
            or np.any(data["losses"] <= 0)):
        raise ValueError(f"invalid training trace: {folder}")
    actual_mse = np.mean((data["train_predictions"] - frozen["train_labels"]) ** 2, axis=1)
    if not np.allclose(actual_mse, data["observation_training_mse"], rtol=1e-8, atol=1e-11):
        raise ValueError(f"saved train predictions disagree with endpoint losses: {folder}")
    endpoints, observations = {}, []
    for index, label in enumerate(data["observation_labels"].astype(str)):
        vp, tp = data["validation_predictions"][index], data["train_predictions"][index]
        observations.append(dict(label=label, physical_time=float(data["observation_times"][index]),
                                 train_mse=float(actual_mse[index]),
                                 train_accuracy=accuracy(tp, frozen["train_labels"]),
                                 validation_label_mse=float(np.mean((vp-frozen["validation_labels"])**2)),
                                 validation_accuracy=accuracy(vp, frozen["validation_labels"])))
        if not label.startswith("loss_"):
            continue
        level = loss_key(float(label[5:]))
        if level in endpoints:
            raise ValueError(f"duplicate loss crossing {level}: {folder}")
        if abs(actual_mse[index] - level) > max(1e-9, 1e-6 * level):
            raise ValueError(f"saved crossing does not match target loss {level}: {folder}")
        endpoints[level] = Endpoint(level=level,
            physical_time=float(data["observation_times"][index]),
            train_mse=float(actual_mse[index]), validation=vp,
            train_accuracy=observations[-1]["train_accuracy"], source=str(arrays_path))
    claimed = {loss_key(level) for level in meta["crossed_losses"]}
    if claimed != set(endpoints):
        raise ValueError(f"summary crossings disagree with observations: {folder}")
    meta["recomputed_observation_metrics"] = observations
    return Run(path=folder, model=model, rtol=float(meta["rtol"]), width=int(meta["width"]),
               seed=int(meta["seed"]), data_sha256=dataset_hash, meta=meta,
               endpoints=endpoints, trace_time=data["times"], trace_loss=data["losses"],
               files=[summary_path, arrays_path])


def write_csv(path, records):
    with path.open("w", newline="") as stream:
        if not records:
            return
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def make_report(summary):
    primary = summary["primary_level"]
    lines = ["# MNIST moment endpoint analysis", "",
             "Validation RMS compares each closure with dense at the same training-loss level, "
             "using each model's own stopping time. These are not same-time comparisons.", ""]
    if primary is None:
        lines += ["No primary fitted endpoint: no predeclared loss level was reached by all "
                  "four models at both original tolerances.", ""]
    else:
        lines += [f"Primary training MSE: **{primary:g}**. It is the smallest predeclared level "
                  "reached by all four models at both original tolerances.", ""]
    lines += ["| Training MSE | P | Validation RMS | Dense / closure rtol | Refinement margin | Numerical gate |",
              "|---:|---:|---:|:---|---:|:---|"]
    for row in summary["comparisons"]:
        margin = row["observed_refinement_margin"]
        margin_text = "unavailable" if margin is None else f"{margin:.6g}"
        lines.append(f"| {row['level']:g} | {row['order']} | {row['rms_difference']:.6g} | "
                     f"{row['dense_rtol']:g} / {row['closure_rtol']:g} | {margin_text} | "
                     f"{'passed' if row['numerical_gate_passed'] else 'inconclusive'} |")
    lines += ["", "Refinement margins sum the observed predictor changes under the latest two "
              "available tolerances. They are empirical sensitivity measures, not rigorous error "
              "bounds or confidence intervals. The gate requires each predictor's change to be "
              "at most both 0.005 and 10% of the closure–dense RMS.", "",
              "| Model | rtol | Status | Final train MSE | Physical time | Integration s | Moving + fixed state MiB |",
              "|:---|---:|:---|---:|---:|---:|---:|"]
    for row in summary["runs"]:
        lines.append(f"| {row['model']} | {row['rtol']:g} | {row['status']} | {row['final_train_mse']:.6g} | "
                     f"{row['final_physical_time']:.6g} | {row['integration_seconds_excluding_observations']:.3f} | "
                     f"{row['persistent_state_bytes']/2**20:.3f} |")
    lines += ["", "State storage includes the evolving state and the retained initial middle matrix "
              "for closures. It excludes retained initialization clones, data, and runtime workspace; "
              "measured CUDA allocation peaks include actual allocations. Peaks and inference time "
              "are in metrics_summary.json. "
              "Training and validation classification metrics are secondary and saved separately "
              "in label_metrics.csv. Every run and reached endpoint is retained.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", nargs="+", type=Path, required=True,
                        help="Run directories or their immediate parent directories; exclude pilots")
    parser.add_argument("--dataset", type=Path, required=True, help="Frozen prepared.npz")
    parser.add_argument("--output", type=Path, required=True, help="Fresh analysis directory")
    parser.add_argument("--protocol", choices=tuple(PROTOCOLS), default="mnist1000",
                        help="Frozen dataset, width and tolerance schedule (default: original mnist1000)")
    args = parser.parse_args(argv)
    protocol = PROTOCOLS[args.protocol]
    started = time.monotonic()
    args.output.mkdir(parents=True, exist_ok=False)
    dataset_hash = sha256(args.dataset)
    with np.load(args.dataset, allow_pickle=False) as archive:
        frozen = {name: archive[name].copy() for name in
                  ("train_labels", "validation_labels", "train_ids", "validation_ids")}
    if (len(frozen["train_labels"]) != protocol.training_count or len(frozen["validation_labels"]) != 1984
            or not np.array_equal(np.unique(frozen["train_labels"]), [-1., 1.])
            or not np.array_equal(np.unique(frozen["validation_labels"]), [-1., 1.])):
        raise ValueError("dataset does not match frozen MNIST 3/8 protocol")
    runs = [load_run(folder, frozen, dataset_hash, protocol) for folder in discover_runs(args.runs)]
    for model in MODELS:
        for rtol in (*protocol.base_rtols, protocol.refined_rtol):
            run_at(runs, model, rtol)
    if len({run.width for run in runs}) != 1 or len({run.meta["initialization_hash"] for run in runs}) != 1:
        raise ValueError("all runs must share the exact initialization and width")
    if len({json.dumps(run.meta["source_sha256"], sort_keys=True) for run in runs}) != 1:
        raise ValueError("runner source hashes differ across supplied scientific runs")
    refinements = {(model, level): refinement_record(runs, model, level)
                   for model in MODELS for level in LEVELS}
    comparisons = [cell for level in LEVELS for model in MODELS[1:]
                   if (cell := compare_cell(runs, model, level, refinements)) is not None]
    primary = primary_level(runs, protocol)
    run_rows, label_rows, endpoint_rows = [], [], []
    for run in sorted(runs, key=lambda r: (MODELS.index(r.model), -r.rtol)):
        m = run.meta
        row = dict(model=run.model, rtol=run.rtol, width=run.width, status=m["status"],
                   run_directory=str(run.path), final_train_mse=m["training_mse"],
                   final_physical_time=m["time"], reached_levels=list(run.endpoints),
                   missing_levels=[level for level in LEVELS if level not in run.endpoints],
                   moving_state_bytes=m["moving_state_bytes"], fixed_W0_bytes=m["fixed_W0_bytes"],
                   persistent_state_bytes=m["moving_state_bytes"] + m["fixed_W0_bytes"],
                   moment_history_scalars=m.get("history_scalars", 0),
                   accepted_steps=m["accepted"], rejected_steps=m["rejected"])
        for name in ("peak_process_rss_bytes", "peak_cuda_allocated_bytes", "peak_cuda_reserved_bytes",
                     "integration_seconds_excluding_observations", "integration_with_observations_seconds",
                     "observation_seconds", "total_work_seconds"):
            row[name] = m[name]
        run_rows.append(row)
        label_rows.extend(dict(model=run.model, rtol=run.rtol, **observation)
                          for observation in m["recomputed_observation_metrics"])
        for level, endpoint in run.endpoints.items():
            endpoint_rows.append(dict(model=run.model, rtol=run.rtol, level=level,
                physical_time=endpoint.physical_time, train_mse=endpoint.train_mse,
                train_accuracy=endpoint.train_accuracy,
                validation_label_mse=float(np.mean((endpoint.validation-frozen["validation_labels"])**2)),
                validation_accuracy=accuracy(endpoint.validation, frozen["validation_labels"])))
    summary = dict(
        schema_version=1, protocol=args.protocol, seed=20260924, digits=[3, 8],
        training_count=protocol.training_count,
        validation_count=len(frozen["validation_labels"]), width=runs[0].width,
        primary_level=primary,
        endpoint_selection=("lowest predeclared loss reached by all four models at "
                            f"rtol={protocol.base_rtols[0]:g} and {protocol.base_rtols[1]:g}"),
        prediction_selection="finest available tolerance separately for each model and endpoint",
        comparison_timing="own training-loss crossing; not common physical time",
        refinement_margin_interpretation="observed sensitivity, not a rigorous error bound or confidence interval",
        practical_agreement_threshold=.1,
        state_memory_accounting="moving state plus fixed W0 only; excludes initialization clones, data, and runtime workspace; CUDA peak reports actual allocations",
        comparisons=comparisons, numerical_refinements=list(refinements.values()),
        order_comparisons=[dict(level=level, comparisons=compare_orders(
            [row for row in comparisons if same(row["level"], level)])) for level in LEVELS],
        refinement_requests=refinement_requests(runs, comparisons, protocol),
        runs=run_rows, capped_runs=[row for row in run_rows if row["status"] != "target_loss"],
        resource_totals={name: sum(row[name] for row in run_rows) for name in
                         ("integration_seconds_excluding_observations",
                          "integration_with_observations_seconds", "observation_seconds", "total_work_seconds")},
        missing_base_runs=[dict(model=model, rtol=rtol) for model in MODELS for rtol in protocol.base_rtols
                           if run_at(runs, model, rtol) is None],
        provenance=dict(dataset=str(args.dataset.resolve()), dataset_sha256=dataset_hash,
                        analysis_source_sha256=sha256(__file__),
                        input_hashes={str(file): sha256(file) for run in runs for file in run.files},
                        run_source_sha256=runs[0].meta["source_sha256"],
                        initialization_hash=runs[0].meta["initialization_hash"],
                        python=sys.version, numpy=np.__version__, command=sys.argv))
    individual = {"validation_ids": frozen["validation_ids"],
                  "validation_labels": frozen["validation_labels"],
                  "validation_digits": np.where(frozen["validation_labels"] == -1, 3, 8)}
    for level in LEVELS:
        tag = format(level, "g").replace(".", "p")
        for model in MODELS:
            available = cell_runs(runs, model, level)
            if available:
                individual[f"prediction_{model}_loss_{tag}"] = available[-1].endpoints[level].validation
        for model in MODELS[1:]:
            dense_key, closure_key = f"prediction_dense_loss_{tag}", f"prediction_{model}_loss_{tag}"
            if dense_key in individual and closure_key in individual:
                individual[f"error_{model}_loss_{tag}"] = individual[closure_key] - individual[dense_key]
    np.savez_compressed(args.output / "validation_predictions_and_errors.npz", **individual)
    summary["individual_predictions_and_errors"] = "validation_predictions_and_errors.npz"
    summary["figures"] = make_plots(runs, comparisons, primary, frozen["validation_labels"], args.output, protocol)
    flat_comparisons = [{key: value for key, value in row.items() if key != "same_tolerance_scores"}
                        for row in comparisons]
    write_csv(args.output / "prediction_comparisons.csv", flat_comparisons)
    write_csv(args.output / "endpoint_metrics.csv", endpoint_rows)
    write_csv(args.output / "label_metrics.csv", label_rows)
    summary["analysis_wall_seconds"] = time.monotonic() - started
    (args.output / "metrics_summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n")
    (args.output / "analysis_report.md").write_text(make_report(summary))
    print(json.dumps(dict(output=str(args.output), primary_level=primary,
                         comparisons=[row for row in comparisons if primary is not None and same(row["level"], primary)],
                         refinement_requests=summary["refinement_requests"],
                         missing_base_runs=summary["missing_base_runs"],
                         analysis_wall_seconds=summary["analysis_wall_seconds"]), indent=2))


if __name__ == "__main__":
    main()
