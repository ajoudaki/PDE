#!/usr/bin/env python3
"""Bounded alternating-circle fit attempts, with canonical replay artifacts.

This study driver optimizes W, middle, v=c/n using ordinary Adam and LBFGS.
It does not implement physical gradient flow. A run is an optimization attempt,
and failure to fit is not a representational lower bound. Imports and common
Torch policy setup precede the per-attempt initialization/training/export timer.
Run ``preflight`` for deterministic forward/gradient checks without training.
"""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time
import traceback

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.finite_network import Parameters, forward, initialize
from pde.finite_torch import NetworkEngine
from pde.observable_initialization import build_dictionary
from pde.observable_torch_p1 import ClosureEngine

STUDY = "alternating_circle_fit_capacity_20260921"
SOURCE_PATHS = (
    Path(__file__).resolve(), ROOT / "code/pde/finite_network.py",
    ROOT / "code/pde/finite_torch.py", ROOT / "code/pde/observable_torch_p1.py",
    ROOT / "code/pde/observable_initialization.py", ROOT / "code/pde/observable_words.py",
    ROOT / "docs/NOTATION.md", ROOT / "code/GENERAL_P1.md",
)


@dataclasses.dataclass(frozen=True)
class Config:
    model: str
    m: int
    seed: int
    width: int | None = None
    gain: str = "primary"
    max_seconds: float = 60.0
    adam_steps: int = 8000
    adam_switch: int = 4000
    adam_lr1: float = .01
    adam_lr2: float = .003
    adam_eps: float = 1e-8
    lbfgs_max_iter: int = 1000
    lbfgs_max_eval: int = 2000
    lbfgs_history: int = 50
    lbfgs_tolerance_grad: float = 1e-12
    lbfgs_tolerance_change: float = 1e-14
    fit_mse: float = .001
    threads: int = 1
    device: str = "cuda:0"
    circle_points: int = 8192
    export_reserve_seconds: float = 5.0

    def resolved(self):
        c = dataclasses.replace(self, width=self.width or (55 if self.model == "network" else 1024))
        if c.model not in ("network", "closure"):
            raise ValueError("model must be network or closure")
        if c.m not in (30, 62, 126, 254) or c.seed not in (20260921, 20260922, 20260923):
            raise ValueError("m/seed is outside the frozen candidate design")
        if c.width not in ((55, 105) if c.model == "network" else (1024,)):
            raise ValueError("network width must be 55/105; closure construction width must be 1024")
        if c.gain not in ("primary", "rescue"):
            raise ValueError("gain must be primary or rescue")
        if not (0 < c.max_seconds <= 60 and 0 < c.export_reserve_seconds < c.max_seconds):
            raise ValueError("attempt must reserve export time inside a maximum 60 seconds")
        if c.threads != 1 or not c.device.startswith("cuda:") or c.circle_points != 8192:
            raise ValueError("this training protocol uses explicit cuda:N, one CPU thread, and 8192 circle points")
        integer_fields = ("adam_steps", "adam_switch", "lbfgs_max_iter", "lbfgs_max_eval", "lbfgs_history")
        if any(type(getattr(c, k)) is not int or getattr(c, k) < 1 for k in integer_fields):
            raise ValueError("optimizer iteration/history caps must be positive integers")
        if c.adam_steps > 8000 or c.lbfgs_max_iter > 1000 or c.lbfgs_max_eval > 2000:
            raise ValueError("optimizer caps exceed the registered design")
        for k in ("adam_lr1", "adam_lr2", "adam_eps", "lbfgs_tolerance_grad", "lbfgs_tolerance_change", "fit_mse"):
            if not math.isfinite(getattr(c, k)) or getattr(c, k) <= 0:
                raise ValueError(f"invalid {k}")
        return c


def configure_torch():
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_default_dtype(torch.float64)


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")


