#!/usr/bin/env python3
"""Capture trajectories and validate response compression in one executable.

``validate`` runs fresh Dense, Harmonic and empirical Logarithmic experiments,
with frozen-NTK, total-state-matched small-MLP and explicit LoRA controls. Its
source approximations and finite-program backend substitutions are recorded;
finite sampled RMS tests are not theorem certificates. Use ``validate --help``.

The original CLI replays float64 adaptive-Heun dense/lifted-Legendre models.
The two closure modules are loaded from the study's preserved, hash-checked
legacy ZIP, without changing or importing other studies. Training/query data
come from the portable paper bundle. All output goes to a fresh --out folder;
publication of its checked response_memory_source.npz is a separate step.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import types
import zipfile

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
LEGACY = ROOT / "studies/neural_response_memory_20260922/legacy_experiments.zip"
HASHES = {
    "moment_engine.py": "ebf39cf377f1eb0f5dea64fa1ab946fddcb11a662b2368472017abef9237acd9",
    "orthogonal_moment_engine.py": "32f80cf35c44b5015821fa8c8726bb8ff3bc6f7eb3e1b7abe9ee62ea8f529909",
}
INITIAL_HASHES = {
    "w": "da24d2b86aed45dfa6e7442e24bfcb968ec28fcfbcfb2f5f07ac066601fffd63",
    "c": "460ee22d13695cbe3226805bf5b24b124100e32be5717737508c79d8679b0db6",
    "M": "559c9ad62fd9feab4fb4671e854b86ec975240a12aa8792873824ebe2344b3f9",
}


def sha(value):
    return hashlib.sha256(value).hexdigest()


def array_sha(value):
    return sha(np.ascontiguousarray(value).tobytes())


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def load_legacy(out):
    with zipfile.ZipFile(LEGACY) as archive:
        for name, expected in HASHES.items():
            source = archive.read(name)
            if sha(source) != expected:
                raise RuntimeError(f"Archived solver hash mismatch: {name}")
            if out is not None:
                (out / name).write_bytes(source)
            module = types.ModuleType(name[:-3])
            module.__file__ = str(LEGACY) + "/" + name
            sys.modules[module.__name__] = module
            exec(compile(source, module.__file__, "exec"), module.__dict__)
    return sys.modules["moment_engine"], sys.modules["orthogonal_moment_engine"]


def rms(x):
    return x.square().mean().sqrt()


def dense_fields(state, inputs):
    w, c, matrix = state
    h1 = (w @ inputs.T).tanh()
    h2 = (matrix @ h1).tanh()
    return h1, h2, c @ h2 / len(c)


def dense_rhs(state, inputs, labels):
    w, c, matrix = state
    h1, h2, f = dense_fields(state, inputs)
    residual = f - labels
    delta2 = c[:, None] * (1 - h2.square())
    delta1 = (matrix.T @ delta2) * (1 - h1.square())
    return [(-2 / len(labels)) * (delta1 * residual) @ inputs,
            (-2 / len(labels)) * (h2 @ residual),
            (-2 / (len(c) * len(labels))) * (delta2 * residual) @ h1.T]


class Dense:
    """Canonical two-hidden-layer flow; no legacy-study dependency."""

    def __init__(self, width, dimension, seed, device):
        generator = torch.Generator(device=device).manual_seed(seed)
        self.initial_state = [
            torch.randn(width, dimension, generator=generator, device=device),
            torch.zeros(width, device=device),
            torch.randn(width, width, generator=generator, device=device) / math.sqrt(width),
        ]
        self.fixed_scalars = 0

    def rhs(self, state, inputs, labels):
        return dense_rhs(state, inputs, labels)

    def predict(self, state, queries, inputs, labels):
        return dense_fields(state, queries)[2]


class DeepDense:
    """Fixed hidden depth L; state [A, w, B2, ..., BL], f=w^T hL/n.

    A has shape (n,d), each hidden mixer is (n,n), and w is (n,).
    The squared-loss flow has mobilities (n,n,1,...,1) in this state order.
    """

    def __init__(self, width, dimension, depth, activation, seed, device):
        if width < 1 or dimension < 1 or depth < 1 or int(depth) != depth:
            raise ValueError('DeepDense needs positive width, dimension and integer hidden depth')
        if activation not in ('tanh', 'atan'):
            raise ValueError('DeepDense activation must be tanh or atan')
        self.depth, self.activation = int(depth), activation
        generator = torch.Generator(device=device).manual_seed(seed)
        self.initial_state = [torch.randn(width, dimension, generator=generator, device=device,
                                          dtype=torch.float64),
                              torch.zeros(width, device=device, dtype=torch.float64)]
        self.initial_state += [torch.randn(width, width, generator=generator, device=device,
                                           dtype=torch.float64)/math.sqrt(width)
                               for _ in range(self.depth-1)]
        self.fixed_scalars = 0

    def fields(self, state, inputs):
        hs, gates = [], []
        z = state[0]@inputs.T
        for layer in range(self.depth):
            if layer:
                z = state[layer+1]@hs[-1]
            h = z.tanh() if self.activation == 'tanh' else z.atan()
            hs.append(h)
            gates.append(1-h.square() if self.activation == 'tanh' else 1/(1+z.square()))
        return hs, gates

    def backward(self, state, hs, gates, readout=None):
        deltas = [None]*self.depth
        deltas[-1] = (state[1] if readout is None else readout)[:, None]*gates[-1]
        for layer in range(self.depth-2, -1, -1):
            deltas[layer] = (state[layer+2].T@deltas[layer+1])*gates[layer]
        return deltas

    def rhs(self, state, inputs, labels):
        hs, gates = self.fields(state, inputs)
        deltas = self.backward(state, hs, gates)
        n, scale = len(state[1]), 2/len(labels)
        deficit = labels-state[1]@hs[-1]/n
        return [scale*(deltas[0]*deficit)@inputs, scale*hs[-1]@deficit] + [
            scale/n*(deltas[layer]*deficit)@hs[layer-1].T
            for layer in range(1, self.depth)]

    def predict(self, state, queries, inputs=None, labels=None):
        return state[1]@self.fields(state, queries)[0][-1]/len(state[1])


class DeepHarmonic(DeepDense):
    """Autonomous fixed-depth metric/deficit optimizer with offline sources.

    Source columns are pre-truncated h/delta lists. Only their immediate
    initialized forward/reverse images are added; no recursive image closure.
    Construction uses float64, four coordinate candidates, and condition cap 16.
    Sources and the dense model are discarded; all retained metrics are counted.
    """

    @torch.no_grad()
    def __init__(self, dense, inputs, labels, source_coefficients, budget, selection_seed=501):
        self.depth, self.activation = dense.depth, dense.activation
        runtime_dtype = dense.initial_state[0].dtype
        original = [value.to(dtype=torch.float64) for value in dense.initial_state]
        a0, w0 = original[:2]
        n, device, budget = len(w0), a0.device, int(budget)
        training, targets = inputs.to(dtype=torch.float64), labels.to(dtype=torch.float64)
        if bool(w0.ne(0).any()):
            raise ValueError('DeepHarmonic initialization requires zero dense readout')
        if budget < len(labels):
            raise ValueError('DeepHarmonic budget must permit a full-rank training feature Gram')
        h0, _ = self.fields(original, training)
        if budget >= n:
            self.metrics = [torch.eye(n, dtype=a0.dtype, device=device)/n for _ in range(self.depth)]
            self.metric_inverses = [torch.eye(n, dtype=a0.dtype, device=device)*n
                                   for _ in range(self.depth-1)]
            self.initial_state = [value.clone() for value in original]+[targets.clone()]
            self.diagnostics = dict(branch='full_retention_uncompressed', widths=[n]*self.depth,
                                    source_ranks=[n]*self.depth)
        else:
            if source_coefficients is None or any(
                    len(source_coefficients[name]) != self.depth for name in ('h', 'delta')):
                raise ValueError('DeepHarmonic needs h and delta source lists of length depth')
            retained = {name: [value.to(dtype=torch.float64, device=device)
                               for value in source_coefficients[name]] for name in ('h', 'delta')}
            if any(value.ndim != 2 or value.shape[0] != n or not bool(torch.isfinite(value).all())
                   for family in retained.values() for value in family):
                raise ValueError('DeepHarmonic sources must be finite (n,r) matrices')
            bases, selected, selections, mandatory_errors = [], [], [], []
            constant = torch.ones(n, 1, dtype=a0.dtype, device=device)
            for layer in range(self.depth):
                mandatory = ([constant, h0[layer], original[layer+1]@h0[layer-1]] if layer
                             else [constant, a0, h0[layer]])
                optional = [retained['h'][layer], retained['delta'][layer]]
                if layer:
                    optional.append(original[layer+1]@retained['h'][layer-1])
                if layer+1 < self.depth:
                    optional.append(original[layer+2].T@retained['delta'][layer+1])
                basis, error = _harmonic_source_basis(torch.cat(mandatory, 1), torch.cat(optional, 1))
                selection = _panel_coordinate_metric(basis, budget, selection_seed+layer, trials=4)
                if selection[-1]['embedding_max'] > 16:
                    raise ArithmeticError(f'DeepHarmonic layer {layer+1} source condition exceeds 16')
                bases.append(basis)
                selected.append(basis[selection[0]])
                selections.append(selection)
                mandatory_errors.append(error)
            self.metrics = [item[1] for item in selections]
            self.metric_inverses = [item[2] for item in selections[:-1]]
            mixers = [selected[layer]@(bases[layer].T@original[layer+1]@bases[layer-1]/n)
                      @(selected[layer-1].T@self.metrics[layer-1]) for layer in range(1, self.depth)]
            indices = [item[0] for item in selections]
            self.initial_state = [a0[indices[0]].clone(), w0[indices[-1]].clone()]+mixers+[targets.clone()]
            hs, _ = self.fields(self.initial_state, training)
            maximum = lambda value: float(value.abs().max()) if value.numel() else 0.
            forward_errors, reverse_errors = [], []
            for layer, mixer in enumerate(mixers, 1):
                forward_errors.append(maximum(mixer@retained['h'][layer-1][indices[layer-1]]
                    -(original[layer+1]@retained['h'][layer-1])[indices[layer]]))
                reverse_errors.append(maximum(self.metric_inverses[layer-1]@mixer.T
                    @self.metrics[layer]@retained['delta'][layer][indices[layer]]
                    -(original[layer+1].T@retained['delta'][layer])[indices[layer-1]]))
            self.diagnostics = dict(branch='empirical_spectral_setup_metric_runtime',
                widths=[len(index) for index in indices], source_ranks=[basis.shape[1] for basis in bases],
                selection=[item[-1] for item in selections], mandatory_source_errors=mandatory_errors,
                initialized_feature_errors=[maximum(h-h0[layer][indices[layer]]) for layer, h in enumerate(hs)],
                initialized_gram_error=maximum(hs[-1].T@self.metrics[-1]@hs[-1]-h0[-1].T@h0[-1]/n),
                paired_forward_action_errors=forward_errors, paired_reverse_action_errors=reverse_errors)
        # Offline geometry is assembled in double precision; deployment preserves
        # the reference state dtype and keeps no dense/source construction arrays.
        self.initial_state = [value.to(dtype=runtime_dtype) for value in self.initial_state]
        self.metrics = [value.to(dtype=runtime_dtype) for value in self.metrics]
        self.metric_inverses = [value.to(dtype=runtime_dtype) for value in self.metric_inverses]
        self.fixed_scalars = sum(value.numel() for value in self.metrics+self.metric_inverses)
        _, _, _, gram = self._readout(self.initial_state, inputs, labels)
        eigenvalues = torch.linalg.eigvalsh(gram)
        self.diagnostics.update(requested_budget=budget, activation=self.activation, depth=self.depth,
            certified_source_setup=False, source_assembly_dtype='torch.float64', runtime_dtype=str(runtime_dtype),
            initial_feature_gram_min=float(eigenvalues[0]),
            initial_feature_gram_condition=float(eigenvalues[-1]/eigenvalues[0]),
            moving_scalars=sum(value.numel() for value in self.initial_state), fixed_scalars=self.fixed_scalars)

    def backward(self, state, hs, gates, readout=None):
        deltas = [None]*self.depth
        deltas[-1] = (state[1] if readout is None else readout)[:, None]*gates[-1]
        for layer in range(self.depth-2, -1, -1):
            deltas[layer] = gates[layer]*(self.metric_inverses[layer]@(state[layer+2].T
                                          @(self.metrics[layer+1]@deltas[layer+1])))
        return deltas

    def _readout(self, state, inputs, labels):
        hs, gates = self.fields(state, inputs)
        normalized = hs[-1]/math.sqrt(len(labels))
        gram = normalized.T@(self.metrics[-1]@normalized)
        gram = (gram+gram.T)/2
        factor, info = torch.linalg.cholesky_ex(gram)
        if int(info) != 0:
            raise ArithmeticError('DeepHarmonic training feature Gram is not positive definite; no ridge added')
        correction = (labels-state[-1])/math.sqrt(len(labels))-normalized.T@(self.metrics[-1]@state[1])
        readout = state[1]+normalized@torch.cholesky_solve(correction[:, None], factor).flatten()
        return readout, hs, gates, gram

    def rhs(self, state, inputs, labels):
        readout, hs, gates, _ = self._readout(state, inputs, labels)
        deltas = self.backward(state, hs, gates, readout)
        scale, deficit = 2/len(labels), state[-1]
        kernel = hs[-1].T@(self.metrics[-1]@hs[-1])
        kernel = kernel+(deltas[0].T@(self.metrics[0]@deltas[0]))*(inputs@inputs.T)
        updates = [scale*(deltas[0]*deficit)@inputs, scale*hs[-1]@deficit]
        for layer in range(1, self.depth):
            incoming = self.metrics[layer-1]@hs[layer-1]
            updates.append(scale*(deltas[layer]*deficit)@incoming.T)
            kernel = kernel+(deltas[layer].T@(self.metrics[layer]@deltas[layer]))*(hs[layer-1].T@incoming)
        return updates+[-scale*kernel@deficit]

    def predict(self, state, queries, inputs, labels):
        return (self.metrics[-1]@self._readout(state, inputs, labels)[0])@self.fields(state, queries)[0][-1]

    def prepare_query(self, state, inputs, labels):
        coefficient = self.metrics[-1]@self._readout(state, inputs, labels)[0]
        first, mixers, activation = state[0], tuple(state[2:self.depth+1]), self.activation

        def predict(queries):
            h = first@queries.T
            h = h.tanh() if activation == 'tanh' else h.atan()
            for mixer in mixers:
                h = mixer@h
                h = h.tanh() if activation == 'tanh' else h.atan()
            return coefficient@h

        return predict


def deep_rollout_small_checks():
    """Tiny CPU gradient, source-pair, full-retention and restart checks."""
    dtype, device = torch.float64, torch.device('cpu')
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]], dtype=dtype)
    labels = torch.tensor([.2, -.1, .3], dtype=dtype)
    generator = torch.Generator().manual_seed(17)
    results = []
    for depth in (2, 3):
        for activation in ('tanh', 'atan'):
            dense = DeepDense(32, 2, depth, activation, 3, device)
            dense.initial_state = [value.to(dtype=dtype) for value in dense.initial_state]
            arbitrary = [(value+.03*torch.randn(value.shape, generator=generator, dtype=dtype))
                         .requires_grad_() for value in dense.initial_state]
            prediction = dense.predict(arbitrary, inputs)
            gradients = torch.autograd.grad((prediction-labels).square().mean(), arbitrary)
            velocities = dense.rhs(arbitrary, inputs, labels)
            maximum = lambda value: float(value.detach().abs().max())
            gradient_error = max(maximum(v+mobility*g) for v, mobility, g in
                                 zip(velocities, [32, 32]+[1]*(depth-1), gradients))
            full = DeepHarmonic(dense, inputs, labels, None, budget=32)
            actual = full.rhs(arbitrary+[labels-prediction], inputs, labels)
            rhs_error = max(maximum(a-b) for a, b in zip(actual[:-1], velocities))
            _, prediction_velocity = torch.autograd.functional.jvp(
                lambda *state: dense.predict(state, inputs), tuple(arbitrary), tuple(velocities))
            deficit_error = maximum(actual[-1]+prediction_velocity)
            with torch.no_grad():
                coefficients = {name: [torch.randn(32, 2, generator=generator, dtype=dtype)
                                       for _ in range(depth)] for name in ('h', 'delta')}
                compressed = DeepHarmonic(dense, inputs, labels, coefficients, budget=31)
                setup = compressed.diagnostics
                setup_error = max(setup['mandatory_source_errors']+setup['initialized_feature_errors']
                    +setup['paired_forward_action_errors']+setup['paired_reverse_action_errors']
                    +[setup['initialized_gram_error']])
                state = [value.clone() for value in compressed.initial_state]
                for _ in range(3):
                    state = [value+.01*velocity for value, velocity in
                             zip(state, compressed.rhs(state, inputs, labels))]
                restored = DeepHarmonic.__new__(DeepHarmonic)
                restored.depth, restored.activation = depth, activation
                restored.metrics = [value.clone() for value in compressed.metrics]
                restored.metric_inverses = [value.clone() for value in compressed.metric_inverses]
                restored.initial_state = [value.clone() for value in state]
                queries = torch.tensor([[0., 1.], [-1., 0.], [.8, -.6]], dtype=dtype)
                expected = compressed.predict(state, queries, inputs, labels)
                restarted = restored.prepare_query(restored.initial_state, inputs, labels)(queries)
                restart_error = max([maximum(restarted-expected)]+[maximum(a-b) for a, b in zip(
                    compressed.rhs(state, inputs, labels), restored.rhs(restored.initial_state, inputs, labels))])
                constraint_error = maximum(compressed.predict(state, inputs, inputs, labels)-labels+state[-1])
                assert compressed.fixed_scalars == (2*depth-1)*31**2
                assert set(vars(compressed)) == {'depth', 'activation', 'metrics', 'metric_inverses',
                                                 'initial_state', 'fixed_scalars', 'diagnostics'}
                json.dumps(setup, allow_nan=False)
            errors = dict(gradient_max_abs=gradient_error, full_retention_rhs_max_abs=rhs_error,
                          full_retention_deficit_max_abs=deficit_error, source_setup_max_abs=setup_error,
                          restart_max_abs=restart_error, training_constraint_max_abs=constraint_error)
            assert max(errors.values()) < 1e-10, (depth, activation, errors)
            results.append(dict(depth=depth, activation=activation, **errors))
    return results


class LoRA:
    """Explicit low-rank increment; its frozen dense mixer is NOT free storage."""

    def __init__(self, dense, rank, seed, multiplier=1.):
        a, w, matrix = dense.initial_state
        n = len(w)
        if not 1 <= rank <= n:
            raise ValueError("LoRA rank must be in [1,n]")
        generator = torch.Generator(device=a.device).manual_seed(seed)
        right = torch.linalg.qr(torch.randn(n, rank, generator=generator,
                                            device=a.device), mode='reduced')[0]
        self.matrix = matrix.clone()
        self.initial_state = [a.clone(), w.clone(), torch.zeros_like(right), right]
        self.mobility = multiplier * n / rank
        self.fixed_scalars = matrix.numel()

    def fields(self, state, inputs):
        a, w, left, right = state
        h1 = (a @ inputs.T).tanh()
        h2 = (self.matrix @ h1 + left @ (right.T @ h1)).tanh()
        return h1, h2, w @ h2 / len(w)

    def rhs(self, state, inputs, labels):
        a, w, left, right = state
        h1, h2, prediction = self.fields(state, inputs)
        residual = prediction - labels
        delta2 = w[:, None] * (1 - h2.square())
        delta1 = (self.matrix.T @ delta2 + right @ (left.T @ delta2)) * (1 - h1.square())
        force = (-2 / len(labels)) * (delta2 * residual)
        return [(-2 / len(labels)) * (delta1 * residual) @ inputs,
                (-2 / len(labels)) * (h2 @ residual),
                self.mobility / len(w) * force @ (h1.T @ right),
                self.mobility / len(w) * h1 @ (force.T @ left)]

    def predict(self, state, queries, inputs, labels):
        return self.fields(state, queries)[2]


def synchronize(device):
    if torch.device(device).type == 'cuda':
        torch.cuda.synchronize(device)


@torch.no_grad()
def integrate(model, inputs, labels, queries, times, step, seconds, observer=None):
    """Fixed-step RK4 at shared times. Refinement is measured separately."""
    device = inputs.device
    synchronize(device)
    started = time.monotonic()
    baseline_bytes = torch.cuda.memory_allocated(device) if device.type == 'cuda' else None
    if device.type == 'cuda':
        torch.cuda.reset_peak_memory_stats(device)
    state = [value.clone() for value in model.initial_state]
    predictions, losses, current, steps, query_seconds, training_seconds, refresh_seconds = [], [], 0., 0, 0., 0., 0.
    for target in times:
        synchronize(device)
        training_started = time.monotonic()
        while current < target - 1e-12:
            if time.monotonic() - started > seconds:
                raise TimeoutError(f"{type(model).__name__} capped at t={current:.6g}")
            h = min(step, target - current)
            k1 = model.rhs(state, inputs, labels)
            k2 = model.rhs([v+h/2*k for v, k in zip(state, k1)], inputs, labels)
            k3 = model.rhs([v+h/2*k for v, k in zip(state, k2)], inputs, labels)
            k4 = model.rhs([v+h*k for v, k in zip(state, k3)], inputs, labels)
            state = [v+h/6*(a+2*b+2*c+d) for v, a, b, c, d in zip(state, k1, k2, k3, k4)]
            current += h
            steps += 1
            if steps % 32 == 0:
                synchronize(device)
        synchronize(device)
        training_seconds += time.monotonic() - training_started
        if steps:
            del k1, k2, k3, k4
        refresh_started = time.monotonic()
        prepared = model.prepare_query(state, inputs, labels) if hasattr(model, 'prepare_query') else None
        synchronize(device)
        refresh_seconds += time.monotonic()-refresh_started
        query_started = time.monotonic()
        prediction = prepared(queries) if prepared is not None else model.predict(state, queries, inputs, labels)
        synchronize(device)
        query_seconds += time.monotonic() - query_started
        train = model.predict(state, inputs, inputs, labels)
        if not bool(torch.isfinite(prediction).all() and torch.isfinite(train).all()):
            raise FloatingPointError(f"nonfinite {type(model).__name__} at t={target}")
        predictions.append(prediction.cpu().numpy())
        losses.append(float((train-labels).square().mean()))
        if observer is not None:
            observer(float(target), state)
        synchronize(device)
        if time.monotonic() - started > seconds:
            raise TimeoutError(f"{type(model).__name__} exceeded cap including query/observer at t={target}")
    synchronize(device)
    elapsed = time.monotonic() - started
    return state, np.stack(predictions), dict(
        seconds=elapsed, query_seconds=query_seconds, query_refresh_seconds=refresh_seconds,
        query_timing_scope='whole query batch, after readout refresh; amortized, not single-query latency',
        training_seconds=training_seconds, steps=steps,
        seconds_per_step=training_seconds/max(1, steps),
        moving_scalars=sum(v.numel() for v in state),
        fixed_scalars=int(model.fixed_scalars), losses=losses,
        process_peak_cuda_bytes=(torch.cuda.max_memory_allocated(device) if device.type == 'cuda' else None),
        incremental_peak_cuda_bytes=(torch.cuda.max_memory_allocated(device)-baseline_bytes if device.type == 'cuda' else None),
        peak_scope='whole process, including other resident references; not isolated model memory')


def frozen_predictions(dense, inputs, labels, queries, times):
    """Exact all-block initial NTK: only the readout block survives w(0)=0."""
    h = dense_fields(dense.initial_state, inputs)[1]
    hq = dense_fields(dense.initial_state, queries)[1]
    kernel = h.T @ h / h.shape[0]
    cross = hq.T @ h / h.shape[0]
    values, vectors = torch.linalg.eigh(kernel)
    tolerance = 128 * torch.finfo(h.dtype).eps * float(kernel.norm())
    if float(values.min()) < -tolerance:
        raise ArithmeticError('Initial NTK is not numerically positive semidefinite')
    values = values.clamp_min(0)
    predictions = []
    for t in times:
        scale = 2 * t / len(labels)
        gain = torch.where(values > tolerance,
                           -torch.expm1(-scale*values)/values.clamp_min(torch.finfo(h.dtype).tiny),
                           torch.full_like(values, scale))
        predictions.append((cross @ (vectors @ (gain * (vectors.T @ labels)))).cpu().numpy())
    return np.stack(predictions)


def validation_data(dimension, samples, queries, seed, device, task='toy', partition='test',
                    raw_images=False, tuning_samples=64, digit_pair=(3, 8)):
    rng = np.random.default_rng(seed)
    if task == 'digits':
        from sklearn.datasets import load_digits
        from sklearn.model_selection import train_test_split
        from sklearn.decomposition import PCA
        if (len(digit_pair) != 2 or len(set(digit_pair)) != 2
                or any(not isinstance(v, (int, np.integer)) or not 0 <= v <= 9
                       for v in digit_pair)):
            raise ValueError('digit_pair must contain two distinct digits from 0 through 9')
        data, target = load_digits(return_X_y=True)
        keep = (target == digit_pair[0]) | (target == digit_pair[1])
        data, target = data[keep], np.where(target[keep] == digit_pair[0], -1., 1.)
        indices, heldout = train_test_split(np.arange(len(target)), train_size=samples,
                                           stratify=target, random_state=seed)
        if tuning_samples:
            tuning, testing = train_test_split(heldout, train_size=tuning_samples,
                                               stratify=target[heldout], random_state=seed+1)
            heldout = tuning if partition == 'pilot' else testing
        if raw_images:
            if dimension != data.shape[1]:
                raise ValueError('Raw digits require dimension 64; no projection is applied')
            train, query = data[indices].copy(), data[heldout].copy()
        else:
            pca = PCA(n_components=dimension, svd_solver='full').fit(data[indices])
            train, query = pca.transform(data[indices]), pca.transform(data[heldout])
        train /= np.linalg.norm(train, axis=1, keepdims=True)
        query /= np.linalg.norm(query, axis=1, keepdims=True)
        labels, truth = target[indices], target[heldout]
    else:
        train = rng.normal(size=(samples, dimension))
        train /= np.linalg.norm(train, axis=1, keepdims=True)
        if dimension == 2:
            angle = np.linspace(0, 2*np.pi, queries, endpoint=False) + .137
            query = np.column_stack((np.cos(angle), np.sin(angle)))
        else:
            query = rng.normal(size=(queries, dimension))
            query /= np.linalg.norm(query, axis=1, keepdims=True)
        def target(v):
            if dimension == 2:
                angle = np.arctan2(v[:, 1], v[:, 0])
                return np.sin(3*angle) + .5*np.cos(5*angle)
            return np.sqrt(dimension)*v[:, 0] + dimension**1.5*v[:, 0]*v[:, 1]*v[:, 2]
        labels, truth = target(train), target(query)
        scale = np.sqrt(np.mean(labels**2))
        labels, truth = labels/scale, truth/scale
    if not all(np.isfinite(v).all() for v in (train, labels, query, truth)):
        raise ValueError('Nonfinite or zero-norm data after preprocessing')
    return tuple(torch.as_tensor(v, device=device) for v in (train, labels, query, truth))


def trajectory_rms(prediction, reference):
    curve = np.sqrt(np.mean((prediction-reference)**2, axis=1))
    return dict(max_time_rms=float(curve.max()), endpoint_rms=float(curve[-1]), curve=curve.tolist())


@torch.no_grad()
def collect_harmonic_sources(dense, inputs, labels, args):
    """Passive-node spectral setup, charged as a complete offline dense rollout."""
    device = inputs.device
    generator = torch.Generator(device=device).manual_seed(args.seed+40000)
    if args.dimension == 2:
        angle = torch.arange(args.spatial_nodes, device=device)*2*math.pi/args.spatial_nodes
        nodes = torch.stack((angle.cos(), angle.sin()), dim=1)
    else:
        nodes = torch.randn(args.spatial_nodes, args.dimension, generator=generator, device=device)
        nodes /= nodes.norm(dim=1, keepdim=True)
    phase = np.linspace(0, np.pi, args.time_nodes)
    times = np.sort(args.horizon * (1+np.cos(phase))/2)
    times[0], times[-1] = 0., args.horizon
    fields = {key: [] for key in ('h1', 'h2', 'delta1', 'delta2')}
    def observe(t, state):
        h1, h2, _ = dense_fields(state, nodes)
        delta2 = state[1][:, None] * (1-h2.square())
        delta1 = (state[2].T @ delta2) * (1-h1.square())
        for key, value in zip(fields, (h1, h2, delta1, delta2)):
            fields[key].append(value.clone())
    synchronize(device)
    started = time.monotonic()
    _, _, info = integrate(dense, inputs, labels, nodes[:1], times, args.step,
                           args.per_run_seconds, observer=observe)
    coefficients, projection = harmonic_source_coefficients(
        {key: torch.stack(value) for key, value in fields.items()},
        times, nodes, args.time_degree, args.spatial_degree)
    synchronize(device)
    return coefficients, dict(seconds=time.monotonic()-started, rollout=info, projection=projection,
                              source_contract='complete finite-horizon offline rollout; not a zero-time jet implementation',
                              test_queries_used=False)


def independent_checks(device):
    model = Dense(9, 3, 17, device)
    generator = torch.Generator(device=device).manual_seed(19)
    inputs = torch.randn(5, 3, generator=generator, device=device)
    inputs /= inputs.norm(dim=1, keepdim=True)
    labels = torch.randn(5, generator=generator, device=device)
    state = [v.clone().requires_grad_() for v in model.initial_state]
    state[1] = torch.randn(9, generator=generator, device=device, requires_grad=True)
    gradients = torch.autograd.grad((dense_fields(state, inputs)[2]-labels).square().mean(), state)
    error = max(float((a+b*g).detach().abs().max()) for a, b, g in
                zip(dense_rhs(state, inputs, labels), (9, 9, 1), gradients))
    lora = LoRA(model, 3, 23)
    ls = [v.clone().requires_grad_() for v in lora.initial_state]
    ls[1] = state[1]
    ls[2] = torch.randn(9, 3, generator=generator, device=device, requires_grad=True)*.1
    gradients = torch.autograd.grad((lora.fields(ls, inputs)[2]-labels).square().mean(), ls)
    lora_error = max(float((a+b*g).detach().abs().max()) for a, b, g in
                     zip(lora.rhs(ls, inputs, labels), (9, 9, 3, 3), gradients))
    if max(error, lora_error) > 1e-10:
        raise AssertionError((error, lora_error))
    return dict(dense_gradient_max_abs=error, lora_gradient_max_abs=lora_error)


def harmonic_source_coefficients(fields, times, nodes, time_degree=3, spatial_degree=5):
    """Empirical time-Chebyshev/sphere-polynomial coefficients, setup only.

    ``fields[name]`` has shape (number_of_times, dense_width, number_of_nodes).
    Circle Fourier modes are real spherical harmonics. In higher dimensions,
    polynomial restrictions span the harmonics through ``spatial_degree``;
    their finite-node least-squares fit is explicitly an empirical backend.
    No continuum quadrature or theorem error certificate is asserted here.
    """
    import itertools

    first = next(iter(fields.values()))
    nodes = torch.as_tensor(nodes, dtype=first.dtype, device=first.device)
    times = torch.as_tensor(times, dtype=first.dtype, device=first.device)
    if len(times) < 2 or not bool(times[-1] > times[0]):
        raise ValueError('Harmonic setup needs at least two increasing source times')
    if time_degree < 0 or spatial_degree < 0:
        raise ValueError('Harmonic source degrees must be nonnegative')
    if time_degree >= len(times):
        raise ValueError('Temporal degree must be smaller than the source-node count')
    coordinate = 2*(times-times[0])/(times[-1]-times[0])-1
    temporal = [torch.ones_like(coordinate)]
    if time_degree:
        temporal.append(coordinate)
    for _ in range(2, time_degree+1):
        temporal.append(2*coordinate*temporal[-1]-temporal[-2])
    temporal = torch.stack(temporal, dim=1)
    if nodes.shape[1] == 2:
        angle = torch.atan2(nodes[:, 1], nodes[:, 0])
        spatial = [torch.ones_like(angle)]
        for degree in range(1, spatial_degree+1):
            spatial.extend((math.sqrt(2)*(degree*angle).cos(),
                            math.sqrt(2)*(degree*angle).sin()))
        backend = 'circle_real_spherical_harmonics_least_squares'
    else:
        spatial = [torch.ones(len(nodes), dtype=nodes.dtype, device=nodes.device)]
        for degree in range(1, spatial_degree+1):
            for factors in itertools.combinations_with_replacement(range(nodes.shape[1]), degree):
                spatial.append(nodes[:, factors].prod(dim=1))
        backend = 'sphere_polynomial_restriction_least_squares'
    spatial = torch.stack(spatial, dim=1)
    # Pseudoinverses apply only to the offline scalar fit, never to the runtime Gram.
    temporal_inverse = torch.linalg.pinv(temporal)
    spatial_inverse = torch.linalg.pinv(spatial)
    coefficients, errors = {}, {}
    for name in ('h1', 'h2', 'delta1', 'delta2'):
        value = fields[name]
        if value.ndim != 3 or value.shape[0] != len(times) or value.shape[2] != len(nodes):
            raise ValueError(f'Invalid source shape for {name}: {tuple(value.shape)}')
        block = torch.einsum('kt,tnx,sx->nks', temporal_inverse, value, spatial_inverse)
        fitted = torch.einsum('tk,nks,xs->tnx', temporal, block, spatial)
        error = fitted-value
        coefficients[name] = block.flatten(1)
        errors[name] = dict(max_coordinate_error=float(error.abs().max()),
                           relative_frobenius_error=float(error.norm()/value.norm().clamp_min(1e-30)))
    diagnostics = dict(backend=backend, certified=False, time_degree=time_degree,
                       spatial_degree=spatial_degree,
                       temporal_rank=int(torch.linalg.matrix_rank(temporal)),
                       spatial_rank=int(torch.linalg.matrix_rank(spatial)),
                       coefficient_count=int(temporal.shape[1]*spatial.shape[1]),
                       source_fit_errors=errors,
                       error_scope='residual at setup nodes only; not a uniform source certificate')
    return coefficients, diagnostics


def _harmonic_source_basis(mandatory, optional):
    """Ordered, twice-reorthogonalized QR; mandatory generators come first."""
    generators = torch.cat((mandatory, optional), dim=1)
    columns = []
    tolerance = 128*torch.finfo(generators.dtype).eps*math.sqrt(generators.shape[0])
    for vector in generators.T:
        scale = vector.norm()
        if float(scale) == 0:
            continue
        residual = vector/scale
        for _ in range(2):
            if columns:
                basis = torch.stack(columns, dim=1)
                residual = residual-basis@(basis.T@residual)
        magnitude = residual.norm()
        if float(magnitude) > tolerance:
            columns.append(residual/magnitude)
    if not columns:
        raise ValueError('Harmonic source space is empty')
    orthogonal, triangular = torch.linalg.qr(torch.stack(columns, dim=1), mode='reduced')
    signs = torch.where(triangular.diagonal() < 0, -1., 1.)
    orthogonal = orthogonal*signs
    error = mandatory-orthogonal@(orthogonal.T@mandatory)
    return math.sqrt(generators.shape[0])*orthogonal, float(error.abs().max())


def _harmonic_bss_metric(source_basis):
    """The appendix's sparsity-nine barrier selector and full positive metric."""
    n, rank = source_basis.shape
    rows = source_basis/math.sqrt(n)
    identity = torch.eye(rank, dtype=rows.dtype, device=rows.device)
    barrier_matrix = torch.zeros_like(identity)
    weights = torch.zeros(n, dtype=rows.dtype, device=rows.device)
    lower, upper = -3.*rank, 6.*rank
    for _ in range(9*rank):
        values, vectors = torch.linalg.eigh(barrier_matrix)
        squared_rows = (rows@vectors).square()
        upper_difference = (2/((upper-values)*(upper+2-values))).sum()
        lower_difference = (1/((values-lower-1)*(values-lower))).sum()
        upper_score = squared_rows@((upper+2-values).reciprocal().square()/upper_difference
                                     +(upper+2-values).reciprocal())
        lower_score = squared_rows@((values-lower-1).reciprocal().square()/lower_difference
                                     -(values-lower-1).reciprocal())
        margin = torch.where(upper_score > 0, lower_score-upper_score,
                             torch.full_like(upper_score, -torch.inf))
        index = int(margin.argmax())
        if float(margin[index]) < -1e-10*float(upper_score[index].abs()):
            raise ArithmeticError('BSS barrier step lost its admissible row in finite precision')
        increment = 2/(lower_score[index]+upper_score[index])
        barrier_matrix = barrier_matrix+increment*torch.outer(rows[index], rows[index])
        weights[index] += increment
        lower += 1
        upper += 2
    indices = torch.nonzero(weights > 0, as_tuple=False).flatten()
    diagonal = weights[indices]/(6*rank*n)
    selected = source_basis[indices]
    gram = selected.T@(diagonal[:, None]*selected)
    gram = (gram+gram.T)/2
    eigenvalues = torch.linalg.eigvalsh(gram)
    if float(eigenvalues.min()) < 1-1e-7 or float(eigenvalues.max()) > 4+1e-7:
        raise ArithmeticError('BSS selected Gram violates the required [1,4] bounds')
    inverse = torch.linalg.solve(gram, identity)
    weighted = diagonal[:, None]*selected
    metric = torch.diag(diagonal)+weighted@(inverse@inverse-inverse)@weighted.T
    metric_inverse = torch.diag(diagonal.reciprocal())+selected@(identity-inverse)@selected.T
    metric, metric_inverse = (metric+metric.T)/2, (metric_inverse+metric_inverse.T)/2
    diagnostics = dict(source_rank=rank, selected_width=len(indices),
                       embedding_min=float(eigenvalues.min()), embedding_max=float(eigenvalues.max()),
                       source_isometry_error=float((selected.T@metric@selected-identity).abs().max()),
                       metric_inverse_error=float((metric@metric_inverse-torch.eye(len(indices),
                           dtype=rows.dtype, device=rows.device)).abs().max()),
                       constant_norm=float(metric.sum()), diagonal_mass=float(diagonal.sum()))
    return indices, metric, metric_inverse, diagonal, diagnostics


