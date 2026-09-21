#!/usr/bin/env python3
"""Bounded full-batch physical-mobility GD, with scalar Armijo backtracking.

Canonical coordinates are W, middle=A/M, c.  Every accepted update is exactly
theta_new = theta - eta * (n*grad_W, grad_middle, n*grad_c), using one old state.
There is no optimizer, momentum, clipping, readout solve, or Heun stage.
Imports and common Torch setup precede each initialization/training/export clock.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import math
import os
from pathlib import Path
import platform
import resource
import signal
import sys
import time
import traceback

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import numpy as np
import torch

from fit_benchmark import (ROOT, STUDY, SOURCE_PATHS as FIT_SOURCE_PATHS,
                           build_finite_closure, circle_dataset, configure_torch,
                           finite_json, scores, sha256, write_json)
from pde.finite_network import Parameters, forward, gd_step, initialize
from pde.finite_torch import NetworkEngine
from pde.observable_torch_p1 import ClosureEngine

SOURCE_PATHS = (Path(__file__).resolve(),) + FIT_SOURCE_PATHS


@dataclasses.dataclass(frozen=True)
class Config:
    model: str
    m: int
    seed: int
    width: int | None = None
    gain: str = "primary"
    eta_max: float = 1.0
    max_accepted_steps: int = 30000
    max_forward_evals: int = 90000
    max_physical_clock: float = 10000.0
    max_seconds: float = 75.0
    export_reserve_seconds: float = 5.0
    fit_mse: float = .001
    armijo: float = 1e-4
    armijo_slack: float = 1e-14
    max_halvings: int = 30
    gradient_floor: float = 1e-28
    threads: int = 1
    device: str = "cuda:0"
    circle_points: int = 8192

    def resolved(self):
        c = dataclasses.replace(self, width=self.width if self.width is not None else
                                (55 if self.model == "network" else 1024))
        if c.model not in ("network", "closure"):
            raise ValueError("model must be network or closure")
        if c.m not in (30, 62, 126, 254) or c.seed not in (20260921, 20260922, 20260923):
            raise ValueError("m/seed outside frozen design")
        if type(c.width) is not int or c.width not in ((55, 105) if c.model == "network" else (1024,)):
            raise ValueError("network width must be 55/105; closure width must be 1024")
        if c.gain not in ("primary", "rescue") or c.eta_max not in (.5, 1.):
            raise ValueError("gain must be primary/rescue; eta_max must be 1 or .5")
        for key, upper in (("max_accepted_steps", 30000), ("max_forward_evals", 90000)):
            if type(getattr(c, key)) is not int or not 1 <= getattr(c, key) <= upper:
                raise ValueError(f"invalid bounded cap {key}")
        if not (0 < c.max_seconds <= 75 and 0 < c.export_reserve_seconds < c.max_seconds
                and 0 < c.max_physical_clock <= 10000):
            raise ValueError("invalid time/physical-clock cap or export reserve")
        if (c.fit_mse != .001 or c.armijo != 1e-4 or c.armijo_slack != 1e-14
                or c.max_halvings != 30 or c.gradient_floor != 1e-28):
            raise ValueError("fit/Armijo/gradient-floor constants are frozen")
        if c.threads != 1 or not c.device.startswith("cuda:") or c.circle_points != 8192:
            raise ValueError("requires explicit cuda:N, one CPU thread, and 8192 circle points")
        return c


@dataclasses.dataclass(frozen=True)
class State:
    W: torch.Tensor
    middle: torch.Tensor
    c: torch.Tensor

    def arrays(self, kind):
        return {k: t.detach().cpu().numpy().copy() for k, t in
                (("W", self.W), ("A" if kind == "network" else "M", self.middle), ("c", self.c))}


class GDModel:
    """Stateless analytic contractions; state tensors are never edited in place."""
    def __init__(self, kind, n, B1=None, B2=None, *, device="cpu"):
        self.kind, self.n, self.device = kind, n, torch.device(device)
        self.B1 = None if B1 is None else torch.tensor(B1, device=device, dtype=torch.float64)
        self.B2 = None if B2 is None else torch.tensor(B2, device=device, dtype=torch.float64)

    def state(self, W, middle, c):
        return State(*(torch.tensor(x, device=self.device, dtype=torch.float64) for x in (W, middle, c)))

    @torch.no_grad()
    def fields(self, state, u):
        h1 = torch.tanh(state.W @ u.T)
        a = h1 if self.kind == "network" else self.B1.T @ h1 / self.n
        z2 = state.middle @ a
        if self.kind == "closure":
            z2 = self.B2 @ z2
        h2 = torch.tanh(z2)
        prediction = state.c @ h2 / self.n
        return h1, a, h2, prediction

    @torch.no_grad()
    def gradients(self, state, u, y, fields):
        h1, a, h2, prediction = fields
        residual = (2. / len(y)) * (prediction - y)
        gc = h2 @ residual / self.n
        d2 = (state.c[:, None] / self.n) * (1 - h2.square()) * residual
        d = d2 if self.kind == "network" else self.B2.T @ d2
        gm = d @ a.T
        d1 = state.middle.T @ d
        if self.kind == "closure":
            d1 = self.B1 @ d1 / self.n
        gw = ((1 - h1.square()) * d1) @ u
        return State(gw, gm, gc)

    @torch.no_grad()
    def step(self, state, gradients, eta):
        # Each right-hand side reads only the same pre-update state and gradient.
        return State(state.W - (eta * self.n) * gradients.W,
                     state.middle - eta * gradients.middle,
                     state.c - (eta * self.n) * gradients.c)

    def gradient_metrics(self, gradients):
        squares = torch.stack([x.square().sum() for x in (gradients.W, gradients.middle, gradients.c)])
        w, middle, c = squares.cpu().tolist()
        return dict(canonical_blocks={"W": math.sqrt(w), "A" if self.kind == "network" else "M": math.sqrt(middle),
                                     "c": math.sqrt(c)},
                    canonical_norm=math.sqrt(w + middle + c), physical_Q=self.n * w + middle + self.n * c)


def state_finite(state):
    return all(bool(torch.isfinite(x).all()) for x in (state.W, state.middle, state.c))


def environment_record():
    return dict(python=sys.version, numpy=np.__version__, torch=str(torch.__version__),
                platform=platform.platform(), machine=platform.machine(), processor=platform.processor(),
                torch_threads=torch.get_num_threads(), torch_interop_threads=torch.get_num_interop_threads(),
                deterministic_algorithms=torch.are_deterministic_algorithms_enabled(),
                tf32=torch.backends.cuda.matmul.allow_tf32, cudnn_tf32=torch.backends.cudnn.allow_tf32,
                cpu_affinity=sorted(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None,
                thread_environment={k: os.environ.get(k) for k in
                    ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "CUBLAS_WORKSPACE_CONFIG")},
                source_sha256={str(p.relative_to(ROOT)): sha256(p) for p in SOURCE_PATHS})


def oracle_prediction(model, state, u):
    a = state.arrays(model.kind)
    if model.kind == "network":
        return forward(Parameters((a["W"], a["A"]), a["c"]), (u * np.sqrt(2)).T).output
    engine = ClosureEngine(model.B1.cpu().numpy(), a["W"], model.B2.cpu().numpy(), a["M"], block_size=512)
    return engine.predict(engine.state(a["W"], a["c"], a["M"]), u).numpy()


@torch.no_grad()
def evaluate_saved(model, state, dataset):
    u, y = (torch.tensor(dataset[key], device=model.device) for key in ("u", "y"))
    fields = model.fields(state, u)
    prediction = fields[-1].cpu().numpy().copy()
    diagnostics = scores(prediction, dataset["y"])
    diagnostics["gradient"] = model.gradient_metrics(model.gradients(state, u, y, fields))
    diagnostics["parameter_norms"] = {k: float(np.linalg.norm(v)) for k, v in state.arrays(model.kind).items()}
    diagnostics["saturation"] = {f"layer{j}":
        {"abs_activation_ge_0.99_fraction": float((h.abs() >= .99).double().mean()),
         "rounded_abs_activation_eq_1_fraction": float((h.abs() == 1).double().mean())}
        for j, h in ((1, fields[0]), (2, fields[2]))}
    circle = torch.cat([model.fields(state, torch.tensor(dataset["circle_u"][i:i + 512], device=model.device))[-1]
                        for i in range(0, len(dataset["circle_u"]), 512)]).cpu().numpy()
    oracle = oracle_prediction(model, state, dataset["u"])
    forward_error = float(np.max(np.abs(prediction - oracle)))
    loss_error = abs(diagnostics["mse"] - float(np.mean((oracle - dataset["y"]) ** 2)))
    diagnostics.update(maintained_oracle_max_abs_error=forward_error,
                       maintained_oracle_loss_abs_error=loss_error,
                       maintained_oracle_pass=forward_error <= 1e-8 and loss_error <= 1e-9)
    return prediction, circle, diagnostics


class AttemptStop(Exception):
    def __init__(self, status, detail):
        self.status, self.detail = status, detail
        super().__init__(detail)


@torch.no_grad()
def run_attempt(config, output, provenance=None):
    """Only the caller owns authorization, campaign branches, and worker caps."""
    config = config.resolved()
    output = Path(output).resolve()
    if not output.is_relative_to((ROOT / "data/generated" / STUDY).resolve()):
        raise ValueError("outputs must be inside this study's generated-data directory")
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    train_deadline = started + config.max_seconds - config.export_reserve_seconds
    record = dict(format="alternating-circle-physical-gd-v1", config=dataclasses.asdict(config),
        provenance=provenance or {}, command=sys.argv, working_directory=os.getcwd(), status="initializing",
        optimizer="plain full-batch simultaneous GD with one scalar Armijo step",
        optimizer_coordinates="canonical W,middle=A/M,c", block_mobilities=[config.width, 1, config.width],
        loss="unhalved uniform mean squared error", fit_rule="MSE <= .001 AND zero sign errors; sign(0)=0",
        best_rule="minimum finite objective among initialization and accepted completed GD states only",
        derivative="1-tanh(z)^2; float64 Torch convention including rounded saturation",
        armijo_rule="Ltrial <= L - armijo*eta*Q + armijo_slack*max(1,L)",
        Q="n*||grad_W||^2 + ||grad_middle||^2 + n*||grad_c||^2",
        eta_rule="first eta_max; next min(eta_max,2*last_accepted); cap by remaining physical clock; halve on rejection",
        forward_evaluation_scope="initial training forward plus all line-search trial forwards; export/replay excluded",
        clock_scope="per-attempt dataset/initialization/training/export; imports/shared Torch setup excluded",
        clock_limit_is_supervised=True, started_unix_seconds=time.time(), environment=environment_record())
    write_json(output / "record.json", record)
    trace, pairs = [], {}
    phases = {}
    current = initial_state = best_state = model = dataset = None
    best_loss = float("inf")
    accepted = forwards = rejected_total = nonfinite_trials = 0
    physical_clock = 0.
    last_eta = None
    latest_pair = None
    requested_stop = None
    active_search = None
    training_started = None
    old_handlers = {s: signal.getsignal(s) for s in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT)}

    def stop_handler(signum, frame):
        nonlocal requested_stop
        requested_stop = ("time_limit" if signum == signal.SIGALRM else "interrupted", signal.Signals(signum).name)

    def check_time():
        if requested_stop is not None:
            raise AttemptStop(*requested_stop)
        if time.perf_counter() >= train_deadline:
            raise AttemptStop("time_limit", "training reserve reached; exporting completed states")

    def evaluate_trial(state):
        nonlocal forwards
        check_time()
        if forwards >= config.max_forward_evals:
            raise AttemptStop("evaluation_limit", "full-batch training forward evaluation cap reached")
        forwards += 1
        fields = model.fields(state, u)
        value = float(torch.mean((fields[-1] - y).square()))
        return fields, value

    try:
        for sig in old_handlers:
            signal.signal(sig, stop_handler)
        signal.setitimer(signal.ITIMER_REAL, max(.001, train_deadline - time.perf_counter()))
        dataset = circle_dataset(config.m, config.circle_points)
        np.savez(output / "dataset.npz", **dataset)
        initial = initialize(config.width, 2, 2, seed=config.seed)
        gain = 1. if config.gain == "primary" else config.m / 2
        W, A, c = initial.weights[0] * gain, initial.weights[1], initial.readout
        record["first_weight_gain"] = gain
        if config.model == "network":
            model = GDModel("network", config.width, device=config.device)
            current = model.state(W, A, c)
            np.savez(output / "initial.npz", W=W, A=A, c=c)
        else:
            closure, record["closure"] = build_finite_closure(W, A)
            model = GDModel("closure", config.width, closure["B1"], closure["B2"], device=config.device)
            current = model.state(W, closure["D"], c)
            np.savez(output / "initial.npz", W=W, c=c, M=closure["D"], A_source=A, **closure)
            del closure
        del initial, W, A, c
        initial_state = current
        torch.cuda.synchronize(model.device)
        u, y = (torch.tensor(dataset[key], device=model.device) for key in ("u", "y"))
        phases["initialization_seconds"] = time.perf_counter() - started
        training_started = time.perf_counter()
        fields, value = evaluate_trial(current)
        if not math.isfinite(value) or not state_finite(current):
            raise AttemptStop("nonfinite", "initial state or objective is nonfinite")
        best_state, best_loss = current, value
        signs = int(torch.count_nonzero(torch.sign(fields[-1]) != y))
        trace.append(dict(accepted_step=0, phase="initial", mse=value, sign_errors=signs,
                          physical_clock=0., forward_evaluations=forwards, elapsed_seconds=time.perf_counter() - started))
        while True:
            if value <= config.fit_mse and signs == 0:
                raise AttemptStop("fit_reached", "registered fit criterion reached by an accepted GD state")
            check_time()
            if accepted >= config.max_accepted_steps:
                raise AttemptStop("step_limit", "accepted GD step cap reached")
            if physical_clock >= config.max_physical_clock:
                raise AttemptStop("physical_clock_limit", "sum of accepted scalar GD steps reached its cap")
            gradients = model.gradients(current, u, y, fields)
            metrics = model.gradient_metrics(gradients)
            Q = metrics["physical_Q"]
            if not math.isfinite(Q):
                raise AttemptStop("nonfinite", "gradient or physical descent norm is nonfinite")
            if Q < config.gradient_floor:
                raise AttemptStop("gradient_floor", "physical squared gradient norm below numerical floor; no convergence claim")
            eta_first = min(config.eta_max, config.eta_max if last_eta is None else 2 * last_eta,
                            config.max_physical_clock - physical_clock)
            slack = config.armijo_slack * max(1., value)
            previous, previous_loss = current, value
            active_search = dict(next_accepted_step=accepted + 1, eta_first=eta_first,
                                 previous_mse=value, physical_Q=Q, rejected_trials=0)
            for halvings in range(config.max_halvings + 1):
                eta = eta_first * (2. ** -halvings)
                candidate = model.step(previous, gradients, eta)
                candidate_fields, candidate_loss = evaluate_trial(candidate)
                finite = math.isfinite(candidate_loss) and state_finite(candidate)
                threshold = previous_loss - config.armijo * eta * Q + slack
                if finite and candidate_loss <= threshold:
                    # Signals only set a flag. This commit never exposes a trial
                    # candidate as current/best until the finite Armijo test passes.
                    current, fields, value = candidate, candidate_fields, candidate_loss
                    accepted += 1
                    physical_clock += eta
                    last_eta = eta
                    signs = int(torch.count_nonzero(torch.sign(fields[-1]) != y))
                    if value < best_loss:
                        best_state, best_loss = current, value
                    entry = dict(accepted_step=accepted, phase="gd", mse=value, sign_errors=signs,
                        previous_mse=previous_loss, best_mse=best_loss, eta=eta, eta_first=eta_first,
                        halvings=halvings, rejected_trials=halvings, rejected_trials_total=rejected_total,
                        physical_clock=physical_clock, gradient_from_previous=metrics,
                        armijo_threshold=threshold, armijo_roundoff_slack=slack,
                        forward_evaluations=forwards, elapsed_seconds=time.perf_counter() - started)
                    trace.append(entry)
                    latest_pair = (previous, current, entry)
                    if accepted in (1, 10, 100, 1000):
                        pairs[accepted] = latest_pair
                    active_search = None
                    break
                rejected_total += 1
                active_search["rejected_trials"] += 1
                if not finite:
                    nonfinite_trials += 1
                    raise AttemptStop("nonfinite", "nonfinite line-search trial; retained previous completed state")
            else:
                raise AttemptStop("line_search_failed", "all 31 trial scales failed finite Armijo; not a capacity conclusion")
    except AttemptStop as exc:
        record.update(status=exc.status, stop_detail=exc.detail)
    except Exception as exc:
        record.update(status="error", stop_detail=f"{type(exc).__name__}: {exc}", traceback=traceback.format_exc())
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    training_end = time.perf_counter()
    phases["gd_seconds"] = 0. if training_started is None else training_end - training_started
    record.update(accepted_steps=accepted, forward_evaluations=forwards, rejected_trials=rejected_total,
                  nonfinite_rejected_trials=nonfinite_trials, physical_clock=physical_clock,
                  unfinished_line_search=active_search, initialization_and_optimization_seconds=training_end - started,
                  phase_counts={"initialization": int(initial_state is not None), "gd_accepted": accepted,
                                "gd_trial_forwards": max(0, forwards - 1)})
    export_started = time.perf_counter()
    try:
        with (output / "trace.jsonl").open("w") as stream:
            for entry in trace:
                stream.write(json.dumps(finite_json(entry), sort_keys=True, allow_nan=False) + "\n")
        if current is not None and best_state is not None:
            np.savez(output / "final.npz", **current.arrays(config.model))
            np.savez(output / "best.npz", **best_state.arrays(config.model))
            if latest_pair is not None:
                pairs[accepted] = latest_pair
            pair_arrays, pair_records = {}, []
            for index, (step, (before, after, entry)) in enumerate(sorted(pairs.items())):
                prefix = f"pair{index}"
                for side, state in (("before", before), ("after", after)):
                    pair_arrays.update({f"{prefix}_{side}_{k}": v for k, v in state.arrays(config.model).items()})
                pair_records.append(dict(prefix=prefix, **entry))
            pair_arrays["record"] = np.asarray(json.dumps(finite_json(pair_records), allow_nan=False))
            np.savez(output / "gd_step_pairs.npz", **pair_arrays)
            predictions, diagnostics = {}, {}
            for label, state in (("initial", initial_state), ("final", current), ("best", best_state)):
                train, circle, diagnostic = evaluate_saved(model, state, dataset)
                predictions[label + "_train"], predictions[label + "_circle"] = train, circle
                diagnostics[label] = diagnostic
            np.savez(output / "predictions.npz", **predictions)
            record["diagnostics"] = diagnostics
            record["fit"] = bool(diagnostics["best"]["mse"] <= config.fit_mse and diagnostics["best"]["sign_errors"] == 0)
            record["oracle_pass"] = all(d["maintained_oracle_pass"] for d in diagnostics.values())
            record["trainable_scalar_count"] = sum(x.numel() for x in (current.W, current.middle, current.c))
            record["frozen_feature_scalar_count"] = 0 if config.model == "network" else model.B1.numel() + model.B2.numel()
            record["saved_step_pairs"] = [r["accepted_step"] for r in pair_records]
            record["export_train_forwards"] = 3
            record["export_circle_block_forwards"] = 3 * math.ceil(config.circle_points / 512)
            record["export_maintained_train_replays"] = 3
    except Exception as exc:
        record.update(export_error=f"{type(exc).__name__}: {exc}", export_traceback=traceback.format_exc())
    record["outputs_sha256"] = {p.name: sha256(p) for p in sorted(output.iterdir()) if p.name != "record.json"}
    phases["export_seconds"] = time.perf_counter() - export_started
    record["phase_times"] = phases
    record["peak_process_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    if torch.cuda.is_initialized():
        record["peak_cuda_allocated_bytes"] = torch.cuda.max_memory_allocated(config.device)
        record["peak_cuda_reserved_bytes"] = torch.cuda.max_memory_reserved(config.device)
        record["cuda_name"] = torch.cuda.get_device_name(config.device)
    record["rss_scope"] = "process lifetime including imports and previous attempts in worker"
    record["elapsed_seconds_before_final_record_write"] = time.perf_counter() - started
    record["budget_overrun_seconds"] = max(0., record["elapsed_seconds_before_final_record_write"] - config.max_seconds)
    record["budget_respected"] = record["budget_overrun_seconds"] == 0
    record["numerical_valid"] = bool(record.get("oracle_pass") and "export_error" not in record
        and record["status"] not in ("error", "nonfinite", "line_search_failed", "interrupted")
        and record["nonfinite_rejected_trials"] == 0)
    write_json(output / "record.json", finite_json(record))
    for sig, handler in old_handlers.items():
        signal.signal(sig, handler)
    return record


def preflight(output):
    """Small CPU algebra/one-step checks only; no fit attempt or training loop."""
    output = Path(output).resolve()
    allowed = (ROOT / "data/generated" / STUDY / "producer_scratch").resolve()
    if not output.is_relative_to(allowed):
        raise ValueError("preflight must use producer_scratch")
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    results = dict(training_performed=False, checks={}, environment=environment_record())
    data = circle_dataset(6, 16)
    init = initialize(7, 2, 2, seed=31)
    W, A, c = init.weights[0], init.weights[1], init.readout
    closure, _ = build_finite_closure(W, A)
    u, y = torch.tensor(data["u"]), torch.tensor(data["y"])
    for kind in ("network", "closure"):
        model = GDModel(kind, 7, closure["B1"], closure["B2"])
        state = model.state(W, A if kind == "network" else closure["D"], c)
        fields = model.fields(state, u)
        grad = model.gradients(state, u, y, fields)
        tensors = tuple(x.clone().requires_grad_() for x in (state.W, state.middle, state.c))
        def objective(w, middle, readout):
            h1 = torch.tanh(w @ u.T)
            a = h1 if kind == "network" else model.B1.T @ h1 / model.n
            z = middle @ a
            if kind == "closure":
                z = model.B2 @ z
            return ((readout @ torch.tanh(z) / model.n - y).square()).mean()
        ag = torch.autograd.grad(objective(*tensors), tensors)
        gradient_errors = {}
        for name, actual, expected in zip(("W", "middle", "c"), (grad.W, grad.middle, grad.c), ag):
            torch.testing.assert_close(actual, expected, rtol=2e-11, atol=2e-13)
            gradient_errors[name] = float((actual - expected).abs().max())
        gradcheck = torch.autograd.gradcheck(objective, tensors, eps=1e-6, atol=2e-7, rtol=2e-5)
        engine = NetworkEngine(2, 7, 31) if kind == "network" else ClosureEngine(
            closure["B1"], W, closure["B2"], closure["D"])
        maintained = engine.state(W, c, state.middle.numpy())
        prepared = engine.prepare_data(data["u"], data["y"])
        velocity = engine.rhs(maintained, prepared)
        expected_prediction = engine.predict(maintained, u)
        torch.testing.assert_close(fields[-1], expected_prediction, rtol=2e-12, atol=2e-13)
        eta = .25
        step = model.step(state, grad, eta)
        step_errors = {}
        for name, after, before, v in (("W", step.W, state.W, velocity.w),
                                     ("middle", step.middle, state.middle, velocity.M),
                                     ("c", step.c, state.c, velocity.c)):
            torch.testing.assert_close(after, before + eta * v, rtol=2e-11, atol=2e-13)
            step_errors[name] = float((after - (before + eta * v)).abs().max())
        if kind == "network":
            numpy_step = gd_step(init, data["x"].T, data["y"], eta)
            for actual, expected in ((step.W.numpy(), numpy_step.weights[0]),
                                     (step.middle.numpy(), numpy_step.weights[1]),
                                     (step.c.numpy(), numpy_step.readout)):
                np.testing.assert_allclose(actual, expected, rtol=2e-11, atol=2e-13)
        L = float((fields[-1] - y).square().mean())
        metrics = model.gradient_metrics(grad)
        eps = 1e-5
        plus = model.fields(model.step(state, grad, eps), u)[-1]
        minus = model.fields(model.step(state, grad, -eps), u)[-1]
        derivative = float(((plus - y).square().mean() - (minus - y).square().mean()) / (2 * eps))
        np.testing.assert_allclose(derivative, -metrics["physical_Q"], rtol=2e-6, atol=2e-9)
        trial_loss = float((model.fields(step, u)[-1] - y).square().mean())
        assert trial_loss <= L - 1e-4 * eta * metrics["physical_Q"] + 1e-14 * max(1., L)
        results["checks"][kind] = dict(autograd_gradient_max_abs_errors=gradient_errors,
            finite_difference_gradcheck=bool(gradcheck), maintained_simultaneous_step_errors=step_errors,
            forward_max_abs_error=float((fields[-1] - expected_prediction).abs().max()),
            Q=metrics["physical_Q"], directional_loss_derivative=derivative, one_step_armijo=True,
            numpy_gd_step=(kind == "network"), eta=eta)
    results["elapsed_seconds"] = time.perf_counter() - started
    results["preflight_pass"] = True
    write_json(output / "preflight.json", results)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("preflight")
    check.add_argument("--output", required=True)
    attempt = sub.add_parser("attempt")
    attempt.add_argument("--config", required=True, help="path to explicit JSON Config object")
    attempt.add_argument("--output", required=True)
    attempt.add_argument("--freeze", required=True)
    worker = sub.add_parser("worker")
    worker.add_argument("--manifest", required=True, help="JSON list of {config,output}; no adaptive branches")
    worker.add_argument("--freeze", required=True)
    worker.add_argument("--max-seconds", required=True, type=float)
    worker.add_argument("--worker-record", required=True)
    args = parser.parse_args()
    configure_torch()
    if args.command == "preflight":
        result = preflight(args.output)
        print(json.dumps({"preflight_pass": result["preflight_pass"], "output": str(Path(args.output).resolve())}))
        return 0
    freeze = Path(args.freeze).resolve()
    if not freeze.is_file():
        parser.error("root-owned frozen GD protocol file is required")
    provenance = dict(freeze_path=str(freeze), freeze_sha256=sha256(freeze))
    if args.command == "attempt":
        provenance.update(config_path=str(Path(args.config).resolve()), config_sha256=sha256(args.config))
        result = run_attempt(Config(**json.loads(Path(args.config).read_text())), args.output, provenance)
        print(json.dumps({k: result.get(k) for k in ("status", "fit", "numerical_valid", "budget_respected",
                                                  "accepted_steps", "elapsed_seconds_before_final_record_write")}))
        return 0 if result["numerical_valid"] and result["budget_respected"] else 1
    entries = json.loads(Path(args.manifest).read_text())
    if not isinstance(entries, list) or not math.isfinite(args.max_seconds) or args.max_seconds <= 0:
        parser.error("manifest must be explicit list; worker cap must be positive")
    provenance.update(manifest_path=str(Path(args.manifest).resolve()), manifest_sha256=sha256(args.manifest))
    worker_path = Path(args.worker_record).resolve()
    if not worker_path.is_relative_to((ROOT / "data/generated" / STUDY).resolve()) or worker_path.exists():
        parser.error("worker record must be fresh and study-owned")
    configs = [Config(**entry["config"]).resolved() for entry in entries]
    started = time.perf_counter()
    report = dict(manifest=provenance, max_seconds=args.max_seconds, attempts=[], status="running")
    worker_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(worker_path, report)
    for index, (entry, config) in enumerate(zip(entries, configs)):
        if args.max_seconds - (time.perf_counter() - started) < config.max_seconds + 1:
            report.update(status="worker_time_limit", next_unstarted_index=index)
            break
        result = run_attempt(config, entry["output"], provenance | {"manifest_index": index})
        report["attempts"].append({"index": index, "output": str(Path(entry["output"]).resolve()),
            **{k: result.get(k) for k in ("status", "fit", "numerical_valid", "budget_respected", "accepted_steps")}})
        write_json(worker_path, report)
    else:
        report["status"] = "manifest_completed"
    report["elapsed_seconds"] = time.perf_counter() - started
    report["budget_respected"] = report["elapsed_seconds"] <= args.max_seconds
    write_json(worker_path, report)
    print(json.dumps(report))
    return 0 if report["status"] == "manifest_completed" and report["budget_respected"] else 1


if __name__ == "__main__":
    sys.exit(main())