def finite_json(value):
    """Represent unavailable/nonfinite diagnostics explicitly, never emit NaN JSON."""
    if isinstance(value, dict):
        return {k: finite_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [finite_json(v) for v in value]
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    return value


def circle_dataset(m, circle_points=8192):
    theta = 2 * np.pi * np.arange(m, dtype=np.float64) / m
    x = np.column_stack((np.cos(theta), np.sin(theta)))
    dense_theta = 2 * np.pi * np.arange(circle_points, dtype=np.float64) / circle_points
    dense_x = np.column_stack((np.cos(dense_theta), np.sin(dense_theta)))
    return dict(theta=theta, x=x, u=x / np.sqrt(2), y=(-1.) ** np.arange(m),
                circle_theta=dense_theta, circle_x=dense_x, circle_u=dense_x / np.sqrt(2))


def word_description(word):
    result = {"op": word.op, "population": word.population}
    if word.scalar is not None:
        result["scalar"] = str(word.scalar)
    if word.args:
        result["args"] = [word_description(arg) for arg in word.args]
    return result


def build_finite_closure(W, A):
    """Evaluate maintained p=1 words with the same finite A and its transpose.

    Source actions have no extra width divisor: A already has variance 1/n.
    Empirical Gram/contraction pairings have exactly one divisor n each.
    """
    n = len(W)
    dictionary = build_dictionary(1)
    cache = {}

    def evaluate(word):
        if word in cache:
            return cache[word]
        op = word.op
        if op == "one":
            value = np.ones(n)
        elif op in ("g1", "g2"):
            value = W[:, int(op[1]) - 1]
        elif op == "action":
            value = (A if word.population == 2 else A.T) @ evaluate(word.args[0])
        elif op in ("tanh", "sin", "cos"):
            value = getattr(np, op)(evaluate(word.args[0]))
        elif op == "scale":
            value = float(word.scalar) * evaluate(word.args[0])
        elif op == "add":
            value = evaluate(word.args[0]) + evaluate(word.args[1])
        elif op == "multiply":
            value = evaluate(word.args[0]) * evaluate(word.args[1])
        else:
            raise ValueError(f"unsupported finite dictionary word {op}")
        cache[word] = value
        return value

    raw1 = np.column_stack([evaluate(word) for word in dictionary.first_words])
    raw2 = np.column_stack([evaluate(word) for word in dictionary.second_words])
    H = np.tanh(W)
    U = np.tanh(A @ H)
    R = np.tanh(A.T @ U)
    manual1, manual2 = np.column_stack((np.ones(n), H, R)), np.column_stack((np.ones(n), U))
    np.testing.assert_allclose(raw1, manual1, rtol=2e-13, atol=2e-13)
    np.testing.assert_allclose(raw2, manual2, rtol=2e-13, atol=2e-13)
    if raw1.shape != (n, 5) or raw2.shape != (n, 3):
        raise AssertionError("p=1 dictionary dimensions changed")
    ridge = 1 / 4096
    L1 = np.linalg.cholesky(raw1.T @ raw1 / n + ridge * np.eye(5))
    L2 = np.linalg.cholesky(raw2.T @ raw2 / n + ridge * np.eye(3))
    B1, B2 = np.linalg.solve(L1, raw1.T).T, np.linalg.solve(L2, raw2.T).T
    D = B2.T @ (A @ B1) / n
    arrays = dict(B1=B1, B2=B2, D=D, rawB1=raw1, rawB2=raw2, L1=L1, L2=L2)
    metadata = dict(dictionary_order=1, K1=5, K2=3, ridge=ridge,
                    normalization="raw @ inverse(L).T; L @ L.T = raw.T @ raw/n + ridge*I",
                    contraction="D = B2.T @ A_source @ B1 / n",
                    source_recipe="H=tanh(W0); U=tanh(A0@H); R=tanh(A0.T@U)",
                    first_words=[word_description(w) for w in dictionary.first_words],
                    second_words=[word_description(w) for w in dictionary.second_words],
                    gram_condition1=float(np.linalg.cond(L1 @ L1.T)),
                    gram_condition2=float(np.linalg.cond(L2 @ L2.T)))
    return arrays, metadata


class FitModel(torch.nn.Module):
    def __init__(self, kind, W, c, middle, B1=None, B2=None):
        super().__init__()
        self.kind, self.n = kind, len(W)
        self.W = torch.nn.Parameter(torch.tensor(W, dtype=torch.float64))
        self.middle = torch.nn.Parameter(torch.tensor(middle, dtype=torch.float64))
        self.v = torch.nn.Parameter(torch.tensor(c / self.n, dtype=torch.float64))
        if kind == "closure":
            self.register_buffer("B1", torch.tensor(B1, dtype=torch.float64))
            self.register_buffer("B2", torch.tensor(B2, dtype=torch.float64))

    def fields(self, u):
        h1 = torch.tanh(self.W @ u.T)
        z2 = self.middle @ h1 if self.kind == "network" else self.B2 @ (self.middle @ (self.B1.T @ h1 / self.n))
        h2 = torch.tanh(z2)
        return h1, h2, self.v @ h2

    def forward(self, u):
        return self.fields(u)[2]

    def snapshot(self):
        return {k: p.detach().clone() for k, p in self.named_parameters()}

    @torch.no_grad()
    def restore(self, state):
        for k, p in self.named_parameters():
            p.copy_(state[k])

    def canonical(self):
        return dict(W=self.W.detach().cpu().numpy().copy(), c=(self.n * self.v).detach().cpu().numpy().copy(),
                    **{("A" if self.kind == "network" else "M"): self.middle.detach().cpu().numpy().copy()})


class AttemptStop(Exception):
    def __init__(self, status, detail):
        self.status, self.detail = status, detail
        super().__init__(detail)


def scores(prediction, labels):
    return dict(mse=float(np.mean((prediction - labels) ** 2)),
                sign_errors=int(np.count_nonzero(np.sign(prediction) != labels)),
                minimum_signed_margin=float(np.min(labels * prediction)),
                max_abs_error=float(np.max(np.abs(prediction - labels))))


def gradient_metrics(model):
    blocks = {k: float(torch.linalg.vector_norm(p.grad)) for k, p in model.named_parameters() if p.grad is not None}
    canonical = {("c" if k == "v" else "A" if k == "middle" and model.kind == "network" else "M" if k == "middle" else k): (v / model.n if k == "v" else v) for k, v in blocks.items()}
    return dict(optimizer_blocks=blocks, canonical_blocks=canonical,
                optimizer_norm=math.sqrt(sum(v * v for v in blocks.values())),
                canonical_norm=math.sqrt(sum(v * v for v in canonical.values())))


def evaluate_saved(model, state, dataset):
    model.restore(state)
    u, y = torch.tensor(dataset["u"], device=model.W.device), torch.tensor(dataset["y"], device=model.W.device)
    model.zero_grad(set_to_none=True)
    prediction = model(u)
    loss = torch.mean((prediction - y) ** 2)
    loss.backward()
    diagnostics = scores(prediction.detach().cpu().numpy(), dataset["y"])
    diagnostics["gradient"] = gradient_metrics(model)
    diagnostics["parameter_norms"] = {k: float(np.linalg.norm(v)) for k, v in model.canonical().items()}
    with torch.no_grad():
        h1, h2, _ = model.fields(u)
        diagnostics["saturation"] = {f"layer{j}": {"abs_activation_ge_0.99_fraction": float((h.abs() >= .99).double().mean()),
                                                        "rounded_abs_activation_eq_1_fraction": float((h.abs() == 1).double().mean())}
                                     for j, h in ((1, h1), (2, h2))}
        circle = torch.cat([model(torch.tensor(dataset["circle_u"][i:i + 512], device=model.W.device))
                            for i in range(0, len(dataset["circle_u"]), 512)]).cpu().numpy()
    return prediction.detach().cpu().numpy().copy(), circle.copy(), diagnostics


def oracle_prediction(model, u, seed):
    canonical = model.canonical()
    if model.kind == "network":
        return forward(Parameters((canonical["W"], canonical["A"]), canonical["c"]), (u * np.sqrt(2)).T).output
    B1, B2 = model.B1.cpu().numpy(), model.B2.cpu().numpy()
    engine = ClosureEngine(B1, canonical["W"], B2, canonical["M"], block_size=512)
    state = engine.state(canonical["W"], canonical["c"], canonical["M"])
    return engine.predict(state, u).numpy()


def environment_record():
    def git(*args):
        return subprocess.run(["git", "-C", str(ROOT), *args], check=True, text=True, capture_output=True).stdout.strip()
    return dict(python=sys.version, numpy=np.__version__, torch=str(torch.__version__),
                platform=platform.platform(), machine=platform.machine(), processor=platform.processor(),
                torch_threads=torch.get_num_threads(), torch_interop_threads=torch.get_num_interop_threads(),
                deterministic_algorithms=torch.are_deterministic_algorithms_enabled(),
                tf32=torch.backends.cuda.matmul.allow_tf32,
                cpu_affinity=sorted(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None,
                thread_environment={k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "CUBLAS_WORKSPACE_CONFIG")},
                git_head=git("rev-parse", "HEAD"), git_status=git("status", "--porcelain"),
                source_sha256={str(p.relative_to(ROOT)): sha256(p) for p in SOURCE_PATHS})


def run_attempt(config, output, provenance=None):
    """One explicit attempt. The caller/supervisor owns campaign and worker caps."""
    config = config.resolved()
    output = Path(output).resolve()
    allowed = (ROOT / "data/generated" / STUDY).resolve()
    if not output.is_relative_to(allowed):
        raise ValueError(f"outputs must be below {allowed}")
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    train_deadline = started + config.max_seconds - config.export_reserve_seconds
    record = dict(format="alternating-circle-fit-v1", config=dataclasses.asdict(config),
                  provenance=provenance or {}, command=sys.argv, working_directory=os.getcwd(),
                  status="initializing", optimizer_coordinates="W,middle,v=c/n for both models",
                  loss="unhalved uniform mean squared error", fit_rule="MSE <= fit_mse AND zero sign errors; sign(0)=0",
                  clock_scope="per-attempt dataset/initialization/training/export; excludes imports and shared torch setup",
                  clock_limit_is_supervised=True, budget_overrun_seconds=None,
                  started_unix_seconds=time.time(), environment=environment_record())
    write_json(output / "record.json", record)
    trace, best_state, best_loss = [], None, float("inf")
    model = None
    phases = {}
    phase = "initialization"
    adam_completed = lbfgs_evals = 0
    lbfgs = None
    original_handler = signal.getsignal(signal.SIGALRM)

    def alarm_handler(signum, frame):
        raise AttemptStop("time_limit", "training reserve reached; exporting retained checkpoints")

    def check_budget():
        if time.perf_counter() >= train_deadline:
            raise AttemptStop("time_limit", "training reserve reached; exporting retained checkpoints")

    def evaluate(optimizer_step=0):
        nonlocal best_state, best_loss, lbfgs_evals
        check_budget()
        if phase == "lbfgs":
            if lbfgs_evals >= config.lbfgs_max_eval:
                raise AttemptStop("evaluation_limit", "LBFGS closure evaluation limit reached")
            lbfgs_evals += 1
        model.zero_grad(set_to_none=True)
        prediction = model(u)
        loss = torch.mean((prediction - y) ** 2)
        value = float(loss.detach())
        if not math.isfinite(value):
            trace.append(dict(evaluation=len(trace), phase=phase, optimizer_step=optimizer_step,
                              elapsed_seconds=time.perf_counter() - started, mse=None, nonfinite=True))
            raise AttemptStop("nonfinite", "nonfinite objective encountered")
        loss.backward()
        signs = int(torch.count_nonzero(torch.sign(prediction.detach()) != y))
        grad = gradient_metrics(model)
        finite_grad = all(bool(torch.isfinite(p.grad).all()) for p in model.parameters())
        if value < best_loss:
            best_loss, best_state = value, model.snapshot()
        trace.append(dict(evaluation=len(trace), phase=phase, optimizer_step=optimizer_step,
                          elapsed_seconds=time.perf_counter() - started, mse=value, sign_errors=signs,
                          gradient_norm=grad["optimizer_norm"], canonical_gradient_norm=grad["canonical_norm"],
                          best_mse=best_loss, gradient_finite=finite_grad))
        if not finite_grad:
            raise AttemptStop("nonfinite", "nonfinite gradient encountered")
        if value <= config.fit_mse and signs == 0:
            raise AttemptStop("fit_reached", "registered fit criterion reached")
        check_budget()
        return loss

    try:
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, max(.001, train_deadline - time.perf_counter()))
        dataset = circle_dataset(config.m, config.circle_points)
        np.savez(output / "dataset.npz", **dataset)
        initial = initialize(config.width, 2, 2, seed=config.seed)
        W = initial.weights[0].copy() * (1 if config.gain == "primary" else config.m / 2)
        A, c = initial.weights[1], initial.readout
        record["first_weight_gain"] = 1 if config.gain == "primary" else config.m / 2
        if config.model == "network":
            model = FitModel("network", W, c, A)
            np.savez(output / "initial.npz", W=W, c=c, A=A)
        else:
            closure, record["closure"] = build_finite_closure(W, A)
            model = FitModel("closure", W, c, closure["D"], closure["B1"], closure["B2"])
            np.savez(output / "initial.npz", W=W, c=c, M=closure["D"], A_source=A, **closure)
            del closure
        # A_source survives only in the immutable initialization archive for replay.
        del initial, W, A, c
        model.to(config.device)
        torch.cuda.synchronize(model.W.device)
        initial_state = model.snapshot()
        best_state = model.snapshot()
        u, y = torch.tensor(dataset["u"], device=model.W.device), torch.tensor(dataset["y"], device=model.W.device)
        phases["initialization_seconds"] = time.perf_counter() - started
        phase = "initial"
        evaluate()
        phase = "adam"
        phase_started = time.perf_counter()
        adam = torch.optim.Adam(model.parameters(), lr=config.adam_lr1, betas=(.9, .999), eps=config.adam_eps,
                                weight_decay=0, amsgrad=False, foreach=False)
        for step in range(config.adam_steps):
            if step == config.adam_switch:
                for group in adam.param_groups:
                    group["lr"] = config.adam_lr2
            evaluate(step)
            adam.step()
            adam_completed += 1
        # Include the state after the last Adam update in checkpoint selection.
        evaluate(adam_completed)
        phases["adam_seconds"] = time.perf_counter() - phase_started
        del adam
        model.restore(best_state)
        phase = "lbfgs"
        phase_started = time.perf_counter()
        lbfgs = torch.optim.LBFGS(model.parameters(), lr=1, max_iter=config.lbfgs_max_iter,
                    max_eval=config.lbfgs_max_eval, tolerance_grad=config.lbfgs_tolerance_grad,
                    tolerance_change=config.lbfgs_tolerance_change, history_size=config.lbfgs_history,
                    line_search_fn="strong_wolfe")
        lbfgs.step(lambda: evaluate(int(lbfgs.state.get(next(iter(model.parameters())), {}).get("n_iter", 0))))
        phases["lbfgs_seconds"] = time.perf_counter() - phase_started
        phase = "terminal_evaluation"
        evaluate()
        record.update(status="optimizer_terminated", stop_detail="Adam cap completed; LBFGS returned under its declared tolerances/caps")
    except AttemptStop as exc:
        record.update(status=exc.status, stop_detail=exc.detail)
    except Exception as exc:
        record.update(status="error", stop_detail=f"{type(exc).__name__}: {exc}", traceback=traceback.format_exc())
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, original_handler)
    training_end = time.perf_counter()
    record.update(stopping_phase=phase, adam_steps_completed=adam_completed, lbfgs_evaluations=lbfgs_evals,
                  objective_evaluations=len(trace), initialization_and_optimization_seconds=training_end - started)
    if phase in ("adam", "lbfgs"):
        phases[phase + "_seconds"] = training_end - phase_started
    if lbfgs is not None:
        state = lbfgs.state.get(next(iter(model.parameters())), {})
        record["lbfgs_iterations_completed_or_started"] = int(state.get("n_iter", 0))
        record["lbfgs_reported_func_evals"] = int(state.get("func_evals", 0))
    # This last prescribed operation is conditional only on time and not yet
    # satisfying the stopping criterion; it never changes the hidden features.
    record["readout_polish"] = {"status": "not_attempted", "rcond": 1e-12}
    if model is not None and best_state is not None and record["status"] not in ("fit_reached", "error", "nonfinite"):
        polish_started = time.perf_counter()
        optimizer_terminal = model.snapshot()
        np.savez(output / "optimizer_terminal.npz", **model.canonical())
        model.restore(best_state)
        np.savez(output / "pre_polish_best.npz", **model.canonical())
        model.restore(optimizer_terminal)
        if polish_started < started + config.max_seconds - 2:
            try:
                model.restore(best_state)
                with torch.no_grad():
                    h2 = model.fields(u)[1].cpu().numpy()
                solution, _, rank, singular = np.linalg.lstsq(h2.T, dataset["y"], rcond=1e-12)
                with torch.no_grad():
                    model.v.copy_(torch.tensor(solution, device=model.W.device))
                np.savez(output / "polish_candidate.npz", **model.canonical())
                model.zero_grad(set_to_none=True)
                prediction = model(u)
                objective = torch.mean((prediction - y) ** 2)
                objective.backward()
                value = float(objective.detach())
                signs = int(torch.count_nonzero(torch.sign(prediction.detach()) != y))
                grad = gradient_metrics(model)
                accepted = math.isfinite(value) and value < best_loss
                if accepted:
                    best_loss, best_state = value, model.snapshot()
                else:
                    model.restore(optimizer_terminal)
                record["readout_polish"] = dict(status="accepted" if accepted else "not_improved", rcond=1e-12,
                    effective_rank=int(rank), singular_values=singular.tolist(),
                    full_condition=float(singular[0] / singular[-1]) if singular[-1] > 0 else None,
                    retained_condition=float(singular[0] / singular[rank - 1]) if rank else None,
                    optimizer_v_norm=float(np.linalg.norm(solution)), canonical_c_norm=float(model.n * np.linalg.norm(solution)),
                    recomputed_mse=value, sign_errors=signs, elapsed_seconds=time.perf_counter() - polish_started)
                trace.append(dict(evaluation=len(trace), phase="readout_polish", optimizer_step=1,
                    elapsed_seconds=time.perf_counter() - started, mse=value, sign_errors=signs,
                    gradient_norm=grad["optimizer_norm"], canonical_gradient_norm=grad["canonical_norm"],
                    best_mse=best_loss, gradient_finite=all(math.isfinite(v) for v in grad["optimizer_blocks"].values())))
                if accepted and value <= config.fit_mse and signs == 0:
                    record.update(status="fit_reached", stop_detail="registered criterion reached by prescribed linear readout polish", stopping_phase="readout_polish")
            except Exception as exc:
                model.restore(optimizer_terminal)
                record["readout_polish"].update(status="error", detail=f"{type(exc).__name__}: {exc}")
        else:
            record["readout_polish"].update(status="insufficient_export_reserve")
        phases["readout_polish_seconds"] = time.perf_counter() - polish_started
    record["objective_evaluations"] = len(trace)
    export_started = time.perf_counter()
    with (output / "trace.jsonl").open("w") as stream:
        for entry in trace:
            stream.write(json.dumps(finite_json(entry), sort_keys=True, allow_nan=False) + "\n")
    try:
        if model is not None and best_state is not None:
            terminal_state = model.snapshot()
            np.savez(output / "final.npz", **model.canonical())
            model.restore(best_state)
            np.savez(output / "best.npz", **model.canonical())
            predictions, diagnostics = {}, {}
            for label, state in (("initial", initial_state), ("final", terminal_state), ("best", best_state)):
                train, dense, diagnostic = evaluate_saved(model, state, dataset)
                predictions[label + "_train"], predictions[label + "_circle"] = train, dense
                oracle = oracle_prediction(model, dataset["u"], config.seed)
                discrepancy = float(np.max(np.abs(train - oracle)))
                diagnostic["maintained_oracle_max_abs_error"] = discrepancy
                diagnostic["maintained_oracle_pass"] = discrepancy <= 1e-8
                diagnostics[label] = diagnostic
            np.savez(output / "predictions.npz", **predictions)
            record["diagnostics"] = diagnostics
            record["fit"] = bool(diagnostics["best"]["mse"] <= config.fit_mse and diagnostics["best"]["sign_errors"] == 0)
            record["oracle_pass"] = all(d["maintained_oracle_pass"] for d in diagnostics.values())
            record["trainable_scalar_count"] = sum(p.numel() for p in model.parameters())
            record["frozen_feature_scalar_count"] = sum(p.numel() for p in model.buffers())
            record["model_tensor_bytes_excluding_optimizer_and_checkpoints"] = sum(p.numel() * p.element_size() for p in list(model.parameters()) + list(model.buffers()))
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
    record["rss_scope"] = "process lifetime including imports and previous attempts in this worker"
    record["elapsed_seconds_before_final_record_write"] = time.perf_counter() - started
    record["budget_overrun_seconds"] = max(0., record["elapsed_seconds_before_final_record_write"] - config.max_seconds)
    record["budget_respected"] = record["budget_overrun_seconds"] == 0
    record["numerical_valid"] = bool(record.get("oracle_pass") and "export_error" not in record and record["status"] not in ("error", "nonfinite"))
    write_json(output / "record.json", finite_json(record))
    return record


