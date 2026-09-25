"""Read-only scoring and figures for the width-2048 matched-loss campaign.

Recompute metrics from saved arrays. No training, coefficient initialization,
dense-network evaluation, or GPU operation is performed by this analyzer.
"""

import argparse
import csv
import json
from pathlib import Path
import shutil
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from analyze_scalar_long_time import (Inputs, digest, nested, rate_diagnostics,
    replay_probe_gap, rms, scalar, spatial_metrics, spectral_checks)


HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/"data/generated/neural_response_memory_20260922"
TARGET = 1e-6
BLACK, PURPLE, GRAY = "#171717", "#7135a8", "#81858b"
HARD_REPRO = "quadrant_alternating_n2048_seed20260920"


class SavedInputs(Inputs):
    def track(self, path):
        path = Path(path)
        key = str(path.resolve())
        if key not in self.hashes:
            self.hashes[key] = digest(path)
        return path

    def trajectory(self, path, model):
        keep = {"time", "times", "losses", "grid", "off_grid", "train_f", "train_probe",
                "grid_angles", "off_grid_angles", "integration_wall_times", "local_error_ratios",
                "train_inputs", "train_labels"}
        if model == "order4":
            keep.update(("state", "segment_times", "segment_states", "segment_training",
                         "milestone_grids", "milestone_states", "milestone_segments"))
        with np.load(self.track(path), allow_pickle=False) as values:
            return {key: values[key] for key in values.files if key in keep}


def read_run(reader, folder, model, initial, original_probe):
    record = reader.json(folder/"result.json")
    path = folder/"trajectory_spatial_refined.npz"
    if not path.exists():
        path = folder/"trajectory.npz"
    run = reader.trajectory(path, model)
    if model == "order4":
        if not record["from_zero"]:
            raise ValueError("wide scalar runs must start from original initialization")
        probe = replay_probe_gap(initial, original_probe, run, record, None)
    else:
        probe = {"passed": True, "peak_training_probe_gap": 0.}
    if run["train_f"].shape != initial["labels"].shape:
        raise ValueError("training sample shape mismatch")
    return dict(folder=folder, arrays=run, record=record, probe=probe,
                raw_loss=float(np.mean((run["train_f"]-initial["labels"])**2)))


def compare_runs(first, second, discrepancy):
    a, b = nested(first["arrays"]["grid"], second["arrays"]["grid"])
    change = rms(a-b)
    dt = abs(float(first["arrays"]["time"])-float(second["arrays"]["time"]))/max(1., float(second["arrays"]["time"]))
    fitted = first["record"]["status"] == second["record"]["status"] == "fitted"
    raw_fit = max(first["raw_loss"], second["raw_loss"]) <= TARGET*(1+1e-6)
    return dict(numerical_change=change, time_relative_change=dt, fitted_statuses=fitted,
                raw_loss_target_pass=raw_fit,
                probe_peak=max(first["probe"]["peak_training_probe_gap"], second["probe"]["peak_training_probe_gap"]),
                passed=bool(fitted and raw_fit and change <= .002 and change <= .1*max(discrepancy, 1e-6)
                            and dt <= .001 and first["probe"]["passed"] and second["probe"]["passed"]))


def coefficient_reproduction(first, second):
    result = {}
    for key in ("f", "Theta", "C", "Q"):
        difference = float(np.max(abs(first[key]-second[key])))
        bound = 1e-11+1e-9*float(np.max(abs(first[key])))
        result[key] = dict(maximum_difference=difference, bound=bound,
                           bitwise_equal=bool(np.array_equal(first[key], second[key])), passed=difference <= bound)
    return result


def verdict(fitted, valid, error):
    if not fitted:
        return "no_matched_endpoint"
    if not valid:
        return "numerically_inconclusive"
    return "agreement" if error <= .1 else "adverse" if error > .2 else "inconclusive"


