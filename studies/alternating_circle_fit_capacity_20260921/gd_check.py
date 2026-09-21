#!/usr/bin/env python3
"""Independent no-training GD gradient/one-step audit; run with NumPy and Torch.

The NumPy chain rule below is independent of the maintained implementation.
No fitting loop is present. Optional snapshots use canonical stored c, inputs
already divided by sqrt(2), and keys kind,w,c,middle,inputs,labels,b1,b2.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.finite_network import Parameters, flow_velocity, gd_step
from pde.finite_torch import NetworkEngine
from pde.observable_torch_p1 import ClosureEngine

ATOL, RTOL = 2e-12, 2e-10
ETA = 0.003


def prediction(case, w, middle, v):
    h = np.tanh(w @ case["inputs"].T)
    if case["kind"] == "dense":
        z = middle @ h
    else:
        z = case["b2"] @ middle @ (case["b1"].T @ h / len(w))
    return v @ np.tanh(z)


def explicit_gradients(case):
    """Return ordinary Euclidean gradients in W,middle,v coordinates."""
    w, a, c = (case[k] for k in ("w", "middle", "c"))
    n, m = len(c), len(case["labels"])
    h = np.tanh(w @ case["inputs"].T)
    s = h if case["kind"] == "dense" else case["b1"].T @ h / n
    z = a @ s
    if case["kind"] == "closure":
        z = case["b2"] @ z
    j = np.tanh(z)
    f = (c / n) @ j
    r = f - case["labels"]
    e = (c / n)[:, None] * (1 - j * j)
    d = e if case["kind"] == "dense" else case["b2"].T @ e
    gm = (2 / m) * (d * r) @ s.T
    back = a.T @ d
    if case["kind"] == "closure":
        back = case["b1"] @ back / n
    gw = (2 / m) * ((back * (1 - h * h)) * r) @ case["inputs"]
    gv = (2 / m) * j @ r
    return (gw, gm, gv), f, float(np.mean(r * r))


def comparison(left, right, *, atol=ATOL, rtol=RTOL):
    left, right = np.asarray(left), np.asarray(right)
    error = np.abs(left - right)
    tolerance = atol + rtol * np.abs(right)
    ratio = np.divide(error, tolerance, out=np.where(error == 0, 0.0, np.inf),
                      where=tolerance > 0)
    return {"pass": bool(np.all(np.isfinite(left)) and np.all(np.isfinite(right))
                         and np.all(error <= tolerance)),
            "max_absolute_error": float(np.max(error)),
            "max_tolerance_ratio": float(np.max(ratio))}


def directional_checks(case, grads):
    point = [case["w"].copy(), case["middle"].copy(), case["c"].copy() / len(case["c"])]
    out = {}
    for block, name in enumerate(("w", "middle", "v")):
        gradient = grads[block]
        norm = float(np.linalg.norm(gradient))
        direction = gradient / norm if norm else np.ones_like(gradient) / np.sqrt(gradient.size)
        plus, minus = [x.copy() for x in point], [x.copy() for x in point]
        plus[block] += 1e-5 * direction
        minus[block] -= 1e-5 * direction
        lp = np.mean((prediction(case, *plus) - case["labels"]) ** 2)
        lm = np.mean((prediction(case, *minus) - case["labels"]) ** 2)
        numerical = (lp - lm) / 2e-5
        analytic = float(np.sum(gradient * direction))
        out[name] = comparison(numerical, analytic, atol=5e-9, rtol=2e-5)
    return out


def torch_checks(case, device, grads, f_numpy, loss_numpy):
    n = len(case["c"])
    tensor = lambda a: torch.tensor(a, dtype=torch.float64, device=device)
    u, y = tensor(case["inputs"]), tensor(case["labels"])
    w = tensor(case["w"]).requires_grad_(True)
    a = tensor(case["middle"]).requires_grad_(True)
    v = tensor(case["c"] / n).requires_grad_(True)
    h = torch.tanh(w @ u.T)
    if case["kind"] == "dense":
        j = torch.tanh(a @ h)
    else:
        j = torch.tanh(tensor(case["b2"]) @ a @ (tensor(case["b1"]).T @ h / n))
    f = v @ j
    loss = torch.mean((f - y).square())
    actual_grads = torch.autograd.grad(loss, (w, a, v), retain_graph=True)
    half_grads = torch.autograd.grad(loss / 2, (w, a, v))
    cpu = lambda x: x.detach().cpu().numpy()
    checks = {"prediction": comparison(cpu(f), f_numpy),
              "loss": comparison(cpu(loss), loss_numpy)}
    for name, actual, half, expected in zip(("w", "middle", "v"), actual_grads, half_grads, grads):
        checks["autograd_" + name] = comparison(cpu(actual), expected)
        checks["half_loss_" + name] = comparison(cpu(half) * 2, expected)

    kwargs = dict(device=device, dtype=torch.float64, block_size=3)
    if case["kind"] == "dense":
        engine = NetworkEngine(2, n, 0, **kwargs)
    else:
        engine = ClosureEngine(case["b1"], case["w"], case["b2"], case["middle"], **kwargs)
    state = engine.state(case["w"], case["c"], case["middle"])
    data = engine.prepare_data(case["inputs"], case["labels"])
    physical = (-n * grads[0], -grads[1], -grads[2])
    rhs = engine.rhs(state, data)
    for name, actual, expected in zip(("w", "middle", "c"), (rhs.w, rhs.M, rhs.c), physical):
        checks["maintained_rhs_" + name] = comparison(cpu(actual), expected)
    if case["kind"] == "closure":
        reference = engine.rhs(state, data, implementation="reference")
        for name, actual, expected in zip(("w", "middle", "c"),
                                          (reference.w, reference.M, reference.c), physical):
            checks["maintained_reference_rhs_" + name] = comparison(cpu(actual), expected)

    # One simultaneous ordinary SGD update with the derived parameter groups.
    opt = torch.optim.SGD([{"params": [w], "lr": ETA * n},
                           {"params": [a], "lr": ETA},
                           {"params": [v], "lr": ETA / n}], lr=ETA)
    for parameter, gradient in zip((w, a, v), actual_grads):
        parameter.grad = gradient.detach().clone()
    opt.step()
    updated = (cpu(w), cpu(a), cpu(v) * n)
    for name, actual, start, velocity in zip(("w", "middle", "c"), updated,
                                             (case["w"], case["middle"], case["c"]), physical):
        checks["simultaneous_sgd_" + name] = comparison(actual, start + ETA * velocity)
    fixed_after = [engine.b1, engine.b2] if case["kind"] == "closure" else []
    for name, actual in zip(("b1", "b2"), fixed_after):
        checks["frozen_" + name] = comparison(cpu(actual), case[name], atol=0, rtol=0)
        # Exact-equality check needs no zero-denominator diagnostic.
        checks["frozen_" + name]["max_tolerance_ratio"] = 0.0
    return checks


def make_cases():
    cases = []
    m = 10
    theta = 2 * np.pi * np.arange(m) / m
    inputs = np.column_stack((np.cos(theta), np.sin(theta))) / np.sqrt(2)
    labels = (-1.0) ** np.arange(m)
    for kind, n in (("dense", 55), ("dense", 105), ("closure", 1024)):
        rng = np.random.default_rng(88103 + n)
        w = 0.6 * rng.standard_normal((n, 2))
        base = dict(kind=kind, w=w, inputs=inputs, labels=labels)
        if kind == "dense":
            base["middle"] = 0.6 * rng.standard_normal((n, n)) / np.sqrt(n)
        else:
            base["b1"] = np.column_stack((np.ones(n), np.tanh(w),
                                          np.tanh(rng.standard_normal((n, 2)))))
            base["b2"] = np.column_stack((np.ones(n), np.tanh(rng.standard_normal((n, 2)))))
            base["middle"] = 0.3 * rng.standard_normal((3, 5))
        for zero in (False, True):
            case = dict(base)
            case["c"] = np.zeros(n) if zero else 0.4 * rng.standard_normal(n)
            case["name"] = f"synthetic_{kind}_n{n}_" + ("zero" if zero else "nonzero")
            case["expect_all_nonzero"] = not zero
            cases.append(case)
    return cases


def highgain_cases():
    """Neutral recipe supplied by supervisor, not copied from producer code."""
    cases = []
    m, seed = 62, 20260921
    theta = 2 * np.pi * np.arange(m) / m
    inputs = np.column_stack((np.cos(theta), np.sin(theta))) / np.sqrt(2)
    labels = (-1.0) ** np.arange(m)
    for kind, n in (("dense", 55), ("dense", 105), ("closure", 1024)):
        rng = np.random.default_rng(seed)
        w = rng.standard_normal((n, 2))
        a = rng.standard_normal((n, n)) / np.sqrt(n)
        c = rng.standard_normal(n) / n
        w *= m / 2
        case = dict(name=f"recipe_highgain_{kind}_n{n}", kind=kind, w=w, c=c,
                    middle=a, inputs=inputs, labels=labels, expect_all_nonzero=True)
        if kind == "closure":
            h = np.tanh(w)
            upper = np.tanh(a @ h)
            reverse = np.tanh(a.T @ upper)
            raw1 = np.column_stack((np.ones(n), h, reverse))
            raw2 = np.column_stack((np.ones(n), upper))
            l1 = np.linalg.cholesky(raw1.T @ raw1 / n + np.eye(5) / 4096)
            l2 = np.linalg.cholesky(raw2.T @ raw2 / n + np.eye(3) / 4096)
            b1 = np.linalg.solve(l1, raw1.T).T
            b2 = np.linalg.solve(l2, raw2.T).T
            case.update(b1=b1, b2=b2, middle=b2.T @ a @ b1 / n)
        cases.append(case)
    return cases


def all_pass(value):
    if isinstance(value, dict):
        return all_pass(list(value.values())) if "pass" not in value else bool(value["pass"])
    if isinstance(value, list):
        return all(all_pass(x) for x in value)
    return True


def run_case(case, devices):
    grads, prediction_numpy, loss_numpy = explicit_gradients(case)
    norms = {k: float(np.linalg.norm(g)) for k, g in zip(("w", "middle", "v"), grads)}
    checks = {"directional": directional_checks(case, grads)}
    if case.get("expect_all_nonzero", False):
        checks["nonvacuity"] = {"pass": all(value > 0 for value in norms.values())}
    if case["kind"] == "dense":
        parameters = Parameters((case["w"], case["middle"]), case["c"])
        # finite_network expects x, whereas the tensor APIs expect u=x/sqrt(d).
        x = case["inputs"].T * np.sqrt(2)
        rhs = flow_velocity(parameters, x, case["labels"])
        updated = gd_step(parameters, x, case["labels"], ETA)
        velocities = (-len(case["c"]) * grads[0], -grads[1], -grads[2])
        checks["maintained_numpy"] = {}
        for name, actual, after, start, expected in zip(
                ("w", "middle", "c"), (*rhs.weights, rhs.readout),
                (*updated.weights, updated.readout), (case["w"], case["middle"], case["c"]), velocities):
            checks["maintained_numpy"][name] = comparison(actual, expected)
            checks["maintained_numpy"][name + "_step"] = comparison(after, start + ETA * expected)
    for device in devices:
        checks[device] = torch_checks(case, device, grads, prediction_numpy, loss_numpy)
    n = len(case["c"])
    # Shared Euclidean LR / desired physical LR ratios in optimizer coordinates.
    mismatch = {"w": 1 / n, "middle": 1.0, "v": float(n)}
    return dict(name=case["name"], kind=case["kind"], population_count=n,
                samples=len(case["labels"]), loss=loss_numpy, gradient_norms=norms,
                euclidean_shared_step_to_physical_step_ratios=mismatch,
                checks=checks, passed=all_pass(checks))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--devices", nargs="+", default=["cpu"])
    parser.add_argument("--include-highgain", action="store_true")
    parser.add_argument("--snapshot", type=Path, action="append", default=[])
    parser.add_argument("--output", type=Path, default=ROOT / "data/generated/alternating_circle_fit_capacity_20260921/gd_check_scratch/preflight.json")
    args = parser.parse_args()
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.use_deterministic_algorithms(True)
    cases = make_cases()
    if args.include_highgain:
        cases += highgain_cases()
    for path in args.snapshot:
        with np.load(path, allow_pickle=False) as saved:
            case = {key: saved[key].copy() for key in saved.files}
        case["kind"] = str(case["kind"])
        case["name"] = "snapshot_" + path.stem
        cases.append(case)
    results = [run_case(case, args.devices) for case in cases]
    source_paths = [Path(__file__), Path(__file__).with_suffix(".md"),
                    ROOT / "docs/NOTATION.md", ROOT / "code/pde/finite_network.py",
                    ROOT / "code/pde/finite_torch.py", ROOT / "code/pde/observable_torch_p1.py"]
    report = dict(passed=all(r["passed"] for r in results), eta=ETA,
                  devices=args.devices, dtype="float64", training_steps=0,
                  independent_single_steps_per_case_per_device=1,
                  versions={"python": sys.version, "numpy": np.__version__, "torch": str(torch.__version__)},
                  source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},
                  results=results)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"passed": report["passed"], "cases": len(cases), "devices": args.devices,
                      "report": str(args.output)}))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
