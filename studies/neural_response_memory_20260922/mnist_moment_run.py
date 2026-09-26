"""Bounded MNIST dense/moment comparison; validation never controls evolution.

All inputs are already scaled U=x/sqrt(d).  The direct moment coordinates
recompute tanh, giving the same continuous closure as the rational response
lift without numerical invariant drift.  Only fixed W0 is stored densely by
the moment engine.  The adaptive solver controls component RMS error; its
accuracy must additionally be checked by an independent tolerance refinement.
"""

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np
import torch

from moment_engine import MomentState, linear_combination
from orthogonal_moment_engine import OrthogonalMomentEngine


@dataclass
class DenseState:
    w: torch.Tensor
    W: torch.Tensor
    c: torch.Tensor

    def names(self):
        return ("w", "W", "c")

    def tensors(self):
        return tuple(getattr(self, name) for name in self.names())

    def clone(self):
        return DenseState(*(value.clone() for value in self.tensors()))


class DenseEngine:
    """Canonical equalwidth2 physical flow with mobilities (n,1,n)."""

    def __init__(self, d, width, inputs, labels, *, seed, device="cpu",
                 dtype=torch.float64):
        self.d, self.n = d, width
        self.device, self.dtype = torch.device(device), dtype
        self.inputs = torch.as_tensor(inputs, device=device, dtype=dtype).detach().clone()
        self.labels = torch.as_tensor(labels, device=device, dtype=dtype).detach().clone()
        self.M = len(self.labels)
        if self.inputs.shape != (self.M, d) or self.M == 0:
            raise ValueError("invalid training shapes")
        rng = np.random.default_rng(seed)
        self.initial = DenseState(*[
            torch.as_tensor(value, device=device, dtype=dtype).clone()
            for value in (rng.standard_normal((width, d)),
                          rng.standard_normal((width, width))/math.sqrt(width),
                          rng.standard_normal(width)/width)
        ])

    def initial_state(self):
        return self.initial.clone()

    def validate_state(self, state):
        if not all(bool(torch.isfinite(value).all()) for value in state.tensors()):
            raise ValueError("nonfinite dense state")
        return state

    @torch.no_grad()
    def predict(self, state, inputs):
        values = torch.as_tensor(inputs, dtype=self.dtype, device=self.device)
        h1 = torch.tanh(state.w @ values.T)
        h2 = torch.tanh(state.W @ h1)
        return state.c @ h2/self.n

    @torch.no_grad()
    def rhs(self, state):
        self.validate_state(state)
        h1 = torch.tanh(state.w @ self.inputs.T)
        h2 = torch.tanh(state.W @ h1)
        residual = state.c @ h2/self.n-self.labels
        delta2 = state.c[:, None]*(1-h2.square())
        delta1 = (state.W.T @ delta2)*(1-h1.square())
        return DenseState(
            (-2/self.M)*(delta1*residual) @ self.inputs,
            (-2/(self.M*self.n))*(delta2*residual) @ h1.T,
            (-2/self.M)*(h2 @ residual),
        )


def combine(coefficients, states):
    if isinstance(states[0], MomentState):
        return linear_combination(coefficients, states)
    return DenseState(*[
        sum((a*value for a, value in zip(coefficients, values)),
            torch.zeros_like(values[0]))
        for values in zip(*(state.tensors() for state in states))
    ])


def scalar(value):
    return float(value.detach().cpu())


def rms(value):
    return value.square().mean().sqrt()


def training_loss(engine, state):
    return scalar((engine.predict(state, engine.inputs)-engine.labels).square().mean())


def component_error(current, euler, candidate, rtol, atol):
    """No dense operator, factor Gram, or validation outputs enter this norm."""
    values = []
    for a, b, c in zip(current.tensors(), euler.tensors(), candidate.tensors()):
        scale = torch.maximum(rms(a), rms(c)).clamp_min(1.)
        values.append(rms(c-b)/(atol+rtol*scale))
    return scalar(torch.stack(values).max())


def heun_trial(engine, state, step, first=None):
    first = engine.rhs(state) if first is None else first
    euler = combine((1., step), (state, first))
    second = engine.rhs(euler)
    candidate = combine((1., step/2, step/2), (state, first, second))
    return first, second, euler, candidate


def heun_interpolant(state, first, second, step, fraction):
    """Second-order continuous extension, exact at both accepted endpoints."""
    if not 0 <= fraction <= 1:
        raise ValueError("interpolation fraction must be in [0,1]")
    return combine((1., step*(fraction-fraction*fraction/2),
                    step*fraction*fraction/2), (state, first, second))


