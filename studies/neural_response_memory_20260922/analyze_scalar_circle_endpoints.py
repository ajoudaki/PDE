"""Rescore and plot saved scalar full-circle endpoints; never run training."""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import sys

for _thread_key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_key] = "1"
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

CASES = ("equal_mixed_odd", "quadrant_alternating")
NAMES = ("dense", "order4", "order2")
COLORS = {"dense": "#141414", "order4": "#773f9a", "order2": "#999999"}
LABELS = {"dense": "Dense", "order4": "Order 4", "order2": "Order 2"}
TITLES = {"equal_mixed_odd": "Four-input mixed", "quadrant_alternating": "Eight-input alternating"}
EXPECTED = [(case, width, seed) for case in CASES for width in (128, 256)
            for seed in (20260920, 20260927)]


def rms(a):
    return float(np.sqrt(np.mean(np.abs(a) ** 2)))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")


def write_csv(path, rows, fields):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


class Audit:
    def __init__(self):
        self.checks = []
        self.inputs = set()

    def read_json(self, path):
        self.inputs.add(path)
        return json.loads(path.read_text())

    def arrays(self, path, keys=None):
        self.inputs.add(path)
        with np.load(path, allow_pickle=False) as data:
            return {key: data[key] for key in (data.files if keys is None else keys)}

    def check(self, name, passed, detail=None):
        self.checks.append({"name": name, "passed": bool(passed), "detail": detail})

    def close(self, name, actual, expected, atol=1e-11, rtol=1e-8):
        self.check(name, np.allclose(actual, expected, atol=atol, rtol=rtol),
                   {"actual": float(actual), "expected": float(expected)})


def fourier_readout(coefficients, angles):
    """Independent normalized-rFFT convention, away from any Nyquist mode."""
    c = np.asarray(coefficients)
    if c.ndim != 1:
        raise ValueError("Endpoint Fourier coefficients must be one-dimensional")
    return c[0].real + 2 * np.real(np.exp(1j * np.outer(angles, np.arange(1, len(c)))) @ c[1:])


def load_endpoint(directory, name, level, audit):
    base = directory / (name + "_resolution" + str(level))
    refined = directory / (name + "_spatial_refined_resolution" + str(level) + ".npz")
    arrays = audit.arrays(refined if refined.exists() else base.with_suffix(".npz"))
    record = audit.read_json(base.with_suffix(".json"))
    return arrays, record


def numerical_gate(a, b, discrepancy):
    change = rms(a["grid"] - b["grid"])
    return {"change": change, "passed": change <= .002 and change <= .1 * max(discrepancy, 1e-6)}