def _panel_coordinate_metric(source_basis, budget, seed, trials=1):
    """Uniform coordinate selection with exact source isometry, not BSS.

    The diagonal-comparison factor is measured, not asserted to be four.
    The full positive metric and its inverse use the same correction formula
    as the BSS backend; no ridge or discarded source directions are introduced.
    """
    n, rank = source_basis.shape
    if not rank <= budget <= n:
        raise ValueError(f'Panel coordinate budget {budget} cannot embed rank {rank} in width {n}')
    generator = torch.Generator(device=source_basis.device).manual_seed(seed)
    best = None
    for _ in range(trials):
        candidate = torch.randperm(n, generator=generator, device=source_basis.device)[:budget]
        selected = source_basis[candidate]
        gram = selected.T @ selected / budget
        values = torch.linalg.eigvalsh((gram+gram.T)/2)
        condition = float(values[-1]/values[0]) if float(values[0]) > 0 else math.inf
        if best is None or condition < best[0]:
            best = condition, candidate, values
    _, indices, eigenvalues = best
    selected = source_basis[indices]
    identity = torch.eye(rank, dtype=selected.dtype, device=selected.device)
    if float(eigenvalues[0]) <= 0 or float(eigenvalues[-1]/eigenvalues[0]) > 1e6:
        raise ArithmeticError('Panel coordinate restriction is singular or too ill-conditioned')
    # Rescale D so that I <= V^T D V <= kappa I. Consequently D/kappa <= M <= D.
    diagonal = torch.full((budget,), 1/(budget*float(eigenvalues[0])),
                          dtype=selected.dtype, device=selected.device)
    gram = selected.T @ (diagonal[:, None]*selected)
    gram = (gram+gram.T)/2
    inverse = torch.linalg.solve(gram, identity)
    weighted = diagonal[:, None]*selected
    metric = torch.diag(diagonal)+weighted@(inverse@inverse-inverse)@weighted.T
    metric_inverse = torch.diag(diagonal.reciprocal())+selected@(identity-inverse)@selected.T
    metric, metric_inverse = (metric+metric.T)/2, (metric_inverse+metric_inverse.T)/2
    diagnostics = dict(source_rank=rank, selected_width=budget, selector='uniform_exact_isometry',
        seed=seed, selection_trials=trials, embedding_min=1.,
        embedding_max=float(eigenvalues[-1]/eigenvalues[0]),
        bss_factor_four_satisfied=bool(eigenvalues[-1] <= 4*eigenvalues[0]),
        source_isometry_error=float((selected.T@metric@selected-identity).abs().max()),
        metric_inverse_error=float((metric@metric_inverse-torch.eye(budget,
            dtype=selected.dtype, device=selected.device)).abs().max()),
        constant_norm=float(metric.sum()), diagonal_mass=float(diagonal.sum()))
    if max(diagnostics['source_isometry_error'], diagnostics['metric_inverse_error']) > 1e-8:
        raise ArithmeticError(f'Panel metric construction lost numerical accuracy: {diagnostics}')
    return indices, metric, metric_inverse, diagonal, diagnostics


class Harmonic:
    """Two-hidden-layer autonomous metric/deficit optimizer from the appendix.

    Source data and the dense reference are used only inside ``__init__``.
    ``source_rank`` truncates each base coefficient family before applying its
    initialized mixer image, preserving the retained forward/reverse pairing.
    Empirical source fitting/truncation has no asserted all-time certificate.
    """

    def __init__(self, dense, inputs, labels, source_coefficients=None, budget=None,
                 source_rank=8, rank_tolerance=1e-9, selector='bss', selection_seed=501):
        a0, w0, matrix0 = dense.initial_state
        n = len(w0)
        if matrix0.shape != (n, n) or a0.shape[0] != n:
            raise ValueError('Harmonic currently implements exactly two equally wide hidden layers')
        if bool(w0.ne(0).any()):
            raise ValueError('The Harmonic initializer requires the paper zero readout')
        budget = n if budget is None else int(budget)
        if budget < len(labels):
            raise ValueError('Harmonic budget must permit a full-rank training feature Gram')
        if source_rank is not None and source_rank < 0:
            raise ValueError('source_rank must be nonnegative or None')
        if selector not in ('bss', 'panel-uniform', 'panel-conditioned'):
            raise ValueError('Unknown coordinate selector')
        h10, h20, _ = dense_fields(dense.initial_state, inputs)
        if budget >= n:
            self.metrics = [torch.eye(n, dtype=a0.dtype, device=a0.device)/n for _ in range(2)]
            self.metric_inverses = [torch.eye(n, dtype=a0.dtype, device=a0.device)*n]
            self.initial_state = [a0.clone(), w0.clone(), matrix0.clone(), labels.clone()]
            self.diagnostics = dict(branch='full_retention_uncompressed', requested_budget=budget,
                                    widths=[n, n], source_ranks=[n, n], certified_source_setup=False)
        else:
            if source_coefficients is None:
                raise ValueError('Compressed Harmonic needs all four offline source coefficient families')
            retained, truncation = {}, {}
            for name in ('h1', 'h2', 'delta1', 'delta2'):
                coefficient = source_coefficients[name].to(dtype=a0.dtype, device=a0.device)
                if coefficient.ndim != 2 or coefficient.shape[0] != n:
                    raise ValueError(f'Invalid Harmonic coefficient matrix for {name}')
                left, singular, right = torch.linalg.svd(coefficient, full_matrices=False)
                numerical_rank = int((singular > rank_tolerance*singular[0]).sum()) if len(singular) else 0
                count = numerical_rank if source_rank is None else min(source_rank, numerical_rank)
                retained[name] = left[:, :count]
                error = coefficient-left[:, :count]@(singular[:count, None]*right[:count])
                truncation[name] = dict(numerical_rank=numerical_rank, retained_rank=count,
                    relative_frobenius_error=float(error.norm()/coefficient.norm().clamp_min(1e-30)),
                    max_coefficient_error=float(error.abs().max()) if error.numel() else 0.)
            constant = torch.ones(n, 1, dtype=a0.dtype, device=a0.device)
            mandatory1 = torch.cat((constant, a0, h10), dim=1)
            mandatory2 = torch.cat((constant, h20, matrix0@h10), dim=1)
            optional1 = torch.cat((retained['h1'], retained['delta1'], matrix0.T@retained['delta2']), dim=1)
            optional2 = torch.cat((retained['h2'], retained['delta2'], matrix0@retained['h1']), dim=1)
            basis1, mandatory_error1 = _harmonic_source_basis(mandatory1, optional1)
            basis2, mandatory_error2 = _harmonic_source_basis(mandatory2, optional2)
            if selector == 'bss':
                selection1 = _harmonic_bss_metric(basis1)
                selection2 = _harmonic_bss_metric(basis2)
            else:
                trials = 4 if selector == 'panel-conditioned' else 1
                selection1 = _panel_coordinate_metric(basis1, budget, selection_seed, trials)
                selection2 = _panel_coordinate_metric(basis2, budget, selection_seed+1, trials)
                if selector == 'panel-conditioned' and max(
                        selection1[-1]['embedding_max'], selection2[-1]['embedding_max']) > 16:
                    raise ArithmeticError('Panel source embedding exceeds empirical condition gate 16')
            i1, metric1, inverse1, diagonal1, diagnostic1 = selection1
            i2, metric2, inverse2, diagonal2, diagnostic2 = selection2
            if max(len(i1), len(i2)) > budget:
                raise ValueError(f'Harmonic budget {budget} is insufficient: BSS retained '
                                 f'{len(i1)}/{len(i2)} rows at source ranks '
                                 f'{basis1.shape[1]}/{basis2.shape[1]}; decrease source_rank '
                                 'or increase budget. Mandatory initialization directions were preserved.')
            selected1, selected2 = basis1[i1], basis2[i2]
            core = basis2.T@(matrix0@basis1)/n
            mixer = selected2@core@(selected1.T@metric1)
            self.metrics = [metric1, metric2]
            # Only the incoming-layer inverse is needed for this two-layer
            # runtime. Diagonal comparison metrics are setup diagnostics.
            self.metric_inverses = [inverse1]
            self.initial_state = [a0[i1].clone(), torch.zeros(len(i2), dtype=a0.dtype, device=a0.device),
                                  mixer, labels.clone()]
            h1 = (self.initial_state[0]@inputs.T).tanh()
            h2 = (mixer@h1).tanh()
            paired_forward = mixer@retained['h1'][i1]-(matrix0@retained['h1'])[i2]
            paired_reverse = inverse1@(mixer.T@(metric2@retained['delta2'][i2])) \
                             -(matrix0.T@retained['delta2'])[i1]
            def maximum(value):
                return float(value.abs().max()) if value.numel() else 0.
            self.diagnostics = dict(branch=('empirical_spectral_setup_bss_runtime' if selector == 'bss'
                                           else 'empirical_spectral_setup_metric_runtime'),
                selector=selector, certified_source_setup=False,
                requested_budget=budget, source_rank_limit=source_rank, rank_tolerance=rank_tolerance,
                widths=[len(i1), len(i2)], source_ranks=[basis1.shape[1], basis2.shape[1]],
                selection=[diagnostic1, diagnostic2], coefficient_truncation=truncation,
                mandatory_source_errors=[mandatory_error1, mandatory_error2],
                initialized_feature_errors=[maximum(h1-h10[i1]), maximum(h2-h20[i2])],
                initialized_gram_error=maximum(h2.T@metric2@h2-h20.T@h20/n),
                paired_forward_action_error=maximum(paired_forward),
                paired_reverse_action_error=maximum(paired_reverse))
        self.fixed_scalars = sum(value.numel() for value in
                                 self.metrics+self.metric_inverses)
        # Fail explicitly on a missing feature gap. A ridge or pseudoinverse would
        # change the corrected-readout construction and is never silently used.
        _, _, gram = self._readout(self.initial_state, inputs, labels)
        eigenvalues = torch.linalg.eigvalsh(gram)
        self.diagnostics['initial_feature_gram_min'] = float(eigenvalues.min())
        self.diagnostics['initial_feature_gram_condition'] = float(eigenvalues.max()/eigenvalues.min())
        self.diagnostics['moving_scalars'] = sum(value.numel() for value in self.initial_state)
        self.diagnostics['fixed_scalars'] = self.fixed_scalars

    def _features(self, state, inputs):
        a, _, mixer, _ = state
        first = (a@inputs.T).tanh()
        return first, (mixer@first).tanh()

    def _readout(self, state, inputs, labels):
        _, w, _, deficit = state
        features = self._features(state, inputs)
        normalized = features[1]/math.sqrt(len(labels))
        gram = normalized.T@(self.metrics[1]@normalized)
        gram = (gram+gram.T)/2
        factor, info = torch.linalg.cholesky_ex(gram)
        if int(info) != 0:
            raise ArithmeticError('Harmonic training feature Gram is not positive definite; no ridge was added')
        correction = (labels-deficit)/math.sqrt(len(labels))-normalized.T@(self.metrics[1]@w)
        solution = torch.cholesky_solve(correction[:, None], factor).flatten()
        return w+normalized@solution, features, gram

    def rhs(self, state, inputs, labels):
        _, _, mixer, deficit = state
        readout, (h1, h2), _ = self._readout(state, inputs, labels)
        metric1, metric2 = self.metrics
        delta2 = (1-h2.square())*readout[:, None]
        delta1 = (1-h1.square())*(self.metric_inverses[0]@(mixer.T@(metric2@delta2)))
        scale = 2/len(labels)
        da = scale*(delta1*deficit)@inputs
        db = scale*(delta2*deficit)@(metric1@h1).T
        dw = scale*h2@deficit
        # Positive sample Gram, exactly the stated optimizer (not autodiff).
        kernel = h2.T@(metric2@h2)
        kernel = kernel+(delta1.T@(metric1@delta1))*(inputs@inputs.T)
        kernel = kernel+(delta2.T@(metric2@delta2))*(h1.T@(metric1@h1))
        return [da, dw, db, -scale*kernel@deficit]

    def predict(self, state, queries, inputs, labels):
        readout, _, _ = self._readout(state, inputs, labels)
        return (self.metrics[1]@readout)@self._features(state, queries)[1]

    def prepare_query(self, state, inputs, labels):
        """Refresh once; returned predictor retains only A, B and M_L w_hat."""
        a, _, mixer, _ = state
        coefficient = self.metrics[1]@self._readout(state, inputs, labels)[0]

        def predict(queries):
            return coefficient@(mixer@(a@queries.T).tanh()).tanh()

        return predict

    def runtime_checks(self, state, inputs, labels):
        readout, (h1, h2), gram = self._readout(state, inputs, labels)
        _, _, mixer, deficit = state
        metric1, metric2 = self.metrics
        delta2 = (1-h2.square())*readout[:, None]
        delta1 = (1-h1.square())*(self.metric_inverses[0]@(mixer.T@(metric2@delta2)))
        kernel = h2.T@(metric2@h2)+(delta1.T@(metric1@delta1))*(inputs@inputs.T)
        kernel = kernel+(delta2.T@(metric2@delta2))*(h1.T@(metric1@h1))
        da, dw, db, dc = self.rhs(state, inputs, labels)
        action = h2.T@(metric2@dw)
        action = action+(delta1*(metric1@(da@inputs.T))).sum(dim=0)
        action = action+(delta2*(metric2@(db@h1))).sum(dim=0)
        return dict(training_constraint_error=float(((metric2@readout)@h2-labels+deficit).abs().max()),
                    feature_gram_min=float(torch.linalg.eigvalsh(gram).min()),
                    update_gram_min=float(torch.linalg.eigvalsh((kernel+kernel.T)/2).min()),
                    update_gram_symmetry_error=float((kernel-kernel.T).abs().max()),
                    gram_action_error=float((dc+action).abs().max()))