def locate_loss_crossing(engine, state, first, second, step, threshold,
                         iterations=32):
    """Bisect the accepted Heun continuous extension using training loss only."""
    initial_loss = training_loss(engine, state)
    endpoint = heun_interpolant(state, first, second, step, 1.)
    final_loss = training_loss(engine, endpoint)
    if not final_loss <= threshold < initial_loss:
        raise ValueError("threshold must be bracketed by this accepted step")
    low, high = 0., 1.
    for _ in range(iterations):
        middle = (low+high)/2
        value = heun_interpolant(state, first, second, step, middle)
        if training_loss(engine, value) > threshold:
            low = middle
        else:
            high = middle
    fraction = (low+high)/2
    value = heun_interpolant(state, first, second, step, fraction)
    return fraction, value, training_loss(engine, value)


def synchronize(device):
    if torch.device(device).type == "cuda":
        torch.cuda.synchronize(device)


def panel_predict(engine, state, inputs, block=256):
    return np.concatenate([
        engine.predict(state, inputs[start:start+block]).detach().cpu().numpy()
        for start in range(0, len(inputs), block)
    ])


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_dataset(path):
    with np.load(path, allow_pickle=False) as archive:
        required = ("train_inputs", "train_labels", "validation_inputs", "validation_labels")
        data = {name: archive[name].copy() for name in required}
        for name in ("train_ids", "validation_ids"):
            if name in archive:
                data[name] = archive[name].copy()
    u, y = data["train_inputs"], data["train_labels"]
    v, z = data["validation_inputs"], data["validation_labels"]
    if u.ndim != 2 or v.ndim != 2 or u.shape[1] != v.shape[1]:
        raise ValueError("training and validation input dimensions must agree")
    if not len(u) or not len(v) or y.shape != (len(u),) or z.shape != (len(v),):
        raise ValueError("invalid dataset shapes")
    if not all(np.isfinite(data[name]).all() for name in required):
        raise ValueError("nonfinite dataset")
    for name, length in (("train_ids", len(u)), ("validation_ids", len(v))):
        if name in data and data[name].shape != (length,):
            raise ValueError("invalid ID shape: " + name)
    return data


def make_engine(args, data):
    common = dict(seed=args.seed, device=args.device, dtype=torch.float64)
    dimension = data["train_inputs"].shape[1]
    if args.model == "dense":
        return DenseEngine(dimension, args.width, data["train_inputs"],
                           data["train_labels"], **common)
    return OrthogonalMomentEngine(dimension, args.width, args.order,
                                  data["train_inputs"], data["train_labels"],
                                  lifted=False, **common)


def source_hashes():
    folder = Path(__file__).parent
    return {name: sha256(folder/name) for name in
            ("mnist_moment_run.py", "moment_engine.py", "orthogonal_moment_engine.py")}