def analyze_configuration(directory, audit):
    summary = audit.read_json(directory / "summary.json")
    metadata, latest = summary["configuration"], summary["latest"]
    key = directory.name
    initial = audit.arrays(directory / "initial_coefficients.npz", ("inputs", "labels"))
    inputs, labels = initial["inputs"], initial["labels"]
    probe_path = directory / "probe_coefficients_refined.npz"
    if not probe_path.exists():
        probe_path = directory / "probe_coefficients.npz"
    probe = audit.arrays(probe_path, ("angles", "off_angles"))
    angles, off_angles = probe["angles"], probe["off_angles"]
    audit.check(key + "/unit_circle_inputs", np.allclose(np.linalg.norm(inputs, axis=1), 1, atol=1e-14, rtol=0))
    audit.check(key + "/uniform_periodic_grid", np.allclose(angles, 2 * np.pi * np.arange(len(angles)) / len(angles), atol=1e-14, rtol=0))
    audit.check(key + "/fixed_off_grid", np.allclose(off_angles, 2 * np.pi * (np.arange(32) + np.sqrt(2) / 10) / 32, atol=1e-14, rtol=0))
    endpoints, records, previous = {}, {}, {}
    endpoint_rows = []
    for name in NAMES:
        arrays, record = load_endpoint(directory, name, latest[name], audit)
        old, old_record = load_endpoint(directory, name, latest[name] - 1, audit)
        endpoints[name], records[name], previous[name] = arrays, record, (old, old_record)
        loss = float(np.mean((arrays["train_f"] - labels) ** 2))
        prefix = key + "/" + name
        audit.check(prefix + "/finite_endpoint", all(np.isfinite(arrays[field]).all() for field in ("grid", "off_grid", "train_f", "train_probe", "state")))
        audit.check(prefix + "/grid_shape", arrays["grid"].shape == angles.shape)
        audit.check(prefix + "/monotone_times", np.all(np.diff(arrays["times"]) > 0))
        audit.check(prefix + "/loss_trace_shape", arrays["times"].shape == arrays["losses"].shape)
        audit.close(prefix + "/recorded_loss", loss, record["loss"])
        audit.close(prefix + "/last_loss", loss, arrays["losses"][-1])
        audit.close(prefix + "/recorded_time", float(arrays["time"]), record["time"])
        audit.close(prefix + "/last_time", float(arrays["times"][-1]), record["time"])
        gap = rms(arrays["train_probe"] - arrays["train_f"])
        audit.close(prefix + "/training_readout_gap", gap, record["training_readout_gap"])
        if record["status"] == "fitted":
            audit.close(prefix + "/target_crossing", loss, metadata["target"], atol=1e-10, rtol=1e-6)
            audit.check(prefix + "/first_saved_crossing", np.all(arrays["losses"][:-1] > metadata["target"]))
        endpoint_rows.append(dict(configuration=key, case=metadata["case"], width=metadata["width"], seed=metadata["seed"], model=name, status=record["status"], time=float(arrays["time"]), training_mse=loss, resolution=latest[name], rtol=record["rtol"], training_readout_rms=gap))
    dense, dense_record = endpoints["dense"], records["dense"]
    rows = []
    plots = {"dense": dense["grid"]}
    for name in ("order4", "order2"):
        a, rec = endpoints[name], records[name]
        difference = a["grid"] - dense["grid"]
        error = rms(difference)
        dense_rms = rms(dense["grid"])
        change = abs(error - rms(difference[::2]))
        spatial_pass = change <= .001 and change <= .01 * max(error, 1e-6)
        scalar_gate = numerical_gate(previous[name][0], a, error)
        dense_gate = numerical_gate(previous["dense"][0], dense, error)
        statuses_match = previous[name][1]["status"] == rec["status"] and previous["dense"][1]["status"] == dense_record["status"]
        fourier = audit.arrays(directory / (name + "_fourier.npz"), ("endpoint", "angles", "endpoint_grid", "endpoint_off_grid"))
        fg = fourier_readout(fourier["endpoint"], angles)
        fo = fourier_readout(fourier["endpoint"], off_angles)
        prefix = key + "/" + name
        audit.check(prefix + "/fourier_angles", np.array_equal(fourier["angles"], angles))
        audit.check(prefix + "/fourier_grid_evaluation", np.allclose(fg, fourier["endpoint_grid"], atol=1e-10, rtol=1e-10))
        audit.check(prefix + "/fourier_off_grid_evaluation", np.allclose(fo, fourier["endpoint_off_grid"], atol=1e-10, rtol=1e-10))
        grid_rms, off_rms = rms(fg - a["grid"]), rms(fo - a["off_grid"])
        fourier_max = float(max(np.max(np.abs(fg - a["grid"])), np.max(np.abs(fo - a["off_grid"]))))
        fourier_pass = max(grid_rms, off_rms) <= 1e-5 and fourier_max <= 1e-4
        plots[name] = fg if fourier_pass else a["grid"]
        fitted = rec["status"] == dense_record["status"] == "fitted"
        valid = scalar_gate["passed"] and dense_gate["passed"] and spatial_pass and fourier_pass and statuses_match
        verdict = ("no_matched_endpoint" if not fitted else "numerically_inconclusive" if not valid else
                   "agreement" if error <= .1 else "adverse" if error > .2 else "inconclusive")
        row = dict(configuration=key, case=metadata["case"], width=metadata["width"], seed=metadata["seed"], model=name,
            fitted_pair=fitted, circle_rms=error, relative_rms=error / max(dense_rms, 1e-30), dense_function_rms=dense_rms,
            maximum_grid_error=float(np.max(np.abs(difference))), scalar_status=rec["status"], dense_status=dense_record["status"],
            scalar_time=float(a["time"]), dense_time=float(dense["time"]), scalar_loss=float(np.mean((a["train_f"] - labels) ** 2)),
            dense_loss=float(np.mean((dense["train_f"] - labels) ** 2)), scalar_resolution_change=scalar_gate["change"],
            dense_resolution_change=dense_gate["change"], scalar_resolution_passed=scalar_gate["passed"], dense_resolution_passed=dense_gate["passed"],
            resolution_statuses_match=statuses_match, grid_size=len(angles), quadrature_change=change, quadrature_passed=spatial_pass,
            fourier_grid_rms=grid_rms, fourier_off_grid_rms=off_rms, fourier_maximum=fourier_max,
            fourier_mode=len(fourier["endpoint"]) - 1, fourier_passed=fourier_pass, valid=valid, verdict=verdict)
        reported = summary["models"][name]
        for field in ("circle_rms", "relative_rms", "dense_function_rms", "maximum_grid_error", "scalar_time", "dense_time", "scalar_loss", "dense_loss"):
            audit.close(prefix + "/summary_" + field, row[field], reported[field])
        for field in ("fitted_pair", "valid", "verdict", "scalar_status", "dense_status"):
            audit.check(prefix + "/summary_" + field, row[field] == reported[field])
        for gate_name, gate in (("scalar_gate", scalar_gate), ("dense_gate", dense_gate)):
            audit.close(prefix + "/" + gate_name, gate["change"], reported[gate_name]["change"])
            audit.check(prefix + "/" + gate_name + "_pass", gate["passed"] == reported[gate_name]["passed"])
        audit.close(prefix + "/quadrature_change", change, reported["quadrature"]["change"])
        audit.check(prefix + "/quadrature_pass", spatial_pass == reported["quadrature"]["passed"])
        audit.check(prefix + "/fourier_pass", fourier_pass == reported["fourier"]["passed"])
        rows.append(row)
    return dict(key=key, metadata=metadata, rows=rows, endpoint_rows=endpoint_rows, angles=angles,
                training_angles=np.mod(np.arctan2(inputs[:, 1], inputs[:, 0]), 2 * np.pi), labels=labels,
                endpoints=endpoints, records=records, plots=plots, latest=latest)


