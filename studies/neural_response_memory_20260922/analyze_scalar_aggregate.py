"""Plot and tabulate the frozen scalar aggregate campaign; never runs dynamics."""
import argparse
import csv
import hashlib
import json
import shutil
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
DEFAULT_INPUT = REPO / "data/generated/neural_response_memory_20260922/scalar_aggregate_primary01"
DEFAULT_OUTPUT = REPO / "data/generated/neural_response_memory_20260922/scalar_aggregate_analysis01"
CASES = ("equal_mixed_odd", "quadrant_alternating")
CASE_LABELS = {"equal_mixed_odd": "Four-sample circle", "quadrant_alternating": "Eight-sample quadrant"}
WIDTHS = (128, 256)
SEEDS = (20260920, 20260927)
MODELS = ("dense", "order2", "order3", "order4")
COLORS = {"dense": "#111827", "order2": "#64748b", "order3": "#c47a13", "order4": "#7c3aed"}
STYLES = {"dense": "-", "order2": "--", "order3": ":", "order4": "-"}
LABELS = {"dense": "Dense network", "order2": "Order 2 (frozen kernel)", "order3": "Order 3", "order4": "Order 4"}


def clean(x):
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [clean(v) for v in x]
    if isinstance(x, np.ndarray):
        return clean(x.tolist())
    if isinstance(x, np.generic):
        return clean(x.item())
    if isinstance(x, float) and not np.isfinite(x):
        return None
    return x


def write_json(path, value):
    path.write_text(json.dumps(clean(value), indent=2, sort_keys=True) + "\n")


def read_json(path, inputs):
    inputs.add(path)
    return json.loads(path.read_text())


def read_arrays(path, inputs):
    inputs.add(path)
    with np.load(path, allow_pickle=False) as data:
        # Dense parameter checkpoints are intentionally not needed by analysis.
        return {key: data[key].copy() for key in ("times", "f", "loss", "eigenmin", "motion", "kernel")}


def common_curves(candidate, dense):
    times, ic, idense = np.intersect1d(candidate["times"], dense["times"], return_indices=True)
    if not len(times):
        raise ValueError("No common saved observations")
    rms = np.sqrt(np.mean((candidate["f"][ic] - dense["f"][idense]) ** 2, axis=1))
    loss = np.abs(candidate["loss"][ic] - dense["loss"][idense])
    return times, rms, loss, ic, idense


def load_campaign(directory):
    inputs = set()
    campaign = read_json(directory / "campaign.json", inputs)
    if campaign["mode"] != "campaign" or len(campaign["configurations"]) != 8:
        raise RuntimeError("Analysis requires all eight completed configuration records")
    data = []
    for case in CASES:
        for width in WIDTHS:
            for seed in SEEDS:
                folder = directory / f"{case}_n{width}_seed{seed}"
                summary = read_json(folder / "summary.json", inputs)
                config = read_json(folder / "configuration.json", inputs)
                if (config["case"], config["width"], config["seed"]) != (case, width, seed):
                    raise ValueError("Configuration identity mismatch")
                coefficient_path = folder / "coefficients.npz"
                inputs.add(coefficient_path)
                with np.load(coefficient_path, allow_pickle=False) as coeff:
                    labels = coeff["labels"].copy()
                runs = {}
                for name in MODELS:
                    level = summary["latest_resolution"][name]
                    run_directory = folder / f"{name}_resolution{level}"
                    records = [read_json(p, inputs) for p in sorted(folder.glob(f"{name}_resolution*/result.json"))]
                    runs[name] = dict(
                        arrays=read_arrays(run_directory / "trajectory.npz", inputs),
                        record=read_json(run_directory / "result.json", inputs),
                        records=records, level=level,
                    )
                    a = runs[name]["arrays"]
                    if not len(a["times"]) or np.any(np.diff(a["times"]) <= 0):
                        raise ValueError("Missing or unordered observations")
                    calculated_loss = np.mean((a["f"] - labels) ** 2, axis=1)
                    if not np.allclose(calculated_loss, a["loss"], atol=1e-12, rtol=1e-11):
                        raise ValueError("Saved loss disagrees with outputs and labels")
                data.append(dict(config=config, summary=summary, runs=runs, labels=labels, folder=folder))
    return data, campaign, inputs


