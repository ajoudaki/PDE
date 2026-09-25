"""Independently score saved long-time scalar runs and render static figures.

No training integration or dense-network evaluation is performed. The only
replay transports eight passive training-probe anchors through saved scalar
segments, to verify the full accumulated probe consistency error.
"""

import argparse
import csv
import hashlib
import json
from pathlib import Path
import shutil
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from scalar_long_time_engine import StiffSignatureHierarchy, recenter_coefficients


STUDY = Path(__file__).resolve().parent
DATA = STUDY.parents[1] / "data/generated/neural_response_memory_20260922"
TARGET = 1e-6
PURPLE, BLACK, GRAY = "#7135a8", "#171717", "#81858b"
NAMES = ("f", "Theta", "C", "Q")


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


class Inputs:
    def __init__(self):
        self.hashes = {}

    def track(self, path):
        path = Path(path)
        self.hashes[str(path.resolve())] = digest(path)
        return path

    def arrays(self, path):
        with np.load(self.track(path), allow_pickle=False) as values:
            return {name: values[name] for name in values.files}

    def json(self, path):
        return json.loads(self.track(path).read_text())


def scalar(value):
    return value.item() if isinstance(value, np.generic) else value


def rms(value):
    value = np.asarray(value, dtype=np.longdouble)
    return float(np.sqrt(np.mean(value * value)))


