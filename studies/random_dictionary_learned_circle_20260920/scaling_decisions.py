"""Persist frozen-protocol branch checks from completed scaling analyses.

No trajectories or scientific search. Scalar error arithmetic is CUDA float64;
dictionary metadata checks supplement the analyzer's replay/refinement gates.
The independent check remains a separate prerequisite for accepting comparisons.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import torch

from benchmark import setup


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metadata_failures(key, record):
    failures = []
    for level in ("primary", "refined"):
        item = record[level]
        if item.get("declared_executed") is False:
            failures.append(f"{level}: producer did not declare execution")
        # Historical adapters had no separate dictionary metadata files. Their
        # unchanged source and exact old-builder equivalence are audited separately.
        if key.endswith("_full") or "declared_executed" not in item:
            continue
        entries = item.get("dictionary_metadata", [])
        if not entries:
            failures.append(f"{level}: missing fresh dictionary metadata")
        for entry in entries:
            meta = entry["metadata"]
            if not meta.get("all_finite"):
                failures.append(f"{level}: dictionary not finite")
            for population in meta["populations"]:
                if not all(population["finite_checks"].values()):
                    failures.append(f"{level}: finite check failed")
                if meta["method"] == "ours":
                    for name, bound in (("ridge_condition", 1e10), ("triangular_solve_residual", 1e-8)):
                        value = population.get(name)
                        if value is None or not math.isfinite(value) or value > bound:
                            failures.append(f"{level}: {name}={value}")
                if meta["method"] == "orthogonal":
                    if any(not math.isfinite(x) or abs(x - 1) > 1e-8
                           for x in population["normalized_gram_eigenvalues"]):
                        failures.append(f"{level}: orthogonal residual failed")
    return failures


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--analysis", type=Path, required=True)
    p.add_argument("--high", type=int, choices=(7, 9), required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--device", required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    summary = json.loads((args.analysis / "summary.json").read_text())
    rows = json.loads((args.analysis / "metrics.json").read_text())
    validation = json.loads((args.analysis / "validation.json").read_text())
    metadata = {key: metadata_failures(key, value) for key, value in validation.items()}
    failures = {key: value["reasons"] + metadata[key] for key, value in validation.items()
                if not value["valid"] or metadata[key]}
    device = setup(args.device)
    tensor = lambda x: torch.tensor(x, dtype=torch.float64, device=device)
    discriminators = {}
    for case in summary["cases"]:
        lookup = {row["model"]: row for row in rows if row["case"] == case}
        result = {"high_order": args.high, "levels": {}}
        involved = [f"{method}_p{order}" for order in (5, args.high)
                    for method in ("ours", "gaussian", "orthogonal")]
        valid = all(model in lookup and lookup[model]["valid"] and not metadata[case + "_" + model]
                    for model in involved) and case + "_full" not in failures
        result["all_involved_valid"] = valid
        for prefix in ("", "refined_"):
            if not valid:
                result["levels"][prefix or "primary"] = {"passes": False, "reason": "invalid/missing involved comparison"}
                continue
            low, high = (tensor(lookup[f"ours_p{order}"][prefix + "l2"]) for order in (5, args.high))
            better = [torch.stack([tensor(lookup[f"{method}_p{order}"][prefix + "l2"])
                                  for method in ("gaussian", "orthogonal")]).min()
                      for order in (5, args.high)]
            ratios = (better[0] / low, better[1] / high)
            reduction, gain = 1 - high / low, ratios[1] / ratios[0] - 1
            result["levels"][prefix or "primary"] = {
                "ours_p5_rms": float(low), "ours_high_rms": float(high),
                "ours_rms_reduction_fraction": float(reduction),
                "p5_better_random_over_ours": float(ratios[0]),
                "high_better_random_over_ours": float(ratios[1]),
                "ratio_increase_fraction": float(gain),
                "passes": bool(reduction >= .15 and gain >= .20)}
        result["passes_both_levels"] = valid and all(v["passes"] for v in result["levels"].values())
        discriminators[case] = result
    extra = sorted(key for key, value in validation.items()
                   if all(value[level]["fitted"] for level in ("primary", "refined"))
                   and value["step_refinement_endpoint_max"] is not None
                   and value["step_refinement_endpoint_max"] > .01)
    result = {
        "analysis": str(args.analysis.resolve()), "command": [sys.executable, "-B", *sys.argv],
        "source_sha256": digest(Path(__file__)),
        "input_hashes": {name: digest(args.analysis / name) for name in ("summary.json", "metrics.json", "validation.json")},
        "all_comparisons_and_metadata_valid": summary["all_comparisons_valid"] and not failures,
        "failures": failures, "eligible_resolution_cells_literal_order": extra,
        "discriminators": discriminators,
        "any_discovery_discriminator": any(v["passes_both_levels"] for v in discriminators.values()),
        "qualification": "Apply independent audit, stage ordering, remaining 12-cell allowance and worker budget before launch. No asymptotic inference."}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    torch.cuda.synchronize(device)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
