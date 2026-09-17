#!/usr/bin/env python3
"""Bounded postprocessing for the frozen first-quadrant experiment.

Usage: python PLOTS.py --run data/generated/quadrant_network_closure/run_001
This program never trains a model.  Missing runs are reported, never imputed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import shlex
import shutil
import subprocess
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


ORDERS = (1, 3, 5)
SEEDS = (11, 29, 47)
COLORS = {"reference": "#242C35", 1: "#7756A8", 3: "#D47716", 5: "#09846C"}
EXPECTED = ([f"net_n{n}_s{s}" for n in (2048, 8192) for s in SEEDS]
            + ["net_n8192_s11_half", "net_n2048_s11_double"]
            + [f"cl_N{n}_{q}" for n in ORDERS for q in ("base", "fine")]
            + ["cl_N3_base_half", "cl_N5_fine_half"])
STYLE = {1: "-", 3: "--", 5: "-."}
PSD_TOL = 1e-5


def as_float(x):
    return float(np.asarray(x))


def relative_gram(a, b):
    """Time x layer relative Frobenius error; reference b is the denominator."""
    numerator = np.linalg.norm(a - b, axis=(-2, -1))
    denominator = np.linalg.norm(b, axis=(-2, -1))
    return np.divide(numerator, denominator, out=np.full_like(numerator, np.nan),
                     where=denominator > 0)


def norm_metrics(a, b, dense_mask):
    g = relative_gram(a["grams"], b["grams"])
    gt = relative_gram(a["grams"][:, :, :16, :16], b["grams"][:, :, :16, :16])
    gc = relative_gram(a["grams"][:, :, 16:, 16:], b["grams"][:, :, 16:, 16:])
    dense_error = a["dense_predictions"][dense_mask] - b["dense_predictions"][dense_mask]
    return {
        "max_absolute_loss_difference": as_float(np.max(np.abs(a["loss"] - b["loss"]))),
        "final_absolute_loss_difference": as_float(abs(a["loss"][-1] - b["loss"][-1])),
        "max_absolute_panel_prediction_difference": as_float(np.max(np.abs(a["predictions"] - b["predictions"]))),
        "final_dense_circle_rmse": as_float(np.sqrt(np.mean(dense_error ** 2))),
        "final_dense_circle_max_absolute_difference": as_float(np.max(np.abs(dense_error))),
        "max_relative_gram_full_by_layer": g.max(axis=0).tolist(),
        "final_relative_gram_full_by_layer": g[-1].tolist(),
        "max_relative_gram_training_by_layer": gt.max(axis=0).tolist(),
        "final_relative_gram_training_by_layer": gt[-1].tolist(),
        "max_relative_gram_circle_by_layer": gc.max(axis=0).tolist(),
        "final_relative_gram_circle_by_layer": gc[-1].tolist(),
    }


def check_run(a, inputs, name):
    times = inputs["times"]
    nt, npanel, ndense = len(times), len(inputs["panel_u"]), len(inputs["dense_u"])
    expected_shapes = {"times": (nt,), "loss": (nt,), "predictions": (nt, npanel),
                       "grams": (nt, 2, npanel, npanel), "rms": (nt, 2),
                       "movement": (nt, 2), "dense_predictions": (ndense,)}
    errors = []
    for key, shape in expected_shapes.items():
        if key not in a or a[key].shape != shape:
            errors.append(f"{key}: expected shape {shape}, got {None if key not in a else a[key].shape}")
        elif not np.isfinite(a[key]).all():
            errors.append(f"{key}: nonfinite values")
    if errors:
        return {"passed": False, "errors": errors}
    if not np.array_equal(a["times"], times):
        errors.append("saved times do not equal the frozen input schedule")
    gram = a["grams"]
    symmetry_error = as_float(np.max(np.abs(gram - gram.swapaxes(-1, -2))))
    # Check the complete observation Gram at every saved time, in small batches.
    minimum_eigenvalue = np.inf
    for start in range(0, nt, 16):
        block = np.asarray(gram[start:start + 16], dtype=np.float64)
        eigenvalues = np.linalg.eigvalsh((block + block.swapaxes(-1, -2)) * .5)
        minimum_eigenvalue = min(minimum_eigenvalue, as_float(eigenvalues.min()))
    loss_increase = as_float(max(0, np.max(np.diff(a["loss"]))))
    reconstructed_loss = ((a["predictions"][:, :16] - inputs["labels"]) ** 2).mean(axis=1)
    loss_identity_error = as_float(np.max(np.abs(a["loss"] - reconstructed_loss)))
    # Stored activation RMS/movement use the training distribution, as do the ODEs.
    # The complete panel provides an independent Gram check of the raw RMS.
    rms_training = np.sqrt(np.maximum(0, np.diagonal(gram[:, :, :16, :16], axis1=-2, axis2=-1).mean(axis=-1)))
    rms_training_error = as_float(np.max(np.abs(a["rms"] - rms_training)))
    rms_identity_error = rms_training_error
    if symmetry_error > 1e-5:
        errors.append("Gram symmetry tolerance exceeded")
    if minimum_eigenvalue < -PSD_TOL:
        errors.append("Gram positive-semidefinite tolerance exceeded")
    if loss_increase > 1e-5:
        errors.append("loss nonincrease tolerance exceeded")
    if loss_identity_error > 1e-5:
        errors.append("MSE identity tolerance exceeded")
    if rms_identity_error > 1e-5:
        errors.append("training-distribution Gram/RMS identity tolerance exceeded")
    if np.min(a["movement"]) < -1e-8 or np.max(np.abs(a["movement"][0])) > 1e-5:
        errors.append("activation movement is negative or nonzero initially")
    return {"passed": not errors, "errors": errors,
            "maximum_gram_asymmetry": symmetry_error,
            "minimum_eigenvalue_all_saved_full_grams": minimum_eigenvalue,
            "maximum_loss_increase": loss_increase,
            "loss_identity_max_absolute_error": loss_identity_error,
            "rms_identity_max_absolute_error": rms_identity_error,
            "rms_scope": "training",
            "initial_activation_rms_by_layer": a["rms"][0].tolist(),
            "final_activation_rms_by_layer": a["rms"][-1].tolist(),
            "final_activation_movement_rms_by_layer": a["movement"][-1].tolist(),
            "final_loss": as_float(a["loss"][-1]),
            "final_training_max_absolute_residual": as_float(np.max(np.abs(a["predictions"][-1, :16] - inputs["labels"]))) }


def frozen_readout(a, labels):
    """Exact readout-only flow with the two initialized hidden layers frozen.

    The cross-Gram extension evaluates passive points without training on them.
    Eigenvalues below -PSD_TOL cause a hard failure; only tiny negatives clip.
    """
    initial_gram = np.asarray(a["grams"][0, 1], dtype=np.float64)
    train_gram = initial_gram[:16, :16]
    values, vectors = np.linalg.eigh((train_gram + train_gram.T) * .5)
    minimum = as_float(values.min())
    if minimum < -PSD_TOL:
        raise ValueError(f"Frozen-feature initial Gram fails PSD check: {minimum}")
    negative_count = int(np.count_nonzero(values < 0))
    values = np.maximum(values, 0)
    times = a["times"]
    residual = np.asarray(a["predictions"][0, :16], dtype=np.float64) - labels
    coefficients = vectors.T @ residual
    exponent = -2 * times[:, None] * values[None, :] / len(labels)
    train = labels + (np.exp(exponent) * coefficients) @ vectors.T
    factors = np.empty_like(exponent)
    positive = values > 0
    factors[:, positive] = np.expm1(exponent[:, positive]) / values[positive]
    factors[:, ~positive] = -2 * times[:, None] / len(labels)
    panel = np.asarray(a["predictions"][0], dtype=np.float64)[None, :] + ((factors * coefficients) @ vectors.T) @ initial_gram[:, :16].T
    # Use the spectral expression on the training set after projecting tiny negatives.
    panel[:, :16] = train
    loss = np.mean((train - labels) ** 2, axis=1)
    return {"predictions": panel, "loss": loss,
            "minimum_initial_training_gram_eigenvalue": minimum,
            "tiny_negative_eigenvalues_clipped": negative_count,
            "final_loss": as_float(loss[-1]),
            "initial_mse_identity_error": as_float(abs(loss[0] - a["loss"][0]))}


def aggregate(jobs, names):
    present = [name for name in names if name in jobs]
    if not present:
        return None, []
    keys = ("loss", "predictions", "grams", "rms", "movement", "dense_predictions")
    avg = {key: np.mean([jobs[name][key] for name in present], axis=0, dtype=np.float64) for key in keys}
    avg["times"] = jobs[present[0]]["times"]
    return avg, present


def check_control(jobs, high, low, dense_mask, quadrature=False):
    if high not in jobs or low not in jobs:
        return {"status": "missing", "comparison": [high, low]}
    result = norm_metrics(jobs[high], jobs[low], dense_mask)
    prediction_tolerance, gram_tolerance = (.02, .03) if quadrature else (.005, .01)
    passed = (result["max_absolute_loss_difference"] <= prediction_tolerance
              and result["max_absolute_panel_prediction_difference"] <= prediction_tolerance
              and result["final_dense_circle_max_absolute_difference"] <= prediction_tolerance
              and max(result["max_relative_gram_full_by_layer"]
                      + result["max_relative_gram_training_by_layer"]
                      + result["max_relative_gram_circle_by_layer"]) <= gram_tolerance)
    return {"status": "pass" if passed else "fail", "comparison": [high, low],
            "absolute_loss_and_prediction_tolerance": prediction_tolerance,
            "relative_gram_tolerance": gram_tolerance, **result}


def set_style():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.titlesize": 12, "axes.labelsize": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": "#A9B0B7", "axes.labelcolor": "#333C45",
                         "text.color": "#25303B", "xtick.color": "#4B5660",
                         "ytick.color": "#4B5660", "grid.color": "#DFE4E8",
                         "grid.linewidth": .65, "axes.axisbelow": True,
                         "savefig.facecolor": "white", "figure.facecolor": "white",
                         "pdf.fonttype": 42, "ps.fonttype": 42})


def finish(fig, directory, stem):
    fig.savefig(directory / f"{stem}.png", dpi=190, bbox_inches="tight")
    fig.savefig(directory / f"{stem}.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {stem}.png and .pdf", flush=True)


def shade(ax, x, arrays, **kwargs):
    if len(arrays) > 1:
        ax.fill_between(x, np.min(arrays, axis=0), np.max(arrays, axis=0),
                        color=COLORS["reference"], alpha=.14, linewidth=0, **kwargs)


def series(ax, times, ref, jobs, reference_names, key, layer=None, frozen=None):
    values = ref[key] if layer is None else ref[key][:, layer]
    samples = [jobs[name][key] if layer is None else jobs[name][key][:, layer]
               for name in reference_names]
    shade(ax, times, samples)
    ax.plot(times, values, color=COLORS["reference"], lw=2.4, label="Network, width 8192 mean")
    for n in ORDERS:
        name = f"cl_N{n}_base"
        if name in jobs:
            value = jobs[name][key] if layer is None else jobs[name][key][:, layer]
            ax.plot(times, value, color=COLORS[n], ls=STYLE[n], lw=1.9, label=f"Closure N={n}")
    if frozen is not None:
        ax.plot(times, frozen, color="#808A93", ls=(0, (3, 2)), lw=2, label="Frozen hidden layers: exact readout fit")
    ax.grid(alpha=.7)
    ax.set_xlim(times[0], times[-1])


def radial_plots(inputs, jobs, ref, reference_names, directory):
    theta = inputs["dense_theta"]
    order = np.argsort(theta)
    th = np.r_[theta[order], theta[order][0] + 2 * np.pi]
    close = lambda v: np.r_[np.asarray(v)[order], np.asarray(v)[order][0]]
    curves = [jobs[name]["dense_predictions"] for name in reference_names]
    curves += [jobs[f"cl_N{n}_base"]["dense_predictions"] for n in ORDERS if f"cl_N{n}_base" in jobs]
    maxabs = max(as_float(np.max(np.abs(v))) for v in curves)
    radius = 2. if all(np.min(2 + v) > 0 for v in curves) else maxabs + 1
    train_theta = np.arctan2(inputs["train_u"][:, 1], inputs["train_u"][:, 0])
    seed_values = [close(jobs[name]["dense_predictions"]) for name in reference_names]
    outer = radius + max(max(as_float(np.max(v)) for v in curves), 1) + .2

    def draw(ax, orders, label_reference=True):
        ax.set_theta_zero_location("E")
        ax.set_theta_direction(1)
        ax.plot(th, np.full_like(th, radius), color="#AAB2B9", ls=":", lw=1)
        if len(seed_values) > 1:
            ax.fill_between(th, radius + np.min(seed_values, axis=0), radius + np.max(seed_values, axis=0),
                            color=COLORS["reference"], alpha=.15, linewidth=0)
        ax.plot(th, radius + close(ref["dense_predictions"]), color=COLORS["reference"], lw=2.5,
                label="Network, width 8192 mean" if label_reference else None)
        for n in orders:
            name = f"cl_N{n}_base"
            if name in jobs:
                ax.plot(th, radius + close(jobs[name]["dense_predictions"]), color=COLORS[n],
                        ls=STYLE[n], lw=2, label=f"Closure N={n}")
        ax.scatter(train_theta, np.full(16, radius), s=19, marker="o", facecolors="white",
                   edgecolors="#353F48", linewidths=.8, zorder=7, label="Training directions at R")
        for sign, color, marker in ((1, "#2369A2", "+"), (-1, "#BD3F47", "_")):
            take = inputs["labels"] == sign
            ax.scatter(train_theta[take], radius + inputs["labels"][take], color=color, marker=marker,
                       s=75, linewidths=1.5, zorder=8, label=f"Target {'+1' if sign == 1 else '−1'} at R+y")
        ax.set_ylim(0, outer)
        ax.set_thetagrids(np.arange(0, 360, 45))
        ax.set_rlabel_position(215)
        ax.grid(alpha=.75)
        ax.spines["polar"].set_color("#CDD3D8")

    fig, ax = plt.subplots(figsize=(9.3, 7.4), subplot_kw={"projection": "polar"})
    draw(ax, ORDERS)
    ax.set_title(f"Final output around the entire circle · T=100\nRadius = {radius:.3g} + f(θ)", pad=25)
    handles, labels = ax.get_legend_handles_labels()
    handles.insert(1, Line2D([0], [0], color=COLORS["reference"], alpha=.25, lw=8))
    labels.insert(1, f"Network seed range ({len(reference_names)} seeds)")
    ax.legend(handles, labels, loc="upper left", bbox_to_anchor=(1.07, 1.02), frameon=False, fontsize=9)
    fig.text(.50, .025, "Closures share Q=2048, P=1024. Equal angular and radial scales.\nSee the angle plot for pointwise differences.",
             ha="center", fontsize=9, color="#586570")
    finish(fig, directory, "radial_overlay")

    fig, axes = plt.subplots(2, 2, figsize=(10.5, 10.5), subplot_kw={"projection": "polar"}, constrained_layout=True)
    for ax, n in zip(axes.ravel(), (None, *ORDERS)):
        draw(ax, () if n is None else (n,))
        ax.set_title("Network reference + seed range" if n is None else f"N={n} and network reference", pad=22)
    fig.suptitle(f"Final radial outputs · common radius R={radius:.3g} · T=100", fontsize=15)
    finish(fig, directory, "radial_individual")
    return radius


def angle_plots(inputs, jobs, ref, reference_names, directory):
    theta = np.degrees(inputs["dense_theta"])
    order = np.argsort(theta)
    theta = theta[order]
    train_theta = np.degrees(np.arctan2(inputs["train_u"][:, 1], inputs["train_u"][:, 0]))
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 4.8), gridspec_kw={"width_ratios": [1.65, 1]}, constrained_layout=True)
    for ax, end in zip(axes, (360, 90)):
        shade(ax, theta, [jobs[name]["dense_predictions"][order] for name in reference_names])
        ax.plot(theta, ref["dense_predictions"][order], color=COLORS["reference"], lw=2.4, label="Network mean ± seed range")
        for n in ORDERS:
            name = f"cl_N{n}_base"
            if name in jobs:
                ax.plot(theta, jobs[name]["dense_predictions"][order], color=COLORS[n], ls=STYLE[n], lw=1.8, label=f"Closure N={n}")
        ax.scatter(train_theta, inputs["labels"], marker="x", color="#232C34", s=31, lw=1.4, zorder=7, label="Training targets")
        ax.axhline(0, color="#9DA7AE", lw=.7)
        ax.set(xlim=(0, end), xlabel="Angle θ (degrees)", ylabel="Final output f(θ)")
        if end == 90:
            use = theta <= 90 + 1e-10
            values = [ref["dense_predictions"][order][use], inputs["labels"]]
            values += [jobs[f"cl_N{n}_base"]["dense_predictions"][order][use] for n in ORDERS if f"cl_N{n}_base" in jobs]
            low, high = min(np.min(v) for v in values), max(np.max(v) for v in values)
            ax.set_ylim(low - .10 * (high - low), high + .10 * (high - low))
            ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
        else:
            ax.set_xticks(np.arange(0, 361, 60))
        ax.set_title("Entire circle" if end == 360 else "Training quadrant")
        ax.grid(alpha=.7)
    axes[0].legend(loc="lower left", fontsize=9, framealpha=.94)
    fig.suptitle("Final output versus angle · T=100 · common base quadrature", fontsize=15)
    finish(fig, directory, "output_vs_angle")

    fig, ax = plt.subplots(figsize=(10, 4.4), constrained_layout=True)
    ax.scatter(train_theta, inputs["labels"], s=90, marker="x", color="#17212B", lw=2, label="Targets", zorder=5)
    samples = [jobs[name]["predictions"][-1, :16] for name in reference_names]
    minimum, maximum = np.min(samples, axis=0), np.max(samples, axis=0)
    center = ref["predictions"][-1, :16]
    ax.errorbar(train_theta, center, yerr=np.array([center - minimum, maximum - center]),
                fmt="o", color=COLORS["reference"], ms=4, capsize=3, label="Network mean and seed range", zorder=6)
    for n, marker in zip(ORDERS, ("s", "^", "D")):
        name = f"cl_N{n}_base"
        if name in jobs:
            ax.scatter(train_theta, jobs[name]["predictions"][-1, :16], s=28,
                       marker=marker, facecolors="none", edgecolors=COLORS[n], lw=1.2, label=f"Closure N={n}", zorder=7)
    ax.set(xlim=(-2, 92), xlabel="Training angle θ (degrees)", ylabel="Final prediction", title="Predictions at all sixteen training inputs · T=100")
    ax.grid(alpha=.7)
    ax.legend(ncol=3, frameon=False, loc="upper center", bbox_to_anchor=(.5, -.17), fontsize=9)
    finish(fig, directory, "training_predictions")


def dataset_plot(inputs, directory):
    u, labels = inputs["train_u"], inputs["labels"]
    fig, ax = plt.subplots(figsize=(6.4, 6.4), constrained_layout=True)
    theta = np.linspace(0, np.pi / 2, 301)
    ax.plot(np.cos(theta), np.sin(theta), color="#D1D7DD", lw=2)
    for sign, color in ((1, "#2369A2"), (-1, "#BD3F47")):
        select = labels == sign
        ax.scatter(u[select, 0], u[select, 1], color=color, edgecolors="white", s=73, lw=1, label=f"Label {'+1' if sign == 1 else '−1'}", zorder=4)
    for k, degrees in enumerate((2.5, 30, 60, 87.5)):
        direction = np.array([np.cos(np.radians(degrees)), np.sin(np.radians(degrees))])
        ax.plot([0, direction[0]], [0, direction[1]], ls=":", color="#BEC6CD", lw=.8)
        pos = 1.12 * direction
        ax.text(*pos, ("+", "−", "+", "−")[k], color=("#2369A2", "#BD3F47")[k % 2],
                ha="center", va="center", fontsize=18, weight="bold")
    ax.set(xlim=(-.07, 1.21), ylim=(-.07, 1.21), xlabel="u₁ = cos θ", ylabel="u₂ = sin θ",
           title="Sixteen training inputs in the first quadrant\nFour clusters, alternating labels +, −, +, −")
    ax.set_aspect("equal")
    ax.grid(alpha=.55)
    ax.legend(frameon=False, loc="lower left", fontsize=10)
    finish(fig, directory, "training_dataset")


def dynamics_plots(inputs, jobs, ref, reference_names, frozen, directory):
    times = inputs["times"]
    baseline_loss = np.mean([frozen[name]["loss"] for name in reference_names if name in frozen], axis=0)
    fig = plt.figure(figsize=(12.8, 11.2), constrained_layout=True)
    gs = fig.add_gridspec(3, 2, height_ratios=[1.05, 1, 1])
    ax = fig.add_subplot(gs[0, :])
    series(ax, times, ref, jobs, reference_names, "loss", frozen=baseline_loss)
    ax.set(ylabel="Mean squared training loss", title="Training loss")
    ax.set_yscale("log")
    ax.legend(ncol=3, frameon=False, fontsize=9)
    for row, sl, panel_label in ((1, slice(0, 16), "Training inputs"), (2, slice(16, None), "Passive circle")):
        target = ref["grams"][:, :, sl, sl]
        frozen_gram = relative_gram(np.broadcast_to(target[:1], target.shape), target)
        for layer in range(2):
            ax = fig.add_subplot(gs[row, layer])
            ax.plot(times, frozen_gram[:, layer], color="#808A93", ls=(0, (3, 2)), lw=2.1, label="Frozen Gref(0)")
            for n in ORDERS:
                name = f"cl_N{n}_base"
                if name in jobs:
                    error = relative_gram(jobs[name]["grams"][:, :, sl, sl], target)
                    ax.plot(times, error[:, layer], color=COLORS[n], ls=STYLE[n], lw=1.9, label=f"Closure N={n}")
            ax.set(xlim=(0, times[-1]), ylim=(0, None), xlabel="Physical time", ylabel="Relative Gram error",
                   title=f"{panel_label} · hidden layer {layer + 1}")
            ax.grid(alpha=.7)
            if row == 1 and layer == 0:
                ax.legend(frameon=False, fontsize=9)
    fig.suptitle("Loss and activation-Gram agreement with the width-8192 mean", fontsize=15)
    finish(fig, directory, "loss_and_gram_errors")

    fig, axes = plt.subplots(2, 2, figsize=(11.7, 7.7), constrained_layout=True)
    for row, key in enumerate(("rms", "movement")):
        for layer in range(2):
            ax = axes[row, layer]
            series(ax, times, ref, jobs, reference_names, key, layer=layer)
            ax.set(xlabel="Physical time", ylabel="Activation RMS" if row == 0 else "RMS change from initialization", ylim=(0, None),
                   title=f"Hidden layer {layer + 1} · {'raw activation' if row == 0 else 'activation movement'}")
    axes[0, 0].legend(frameon=False, fontsize=9)
    fig.suptitle("Activation magnitude and movement · mean and network seed range", fontsize=15)
    finish(fig, directory, "activation_rms_and_movement")

    selections = [int(np.argmin(abs(times - t))) for t in (0, 25, 50, 100)]
    models = [("Network mean", ref)] + [(f"Closure N={n}", jobs[f"cl_N{n}_base"]) for n in ORDERS if f"cl_N{n}_base" in jobs]
    for layer in range(2):
        scale = max(np.max(np.abs(a["grams"][selections, layer, :16, :16])) for _, a in models)
        fig, axes = plt.subplots(len(models), 4, figsize=(11.5, 2.7 * len(models)), squeeze=False, constrained_layout=True)
        for row, (label, a) in enumerate(models):
            for col, index in enumerate(selections):
                ax = axes[row, col]
                im = ax.imshow(a["grams"][index, layer, :16, :16], cmap="RdBu_r", vmin=-scale, vmax=scale, interpolation="nearest")
                ax.set_xticks([1.5, 5.5, 9.5, 13.5], ["1", "2", "3", "4"])
                ax.set_yticks([1.5, 5.5, 9.5, 13.5], ["1", "2", "3", "4"])
                for boundary in (3.5, 7.5, 11.5):
                    ax.axhline(boundary, color="white", lw=.55, alpha=.7)
                    ax.axvline(boundary, color="white", lw=.55, alpha=.7)
                if row == 0:
                    ax.set_title(f"t = {times[index]:g}")
                if col == 0:
                    ax.set_ylabel(label + "\nTraining cluster")
                if row == len(models) - 1:
                    ax.set_xlabel("Training cluster")
        fig.colorbar(im, ax=axes, shrink=.65, pad=.02, label="Mean activation product")
        fig.suptitle(f"Training activation Gram · hidden layer {layer + 1}\nFull 16 × 16 matrices; one shared color scale", fontsize=15)
        finish(fig, directory, f"gram_heatmaps_layer{layer + 1}")


def control_plots(inputs, jobs, comparisons, directory, stem, title, pred_tol, gram_tol):
    usable = [(label, high, low, color) for label, high, low, color in comparisons if high in jobs and low in jobs]
    if not usable:
        return
    times = inputs["times"]
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.1), constrained_layout=True)
    for label, high, low, color in usable:
        a, b = jobs[high], jobs[low]
        curves = [np.abs(a["loss"] - b["loss"]), np.max(np.abs(a["predictions"] - b["predictions"]), axis=1)]
        grams = [relative_gram(a["grams"][:, :, sl, sl], b["grams"][:, :, sl, sl]) for sl in (slice(None), slice(0, 16), slice(16, None))]
        curves.append(np.max(np.concatenate(grams, axis=1), axis=1))
        for ax, curve in zip(axes, curves):
            ax.plot(times, curve, lw=1.8, label=label, color=color)
    for ax, label, tol in zip(axes, ("Absolute loss difference", "Maximum absolute panel output difference", "Largest relative Gram difference"), (pred_tol, pred_tol, gram_tol)):
        ax.axhline(tol, color="#626C75", ls=":", lw=1.4, label=f"Gate {tol:g}")
        ax.set(xlim=(0, times[-1]), ylim=(0, None), xlabel="Physical time", ylabel=label)
        ax.grid(alpha=.7)
    axes[0].legend(frameon=False, fontsize=8)
    fig.suptitle(title, fontsize=14)
    finish(fig, directory, stem)


def width_plot(inputs, jobs, ref, reference_names, width_ref, small_names, directory):
    if width_ref is None:
        return
    times = inputs["times"]
    fig, axes = plt.subplots(1, 3, figsize=(13.7, 4.4), constrained_layout=True)
    for data, names, color, width in ((width_ref, small_names, "#477FA1", 2048), (ref, reference_names, COLORS["reference"], 8192)):
        values = [jobs[name]["loss"] for name in names]
        axes[0].fill_between(times, np.min(values, axis=0), np.max(values, axis=0), color=color, alpha=.15)
        axes[0].plot(times, data["loss"], color=color, lw=2, label=f"Width {width}: mean + range")
    axes[0].set(yscale="log", xlabel="Physical time", ylabel="Training MSE", title="Width and seed uncertainty")
    theta = np.degrees(inputs["dense_theta"])
    for names, color, width in ((small_names, "#477FA1", 2048), (reference_names, COLORS["reference"], 8192)):
        differences = [jobs[name]["dense_predictions"] - ref["dense_predictions"] for name in names]
        axes[1].fill_between(theta, np.min(differences, axis=0), np.max(differences, axis=0), color=color, alpha=.18)
        axes[1].plot(theta, np.mean(differences, axis=0), color=color, lw=1.8, label=f"Width {width}")
    axes[1].set(xlim=(0, 360), xlabel="Angle θ (degrees)", ylabel="Final output minus width-8192 mean", title="Final circle output uncertainty")
    width_errors = relative_gram(width_ref["grams"], ref["grams"])
    for layer, color in enumerate(("#7756A8", "#09846C")):
        axes[2].plot(times, width_errors[:, layer], color=color, lw=2, label=f"Width means, layer {layer + 1}")
        spread = np.max([relative_gram(jobs[name]["grams"], ref["grams"])[:, layer] for name in reference_names], axis=0)
        axes[2].plot(times, spread, color=color, lw=1.3, ls="--", label=f"8192 max seed deviation, layer {layer + 1}")
    axes[2].set(xlabel="Physical time", ylabel="Relative full-panel Gram difference", title="Gram width and seed uncertainty", ylim=(0, None))
    for ax in axes:
        ax.grid(alpha=.65)
        ax.legend(fontsize=7.4, frameon=False)
    finish(fig, directory, "width_and_seed_uncertainty")


def analyze(run):
    run = run.resolve()
    for product in ("analysis.json", "frozen_readout_baselines.npz"):
        if (run / product).exists():
            raise FileExistsError(f"Refusing to overwrite existing postprocessing product: {run / product}")
    directory = run / "figures"
    directory.mkdir(exist_ok=True)
    with np.load(run / "inputs.npz", allow_pickle=False) as data:
        inputs = {key: data[key] for key in data.files}
    dense_step = 2 * np.pi / 1440
    grid_coordinates = inputs["dense_theta"] / dense_step
    if "dense_uniform_indices" in inputs:
        indices = np.asarray(inputs["dense_uniform_indices"], dtype=np.int64)
        if indices.shape != (1440,) or len(np.unique(indices)) != 1440:
            raise ValueError("dense_uniform_indices must contain exactly 1440 distinct indices")
        dense_mask = np.zeros(len(inputs["dense_theta"]), dtype=bool)
        dense_mask[indices] = True
        if not np.allclose(inputs["dense_theta"][indices], np.arange(1440) * dense_step, rtol=0, atol=1e-12):
            raise ValueError("Explicit uniform dense indices do not select the frozen uniform circle")
    else:
        dense_mask = np.isclose(grid_coordinates, np.rint(grid_coordinates), rtol=0, atol=1e-8)
    if int(dense_mask.sum()) != 1440:
        raise ValueError(f"Expected exactly 1440 uniform-circle evaluation angles; found {dense_mask.sum()}")
    if inputs["train_u"].shape != (16, 2) or not np.array_equal(inputs["labels"], np.repeat([1, -1, 1, -1], 4)):
        raise ValueError("Training inputs/labels differ from the frozen design")
    if not np.allclose(inputs["times"], np.arange(201) / 2, atol=0, rtol=0):
        raise ValueError("Input schedule differs from 0, .5, ..., 100")
    jobs, records, correctness, unreadable = {}, {}, {}, {}
    for name in EXPECTED:
        path = run / name / "trajectories.npz"
        record = run / name / "record.json"
        if record.exists():
            records[name] = json.loads(record.read_text())
        if not path.exists():
            continue
        print(f"Loading and checking {name}", flush=True)
        try:
            with np.load(path, allow_pickle=False) as data:
                a = {key: data[key] for key in data.files}
            correctness[name] = check_run(a, inputs, name)
            if not correctness[name]["passed"]:
                unreadable[name] = correctness[name]["errors"]
                continue
            jobs[name] = a
        except (ValueError, KeyError, OSError) as exc:
            unreadable[name] = str(exc)
    ref, reference_names = aggregate(jobs, [f"net_n8192_s{s}" for s in SEEDS])
    width_ref, small_names = aggregate(jobs, [f"net_n2048_s{s}" for s in SEEDS])
    output = {"study": "quadrant_network_closure", "run": str(run),
              "postprocessing_provenance": {
                  "source_path": str(Path(__file__).resolve()),
                  "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "inputs_sha256": hashlib.sha256((run / "inputs.npz").read_bytes()).hexdigest(),
                  "command": shlex.join(getattr(sys, "orig_argv", [sys.executable, *sys.argv])),
                  "versions": {"python": platform.python_version(), "numpy": np.__version__, "matplotlib": matplotlib.__version__}},
              "expected_jobs": EXPECTED, "available_jobs": list(jobs),
              "missing_or_rejected_jobs": [name for name in EXPECTED if name not in jobs],
              "unreadable_or_rejected": unreadable, "correctness_checks": correctness,
              "reference_jobs": reference_names, "reference_complete": len(reference_names) == 3,
              "uniform_dense_circle_count": int(dense_mask.sum()),
              "interpretation": "Finite-horizon, finite-width, finite-quadrature empirical comparisons; no hierarchy convergence claim.",
              "controls": {}, "closures": {}, "frozen_readout": {},
              "seed_spread": {}, "source_job_status": {name: rec.get("status") for name, rec in records.items()}}
    frozen, baseline_arrays = {}, {"times": inputs["times"]}
    for name, a in jobs.items():
        if name.startswith("net_"):
            f = frozen_readout(a, inputs["labels"])
            frozen[name] = f
            output["frozen_readout"][name] = {key: value for key, value in f.items() if key not in ("predictions", "loss")}
            output["frozen_readout"][name]["actual_network_final_loss"] = as_float(a["loss"][-1])
            output["frozen_readout"][name]["final_circle_rmse_vs_trained_network"] = as_float(np.sqrt(np.mean((f["predictions"][-1, 16:] - a["predictions"][-1, 16:]) ** 2)))
            baseline_arrays[name + "_predictions"] = f["predictions"]
            baseline_arrays[name + "_loss"] = f["loss"]
    np.savez_compressed(run / "frozen_readout_baselines.npz", **baseline_arrays)
    controls = output["controls"]
    controls["network_step"] = check_control(jobs, "net_n8192_s11_half", "net_n8192_s11", dense_mask)
    controls["network_precision"] = check_control(jobs, "net_n2048_s11_double", "net_n2048_s11", dense_mask)
    controls["closure_N3_step"] = check_control(jobs, "cl_N3_base_half", "cl_N3_base", dense_mask)
    controls["closure_N5_step"] = check_control(jobs, "cl_N5_fine_half", "cl_N5_fine", dense_mask)
    for n in ORDERS:
        controls[f"closure_N{n}_quadrature"] = check_control(jobs, f"cl_N{n}_fine", f"cl_N{n}_base", dense_mask, quadrature=True)
    if ref is not None:
        output["reference_final_loss"] = as_float(ref["loss"][-1])
        output["reference_final_frozen_readout_mean_loss"] = as_float(np.mean([frozen[name]["loss"][-1] for name in reference_names]))
        for n in ORDERS:
            name = f"cl_N{n}_base"
            if name not in jobs:
                continue
            metrics = norm_metrics(jobs[name], ref, dense_mask)
            ratios = [metrics["max_absolute_loss_difference"] / .05,
                      metrics["final_dense_circle_rmse"] / .10,
                      *[value / .10 for value in metrics["max_relative_gram_training_by_layer"]]]
            result = "strong agreement" if max(ratios) <= 1 else "clear mismatch" if max(ratios) > 2 else "inconclusive"
            metrics["raw_empirical_criterion"] = result
            metrics["final_loss"] = as_float(jobs[name]["loss"][-1])
            metrics["quadrature_gate"] = controls[f"closure_N{n}_quadrature"]["status"]
            metrics["interpretation_qualification"] = ("Population accuracy remains unresolved because the quadrature gate failed."
                if metrics["quadrature_gate"] == "fail" else "All applicable discretization controls and finite-width uncertainty still qualify this empirical comparison.")
            metrics["reference_seed_dense_rmse"] = {seed_name: as_float(np.sqrt(np.mean((jobs[name]["dense_predictions"][dense_mask] - jobs[seed_name]["dense_predictions"][dense_mask]) ** 2))) for seed_name in reference_names}
            metrics["gram_vs_frozen_baseline"] = {}
            for scope, sl in (("training", slice(0, 16)), ("circle", slice(16, None))):
                target = ref["grams"][:, :, sl, sl]
                closure_error = relative_gram(jobs[name]["grams"][:, :, sl, sl], target)
                baseline_error = relative_gram(np.broadcast_to(target[:1], target.shape), target)
                metrics["gram_vs_frozen_baseline"][scope] = {
                    "frozen_max_relative_error_by_layer": baseline_error.max(axis=0).tolist(),
                    "frozen_final_relative_error_by_layer": baseline_error[-1].tolist(),
                    "closure_fraction_postinitial_times_better_by_layer": np.mean(closure_error[1:] < baseline_error[1:], axis=0).tolist(),
                    "closure_minus_frozen_final_error_by_layer": (closure_error[-1] - baseline_error[-1]).tolist()}
            output["closures"][str(n)] = metrics
        if width_ref is not None:
            output["width_mean_2048_vs_8192"] = norm_metrics(width_ref, ref, dense_mask)
        for width, names, center in ((2048, small_names, width_ref), (8192, reference_names, ref)):
            if center is None:
                continue
            losses = np.array([jobs[name]["loss"] for name in names])
            predictions = np.array([jobs[name]["predictions"] for name in names])
            dense_predictions = np.array([jobs[name]["dense_predictions"][dense_mask] for name in names])
            output["seed_spread"][str(width)] = {
                "jobs": names, "max_loss_range": as_float(np.ptp(losses, axis=0).max()),
                "final_loss_range": as_float(np.ptp(losses[:, -1])),
                "max_panel_prediction_range": as_float(np.ptp(predictions, axis=0).max()),
                "final_dense_circle_max_prediction_range": as_float(np.ptp(dense_predictions, axis=0).max()),
                "final_dense_circle_rmse_range": as_float(np.sqrt(np.mean(np.ptp(dense_predictions, axis=0) ** 2))),
                "per_seed_vs_width_mean": {name: norm_metrics(jobs[name], center, dense_mask) for name in names}}
        set_style()
        dataset_plot(inputs, directory)
        output["radial_offset_R"] = radial_plots(inputs, jobs, ref, reference_names, directory)
        angle_plots(inputs, jobs, ref, reference_names, directory)
        dynamics_plots(inputs, jobs, ref, reference_names, frozen, directory)
        width_plot(inputs, jobs, ref, reference_names, width_ref, small_names, directory)
    else:
        output["analysis_warning"] = "No validated width-8192 reference was available; primary comparison plots omitted."
        set_style()
        dataset_plot(inputs, directory)
    control_plots(inputs, jobs,
        [(f"N={n}: fine − base", f"cl_N{n}_fine", f"cl_N{n}_base", COLORS[n]) for n in ORDERS],
        directory, "quadrature_controls", "Quadrature controls · fine Q=4096, P=2048 versus common base", .02, .03)
    control_plots(inputs, jobs,
        [("Network 8192: half step", "net_n8192_s11_half", "net_n8192_s11", "#242C35"),
         ("Network 2048: float64", "net_n2048_s11_double", "net_n2048_s11", "#477FA1"),
         ("N=3 base: half step", "cl_N3_base_half", "cl_N3_base", COLORS[3]),
         ("N=5 fine: half step", "cl_N5_fine_half", "cl_N5_fine", COLORS[5])],
        directory, "step_and_precision_controls", "Time-step and floating-point controls", .005, .01)
    pdf_order = ["radial_overlay", "output_vs_angle", "loss_and_gram_errors",
                 "gram_heatmaps_layer1", "gram_heatmaps_layer2", "radial_individual",
                 "training_dataset", "training_predictions", "activation_rms_and_movement",
                 "width_and_seed_uncertainty", "quadrature_controls", "step_and_precision_controls"]
    pdfs = [directory / (stem + ".pdf") for stem in pdf_order if (directory / (stem + ".pdf")).exists()]
    pdfunite = shutil.which("pdfunite")
    if pdfunite is not None and pdfs:
        subprocess.run([pdfunite, *map(str, pdfs), str(directory / "all_plots.pdf")], check=True)
        output["combined_pdf"] = "figures/all_plots.pdf"
    else:
        output["combined_pdf_warning"] = "pdfunite was unavailable or no PDF figures were generated."
    output["figure_files"] = [str(path.relative_to(run)) for path in sorted(directory.glob("*"))]
    output["metric_conventions"] = {
        "reference": "Arithmetic mean of valid width-8192 seeds; losses are averaged before comparison.",
        "seed_band": "Pointwise min/max across the three prescribed seeds, not a confidence interval.",
        "dense_circle_rmse": "Uniform mean over exactly 1440 directions, selected by frozen dense_uniform_indices when supplied; appended training directions excluded.",
        "gram_errors": "Relative Frobenius norm using the contemporaneous reference Gram denominator.",
        "control_gate": "Tests maximum absolute loss, saved-panel and final dense-circle output differences and maximum relative Grams on full, training and passive-circle panels.",
        "frozen_readout": "Both hidden layers fixed at each network's own initialization, exact physical-time readout flow exp(-2t G2(0)/16).",
        "rms_scope": "Training-distribution RMS, checked against the mean diagonal of each training Gram."}
    (run / "analysis.json").write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
    print(f"Analysis complete: {run / 'analysis.json'}", flush=True)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, type=Path)
    args = parser.parse_args()
    analyze(args.run)


if __name__ == "__main__":
    main()