@torch.no_grad()
def harmonic_small_checks(device='cpu'):
    """Small deterministic algebra and integrator checks; no empirical sweep."""
    device = torch.device(device)
    dtype = torch.float64
    generator = torch.Generator(device=device).manual_seed(11)
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]], dtype=dtype, device=device)
    labels = torch.tensor([.2, -.1, .3], dtype=dtype, device=device)
    dense = Dense(64, 2, 3, device)
    dense.initial_state = [value.to(dtype=dtype) for value in dense.initial_state]
    families = ('h1', 'h2', 'delta1', 'delta2')
    coefficients = {name: torch.randn(64, 5, generator=generator, dtype=dtype, device=device)
                    for name in families}
    compressed = Harmonic(dense, inputs, labels, coefficients, budget=63, source_rank=2)
    setup = compressed.diagnostics
    setup_errors = (setup['mandatory_source_errors']+setup['initialized_feature_errors']
                    +[setup['initialized_gram_error'], setup['paired_forward_action_error'],
                      setup['paired_reverse_action_error']]
                    +[item[key] for item in setup['selection']
                      for key in ('source_isometry_error', 'metric_inverse_error')])
    assert max(setup_errors) < 1e-11, setup
    for item in setup['selection']:
        assert 1-1e-10 <= item['embedding_min'] <= item['embedding_max'] <= 4+1e-10, item
        assert abs(item['constant_norm']-1) < 1e-11, item
        assert item['diagonal_mass'] <= 4+1e-10, item
    expected_fixed = 2*compressed.metrics[0].numel()+compressed.metrics[1].numel()
    assert compressed.fixed_scalars == expected_fixed
    assert len(compressed.metric_inverses) == 1
    assert not hasattr(compressed, 'diagonal_metrics')
    state, _, _ = integrate(compressed, inputs, labels, inputs, [0., .2], .01, 20.)
    evolving = compressed.runtime_checks(state, inputs, labels)
    assert evolving['training_constraint_error'] < 1e-11, evolving
    assert evolving['gram_action_error'] < 1e-11, evolving
    assert evolving['feature_gram_min'] > 0, evolving
    assert evolving['update_gram_min'] > -1e-11, evolving
    assert evolving['update_gram_symmetry_error'] < 1e-11, evolving

    restored = Harmonic.__new__(Harmonic)
    restored.metrics = [value.clone() for value in compressed.metrics]
    restored.metric_inverses = [value.clone() for value in compressed.metric_inverses]
    restored.initial_state = [value.clone() for value in state]
    queries = torch.stack((inputs[:, 1], -inputs[:, 0]), dim=1)
    prediction = compressed.predict(state, queries, inputs, labels)
    restarted = restored.predict(restored.initial_state, queries, inputs, labels)
    restart_error = float((prediction-restarted).abs().max())
    for actual, expected in zip(restored.rhs(restored.initial_state, inputs, labels),
                                compressed.rhs(state, inputs, labels)):
        restart_error = max(restart_error, float((actual-expected).abs().max()))
    ready = restored.prepare_query(restored.initial_state, inputs, labels)
    permutation = torch.tensor([2, 0, 1], device=device)
    query_error = float((ready(queries[permutation])-prediction[permutation]).abs().max())
    assert all(torch.is_tensor(cell.cell_contents) for cell in ready.__closure__)
    assert restart_error < 1e-11 and query_error < 1e-11, (restart_error, query_error)

    full = Harmonic(dense, inputs, labels, budget=64)
    arbitrary = [value+.03*torch.randn(value.shape, generator=generator, dtype=dtype, device=device)
                 for value in dense.initial_state]
    full_state = arbitrary+[labels-dense_fields(arbitrary, inputs)[2]]
    actual = full.rhs(full_state, inputs, labels)
    expected = dense.rhs(arbitrary, inputs, labels)
    rhs_error = max(float((a-b).abs().max()) for a, b in zip(actual[:3], expected))
    assert rhs_error < 1e-11, rhs_error
    refinement = []
    for step in (.1, .05):
        _, dense_predictions, _ = integrate(dense, inputs, labels, inputs, [0., 1.], step, 20.)
        final, full_predictions, _ = integrate(full, inputs, labels, inputs, [0., 1.], step, 20.)
        error = float(np.abs(dense_predictions-full_predictions).max())
        refinement.append(error)
        checks = full.runtime_checks(final, inputs, labels)
        assert checks['training_constraint_error'] < 1e-11, checks
    # RK4 constraint drift should decrease at fourth order until roundoff.
    assert refinement[1] <= refinement[0]/8+1e-13, refinement
    assert refinement[1] < 1e-9, refinement

    times = torch.tensor([0., .5, 1.], dtype=dtype, device=device)
    angles = torch.arange(12, dtype=dtype, device=device)*2*math.pi/12
    nodes = torch.stack((angles.cos(), angles.sin()), dim=1)
    values = torch.ones(3, 64, 12, dtype=dtype, device=device) \
             *(1+times[:, None, None])*angles.cos()[None, None, :]
    _, projection = harmonic_source_coefficients({name: values for name in families}, times, nodes,
                                                 time_degree=1, spatial_degree=1)
    projection_error = max(item['max_coordinate_error'] for item in projection['source_fit_errors'].values())
    assert projection_error < 1e-11, projection
    return dict(source_setup_max_abs=max(setup_errors), source_ranks=setup['source_ranks'],
                selected_widths=setup['widths'], runtime=evolving,
                full_retention_rhs_max_abs=rhs_error,
                full_retention_refinement_errors=refinement,
                source_projection_max_abs=projection_error,
                checkpoint_restart_max_abs=restart_error, passive_query_permutation_max_abs=query_error,
                fixed_scalars=compressed.fixed_scalars)


def small_checks(base, orthogonal):
    """Independent loss-gradient and reconstructed-matrix checks."""
    rng = np.random.default_rng(712)
    inputs = torch.tensor(rng.normal(size=(3, 2)))
    labels = torch.tensor(rng.normal(size=3))
    engine = orthogonal.MomentEngine(2, 9, 3, inputs, labels, lifted=True)
    state = engine.initial_state()
    state.A += torch.tensor(rng.normal(scale=.03, size=tuple(state.A.shape)))
    state.B += torch.tensor(rng.normal(scale=.03, size=tuple(state.B.shape)))
    left, right = engine.delta_factors(state)
    matrix = engine.W0 + left @ right.T
    state.h1 = (state.w @ inputs.T).tanh()
    state.h2 = (matrix @ state.h1).tanh()
    state.rho = rms(state.c @ state.h2 / engine.n - labels)
    dense = [v.detach().clone().requires_grad_() for v in (state.w, state.c, matrix)]
    loss = (dense_fields(dense, inputs)[2] - labels).square().mean()
    gradients = torch.autograd.grad(loss, dense)
    oracle = [-mobility * g for mobility, g in zip((9, 9, 1), gradients)]
    actual = dense_rhs(dense, inputs, labels)
    maximum = max(float((x-y).abs().max()) for x, y in zip(oracle, actual))
    velocity = engine.rhs(state)
    maximum = max(maximum, float((velocity.w-actual[0]).abs().max()),
                  float((velocity.c-actual[1]).abs().max()))
    dl, dr = engine._derivative_factors(state, velocity)
    dh1 = (1-state.h1.square()) * (velocity.w @ inputs.T)
    dh2 = (1-state.h2.square()) * (matrix @ dh1 + (dl @ dr.T) @ state.h1)
    maximum = max(maximum, float((dh1-velocity.h1).abs().max()),
                  float((dh2-velocity.h2).abs().max()))
    assert maximum < 1e-12, maximum
    prediction = engine.predict(state, inputs)
    assert torch.allclose(prediction, dense_fields(dense, inputs)[2], atol=1e-14, rtol=1e-14)
    return {"independent_gradient_and_matrix_max_abs": maximum}


class BoundedGaussianPackets(Dense):
    """Empirical covariance-balanced small network, with ordinary Dense flow.

    Training-only source features set the covariance of dependent Gaussian-action
    packets. This variance-reduction initialization does not preserve the adaptive
    Logarithmic posterior and carries no theorem guarantee. Only A, c and B remain
    after construction; source features, packets and factorizations are discarded.
    """

    @torch.no_grad()
    def __init__(self, source_width, width, inputs, seed, source_seed):
        if inputs.ndim != 2 or not len(inputs) or not inputs.shape[1]:
            raise ValueError('Packet initialization needs nonempty training inputs (m,d)')
        m, d = inputs.shape
        if width < m or source_width < m:
            raise ValueError('Packet and source widths must each be at least the training count')
        device, dtype = inputs.device, torch.float64
        training = inputs.detach().to(dtype=dtype)
        if not bool(torch.isfinite(training).all()):
            raise FloatingPointError('Packet training inputs contain nonfinite entries')
        generator = torch.Generator(device=device).manual_seed(seed)
        first = torch.randn(width, d, generator=generator, dtype=dtype, device=device)
        readout = torch.zeros(width, dtype=dtype, device=device)
        gaussian = torch.randn(width, width, generator=generator, dtype=dtype, device=device)/math.sqrt(width)
        source_generator = torch.Generator(device=device).manual_seed(source_seed)
        source_first = torch.randn(source_width, d, generator=source_generator, dtype=dtype, device=device)
        source_features = (source_first@training.T).tanh()
        covariance = source_features.T@source_features/source_width
        factor, info = torch.linalg.cholesky_ex(covariance)
        if int(info) != 0:
            raise ArithmeticError('Packet source Gram is not positive definite; no ridge is added')
        packet_gaussian = torch.randn(width, m, generator=source_generator, dtype=dtype, device=device)
        packet_basis, packet_triangular = torch.linalg.qr(packet_gaussian, mode='reduced')
        packet_basis *= torch.where(packet_triangular.diagonal() >= 0, 1., -1.)
        packets = math.sqrt(width)*packet_basis@factor.T
        features = (first@training.T).tanh()
        basis, triangular = torch.linalg.qr(features, mode='reduced')
        singular = torch.linalg.svdvals(triangular)
        tolerance = max(width, m)*torch.finfo(dtype).eps*float(singular[0])
        rank = int((singular > tolerance).sum())
        if rank != m:
            raise ArithmeticError('Packet small-network feature matrix lacks full column rank; no ridge is added')
        # (Z-GH) R^{-1} is a right triangular solve, not an explicit inverse.
        correction = torch.linalg.solve_triangular(
            triangular.T, (packets-gaussian@features).T, upper=False).T
        mixer = gaussian+correction@basis.T
        if not bool(torch.isfinite(mixer).all()):
            raise FloatingPointError('Packet initialization produced a nonfinite hidden matrix')
        eigenvalues = torch.linalg.eigvalsh(covariance)
        self.initial_state, self.fixed_scalars = [first, readout, mixer], 0
        self.diagnostics = dict(
            method='empirical_source_conditioned_covariance_balanced_small_network',
            claim_scope='dependent packets; not the adaptive Logarithmic decoder or its theorem',
            source_width=int(source_width), width=int(width), samples=m, dimension=d,
            seed=int(seed), source_seed=int(source_seed), construction_dtype=str(dtype),
            feature_rank=rank, feature_min_singular=float(singular[-1]),
            feature_condition=float(singular[0]/singular[-1]),
            source_gram_min=float(eigenvalues[0]), source_gram_condition=float(eigenvalues[-1]/eigenvalues[0]),
            initialized_action_max_abs=float((mixer@features-packets).abs().max()),
            initialized_covariance_max_abs=float((packets.T@packets/width-covariance).abs().max()),
            mixer_frobenius=float(mixer.norm()), moving_scalars=sum(value.numel() for value in self.initial_state))


def bounded_gaussian_packet_small_checks(device='cpu'):
    """Tiny algebra, inherited-gradient and checkpoint checks for the new model."""
    device, dtype = torch.device(device), torch.float64
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]], dtype=dtype, device=device)
    labels = torch.tensor([.2, -.1, .3], dtype=dtype, device=device)
    model = BoundedGaussianPackets(64, 16, inputs, 17, 29)
    first, readout, mixer = model.initial_state
    source_generator = torch.Generator(device=device).manual_seed(29)
    source_first = torch.randn(64, 2, generator=source_generator, dtype=dtype, device=device)
    source_features = (source_first@inputs.T).tanh()
    covariance = source_features.T@source_features/64
    packet_gaussian = torch.randn(16, 3, generator=source_generator, dtype=dtype, device=device)
    packet_basis, packet_triangular = torch.linalg.qr(packet_gaussian, mode='reduced')
    packet_basis *= torch.where(packet_triangular.diagonal() >= 0, 1., -1.)
    packets = 4*packet_basis@torch.linalg.cholesky(covariance).T
    features = (first@inputs.T).tanh()
    action_error = float((mixer@features-packets).abs().max())
    covariance_error = float((packets.T@packets/16-covariance).abs().max())
    assert max(action_error, covariance_error) < 1e-12, (action_error, covariance_error)
    assert model.diagnostics['feature_rank'] == 3 and bool(torch.isfinite(mixer.norm()))
    assert torch.count_nonzero(readout) == 0
    assert set(vars(model)) == {'initial_state', 'fixed_scalars', 'diagnostics'}
    assert all(isinstance(value, (int, float, str)) for value in model.diagnostics.values())
    assert model.fixed_scalars == 0 and sum(value.numel() for value in model.initial_state) == 16*(2+1)+16**2
    state = [value.clone().requires_grad_() for value in model.initial_state]
    state[1] = torch.linspace(-.2, .2, 16, dtype=dtype, device=device).requires_grad_()
    loss = (model.predict(state, inputs, inputs, labels)-labels).square().mean()
    gradients = torch.autograd.grad(loss, state)
    gradient_error = max(float((velocity+mobility*gradient).detach().abs().max())
                         for velocity, mobility, gradient in
                         zip(model.rhs(state, inputs, labels), (16, 16, 1), gradients))
    assert gradient_error < 1e-12, gradient_error
    with torch.no_grad():
        endpoint, _, _ = integrate_euler(model, inputs, labels, inputs, .01, 10., horizon=.05)
        restored = Dense.__new__(Dense)
        restored.initial_state, restored.fixed_scalars = [value.clone() for value in endpoint], 0
        restart_error = float((model.predict(endpoint, inputs, inputs, labels)
                               -restored.predict(restored.initial_state, inputs, inputs, labels)).abs().max())
        restart_error = max(restart_error, *(float((a-b).abs().max()) for a, b in zip(
            model.rhs(endpoint, inputs, labels), restored.rhs(restored.initial_state, inputs, labels))))
    assert restart_error == 0., restart_error
    return dict(action_max_abs=action_error, covariance_max_abs=covariance_error,
                inherited_gradient_max_abs=gradient_error, checkpoint_restart_max_abs=restart_error,
                retained_scalars=sum(value.numel() for value in model.initial_state), diagnostics=model.diagnostics)


@torch.no_grad()
def integrate_euler(model, inputs, labels, queries, step, seconds, horizon=None,
                    loss_target=None, max_steps=1_000_000, observation_every=100):
    """Bounded explicit Euler, preserving the caller's state/data precision.

    All blocks use the same pre-update RHS: ``state += h * model.rhs(state)``.
    A prescribed ``horizon`` takes precedence over loss stopping and is reached
    with one shortened final Euler step if necessary. Without a horizon, stop
    at the first sampled training MSE strictly below ``loss_target``. MSE is
    checked at most eight updates apart; queries are evaluated only every
    ``observation_every`` updates and at the actual initial/terminal states.

    Return ``(state, predictions, report)``. Rows of ``predictions`` correspond
    to ``report['times']`` and ``report['observation_steps']``. A wall/step cap
    returns a partial trajectory with its actual terminal time and stop reason;
    it does not extrapolate to the requested horizon. The wall budget includes
    observations and is capped at 300 seconds. A running device operation and
    the required terminal observation cannot be interrupted, so any overrun is
    reported. Only the current state/RHS and CPU query observations are retained.
    """
    step, seconds = float(step), float(seconds)
    if not math.isfinite(step) or step <= 0:
        raise ValueError('Euler step must be finite and positive')
    if not math.isfinite(seconds) or seconds <= 0:
        raise ValueError('Euler wall budget must be finite and positive')
    if isinstance(max_steps, bool) or not isinstance(max_steps, (int, np.integer)) or max_steps < 0:
        raise ValueError('Euler max_steps must be a nonnegative integer')
    if (isinstance(observation_every, bool)
            or not isinstance(observation_every, (int, np.integer)) or observation_every < 1):
        raise ValueError('Euler observation_every must be a positive integer')
    if horizon is not None:
        horizon = float(horizon)
        if not math.isfinite(horizon) or horizon < 0:
            raise ValueError('Euler horizon must be finite and nonnegative')
        ratio = horizon/step
        if not math.isfinite(ratio):
            raise ValueError('Euler horizon/step is too large')
        nearest = round(ratio)
        horizon_steps = (nearest if abs(ratio-nearest) <= 8*math.ulp(ratio)
                         else math.ceil(ratio))
    else:
        horizon_steps = None
    if loss_target is not None:
        loss_target = float(loss_target)
        if not math.isfinite(loss_target) or loss_target < 0:
            raise ValueError('Euler loss target must be finite and nonnegative')
    if inputs.ndim != 2 or labels.ndim != 1 or len(inputs) != len(labels) or not len(labels):
        raise ValueError('Euler expects nonempty inputs (m,d) and labels (m,)')
    if queries.ndim != 2 or queries.shape[1] != inputs.shape[1] or not len(queries):
        raise ValueError('Euler expects nonempty queries with the input dimension')
    device = inputs.device
    if not inputs.is_floating_point() or any(
            value.device != device or value.dtype != inputs.dtype for value in (labels, queries)):
        raise ValueError('Euler data must share one floating dtype and device')
    if not model.initial_state or any(
            not torch.is_tensor(value) or value.dtype != inputs.dtype or value.device != device
            for value in model.initial_state):
        raise ValueError('Euler initial state must share the data dtype and device')

    seconds = min(seconds, 300.)
    max_steps, observation_every = int(max_steps), int(observation_every)
    check_every = min(8, observation_every)
    synchronize(device)
    started = time.monotonic()
    baseline_bytes = torch.cuda.memory_allocated(device) if device.type == 'cuda' else None
    if device.type == 'cuda':
        torch.cuda.reset_peak_memory_stats(device)
    state = [value.detach().clone() for value in model.initial_state]
    if not all(bool(torch.isfinite(value).all()) for value in (inputs, labels, queries)):
        raise FloatingPointError('Euler data contain nonfinite entries')
    predictions, times, observation_steps, losses = [], [], [], []
    loss_check_steps, loss_check_times, loss_checks = [], [], []
    steps, current, last_step = 0, 0., 0.
    training_seconds = loss_seconds = query_seconds = refresh_seconds = 0.

    def check_training_loss():
        nonlocal loss_seconds
        check_started = time.monotonic()
        if not all(bool(torch.isfinite(value).all()) for value in state):
            raise FloatingPointError(f'Nonfinite Euler state at step {steps}, t={current:.9g}')
        prediction = model.predict(state, inputs, inputs, labels)
        if prediction.shape != labels.shape:
            raise ValueError('Euler training prediction must have the label shape')
        loss = float((prediction-labels).square().mean())
        if not math.isfinite(loss):
            raise FloatingPointError(f'Nonfinite Euler training MSE at step {steps}, t={current:.9g}')
        synchronize(device)
        loss_seconds += time.monotonic()-check_started
        loss_check_steps.append(steps)
        loss_check_times.append(current)
        loss_checks.append(loss)
        return loss

    def observe(loss):
        nonlocal query_seconds, refresh_seconds
        if observation_steps and observation_steps[-1] == steps:
            return
        refresh_started = time.monotonic()
        prepared = model.prepare_query(state, inputs, labels) if hasattr(model, 'prepare_query') else None
        synchronize(device)
        refresh_seconds += time.monotonic()-refresh_started
        query_started = time.monotonic()
        prediction = (prepared(queries) if prepared is not None
                      else model.predict(state, queries, inputs, labels))
        if prediction.shape != (len(queries),):
            raise ValueError('Euler query prediction must have shape (number_of_queries,)')
        if not bool(torch.isfinite(prediction).all()):
            raise FloatingPointError(f'Nonfinite Euler query prediction at step {steps}, t={current:.9g}')
        predictions.append(prediction.detach().cpu().numpy().copy())
        synchronize(device)
        query_seconds += time.monotonic()-query_started
        times.append(current)
        observation_steps.append(steps)
        losses.append(loss)

    def stopping_reason(loss):
        if time.monotonic()-started >= seconds:
            return 'wall_time_cap'
        if horizon_steps is not None and steps == horizon_steps:
            return 'horizon'
        if horizon is None and loss_target is not None and loss < loss_target:
            return 'loss_target'
        if steps == max_steps:
            return 'max_steps'
        return None

    loss = check_training_loss()
    observe(loss)
    reason = stopping_reason(loss)
    while reason is None:
        next_observation = (steps//observation_every+1)*observation_every
        block_end = min(steps+check_every, next_observation, max_steps)
        if horizon_steps is not None:
            block_end = min(block_end, horizon_steps)
        training_started = time.monotonic()
        while steps < block_end:
            if time.monotonic()-started >= seconds:
                break
            last_step = (horizon-steps*step if horizon_steps is not None and steps+1 == horizon_steps
                         else step)
            velocity = model.rhs(state, inputs, labels)
            if len(velocity) != len(state) or any(
                    derivative.shape != value.shape for value, derivative in zip(state, velocity)):
                raise ValueError('Euler RHS must provide one matching derivative per state block')
            # Finish every derivative before mutating any state block.
            for value, derivative in zip(state, velocity):
                value.add_(derivative, alpha=last_step)
            del velocity, derivative
            steps += 1
            current = horizon if horizon_steps is not None and steps == horizon_steps else steps*step
        synchronize(device)
        training_seconds += time.monotonic()-training_started
        loss = check_training_loss()
        reason = stopping_reason(loss)
        if steps % observation_every == 0 or reason is not None:
            observe(loss)
        # Query work belongs to the wall budget as well as the training work.
        if time.monotonic()-started >= seconds:
            reason = 'wall_time_cap'
    observe(loss)
    synchronize(device)
    elapsed = time.monotonic()-started
    peak_bytes = torch.cuda.max_memory_allocated(device) if device.type == 'cuda' else None
    return state, np.stack(predictions), dict(
        method='explicit_euler', dtype=str(inputs.dtype), step=step, last_step=last_step,
        requested_horizon=horizon, actual_horizon=current, steps=steps,
        times=times, observation_steps=observation_steps, losses=losses,
        final_training_mse=loss, loss_target=loss_target,
        loss_target_reached=(loss < loss_target if loss_target is not None else None),
        horizon_reached=(steps == horizon_steps if horizon_steps is not None else None),
        stop_reason=reason, complete=reason in ('horizon', 'loss_target'),
        max_steps=max_steps, observation_every=observation_every,
        loss_check_every_at_most=check_every, loss_check_steps=loss_check_steps,
        loss_check_times=loss_check_times, loss_checks=loss_checks,
        seconds=elapsed, wall_time_cap_seconds=seconds, within_wall_time_cap=elapsed <= seconds,
        training_seconds=training_seconds, training_loss_seconds=loss_seconds,
        query_seconds=query_seconds, query_refresh_seconds=refresh_seconds,
        query_timing_scope='whole sparse query batches plus CPU copies, after readout refresh',
        seconds_per_step=training_seconds/max(1, steps),
        moving_scalars=sum(value.numel() for value in state),
        fixed_scalars=int(model.fixed_scalars), process_peak_cuda_bytes=peak_bytes,
        incremental_peak_cuda_bytes=(peak_bytes-baseline_bytes if peak_bytes is not None else None),
        peak_scope='whole process, including other resident references; not isolated model memory')


@torch.no_grad()
def euler_small_checks(device='cpu'):
    """Deterministic tiny-Dense checks; no data loading or scientific rollout."""
    device, dtype = torch.device(device), torch.float64
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]], dtype=dtype, device=device)
    labels = torch.tensor([.7, -.4, .3], dtype=dtype, device=device)
    queries = torch.tensor([[0., 1.], [-1., 0.]], dtype=dtype, device=device)
    model = Dense(7, 2, 17, device)
    model.initial_state = [value.to(dtype=dtype) for value in model.initial_state]
    model.initial_state[1] = torch.linspace(-.3, .3, 7, dtype=dtype, device=device)
    original = [value.clone() for value in model.initial_state]
    manual = [value.clone() for value in original]
    for h in (.01, .01, .01, .005):
        velocity = dense_rhs(manual, inputs, labels)
        manual = [value+h*derivative for value, derivative in zip(manual, velocity)]
    actual, prediction, report = integrate_euler(
        model, inputs, labels, queries, .01, 10., horizon=.035,
        loss_target=10., observation_every=3)
    manual_error = max(float((a-b).abs().max()) for a, b in zip(actual, manual))
    assert manual_error < 1e-13, manual_error
    assert report['steps'] == 4 and report['observation_steps'] == [0, 3, 4], report
    assert report['times'] == [0., .03, .035] and report['stop_reason'] == 'horizon', report
    assert abs(report['last_step']-.005) < 1e-15 and report['horizon_reached'], report
    assert all(torch.equal(a, b) for a, b in zip(model.initial_state, original))
    assert all(not value.requires_grad and value.grad_fn is None for value in actual)
    query_error = float(np.abs(prediction[-1]-model.predict(manual, queries, inputs, labels).cpu().numpy()).max())
    assert query_error < 1e-13, query_error

    endpoints = []
    for h in (.04, .02, .01):
        endpoint, _, info = integrate_euler(
            model, inputs, labels, queries, h, 10., horizon=.4, observation_every=100)
        assert info['actual_horizon'] == .4 and info['horizon_reached'], info
        endpoints.append(torch.cat([value.flatten() for value in endpoint]))
    differences = [float((a-b).norm()) for a, b in zip(endpoints[:-1], endpoints[1:])]
    ratio = differences[0]/differences[1]
    assert 1.8 < ratio < 2.2, (differences, ratio)

    initial_loss = float((model.predict(original, inputs, inputs, labels)-labels).square().mean())
    _, _, eight = integrate_euler(
        model, inputs, labels, queries, .01, 10., max_steps=8, observation_every=100)
    assert eight['final_training_mse'] < initial_loss, eight
    target = (initial_loss+eight['final_training_mse'])/2
    _, _, stopped = integrate_euler(
        model, inputs, labels, queries, .01, 10., loss_target=target,
        max_steps=16, observation_every=100)
    assert stopped['stop_reason'] == 'loss_target' and stopped['steps'] == 8, stopped
    assert stopped['observation_steps'] == [0, 8] and stopped['loss_target_reached'], stopped
    _, _, capped = integrate_euler(
        model, inputs, labels, queries, .01, 10., horizon=1., max_steps=2, observation_every=100)
    assert capped['stop_reason'] == 'max_steps' and not capped['horizon_reached'], capped
    assert capped['times'] == [0., .02] and not capped['complete'], capped
    _, _, zero = integrate_euler(
        model, inputs, labels, queries, .01, 10., horizon=0., observation_every=100)
    assert zero['steps'] == 0 and zero['times'] == [0.] and zero['horizon_reached'], zero
    return dict(manual_euler_max_abs=manual_error, terminal_query_max_abs=query_error,
                step_halving_state_differences=differences, step_halving_ratio=ratio,
                threshold_stop_steps=stopped['steps'], step_cap_terminal_time=capped['actual_horizon'])


