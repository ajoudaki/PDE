#!/usr/bin/env python3
"""Analyze the frozen middle saturation/nonalignment experiment."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


WIDTHS = (512, 1024, 2048, 4096)
HORIZONS = (1.0, 2.0, 4.0)
MOMENTS = (2, 4, 6, 8, 12, 16)
LAMBDAS = (0.25, 0.5, 1.0)
LEVELS = (2.0, 3.0, 4.0)


def hkey(t):
    return str(t).replace(".", "p")


def load(path):
    return np.load(path, allow_pickle=False)


def lme(x, lam):
    y = lam * np.abs(x.astype(np.float64).ravel())
    m = float(np.max(y))
    return (m + math.log(float(np.exp(y - m).mean()))) / lam


def checkpoint_stats(data, t, replica_limit=None):
    prefix = f"s{hkey(t)}_"
    arrays = {name: data[prefix + name] for name in ("R", "D", "S", "H", "V")}
    if replica_limit is not None:
        arrays = {name: value[:replica_limit] for name, value in arrays.items()}
    r = arrays["R"].astype(np.float64).ravel()
    d = arrays["D"].astype(np.float64).ravel()
    s = arrays["S"].astype(np.float64).ravel()
    bath = arrays["H"].astype(np.float64).ravel()
    vel = arrays["V"].astype(np.float64).ravel()
    b = d * r
    out = {
        "coordinates": int(r.size),
        "identity_residual": float(np.max(data[prefix + "identity_residual"])),
    }
    for q in MOMENTS:
        out[f"R_q{q}"] = float(np.mean(np.abs(r) ** q) ** (1.0 / q))
        out[f"B_q{q}"] = float(np.mean(np.abs(b) ** q) ** (1.0 / q))
    for lam in LAMBDAS:
        key = str(lam).replace(".", "p")
        out[f"R_lme{key}"] = lme(r, lam)
    out["R_max"] = float(np.max(np.abs(r)))
    denom_rel = np.abs(s) + np.abs(bath) + 1e-12
    relative_velocity = np.abs(vel) / denom_rel
    for level in LEVELS:
        lk = str(int(level))
        tail = np.abs(r) >= level
        dangerous = tail & (d >= 0.5) & (s * bath < 0.0) & (np.abs(vel) <= 0.25 * np.abs(s))
        tail_count = int(np.sum(tail))
        danger_count = int(np.sum(dangerous))
        out[f"L{lk}_tail_count"] = tail_count
        out[f"L{lk}_danger_count"] = danger_count
        out[f"L{lk}_tail_frequency"] = float(tail_count / r.size)
        out[f"L{lk}_danger_frequency"] = float(danger_count / r.size)
        out[f"L{lk}_conditional"] = (
            float(danger_count / tail_count) if tail_count >= 25 else None
        )
        out[f"L{lk}_conditional_haldane"] = float((danger_count + 0.5) / (tail_count + 1.0))
        if tail_count:
            out[f"L{lk}_median_gate"] = float(np.median(d[tail]))
            out[f"L{lk}_median_relative_velocity"] = float(np.median(relative_velocity[tail]))
            out[f"L{lk}_suppressed_fraction"] = float(np.mean(d[tail] < 0.5))
        else:
            out[f"L{lk}_median_gate"] = None
            out[f"L{lk}_median_relative_velocity"] = None
            out[f"L{lk}_suppressed_fraction"] = None
    return out


def sym_relative(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-15)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    args = parser.parse_args()

    main_data = {
        n: load(args.input_dir / f"middle_saturation_main_n{n}.npz")
        for n in WIDTHS
    }
    stats = {
        str(n): {str(t): checkpoint_stats(main_data[n], t) for t in HORIZONS}
        for n in WIDTHS
    }
    logn = np.log(np.asarray(WIDTHS, dtype=np.float64))
    slopes = {}
    ratios = {}
    for t in HORIZONS:
        for q in MOMENTS:
            values = np.asarray([stats[str(n)][str(t)][f"R_q{q}"] / q for n in WIDTHS])
            slope = float(np.polyfit(logn, np.log(values), 1)[0])
            slopes[f"T{t}_q{q}"] = slope
            ratios[f"T{t}_q{q}"] = float(values[-1] / values[0])

    evidence_against = []
    for t in HORIZONS:
        for level in LEVELS:
            lk = str(int(level))
            left = stats["512"][str(t)]
            right = stats["4096"][str(t)]
            if left[f"L{lk}_tail_count"] >= 100 and right[f"L{lk}_tail_count"] >= 100:
                c_left = left[f"L{lk}_conditional_haldane"]
                c_right = right[f"L{lk}_conditional_haldane"]
                if c_right > 0.10 and c_right / c_left > 1.5:
                    evidence_against.append({
                        "horizon": t, "level": level,
                        "conditional_512": c_left,
                        "conditional_4096": c_right,
                        "ratio": c_right / c_left,
                    })

    primary_keys = [f"T{t}_q{q}" for t in HORIZONS for q in (2, 4, 6, 8, 12)]
    primary_slope_max = max(slopes[key] for key in primary_keys)
    primary_ratio_max = max(ratios[key] for key in primary_keys)
    c_t4_l2 = stats["4096"]["4.0"]["L2_conditional"]

    audit = {}
    h_data = load(args.input_dir / "middle_saturation_audit_h0005_n512.npz")
    main_512_16 = {str(t): checkpoint_stats(main_data[512], t, replica_limit=16) for t in HORIZONS}
    h_512_16 = {str(t): checkpoint_stats(h_data, t) for t in HORIZONS}
    h_moment_max = 0.0
    h_probability_max = 0.0
    for t in HORIZONS:
        for q in MOMENTS:
            for prefix in ("R", "B"):
                h_moment_max = max(
                    h_moment_max,
                    sym_relative(main_512_16[str(t)][f"{prefix}_q{q}"],
                                 h_512_16[str(t)][f"{prefix}_q{q}"]),
                )
        for lam in LAMBDAS:
            key = str(lam).replace(".", "p")
            h_moment_max = max(
                h_moment_max,
                sym_relative(main_512_16[str(t)][f"R_lme{key}"],
                             h_512_16[str(t)][f"R_lme{key}"]),
            )
        for level in LEVELS:
            lk = str(int(level))
            if (main_512_16[str(t)][f"L{lk}_tail_count"] >= 100 and
                    h_512_16[str(t)][f"L{lk}_tail_count"] >= 100):
                for suffix in ("tail_frequency", "danger_frequency", "conditional_haldane"):
                    h_probability_max = max(
                        h_probability_max,
                        sym_relative(main_512_16[str(t)][f"L{lk}_{suffix}"],
                                     h_512_16[str(t)][f"L{lk}_{suffix}"]),
                    )
    audit["step_moment_max_relative"] = h_moment_max
    audit["step_probability_max_relative"] = h_probability_max

    f32 = load(args.input_dir / "middle_saturation_audit_fp32draw64_n256.npz")
    f64 = load(args.input_dir / "middle_saturation_audit_fp64_n256.npz")
    dtype_moment_max = 0.0
    dtype_probability_max = 0.0
    for t in HORIZONS:
        s32 = checkpoint_stats(f32, t)
        s64 = checkpoint_stats(f64, t)
        for q in MOMENTS:
            for prefix in ("R", "B"):
                dtype_moment_max = max(
                    dtype_moment_max,
                    sym_relative(s32[f"{prefix}_q{q}"], s64[f"{prefix}_q{q}"]),
                )
        for lam in LAMBDAS:
            key = str(lam).replace(".", "p")
            dtype_moment_max = max(
                dtype_moment_max,
                sym_relative(s32[f"R_lme{key}"], s64[f"R_lme{key}"]),
            )
        for level in LEVELS:
            lk = str(int(level))
            if s32[f"L{lk}_tail_count"] >= 100 and s64[f"L{lk}_tail_count"] >= 100:
                for suffix in ("tail_frequency", "danger_frequency", "conditional_haldane"):
                    dtype_probability_max = max(
                        dtype_probability_max,
                        abs(s32[f"L{lk}_{suffix}"] - s64[f"L{lk}_{suffix}"]),
                    )
    audit["dtype_moment_max_relative"] = dtype_moment_max
    audit["dtype_probability_max_absolute"] = dtype_probability_max
    audit["float32_identity_max"] = max(
        stats[str(n)][str(t)]["identity_residual"] for n in WIDTHS for t in HORIZONS
    )
    audit["float64_identity_max"] = max(
        checkpoint_stats(f64, t)["identity_residual"] for t in HORIZONS
    )

    audit_pass = (
        h_moment_max <= 0.04
        and h_probability_max <= 0.08
        and dtype_moment_max <= 0.01
        and dtype_probability_max <= 0.02
        and audit["float32_identity_max"] <= 5e-5
        and audit["float64_identity_max"] <= 5e-10
    )
    formal_support = (
        not evidence_against
        and primary_slope_max <= 0.08
        and primary_ratio_max <= 1.25
        and c_t4_l2 is not None
        and c_t4_l2 < 0.10
        and audit_pass
    )
    result = {
        "stats": stats,
        "slopes": slopes,
        "endpoint_ratios": ratios,
        "primary_max_slope": primary_slope_max,
        "primary_max_ratio": primary_ratio_max,
        "T4_L2_conditional_4096": c_t4_l2,
        "evidence_against_cells": evidence_against,
        "audit": audit,
        "audit_pass": audit_pass,
        "formal_support": formal_support,
    }
    args.output_json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    rows = []
    for n in WIDTHS:
        s = stats[str(n)]["4.0"]
        rows.append(
            f"| {n} | {s['R_q8']:.4f} | {s['R_q12']:.4f} | "
            f"{s['R_lme1p0']:.4f} | {s['L2_conditional_haldane']:.4f} | "
            f"{s['L2_median_gate']:.4f} | {s['L2_suppressed_fraction']:.4f} |"
        )
    md = f"""# GPU result: middle-query saturation versus bath cancellation

