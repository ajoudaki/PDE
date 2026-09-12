"""Summarize saved bounded runs without executing trajectories or claiming accuracy."""
from pathlib import Path
import argparse
import hashlib
import json
import sys

import numpy as np
from scipy.special import ndtr, ndtri, roots_hermitenorm

from directional_solver import DirectionalSolver


def normal_quadrature_transport(order):
    nodes, weights = roots_hermitenorm(order)
    weights = weights/np.sqrt(2*np.pi)
    weights = weights/weights.sum()
    bounds = np.r_[0., np.cumsum(weights)]
    bounds[-1] = 1.
    quantiles = ndtri(np.clip(bounds, 0, 1))
    density = lambda x: np.exp(-x*x/2)/np.sqrt(2*np.pi)
    result = 0.
    for i, node in enumerate(nodes):
        middle = np.clip(node, quantiles[i], quantiles[i+1])
        result += node*(2*ndtr(middle)-bounds[i]-bounds[i+1])+2*density(middle)-density(quantiles[i])-density(quantiles[i+1])
    return float(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=Path, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    study = Path(__file__).resolve().parent
    generated = study.parents[1]/"data/generated/population_flow_computation"
    if not args.output.resolve().is_relative_to(generated.resolve()):
        parser.error("output must be study-owned generated data")
    args.output.mkdir(parents=True, exist_ok=False)
    results, predictions, sources = {}, {}, {}
    for run in args.runs:
        for outcome in json.loads((run/"outcomes.json").read_text()):
            name = outcome["name"]
            if outcome["status"] != "completed":
                results[name] = outcome
                continue
            folder = run/name
            diagnostics = json.loads((folder/"diagnostics.json").read_text())
            moments = json.loads((folder/"joint_moments.json").read_text())
            with np.load(folder/"predictions.npz") as z:
                predictions[name] = {k:z[k].copy() for k in z.files}
            solver = DirectionalSolver.load(folder/"final_state.npz")
            sigma = np.sqrt(solver._passive_fields(predictions[name]["circle"])[3])
            transport = normal_quadrature_transport(32)
            quad_bound = np.mean(np.abs(solver.c))*float(np.max(sigma))*transport
            results[name] = {**outcome, "diagnostics": diagnostics, "joint_moments": moments,
                             "conditional_quadrature_grid_bound_estimate_q32": float(quad_bound),
                             "conditional_quadrature_whole_circle_bound_estimate_q32": float(np.mean(np.abs(solver.c))*transport)}
            sources[str(folder/"final_state.npz")] = outcome["checkpoint_sha256"]
            del solver
    comparisons = {}
    for name in ("reference_time", "reference_samples", "reference_noise", "reference_precision", "reference_combined"):
        if name in predictions and "reference_base" in predictions:
            comparisons[name+"_vs_base"] = float(np.max(np.abs(predictions[name]["predictions"]-predictions["reference_base"]["predictions"])))
    for first, second in (("reference_combined", "reference_time"), ("reference_combined", "reference_samples"), ("arc_quadrature_2", "arc_quadrature_4")):
        if first in predictions and second in predictions:
            comparisons[first+"_vs_"+second] = float(np.max(np.abs(predictions[first]["predictions"]-predictions[second]["predictions"])))
    summary = {"status": "empirical grid comparisons; no population-error certificate", "results": results,
               "comparisons": comparisons, "gaussian_quadrature_W1_estimates": {str(q):normal_quadrature_transport(q) for q in (16,32,64,128)},
               "input_checkpoint_hashes": sources, "argv": sys.argv,
               "analysis_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (args.output/"summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    lines = ["# Bounded numerical diagnostics", "", "These are finite-process observations, not certified population errors.", "",
             "| Case | Physical time | Calls | State MB | Seconds | Passive training loss |", "|---|---:|---:|---:|---:|---:|"]
    for name, result in results.items():
        d = result.get("diagnostics", {})
        if d:
            lines.append(f"| {name} | {d['physical_time']:g} | {d['calls']} | {d['state_array_bytes']/1e6:.2f} | {result['wall_seconds']:.2f} | {d['passive_training_loss']:.6g} |")
    lines += ["", "Grid comparison: 9 physical times and 65 circle directions for the time-40 cases.", "",
              "| Refinement comparison | Maximum checked prediction difference |", "|---|---:|"]
    for name, error in comparisons.items():
        lines.append(f"| {name} | {error:.8g} |")
    lines += ["", "Sampling/time refinements use a single seed and are not an error decomposition. The arc cases approximate one fixed nonatomic law outside the certified regime claimed here.", "",
              "The passive quadrature bounds use the exact-arithmetic formula in passive_quadrature.md evaluated with floating-point Gaussian functions; they do not include certified function/node rounding or any other solver error.", ""]
    (args.output/"summary.md").write_text("\n".join(lines))
    print(json.dumps({"comparisons":comparisons,"quadrature_W1":summary["gaussian_quadrature_W1_estimates"]}))


if __name__ == "__main__":
    main()
