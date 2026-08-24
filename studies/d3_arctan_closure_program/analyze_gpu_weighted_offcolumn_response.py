#!/usr/bin/env python3
"""Analyze the preregistered weighted off-column response experiment."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


WIDTHS = (256, 512, 1024, 2048)
AUDIT_WIDTHS = (256, 512)
HORIZONS = (1.0, 2.0, 4.0)
METRICS = ("f_cx", "f_ax", "q_ax", "f_b", "f_ab", "q_ab")
BOOTSTRAPS = 2000
BOOTSTRAP_SEED = 2026082306


def hkey(s: float) -> str:
    return f"s{str(s).replace('.', 'p')}"


def load(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as z:
        return {key: z[key] for key in z.files}


def relative_rms(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    absolute = float(np.sqrt(np.mean((a - b) ** 2)))
    denominator = max(float(np.sqrt(np.mean(b ** 2))), 1e-30)
    return absolute / denominator, absolute


def comparison(a: np.ndarray, b: np.ndarray, tolerance: float) -> dict[str, object]:
    relative, absolute = relative_rms(a, b)
    valid = relative <= tolerance or absolute <= 1e-6
    return {"relative_rms": relative, "absolute_rms": absolute,
            "valid": bool(valid)}


def interval(values: np.ndarray) -> list[float]:
    return [float(np.quantile(values, 0.025)),
            float(np.quantile(values, 0.975))]


def main() -> None:
    root = Path(__file__).resolve().parent
    data_dir = root / "gpu_weighted_response_results"
    rng = np.random.default_rng(BOOTSTRAP_SEED)

    main_data = {
        n: load(data_dir / f"weighted_main_h001_eps002_fp32_n{n}.npz")
        for n in WIDTHS
    }
    report: dict[str, object] = {
        "main": {}, "width_slopes": {}, "solver": {},
        "perturbation": {}, "arithmetic": {},
    }
    bootstrap_medians: dict[tuple[int, float, str], np.ndarray] = {}

    # Cluster at the independent-network level.  Probe randomness was already
    # averaged inside each network record by the generator.
    for n in WIDTHS:
        report["main"][str(n)] = {}
        replicas = int(main_data[n]["replicas"])
        for horizon in HORIZONS:
            key = hkey(horizon)
            entry: dict[str, object] = {}
            for metric in METRICS:
                values = main_data[n][f"{key}_{metric}"].astype(np.float64)
                boots = np.empty(BOOTSTRAPS)
                for b in range(BOOTSTRAPS):
                    ids = rng.integers(0, replicas, size=replicas)
                    boots[b] = np.median(values[ids])
                bootstrap_medians[(n, horizon, metric)] = boots
                entry[metric] = {
                    "median": float(np.median(values)),
                    "median_ci": interval(boots),
                    "quantiles": {
                        str(q): float(np.quantile(values, q))
                        for q in (0.25, 0.75, 0.9, 0.99)
                    },
                    "max": float(np.max(values)),
                }
            for metric in ("ipr_ax", "top_ax", "ipr_ab", "top_ab"):
                values = main_data[n][f"{key}_{metric}"].astype(np.float64)
                entry[metric] = {
                    "median": float(np.median(values)),
                    "quantiles": {
                        str(q): float(np.quantile(values, q))
                        for q in (0.25, 0.75, 0.9, 0.99)
                    },
                }
            report["main"][str(n)][str(horizon)] = entry

    log_widths = np.log(np.asarray(WIDTHS, dtype=np.float64))
    for horizon in HORIZONS:
        report["width_slopes"][str(horizon)] = {}
        for metric in METRICS:
            medians = np.asarray([
                report["main"][str(n)][str(horizon)][metric]["median"]
                for n in WIDTHS
            ])
            point = float(np.polyfit(log_widths, np.log(medians), 1)[0])
            boots = np.empty(BOOTSTRAPS)
            for b in range(BOOTSTRAPS):
                sample = np.asarray([
                    bootstrap_medians[(n, horizon, metric)][b]
                    for n in WIDTHS
                ])
                boots[b] = np.polyfit(log_widths, np.log(sample), 1)[0]
            report["width_slopes"][str(horizon)][metric] = {
                "point": point, "ci": interval(boots)
            }

    numerical_valid = True
    for n in AUDIT_WIDTHS:
        replicas = 8
        coarse = main_data[n]
        fine = load(data_dir / f"weighted_fine_h0005_eps002_fp32_n{n}.npz")
        half_epsilon = load(
            data_dir / f"weighted_fine_h0005_eps001_fp32_n{n}.npz"
        )
        fp64 = load(data_dir / f"weighted_fine_h0005_eps001_fp64_n{n}.npz")
        report["solver"][str(n)] = {}
        report["perturbation"][str(n)] = {}
        report["arithmetic"][str(n)] = {}
        for horizon in HORIZONS:
            key = hkey(horizon)
            report["solver"][str(n)][str(horizon)] = {}
            report["perturbation"][str(n)][str(horizon)] = {}
            report["arithmetic"][str(n)][str(horizon)] = {}
            for metric in ("f_cx", "f_ax", "q_ax"):
                solver = comparison(
                    coarse[f"{key}_{metric}"][:replicas],
                    fine[f"{key}_{metric}"], 0.05,
                )
                perturbation = comparison(
                    fine[f"{key}_{metric}"],
                    half_epsilon[f"{key}_{metric}"], 0.05,
                )
                arithmetic = comparison(
                    half_epsilon[f"{key}_{metric}"],
                    fp64[f"{key}_{metric}"], 0.02,
                )
                report["solver"][str(n)][str(horizon)][metric] = solver
                report["perturbation"][str(n)][str(horizon)][metric] = perturbation
                report["arithmetic"][str(n)][str(horizon)][metric] = arithmetic
                numerical_valid &= bool(solver["valid"])
                numerical_valid &= bool(perturbation["valid"])
                numerical_valid &= bool(arithmetic["valid"])

    support = numerical_valid
    against = False
    support_by_horizon: dict[str, bool] = {}
    against_by_horizon: dict[str, bool] = {}
    q_ratio: dict[str, float] = {}
    for horizon in (2.0, 4.0):
        slopes = report["width_slopes"][str(horizon)]
        ratio = (
            report["main"]["2048"][str(horizon)]["q_ax"]["median"]
            / report["main"]["256"][str(horizon)]["q_ax"]["median"]
        )
        q_ratio[str(horizon)] = float(ratio)
        local_support = (
            slopes["f_ax"]["ci"][1] < 0.15
            and slopes["q_ax"]["ci"][1] < 0.10
            and ratio <= 1.25
        )
        local_against = (
            numerical_valid
            and slopes["f_ax"]["ci"][0] > 0.30
            and ratio > 1.35
        )
        support_by_horizon[str(horizon)] = bool(local_support)
        against_by_horizon[str(horizon)] = bool(local_against)
        support &= local_support
        against |= local_against

    report["numerical_valid"] = bool(numerical_valid)
    report["support_by_horizon"] = support_by_horizon
    report["against_by_horizon"] = against_by_horizon
    report["q_ax_width_ratio_2048_over_256"] = q_ratio
    report["formal_support"] = bool(support)
    report["formal_evidence_against"] = bool(against)

    output_json = root / "GPU_WEIGHTED_OFFCOLUMN_RESPONSE_RESULTS_2026-08-23.json"
    output_json.write_text(json.dumps(report, indent=2) + "\n")
    lines = [
        "# Results: endpoint-weighted off-column response",
        "",
        f"- All preregistered numerical checks valid: **{numerical_valid}**.",
        f"- Formal support criterion: **{support}**.",
        f"- Formal evidence-against criterion: **{against}**.",
        "",
        "The slopes use network-cluster bootstrap medians and 95% percentile intervals.",
        "",
        "| horizon | metric | width slope (95% CI) | Q_A(2048)/Q_A(256) |",
        "|---:|:---|:---|---:|",
    ]
    for horizon in HORIZONS:
        for metric in ("f_ax", "q_ax"):
            value = report["width_slopes"][str(horizon)][metric]
            ratio = q_ratio.get(str(horizon), float("nan"))
            lines.append(
                f"| {horizon:g} | {metric} | {value['point']:.3f} "
                f"[{value['ci'][0]:.3f}, {value['ci'][1]:.3f}] | "
                f"{ratio:.3f} |"
            )
    lines.extend([
        "",
        "This is a mechanism diagnostic.  A support verdict does not prove",
        "the marked two-cavity or third-mixed joint-leverage lemma.",
    ])
    output_md = root / "GPU_WEIGHTED_OFFCOLUMN_RESPONSE_RESULTS_2026-08-23.md"
    output_md.write_text("\n".join(lines) + "\n")
    print(json.dumps({
        "json": str(output_json), "markdown": str(output_md),
        "numerical_valid": bool(numerical_valid),
        "formal_support": bool(support),
        "formal_evidence_against": bool(against),
    }))


if __name__ == "__main__":
    main()
