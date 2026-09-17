"""Study-owned, dense finite-network GPU comparison. See the frozen plan."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, allow_nan=False) + "\n")


def setup(dtype):
    torch.set_num_threads(4)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction = False
    torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction = False
    torch.cuda.set_device(0)
    torch.cuda.set_per_process_memory_fraction(0.75, 0)
    return torch.float64 if dtype == "float64" else torch.float32


def initialize(n, seed, dtype, device="cuda"):
    rng = np.random.default_rng(seed)
    blocks = []
    hashes = []
    for shape, scale in [((n, 2), 1.0), ((n, n), n ** -0.5), ((n,), 1.0/n)]:
        array = rng.normal(size=shape) * scale
        hashes.append(hashlib.sha256(array.tobytes()).hexdigest())
        blocks.append(torch.tensor(array, dtype=dtype, device=device))
    return tuple(blocks), hashes


def fields(state, u):
    w, b, c = state
    z1 = w @ u
    h1 = torch.tanh(z1)
    z2 = b @ h1
    h2 = torch.tanh(z2)
    f = c @ h2 / c.numel()
    return z1, h1, z2, h2, f


def derivative(z):
    e = torch.exp(-torch.abs(z))
    return (2*e / (1+e*e)).square()


def rhs(state, u, y, p):
    w, b, c = state
    z1, h1, z2, h2, f = fields(state, u)
    residual = p * (f-y)
    d2 = c[:, None] * derivative(z2)
    d1 = derivative(z1) * (b.T @ d2)
    return (-2 * ((d1 * residual) @ u.T),
            (-2/c.numel()) * ((d2 * residual) @ h1.T),
            -2 * (h2 @ residual))


def heun(state, u, y, p, step):
    first = rhs(state, u, y, p)
    stage = tuple(a + step*k for a, k in zip(state, first))
    second = rhs(stage, u, y, p)
    # Out of place preserves the previous endpoint for observation interpolation.
    return tuple(a + (step/2)*(k+l) for a, k, l in zip(state, first, second))


def observe(state, u, y, p, circle, initial):
    _, h1, _, h2, f = fields(state, u)
    hs = (h1, h2)
    moments = torch.stack([(h.square().mean(dim=0)*p).sum() for h in hs])
    initial_moments = torch.stack([(h.square().mean(dim=0)*p).sum() for h in initial])
    crosses = torch.stack([((h*a).mean(dim=0)*p).sum() for h, a in zip(hs, initial)])
    motions = torch.stack([((h-a).square().mean(dim=0)*p).sum().sqrt()
                           for h, a in zip(hs, initial)])
    obs = dict(loss=((f-y).square()*p).sum(),
               mean_prediction=(f*p).sum(), raw_rms=moments.sqrt(), motion_rms=motions,
               second_moments=moments, initial_second_moments=initial_moments,
               cross_moments=crosses, predictions=fields(state, circle)[-1],
               data_predictions=f)
    return {key: value.detach().cpu().double().numpy() for key, value in obs.items()}


def verification():
    sys.path.insert(0, str(ROOT / "code"))
    from pde.finite_network import Parameters, flow_velocity
    rng = np.random.default_rng(917)
    n = 7
    u_np = rng.normal(size=(2, 4)) * .7
    y_np = rng.normal(size=4)
    p_np = np.array([.1, .2, .3, .4])
    blocks = (rng.normal(size=(n, 2))*.6,
              rng.normal(size=(n, n))*.4, rng.normal(size=n)*.8)
    ref = flow_velocity(Parameters(blocks[:2], blocks[2]),
                        np.repeat(u_np*np.sqrt(2), [1, 2, 3, 4], axis=1),
                        np.repeat(y_np, [1, 2, 3, 4]))
    reference = ref.weights + (ref.readout,)
    checks = []
    for device in ["cpu", "cuda"]:
        for dtype, tolerance in [(torch.float64, 1e-10), (torch.float32, 2e-5)]:
            state = tuple(torch.tensor(a, dtype=dtype, device=device, requires_grad=True)
                          for a in blocks)
            u, y, p = [torch.tensor(a, dtype=dtype, device=device)
                       for a in [u_np, y_np, p_np]]
            f = fields(state, u)[-1]
            loss = ((f-y).square()*p).sum()
            grads = torch.autograd.grad(loss, state)
            expected = tuple(-m*g for m, g in zip((n, 1, n), grads))
            actual = rhs(state, u, y, p)
            errors = []
            for got, auto, numpy_ref in zip(actual, expected, reference):
                got_np = got.detach().cpu().double().numpy()
                np.testing.assert_allclose(got_np, numpy_ref, rtol=tolerance, atol=tolerance*1e-2)
                torch.testing.assert_close(got, auto, rtol=tolerance, atol=tolerance*1e-2)
                errors.append(float(np.linalg.norm(got_np-numpy_ref)/max(np.linalg.norm(numpy_ref), 1e-30)))
            energy = sum((g*v).sum() for g, v in zip(grads, actual))
            metric = -sum(v.square().sum()/m for v, m in zip(actual, (n, 1, n)))
            torch.testing.assert_close(energy, metric, rtol=tolerance, atol=tolerance*1e-2)
            with torch.no_grad():
                initial = (fields(state, u)[1].clone(), fields(state, u)[3].clone())
                observation = observe(state, u, y, p, u, initial)
                np.testing.assert_array_equal(observation["motion_rms"], np.zeros(2))
                next_state = heun(state, u, y, p, .01)
                observation = observe(next_state, u, y, p, u, initial)
                np.testing.assert_allclose(observation["motion_rms"]**2,
                    observation["second_moments"]+observation["initial_second_moments"]-2*observation["cross_moments"],
                    atol=tolerance, rtol=tolerance)
            checks.append(dict(device=device, dtype=str(dtype), rhs_relative_errors=errors,
                               weighted_autograd=True, weighted_numpy=True, energy=True, moments=True))
    a, hashes_a = initialize(23, 11, torch.float32)
    b, hashes_b = initialize(23, 11, torch.float64)
    assert hashes_a == hashes_b
    for x, y in zip(a, b):
        torch.testing.assert_close(x, y.float(), rtol=0, atol=0)
    return dict(status="passed", checks=checks, matching_initializations=True)


def load_inputs(base, case, dtype):
    with np.load(base / "inputs.npz") as data:
        times = data["times"].copy()
        u = torch.tensor(data[case+"_inputs"].T, dtype=dtype, device="cuda")
        y = torch.tensor(data[case+"_labels"], dtype=dtype, device="cuda")
        p = torch.tensor(data[case+"_probabilities"], dtype=dtype, device="cuda")
        circle = torch.tensor(data["circle"].T, dtype=dtype, device="cuda")
    return times, u, y, p, circle


@torch.no_grad()
def calibrate(base):
    dtype = setup("float32")
    _, u, y, p, _ = load_inputs(base, "arcs", dtype)
    state, _ = initialize(8192, 11, dtype)
    for _ in range(2):
        state = heun(state, u, y, p, .01)
    torch.cuda.synchronize()
    start = time.monotonic()
    for _ in range(30):
        state = heun(state, u, y, p, .01)
    torch.cuda.synchronize()
    seconds = time.monotonic()-start
    projection = seconds/30*4000
    # Benchmark excludes scientific observations and initialization, reserve 15%.
    projection *= 1.15
    result = dict(width=8192, measured_steps=30, warmup_steps=2,
                  seconds=seconds, projected_seconds_with_15_percent_overhead=projection,
                  selected_large_width=4096 if projection > 300 else 8192,
                  peak_allocated_bytes=torch.cuda.max_memory_allocated())
    write_json(base / "calibration.json", result)
    print(json.dumps(result), flush=True)
    return result


@torch.no_grad()
def run(base, config):
    out = base / "network" / config["name"]
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    record = dict(config, status="running", source_sha256=digest(__file__),
                  inputs_sha256=digest(base/"inputs.npz"), torch_version=torch.__version__,
                  numpy_version=np.__version__, cuda_version=torch.version.cuda,
                  visible_device=os.environ.get("CUDA_VISIBLE_DEVICES"), command=sys.argv,
                  tf32=False, reduced_precision_accumulation=False)
    write_json(out/"record.json", record)
    rows = []
    increases = []
    times = np.empty(0)
    try:
        dtype = setup(config["dtype"])
        record["gpu"] = torch.cuda.get_device_name()
        times, u, y, p, circle = load_inputs(base, config["case"], dtype)
        state, hashes = initialize(config["width"], config["seed"], dtype)
        record["initial_float64_block_hashes"] = hashes
        record["trainable_parameters"] = sum(a.numel() for a in state)
        fs = fields(state, u)
        initial = (fs[1].clone(), fs[3].clone())
        del fs
        rows = [observe(state, u, y, p, circle, initial)]
        index = 1
        h = config["step"]
        steps = round(40/h)
        previous_loss = float(rows[0]["loss"])
        for k in range(1, steps+1):
            old = state
            state = heun(old, u, y, p, h)
            while index < len(times) and times[index] <= k*h+1e-10:
                fraction = (times[index]-(k-1)*h)/h
                observed = state if fraction >= 1-1e-9 else tuple(
                    a + fraction*(b-a) for a, b in zip(old, state))
                row = observe(observed, u, y, p, circle, initial)
                if not all(np.isfinite(value).all() for value in row.values()):
                    raise FloatingPointError(f"Nonfinite observation at {times[index]}")
                if float(row["loss"]) > previous_loss + 1e-6:
                    increases.append(dict(time=float(times[index]), previous=previous_loss, current=float(row["loss"])))
                previous_loss = float(row["loss"])
                rows.append(row)
                index += 1
            if k % 500 == 0:
                np.savez_compressed(out/"observations.npz", times=times[:len(rows)],
                                    **{key: np.stack([row[key] for row in rows]) for key in rows[0]})
                record.update(last_time=k*h, completed_observations=len(rows),
                              observed_loss_increases=increases, wall_seconds=time.monotonic()-started)
                write_json(out/"record.json", record)
                print(json.dumps(dict(name=config["name"], time=k*h, loss=previous_loss,
                                      wall_seconds=time.monotonic()-started)), flush=True)
                if time.monotonic()-started > 600:
                    raise TimeoutError("Predeclared per-trajectory wall cap")
        assert len(rows) == len(times)
        torch.cuda.synchronize()
        np.savez_compressed(out/"observations.npz", times=times,
                            **{key: np.stack([row[key] for row in rows]) for key in rows[0]})
        record.update(status="complete", final_loss=previous_loss, observed_loss_increases=increases,
                      peak_allocated_bytes=torch.cuda.max_memory_allocated(), steps=steps,
                      observations_sha256=digest(out/"observations.npz"))
    except Exception:
        record.update(status="failed", error=traceback.format_exc())
        raise
    finally:
        if rows:
            np.savez_compressed(out/"observations.npz", times=times[:len(rows)],
                                **{key: np.stack([row[key] for row in rows]) for key in rows[0]})
            record["observations_sha256"] = digest(out/"observations.npz")
        record["observed_loss_increases"] = increases
        record["completed_observations"] = len(rows)
        record["wall_seconds"] = time.monotonic()-started
        write_json(out/"record.json", record)


def campaign(base):
    setup("float64")
    verify = verification()
    write_json(base/"verification.json", verify)
    print("Finite RHS, weighted autodiff, energy and moment gates passed.", flush=True)
    start = time.monotonic()
    calibration = calibrate(base)
    large = calibration["selected_large_width"]
    configs = []
    for width in [2048, large]:
        for seed in [11, 29, 47]:
            for case in ["axis", "arcs"]:
                configs.append(dict(name=f"{case}_n{width}_s{seed}", case=case, width=width,
                                    seed=seed, step=.01, dtype="float32", kind="primary"))
    for case in ["axis", "arcs"]:
        configs.append(dict(name=f"{case}_n{large}_s11_halfstep", case=case, width=large,
                            seed=11, step=.005, dtype="float32", kind="time_control"))
        configs.append(dict(name=f"{case}_n2048_s11_float64", case=case, width=2048,
                            seed=11, step=.01, dtype="float64", kind="precision_control"))
    frozen = dict(configs=configs, calibration=calibration, frozen_before_full_trajectories=True,
                  source_sha256=digest(__file__), plan_sha256=digest(Path(__file__).with_name("WIDE_GPU_20260914_PLAN.md")),
                  git_head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                  git_status=subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True),
                  started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), command=sys.argv)
    write_json(base/"network_campaign.json", frozen)
    # Release calibration tensors before starting the two isolated workers.
    torch.cuda.empty_cache()
    active = {}
    pending = list(configs)
    finished = []
    worker_seconds = 0.0
    while pending or active:
        elapsed = time.monotonic()-start
        live_wall = sum(time.monotonic()-v[2] for v in active.values())
        budget_hit = elapsed > 2400 or worker_seconds+live_wall > 3600
        for gpu, (process, config, launch, log) in list(active.items()):
            exceeded = time.monotonic()-launch > 600
            if process.poll() is None and (budget_hit or exceeded):
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
            if process.poll() is not None:
                spent = time.monotonic()-launch
                record_path = base/"network"/config["name"]/"record.json"
                if process.returncode != 0:
                    record = json.loads(record_path.read_text()) if record_path.exists() else dict(config)
                    record.update(status="failed", worker_exit_code=process.returncode,
                                  supervisor_wall_seconds=spent, budget_stop=budget_hit or exceeded)
                    record_path.parent.mkdir(parents=True, exist_ok=True)
                    write_json(record_path, record)
                worker_seconds += spent
                item = dict(name=config["name"], exit_code=process.returncode, wall_seconds=spent,
                            budget_stop=budget_hit or exceeded, gpu=gpu)
                finished.append(item)
                log.close()
                del active[gpu]
                print(json.dumps(item), flush=True)
        if budget_hit:
            break
        for gpu in [1, 0]:
            if gpu not in active and pending:
                config = pending.pop(0)
                env = dict(os.environ, CUDA_VISIBLE_DEVICES=str(gpu), OPENBLAS_NUM_THREADS="1",
                           OMP_NUM_THREADS="4", MKL_NUM_THREADS="4", PYTHONDONTWRITEBYTECODE="1")
                log = (base/(config["name"]+".log")).open("w")
                command = [sys.executable, str(Path(__file__).resolve()), "--output", str(base),
                           "--worker", json.dumps(config)]
                process = subprocess.Popen(command, env=env, stdout=log, stderr=subprocess.STDOUT)
                active[gpu] = (process, config, time.monotonic(), log)
                print("Started " + config["name"] + " on GPU " + str(gpu), flush=True)
        time.sleep(1)
    result = dict(finished=finished, unstarted=[c["name"] for c in pending],
                  worker_wall_seconds=worker_seconds, wall_seconds=time.monotonic()-start)
    write_json(base/"network_campaign_result.json", result)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--campaign", action="store_true")
    parser.add_argument("--worker")
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    if args.worker:
        run(args.output, json.loads(args.worker))
    elif args.verify_only:
        setup("float64")
        print(json.dumps(verification()))
    elif args.campaign:
        campaign(args.output)
    else:
        parser.error("Choose --campaign, --worker or --verify-only")