def analyze_case(reader, source, directory, reproduction_source, reproduction):
    config = reader.json(source/"configuration.json")
    initialization = reader.json(source/"initialization.json")
    if config["width"] != 2048:
        raise ValueError("this analysis requires the declared width2048")
    initial = reader.arrays(source/"initial_coefficients.npz")
    original_probe = reader.arrays(source/"probe_coefficients.npz")
    probe = (reader.arrays(directory/"probe_coefficients_refined.npz")
             if (directory/"probe_coefficients_refined.npz").exists() else original_probe)
    families = {}
    for model in ("dense", "order4"):
        folders = sorted((p for p in directory.glob(model+"_resolution*") if p.is_dir() and (p/"result.json").exists()),
                         key=lambda p:int(p.name.split("resolution")[-1]))
        if len(folders) < 2:
            raise ValueError("two completed resolutions required: "+source.name+"/"+model)
        families[model] = [read_run(reader, p, model, initial, original_probe) for p in folders]
    dense, candidate = families["dense"][-1], families["order4"][-1]
    dense_arrays, candidate_arrays = dense["arrays"], candidate["arrays"]
    a, b = nested(candidate_arrays["grid"], dense_arrays["grid"])
    discrepancy = rms(a-b)
    gates = {model:compare_runs(runs[-2], runs[-1], discrepancy) for model, runs in families.items()}
    spatial = spatial_metrics(candidate_arrays, probe, dense_arrays)
    device_checks = []
    for run in families["dense"]:
        record = run["record"]
        check = dict(device=record.get("device"), dtype=record.get("dtype"),
                     width=record.get("width"),
                     initialization_hash_matches=record.get("initialization_hash") == initialization["initialization_hash"],
                     inputs_match=bool(np.array_equal(run["arrays"]["train_inputs"], initial["inputs"])),
                     labels_match=bool(np.array_equal(run["arrays"]["train_labels"], initial["labels"])),
                     deterministic_algorithms=record.get("deterministic_algorithms"), tf32=record.get("tf32"))
        check["passed"] = (str(check["device"]).startswith("cuda") and check["dtype"] == "float64"
                           and check["width"] == 2048 and check["inputs_match"] and check["labels_match"]
                           and check["initialization_hash_matches"] and check["deterministic_algorithms"] is True
                           and check["tf32"] is False and record.get("resource_limits_satisfied", False))
        device_checks.append(check)
    repeated = {}
    reproduction_pass = source.name != HARD_REPRO
    if source.name == HARD_REPRO:
        if reproduction_source is None or reproduction is None:
            raise ValueError("mandatory hard-case reproduction paths are required")
        repeated_initial = reader.arrays(reproduction_source/"initial_coefficients.npz")
        repeated_probe = reader.arrays(reproduction_source/"probe_coefficients.npz")
        repeated_receipt = reader.json(reproduction_source/"initialization.json")
        repeated["training_coefficients"] = coefficient_reproduction(initial, repeated_initial)
        repeated["probe_coefficients"] = coefficient_reproduction(original_probe, repeated_probe)
        repeated["initialization_hash_matches"] = initialization["initialization_hash"] == repeated_receipt["initialization_hash"]
        for model in ("dense", "order4"):
            other = read_run(reader, reproduction/model, model, repeated_initial, repeated_probe)
            repeated[model] = dict(comparison=compare_runs(families[model][-1], other, discrepancy),
                                   probe=other["probe"], status=other["record"]["status"], raw_loss=other["raw_loss"])
        reproduction_pass = (repeated["initialization_hash_matches"]
            and all(entry["passed"] for kind in ("training_coefficients", "probe_coefficients") for entry in repeated[kind].values())
            and all(repeated[model]["comparison"]["passed"] for model in ("dense", "order4")))
    fitted = dense["record"]["status"] == candidate["record"]["status"] == "fitted"
    direct_valid = (all(g["passed"] for g in gates.values()) and spatial["quadrature_pass"]
                    and all(c["passed"] for c in device_checks) and reproduction_pass)
    encoded_valid = direct_valid and spatial["fourier_pass"]
    control = reader.arrays(directory/"order2_spectral.npz")
    control_spatial = spatial_metrics(control, probe, dense_arrays)
    control_spectral, spectrum = spectral_checks(initial, control, probe)
    control_fitted = str(control["status"].item()) == "fitted" and dense["record"]["status"] == "fitted"
    control_valid = (control_spectral["passed"] and control_spatial["quadrature_pass"]
                     and control_spatial["fourier_pass"] and all(c["passed"] for c in device_checks))
    # Verify the dense refinement gate at the control's own discrepancy scale.
    control_dense_gate = compare_runs(*families["dense"][-2:], control_spatial["circle_rms"])
    control_valid = control_valid and control_dense_gate["passed"]
    rates = rate_diagnostics(reader, candidate["folder"], candidate_arrays, initial["labels"])
    rates["interpretation"] = "L'/L=-(4/M)*effective_rate, with M="+str(len(initial["labels"]))+". Negative rate means instantaneous loss growth."
    dense_time, candidate_time = float(dense_arrays["time"]), float(candidate_arrays["time"])
    candidate_seconds = candidate["record"]["seconds"]
    dense_seconds = dense["record"]["integration_seconds"]
    m = len(initial["labels"])
    record = dict(configuration=source.name, case=config["case"], width=config["width"], seed=config["seed"], samples=m,
        initializer=dict(coefficient_seconds=initialization["coefficient_seconds"],
                         total_preparation_seconds=initialization["seconds"],
                         peak_rss_bytes=initialization["peak_rss_bytes"],
                         legacy_four_probe_check=initialization["initialization_oracle"]),
        dense=dict(status=dense["record"]["status"], loss=dense["raw_loss"], time=dense_time,
                   wall_seconds=dense_seconds, total_work_seconds=dense["record"]["total_work_seconds"],
                   cpu_process_seconds=dense["record"].get("integration_cpu_process_seconds"),
                   cuda_timeline_seconds=dense["record"].get("integration_cuda_event_interval_seconds"),
                   cuda_timeline_note="Device timeline interval includes host submission gaps; it is not kernel-only time.",
                   device=dense["record"]["device"], device_name=dense["record"]["device_name"],
                   peak_cuda_allocated_bytes=dense["record"]["peak_cuda_allocated_bytes"],
                   moving_state_bytes=dense["record"]["moving_state_bytes"],
                   accepted_steps=dense["record"]["accepted"], rtol=dense["record"]["rtol"]),
        order4=dict(status=candidate["record"]["status"], loss=candidate["raw_loss"], time=candidate_time,
                    time_ratio_to_dense=candidate_time/dense_time,
                    wall_seconds=candidate_seconds, wall_scope="CPU scalar run, including endpoint transport and saving",
                    initialization_plus_run_seconds=initialization["coefficient_seconds"]+candidate_seconds,
                    scalar_cpu_run_to_dense_gpu_wall_ratio=candidate_seconds/dense_seconds,
                    rtol=candidate["record"]["rtol"], accepted_steps=candidate["record"]["accepted_steps"],
                    nfev=candidate["record"]["nfev"], segments=candidate["record"]["segments"],
                    moving_state_scalars=2*(m+m*m+m**3), initialized_training_scalars=sum(m**k for k in range(1, 5)),
                    spatial=spatial, probe=candidate["probe"], rates=rates,
                    direct_grid_qualified=bool(direct_valid), encoded_qualified=bool(encoded_valid),
                    direct_grid_verdict=verdict(fitted, direct_valid, discrepancy),
                    verdict=verdict(fitted, encoded_valid, discrepancy)),
        order2=dict(status=str(control["status"].item()), time=float(control["time"]),
                    time_ratio_to_dense=float(control["time"])/dense_time,
                    loss=float(np.mean((control["train_f"]-initial["labels"])**2)),
                    wall_seconds=None, wall_scope="Analytic spectral evaluation; elapsed evaluation time not recorded",
                    spatial=control_spatial, spectral=control_spectral, dense_gate=control_dense_gate,
                    verdict=verdict(control_fitted, control_valid, control_spatial["circle_rms"])),
        refinement=gates, dense_device_checks=device_checks, reproduction=repeated,
        reproduction_pass=bool(reproduction_pass),
        resolution_records={model:[run["record"] for run in runs] for model, runs in families.items()},
        resolution_probe_checks={model:[run["probe"] for run in runs] for model, runs in families.items()})
    summary = reader.json(directory/"summary.json")
    record["summary_crosscheck"] = dict(verdict_matches=record["order4"]["verdict"] == summary["verdict"],
        circle_rms_difference=abs(discrepancy-summary["spatial"]["circle_rms"]),
        dense_refinement_difference=abs(gates["dense"]["numerical_change"]-summary["gates"]["dense"]["numerical_change"]),
        scalar_refinement_difference=abs(gates["order4"]["numerical_change"]-summary["gates"]["order4"]["numerical_change"]))
    plot = dict(dense=dense_arrays, order4=candidate_arrays, order2=control,
                inputs=initial["inputs"], labels=initial["labels"], spectrum=spectrum)
    return record, plot


