"""Plot complete p=4 validation and optional one-seed extrapolation evidence.

Inputs are the frozen analysis CSV files. Other schedules are intentionally
excluded because their grids are incomplete. Bands show observed seed ranges,
not confidence intervals. The 8192 stress is never connected to these bands.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import sys

import numpy as np


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def key(row):
    return tuple(int(float(row[k])) for k in ("n", "seed", "angle", "sign"))


def read_phase(root, phase):
    root = Path(root)
    with (root / "all_comparisons.csv").open() as handle:
        models = [row for row in csv.DictReader(handle) if row["p"] == "4"]
    with (root / "controls.csv").open() as handle:
        controls = [row for row in csv.DictReader(handle) if row["model"] == "dense_independent"]
    widths, seeds = ((512, 1024, 2048, 4096), range(8511, 8516)) if phase == "validation" else ((8192,), (8611,))
    expected = {(n, seed, angle, sign) for n in widths for seed in seeds
                for angle in (60, 90) for sign in (-1, 1)}
    for name, rows in (("p4", models), ("dense copy", controls)):
        if len(rows) != len(expected) or {key(row) for row in rows} != expected:
            raise ValueError(f"{phase} {name}: incomplete or duplicated case grid")
        for row in rows:
            if row["phase"] != phase:
                raise ValueError("Phase does not match the requested input")
            scaled = float(row["scaled_rms"])
            computed = math.sqrt(int(row["n"])) * float(row["rms_time_sup"])
            if not np.isfinite(scaled) or scaled <= 0 or not np.isclose(scaled, computed, rtol=1e-12, atol=1e-14):
                raise ValueError("Invalid or inconsistent scaled RMS")
    dense = {key(row): row for row in controls}
    for row in models:
        n_selected, retained = int(row["N"]), int(row["P"])
        if retained != n_selected ** 2 + 5 * n_selected + 6:
            raise ValueError("Retained-state count does not match N")
        if not np.isclose(float(row["dense_scaled_rms"]), float(dense[key(row)]["scaled_rms"]), rtol=1e-12, atol=1e-14):
            raise ValueError("Model and independent-control CSV disagree on the baseline")
    source_hashes = {str(root / name): sha256(root / name)
                     for name in ("all_comparisons.csv", "controls.csv")}
    return models, controls, source_hashes


def aggregates(models, controls):
    result = []
    for phase in sorted({r["phase"] for r in models}):
        for n in sorted({int(r["n"]) for r in models if r["phase"] == phase}):
            for angle, sign in ((90, 1), (90, -1), (60, 1), (60, -1)):
                for name, rows in (("p4", models), ("dense_independent", controls)):
                    selected = [r for r in rows if r["phase"] == phase and
                                (int(r["n"]), int(float(r["angle"])), int(r["sign"])) == (n, angle, sign)]
                    values = np.array([float(r["scaled_rms"]) for r in selected])
                    result.append(dict(phase=phase, n=n, angle=angle, sign=sign, model=name,
                                       count=len(values), median=float(np.median(values)),
                                       minimum=float(values.min()), maximum=float(values.max())))
    return result


def write_csv(path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validation", required=True)
    parser.add_argument("--extrapolation")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    models, controls, hashes = read_phase(args.validation, "validation")
    if args.extrapolation:
        extra, baseline, extra_hashes = read_phase(args.extrapolation, "extrapolation")
        models += extra; controls += baseline; hashes.update(extra_hashes)
    rows = aggregates(models, controls)
    states = []
    for n in sorted({int(r["n"]) for r in models}):
        values = {(int(r["N"]), int(r["rank"]), int(r["P"])) for r in models if int(r["n"]) == n}
        if len(values) != 1:
            raise ValueError("The same width has inconsistent state counts or ranks")
        count, rank, retained = values.pop()
        states.append(dict(n=n, N=count, rank=rank, P=retained,
                           cases=sum(int(r["n"]) == n for r in models),
                           seeds=len({r["seed"] for r in models if int(r["n"]) == n})))
    ranks = {state["rank"] for state in states}
    if len(ranks) != 1:
        raise ValueError("The frozen rank changed across widths")
    anchor = next(state["P"] for state in states if state["n"] == 512)
    for state in states:
        budget = anchor * (math.log(state["n"]) / math.log(512)) ** 4
        next_n = state["N"] + 1
        if not state["P"] <= budget + 1e-8 or next_n ** 2 + 5 * next_n + 6 <= budget - 1e-8:
            raise ValueError("State counts violate the maximal-integer p=4 budget")
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    os.environ.setdefault("MPLCONFIGDIR", str((out / "matplotlib_cache").resolve()))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    color, gray = "#0072B2", "#777777"
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.5), sharex=True, sharey=True, layout="constrained")
    widths = [512, 1024, 2048, 4096]
    all_widths = widths + ([8192] if args.extrapolation else [])
    for ax, (angle, sign) in zip(axes.flat, ((90, 1), (90, -1), (60, 1), (60, -1))):
        for name, ink, linestyle in (("p4", color, "-"), ("dense_independent", gray, "--")):
            group = sorted([r for r in rows if (r["phase"], r["angle"], r["sign"], r["model"]) ==
                            ("validation", angle, sign, name)], key=lambda r: r["n"])
            assert [r["n"] for r in group] == widths and all(r["count"] == 5 for r in group)
            ax.plot(widths, [r["median"] for r in group], linestyle, color=ink, marker="o", markersize=4)
            ax.fill_between(widths, [r["minimum"] for r in group], [r["maximum"] for r in group], color=ink, alpha=.12)
            source = models if name == "p4" else controls
            points = [r for r in source if r["phase"] == "validation" and
                      (int(float(r["angle"])), int(r["sign"])) == (angle, sign)]
            ax.scatter([int(r["n"]) for r in points], [float(r["scaled_rms"]) for r in points],
                       color=ink, alpha=.5, s=10, zorder=3)
            stress = [r for r in rows if (r["phase"], r["angle"], r["sign"], r["model"]) ==
                      ("extrapolation", angle, sign, name)]
            if stress:
                assert len(stress) == 1 and stress[0]["count"] == 1
                ax.scatter([8192], [stress[0]["median"]], color=ink, edgecolors="white", linewidths=.7,
                           marker="D" if name == "p4" else "s", s=55, zorder=5)
        ax.axhline(.15, color="black", linestyle=":", linewidth=1.2)
        ax.set_title(f"{angle}° inputs · " + ("same-sign labels" if sign == 1 else "opposite-sign labels"))
        ax.set_xscale("log", base=2); ax.set_yscale("log")
        ax.set_xticks(all_widths, labels=[str(n) for n in all_widths]); ax.tick_params(axis="x", labelsize=9)
        ax.grid(alpha=.18); ax.set_xlabel("Dense width n")
        ax.set_ylabel(r"$\sqrt{n}\,E$  (circle RMS of time maximum)")
    handles = [Line2D([], [], color=color, marker="o", label="Compressed p=4 · median over 5 seeds"),
               Line2D([], [], color=gray, linestyle="--", marker="o", label="Independent dense copy · median over 5 seeds"),
               Line2D([], [], color="black", linestyle=":", label="Predeclared ceiling C=0.15")]
    if args.extrapolation:
        handles.append(Line2D([], [], color=color, marker="D", linestyle="none", label="8192 stress · one seed in each panel"))
    fig.legend(handles=handles, loc="outside lower center", ncol=2, fontsize=9)
    fig.suptitle("Complete p=4 schedule: unseen-circle prediction error\n"
                 "Validation bands show observed min–max, not confidence intervals", fontsize=12)
    fig.savefig(out / "p4_rms_summary.png", dpi=190)
    fig.savefig(out / "p4_rms_summary.pdf")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.4, 4.2), layout="constrained")
    ax.plot([s["n"] for s in states], [s["P"] for s in states], color=color, marker="o")
    for s in states:
        ax.annotate(f"{s['P']:,} scalars\nN={s['N']}", (s["n"], s["P"]),
                    xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9)
    ax.set_xscale("log", base=2); ax.set_xticks(all_widths, labels=[str(n) for n in all_widths])
    ax.set_ylim(0, max(s["P"] for s in states) * 1.22)
    ax.set_xlabel("Dense width n"); ax.set_ylabel("Retained moving and fixed scalars P")
    ax.set_title(f"Prespecified p=4 state budget · fixed source rank {next(iter(ranks))}")
    ax.grid(alpha=.18)
    fig.savefig(out / "p4_state_counts.png", dpi=190)
    fig.savefig(out / "p4_state_counts.pdf")
    plt.close(fig)
    write_csv(out / "plotted_aggregates.csv", rows)
    write_csv(out / "state_counts.csv", states)
    pooled = []
    for n in all_widths:
        values = [float(r["scaled_rms"]) for r in models if int(r["n"]) == n]
        pooled.append(dict(n=n, count=len(values), median=float(np.median(values)), maximum=max(values)))
    audit = dict(argv=sys.argv, source_sha256=sha256(__file__), input_sha256=hashes,
                 validation_comparisons=sum(r["phase"] == "validation" for r in models),
                 extrapolation_comparisons=sum(r["phase"] == "extrapolation" for r in models),
                 valid_models=all(r["valid_model"] == "True" for r in models),
                 dense_controls_settled=all(r["settled"] == "True" for r in controls),
                 complete_prescribed_case_grids=True, scaled_metrics_match=True,
                 paired_dense_csvs_match=True, state_budget_checked=True,
                 range_bands="Five-seed validation min/max only; no stress interval or connecting uncertainty band",
                 other_schedules_displayed=False, pooled=pooled)
    (out / "plot_audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    (out / "plot_source.py").write_bytes(Path(__file__).read_bytes())
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
