"""Two-worker continuation of the fixed-dictionary circle experiment."""
import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time

from benchmark import (ROOT, NetworkEngine, ClosureEngine, TensorState, setup,
                       circle, blend, save_json, source_hashes, np, torch)
from diverse_cases import CASES_V2, validate_cases
from diverse_dictionary import build

WIDTH, NETWORK_SEED, DICTIONARY_SEED = 2048, 20260920, 7319
THRESHOLD, MAX_TIME, MAX_STEPS = 1e-3, 10000., 30000
SNAPSHOTS = [0, 1, 2, 5, 10, 20, 40, 80, 160, 300, 600, 1200, 2500, 5000, 10000]
METHODS = ["full"] + [f"{method}_p{p}" for p in (1, 3, 5)
                      for method in ("ours", "gaussian", "orthogonal")]


@torch.no_grad()
def heun_trial(engine, state, data, h, initial_M, rtol, atol):
    """Same simultaneous Heun update, with embedded Euler error controller.

    Row/readout errors use RMS. Middle errors use Frobenius norm, scaled by
    the trained increment rather than the possibly large initial Gaussian bulk.
    This is a numerical controller, not an a posteriori exact-flow certificate.
    """
    k = engine.rhs(state, data)
    euler = TensorState(*(getattr(state, a) + h*getattr(k, a) for a in ("w", "c", "M")))
    ell = engine.rhs(euler, data)
    candidate = TensorState(*(getattr(state, a) + .5*h*(getattr(k, a)+getattr(ell, a))
                              for a in ("w", "c", "M")))
    engine.validate_state(candidate)
    ratios = []
    for name in ("w", "c"):
        x, y, z = (getattr(s, name) for s in (state, euler, candidate))
        scale = atol + rtol*torch.maximum(x.square().mean().sqrt(), z.square().mean().sqrt())
        ratios.append((z-y).square().mean().sqrt()/scale)
    middle_scale = atol + rtol*torch.maximum((state.M-initial_M).norm(), (candidate.M-initial_M).norm()).clamp_min(1)
    ratios.append((candidate.M-euler.M).norm()/middle_scale)
    return candidate, float(torch.stack(ratios).max())