def full_run(run, end):
    return run["record"]["status"] == "complete" and run["arrays"]["times"][-1] >= end


def tables(data):
    rows, prefixes, curve_checks = [], [], []
    for item in data:
        c, summary, runs = item["config"], item["summary"], item["runs"]
        dense = runs["dense"]["arrays"]
        end = c["end"]
        d_complete = full_run(runs["dense"], end)
        frozen_times, frozen_errors, _, _, _ = common_curves(runs["order2"]["arrays"], dense)
        frozen_complete = full_run(runs["order2"], end) and d_complete
        for name in MODELS:
            run = runs[name]
            a, record = run["arrays"], run["record"]
            times, errors, loss_errors, ia, idense = common_curves(a, dense)
            kernel_difference = np.linalg.norm(a["kernel"][ia]-dense["kernel"][idense], axis=(1, 2))
            initial_kernel_norm = float(np.linalg.norm(dense["kernel"][0]))
            dense_kernel_norm = np.linalg.norm(dense["kernel"][idense], axis=(1, 2))
            complete = full_run(run, end) and d_complete
            producer = summary["orders"].get(name, {})
            max_error, max_loss = float(np.max(errors)), float(np.max(loss_errors))
            if name != "dense":
                if not np.isclose(max_error, producer["prediction_error"], atol=1e-12, rtol=1e-10):
                    raise ValueError("Independent curve error disagrees with producer")
                if not np.isclose(max_loss, producer["loss_error"], atol=1e-12, rtol=1e-10):
                    raise ValueError("Independent loss error disagrees with producer")
                curve_checks.append(dict(case=c["case"], width=c["width"], seed=c["seed"], model=name,
                                         prediction_error=max_error, loss_error=max_loss, matches_summary=True))
            frozen_max = float(np.max(frozen_errors))
            ratio = max_error / frozen_max if name != "dense" and complete and frozen_complete and frozen_max > 0 else None
            storage = record.get("storage", {})
            scalar_gate = producer.get("scalar_gate", {})
            dense_gate = producer.get("dense_gate", {})
            row = dict(
                case=c["case"], samples=c["M"], width=c["width"], seed=c["seed"], model=name,
                latest_resolution=run["level"], rtol=record["rtol"], status=record["status"],
                full_horizon_complete=complete, solver_final_time=record["final_time"],
                last_saved_time=float(a["times"][-1]), last_compared_time=float(times[-1]),
                max_sampled_output_rms_error=max_error, max_sampled_absolute_loss_error=max_loss,
                final_saved_loss=float(a["loss"][-1]), loss_at_128=float(a["loss"][-1]) if complete else None,
                scalar_numerical_gate=scalar_gate.get("pass_gate"), dense_numerical_gate=dense_gate.get("pass_gate"),
                validity_pass=producer.get("validity_pass"), producer_verdict=producer.get("verdict", "reference"),
                scalar_refinement_prediction_change=scalar_gate.get("prediction_change"),
                scalar_refinement_loss_change=scalar_gate.get("loss_change"),
                dense_refinement_prediction_change=dense_gate.get("prediction_change"),
                dense_refinement_loss_change=dense_gate.get("loss_change"),
                min_kernel_eigenvalue=float(np.min(a["eigenmin"])),
                max_kernel_frobenius_error=float(np.max(kernel_difference)),
                max_kernel_error_over_initial_dense_norm=float(np.max(kernel_difference)/initial_kernel_norm),
                last_kernel_relative_error=float(kernel_difference[-1]/max(dense_kernel_norm[-1], 1e-300)),
                max_dense_kernel_change_over_initial_norm=float(np.max(np.linalg.norm(dense["kernel"]-dense["kernel"][0], axis=(1, 2)))/initial_kernel_norm),
                dense_activation_motion_max=float(np.max(dense["motion"])),
                dense_activation_motion_layer1=float(np.max(dense["motion"][:, 0])),
                dense_activation_motion_layer2=float(np.max(dense["motion"][:, 1])),
                dense_activation_motion_layer3=float(np.max(dense["motion"][:, 2])),
                error_ratio_to_frozen_full_horizon=ratio,
                relative_error_reduction_vs_frozen=1-ratio if ratio is not None else None,
                producer_nonlinear_improvement=producer.get("nonlinear_improvement"),
                moving_scalars=storage.get("state_scalars", c["dense_parameter_count"]),
                fixed_terminal_scalars=storage.get("terminal_scalars", 0),
                aggregate_scalars=storage.get("aggregate_scalars"),
                label_scalars=storage.get("label_scalars", c["M"]),
                engine_array_scalars=storage.get("engine_array_scalars"),
                stored_initial_scalars=storage.get("stored_initial_scalars"),
                dense_parameter_count=c["dense_parameter_count"],
                initializer_seconds=c["initialization_seconds"],
                latest_trajectory_seconds=record["compute_seconds"],
                all_resolutions_seconds=sum(r["compute_seconds"] for r in run["records"]),
                latest_dense_seconds=runs["dense"]["record"]["compute_seconds"],
                latest_speedup_vs_dense=runs["dense"]["record"]["compute_seconds"]/record["compute_seconds"],
                configuration_total_seconds=summary["total_seconds"],
                peak_process_rss_bytes=summary["peak_process_rss_bytes"],
            )
            rows.append(row)
            for horizon in (1., 8., 32., 128.):
                mask = times <= horizon
                prefixes.append(dict(case=c["case"], width=c["width"], seed=c["seed"], model=name,
                                     prefix_horizon=horizon, prefix_complete=bool(times[-1] >= horizon),
                                     last_compared_time=float(times[mask][-1]),
                                     max_sampled_output_rms_error=float(np.max(errors[mask])),
                                     max_sampled_absolute_loss_error=float(np.max(loss_errors[mask]))))
    return rows, prefixes, curve_checks