def validation_main(argv):
    parser = argparse.ArgumentParser(description='Fresh empirical validation; no legacy imports')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--width', type=int, default=512)
    parser.add_argument('--dimension', type=int, default=2)
    parser.add_argument('--samples', type=int, default=7)
    parser.add_argument('--queries', type=int, default=256)
    parser.add_argument('--seed', type=int, default=101)
    parser.add_argument('--data-seed', type=int, default=47)
    parser.add_argument('--horizon', type=float, default=20.)
    parser.add_argument('--step', type=float, default=.125)
    parser.add_argument('--per-run-seconds', type=float, default=120.)
    parser.add_argument('--task', choices=('toy', 'digits'), default='toy')
    parser.add_argument('--raw-images', action='store_true', help='Use all 64 pixels, with norm scaling but no PCA')
    parser.add_argument('--tuning-samples', type=int, default=64,
                        help='Digits tuning split; zero reserves all nontraining images for evaluation')
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--refine', action='store_true')
    parser.add_argument('--small-width', type=int, default=0)
    parser.add_argument('--lora-rank', type=int, default=0)
    parser.add_argument('--lora-step', type=float, default=.01)
    parser.add_argument('--lora-multiplier', type=float, default=1.)
    parser.add_argument('--harmonic-budget', type=int, default=0)
    parser.add_argument('--source-rank', type=int, default=8)
    parser.add_argument('--time-degree', type=int, default=3)
    parser.add_argument('--spatial-degree', type=int, default=3)
    parser.add_argument('--time-nodes', type=int, default=9)
    parser.add_argument('--spatial-nodes', type=int, default=64)
    parser.add_argument('--log-probe', action='store_true')
    parser.add_argument('--log-steps', type=int, default=4)
    parser.add_argument('--log-step', type=float, default=.125)
    parser.add_argument('--log-noise', type=float, default=.01)
    parser.add_argument('--log-queries', type=int, default=8)
    parser.add_argument('--log-all-times', action='store_true', help='Observe every prescribed decoder panel')
    args = parser.parse_args(argv)
    if args.raw_images and (args.task != 'digits' or args.dimension != 64):
        parser.error('--raw-images requires --task digits --dimension 64')
    if args.tuning_samples < 0:
        parser.error('--tuning-samples must be nonnegative')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    checks = independent_checks(args.device)
    if args.check_only:
        checks['harmonic'] = harmonic_small_checks('cpu')
        checks['logarithmic'] = logarithmic_small_checks()
    config = {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()}
    report = dict(config=config, checks=checks, source_sha256=sha(Path(__file__).read_bytes()),
                  python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
                  device=(torch.cuda.get_device_name(args.device) if args.device.startswith('cuda') else 'CPU'),
                  metric='maximum over recorded physical times of unseen-input RMS',
                  finite_scope='not an all-time or whole-sphere supremum or an asymptotic theorem',
                  complete=False, runs={})
    save_json(args.out/'report.json', report)
    if args.check_only:
        print(json.dumps(checks), flush=True)
        return
    partition = 'pilot' if args.seed in (101, 102) else 'test'
    inputs, labels, queries, truth = validation_data(args.dimension, args.samples, args.queries,
        args.data_seed, args.device, args.task, partition, args.raw_images, args.tuning_samples)
    times = sorted(set(t for t in [0., .5, 1., 2., 5., 10., 20., args.horizon] if t <= args.horizon))
    if args.log_probe and args.log_all_times:
        times = sorted(set(times + [index*args.log_step for index in range(args.log_steps+1)
                                     if index*args.log_step <= args.horizon+1e-10]))
    report.update(times=times, query_partition=partition, training_rank=int(torch.linalg.matrix_rank(inputs)),
                  label_rms=float(rms(labels)), query_count=len(queries),
                  train_inputs_sha256=array_sha(inputs.cpu().numpy()),
                  test_inputs_sha256=array_sha(queries.cpu().numpy()),
                  preprocessing=('raw pixels, per-image unit-norm scaling, no PCA' if args.raw_images
                                 else 'training-only PCA and unit-norm scaling' if args.task == 'digits'
                                 else 'unit sphere directions'))
    arrays = dict(times=times, train_inputs=inputs.cpu().numpy(), train_labels=labels.cpu().numpy(),
                  query_inputs=queries.cpu().numpy(), query_labels=truth.cpu().numpy())
    models = [('dense', Dense(args.width, args.dimension, args.seed, args.device)),
              ('dense_iid', Dense(args.width, args.dimension, args.seed+10000, args.device))]
    if args.small_width:
        models.append(('small_dense', Dense(args.small_width, args.dimension, args.seed+20000, args.device)))
    if args.lora_rank > 0:
        models.append(('lora', LoRA(models[0][1], args.lora_rank, args.seed+30000, args.lora_multiplier)))
    try:
        if args.harmonic_budget:
            synchronize(inputs.device)
            warmup_started = time.monotonic()
            if inputs.device.type == 'cuda':
                torch.cuda.reset_peak_memory_stats(inputs.device)
            coefficients, setup_info = collect_harmonic_sources(models[0][1], inputs, labels, args)
            synchronize(inputs.device)
            assembly_started = time.monotonic()
            harmonic = Harmonic(models[0][1], inputs, labels, coefficients,
                                args.harmonic_budget, source_rank=args.source_rank)
            synchronize(inputs.device)
            setup_info['assembly_seconds'] = time.monotonic()-assembly_started
            setup_info['diagnostics'] = harmonic.diagnostics
            setup_info['seconds_total_after_dense_allocation'] = time.monotonic()-warmup_started
            setup_info['whole_process_peak_cuda_bytes'] = (torch.cuda.max_memory_allocated(inputs.device)
                                                           if inputs.device.type == 'cuda' else None)
            setup_info['peak_scope'] = 'source rollout, spectral fit and assembly; includes other resident references'
            report['harmonic_setup'] = setup_info
            del coefficients
            models.append(('harmonic', harmonic))
            budget = sum(v.numel() for v in harmonic.initial_state) + harmonic.fixed_scalars
            matched_width = int((math.sqrt((args.dimension+1)**2+4*budget)-args.dimension-1)/2)
            models.append(('matched_dense', Dense(matched_width, args.dimension, args.seed+20000, args.device)))
            report['matched_budget'] = dict(target_total_scalars=budget, dense_width=matched_width,
                                           dense_total_scalars=matched_width**2+matched_width*(args.dimension+1))
            if args.lora_rank == -1:
                moving = sum(v.numel() for v in harmonic.initial_state)
                rank = (moving-args.width*(args.dimension+1))//(2*args.width)
                if rank < 1:
                    report['lora_matching'] = dict(feasible=False, reason='Dense outer layers exhaust moving-state budget')
                else:
                    models.append(('lora', LoRA(models[0][1], min(rank, args.width),
                                                args.seed+30000, args.lora_multiplier)))
                    report['lora_matching'] = dict(feasible=True, target_moving_scalars=moving,
                        actual_moving_scalars=args.width*(args.dimension+1)+2*args.width*rank,
                        rank=rank, fixed_dense_scalars=args.width**2,
                        scope='moving-state matched, not total-state matched')
        for name, model in models:
            with torch.no_grad():
                model_step = args.lora_step if name == 'lora' else args.step
                final, prediction, info = integrate(model, inputs, labels, queries, times,
                                                    model_step, args.per_run_seconds)
                arrays[name] = prediction
                info['test_label_rms'] = float(rms(torch.as_tensor(prediction[-1], device=args.device)-truth))
                if args.task == 'digits':
                    info['test_accuracy'] = float((torch.as_tensor(prediction[-1], device=args.device).sign() == truth).double().mean())
                if name == 'dense':
                    before = dense_fields(model.initial_state, queries)[1]
                    after = dense_fields(final, queries)[1]
                    info['feature_rms_movement'] = float(rms(after-before))
                    info['relative_feature_gram_change'] = float((after.T@after-before.T@before).norm()/(before.T@before).norm())
                    arrays['frozen_ntk'] = frozen_predictions(model, inputs, labels, queries, times)
                if args.refine:
                    fine_state, fine, fine_info = integrate(model, inputs, labels, queries, times,
                                                   model_step/2, args.per_run_seconds)
                    arrays[name+'_fine'] = fine
                    info['refinement'] = trajectory_rms(prediction, fine)
                    info['refinement_seconds'] = fine_info['seconds']
                    arrays[name+'_coarse'] = prediction
                    arrays[name] = fine
                    final = fine_state
                    info['test_label_rms'] = float(rms(torch.as_tensor(fine[-1], device=args.device)-truth))
                    if args.task == 'digits':
                        info['test_accuracy'] = float((torch.as_tensor(fine[-1], device=args.device).sign() == truth).double().mean())
                if name == 'harmonic':
                    info['runtime_checks'] = model.runtime_checks(final, inputs, labels)
                report['runs'][name] = info
                print(json.dumps(dict(event='complete', model=name, **info)), flush=True)
                save_json(args.out/'report.json', report)
        report['dense_variability'] = trajectory_rms(arrays['dense_iid'], arrays['dense'])
        denominator = report['dense_variability']['max_time_rms']
        report['comparisons'] = {}
        for name in ['frozen_ntk', 'small_dense', 'matched_dense', 'lora', 'harmonic']:
            if name in arrays:
                comparison = trajectory_rms(arrays[name], arrays['dense'])
                comparison['ratio_to_dense_pair'] = comparison['max_time_rms']/denominator if denominator > 1e-14 else None
                sensitivity = report['runs']['dense'].get('refinement', {}).get('max_time_rms')
                iid_sensitivity = report['runs']['dense_iid'].get('refinement', {}).get('max_time_rms')
                own_sensitivity = 0. if name == 'frozen_ntk' else report['runs'][name].get('refinement', {}).get('max_time_rms')
                combined = sensitivity + own_sensitivity if sensitivity is not None and own_sensitivity is not None else None
                pair_sensitivity = sensitivity + iid_sensitivity if sensitivity is not None and iid_sensitivity is not None else None
                comparison['combined_numerical_sensitivity'] = combined
                comparison['dense_pair_numerical_sensitivity'] = pair_sensitivity
                comparison['numerically_resolved'] = bool(combined is not None and pair_sensitivity is not None
                    and max(combined, pair_sensitivity) <= .1*denominator)
                comparison['comparability_pass'] = bool(comparison['numerically_resolved'] and
                                                       denominator > 1e-14 and comparison['ratio_to_dense_pair'] <= 3.)
                report['comparisons'][name] = comparison
        if args.log_probe:
            log_indices = [index for index, t in enumerate(times)
                           if t <= args.log_steps*args.log_step+1e-10
                           and abs(t/args.log_step-round(t/args.log_step)) < 1e-9]
            log_steps = [int(round(times[index]/args.log_step)) for index in log_indices]
            log_info, log_prediction = logarithmic_probe(
                inputs, labels, queries[:args.log_queries], args.width, args.seed+50000,
                args.log_steps, args.log_step, args.log_noise, args.device, args.per_run_seconds,
                capture_steps=log_steps)
            report['logarithmic_probe'] = log_info
            if log_prediction is not None:
                arrays['logarithmic'] = log_prediction
                arrays['logarithmic_times'] = np.asarray(times)[log_indices]
                count = log_prediction.shape[1]
                reference = arrays['dense'][log_indices, :count]
                variability = trajectory_rms(arrays['dense_iid'][log_indices, :count], reference)
                comparison = trajectory_rms(log_prediction, reference)
                scale = variability['max_time_rms']
                comparison['ratio_to_dense_pair'] = comparison['max_time_rms']/scale if scale > 1e-14 else None
                comparison['scope'] = 'recorded times and query subset only; empirical finite Euler program'
                pair_sensitivity = (sum(trajectory_rms(arrays[name][log_indices, :count],
                    arrays[name+'_coarse'][log_indices, :count])['max_time_rms']
                    for name in ('dense', 'dense_iid')) if args.refine else None)
                comparison['dense_pair_numerical_sensitivity'] = pair_sensitivity
                comparison['dense_reference_numerically_resolved'] = bool(args.refine and
                    pair_sensitivity < .1*scale)
                comparison['comparability_pass'] = bool(comparison['dense_reference_numerically_resolved'] and
                    log_info['replay_passed'] and scale > 1e-14 and comparison['ratio_to_dense_pair'] <= 3.)
                log_info['dense_variability_same_queries'] = variability
                log_info['comparison'] = comparison
                if args.task == 'digits':
                    log_info['test_accuracy'] = float(np.mean(np.sign(log_prediction[-1]) == truth[:count].cpu().numpy()))
                report['comparisons']['logarithmic'] = comparison
                matched_budget = (log_info['retained']['numerical_words']
                                  - log_info['retained']['parts']['training_data'])
                width = int((math.sqrt((args.dimension+1)**2+4*matched_budget)-args.dimension-1)/2)
                control = Dense(width, args.dimension, args.seed+60000, args.device)
                with torch.no_grad():
                    _, control_prediction, control_info = integrate(
                        control, inputs, labels, queries[:count], np.asarray(times)[log_indices],
                        args.step, args.per_run_seconds)
                    if args.refine:
                        arrays['log_matched_dense_coarse'] = control_prediction
                        _, control_fine, fine_info = integrate(
                            control, inputs, labels, queries[:count], np.asarray(times)[log_indices],
                            args.step/2, args.per_run_seconds)
                        control_info['refinement'] = trajectory_rms(control_prediction, control_fine)
                        control_info['refinement_seconds'] = fine_info['seconds']
                        arrays['log_matched_dense_fine'] = control_fine
                        control_prediction = control_fine
                control_info.update(width=width, target_model_words=matched_budget)
                control_info['smaller_than_dense_reference'] = bool(width < args.width)
                if args.task == 'digits':
                    control_info['test_accuracy'] = float(np.mean(np.sign(control_prediction[-1]) == truth[:count].cpu().numpy()))
                report['runs']['log_matched_dense'] = control_info
                arrays['log_matched_dense'] = control_prediction
                control_comparison = trajectory_rms(control_prediction, reference)
                control_comparison['ratio_to_dense_pair'] = control_comparison['max_time_rms']/scale if scale > 1e-14 else None
                report['comparisons']['log_matched_dense'] = control_comparison
            print(json.dumps(dict(event='logarithmic_probe', **log_info)), flush=True)
        report['requested_methods_completed'] = bool(not args.log_probe or report['logarithmic_probe']['completed'])
        report['complete'] = True
    except Exception as error:
        report['failure'] = dict(type=type(error).__name__, message=str(error))
        raise
    finally:
        np.savez_compressed(args.out/'trajectories.npz', **arrays)
        save_json(args.out/'report.json', report)
    print(json.dumps(dict(event='summary', dense_variability=report['dense_variability'],
                          comparisons=report['comparisons'])), flush=True)


@torch.no_grad()
def capture(order, level, arrays, schedule, args, base, orthogonal):
    started = time.monotonic()
    name = f"{'dense' if order == 0 else 'memory_' + str(order)}_level{level}"
    inputs = torch.tensor(arrays["train_inputs"], device=args.device)
    labels = torch.tensor(arrays["train_labels"], device=args.device)
    angles = arrays["history_angles"]
    queries = torch.tensor(np.column_stack((np.cos(angles), np.sin(angles))), device=args.device)
    engine = orthogonal.MomentEngine(2, 2048, max(1, order), inputs, labels,
                                    device=args.device, lifted=True)
    state = engine.initial_state()
    for key, value in (("w", state.w), ("c", state.c), ("M", engine.W0)):
        assert array_sha(value.cpu().numpy()) == INITIAL_HASHES[key], key
    initial_matrix = engine.W0
    if order == 0:
        state = [state.w, state.c, initial_matrix.clone()]
    rtol, atol = 6.25e-5 / 4**level, 6.25e-7 / 4**level

    def predict(s):
        chunks = []
        for q in queries.split(256 if order == 0 else 512):
            pred = dense_fields(s, q)[2] if order == 0 else engine.predict(s, q)
            chunks.append(pred.cpu().numpy())
        return np.concatenate(chunks)

    def loss(s):
        pred = (dense_fields(s, inputs)[2] if order == 0 else s.c @ s.h2 / 2048)
        return float((pred-labels).square().mean())

    def trial(s, step):
        if order == 0:
            first = dense_rhs(s, inputs, labels)
            euler = [v+step*f for v, f in zip(s, first)]
            second = dense_rhs(euler, inputs, labels)
            candidate = [v+.5*step*(f+g) for v, f, g in zip(s, first, second)]
            ratios = [rms(c-b)/(atol+rtol*torch.maximum(rms(a), rms(c)))
                      for a, b, c in zip(s[:2], euler[:2], candidate[:2])]
            scale = torch.maximum((s[2]-initial_matrix).norm(),
                                  (candidate[2]-initial_matrix).norm()).clamp_min(1.)
            ratios.append((candidate[2]-euler[2]).norm()/(atol+rtol*scale))
        else:
            first = engine.rhs(s)
            euler = s.add_scaled(first, step)
            second = engine.rhs(euler)
            candidate = base.linear_combination((1., step/2, step/2), (s, first, second))
            ratios = [rms(c-b)/(atol+rtol*torch.maximum(rms(a), rms(c)).clamp_min(1.))
                      for a, b, c in zip(s.tensors(), euler.tensors(), candidate.tensors())]
            lc, rc = engine.delta_factors(candidate)
            le, re = engine.delta_factors(euler)
            l0, r0 = engine.delta_factors(s)
            numerator = base.factor_frobenius(torch.cat((lc-le, le), 1), torch.cat((rc, rc-re), 1))
            scale = torch.maximum(base.factor_frobenius(l0, r0), base.factor_frobenius(lc, rc)).clamp_min(1.)
            ratios.append(numerator/(atol+rtol*scale))
        return candidate, float(torch.stack(ratios).max())

    t, step, accepted, rejected = 0., .05, 0, 0
    observed, predictions, losses, physical_losses, drift = [0.], [predict(state)], [loss(state)], [], []
    current_loss = losses[0]
    last_report = time.monotonic()
    for target in schedule[1:]:
        while t < target - 1e-12:
            if time.monotonic()-started > args.per_run_seconds or accepted+rejected >= 30000:
                np.savez_compressed(args.out/(name+"_partial.npz"), times=observed, predictions=predictions)
                raise RuntimeError(f"Resource cap in {name} at t={t}; partial data retained")
            h = min(step, 2., float(target)-t)
            if h < 1e-9:
                raise RuntimeError(f"Step underflow in {name}")
            candidate, error = trial(state, h)
            next_loss = loss(candidate)
            finite = math.isfinite(error) and math.isfinite(next_loss)
            decreasing = order != 0 or next_loss <= current_loss*(1+1e-8)+1e-12
            if not finite or error > 1 or not decreasing:
                rejected += 1
                step = h*(max(.1, min(.5, .9/math.sqrt(max(error, 1e-16)))) if finite else .1)
                continue
            state, current_loss = candidate, next_loss
            t = float(target) if abs(t+h-target) < 1e-12 else t+h
            accepted += 1
            step = h*max(.5, min(2., .9/math.sqrt(max(error, 1e-16))))
            if time.monotonic()-last_report > 20:
                print(json.dumps(dict(event="progress", model=name, t=t, steps=accepted)), flush=True)
                last_report = time.monotonic()
        observed.append(float(target))
        predictions.append(predict(state))
        losses.append(current_loss)
        if order:
            physical_losses.append(float((engine.predict(state, inputs)-labels).square().mean()))
            diag = engine.lift_diagnostics(state)
            drift.append({k:float(v) for k,v in diag.items()})
    observed, predictions = np.asarray(observed), np.asarray(predictions)
    assert np.array_equal(observed, schedule)
    assert predictions.shape == (len(schedule), 2048) and np.isfinite(predictions).all()
    result = dict(model=name, order=order, level=level, rtol=rtol, atol=atol,
                  accepted=accepted, rejected=rejected, last_time=t, final_loss=current_loss,
                  seconds=time.monotonic()-started, prediction_sha256=array_sha(predictions),
                  max_activation_drift=max((max(d['h1_max'], d['h2_max']) for d in drift), default=0.))
    np.savez_compressed(args.out/(name+".npz"), times=observed, predictions=predictions,
                        losses=losses, physical_losses=physical_losses)
    save_json(args.out/(name+".json"), result)
    print(json.dumps(dict(event="complete", **result)), flush=True)
    return predictions, result


class _LogarithmicBudget(RuntimeError):
    pass


class _LogarithmicTape:
    """Empirical FC.15--55 row program; no saved future scalar answers.

    The certified bit/Toeplitz backends are replaced explicitly by float64 and
    counter-seeded Box--Muller packets. Nodes contain immutable creation-time
    coefficients. Dense row values exist only in source setup; selected values
    are cached in compact training; passive queries reevaluate row blocks.
    """

    def __init__(self, width, seed, deadline, rows=None, metric=None, stream=False):
        self.width, self.seed, self.deadline = int(width), int(seed), deadline
        self.rows = np.arange(width, dtype=np.int64) if rows is None else np.asarray(rows, dtype=np.int64)
        self.metric, self.stream = metric, stream
        self.nodes, self.values, self.metric_values = [], [], {}
        self.pairs, self.root_count = {}, 0
        self.max_stream_words, self.stream_passes = 0, 0

    def check(self):
        if time.monotonic() > self.deadline:
            raise _LogarithmicBudget("Logarithmic finite-program wall-clock cap reached")

    def root_values(self, root, rows):
        # A conventional counter-based PRNG, not the paper's proved space PRG.
        mask = (1 << 64) - 1
        offset = (self.seed + (int(root) + 1) * 0xD2B74407B1CE6E93) & mask
        with np.errstate(over='ignore'):
            key = np.asarray(rows, dtype=np.uint64) + np.uint64(offset)

            def mix(value):
                value = value + np.uint64(0x9E3779B97F4A7C15)
                value = (value ^ (value >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9)
                value = (value ^ (value >> np.uint64(27))) * np.uint64(0x94D049BB133111EB)
                return value ^ (value >> np.uint64(31))

            first, second = mix(key), mix(key ^ np.uint64(0xA0761D6478BD642F))
        u = ((first >> np.uint64(11)).astype(np.float64) + .5) * 2.**-53
        v = ((second >> np.uint64(11)).astype(np.float64) + .5) * 2.**-53
        return np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * v)

    def _append(self, op, parents=(), coefficients=(), root=-1):
        self.check()
        parents = tuple(int(i) for i in parents)
        coefficients = np.asarray(coefficients, dtype=np.float64).copy()
        coefficients.flags.writeable = False
        node = (op, parents, coefficients, int(root))
        index = len(self.nodes)
        self.nodes.append(node)
        if not self.stream:
            if len(self.rows) * len(self.nodes) > 24_000_000:
                raise _LogarithmicBudget("Source/selected field cache exceeded 24 million float64 values")
            self.values.append(self._node_value(node, self.values, self.rows))
        return index

    def _node_value(self, node, values, rows):
        op, parents, coefficients, root = node
        if op == 'root':
            return self.root_values(root, rows)
        if op == 'constant':
            return np.full(len(rows), float(coefficients[0]))
        if op == 'affine':
            result = np.zeros(len(rows), dtype=np.float64)
            for parent, coefficient in zip(parents, coefficients):
                result += coefficient * values[parent]
            return result
        if op == 'tanh':
            return np.tanh(values[parents[0]])
        if op == 'gate':
            return 1 - values[parents[0]] ** 2
        if op == 'product':
            return values[parents[0]] * values[parents[1]]
        raise RuntimeError(f"Unknown Logarithmic row operation {op}")

    def root(self):
        root = self.root_count
        self.root_count += 1
        return self._append('root', root=root)

    def constant(self, value):
        return self._append('constant', coefficients=[value])

    def affine(self, parents, coefficients):
        return self._append('affine', parents, coefficients)

    def unary(self, op, parent):
        return self._append(op, [parent])

    def product(self, left, right):
        return self._append('product', [left, right])

    def evaluate_rows(self, rows):
        self.check()
        values = np.empty((len(self.nodes), len(rows)), dtype=np.float64)
        # Includes row IDs and a conservative allowance for simultaneous
        # Box--Muller/hash/affine-operation temporary block vectors.
        self.max_stream_words = max(self.max_stream_words, values.size + 32 * len(rows))
        for index, node in enumerate(self.nodes):
            if index % 128 == 0:
                self.check()
            values[index] = self._node_value(node, values, rows)
        return values

    def pair_many(self, pairs):
        self.check()
        keys = [(min(int(a), int(b)), max(int(a), int(b))) for a, b in pairs]
        missing = list(dict.fromkeys(key for key in keys if key not in self.pairs))
        if missing and self.stream:
            totals = np.zeros(len(missing), dtype=np.float64)
            # Full empirical row reduction: selected metrics are never used here.
            for start in range(0, self.width, 128):
                rows = np.arange(start, min(start + 128, self.width), dtype=np.int64)
                values = self.evaluate_rows(rows)
                for index, (left, right) in enumerate(missing):
                    totals[index] += np.dot(values[left], values[right])
                del values
            self.stream_passes += 1
            self.pairs.update(zip(missing, totals / self.width))
        elif missing:
            for left, right in missing:
                if self.metric is None:
                    value = np.dot(self.values[left], self.values[right]) / self.width
                else:
                    if right not in self.metric_values:
                        self.metric_values[right] = self.metric @ self.values[right]
                    value = np.dot(self.values[left], self.metric_values[right])
                self.pairs[left, right] = float(value)
        return np.asarray([self.pairs[key] for key in keys], dtype=np.float64)

    def pair(self, left, right):
        return float(self.pair_many([(left, right)])[0])

    def gram(self, left, right):
        return self.pair_many([(a, b) for a in left for b in right]).reshape(len(left), len(right))

    def fork_query(self):
        query = _LogarithmicTape(self.width, self.seed, self.deadline, rows=[], stream=True)
        query.nodes = list(self.nodes)
        query.root_count = self.root_count
        query.pairs = dict(self.pairs)
        return query


