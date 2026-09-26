"""CPU-only initial prediction-kernel diagnostic for the frozen eight cases.

This computes no training trajectory and supplies no campaign decisions.
Run once with --out FRESH. Width, seed, activations and cases are fixed.
"""

from __future__ import annotations

import os

for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np
from scipy.special import expit, ndtr


STUDY = Path(__file__).resolve().parent
WIDTH, SEED = 4096, 20260920
ALPHA = 1.6732632423543772848170429916717
SCALE = 1.0507009873554804934193349852946
BLOCKS = ("W1", "W2", "W3", "c")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def array_hash(values):
    digest = hashlib.sha256()
    for value in values:
        digest.update(str(value.shape).encode())
        digest.update(str(value.dtype).encode())
        digest.update(memoryview(np.ascontiguousarray(value)).cast("B"))
    return digest.hexdigest()


def initialize(width, seed):
    rng = np.random.default_rng(seed)
    return (rng.standard_normal((width, 2)),
            rng.standard_normal((width, width)) / np.sqrt(width),
            rng.standard_normal((width, width)) / np.sqrt(width),
            rng.standard_normal(width) / width)


def frozen_inputs(case):
    """Match the launcher's scalar degree conversion and libm trig arithmetic exactly."""
    angles = [value * math.pi / 180 for value in case["angles_degrees"]]
    return np.asarray([[math.cos(angle), math.sin(angle)] for angle in angles], dtype=np.float64)


def activation_fields(z, name):
    if name == "relu":
        return np.maximum(z, 0.), (z > 0).astype(z.dtype)
    if name == "gelu":
        cdf = ndtr(z)
        return z * cdf, cdf + z * np.exp(-z * z / 2) / np.sqrt(2 * np.pi)
    if name == "selu":
        positive = z > 0
        h, derivative = np.empty_like(z), np.empty_like(z)
        h[positive], derivative[positive] = SCALE * z[positive], SCALE
        h[~positive] = SCALE * ALPHA * np.expm1(z[~positive])
        derivative[~positive] = SCALE * ALPHA * np.exp(z[~positive])
        return h, derivative
    if name == "sigmoid":
        h = expit(z)
        return h, h * (1 - h)
    raise ValueError("Unknown frozen activation")


def kernel_fields(weights, inputs, activation):
    """Return the four mobility-weighted Jacobian Gram blocks without n-by-n gradients."""
    w, W2, W3, c = weights
    n = len(c)
    h1, p1 = activation_fields(w @ inputs.T, activation)
    h2, p2 = activation_fields(W2 @ h1, activation)
    h3, p3 = activation_fields(W3 @ h2, activation)
    d3 = c[:, None] * p3
    d2 = p2 * (W3.T @ d3)
    d1 = p1 * (W2.T @ d2)
    blocks = dict(W1=(d1.T @ d1) * (inputs @ inputs.T) / n,
                  W2=(d2.T @ d2) * (h1.T @ h1) / n**2,
                  W3=(d3.T @ d3) * (h2.T @ h2) / n**2,
                  c=(h3.T @ h3) / n)
    fields = dict(inputs=inputs, h1=h1, h2=h2, h3=h3, d1=d1, d2=d2, d3=d3,
                  f=c @ h3 / n, n=n)
    return blocks, fields


def stable_quadratics(fields, q):
    """Evaluate q^T K_block q through squared norms, avoiding small Gram-quadratic cancellation."""
    n = fields["n"]
    result = dict(W1=float(np.sum(((fields["d1"] * q) @ fields["inputs"])**2) / n),
                  c=float(np.sum((fields["h3"] @ q)**2) / n))
    for name, backward, forward in (("W2", "d2", "h1"), ("W3", "d3", "h2")):
        _, left = np.linalg.qr(fields[backward] * q, mode="reduced")
        _, right = np.linalg.qr(fields[forward], mode="reduced")
        result[name] = float(np.sum((left @ right.T)**2) / n**2)
    return result