def run(args):
    process_start = time.monotonic()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(args.threads)
    torch.set_default_dtype(torch.float64)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    data = load_dataset(args.dataset)
    if torch.device(args.device).type == "cuda":
        torch.cuda.set_device(torch.device(args.device))
        torch.cuda.reset_peak_memory_stats(args.device)
    setup_start = time.monotonic()
    engine = make_engine(args, data)
    state = engine.initial_state()
    synchronize(args.device)
    initialization_seconds = time.monotonic()-setup_start
    dataset_hash = sha256(args.dataset)
    hashes = source_hashes()
    initial_arrays = {name: value.detach().cpu().numpy().copy()
                      for name, value in zip(state.names(), state.tensors())
                      if name in ("w", "W", "c")}
    if args.model == "moment":
        initial_arrays["W"] = engine.W0.detach().cpu().numpy().copy()
    initialization_hash = hashlib.sha256()
    for name in ("w", "W", "c"):
        initialization_hash.update(initial_arrays[name].tobytes(order="C"))
    del initial_arrays

    observation_seconds = 0.
    checkpoints = []
    predictions = []
    train_predictions = []
    observation_times = []
    observation_losses = []
    labels = []

    def observe(value, t, loss, label, *, save_state=False):
        nonlocal observation_seconds
        start = time.monotonic()
        train = panel_predict(engine, value, data["train_inputs"], args.validation_block)
        prediction = panel_predict(engine, value, data["validation_inputs"], args.validation_block)
        train_predictions.append(train)
        predictions.append(prediction)
        observation_times.append(t)
        observation_losses.append(loss)
        labels.append(label)
        if save_state:
            name = "checkpoint_" + label.replace(".", "p") + ".npz"
            payload = {key: tensor.detach().cpu().numpy()
                       for key, tensor in zip(value.names(), value.tensors())}
            if args.model == "moment":
                payload["W0"] = engine.W0.detach().cpu().numpy()
            np.savez(out/name, **payload, physical_time=np.array(t))
            checkpoints.append(name)
        synchronize(args.device)
        observation_seconds += time.monotonic()-start

    t, step = 0., args.initial_step
    current_loss = training_loss(engine, state)
    times, losses, steps, errors = [t], [current_loss], [], []
    rejected = loss_increases = 0
    thresholds = sorted(set(args.loss_crossings + [args.target_loss]), reverse=True)
    crossed = {value for value in thresholds if current_loss <= value}
    observe(state, t, current_loss, "initial")
    initial_observation_seconds = observation_seconds
    start = last_report = time.monotonic()
    status = "running"
    error_message = None
    while True:
        elapsed = time.monotonic()-start
        if current_loss <= args.target_loss*(1+1e-8):
            status = "target_loss"; break
        if elapsed >= args.wall_seconds:
            status = "wall_limit"; break
        if t >= args.max_time:
            status = "max_time"; break
        if len(steps) >= args.max_steps:
            status = "max_steps"; break
        proposed = min(step, args.max_step, args.max_time-t)
        if proposed < 1e-12*max(1., t):
            status = "step_underflow"; break
        try:
            first, second, euler, candidate = heun_trial(engine, state, proposed)
            engine.validate_state(candidate)
            error = component_error(state, euler, candidate, args.rtol, args.atol)
            candidate_loss = training_loss(engine, candidate)
            valid = math.isfinite(error) and math.isfinite(candidate_loss)
        except (ValueError, FloatingPointError) as exc:
            error, valid = float("inf"), False
            error_message = str(exc)
        if not valid or error > 1:
            rejected += 1
            step = proposed*(max(.1, min(.5, .9/math.sqrt(error)))
                             if math.isfinite(error) else .1)
        else:
            actual_step = proposed
            for threshold in thresholds:
                if threshold in crossed or not candidate_loss <= threshold < current_loss:
                    continue
                fraction, event_state, event_loss = locate_loss_crossing(
                    engine, state, first, second, proposed, threshold)
                event_time = t+fraction*proposed
                observe(event_state, event_time, event_loss, "loss_"+format(threshold, ".12g"),
                        save_state=True)
                crossed.add(threshold)
                if threshold == args.target_loss:
                    candidate, candidate_loss = event_state, event_loss
                    actual_step = fraction*proposed
                    break
            loss_increases += int(candidate_loss > current_loss+1e-12)
            state, current_loss = candidate, candidate_loss
            t += actual_step
            times.append(t); losses.append(current_loss)
            steps.append(actual_step); errors.append(error)
            step = proposed*max(.5, min(2., .9/math.sqrt(max(error, 1e-16))))
        if time.monotonic()-last_report >= 30:
            synchronize(args.device)
            print(json.dumps(dict(event="progress", model=args.model, P=args.order,
                                  width=args.width, time=t, training_mse=current_loss,
                                  accepted=len(steps), rejected=rejected,
                                  wall_seconds=time.monotonic()-start)), flush=True)
            last_report = time.monotonic()
    synchronize(args.device)
    integration_with_observations_seconds = time.monotonic()-start
    observations_before_final = observation_seconds
    observe(state, t, current_loss, "final")
    arrays = {name: value.detach().cpu().numpy()
              for name, value in zip(state.names(), state.tensors())}
    if args.model == "moment":
        arrays["W0"] = engine.W0.detach().cpu().numpy()
    arrays.update(times=np.asarray(times), losses=np.asarray(losses),
                  accepted_steps=np.asarray(steps), local_error_ratios=np.asarray(errors),
                  observation_times=np.asarray(observation_times),
                  observation_training_mse=np.asarray(observation_losses),
                  observation_labels=np.asarray(labels),
                  validation_predictions=np.asarray(predictions),
                  train_predictions=np.asarray(train_predictions),
                  validation_labels=data["validation_labels"],
                  train_labels=data["train_labels"])
    for name in ("train_ids", "validation_ids"):
        if name in data:
            arrays[name] = data[name]
    np.savez(out/"arrays.npz", **arrays)
    device = torch.device(args.device)
    moving_bytes = sum(value.numel()*value.element_size() for value in state.tensors())
    summary = dict(
        model=args.model, P=args.order if args.model == "moment" else None,
        width=args.width, d=engine.d, sample_count=engine.M,
        validation_count=len(data["validation_labels"]), dtype="float64",
        device=str(device), seed=args.seed, status=status, time=t,
        training_mse=current_loss, target_loss=args.target_loss,
        crossed_losses=sorted(crossed, reverse=True), accepted=len(steps),
        rejected=rejected, loss_increases=loss_increases, rtol=args.rtol,
        atol=args.atol, maximum_step=args.max_step, initial_step=args.initial_step,
        max_time=args.max_time, max_steps=args.max_steps,
        wall_limit_seconds=args.wall_seconds,
        initialization_seconds=initialization_seconds,
        integration_with_observations_seconds=integration_with_observations_seconds,
        observation_seconds=observation_seconds,
        integration_seconds_excluding_observations=(integration_with_observations_seconds
                                                   - observations_before_final
                                                   + initial_observation_seconds),
        moving_state_bytes=moving_bytes,
        fixed_W0_bytes=engine.W0.numel()*engine.W0.element_size() if args.model == "moment" else 0,
        initialization_hash=initialization_hash.hexdigest(),
        peak_process_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
        peak_cuda_allocated_bytes=torch.cuda.max_memory_allocated(device) if device.type == "cuda" else 0,
        peak_cuda_reserved_bytes=torch.cuda.max_memory_reserved(device) if device.type == "cuda" else 0,
        dataset=str(Path(args.dataset).resolve()), dataset_sha256=dataset_hash,
        source_sha256=hashes, checkpoints=checkpoints,
        software=dict(python=sys.version, numpy=np.__version__, torch=torch.__version__,
                      cuda=torch.version.cuda, threads=args.threads),
        command=sys.argv,
        error_control="max component RMS / (atol + rtol*max(1,RMS(current),RMS(candidate)))",
        endpoint_method="32 bisections of accepted quadratic Heun continuous extension",
        closure_mode="direct_tanh" if args.model == "moment" else None,
        last_rejected_stage_error=error_message,
        arrays_sha256=sha256(out/"arrays.npz"),
    )
    if args.model == "moment":
        summary.update(history_rank_bound=args.order*engine.M,
                       history_scalars=2*args.order*engine.n*engine.M,
                       activity=scalar(state.s),
                       C_minus_L_max=scalar((state.C-state.s-1).abs().max()))
    summary["total_work_seconds"] = time.monotonic()-process_start
    (out/"summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(dict(event="complete", **summary)), flush=True)
    return summary


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--dataset", required=True)
    result.add_argument("--out", required=True)
    result.add_argument("--model", choices=("dense", "moment"), required=True)
    result.add_argument("--order", type=int, choices=(1, 2, 3), default=1)
    result.add_argument("--width", type=int, default=512)
    result.add_argument("--seed", type=int, default=20260924)
    result.add_argument("--device", default="cpu")
    result.add_argument("--threads", type=int, default=1)
    result.add_argument("--rtol", type=float, default=2e-4)
    result.add_argument("--atol", type=float)
    result.add_argument("--initial-step", type=float, default=.05)
    result.add_argument("--max-step", type=float, default=2.)
    result.add_argument("--target-loss", type=float, default=.001)
    result.add_argument("--loss-crossings", nargs="+", type=float, default=[.1, .03, .01, .003, .001])
    result.add_argument("--max-time", type=float, default=10000.)
    result.add_argument("--wall-seconds", type=float, default=600.)
    result.add_argument("--max-steps", type=int, default=30000)
    result.add_argument("--validation-block", type=int, default=256)
    return result


def main():
    args = parser().parse_args()
    if args.atol is None:
        args.atol = args.rtol*.01
    positive = (args.width, args.threads, args.rtol, args.atol, args.initial_step,
                args.max_step, args.target_loss, args.max_time, args.wall_seconds,
                args.max_steps, args.validation_block, *args.loss_crossings)
    if not all(math.isfinite(value) and value > 0 for value in positive) or args.seed < 0:
        raise ValueError("all numerical controls must be positive; seed nonnegative")
    run(args)


if __name__ == "__main__":
    main()
