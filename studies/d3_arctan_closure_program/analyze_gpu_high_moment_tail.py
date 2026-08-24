#!/usr/bin/env python3
"""Analyze the frozen GPU high-moment experiment with clustered bootstrap."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


WIDTHS = (256, 512, 1024, 2048)
HORIZONS = (1.0, 2.0, 4.0, 8.0)
FIELDS = ("r2", "b2", "q1")
BOOTSTRAPS = 2000
BOOTSTRAP_SEED = 2026082304


def hkey(s: float) -> str:
    return f"s{str(s).replace('.', 'p')}"


def pooled_moments(rows: np.ndarray, orders: np.ndarray) -> np.ndarray:
    return np.asarray([(np.mean(rows[:, j] ** p)) ** (1.0 / p)
                       for j, p in enumerate(orders)])


def alpha_and_ratio(m: np.ndarray, orders: np.ndarray):
    ids = [int(np.where(orders == p)[0][0]) for p in (4, 6, 8, 10, 12)]
    x = np.log(orders[ids].astype(float))
    y = np.log(m[ids] / m[int(np.where(orders == 2)[0][0])])
    alpha = float(np.polyfit(x, y, 1)[0])
    i6 = int(np.where(orders == 6)[0][0])
    i12 = int(np.where(orders == 12)[0][0])
    ratio = float(m[i12] / (2.0 * m[i6]))
    return alpha, ratio


def ci(x):
    return [float(np.quantile(x, 0.025)), float(np.quantile(x, 0.975))]


def load(path: Path):
    with np.load(path, allow_pickle=False) as z:
        return {k: z[k] for k in z.files}


def relative_rms(a, b):
    den = max(float(np.sqrt(np.mean(np.asarray(b, dtype=np.float64) ** 2))), 1e-30)
    return float(np.sqrt(np.mean((np.asarray(a, dtype=np.float64)
                                  - np.asarray(b, dtype=np.float64)) ** 2)) / den)


def main() -> None:
    root = Path(__file__).resolve().parent
    data_dir = root / "gpu_tail_results"
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    main_data = {n: load(data_dir / f"tail_main_n{n}_h0.01.npz") for n in WIDTHS}
    orders = main_data[WIDTHS[0]]["p_orders"].astype(int)
    report = {"orders": orders.tolist(), "main": {}, "solver": {}, "arithmetic": {}}

    # Frozen solver comparisons.
    solver_valid = True
    for n in WIDTHS:
        coarse = load(data_dir / f"tail_paired_coarse_n{n}_h0.01.npz")
        fine = load(data_dir / f"tail_paired_fine_n{n}_h0.005.npz")
        report["solver"][str(n)] = {}
        for s in HORIZONS:
            k = hkey(s)
            entry = {}
            for field in FIELDS:
                entry[f"{field}_relative_rms"] = relative_rms(
                    coarse[f"{k}_{field}_values"], fine[f"{k}_{field}_values"]
                )
                cm = pooled_moments(coarse[f"{k}_{field}_moments"], orders)
                fm = pooled_moments(fine[f"{k}_{field}_moments"], orders)
                entry[f"{field}_moment_relative"] = np.abs(cm - fm) / np.maximum(fm, 1e-30)
            entry["kernel_relative_rms"] = relative_rms(
                coarse[f"{k}_kernel_blocks"], fine[f"{k}_kernel_blocks"]
            )
            valid = entry["kernel_relative_rms"] <= 0.03
            for field in FIELDS:
                valid &= entry[f"{field}_relative_rms"] <= 0.03
                rel = entry[f"{field}_moment_relative"]
                valid &= bool(np.all(rel[:5] <= 0.06) and np.all(rel[5:] <= 0.12))
                entry[f"{field}_moment_relative"] = rel.tolist()
            entry["valid"] = bool(valid)
            solver_valid &= bool(valid)
            report["solver"][str(n)][str(s)] = entry

    # Common-draw arithmetic audit.
    for n in (256, 512):
        fp32 = load(data_dir / f"tail_arithmetic_fp32_n{n}_h0.005.npz")
        fp64 = load(data_dir / f"tail_arithmetic_fp64_n{n}_h0.005.npz")
        report["arithmetic"][str(n)] = {}
        for s in HORIZONS:
            k = hkey(s)
            report["arithmetic"][str(n)][str(s)] = {
                field: relative_rms(fp32[f"{k}_{field}_values"], fp64[f"{k}_{field}_values"])
                for field in FIELDS
            }
            report["arithmetic"][str(n)][str(s)]["kernel"] = relative_rms(
                fp32[f"{k}_kernel_blocks"], fp64[f"{k}_kernel_blocks"]
            )

    # Main clustered estimates.
    bootstrap_cache = {}
    kernel_bootstrap_cache = {}
    for n in WIDTHS:
        z = main_data[n]
        report["main"][str(n)] = {}
        reps = int(z["replicas"])
        for s in HORIZONS:
            k = hkey(s)
            sentry = {}
            for field in FIELDS:
                rows = z[f"{k}_{field}_moments"].astype(np.float64)
                m = pooled_moments(rows, orders)
                alpha, ratio = alpha_and_ratio(m, orders)
                bs_m = np.empty((BOOTSTRAPS, len(orders)))
                bs_alpha = np.empty(BOOTSTRAPS)
                bs_ratio = np.empty(BOOTSTRAPS)
                for b in range(BOOTSTRAPS):
                    idx = rng.integers(0, reps, size=reps)
                    mb = pooled_moments(rows[idx], orders)
                    bs_m[b] = mb
                    bs_alpha[b], bs_ratio[b] = alpha_and_ratio(mb, orders)
                bootstrap_cache[(n, s, field)] = bs_m
                vals = z[f"{k}_{field}_values"].reshape(-1).astype(np.float64)
                sentry[field] = {
                    "moments": m.tolist(),
                    "moment_ci": [ci(bs_m[:, j]) for j in range(len(orders))],
                    "alpha": alpha,
                    "alpha_ci": ci(bs_alpha),
                    "m12_over_2m6": ratio,
                    "m12_over_2m6_ci": ci(bs_ratio),
                    "abs_quantiles": {
                        str(q): float(np.quantile(np.abs(vals), q))
                        for q in (0.99, 0.999, 0.9999)
                    },
                    "abs_max": float(np.max(np.abs(vals))),
                }

            kernels = z[f"{k}_kernel_blocks"].astype(np.float64)
            action = z[f"{k}_accumulated_action"].astype(np.float64)
            sentry["kernel_mean"] = kernels.mean(axis=0).tolist()
            kboot = np.empty((BOOTSTRAPS, 4))
            for b in range(BOOTSTRAPS):
                idx = rng.integers(0, reps, size=reps)
                kboot[b] = kernels[idx].mean(axis=0)
            kernel_bootstrap_cache[(n, s)] = kboot
            sentry["action_quantiles"] = {
                str(q): float(np.quantile(action, q)) for q in (0.25, 0.5, 0.75, 0.99)
            }
            # Exploratory, predeclared action quartiles.
            edges = np.quantile(action, (0.0, 0.25, 0.5, 0.75, 1.0))
            strata = []
            rows = z[f"{k}_r2_moments"].astype(np.float64)
            for j in range(4):
                mask = (action >= edges[j]) & ((action <= edges[j + 1]) if j == 3 else (action < edges[j + 1]))
                mm = pooled_moments(rows[mask], orders)
                aa, rr = alpha_and_ratio(mm, orders)
                strata.append({"count": int(mask.sum()), "alpha": aa,
                               "m12_over_2m6": rr, "moments": mm.tolist()})
            sentry["r2_action_strata"] = strata
            report["main"][str(n)][str(s)] = sentry

    # Width slopes, bootstrapped independently by network within width.
    report["width_slopes"] = {}
    logn = np.log(np.asarray(WIDTHS, dtype=float))
    for s in HORIZONS:
        report["width_slopes"][str(s)] = {}
        for field in FIELDS:
            slopes = []
            point = []
            for j, p in enumerate(orders):
                ys = []
                for n in WIDTHS:
                    m = np.asarray(report["main"][str(n)][str(s)][field]["moments"])
                    ys.append(m[j] / p)
                point.append(float(np.polyfit(logn, np.log(ys), 1)[0]))
                bs = np.empty(BOOTSTRAPS)
                for b in range(BOOTSTRAPS):
                    yb = [bootstrap_cache[(n, s, field)][b, j] / p for n in WIDTHS]
                    bs[b] = np.polyfit(logn, np.log(yb), 1)[0]
                slopes.append(ci(bs))
            report["width_slopes"][str(s)][field] = {
                "point": point, "ci": slopes
            }
        kernel_point = []
        kernel_ci = []
        for block in range(4):
            y = [report["main"][str(n)][str(s)]["kernel_mean"][block]
                 for n in WIDTHS]
            kernel_point.append(float(np.polyfit(logn, np.log(y), 1)[0]))
            bs = np.empty(BOOTSTRAPS)
            for b in range(BOOTSTRAPS):
                yb = [kernel_bootstrap_cache[(n, s)][b, block] for n in WIDTHS]
                bs[b] = np.polyfit(logn, np.log(yb), 1)[0]
            kernel_ci.append(ci(bs))
        report["width_slopes"][str(s)]["kernel_blocks"] = {
            "point": kernel_point, "ci": kernel_ci
        }

    report["solver_all_valid"] = bool(solver_valid)

    # Apply the frozen formal interpretation rules literally.
    support = solver_valid
    for s in (2.0, 4.0):
        for n in WIDTHS:
            e = report["main"][str(n)][str(s)]["r2"]
            support &= e["alpha_ci"][1] <= 1.05
            support &= e["m12_over_2m6_ci"][1] <= 1.20
        rslopes = report["width_slopes"][str(s)]["r2"]["ci"]
        support &= all(x[1] < 0.10 for x in rslopes)
        support &= all(x[1] < 0.10 for x in
                       report["width_slopes"][str(s)]["kernel_blocks"]["ci"])

    against = solver_valid
    for s in HORIZONS:
        local = True
        for n in (1024, 2048):
            e = report["main"][str(n)][str(s)]["r2"]
            local &= e["alpha_ci"][0] > 1.15
            local &= e["m12_over_2m6_ci"][0] > 1.20
        against &= local
    # The preregistration says evidence against at a solver-valid horizon,
    # so replace the all-horizon conjunction by an existential calculation.
    against = solver_valid and any(
        all(report["main"][str(n)][str(s)]["r2"]["alpha_ci"][0] > 1.15
            and report["main"][str(n)][str(s)]["r2"]["m12_over_2m6_ci"][0] > 1.20
            for n in (1024, 2048))
        and report["main"]["2048"][str(s)]["r2"]["alpha"]
            >= report["main"]["1024"][str(s)]["r2"]["alpha"]
        and report["main"]["2048"][str(s)]["r2"]["m12_over_2m6"]
            >= report["main"]["1024"][str(s)]["r2"]["m12_over_2m6"]
        for s in HORIZONS
    )
    report["formal_support"] = bool(support)
    report["formal_evidence_against"] = bool(against)

    out_json = root / "GPU_HIGH_MOMENT_TAIL_RESULTS_2026-08-23.json"
    out_json.write_text(json.dumps(report, indent=2) + "\n")

    lines = [
        "# Results: GPU high-moment middle-query audit",
        "",
        f"- All preregistered solver checks valid: **{solver_valid}**.",
        f"- Formal support criterion: **{support}**.",
        f"- Formal evidence-against criterion: **{against}**.",
        "",
        "The table reports the cluster-bootstrap point estimate and 95% CI",
        "for the moment-growth exponent of `R2`, followed by `m12/(2 m6)`.",
        "",
        "| horizon | width | alpha (95% CI) | m12/(2m6) (95% CI) |",
        "|---:|---:|---:|---:|",
    ]
    for s in HORIZONS:
        for n in WIDTHS:
            e = report["main"][str(n)][str(s)]["r2"]
            lines.append(
                f"| {s:g} | {n} | {e['alpha']:.3f} "
                f"[{e['alpha_ci'][0]:.3f}, {e['alpha_ci'][1]:.3f}] | "
                f"{e['m12_over_2m6']:.3f} "
                f"[{e['m12_over_2m6_ci'][0]:.3f}, {e['m12_over_2m6_ci'][1]:.3f}] |"
            )
    lines.extend([
        "",
        "This experiment supplies empirical weight only.  In particular, a",
        "support result does not prove the missing signed causal-predictor or",
        "joint-leverage estimate and changes no theorem rung by itself.",
    ])
    (root / "GPU_HIGH_MOMENT_TAIL_RESULTS_2026-08-23.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"json": str(out_json), "solver_valid": solver_valid,
                      "formal_support": bool(support),
                      "formal_evidence_against": bool(against)}))


if __name__ == "__main__":
    main()
