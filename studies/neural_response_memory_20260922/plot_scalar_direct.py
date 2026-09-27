"""Plot completed no-Fourier scalar runs; never launch or alter simulations.

Usage: python -B plot_scalar_direct.py --out data/generated/.../scalar_direct01
Requires config.json and scores.json written by run_scalar_direct.py.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


TASK_COLORS = {"broad_pair": "#1764a3", "close_pair": "#c16a14", "triple": "#27825e"}
TASK_LABELS = {"broad_pair": "Broad pair", "close_pair": "Close pair", "triple": "Triple"}
DEFAULT_OUT = Path(__file__).resolve().parents[2] / "data/generated/neural_response_memory_20260922/scalar_direct01"
FIGURES = ("flagship_trajectories", "cutoff_passive_errors", "gram_errors", "resource_costs")


def load_json(path):
    return json.loads(path.read_text())


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def base_records(scores):
    """Primary panel consists of clipped, unrefined population-order-one runs."""
    return sorted((r for r in scores["records"] if r.get("P") == 1
                   and not r.get("refined", False) and r.get("clip", True)
                   and not r["cell"].endswith(("_refined", "_unclipped"))),
                  key=lambda r: (r["task"], r["width"], r["seed"], r["K"]))


def parent_name(record):
    return f'parent_{record["task"]}_P{record["P"]}_n{record["width"]}_s{record["seed"]}'


def load_arrays(path):
    with np.load(path, allow_pickle=False) as saved:
        return {name: saved[name] for name in ("times", "train", "test", "grams")}


def checked_data(out, records):
    """Recompute plotted discrepancies and reject stale or incompatible scores."""
    data, parents, files = {}, {}, {out / "config.json", out / "scores.json"}
    for record in records:
        if not record.get("success"):
            continue
        p_name = parent_name(record)
        if p_name not in parents:
            p_path = out / p_name
            parents[p_name] = (load_arrays(p_path / "trajectory.npz"),
                               load_json(p_path / "result.json"))
            files.update((p_path / "trajectory.npz", p_path / "result.json"))
        parent, _ = parents[p_name]
        path = out / record["cell"] / "trajectory.npz"
        scalar = load_arrays(path)
        files.add(path)
        if not np.array_equal(scalar["times"], parent["times"]):
            raise ValueError(f'{record["cell"]}: scalar and parent times differ')
        for name in ("train", "test", "grams"):
            if scalar[name].shape != parent[name].shape:
                raise ValueError(f'{record["cell"]}: incompatible {name} shapes')
            if not np.isfinite(scalar[name]).all() or not np.isfinite(parent[name]).all():
                raise ValueError(f'{record["cell"]}: nonfinite saved {name}')
        test_error = float(np.sqrt(np.mean((scalar["test"] - parent["test"])**2, axis=1)).max())
        gram_errors = np.sqrt(np.mean((scalar["grams"] - parent["grams"])**2, axis=(2, 3))).max(axis=0)
        if not np.isclose(test_error, record["test_max_rms_error"], rtol=2e-9, atol=1e-12):
            raise ValueError(f'{record["cell"]}: passive RMS does not reproduce scores.json')
        if not np.allclose(gram_errors, record["gram_max_rms_errors"], rtol=2e-9, atol=1e-12):
            raise ValueError(f'{record["cell"]}: Gram errors do not reproduce scores.json')
        data[record["cell"]] = scalar
    return data, parents, files


def setup_style():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "axes.titlepad": 10,
                         "axes.labelsize": 10, "axes.titlesize": 11,
                         "figure.titlesize": 14, "legend.frameon": False,
                         "savefig.dpi": 190, "pdf.fonttype": 42,
                         "axes.grid": True, "grid.alpha": .18})


def save(fig, out, name):
    for extension in ("pdf", "png"):
        fig.savefig(out / f"{name}.{extension}", bbox_inches="tight")
    plt.close(fig)


def log_floor(values):
    positive = [float(v) for v in values if np.isfinite(v) and v > 0]
    return min(positive) / 10 if positive else 1e-16


def flagship_plot(out, config, selected, data, parents):
    fig, axes = plt.subplots(2, 2, figsize=(11.2, 7.1), constrained_layout=True)
    first = selected[0]
    parent, _ = parents[parent_name(first)]
    times = parent["times"]
    labels = np.asarray(config["tasks"]["broad_pair"][1])
    colors = plt.get_cmap("viridis")(np.linspace(.12, .85, len(selected)))
    ax = axes.flat[0]
    ax.plot(times, np.sqrt(np.mean((parent["train"] - labels)**2, axis=1)),
            color="#20252a", lw=2.3, label="Population parent")
    for record, color in zip(selected, colors):
        scalar = data[record["cell"]]
        ax.plot(times, np.sqrt(np.mean((scalar["train"] - labels)**2, axis=1)),
                lw=1.8, color=color, label=f'K = {record["K"]}')
        difference = scalar["test"] - parent["test"]
        for query, qax in enumerate(list(axes.flat)[1:]):
            qax.plot(times, difference[:, query], lw=1.7, color=color)
    ax.axhline(.05, color="#90979c", ls=":", lw=1, label="Fit threshold 0.05")
    ax.set(yscale="log", title="Training residual RMS", ylabel="RMS")
    ax.legend(fontsize=8, ncol=2)
    for query, qax in enumerate(list(axes.flat)[1:]):
        qax.axhline(0, color="#60686e", lw=.8)
        qax.set(title=f'Passive query at {config["queries"][query]:g}°',
                ylabel="Scalar output − parent output")
    for ax in axes.flat:
        ax.set_xlabel("Physical time")
        ax.set_xlim(times[0], times[-1])
    fig.suptitle("Broad pair · P = 1 · width 16 · seed 20260920")
    save(fig, out, "flagship_trajectories")


def track_style(task, width, seed, config):
    widths, seeds = sorted(config["widths"]), sorted(config["seeds"])
    return dict(color=TASK_COLORS.get(task, "#666666"),
                marker=("o", "s", "^", "D")[widths.index(width) % 4],
                ls=("-", "--", ":", "-.")[seeds.index(seed) % 4],
                lw=1.35, ms=5, alpha=.85)


def tracks(config, records):
    for task in config["tasks"]:
        for width in config["widths"]:
            for seed in config["seeds"]:
                selected = [r for r in records if r.get("success") and
                            (r["task"], r["width"], r["seed"]) == (task, width, seed)]
                yield task, width, seed, sorted(selected, key=lambda r: r["K"])


def missing_cutoffs(ax, records):
    """Visibly distinguish an attempted cutoff with no successful trajectory."""
    for cutoff in sorted({r["K"] for r in records}):
        selected = [r for r in records if r["K"] == cutoff]
        if selected and not any(r.get("success") for r in selected):
            ax.axvspan(cutoff - .12, cutoff + .12, color="#c8ced3", alpha=.25, zorder=0)
            ax.text(cutoff, .025, "No completed runs", transform=ax.get_xaxis_transform(),
                    ha="center", va="bottom", rotation=90, color="#58636b", fontsize=8)


def cutoff_plot(out, config, records):
    fig, ax = plt.subplots(figsize=(10.5, 6.4), constrained_layout=True)
    successful = [r for r in records if r.get("success")]
    floor = log_floor([r["test_max_rms_error"] for r in successful])
    completed_tracks = 0
    for task, width, seed, selected in tracks(config, records):
        if not selected:
            continue
        completed_tracks += 1
        ax.plot([r["K"] for r in selected],
                [max(r["test_max_rms_error"], floor) for r in selected],
                label=f'{TASK_LABELS.get(task, task)} · n={width} · s={seed}',
                **track_style(task, width, seed, config))
    cutoffs = sorted({r["K"] for r in records})
    total_cells = len(config["tasks"]) * len(config["widths"]) * len(config["seeds"])
    completion = ", ".join(f"K={k}: {sum(r.get('success', False) for r in records if r['K'] == k)}/{total_cells}"
                           for k in cutoffs)
    ax.set(yscale="log", xlabel="Scalar tree cutoff K",
           ylabel="Maximum over saved times of passive output RMS error",
           title=f"Passive fidelity across {completed_tracks}/{total_cells} cells · P = 1\nCompleted cells: {completion}")
    if cutoffs:
        ax.set_xticks(cutoffs)
    ax.axhline(.02, color="#80888e", ls=":", lw=1, label="0.02 observable threshold")
    ax.axhline(.1, color="#b85c61", ls=":", lw=1, label="0.1 observable threshold")
    missing_cutoffs(ax, records)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=8)
    save(fig, out, "cutoff_passive_errors")
    return completed_tracks, floor


def gram_plot(out, config, records):
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.9), constrained_layout=True, sharex=True)
    successful = [r for r in records if r.get("success")]
    floor = log_floor([e for r in successful for e in r["gram_max_rms_errors"]])
    for task, width, seed, selected in tracks(config, records):
        if not selected:
            continue
        for layer, ax in enumerate(axes):
            ax.plot([r["K"] for r in selected],
                    [max(r["gram_max_rms_errors"][layer], floor) for r in selected],
                    label=f'{TASK_LABELS.get(task, task)} · n={width} · s={seed}',
                    **track_style(task, width, seed, config))
    for layer, ax in enumerate(axes):
        ax.set(yscale="log", xlabel="Scalar tree cutoff K", title=f"Hidden layer {layer + 1}",
               ylabel="Maximum over saved times of Gram RMS error")
        cutoffs = sorted({r["K"] for r in records})
        if cutoffs:
            ax.set_xticks(cutoffs)
        ax.axhline(.02, color="#80888e", ls=":", lw=1)
        missing_cutoffs(ax, records)
    axes[1].legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=7)
    fig.suptitle("Training response Gram discrepancies · P = 1")
    save(fig, out, "gram_errors")
    return floor


def resource_plot(out, selected, parents):
    _, parent = parents[parent_name(selected[0])]
    cutoffs = [r["K"] for r in selected]
    fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.2), constrained_layout=True)
    axes[0].plot(cutoffs, [r["solver_seconds"] for r in selected], "o-", color="#1764a3", label="Scalar solve")
    axes[0].axhline(parent["solver_seconds"], color="#333333", ls="--", label="Parent solve")
    axes[0].set(title="Recorded integration time", ylabel="Seconds")
    axes[1].plot(cutoffs, [r["scalar_count"] for r in selected], "o-", color="#1764a3", label="Scalar state")
    axes[1].axhline(parent["population_state_count"], color="#333333", ls="--", label="Parent state")
    axes[1].set(title="Evolving state size", ylabel="Float64 coordinates")
    for key, factor, label, color in (("scalar_count", 8, "Scalar evolving state", "#1764a3"),
                                       ("runtime_array_bytes", 1, "Reported runtime arrays", "#c16a14"),
                                       ("table_bytes", 1, "Sparse training table", "#27825e")):
        axes[2].plot(cutoffs, [factor * r[key] for r in selected], "o-", color=color, label=label)
    axes[2].axhline(parent["population_total_array_bytes"], color="#333333", ls="--", label="Parent state + fixed matrices")
    axes[2].set(title="Stored numerical array sizes", ylabel="Bytes")
    for ax in axes:
        ax.set(xlabel="Scalar tree cutoff K", yscale="log", xticks=cutoffs)
        ax.legend(fontsize=7)
    fig.suptitle("Recorded costs · broad pair · P = 1 · width 16 · seed 20260920")
    save(fig, out, "resource_costs")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--overwrite", action="store_true", help="Replace existing plot artifacts only")
    args = parser.parse_args()
    out = args.out.resolve()
    if not (out / "scores.json").is_file():
        parser.error("scores.json must exist; this script does not wait for or start simulations")
    outputs = [out / f"{name}.{ext}" for name in FIGURES for ext in ("pdf", "png")]
    outputs += [out / "figure_captions.md", out / "figure_manifest.json"]
    existing = [str(path) for path in outputs if path.exists()]
    if existing and not args.overwrite:
        parser.error("plot artifacts already exist; use --overwrite: " + ", ".join(existing))
    config, scores = load_json(out / "config.json"), load_json(out / "scores.json")
    records = base_records(scores)
    data, parents, files = checked_data(out, records)
    selected = [r for r in records if r.get("success") and
                (r["task"], r["width"], r["seed"]) == ("broad_pair", 16, 20260920)]
    selected.sort(key=lambda r: r["K"])
    if not selected:
        raise ValueError("No successful flagship trajectories; no plots written")
    setup_style()
    flagship_plot(out, config, selected, data, parents)
    track_count, test_floor = cutoff_plot(out, config, records)
    gram_floor = gram_plot(out, config, records)
    resource_plot(out, selected, parents)
    successful = sum(bool(r.get("success")) for r in records)
    failed = [r["cell"] for r in records if not r.get("success")]
    completion = {str(k): dict(completed=sum(bool(r.get("success")) for r in records if r["K"] == k),
                               attempted=sum(r["K"] == k for r in records))
                  for k in sorted({r["K"] for r in records})}
    clipped = {r["cell"]: r.get("clipped_coordinate_count", 0) for r in records
               if r.get("success") and r.get("clipped_coordinate_count", 0)}
    exclusions = [r["cell"] for r in scores["records"] if r not in records]
    caption = f"""# Scalar direct experiment figures

