#!/usr/bin/env python3
"""Analyze the preregistered hidden-neuron gauge-block gradient data."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


WIDTHS = (256, 512, 1024, 2048)
AUDIT_WIDTHS = (256, 512)
HORIZONS = (1.0, 2.0, 4.0)
MODES = ("gauge", "row", "column")
ORDERS = np.asarray((2, 4, 6, 8), dtype=int)
BOOTSTRAPS = 2000
BOOTSTRAP_SEED = 2026082308


def hkey(value: float) -> str:
    return f"s{str(value).replace('.', 'p')}"


def load(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as z:
        return {key: z[key] for key in z.files}


def interval(values: np.ndarray) -> list[float]:
    return [float(np.quantile(values, 0.025)),
            float(np.quantile(values, 0.975))]


def relative_rms(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    absolute = float(np.sqrt(np.mean((a - b) ** 2)))
    denominator = max(float(np.sqrt(np.mean(b ** 2))), 1e-30)
    return absolute / denominator, absolute


def comparison(a: np.ndarray, b: np.ndarray, tolerance: float) -> dict[str, object]:
    relative, absolute = relative_rms(a, b)
    return {
        "relative_rms": relative,
        "absolute_rms": absolute,
        "valid": bool(relative <= tolerance or absolute <= 1e-6),
    }


def pooled_moments(directions: np.ndarray) -> np.ndarray:
    values = np.abs(np.asarray(directions, dtype=np.float64)).reshape(-1)
    return np.asarray([(np.mean(values ** order)) ** (1.0 / order)
                       for order in ORDERS])


def moment_exponent(moments: np.ndarray) -> float:
    normalized = moments / moments[0]
    return float(np.polyfit(np.log(ORDERS.astype(float)),
                            np.log(normalized), 1)[0])


def main() -> None:
    root = Path(__file__).resolve().parent
    data_dir = root / "gpu_gauge_gradient_results"
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    data = {
        width: load(data_dir / f"gauge_main_h001_eps002_fp32_n{width}.npz")
        for width in WIDTHS
    }
    report: dict[str, object] = {
        "main": {}, "width_slopes": {}, "solver": {},
        "perturbation": {}, "arithmetic": {},
    }
    median_boots: dict[tuple[int, float], np.ndarray] = {}

    for width in WIDTHS:
        report["main"][str(width)] = {}
        replicas = int(data[width]["replicas"])
        for horizon in HORIZONS:
            key = hkey(horizon)
            entry: dict[str, object] = {}
            for mode in MODES:
                gradients = data[width][f"{key}_grad_{mode}"].astype(np.float64)
                directions = data[width][f"{key}_dir_{mode}"].astype(np.float64)
                entry[f"grad_{mode}"] = {
                    "median": float(np.median(gradients)),
                    "quantiles": {
                        str(q): float(np.quantile(gradients, q))
                        for q in (0.25, 0.75, 0.9, 0.99)
                    },
                    "max": float(np.max(gradients)),
                }
                moments = pooled_moments(directions)
                alpha = moment_exponent(moments)
                alpha_boot = np.empty(BOOTSTRAPS)
                if mode == "gauge":
                    med_boot = np.empty(BOOTSTRAPS)
                for b in range(BOOTSTRAPS):
                    ids = rng.integers(0, replicas, size=replicas)
                    alpha_boot[b] = moment_exponent(pooled_moments(directions[ids]))
                    if mode == "gauge":
                        med_boot[b] = np.median(gradients[ids])
                entry[f"dir_{mode}"] = {
                    "moments": moments.tolist(),
                    "alpha": alpha,
                    "alpha_ci": interval(alpha_boot),
                }
                if mode == "gauge":
                    entry[f"grad_{mode}"]["median_ci"] = interval(med_boot)
                    median_boots[(width, horizon)] = med_boot
            query = data[width][f"{key}_query"].astype(np.float64)
            entry["query"] = {
                "moments": [float((np.mean(np.abs(query) ** order)) **
                                    (1.0 / order)) for order in ORDERS],
                "abs_quantiles": {
                    str(q): float(np.quantile(np.abs(query), q))
                    for q in (0.9, 0.99)
                },
            }
            report["main"][str(width)][str(horizon)] = entry

    log_widths = np.log(np.asarray(WIDTHS, dtype=np.float64))
    for horizon in HORIZONS:
        medians = np.asarray([
            report["main"][str(width)][str(horizon)]["grad_gauge"]["median"]
            for width in WIDTHS
        ])
        point = float(np.polyfit(log_widths, np.log(medians), 1)[0])
        boots = np.empty(BOOTSTRAPS)
        for b in range(BOOTSTRAPS):
            samples = np.asarray([
                median_boots[(width, horizon)][b] for width in WIDTHS
            ])
            boots[b] = np.polyfit(log_widths, np.log(samples), 1)[0]
        report["width_slopes"][str(horizon)] = {
            "point": point, "ci": interval(boots)
        }

    numerical_valid = True
    for width in AUDIT_WIDTHS:
        replicas = 8
        coarse = data[width]
        fine = load(data_dir / f"gauge_fine_h0005_eps002_fp32_n{width}.npz")
        half = load(data_dir / f"gauge_fine_h0005_eps001_fp32_n{width}.npz")
        fp64 = load(data_dir / f"gauge_fine_h0005_eps001_fp64_n{width}.npz")
        report["solver"][str(width)] = {}
        report["perturbation"][str(width)] = {}
        report["arithmetic"][str(width)] = {}
        for horizon in HORIZONS:
            key = hkey(horizon)
            solver = comparison(coarse[f"{key}_grad_gauge"][:replicas],
                                fine[f"{key}_grad_gauge"], 0.05)
            perturbation = comparison(fine[f"{key}_grad_gauge"],
                                      half[f"{key}_grad_gauge"], 0.05)
            arithmetic = comparison(half[f"{key}_grad_gauge"],
                                    fp64[f"{key}_grad_gauge"], 0.02)
            report["solver"][str(width)][str(horizon)] = solver
            report["perturbation"][str(width)][str(horizon)] = perturbation
            report["arithmetic"][str(width)][str(horizon)] = arithmetic
            numerical_valid &= bool(solver["valid"])
            numerical_valid &= bool(perturbation["valid"])
            numerical_valid &= bool(arithmetic["valid"])

    support = numerical_valid
    against = False
    ratios: dict[str, float] = {}
    support_by_horizon: dict[str, bool] = {}
    against_by_horizon: dict[str, bool] = {}
    for horizon in (2.0, 4.0):
        slope = report["width_slopes"][str(horizon)]
        ratio = (
            report["main"]["2048"][str(horizon)]["grad_gauge"]["median"]
            / report["main"]["256"][str(horizon)]["grad_gauge"]["median"]
        )
        ratios[str(horizon)] = float(ratio)
        local_support = slope["ci"][1] < 0.15 and ratio <= 1.25
        local_support &= all(
            report["main"][str(width)][str(horizon)]["dir_gauge"]["alpha_ci"][1]
            < 0.75 for width in WIDTHS
        )
        local_against = (
            numerical_valid and slope["ci"][0] > 0.30 and ratio > 1.35
        )
        support_by_horizon[str(horizon)] = bool(local_support)
        against_by_horizon[str(horizon)] = bool(local_against)
        support &= local_support
        against |= local_against

    report["numerical_valid"] = bool(numerical_valid)
    report["median_ratio_2048_over_256"] = ratios
    report["support_by_horizon"] = support_by_horizon
    report["against_by_horizon"] = against_by_horizon
    report["formal_support"] = bool(support)
    report["formal_evidence_against"] = bool(against)

    output_json = root / "GPU_GAUGE_BLOCK_GRADIENT_RESULTS_2026-08-23.json"
    output_json.write_text(json.dumps(report, indent=2) + "\n")
    lines = [
        "# Results: hidden-neuron gauge-block gradient",
        "",
        f"- All preregistered numerical checks valid: **{numerical_valid}**.",
        f"- Formal support criterion: **{support}**.",
        f"- Formal evidence-against criterion: **{against}**.",
        "",
        "| horizon | gradient width slope (95% CI) | median ratio 2048/256 |",
        "|---:|:---|---:|",
    ]
    for horizon in HORIZONS:
        slope = report["width_slopes"][str(horizon)]
        ratio = ratios.get(str(horizon), float("nan"))
        lines.append(
            f"| {horizon:g} | {slope['point']:.3f} "
            f"[{slope['ci'][0]:.3f}, {slope['ci'][1]:.3f}] | {ratio:.3f} |"
        )
    lines.extend([
        "",
        "This is empirical evidence only.  In particular, support does not",
        "prove the mesh-uniform signed gauge-tangent estimate.",
    ])
    output_md = root / "GPU_GAUGE_BLOCK_GRADIENT_RESULTS_2026-08-23.md"
    output_md.write_text("\n".join(lines) + "\n")
    print(json.dumps({
        "json": str(output_json), "markdown": str(output_md),
        "numerical_valid": bool(numerical_valid),
        "formal_support": bool(support),
        "formal_evidence_against": bool(against),
    }))


if __name__ == "__main__":
    main()
