#!/usr/bin/env python3
"""Exact two-hidden-layer tanh network for the frozen quadrant experiment.

The physical input is x=sqrt(2)*u, hence z1=A@u. The stored middle
matrix B has no extra forward normalization and f=c@tanh(B@h1)/n.
Heun predictor products use their exact rank-m corrections; no matrix
approximation or persistent low-rank truncation is made.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
import torch


@dataclass
class State:
    a: torch.Tensor
    b: torch.Tensor
    c: torch.Tensor

    @property
    def width(self):
        return self.c.numel()


def derivative(z):
    """Stable tanh derivative, matching the maintained NumPy reference."""
    e = torch.exp(-torch.abs(z))
    return (2 * e / (1 + e * e)).square()


def initialize(width, seed, dtype, device, *, return_hashes=False):
    """PCG64 draws in maintained layer order, float64 before casting.

    Middle-matrix row blocks limit host-memory use without changing the
    generator's draw stream or the elementwise float64 normalization.
    """
    rng = np.random.default_rng(seed)
    raw_a = rng.standard_normal((width, 2))
    block_hashes = {name: hashlib.sha256() for name in ('a', 'b', 'c')}
    combined_hash = hashlib.sha256()
    block_hashes['a'].update(raw_a.tobytes())
    combined_hash.update(raw_a.tobytes())
    a = torch.as_tensor(raw_a, dtype=dtype, device=device)
    b = torch.empty((width, width), dtype=dtype, device=device)
    for start in range(0, width, 512):
        end = min(start + 512, width)
        rows = rng.standard_normal((end - start, width)) / np.sqrt(width)
        block_hashes['b'].update(rows.tobytes())
        combined_hash.update(rows.tobytes())
        b[start:end].copy_(torch.as_tensor(rows, dtype=dtype, device=device))
    raw_c = rng.standard_normal(width) / width
    block_hashes['c'].update(raw_c.tobytes())
    combined_hash.update(raw_c.tobytes())
    c = torch.as_tensor(raw_c, dtype=dtype, device=device)
    state = State(a, b, c)
    if return_hashes:
        hashes = {name: digest.hexdigest() for name, digest in block_hashes.items()}
        hashes['combined_a_b_c'] = combined_hash.hexdigest()
        return state, hashes
    return state


def forward(state, u):
    z1 = state.a @ u
    h1 = torch.tanh(z1)
    z2 = state.b @ h1
    h2 = torch.tanh(z2)
    prediction = state.c @ h2 / state.width
    return prediction, (h1, h2), (z1, z2)


def rhs(state, u, labels, correction=None):
    """Return (A velocity, left B factor, right B factor, c velocity).

    With correction=(step,L,H), the effective middle matrix is
    state.b+step*L@H.T. First/readout arrays must already be predicted.
    """
    z1 = state.a @ u
    h1 = torch.tanh(z1)
    z2 = state.b @ h1
    if correction is not None:
        step, left, right = correction
        z2.add_(left @ (right.T @ h1), alpha=step)
    h2 = torch.tanh(z2)
    residual = state.c @ h2 / state.width - labels
    delta2 = state.c[:, None] * derivative(z2)
    propagated = state.b.T @ delta2
    if correction is not None:
        propagated.add_(right @ (left.T @ delta2), alpha=step)
    delta1 = propagated * derivative(z1)
    scale = -2.0 / labels.numel()
    va = (delta1 * residual) @ u.T * scale
    left = delta2 * residual * (scale / state.width)
    vc = h2 @ residual * scale
    return va, left, h1, vc


def heun_step(state, u, labels, step):
    va, left, right, vc = rhs(state, u, labels)
    predictor = State(state.a + step * va, state.b, state.c + step * vc)
    va2, left2, right2, vc2 = rhs(
        predictor, u, labels, correction=(step, left, right))
    state.a.add_(va + va2, alpha=step / 2)
    state.c.add_(vc + vc2, alpha=step / 2)
    state.b.addmm_(left, right.T, beta=1, alpha=step / 2)
    state.b.addmm_(left2, right2.T, beta=1, alpha=step / 2)


def numpy(tensor):
    return tensor.detach().cpu().numpy()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def sync(device):
    if device.type == 'cuda':
        torch.cuda.synchronize(device)


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + '\n')


def observation(state, panel, labels, initial_hidden):
    prediction, hidden, _ = forward(state, panel)
    m = labels.numel()
    # Scalar RMS/loss reductions use float64; Grams use the dynamics dtype.
    grams = torch.stack([h.T @ h / state.width for h in hidden])
    rms = torch.stack([h[:, :m].double().square().mean().sqrt() for h in hidden])
    movement = torch.stack([
        (h[:, :m].double() - h0.double()).square().mean().sqrt()
        for h, h0 in zip(hidden, initial_hidden)])
    loss = (prediction[:m].double() - labels.double()).square().mean()
    return (float(loss), numpy(prediction), numpy(grams), numpy(rms), numpy(movement))


def validate_inputs(data, step):
    required = ('train_u', 'labels', 'panel_u', 'panel_theta', 'dense_u', 'dense_theta', 'times')
    for key in required:
        if key not in data or not np.isfinite(data[key]).all():
            raise ValueError(f'Missing or nonfinite input {key}')
    train, labels, panel, times = (data[key] for key in ('train_u', 'labels', 'panel_u', 'times'))
    if train.shape != (16, 2) or labels.shape != (16,) or panel.shape != (144, 2):
        raise ValueError('Frozen input shapes are 16 training and 144 panel points in dimension 2')
    if not np.array_equal(panel[:16], train):
        raise ValueError('Panel must start with the exact training inputs')
    if data['panel_theta'].shape != (144,):
        raise ValueError('Panel angles have wrong shape')
    if data['dense_u'].shape != (len(data['dense_theta']), 2):
        raise ValueError('Dense directions and angles have inconsistent shapes')
    if times.ndim != 1 or times[0] != 0 or np.any(np.diff(times) <= 0):
        raise ValueError('Observation times must be strictly increasing from zero')
    indices = np.rint(times / step).astype(np.int64)
    if np.max(np.abs(indices * step - times)) > 1e-10:
        raise ValueError('Every observation must lie on the Heun time mesh')
    if np.any(np.diff(indices) <= 0):
        raise ValueError('Observation indices must increase strictly')
    return indices


@torch.no_grad()
def run(args):
    start = time.monotonic()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name in ('record.json', 'trajectories.npz', 'state.pt'):
        if (out / name).exists():
            raise FileExistsError(f'Refusing to replace {out / name}')
    device = torch.device(args.device)
    dtype = {'float32': torch.float32, 'float64': torch.float64}[args.dtype]
    if args.width < 1 or args.seed < 0 or not math.isfinite(args.step) or args.step <= 0:
        raise ValueError('Width, seed or step is invalid')
    if device.type == 'cuda':
        torch.cuda.set_device(device)
        torch.cuda.reset_peak_memory_stats(device)
    with np.load(args.inputs, allow_pickle=False) as archive:
        data = {key: archive[key].copy() for key in archive.files}
    indices = validate_inputs(data, args.step)
    config = dict(width=args.width, seed=args.seed, step=args.step, dtype=args.dtype,
                  device=str(device), horizon=float(data['times'][-1]),
                  mobilities=[args.width, 1, args.width],
                  input_convention='physical x=sqrt(2)*u; z1=A@u',
                  loss='mean((f-y)^2)', integrator='simultaneous explicit Heun',
                  rng='NumPy PCG64 float64 draws in A,B,c order, cast afterwards',
                  tf32=False)
    record = dict(status='running', config=config, input_sha256=sha256(args.inputs),
                  source_sha256=sha256(__file__),
                  environment=dict(python=sys.version, numpy=np.__version__,
                                   torch=torch.__version__, platform=platform.platform(),
                                   cuda=torch.version.cuda,
                                   gpu=torch.cuda.get_device_name(device) if device.type == 'cuda' else None),
                  command=sys.argv)
    write_json(out / 'record.json', record)
    u = torch.as_tensor(data['train_u'].T.copy(), dtype=dtype, device=device)
    labels = torch.as_tensor(data['labels'], dtype=dtype, device=device)
    panel = torch.as_tensor(data['panel_u'].T.copy(), dtype=dtype, device=device)
    state, init_hashes = initialize(args.width, args.seed, dtype, device, return_hashes=True)
    record['initial_float64_sha256'] = init_hashes
    _, initial_hidden, _ = forward(state, u)
    initial_hidden = tuple(h.clone() for h in initial_hidden)
    sync(device)
    record['initialization_seconds'] = time.monotonic() - start
    values = {key: [] for key in ('loss', 'predictions', 'grams', 'rms', 'movement')}
    current_step = 0
    last_log = time.monotonic()
    for target_step, target_time in zip(indices, data['times']):
        while current_step < target_step:
            heun_step(state, u, labels, args.step)
            current_step += 1
        observed = observation(state, panel, labels, initial_hidden)
        if not all(np.isfinite(value).all() for value in observed):
            record.update(status='failed_nonfinite', completed_time=float(target_time),
                          elapsed_seconds=time.monotonic() - start, finite=False)
            write_json(out / 'record.json', record)
            raise FloatingPointError(f'Nonfinite observation at t={target_time}')
        for key, value in zip(values, observed):
            values[key].append(value)
        if time.monotonic() - last_log > 15 or target_step == indices[-1]:
            print(json.dumps(dict(time=float(target_time), loss=observed[0],
                                  elapsed_seconds=time.monotonic() - start)), flush=True)
            last_log = time.monotonic()
    arrays = {key: np.asarray(value) for key, value in values.items()}
    arrays['times'] = data['times']
    dense_predictions = []
    for begin in range(0, len(data['dense_u']), 256):
        dense = torch.as_tensor(data['dense_u'][begin:begin + 256].T.copy(), dtype=dtype, device=device)
        dense_predictions.append(numpy(forward(state, dense)[0]))
    arrays['dense_predictions'] = np.concatenate(dense_predictions)
    arrays['dense_theta'] = data['dense_theta']
    arrays['panel_theta'] = data['panel_theta']
    finite_state = all(bool(torch.isfinite(t).all()) for t in (state.a, state.b, state.c))
    finite = finite_state and all(np.isfinite(value).all() for value in arrays.values())
    gram_asymmetry = float(np.max(np.abs(arrays['grams'] - arrays['grams'].swapaxes(-1, -2))))
    min_eigenvalue = float(np.linalg.eigvalsh(arrays['grams'].astype(np.float64)).min())
    max_loss_increase = float(np.max(np.diff(arrays['loss'])))
    # Oddness is checked on all 128 passive directions at every saved time.
    circle_prediction = arrays['predictions'][:, 16:]
    odd_error = float(np.max(np.abs(circle_prediction[:, :64] + circle_prediction[:, 64:])))
    checks = dict(finite=finite, max_gram_asymmetry=gram_asymmetry,
                  min_gram_eigenvalue=min_eigenvalue, max_loss_increase=max_loss_increase,
                  max_circle_prediction_oddness_error=odd_error,
                  initial_movement_max=float(np.max(np.abs(arrays['movement'][0]))))
    checks['valid'] = bool(finite and gram_asymmetry <= 1e-5 and min_eigenvalue >= -1e-5
                           and max_loss_increase <= 1e-5 and odd_error <= 1e-5
                           and checks['initial_movement_max'] <= 1e-6)
    np.savez(out / 'trajectories.npz', **arrays)
    torch.save(dict(a=state.a.cpu(), b=state.b.cpu(), c=state.c.cpu(),
                    physical_time=float(data['times'][-1]), completed_steps=current_step,
                    config=config, train_u=data['train_u'], labels=data['labels'],
                    input_sha256=record['input_sha256'], source_sha256=record['source_sha256']),
               out / 'state.pt')
    sync(device)
    record.update(status='complete' if checks['valid'] else 'completed_with_failed_validity_gate',
                  completed_time=float(data['times'][-1]), elapsed_seconds=time.monotonic() - start,
                  finite=finite, checks=checks, saved_observations=len(indices),
                  retained_parameter_bytes=sum(t.numel() * t.element_size() for t in (state.a, state.b, state.c)),
                  peak_cuda_allocated_bytes=torch.cuda.max_memory_allocated(device) if device.type == 'cuda' else 0,
                  output_sha256={name: sha256(out / name) for name in ('trajectories.npz', 'state.pt')})
    write_json(out / 'record.json', record)
    print(json.dumps(record, sort_keys=True), flush=True)


def check(args):
    """Nonzero-state oracle, autograd, full Heun and observable identities."""
    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root / 'code'))
    from pde.finite_network import Parameters, flow_velocity, forward as oracle_forward, kernel
    from pde.finite_network import initialize as oracle_initialize

    device = torch.device(args.device)
    dtype = torch.float64
    rng = np.random.default_rng(731)
    n, m = 7, 5
    u_np = rng.normal(size=(2, m))
    u_np /= np.linalg.norm(u_np, axis=0)
    y_np = rng.normal(size=m)
    # Explicitly move every block away from its initializer, with O(1) c.
    a_np = rng.normal(size=(n, 2)) + 0.2
    b_np = rng.normal(size=(n, n)) / np.sqrt(n) + 0.13
    c_np = rng.normal(size=n) * 0.7 + 0.2
    state = State(*(torch.tensor(v, dtype=dtype, device=device) for v in (a_np, b_np, c_np)))
    u = torch.tensor(u_np, dtype=dtype, device=device)
    y = torch.tensor(y_np, dtype=dtype, device=device)
    parameters = Parameters((a_np, b_np), c_np)
    x_np = np.sqrt(2) * u_np
    reference = oracle_forward(parameters, x_np)
    velocity = flow_velocity(parameters, x_np, y_np)
    errors = {}
    predicted, hidden, z = forward(state, u)
    errors['forward'] = float(np.max(np.abs(numpy(predicted) - reference.output)))
    errors['hidden'] = max(float(np.max(np.abs(numpy(h) - h0))) for h, h0 in zip(hidden, reference.hidden))
    va, left, right, vc = rhs(state, u, y)
    dense_rhs = (va, left @ right.T, vc)
    oracle_rhs = velocity.weights + (velocity.readout,)
    errors['velocity_oracle'] = max(float(np.max(np.abs(numpy(v) - ref))) for v, ref in zip(dense_rhs, oracle_rhs))
    autograd_state = State(*(v.detach().clone().requires_grad_(True) for v in (state.a, state.b, state.c)))
    autograd_loss = (forward(autograd_state, u)[0] - y).square().mean()
    grads = torch.autograd.grad(autograd_loss, (autograd_state.a, autograd_state.b, autograd_state.c))
    errors['velocity_autograd'] = max(float(torch.max(torch.abs(v + mobility * g)))
                                      for v, g, mobility in zip(dense_rhs, grads, (n, 1, n)))
    energy_derivative = sum(float(torch.sum(g * v)) for g, v in zip(grads, dense_rhs))
    mobility_dissipation = -sum(float(torch.sum(v.square())) / mobility
                               for v, mobility in zip(dense_rhs, (n, 1, n)))
    residual_np = reference.output - y_np
    kernel_dissipation = -4 / m ** 2 * float(residual_np @ kernel(parameters, x_np) @ residual_np)
    errors['gradient_flow_dissipation'] = abs(energy_derivative - mobility_dissipation)
    errors['kernel_dissipation'] = abs(energy_derivative - kernel_dissipation)
    step = 0.037
    predicted_parameters = Parameters(tuple(w + step * v for w, v in zip(parameters.weights, velocity.weights)),
                                      parameters.readout + step * velocity.readout)
    second_velocity = flow_velocity(predicted_parameters, x_np, y_np)
    exact_step = tuple(w + step / 2 * (v + v2) for w, v, v2 in zip(
        parameters.weights + (parameters.readout,), oracle_rhs,
        second_velocity.weights + (second_velocity.readout,)))
    with torch.no_grad():
        heun_step(state, u, y, step)
    errors['heun_all_blocks'] = max(float(np.max(np.abs(numpy(w) - ref))) for w, ref in zip((state.a, state.b, state.c), exact_step))
    initialized = initialize(11, 42, dtype, device)
    initialized_reference = oracle_initialize(11, 2, 2, seed=42)
    errors['initializer'] = max(float(np.max(np.abs(numpy(v) - ref))) for v, ref in zip(
        (initialized.a, initialized.b, initialized.c),
        initialized_reference.weights + (initialized_reference.readout,)))
    # Exercise a row-block boundary without allocating a scientific-sized model.
    initialized_blocked = initialize(513, 42, dtype, device)
    reference_blocked = oracle_initialize(513, 2, 2, seed=42)
    errors['initializer_row_block_boundary'] = max(float(np.max(np.abs(numpy(v) - ref))) for v, ref in zip(
        (initialized_blocked.a, initialized_blocked.b, initialized_blocked.c),
        reference_blocked.weights + (reference_blocked.readout,)))
    h0 = tuple(v.clone() for v in hidden)
    measured = observation(state, u, y, h0)
    final_prediction, final_hidden, _ = forward(state, u)
    reference_grams = np.stack([numpy(h).T @ numpy(h) / n for h in final_hidden])
    errors['grams'] = float(np.max(np.abs(measured[2] - reference_grams)))
    errors['gram_rms_identity'] = float(np.max(np.abs(measured[3] ** 2 - np.trace(measured[2], axis1=1, axis2=2) / m)))
    reference_movement = np.array([np.sqrt(np.mean((numpy(h) - numpy(initial)) ** 2))
                                   for h, initial in zip(final_hidden, h0)])
    errors['movement'] = float(np.max(np.abs(measured[4] - reference_movement)))
    errors['loss'] = abs(measured[0] - float(np.mean((numpy(final_prediction) - y_np) ** 2)))
    errors['oddness'] = float(torch.max(torch.abs(forward(state, -u)[0] + final_prediction)))
    record = dict(status='pass' if max(errors.values()) <= 1e-10 else 'fail',
                  passed=bool(max(errors.values()) <= 1e-10),
                  device=str(device), dtype='float64', errors=errors, tolerance=1e-10,
                  nonzero_state=dict(width=n, samples=m, step=step, readout_rms=float(np.sqrt(np.mean(c_np ** 2)))),
                  source_sha256=sha256(__file__), oracle_sha256=sha256(root / 'code/pde/finite_network.py'))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if (out / 'check.json').exists():
        raise FileExistsError(f'Refusing to replace {out / "check.json"}')
    write_json(out / 'check.json', record)
    print(json.dumps(record, indent=2, sort_keys=True), flush=True)
    if record['status'] != 'pass':
        raise AssertionError('Correctness gate failed')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs')
    parser.add_argument('--out', required=True)
    parser.add_argument('--width', type=int, default=2048)
    parser.add_argument('--seed', type=int, default=11)
    parser.add_argument('--step', type=float, default=.01)
    parser.add_argument('--dtype', choices=('float32', 'float64'), default='float32')
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_float32_matmul_precision('highest')
    if args.check:
        check(args)
    else:
        if not args.inputs:
            parser.error('--inputs is required for a scientific run')
        run(args)


if __name__ == '__main__':
    main()
