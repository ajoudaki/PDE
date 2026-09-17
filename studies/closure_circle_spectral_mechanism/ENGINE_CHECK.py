"""Bounded deterministic implementation checks; no scientific training run."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import time

import numpy as np
import torch

from ENGINE import ARRAYS, Closure, initialize, load_npz
from pde.observable_solver import DataLaw, _fields, evolve, initialize as reference_initialize
from pde.observable_solver import paired_observations, rhs


def check(device, output):
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    signal.alarm(120)
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    output.mkdir(parents=True, exist_ok=True)
    started, cpu_started = time.perf_counter(), time.process_time()
    errors, records = {}, []
    def compare(key, actual, expected, exact=False):
        if isinstance(actual, torch.Tensor):
            actual = actual.detach().cpu().numpy()
        if isinstance(expected, torch.Tensor):
            expected = expected.detach().cpu().numpy()
        actual, expected = np.asarray(actual), np.asarray(expected)
        if actual.shape != expected.shape:
            raise AssertionError((key, actual.shape, expected.shape))
        error = float(np.max(np.abs(actual-expected))) if actual.size else 0.0
        errors[key] = max(errors.get(key, 0), error)
        if not np.all(np.isfinite(actual)) or (error != 0 if exact else error > 1e-10):
            raise AssertionError((key, error))

    angles = np.array([0.13, 0.51, 1.37, 2.11])
    u = np.column_stack((np.cos(angles), np.sin(angles)))
    y, p = np.array([-1.0, 0.7, -0.2, 0.8]), np.array([0.1, 0.2, 0.3, 0.4])
    circle_angles = 2*np.pi*np.arange(32)/32
    panel = np.column_stack((np.cos(circle_angles), np.sin(circle_angles)))
    for order in (1, 2, 3, 5):
        reference = reference_initialize(order, initialization_nodes=256, population_nodes=96)
        engine = initialize(order, 256, 96, device)
        for key in ARRAYS:
            compare("initialized_"+key, getattr(engine, key), getattr(reference, key), exact=True)
        # A nonzero readout and moved state make every derivative block active.
        rng = np.random.default_rng(731+order)
        reference.w += 0.03*rng.normal(size=reference.w.shape)
        reference.c += 0.2*rng.normal(size=reference.c.shape)
        reference.M += 0.01*rng.normal(size=reference.M.shape)
        # Exercise the probability metric with genuinely nonuniform populations.
        reference.p1[:] = np.arange(1, 97, dtype=float)/sum(range(1, 97))
        reference.p2[:] = np.arange(96, 0, -1, dtype=float)/sum(range(1, 97))
        engine = Closure({k: getattr(reference, k) for k in ARRAYS}, reference.metadata, device)
        for count in (2, 3, 4):
            data = DataLaw(u[:count], y[:count], p[:count]/p[:count].sum())
            prepared = engine.prepare_data(data.inputs, data.labels, data.probabilities)
            actual, expected = engine.fields(data.inputs), _fields(reference, data.inputs)
            for key in expected:
                compare("fields_"+key, actual[key], expected[key])
            for key, a, b in zip(("w", "c", "M"), engine.rhs(prepared), rhs(reference, data)):
                compare("rhs_"+key, a, b)
            clone = engine.clone().step_data(prepared, 0.013)
            evolved = evolve(reference, data, steps=1, step_size=0.013)
            for key in ARRAYS:
                compare("heun_"+key, getattr(clone, key), getattr(evolved, key))

        data = DataLaw(u, y, p)
        prepared = engine.prepare_data(u, y, p)
        # Independently differentiate the literal output contractions (no engine
        # cached contractions) and use the diagonal inverse probability metric.
        w = engine.w.clone().requires_grad_()
        c = engine.c.clone().requires_grad_()
        M = engine.M.clone().requires_grad_()
        h1 = torch.tanh(w @ prepared.inputs.T)
        a = engine.b1.T @ (engine.p1[:, None]*h1)
        h2 = torch.tanh(engine.b2 @ (M @ a))
        f = engine.p2 @ (c[:, None]*h2)
        jacobians = [[], [], []]
        for index in range(len(u)):
            grads = torch.autograd.grad(f[index], (w, c, M), retain_graph=True)
            for target, grad in zip(jacobians, grads):
                target.append(grad.reshape(-1))
        jacobians = [torch.stack(j) for j in jacobians]
        inverse_metric = (1/engine.p1.repeat_interleave(2), 1/engine.p2,
                          torch.ones(M.numel(), dtype=torch.float64, device=device))
        autograd_blocks = torch.stack([(j*metric) @ j.T for j, metric in zip(jacobians, inverse_metric)])
        compare("tangent_autograd", engine.tangent_blocks(u), autograd_blocks)
        loss = (prepared.probabilities*(f-prepared.labels)**2).sum()
        grads = torch.autograd.grad(loss, (w, c, M))
        metric_grads = (-grads[0]/engine.p1[:, None], -grads[1]/engine.p2, -grads[2])
        for key, actual, expected in zip(("w", "c", "M"), engine.rhs(prepared), metric_grads):
            compare("gradient_metric_"+key, actual, expected)
        velocity = engine.rhs(prepared)
        output_velocity = sum(j @ v.reshape(-1) for j, v in zip(jacobians, velocity))
        predicted_velocity = -2*autograd_blocks.sum(0) @ (prepared.probabilities*(f-prepared.labels))
        compare("output_velocity", output_velocity, predicted_velocity)
        compare("oddness", engine.predict(-u), -engine.predict(u))
        physical_inputs = np.sqrt(2)*u
        compare("normalization", engine.fields(u)["h1"],
                torch.tanh(engine.w @ engine._tensor(physical_inputs).T / np.sqrt(2)))
        try:
            engine.fields(physical_inputs)
        except ValueError:
            pass
        else:
            raise AssertionError("physical inputs must be explicitly normalized")

        stats = engine.diagnostics(panel, u, p)
        pair = paired_observations(reference, data, include_pairs=False)
        for layer in (1, 2):
            compare("paired_motion_"+str(layer), stats[f"hidden{layer}_motion_rms_training"], pair[f"rms{layer}"])
            values = engine.fields(panel, backward=False)[f"h{layer}"]
            population = getattr(engine, "p"+str(layer))
            compare("parseval_"+str(layer), stats[f"hidden{layer}_power_current"].sum(),
                    (population @ (values**2)).mean())
        compare("rectangular_kernel", engine.tangent_blocks(u[:2], u[2:]),
                engine.tangent_blocks(u)[:, :2, 2:])

        checkpoint = output / f"restart_N{order}.npz"
        engine.step_data(prepared, 0.017)
        engine.save_npz(checkpoint, metadata={"purpose": "deterministic restart check"}, data=prepared)
        restored = load_npz(checkpoint, device)
        if restored.metadata != engine.metadata or restored.clock != engine.clock:
            raise AssertionError("restart metadata differs")
        if restored.checkpoint_metadata != {"purpose": "deterministic restart check"}:
            raise AssertionError("restart extra metadata differs")
        for key in ARRAYS:
            compare("restart_exact_"+key, getattr(restored, key), getattr(engine, key), exact=True)
        for _ in range(3):
            engine.step_data(prepared, 0.017)
            restored.step_data(restored.checkpoint_data, 0.017)
        for key in ARRAYS:
            compare("restart_continuation_"+key, getattr(restored, key), getattr(engine, key), exact=True)
        compare("restart_prediction", restored.predict(panel), engine.predict(panel), exact=True)
        records.append(dict(order=order, Q=256, P=96,
                            dimensions=[engine.b1.shape[1], engine.b2.shape[1]],
                            checkpoint_bytes=checkpoint.stat().st_size))
    if torch.device(device).type == "cuda":
        torch.cuda.synchronize()
    report = dict(status="PASS", device=str(device), torch=torch.__version__, numpy=np.__version__,
                  max_absolute_error=max(errors.values()), tolerance=1e-10, errors=errors,
                  checks=records, wall_seconds=time.perf_counter()-started,
                  cpu_seconds=time.process_time()-cpu_started,
                  threads=torch.get_num_threads(), source_sha256={
                      name: hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest()
                      for name in ("ENGINE.py", "ENGINE_CHECK.py")})
    (output/"checks.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[2]/
                        "data/generated/closure_circle_spectral_mechanism/worker_checks/cpu")
    args = parser.parse_args()
    check(args.device, args.output)
