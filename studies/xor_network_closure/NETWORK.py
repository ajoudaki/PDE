#!/usr/bin/env python3
"""Predeclared shifted-XOR finite tanh network; independent study-local runner.

Training: NETWORK.py --output RUN_DIRECTORY --run-id MANIFEST_NAME --device cuda:0
Checks:   NETWORK.py --verify --output CHECK_DIRECTORY [--device cpu|cuda:0]

Inputs are unit directions (the maintained physical inputs are sqrt(2)*u).
Scalar hidden RMS quantities average the first 16 training points with their
declared weights; Grams, predictions and saved initial features use all 144 points.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import shlex
import shutil
import signal
import sys
import time
import traceback

sys.dont_write_bytecode = True
for _variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                  "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_variable] = "1"
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
os.environ["NVIDIA_TF32_OVERRIDE"] = "0"

import numpy as np
import torch

SOURCE = Path(__file__).resolve()
STUDY = SOURCE.parent
REPO = SOURCE.parents[2]
PLAN = STUDY / "EXPERIMENT_PLAN.md"
GIB = 1024 ** 3
ALLOWED_CONFIGS = {(n, seed, 0.01, "float32")
                   for n in (2048, 8192) for seed in (11, 29, 47)} | {
    (8192, 11, 0.005, "float32"), (2048, 11, 0.01, "float64")}


def now_utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def array_record(value):
    value = np.ascontiguousarray(value)
    return {"sha256": hashlib.sha256(memoryview(value).cast("B")).hexdigest(),
            "shape": list(value.shape), "dtype": value.dtype.str,
            "hash_encoding": "C-contiguous raw array bytes"}


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")
    temporary.replace(path)


def configure(device):
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.set_float32_matmul_precision("highest")
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    for name in ("allow_fp16_reduced_precision_reduction",
                 "allow_bf16_reduced_precision_reduction", "allow_fp16_accumulation"):
        if hasattr(torch.backends.cuda.matmul, name):
            setattr(torch.backends.cuda.matmul, name, False)
    resolved = torch.device(device)
    if resolved.type == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA is required for the requested device")
        torch.cuda.set_device(resolved)
        torch.cuda.reset_peak_memory_stats(resolved)
    elif resolved.type != "cpu":
        raise ValueError("Only cpu and cuda devices are supported")
    return resolved


def environment(device):
    result = {"python": sys.version, "executable": sys.executable,
              "platform": platform.platform(), "numpy": np.__version__,
              "torch": torch.__version__, "torch_cuda": torch.version.cuda,
              "cudnn": torch.backends.cudnn.version(), "device": str(device),
              "threads": torch.get_num_threads(),
              "interop_threads": torch.get_num_interop_threads(),
              "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
              "float32_matmul_precision": torch.get_float32_matmul_precision(),
              "allow_tf32": torch.backends.cuda.matmul.allow_tf32,
              "cudnn_allow_tf32": torch.backends.cudnn.allow_tf32,
              "environment": {key: os.environ.get(key) for key in (
                  "CUDA_VISIBLE_DEVICES", "CUBLAS_WORKSPACE_CONFIG", "NVIDIA_TF32_OVERRIDE",
                  "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                  "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")}}
    for name in ("allow_fp16_reduced_precision_reduction",
                 "allow_bf16_reduced_precision_reduction", "allow_fp16_accumulation"):
        if hasattr(torch.backends.cuda.matmul, name):
            result[name] = getattr(torch.backends.cuda.matmul, name)
    if device.type == "cuda":
        props = torch.cuda.get_device_properties(device)
        result["gpu"] = {"name": props.name, "total_memory_bytes": props.total_memory,
                         "capability": [props.major, props.minor],
                         "multiprocessor_count": props.multi_processor_count,
                         "uuid": str(getattr(props, "uuid", "unavailable"))}
    return result


def initial_arrays(width, seed):
    generator = np.random.default_rng(seed)
    return (generator.standard_normal((width, 2)),
            generator.standard_normal((width, width)) / np.sqrt(width),
            generator.standard_normal(width) / width)


def fields(state, directions):
    w1, w2, c = state
    z1 = w1 @ directions
    h1 = torch.tanh(z1)
    z2 = w2 @ h1
    h2 = torch.tanh(z2)
    prediction = (c @ h2) / c.numel()
    return z1, h1, z2, h2, prediction


def tanh_prime(z):
    # Same stable mathematical derivative as maintained TANH; avoid 1-tanh(z)^2
    # cancellation in saturated working-precision activations.
    exponential = torch.exp(-torch.abs(z))
    return (2.0 * exponential / (1.0 + exponential * exponential)).square()


def stage(state, directions, labels):
    """Factorized exact physical RHS with mobilities (n,1,n)."""
    _, w2, c = state
    z1, h1, z2, h2, prediction = fields(state, directions)
    residual = prediction - labels
    delta2 = c[:, None] * tanh_prime(z2)
    delta1 = (w2.T @ delta2) * tanh_prime(z1)
    common = -2.0 / labels.numel()
    velocity1 = common * ((delta1 * residual) @ directions.T)
    factor2 = delta2 * residual
    velocity_c = common * (h2 @ residual)
    return velocity1, factor2, h1, velocity_c


def rhs(state, directions, labels):
    v1, factor2, h1, vc = stage(state, directions, labels)
    return v1, (-2.0 / (labels.numel() * state[2].numel())) * (factor2 @ h1.T), vc


def heun_step(state, predictor, directions, labels, step):
    """Simultaneous explicit Heun using rank-m products and two matrix stores."""
    n = state[2].numel()
    scale2 = -2.0 / (labels.numel() * n)
    v1, a2, h1, vc = stage(state, directions, labels)
    torch.add(state[0], v1, alpha=step, out=predictor[0])
    torch.addmm(state[1], a2, h1.T, beta=1.0, alpha=step * scale2, out=predictor[1])
    torch.add(state[2], vc, alpha=step, out=predictor[2])
    v1b, a2b, h1b, vcb = stage(predictor, directions, labels)
    state[0].add_(v1, alpha=step / 2).add_(v1b, alpha=step / 2)
    state[1].addmm_(a2, h1.T, beta=1.0, alpha=step * scale2 / 2)
    state[1].addmm_(a2b, h1b.T, beta=1.0, alpha=step * scale2 / 2)
    state[2].add_(vc, alpha=step / 2).add_(vcb, alpha=step / 2)


def observe(state, panel, initial_hidden, weights):
    z1, h1, z2, h2, prediction = fields(state, panel)
    if not all(torch.isfinite(t).all().item() for t in (z1, z2, prediction)):
        raise FloatingPointError("Nonfinite network observation")
    hidden64 = (h1.double(), h2.double())
    m = weights.numel()
    grams, raw, movement, identities = [], [], [], []
    for h, h0 in zip(hidden64, initial_hidden):
        gram = (h.T @ h) / state[2].numel()
        raw2 = (h[:, :m].square().mean(dim=0) * weights).sum()
        movement2 = ((h[:, :m] - h0[:, :m].double()).square().mean(dim=0) * weights).sum()
        diagonal2 = (torch.diag(gram)[:m] * weights).sum()
        grams.append(gram.cpu().numpy())
        raw.append(float(raw2.sqrt().item()))
        movement.append(float(movement2.sqrt().item()))
        identities.append(float(torch.abs(raw2 - diagonal2).item()))
    return (prediction.double().cpu().numpy(), np.stack(grams),
            np.asarray(raw), np.asarray(movement), identities)


def directory_bytes(path):
    total = 0
    for directory, _, files in os.walk(path):
        for name in files:
            try:
                total += (Path(directory) / name).stat().st_size
            except FileNotFoundError:
                pass  # Another predeclared worker atomically replaced metadata.
    return total


def budget_check(start, global_start, generated_root, reserve=0, check_disk=False):
    if time.monotonic() - start >= 600:
        raise TimeoutError("600 second worker cap reached")
    if time.time() >= global_start + 1200:
        raise TimeoutError("1200 second scientific wall-time cap reached")
    if check_disk:
        free = shutil.disk_usage(generated_root).free
        size = directory_bytes(generated_root)
        if free - reserve < 3 * GIB:
            raise OSError("3 GiB minimum free-disk constraint reached")
        if size + reserve > 8 * GIB:
            raise OSError("8 GiB generated-product constraint reached")


def alarm_handler(signum, frame):
    if signum == signal.SIGTERM:
        raise TimeoutError("Supervisor sent SIGTERM; stopping and retaining partial observations")
    raise TimeoutError("Worker or global wall-time deadline reached")


def validate_inputs(data):
    expected = {"inputs": (16, 2), "labels": (16,), "weights": (16,),
                "panel": (144, 2), "times": (201,)}
    for name, shape in expected.items():
        if data[name].shape != shape or not np.isfinite(data[name]).all():
            raise ValueError(f"Invalid {name}: expected finite shape {shape}")
    if not np.array_equal(data["times"], np.arange(201, dtype=np.float64) / 2):
        raise ValueError("Observation times must be exactly 0,0.5,...,100")
    if not np.array_equal(data["weights"], np.full(16, 1 / 16)):
        raise ValueError("The declared finite law has exactly uniform weights")
    if not np.array_equal(data["panel"][:16], data["inputs"]):
        raise ValueError("Panel must begin with the 16 training inputs")
    if not np.allclose(np.linalg.norm(data["panel"], axis=1), 1, atol=2e-14, rtol=0):
        raise ValueError("Inputs must be unrescaled unit directions")


def run(args, start):
    output = Path(args.output).resolve()
    if not args.run_id or Path(args.run_id).name != args.run_id:
        raise ValueError("A simple manifest run-id is required")
    run_dir = output / "network" / args.run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    metadata = {"status": "running", "run_id": args.run_id, "started_at": now_utc(),
                "start_epoch": time.time(), "command": shlex.join(sys.orig_argv),
                "argv": list(sys.orig_argv), "cwd": str(Path.cwd()),
                "counts": {"observations": 0, "steps": 0}, "last_time": None,
                "last_step_time": 0.0, "scalar_panel": "training-weighted first 16 columns",
                "gram_panel": "all 144 columns, training first then passive circle",
                "physical_mobilities": "(width,1,width)",
                "loss_convention": "unhalved training mean squared residual",
                "integrator": "simultaneous explicit Heun",
                "source_hashes": {str(SOURCE): file_hash(SOURCE), str(PLAN): file_hash(PLAN)},
                "output_hashes": {}}
    metadata_path = run_dir / "record.json"
    write_json(metadata_path, metadata)
    gram_file = None
    observed_times, losses, predictions, raw_values, movements = [], [], [], [], []
    success = False
    try:
        manifest_path, input_path = output / "manifest.json", output / "inputs.npz"
        manifest = json.loads(manifest_path.read_text())
        actual_plan_hash, actual_input_hash = file_hash(PLAN), file_hash(input_path)
        if manifest["plan_sha256"] != actual_plan_hash:
            raise ValueError("Plan differs from the frozen manifest")
        if manifest["inputs_sha256"] != actual_input_hash:
            raise ValueError("Inputs differ from the frozen manifest")
        source_key = str(SOURCE.relative_to(REPO))
        if manifest["source_hashes"].get(source_key) != file_hash(SOURCE):
            raise ValueError("Runner differs from the frozen manifest or was not frozen")
        candidates = [r for r in manifest["network_runs"] if r["name"] == args.run_id]
        if len(candidates) != 1:
            raise ValueError("Run id must identify exactly one network_runs configuration")
        config = candidates[0]
        n, seed, step, dtype_name = (int(config["width"]), int(config["seed"]),
                                    float(config["step"]), config["dtype"])
        if (n, seed, step, dtype_name) not in ALLOWED_CONFIGS:
            raise ValueError("Configuration is outside the eight predeclared runs")
        global_start = float(manifest["scientific_start_epoch"])
        if not np.isfinite(global_start) or global_start > time.time() + 1:
            raise ValueError("scientific_start_epoch must be a finite actual launch epoch")
        generated_root = output.parent
        budget_check(start, global_start, generated_root, check_disk=True)
        remaining = min(600 - (time.monotonic() - start), global_start + 1200 - time.time())
        if remaining <= 0:
            raise TimeoutError("No worker budget remains")
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.signal(signal.SIGTERM, alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, remaining)
        with np.load(input_path, allow_pickle=False) as archive:
            data = {name: np.asarray(archive[name], dtype=np.float64) for name in (
                "inputs", "labels", "weights", "panel", "times")}
        validate_inputs(data)
        device = configure(args.device or "cuda:0")
        dtype = getattr(torch, dtype_name)
        metadata.update(config=config, software=environment(device),
                        scientific_start_epoch=global_start,
                        input_hashes={str(manifest_path): file_hash(manifest_path),
                                      str(input_path): file_hash(input_path)},
                        expected_observations=201, expected_steps=round(100 / step))
        arrays = initial_arrays(n, seed)
        metadata["initial_float64_arrays"] = {name: array_record(a) for name, a in
                                             zip(("W1", "W2", "c"), arrays)}
        state = tuple(torch.tensor(a, dtype=dtype, device=device) for a in arrays)
        del arrays
        predictor = tuple(torch.empty_like(a) for a in state)
        directions = torch.tensor(data["inputs"].T.copy(), dtype=dtype, device=device)
        labels = torch.tensor(data["labels"], dtype=dtype, device=device)
        panel = torch.tensor(data["panel"].T.copy(), dtype=dtype, device=device)
        weights = torch.tensor(data["weights"], dtype=torch.float64, device=device)
        gram_bytes = 201 * 2 * 144 * 144 * 8 + 1024
        checkpoint_bytes = (n * n + 3 * n + 2 * n * 144) * torch.tensor([], dtype=dtype).element_size()
        budget_check(start, global_start, generated_root,
                     reserve=gram_bytes + checkpoint_bytes + 2 * 1024 ** 2, check_disk=True)
        gram_file = np.lib.format.open_memmap(run_dir / "gram.npy", mode="w+",
                                             dtype=np.float64, shape=(201, 2, 144, 144))
        gram_file[:] = np.nan
        gram_file.flush()
        gates = {"all_observations_finite": True, "gram_symmetry_max_abs": 0.0,
                 "gram_abs_max": 0.0, "raw_gram_identity_max_abs": 0.0,
                 "endpoint_min_eigenvalues": {}, "sampled_loss_increases": []}
        metadata["gates"] = gates
        with torch.inference_mode():
            initial_fields = fields(state, panel)
            initial_hidden = (initial_fields[1].clone(), initial_fields[3].clone())
            metadata["initial_working_arrays"] = {
                name: array_record(value.cpu().numpy())
                for name, value in zip(("W1", "W2", "c"), state)}
            del initial_fields
            write_json(metadata_path, metadata)
            steps_per_observation = round(0.5 / step)
            if steps_per_observation * step != 0.5:
                raise ValueError("Fixed step must land exactly on observation nodes")
            for index, target_time in enumerate(data["times"]):
                if index:
                    for _ in range(steps_per_observation):
                        budget_check(start, global_start, generated_root)
                        heun_step(state, predictor, directions, labels, step)
                        metadata["counts"]["steps"] += 1
                        metadata["last_step_time"] = metadata["counts"]["steps"] * step
                        if device.type == "cuda" and metadata["counts"]["steps"] % 10 == 0:
                            torch.cuda.synchronize(device)
                budget_check(start, global_start, generated_root, check_disk=True)
                prediction, gram, raw, movement, identities = observe(
                    state, panel, initial_hidden, weights)
                loss_value = float(np.sum(data["weights"] * (prediction[:16] - data["labels"]) ** 2))
                values = (prediction, gram, raw, movement, np.asarray(loss_value))
                if not all(np.isfinite(value).all() for value in values):
                    gates["all_observations_finite"] = False
                    raise FloatingPointError("Nonfinite recorded scalar or array")
                symmetry = float(np.max(np.abs(gram - gram.transpose(0, 2, 1))))
                gram_max = float(np.max(np.abs(gram)))
                identity_error = max(identities)
                gates["gram_symmetry_max_abs"] = max(gates["gram_symmetry_max_abs"], symmetry)
                gates["gram_abs_max"] = max(gates["gram_abs_max"], gram_max)
                gates["raw_gram_identity_max_abs"] = max(gates["raw_gram_identity_max_abs"], identity_error)
                if symmetry > 2e-10 or gram_max > 1 + 2e-10 or identity_error > 2e-10:
                    raise FloatingPointError("Gram bound, symmetry or scalar identity failed")
                if index in (0, 200):
                    minimum = [float(np.linalg.eigvalsh(g)[0]) for g in gram]
                    gates["endpoint_min_eigenvalues"][str(float(target_time))] = minimum
                    if min(minimum) < -2e-10:
                        raise FloatingPointError("Endpoint Gram PSD gate failed")
                if losses and loss_value - losses[-1] > max(1e-6, 1e-4 * losses[-1]):
                    gates["sampled_loss_increases"].append({"time": float(target_time),
                        "preceding_loss": losses[-1], "loss": loss_value})
                gram_file[index] = gram
                observed_times.append(float(target_time))
                losses.append(loss_value)
                predictions.append(prediction)
                raw_values.append(raw)
                movements.append(movement)
                metadata["counts"]["observations"] = len(observed_times)
                metadata["last_time"] = float(target_time)
                metadata["elapsed_seconds"] = time.monotonic() - start
                write_json(metadata_path, metadata)
            budget_check(start, global_start, generated_root, reserve=checkpoint_bytes, check_disk=True)
            checkpoint = {"W1": state[0].cpu(), "W2": state[1].cpu(), "c": state[2].cpu(),
                          "initial_hidden_panel": tuple(h.cpu() for h in initial_hidden),
                          "time": 100.0, "step": step, "steps": metadata["counts"]["steps"],
                          "config": config, "input_hashes": metadata["input_hashes"],
                          "source_hashes": metadata["source_hashes"],
                          "initial_float64_arrays": metadata["initial_float64_arrays"]}
            torch.save(checkpoint, run_dir / "checkpoint.pt")
        budget_check(start, global_start, generated_root, check_disk=True)
        success = True
    except BaseException as error:
        metadata["status"] = "failed"
        metadata["failure"] = {"type": type(error).__name__, "message": str(error),
                               "traceback": traceback.format_exc()}
        print(metadata["failure"]["traceback"], file=sys.stderr, flush=True)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if gram_file is not None:
            gram_file.flush()
            del gram_file
        np.savez(run_dir / "observations.npz", times=np.asarray(observed_times),
                 loss=np.asarray(losses), predictions=np.asarray(predictions).reshape(-1, 144),
                 raw_rms=np.asarray(raw_values).reshape(-1, 2),
                 movement_rms=np.asarray(movements).reshape(-1, 2))
        if success:
            metadata["status"] = "complete"
        metadata["finished_at"] = now_utc()
        metadata["elapsed_seconds"] = time.monotonic() - start
        metadata["exit_status"] = 0 if success else 1
        metadata["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        if torch.cuda.is_initialized():
            metadata["cuda_peak_allocated_bytes"] = torch.cuda.max_memory_allocated()
            metadata["cuda_peak_reserved_bytes"] = torch.cuda.max_memory_reserved()
        metadata["output_hashes"] = {p.name: {"sha256": file_hash(p), "bytes": p.stat().st_size}
                                      for p in sorted(run_dir.iterdir())
                                      if p.is_file() and p.name not in ("record.json", "record.json.tmp")}
        metadata["elapsed_including_hashes_seconds"] = time.monotonic() - start
        write_json(metadata_path, metadata)
    return 0 if success else 1


def verify(args):
    """Deterministic tiny equations only; this never starts a training trajectory."""
    check_dir = Path(args.output).resolve()
    check_dir.mkdir(parents=True, exist_ok=True)
    device = configure(args.device or "cpu")
    check_path = check_dir / ("network_verification_" + str(device).replace(":", "_") + ".json")
    if check_path.exists():
        raise FileExistsError(f"Refusing to overwrite a frozen verification: {check_path}")
    sys.path.insert(0, str(REPO / "code"))
    from pde import finite_network as maintained
    report = {"status": "running", "started_at": now_utc(), "command": shlex.join(sys.orig_argv),
        "argv": list(sys.orig_argv), "cwd": str(Path.cwd()), "software": environment(device),
        "source_hashes": {str(SOURCE): file_hash(SOURCE), str(PLAN): file_hash(PLAN),
                          str(Path(maintained.__file__).resolve()): file_hash(maintained.__file__)},
        "checks": {}, "scope": "tiny deterministic equations; no training campaign"}
    checks = report["checks"]

    def compare(name, actual, expected, tolerance=2e-10):
        a, b = np.asarray(actual), np.asarray(expected)
        error = float(np.max(np.abs(a - b)))
        scale = max(1.0, float(np.max(np.abs(b))))
        passed = bool(np.isfinite(a).all() and np.isfinite(b).all() and error <= tolerance * scale)
        checks[name] = {"max_abs_error": error, "scale": scale,
                        "tolerance": tolerance, "passed": passed}
        if not passed:
            raise AssertionError(f"{name} failed: error {error}, scale {scale}")

    try:
        n, m = 7, 5
        generator = np.random.default_rng(271828)
        directions_np = generator.normal(size=(2, m))
        directions_np /= np.linalg.norm(directions_np, axis=0)
        labels_np = generator.normal(size=m)
        arrays = (generator.normal(size=(n, 2)), generator.normal(size=(n, n)) / np.sqrt(n),
                  generator.normal(size=n) * 0.7)
        parameters = maintained.Parameters(arrays[:2], arrays[2])
        physical = np.sqrt(2.0) * directions_np
        state = tuple(torch.tensor(a, dtype=torch.float64, device=device) for a in arrays)
        directions = torch.tensor(directions_np, dtype=torch.float64, device=device)
        labels = torch.tensor(labels_np, dtype=torch.float64, device=device)
        expected = maintained.flow_velocity(parameters, physical, labels_np)
        actual = rhs(state, directions, labels)
        for name, a, b in zip(("W1", "W2", "c"), actual, expected.weights + (expected.readout,)):
            compare("maintained_rhs_" + name, a.cpu().numpy(), b)
        maintained_fields = maintained.forward(parameters, physical)
        computed_fields = fields(state, directions)
        compare("forward", computed_fields[-1].cpu().numpy(), maintained_fields.output)
        for layer in range(2):
            compare(f"hidden_{layer + 1}", computed_fields[1 + 2 * layer].cpu().numpy(),
                    maintained_fields.hidden[layer])
        autodiff = tuple(a.detach().clone().requires_grad_(True) for a in state)
        loss_value = (fields(autodiff, directions)[-1] - labels).square().mean()
        gradients = torch.autograd.grad(loss_value, autodiff)
        for name, velocity, gradient, mobility in zip(("W1", "W2", "c"), actual, gradients, (n, 1, n)):
            compare("autograd_rhs_" + name, velocity.detach().cpu().numpy(),
                    (-mobility * gradient).detach().cpu().numpy())
        compare("unhalved_mse", loss_value.detach().cpu().numpy(), maintained.loss(parameters, physical, labels_np))
        residual = maintained_fields.output - labels_np
        expected_dissipation = -4 / m ** 2 * (residual @ maintained.kernel(parameters, physical) @ residual)
        actual_dissipation = -sum(float(a.square().sum().item()) / mu for a, mu in zip(actual, (n, 1, n)))
        compare("physical_loss_dissipation", actual_dissipation, expected_dissipation)
        initial = initial_arrays(n, 41)
        established_initial = maintained.initialize(n, 2, 2, seed=41)
        for name, a, b in zip(("W1", "W2", "c"), initial,
                              established_initial.weights + (established_initial.readout,)):
            compare("initialization_" + name, a, b, tolerance=0)
        small_step = 0.01
        predicted = maintained.Parameters(tuple(a + small_step * b for a, b in
            zip(parameters.weights, expected.weights)), parameters.readout + small_step * expected.readout)
        expected_second = maintained.flow_velocity(predicted, physical, labels_np)
        expected_heun = [a + small_step / 2 * (b + c) for a, b, c in zip(arrays,
            expected.weights + (expected.readout,), expected_second.weights + (expected_second.readout,))]
        stepped = tuple(a.clone() for a in state)
        with torch.inference_mode():
            heun_step(stepped, tuple(torch.empty_like(a) for a in state), directions, labels, small_step)
        for name, a, b in zip(("W1", "W2", "c"), stepped, expected_heun):
            compare("simultaneous_heun_" + name, a.cpu().numpy(), b)
        weights = torch.full((m,), 1 / m, dtype=torch.float64, device=device)
        initial_hidden = (computed_fields[1], computed_fields[3])
        prediction, grams, raw, movement, identities = observe(state, directions, initial_hidden, weights)
        compare("zero_initial_movement", movement, np.zeros(2), tolerance=0)
        compare("scalar_gram_identity", identities, np.zeros(2))
        for layer, h in enumerate(maintained_fields.hidden):
            gram = h.T @ h / n
            compare(f"gram_{layer + 1}", grams[layer], gram)
            compare(f"raw_rms_{layer + 1}", raw[layer], np.sqrt(np.mean(h ** 2)))
        observed_stepped = observe(stepped, directions, initial_hidden, weights)
        stepped_fields = fields(stepped, directions)
        for layer in range(2):
            h = stepped_fields[1 + layer * 2].cpu().numpy()
            h0 = maintained_fields.hidden[layer]
            compare(f"movement_rms_{layer + 1}", observed_stepped[3][layer], np.sqrt(np.mean((h - h0) ** 2)))
        kernel = grams[1]
        eigenvalues, vectors = np.linalg.eigh(kernel)
        initial_residual = prediction - labels_np
        coefficients = vectors.T @ initial_residual
        frozen = lambda t: labels_np + vectors @ (np.exp(-2 * t * eigenvalues / m) * coefficients)
        compare("frozen_readout_zero_time", frozen(0), prediction)
        t = 0.37
        spectral_velocity = vectors @ ((-2 * eigenvalues / m) * np.exp(-2 * t * eigenvalues / m) * coefficients)
        compare("frozen_readout_ode", spectral_velocity, -2 / m * kernel @ (frozen(t) - labels_np))
        epsilon = 1e-5
        compare("frozen_readout_finite_difference", (frozen(t + epsilon) - frozen(t - epsilon)) / (2 * epsilon),
                spectral_velocity, tolerance=2e-9)
        frozen_velocity = -2 / m * (maintained_fields.hidden[-1] @ initial_residual)
        compare("frozen_readout_mobility", maintained_fields.hidden[-1].T @ frozen_velocity / n,
                -2 / m * kernel @ initial_residual)
        report["status"] = "passed"
        report["passed_count"] = len(checks)
    except BaseException as error:
        report["status"] = "failed"
        report["failure"] = {"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()}
    report["finished_at"] = now_utc()
    write_json(check_path, report)
    print(json.dumps({"status": report["status"], "path": str(check_path),
                      "checks": len(checks), "source_sha256": file_hash(SOURCE)}), flush=True)
    return 0 if report["status"] == "passed" else 1


def main():
    start = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--device")
    args = parser.parse_args()
    if args.verify:
        if args.run_id:
            parser.error("--verify does not take --run-id")
        return verify(args)
    if not args.run_id:
        parser.error("training requires --run-id")
    return run(args, start)


if __name__ == "__main__":
    raise SystemExit(main())