def status_text(record):
    status = record["status"]
    label = "FITTED" if status == "fitted" else "CAPPED: " + status.removesuffix("_cap") if status.endswith("_cap") else status.upper()
    return f"{label}, t={record['time']:.4g}, MSE={record['loss']:.2g}"


def format_axes(ax):
    ax.set_xlim(0, 360)
    ax.set_xticks([0, 90, 180, 270, 360])
    ax.grid(alpha=.16)
    ax.spines[["top", "right"]].set_visible(False)


def title(config):
    m = config["metadata"]
    return f"{TITLES[m['case']]} · n={m['width']} · seed {m['seed']}"


def plot_overlay(ax, config, annotate=True):
    theta = np.degrees(config["angles"])
    theta_closed = np.r_[theta, 360.]
    for name in ("order2", "order4", "dense"):
        values = config["plots"][name]
        ax.plot(theta_closed, np.r_[values, values[0]], color=COLORS[name], lw=1.7 if name != "order2" else 1.4,
                ls="--" if name == "order2" else "-", label=LABELS[name], zorder=2 if name == "dense" else 1)
    train = np.degrees(config["training_angles"])
    ax.scatter(train, config["labels"], s=25, marker="x", color="#b55c19", zorder=5)
    for angle, label in zip(train, config["labels"]):
        ax.axvline(angle, color="#b55c19", lw=.5, alpha=.15)
        if annotate:
            ax.annotate(f"{label:+g}", (angle, label), xytext=(0, 6 if label >= 0 else -12),
                        textcoords="offset points", ha="center", fontsize=6, color="#994b12")
    status = "\n".join(f"{LABELS[name]}: {status_text(config['records'][name])}" for name in NAMES)
    if any(not row["fourier_passed"] for row in config["rows"]):
        status += "\nFourier unresolved; direct finite-grid scalar outputs shown"
    ax.text(.985, .98, status, va="top", ha="right", transform=ax.transAxes, fontsize=7.1,
            bbox=dict(facecolor="white", edgecolor="none", alpha=.82, pad=2))
    ax.set_title(title(config), fontsize=10, loc="left")
    ax.set_ylabel("Final predictor f(θ)")
    ax.margins(y=.28)
    format_axes(ax)