def preflight(output):
    """Tiny deterministic tests only; no optimizer is created and no fit is run."""
    output = Path(output).resolve()
    allowed = (ROOT / "data/generated" / STUDY / "producer_scratch").resolve()
    if not output.is_relative_to(allowed):
        raise ValueError("preflight output must use producer_scratch")
    output.mkdir(parents=True, exist_ok=False)
    results = {"training_performed": False, "checks": {}, "environment": environment_record()}
    dataset = circle_dataset(6, 16)
    initial = initialize(7, 2, 2, seed=31)
    W, A, c = initial.weights[0], initial.weights[1], initial.readout
    closure, metadata = build_finite_closure(W, A)
    results["dictionary"] = metadata
    for kind in ("network", "closure"):
        model = FitModel(kind, W, c, A if kind == "network" else closure["D"], closure["B1"], closure["B2"])
        u, y = torch.tensor(dataset["u"]), torch.tensor(dataset["y"])
        prediction = model(u)
        oracle = oracle_prediction(model, dataset["u"], 31)
        np.testing.assert_allclose(prediction.detach().numpy(), oracle, rtol=2e-13, atol=2e-13)
        engine = (NetworkEngine(2, 7, 31) if kind == "network" else
                  ClosureEngine(closure["B1"], W, closure["B2"], closure["D"]))
        state = engine.state(W, c, model.middle.detach().numpy())
        data = engine.prepare_data(dataset["u"], dataset["y"])
        np.testing.assert_allclose(prediction.detach().numpy(), engine.predict(state, u).numpy(), rtol=2e-13, atol=2e-13)
        loss = torch.mean((prediction - y) ** 2)
        loss.backward()
        velocity = engine.rhs(state, data)
        discrepancies = {}
        for name, target in (("W", -velocity.w / 7), ("middle", -velocity.M), ("v", -velocity.c)):
            actual = getattr(model, name).grad
            torch.testing.assert_close(actual, target, rtol=2e-11, atol=2e-13)
            discrepancies[name] = float((actual - target).abs().max())
        def objective(w, middle, v):
            h = torch.tanh(w @ u.T)
            z = middle @ h if kind == "network" else model.B2 @ (middle @ (model.B1.T @ h / 7))
            return torch.mean((v @ torch.tanh(z) - y) ** 2)
        passed = torch.autograd.gradcheck(objective, (model.W, model.middle, model.v), eps=1e-6, atol=2e-7, rtol=2e-5)
        results["checks"][kind] = dict(forward_max_abs_error=float(np.max(np.abs(prediction.detach().numpy() - oracle))),
                                      gradient_max_abs_errors=discrepancies, finite_difference_gradcheck=passed)
    # Scaling W before compilation must affect all dependent source words.
    rescue, _ = build_finite_closure(3 * W, A)
    np.testing.assert_allclose(rescue["rawB1"][:, 1:3], np.tanh(3 * W), atol=1e-14)
    results["checks"]["gain_before_sources"] = True
    write_json(output / "preflight.json", results)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("preflight")
    check.add_argument("--output", required=True)
    attempt = sub.add_parser("attempt")
    attempt.add_argument("--config", required=True, help="explicit JSON Config object")
    attempt.add_argument("--output", required=True)
    attempt.add_argument("--freeze", required=True, help="root-owned frozen protocol file; recorded with hash")
    worker = sub.add_parser("worker")
    worker.add_argument("--manifest", required=True, help="JSON list of {config,output} entries; no adaptive branches")
    worker.add_argument("--freeze", required=True)
    worker.add_argument("--max-seconds", required=True, type=float)
    worker.add_argument("--worker-record", required=True)
    args = parser.parse_args()
    configure_torch()
    if args.command == "preflight":
        result = preflight(args.output)
        print(json.dumps({"preflight_pass": True, "output": str(Path(args.output).resolve())}))
        return 0
    freeze = Path(args.freeze).resolve()
    if not freeze.is_file():
        parser.error("a root-owned frozen protocol file is required")
    provenance = dict(freeze_path=str(freeze), freeze_sha256=sha256(freeze))
    if args.command == "attempt":
        provenance.update(config_path=str(Path(args.config).resolve()), config_sha256=sha256(args.config))
        result = run_attempt(Config(**json.loads(Path(args.config).read_text())), args.output, provenance)
        print(json.dumps({k: result.get(k) for k in ("status", "fit", "numerical_valid", "budget_respected", "elapsed_seconds_before_final_record_write")}))
        return 0 if result["numerical_valid"] and result["budget_respected"] else 1
    entries = json.loads(Path(args.manifest).read_text())
    if not isinstance(entries, list) or not math.isfinite(args.max_seconds) or args.max_seconds <= 0:
        parser.error("manifest must be an explicit list and worker time cap must be positive")
    provenance.update(manifest_path=str(Path(args.manifest).resolve()), manifest_sha256=sha256(args.manifest))
    worker_path = Path(args.worker_record).resolve()
    if not worker_path.is_relative_to((ROOT / "data/generated" / STUDY).resolve()) or worker_path.exists():
        parser.error("worker record must be a fresh study-generated path")
    configs = [Config(**entry["config"]).resolved() for entry in entries]
    started = time.perf_counter()
    report = dict(manifest=provenance, max_seconds=args.max_seconds, attempts=[], status="running")
    worker_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(worker_path, report)
    for index, (entry, config) in enumerate(zip(entries, configs)):
        remaining = args.max_seconds - (time.perf_counter() - started)
        if remaining < config.max_seconds + 1:
            report.update(status="worker_time_limit", next_unstarted_index=index)
            break
        result = run_attempt(config, entry["output"], provenance | {"manifest_index": index})
        report["attempts"].append({"index": index, "output": str(Path(entry["output"]).resolve()),
                                   **{k: result.get(k) for k in ("status", "fit", "numerical_valid", "budget_respected")}})
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