**Status:** formal empirical support = **{formal_support}**; numerical audit
pass = **{audit_pass}**.  This is numerical evidence only.

The largest preregistered log-width slope of \(\|R_2\|_q/q\) was
`{primary_slope_max:.6g}`, and the largest width-4096/512 ratio was
`{primary_ratio_max:.6g}`.  The width-4096, \(T=4\), \(L=2\) dangerous
conditional fraction was `{c_t4_l2}`.  There were
`{len(evidence_against)}` evidence-against cells.

| width | R q8 | R q12 | log-mean-exp lambda1 | dangerous/tail L2 | median gate in tail | gate<1/2 in tail |
|---:|---:|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

Numerical audit maxima: step moment `{h_moment_max:.3g}`, step probability
`{h_probability_max:.3g}`, dtype moment `{dtype_moment_max:.3g}`, dtype
probability `{dtype_probability_max:.3g}`, float32 identity
`{audit['float32_identity_max']:.3g}`, and float64 identity
`{audit['float64_identity_max']:.3g}`.

Passing this diagnostic supports only the proposed saturation/nonalignment
mechanism at sampled tail scales.  It does not prove a cavity estimate,
exclude rarer cancellations, or change any theorem rung.
"""
    args.output_md.write_text(md)


if __name__ == "__main__":
    main()
