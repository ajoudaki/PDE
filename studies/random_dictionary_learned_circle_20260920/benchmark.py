"""Bounded CUDA comparison; see README for the pre-training contract."""
import os
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.finite_torch import NetworkEngine
from pde.observable_torch_p1 import ClosureEngine, TensorState
from pde.observable_initialization import build_dictionary

CASES = {
    "four": ([15, 70, 160, 265], [1, -1, 1, -1]),
    "eight": ([11, 39, 86, 129, 174, 226, 278, 323], [1, 1, -1, -1, 1, -1, 1, -1]),
}
N, NETWORK_SEED, DICTIONARY_SEED = 512, 20260920, 7319
THRESHOLD, MAX_TIME = 1e-3, 300.0
SNAPSHOTS = [0, 1, 2, 5, 10, 20, 40, 80, 160, 300]


def setup(device="cuda:1"):
    if not torch.cuda.is_available():
        raise RuntimeError("GPU required; CPU simulation is forbidden")
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.set_float32_matmul_precision("highest")
    torch.cuda.set_device(device)
    return device


def circle(size, device):
    angles = torch.arange(size, device=device, dtype=torch.float64) * (2 * math.pi / size)
    return angles, torch.stack((angles.cos(), angles.sin()), dim=1)


def polynomial_values(coordinates, exponents, order):
    terms = [torch.ones_like(coordinates), coordinates]
    for _ in range(1, order):
        terms.append(2 * coordinates * terms[-1] - terms[-2])
    columns = []
    for powers in exponents:
        v = torch.ones(len(coordinates), dtype=coordinates.dtype, device=coordinates.device)
        for j, degree in enumerate(powers):
            v = v * terms[degree][:, j]
        columns.append(v)
    return torch.stack(columns, dim=1)


@torch.no_grad()
def dictionaries(initial, order, method):
    definition = build_dictionary(order)
    if definition.first_tail or definition.second_tail or order not in (1, 3):
        raise ValueError("This bounded adapter only implements the exact p=1,3 polynomial cores")
    ranks = (len(definition.first_words), len(definition.second_words))
    n, device = len(initial.w), initial.w.device
    if method == "ours":
        lower = initial.w.tanh()
        upper = (initial.M @ lower).tanh()
        reverse = (initial.M.T @ upper).tanh()
        coordinates = (torch.cat((lower, reverse), dim=1), upper)
        bases = []
        ridge = 1 / (1024 * (order + 1) ** 2)
        for x, exponents in zip(coordinates, (definition.first_exponents, definition.second_exponents)):
            raw = polynomial_values(x, exponents, order)
            gram = raw.T @ raw / n
            L = torch.linalg.cholesky(gram + ridge * torch.eye(len(exponents), device=device, dtype=x.dtype))
            bases.append(torch.linalg.solve_triangular(L, raw.T, upper=False).T.contiguous())
        return bases
    if method not in ("gaussian", "orthogonal"):
        raise ValueError(method)
    bases = []
    for layer, rank in enumerate(ranks):
        gen = torch.Generator(device=device).manual_seed(DICTIONARY_SEED + layer)
        # Maximal array gives a nested prefix for both declared orders.
        raw = torch.randn((n, (35, 10)[layer]), generator=gen, device=device, dtype=torch.float64)[:, :rank]
        if method == "gaussian":
            basis = raw / raw.square().mean(dim=0).sqrt()
        else:
            basis = math.sqrt(n) * torch.linalg.qr(raw, mode="reduced")[0]
        bases.append(basis.contiguous())
    return bases


@torch.no_grad()
def closure(initial, order, method):
    b1, b2 = dictionaries(initial, order, method)
    D = b2.T @ (initial.M @ b1) / len(initial.w)
    engine = ClosureEngine(b1, initial.w, b2, D, device=initial.w.device,
                           dtype=torch.float64, block_size=256)
    state = engine.state(initial.w, initial.c, D)
    return engine, state


def blend(a, b, fraction):
    return TensorState(*(getattr(a, k) + fraction * (getattr(b, k) - getattr(a, k))
                         for k in ("w", "c", "M")))


def save_json(path, data):
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")


def source_hashes():
    files = list(Path(__file__).parent.glob("*.py")) + [Path(__file__).parent / "README.md"]
    for module in list(sys.modules.values()):
        name = getattr(module, "__file__", None)
        if name and str(ROOT / "code" / "pde") in name and name.endswith(".py"):
            files.append(Path(name))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(set(files))}