@torch.no_grad()
def trajectory(engine, initial, case, directory, rtol, atol, worker_start, worker_limit):
    directory.mkdir()
    device = initial.w.device
    angles = torch.tensor(case["angles_degrees"], device=device, dtype=torch.float64)*(math.pi/180)
    inputs = torch.stack((angles.cos(), angles.sin()), 1)
    data = engine.prepare_data(inputs, case["labels"])
    grid_angles, grid = circle(2048, device)
    end_angles, end_grid = circle(8192, device)
    state = initial.clone()
    records, outputs, saved_states = [], [], []
    times, losses, accepted_steps, errors = [0.], [float(engine.loss(state, data))], [], []
    t, h, rejected = 0., .05, 0
    status = "fitted" if losses[0] <= THRESHOLD else "time_cap"
    start = time.monotonic()
    next_progress = start + 30
    next_snapshot = 1

    def snapshot():
        records.append(t)
        outputs.append(engine.predict(state, grid).cpu().numpy())
        saved_states.append(state.numpy())

    snapshot()
    try:
        while t < MAX_TIME-1e-9 and losses[-1] > THRESHOLD:
            elapsed = time.monotonic()-start
            if elapsed > 180 or time.monotonic()-worker_start > worker_limit:
                status = "wall_cap"
                break
            if len(accepted_steps) >= MAX_STEPS:
                status = "step_cap"
                break
            if time.monotonic() >= next_progress:
                print(json.dumps(dict(progress=directory.name, t=t, loss=losses[-1], seconds=elapsed,
                                      steps=len(accepted_steps), rejected=rejected)), flush=True)
                next_progress = time.monotonic()+30
            h = min(h, 2., MAX_TIME-t, SNAPSHOTS[next_snapshot]-t)
            try:
                candidate, error = heun_trial(engine, state, data, h, initial.M, rtol, atol)
                candidate_loss = float(engine.loss(candidate, data))
            except (ValueError, RuntimeError):
                rejected += 1
                h *= .25
                if h < 1e-7:
                    raise
                continue
            decreasing = candidate_loss <= losses[-1]*(1+1e-8)+1e-12
            if error > 1 or not decreasing:
                rejected += 1
                h *= max(.1, min(.5, .9/math.sqrt(max(error, 1e-16))))
                if h < 1e-7:
                    raise RuntimeError("Adaptive step fell below the declared minimum")
                continue
            used_h = h
            if candidate_loss <= THRESHOLD:
                lo, hi = 0., 1.
                for _ in range(30):
                    mid = .5*(lo+hi)
                    if float(engine.loss(blend(state, candidate, mid), data)) <= THRESHOLD:
                        hi = mid
                    else:
                        lo = mid
                state = blend(state, candidate, hi)
                used_h = h*hi
                candidate_loss = float(engine.loss(state, data))
                status = "fitted"
            else:
                state = candidate
            t += used_h
            times.append(t)
            losses.append(candidate_loss)
            accepted_steps.append(used_h)
            errors.append(error)
            if t >= SNAPSHOTS[next_snapshot]-1e-9:
                snapshot()
                next_snapshot += 1
            h *= min(2., max(.5, .9/math.sqrt(max(error, 1e-16))))
        if abs(records[-1]-t) > 1e-12:
            snapshot()
    except (RuntimeError, ValueError) as exc:
        status = "numerical_failure"
        save_json(directory / "exception.json", dict(type=type(exc).__name__, message=str(exc)))
        if abs(records[-1]-t) > 1e-12:
            snapshot()

    final = engine.predict(state, end_grid)
    obs = engine.observations(state, inputs, **({"include_grams": False} if isinstance(engine, ClosureEngine) else {}))
    arrays = dict(circle_angles=grid_angles.cpu().numpy(), circle_inputs=grid.cpu().numpy(),
                  snapshot_times=np.asarray(records), circle_predictions=np.asarray(outputs),
                  times=np.asarray(times), losses=np.asarray(losses),
                  accepted_steps=np.asarray(accepted_steps), local_error_ratios=np.asarray(errors),
                  endpoint_angles=end_angles.cpu().numpy(), endpoint_inputs=end_grid.cpu().numpy(),
                  endpoint_prediction=final.cpu().numpy(), training_inputs=inputs.cpu().numpy(),
                  labels=np.asarray(case["labels"]))
    arrays.update({k: np.stack([s[k] for s in saved_states]) for k in ("w", "c", "M")})
    gram_eigenvalues = None
    if isinstance(engine, ClosureEngine):
        arrays.update({k: getattr(engine, k).cpu().numpy() for k in ("b1", "b2", "g", "D", "p1", "p2")})
        gram_eigenvalues = [torch.linalg.eigvalsh(b.T@b/len(b)).cpu().tolist() for b in (engine.b1, engine.b2)]
    np.savez(directory / "arrays.npz", **arrays)
    result = dict(status=status, time=t, loss=losses[-1], initial_loss=losses[0],
                  seconds=time.monotonic()-start, steps=len(accepted_steps), rejected_steps=rejected,
                  rtol=rtol, atol=atol, step_size=None,
                  max_step=max(accepted_steps, default=0), min_step=min(accepted_steps, default=0),
                  rms_hidden1=float(obs["rms1"]), rms_hidden2=float(obs["rms2"]),
                  gram_eigenvalues=gram_eigenvalues, retained_bytes=engine.retained_bytes(state),
                  peak_cuda_allocated=torch.cuda.max_memory_allocated(device))
    result["loss_increases_above_1e-10"] = int(np.sum(np.diff(losses)>1e-10))
    save_json(directory / "summary.json", result)
    print(json.dumps(dict(completed=directory.name, **{k: result[k] for k in
                      ("status", "time", "loss", "seconds", "steps", "rejected_steps")})), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--worker", type=int, choices=(0, 1), required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--refined", action="store_true")
    args = parser.parse_args()
    validate_cases()
    device = setup(args.device)
    rtol, atol = ((2.5e-4, 2.5e-6) if args.refined else (1e-3, 1e-5))
    worker_limit = 1800 if args.refined else 1200
    args.out.mkdir(parents=True, exist_ok=True)
    config_path = args.out / f"config_worker{args.worker}.json"
    if config_path.exists():
        raise FileExistsError(config_path)
    config = dict(cases=CASES_V2, width=WIDTH, network_seed=NETWORK_SEED, dictionary_seed=DICTIONARY_SEED,
                  threshold=THRESHOLD, orders=[1,3,5], dtype="float64", step=.05, max_step=2.,
                  rtol=rtol, atol=atol, max_time=MAX_TIME, max_steps=MAX_STEPS,
                  worker_limit_seconds=worker_limit, per_trajectory_limit_seconds=180,
                  snapshot_times=SNAPSHOTS, endpoint_nodes=8192, circle_nodes=2048,
                  worker=args.worker, device=device, gpu=torch.cuda.get_device_name(device),
                  torch=str(torch.__version__), numpy=np.__version__, python=sys.version,
                  source_hashes=source_hashes(), command=sys.argv, cwd=str(Path.cwd()),
                  head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                  started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    save_json(config_path, config)
    start = time.monotonic()
    net = NetworkEngine(2, WIDTH, NETWORK_SEED, device=device, dtype=torch.float64, block_size=256)
    initial = net.initial_state()
    engines = {"full": (net, initial)}
    for p in (1,3,5):
        for method in ("ours", "gaussian", "orthogonal"):
            engines[f"{method}_p{p}"] = build(initial, p, method)
    results = {}
    for index, (name, case) in enumerate(CASES_V2.items()):
        if index % 2 != args.worker:
            continue
        for method in METHODS:
            key = name + "_" + method
            engine, state = engines[method]
            results[key] = trajectory(engine, state, case, args.out/key, rtol, atol, start, worker_limit)
            save_json(args.out / f"results_worker{args.worker}.json", results)
        # Even after a time cap, preserve each remaining cell's initialized
        # checkpoint and explicit wall_cap status, rather than omitting it.
    save_json(args.out / f"completion_worker{args.worker}.json",
              dict(exit_status=0, seconds=time.monotonic()-start,
                   fitted=sum(v["status"] == "fitted" for v in results.values()),
                   total=len(results), finished_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))


if __name__ == "__main__":
    main()