class _LogarithmicGaussian:
    """Both orientations of the noisy Gaussian posterior, FC.28--38."""

    def __init__(self, tape, noise):
        if noise <= 0:
            raise ValueError('Logarithmic Gaussian observation noise must be positive')
        self.tape, self.noise = tape, float(noise)
        self.forward_queries, self.forward_answers = [], []
        self.reverse_queries, self.reverse_answers = [], []
        self.minimum_conditional_variance = 0.

    def fork(self, tape):
        result = _LogarithmicGaussian(tape, self.noise)
        for name in ('forward_queries', 'forward_answers', 'reverse_queries', 'reverse_answers'):
            setattr(result, name, list(getattr(self, name)))
        return result

    def action(self, operand, transpose=False):
        tape, delta = self.tape, self.noise ** 2
        tape.check()
        if transpose:
            V, Y = self.reverse_queries, self.reverse_answers
            U, X = self.forward_queries, self.forward_answers
        else:
            V, Y = self.forward_queries, self.forward_answers
            U, X = self.reverse_queries, self.reverse_answers
        # Streaming queries need a single row pass. Ordinary execution acquires
        # these same moments below; repeating the lists costs cubic Python work.
        if tape.stream:
            requests = ([(a, b) for a in V for b in V]
                        + [(a, b) for a in U for b in U]
                        + [(a, b) for a in U for b in Y]
                        + [(a, b) for a in X for b in V]
                        + [(a, operand) for a in V + X] + [(operand, operand)])
            tape.pair_many(requests)
        Q, K = tape.gram(V, V), tape.gram(U, U)
        qvalues, qvectors = np.linalg.eigh((Q + Q.T) / 2)
        kvalues, kvectors = np.linalg.eigh((K + K.T) / 2)
        qvalues, kvalues = np.maximum(qvalues, 0.), np.maximum(kvalues, 0.)
        C = (qvectors / (delta + qvalues)) @ qvectors.T
        D = (kvectors / (delta + kvalues)) @ kvectors.T
        right = -tape.gram(U, Y) @ C - D @ tape.gram(X, V)
        E = kvectors @ ((kvectors.T @ right @ qvectors)
                        / (delta + kvalues[:, None] + qvalues[None, :])) @ qvectors.T
        v = tape.gram(V, [operand]).ravel()
        x = tape.gram(X, [operand]).ravel()
        dq = tape.pair(operand, operand)
        projected = qvectors.T @ v
        base_variance = dq - np.sum(projected ** 2 / (delta + qvalues))
        variances = (delta / (delta + kvalues)
                     * (dq - np.sum(projected[None, :] ** 2
                                    / (delta + kvalues[:, None] + qvalues[None, :]), axis=1)))
        smallest = min(float(base_variance), float(np.min(variances, initial=0.)))
        self.minimum_conditional_variance = min(self.minimum_conditional_variance, smallest)
        if smallest < -1e-7 * max(1., dq):
            raise FloatingPointError(f'Inconsistent Logarithmic conditional variance: {smallest:g}')
        base_variance, variances = max(0., base_variance), np.maximum(variances, 0.)
        c = math.sqrt(delta + base_variance)
        divided = (-base_variance + delta * np.sum(
            projected[None, :] ** 2 / ((delta + qvalues[None, :])
                                       * (delta + kvalues[:, None] + qvalues[None, :])), axis=1))
        divided /= (delta + kvalues) * (np.sqrt(delta + variances) + c)
        correction = (kvectors * divided) @ kvectors.T
        innovation = tape.root()
        innovation_pairs = tape.gram(U, [innovation]).ravel()
        coefficients = np.concatenate((C @ v, D @ x + E @ v + correction @ innovation_pairs, [c]))
        answer = tape.affine(Y + U + [innovation], coefficients)
        V.append(operand)
        Y.append(answer)
        return answer


class _LogarithmicProgram:
    """Two-hidden-layer physical Euler program with a regenerative row DAG."""

    def __init__(self, inputs, labels, width, seed, noise, deadline, rows=None, metric=None):
        self.inputs = np.asarray(inputs, dtype=np.float64).copy()
        self.labels = np.asarray(labels, dtype=np.float64).copy()
        self.tape = _LogarithmicTape(width, seed, deadline, rows, metric)
        self.gaussian = _LogarithmicGaussian(self.tape, noise)
        self.first = [self.tape.root() for _ in range(self.inputs.shape[1])]
        self.one, self.readout = self.tape.constant(1.), self.tape.constant(0.)
        self.ranks, self.losses = [], []
        self.final_train_predictions = None
        self.query_root_start = self.tape.root_count

    def learned_action(self, tape, operand, transpose=False):
        if transpose:
            left = [right for _, right, _ in self.ranks]
            right = [left for left, _, _ in self.ranks]
        else:
            left = [left for left, _, _ in self.ranks]
            right = [right for _, right, _ in self.ranks]
        pairs = tape.pair_many([(field, operand) for field in right])
        return left, pairs * np.asarray([weight for _, _, weight in self.ranks])

    def forward(self, vector, tape=None, gaussian=None):
        tape = self.tape if tape is None else tape
        gaussian = self.gaussian if gaussian is None else gaussian
        z1 = tape.affine(self.first, vector)
        h1 = tape.unary('tanh', z1)
        initial = gaussian.action(h1)
        factors, coefficients = self.learned_action(tape, h1)
        z2 = tape.affine([initial] + factors, np.concatenate(([1.], coefficients)))
        h2 = tape.unary('tanh', z2)
        return h1, h2, tape.pair(self.readout, h2)

    def train(self, steps, step, observer=None):
        tape, m = self.tape, len(self.labels)
        # Query innovations occupy reserved packet coordinates disjoint from
        # every prescribed training call, including unreached future calls.
        self.query_root_start = self.inputs.shape[1] + (2 * steps + 1) * m
        if observer is not None:
            observer(self, 0)
        for iteration in range(steps):
            fields = [self.forward(vector) for vector in self.inputs]
            residual = np.asarray([field[2] for field in fields]) - self.labels
            self.losses.append(float(np.mean(residual ** 2)))
            delta1, delta2 = [], []
            for h1, h2, _ in fields:
                d2 = tape.product(self.readout, tape.unary('gate', h2))
                initial = self.gaussian.action(d2, transpose=True)
                factors, coefficients = self.learned_action(tape, d2, transpose=True)
                carrier = tape.affine([initial] + factors, np.concatenate(([1.], coefficients)))
                delta1.append(tape.product(carrier, tape.unary('gate', h1)))
                delta2.append(d2)
            weights = -2 * float(step) * residual / m
            self.first = [tape.affine([old] + delta1,
                                     np.concatenate(([1.], weights * self.inputs[:, k])))
                          for k, old in enumerate(self.first)]
            self.readout = tape.affine([self.readout] + [field[1] for field in fields],
                                       np.concatenate(([1.], weights)))
            self.ranks.extend((d2, field[0], float(weight))
                              for d2, field, weight in zip(delta2, fields, weights))
            if observer is not None and iteration + 1 < steps:
                observer(self, iteration + 1)
        terminal = [self.forward(vector)[2] for vector in self.inputs]
        self.final_train_predictions = np.asarray(terminal)
        self.losses.append(float(np.mean((self.final_train_predictions - self.labels) ** 2)))
        if observer is not None and steps > 0:
            observer(self, steps)

    def query(self, vector):
        tape = self.tape.fork_query()
        tape.root_count = max(tape.root_count, self.query_root_start)
        gaussian = self.gaussian.fork(tape)
        value = self.forward(vector, tape, gaussian)[2]
        # Numeric/descriptor payload beyond the shared compact training state.
        new_nodes = tape.nodes[len(self.tape.nodes):]
        descriptor_words = (len(tape.nodes) + 3 * len(tape.pairs)
                            + sum(4 + len(node[1]) + node[2].size for node in new_nodes)
                            + 2 * (len(gaussian.forward_queries) + len(gaussian.reverse_queries)))
        history_size = max(len(gaussian.forward_queries), len(gaussian.reverse_queries), 1)
        # Conservative count for concurrent Gram, eigenbasis, inverse,
        # Sylvester, divided-difference and temporary matrix arrays.
        # Also pays for pair-request/index lists, reduction accumulators and
        # small vectors live alongside the numeric matrix arrays.
        solve_words = 96 * history_size ** 2 + 32 * history_size
        scratch = dict(row_block_words=tape.max_stream_words,
                       scalar_descriptor_words=int(descriptor_words),
                       conditional_solve_word_envelope=int(solve_words))
        self.tape.check()
        return value, scratch, tape.stream_passes

    def query_many(self, vectors):
        """Independent passive queries sharing only the regenerated row blocks.

        Each input uses the same reserved innovation as query(input), its own
        FC.31--34 coefficients and its own empirical contractions. No input is
        inserted into another input's Gaussian conditioning history.
        """
        vectors = np.asarray(vectors, dtype=np.float64)
        self.tape.check()
        if vectors.ndim != 2 or vectors.shape[1] != len(self.first):
            raise ValueError('Logarithmic batched query input shape mismatch')
        count = len(vectors)
        if count == 0:
            return np.empty(0), dict(row_block_words=0, scalar_descriptor_words=0,
                                     conditional_solve_word_envelope=0, batched_scalar_words=0), 0
        tape = self.tape.fork_query()
        V, Y = self.gaussian.forward_queries, self.gaussian.forward_answers
        U, X = self.gaussian.reverse_queries, self.gaussian.reverse_answers
        delta = self.gaussian.noise ** 2
        # Missing old-history moments are acquired in the local fork only.
        tape.pair_many([(a, b) for a in V for b in V]
                       + [(a, b) for a in U for b in U]
                       + [(a, b) for a in U for b in Y]
                       + [(a, b) for a in X for b in V])
        Q, K = tape.gram(V, V), tape.gram(U, U)
        qvalues, qvectors = np.linalg.eigh((Q + Q.T) / 2)
        kvalues, kvectors = np.linalg.eigh((K + K.T) / 2)
        qvalues, kvalues = np.maximum(qvalues, 0.), np.maximum(kvalues, 0.)
        C = (qvectors / (delta + qvalues)) @ qvectors.T
        D = (kvectors / (delta + kvalues)) @ kvectors.T
        right = -tape.gram(U, Y) @ C - D @ tape.gram(X, V)
        E = kvectors @ ((kvectors.T @ right @ qvectors)
                        / (delta + kvalues[:, None] + qvalues[None, :])) @ qvectors.T
        tape.check()
        rank_left = [left for left, _, _ in self.ranks]
        rank_right = [right for _, right, _ in self.ranks]
        operands = V + X + rank_right
        moments = np.zeros((len(operands), count))
        norms, innovation_pairs = np.zeros(count), np.zeros(len(U))
        root_index = max(tape.root_count, self.query_root_start)

        def first_features(values, block_size):
            z = np.zeros((block_size, count))
            for coordinate, field in enumerate(self.first):
                z += values[field, :, None] * vectors[None, :, coordinate]
            return np.tanh(z)

        # Pass one obtains every new empirical contraction and U^T g/n.
        for start in range(0, tape.width, 128):
            rows = np.arange(start, min(start + 128, tape.width), dtype=np.int64)
            values = tape.evaluate_rows(rows)
            features = first_features(values, len(rows))
            moments += values[operands] @ features
            norms += np.sum(features ** 2, axis=0)
            innovation = tape.root_values(root_index, rows)
            innovation_pairs += values[U] @ innovation
            del values, features, innovation
        moments /= tape.width
        norms /= tape.width
        innovation_pairs /= tape.width
        v = moments[:len(V)]
        x = moments[len(V):len(V) + len(X)]
        y_coefficients = C @ v
        u_coefficients = D @ x + E @ v
        c = np.empty(count)
        projected = qvectors.T @ v
        # The posterior matrix coefficients are prepared once per input,
        # outside both row streams, with the full reverse-history correction.
        for column in range(count):
            ve = projected[:, column]
            f0 = norms[column] - np.sum(ve ** 2 / (delta + qvalues))
            fa = delta / (delta + kvalues) * (norms[column] - np.sum(
                ve[None, :] ** 2 / (delta + kvalues[:, None] + qvalues[None, :]), axis=1))
            smallest = min(float(f0), float(np.min(fa, initial=0.)))
            if smallest < -1e-7 * max(1., norms[column]):
                raise FloatingPointError(f'Inconsistent batched Logarithmic variance: {smallest:g}')
            f0, fa = max(0., f0), np.maximum(fa, 0.)
            c[column] = math.sqrt(delta + f0)
            divided = (-f0 + delta * np.sum(ve[None, :] ** 2 / (
                (delta + qvalues[None, :])
                * (delta + kvalues[:, None] + qvalues[None, :])), axis=1))
            divided /= (delta + kvalues) * (np.sqrt(delta + fa) + c[column])
            correction = (kvectors * divided) @ kvectors.T
            u_coefficients[:, column] += correction @ innovation_pairs
        rank_coefficients = (moments[len(V) + len(X):]
                             * np.asarray([weight for _, _, weight in self.ranks])[:, None])
        predictions = np.zeros(count)
        # Pass two evaluates all initialized/learned actions and readouts.
        for start in range(0, tape.width, 128):
            rows = np.arange(start, min(start + 128, tape.width), dtype=np.int64)
            values = tape.evaluate_rows(rows)
            innovation = tape.root_values(root_index, rows)
            preactivation = (values[Y].T @ y_coefficients + values[U].T @ u_coefficients
                             + innovation[:, None] * c[None, :]
                             + values[rank_left].T @ rank_coefficients)
            predictions += values[self.readout] @ np.tanh(preactivation)
            del values, innovation, preactivation
        predictions /= tape.width
        h = max(len(V), len(U), 1)
        block = min(tape.width, 128)
        scratch = dict(
            row_block_words=max(tape.max_stream_words, block * (len(tape.nodes) + 32 + 4 * count
                                 + len(operands) + len(Y) + len(U) + len(rank_left))),
            scalar_descriptor_words=len(tape.nodes) + 3 * len(tape.pairs)
                                    + 4 * (len(V) + len(U) + len(self.ranks)),
            conditional_solve_word_envelope=96 * h ** 2 + 32 * h,
            batched_scalar_words=6 * (len(V) + len(U) + len(self.ranks) + 2) * count)
        self.tape.check()
        return predictions, scratch, tape.stream_passes + 2


def _logarithmic_selected_metric(tape):
    """Full numerical span selection, not a supplied-rank truncation."""
    from scipy.linalg import qr
    tape.check()
    table = np.column_stack(tape.values)
    norms = np.linalg.norm(table, axis=0)
    active = norms > 0
    normalized = table[:, active] / norms[active]
    basis, singular, _ = np.linalg.svd(normalized, full_matrices=False)
    tolerance = np.finfo(np.float64).eps * max(normalized.shape) * singular[0]
    rank = int(np.sum(singular > tolerance))
    tape.check()
    if rank == tape.width:
        rows = np.arange(tape.width)
        metric = np.eye(tape.width) / tape.width
        condition, projection_error = 1., 0.
    else:
        basis = basis[:, :rank]
        _, _, pivot = qr(basis.T, pivoting=True, mode='economic')
        tape.check()
        rows = pivot[:rank]
        inverse = np.linalg.solve(basis[rows], np.eye(rank))
        tape.check()
        metric = inverse.T @ inverse / tape.width
        metric = (metric + metric.T) / 2
        condition = float(np.linalg.cond(basis[rows]))
        tape.check()
        reconstruction = basis @ (inverse @ table[rows])
        projection_error = float(np.linalg.norm(reconstruction - table)
                                 / max(np.linalg.norm(table), np.finfo(float).tiny))
    # The matrix is positive definite by construction; no inverse metric is used.
    np.linalg.cholesky(metric)
    tape.check()
    details = dict(selected_rank=rank, named_fields=len(tape.nodes),
                   numerical_rank_tolerance=float(tolerance),
                   rank_rule='column-normalized SVD, eps * max(shape) * largest singular value; no rank cap',
                   selected_basis_condition=condition,
                   field_reconstruction_relative_error=projection_error,
                   rank_saturated=bool(rank == tape.width),
                   discarded_normalized_singular_max=float(singular[rank]) if rank < len(singular) else 0.)
    return rows, metric, details


def _logarithmic_inventory(program):
    tape = program.tape
    parts = dict(selected_field_values=sum(value.size for value in tape.values),
                 cached_metric_products=sum(value.size for value in tape.metric_values.values()),
                 metric=tape.metric.size, selected_row_indices=tape.rows.size,
                 immutable_affine_coefficients=sum(node[2].size for node in tape.nodes),
                 field_instructions=sum(4 + len(node[1]) for node in tape.nodes),
                 acquired_pairs=3 * len(tape.pairs),
                 training_data=program.inputs.size + program.labels.size,
                 recorded_training_observables=len(program.losses) + program.final_train_predictions.size,
                 live_parameter_ids=len(program.first) + 1 + 3 * len(program.ranks),
                 gaussian_history_ids=2 * (len(program.gaussian.forward_queries)
                                           + len(program.gaussian.reverse_queries)),
                 generator_seed_counters_and_scalar_controls=20)
    return dict(parts=parts, numerical_words=sum(parts.values()),
                payload_bytes=8 * sum(parts.values()),
                accounting='float64 arrays plus 64-bit scalar/index payload; excludes Python object overhead',
                dense_hidden_matrix_retained=False, future_scalar_answers_retained=False,
                source_object_discarded=True,
                selected_cache_covers_full_width=bool(len(tape.rows) == tape.width))


def logarithmic_probe(inputs, labels, queries, width, seed, steps, step, noise,
                      device='cpu', seconds=120., capture_steps=None):
    """Return (JSON summary, predictions or None) for empirical Logarithmic.

    Inputs are the same normalized vectors v used by dense_fields, without an
    implicit sqrt(d) change. This uses two tanh hidden layers, one complete
    source member, empirical Euler order/step and positive observation noise.
    It preserves the conditional sampler, selected-metric causal replay, and
    full empirical query streams. It does not claim the theorem's finite-bit
    law transfer, median confidence amplification, or certified error bound.
    CPU is deliberate: small sequential posterior solves and field DAGs.
    With capture_steps, predictions have shape (captures, queries), recorded
    from the acquired causal prefix during selected training. Otherwise the
    original endpoint-only array is returned. Captured arrays are external
    observations and are never operands of subsequent training or querying.
    """
    def as_numpy(value):
        if isinstance(value, torch.Tensor):
            value = value.detach().cpu().numpy()
        return np.asarray(value, dtype=np.float64)

    inputs, labels, queries = map(as_numpy, (inputs, labels, queries))
    if (inputs.ndim != 2 or queries.ndim != 2 or queries.shape[1] != inputs.shape[1]
            or labels.shape != (len(inputs),) or len(inputs) == 0 or width < 1
            or steps < 0 or step <= 0 or noise <= 0 or seconds <= 0):
        raise ValueError('Invalid Logarithmic probe shapes or positive algorithm parameters')
    if not all(np.isfinite(value).all() for value in (inputs, labels, queries)):
        raise ValueError('Logarithmic data must be finite')
    requested = None
    if capture_steps is not None:
        raw_steps = list(capture_steps)
        requested = [int(index) for index in raw_steps]
        if (any(index != raw for index, raw in zip(requested, raw_steps))
                or requested != sorted(set(requested))
                or any(index < 0 or index > steps for index in requested)):
            raise ValueError('capture_steps must be strictly increasing integers between zero and steps')
    started = time.monotonic()
    deadline = started + float(seconds)
    summary = dict(model='logarithmic_empirical_finite_program', width=int(width),
                   seed=int(seed), steps=int(steps), step=float(step), final_time=steps * step,
                   observation_noise=float(noise), device='cpu', requested_device=str(device),
                   dtype='float64', members=1, completed=False,
                   mechanism='named row DAG, both-orientation conditional Gaussian actions, selected metric, causal replay, empirical row-stream queries',
                   empirical_backend='counter PRNG Gaussian packets; float64; Euler; one member; no certified precision/PRG/confidence claim')
    if requested is not None:
        summary['capture_steps'] = requested
        summary['capture_times'] = [index * float(step) for index in requested]
    query_scratch = dict(row_block_words=0, scalar_descriptor_words=0,
                         conditional_solve_word_envelope=0)
    query_seconds, passes, query_calls = 0., 0, 0
    captured = {}

    def query_batch(program):
        nonlocal query_seconds, passes, query_calls
        query_started = time.monotonic()
        before = (len(program.tape.nodes), tuple(program.tape.pairs.items()),
                  program.tape.root_count, tuple(program.losses), tuple(program.first),
                  program.readout, tuple(program.ranks),
                  tuple(program.gaussian.forward_queries), tuple(program.gaussian.forward_answers),
                  tuple(program.gaussian.reverse_queries), tuple(program.gaussian.reverse_answers))
        answers, scratch, count = program.query_many(queries)
        for key, words in scratch.items():
            query_scratch[key] = max(query_scratch.get(key, 0), words)
        passes += count
        query_calls += len(queries)
        after = (len(program.tape.nodes), tuple(program.tape.pairs.items()),
                 program.tape.root_count, tuple(program.losses), tuple(program.first),
                 program.readout, tuple(program.ranks),
                 tuple(program.gaussian.forward_queries), tuple(program.gaussian.forward_answers),
                 tuple(program.gaussian.reverse_queries), tuple(program.gaussian.reverse_answers))
        if before != after:
            raise RuntimeError('Passive Logarithmic query altered the training transcript')
        program.tape.check()
        query_seconds += time.monotonic() - query_started
        answers = np.asarray(answers, dtype=np.float64)
        if not np.isfinite(answers).all():
            raise FloatingPointError('Nonfinite Logarithmic query predictions')
        return answers

    def observer(program, index):
        nonlocal phase
        if requested is not None and index in requested:
            phase = 'streamed_queries'
            captured[index] = query_batch(program)
            phase = 'causal_training'

    phase = 'source_setup'
    try:
        source = _LogarithmicProgram(inputs, labels, width, seed, noise, deadline)
        source.train(int(steps), float(step))
        summary['source_seconds'] = time.monotonic() - started
        summary['named_fields'] = len(source.tape.nodes)
        summary['innovation_fields'] = source.tape.root_count - inputs.shape[1]
        summary['source_training_losses'] = list(source.losses)
        summary['source_field_payload_bytes'] = 8 * width * len(source.tape.nodes)
        phase = 'metric_selection'
        metric_started = time.monotonic()
        rows, metric, details = _logarithmic_selected_metric(source.tape)
        details['innovation_fields'] = source.tape.root_count - inputs.shape[1]
        summary.update(details)
        summary['metric_seconds'] = time.monotonic() - metric_started
        source_pairs = dict(source.tape.pairs)
        source_predictions = source.final_train_predictions.copy()
        del source
        phase = 'causal_training'
        replay_started = time.monotonic()
        compact = _LogarithmicProgram(inputs, labels, width, seed, noise, deadline, rows, metric)
        compact.train(int(steps), float(step), observer if requested is not None else None)
        summary['training_seconds'] = max(0., time.monotonic() - replay_started - query_seconds)
        summary['minimum_computed_conditional_variance'] = compact.gaussian.minimum_conditional_variance
        if set(source_pairs) != set(compact.tape.pairs):
            raise FloatingPointError('Source and selected scalar instruction sets differ')
        differences = np.asarray([compact.tape.pairs[key] - value for key, value in source_pairs.items()])
        scales = np.asarray([max(1., abs(value)) for value in source_pairs.values()])
        summary['scalar_replay_max_abs'] = float(np.max(np.abs(differences), initial=0.))
        summary['scalar_replay_max_scaled'] = float(np.max(np.abs(differences) / scales, initial=0.))
        summary['training_prediction_replay_max_abs'] = float(np.max(np.abs(
            compact.final_train_predictions - source_predictions), initial=0.))
        summary['replay_passed'] = bool(summary['scalar_replay_max_scaled'] <= 1e-7)
        summary['training_losses'] = list(compact.losses)
        del source_pairs, source_predictions
        summary['retained'] = _logarithmic_inventory(compact)
        summary['dense_parameter_words'] = int(width * inputs.shape[1] + width * width + width)
        summary['retained_to_dense_parameter_ratio'] = (summary['retained']['numerical_words']
                                                        / summary['dense_parameter_words'])
        if not summary['replay_passed']:
            summary.update(status='numerical_replay_failed', seconds=time.monotonic() - started)
            return summary, None
        phase = 'streamed_queries'
        if requested is None:
            predictions = query_batch(compact)
        else:
            predictions = (np.stack([captured[index] for index in requested])
                           if requested else np.empty((0, len(queries))))
        compact.tape.check()
        summary.update(status='complete', completed=True, query_seconds=query_seconds,
                       query_count=len(queries), total_query_calls=query_calls, query_stream_passes=passes,
                       query_batch_size=len(queries),
                       query_execution='shared row regeneration; separate posterior coefficients and same reserved innovation per input',
                       query_row_scratch_words=query_scratch['row_block_words'],
                       query_scratch=query_scratch,
                       retained_plus_query_word_envelope=(summary['retained']['numerical_words']
                                                           + sum(query_scratch.values())),
                       query_scratch_note='numeric/index payload envelope; excludes Python and LAPACK internal workspace',
                       external_observation_words=int(predictions.size),
                       query_preserved_training_transcript=True, seconds=time.monotonic() - started)
        return summary, predictions
    except (_LogarithmicBudget, FloatingPointError, np.linalg.LinAlgError) as error:
        summary.update(status='resource_cap' if isinstance(error, _LogarithmicBudget) else 'numerical_failure',
                       failed_phase=phase, error=str(error), seconds=time.monotonic() - started)
        return summary, None