@torch.no_grad()
def run_trajectory(engine, state, angles_deg, labels, directory, step, suite_start):
    directory.mkdir()
    device = state.w.device
    angles = torch.tensor(angles_deg, dtype=torch.float64, device=device) * (math.pi / 180)
    inputs = torch.stack((angles.cos(), angles.sin()), dim=1)
    data = engine.prepare_data(inputs, labels)
    grid_angles, grid = circle(2048, device)
    endpoint_angles, endpoint_grid = circle(8192, device)
    records, predictions, times, losses, saved_states = [], [], [], [], []
    start = time.monotonic()
    t = 0.0
    status = "time_cap"
    loss = float(engine.loss(state, data))
    times.append(t)
    losses.append(loss)

    def snapshot():
        records.append(t)
        predictions.append(engine.predict(state, grid).cpu().numpy())
        saved_states.append(state.numpy())

    snapshot()
    next_snapshot = 1
    try:
        while t < MAX_TIME - 1e-10 and loss > THRESHOLD:
            if time.monotonic() - start > 180 or time.monotonic() - suite_start > 900:
                status = "wall_cap"
                break
            h = min(step, MAX_TIME - t)
            if next_snapshot < len(SNAPSHOTS):
                h = min(h, SNAPSHOTS[next_snapshot] - t)
            candidate = engine.heun_step(state, data, h)
            candidate_loss = float(engine.loss(candidate, data))
            if candidate_loss <= THRESHOLD:
                lo, hi = 0.0, 1.0
                for _ in range(30):
                    mid = (lo + hi) / 2
                    if float(engine.loss(blend(state, candidate, mid), data)) <= THRESHOLD:
                        hi = mid
                    else:
                        lo = mid
                state = blend(state, candidate, hi)
                t += h * hi
                loss = float(engine.loss(state, data))
                status = "fitted"
            else:
                state, loss = candidate, candidate_loss
                t += h
            times.append(t)
            losses.append(loss)
            if next_snapshot < len(SNAPSHOTS) and t >= SNAPSHOTS[next_snapshot] - 1e-10:
                snapshot()
                next_snapshot += 1
        if abs(records[-1] - t) > 1e-12:
            snapshot()
    except (ValueError, RuntimeError) as exc:
        status = "numerical_failure"
        save_json(directory / "exception.json", {"type": type(exc).__name__, "message": str(exc)})
        if abs(records[-1] - t) > 1e-12:
            snapshot()

    final_prediction = engine.predict(state, endpoint_grid)
    obs = engine.observations(state, inputs, **({"include_grams": False} if isinstance(engine, ClosureEngine) else {}))
    arrays = {
        "circle_angles": grid_angles.cpu().numpy(), "circle_inputs": grid.cpu().numpy(),
        "snapshot_times": np.asarray(records), "circle_predictions": np.asarray(predictions),
        "times": np.asarray(times), "losses": np.asarray(losses),
        "endpoint_angles": endpoint_angles.cpu().numpy(), "endpoint_inputs": endpoint_grid.cpu().numpy(),
        "endpoint_prediction": final_prediction.cpu().numpy(),
        "training_inputs": inputs.cpu().numpy(), "labels": np.asarray(labels),
    }
    arrays.update({k: np.stack([s[k] for s in saved_states]) for k in ("w", "c", "M")})
    if isinstance(engine, ClosureEngine):
        arrays.update({k: getattr(engine, k).cpu().numpy() for k in ("b1", "b2", "g", "D", "p1", "p2")})
        eigenvalues = [torch.linalg.eigvalsh(b.T @ b / len(b)).cpu().tolist() for b in (engine.b1, engine.b2)]
    else:
        eigenvalues = None
    np.savez(directory / "arrays.npz", **arrays)
    summary = {
        "status": status, "time": t, "loss": loss, "initial_loss": losses[0],
        "steps": len(times) - 1, "step_size": step, "seconds": time.monotonic() - start,
        "rms_hidden1": float(obs["rms1"]), "rms_hidden2": float(obs["rms2"]),
        "gram_eigenvalues": eigenvalues, "retained_bytes": engine.retained_bytes(state),
        "loss_increases_above_1e-10": int(np.sum(np.diff(losses) > 1e-10)),
    }
    save_json(directory / "summary.json", summary)
    print(directory.name, json.dumps({k: summary[k] for k in ("status", "time", "loss", "seconds")}), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--step", type=float, default=0.05)
    parser.add_argument("--device", default="cuda:1")
    parser.add_argument("--only", nargs="*", help="Declared refinement cells, e.g. four_ours_p1")
    args = parser.parse_args()
    device = setup(args.device)
    args.out.mkdir(parents=True, exist_ok=False)
    config = {
        "cases": CASES, "width": N, "network_seed": NETWORK_SEED, "dictionary_seed": DICTIONARY_SEED,
        "orders": [1, 3], "threshold": THRESHOLD, "max_time": MAX_TIME,
        "step": args.step, "snapshot_times": SNAPSHOTS, "circle_nodes": 2048, "endpoint_nodes": 8192,
        "torch": torch.__version__, "numpy": np.__version__, "python": sys.version,
        "device": device, "gpu": torch.cuda.get_device_name(device), "dtype": "float64",
        "source_hashes": source_hashes(), "command": sys.argv, "cwd": str(Path.cwd()),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    save_json(args.out / "config.json", config)
    suite_start = time.monotonic()
    results = {}
    for case, (angles, labels) in CASES.items():
        net = NetworkEngine(2, N, NETWORK_SEED, device=device, dtype=torch.float64, block_size=256)
        initial = net.initial_state()
        variants = [("full", None)] + [(f"{method}_p{p}", (p, method)) for p in (1, 3)
                                      for method in ("ours", "gaussian", "orthogonal")]
        for name, spec in variants:
            key = case + "_" + name
            if args.only and key not in args.only:
                continue
            engine, state = (net, initial.clone()) if spec is None else closure(initial, *spec)
            results[key] = run_trajectory(engine, state, angles, labels, args.out / key, args.step, suite_start)
            save_json(args.out / "results.json", results)
            if time.monotonic() - suite_start > 900:
                raise RuntimeError("Suite wall budget exhausted; completed/partial results retained")
    save_json(args.out / "completion.json", {"exit_status": 0, "seconds": time.monotonic() - suite_start,
                                           "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})


if __name__ == "__main__":
    main()