def tiny_autograd_check(inputs):
    """One independent blockwise verification suite using Torch's activation/backward implementations."""
    import torch
    import torch.nn.functional as F
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    n = 7
    # The same seed and literal inputs are used; only width is reduced for verification.
    weights = initialize(n, SEED)
    tensor_inputs = torch.tensor(inputs, dtype=torch.float64)
    checks = []
    for activation in ("relu", "gelu", "selu", "sigmoid"):
        tensors = tuple(torch.tensor(value, dtype=torch.float64, requires_grad=True) for value in weights)
        phi = {"relu": torch.relu, "gelu": lambda z: F.gelu(z, approximate="none"),
               "selu": F.selu, "sigmoid": torch.sigmoid}[activation]
        w, W2, W3, c = tensors
        hidden = phi(W3 @ phi(W2 @ phi(w @ tensor_inputs.T)))
        f = c @ hidden / n
        jacobians = [[] for _ in tensors]
        for value in f:
            derivatives = torch.autograd.grad(value, tensors, retain_graph=True)
            for collection, derivative in zip(jacobians, derivatives):
                collection.append(derivative.detach().numpy().ravel())
        formula, fields = kernel_fields(weights, inputs, activation)
        q = np.array([1., -1.] * (len(inputs) // 2))
        quadratic = stable_quadratics(fields, q)
        for name, mobility, rows in zip(BLOCKS, (n, 1., 1., n), jacobians):
            jacobian = np.stack(rows)
            independent = mobility * jacobian @ jacobian.T
            error = float(np.max(np.abs(independent - formula[name])))
            q_independent = float(mobility * np.sum((q @ jacobian)**2))
            quadratic_error = abs(quadratic[name] - q_independent)
            passed = np.allclose(independent, formula[name], rtol=2e-12, atol=2e-14) and np.isclose(
                quadratic[name], q_independent, rtol=2e-12, atol=2e-14)
            checks.append(dict(activation=activation, block=name, maximum_absolute_error=error,
                               quadratic_absolute_error=quadratic_error, passed=bool(passed)))
        if not np.allclose(f.detach().numpy(), fields["f"], rtol=2e-12, atol=2e-14):
            raise ArithmeticError("Tiny forward check failed")
    if not all(row["passed"] for row in checks):
        raise ArithmeticError("Tiny kernel autograd check failed")
    return dict(width=n, seed=SEED, sample_count=len(inputs), checks=checks,
                torch_version=torch.__version__, device="cpu", threads=1, passed=True)


def analyze_case(weights, inputs, labels, activation):
    start = time.monotonic()
    blocks, fields = kernel_fields(weights, inputs, activation)
    kernel = sum(blocks.values())
    symmetry_error = float(np.max(np.abs(kernel - kernel.T)))
    kernel = (kernel + kernel.T) / 2
    eigenvalues, eigenvectors = np.linalg.eigh(kernel)
    label_weights = (eigenvectors.T @ labels)**2
    residual = fields["f"] - labels
    residual_weights = (eigenvectors.T @ residual)**2
    label_quadratics, residual_quadratics = stable_quadratics(fields, labels), stable_quadratics(fields, residual)
    label_q, residual_q = sum(label_quadratics.values()), sum(residual_quadratics.values())
    m, n = len(labels), fields["n"]
    scale = float(max(np.max(np.abs(eigenvalues)), np.finfo(float).tiny))
    # Heuristic float64 screen accounting for length-n contractions; not a certified error bound.
    screen = float(64 * max(n, m) * np.finfo(float).eps * scale)
    resolved = eigenvalues > screen
    if float(eigenvalues[0]) < -screen:
        raise ArithmeticError("Kernel has negative eigenvalue beyond the diagnostic precision screen")
    eigen_label_q = float(eigenvalues @ label_weights)
    row = dict(activation=activation, width=n, M=m, initialization_prediction_rms=float(np.sqrt(np.mean(fields["f"]**2))),
               initialization_loss=float(np.mean(residual**2)), kernel_trace=float(np.trace(kernel)),
               lambda_min=float(eigenvalues[0]), lambda_max=float(eigenvalues[-1]),
               numerical_resolution_screen=screen, modes_above_screen=int(np.count_nonzero(resolved)),
               condition_number_if_resolved=float(eigenvalues[-1] / eigenvalues[0]) if np.all(resolved) else None,
               raw_eigenvalue_ratio=float(eigenvalues[-1] / eigenvalues[0]) if eigenvalues[0] > 0 else None,
               label_energy_fraction_below_screen=float(label_weights[~resolved].sum() / (labels @ labels)),
               label_energy_fraction_in_two_slowest_modes=float(label_weights[:2].sum() / (labels @ labels)),
               label_quadratic=label_q, residual_quadratic=residual_q,
               label_initial_loss_decay_rate=4 * label_q / m**2,
               actual_initial_loss_decay_rate=4 * residual_q / m**2,
               actual_initial_relative_loss_decay_rate=4 * residual_q / (m * float(residual @ residual)),
               label_rayleigh_quotient=label_q / float(labels @ labels),
               stable_vs_gram_label_quadratic_absolute_difference=abs(label_q - float(labels @ kernel @ labels)),
               stable_vs_eigen_label_quadratic_absolute_difference=abs(label_q - eigen_label_q),
               kernel_symmetry_max_absolute_error=symmetry_error,
               eigendecomposition_max_absolute_residual=float(np.max(np.abs(kernel @ eigenvectors - eigenvectors * eigenvalues))),
               readout_trace_fraction=float(np.trace(blocks["c"]) / np.trace(kernel)),
               readout_label_quadratic_fraction=label_quadratics["c"] / label_q if label_q > 0 else None,
               cpu_wall_seconds=time.monotonic() - start)
    for name in BLOCKS:
        row[name + "_trace"] = float(np.trace(blocks[name]))
        row[name + "_label_quadratic"] = label_quadratics[name]
        row[name + "_residual_quadratic"] = residual_quadratics[name]
    arrays = dict(kernel=kernel, eigenvalues=eigenvalues, eigenvectors=eigenvectors,
                  label_eigenmode_weights=label_weights, residual_eigenmode_weights=residual_weights,
                  initialization_predictions=fields["f"], initialization_residual=residual,
                  inputs=inputs, labels=labels, **{"kernel_" + name: value for name, value in blocks.items()})
    return row, arrays


def run(out, max_seconds=120.):
    started = time.monotonic()
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    cases = json.loads((STUDY / "activation_circle_cases.json").read_text())
    inputs = {name: frozen_inputs(case) for name, case in cases.items()}
    # Build the frozen configurations without launching any process or training.
    from run_activation_circle_campaign import build_jobs
    jobs = build_jobs("primary", cases)
    input_checks = []
    for name, values in inputs.items():
        references = [job["config"] for job in jobs if job["config"]["case"] == name]
        exact = all(np.array_equal(values, np.asarray(config["inputs"], dtype=np.float64))
                    for config in references)
        if len(references) != 8 or not exact:
            raise ArithmeticError("Diagnostic inputs differ from frozen launcher configurations")
        input_checks.append(dict(case=name, matched_launcher_configs=len(references), bitwise_equal=exact,
                                 data_sha256=array_hash((values, np.asarray(cases[name]["labels"], dtype=np.float64)))))
    write_json(out / "input_verification.json", dict(reference="run_activation_circle_campaign.build_jobs('primary', cases)",
        no_process_launched=True, checks=input_checks, launcher_sha256=sha256(STUDY / "run_activation_circle_campaign.py")))
    checked = tiny_autograd_check(inputs[next(iter(cases))])
    write_json(out / "tiny_autograd_check.json", checked)
    weights = initialize(WIDTH, SEED)
    initial_hash = array_hash(weights)
    records, inventory = [], []
    for name, case in cases.items():
        if time.monotonic() - started > max_seconds:
            break
        row, arrays = analyze_case(weights, inputs[name], np.asarray(case["labels"], dtype=float), case["activation"])
        row.update(case=name, task=case["task"])
        records.append(row)
        filename = name + ".npz"
        np.savez(out / filename, **arrays)
        inventory.append(dict(case=name, file=filename, sha256=sha256(out / filename)))
        print(json.dumps(dict(case=name, lambda_min=row["lambda_min"], lambda_max=row["lambda_max"],
                             initial_loss_decay_rate=row["actual_initial_loss_decay_rate"],
                             modes_above_screen=row["modes_above_screen"], seconds=row["cpu_wall_seconds"])), flush=True)
    result = dict(status="complete" if len(records) == 8 else "cpu_wall_budget_stopped", exploratory=True,
                  no_training=True, no_gpu=True, width=WIDTH, seed=SEED, threads=1,
                  initialization_sha256=initial_hash, source_sha256={name: sha256(STUDY / name) for name in
                  ("activation_initial_kernel.py", "ACTIVATION_CIRCLE_PROTOCOL.md", "activation_circle_cases.json",
                   "run_activation_circle_campaign.py")},
                  input_arithmetic="degrees*math.pi/180; math.cos, math.sin; bitwise checked against all64 launcher configurations",
                  cpu_wall_seconds=time.monotonic() - started, max_seconds=max_seconds,
                  completed_cases=len(records), records=records, artifacts=inventory,
                  tiny_autograd_check_passed=checked["passed"],
                  environment=dict(python=sys.version, numpy=np.__version__, platform=platform.platform()),
                  precision_caveat="64*max(n,M)*eps*max_abs_eigenvalue is a heuristic float64 resolution screen, not a certified bound",
                  interpretation="Initial local linear response only; does not identify later feature-moving dynamics or cause slow fitting")
    write_json(out / "metrics_summary.json", result)
    if records:
        with (out / "kernel_metrics.csv").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(records[0]))
            writer.writeheader()
            writer.writerows(records)
    write_json(out / "artifact_manifest.json", {p.name: sha256(p) for p in sorted(out.iterdir()) if p.is_file()})
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    result = run(args.out)
    print(json.dumps(dict(status=result["status"], completed_cases=result["completed_cases"],
                          cpu_wall_seconds=result["cpu_wall_seconds"])), flush=True)