def csv_table(path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(clean(rows))


def configure_plotting():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.titleweight": "semibold", "axes.labelcolor": "#334155",
                         "text.color": "#172033", "axes.edgecolor": "#cbd5e1",
                         "xtick.color": "#475569", "ytick.color": "#475569",
                         "figure.facecolor": "white", "savefig.facecolor": "white",
                         "pdf.fonttype": 42, "ps.fonttype": 42})


def format_axis(ax, *, error=False):
    ax.set_xscale("symlog", linthresh=1.)
    ax.set_xlim(0., 128.)
    ax.set_xticks([0., 1., 8., 32., 128.], ["0", "1", "8", "32", "128"])
    ax.set_yscale("symlog", linthresh=1e-5 if error else 1e-4)
    ax.grid(True, which="major", alpha=.18)
    ax.set_xlabel("Physical training time")
    ax.set_ylabel("Training-output RMS error" if error else "Training loss (mean squared residual)")
    if error:
        ax.axhline(.1, color="#15966d", linewidth=.8, linestyle="--", alpha=.85, zorder=0)
        ax.axhline(.2, color="#c74141", linewidth=.8, linestyle="--", alpha=.85, zorder=0)
        ax.set_ylim(bottom=0.)
    else:
        ax.set_ylim(bottom=0.)


def draw_panel(ax, item, *, error=False, title=None):
    runs = item["runs"]
    dense = runs["dense"]["arrays"]
    stops = []
    for name in MODELS[1:] if error else MODELS:
        run = runs[name]
        a = run["arrays"]
        if error:
            ts, ys, _, _, _ = common_curves(a, dense)
        else:
            ts, ys = a["times"], a["loss"]
        ax.plot(ts, ys, color=COLORS[name], linestyle=STYLES[name],
                linewidth=2.0 if name in ("dense", "order4") else 1.6,
                label=LABELS[name], zorder=4 if name == "order4" else 3)
        if not full_run(run, item["config"]["end"]):
            ax.plot(ts[-1], ys[-1], "x", color=COLORS[name], markersize=8, markeredgewidth=2)
            stops.append(f"{name}: stopped at {run['record']['final_time']:.3g}")
    format_axis(ax, error=error)
    if title:
        ax.set_title(title, loc="left", fontsize=11, pad=10)
    if stops:
        ax.text(.98, .98, "\n".join(stops), transform=ax.transAxes, ha="right", va="top", fontsize=8,
                bbox=dict(facecolor="white", edgecolor="#e2e8f0", alpha=.9, pad=3))


def handles():
    return [Line2D([0], [0], color=COLORS[n], linestyle=STYLES[n], linewidth=2, label=LABELS[n]) for n in MODELS]


def save_figure(fig, stem, outputs):
    for suffix in ("png", "pdf"):
        path = stem.with_suffix("." + suffix)
        fig.savefig(path, dpi=180, bbox_inches="tight")
        outputs.append(path)
    plt.close(fig)