def finish_figure(figure, axes, output, stem, title, subtitle):
    handles, labels = [], []
    for axis in np.asarray(axes).flat:
        for handle, label in zip(*axis.get_legend_handles_labels()):
            if label not in labels:
                handles.append(handle); labels.append(label)
    figure.suptitle(title, x=.07, y=.985, ha="left", fontsize=16, fontweight="bold")
    short = figure.get_size_inches()[1] < 6
    figure.text(.07, .912 if short else .947, subtitle, ha="left", fontsize=9.2, color="#444444")
    if handles:
        figure.legend(handles, labels, loc="lower center", ncol=min(4, len(labels)), frameon=False, fontsize=9)
    figure.tight_layout(rect=(.01, .065, 1., .85 if short else .922), h_pad=2.3, w_pad=2.)
    for suffix in ("png", "pdf"):
        figure.savefig(output/(stem+"."+suffix), bbox_inches="tight")
    plt.close(figure)


def figures(output, records, plots):
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":10,
        "axes.spines.top":False, "axes.spines.right":False, "axes.titlesize":11,
        "savefig.dpi":220, "pdf.fonttype":42})
    loss_figure, loss_axes = plt.subplots(2, 2, figsize=(12.4, 8.6), sharey=True)
    circle_figure, circle_axes = plt.subplots(2, 2, figsize=(12.4, 8.6), sharex=True)
    upper_loss = max(10., 3*max(float(np.max(p["order4"]["losses"])) for p in plots))
    for record, plot, axis, circle_axis in zip(records, plots, loss_axes.flat, circle_axes.flat):
        title = ("Four inputs" if record["samples"] == 4 else "Eight inputs")+" · seed "+str(record["seed"])
        for model, color, label in (("dense", BLACK, "Dense GPU"), ("order4", PURPLE, "Scalar order four")):
            values = plot[model]
            axis.plot(values["times"], values["losses"], color=color, linewidth=1.7, label=label)
        horizon = max(float(plot[model]["time"]) for model in ("dense", "order4", "order2"))
        stop = float(plot["order2"]["time"])
        times = np.concatenate(([0.], np.geomspace(.01, max(.02, stop), 600)))
        eig, components = plot["spectrum"]
        analytic_loss = np.exp(-4/record["samples"]*np.outer(times, eig)) @ (components**2)/record["samples"]
        axis.plot(times, analytic_loss, color=GRAY, linestyle="--", linewidth=1.4, label="Frozen kernel (analytic)")
        axis.axhline(TARGET, color="#b2652f", linestyle=":", linewidth=1., label="Target MSE")
        axis.set_xscale("symlog", linthresh=1.)
        axis.set_yscale("log")
        axis.set_xlim(0., 1.15*horizon); axis.set_ylim(4e-7, upper_loss)
        ticks = [0., 1.]+[10.**k for k in range(2, 11, 2) if 10.**k <= 1.15*horizon]
        axis.set_xticks(ticks)
        axis.set_xlabel("Physical training time"); axis.set_ylabel("Training mean squared error")
        axis.set_title(title); axis.grid(True, which="major", alpha=.14)
        text = "Scalar: {} · t = {:.4g}\n{:.3g}× dense physical time".format(
            record["order4"]["status"].replace("_", " "), record["order4"]["time"], record["order4"]["time_ratio_to_dense"])
        axis.text(.03, .97, text, transform=axis.transAxes, va="top", fontsize=8.4,
                  bbox=dict(facecolor="white", alpha=.88, edgecolor="none"))
        inset = None
        if record["case"] == "quadrant_alternating":
            circle_axis.axvspan(10., 80., color="#c9d9eb", alpha=.22, zorder=0)
            if max(np.max(abs(plot[k]["grid"])) for k in ("order4", "order2")) > 4*max(1., np.max(abs(plot["dense"]["grid"]))):
                inset = circle_axis.inset_axes([.59, .065, .37, .27])
        for model, color, label in (("dense", BLACK, "Dense GPU"), ("order4", PURPLE, "Scalar order four (direct grid)"),
                                    ("order2", GRAY, "Frozen kernel")):
            if record[model]["status"] != "fitted":
                continue
            values = plot[model]["grid"]
            angles = np.linspace(0., 360., len(values)+1)
            values = np.concatenate((values, values[:1]))
            style = "--" if model == "order2" else "-"
            circle_axis.plot(angles, values, color=color, linestyle=style, linewidth=1.6, label=label)
            if inset is not None:
                inset.plot(angles, values, color=color, linestyle=style, linewidth=1.)
        angles = np.rad2deg(np.arctan2(plot["inputs"][:, 1], plot["inputs"][:, 0])) % 360
        circle_axis.scatter(angles, plot["labels"], s=23, facecolor="white", edgecolor=BLACK,
                            linewidth=.9, zorder=4, label="Training labels")
        if inset is not None:
            inset.scatter(angles, plot["labels"], s=10, facecolor="white", edgecolor=BLACK, linewidth=.7, zorder=4)
            inset.set_xlim(0., 90.); inset.set_ylim(-1.6, 1.6)
            inset.set_xticks((0, 45, 90)); inset.set_yticks((-1, 0, 1)); inset.tick_params(labelsize=6.5, length=2)
            inset.set_title("Training arc (expanded)", fontsize=7, pad=2)
        circle_axis.set_xlim(0., 360.); circle_axis.set_xticks((0, 90, 180, 270, 360))
        circle_axis.margins(y=.18)
        circle_axis.set_xlabel("Circle angle (degrees)"); circle_axis.set_ylabel("Prediction")
        circle_axis.set_title(title); circle_axis.grid(True, alpha=.14)
        text = "Direct-grid RMS: {:.4g} · {}\nFourier encoding: {}".format(
            record["order4"]["spatial"]["circle_rms"], record["order4"]["direct_grid_verdict"].replace("_", " "),
            "passed" if record["order4"]["spatial"]["fourier_pass"] else "unresolved")
        circle_axis.text(.03, .97, text, transform=circle_axis.transAxes, va="top", fontsize=8.4,
                         bbox=dict(facecolor="white", alpha=.9, edgecolor="none"))
    finish_figure(loss_figure, loss_axes, output, "wide_training_loss", "Width 2048: fitting at each model’s own training time",
                  "Dense reference runs use a GPU. Physical time is distinct from runtime; curves end at their recorded fit or cap.")
    finish_figure(circle_figure, circle_axes, output, "wide_matched_circle_functions", "Width 2048: learned circle functions at matched training loss",
                  "Only fitted endpoints are drawn. Direct-grid validity and the stricter Fourier encoding check are reported separately.")
    timing, axes = plt.subplots(1, 2, figsize=(12.4, 5.2))
    x = np.arange(len(records))
    labels = [("4 inputs" if r["samples"] == 4 else "8 inputs")+"\nseed "+str(r["seed"])[-2:] for r in records]
    init = np.array([r["initializer"]["coefficient_seconds"] for r in records])
    scalar_run = np.array([r["order4"]["wall_seconds"] for r in records])
    dense_run = np.array([r["dense"]["wall_seconds"] for r in records])
    axes[0].bar(x-.19, init, .36, color="#c9b1de", label="CPU coefficient initialization")
    axes[0].bar(x-.19, scalar_run, .36, bottom=init, color=PURPLE, label="CPU scalar run")
    axes[0].bar(x+.19, dense_run, .36, color=BLACK, label="GPU dense integration")
    axes[0].set_ylabel("Recorded wall seconds"); axes[0].set_title("Preparation and selected fine run")
    axes[1].bar(x-.19, scalar_run, .36, color=PURPLE, label="CPU scalar run")
    axes[1].bar(x+.19, dense_run, .36, color=BLACK, label="GPU dense integration")
    axes[1].set_yscale("log"); axes[1].set_ylabel("Recorded wall seconds (log scale)")
    axes[1].set_title("Integration / run timing without initialization")
    for axis in axes:
        axis.set_xticks(x, labels); axis.grid(True, axis="y", alpha=.14); axis.set_axisbelow(True)
    finish_figure(timing, axes, output, "wide_computational_cost", "Width 2048: preparation cost and training runtime",
                  "Different hardware is labeled explicitly. CPU scalar timing includes readout/saving; GPU timing measures integration.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DATA/"scalar_wide_source01")
    parser.add_argument("--campaign", type=Path, default=DATA/"scalar_wide_primary01")
    parser.add_argument("--reproduction-source", type=Path, default=DATA/"scalar_wide_source_reproduction01"/HARD_REPRO)
    parser.add_argument("--reproduction", type=Path, default=DATA/"scalar_wide_reproduction01"/HARD_REPRO)
    parser.add_argument("--output", type=Path, default=DATA/"scalar_wide_analysis01")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    sources = sorted(args.source.glob("*_n2048_seed*"))
    if len(sources) != 4 or any(not (args.campaign/p.name/"summary.json").exists() for p in sources):
        raise RuntimeError("wait for all four configuration scores before analysis")
    if any(not (args.reproduction/model/"result.json").exists() for model in ("dense", "order4")):
        raise RuntimeError("wait for mandatory complete reproduction before analysis")
    args.output.mkdir(parents=True, exist_ok=args.overwrite)
    reader, records, plots = SavedInputs(), [], []
    for name in ("SCALAR_WIDE_PROTOCOL.md", "scalar_wide_initialization.py", "scalar_wide_dense.py",
                 "run_scalar_wide.py", "scalar_long_time_engine.py", "analyze_scalar_long_time.py"):
        reader.track(HERE/name)
    for source in sources:
        record, plot = analyze_case(reader, source, args.campaign/source.name,
                                    args.reproduction_source if source.name == HARD_REPRO else None,
                                    args.reproduction if source.name == HARD_REPRO else None)
        records.append(record); plots.append(plot)
    report = dict(width=2048, target=TARGET, configurations=records,
                  measurement_notes=["Physical time is distinct from wall time.",
                    "Coefficient initialization uses CPU BLAS; dense integration uses GPU; scalar integration uses CPU.",
                    "Scalar run time includes endpoint transport and saving, while dense integration time excludes final readout and saving.",
                    "Fourier encoding validity is separate from fitted status and direct-grid numerical validity."],
                  research_computation_performed=False)
    (args.output/"analysis.json").write_text(json.dumps(report, indent=2, default=scalar)+"\n")
    fields = ("configuration", "case", "width", "seed", "samples", "model", "status", "loss", "time",
              "time_ratio_to_dense", "wall_seconds", "initializer_seconds", "circle_rms", "relative_rms", "maximum_error",
              "direct_grid_verdict", "encoded_verdict", "fourier_pass", "dense_refinement_change", "scalar_refinement_change")
    with (args.output/"endpoints.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields); writer.writeheader()
        for record in records:
            for model in ("dense", "order4", "order2"):
                own = record[model]
                row = {key:record[key] for key in ("configuration", "case", "width", "seed", "samples")}
                row.update(model=model, **{key:own.get(key, "") for key in ("status", "loss", "time", "time_ratio_to_dense", "wall_seconds")})
                row.update(initializer_seconds=record["initializer"]["coefficient_seconds"] if model != "dense" else "",
                    **{key:own.get("spatial", {}).get(key, "") for key in ("circle_rms", "relative_rms", "maximum_error", "fourier_pass")},
                    direct_grid_verdict=own.get("direct_grid_verdict", ""), encoded_verdict=own.get("verdict", ""),
                    dense_refinement_change=record["refinement"]["dense"]["numerical_change"],
                    scalar_refinement_change=record["refinement"]["order4"]["numerical_change"])
                writer.writerow(row)
    figures(args.output, records, plots)
    shutil.copy2(Path(__file__), args.output/Path(__file__).name)
    manifest = dict(command=sys.argv, source_sha256=digest(Path(__file__)), inputs=reader.hashes,
                    outputs={p.name:digest(p) for p in sorted(args.output.iterdir()) if p.is_file() and p.name != "manifest.json"})
    (args.output/"manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    print(json.dumps({r["configuration"]:{key:r["order4"][key] for key in
        ("status", "time", "time_ratio_to_dense", "direct_grid_verdict", "verdict")} for r in records}, indent=2))


if __name__ == "__main__":
    main()
