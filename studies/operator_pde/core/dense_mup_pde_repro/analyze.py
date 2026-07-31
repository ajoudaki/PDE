#!/usr/bin/env python3
"""Audit-fixed analysis for the genuine operator-Galerkin PDE runs."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from dense_pde import (
    PDESpec,
    PDEState,
    build_hybrid_quadrature,
    build_quadrature,
    solve_fields,
)

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "results" / "raw"
PROCESSED = ROOT / "results" / "processed"
FIGURES = ROOT / "figures"
PROCESSED.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)


def load(name: str) -> np.lib.npyio.NpzFile:
    return np.load(RAW / name)


def interpolate_grams(grams: np.ndarray, target_nodes: int) -> np.ndarray:
    source_nodes = grams.shape[1]
    source_s = np.linspace(0.0, 1.0, source_nodes)
    target_s = np.linspace(0.0, 1.0, target_nodes)
    output = np.empty((grams.shape[0], target_nodes, 3, 3))
    for time in range(grams.shape[0]):
        for r in range(3):
            for q in range(3):
                output[time, :, r, q] = np.interp(
                    target_s, source_s, grams[time, :, r, q]
                )
    return output


def max_curve_norm(array: np.ndarray) -> float:
    return float(np.max(np.linalg.norm(array, axis=(-2, -1))))


def reference_metrics(
    pde: np.lib.npyio.NpzFile,
    reference: np.lib.npyio.NpzFile,
) -> dict[str, float]:
    pde_grams = interpolate_grams(
        pde["grams"], reference["grams_mean"].shape[1]
    )
    f_gap = np.linalg.norm(pde["f"] - reference["f_mean"], axis=-1)
    gram_gap = np.linalg.norm(
        pde_grams - reference["grams_mean"], axis=(-2, -1)
    )
    theta_gap = np.linalg.norm(
        pde["theta"] - reference["theta_mean"], axis=(-2, -1)
    )
    pde_increment = pde_grams - pde_grams[0:1]
    reference_increment = (
        reference["grams_mean"] - reference["grams_mean"][0:1]
    )
    increment_gap = np.linalg.norm(
        pde_increment - reference_increment, axis=(-2, -1)
    )
    y = np.array([0.8, -0.55, 0.35])
    reference_loss = 0.5 * np.sum(
        (reference["f_mean"] - y) ** 2, axis=-1
    )
    return {
        "max_output_gap": float(np.max(f_gap)),
        "max_output_gap_after_t0": float(np.max(f_gap[1:])),
        "max_loss_of_mean_gap": float(
            np.max(np.abs(pde["loss"] - reference_loss))
        ),
        "max_absolute_gram_gap": float(np.max(gram_gap)),
        "terminal_absolute_gram_gap": float(np.max(gram_gap[-1])),
        "max_gram_increment_gap": float(np.max(increment_gap)),
        "terminal_gram_increment_gap": float(
            np.max(increment_gap[-1])
        ),
        "max_theta_gap": float(np.max(theta_gap)),
        "reference_feature_motion": float(
            np.max(
                np.linalg.norm(
                    reference_increment[-1], axis=(-2, -1)
                )
            )
        ),
        "pde_feature_motion": float(
            np.max(
                np.linalg.norm(
                    pde_increment[-1], axis=(-2, -1)
                )
            )
        ),
    }


def compare(
    coarse: np.lib.npyio.NpzFile,
    fine: np.lib.npyio.NpzFile,
    fine_limit: int | None = None,
) -> dict[str, float]:
    if fine_limit is None:
        fine_limit = coarse["times"].size
    fine_grams = fine["grams"][:fine_limit]
    coarse_grams = interpolate_grams(coarse["grams"], fine_grams.shape[1])
    return {
        "output": float(
            np.max(
                np.linalg.norm(
                    coarse["f"] - fine["f"][:fine_limit], axis=-1
                )
            )
        ),
        "grams": float(
            np.max(
                np.linalg.norm(
                    coarse_grams - fine_grams, axis=(-2, -1)
                )
            )
        ),
        "theta": float(
            np.max(
                np.linalg.norm(
                    coarse["theta"] - fine["theta"][:fine_limit],
                    axis=(-2, -1),
                )
            )
        ),
    }


def final_projected_p_energy(run: np.lib.npyio.NpzFile) -> float:
    metadata = json.loads(str(run["metadata_json"]))
    spec = PDESpec(
        X=np.asarray(metadata["X"]),
        y=np.asarray(metadata["y"]),
        basis_size=metadata["basis_size_P"],
        depth_nodes=metadata["depth_nodes_N"],
        base_points=metadata["base_quadrature_M"],
        fast_points=metadata["fast_quadrature_R"],
        quadrature_seed=metadata["quadrature_seed"],
        sigma_w=metadata["sigma_w"],
        A=metadata["A"],
        gamma=metadata["gamma"],
    )
    if metadata["quadrature"] == "hybrid":
        quadrature = build_hybrid_quadrature(
            spec, base_order=metadata["base_order"]
        )
    elif metadata["quadrature"] == "sobol":
        quadrature = build_quadrature(spec)
    else:
        raise ValueError("projected-p audit currently supports QMC/hybrid")
    state = PDEState(
        B=run["final_B"],
        a=run["final_a"],
        c=run["final_c"],
    )
    fields = solve_fields(state, spec, quadrature)
    pcoef = np.einsum(
        "ip,lim,i->lpm",
        quadrature.phi,
        fields.p,
        quadrature.base_weights,
        optimize=True,
    )
    projected = np.einsum("lpm,lpn->lmn", pcoef, pcoef, optimize=True)
    full = np.einsum(
        "i,lim,lin->lmn",
        quadrature.base_weights,
        fields.p,
        fields.p,
        optimize=True,
    )
    ratio = np.diagonal(projected, axis1=1, axis2=2) / np.diagonal(
        full, axis1=1, axis2=2
    )
    return float(np.min(ratio))


def main() -> None:
    primary = load(
        "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz"
    )
    tail = load(
        "pde_QMC_P5_N16_M256_R128_s20260723_dt0p1_T24"
        "_from8_to32.npz"
    )
    reference_256_32_s64 = np.load(
        PROCESSED / "exact_combined_n256_L32_S64.npz"
    )
    reference_256_32 = np.load(
        PROCESSED / "exact_combined_n256_L32_S128.npz"
    )
    reference_256_64_s16 = load(
        "exact_ensemble_n256_L64_S16_seed7000_dt0p02_T8p0.npz"
    )
    reference_256_64 = np.load(
        PROCESSED / "exact_combined_n256_L64_S64.npz"
    )
    reference_512_32 = load(
        "exact_ensemble_n512_L32_S16_seed14000_dt0p02_T8p0.npz"
    )
    reference_64_32 = load(
        "exact_ensemble_n64_L32_S64_seed4000_dt0p02_T8p0.npz"
    )
    reference_128_32 = np.load(
        PROCESSED / "exact_combined_n128_L32_S96.npz"
    )

    summary: dict[str, object] = {
        "scientific_label": (
            "genuine width-independent operator-Galerkin PDE experiment; "
            "not a simulation of the un-emitted K/J/N response compiler"
        ),
        "primary_pde": json.loads(str(primary["metadata_json"])),
        "reference_comparisons": {
            "n64_L32_S64": reference_metrics(primary, reference_64_32),
            "n128_L32_S96": reference_metrics(primary, reference_128_32),
            "n256_L32_S64": reference_metrics(
                primary, reference_256_32_s64
            ),
            "n256_L32_S128": reference_metrics(primary, reference_256_32),
            "n256_L64_S16": reference_metrics(
                primary, reference_256_64_s16
            ),
            "n256_L64_S64": reference_metrics(primary, reference_256_64),
            "n512_L32_S16": reference_metrics(primary, reference_512_32),
        },
    }

    # Plateau continuation.
    tail_gram_drift = np.linalg.norm(
        tail["grams"] - tail["grams"][0:1], axis=(-2, -1)
    )
    summary["plateau"] = {
        "start_time": float(tail["times"][0]),
        "end_time": float(tail["times"][-1]),
        "max_output_drift": float(
            np.max(np.linalg.norm(tail["f"] - tail["f"][0], axis=-1))
        ),
        "max_all_depth_gram_drift": float(np.max(tail_gram_drift)),
        "max_theta_drift": float(
            np.max(
                np.linalg.norm(
                    tail["theta"] - tail["theta"][0], axis=(-2, -1)
                )
            )
        ),
        "max_residual": float(np.max(tail["residual_norm"])),
        "max_abs_loss_derivative": float(np.max(np.abs(tail["loss_dot"]))),
    }

    # Integrator refinement.
    dt_02 = load(
        "pde_QMC_P5_N16_M64_R32_s20260723_dt0p02_T4.npz"
    )
    dt_01 = load(
        "pde_QMC_P5_N16_M64_R32_s20260723_dt0p01_T4.npz"
    )
    dt_005 = load(
        "pde_QMC_P5_N16_M64_R32_s20260723_dt0p005_T4.npz"
    )
    heun_005 = load(
        "pde_QMC_P5_N16_M64_R32_s20260723_dt0p005_T4_HEUN.npz"
    )
    summary["time_step_refinement"] = {
        "rk4_dt0.02_vs_dt0.01": compare(dt_02, dt_01),
        "rk4_dt0.01_vs_dt0.005": compare(dt_01, dt_005),
        "heun_vs_rk4_at_dt0.005": compare(heun_005, dt_005),
    }

    # Depth refinement.
    depth_runs = {
        N: load(
            f"pde_QMC_P5_N{N}_M128_R64_s20260724_dt0p02_T4.npz"
        )
        for N in (8, 16, 32)
    }
    summary["depth_refinement_against_N32"] = {
        f"N{N}": compare(depth_runs[N], depth_runs[32])
        for N in (8, 16)
    }

    # Quadrature resolution around the primary compiler.
    quadrature_runs = {
        "M64_R32": load(
            "pde_QMC_P5_N16_M64_R32_s20260723_dt0p02_T4.npz"
        ),
        "M128_R64": load(
            "pde_QMC_P5_N16_M128_R64_s20260723_dt0p02_T4.npz"
        ),
        "M512_R128": load(
            "pde_QMC_P5_N16_M512_R128_s20260723_dt0p02_T4.npz"
        ),
        "M256_R256": load(
            "pde_QMC_P5_N16_M256_R256_s20260723_dt0p02_T4.npz"
        ),
    }
    summary["quadrature_refinement_against_M256_R128"] = {
        name: compare(run, primary, fine_limit=run["times"].size)
        for name, run in quadrature_runs.items()
    }

    # Independent high-resolution QMC replicates.
    replicates = [
        primary,
        load(
            "pde_QMC_P5_N16_M256_R128_s20260725_dt0p02_T4.npz"
        ),
        load(
            "pde_QMC_P5_N16_M256_R128_s20260726_dt0p02_T4.npz"
        ),
    ]
    replicate_limit = replicates[1]["times"].size
    replicate_summary: dict[str, float] = {}
    for key, axes in (
        ("f", (-1,)),
        ("grams", (-2, -1)),
        ("theta", (-2, -1)),
    ):
        stacked = np.stack([run[key][:replicate_limit] for run in replicates])
        mean = np.mean(stacked, axis=0)
        radii = [
            float(np.max(np.linalg.norm(item - mean, axis=axes)))
            for item in stacked
        ]
        replicate_summary[f"{key}_max_radius"] = max(radii)
    summary["qmc_replicates"] = replicate_summary

    # Hermite order and independent tensor-cubature stress checks.
    p5 = quadrature_runs["M128_R64"]
    p15 = load(
        "pde_QMC_P15_N16_M128_R64_s20260723_dt0p02_T4.npz"
    )
    p15_refined = load(
        "pde_QMC_P15_N16_M256_R128_s20260723_dt0p02_T8.npz"
    )
    gh = load("pde_GH_P5_N16_M81_R243_s20260723_dt0p02_T8.npz")
    hybrid_p5 = load(
        "pde_HYBRID_P5_N16_M81_R128_s20260723_dt0p02_T8.npz"
    )
    hybrid_p15_r128 = load(
        "pde_HYBRID_P15_N16_M81_R128_s20260723_dt0p02_T8.npz"
    )
    hybrid_p15_r256 = load(
        "pde_HYBRID_P15_N16_M81_R256_s20260723_dt0p02_T8.npz"
    )
    hybrid_p35_r128 = load(
        "pde_HYBRID_P35_N16_M256_R128_s20260723_dt0p02_T8.npz"
    )
    summary["basis_and_method_checks"] = {
        "P5_vs_P15_same_nominal_MR": compare(p5, p15),
        "P5_vs_P15_refined_QMC": compare(primary, p15_refined),
        "hybrid_nested_P5_vs_P15_R128": compare(
            hybrid_p5, hybrid_p15_r128
        ),
        "hybrid_P15_R128_vs_R256": compare(
            hybrid_p15_r128, hybrid_p15_r256
        ),
        "hybrid_P15_R256_vs_refined_QMC_P15": compare(
            hybrid_p15_r256, p15_refined
        ),
        "hybrid_P15_R256_vs_P35_R128": compare(
            hybrid_p15_r256, hybrid_p35_r128
        ),
        "GH3_tensor_vs_primary_QMC": compare(gh, primary),
        "primary_min_projected_h_energy": float(
            np.min(primary["projected_energy"])
        ),
        "primary_final_min_projected_p_energy": (
            final_projected_p_energy(primary)
        ),
        "refined_P15_final_min_projected_p_energy": (
            final_projected_p_energy(p15_refined)
        ),
        "hybrid_P35_final_min_projected_p_energy": (
            final_projected_p_energy(hybrid_p35_r128)
        ),
        "warning": (
            "The old P35/M64/R64 pilot is excluded. The clean-base "
            "P35/R128 run is valid directional stress evidence, but its "
            "fast raw condition 6.20 and lack of R refinement prevent a "
            "cofinal P-convergence claim."
        ),
    }
    summary["compiler_level_reference_checks"] = {
        "QMC_P5": reference_metrics(primary, reference_256_32),
        "QMC_P15_complete_quadratic": reference_metrics(
            p15_refined, reference_256_32
        ),
        "hybrid_P5": reference_metrics(hybrid_p5, reference_256_32),
        "hybrid_P15_R128_complete_quadratic": reference_metrics(
            hybrid_p15_r128, reference_256_32
        ),
        "hybrid_P15_R256_complete_quadratic": reference_metrics(
            hybrid_p15_r256, reference_256_32
        ),
        "hybrid_P35_R128_complete_cubic_stress": reference_metrics(
            hybrid_p35_r128, reference_256_32
        ),
    }

    # Dense depth refinement using variance-reduced Gram increments.
    increment_32 = (
        reference_256_32["grams_mean"]
        - reference_256_32["grams_mean"][0:1]
    )
    increment_64 = (
        reference_256_64["grams_mean"]
        - reference_256_64["grams_mean"][0:1]
    )
    increment_32_interp = interpolate_grams(
        increment_32, increment_64.shape[1]
    )
    summary["dense_depth_check"] = {
        "n256_L32_vs_L64_increment_gap": float(
            np.max(
                np.linalg.norm(
                    increment_32_interp - increment_64,
                    axis=(-2, -1),
                )
            )
        ),
        "n256_vs_n512_at_L32_increment_gap": float(
            np.max(
                np.linalg.norm(
                    (
                        reference_512_32["grams_mean"]
                        - reference_512_32["grams_mean"][0:1]
                    )
                    - increment_32,
                    axis=(-2, -1),
                )
            )
        ),
        "interpretation": (
            "These are finite-grid Cauchy diagnostics, not extrapolated "
            "ordered-limit estimates. See the preregistered bootstrap "
            "audit under agent_outputs/statistical_audit."
        ),
    }

    with (PROCESSED / "summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True)

    # Compact CSV tables.
    with (PROCESSED / "reference_comparisons.csv").open(
        "w", newline=""
    ) as handle:
        rows = summary["reference_comparisons"]
        keys = ["reference", *next(iter(rows.values())).keys()]
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        for name, metrics in rows.items():
            writer.writerow({"reference": name, **metrics})

    with (PROCESSED / "compiler_level_comparisons.csv").open(
        "w", newline=""
    ) as handle:
        rows = summary["compiler_level_reference_checks"]
        keys = ["pde_level", *next(iter(rows.values())).keys()]
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        for name, metrics in rows.items():
            writer.writerow({"pde_level": name, **metrics})

    with (PROCESSED / "solver_refinement.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["axis", "comparison", "output", "grams", "theta"]
        )
        writer.writeheader()
        for axis, table in (
            ("depth", summary["depth_refinement_against_N32"]),
            (
                "quadrature",
                summary["quadrature_refinement_against_M256_R128"],
            ),
        ):
            for name, metrics in table.items():
                writer.writerow(
                    {"axis": axis, "comparison": name, **metrics}
                )
        for name, metrics in summary["time_step_refinement"].items():
            writer.writerow(
                {
                    "axis": "time_step",
                    "comparison": name,
                    **metrics,
                }
            )

    # Figure 1: output and loss curves.
    y = np.array([0.8, -0.55, 0.35])
    ref_loss = 0.5 * np.sum(
        (reference_256_32["f_mean"] - y) ** 2, axis=-1
    )
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), constrained_layout=True)
    axes[0, 0].semilogy(primary["times"], primary["loss"], label="PDE")
    axes[0, 0].semilogy(
        reference_256_32["times"], ref_loss, "--", label="dense mean"
    )
    axes[0, 0].set(title="Loss curve", xlabel="training time")
    axes[0, 0].legend()
    for r in range(3):
        axes[0, 1].plot(primary["times"], primary["f"][:, r])
        axes[0, 1].plot(
            reference_256_32["times"],
            reference_256_32["f_mean"][:, r],
            "--",
        )
    axes[0, 1].set(title="Outputs (solid PDE, dashed dense)", xlabel="time")
    terminal_entries = ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2))
    for r, q in terminal_entries:
        axes[1, 0].plot(
            primary["times"],
            primary["grams"][:, -1, r, q]
            - primary["grams"][0, -1, r, q],
            label=f"{r+1}{q+1}",
        )
        axes[1, 0].plot(
            reference_256_32["times"],
            reference_256_32["grams_mean"][:, -1, r, q]
            - reference_256_32["grams_mean"][0, -1, r, q],
            "--",
        )
    axes[1, 0].set(
        title="Output-depth Gram increments",
        xlabel="time",
    )
    axes[1, 0].legend(ncol=3, fontsize=8)
    pde_ref_grams = interpolate_grams(
        primary["grams"], reference_256_32["grams_mean"].shape[1]
    )
    gram_error = np.linalg.norm(
        (pde_ref_grams - pde_ref_grams[0:1])
        - (
            reference_256_32["grams_mean"]
            - reference_256_32["grams_mean"][0:1]
        ),
        axis=(-2, -1),
    )
    image = axes[1, 1].imshow(
        gram_error.T,
        origin="lower",
        aspect="auto",
        extent=[0, 8, 0, 1],
    )
    axes[1, 1].set(
        title="Gram-increment Frobenius error",
        xlabel="time",
        ylabel="depth",
    )
    fig.colorbar(image, ax=axes[1, 1])
    fig.savefig(FIGURES / "pde_vs_dense_curves.png", dpi=180)
    plt.close(fig)

    # Figure 2: plateau continuation.
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), constrained_layout=True)
    axes[0].semilogy(tail["times"], np.maximum(tail["residual_norm"], 1e-18))
    axes[0].set(title="PDE residual through plateau", xlabel="time")
    axes[1].semilogy(
        tail["times"],
        np.maximum(np.max(tail_gram_drift, axis=1), 1e-18),
    )
    axes[1].set(title="All-depth Gram drift from t=8", xlabel="time")
    fig.savefig(FIGURES / "pde_plateau_tail.png", dpi=180)
    plt.close(fig)

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
