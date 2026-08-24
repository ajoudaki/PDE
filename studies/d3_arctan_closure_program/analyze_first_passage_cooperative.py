#!/usr/bin/env python3
"""Analyze the frozen first-passage cooperative-drift experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


LEVELS = (1.5, 2.0, 3.0)


def flat(data, name):
    return np.asarray(data[name]).reshape(-1)


def finite_median(x):
    x = np.asarray(x, dtype=np.float64)
    x = x[np.isfinite(x)]
    return float(np.median(x)) if x.size else None


def summarize(path):
    with np.load(path, allow_pickle=False) as data:
        width = int(data["width"])
        horizon = float(data["horizon"])
        result = {
            "path": str(path),
            "width": width,
            "replicas": int(data["replicas"]),
            "step": float(data["step"]),
            "dtype": str(data["dtype"]),
            "draw_float64": bool(data["draw_float64"]),
            "script_sha256": str(data["script_sha256"]),
            "identity_residual_max": float(np.max(data["identity_residual"])),
            "dz3_identity_residual_max": float(np.max(data["dz3_identity_residual"])),
            "dr2_identity_residual_max": float(np.max(data["dr2_identity_residual"])),
            "derivative_audit": {},
            "levels": {},
        }
        for field in ("z2", "z3", "r2"):
            result["derivative_audit"][field] = {
                "rms_max": float(np.max(data[f"fd_{field}_rms"])),
                "relative_max": float(np.max(data[f"fd_{field}_relative"])),
            }
        for level in LEVELS:
            key = str(level).replace(".", "p")
            prefix = f"L{key}_"
            seen = flat(data, prefix + "seen").astype(bool)
            om = flat(data, prefix + "open_misaligned_at_cross").astype(bool)
            cross_t = flat(data, prefix + "cross_time").astype(np.float64)
            coop = flat(data, prefix + "cross_coop").astype(np.float64)
            d = flat(data, prefix + "cross_D").astype(np.float64)
            zr = flat(data, prefix + "cross_ZR").astype(np.float64)
            rgrowth = flat(data, prefix + "cross_Rgrowth").astype(np.float64)
            opp = flat(data, prefix + "cross_opp_ratio").astype(np.float64)
            t_align = flat(data, prefix + "time_align").astype(np.float64)
            t_close = flat(data, prefix + "time_close").astype(np.float64)
            t_exit = flat(data, prefix + "time_exit").astype(np.float64)
            occ_o = flat(data, prefix + "occupation_O").astype(np.float64)
            occ_c = flat(data, prefix + "occupation_C").astype(np.float64)
            longest_o = flat(data, prefix + "longest_O").astype(np.float64)
            longest_c = flat(data, prefix + "longest_C").astype(np.float64)

            remaining = np.maximum(0.0, horizon - cross_t)
            ta = np.where(np.isfinite(t_align), t_align, remaining)
            tc = np.where(np.isfinite(t_close), t_close, remaining)
            te = np.where(np.isfinite(t_exit), t_exit, remaining)
            resolve = np.minimum(np.minimum(ta, tc), te)
            eligible = seen & om
            cell = {
                "coordinate_paths": int(seen.size),
                "passages": int(seen.sum()),
                "open_misaligned_passages": int(eligible.sum()),
                "passage_fraction": float(seen.mean()),
                "open_misaligned_fraction_of_passages": (
                    float(eligible.sum() / seen.sum()) if seen.sum() else None
                ),
                "p_coop_open_misaligned": (
                    float(np.mean(coop[eligible] > 0.0)) if eligible.any() else None
                ),
                "median_resolve_open_misaligned": finite_median(resolve[eligible]),
                "median_cross_D": finite_median(d[seen]),
                "fraction_cross_aligned": (
                    float(np.mean(zr[seen] > 0.0)) if seen.any() else None
                ),
                "fraction_cross_gate_closed": (
                    float(np.mean(d[seen] < 0.5)) if seen.any() else None
                ),
                "median_cross_coop": finite_median(coop[seen]),
                "median_cross_Rgrowth": finite_median(rgrowth[seen]),
                "median_opposing_ratio": finite_median(opp[seen]),
                "median_occupation_O": finite_median(occ_o[seen]),
                "median_occupation_C": finite_median(occ_c[seen]),
                "mean_occupation_O": (
                    float(np.mean(occ_o[seen])) if seen.any() else None
                ),
                "mean_occupation_C": (
                    float(np.mean(occ_c[seen])) if seen.any() else None
                ),
                "median_longest_O": finite_median(longest_o[seen]),
                "median_longest_C": finite_median(longest_c[seen]),
                "max_longest_O": float(np.max(longest_o[seen])) if seen.any() else None,
                "max_longest_C": float(np.max(longest_c[seen])) if seen.any() else None,
            }
            result["levels"][str(level)] = cell
    return result


def scalar_discrepancy(a, b, name):
    values = []
    for level in LEVELS:
        ca = a["levels"][str(level)]
        cb = b["levels"][str(level)]
        va, vb = ca.get(name), cb.get(name)
        if va is not None and vb is not None:
            values.append(abs(va - vb))
    return max(values) if values else None


def audit_pair(a, b):
    fields = (
        "passage_fraction", "open_misaligned_fraction_of_passages",
        "p_coop_open_misaligned", "median_resolve_open_misaligned",
        "median_occupation_O", "median_occupation_C",
    )
    return {name: scalar_discrepancy(a, b, name) for name in fields}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    files = sorted(args.input_dir.glob("first_passage_*.npz"))
    summaries = [summarize(path) for path in files]
    mains = {s["width"]: s for s in summaries if "_main_" in s["path"]}
    by_tag = {Path(s["path"]).stem: s for s in summaries}

    step_a = next((s for k, s in by_tag.items() if "audit_h001_n512" in k), None)
    step_b = next((s for k, s in by_tag.items() if "audit_h0005_n512" in k), None)
    fp32 = next((s for k, s in by_tag.items() if "audit_fp32draw64_n256" in k), None)
    fp64 = next((s for k, s in by_tag.items() if "audit_fp64_n256" in k), None)
    audits = {
        "step_halving": audit_pair(step_a, step_b) if step_a and step_b else None,
        "precision": audit_pair(fp32, fp64) if fp32 and fp64 else None,
    }

    target = mains.get(4096, {}).get("levels", {}).get("2.0")
    base = mains.get(512, {}).get("levels", {}).get("2.0")
    eligible = bool(target and target["passages"] >= 100 and
                    target["open_misaligned_passages"] >= 25)
    reasons = []
    if eligible:
        if target["p_coop_open_misaligned"] < 0.75:
            reasons.append("p_coop_below_0.75")
        if target["median_resolve_open_misaligned"] > 0.25:
            reasons.append("median_resolution_above_0.25")
        if target["median_occupation_C"] > 0.10:
            reasons.append("median_slow_tube_occupation_above_0.10")
        if (base and base["median_occupation_O"] is not None and
                target["median_occupation_O"] > 0.10 and
                target["median_occupation_O"] > 1.5 * base["median_occupation_O"]):
            reasons.append("open_misaligned_occupation_grows_with_width")
    evidence_against = eligible and bool(reasons)
    formal_support = bool(
        eligible and not evidence_against and
        target["p_coop_open_misaligned"] > 0.90 and
        target["median_resolve_open_misaligned"] < 0.10 and
        target["median_occupation_C"] < 0.05
    )

    payload = {
        "frozen_rule": {
            "eligible": eligible,
            "evidence_against": evidence_against,
            "evidence_against_reasons": reasons,
            "formal_support": formal_support,
        },
        "audits": audits,
        "runs": summaries,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload["frozen_rule"], indent=2))
    print(json.dumps(audits, indent=2))


if __name__ == "__main__":
    main()
