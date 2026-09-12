"""Evaluate analytic component bounds from retained data; no solver evolution."""
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import sys

import numpy as np


def strip_bound(coefficient, sigma, order, radius):
    if coefficient == 0 or sigma == 0:
        return 0.0
    logarithm = (math.log(coefficient) + math.lgamma(order + 1)
                 + math.log(max(1.0, math.tan(radius)))
                 + 2 * order * math.log(sigma / radius))
    return math.exp(min(math.log(2 * coefficient), logarithm))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--case", action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    generated = root / "data/generated/population_flow_computation"
    for path in (args.summary, args.output):
        if not path.resolve().is_relative_to(generated.resolve()):
            parser.error("input and output must belong to this study's generated data")
    args.output.mkdir(parents=True, exist_ok=False)
    prior_bytes = args.summary.read_bytes()
    summary = json.loads(prior_bytes)
    transport = summary["gaussian_quadrature_W1_estimates"]["32"]
    results = {}
    for name in args.case:
        record = summary["results"][name]
        paths = [Path(p) for p in summary["input_checkpoint_hashes"]
                 if Path(p).parent.name == name]
        if len(paths) != 1:
            raise ValueError("expected exactly one retained checkpoint per case")
        checkpoint = paths[0] if paths[0].is_absolute() else root / paths[0]
        if not checkpoint.resolve().is_relative_to(generated.resolve()):
            raise ValueError("checkpoint outside study data")
        with np.load(checkpoint, allow_pickle=False) as saved:
            w = saved["w"].astype(np.float64)
        with np.load(checkpoint.parent / "predictions.npz", allow_pickle=False) as saved:
            circle = saved["circle"].astype(np.float64)
        count = len(circle)
        angles = np.arange(count) * 2 * np.pi / count
        expected_circle = np.column_stack((np.cos(angles), np.sin(angles)))
        if not np.allclose(circle, expected_circle, rtol=0, atol=1e-14):
            raise ValueError("retained grid is not the stated uniform circle grid")
        whole_transport = record["conditional_quadrature_whole_circle_bound_estimate_q32"]
        grid_transport = record["conditional_quadrature_grid_bound_estimate_q32"]
        coefficient = whole_transport / transport
        max_sigma = grid_transport / whole_transport if coefficient else 0.0
        w_rms = float(np.sqrt(np.mean(np.sum(w * w, axis=1))))
        whole_sigma = min(1.0, max_sigma + 2 * w_rms * math.sin(math.pi / (2 * count)))
        estimates = {}
        for order in (16, 32):
            estimates[str(order)] = {
                "grid": min(strip_bound(coefficient, max_sigma, order, radius)
                            for radius in (math.pi / 4, 1.5)),
                "whole_circle": min(strip_bound(coefficient, whole_sigma, order, radius)
                                    for radius in (math.pi / 4, 1.5)),
            }
        results[name] = {
            "physical_time": record["physical_time"], "coefficient_mean_abs": coefficient,
            "grid_points": count, "maximum_grid_sigma": max_sigma,
            "w_rms": w_rms, "whole_circle_sigma_bound_estimate": whole_sigma,
            "quadrature_bound_estimates": estimates,
            "checkpoint_path": str(checkpoint),
            "prior_checkpoint_sha256": record["checkpoint_sha256"],
            "read_w_array_sha256": hashlib.sha256(w.tobytes()).hexdigest(),
        }
    payload = {
        "status": "floating evaluations of exact-arithmetic passive component bounds; not certified total errors",
        "trajectories": 0, "new_random_samples": 0,
        "input_summary_sha256": hashlib.sha256(prior_bytes).hexdigest(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "numpy": np.__version__,
        "argv": sys.argv, "results": results,
        "limitations": ["No interval enclosure of saved covariance or arithmetic.",
                        "Only the final saved state is covered by these evaluations.",
                        "No source, response, time, law or population error is bounded."],
    }
    (args.output / "results.json").write_text(json.dumps(payload, indent=2) + "\n")
    lines = ["# Passive analytic component evaluations", "",
             payload["status"], "",
             "| Case | max grid sigma | whole-circle sigma estimate | q=16 whole circle | q=32 whole circle |",
             "|---|---:|---:|---:|---:|"]
    for name, value in results.items():
        bounds = value["quadrature_bound_estimates"]
        lines.append(f"| {name} | {value['maximum_grid_sigma']:.6g} | "
                     f"{value['whole_circle_sigma_bound_estimate']:.6g} | "
                     f"{bounds['16']['whole_circle']:.6g} | {bounds['32']['whole_circle']:.6g} |")
    lines += ["", "Zero new trajectories or random samples; final saved-state component only.", ""]
    (args.output / "results.md").write_text("\n".join(lines))
    print(json.dumps(results))


if __name__ == "__main__":
    main()
