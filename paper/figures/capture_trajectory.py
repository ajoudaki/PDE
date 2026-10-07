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
    predictions, losses, current, steps, query_seconds, training_seconds = [], [], 0., 0, 0., 0.
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
        query_started = time.monotonic()
        prediction = model.predict(state, queries, inputs, labels)
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
        seconds=elapsed, query_seconds=query_seconds, training_seconds=training_seconds, steps=steps,
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


def validation_data(dimension, samples, queries, seed, device, task='toy', partition='test'):
    rng = np.random.default_rng(seed)
    if task == 'digits':
        from sklearn.datasets import load_digits
        from sklearn.model_selection import train_test_split
        from sklearn.decomposition import PCA
        data, target = load_digits(return_X_y=True)
        keep = (target == 3) | (target == 8)
        data, target = data[keep], np.where(target[keep] == 3, -1., 1.)
        indices, heldout = train_test_split(np.arange(len(target)), train_size=samples,
                                           stratify=target, random_state=seed)
        tuning, testing = train_test_split(heldout, train_size=64, stratify=target[heldout],
                                           random_state=seed+1)
        heldout = tuning if partition == 'pilot' else testing
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


class Harmonic:
    """Two-hidden-layer autonomous metric/deficit optimizer from the appendix.

    Source data and the dense reference are used only inside ``__init__``.
    ``source_rank`` truncates each base coefficient family before applying its
    initialized mixer image, preserving the retained forward/reverse pairing.
    Empirical source fitting/truncation has no asserted all-time certificate.
    """

    def __init__(self, dense, inputs, labels, source_coefficients=None, budget=None,
                 source_rank=8, rank_tolerance=1e-9, selector='bss'):
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
        if selector != 'bss':
            raise ValueError('Only the appendix BSS selector is implemented')
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
                    max_coefficient_error=float(error.abs().max()))
            constant = torch.ones(n, 1, dtype=a0.dtype, device=a0.device)
            mandatory1 = torch.cat((constant, a0, h10), dim=1)
            mandatory2 = torch.cat((constant, h20, matrix0@h10), dim=1)
            optional1 = torch.cat((retained['h1'], retained['delta1'], matrix0.T@retained['delta2']), dim=1)
            optional2 = torch.cat((retained['h2'], retained['delta2'], matrix0@retained['h1']), dim=1)
            basis1, mandatory_error1 = _harmonic_source_basis(mandatory1, optional1)
            basis2, mandatory_error2 = _harmonic_source_basis(mandatory2, optional2)
            selection1 = _harmonic_bss_metric(basis1)
            selection2 = _harmonic_bss_metric(basis2)
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
            self.diagnostics = dict(branch='empirical_spectral_setup_bss_runtime', certified_source_setup=False,
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
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--refine', action='store_true')
    parser.add_argument('--small-width', type=int, default=0)
    parser.add_argument('--lora-rank', type=int, default=0)
    parser.add_argument('--lora-step', type=float, default=.01)
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
    args = parser.parse_args(argv)
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
                                                   args.data_seed, args.device, args.task, partition)
    times = sorted(set(t for t in [0., .5, 1., 2., 5., 10., 20., args.horizon] if t <= args.horizon))
    report.update(times=times, query_partition=partition, training_rank=int(torch.linalg.matrix_rank(inputs)),
                  label_rms=float(rms(labels)), query_count=len(queries),
                  train_inputs_sha256=array_sha(inputs.cpu().numpy()),
                  test_inputs_sha256=array_sha(queries.cpu().numpy()))
    arrays = dict(times=times, train_inputs=inputs.cpu().numpy(), train_labels=labels.cpu().numpy(),
                  query_inputs=queries.cpu().numpy(), query_labels=truth.cpu().numpy())
    models = [('dense', Dense(args.width, args.dimension, args.seed, args.device)),
              ('dense_iid', Dense(args.width, args.dimension, args.seed+10000, args.device))]
    if args.small_width:
        models.append(('small_dense', Dense(args.small_width, args.dimension, args.seed+20000, args.device)))
    if args.lora_rank:
        models.append(('lora', LoRA(models[0][1], args.lora_rank, args.seed+30000)))
    try:
        if args.harmonic_budget:
            coefficients, setup_info = collect_harmonic_sources(models[0][1], inputs, labels, args)
            synchronize(inputs.device)
            assembly_started = time.monotonic()
            harmonic = Harmonic(models[0][1], inputs, labels, coefficients,
                                args.harmonic_budget, source_rank=args.source_rank)
            synchronize(inputs.device)
            setup_info['assembly_seconds'] = time.monotonic()-assembly_started
            setup_info['diagnostics'] = harmonic.diagnostics
            report['harmonic_setup'] = setup_info
            del coefficients
            models.append(('harmonic', harmonic))
            budget = sum(v.numel() for v in harmonic.initial_state) + harmonic.fixed_scalars
            matched_width = int((math.sqrt((args.dimension+1)**2+4*budget)-args.dimension-1)/2)
            models.append(('matched_dense', Dense(matched_width, args.dimension, args.seed+20000, args.device)))
            report['matched_budget'] = dict(target_total_scalars=budget, dense_width=matched_width,
                                           dense_total_scalars=matched_width**2+matched_width*(args.dimension+1))
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
                    _, fine, fine_info = integrate(model, inputs, labels, queries, times,
                                                   model_step/2, args.per_run_seconds)
                    arrays[name+'_fine'] = fine
                    info['refinement'] = trajectory_rms(prediction, fine)
                    info['refinement_seconds'] = fine_info['seconds']
                    arrays[name+'_coarse'] = prediction
                    arrays[name] = fine
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
                own_sensitivity = 0. if name == 'frozen_ntk' else report['runs'][name].get('refinement', {}).get('max_time_rms')
                combined = sensitivity + own_sensitivity if sensitivity is not None and own_sensitivity is not None else None
                comparison['combined_numerical_sensitivity'] = combined
                comparison['numerically_resolved'] = bool(combined is not None and combined <= .1*denominator)
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
                comparison['dense_reference_numerically_resolved'] = bool(args.refine and
                    report['runs']['dense']['refinement']['max_time_rms'] < .1*scale)
                comparison['comparability_pass'] = bool(comparison['dense_reference_numerically_resolved'] and
                    log_info['replay_passed'] and scale > 1e-14 and comparison['ratio_to_dense_pair'] <= 3.)
                log_info['dense_variability_same_queries'] = variability
                log_info['comparison'] = comparison
                report['comparisons']['logarithmic'] = comparison
            print(json.dumps(dict(event='logarithmic_probe', **log_info)), flush=True)
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
        # Acquire all needed moments in one pass when evaluating a passive query.
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
        answers = []
        for vector in queries:
            value, scratch, count = program.query(vector)
            answers.append(value)
            for key, words in scratch.items():
                query_scratch[key] = max(query_scratch[key], words)
            passes += count
            query_calls += 1
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
    assert max(posterior_error, replay_error, regeneration_error, query_error, euler_error) < 1e-10
    assert repeated_query == selected_query
    return dict(gaussian_both_orientation_posterior_max_abs=posterior_error,
                scalar_replay_max_abs=replay_error, row_regeneration_max_abs=regeneration_error,
                source_vs_selected_passive_query_max_abs=query_error,
                fixed_matrix_euler_autograd_max_abs=euler_error,
                repeated_query_identical=True, selected_rank=len(rows), virtual_width=128)


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


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'validate':
        validation_main(sys.argv[2:])
    else:
        main()