def logarithmic_small_checks():
    """Tiny implementation checks, not a scientific accuracy experiment."""
    deadline = time.monotonic() + 30.
    posterior_error = 0.
    for transpose in (False, True):
        n, noise = 6, .2
        tape = _LogarithmicTape(n, 772, deadline)
        V, Y, U, X = [[tape.root() for _ in range(2)] for _ in range(4)]
        operand = tape.root()
        gaussian = _LogarithmicGaussian(tape, noise)
        gaussian.forward_queries, gaussian.forward_answers = V.copy(), Y.copy()
        gaussian.reverse_queries, gaussian.reverse_answers = U.copy(), X.copy()
        observations, observed = [], []
        for reverse, queries, answers in ((False, V, Y), (True, U, X)):
            for query, answer in zip(queries, answers):
                for index in range(n):
                    row = np.zeros((n, n))
                    if reverse:
                        row[:, index] = tape.values[query]
                    else:
                        row[index, :] = tape.values[query]
                    observations.append(row.ravel())
                    observed.append(tape.values[answer][index])
        observations = np.asarray(observations)
        precision = n * np.eye(n * n) + observations.T @ observations / noise ** 2
        covariance = np.linalg.inv(precision)
        mean = covariance @ observations.T @ np.asarray(observed) / noise ** 2
        action = []
        for index in range(n):
            row = np.zeros((n, n))
            if transpose:
                row[:, index] = tape.values[operand]
            else:
                row[index, :] = tape.values[operand]
            action.append(row.ravel())
        action = np.asarray(action)
        eigenvalues, eigenvectors = np.linalg.eigh(action @ covariance @ action.T + noise ** 2 * np.eye(n))
        root = (eigenvectors * np.sqrt(eigenvalues)) @ eigenvectors.T
        answer = gaussian.action(operand, transpose)
        innovation = tape.nodes[answer][1][-1]
        expected = action @ mean + root @ tape.values[innovation]
        posterior_error = max(posterior_error, float(np.max(np.abs(tape.values[answer] - expected))))
    inputs, labels = np.eye(2), np.asarray([.1, -.06])
    source = _LogarithmicProgram(inputs, labels, 128, 712, .03, deadline)
    source.train(2, .05)
    rows, metric, _ = _logarithmic_selected_metric(source.tape)
    selected = _LogarithmicProgram(inputs, labels, 128, 712, .03, deadline, rows, metric)
    selected.train(2, .05)
    replay_error = max(abs(value - selected.tape.pairs[key]) for key, value in source.tape.pairs.items())
    regenerated = source.tape.evaluate_rows(np.arange(128))
    regeneration_error = float(np.max(np.abs(regenerated - np.asarray(source.tape.values))))
    vector = np.asarray([.8, .6])
    source_query = source.query(vector)[0]
    selected_query = selected.query(vector)[0]
    repeated_query = selected.query(vector)[0]
    query_error = abs(source_query - selected_query)
    query_vectors = np.asarray([vector, [-.6, .8], [.6, -.8]])
    separate = np.asarray([selected.query(point)[0] for point in query_vectors])
    batched = selected.query_many(query_vectors)[0]
    permutation = np.asarray([2, 0, 1])
    permuted = selected.query_many(query_vectors[permutation])[0]
    batch_error = float(np.max(np.abs(batched - separate)))
    permutation_error = float(np.max(np.abs(permuted - batched[permutation])))
    # Independently check two Euler updates against loss autodifferentiation.
    # Only this algebra test supplies a fixed dense initialized matrix.
    fixed = _LogarithmicProgram(inputs, labels, 9, 1902, .03, deadline)
    matrix = np.random.default_rng(904).normal(size=(9, 9)) / 3
    initial_first = np.column_stack([fixed.tape.values[index] for index in fixed.first])
    basis_ids = [fixed.tape.root() for _ in range(9)]
    basis = np.column_stack([fixed.tape.values[index] for index in basis_ids])

    class FixedMatrixAlgebraCheck:
        def action(self, operand, transpose=False):
            answer = (matrix.T if transpose else matrix) @ fixed.tape.values[operand]
            return fixed.tape.affine(basis_ids, np.linalg.solve(basis, answer))

    fixed.gaussian = FixedMatrixAlgebraCheck()
    fixed.train(2, .05)
    exact = [torch.tensor(value, dtype=torch.float64) for value in
             (initial_first, np.zeros(9), matrix)]
    sample_inputs = torch.tensor(inputs, dtype=torch.float64)
    sample_labels = torch.tensor(labels, dtype=torch.float64)
    with torch.enable_grad():
        for _ in range(2):
            exact = [value.detach().requires_grad_() for value in exact]
            first, readout, hidden = exact
            predictions = readout @ (hidden @ (first @ sample_inputs.T).tanh()).tanh() / 9
            loss = (predictions - sample_labels).square().mean()
            gradients = torch.autograd.grad(loss, exact)
            exact = [(value - .05 * mobility * gradient).detach()
                     for value, gradient, mobility in zip(exact, gradients, (9, 9, 1))]
    reconstructed = matrix.copy()
    for left, right, weight in fixed.ranks:
        reconstructed += weight * np.outer(fixed.tape.values[left], fixed.tape.values[right]) / 9
    actual = (np.column_stack([fixed.tape.values[index] for index in fixed.first]),
              fixed.tape.values[fixed.readout], reconstructed)
    euler_error = max(float(np.max(np.abs(value - expected.numpy())))
                      for value, expected in zip(actual, exact))
    assert max(posterior_error, replay_error, regeneration_error, query_error,
               euler_error, batch_error, permutation_error) < 1e-10
    assert repeated_query == selected_query
    return dict(gaussian_both_orientation_posterior_max_abs=posterior_error,
                scalar_replay_max_abs=replay_error, row_regeneration_max_abs=regeneration_error,
                source_vs_selected_passive_query_max_abs=query_error,
                fixed_matrix_euler_autograd_max_abs=euler_error,
                batched_vs_separate_query_max_abs=batch_error,
                query_permutation_max_abs=permutation_error,
                repeated_query_identical=True, selected_rank=len(rows), virtual_width=128)


def validation_plot_main(argv):
    """Render only measured results; preserve every run in a portable ledger."""
    parser = argparse.ArgumentParser(description='Render empirical validation results')
    parser.add_argument('--root', type=Path, default=ROOT/'data/generated/compression_empirical_validation_20261007')
    parser.add_argument('--bundle', type=Path, help='Portable report ledger; no raw run folders needed')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    args.out.mkdir(parents=True, exist_ok=False)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    reports = {}
    if args.bundle:
        reports = json.loads(args.bundle.read_text())['reports']
    else:
        for path in sorted(args.root.glob('*/report.json')):
            report = json.loads(path.read_text())
            if 'config' in report:
                reports[path.parent.name] = report
    save_json(args.out/'compression_validation_source.json', dict(
        scope='Finite-grid empirical results, not supremum/asymptotic/confidence certificates',
        inventory='Harmonic model tensors include metrics; Logarithmic numerical payload includes descriptors/caches',
        plot_source_sha256=sha(Path(__file__).read_bytes()), reports=reports))
    plt.rcParams.update({'font.size': 9, 'axes.titlesize': 10, 'axes.labelsize': 9,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'pdf.fonttype': 42, 'savefig.facecolor': 'white'})
    colors = dict(dense='#30343B', harmonic='#008A89', matched_dense='#D87936', frozen_ntk='#9B6FA2',
                  logarithmic='#3575B8')
    labels = dict(dense='Independent dense pair', harmonic='Harmonic',
                  matched_dense='State-matched MLP', frozen_ntk='Frozen NTK', logarithmic='Logarithmic')

    def save(fig, name):
        fig.savefig(args.out/(name+'.pdf'), bbox_inches='tight')
        fig.savefig(args.out/(name+'.png'), bbox_inches='tight', dpi=180)
        plt.close(fig)

    def eligible(report, *models):
        return (report.get('complete', False) and 'dense_variability' in report
                and all(model in report.get('comparisons', {}) for model in models))

    def log_eligible(report):
        return (eligible(report, 'logarithmic', 'log_matched_dense', 'frozen_ntk')
                and report.get('logarithmic_probe', {}).get('completed', False)
                and report['config'].get('task') == 'toy')

    circle = [r for name, r in reports.items() if name.startswith('confirm_circle_')
              and eligible(r, 'harmonic', 'matched_dense', 'frozen_ntk')]
    if circle:
        fig, axes = plt.subplots(1, 2, figsize=(9.3, 3.25), layout='constrained')
        widths = sorted(set(r['config']['width'] for r in circle))
        for model in ('dense', 'harmonic', 'matched_dense', 'frozen_ntk'):
            groups = [[r['dense_variability']['max_time_rms'] if model == 'dense' else
                       r['comparisons'][model]['max_time_rms'] for r in circle if r['config']['width'] == n]
                      for n in widths]
            middle = np.asarray([np.median(group) for group in groups])
            axes[0].plot(widths, middle, 'o-', color=colors[model], label=labels[model], ms=4, lw=1.6)
            axes[0].fill_between(widths, [min(g) for g in groups], [max(g) for g in groups],
                                 color=colors[model], alpha=.10, linewidth=0)
        for model in ('dense', 'harmonic'):
            groups = [[r['runs']['dense']['moving_scalars'] if model == 'dense' else
                       r['matched_budget']['target_total_scalars'] for r in circle if r['config']['width'] == n]
                      for n in widths]
            axes[1].plot(widths, [np.median(g) for g in groups], 'o-', color=colors[model],
                         label='Dense' if model == 'dense' else 'Harmonic, including metrics', ms=4, lw=1.6)
        for axis in axes:
            axis.set_xscale('log', base=2)
            axis.set_yscale('log')
            axis.set_xticks(widths, [str(n) for n in widths])
            axis.set_xlabel('Dense width n')
            axis.grid(axis='y', alpha=.16)
        axes[0].set_title('(a) Harmonic: unseen-input fidelity', loc='left')
        axes[0].set_ylabel('Maximum recorded-time RMS')
        axes[0].legend(frameon=False, fontsize=8, loc='center right')
        axes[1].set_title('(b) Harmonic: retained model tensors', loc='left')
        axes[1].set_ylabel('Scalar entries')
        axes[1].legend(frameon=False, fontsize=8, loc='upper left')
        save(fig, 'compression_validation')

    logarithmic_width = [r for name, r in reports.items() if name.startswith('confirm_log_d5_')
                         and log_eligible(r)]
    if logarithmic_width:
        fig, axes = plt.subplots(1, 2, figsize=(9.3, 3.25), layout='constrained')
        widths = sorted(set(r['config']['width'] for r in logarithmic_width))
        for model in ('dense', 'logarithmic', 'log_matched_dense', 'frozen_ntk'):
            groups = []
            for width in widths:
                group = []
                for r in logarithmic_width:
                    if r['config']['width'] != width:
                        continue
                    if model == 'dense':
                        value = r['logarithmic_probe']['dense_variability_same_queries']['max_time_rms']
                    else:
                        value = r['comparisons'][model]['max_time_rms']
                    group.append(value)
                groups.append(group)
            style = 'matched_dense' if model == 'log_matched_dense' else model
            axes[0].plot(widths, [np.median(g) for g in groups], 'o-', color=colors[style],
                         label=labels[style], ms=4, lw=1.6)
            axes[0].fill_between(widths, [min(g) for g in groups], [max(g) for g in groups],
                                 color=colors[style], alpha=.10, linewidth=0)
        for name, key, color, line in (
                ('Dense parameters', 'dense_parameter_words', colors['dense'], '-'),
                ('Logarithmic retained payload', 'numerical_words', colors['logarithmic'], '-'),
                ('Including query workspace envelope', 'retained_plus_query_word_envelope', colors['logarithmic'], ':')):
            values = []
            for width in widths:
                group = [r['logarithmic_probe'] for r in logarithmic_width if r['config']['width'] == width]
                values.append(np.median([g['retained'][key] if key == 'numerical_words' else g[key] for g in group]))
            axes[1].plot(widths, values, marker='o', ls=line, color=color, label=name, ms=4, lw=1.6)
        for axis in axes:
            axis.set_xscale('log', base=2)
            axis.set_yscale('log')
            axis.set_xticks(widths, [str(n) for n in widths])
            axis.set_xlabel('Dense width n')
            axis.grid(axis='y', alpha=.16)
        axes[0].set_title('(c) Logarithmic: unseen-input fidelity', loc='left')
        axes[0].set_ylabel('Maximum recorded-time RMS')
        axes[0].legend(frameon=False, fontsize=8, loc='center right')
        axes[1].set_title('(d) Logarithmic: retained numerical words', loc='left')
        axes[1].set_ylabel('64-bit numerical / index payload')
        axes[1].legend(frameon=False, fontsize=8, loc='upper left')
        save(fig, 'compression_logarithmic')

    fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.25), layout='constrained')
    sphere = [r for name, r in reports.items() if name.startswith('confirm_sphere_')
              and eligible(r, 'harmonic', 'matched_dense', 'frozen_ntk')]
    sphere.sort(key=lambda r: r['config']['dimension'])
    for offset, model in zip((-.23, 0., .23), ('harmonic', 'matched_dense', 'frozen_ntk')):
        axes[0].bar(np.arange(len(sphere))+offset,
                    [r['comparisons'][model]['ratio_to_dense_pair'] for r in sphere],
                    width=.22, label=labels[model], color=colors[model])
    axes[0].set_xticks(np.arange(len(sphere)), [str(r['config']['dimension']) for r in sphere])
    axes[0].set_xlabel('Input dimension d')
    axes[0].set_ylabel('Trajectory RMS / dense-pair RMS')
    axes[0].set_yscale('log')
    axes[0].axhline(3, color='#555555', ls=':', lw=1)
    axes[0].set_title('(a) Sphere checks, n = 2048', loc='left')
    axes[0].legend(frameon=False, fontsize=7)

    digits = [r for name, r in reports.items() if name.startswith('confirm_digits_')
              and r['config'].get('task') == 'digits'
              and eligible(r, 'harmonic', 'matched_dense', 'frozen_ntk')]
    if digits:
        times = np.asarray(digits[0]['times'])[1:]
        for model in ('dense', 'harmonic', 'matched_dense', 'frozen_ntk'):
            values = np.asarray([r['dense_variability']['curve'] if model == 'dense' else
                                 r['comparisons'][model]['curve'] for r in digits])[:, 1:]
            axes[1].plot(times, np.median(values, axis=0), 'o-', color=colors[model], label=labels[model], ms=3, lw=1.4)
            axes[1].fill_between(times, values.min(axis=0), values.max(axis=0), color=colors[model], alpha=.1)
    axes[1].set_yscale('log')
    axes[1].set_xlabel('Physical training time')
    axes[1].set_ylabel('Unseen-image RMS versus dense')
    axes[1].set_title('(b) Embedded digits 3 versus 8', loc='left')
    axes[1].legend(frameon=False, fontsize=6.5, loc='lower right')

    logs = [r for name, r in reports.items() if name.startswith('confirm_log_') and log_eligible(r)]
    if not logs:
        logs = [r for name, r in reports.items() if name.startswith('pilot_log_trajectory_') and log_eligible(r)]
    logs = [r for r in logs if r['config']['width'] == 4096]
    dimensions = sorted(set(r['config']['dimension'] for r in logs))
    for index, dimension in enumerate(dimensions):
        group = [r['logarithmic_probe'] for r in logs if r['config']['dimension'] == dimension]
        values = [g['comparison']['ratio_to_dense_pair'] for g in group]
        middle = np.median(values)
        axes[2].bar(index, middle, color=colors['logarithmic'], width=.6)
        axes[2].errorbar(index, middle, yerr=[[middle-min(values)], [max(values)-middle]],
                         color=colors['dense'], capsize=3, lw=1)
        compression = np.median([g['dense_parameter_words']/g['retained']['numerical_words'] for g in group])
        axes[2].text(index, max(values)*1.13, f'{compression:.0f}x smaller', ha='center', fontsize=7)
    axes[2].axhline(3, color='#555555', ls=':', lw=1)
    axes[2].set_yscale('log')
    axes[2].set_xticks(range(len(dimensions)), [str(d) for d in dimensions])
    axes[2].set_ylim(.5, 15)
    axes[2].set_xlabel('Input dimension d (n = 4096)')
    axes[2].set_ylabel('Trajectory RMS / dense-pair RMS')
    axes[2].set_title('(c) Empirical Logarithmic decoder', loc='left')
    for axis in axes:
        axis.grid(axis='y', alpha=.16)
    save(fig, 'compression_checks')
    print(json.dumps(dict(reports=len(reports), circle_confirmations=len(circle),
                          sphere_checks=len(sphere), digits_confirmations=len(digits),
                          logarithmic_points=len(logs), out=str(args.out))), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', type=Path, default=HERE/'response_memory_source.npz')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:1')
    parser.add_argument('--per-run-seconds', type=float, default=300.)
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    base, orthogonal = load_legacy(args.out)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    checks = small_checks(base, orthogonal)
    save_json(args.out/'operator_checks.json', checks)
    if args.check_only:
        print(json.dumps(checks)); return
    if not args.device.startswith('cuda') or not torch.cuda.is_available():
        raise RuntimeError('Full capture requires an explicitly available CUDA device')
    with np.load(args.bundle, allow_pickle=False) as source:
        arrays = {k:source[k].copy() for k in source.files if k != 'metadata_json'}
        meta = json.loads(str(source['metadata_json']))
    schedule = np.unique(np.concatenate(([0.], np.geomspace(.5, 80., 32), [1., 2., 5., 10., 20., 40., 80.])))
    assert len(schedule) == 39 and schedule[-1] == 80.
    report = dict(protocol='One fixed task, four models, two resolutions; no tuning or endpoint stopping',
                  task='quadrant_pairs', width=2048, hidden_layers=2, activation='tanh',
                  seed=20260920, dtype='float64', query_count=2048, common_times=schedule.tolist(),
                  solver='adaptive explicit Heun, original per-model error controllers and lifted closure',
                  sensitivity='RMS(dense coarse-fine) + RMS(closure coarse-fine); not an error certificate',
                  archive_replay_gate='At old checkpoints, each model RMS change <= 5e-6 + 2 times old combined sensitivity',
                  per_model_seconds=args.per_run_seconds, maximum_model_runs=8,
                  python=platform.python_version(), numpy=np.__version__, torch=torch.__version__,
                  device=args.device, gpu=torch.cuda.get_device_name(args.device),
                  git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                  command=sys.argv, base_bundle_sha256=sha(args.bundle.read_bytes()),
                  capture_source_sha256=sha(Path(__file__).read_bytes()), legacy_sources=HASHES,
                  initialization_hashes=INITIAL_HASHES, operator_checks=checks,
                  train_inputs_sha256=array_sha(arrays['train_inputs']),
                  train_labels_sha256=array_sha(arrays['train_labels']),
                  history_angles_sha256=array_sha(arrays['history_angles']))
    save_json(args.out/'protocol.json', report)
    results, runs = {}, []
    for order in (0, 1, 3, 7):
        for level in ((1, 2) if order == 0 else (0, 1)):
            results[order, level], row = capture(order, level, arrays, schedule, args, base, orthogonal)
            runs.append(row)
    old_times = arrays['common_times'].copy()
    indices = np.array([np.flatnonzero(schedule == t)[0] for t in old_times])
    replay = {}
    for order in (0, 1, 3, 7):
        key = 'common_dense' if order == 0 else f'common_memory_{order}'
        fine = results[order, 2 if order == 0 else 1]
        change = np.sqrt(np.mean((fine[indices]-arrays[key])**2, axis=1))
        sensitivity = (np.maximum.reduce([arrays[f'common_sensitivity_{p}'] for p in (1,3,7)])
                       if order == 0 else arrays[f'common_sensitivity_{order}'])
        gate = 5e-6 + 2*sensitivity
        replay[key] = dict(times=old_times.tolist(), rms_change=change.tolist(),
                           allowed_change=gate.tolist(), passed=bool(np.all(change <= gate)))
    report.update(runs=runs, archive_replay=replay, complete=True)
    save_json(args.out/'report.json', report)
    if not all(x['passed'] for x in replay.values()):
        raise RuntimeError('Archive replay gate failed; capture retained but bundle not published')
    arrays['common_times'] = schedule
    arrays['common_dense'], arrays['common_dense_coarse'] = results[0,2], results[0,1]
    dense_sensitivity = np.sqrt(np.mean((results[0,2]-results[0,1])**2, axis=1))
    for p in (1,3,7):
        fine, coarse = results[p,1], results[p,0]
        arrays[f'common_memory_{p}'], arrays[f'common_memory_{p}_coarse'] = fine, coarse
        arrays[f'common_rms_{p}'] = np.sqrt(np.mean((fine-results[0,2])**2, axis=1))
        arrays[f'common_sensitivity_{p}'] = dense_sensitivity + np.sqrt(np.mean((fine-coarse)**2, axis=1))
    meta['trajectory_previous'] = meta['trajectory']
    meta['trajectory'] = dict(case='quadrant_pairs', width=2048, hidden_layers=2, query_count=2048,
                             common_times=schedule.tolist(), displayed_times=[0,5,20,80],
                             metric='RMS versus freshly replayed fine dense reference at identical physical times',
                             sensitivity=report['sensitivity'],
                             note='New genuine checkpoints; no interpolated predictions. Endpoint figures unchanged.')
    meta['trajectory_capture'] = report
    np.savez_compressed(args.out/'response_memory_source.npz', **arrays,
                        metadata_json=np.array(json.dumps(meta, allow_nan=False)))
    print(json.dumps(dict(event='checked_bundle', checkpoints=len(schedule), out=str(args.out))), flush=True)


def logarithmic_euler_inventory_floor(width, samples, dimension, steps):
    """Exact current-code instruction counts, not a bound on all compressions."""
    calls = samples * (2 * steps + 1)  # Includes terminal training evaluation.
    fields = dimension + 2 + steps * (13 * samples + dimension + 1) + 6 * samples
    words = calls * (calls + 1)  # Every Gaussian answer's coefficients and parent IDs.
    dense = width * width + width * (dimension + 1)
    return dict(steps=int(steps), gaussian_calls=int(calls), named_fields=int(fields),
                independent_root_fields=int(dimension + calls),
                source_cache_values=int(width * fields),
                gaussian_answer_coefficient_and_parent_words=int(words),
                dense_parameter_words=int(dense),
                instruction_floor_exceeds_dense=bool(words >= dense),
                full_rank_expected_under_iid_roots=bool(dimension + calls >= width),
                scope='Current unpruned empirical Euler program; not an impossibility theorem. '
                      'Full-rank statement is almost sure for ideal iid Gaussian roots; '
                      'the counter-PRNG implementation is not an iid-law certificate.')


def euler_fit_main(argv):
    """One reproducible Euler reference/control run, with no method substitution."""
    parser = argparse.ArgumentParser(description='Raw-image full-training Euler benchmark')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--width', type=int, default=4096)
    parser.add_argument('--model', choices=('dense', 'bounded-packets'), default='dense')
    parser.add_argument('--packet-width', type=int, default=256)
    parser.add_argument('--source-seed', type=int, default=40201)
    parser.add_argument('--seed', type=int, default=201)
    parser.add_argument('--digits', type=int, nargs=2, default=(3, 8), metavar=('NEGATIVE', 'POSITIVE'))
    parser.add_argument('--step', type=float, default=.05)
    parser.add_argument('--dtype', choices=('float64', 'float32'), default='float64')
    parser.add_argument('--horizon', type=float)
    parser.add_argument('--max-horizon', type=float, default=200.)
    parser.add_argument('--loss-target', type=float, default=.005)
    parser.add_argument('--per-run-seconds', type=float, default=300.)
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args(argv)
    if args.width < 1 or not 0 < args.step <= .5 or args.max_horizon <= 0:
        parser.error('Positive width/horizon and 0 < step <= 0.5 are required')
    if len(set(args.digits)) != 2 or any(not 0 <= v <= 9 for v in args.digits):
        parser.error('--digits requires two distinct digits from 0 through 9')
    if not math.isclose(.5 / args.step, round(.5 / args.step), abs_tol=1e-9):
        parser.error('step must divide 0.5 for shared physical observation times')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    config = {key: str(value) if isinstance(value, Path) else value
              for key, value in vars(args).items()}
    report = dict(config=config, source_sha256=sha(Path(__file__).read_bytes()),
                  git_head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                                                   text=True).strip(),
                  command=sys.argv, python=platform.python_version(), torch=torch.__version__,
                  numpy=np.__version__, threads=torch.get_num_threads(),
                  device=torch.cuda.get_device_name(args.device) if args.device.startswith('cuda') else 'CPU',
                  method='ordinary Gaussian dense network; full-batch physical Euler',
                  preprocessing=f'raw digits {args.digits[0]} versus {args.digits[1]}, '
                                'all 64 pixels, per-image normalization, no PCA',
                  complete=False)
    save_json(args.out / 'report.json', report)
    if args.check_only:
        report['checks'] = euler_small_checks('cpu')
        if args.model == 'bounded-packets':
            report['checks']['bounded_packets'] = bounded_gaussian_packet_small_checks('cpu')
        report['complete'] = True
        save_json(args.out / 'report.json', report)
        print(json.dumps(report['checks']), flush=True)
        return
    inputs, labels, queries, truth = validation_data(64, 100, 0, 47, args.device,
                                                    'digits', 'test', True, 0, args.digits)
    synchronize(inputs.device)
    setup_started = time.monotonic()
    if inputs.device.type == 'cuda':
        torch.cuda.reset_peak_memory_stats(inputs.device)
    if args.model == 'bounded-packets':
        model = BoundedGaussianPackets(args.width, args.packet_width, inputs,
                                       args.seed, args.source_seed)
        report.update(method='bounded Gaussian-action packets; new empirical approximation',
                      approximation_scope='covariance-balanced, source-conditioned initialization; '
                      'not the adaptive-history Logarithmic decoder; no inherited theorem',
                      setup=model.diagnostics)
    else:
        model = Dense(args.width, 64, args.seed, args.device)
    synchronize(inputs.device)
    report['setup_seconds'] = time.monotonic() - setup_started
    report['setup_process_peak_cuda_bytes'] = (torch.cuda.max_memory_allocated(inputs.device)
                                               if inputs.device.type == 'cuda' else None)
    # Generate exactly the same float64 initialization before either precision run.
    initial_hashes = [array_sha(value.cpu().numpy()) for value in model.initial_state]
    dtype = getattr(torch, args.dtype)
    model.initial_state = [value.to(dtype=dtype) for value in model.initial_state]
    inputs, labels, queries, truth = [value.to(dtype=dtype) for value in
                                    (inputs, labels, queries, truth)]
    report.update(initial_float64_sha256=initial_hashes,
                  train_inputs_sha256=array_sha(inputs.cpu().numpy()),
                  query_inputs_sha256=array_sha(queries.cpu().numpy()),
                  training_count=len(inputs), validation_count=len(queries),
                  parameter_words=sum(value.numel() for value in model.initial_state),
                  common_training_data_words=inputs.numel()+labels.numel(),
                  retained_state_scope='Three deployable weight arrays; scalar diagnostics/provenance '
                  'are experiment metadata, not inference state. Training peak also includes '
                  'the initial-state copy, gradient workspace, data and evaluation buffers.')
    save_json(args.out / 'report.json', report)
    print(json.dumps(dict(event='euler_start', seed=args.seed, model=args.model,
                          width=len(model.initial_state[1]), source_width=args.width,
                          dtype=args.dtype, step=args.step, horizon=args.horizon,
                          loss_target=args.loss_target)), flush=True)
    try:
        remaining_seconds = args.per_run_seconds - report['setup_seconds']
        if remaining_seconds <= 0:
            raise RuntimeError('Euler model setup exhausted the combined setup/training time budget')
        state, predictions, result = integrate_euler(model, inputs, labels, queries,
            step=args.step, seconds=remaining_seconds, horizon=args.horizon,
            loss_target=args.loss_target, max_steps=int(args.max_horizon / args.step),
            observation_every=round(.5 / args.step))
        report['run'] = result
        steps = result['steps']
        report['logarithmic_current_implementation'] = logarithmic_euler_inventory_floor(
            args.width, len(inputs), inputs.shape[1], steps)
        report['complete'] = result['complete']
        save_json(args.out / 'report.json', report)
        np.savez_compressed(args.out / 'trajectories.npz', predictions=predictions,
            times=np.asarray(result['times']), train_inputs=inputs.cpu().numpy(),
            train_labels=labels.cpu().numpy(), query_inputs=queries.cpu().numpy(),
            query_labels=truth.cpu().numpy(), train_predictions=model.predict(
                state, inputs, inputs, labels).detach().cpu().numpy())
        if len(state[1]) <= 512:
            np.savez_compressed(args.out / 'weights.npz',
                                first=state[0].cpu().numpy(), readout=state[1].cpu().numpy(),
                                hidden=state[2].cpu().numpy())
        print(json.dumps(dict(event='euler_complete', out=str(args.out),
                              **{key: result[key] for key in ('steps', 'actual_horizon',
                                  'final_training_mse', 'seconds', 'stop_reason', 'complete')})), flush=True)
    except (RuntimeError, ValueError, ArithmeticError) as error:
        report['error'] = f'{type(error).__name__}: {error}'
        save_json(args.out / 'report.json', report)
        raise


