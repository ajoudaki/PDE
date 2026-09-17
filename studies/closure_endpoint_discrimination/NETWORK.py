"""Study-local, exact two-hidden-layer tanh flow with a GPU Heun integrator.

The middle Euler predictor is applied as a rank-m correction, with its actual
transpose used in the backward pass. No independent transpose or fixed kernel
is introduced. Stored parameters a,b,c correspond to W1,W2,readout.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import sys
import time

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import numpy as np
import torch


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / "data/generated/closure_endpoint_discrimination"


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def config_hash(config):
    encoded = json.dumps(config, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def setup(device):
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_float32_matmul_precision("highest")
    torch.use_deterministic_algorithms(True)
    if str(device).startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("CUDA unavailable: run through the approved GPU execution route")


def sync(device):
    if str(device).startswith("cuda"):
        torch.cuda.synchronize(device)


@dataclass
class State:
    a: torch.Tensor
    b: torch.Tensor
    c: torch.Tensor

    @property
    def n(self):
        return self.c.numel()

    def clone(self):
        return State(self.a.clone(), self.b.clone(), self.c.clone())


def tanh_derivative(z):
    # The maintained finite model uses this saturation-stable formula.
    u = torch.exp(-torch.abs(z))
    return (2 * u / (1 + u * u)).square()


def forward(state, u):
    """u has shape (2,m), and equals the physical inputs divided by sqrt(2)."""
    z1 = state.a @ u
    h1 = torch.tanh(z1)
    z2 = state.b @ h1
    h2 = torch.tanh(z2)
    output = state.c @ h2 / state.n
    return output, (h1, h2), (z1, z2)


def contractions(state, u, labels):
    output, hidden, z = forward(state, u)
    residual = output - labels
    source = state.c[:, None] * tanh_derivative(z[1]) * residual
    factor = -2.0 / labels.numel()
    da = factor * ((state.b.T @ source) * tanh_derivative(z[0])) @ u.T
    dc = factor * (hidden[1] @ residual)
    return da, dc, source, hidden[0]


def velocity(state, u, labels):
    """Dense RHS for validation; the training integrator avoids forming db."""
    da, dc, source, hidden = contractions(state, u, labels)
    db = (-2.0 / (labels.numel() * state.n)) * (source @ hidden.T)
    return State(da, db, dc)


@torch.no_grad()
def heun_step(state, u, labels, h):
    da, dc, source, hidden = contractions(state, u, labels)
    factor = -2.0 / labels.numel()
    middle_factor = factor / state.n
    ap = state.a + h * da
    cp = state.c + h * dc
    z1p = ap @ u
    h1p = torch.tanh(z1p)
    z2p = state.b @ h1p + (h * middle_factor) * (source @ (hidden.T @ h1p))
    h2p = torch.tanh(z2p)
    residualp = cp @ h2p / state.n - labels
    sourcep = cp[:, None] * tanh_derivative(z2p) * residualp
    backwards = state.b.T @ sourcep + (h * middle_factor) * (hidden @ (source.T @ sourcep))
    dap = factor * (backwards * tanh_derivative(z1p)) @ u.T
    dcp = factor * (h2p @ residualp)
    state.a.add_(da + dap, alpha=h / 2)
    state.c.add_(dc + dcp, alpha=h / 2)
    # A single rank-2m update rounds the stored middle matrix only once.
    state.b.addmm_(torch.cat((source, sourcep), dim=1),
                   torch.cat((hidden, h1p), dim=1).T,
                   alpha=h * middle_factor / 2)
    return state


def initialize(width, seed, dtype, device, block_rows=256):
    """Same PCG64 float64 stream and scaling as maintained initialize()."""
    rng = np.random.default_rng(seed)
    hashes = {}
    a64 = rng.standard_normal((width, 2))
    hashes["a"] = hashlib.sha256(a64.tobytes(order="C")).hexdigest()
    a = torch.as_tensor(a64, dtype=dtype, device=device).clone()
    b = torch.empty((width, width), dtype=dtype, device=device)
    digest = hashlib.sha256()
    for row in range(0, width, block_rows):
        block = rng.standard_normal((min(block_rows, width - row), width)) / np.sqrt(width)
        digest.update(block.tobytes(order="C"))
        b[row:row + block.shape[0]].copy_(torch.as_tensor(block, dtype=dtype, device=device))
    hashes["b"] = digest.hexdigest()
    c64 = rng.standard_normal(width) / width
    hashes["c"] = hashlib.sha256(c64.tobytes(order="C")).hexdigest()
    c = torch.as_tensor(c64, dtype=dtype, device=device).clone()
    return State(a, b, c), hashes


def array(tensor):
    return tensor.detach().cpu().numpy().copy()


def atomic_json(path, content):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(content, indent=2, sort_keys=True, allow_nan=False) + "\n")
    temporary.replace(path)


def validate_out(path):
    path = Path(path).resolve()
    if not path.is_relative_to(GENERATED.resolve()):
        raise ValueError(f"output must be inside {GENERATED}")
    path.mkdir(parents=True, exist_ok=False)
    return path


def plateau(history, t_min):
    times = np.asarray(history["times"])
    if len(times) < 3 or times[-1] < t_min - 1e-8:
        return False, None
    now = times[-1]
    if abs(now / 25 - round(now / 25)) > 1e-8:
        return False, None
    indices = []
    for wanted in (now - 50, now - 25, now):
        candidates = np.flatnonzero(np.abs(times - wanted) < 1e-8)
        if not len(candidates):
            return False, None
        indices.append(int(candidates[-1]))
    m = history["grams"][-1].shape[-1]
    drifts, loss_changes = [], []
    for first, second in zip(indices[:-1], indices[1:]):
        drifts.append(float(np.max(np.abs(history["predictions"][second][m:] -
                                            history["predictions"][first][m:]))))
        loss_changes.append(abs(float(history["loss"][second]) - float(history["loss"][first])))
    return max(drifts) < .005 and max(loss_changes) < .0005, {
        "circle_drift_last_two_25": drifts, "loss_change_last_two_25": loss_changes}


@torch.no_grad()
def observe(state, evaluation_u, labels, h0):
    predictions, hidden, _ = forward(state, evaluation_u)
    m = labels.numel()
    training = tuple(value[:, :m] for value in hidden)
    grams = torch.stack([value.T @ value / state.n for value in training])
    rms = torch.stack([value.square().mean().sqrt() for value in training])
    movement = torch.stack([(value - initial).square().mean().sqrt()
                            for value, initial in zip(training, h0)])
    loss = (predictions[:m] - labels).square().mean()
    values = {"predictions": array(predictions), "grams": array(grams),
              "rms": array(rms), "movement": array(movement), "loss": float(loss)}
    if not all(np.all(np.isfinite(value)) for value in values.values()):
        raise FloatingPointError("nonfinite trajectory observation")
    return values


def save_history(out, history, dense=None):
    values = {key: np.asarray(value) for key, value in history.items()}
    if dense is not None:
        values["dense_predictions"] = np.asarray(dense)
    temporary = out / "trajectories.tmp.npz"
    np.savez_compressed(temporary, **values)
    temporary.replace(out / "trajectories.npz")


def checkpoint(out, state, h0, config, current_time, source_hash, inputs_hash, init_hashes):
    payload = {"a": state.a.cpu(), "b": state.b.cpu(), "c": state.c.cpu(),
               "h0": [value.cpu() for value in h0], "config": config,
               "time": current_time, "source_hash": source_hash,
               "inputs_hash": inputs_hash, "initialization_hashes": init_hashes}
    temporary = out / "state.tmp.pt"
    torch.save(payload, temporary)
    temporary.replace(out / "state.pt")


def load_checkpoint(path, dtype, device):
    saved = torch.load(path, map_location="cpu", weights_only=False)
    state = State(*(saved[key].to(device=device, dtype=dtype) for key in ("a", "b", "c")))
    h0 = tuple(value.to(device=device, dtype=dtype) for value in saved["h0"])
    return state, h0, saved


@torch.no_grad()
def run(config, out, resume=None):
    start = time.monotonic()
    device = config.get("device", "cuda:0")
    setup(device)
    dtype = {"float32": torch.float32, "float64": torch.float64}[config.get("dtype", "float32")]
    width, seed = int(config["width"]), int(config["seed"])
    h, obs_dt = float(config.get("h", .02)), float(config.get("obs_dt", 5))
    t_min, t_max = float(config.get("t_min", 100)), float(config.get("t_max", 600))
    if config.get("kind") != "network" or width < 1 or seed < 0:
        raise ValueError("invalid network configuration")
    if not (0 < h <= .02 and 0 < obs_dt <= 25 and 0 <= t_min <= t_max <= 1600):
        raise ValueError("invalid time grid or campaign time cap")
    observation_steps, final_step = round(obs_dt / h), round(t_max / h)
    if abs(observation_steps * h - obs_dt) > 1e-10 or abs(final_step * h - t_max) > 1e-10:
        raise ValueError("observation spacing and horizon must lie on the Heun mesh")
    inputs_path = Path(config["inputs_path"]).resolve()
    if not inputs_path.is_relative_to(GENERATED.resolve()):
        raise ValueError("inputs must belong to this study")
    source_hash, inputs_hash = sha256(__file__), sha256(inputs_path)
    with np.load(inputs_path, allow_pickle=False) as inputs:
        train_u = np.array(inputs["train_u"])
        labels_np = np.array(inputs["labels"])
        probabilities = np.array(inputs["probabilities"])
        circle_u, dense_u = np.array(inputs["circle_u"]), np.array(inputs["dense_u"])
    m = len(labels_np)
    if train_u.shape != (m, 2) or circle_u.shape != (720, 2) or dense_u.shape != (1440, 2):
        raise ValueError("unexpected input-panel shapes")
    if probabilities.shape != (m,) or np.any(probabilities <= 0) or not np.allclose(probabilities, 1 / m, atol=1e-15, rtol=0):
        raise ValueError("the network requires positive uniform sample probabilities")
    if not all(np.all(np.isfinite(value)) for value in (train_u, labels_np, circle_u, dense_u)):
        raise ValueError("nonfinite inputs")
    if not all(np.allclose(np.sum(value * value, axis=1), 1, atol=1e-12, rtol=0)
               for value in (train_u, circle_u, dense_u)):
        raise ValueError("campaign directions must have unit Euclidean length")
    u = torch.tensor(train_u.T, dtype=dtype, device=device)
    labels = torch.tensor(labels_np, dtype=dtype, device=device)
    evaluation_u = torch.tensor(np.concatenate((train_u, circle_u)).T, dtype=dtype, device=device)
    dense_tensor = torch.tensor(dense_u.T, dtype=dtype, device=device)
    history = {key: [] for key in ("times", "predictions", "loss", "grams", "rms", "movement")}
    if resume:
        resume = Path(resume).resolve()
        if not resume.is_relative_to(GENERATED.resolve()):
            raise ValueError("checkpoint must belong to this study")
        prior_record = json.loads((resume.parent / "record.json").read_text())
        for name in ("state.pt", "trajectories.npz"):
            if sha256(resume.parent / name) != prior_record["output_hashes"][name]:
                raise ValueError(f"checkpoint output hash mismatch: {name}")
        state, h0, saved = load_checkpoint(resume, dtype, device)
        if saved["config"] != prior_record["config"] or config_hash(saved["config"]) != prior_record["config_hash"]:
            raise ValueError("checkpoint configuration hash mismatch")
        if saved["source_hash"] != source_hash or saved["inputs_hash"] != inputs_hash:
            raise ValueError("checkpoint source or input hash mismatch")
        for key, default in (("kind", None), ("stage", None), ("width", None), ("seed", None),
                             ("dtype", "float32"), ("h", .02), ("obs_dt", 5)):
            if config.get(key, default) != saved["config"].get(key, default):
                raise ValueError(f"checkpoint configuration mismatch: {key}")
        current_time = float(saved["time"])
        init_hashes = saved["initialization_hashes"]
        with np.load(resume.parent / "trajectories.npz", allow_pickle=False) as prior:
            for key in history:
                history[key] = list(prior[key])
        if abs(float(history["times"][-1]) - current_time) > 1e-9:
            raise ValueError("checkpoint and trajectory times disagree")
        replay = observe(state, evaluation_u, labels, h0)
        for key, value in replay.items():
            if not np.array_equal(value, history[key][-1]):
                raise ValueError(f"checkpoint history replay mismatch: {key}")
    else:
        state, init_hashes = initialize(width, seed, dtype, device)
        _, initial_hidden, _ = forward(state, u)
        h0 = tuple(value.clone() for value in initial_hidden)
        current_time = 0.0
        observation = observe(state, evaluation_u, labels, h0)
        history["times"].append(current_time)
        for key, value in observation.items():
            history[key].append(value)
    current_step = round(current_time / h)
    if current_step > final_step or abs(current_step * h - current_time) > 1e-8:
        raise ValueError("resume time is beyond horizon or off mesh")
    stop_requested = [False]
    def on_signal(signum, frame):
        stop_requested[0] = True
    old_handlers = {sig: signal.signal(sig, on_signal) for sig in (signal.SIGTERM, signal.SIGINT)}
    status, reason = "complete", "horizon"
    settled, settle_details = plateau(history, t_min)
    save_history(out, history)
    try:
        for step in range(current_step + 1, final_step + 1):
            heun_step(state, u, labels, h)
            current_time = step * h
            should_stop = stop_requested[0] or time.monotonic() - start > float(config.get("worker_timeout", 1150))
            if step % observation_steps == 0 or step == final_step or should_stop:
                observation = observe(state, evaluation_u, labels, h0)
                history["times"].append(current_time)
                for key, value in observation.items():
                    history[key].append(value)
                save_history(out, history)
                settled, settle_details = plateau(history, t_min)
                if len(history["loss"]) > 1 and history["loss"][-1] - history["loss"][-2] > 1e-5:
                    status, reason = "failed", "saved-interval loss increase exceeds 1e-5"
                    break
                if should_stop:
                    status, reason = "partial", "signal or worker wall-time limit"
                    break
                if settled and config.get("auto_stop", True):
                    reason = "plateau"
                    break
    finally:
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)
    dense = array(forward(state, dense_tensor)[0])
    if not np.all(np.isfinite(dense)):
        raise FloatingPointError("nonfinite endpoint circle output")
    save_history(out, history, dense)
    checkpoint(out, state, h0, config, current_time, source_hash, inputs_hash, init_hashes)
    replay_state, replay_h0, saved = load_checkpoint(out / "state.pt", dtype, device)
    state_exact = all(torch.equal(getattr(state, key), getattr(replay_state, key)) for key in ("a", "b", "c"))
    state_exact = state_exact and all(torch.equal(a, b) for a, b in zip(h0, replay_h0))
    replay_dense = array(forward(replay_state, dense_tensor)[0])
    grams = np.asarray(history["grams"], dtype=np.float64)
    all_losses = np.asarray(history["loss"], dtype=np.float64)
    rms = np.asarray(history["rms"], dtype=np.float64)
    # Explicit negative queries avoid assuming an index pairing for the panel.
    opposite = array(forward(replay_state, -dense_tensor)[0])
    checks = {"all_finite": all(np.all(np.isfinite(value)) for value in history.values()) and bool(np.all(np.isfinite(dense))),
              "unit_uniform_probabilities": True,
              "gram_symmetry_error": float(np.max(np.abs(grams - grams.swapaxes(-1, -2)))),
              "gram_min_eigenvalue": float(np.min(np.linalg.eigvalsh(grams))),
              "rms_gram_error": float(np.max(np.abs(rms ** 2 - np.diagonal(grams, axis1=-2, axis2=-1).mean(axis=-1)))),
              "mse_recompute_error": float(np.max(np.abs(all_losses - np.mean((np.asarray(history["predictions"], dtype=np.float64)[:, :m] - labels_np) ** 2, axis=1)))),
              "max_loss_increase": float(max(0, np.max(np.diff(all_losses)))) if len(all_losses) > 1 else 0.0,
              "oddness_error": float(np.max(np.abs(dense + opposite))),
              "checkpoint_state_exact": bool(state_exact),
              "checkpoint_prediction_replay_error": float(np.max(np.abs(dense - replay_dense))),
              "tf32_disabled": not torch.backends.cuda.matmul.allow_tf32}
    if (not checks["all_finite"] or not state_exact or checks["gram_min_eigenvalue"] < -1e-5
            or checks["max_loss_increase"] > 1e-5 or checks["checkpoint_prediction_replay_error"] != 0
            or max(checks["gram_symmetry_error"], checks["rms_gram_error"],
                   checks["mse_recompute_error"], checks["oddness_error"]) > 1e-5):
        status, reason = "failed", "endpoint validation check failed"
    sync(device)
    record = {"status": status, "stop_reason": reason, "settled": bool(settled),
              "last_time": current_time, "config": config, "checks": checks,
              "settling": settle_details, "elapsed": time.monotonic() - start,
              "inputs_hash": inputs_hash, "source_hash": source_hash,
              "config_hash": config_hash(config),
              "initialization_hashes": init_hashes,
              "resume_from": str(resume) if resume else None,
              "environment": {"python": sys.version, "numpy": np.__version__, "torch": torch.__version__,
                              "device": str(device), "gpu": torch.cuda.get_device_name(device) if str(device).startswith("cuda") else None},
              "output_hashes": {name: sha256(out / name) for name in ("state.pt", "trajectories.npz")}}
    atomic_json(out / "record.json", record)
    print(json.dumps({"out": str(out), "status": status, "time": current_time,
                      "settled": settled, "loss": float(history["loss"][-1]), "elapsed": record["elapsed"]}), flush=True)
    return record


def check(out, device):
    setup(device)
    sys.path.insert(0, str(ROOT / "code"))
    from pde.finite_network import Parameters, forward as reference_forward
    from pde.finite_network import flow_velocity, initialize as reference_initialize
    rng = np.random.default_rng(83041)
    n, m = 9, 5
    values = (rng.normal(size=(n, 2)) * .7, rng.normal(size=(n, n)) * .25,
              rng.normal(size=n) * .4)
    u_np = rng.normal(size=(2, m))
    labels_np = rng.normal(size=m)
    state = State(*(torch.tensor(value, dtype=torch.float64, device=device) for value in values))
    u = torch.tensor(u_np, dtype=torch.float64, device=device)
    labels = torch.tensor(labels_np, dtype=torch.float64, device=device)
    reference = Parameters(values[:2], values[2])
    inputs = np.sqrt(2) * u_np
    errors = {}
    output, hidden, _ = forward(state, u)
    reference_fields = reference_forward(reference, inputs)
    errors["forward"] = float(np.max(np.abs(array(output) - reference_fields.output)))
    errors["hidden"] = max(float(np.max(np.abs(array(value) - other))) for value, other in zip(hidden, reference_fields.hidden))
    rhs = velocity(state, u, labels)
    reference_rhs = flow_velocity(reference, inputs, labels_np)
    errors["maintained_rhs"] = max(float(np.max(np.abs(array(value) - other)))
                                  for value, other in zip((rhs.a, rhs.b, rhs.c), reference_rhs.weights + (reference_rhs.readout,)))
    autograd_state = State(*(value.detach().clone().requires_grad_() for value in (state.a, state.b, state.c)))
    autograd_loss = (forward(autograd_state, u)[0] - labels).square().mean()
    grads = torch.autograd.grad(autograd_loss, (autograd_state.a, autograd_state.b, autograd_state.c))
    errors["autograd_rhs"] = max(float(torch.max(torch.abs(actual + mobility * grad)))
                                 for actual, grad, mobility in zip((rhs.a, rhs.b, rhs.c), grads, (n, 1, n)))
    heun_reference = reference
    heun_actual = state.clone()
    step = .017
    for _ in range(7):
        k1 = flow_velocity(heun_reference, inputs, labels_np)
        predictor = Parameters(tuple(w + step * dw for w, dw in zip(heun_reference.weights, k1.weights)),
                               heun_reference.readout + step * k1.readout)
        k2 = flow_velocity(predictor, inputs, labels_np)
        heun_reference = Parameters(tuple(w + step / 2 * (v1 + v2) for w, v1, v2 in zip(heun_reference.weights, k1.weights, k2.weights)),
                                    heun_reference.readout + step / 2 * (k1.readout + k2.readout))
        heun_step(heun_actual, u, labels, step)
    errors["seven_step_heun"] = max(float(np.max(np.abs(array(value) - other)))
                                     for value, other in zip((heun_actual.a, heun_actual.b, heun_actual.c),
                                                             heun_reference.weights + (heun_reference.readout,)))
    initialized, init_hashes = initialize(n, 19, torch.float64, device, block_rows=4)
    init_reference = reference_initialize(n, 2, 2, seed=19)
    errors["initialization"] = max(float(np.max(np.abs(array(value) - other)))
                                    for value, other in zip((initialized.a, initialized.b, initialized.c),
                                                            init_reference.weights + (init_reference.readout,)))
    hash_match = all(init_hashes[key] == hashlib.sha256(value.tobytes(order="C")).hexdigest()
                     for key, value in zip(("a", "b", "c"), init_reference.weights + (init_reference.readout,)))
    initialized32, hashes32 = initialize(n, 19, torch.float32, device, block_rows=4)
    hash_match = hash_match and init_hashes == hashes32
    h0 = tuple(value.clone() for value in hidden)
    checkpoint(out, heun_actual, h0, {"kind": "synthetic_check"}, 7 * step, sha256(__file__), "synthetic", init_hashes)
    restored, restored_h0, saved = load_checkpoint(out / "state.pt", torch.float64, device)
    restart_exact = all(torch.equal(getattr(heun_actual, key), getattr(restored, key)) for key in ("a", "b", "c"))
    restart_exact = restart_exact and all(torch.equal(a, b) for a, b in zip(h0, restored_h0))
    uninterrupted = heun_actual.clone()
    for _ in range(3):
        heun_step(uninterrupted, u, labels, step)
        heun_step(restored, u, labels, step)
    errors["restart_continuation"] = max(float(torch.max(torch.abs(getattr(uninterrupted, key) - getattr(restored, key)))) for key in ("a", "b", "c"))
    errors["oddness"] = float(torch.max(torch.abs(forward(state, u)[0] + forward(state, -u)[0])))
    check_observation = observe(state, u, labels, h0)
    errors["rms_gram_identity"] = float(np.max(np.abs(check_observation["rms"] ** 2 -
        np.diagonal(check_observation["grams"], axis1=-2, axis2=-1).mean(axis=-1))))
    # Exercise the same serialized observation/history/configuration route as
    # scientific runs, using nine neurons and only four synthetic Heun steps.
    theta = np.linspace(0, 2 * np.pi, 720, endpoint=False)
    dense_theta = np.linspace(0, 2 * np.pi, 1440, endpoint=False)
    train_theta = np.array([-.3, .2, 1.0, 1.6, 2.8])
    synthetic_inputs = out / "synthetic_inputs.npz"
    np.savez(synthetic_inputs,
             train_u=np.column_stack((np.cos(train_theta), np.sin(train_theta))),
             labels=labels_np, probabilities=np.full(m, 1 / m),
             circle_u=np.column_stack((np.cos(theta), np.sin(theta))),
             dense_u=np.column_stack((np.cos(dense_theta), np.sin(dense_theta))))
    synthetic_config = {"id": "synthetic_check", "stage": "synthetic", "kind": "network",
                        "inputs_path": str(synthetic_inputs), "width": n, "seed": 19,
                        "dtype": "float64", "h": .02, "t_min": .02, "t_max": .08,
                        "auto_stop": False, "obs_dt": .02, "device": device}
    continuous_out = validate_out(out / "continuous")
    continuous_record = run(synthetic_config, continuous_out)
    split_out = validate_out(out / "split")
    split_record = run(dict(synthetic_config, t_max=.04), split_out)
    resumed_out = validate_out(out / "resumed")
    resumed_record = run(synthetic_config, resumed_out, split_out / "state.pt")
    with np.load(continuous_out / "trajectories.npz", allow_pickle=False) as left, np.load(resumed_out / "trajectories.npz", allow_pickle=False) as right:
        errors["serialized_history_restart"] = max(float(np.max(np.abs(left[key] - right[key]))) for key in left.files)
    serialization_passed = all(record["status"] == "complete" for record in (continuous_record, split_record, resumed_record))
    passed = all(error < 1e-10 for error in errors.values()) and hash_match and restart_exact
    passed = passed and serialization_passed
    result = {"passed": bool(passed), "errors": errors, "initialization_hashes_match": bool(hash_match),
              "checkpoint_state_exact": bool(restart_exact), "device": device,
              "source_hash": sha256(__file__), "torch": torch.__version__, "tf32_disabled": not torch.backends.cuda.matmul.allow_tf32,
              "scope": "tiny arbitrary nonzero state; no scientific trajectory"}
    atomic_json(out / "check.json", result)
    print(json.dumps(result, indent=2), flush=True)
    return passed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    out = validate_out(args.out)
    try:
        if args.check:
            return 0 if check(out, args.device) else 2
        if args.config is None:
            parser.error("--config is required unless --check is used")
        config = json.loads(args.config.read_text())
        record = run(config, out, args.resume)
        return 0 if record["status"] == "complete" else 2
    except Exception as error:
        atomic_json(out / "failure.json", {"error": repr(error), "source_hash": sha256(__file__)})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
