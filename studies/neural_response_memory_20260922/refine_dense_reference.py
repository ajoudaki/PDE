"""Refine selected finite dense GF targets; never overwrite an existing cell.

Each arrays.npz stores FINAL w(n,2), c(n), M(n,n), without a snapshot axis.
Only predictions carry a snapshot axis. Original eight training samples are
preserved, including all antipodal pairs in equal_mixed_odd. Controller scales
match the archived diverse_benchmark.py; threshold localization uses 32 rather
than 30 chord bisections. The CLI runs CUDA float64 only.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.finite_torch import NetworkEngine
from pde.observable_torch_p1 import TensorState

# Literal selected references, frozen from run_moment_experiment.py.
REFERENCES = {
    "two_outliers_alternating": "scaling_discovery_refined01/two_outliers_alternating_full",
    "quadrant_alternating": "diverse_fine_early01/quadrant_alternating_full",
    "quadrant_pairs": "scaling_discovery_refined01/quadrant_pairs_full",
    "quadrant_center_edges": "diverse_refined01/quadrant_center_edges_full",
    "equal_mixed_odd": "diverse_refined01/equal_mixed_odd_full",
}
THRESHOLD, WIDTH, SEED = 1e-3, 2048, 20260920


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def array_hash(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def save_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def source_hashes():
    paths = {Path(__file__).resolve()}
    for module in tuple(sys.modules.values()):
        filename = getattr(module, "__file__", None)
        if filename:
            p = Path(filename).resolve()
            if p.suffix == ".py" and ROOT / "code" in p.parents:
                paths.add(p)
    for rel in (
        "studies/neural_response_memory_20260922/run_moment_experiment.py",
        "studies/random_dictionary_learned_circle_20260920/diverse_benchmark.py",
    ):
        paths.add(ROOT / rel)
    return {str(p.relative_to(ROOT)): sha256(p) for p in sorted(paths)}


def blend(a, b, fraction):
    return TensorState(*(getattr(a, k) + fraction * (getattr(b, k) - getattr(a, k))
                         for k in ("w", "c", "M")))


@torch.no_grad()
def heun_trial(engine, state, data, step, initial_M, rtol, atol):
    first = engine.rhs(state, data)
    euler = TensorState(*(getattr(state, k) + step * getattr(first, k)
                          for k in ("w", "c", "M")))
    second = engine.rhs(euler, data)
    candidate = TensorState(*(
        getattr(state, k) + .5 * step * (getattr(first, k) + getattr(second, k))
        for k in ("w", "c", "M")))
    engine.validate_state(candidate)
    ratios = []
    for name in ("w", "c"):
        a, b, c = (getattr(s, name) for s in (state, euler, candidate))
        scale = atol + rtol * torch.maximum(a.square().mean().sqrt(),
                                            c.square().mean().sqrt())
        ratios.append((c - b).square().mean().sqrt() / scale)
    scale = atol + rtol * torch.maximum((state.M - initial_M).norm(),
                                        (candidate.M - initial_M).norm()).clamp_min(1)
    ratios.append((candidate.M - euler.M).norm() / scale)
    return candidate, float(torch.stack(ratios).max())


@torch.no_grad()
def integrate(engine, initial, data, panel, snapshot_panel, requested_times,
              rtol, atol, *, run_seconds=240., max_steps=30000, max_time=10000.):
    """Return last accepted state and diagnostics, including capped attempts."""
    state = initial.clone()
    current_loss = float(engine.loss(state, data))
    times, losses, steps, errors = [0.], [current_loss], [], []
    snapshot_times = [0.]
    snapshots = [engine.predict(state, snapshot_panel).cpu().numpy()]
    schedule = sorted(set(float(x) for x in requested_times if 0 < x <= max_time))
    next_snapshot = 0
    t, step, rejected = 0., .05, 0
    start = last_report = time.monotonic()
    status, exception = "time_cap", None
    try:
        while current_loss > THRESHOLD:
            if time.monotonic() - start >= run_seconds:
                status = "wall_cap"
                break
            if len(steps) >= max_steps:
                status = "step_cap"
                break
            if t >= max_time - 1e-9:
                status = "time_cap"
                break
            if time.monotonic() - last_report >= 20:
                print(json.dumps(dict(event="progress", time=t, loss=current_loss,
                                      steps=len(steps), wall_seconds=time.monotonic()-start)),
                      flush=True)
                last_report = time.monotonic()
            proposed = min(step, 2., max_time - t)
            if next_snapshot < len(schedule):
                proposed = min(proposed, schedule[next_snapshot] - t)
            if proposed <= 0:
                raise RuntimeError("nonpositive proposed step")
            try:
                candidate, error = heun_trial(engine, state, data, proposed,
                                              initial.M, rtol, atol)
                candidate_loss = float(engine.loss(candidate, data))
                if not math.isfinite(error) or not math.isfinite(candidate_loss):
                    raise ValueError("nonfinite trial error or loss")
            except (ValueError, RuntimeError):
                rejected += 1
                step = proposed * .25
                if step < 1e-7:
                    raise
                continue
            decreasing = candidate_loss <= current_loss * (1 + 1e-8) + 1e-12
            if error > 1 or not decreasing:
                rejected += 1
                step = proposed * max(.1, min(.5, .9 / math.sqrt(max(error, 1e-16))))
                if step < 1e-7:
                    raise RuntimeError("adaptive step below 1e-7")
                continue
            used_step = proposed
            if candidate_loss <= THRESHOLD:
                low, high = 0., 1.
                for _ in range(32):
                    middle = .5 * (low + high)
                    if float(engine.loss(blend(state, candidate, middle), data)) <= THRESHOLD:
                        high = middle
                    else:
                        low = middle
                candidate = blend(state, candidate, high)
                used_step = proposed * high
                candidate_loss = float(engine.loss(candidate, data))
            state, current_loss = candidate, candidate_loss
            t += used_step
            times.append(t)
            losses.append(current_loss)
            steps.append(used_step)
            errors.append(error)
            if next_snapshot < len(schedule) and t >= schedule[next_snapshot] - 1e-9:
                snapshot_times.append(t)
                snapshots.append(engine.predict(state, snapshot_panel).cpu().numpy())
                next_snapshot += 1
            step = proposed * min(2., max(.5, .9 / math.sqrt(max(error, 1e-16))))
        if current_loss <= THRESHOLD:
            status = "fitted"
    except (ValueError, RuntimeError) as exc:
        status = "numerical_failure"
        exception = {"type": type(exc).__name__, "message": str(exc)}
    integration_seconds = time.monotonic() - start
    if abs(snapshot_times[-1] - t) > 1e-12:
        snapshot_times.append(t)
        snapshots.append(engine.predict(state, snapshot_panel).cpu().numpy())
    arrays = dict(times=np.asarray(times), losses=np.asarray(losses),
                  accepted_steps=np.asarray(steps), local_error_ratios=np.asarray(errors),
                  snapshot_times=np.asarray(snapshot_times), circle_predictions=np.asarray(snapshots),
                  endpoint_prediction=engine.predict(state, panel).cpu().numpy(),
                  w=state.w.cpu().numpy(), c=state.c.cpu().numpy(), M=state.M.cpu().numpy())
    summary = dict(status=status, physical_fit_status=status, time=t, loss=current_loss,
                   initial_loss=losses[0], steps=len(steps), rejected_steps=rejected,
                   integration_seconds=integration_seconds, exception=exception,
                   loss_increases_above_1e_10=int(np.count_nonzero(np.diff(losses) > 1e-10)))
    return arrays, summary


@torch.no_grad()
def run_cell(case, level, out, device):
    started = time.monotonic()
    directory = Path(out) / f"{case}_full_level{level}"
    directory.mkdir(parents=True, exist_ok=False)
    archive_path = (ROOT / "data/generated/random_dictionary_learned_circle_20260920"
                    / REFERENCES[case] / "arrays.npz")
    engine = NetworkEngine(2, WIDTH, SEED, device=device, dtype=torch.float64, block_size=256)
    initial = engine.initial_state()
    with np.load(archive_path) as archive:
        initial_match, initial_hashes = {}, {}
        for name in ("w", "c", "M"):
            archived = archive[name][0]
            current = getattr(initial, name).cpu().numpy()
            initial_match[name] = np.array_equal(current, archived)
            initial_hashes[name] = array_hash(archived)
            del archived
        if not all(initial_match.values()):
            raise RuntimeError("canonical initialization differs from selected archive")
        retained = {k: archive[k].copy() for k in
                    ("training_inputs", "labels", "endpoint_angles", "endpoint_inputs",
                     "circle_angles", "circle_inputs")}
        reference_times = archive["snapshot_times"].copy()
    if retained["training_inputs"].shape != (8, 2) or retained["labels"].shape != (8,):
        raise ValueError("dense reference requires the original eight training samples")
    if retained["endpoint_inputs"].shape != (8192, 2):
        raise ValueError("archived endpoint grid must have 8192 nodes")
    rtol = 6.25e-5 / 4 ** level
    atol = rtol / 100
    config = dict(case=case, level=level, width=WIDTH, input_dimension=2, network_seed=SEED,
                  dtype="float64", device=str(device), gpu=torch.cuda.get_device_name(device),
                  rtol=rtol, atol=atol, threshold=THRESHOLD, initial_step=.05,
                  max_step=2., min_step=1e-7, max_time=10000., max_steps=30000,
                  per_trajectory_limit_seconds=240., crossing_bisections=32,
                  training_sample_count=8, loss="unhalved mean squared error",
                  physical_mobilities=[WIDTH, 1, WIDTH], initial_match=initial_match,
                  initial_array_sha256=initial_hashes, reference=str(archive_path.relative_to(ROOT)),
                  reference_sha256=sha256(archive_path), source_hashes=source_hashes(),
                  command=sys.argv, cwd=str(Path.cwd()), python=sys.version,
                  numpy=np.__version__, torch=str(torch.__version__),
                  final_state_layout={"w": [WIDTH, 2], "c": [WIDTH], "M": [WIDTH, WIDTH]},
                  state_arrays_have_snapshot_axis=False,
                  started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    save_json(directory / "config.json", config)
    data = engine.prepare_data(retained["training_inputs"], retained["labels"])
    arrays, summary = integrate(engine, initial, data, retained["endpoint_inputs"],
                                retained["circle_inputs"], reference_times, rtol, atol)
    arrays.update(retained)
    arrays["reference_snapshot_times"] = reference_times
    np.savez(directory / "arrays.npz", **arrays)
    torch.cuda.synchronize(device)
    summary.update(case=case, level=level, rtol=rtol, atol=atol, initial_match=initial_match,
                   source_hashes=config["source_hashes"], reference=config["reference"],
                   final_state_layout=config["final_state_layout"],
                   state_arrays_have_snapshot_axis=False, seconds=time.monotonic()-started,
                   wall_seconds=time.monotonic()-started,
                   arrays_sha256=sha256(directory / "arrays.npz"))
    # Accounting includes output serialization and hashing.
    summary["seconds"] = summary["wall_seconds"] = time.monotonic() - started
    save_json(directory / "summary.json", summary)
    print(json.dumps(dict(event="completed", directory=str(directory), **summary)), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", nargs="+", choices=tuple(REFERENCES), required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--levels", nargs="+", type=int, choices=(0, 1, 2, 3), default=[1, 2])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if len(set(args.cases)) != len(args.cases) or len(set(args.levels)) != len(args.levels):
        parser.error("duplicate case or level")
    if not args.device.startswith("cuda:") or not torch.cuda.is_available():
        parser.error("CUDA device required for benchmark runs")
    targets = [args.out / f"{case}_full_level{level}"
               for case in args.cases for level in args.levels]
    if any(p.exists() for p in targets):
        parser.error("an output cell already exists; select fresh output paths")
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.set_float32_matmul_precision("highest")
    torch.cuda.set_device(args.device)
    results = []
    for case in args.cases:
        for level in args.levels:
            results.append(run_cell(case, level, args.out, args.device))
    return 0 if all(r["status"] == "fitted" for r in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