All figures use completed, clipped, unrefined P=1 scalar runs and their matching
population references. Both systems use the same width, seed, history order,
training data and saved physical times. These are finite-width, finite-cutoff
numerical results; they do not establish hierarchy convergence. The passive
query panel contains only the three fixed query angles {config['queries']} degrees.

**flagship_trajectories.pdf/png.** Broad-pair task, width 16, seed 20260920.
The first panel shows training residual RMS; the other panels show signed
scalar-minus-parent output differences at each passive query. Completed scalar
cutoffs are {[r['K'] for r in selected]}. The dotted training line is RMS 0.05.

**cutoff_passive_errors.pdf/png.** Each separately marked track identifies a
task/width/seed cell; {track_count}/12 cells have completed trajectories. Colors
identify tasks, marker shapes identify widths, and line styles identify seeds.
For each cutoff, the ordinate is max_t sqrt(mean_q((f_scalar-f_parent)^2)),
over the saved time grid and three passive queries. Lines connect available
cutoffs only and do not represent measured intermediate-cutoff performance.
Gray bands mark attempted cutoffs with no completed runs. Completion and attempt
counts by cutoff are {completion}. Dotted lines at 0.02 and 0.1 are individual-observable reporting
thresholds; a point's position alone does not determine the experiment's joint
accuracy gate. There are {successful} completed P=1 records and {len(failed)}
recorded failed P=1 simulations with identifiable metadata. Missing points are
not treated as zero error. Exact zero errors, if any, are displayed at
{test_floor:.8g} to permit logarithmic axes.