def figures(data, output):
    configure_plotting()
    outputs = []
    representatives = [next(d for d in data if d["config"]["case"] == case
                            and d["config"]["width"] == 256 and d["config"]["seed"] == SEEDS[0]) for case in CASES]
    fig, axs = plt.subplots(2, 2, figsize=(12., 8.2))
    for row, item in enumerate(representatives):
        label = CASE_LABELS[item["config"]["case"]]
        draw_panel(axs[row, 0], item, title=f"{label} · loss")
        draw_panel(axs[row, 1], item, error=True, title=f"{label} · output error against dense")
    fig.suptitle("Scalar-only dynamics against dense nonlinear training", fontsize=17, x=.08, ha="left", y=.995)
    fig.text(.08, .952, "Representative protocol configurations: width 256, seed 20260920 · common physical horizon 128", fontsize=10, color="#64748b")
    fig.legend(handles=handles(), loc="lower center", bbox_to_anchor=(.51, .025), ncol=4, frameon=False)
    fig.text(.08, .012, "Error is RMS over training samples at saved times. Dashed error thresholds: 0.1 / 0.2. Crosses mark incomplete curves.", fontsize=8, color="#64748b")
    fig.subplots_adjust(left=.085, right=.99, top=.875, bottom=.155, hspace=.40, wspace=.27)
    save_figure(fig, output / "scalar_aggregate_main", outputs)

    fig, axs = plt.subplots(4, 4, figsize=(17., 13.))
    for row, (case, width) in enumerate((c, w) for c in CASES for w in WIDTHS):
        for seed_index, seed in enumerate(SEEDS):
            item = next(d for d in data if (d["config"]["case"], d["config"]["width"], d["config"]["seed"]) == (case, width, seed))
            base = f"{CASE_LABELS[case]}\nn={width}, seed={seed}"
            draw_panel(axs[row, 2*seed_index], item, title=base + " · loss")
            draw_panel(axs[row, 2*seed_index+1], item, error=True, title=base + " · error")
            for ax in axs[row, 2*seed_index:2*seed_index+2]:
                ax.set_ylabel("Output RMS error" if ax is axs[row, 2*seed_index+1] else "Training loss")
                ax.tick_params(labelsize=8)
                ax.xaxis.label.set_size(9)
                ax.yaxis.label.set_size(9)
                ax.title.set_fontsize(9)
    fig.suptitle("All eight fixed configurations · matched-time loss and output error", fontsize=16, y=.995)
    fig.legend(handles=handles(), loc="lower center", bbox_to_anchor=(.51, .018), ncol=4, frameon=False)
    fig.text(.06, .006, "No failed tail is extrapolated. Errors cover only shared saved times; crosses and stop labels show incomplete trajectories.", fontsize=9, color="#64748b")
    fig.subplots_adjust(left=.06, right=.995, top=.93, bottom=.09, hspace=.72, wspace=.32)
    save_figure(fig, output / "scalar_aggregate_all_eight", outputs)

    fig, axs = plt.subplots(2, 2, figsize=(12., 8.2))
    for row, item in enumerate(representatives):
        dense = item["runs"]["dense"]["arrays"]
        initial_norm = np.linalg.norm(dense["kernel"][0])
        for name in MODELS:
            run = item["runs"][name]
            a = run["arrays"]
            if name != "dense":
                ts, _, _, ia, idense = common_curves(a, dense)
                values = np.linalg.norm(a["kernel"][ia]-dense["kernel"][idense], axis=(1, 2))/initial_norm
                axs[row, 0].plot(ts, values, color=COLORS[name], linestyle=STYLES[name], linewidth=1.8)
                if not full_run(run, item["config"]["end"]):
                    axs[row, 0].plot(ts[-1], values[-1], "x", color=COLORS[name], markersize=7)
            axs[row, 1].plot(a["times"], a["eigenmin"], color=COLORS[name], linestyle=STYLES[name], linewidth=1.8)
            if not full_run(run, item["config"]["end"]):
                axs[row, 1].plot(a["times"][-1], a["eigenmin"][-1], "x", color=COLORS[name], markersize=7)
        for ax in axs[row]:
            ax.set_xscale("symlog", linthresh=1.)
            ax.set_xlim(0., 128.)
            ax.set_xticks([0., 1., 8., 32., 128.], ["0", "1", "8", "32", "128"])
            ax.set_xlabel("Physical training time")
            ax.grid(True, alpha=.18)
        axs[row, 0].set_yscale("symlog", linthresh=1e-4)
        axs[row, 1].set_yscale("symlog", linthresh=1e-5)
        axs[row, 1].axhline(0., color="#94a3b8", linewidth=.8)
        label = CASE_LABELS[item["config"]["case"]]
        axs[row, 0].set_title(f"{label} · kernel discrepancy", loc="left")
        axs[row, 1].set_title(f"{label} · smallest kernel eigenvalue", loc="left")
        axs[row, 0].set_ylabel("Kernel error / initial dense kernel norm")
        axs[row, 1].set_ylabel("Smallest eigenvalue")
    fig.suptitle("Kernel diagnostics · width 256, seed 20260920", fontsize=16, y=.995)
    fig.legend(handles=handles(), loc="lower center", bbox_to_anchor=(.51, .025), ncol=4, frameon=False)
    fig.text(.08, .012, "Kernel discrepancy uses the Frobenius norm. Positive kernels can still produce inaccurate training trajectories.", fontsize=9, color="#64748b")
    fig.subplots_adjust(left=.085, right=.99, top=.91, bottom=.16, hspace=.4, wspace=.28)
    save_figure(fig, output / "scalar_aggregate_kernel_diagnostics", outputs)

    for item in data:
        c, runs, labels = item["config"], item["runs"], item["labels"]
        ncols = 2 if len(labels) == 4 else 4
        fig, axs = plt.subplots(2, ncols, figsize=(5*ncols, 6.5), squeeze=False)
        for a, ax in enumerate(axs.flat):
            for name in MODELS:
                run = runs[name]
                values = run["arrays"]
                ax.plot(values["times"], values["f"][:, a], color=COLORS[name], linestyle=STYLES[name],
                        linewidth=1.8 if name in ("dense", "order4") else 1.3)
                if not full_run(run, c["end"]):
                    ax.plot(values["times"][-1], values["f"][-1, a], "x", color=COLORS[name], markersize=7)
            ax.axhline(labels[a], color="#94a3b8", linewidth=.7, linestyle="--")
            ax.set_title(f"Sample {a+1} · label {labels[a]:+g}", loc="left")
            ax.set_xscale("symlog", linthresh=1.)
            ax.set_xlim(0., 128.)
            ax.set_xticks([0., 1., 8., 32., 128.], ["0", "1", "8", "32", "128"])
            ax.set_xlabel("Physical training time")
            ax.set_ylabel("Network output")
            ax.grid(True, alpha=.18)
        fig.suptitle(f"{CASE_LABELS[c['case']]} · every training output · n={c['width']}, seed={c['seed']}", fontsize=14, y=.995)
        incomplete = [f"{n}: {runs[n]['record']['status']} at t={runs[n]['record']['final_time']:.4g}" for n in MODELS if not full_run(runs[n], c["end"])]
        foot = "; ".join(incomplete) if incomplete else "All trajectories cover the declared horizon. Dashed horizontal lines show labels."
        fig.text(.06, .012, foot, fontsize=9, color="#64748b")
        fig.legend(handles=handles(), loc="lower center", bbox_to_anchor=(.5, .037), ncol=4, frameon=False)
        fig.subplots_adjust(left=.07, right=.995, top=.88, bottom=.20, hspace=.48, wspace=.28)
        stem = output / f"sample_outputs_{c['case']}_n{c['width']}_seed{c['seed']}"
        save_figure(fig, stem, outputs)
    return outputs