def euler_summary_main(argv):
    """Audit matched Euler runs and compute RMS directly from saved predictions."""
    parser = argparse.ArgumentParser(description='Matched full-training Euler RMS summary')
    parser.add_argument('--pair', nargs=3, action='append', required=True,
                        metavar=('LABEL', 'COARSE_DIRECTORY', 'FINE_DIRECTORY'))
    parser.add_argument('--reference', default='dense')
    parser.add_argument('--iid', default='iid')
    parser.add_argument('--precision', nargs=2, action='append', default=[],
                        metavar=('FLOAT64_DIRECTORY', 'FLOAT32_DIRECTORY'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)

    def load(directory):
        directory = Path(directory)
        metadata = json.loads((directory/'report.json').read_text())
        with np.load(directory/'trajectories.npz') as saved:
            arrays = {key: saved[key].copy() for key in saved.files}
        if not metadata['complete'] or not metadata['run']['complete']:
            raise ValueError(f'Incomplete Euler run: {directory}')
        return metadata, arrays

    def compatible(left, right):
        for key in ('times', 'train_inputs', 'train_labels', 'query_inputs', 'query_labels'):
            if not np.array_equal(left[key], right[key]):
                raise ValueError(f'Mismatched {key} in the Euler comparison')

    pairs = {}
    for label, coarse_path, fine_path in args.pair:
        if label in pairs:
            raise ValueError(f'Duplicate Euler label: {label}')
        coarse, ca = load(coarse_path)
        fine, fa = load(fine_path)
        compatible(ca, fa)
        if coarse['initial_float64_sha256'] != fine['initial_float64_sha256']:
            raise ValueError(f'Changed initialization in step refinement: {label}')
        if not math.isclose(coarse['run']['step'], 2*fine['run']['step']):
            raise ValueError(f'Refinement is not step halving: {label}')
        pairs[label] = (coarse, ca, fine, fa)
    if args.reference not in pairs or args.iid not in pairs:
        raise ValueError('Both large reference and independent dense pair are required')
    reference, reference_arrays = pairs[args.reference][2:]
    for _, _, fine, fa in pairs.values():
        compatible(reference_arrays, fa)
        if fine['run']['step'] != reference['run']['step']:
            raise ValueError('Final models do not share the same Euler step')
    reference_predictions = reference_arrays['predictions'].astype(np.float64)
    iid_predictions = pairs[args.iid][3]['predictions'].astype(np.float64)
    variability = trajectory_rms(iid_predictions, reference_predictions)
    if variability['max_time_rms'] <= 0:
        raise ValueError('Zero dense variability makes the relative gate undefined')
    report = dict(metric='whole-validation prediction RMS; final time is primary',
                  scope='one split and one reference pair; new bounded packet initialization, '
                        'not the certified Logarithmic decoder or an asymptotic validation',
                  source_sha256=sha(Path(__file__).read_bytes()), config=dict(vars(args)),
                  reference_directory=next(row[2] for row in args.pair if row[0] == args.reference),
                  common_step=reference['run']['step'], steps=reference['run']['steps'],
                  horizon=reference['run']['actual_horizon'],
                  training_count=len(reference_arrays['train_labels']),
                  validation_count=len(reference_arrays['query_labels']),
                  dense_variability=variability, models={}, precision=[])
    report['config']['out'] = str(args.out)
    arrays = dict(times=reference_arrays['times'])
    for label, (coarse, ca, fine, fa) in pairs.items():
        prediction = fa['predictions'].astype(np.float64)
        sensitivity = trajectory_rms(prediction, ca['predictions'].astype(np.float64))
        error = trajectory_rms(prediction, reference_predictions)
        gate = (sensitivity['max_time_rms'] <= .001
                and sensitivity['max_time_rms'] <= .1*variability['max_time_rms'])
        mse = float(np.mean((fa['train_predictions'].astype(np.float64)
                            -fa['train_labels'].astype(np.float64))**2))
        report['models'][label] = dict(
            model=fine['method'], parameter_words=fine['parameter_words'],
            final_training_mse=mse, below_001=mse < .01,
            discrepancy=error, step_halving=sensitivity, numerical_gate_passed=gate,
            final_dense_variability_ratio=(error['endpoint_rms']/variability['endpoint_rms']
                                           if variability['endpoint_rms'] else None),
            max_dense_variability_ratio=error['max_time_rms']/variability['max_time_rms'],
            setup_seconds=fine['setup_seconds'], run_seconds=fine['run']['seconds'],
            setup_process_peak_cuda_bytes=fine['setup_process_peak_cuda_bytes'],
            run_process_peak_cuda_bytes=fine['run']['process_peak_cuda_bytes'],
            initial_float64_sha256=fine['initial_float64_sha256'])
        arrays[label+'_rms'] = np.sqrt(np.mean((prediction-reference_predictions)**2, axis=1))
    precision_coverage = {label: [] for label in pairs}
    for high_path, low_path in args.precision:
        high, ha = load(high_path)
        low, la = load(low_path)
        if high['run']['dtype'] != 'torch.float64' or low['run']['dtype'] != 'torch.float32':
            raise ValueError('Precision pairs must actually compare float64 with float32')
        if (high['initial_float64_sha256'] != low['initial_float64_sha256']
                or high['run']['step'] != low['run']['step']
                or not np.array_equal(ha['times'], la['times'])):
            raise ValueError('Precision check changed initialization, Euler step or observations')
        for key in ('train_inputs', 'train_labels', 'query_inputs', 'query_labels'):
            if not np.array_equal(ha[key].astype(la[key].dtype), la[key]):
                raise ValueError(f'Precision check changed {key}')
        error = trajectory_rms(ha['predictions'].astype(np.float64),
                               la['predictions'].astype(np.float64))
        matched_labels = []
        for label, (coarse, _, fine, fa) in pairs.items():
            if (fine['initial_float64_sha256'] == high['initial_float64_sha256']
                    and high['run']['step'] in (coarse['run']['step'], fine['run']['step'])):
                compatible(la, fa)
                matched_labels.append(label)
                precision_coverage[label].append(high['run']['step'])
        if not matched_labels:
            raise ValueError('Precision check does not cover any final model initialization')
        report['precision'].append(dict(float64_directory=high_path, float32_directory=low_path,
                                        tested_step=high['run']['step'], models=matched_labels,
                                        discrepancy=error, passed=error['max_time_rms'] < .00005))
    report['all_fitted'] = all(row['below_001'] for row in report['models'].values())
    report['all_numerically_resolved'] = all(row['numerical_gate_passed'] for row in report['models'].values())
    report['precision_coverage_steps'] = precision_coverage
    report['precision_passed'] = (all(precision_coverage.values())
                                  and all(row['passed'] for row in report['precision']))
    args.out.mkdir(parents=True, exist_ok=False)
    save_json(args.out/'report.json', report)
    np.savez_compressed(args.out/'rms.npz', **arrays)
    print(json.dumps(dict(all_fitted=report['all_fitted'],
                          all_numerically_resolved=report['all_numerically_resolved'],
                          precision_passed=report['precision_passed'],
                          models={label: dict(mse=row['final_training_mse'],
                                  endpoint_rms=row['discrepancy']['endpoint_rms'],
                                  max_time_rms=row['discrepancy']['max_time_rms'],
                                  step_halving_max=row['step_halving']['max_time_rms'])
                                  for label, row in report['models'].items()})), flush=True)


@torch.no_grad()
def finite_panel_rollout_sources(dense, inputs, labels, panel, horizon=100., step=.5,
                                degree=4, source_rank=32, seed=501, seconds=300.,
                                rollout_dtype=None):
    """Piecewise temporal sources from a disposable, full-horizon dense solve.

    Even Chebyshev nodes fit each polynomial; interlaced odd nodes only audit
    its error. No query label enters this function. Rank truncation acts on
    base families before their initialized images are formed by ``Harmonic``.
    This is a measured numerical source, not the theorem's certified compiler.
    """
    if horizon <= 0 or step <= 0 or degree < 1 or source_rank < 1:
        raise ValueError('Rollout horizon, step, degree and source rank must be positive')
    started = time.monotonic()
    boundaries = [0., min(1., horizon)]
    while boundaries[-1] < horizon:
        boundaries.append(min(2*boundaries[-1], horizon))
    intervals, all_times = [], []
    for left, right in zip(boundaries[:-1], boundaries[1:]):
        times = left+(right-left)*(1-np.cos(np.linspace(0, np.pi, 2*degree+1)))/2
        times[0], times[-1] = left, right
        intervals.append(times)
        all_times.extend(times)
    all_times = np.asarray(sorted(set(all_times)))
    teacher = Dense.__new__(Dense)
    teacher.initial_state = [v.to(dtype=rollout_dtype or v.dtype) for v in dense.initial_state]
    teacher.fixed_scalars = 0
    source_inputs, source_labels, source_panel = [v.to(dtype=teacher.initial_state[0].dtype)
                                                 for v in (inputs, labels, panel)]
    fields = {name: [] for name in ('h1', 'h2', 'delta1', 'delta2')}
    def observe(t, state):
        h1, h2, _ = dense_fields(state, source_panel)
        delta2 = state[1][:, None]*(1-h2[:, :len(labels)].square())
        delta1 = (state[2].T@delta2)*(1-h1[:, :len(labels)].square())
        for name, value in zip(fields, (h1, h2, delta1, delta2)):
            fields[name].append(value.clone())
    _, _, rollout = integrate(teacher, source_inputs, source_labels, source_panel[:1], all_times,
                              step, seconds, observer=observe)
    del teacher, source_inputs, source_labels, source_panel
    fields = {name: torch.stack(values) for name, values in fields.items()}
    h10, h20, _ = dense_fields(dense.initial_state, inputs)
    a0, _, matrix0 = dense.initial_state
    n = len(a0)
    constant = torch.ones(n, 1, dtype=a0.dtype, device=a0.device)
    mandatory = dict(h1=h10, h2=torch.cat((constant, h20, matrix0@h10), dim=1),
                     delta1=torch.cat((constant, a0, h10), dim=1))
    coefficients, diagnostics = {}, {}
    for family, values in fields.items():
        values = values.to(dtype=a0.dtype)
        blocks, fit_max, fit_square, fit_count = [], 0., 0., 0
        for times in intervals:
            index = np.searchsorted(all_times, times)
            coordinate = 2*(times-times[0])/(times[-1]-times[0])-1
            design = torch.as_tensor(np.polynomial.chebyshev.chebvander(coordinate, degree),
                                     dtype=values.dtype, device=values.device)
            fit = values[index[::2]]
            block = torch.einsum('kt,tnp->nkp', torch.linalg.pinv(design[::2]), fit)
            error = torch.einsum('tk,nkp->tnp', design[1::2], block)-values[index[1::2]]
            fit_max = max(fit_max, float(error.abs().max()))
            fit_square += float(error.square().sum())
            fit_count += error.numel()
            blocks.append(block.flatten(1))
        source = torch.cat(blocks, dim=1)
        del blocks, block, fit, error
        # Remove only components whose necessary initialized images are already
        # mandatory. In particular delta2 is NOT projected against h20.
        if family in mandatory:
            basis, _ = _harmonic_source_basis(mandatory[family], source[:, :0])
            basis = basis/math.sqrt(n)
            for _ in range(2):
                source -= basis@(basis.T@source)
        else:
            basis = source[:, :0]
        rank = min(source_rank+16, *source.shape)
        # A deterministic randomized SVD avoids a full n-by-(panel*modes) SVD.
        devices = [a0.device.index] if a0.device.type == 'cuda' else []
        with torch.random.fork_rng(devices=devices):
            torch.manual_seed(seed+list(fields).index(family))
            left, singular, _ = torch.svd_lowrank(source, q=rank, niter=2)
        numerical_rank = int((singular > max(source.shape)*torch.finfo(source.dtype).eps*
                              singular[0]).sum()) if len(singular) else 0
        retained = left[:, :min(source_rank, numerical_rank)]
        coefficients[family] = retained
        truncation = source-retained@(retained.T@source)
        # Audit projection of actual sampled fields, including unused fit nodes.
        projection_max = projection_rms = 0.
        for sample in values:
            residual = sample-basis@(basis.T@sample)
            residual -= retained@(retained.T@residual)
            projection_max = max(projection_max, float(residual.abs().max()))
            projection_rms = max(projection_rms, float(rms(residual)))
        diagnostics[family] = dict(coefficient_columns=source.shape[1], retained_rank=retained.shape[1],
            numerical_rank_within_randomized_subspace=numerical_rank,
            removed_mandatory_rank=basis.shape[1], heldout_temporal_max_abs=fit_max,
            heldout_temporal_rms=math.sqrt(fit_square/max(1, fit_count)),
            residual_coefficient_relative_error=float(truncation.norm()/source.norm().clamp_min(1e-30)),
            sampled_projection_max_abs=projection_max, sampled_projection_max_rms=projection_rms)
        del source, truncation, left, singular, values
        if time.monotonic()-started > seconds:
            raise TimeoutError('Finite-panel rollout/source compression exceeded its setup budget')
    synchronize(a0.device)
    return coefficients, dict(method='piecewise_chebyshev_dense_rollout',
        horizon=horizon, rk4_step=step, degree_per_interval=degree, boundaries=boundaries,
        source_observation_count=len(all_times), fitted_node_rule='even indices; odd indices held out',
        source_rank_cap=source_rank, source_checks=diagnostics, rollout=rollout,
        rollout_dtype=str(rollout_dtype or a0.dtype), assembly_dtype=str(a0.dtype),
        seconds=time.monotonic()-started, dense_training_rhs_calls=4*rollout['steps'],
        source_contract='full physical interval; disposable teacher; not an early-prefix extrapolation',
        source_certificate=False, passive_labels_used=False)


@torch.no_grad()
def finite_panel_initial_jets(dense, inputs, labels, panel):
    """Order-two dense initialization jets, with no trajectory observations.

    Forward coefficients cover all predeclared inputs; backward coefficients
    involve training inputs only. Second derivatives are divided by 2!, so
    these are Taylor coefficients, not samples from an evolved dense model.
    """
    a, w, matrix = dense.initial_state
    if bool(w.ne(0).any()):
        raise ValueError('Finite-panel jets require zero initial readout')
    if not torch.equal(panel[:len(inputs)], inputs):
        raise ValueError('The panel must start with the training inputs')
    h1, h2, _ = dense_fields(dense.initial_state, panel)
    m, n = len(labels), len(w)
    train1, train2 = h1[:, :m], h2[:, :m]
    dw = (2/m)*(train2@labels)
    dc = (-2/m)*(train2.T@(train2@labels)/n)
    ddw = (2/m)*(train2@dc)
    delta2_first = (1-train2.square())*dw[:, None]
    delta1_first = (1-train1.square())*(matrix.T@delta2_first)
    delta2_second = (1-train2.square())*ddw[:, None]
    delta1_second = (1-train1.square())*(matrix.T@delta2_second)
    dda = (2/m)*(delta1_first*labels)@inputs
    ddb = (2/(m*n))*(delta2_first*labels)@train1.T
    ddh1 = (1-h1.square())*(dda@panel.T)
    ddh2 = (1-h2.square())*(ddb@h1+matrix@ddh1)
    return dict(h1=torch.cat((h1, .5*ddh1), dim=1),
                h2=torch.cat((h2, .5*ddh2), dim=1),
                delta1=torch.cat((delta1_first, .5*delta1_second), dim=1),
                delta2=torch.cat((delta2_first, .5*delta2_second), dim=1)), [dda, ddw, ddb]


class FinitePanelCompression(Harmonic):
    """Empirical zero-time-jet compiler for the finite-panel corrected runtime.

    Only source generation/coordinate selection differ from the Harmonic
    compiler. The nonlinear autonomous equations are precisely the shared
    metric/deficit optimizer. Low-order jets and numerical selection do not
    inherit the continued-source theorem's all-time accuracy certificate.
    """

    def __init__(self, dense, inputs, labels, queries, budget=768, source_rank=8,
                 selection_seed=501, source_mode='jets', source_horizon=100.,
                 source_step=.5, time_degree=4, source_dtype=None):
        panel = torch.cat((inputs, queries))
        if source_mode == 'rollout':
            sources, source_info = finite_panel_rollout_sources(dense, inputs, labels, panel,
                source_horizon, source_step, time_degree, source_rank, selection_seed,
                rollout_dtype=source_dtype)
        elif source_mode == 'jets':
            sources, _ = finite_panel_initial_jets(dense, inputs, labels, panel)
            source_info = dict(method='order_two_initial_jets', source_jet_order=2,
                               dense_training_rhs_calls=0)
        else:
            raise ValueError('Unknown finite-panel source mode')
        super().__init__(dense, inputs, labels, sources, budget=budget,
                         source_rank=None if source_mode == 'rollout' else source_rank,
                         selector='panel-conditioned' if source_mode == 'rollout' else 'panel-uniform',
                         selection_seed=selection_seed)
        self.diagnostics.update(branch='finite_panel_'+source_mode, source=source_info,
            training_inputs=len(inputs), passive_inputs=len(queries),
            passive_labels_used=False, passive_inputs_declared_before_initialization=True,
            source_scope=('rank-truncated measured rollout coefficients' if source_mode == 'rollout'
                          else 'rank-truncated order-two jets, not continued global source coefficients'),
            guarantee='empirical only; no log^5 accuracy certificate')


@torch.no_grad()
def finite_panel_small_checks():
    """Independent jet oracle, algebra, restart and information-flow checks."""
    torch.set_default_dtype(torch.float64)
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]])
    labels = torch.tensor([.7, -.4, .3])
    queries = torch.tensor([[0., 1.], [-.6, -.8]])
    dense = Dense(80, 2, 201, 'cpu')
    state = tuple(dense.initial_state)
    velocity = tuple(dense_rhs(state, inputs, labels))
    sources, acceleration = finite_panel_initial_jets(
        dense, inputs, labels, torch.cat((inputs, queries)))
    _, oracle = torch.func.jvp(lambda *s: tuple(dense_rhs(s, inputs, labels)), state, velocity)
    jet_error = max(float((a-b).abs().max()) for a, b in zip(acceleration, oracle))
    _, forward_oracle = torch.func.jvp(
        lambda *s: dense_fields(s, torch.cat((inputs, queries)))[:2], state, tuple(acceleration))
    for name, expected in zip(('h1', 'h2'), forward_oracle):
        jet_error = max(jet_error, float((2*sources[name][:, 5:]-expected).abs().max()))
    assert jet_error < 1e-12, jet_error
    model = FinitePanelCompression(dense, inputs, labels, queries, budget=48, source_rank=2)
    errors = model.diagnostics['mandatory_source_errors']+model.diagnostics['initialized_feature_errors']
    errors += [model.diagnostics[key] for key in (
        'initialized_gram_error', 'paired_forward_action_error', 'paired_reverse_action_error')]
    errors += [row[key] for row in model.diagnostics['selection']
               for key in ('source_isometry_error', 'metric_inverse_error')]
    assert max(errors) < 1e-10, errors
    final, prediction, info = integrate_euler(model, inputs, labels, queries,
        step=.005, seconds=20, horizon=.2, observation_every=20)
    checks = model.runtime_checks(final, inputs, labels)
    assert checks['training_constraint_error'] < 1e-11, checks
    assert checks['gram_action_error'] < 1e-11, checks
    restored = FinitePanelCompression.__new__(FinitePanelCompression)
    restored.metrics = [x.clone() for x in model.metrics]
    restored.metric_inverses = [x.clone() for x in model.metric_inverses]
    restored.initial_state = [x.clone() for x in final]
    restored.fixed_scalars = model.fixed_scalars
    restart_error = max(float((a-b).abs().max()) for a, b in zip(
        model.rhs(final, inputs, labels), restored.rhs(restored.initial_state, inputs, labels)))
    assert restart_error == 0
    assert not any(hasattr(model, key) for key in ('dense', 'sources', 'panel', 'queries'))
    assert model.fixed_scalars == sum(x.numel() for x in model.metrics+model.metric_inverses)
    return dict(jet_jvp_max_abs=jet_error, setup_max_abs=max(errors),
                runtime=checks, restart_rhs_max_abs=restart_error,
                passive_labels_used=False, full_dense_or_source_retained=False)


def finite_panel_rollout_checks():
    """Small deterministic source/paired-action/restart checks, without data."""
    dense = Dense(96, 3, 811, 'cpu')
    generator = torch.Generator().manual_seed(812)
    panel = torch.randn(10, 3, generator=generator)
    panel /= panel.norm(dim=1, keepdim=True)
    inputs, queries = panel[:4], panel[4:]
    labels = torch.tensor([.2, -.3, .4, -.1])
    model = FinitePanelCompression(dense, inputs, labels, queries, budget=80,
        source_rank=4, source_mode='rollout', source_horizon=1., source_step=.025, time_degree=3)
    checks = model.runtime_checks(model.initial_state, inputs, labels)
    errors = [model.diagnostics[name] for name in
              ('initialized_gram_error', 'paired_forward_action_error', 'paired_reverse_action_error')]
    errors += model.diagnostics['initialized_feature_errors']
    if max(errors) > 1e-9:
        raise AssertionError(('rollout initialization', errors))
    restart = FinitePanelCompression.__new__(FinitePanelCompression)
    for key in ('initial_state', 'metrics', 'metric_inverses'):
        setattr(restart, key, [v.clone() for v in getattr(model, key)])
    restart.fixed_scalars = model.fixed_scalars
    expected, actual = model.rhs(model.initial_state, inputs, labels), restart.rhs(
        restart.initial_state, inputs, labels)
    restart_error = max(float((a-b).abs().max()) for a, b in zip(actual, expected))
    if restart_error > 1e-12:
        raise AssertionError(('rollout restart', restart_error))
    return dict(setup_max_abs=max(errors), runtime=checks, restart_rhs_max_abs=restart_error,
                source=model.diagnostics['source'], selection=model.diagnostics['selection'])