def save_figure(fig, output, stem):
    for extension in ("png", "pdf"):
        fig.savefig(output / f"{stem}.{extension}", dpi=170, bbox_inches="tight")
    plt.close(fig)


def make_figures(configurations, output):
    lookup = {(c["metadata"]["case"], c["metadata"]["width"], c["metadata"]["seed"]): c for c in configurations}
    handles = [Line2D([0], [0], color=COLORS[n], ls="--" if n == "order2" else "-", lw=2, label=LABELS[n]) for n in NAMES]
    handles.append(Line2D([0], [0], color="#b55c19", marker="x", linestyle="none", label="Training locations and labels"))
    fig, axes = plt.subplots(4, 2, figsize=(16, 14), constrained_layout=True)
    # Keep task families in columns and initialization/width settings in rows.
    for ax, key in zip(axes.T.flat, EXPECTED):
        if key in lookup:
            plot_overlay(ax, lookup[key])
        else:
            ax.text(.5, .5, "Configuration incomplete / unavailable", ha="center", transform=ax.transAxes)
            ax.set_title(f"{TITLES[key[0]]} · n={key[1]} · seed {key[2]}", fontsize=10)
            format_axes(ax)
    for ax in axes[-1]:
        ax.set_xlabel("Circle angle θ (degrees)")
    fig.suptitle("Final full-circle functions at each model’s own stopping time\nCapped curves are finite-time outputs; they are not matched fitted endpoints", fontsize=14)
    fig.legend(handles=handles, loc="outside lower center", ncol=4, frameon=False)
    save_figure(fig, output, "scalar_circle_endpoint_all_eight")
    fig, axes = plt.subplots(2, 2, figsize=(15, 9), constrained_layout=True)
    for row, case in enumerate(CASES):
        config = lookup.get((case, 128, 20260920))
        if config is None:
            for ax in axes[row]:
                ax.text(.5, .5, "Configuration unavailable", ha="center", transform=ax.transAxes)
            continue
        plot_overlay(axes[row, 0], config)
        ax = axes[row, 1]
        theta = np.degrees(config["angles"])
        for name in ("order4", "order2"):
            diff = config["endpoints"][name]["grid"] - config["endpoints"]["dense"]["grid"]
            result = next(r for r in config["rows"] if r["model"] == name)
            status = "matched fitted endpoints" if result["fitted_pair"] else "unmatched: capped / unfitted"
            ax.plot(np.r_[theta, 360.], np.r_[diff, diff[0]], color=COLORS[name], ls="--" if name == "order2" else "-",
                    label=f"{LABELS[name]}: RMS={result['circle_rms']:.4g}; {status}")
        ax.axhline(0, color="black", lw=.7)
        for angle in np.degrees(config["training_angles"]):
            ax.axvline(angle, color="#b55c19", lw=.6, alpha=.2)
        ax.set_title("Function difference from dense at separate stopping times", fontsize=10, loc="left")
        ax.set_ylabel("Scalar minus dense")
        ax.legend(fontsize=7, loc="best", framealpha=.85)
        format_axes(ax)
    for ax in axes[-1]:
        ax.set_xlabel("Circle angle θ (degrees)")
    fig.suptitle("Fixed representatives: n=128, seed 20260920, both task families", fontsize=14)
    fig.legend(handles=handles, loc="outside lower center", ncol=4, frameon=False)
    save_figure(fig, output, "scalar_circle_endpoint_representatives")
    fig, axes = plt.subplots(4, 2, figsize=(16, 13), constrained_layout=True)
    for ax, key in zip(axes.T.flat, EXPECTED):
        config = lookup.get(key)
        if config is None:
            ax.text(.5, .5, "Configuration unavailable", ha="center", transform=ax.transAxes)
            continue
        for name in NAMES:
            a = config["endpoints"][name]
            ax.plot(a["times"], a["losses"], color=COLORS[name], ls="--" if name == "order2" else "-", label=LABELS[name])
            ax.plot(a["times"][-1], a["losses"][-1], marker="o" if config["records"][name]["status"] == "fitted" else "x", color=COLORS[name], ms=5)
        ax.axhline(config["metadata"]["target"], color="#b55c19", ls=":", lw=1)
        ax.set_yscale("log")
        ax.set_xscale("symlog", linthresh=1)
        ax.set_xlim(0, max(float(config["endpoints"][name]["time"]) for name in NAMES) * 1.04)
        ax.set_title(title(config), fontsize=10, loc="left")
        ax.set_ylabel("Training MSE")
        ax.grid(alpha=.15)
        ax.spines[["top", "right"]].set_visible(False)
    for ax in axes[-1]:
        ax.set_xlabel("Own training time (linear to 1, then logarithmic)")
    fig.suptitle("Stopping loss for every configuration\nCircles: fitted target crossing · crosses: capped or failed endpoint · dotted line: MSE 10⁻⁶", fontsize=13)
    fig.legend(handles=handles[:3], loc="outside lower center", ncol=3, frameon=False)
    save_figure(fig, output, "scalar_circle_endpoint_losses")