**gram_errors.pdf/png.** Maximum over saved times of entrywise RMS discrepancies
between scalar and parent training Gram matrices h_l.T h_l/n, separately for
hidden layers 1 and 2. Track encodings match the passive-error figure. Exact
zero values, if any, use display floor {gram_floor:.8g}.

**resource_costs.pdf/png.** Flagship solve times, evolving-coordinate counts,
and reported numerical-array byte counts versus cutoff. Times are measured
solver wall times for these runs, not controlled speed benchmarks; compilation
and scalar initialization are excluded. Scalar state bytes equal eight times
its evolving-coordinate count. Runtime arrays and training-table bytes are
reported separately and may overlap; they are not additive memory totals.
The parent byte reference includes evolving state and fixed initialized hidden
matrices. Python objects, compiler objects and peak temporary memory are excluded.

Failed primary records: {failed or 'none'}.

Completed primary records with active coordinate clipping (coordinate counts):
{clipped or 'none'}. These plotted runs therefore include the declared clipping
rule; the figures do not establish accuracy for an unclipped closure.

Additional records excluded from these P=1 primary plots (including P=2,
refinement and unclipped controls): {exclusions or 'none'}.

Passive and Gram error entries were independently recomputed from trajectory
arrays and matched to scores.json before plotting. No simulation was run.
"""
    (out / "figure_captions.md").write_text(caption)
    manifest = dict(plot_source=str(Path(__file__).resolve()), plot_source_sha256=digest(Path(__file__)),
                    plotted_records=[r["cell"] for r in records if r.get("success")],
                    failed_primary_records=failed, excluded_records=exclusions,
                    completion_by_cutoff=completion, active_clipping=clipped,
                    input_sha256={str(path.relative_to(out)): digest(path) for path in sorted(files)},
                    outputs=[str(path.relative_to(out)) for path in outputs],
                    matplotlib=matplotlib.__version__, numpy=np.__version__)
    (out / "figure_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(dict(figures=len(FIGURES), successful_primary_records=successful,
                          completed_cells=track_count, out=str(out))))


if __name__ == "__main__":
    main()