def finite_panel_summary_main(argv):
    """Audit common data/time/Euler contracts and compare saved predictions."""
    parser = argparse.ArgumentParser(description='Audit a one-pair finite-panel comparison')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--primary', choices=('endpoint', 'trajectory'), default='endpoint')
    for name in ('dense', 'iid', 'panel', 'small'):
        parser.add_argument('--'+name, type=Path, required=True)
        parser.add_argument('--'+name+'-coarse', type=Path, required=True)
    args = parser.parse_args(argv)
    rows, arrays, refinements, reports = {}, {}, {}, {}
    reference_arrays = None
    for name in ('dense', 'iid', 'panel', 'small'):
        directory = getattr(args, name)
        report = json.loads((directory/'report.json').read_text())
        coarse_report = json.loads((getattr(args, name+'_coarse')/'report.json').read_text())
        expected_model = dict(dense='dense', iid='dense', panel='panel', small='small')[name]
        if report['config']['model'] != expected_model or coarse_report['config']['model'] != expected_model:
            raise ValueError(f'{name}: incorrect model identity')
        for key in ('seed', 'width', 'budget', 'source_rank', 'dtype'):
            if report['config'][key] != coarse_report['config'][key]:
                raise ValueError(f'{name}: coarse/fine {key} mismatch')
        with np.load(directory/'trajectories.npz') as data:
            current = {k: data[k] for k in data.files}
        with np.load(getattr(args, name+'_coarse')/'trajectories.npz') as data:
            coarse = {k: data[k] for k in data.files}
        if reference_arrays is None:
            reference_arrays = current
        for other in (reference_arrays, coarse):
            for key in ('times', 'train_inputs', 'train_labels', 'query_inputs', 'query_labels'):
                if not np.array_equal(current[key], other[key]):
                    raise ValueError(f'{name}: incompatible {key}')
        if (not report['complete'] or not coarse_report['complete']
                or report['run']['method'] != 'explicit_euler'
                or coarse_report['run']['method'] != 'explicit_euler'
                or not math.isclose(coarse_report['run']['step'], 2*report['run']['step'])
                or report['initial_float64_sha256'] != coarse_report['initial_float64_sha256']):
            raise ValueError(f'{name}: incomplete or unmatched half-step comparison')
        if name == 'panel' and report.get('checkpoint_sha256') != coarse_report.get('checkpoint_sha256'):
            raise ValueError('Panel refinements use different metric/state checkpoints')
        if name == 'panel':
            for candidate in (report, coarse_report):
                source = candidate['setup'].get('source', {})
                if (source.get('method') == 'piecewise_chebyshev_dense_rollout' and
                        candidate['run']['actual_horizon'] > source['horizon']+1e-10):
                    raise ValueError('Panel trajectory exceeds the compiled source horizon')
        if name != 'dense' and report['run']['step'] != reports['dense']['run']['step']:
            raise ValueError('Models do not use the same final Euler step')
        if name != 'dense' and report['run']['dtype'] != reports['dense']['run']['dtype']:
            raise ValueError('Models do not use the same runtime precision')
        predictions, reference = current['predictions'], reference_arrays['predictions']
        refinements[name] = trajectory_rms(predictions, coarse['predictions'])
        comparison = trajectory_rms(predictions, reference)
        times = current['times']
        curve = np.asarray(comparison['curve'])
        comparison['time_average_validation_rms'] = float(np.trapz(curve, times)/times[-1])
        comparison['time_weighted_prediction_rms'] = float(np.sqrt(np.trapz(curve**2, times)/times[-1]))
        rows[name] = dict(hidden_widths=report['hidden_widths'],
            moving_words=report['moving_words'], fixed_words=report['fixed_words'],
            total_model_words=report['total_model_words'], common_data_words=report['common_data_words'],
            training_mse=report['run']['final_training_mse'], comparison=comparison,
            setup_seconds=report['setup_seconds'], training_seconds=report['run']['seconds'],
            euler_steps=report['run']['steps'], step_halving=refinements[name],
            setup_process_peak_cuda_bytes=report['setup_process_peak_cuda_bytes'],
            run_process_peak_cuda_bytes=report['run']['process_peak_cuda_bytes'],
            source_directory=str(directory), coarse_directory=str(getattr(args, name+'_coarse')))
        arrays[name] = predictions
        reports[name] = report
    dense_config, panel_config, iid_config = [reports[name]['config'] for name in ('dense', 'panel', 'iid')]
    if (dense_config['width'] != panel_config['width'] or dense_config['seed'] != panel_config['seed']
            or iid_config['width'] != dense_config['width'] or iid_config['seed'] == dense_config['seed']):
        raise ValueError('Panel/source or iid/reference initialization contract mismatch')
    if reports['small']['matched_panel_words'] != rows['panel']['total_model_words']:
        raise ValueError('Small control was matched to a different model budget')
    gate = (.1*rows['iid']['comparison']['max_time_rms'] if args.primary == 'trajectory' else
            .1*min(rows[name]['comparison']['endpoint_rms'] for name in ('iid', 'panel', 'small')))
    endpoint_gate = .1*rows['iid']['comparison']['endpoint_rms'] if args.primary == 'trajectory' else gate
    # Sum both models' measured discretization discrepancies for every comparison.
    for name in ('iid', 'panel', 'small'):
        rows[name]['numerical_gate_passed'] = (
            refinements[name]['max_time_rms']+refinements['dense']['max_time_rms'] < gate)
        rows[name]['endpoint_refinement_sum'] = (
            refinements[name]['endpoint_rms']+refinements['dense']['endpoint_rms'])
        rows[name]['endpoint_numerically_resolved'] = rows[name]['endpoint_refinement_sum'] < endpoint_gate
        rows[name]['dense_variability_ratio'] = (rows[name]['comparison']['max_time_rms']/
                                                rows['iid']['comparison']['max_time_rms'])
    if rows['small']['total_model_words'] > rows['panel']['total_model_words']:
        raise ValueError('Small dense control exceeds the declared matching budget')
    args.out.mkdir(parents=True, exist_ok=False)
    result = dict(rows=rows, horizon=float(reference_arrays['times'][-1]),
        step=reports['dense']['run']['step'], validation_count=len(reference_arrays['query_labels']),
        training_count=len(reference_arrays['train_labels']),
        all_fitted=all(row['training_mse'] < .01 for row in rows.values()),
        numerical_gate_absolute=gate,
        endpoint_numerical_gate_absolute=endpoint_gate, primary=args.primary,
        all_numerically_resolved=all(rows[name]['numerical_gate_passed'] for name in ('iid', 'panel', 'small')),
        endpoints_numerically_resolved=all(
            rows[name]['endpoint_numerically_resolved'] for name in ('iid', 'panel', 'small')),
        panel_better_than_matched_small=rows['panel']['comparison']['endpoint_rms'] <
                                       rows['small']['comparison']['endpoint_rms'],
        panel_trajectory_better_than_matched_small=rows['panel']['comparison']['max_time_rms'] <
                                                   rows['small']['comparison']['max_time_rms'],
        panel_trajectory_within_three_dense_pairs=rows['panel']['dense_variability_ratio'] <= 3,
        setup=reports['panel']['setup'],
        approximation=reports['panel']['setup'].get('source_scope', 'empirical finite-panel source'),
        source_sha256=sha(Path(__file__).read_bytes()),
        metric='RMS of prediction differences over all validation images, not classification accuracy')
    save_json(args.out/'report.json', result)
    np.savez_compressed(args.out/'predictions.npz', times=reference_arrays['times'], **arrays)
    print(json.dumps({k: v for k, v in result.items() if k not in ('setup', 'rows')}), flush=True)
    print(json.dumps({name: dict(total_model_words=row['total_model_words'],
        training_mse=row['training_mse'],
        endpoint_rms=row['comparison']['endpoint_rms'],
        time_average_validation_rms=row['comparison']['time_average_validation_rms'],
        sampled_max_time_rms=row['comparison']['max_time_rms'],
        step_halving_endpoint=row['step_halving']['endpoint_rms'],
        step_halving_sampled_max=row['step_halving']['max_time_rms'])
        for name, row in rows.items()}), flush=True)


def finite_panel_fit_main(argv):
    """One fixed-panel setup or fair physical-Euler digit comparison run."""
    parser = argparse.ArgumentParser(description='Predeclared-panel temporal-source compression')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--model', choices=('panel', 'dense', 'small'), default='panel')
    parser.add_argument('--width', type=int, default=4096)
    parser.add_argument('--budget', type=int, default=768)
    parser.add_argument('--source-rank', type=int, default=8)
    parser.add_argument('--source-mode', choices=('jets', 'rollout'), default='jets')
    parser.add_argument('--source-horizon', type=float, default=100.)
    parser.add_argument('--source-step', type=float, default=.5)
    parser.add_argument('--source-dtype', choices=('float64', 'float32'), default='float64')
    parser.add_argument('--time-degree', type=int, default=4)
    parser.add_argument('--seed', type=int, default=201)
    parser.add_argument('--digits', type=int, nargs=2, default=(3, 8))
    parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--setup-only', action='store_true')
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--step', type=float, default=.05)
    parser.add_argument('--horizon', type=float)
    parser.add_argument('--max-horizon', type=float, default=200.)
    parser.add_argument('--loss-target', type=float, default=.005)
    parser.add_argument('--per-run-seconds', type=float, default=300.)
    parser.add_argument('--dtype', choices=('float64', 'float32'), default='float64')
    args = parser.parse_args(argv)
    if (args.width < 1 or not 0 < args.step <= .5 or args.max_horizon <= 0
            or args.budget < 1 or args.source_rank < 0
            or not math.isclose(.5/args.step, round(.5/args.step), abs_tol=1e-9)):
        parser.error('Invalid size/order/time parameters; Euler step must divide 0.5')
    if args.model == 'small' and args.checkpoint is None:
        parser.error('The small dense control requires --checkpoint for total-state matching')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    report = dict(config={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        git_head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
        threads=torch.get_num_threads(), complete=False,
        experiment_scope='one digit pair; empirical finite-panel temporal source construction',
        passive_inputs_known_at_setup=True, passive_labels_used=False)
    save_json(args.out/'report.json', report)
    if args.check_only:
        checks = finite_panel_small_checks()
        if args.source_mode == 'rollout':
            checks['rollout'] = finite_panel_rollout_checks()
        report.update(checks=checks, complete=True)
        save_json(args.out/'report.json', report)
        print(json.dumps(report['checks']), flush=True)
        return
    report['device'] = torch.cuda.get_device_name(args.device) if args.device.startswith('cuda') else 'CPU'
    inputs, labels, queries, truth = validation_data(64, 100, 0, 47, args.device,
                                                    'digits', 'test', True, 0, args.digits)
    data_hashes = dict(train_inputs=array_sha(inputs.cpu().numpy()),
                       training_labels=array_sha(labels.cpu().numpy()),
                       passive_inputs=array_sha(queries.cpu().numpy()))
    report.update(data_sha256=data_hashes, training_count=len(inputs), validation_count=len(queries),
        preprocessing='all 64 raw pixels, per-image unit normalization; no PCA',
        common_data_words=inputs.numel()+labels.numel()+queries.numel(),
        retained_scope='deployable current state plus fixed metrics/inverse; common data separately; '
                       'excludes benchmark initial-state copy, Euler RHS/temporaries and saved observations',
        initial_source='float64 Gaussian initialization, then optional runtime dtype conversion')
    synchronize(inputs.device)
    started = time.monotonic()
    if inputs.device.type == 'cuda':
        torch.cuda.reset_peak_memory_stats(inputs.device)
    try:
        payload = None
        if args.checkpoint is not None:
            payload = torch.load(args.checkpoint, map_location=args.device, weights_only=True)
            if payload['data_sha256'] != data_hashes:
                raise ValueError('Checkpoint training/panel inputs or training labels differ')
            report['checkpoint_sha256'] = sha(args.checkpoint.read_bytes())
        if args.model == 'panel':
            if payload is None:
                # The full panel was loaded before the Gaussian reference is initialized.
                dense = Dense(args.width, 64, args.seed, args.device)
                model = FinitePanelCompression(dense, inputs, labels, queries,
                    budget=args.budget, source_rank=args.source_rank, source_mode=args.source_mode,
                    source_horizon=args.source_horizon, source_step=args.source_step,
                    time_degree=args.time_degree, source_dtype=getattr(torch, args.source_dtype))
                del dense
                payload = dict(initial_state=[v.cpu() for v in model.initial_state],
                    metrics=[v.cpu() for v in model.metrics],
                    metric_inverses=[v.cpu() for v in model.metric_inverses],
                    fixed_scalars=model.fixed_scalars, diagnostics=model.diagnostics,
                    data_sha256=data_hashes, source_width=args.width, source_seed=args.seed,
                    compiler_source_sha256=report['source_sha256'], compiler_config=report['config'])
                torch.save(payload, args.out/'compiled_model.pt')
            else:
                if payload['source_width'] != args.width or payload['source_seed'] != args.seed:
                    raise ValueError('Checkpoint source width/seed mismatch')
                model = FinitePanelCompression.__new__(FinitePanelCompression)
                for key in ('initial_state', 'metrics', 'metric_inverses', 'fixed_scalars', 'diagnostics'):
                    setattr(model, key, payload[key])
            report['setup'] = model.diagnostics
            report['compiler_source_sha256'] = payload.get('compiler_source_sha256')
            report['compiler_config'] = payload.get('compiler_config')
            report['effective_source_config'] = dict(source=model.diagnostics.get('source'),
                requested_budget=model.diagnostics.get('requested_budget'),
                hidden_widths=model.diagnostics.get('widths'), selector=model.diagnostics.get('selector'))
        else:
            width = args.width
            if args.model == 'small':
                total = sum(v.numel() for v in payload['initial_state'])+payload['fixed_scalars']
                width = math.floor((math.sqrt(65**2+4*total)-65)/2)
                report['matched_panel_words'] = total
                report['matching_shortfall_words'] = total-width*(width+65)
            model = Dense(width, 64, args.seed, args.device)
        synchronize(inputs.device)
        report['setup_seconds'] = time.monotonic()-started
        report['setup_process_peak_cuda_bytes'] = (torch.cuda.max_memory_allocated(inputs.device)
                                                  if inputs.device.type == 'cuda' else None)
        report['initial_float64_sha256'] = [array_sha(v.cpu().numpy()) for v in model.initial_state]
        report['moving_words'] = sum(v.numel() for v in model.initial_state)
        report['benchmark_restart_copy_words'] = report['moving_words']
        report['fixed_words'] = int(model.fixed_scalars)
        report['total_model_words'] = report['moving_words']+report['fixed_words']
        report['hidden_widths'] = [len(model.initial_state[0]), len(model.initial_state[1])]
        if args.model == 'panel' and model.diagnostics.get('source', {}).get('method') == 'piecewise_chebyshev_dense_rollout':
            source_horizon = model.diagnostics['source']['horizon']
            report['source_horizon'] = source_horizon
            if args.horizon is not None and args.horizon > source_horizon+1e-10:
                raise ValueError('Requested training horizon exceeds this checkpoint source horizon')
        del payload
        if report['setup_seconds'] > 300:
            raise TimeoutError('Panel setup exceeded its 300-second budget')
        if args.setup_only:
            report['complete'] = True
            save_json(args.out/'report.json', report)
            print(json.dumps(dict(event='panel_setup_complete', **{
                k: report[k] for k in ('setup_seconds', 'total_model_words', 'hidden_widths')})), flush=True)
            return
        dtype = getattr(torch, args.dtype)
        model.initial_state = [v.to(dtype=dtype) for v in model.initial_state]
        if hasattr(model, 'metrics'):
            model.metrics = [v.to(dtype=dtype) for v in model.metrics]
            model.metric_inverses = [v.to(dtype=dtype) for v in model.metric_inverses]
        inputs, labels, queries, truth = [v.to(dtype=dtype) for v in (inputs, labels, queries, truth)]
        save_json(args.out/'report.json', report)
        print(json.dumps(dict(event='panel_euler_start', model=args.model, seed=args.seed,
            widths=report['hidden_widths'], step=args.step, horizon=args.horizon)), flush=True)
        state, predictions, info = integrate_euler(model, inputs, labels, queries,
            args.step, args.per_run_seconds, horizon=args.horizon, loss_target=args.loss_target,
            max_steps=round(args.max_horizon/args.step), observation_every=round(.5/args.step))
        report.update(run=info, complete=info['complete'])
        if 'source_horizon' in report:
            report['within_source_horizon'] = info['actual_horizon'] <= report['source_horizon']+1e-10
            if not report['within_source_horizon']:
                report['source_scope_warning'] = 'Training extrapolated beyond the compiled source interval'
        if hasattr(model, 'runtime_checks'):
            report['final_runtime_checks'] = model.runtime_checks(state, inputs, labels)
        np.savez_compressed(args.out/'trajectories.npz', predictions=predictions,
            times=np.asarray(info['times']), training_mse=np.asarray(info['losses']),
            train_inputs=inputs.cpu().numpy(), train_labels=labels.cpu().numpy(),
            query_inputs=queries.cpu().numpy(), query_labels=truth.cpu().numpy(),
            train_predictions=model.predict(state, inputs, inputs, labels).detach().cpu().numpy())
        save_json(args.out/'report.json', report)
        print(json.dumps(dict(event='panel_euler_complete', model=args.model, **{
            k: info[k] for k in ('actual_horizon', 'final_training_mse', 'steps', 'seconds', 'stop_reason')})),
            flush=True)
    except (RuntimeError, ValueError, ArithmeticError, TimeoutError) as error:
        report['error'] = f'{type(error).__name__}: {error}'
        save_json(args.out/'report.json', report)
        raise


@torch.no_grad()
def deep_rollout_sources(dense, inputs, labels, calibration, horizon, rank, seed, seconds=180.):
    """Measured temporal sources; scored query inputs are deliberately not an argument."""
    panel = torch.cat((inputs, calibration))
    boundaries = [0., min(1., horizon)]
    while boundaries[-1] < horizon:
        boundaries.append(min(2*boundaries[-1], horizon))
    intervals = [left+(right-left)*(1-np.cos(np.linspace(0, np.pi, 17)))/2
                 for left, right in zip(boundaries[:-1], boundaries[1:])]
    times = np.unique(np.concatenate(intervals))
    fields = {name: [[] for _ in range(dense.depth)] for name in ('h', 'delta')}
    teacher = DeepDense.__new__(DeepDense)
    teacher.depth, teacher.activation = dense.depth, dense.activation
    teacher.initial_state = [v.float() for v in dense.initial_state]
    teacher.fixed_scalars = 0
    source_inputs, source_labels, source_panel = [v.float() for v in (inputs, labels, panel)]
    def observe(t, state):
        hs, gates = teacher.fields(state, source_panel)
        deltas = teacher.backward(state, [h[:, :len(labels)] for h in hs],
                                  [g[:, :len(labels)] for g in gates])
        for name, values in (('h', hs), ('delta', deltas)):
            for layer, value in enumerate(values):
                fields[name][layer].append(value.cpu())
    _, _, source_run = integrate(teacher, source_inputs, source_labels, source_inputs[:1],
                                 times, .125, seconds, observer=observe)
    del teacher, source_inputs, source_labels, source_panel
    h0, _ = dense.fields(dense.initial_state, inputs)
    n, device = len(dense.initial_state[1]), inputs.device
    constant = torch.ones(n, 1, dtype=inputs.dtype, device=device)
    coefficients, checks = {name: [] for name in fields}, {name: [] for name in fields}
    for name in fields:
        for layer, observations in enumerate(fields[name]):
            values = torch.stack(observations).to(device=device, dtype=torch.float64)
            blocks, square, count = [], 0., 0
            for nodes in intervals:
                indices = np.searchsorted(times, nodes)
                coordinate = 2*(nodes-nodes[0])/(nodes[-1]-nodes[0])-1
                design = torch.as_tensor(np.polynomial.chebyshev.chebvander(coordinate, 8),
                                         dtype=values.dtype, device=device)
                block = torch.einsum('kt,tnp->nkp', torch.linalg.pinv(design[::2]), values[indices[::2]])
                error = torch.einsum('tk,nkp->tnp', design[1::2], block)-values[indices[1::2]]
                square += float(error.square().sum())
                count += error.numel()
                blocks.append(block.flatten(1))
            source = torch.cat(blocks, dim=1)
            # Remove only directions whose required initialized images are already
            # mandatory; other layers' reverse images must not be lost.
            mandatory = source[:, :0]
            if name == 'h':
                mandatory = h0[layer]
                if layer == dense.depth-1:
                    mandatory = torch.cat((constant, h0[layer], dense.initial_state[layer+1]@h0[layer-1]), 1)
            elif layer == 0:
                mandatory = torch.cat((constant, dense.initial_state[0], h0[0]), 1)
            if mandatory.shape[1]:
                basis, _ = _harmonic_source_basis(mandatory, source[:, :0])
                basis = basis/math.sqrt(n)
                for _ in range(2):
                    source -= basis@(basis.T@source)
            devices = [device.index] if device.type == 'cuda' else []
            with torch.random.fork_rng(devices=devices):
                torch.manual_seed(seed+layer+(100 if name == 'delta' else 0))
                left, singular, _ = torch.svd_lowrank(source, q=min(rank+8, *source.shape), niter=2)
            available = int((singular > max(source.shape)*torch.finfo(source.dtype).eps*singular[0]).sum())
            retained = left[:, :min(rank, available)]
            coefficients[name].append(retained)
            checks[name].append(dict(rank=retained.shape[1], temporal_holdout_rms=math.sqrt(square/count),
                residual_coefficient_relative_error=float((source-retained@(retained.T@source)).norm()
                                                          /source.norm().clamp_min(1e-30))))
            del values, blocks, source, left, singular, error, block
    return coefficients, dict(horizon=horizon, rk4_step=.125, chebyshev_degree=8,
        observation_count=len(times), boundaries=boundaries, dense_rhs_calls=4*source_run['steps'],
        source_run_seconds=source_run['seconds'], diagnostics=checks,
        training_count=len(inputs), unlabeled_calibration_count=len(calibration),
        scored_inputs_used=False, calibration_labels_used=False, source_certificate=False)


@torch.no_grad()
def compression_probe_main(argv):
    """One small, fixed-budget unseen-query comparison, with no parameter search."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--width', type=int, default=8192)
    parser.add_argument('--depth', type=int, default=3)
    parser.add_argument('--activation', choices=('tanh', 'atan'), default='tanh')
    parser.add_argument('--digits', type=int, nargs=2, default=(3, 8))
    parser.add_argument('--samples', type=int, default=8)
    parser.add_argument('--calibration', type=int, default=32)
    parser.add_argument('--seed', type=int, default=601)
    parser.add_argument('--horizon', type=float, default=32.)
    parser.add_argument('--step', type=float, default=.003125)
    parser.add_argument('--per-run-seconds', type=float, default=180.)
    args = parser.parse_args(argv)
    if args.depth < 2 or args.width < 1 or args.samples < 2 or args.calibration < 1:
        parser.error('Need depth>=2, positive width/calibration and at least two samples')
    if (not math.isfinite(args.horizon) or args.horizon <= 0 or not math.isfinite(args.step)
            or args.step <= 0 or not math.isclose(.5/(2*args.step), round(.5/(2*args.step)), abs_tol=1e-9)):
        parser.error('Need a positive horizon and a step whose double divides the 0.5 observation interval')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    scale = (math.log(math.e*args.width)/math.log(math.e*4096))**2.5
    budget, rank = math.ceil(320*scale), math.ceil(12*scale)
    report = dict(config={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
        device=torch.cuda.get_device_name(device) if device.type == 'cuda' else 'CPU',
        budget=budget, source_rank=rank, complete=False, runs={}, comparisons={})
    arrays = {}
    save_json(args.out/'report.json', report)
    try:
        inputs, labels, pool, truth = validation_data(64, args.samples, 0, 47, device,
                                                     'digits', 'test', True, 0, args.digits)
        permutation = np.random.default_rng(48).permutation(len(pool))
        calibration = pool[permutation[:args.calibration]]
        queries, query_truth = pool[permutation[args.calibration:]], truth[permutation[args.calibration:]]
        if len(queries) == 0 or bool(((calibration[:, None]-queries[None]).square().sum(-1) == 0).any()):
            raise ValueError('Calibration/test sets must be nonempty and disjoint')
        arrays.update(train_inputs=inputs.cpu().numpy(), train_labels=labels.cpu().numpy(),
                      calibration_inputs=calibration.cpu().numpy(), query_inputs=queries.cpu().numpy(),
                      query_labels=query_truth.cpu().numpy())
        report['data_sha256'] = {key: array_sha(value) for key, value in arrays.items()}
        report['validation_count'] = len(queries)
        report['common_training_words'] = inputs.numel()+labels.numel()
        report['transient_calibration_words'] = calibration.numel()
        synchronize(device)
        started = time.monotonic()
        if device.type == 'cuda':
            torch.cuda.reset_peak_memory_stats(device)
        dense = DeepDense(args.width, 64, args.depth, args.activation, args.seed, device)
        coefficients, source = deep_rollout_sources(dense, inputs, labels, calibration,
                                                    args.horizon, rank, args.seed)
        compact = DeepHarmonic(dense, inputs, labels, coefficients, budget=budget)
        del coefficients
        synchronize(device)
        report['setup'] = dict(seconds=time.monotonic()-started, source=source,
            diagnostics=compact.diagnostics, peak_cuda_bytes=torch.cuda.max_memory_allocated(device)
            if device.type == 'cuda' else None)
        if report['setup']['seconds'] > 180:
            raise TimeoutError('Source compilation exceeded its 180-second budget')
        for name, model in (('dense', dense), ('compact', compact)):
            moving = sum(v.numel() for v in model.initial_state)
            report[name+'_words'] = dict(moving=moving, fixed=model.fixed_scalars,
                                         total=moving+model.fixed_scalars)
        expected = (3*args.depth-2)*budget**2+65*budget+args.samples
        assert report['compact_words']['total'] == expected
        small_width = math.floor((math.sqrt(65**2+4*(args.depth-1)*expected)-65)/(2*(args.depth-1)))
        report['small_width'] = small_width
        report['storage_reduction'] = report['dense_words']['total']/expected
        def move(model, destination):
            for key in ('initial_state', 'metrics', 'metric_inverses'):
                if hasattr(model, key):
                    setattr(model, key, [v.to(device=destination, dtype=torch.float32) for v in getattr(model, key)])
        move(dense, 'cpu')
        move(compact, 'cpu')
        torch.save(dict(depth=compact.depth, activation=compact.activation,
                        initial_state=compact.initial_state, metrics=compact.metrics,
                        metric_inverses=compact.metric_inverses), args.out/'compiled_model.pt')
        report['checkpoint_sha256'] = sha((args.out/'compiled_model.pt').read_bytes())
        inputs, labels, queries = [v.float() for v in (inputs, labels, queries)]
        del calibration, pool, truth
        for name in ('dense', 'compact', 'iid', 'small'):
            model = (dense if name == 'dense' else compact if name == 'compact' else
                     DeepDense(args.width if name == 'iid' else small_width, 64, args.depth,
                               args.activation, args.seed+(10000 if name == 'iid' else 20000), device))
            move(model, device)
            words = sum(v.numel() for v in model.initial_state)+model.fixed_scalars
            for suffix, step in ([('_coarse', 2*args.step), ('', args.step)]
                                 if name in ('dense', 'compact') else [('', args.step)]):
                print(json.dumps(dict(event='probe_start', model=name+suffix, step=step,
                                      width=args.width, depth=args.depth)), flush=True)
                state, prediction, info = integrate_euler(model, inputs, labels, queries, step,
                    args.per_run_seconds, horizon=args.horizon, max_steps=math.ceil(args.horizon/step),
                    observation_every=round(.5/step))
                report['runs'][name+suffix] = dict(info, total_model_words=words)
                arrays[name+suffix] = prediction
                arrays['times'] = np.asarray(info['times'])
                if not info['complete']:
                    raise TimeoutError(f'{name+suffix}: {info["stop_reason"]}')
                if name == 'compact' and not suffix:
                    report['training_constraint_max_abs'] = float((model.predict(state, inputs, inputs, labels)
                                                                   -labels+state[-1]).abs().max())
                del state
                save_json(args.out/'report.json', report)
                print(json.dumps(dict(event='probe_done', model=name+suffix, seconds=info['seconds'],
                                      mse=info['final_training_mse'])), flush=True)
            move(model, 'cpu')
            if name in ('iid', 'small'):
                del model
        assert report['runs']['small']['total_model_words'] <= expected
        reference = arrays['dense'].astype(float)
        for name in ('iid', 'compact', 'small'):
            error = arrays[name].astype(float)-reference
            curve = np.sqrt(np.mean(error**2, axis=1))
            report['comparisons'][name] = dict(max_time_rms=float(curve.max()), endpoint_rms=float(curve[-1]),
                mean_time_rms=float(np.trapz(curve, arrays['times'])/args.horizon),
                max_time_pointwise=float(abs(error).max()))
        variability = report['comparisons']['iid']['max_time_rms']
        if variability <= 1e-12:
            raise ArithmeticError('Degenerate dense-versus-dense benchmark')
        refinement = sum(trajectory_rms(arrays[name].astype(float), arrays[name+'_coarse'].astype(float))
                         ['max_time_rms'] for name in ('dense', 'compact'))
        report.update(refinement_sum=refinement, numerical_threshold=.1*variability,
            numerical_gate_pass=bool(refinement < .1*variability),
            all_fitted=all(v['final_training_mse'] < .01 for v in report['runs'].values()),
            complete=True, scored_inputs_used_for_setup=False,
            retained_scope='current model arrays including all fixed metrics/inverses; data and workspaces separate')
        for value in report['comparisons'].values():
            value['ratio_to_dense_pair'] = value['max_time_rms']/variability
        report['accuracy_pass'] = report['comparisons']['compact']['ratio_to_dense_pair'] <= 3
        print(json.dumps({k: report[k] for k in ('storage_reduction', 'comparisons', 'all_fitted',
                                                'numerical_gate_pass', 'accuracy_pass')}), flush=True)
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        np.savez_compressed(args.out/'trajectories.npz', **arrays)
        save_json(args.out/'report.json', report)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'validate':
        validation_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'plot-validation':
        validation_plot_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'euler-fit':
        euler_fit_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'euler-summary':
        euler_summary_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'panel-fit':
        finite_panel_fit_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'panel-summary':
        finite_panel_summary_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'compression-probe':
        compression_probe_main(sys.argv[2:])
    else:
        main()