def reproduction_check(primary, reproduction, audit):
    results = []
    for summary_path in sorted(reproduction.glob("*/summary.json")):
        key = summary_path.parent.name
        original = primary / key
        if not (original / "summary.json").exists():
            results.append({"configuration": key, "status": "primary_unavailable"})
            continue
        a_summary = audit.read_json(original / "summary.json")
        b_summary = audit.read_json(summary_path)
        audit.check(key + "/reproduction_initialization_hash", a_summary["configuration"]["initialization_hash"] == b_summary["configuration"]["initialization_hash"])
        a_initial = audit.arrays(original / "initial_coefficients.npz")
        b_initial = audit.arrays(summary_path.parent / "initial_coefficients.npz")
        exact_initial = all(np.array_equal(a_initial[field], b_initial[field]) for field in a_initial)
        audit.check(key + "/reproduction_initial_coefficients", exact_initial)
        models = {}
        for name in NAMES:
            level = min(a_summary["latest"][name], b_summary["latest"][name])
            a, ar = load_endpoint(original, name, level, audit)
            b, br = load_endpoint(summary_path.parent, name, level, audit)
            timed = ar["status"] in ("wall_cap", "memory_cap") or br["status"] in ("wall_cap", "memory_cap")
            equal_shapes = all(a[k].shape == b[k].shape for k in ("grid", "off_grid", "state", "train_f", "times", "losses"))
            exact = equal_shapes and all(np.array_equal(a[k], b[k]) for k in ("grid", "off_grid", "state", "train_f", "times", "losses", "time"))
            if not timed:
                audit.check(key + "/reproduction_" + name, exact and ar["status"] == br["status"])
            models[name] = dict(resolution=level, primary_status=ar["status"], reproduction_status=br["status"], arrays_bitwise_equal=exact,
                                primary_time=ar["time"], reproduction_time=br["time"], comparison="resource_timing_dependent" if timed else "deterministic_endpoint")
        results.append(dict(configuration=key, initial_coefficients_bitwise_equal=exact_initial, models=models))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--reproduction", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.input, args.output = args.input.resolve(), args.output.resolve()
    if args.reproduction is not None:
        args.reproduction = args.reproduction.resolve()
    args.output.mkdir(parents=True, exist_ok=False)
    audit = Audit()
    configurations = [analyze_configuration(path.parent, audit) for path in sorted(args.input.glob("*/summary.json"))]
    rows = [row for config in configurations for row in config["rows"]]
    endpoints = [row for config in configurations for row in config["endpoint_rows"]]
    fitted = [row for row in rows if row["fitted_pair"]]
    capped = [row for row in rows if not row["fitted_pair"]]
    reproduction = reproduction_check(args.input, args.reproduction, audit) if args.reproduction else None
    missing = [f"{c}_n{w}_seed{s}" for c, w, s in EXPECTED if not (args.input / f"{c}_n{w}_seed{s}" / "summary.json").exists()]
    receipt = dict(expected_configurations=8, completed_configurations=len(configurations), incomplete_configurations=missing,
        primary_fitted_pairs=fitted, capped_or_unfitted_comparisons=capped, endpoints=endpoints, reproduction=reproduction,
        interpretation="The primary metric uses pairs fitted at MSE 1e-6 at their own tolerance-defined stopping times. Capped differences are descriptive, not matched-endpoint verdicts. The dense function is the comparison target; no unseen labels or test-risk claim are used.",
        metric="sqrt(mean((scalar_grid - dense_grid)**2)) on periodic uniform angles, approximating normalized circle L2", 
        representative_selection="n=128, seed=20260920 for each of the two frozen cases; fixed before seeing endpoint results")
    write_json(args.output / "summary.json", receipt)
    fields = list(rows[0]) if rows else ["configuration", "model", "fitted_pair", "circle_rms", "verdict"]
    write_csv(args.output / "primary_fitted_pairs.csv", fitted, fields)
    write_csv(args.output / "capped_function_comparisons.csv", capped, fields)
    write_csv(args.output / "all_comparisons.csv", rows, fields)
    write_csv(args.output / "endpoint_losses.csv", endpoints, list(endpoints[0]) if endpoints else ["configuration", "model", "status", "time", "training_mse"])
    checks = dict(checks=len(audit.checks), passed=sum(c["passed"] for c in audit.checks), failed=sum(not c["passed"] for c in audit.checks), details=audit.checks)
    write_json(args.output / "metric_audit.json", checks)
    make_figures(configurations, args.output)
    shutil.copy2(__file__, args.output / Path(__file__).name)
    manifest = dict(command=sys.argv, source_file=str(Path(__file__).resolve()), source_sha256=sha256(__file__),
        inputs={str(path): sha256(path) for path in sorted(audit.inputs)},
        outputs={path.name: sha256(path) for path in sorted(args.output.iterdir()) if path.is_file()},
        environment=dict(python=sys.version, executable=sys.executable, numpy=np.__version__, matplotlib=matplotlib.__version__, platform=platform.platform(),
                         threads={name: os.environ.get(name) for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}))
    write_json(args.output / "manifest.json", manifest)
    print(json.dumps(dict(output=str(args.output), configurations=len(configurations), fitted_pairs=len(fitted), capped_pairs=len(capped), checks=checks["checks"], failed_checks=checks["failed"])))
    return 1 if checks["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