def number(x, digits=4):
    return "—" if x is None else f"{x:.{digits}g}"


def markdown_summary(rows, output, campaign):
    lines = ["# Scalar aggregate campaign: saved-output analysis", "",
             "All eight predeclared configurations are included. Errors are maxima over saved matched physical times, not certified continuous-time bounds. Incomplete trajectories retain only their observed prefix; they never count as full-horizon agreement.", "",
             "## Order-four results", "",
             "| Task | Width | Seed | Complete | Output RMS error | Loss error | Error / frozen | Numerical gates | Absolute verdict | Nonlinear gain gate |",
             "|---|---:|---:|:---:|---:|---:|---:|:---:|---|:---:|"]
    for r in rows:
        if r["model"] == "order4":
            lines.append(f"| {r['case']} | {r['width']} | {r['seed']} | {r['full_horizon_complete']} | {number(r['max_sampled_output_rms_error'])} | {number(r['max_sampled_absolute_loss_error'])} | {number(r['error_ratio_to_frozen_full_horizon'])} | {r['validity_pass']} | {r['producer_verdict']} | {r['producer_nonlinear_improvement']} |")
    lines.extend(["", "Absolute agreement requires output error ≤0.1 and loss error ≤0.05, complete trajectories and passed numerical gates. An adverse error is output error >0.2 or loss error >0.1 on a complete valid comparison; reproduced state escape or solver failure is also adverse. Other outcomes are inconclusive.", "",
                  "The separate nonlinear-gain gate requires order-four output error ≤ half the frozen-kernel error, frozen error ≥0.05, dense hidden-activation RMS motion ≥0.1, completeness and numerical validity. Passing that relative gate does not imply absolute agreement.", "",
                  "## Storage and measured cost", "",
                  "| Task | Width | Seed | Dense moving scalars | Order-four moving | Order-four terminal | Initializer seconds | Dense seconds | Order-four seconds |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|"])
    for r in rows:
        if r["model"] == "order4":
            lines.append(f"| {r['case']} | {r['width']} | {r['seed']} | {r['dense_parameter_count']} | {r['moving_scalars']} | {r['fixed_terminal_scalars']} | {number(r['initializer_seconds'])} | {number(r['latest_dense_seconds'])} | {number(r['latest_trajectory_seconds'])} |")
    lines.extend(["", "Times in this table are initialization and the latest trajectory resolution separately. Every resolution's total is retained in the CSV. Failed trajectories have shorter measured runtimes and therefore are not valid full-horizon speed comparisons. Labels and solver workspace are additional to the aggregate counts. Initialization uses the original dense network once; scalar evolution contains zero neuron or network-parameter coordinates.", "",
                  f"Recorded primary campaign wall time: {campaign['seconds']:.3f} seconds. This analysis performs no new integrations or coefficient fitting.", "",
                  "## Artifacts", "", "- `scalar_aggregate_main.png` / `.pdf`: two fixed representative configurations.",
                  "- `scalar_aggregate_all_eight.png` / `.pdf`: every configuration.",
                  "- `scalar_aggregate_kernel_diagnostics.png` / `.pdf`: representative kernel errors and eigenvalues.",
                  "- `sample_outputs_*.png` / `.pdf`: every training sample's output in every configuration.",
                  "- `summary.csv` / `.json`: all four models, exact reported gates, endpoint coverage, scalar counts and timings.",
                  "- `prefix_errors.csv`: fixed horizons 1, 8, 32 and 128, with explicit coverage flags.",
                  "- `input_manifest.json`: hashes of the inputs actually used and the analyzer source.", ""])
    (output / "ANALYSIS.md").write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    started = time.perf_counter()
    directory, output = args.input.resolve(), args.output.resolve()
    if output.exists():
        raise FileExistsError("Analysis outputs are immutable; select a fresh output directory")
    data, campaign, inputs = load_campaign(directory)
    rows, prefixes, checks = tables(data)
    output.mkdir(parents=True, exist_ok=False)
    csv_table(output / "summary.csv", rows)
    csv_table(output / "prefix_errors.csv", prefixes)
    write_json(output / "summary.json", dict(rows=rows, prefixes=prefixes, curve_checks=checks,
                                             producer_campaign_seconds=campaign["seconds"],
                                             metrics="saved matched times; RMS across training samples"))
    markdown_summary(rows, output, campaign)
    generated = figures(data, output)
    source = Path(__file__).resolve()
    shutil.copy2(source, output / source.name)
    inputs.add(source)
    write_json(output / "input_manifest.json", dict(
        input_directory=str(directory), analysis_seconds=time.perf_counter()-started,
        source_hashes={str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(inputs)},
        figures=[p.name for p in generated], independent_curve_checks=len(checks),
        all_configurations=8, new_simulations=0))
    print(json.dumps(dict(output=str(output), configurations=len(data), rows=len(rows),
                          figures=len(generated), seconds=time.perf_counter()-started)))


if __name__ == "__main__":
    main()