def nested(*grids):
    count = min(map(len, grids))
    if any(len(grid) % count for grid in grids):
        raise ValueError("comparison grids must be nested")
    return [np.asarray(grid)[::len(grid)//count] for grid in grids]


def spatial_metrics(values, probe, dense):
    grid, target = nested(values["grid"], dense["grid"])
    difference = grid-target
    error = rms(difference)
    quadrature_change = abs(error-rms(difference[::2]))
    n = len(values["grid"])
    angles = 2*np.pi*np.arange(n)/n
    off_angles = np.asarray(probe["off_angles"])
    fourier = []
    for degree in (64, 128, 256):
        modes = np.fft.rfft(values["grid"])[:degree+1]/n
        def evaluate(points):
            return modes[0].real + 2*np.real(np.exp(1j*np.outer(points, np.arange(1, len(modes)))) @ modes[1:])
        grid_error = evaluate(angles)-values["grid"]
        off_error = evaluate(off_angles)-values["off_grid"]
        check = dict(mode=degree, grid_rms=rms(grid_error), off_grid_rms=rms(off_error),
                     maximum=float(max(np.max(abs(grid_error)), np.max(abs(off_error)))))
        check["passed"] = max(check["grid_rms"], check["off_grid_rms"]) <= 1e-5 and check["maximum"] <= 1e-4
        fourier.append(check)
        if check["passed"]:
            break
    return dict(circle_rms=error, relative_rms=error/max(rms(target), 1e-300),
                maximum_error=float(np.max(abs(difference))),
                dense_function_rms=rms(target), quadrature_change=quadrature_change,
                quadrature_pass=quadrature_change <= .001 and quadrature_change <= .01*max(error, 1e-6),
                fourier=fourier, fourier_pass=fourier[-1]["passed"])


def replay_probe_gap(initial, original_probe, run, record, prefix):
    """Check all segment boundaries using only the eight passive training probes."""
    m = len(initial["labels"])
    model = StiffSignatureHierarchy(initial, initial["labels"], 4)
    passive = {key: original_probe[key][-m:].copy() for key in NAMES}
    if not record["from_zero"]:
        passive = recenter_coefficients(passive, model.signatures(prefix["state"]))
        start_f = prefix["state"][:m]
    else:
        start_f = initial["f"]
    peak = rms(passive["f"]-start_f)
    kernel_peak = c_peak = 0.
    for state in run["segment_states"]:
        passive = recenter_coefficients(passive, model.signatures(state))
        fields = model.training.tensors(model.training_state(state))
        peak = max(peak, rms(passive["f"]-fields["f"]))
        kernel_peak = max(kernel_peak, rms(passive["Theta"]-fields["Theta"]))
        c_peak = max(c_peak, rms(passive["C"]-fields["C"]))
    return dict(peak_training_probe_gap=peak, final_training_probe_gap=rms(run["train_probe"]-run["train_f"]),
                replay_vs_saved_probe=rms(passive["f"]-run["train_probe"]),
                peak_passive_kernel_gap=kernel_peak, peak_passive_C_gap=c_peak,
                passed=peak <= 1e-4)


def pair_metrics(first, second, first_record, second_record, first_probe, second_probe, dense):
    a, b, reference = nested(first["grid"], second["grid"], dense["grid"])
    error, change = rms(b-reference), rms(a-b)
    time_change = abs(float(first["time"])-float(second["time"]))/max(1., float(second["time"]))
    return dict(circle_rms=error, numerical_change=change, time_relative_change=time_change,
                passed=(first_record["status"] == second_record["status"] == "fitted"
                        and change <= .002 and change <= .1*max(error, 1e-6)
                        and time_change <= .001 and first_probe["passed"] and second_probe["passed"]))


def spectral_checks(initial, baseline, probe):
    """Recompute spectral predictions and their integral from initialized scalars."""
    theta = initial["Theta"]
    values, vectors = np.linalg.eigh(theta)
    alpha = 2/len(initial["labels"])
    components = vectors.T @ (initial["f"]-initial["labels"])
    time = float(baseline["time"])
    exponent = -alpha*values*time
    quotient = np.empty_like(values)
    nonzero = values != 0
    quotient[nonzero] = np.expm1(exponent[nonzero])/values[nonzero]
    quotient[~nonzero] = -alpha*time
    prediction = initial["labels"]+vectors @ (np.exp(exponent)*components)
    integral = vectors @ (quotient*components)
    own_probe = np.asarray(probe["f"], dtype=np.longdouble) + np.asarray(probe["Theta"], dtype=np.longdouble) @ np.asarray(integral, dtype=np.longdouble)
    count = len(baseline["grid"])
    checks = dict(eigen_residual=float(np.max(abs(theta@vectors-vectors*values))),
        orthogonality_residual=float(np.max(abs(vectors.T@vectors-np.eye(len(values))))),
        training_prediction_difference=rms(prediction-baseline["train_f"]),
        integral_difference=rms(integral-baseline["z"]),
        integral_identity_residual=rms(initial["f"]+theta@baseline["z"]-baseline["train_f"]),
        training_probe_gap=rms(baseline["train_probe"]-baseline["train_f"]),
        passive_grid_difference=rms(own_probe[:count]-baseline["grid"]))
    checks["passed"] = (checks["eigen_residual"] <= 1e-10*max(1., np.max(abs(theta)))
                         and checks["orthogonality_residual"] <= 1e-10
                         and checks["training_prediction_difference"] <= 1e-8
                         and checks["integral_identity_residual"] <= 1e-4
                         and checks["training_probe_gap"] <= 1e-4
                         and checks["passive_grid_difference"] <= 1e-6)
    return checks, (values, components)


def load_run(inputs, directory, initial, original_probe, source):
    record = inputs.json(directory/"result.json")
    path = directory/"trajectory_spatial_refined.npz"
    if not path.exists():
        path = directory/"trajectory.npz"
    run = inputs.arrays(path)
    prefix = None if record["from_zero"] else inputs.arrays(source/("order4_resolution"+str(record["start_level"])+".npz"))
    probe_gate = replay_probe_gap(initial, original_probe, run, record, prefix)
    return run, record, probe_gate


def rate_diagnostics(inputs, directory, run, labels):
    """Recompute rates from stored training fields, rather than milestone scores."""
    times = inputs.json(directory/"milestones.json")
    m = len(labels)
    records = []
    for metadata, state in zip(times, run["milestone_states"]):
        residual = state[:m]-labels
        theta = state[m:m+m*m].reshape(m, m)
        square = float(residual@residual)
        rate = float(residual@theta@residual/square) if square else 0.
        records.append(dict(time=metadata["time"], loss=square/m,
            effective_rate=rate, relative_loss_derivative=-4/m*rate,
            eigenmin=float(np.linalg.eigvalsh((theta+theta.T)/2)[0])))
    state = run["state"]
    residual = state[:m]-labels
    theta = state[m:m+m*m].reshape(m, m)
    spectrum = np.linalg.eigvalsh((theta+theta.T)/2)
    positive = spectrum[spectrum > 0]
    changes = np.diff(run["losses"])
    resolved_growth = changes > np.maximum(1e-12, 1e-9*run["losses"][:-1])
    return dict(milestones=records,
                negative_sampled_rates=[record for record in records if record["effective_rate"] < 0],
                endpoint_effective_rate=float(residual@theta@residual/(residual@residual)),
                endpoint_eigenvalues=spectrum.tolist(),
                endpoint_positive_spectral_ratio=float(positive[-1]/positive[0]) if len(positive) else None,
                maximum_recorded_loss=float(np.max(run["losses"])),
                time_at_maximum_loss=float(run["times"][np.argmax(run["losses"])]),
                accepted_steps_with_loss_increase=int(np.count_nonzero(resolved_growth)),
                largest_accepted_step_loss_increase=float(max(0., np.max(changes))) if len(changes) else 0.,
                interpretation="For M=8, L'/L=-effective_rate/2. A negative rate means instantaneous loss growth; an indefinite kernel alone does not establish growth.")


def analyze_configuration(inputs, source, result):
    metadata = inputs.json(source/"configuration.json")
    initial = inputs.arrays(source/"initial_coefficients.npz")
    original_probe = inputs.arrays(source/"probe_coefficients.npz")
    probe = inputs.arrays(result/"probe_coefficients_refined.npz") if (result/"probe_coefficients_refined.npz").exists() else original_probe
    dense = inputs.arrays(result/"dense_reference_refined.npz") if (result/"dense_reference_refined.npz").exists() else inputs.arrays(source/"dense_resolution1.npz")
    dense_record = inputs.json(source/"dense_resolution1.json")
    directories = sorted((p for p in result.glob("order4_resolution*") if (p/"result.json").exists()),
                         key=lambda p: int(p.name.removeprefix("order4_resolution")))
    if len(directories) < 2:
        raise ValueError("configuration has fewer than two completed resolutions: "+result.name)
    resolved = [load_run(inputs, directory, initial, original_probe, source) for directory in directories]
    fine, fine_record, fine_probe = resolved[-1]
    coarse, coarse_record, coarse_probe = resolved[-2]
    gate = pair_metrics(coarse, fine, coarse_record, fine_record, coarse_probe, fine_probe, dense)
    spatial = spatial_metrics(fine, probe, dense)
    extra = {}
    for name in ("radau_crosscheck", "fresh_reproduction"):
        if (result/name/"result.json").exists():
            arrays, record, own_probe = load_run(inputs, result/name, initial, original_probe, source)
            extra[name] = dict(record=record, probe=own_probe,
                              comparison=pair_metrics(fine, arrays, fine_record, record, fine_probe, own_probe, dense))
    first = source.name == "quadrant_alternating_n128_seed20260920"
    direct_qualified = (gate["passed"] and spatial["quadrature_pass"]
                        and (not first or len(extra) == 2 and all(check["comparison"]["passed"] for check in extra.values())))
    qualified = direct_qualified and spatial["fourier_pass"]
    fitted = fine_record["status"] == "fitted"
    verdict = ("no_matched_endpoint" if not fitted else "numerically_inconclusive" if not qualified else
               "agreement" if spatial["circle_rms"] <= .1 else "adverse" if spatial["circle_rms"] > .2 else "inconclusive")
    baseline = inputs.arrays(result/"order2_spectral.npz")
    baseline_spatial = spatial_metrics(baseline, probe, dense)
    baseline_checks, spectrum = spectral_checks(initial, baseline, probe)
    baseline_status = str(baseline["status"].item())
    baseline_valid = baseline_status == "fitted" and baseline_checks["passed"] and baseline_spatial["quadrature_pass"] and baseline_spatial["fourier_pass"]
    baseline_verdict = ("no_matched_endpoint" if baseline_status != "fitted" else "numerically_inconclusive" if not baseline_valid else
                        "agreement" if baseline_spatial["circle_rms"] <= .1 else "adverse" if baseline_spatial["circle_rms"] > .2 else "inconclusive")
    dense_time, fine_time = float(dense["time"]), float(fine["time"])
    prefix_seconds = 0.
    if not fine_record["from_zero"]:
        prefix_seconds = inputs.json(source/("order4_resolution"+str(fine_record["start_level"])+".json"))["seconds"]
    rates = rate_diagnostics(inputs, directories[-1], fine, initial["labels"])
    case = dict(configuration=source.name, width=metadata["width"], seed=metadata["seed"], target=TARGET,
                dense=dict(status=dense_record["status"], time=dense_time,
                           loss=float(np.mean((dense["train_f"]-initial["labels"])**2)),
                           wall_seconds=dense_record["seconds"]),
                order4=dict(status=fine_record["status"], verdict=verdict, qualified_endpoint=bool(qualified),
                            direct_grid_qualified=bool(direct_qualified),
                            direct_grid_verdict=("adverse" if spatial["circle_rms"] > .2 else "agreement" if spatial["circle_rms"] <= .1 else "inconclusive") if direct_qualified else "unresolved",
                            time=fine_time, time_ratio_to_dense=fine_time/dense_time,
                            loss=float(np.mean((fine["train_f"]-initial["labels"])**2)),
                            wall_seconds=fine_record["seconds"], wall_scope="selected scalar run only; continuation excludes initialization and t<=2048",
                            prefix_wall_seconds=prefix_seconds, total_training_wall_seconds=prefix_seconds+fine_record["seconds"],
                            training_wall_ratio_to_dense=(prefix_seconds+fine_record["seconds"])/dense_record["seconds"],
                            accepted_steps=fine_record["accepted_steps"], nfev=fine_record["nfev"],
                            njev=fine_record["njev"], nlu=fine_record["nlu"], segments=fine_record["segments"],
                            rtol=fine_record["rtol"], from_zero=fine_record["from_zero"],
                            spatial=spatial, refinement=gate, probe=fine_probe, checks=extra, rates=rates,
                            all_resolution_records=[entry[1] for entry in resolved],
                            all_resolution_probe_checks=[entry[2] for entry in resolved]),
                order2=dict(status=baseline_status, verdict=baseline_verdict, qualified_endpoint=bool(baseline_valid),
                            time=float(baseline["time"]), time_ratio_to_dense=float(baseline["time"])/dense_time,
                            loss=float(np.mean((baseline["train_f"]-initial["labels"])**2)),
                            wall_seconds=None, wall_scope="analytic spectral evaluation; evaluation wall time not recorded",
                            spatial=baseline_spatial, spectral=baseline_checks))
    # The run summaries are only cross-checks; every metric above comes from arrays.
    summary = inputs.json(result/"summary.json")
    case["summary_crosscheck"] = dict(verdict_matches=summary["verdict"] == verdict,
        circle_rms_difference=abs(summary["spatial"]["circle_rms"]-spatial["circle_rms"]),
        numerical_change_difference=abs(summary["gate"]["numerical_change"]-gate["numerical_change"]),
        probe_peak_difference=abs(fine_record["training_probe_gap"]-fine_probe["peak_training_probe_gap"]))
    prefix = None
    if not fine_record["from_zero"]:
        prefix = inputs.arrays(source/("order4_resolution"+str(fine_record["start_level"])+".npz"))
    plot = dict(dense=dense, fine=fine, fine_record=fine_record, prefix=prefix,
                baseline=baseline, spectrum=spectrum, labels=initial["labels"], inputs=initial["inputs"])
    return case, plot


def figures(output, cases, plots):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.titlesize": 11, "figure.dpi": 150, "savefig.dpi": 220,
                         "pdf.fonttype": 42})
    loss_figure, loss_axes = plt.subplots(2, 2, figsize=(12.3, 8.5), sharex=False, sharey=True)
    function_figure, function_axes = plt.subplots(2, 2, figsize=(12.3, 8.5), sharex=True)
    loss_upper = max(2., 1.5*max(float(np.max(plot["fine"]["losses"])) for plot in plots))
    for index, (case, plot) in enumerate(zip(cases, plots)):
        axis, function_axis = loss_axes.flat[index], function_axes.flat[index]
        dense, fine = plot["dense"], plot["fine"]
        times, losses = fine["times"], fine["losses"]
        if plot["prefix"] is not None:
            prefix = plot["prefix"]
            times = np.concatenate((prefix["times"][:-1], times))
            losses = np.concatenate((prefix["losses"][:-1], losses))
        axis.plot(dense["times"], dense["losses"], color=BLACK, linewidth=1.8, label="Dense")
        axis.plot(times, losses, color=PURPLE, linewidth=1.8, label="Scalar order four")
        horizon = max(float(fine["time"]), float(plot["baseline"]["time"]), float(dense["time"]))
        analytic_times = np.concatenate(([0.], np.geomspace(.01, max(.02, horizon), 700)))
        eig, components = plot["spectrum"]
        exponent = -4/len(plot["labels"]) * np.outer(analytic_times, eig)
        analytic_loss = np.exp(exponent) @ (components**2) / len(components)
        selected = analytic_times <= float(plot["baseline"]["time"])
        axis.plot(analytic_times[selected], analytic_loss[selected], color=GRAY, linestyle="--", linewidth=1.5,
                  label="Frozen kernel (analytic)")
        axis.axhline(TARGET, color="#b2652f", linestyle=":", linewidth=1., label="Target MSE")
        axis.set_xscale("symlog", linthresh=1.)
        axis.set_yscale("log")
        axis.set_xlim(0., 1.15*horizon)
        axis.set_xticks((0., 1., 100., 1e4, 1e6, 1e8))
        axis.set_ylim(4e-7, loss_upper)
        axis.set_xlabel("Physical training time")
        axis.set_ylabel("Training mean squared error")
        axis.set_title("Width {} · seed {}".format(case["width"], case["seed"]))
        axis.grid(True, which="major", alpha=.14)
        note = ("Order four: {}\nt = {:.4g}; {:.3g}× dense time\nRecorded continuation: {:.2f} wall seconds".format(
            case["order4"]["status"].replace("_", " "), case["order4"]["time"],
            case["order4"]["time_ratio_to_dense"], case["order4"]["wall_seconds"]))
        axis.text(.03, .97, note, transform=axis.transAxes, fontsize=8.5,
                  va="top", bbox=dict(facecolor="white", alpha=.9, edgecolor="none"))
        inset = function_axis.inset_axes([.59, .065, .37, .27])
        function_axis.axvspan(10., 80., color="#c9d9eb", alpha=.22, zorder=0)
        for key, color, label in (("dense", BLACK, "Dense"), ("fine", PURPLE, "Scalar order four (direct grid)"),
                                  ("baseline", GRAY, "Frozen kernel")):
            model_name = {"dense": "dense", "fine": "order4", "baseline": "order2"}[key]
            info = case[model_name]
            if info["status"] != "fitted":
                continue
            values = plot[key]["grid"]
            angles = np.linspace(0., 360., len(values)+1)
            values = np.concatenate((values, values[:1]))
            valid = info.get("direct_grid_qualified", info.get("qualified_endpoint", True))
            style = "-" if key != "baseline" and valid else "--"
            function_axis.plot(angles, values, color=color, linewidth=1.65, linestyle=style,
                               label=label + (" (unresolved)" if not valid else ""))
            inset.plot(angles, values, color=color, linewidth=1., linestyle=style)
        training_angles = np.rad2deg(np.arctan2(plot["inputs"][:, 1], plot["inputs"][:, 0])) % 360.
        function_axis.scatter(training_angles, plot["labels"], s=22, facecolor="white",
                              edgecolor=BLACK, linewidth=.9, zorder=4, label="Training labels")
        inset.scatter(training_angles, plot["labels"], s=10, facecolor="white", edgecolor=BLACK, linewidth=.7, zorder=4)
        inset.set_xlim(0., 90.); inset.set_ylim(-1.6, 1.6)
        inset.set_xticks((0, 45, 90)); inset.set_yticks((-1, 0, 1))
        inset.tick_params(labelsize=6.5, length=2)
        inset.set_title("Training arc (expanded)", fontsize=7, pad=2)
        inset.patch.set_alpha(.96)
        function_axis.set_xlim(0., 360.)
        function_axis.set_xticks((0, 90, 180, 270, 360))
        function_axis.set_xlabel("Circle angle (degrees)")
        function_axis.set_ylabel("Prediction")
        function_axis.grid(True, alpha=.14)
        function_axis.set_title("Width {} · seed {}".format(case["width"], case["seed"]))
        status = case["order4"]["verdict"].replace("_", " ")
        if case["order4"]["status"] == "fitted":
            text = "Order-four direct-grid RMS: {:.4g}\nDirect grid: {}; Fourier: {}".format(
                case["order4"]["spatial"]["circle_rms"], case["order4"]["direct_grid_verdict"],
                "passed" if case["order4"]["spatial"]["fourier_pass"] else "unresolved")
        else:
            text = "Order four has no matched-loss endpoint\n{}; MSE {:.4g}".format(
                case["order4"]["status"].replace("_", " "), case["order4"]["loss"])
        function_axis.text(.03, .97, text, transform=function_axis.transAxes, va="top", fontsize=8.5,
                           bbox=dict(facecolor="white", alpha=.92, edgecolor="none"))
    for fig, axes, title, subtitle, stem in (
        (loss_figure, loss_axes, "Longer physical training time for the scalar closure",
         "Physical time is not computational cost. Curves end at each model’s own target crossing or recorded cap.", "long_time_training_loss"),
        (function_figure, function_axes, "Learned circle functions at each model’s own low-loss endpoint",
         "Each curve fits at MSE 10⁻⁶. Direct-grid disagreement and the separate Fourier encoding check are labeled individually.", "matched_loss_circle_functions")):
        handles, labels = [], []
        for axis in axes.flat:
            for handle, label in zip(*axis.get_legend_handles_labels()):
                if label not in labels:
                    handles.append(handle); labels.append(label)
        fig.suptitle(title, x=.07, y=.988, ha="left", fontsize=16, fontweight="bold")
        fig.text(.07, .95, subtitle, ha="left", fontsize=9.4, color="#444444")
        fig.legend(handles, labels, loc="lower center", ncol=min(4, len(labels)), frameon=False, fontsize=9)
        fig.tight_layout(rect=(.01, .06, 1., .925), h_pad=2.2, w_pad=2.)
        for suffix in ("png", "pdf"):
            fig.savefig(output/(stem+"."+suffix), bbox_inches="tight")
        plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DATA/"scalar_circle_endpoint_primary01")
    parser.add_argument("--campaign", type=Path, default=DATA/"scalar_long_time_primary01")
    parser.add_argument("--output", type=Path, default=DATA/"scalar_long_time_analysis01")
    parser.add_argument("--overwrite", action="store_true", help="regenerate this analyzer's output files")
    args = parser.parse_args()
    source_directories = sorted(args.source.glob("quadrant_alternating_*"))
    if len(source_directories) != 4 or any(not (args.campaign/source.name/"summary.json").exists() for source in source_directories):
        raise RuntimeError("wait for all four completed configuration summaries before analysis")
    args.output.mkdir(parents=True, exist_ok=args.overwrite)
    inputs, cases, plots = Inputs(), [], []
    inputs.track(STUDY/"SCALAR_LONG_TIME_PROTOCOL.md")
    inputs.track(STUDY/"scalar_long_time_engine.py")
    inputs.track(STUDY/"run_scalar_long_time.py")
    inputs.track(args.campaign/"manifest.json")
    if (args.campaign/"campaign.json").exists():
        inputs.track(args.campaign/"campaign.json")
    for source in source_directories:
        case, plot = analyze_configuration(inputs, source, args.campaign/source.name)
        cases.append(case); plots.append(plot)
    report = dict(target=TARGET, configurations=cases,
                  interpretation="Training fit, physical-time slowdown, computational wall cost, and dense-function agreement are distinct quantities.",
                  baseline="Frozen-kernel curves use the analytic spectral solution, without training integration.")
    (args.output/"analysis.json").write_text(json.dumps(report, indent=2, default=scalar)+"\n")
    fields = ("configuration", "width", "seed", "model", "status", "verdict", "qualified_endpoint", "time",
              "time_ratio_to_dense", "loss", "wall_seconds", "circle_rms", "relative_rms", "maximum_error",
              "refinement_change", "time_relative_change", "peak_training_probe_gap", "wall_scope")
    with (args.output/"endpoints.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for case in cases:
            for model in ("dense", "order4", "order2"):
                item = case[model]
                row = dict(configuration=case["configuration"], width=case["width"], seed=case["seed"], model=model)
                row.update({key: item.get(key, "") for key in fields if key not in row})
                for key in ("circle_rms", "relative_rms", "maximum_error"):
                    row[key] = item.get("spatial", {}).get(key, "")
                row["refinement_change"] = item.get("refinement", {}).get("numerical_change", "")
                row["time_relative_change"] = item.get("refinement", {}).get("time_relative_change", "")
                row["peak_training_probe_gap"] = item.get("probe", {}).get("peak_training_probe_gap", "")
                writer.writerow(row)
    figures(args.output, cases, plots)
    shutil.copy2(Path(__file__), args.output/Path(__file__).name)
    (args.output/"manifest.json").write_text(json.dumps(dict(command=sys.argv,
        analysis_source=digest(Path(__file__)), inputs=inputs.hashes,
        outputs={path.name: digest(path) for path in sorted(args.output.iterdir()) if path.is_file() and path.name != "manifest.json"}), indent=2)+"\n")
    print(json.dumps({case["configuration"]: {name:case[name]["verdict"] for name in ("order4", "order2")}
                      for case in cases}, indent=2))


if __name__ == "__main__":
    main()
