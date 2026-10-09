#!/usr/bin/env python3
"""Capture trajectories and validate response compression in one executable.

``unified-case`` compares self-contained Legendre, geometric Harmonic and
rank-safe finite-panel Logarithmic models, with moving-state-matched small
dense/low-rank and exact Euler frozen-NTK controls. ``unified-check`` runs tiny
algebra oracles; ``compression-sweep --protocol unified`` executes a frozen
manifest on two GPUs; ``unified-plot`` renders its figures. Practical spectral
source setup uses complete offline rollouts, not an initialization-only method.

``run --config compression_experiment.json`` uses the compact grouped config
and generated dotted CLI overrides. Each seed rebuilds its coupled models;
``plot`` only reads saved trajectories. With no arguments, ``run`` uses defaults.

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


DEEP_ACTIVATIONS = ('tanh', 'atan', 'gelu', 'silu', 'softplus', 'erf')


def _deep_activation(z, activation, with_derivative=True):
    """Evaluate a smooth activation and, optionally, its analytic derivative.

    GELU uses the exact Gaussian CDF, not its tanh approximation. Softplus
    uses logaddexp, so its stable evaluation has no linear threshold branch.
    """
    if activation == 'tanh':
        h = z.tanh()
        gate = 1-h.square() if with_derivative else None
    elif activation == 'atan':
        h = z.atan()
        gate = 1/(1+z.square()) if with_derivative else None
    elif activation == 'gelu':
        cdf = .5*(1+torch.erf(z/math.sqrt(2)))
        h = z*cdf
        gate = cdf+z*torch.exp(-.5*z.square())/math.sqrt(2*math.pi) if with_derivative else None
    elif activation == 'silu':
        sigmoid = z.sigmoid()
        h = z*sigmoid
        gate = sigmoid*(1+z*(1-sigmoid)) if with_derivative else None
    elif activation == 'softplus':
        h = torch.logaddexp(z, z.new_zeros(()))
        gate = z.sigmoid() if with_derivative else None
    elif activation == 'erf':
        h = z.erf()
        gate = (2/math.sqrt(math.pi))*torch.exp(-z.square()) if with_derivative else None
    else:
        raise ValueError(f'DeepDense activation must be one of {DEEP_ACTIVATIONS}')
    return h, gate


class DeepDense:
    """Fixed hidden depth L; state [A, w, B2, ..., BL], f=w^T hL/n.

    A has shape (n,d), each hidden mixer is (n,n), and w is (n,).
    The squared-loss flow has mobilities (n,n,1,...,1) in this state order.
    """

    def __init__(self, width, dimension, depth, activation, seed, device):
        if width < 1 or dimension < 1 or depth < 1 or int(depth) != depth:
            raise ValueError('DeepDense needs positive width, dimension and integer hidden depth')
        if activation not in DEEP_ACTIVATIONS:
            raise ValueError(f'DeepDense activation must be one of {DEEP_ACTIVATIONS}')
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
            h, gate = _deep_activation(z, self.activation)
            hs.append(h)
            gates.append(gate)
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

    def euler_step(self, state, inputs, labels, step):
        """Same dense Euler update without allocating n-by-n gradient tensors.

        All forward/backward fields and small derivatives use the old state.
        The integrator dispatches here only for exact DeepDense, never for a
        subclass with different RHS dynamics. GEMM fusion can change rounding.
        """
        hs, gates = self.fields(state, inputs)
        deltas = self.backward(state, hs, gates)
        n, scale = len(state[1]), 2/len(labels)
        deficit = labels-state[1]@hs[-1]/n
        first = scale*(deltas[0]*deficit)@inputs
        readout = scale*hs[-1]@deficit
        state[0].add_(first, alpha=step)
        state[1].add_(readout, alpha=step)
        for layer in range(1, self.depth):
            state[layer+1].addmm_(scale/n*(deltas[layer]*deficit), hs[layer-1].T,
                                  beta=1., alpha=step)

    def predict(self, state, queries, inputs=None, labels=None):
        return state[1]@self.fields(state, queries)[0][-1]/len(state[1])


@torch.no_grad()
def _panel_span_dense(dense, inputs, queries):
    """Couple the dense model exactly on the declared panel, up to rank tolerance.

    V spans the rows of [inputs; queries]. Set A_span=A@V and x_span=x@V;
    keep all hidden weights/readout unchanged and never renormalize x_span.
    First-layer velocities lie in the training span, so this coordinate change
    preserves dense Euler/GF panel predictions. It does not certify a subsequent
    empirical coordinate selection or predictions outside the declared span.
    """
    panel = torch.cat((inputs, queries)).to(dtype=torch.float64)
    if panel.ndim != 2 or not len(panel) or not bool(torch.isfinite(panel).all()):
        raise ValueError('Panel-span setup requires a nonempty finite input panel')
    _, singular, right = torch.linalg.svd(panel, full_matrices=False)
    tolerance = max(panel.shape)*torch.finfo(panel.dtype).eps*float(singular[0])
    rank = int((singular > tolerance).sum())
    basis = right[:rank].T.contiguous()
    reduced = DeepDense.__new__(DeepDense)
    reduced.depth, reduced.activation, reduced.fixed_scalars = dense.depth, dense.activation, 0
    reduced.initial_state = [dense.initial_state[0]@basis.to(dense.initial_state[0])]
    reduced.initial_state += [value.clone() for value in dense.initial_state[1:]]
    residual = panel-panel@basis@basis.T
    info = dict(original_dimension=panel.shape[1], panel_size=len(panel), rank=rank,
        rank_tolerance=tolerance, construction_dtype=str(panel.dtype),
        input_reconstruction_max_abs=float(residual.abs().max()),
        orthogonality_max_abs=(float((basis.T@basis-torch.eye(rank, device=panel.device,
                                    dtype=panel.dtype)).abs().max()) if rank else 0.),
        basis_fixed_scalars=basis.numel(),
        guarantee='coupled dense Euler/GF on training and declared-query span, up to numerical rank tolerance',
        unseen_query_rule='evaluate x@V without renormalization; outside-span accuracy is not guaranteed',
        storage='moving first layer uses width*rank; fixed dimension*rank basis is included in total storage')
    return reduced, basis, info


class PanelSpanModel:
    """Raw-input interface for a core already constructed in panel coordinates."""

    def __init__(self, core, input_basis, diagnostics):
        self.core = core
        self.input_basis = input_basis.to(core.initial_state[0])
        self.initial_state = core.initial_state
        self.depth, self.activation = core.depth, core.activation
        self.fixed_scalars = core.fixed_scalars+self.input_basis.numel()
        if hasattr(core, 'readout_floor'):
            self.readout_floor = core.readout_floor
        self.diagnostics = dict(getattr(core, 'diagnostics', {}), panel_span=dict(diagnostics),
                                fixed_scalars=self.fixed_scalars)

    def fields(self, state, inputs):
        return self.core.fields(state, inputs@self.input_basis)

    def rhs(self, state, inputs, labels):
        return self.core.rhs(state, inputs@self.input_basis, labels)

    def predict(self, state, queries, inputs, labels):
        return self.core.predict(state, queries@self.input_basis, inputs@self.input_basis, labels)

    def _readout(self, state, inputs, labels):
        return self.core._readout(state, inputs@self.input_basis, labels)

    def prepare_query(self, state, inputs, labels):
        training = inputs@self.input_basis
        prepared = (self.core.prepare_query(state, training, labels)
                    if hasattr(self.core, 'prepare_query') else
                    lambda queries: self.core.predict(state, queries, training, labels))
        return lambda queries: prepared(queries@self.input_basis)


@torch.no_grad()
def panel_span_small_checks():
    """Dense coupling oracle: redundant panels, rank deficiency, and zero span."""
    dtype, device = torch.float64, torch.device('cpu')
    generator = torch.Generator().manual_seed(231)
    results = {}
    for dimension, panel_count, expected_rank in ((3, 11, 3), (9, 12, 4), (7, 13, 0)):
        frame = torch.linalg.qr(torch.randn(dimension, max(1, expected_rank),
                                           dtype=dtype, generator=generator)).Q[:, :expected_rank]
        panel = torch.randn(panel_count, expected_rank, dtype=dtype, generator=generator)@frame.T
        panel[-2:] = panel[:2]  # Explicit duplicate points; the panel has p>d.
        inputs, queries = panel[:5], panel[5:]
        labels = torch.randn(len(inputs), dtype=dtype, generator=generator)/5
        dense = DeepDense(19, dimension, 3, 'tanh', 17, device)
        dense.initial_state[1].copy_(torch.randn(19, dtype=dtype, generator=generator)/5)
        reduced, basis, info = _panel_span_dense(dense, inputs, queries)
        assert info['rank'] == expected_rank, info
        model = PanelSpanModel(reduced, basis, info)
        original = [value.clone() for value in dense.initial_state]
        projected = [value.clone() for value in model.initial_state]
        prediction_error = velocity_error = state_error = 0.
        maximum = lambda value: float(value.abs().max()) if value.numel() else 0.
        for _ in range(6):
            prediction_error = max(prediction_error, maximum(
                dense.predict(original, panel)-model.predict(projected, panel, inputs, labels)))
            full_velocity, reduced_velocity = dense.rhs(original, inputs, labels), model.rhs(projected, inputs, labels)
            velocity_error = max(velocity_error, maximum(full_velocity[0]@basis-reduced_velocity[0]),
                maximum(full_velocity[0]-reduced_velocity[0]@basis.T),
                *(maximum(a-b) for a, b in zip(full_velocity[1:], reduced_velocity[1:])))
            for state, velocity in ((original, full_velocity), (projected, reduced_velocity)):
                for value, derivative in zip(state, velocity):
                    value.add_(derivative, alpha=.007)
            state_error = max(state_error, maximum(original[0]@basis-projected[0]),
                             *(maximum(a-b) for a, b in zip(original[1:], projected[1:])))
        assert model.fixed_scalars == dimension*expected_rank
        assert max(prediction_error, velocity_error, state_error) < 1e-11
        _experiment_move(model, device, torch.float32)
        assert model.core.initial_state is model.initial_state and model.input_basis.dtype == torch.float32
        torch.testing.assert_close(model.prepare_query(model.initial_state, inputs.float(), labels.float())(panel.float()),
            model.predict(model.initial_state, panel.float(), inputs.float(), labels.float()))
        results[f'd{dimension}_p{panel_count}_rank{expected_rank}'] = dict(
            prediction_max_abs=prediction_error, velocity_max_abs=velocity_error,
            state_max_abs=state_error, basis_fixed_scalars=model.fixed_scalars)
    return results


class DeepHarmonic(DeepDense):
    """Autonomous fixed-depth metric/deficit optimizer with offline sources.

    Source columns are pre-truncated h/delta lists. Only their immediate
    initialized forward/reverse images are added; no recursive image closure.
    Construction uses float64, four coordinate candidates by default, and condition cap 16.
    Sources and the dense model are discarded; all retained metrics are counted.
    """

    @torch.no_grad()
    def __init__(self, dense, inputs, labels, source_coefficients, budget, selection_seed=501,
                 readout_floor=None, selection_trials=4, condition_limit=16., selection_strategy='uniform'):
        if not isinstance(selection_trials, int) or isinstance(selection_trials, bool) or selection_trials < 1:
            raise ValueError('Coordinate-selection trials must be a positive integer')
        if not math.isfinite(condition_limit) or condition_limit < 1:
            raise ValueError('Coordinate-selection condition limit must be finite and at least one')
        self.depth, self.activation = dense.depth, dense.activation
        runtime_dtype = dense.initial_state[0].dtype
        original = [value.to(dtype=torch.float64) for value in dense.initial_state]
        a0, w0 = original[:2]
        n, device, budget = len(w0), a0.device, int(budget)
        training, targets = inputs.to(dtype=torch.float64), labels.to(dtype=torch.float64)
        if bool(w0.ne(0).any()):
            raise ValueError('DeepHarmonic initialization requires zero dense readout')
        if readout_floor is not None:
            if not math.isfinite(readout_floor) or readout_floor <= 0:
                raise ValueError('Readout floor must be finite and strictly positive')
            self.readout_floor = float(readout_floor)
        if budget < 1:
            raise ValueError('DeepHarmonic needs a positive width budget')
        if readout_floor is None and budget < len(labels):
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
            bases, selected, selections, mandatory_errors, truncations = [], [], [], [], []
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
                truncation = dict(full_rank=basis.shape[1], truncated=False)
                if readout_floor is not None and basis.shape[1] > budget:
                    # Constant-preserving low-budget source ordering. No training
                    # column is mandatory here; truncation is empirical, not BSS.
                    basis, error, omitted = _rank_safe_source_basis(
                        torch.cat(mandatory, 1), torch.cat(optional, 1), max(1, budget//4))
                    truncation.update(truncated=True, retained_rank=basis.shape[1],
                                      normalized_source_relative_error=omitted)
                selection = _panel_coordinate_metric(basis, budget, selection_seed+layer,
                    trials=selection_trials, strategy=selection_strategy)
                if selection[-1]['embedding_max'] > condition_limit:
                    raise ArithmeticError(f'DeepHarmonic layer {layer+1} source condition '
                        f'{selection[-1]["embedding_max"]:.9g} exceeds {condition_limit:g} '
                        f'after {selection[-1]["selection_trials"]} {selection_strategy} candidates')
                bases.append(basis)
                selected.append(basis[selection[0]])
                selections.append(selection)
                mandatory_errors.append(error)
                truncations.append(truncation)
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
                source_truncations=truncations,
                initialized_feature_errors=[maximum(h-h0[layer][indices[layer]]) for layer, h in enumerate(hs)],
                initialized_gram_error=maximum(hs[-1].T@self.metrics[-1]@hs[-1]-h0[-1].T@h0[-1]/n),
                paired_forward_action_errors=forward_errors, paired_reverse_action_errors=reverse_errors)
        # Offline geometry is assembled in double precision; deployment preserves
        # the reference state dtype and keeps no dense/source construction arrays.
        self.initial_state = [value.to(dtype=runtime_dtype) for value in self.initial_state]
        self.metrics = [value.to(dtype=runtime_dtype) for value in self.metrics]
        self.metric_inverses = [value.to(dtype=runtime_dtype) for value in self.metric_inverses]
        self.fixed_scalars = sum(value.numel() for value in self.metrics+self.metric_inverses)
        self.fixed_scalars += int(readout_floor is not None)
        _, _, _, gram = self._readout(self.initial_state, inputs, labels)
        eigenvalues = torch.linalg.eigvalsh(gram)
        self.diagnostics.update(requested_budget=budget, activation=self.activation, depth=self.depth,
            certified_source_setup=False, source_assembly_dtype='torch.float64', runtime_dtype=str(runtime_dtype),
            condition_limit=float(condition_limit),
            selection_strategy=selection_strategy,
            initial_feature_gram_min=float(eigenvalues[0]),
            initial_feature_gram_condition=(float(eigenvalues[-1]/eigenvalues[0])
                                           if float(eigenvalues[0]) > 0 else None),
            readout_floor=readout_floor,
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
        floor = getattr(self, 'readout_floor', None)
        if floor is not None:
            # Form the singular Gram in double precision: in float32, numerical
            # null directions times 1/tau can swamp the retained correction.
            normalized = hs[-1].double()/math.sqrt(len(labels))
            metric = self.metrics[-1].double()
            gram = normalized.T@(metric@normalized)
            gram = (gram+gram.T)/2
            correction = ((labels.double()-state[-1].double())/math.sqrt(len(labels))
                          -normalized.T@(metric@state[1].double()))
            readout = state[1].double()+normalized@_rank_safe_spectral_solve(gram, correction, floor)
            return readout.to(state[1].dtype), hs, gates, gram
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
            h = _deep_activation(h, activation, with_derivative=False)[0]
            for mixer in mixers:
                h = mixer@h
                h = _deep_activation(h, activation, with_derivative=False)[0]
            return coefficient@h

        return predict


@torch.no_grad()
def rank_safe_small_checks():
    """Bounded algebra/regression checks; no fitted or scored experiment data."""
    device, dtype = torch.device('cpu'), torch.float64
    generator = torch.Generator().manual_seed(91)
    inputs = torch.randn(7, 3, generator=generator, dtype=dtype)
    inputs /= inputs.norm(dim=1, keepdim=True)
    labels = torch.randn(7, generator=generator, dtype=dtype)/5
    dense = DeepDense(40, 3, 2, 'tanh', 19, device)
    legacy = DeepHarmonic(dense, inputs, labels, None, budget=40)
    safe = DeepHarmonic(dense, inputs, labels, None, budget=40, readout_floor=1e-10)
    state = [v+.001*torch.randn(v.shape, generator=generator, dtype=dtype)
             for v in legacy.initial_state]
    maximum = lambda v: float(v.abs().max())
    errors = dict(legacy_readout=maximum(legacy._readout(state, inputs, labels)[0]
                                         -safe._readout(state, inputs, labels)[0]),
                  legacy_rhs=max(maximum(a-b) for a, b in zip(
                      legacy.rhs(state, inputs, labels), safe.rhs(state, inputs, labels))))
    sources = {name: [torch.randn(40, 3, generator=generator, dtype=dtype) for _ in range(2)]
               for name in ('h', 'delta')}
    for budget in (1, 4):
        model = DeepHarmonic(dense, inputs, labels, sources, budget, readout_floor=.0001)
        state = [v+.001*torch.randn(v.shape, generator=generator, dtype=dtype)
                 for v in model.initial_state]
        readout, hs, _, gram = model._readout(state, inputs, labels)
        normalized = hs[-1]/math.sqrt(len(labels))
        b = ((labels-state[-1])/math.sqrt(len(labels))
             -normalized.T@(model.metrics[-1]@state[1]))
        expected = -state[-1]-math.sqrt(len(labels))*(b-gram@_rank_safe_spectral_solve(gram, b, .0001))
        residual = model.predict(state, inputs, inputs, labels)-labels
        errors[f'residual_identity_q{budget}'] = maximum(residual-expected)
        velocity = model.rhs(state, inputs, labels)
        norm = ((velocity[0]*(model.metrics[0]@velocity[0])).sum()
                +velocity[1]@(model.metrics[-1]@velocity[1])
                +(velocity[2].T@model.metrics[1]@velocity[2]*model.metric_inverses[0].T).sum())
        errors[f'energy_identity_q{budget}'] = float(abs(norm+2/len(labels)*(state[-1]@velocity[-1])))
        restored = DeepHarmonic.__new__(DeepHarmonic)
        for key in ('depth', 'activation', 'readout_floor', 'fixed_scalars'):
            setattr(restored, key, getattr(model, key))
        for key in ('metrics', 'metric_inverses'):
            setattr(restored, key, [v.clone() for v in getattr(model, key)])
        restored.initial_state = [v.clone() for v in state]
        errors[f'restart_q{budget}'] = maximum(restored.prepare_query(state, inputs, labels)(inputs)
                                              -model.predict(state, inputs, inputs, labels))
        assert model.fixed_scalars == 3*budget**2+1
        assert all(r <= max(1, budget//4) for r in model.diagnostics['source_ranks'])
        assert all(abs(float(metric.sum())-1) < 1e-10 for metric in model.metrics)
        assert all(bool(torch.isfinite(v).all()) for v in velocity)
        json.dumps(model.diagnostics, allow_nan=False)
    zeros = torch.zeros(7, 7, dtype=dtype)
    errors['zero_gram'] = maximum(_rank_safe_spectral_solve(zeros, labels, .01)-labels/.01)
    assert max(errors.values()) < 1e-9, errors
    return errors


def deep_rollout_small_checks():
    """Tiny CPU activation, gradient, source-pair, retention and restart checks."""
    dtype, device = torch.float64, torch.device('cpu')
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]], dtype=dtype)
    labels = torch.tensor([.2, -.1, .3], dtype=dtype)
    generator = torch.Generator().manual_seed(17)
    activation_references = dict(tanh=torch.tanh, atan=torch.atan,
        gelu=lambda z: torch.nn.functional.gelu(z, approximate='none'),
        silu=torch.nn.functional.silu, softplus=torch.nn.functional.softplus, erf=torch.erf)
    results = []
    for depth in (2, 3):
        for activation in DEEP_ACTIVATIONS:
            probes = torch.linspace(-12., 12., 97, dtype=dtype, requires_grad=True)
            values, derivatives = _deep_activation(probes, activation)
            reference = activation_references[activation](probes)
            reference_derivative, = torch.autograd.grad(reference.sum(), probes)
            maximum = lambda value: float(value.detach().abs().max())
            value_error = maximum(values-reference)
            derivative_error = maximum(derivatives-reference_derivative)
            assert torch.equal(values, _deep_activation(probes, activation, with_derivative=False)[0])
            tails = torch.tensor([-1000., -100., -40., 40., 100., 1000.], dtype=dtype)
            assert all(bool(torch.isfinite(value).all()) for value in _deep_activation(tails, activation))
            dense = DeepDense(32, 2, depth, activation, 3, device)
            dense.initial_state = [value.to(dtype=dtype) for value in dense.initial_state]
            arbitrary = [(value+.03*torch.randn(value.shape, generator=generator, dtype=dtype))
                         .requires_grad_() for value in dense.initial_state]
            prediction = dense.predict(arbitrary, inputs)
            gradients = torch.autograd.grad((prediction-labels).square().mean(), arbitrary)
            velocities = dense.rhs(arbitrary, inputs, labels)
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
            errors = dict(activation_value_max_abs=value_error, activation_derivative_max_abs=derivative_error,
                          gradient_max_abs=gradient_error, full_retention_rhs_max_abs=rhs_error,
                          full_retention_deficit_max_abs=deficit_error, source_setup_max_abs=setup_error,
                          restart_max_abs=restart_error, training_constraint_max_abs=constraint_error)
            assert max(errors.values()) < 1e-10, (depth, activation, errors)
            results.append(dict(depth=depth, activation=activation, **errors))
    return results


class LegendreCompression:
    """Lifted order-q Legendre history model for the canonical L=2 tanh flow.

    State is [A, w, bar_delta, bar_h, tau, h1, h2, rho], with moments
    shaped (q,n,m). Here A=W^(1), w=W^(3), and inputs already include
    1/sqrt(d). The unit prefix has bar_h[0]=h1(0), all other moments zero,
    and tau(0)=1. The exact same lifted equations as the archived solver
    are used, with tau=s+1 and the redundant coordinates C_j=tau omitted.

    Moving storage is n(d+1)+2qnm+2nm+2; fixed storage is n^2+2q.
    The fixed dense mixer is charged in full. No learned n-by-n matrix is
    formed by training or querying. Shared training data are not retained.
    """

    def __init__(self, dense, inputs, labels, order):
        if (isinstance(order, bool) or int(order) != order or order < 1
                or len(dense.initial_state) != 3
                or getattr(dense, 'depth', 2) != 2
                or getattr(dense, 'activation', 'tanh') != 'tanh'):
            raise ValueError('LegendreCompression needs positive integer order and L=2 tanh')
        a, w, matrix = dense.initial_state
        n, d = a.shape
        if (inputs.ndim != 2 or inputs.shape[1] != d or len(inputs) < 1
                or labels.shape != (len(inputs),) or matrix.shape != (n, n)
                or w.shape != (n,) or bool(w.ne(0).any())):
            raise ValueError('LegendreCompression needs matching data and a zero dense readout')
        if any(value.dtype != a.dtype or value.device != a.device
               or not bool(torch.isfinite(value).all()) for value in (a, w, matrix, inputs, labels)):
            raise ValueError('LegendreCompression requires finite, same-device, same-dtype arrays')
        self.order, self.samples, self.width = int(order), len(inputs), n
        self.matrix = matrix.detach().clone()
        self.degrees = torch.arange(self.order, dtype=a.dtype, device=a.device)
        self.weights = 2*self.degrees+1
        h1 = (a@inputs.T).tanh()
        h2 = (self.matrix@h1).tanh()
        bar_delta = a.new_zeros((self.order, n, self.samples))
        bar_h = torch.zeros_like(bar_delta)
        bar_h[0] = h1
        self.initial_state = [a.detach().clone(), w.detach().clone(), bar_delta, bar_h,
                              a.new_ones(()), h1, h2, labels.square().mean().sqrt()]
        self.fixed_scalars = self.matrix.numel()+self.degrees.numel()+self.weights.numel()

    @staticmethod
    def _columns(value):
        return value.permute(1, 0, 2).reshape(value.shape[1], -1)

    def _factors(self, state):
        return ((-2/(self.samples*self.width))*self._columns(self.weights[:, None, None]*state[2]),
                self._columns(state[3]/state[4]))

    def _apply_hidden(self, factors, values, transpose=False):
        left, right = factors
        if transpose:
            return self.matrix.T@values+right@(left.T@values)
        return self.matrix@values+left@(right.T@values)

    def _transport(self, moments, endpoint_source, rho, tau):
        weighted = self.weights[:, None, None]*moments
        lower = torch.cat((torch.zeros_like(weighted[:1]), weighted[:-1].cumsum(0)), 0)
        return endpoint_source[None]-(rho/tau)*(self.degrees[:, None, None]*moments+lower)

    @torch.no_grad()
    def rhs(self, state, inputs, labels):
        a, w, bar_delta, bar_h, tau, h1, h2, rho = state
        if bool((tau < 1) | (rho < 0) | ~torch.isfinite(tau+rho)):
            raise FloatingPointError('Legendre clock/rho left its domain; reduce integration step')
        if bool(rho == 0):
            return [torch.zeros_like(value) for value in state]
        factors = self._factors(state)
        residual = w@h2/self.width-labels
        delta2 = w[:, None]*(1-h2.square())
        delta1 = self._apply_hidden(factors, delta2, transpose=True)*(1-h1.square())
        a_dot = (-2/self.samples)*(delta1*residual)@inputs
        w_dot = (-2/self.samples)*(h2@residual)
        delta_dot = self._transport(bar_delta, delta2*residual, rho, tau)
        h_dot = self._transport(bar_h, rho*h1, rho, tau)
        h1_dot = (1-h1.square())*(a_dot@inputs.T)
        left, right = factors
        left_dot = (-2/(self.samples*self.width))*self._columns(self.weights[:, None, None]*delta_dot)
        right_dot = self._columns((h_dot-bar_h*rho/tau)/tau)
        z2_dot = (self._apply_hidden(factors, h1_dot)
                  +left_dot@(right.T@h1)+left@(right_dot.T@h1))
        h2_dot = (1-h2.square())*z2_dot
        f_dot = (w_dot@h2+w@h2_dot)/self.width
        rho_dot = (residual*f_dot).mean()/rho
        return [a_dot, w_dot, delta_dot, h_dot, rho.clone(), h1_dot, h2_dot, rho_dot]

    def prepare_query(self, state, inputs=None, labels=None):
        factors = self._factors(state)
        def query(queries):
            h1 = (state[0]@queries.T).tanh()
            h2 = self._apply_hidden(factors, h1).tanh()
            return state[1]@h2/self.width
        return query

    def predict(self, state, queries, inputs=None, labels=None):
        return self.prepare_query(state)(queries)

    @torch.no_grad()
    def lift_diagnostics(self, state, inputs, labels):
        h1 = (state[0]@inputs.T).tanh()
        h2 = self._apply_hidden(self._factors(state), h1).tanh()
        residual = state[1]@h2/self.width-labels
        lifted_residual = state[1]@state[6]/self.width-labels
        return dict(h1_max=float((state[5]-h1).abs().max()),
                    h2_max=float((state[6]-h2).abs().max()),
                    rho_abs=float((state[7]-lifted_residual.square().mean().sqrt()).abs()),
                    rho_recomputed_abs=float((state[7]-residual.square().mean().sqrt()).abs()),
                    tau=float(state[4]), rho=float(state[7]))


@torch.no_grad()
def legendre_smoke_test(device='cpu'):
    """Small algebra checks, independent of the legacy ZIP and dense rollouts."""
    errors = {}
    for dimension, order in ((1, 1), (3, 3)):
        dense = DeepDense(7, dimension, 2, 'tanh', 913+order, device)
        generator = torch.Generator(device=device).manual_seed(51)
        inputs = torch.randn(4, dimension, generator=generator, device=device, dtype=torch.float64)
        inputs = inputs/inputs.norm(dim=1, keepdim=True)
        labels = torch.linspace(-.3, .4, 4, device=device, dtype=torch.float64)
        model = LegendreCompression(dense, inputs, labels, order)
        state = [value.clone() for value in model.initial_state]
        assert sum(value.numel() for value in state) == 7*(dimension+1)+2*order*7*4+2*7*4+2
        assert model.fixed_scalars == 49+2*order
        assert not bool(model.predict(state, inputs).ne(0).any())
        velocity = model.rhs(state, inputs, labels)
        reference = dense.rhs(dense.initial_state, inputs, labels)
        initial_error = max(float((velocity[i]-reference[i]).abs().max()) for i in (0, 1))
        # Nonzero moments/readout exercise both product-rule terms and transpose action.
        for index in (1, 2, 3):
            state[index] += .02*torch.randn(state[index].shape, generator=generator,
                                            device=device, dtype=torch.float64)
        state[4] += .4
        left, right = model._factors(state)
        matrix = model.matrix+left@right.T
        state[5] = (state[0]@inputs.T).tanh()
        state[6] = (matrix@state[5]).tanh()
        state[7] = (state[1]@state[6]/7-labels).square().mean().sqrt()
        action_error = max(float((model._apply_hidden((left, right), state[5], transpose=transpose)
                                 -(matrix.T if transpose else matrix)@state[5]).abs().max())
                           for transpose in (False, True))
        velocity = model.rhs(state, inputs, labels)
        matrix_dot = torch.zeros_like(matrix)
        for j in range(order):
            matrix_dot += (-2*(2*j+1)/(4*7*state[4]))*(
                velocity[2][j]@state[3][j].T+state[2][j]@velocity[3][j].T
                -state[2][j]@state[3][j].T*velocity[4]/state[4])
        expected_h2_dot = (1-state[6].square())*(matrix@velocity[5]+matrix_dot@state[5])
        derivative_error = float((velocity[6]-expected_h2_dot).abs().max())
        step = 1e-5
        plus = model.predict([value+step*dot for value, dot in zip(state, velocity)], inputs)
        minus = model.predict([value-step*dot for value, dot in zip(state, velocity)], inputs)
        expected_f_dot = (velocity[1]@state[6]+state[1]@velocity[6])/7
        tangency_error = float(((plus-minus)/(2*step)-expected_f_dot).abs().max())
        zero = LegendreCompression(dense, inputs, torch.zeros_like(labels), order)
        assert all(not bool(value.ne(0).any()) for value in zero.rhs(zero.initial_state, inputs,
                                                                  torch.zeros_like(labels)))
        errors[f'd{dimension}_q{order}'] = dict(initial=initial_error, action=action_error,
                                             derivative=derivative_error, tangency=tangency_error)
        assert max(initial_error, action_error, derivative_error) < 1e-12
        assert tangency_error < 1e-9
    return errors


class LoRA:
    """Explicit low-rank increment; its frozen dense mixer is NOT free storage."""

    def __init__(self, dense, rank, seed, multiplier=1.):
        a, w, matrix = dense.initial_state
        n = len(w)
        if not 1 <= rank <= n:
            raise ValueError("LoRA rank must be in [1,n]")
        generator = torch.Generator(device=a.device).manual_seed(seed)
        right = torch.linalg.qr(torch.randn(n, rank, generator=generator,
                                            device=a.device, dtype=a.dtype), mode='reduced')[0]
        self.matrix = matrix.clone()
        self.initial_state = [a.clone(), w.clone(), torch.zeros_like(right), right]
        self.mobility = multiplier * n / rank
        self.fixed_scalars = matrix.numel()

    def _fields(self, state, inputs):
        a, w, left, right = state
        h1 = (a @ inputs.T).tanh()
        projected = right.T@h1
        h2 = (self.matrix@h1+left@projected).tanh()
        return h1, h2, w@h2/len(w), projected

    def fields(self, state, inputs):
        return self._fields(state, inputs)[:3]

    def rhs(self, state, inputs, labels):
        a, w, left, right = state
        h1, h2, prediction, projected = self._fields(state, inputs)
        residual = prediction - labels
        delta2 = w[:, None] * (1 - h2.square())
        delta1 = (self.matrix.T@delta2+right@(left.T@delta2))*(1-h1.square())
        force = (-2 / len(labels)) * (delta2 * residual)
        # Reuse the forward projection; no dense adapter is formed.
        return [(-2 / len(labels)) * (delta1 * residual) @ inputs,
                (-2 / len(labels)) * (h2 @ residual),
                self.mobility/len(w)*force@projected.T,
                self.mobility/len(w)*h1@(force.T@left)]

    def predict(self, state, queries, inputs, labels):
        return self.fields(state, queries)[2]


class BudgetLoRA:
    """Two-block low-rank adaptation with a hard moving-state budget.

    Both dense Gaussian matrices are frozen at the reference initialization.
    State order is [readout, first_left, first_right, hidden_left, hidden_right].
    Zero left factors preserve the exact initial dense network. Orthonormal
    right factors and mobilities (n*d/r1, n/r2) match the expected initial
    induced first/hidden block velocities, not their later trajectories.
    """

    def __init__(self, dense, budget, seed):
        if (len(dense.initial_state) != 3 or getattr(dense, 'depth', 2) != 2
                or getattr(dense, 'activation', 'tanh') != 'tanh'):
            raise ValueError('BudgetLoRA requires a two-hidden-layer tanh reference')
        if isinstance(budget, bool) or not isinstance(budget, (int, np.integer)):
            raise ValueError('BudgetLoRA budget must be an integer')
        first, readout, matrix = dense.initial_state
        n, d = first.shape
        if readout.shape != (n,) or matrix.shape != (n, n):
            raise ValueError('BudgetLoRA requires equal hidden widths')
        budget = int(budget)
        if budget < 4*n+d:
            raise ValueError(f'BudgetLoRA needs at least {4*n+d} moving scalars; got {budget}')

        def size(rank):
            return n+min(rank, n, d)*(n+d)+2*n*min(rank, n)

        lower, upper = 1, n
        while lower < upper:
            middle = (lower+upper+1)//2
            if size(middle) <= budget:
                lower = middle
            else:
                upper = middle-1
        self.rank_first, self.rank_hidden = min(lower, n, d), lower
        generator = torch.Generator(device=first.device).manual_seed(seed)
        first_right = torch.linalg.qr(torch.randn(d, self.rank_first,
            generator=generator, device=first.device, dtype=first.dtype), mode='reduced')[0]
        hidden_right = torch.linalg.qr(torch.randn(n, self.rank_hidden,
            generator=generator, device=first.device, dtype=first.dtype), mode='reduced')[0]
        self.first, self.matrix = first.detach().clone(), matrix.detach().clone()
        self.initial_state = [readout.detach().clone(), first.new_zeros((n, self.rank_first)),
                              first_right, torch.zeros_like(hidden_right), hidden_right]
        self.first_mobility = n*d/self.rank_first
        self.hidden_mobility = n/self.rank_hidden
        self.readout_mobility = n
        self.moving_scalars = sum(value.numel() for value in self.initial_state)
        self.fixed_scalars = self.first.numel()+self.matrix.numel()
        self.diagnostics = dict(target_moving_scalars=budget,
            actual_moving_scalars=self.moving_scalars, unused_moving_scalars=budget-self.moving_scalars,
            rank_first=self.rank_first, rank_hidden=self.rank_hidden,
            rank_policy='largest common rank, with first rank capped by input dimension',
            first_factor_mobility=self.first_mobility, hidden_factor_mobility=self.hidden_mobility,
            readout_mobility=n, fixed_dense_scalars=self.fixed_scalars,
            normalization='expected induced block mobility at zero adapters; no fitted multiplier')

    def _fields(self, state, inputs):
        readout, first_left, first_right, left, right = state
        first_projected = first_right.T@inputs.T
        h1 = (self.first@inputs.T+first_left@first_projected).tanh()
        projected = right.T@h1
        h2 = (self.matrix@h1+left@projected).tanh()
        return h1, h2, readout@h2/len(readout), first_projected, projected

    def fields(self, state, inputs):
        return self._fields(state, inputs)[:3]

    def rhs(self, state, inputs, labels):
        readout, first_left, first_right, left, right = state
        h1, h2, prediction, first_projected, projected = self._fields(state, inputs)
        residual = prediction-labels
        delta2 = readout[:, None]*(1-h2.square())
        delta1 = (self.matrix.T@delta2+right@(left.T@delta2))*(1-h1.square())
        force1, force2 = (-2/len(labels))*(delta1*residual), (-2/len(labels))*(delta2*residual)
        first_scale, hidden_scale = self.first_mobility/len(readout), self.hidden_mobility/len(readout)
        # Projections are per-call temporaries, not additional retained state.
        return [(-2/len(labels))*h2@residual,
                first_scale*force1@first_projected.T,
                first_scale*inputs.T@(force1.T@first_left),
                hidden_scale*force2@projected.T,
                hidden_scale*h1@(force2.T@left)]

    def predict(self, state, queries, inputs=None, labels=None):
        return self.fields(state, queries)[2]


def feedback_control_checks():
    """Tiny deterministic oracles for factorized LoRA and coordinate selection.

    Full-rank trainable factors are not a dense-gradient parametrization.
    A separate fixed-orthonormal-right additive adapter is used only here as
    an exact full-rank Euler oracle, never substituted for the plotted baseline.
    """
    torch.set_num_threads(1)
    dtype, device = torch.float64, torch.device('cpu')
    generator = torch.Generator().manual_seed(811)
    n, d, m = 12, 3, 5
    inputs = torch.randn(m, d, generator=generator, dtype=dtype)
    inputs /= inputs.norm(dim=1, keepdim=True)
    labels = torch.randn(m, generator=generator, dtype=dtype)
    dense = DeepDense(n, d, 2, 'tanh', 19, device)
    budget = n+d*(n+d)+2*n*n
    model = BudgetLoRA(dense, budget, 41)
    maximum = lambda value: float(value.detach().abs().max())
    state = [(value+.15*torch.randn(value.shape, generator=generator, dtype=dtype))
             .requires_grad_() for value in model.initial_state]
    gradients = torch.autograd.grad((model.predict(state, inputs)-labels).square().mean(), state)
    velocity = model.rhs(state, inputs, labels)
    mobilities = [n, model.first_mobility, model.first_mobility,
                  model.hidden_mobility, model.hidden_mobility]
    errors = dict(autograd=max(maximum(v+mu*g) for v, mu, g in zip(velocity, mobilities, gradients)))
    reconstructed = [model.first+state[1]@state[2].T, state[0], model.matrix+state[3]@state[4].T]
    dense_velocity = dense.rhs(reconstructed, inputs, labels)
    for name, offset, dense_index, mu, canonical_mu in (
            ('first', 1, 0, model.first_mobility, n),
            ('hidden', 3, 2, model.hidden_mobility, 1)):
        left, right = state[offset:offset+2]
        induced = velocity[offset]@right.T+left@velocity[offset+1].T
        gradient = -dense_velocity[dense_index]/canonical_mu
        expected = -mu*(gradient@(right@right.T)+(left@left.T)@gradient)
        errors[name+'_induced_metric'] = maximum(induced-expected)
    with torch.no_grad():
        # Nonzero readout makes the initial block-velocity comparison nonvacuous.
        probe = [v.clone() for v in model.initial_state]
        probe[0] = torch.randn(n, generator=generator, dtype=dtype)
        reference_probe = [dense.initial_state[0], probe[0], dense.initial_state[2]]
        v, dv = model.rhs(probe, inputs, labels), dense.rhs(reference_probe, inputs, labels)
        errors['full_rank_initial_first_velocity'] = maximum(v[1]@probe[2].T-dv[0])
        errors['full_rank_initial_hidden_velocity'] = maximum(v[3]@probe[4].T-dv[2])
        reference = [v.clone() for v in dense.initial_state]
        factored = [v.clone() for v in model.initial_state]
        fixed = [v.clone() for v in model.initial_state]
        errors['fixed_right_full_rank_euler'] = 0.
        step, steps = .04, 32
        for _ in range(steps):
            reference_rhs = dense.rhs(reference, inputs, labels)
            fixed_dense = [model.first+fixed[1]@fixed[2].T, fixed[0], model.matrix+fixed[3]@fixed[4].T]
            fixed_rhs = dense.rhs(fixed_dense, inputs, labels)
            fixed = [fixed[0]+step*fixed_rhs[1], fixed[1]+step*fixed_rhs[0]@fixed[2],
                     fixed[2], fixed[3]+step*fixed_rhs[2]@fixed[4], fixed[4]]
            factored = [v+step*dv for v, dv in zip(factored, model.rhs(factored, inputs, labels))]
            reference = [v+step*dv for v, dv in zip(reference, reference_rhs)]
            fixed_dense = [model.first+fixed[1]@fixed[2].T, fixed[0], model.matrix+fixed[3]@fixed[4].T]
            errors['fixed_right_full_rank_euler'] = max(errors['fixed_right_full_rank_euler'],
                max(maximum(a-b) for a, b in zip(fixed_dense, reference)))
        divergence = maximum(model.predict(factored, inputs)-dense.predict(reference, inputs))
        basis = math.sqrt(80)*torch.linalg.qr(torch.randn(80, 8, generator=generator, dtype=dtype))[0]
        selection = _panel_coordinate_metric(basis, 24, 7, strategy='qr_leverage')
        repeat = _panel_coordinate_metric(basis, 24, 99, strategy='qr_leverage')
        assert torch.equal(selection[0], repeat[0])
        assert len(selection[0].unique()) == 24
        errors['selector_source_isometry'] = selection[-1]['source_isometry_error']
        errors['selector_metric_inverse'] = selection[-1]['metric_inverse_error']
    assert max(errors.values()) < 1e-10, errors
    assert divergence > 1e-8, divergence
    return dict(errors=errors, full_rank_trainable_factor_prediction_difference=divergence,
        oracle_steps=steps, oracle_step=step, rank_first=model.rank_first, rank_hidden=model.rank_hidden,
        selector=selection[-1], baseline_equations_changed=False,
        conclusion='Factorized LoRA passes its gradient oracle; fixed right full-rank adapters reproduce dense Euler; trainable factors do not.')


def feedback_conditioning_main(argv=None):
    """Reproduce three saved failures, then try one fixed replacement selector."""
    parser = argparse.ArgumentParser(description=feedback_conditioning_main.__doc__)
    parser.add_argument('--config', required=True)
    args = parser.parse_args(argv)
    config_path = Path(args.config)
    config = json.loads(config_path.read_text())
    out = Path(config['output'])
    out.mkdir(parents=True, exist_ok=False)
    source_bytes = Path(__file__).read_bytes()
    (out/'source.py').write_bytes(source_bytes)
    save_json(out/'config.json', config)
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(config['device'])
    started = time.monotonic()
    report = dict(source_sha256=sha(source_bytes), config_sha256=sha(config_path.read_bytes()),
        environment=dict(python=sys.version, torch=torch.__version__, numpy=np.__version__,
            device=str(device), hardware=torch.cuda.get_device_name(device), threads=1, tf32=False),
        control_checks=feedback_control_checks(), cases={}, scope='Single-selector finite Euler diagnostics, not theory certificates')
    save_json(out/'report.json', report)
    for request in config['cases']:
        if time.monotonic()-started > config['queue_seconds']:
            report['cases'][request['case']] = dict(status='inconclusive', reason='Queue cap reached')
            continue
        case = request['case']
        case_out = out/case
        case_out.mkdir()
        original_root = ROOT/'data/generated/paper_appendix_pilots_20261009'/case
        old_config = json.loads((original_root/'config.json').read_text())
        old_path = original_root/'seed_901/attempt_001'
        old = json.loads((old_path/'report.json').read_text())
        archive_bytes = (old_path/'trajectories.npz').read_bytes()
        assert sha(archive_bytes) == old['trajectories_sha256']
        archive = np.load(old_path/'trajectories.npz', allow_pickle=False)
        inputs, labels, queries = [torch.as_tensor(archive[key], device=device, dtype=torch.float64)
                                  for key in ('train_inputs', 'train_labels', 'query_inputs')]
        n, d = old_config['model']['width'], inputs.shape[1]
        training = old_config['training']
        setup = old_config['methods']['non_oblivious']['setup']
        entry = dict(original_report=str(old_path/'report.json'), original_errors=old['errors'],
            original_trajectories_sha256=sha(archive_bytes), requested_width=request['width'],
            source_rank=request['source_rank'], status='inconclusive')
        report['cases'][case] = entry
        save_json(out/'report.json', report)
        try:
            dense = DeepDense(n, d, old_config['model']['depth'], old_config['model']['activation'], 901, device)
            hashes = [array_sha(v.cpu().numpy()) for v in dense.initial_state]
            assert hashes == old['reference_initial_state_sha256']
            ranks = tuple(old['sources']['logarithmic']['nested_ranks'])
            with torch.no_grad():
                sources, source_info = cubic_rollout_sources(dense, inputs, labels, queries,
                    training['horizon'], seed=old['seeds']['logarithmic_source'], ranks=ranks,
                    partitions=('new',), step=setup['rollout_step'], time_degree=setup['time_degree'],
                    rollout_dtype=setup['rollout_dtype'], coefficient_dtype=setup['coefficient_dtype'],
                    seconds=config['seconds_per_fit'])
                source = sources['new'][request['source_rank']]
                entry['source'] = source_info
                entry['source_hashes'] = {key: [array_sha(v.cpu().numpy()) for v in values]
                                           for key, values in source.items()}
                old_source = old['sources']['logarithmic']
                assert source_info['partitions']['new']['boundaries'] == old_source['partitions']['new']['boundaries']
                residual_error = float(np.max(np.abs(np.asarray(source_info['precursor_residual_rms'])
                                                     -old_source['precursor_residual_rms'])))
                entry['source_precursor_reproduction_max_abs'] = residual_error
                assert residual_error < 1e-6
                h0 = dense.fields(dense.initial_state, inputs)[0]
                constant = inputs.new_ones((n, 1))
                arrays = {f'{key}_{layer}': v.cpu().numpy() for key, values in source.items()
                          for layer, v in enumerate(values)}
                entry['selections'] = []
                for layer in range(dense.depth):
                    mandatory = ([constant, h0[layer], dense.initial_state[layer+1]@h0[layer-1]]
                                 if layer else [constant, dense.initial_state[0], h0[layer]])
                    optional = [source['h'][layer], source['delta'][layer]]
                    if layer:
                        optional.append(dense.initial_state[layer+1]@source['h'][layer-1])
                    if layer+1 < dense.depth:
                        optional.append(dense.initial_state[layer+2].T@source['delta'][layer+1])
                    basis, mandatory_error = _harmonic_source_basis(torch.cat(mandatory, 1), torch.cat(optional, 1))
                    assert basis.shape[1] <= request['width'], 'No source truncation permitted'
                    arrays[f'basis_{layer}'] = basis.cpu().numpy()
                    layer_result = dict(layer=layer+1, source_rank=basis.shape[1], mandatory_error=mandatory_error)
                    for strategy in ('uniform', 'qr_leverage'):
                        selection = _panel_coordinate_metric(basis, request['width'],
                            old['seeds']['logarithmic_selector']+layer, trials=setup['selection_trials'], strategy=strategy)
                        layer_result[strategy] = selection[-1]
                        arrays[f'{strategy}_indices_{layer}'] = selection[0].cpu().numpy()
                    entry['selections'].append(layer_result)
                original_failure = entry['selections'][request['failed_layer']-1]['uniform']['embedding_max']
                entry['original_failure_reproduction_absolute_error'] = abs(original_failure-request['original_condition'])
                assert abs(original_failure-request['original_condition']) < 1e-3
                np.savez_compressed(case_out/'sources_and_bases.npz', **arrays)
                entry['sources_and_bases_sha256'] = sha((case_out/'sources_and_bases.npz').read_bytes())
                save_json(out/'report.json', report)
                if any(row['qr_leverage']['embedding_max'] > 16 for row in entry['selections']):
                    entry['reason'] = 'Replacement selector exceeds unchanged condition cap 16; no fit run'
                    continue
                gap = float(torch.linalg.eigvalsh(h0[-1].T@h0[-1]/(n*len(labels)))[0])
                model = DeepHarmonic(dense, inputs, labels, source, request['width'],
                    selection_seed=old['seeds']['logarithmic_selector'], readout_floor=min(1e-4, gap/8),
                    selection_trials=setup['selection_trials'], condition_limit=16., selection_strategy='qr_leverage')
                assert not any(row['truncated'] for row in model.diagnostics['source_truncations'])
                entry['model'] = model.diagnostics
                _experiment_move(model, device, torch.float32)
                state, predictions, run = integrate_euler(model, inputs.float(), labels.float(),
                    torch.cat((inputs, queries)).float(), training['step'], config['seconds_per_fit'],
                    horizon=training['horizon'], observation_every=training['record_every'])
                entry['run'] = run
                np.savez_compressed(case_out/'trajectory.npz', prediction=predictions, times=run['times'],
                    reference=archive['reference'], dense_pair=archive[f'dense_{n}'])
                entry['trajectory_sha256'] = sha((case_out/'trajectory.npz').read_bytes())
                if not run['complete']:
                    entry['reason'] = run['stop_reason']
                    continue
                assert np.array_equal(np.asarray(run['times']), archive['times_reference'])
                reference = archive['reference'][:, len(labels):].astype(float)
                error = np.sqrt(np.mean((predictions[:, len(labels):].astype(float)-reference)**2, axis=1))
                baseline = np.sqrt(np.mean((archive[f'dense_{n}'][:, len(labels):].astype(float)-reference)**2, axis=1))
                entry['metrics'] = dict(endpoint_rms=float(error[-1]), worst_recorded_rms=float(error.max()),
                    endpoint_ratio=float(error[-1]/baseline[-1]), worst_recorded_ratio=float(error.max()/baseline.max()),
                    threshold_factor=1., passed=bool(error[-1] <= baseline[-1] and error.max() <= baseline.max()))
                entry['status'] = 'pass' if entry['metrics']['passed'] else 'fail'
                del state, model, sources, source, arrays
        except (ValueError, RuntimeError, ArithmeticError, TimeoutError, AssertionError) as error:
            entry['reason'] = f'{type(error).__name__}: {error}'
        finally:
            entry['queue_elapsed_seconds'] = time.monotonic()-started
            save_json(out/'report.json', report)
            print(json.dumps(dict(case=case, status=entry['status'], metrics=entry.get('metrics'),
                reason=entry.get('reason'), conditions=[row['qr_leverage']['embedding_max']
                    for row in entry.get('selections', [])])), flush=True)
    report['seconds'] = time.monotonic()-started
    save_json(out/'report.json', report)
    return 0


def feedback_conditioning_followup_main(argv=None):
    """Two frozen follow-ups using cached sources, never another dense rollout."""
    import ast
    parser = argparse.ArgumentParser(description=feedback_conditioning_followup_main.__doc__)
    parser.add_argument('--config', required=True)
    args = parser.parse_args(argv)
    config_path = Path(args.config)
    config = json.loads(config_path.read_text())
    cached = Path(config['cached'])
    previous = json.loads((cached/'report.json').read_text())
    # Check that rebuilding cached geometry executes precisely the same code.
    current_bytes, old_bytes = Path(__file__).read_bytes(), (cached/'source.py').read_bytes()
    def geometry_code(data):
        tree = ast.parse(data)
        return {node.name: ast.dump(node, include_attributes=False) for node in tree.body
                if isinstance(node, (ast.ClassDef, ast.FunctionDef))
                if node.name in ('DeepHarmonic', '_panel_coordinate_metric', '_harmonic_source_basis')}
    assert geometry_code(current_bytes) == geometry_code(old_bytes)
    out = Path(config['output'])
    out.mkdir(parents=True, exist_ok=False)
    (out/'source.py').write_bytes(current_bytes)
    save_json(out/'config.json', config)
    device = torch.device(config['device'])
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    started = time.monotonic()
    report = dict(source_sha256=sha(current_bytes), config_sha256=sha(config_path.read_bytes()),
        cached_report_sha256=sha((cached/'report.json').read_bytes()), source_rollouts=0,
        compiled_geometry_code_unchanged=True, cases={})
    for request in config['cases']:
        case = request['case']
        entry = dict(request=request, status='inconclusive')
        report['cases'][case] = entry
        try:
            remaining = config['queue_seconds']-(time.monotonic()-started)
            if remaining <= 0:
                raise TimeoutError('Follow-up queue cap reached')
            case_out = out/case
            case_out.mkdir()
            old_path = ROOT/'data/generated/paper_appendix_pilots_20261009'/case/'seed_901/attempt_001'
            old = json.loads((old_path/'report.json').read_text())
            assert sha((old_path/'trajectories.npz').read_bytes()) == old['trajectories_sha256']
            data = np.load(old_path/'trajectories.npz', allow_pickle=False)
            source_path = cached/case/'sources_and_bases.npz'
            assert sha(source_path.read_bytes()) == previous['cases'][case]['sources_and_bases_sha256']
            saved_source = np.load(source_path, allow_pickle=False)
            inputs, labels, queries = [torch.as_tensor(data[key], device=device, dtype=torch.float64)
                                      for key in ('train_inputs', 'train_labels', 'query_inputs')]
            dense = DeepDense(2048, inputs.shape[1], 2, 'silu' if case == 'architecture_silu' else 'tanh', 901, device)
            assert [array_sha(v.cpu().numpy()) for v in dense.initial_state] == old['reference_initial_state_sha256']
            source = {key: [torch.as_tensor(saved_source[f'{key}_{layer}'], device=device)
                           for layer in range(2)] for key in ('h', 'delta')}
            assert {key: [array_sha(v.cpu().numpy()) for v in values] for key, values in source.items()} == previous['cases'][case]['source_hashes']
            with torch.no_grad():
                h0 = dense.fields(dense.initial_state, inputs)[0][-1]
                gap = float(torch.linalg.eigvalsh(h0.T@h0/(2048*len(labels)))[0])
                model = DeepHarmonic(dense, inputs, labels, source, request['width'],
                    selection_seed=old['seeds']['logarithmic_selector'], readout_floor=min(1e-4, gap/8),
                    selection_trials=64, condition_limit=16., selection_strategy='qr_leverage')
                assert not any(v['truncated'] for v in model.diagnostics['source_truncations'])
                entry['model'] = model.diagnostics
                if request.get('half_step_check'):
                    assert model.diagnostics == previous['cases'][case]['model'], 'Compiled geometry changed'
                    entry['compiled_geometry_matches_coarse'] = True
                _experiment_move(model, device, torch.float32)
                entry['compiled_state_sha256'] = [array_sha(v.cpu().numpy()) for v in model.initial_state]
                entry['compiled_metrics_sha256'] = [array_sha(v.cpu().numpy())
                    for v in model.metrics+model.metric_inverses]
                remaining = config['queue_seconds']-(time.monotonic()-started)
                state, predictions, run = integrate_euler(model, inputs.float(), labels.float(),
                    torch.cat((inputs, queries)).float(), request['step'], remaining,
                    horizon=32., observation_every=round(.5/request['step']))
                entry['run'] = run
                np.savez_compressed(case_out/'trajectory.npz', prediction=predictions, times=run['times'])
                entry['trajectory_sha256'] = sha((case_out/'trajectory.npz').read_bytes())
                if not run['complete']:
                    raise TimeoutError(run['stop_reason'])
                assert np.array_equal(np.asarray(run['times']), data['times_reference'])
                reference = data['reference'][:, len(labels):].astype(float)
                baseline = np.sqrt(np.mean((data['dense_2048'][:, len(labels):].astype(float)-reference)**2, axis=1))
                def ratios(curve):
                    return dict(endpoint_rms=float(curve[-1]), worst_recorded_rms=float(curve.max()),
                        endpoint_ratio=float(curve[-1]/baseline[-1]), worst_recorded_ratio=float(curve.max()/baseline.max()))
                error = np.sqrt(np.mean((predictions[:, len(labels):].astype(float)-reference)**2, axis=1))
                entry['versus_saved_dense'] = ratios(error)
                if request.get('half_step_check'):
                    coarse_path = cached/case/'trajectory.npz'
                    assert sha(coarse_path.read_bytes()) == previous['cases'][case]['trajectory_sha256']
                    coarse = np.load(coarse_path, allow_pickle=False)['prediction'][:, len(labels):].astype(float)
                    difference = np.sqrt(np.mean((predictions[:, len(labels):].astype(float)-coarse)**2, axis=1))
                    entry['coarse_fine_compact'] = ratios(difference)
                    entry['coarse_fine_compact']['threshold_factor'] = .1
                    passed = difference[-1] <= .1*baseline[-1] and difference.max() <= .1*baseline.max()
                    entry['comparison_scope'] = 'Fine compact versus saved coarse dense is mixed-step diagnostic only'
                else:
                    passed = error[-1] <= baseline[-1] and error.max() <= baseline.max()
                    entry['comparison_scope'] = 'Same-step Euler comparison, factor-one criterion'
                entry['status'] = 'pass' if passed else 'fail'
                del state, model, source
        except (ValueError, RuntimeError, ArithmeticError, TimeoutError, AssertionError) as error:
            entry['reason'] = f'{type(error).__name__}: {error}'
        finally:
            entry['queue_elapsed_seconds'] = time.monotonic()-started
            save_json(out/'report.json', report)
            print(json.dumps(dict(case=case, status=entry['status'], reason=entry.get('reason'),
                comparison=entry.get('versus_saved_dense'), coarse_fine=entry.get('coarse_fine_compact'))), flush=True)
    report['seconds'] = time.monotonic()-started
    save_json(out/'report.json', report)
    return 0


class FrozenNTK:
    """Exact initial-kernel Euler dynamics on an explicitly retained finite panel.

    With zero reference readout, only the readout contributes to the initial
    all-block NTK. The moving state is a dual vector of length m. Fixed model
    scalars count K and K_query; retained input/query coordinates are counted
    separately as data_scalars. No dense weights or arbitrary-query decoder
    are retained, and prediction rejects an unregistered query panel.
    """

    def __init__(self, dense, inputs, queries):
        if (len(dense.initial_state) != 3 or getattr(dense, 'depth', 2) != 2
                or getattr(dense, 'activation', 'tanh') != 'tanh'):
            raise ValueError('FrozenNTK requires a two-hidden-layer tanh reference')
        if bool(dense.initial_state[1].ne(0).any()):
            raise ValueError('FrozenNTK readout-only construction requires zero initial readout')
        with torch.no_grad():
            features = dense_fields(dense.initial_state, inputs)[1]
            query_features = dense_fields(dense.initial_state, queries)[1]
            self.kernel = features.T@features/features.shape[0]
            self.cross = query_features.T@features/features.shape[0]
        self.train_inputs = inputs.detach().clone()
        self.query_inputs = queries.detach().clone()
        self.initial_state = [inputs.new_zeros(len(inputs))]
        self.moving_scalars = len(inputs)
        self.fixed_scalars = self.kernel.numel()+self.cross.numel()
        self.data_scalars = self.train_inputs.numel()+self.query_inputs.numel()
        self.diagnostics = dict(moving_scalars=self.moving_scalars, fixed_scalars=self.fixed_scalars,
            data_scalars=self.data_scalars, query_scope='registered training and scored panels only',
            dynamics='dual initial-NTK ODE integrated by the common Euler driver')

    def rhs(self, state, inputs, labels):
        return [(2/len(labels))*(labels-self.kernel@state[0])]

    def predict(self, state, queries, inputs=None, labels=None):
        if queries.shape == self.train_inputs.shape and torch.equal(queries, self.train_inputs):
            return self.kernel@state[0]
        if queries.shape == self.query_inputs.shape and torch.equal(queries, self.query_inputs):
            return self.cross@state[0]
        m = len(self.train_inputs)
        if (queries.shape == (m+len(self.query_inputs), self.train_inputs.shape[1])
                and torch.equal(queries[:m], self.train_inputs)
                and torch.equal(queries[m:], self.query_inputs)):
            return torch.cat((self.kernel@state[0], self.cross@state[0]))
        raise ValueError('FrozenNTK only predicts on its registered training and scored panels')


def unified_baseline_checks():
    """Tiny CPU oracles for budget, factor gradients and exact kernel Euler."""
    dense = DeepDense(5, 3, 2, 'tanh', 891, 'cpu')
    generator = torch.Generator().manual_seed(892)
    inputs = torch.randn(4, 3, generator=generator, dtype=torch.float64)
    queries = torch.randn(6, 3, generator=generator, dtype=torch.float64)
    inputs, queries = inputs/inputs.norm(dim=1, keepdim=True), queries/queries.norm(dim=1, keepdim=True)
    labels = torch.tensor([-.7, .2, .8, -.3], dtype=torch.float64)
    model = BudgetLoRA(dense, 41, 893)
    initial_error = max(float((a-b).abs().max()) for a, b in
        zip(model.fields(model.initial_state, inputs), dense_fields(dense.initial_state, inputs)))
    with torch.enable_grad():
        state = [(value+.1*torch.randn(value.shape, generator=generator, dtype=value.dtype))
                 .detach().requires_grad_(True) for value in model.initial_state]
        loss = (model.predict(state, inputs)-labels).square().mean()
        gradients = torch.autograd.grad(loss, state)
        velocity = model.rhs(state, inputs, labels)
        mobilities = [model.readout_mobility, model.first_mobility, model.first_mobility,
                      model.hidden_mobility, model.hidden_mobility]
        gradient_error = max(float((dot.detach()+mobility*gradient.detach()).abs().max())
                             for dot, mobility, gradient in zip(velocity, mobilities, gradients))
    with torch.no_grad():
        full = BudgetLoRA(dense, 79, 894)
        full_state = [value.clone() for value in full.initial_state]
        full_state[0] = torch.linspace(-.4, .5, 5, dtype=torch.float64)
        velocity = full.rhs(full_state, inputs, labels)
        reference = dense.rhs([full.first, full_state[0], full.matrix], inputs, labels)
        induced_first = velocity[1]@full_state[2].T+full_state[1]@velocity[2].T
        induced_hidden = velocity[3]@full_state[4].T+full_state[3]@velocity[4].T
        mobility_error = max(float((induced_first-reference[0]).abs().max()),
                             float((velocity[0]-reference[1]).abs().max()),
                             float((induced_hidden-reference[2]).abs().max()))
        budgets_checked = 0
        for budget in (23, 40, 41, 78, 79, 100):
            matched = BudgetLoRA(dense, budget, 895)
            assert matched.moving_scalars == sum(value.numel() for value in matched.initial_state)
            assert matched.moving_scalars <= budget
            assert matched.fixed_scalars == 40
            if matched.rank_hidden < 5:
                next_rank = matched.rank_hidden+1
                assert 5+min(next_rank, 3)*8+10*next_rank > budget
            budgets_checked += 1
        try:
            BudgetLoRA(dense, 22, 896)
        except ValueError:
            pass
        else:
            raise AssertionError('An infeasible LoRA budget was accepted')
        frozen = FrozenNTK(dense, inputs, queries)
        state = [value.clone() for value in frozen.initial_state]
        readout = dense.initial_state[1].clone()
        h = dense_fields(dense.initial_state, inputs)[1]
        hq = dense_fields(dense.initial_state, queries)[1]
        kernel_error = 0.
        for step in (.07, .07, .023):
            dual_velocity = frozen.rhs(state, inputs, labels)[0]
            readout -= (2*step/len(labels))*h@(readout@h/len(readout)-labels)
            state[0] += step*dual_velocity
            kernel_error = max(kernel_error,
                float((frozen.predict(state, inputs)-readout@h/len(readout)).abs().max()),
                float((frozen.predict(state, queries.clone())-readout@hq/len(readout)).abs().max()))
        assert frozen.moving_scalars == 4 and frozen.fixed_scalars == 40 and frozen.data_scalars == 30
        try:
            frozen.predict(state, queries+.01)
        except ValueError:
            pass
        else:
            raise AssertionError('An unregistered NTK query panel was accepted')
    errors = dict(initial_fields_max_abs=initial_error, factor_gradient_max_abs=gradient_error,
                  full_rank_mobility_max_abs=mobility_error, kernel_euler_max_abs=kernel_error)
    assert max(errors.values()) < 1e-11, errors
    return dict(**errors, budget_cases=budgets_checked+1)


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
    predictions, losses, finite_checks = [], [], []
    current, steps, query_seconds, training_seconds, refresh_seconds = 0., 0, 0., 0., 0.
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
        finite_checks.append(torch.isfinite(prediction).all() & torch.isfinite(train).all())
        predictions.append(prediction.detach().clone())
        losses.append((train-labels).square().mean().detach())
        if observer is not None:
            observer(float(target), state)
        synchronize(device)
        if time.monotonic() - started > seconds:
            raise TimeoutError(f"{type(model).__name__} exceeded cap including query/observer at t={target}")
    # Observations stay on the simulation device; export only after the rollout.
    export_started = time.monotonic()
    host_checks = torch.stack(finite_checks).cpu().numpy()
    if not host_checks.all():
        raise FloatingPointError(f'nonfinite {type(model).__name__} at t={times[np.flatnonzero(~host_checks)[0]]}')
    host_predictions = torch.stack(predictions).cpu().numpy()
    host_losses = torch.stack(losses).cpu().tolist()
    synchronize(device)
    export_seconds = time.monotonic()-export_started
    elapsed = time.monotonic() - started
    if elapsed > seconds:
        raise TimeoutError(f'{type(model).__name__} exceeded cap including final export')
    return state, host_predictions, dict(
        seconds=elapsed, query_seconds=query_seconds, query_refresh_seconds=refresh_seconds,
        observation_storage='simulation device until final export', export_seconds=export_seconds,
        query_timing_scope='whole query batch, after readout refresh; amortized, not single-query latency',
        training_seconds=training_seconds, steps=steps,
        seconds_per_step=training_seconds/max(1, steps),
        moving_scalars=sum(v.numel() for v in state),
        fixed_scalars=int(model.fixed_scalars), losses=host_losses,
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


def _unified_harmonic_geometry(dimension, spatial_degree=5):
    """Real harmonics through the requested degree and probability-sphere quadrature."""
    if (not isinstance(spatial_degree, (int, np.integer))
            or isinstance(spatial_degree, bool) or spatial_degree < 0):
        raise ValueError('Harmonic spatial degree must be a nonnegative integer')
    if dimension == 2:
        circle_count = max(32, 2*(spatial_degree+1))
        angle = torch.arange(circle_count, dtype=torch.float64)*2*math.pi/circle_count
        nodes = torch.stack((angle.cos(), angle.sin()), 1)
        weights = torch.full((circle_count,), 1/circle_count, dtype=torch.float64)
        columns = [torch.ones_like(angle)]
        for degree in range(1, spatial_degree+1):
            columns.extend((math.sqrt(2)*(degree*angle).cos(),
                            math.sqrt(2)*(degree*angle).sin()))
    elif dimension == 3:
        polar_count, azimuth_count = spatial_degree+1, 2*(spatial_degree+1)
        polar, polar_weights = np.polynomial.legendre.leggauss(polar_count)
        z = torch.as_tensor(polar, dtype=torch.float64).repeat_interleave(azimuth_count)
        angle = (torch.arange(azimuth_count, dtype=torch.float64)*2*math.pi/azimuth_count).repeat(polar_count)
        radius = (1-z.square()).sqrt()
        nodes = torch.stack((radius*angle.cos(), radius*angle.sin(), z), 1)
        weights = (torch.as_tensor(polar_weights, dtype=torch.float64)
                   .repeat_interleave(azimuth_count)/(2*azimuth_count))
        associated = {(0, 0): torch.ones_like(z)}
        for order in range(spatial_degree+1):
            if order:
                associated[order, order] = -(2*order-1)*radius*associated[order-1, order-1]
            if order < spatial_degree:
                associated[order+1, order] = (2*order+1)*z*associated[order, order]
            for degree in range(order+2, spatial_degree+1):
                associated[degree, order] = ((2*degree-1)*z*associated[degree-1, order]
                    -(degree+order-1)*associated[degree-2, order])/(degree-order)
        columns = []
        for degree in range(spatial_degree+1):
            columns.append(math.sqrt(2*degree+1)*associated[degree, 0])
            for order in range(1, degree+1):
                normalizer = math.sqrt(2*(2*degree+1)*math.factorial(degree-order)
                                       /math.factorial(degree+order))
                value = normalizer*associated[degree, order]
                columns.extend((value*(order*angle).cos(), value*(order*angle).sin()))
    else:
        raise ValueError('Independent Harmonic geometry supports only dimensions two and three')
    return nodes, weights, torch.stack(columns, 1)


@torch.no_grad()
def unified_harmonic_sources(dense, inputs, labels, horizon, rank, seed, seconds=120., step=.125,
                             *, time_degree=8, spatial_degree=5,
                             rollout_dtype=torch.float32, coefficient_dtype=torch.float64):
    """Empirical time/sphere sources, independent of every scored input.

    A dense RK4 rollout supplies passive fields on fixed sphere nodes, using
    float32 by default. Each dyadic panel fits the requested Chebyshev degree
    on degree+1 nodes and checks the degree interleaved nodes. Spatial projection and batched
    coefficient fitting use float64; neither fit has a continuum certificate.
    Returned source lists are ready for the unchanged DeepHarmonic runtime.
    """
    if (dense.depth != 2 or dense.activation != 'tanh' or inputs.shape[1] not in (2, 3)
            or not math.isfinite(horizon) or horizon <= 0
            or not math.isfinite(step) or step <= 0
            or not math.isfinite(seconds) or seconds <= 0 or int(rank) != rank or rank < 1):
        raise ValueError('Harmonic setup needs two tanh layers, d=2/3 and positive finite orders/times')
    if (not isinstance(time_degree, (int, np.integer))
            or isinstance(time_degree, bool) or time_degree < 1):
        raise ValueError('Harmonic time degree must be a positive integer')
    if rollout_dtype in ('float32', 'float64'):
        rollout_dtype = getattr(torch, rollout_dtype)
    if rollout_dtype not in (torch.float32, torch.float64):
        raise ValueError('Harmonic rollout dtype must be float32 or float64')
    if coefficient_dtype not in (torch.float64, 'float64'):
        raise ValueError('Harmonic coefficient dtype currently supports only float64')
    started = time.monotonic()
    n, device, rank = len(dense.initial_state[1]), inputs.device, int(rank)
    nodes, weights, spatial = _unified_harmonic_geometry(inputs.shape[1], spatial_degree)
    geometry_hash = array_sha(nodes.numpy())
    geometry_weight_sum = float(weights.sum())
    spatial_gram_error = float((spatial.T@(weights[:, None]*spatial)
                              -torch.eye(spatial.shape[1], dtype=spatial.dtype)).abs().max())
    if spatial_gram_error > 1e-12:
        raise ArithmeticError('Harmonic geometry lost discrete orthonormality')
    weights, spatial = weights.to(device), spatial.to(device)
    boundaries = [0., min(1., horizon)]
    while boundaries[-1] < horizon:
        boundaries.append(min(2*boundaries[-1], horizon))
    coordinate = -np.cos(np.linspace(0, np.pi, 2*time_degree+1))
    intervals = [left+(right-left)*(coordinate+1)/2
                 for left, right in zip(boundaries[:-1], boundaries[1:])]
    times = np.unique(np.concatenate(intervals))
    panel_indices = [torch.as_tensor(np.searchsorted(times, values), device=device) for values in intervals]
    design = torch.as_tensor(np.polynomial.chebyshev.chebvander(coordinate, time_degree),
                             dtype=torch.float64, device=device)
    temporal_inverse = torch.linalg.pinv(design[::2])
    weighted_spatial = weights[:, None]*spatial
    fields = {name: [[], []] for name in ('h', 'delta')}
    teacher = DeepDense.__new__(DeepDense)
    teacher.depth, teacher.activation, teacher.fixed_scalars = 2, 'tanh', 0
    teacher.initial_state = [value.to(dtype=rollout_dtype) for value in dense.initial_state]
    source_inputs, source_labels = inputs.to(dtype=rollout_dtype), labels.to(dtype=rollout_dtype)
    source_nodes = nodes.to(device=device, dtype=rollout_dtype)

    def observe(t, state):
        hs, gates = teacher.fields(state, source_nodes)
        deltas = teacher.backward(state, hs, gates)
        for name, values in (('h', hs), ('delta', deltas)):
            for layer, value in enumerate(values):
                fields[name][layer].append(value.detach())

    _, _, source_run = integrate(teacher, source_inputs, source_labels, source_inputs[:1],
                                 times, step, seconds, observer=observe)
    del teacher, source_inputs, source_labels, source_nodes
    initial = [value.double() for value in dense.initial_state]
    h0, _ = dense.fields(initial, inputs.double())
    constant = torch.ones(n, 1, dtype=torch.float64, device=device)
    coefficients, checks = {name: [] for name in fields}, {name: [] for name in fields}
    for name in fields:
        for layer, observations in enumerate(fields[name]):
            source = torch.empty(n, len(intervals)*(time_degree+1)*spatial.shape[1],
                                 dtype=torch.float64, device=device)
            square, reference_square, maximum = [source.new_zeros(()) for _ in range(3)]
            count = 0
            batch = 512 if device.type == 'cuda' else 64
            for start in range(0, n, batch):
                if time.monotonic()-started > seconds:
                    raise TimeoutError('Harmonic source setup exceeded its complete setup budget')
                values = torch.stack([value[start:start+batch] for value in observations]).double()
                projected = values@weighted_spatial
                blocks = []
                for indices in panel_indices:
                    block = torch.einsum('kt,tbs->bks', temporal_inverse, projected[indices[::2]])
                    fitted = torch.einsum('tk,bks,ps->tbp', design[1::2], block, spatial)
                    reference = values[indices[1::2]]
                    error = fitted-reference
                    square += (error.square()*weights).sum()
                    reference_square += (reference.square()*weights).sum()
                    count += error.shape[0]*error.shape[1]
                    maximum = torch.maximum(maximum, error.abs().max())
                    blocks.append(block.flatten(1))
                source[start:start+len(values[0])] = torch.cat(blocks, 1)
            observations.clear()
            square, reference_square, maximum = torch.stack((square, reference_square, maximum)).cpu().tolist()
            # Remove only directions whose initialized images are already mandatory.
            mandatory = source[:, :0]
            if name == 'h':
                mandatory = h0[layer]
                if layer == 1:
                    mandatory = torch.cat((constant, h0[1], initial[2]@h0[0]), 1)
            elif layer == 0:
                mandatory = torch.cat((constant, initial[0], h0[0]), 1)
            if mandatory.shape[1]:
                basis, _ = _harmonic_source_basis(mandatory, source[:, :0])
                basis = basis/math.sqrt(n)
                for _ in range(2):
                    source -= basis@(basis.T@source)
            devices = [device.index] if device.type == 'cuda' else []
            with torch.random.fork_rng(devices=devices):
                torch.manual_seed(seed+layer+(100 if name == 'delta' else 0))
                left, singular, _ = torch.svd_lowrank(source, q=min(rank+8, *source.shape), niter=2)
            tolerance = max(source.shape)*torch.finfo(source.dtype).eps*singular[0]
            available = int((singular > tolerance).sum())
            retained = left[:, :min(rank, available)]
            coefficients[name].append(retained)
            checks[name].append(dict(rank=retained.shape[1], coefficient_count=source.shape[1],
                removed_mandatory_columns=mandatory.shape[1],
                space_time_holdout_rms=math.sqrt(square/count),
                space_time_holdout_relative_rms=math.sqrt(square/max(reference_square, 1e-60)),
                space_time_holdout_max_abs=maximum,
                residual_coefficient_relative_error=float((source-retained@(retained.T@source)).norm()
                                                          /source.norm().clamp_min(1e-30))))
            if time.monotonic()-started > seconds:
                raise TimeoutError('Harmonic source setup exceeded its complete setup budget')
    synchronize(device)
    return coefficients, dict(method='piecewise_chebyshev_real_spherical_harmonic_dense_rollout',
        source_contract='complete finite-horizon offline dense rollout; not a certified local-jet initializer',
        horizon=horizon, rk4_step=step, rollout_dtype=str(rollout_dtype), coefficient_dtype='torch.float64',
        chebyshev_degree=time_degree, spatial_degree=spatial_degree, spatial_modes=spatial.shape[1],
        geometry=(f'{len(nodes)}_equispaced_circle_nodes' if inputs.shape[1] == 2 else
                  f'gauss_legendre_{spatial_degree+1}_azimuth_{2*(spatial_degree+1)}'),
        geometry_count=len(nodes), geometry_sha256=geometry_hash,
        geometry_weight_sum=geometry_weight_sum, spatial_gram_max_abs=spatial_gram_error,
        source_geometry_uses_training_inputs=False, scored_inputs_used=False,
        passive_labels_used=False, source_certificate=False,
        observation_count=len(times), panel_fit_nodes=time_degree+1, panel_holdout_nodes=time_degree,
        boundaries=boundaries, fit_neuron_batch=batch, requested_rank=rank,
        source_observation_storage=str(device), coefficient_fitting_device=str(device),
        dense_rhs_calls=4*source_run['steps'], source_run_seconds=source_run['seconds'],
        seconds=time.monotonic()-started, training_count=len(inputs), diagnostics=checks,
        diagnostic_scope='weighted errors only at withheld temporal nodes on the fixed sphere grid')


@torch.no_grad()
def unified_harmonic_source_checks():
    """Tiny geometry and retained time/sphere product checks; no training."""
    results = {}
    coordinate = -np.cos(np.linspace(0, np.pi, 17))
    temporal = torch.as_tensor(np.polynomial.chebyshev.chebvander(coordinate, 8), dtype=torch.float64)
    inverse = torch.linalg.pinv(temporal[::2])
    for dimension in (2, 3):
        nodes, weights, spatial = _unified_harmonic_geometry(dimension)
        expected_modes = 11 if dimension == 2 else 36
        assert spatial.shape == (len(nodes), expected_modes)
        gram_error = float((spatial.T@(weights[:, None]*spatial)
                           -torch.eye(expected_modes, dtype=torch.float64)).abs().max())
        # Include the highest temporal degree and last spatial harmonic.
        coefficients = torch.arange(9*expected_modes, dtype=torch.float64).reshape(9, expected_modes)
        coefficients = coefficients.cos()/math.sqrt(coefficients.numel())
        values = temporal@coefficients@spatial.T
        fitted = inverse@values[::2]@(weights[:, None]*spatial)
        holdout_error = float((temporal[1::2]@fitted@spatial.T-values[1::2]).abs().max())
        coefficient_error = float((fitted-coefficients).abs().max())
        assert max(gram_error, holdout_error, coefficient_error) < 1e-12
        assert float((nodes.norm(dim=1)-1).abs().max()) < 1e-14
        assert abs(float(weights.sum())-1) < 1e-14 and bool((weights > 0).all())
        results[str(dimension)] = dict(spatial_modes=expected_modes, geometry_count=len(nodes),
            spatial_gram_max_abs=gram_error, coefficient_max_abs=coefficient_error,
            temporal_holdout_max_abs=holdout_error)
    return results


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


def _rank_safe_spectral_solve(gram, vector, floor):
    """Smooth g_tau(Q)b; equals Q^-1 b above tau, finite at rank changes."""
    values, vectors = torch.linalg.eigh(gram)
    values = values.clamp_min(0)  # Gram roundoff, not a positive rank threshold.
    coordinate = values/floor
    interior = coordinate.clamp(.5+1e-15, 1-1e-15)
    cutoff = torch.sigmoid(1/(interior-.5)-1/(1-interior))
    cutoff = torch.where(coordinate <= .5, torch.ones_like(cutoff),
                         torch.where(coordinate >= 1, torch.zeros_like(cutoff), cutoff))
    return vectors@((vectors.T@vector)/(values+floor*cutoff))


def _rank_safe_source_basis(mandatory, optional, rank):
    """Constant plus leading normalized-generator directions; setup only."""
    generators = torch.cat((mandatory, optional), 1)
    n = generators.shape[0]
    constant = torch.ones(n, 1, dtype=generators.dtype, device=generators.device)/math.sqrt(n)
    normalized = generators/generators.norm(dim=0).clamp_min(torch.finfo(generators.dtype).tiny)
    centered = normalized-constant@(constant.T@normalized)
    left, singular, _ = torch.linalg.svd(centered, full_matrices=False)
    tolerance = max(centered.shape)*torch.finfo(centered.dtype).eps*singular[0]
    retained = min(max(0, rank-1), int((singular > tolerance).sum()))
    basis = torch.cat((constant, left[:, :retained]), 1)
    # Reorthogonalize against the exactly retained constant before selection.
    basis = torch.linalg.qr(basis, mode='reduced')[0]
    error = float((mandatory-basis@(basis.T@mandatory)).abs().max())
    omitted = float((normalized-basis@(basis.T@normalized)).norm()/normalized.norm())
    return math.sqrt(n)*basis, error, omitted


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


def _panel_coordinate_metric(source_basis, budget, seed, trials=1, strategy='uniform'):
    """Coordinate selection with exact source isometry, not BSS.

    The diagonal-comparison factor is measured, not asserted to be four.
    The full positive metric and its inverse use the same correction formula
    as the BSS backend; no ridge or discarded source directions are introduced.
    """
    n, rank = source_basis.shape
    if not rank <= budget <= n:
        raise ValueError(f'Panel coordinate budget {budget} cannot embed rank {rank} in width {n}')
    if strategy not in ('uniform', 'qr_leverage'):
        raise ValueError('Coordinate strategy must be uniform or qr_leverage')
    generator = torch.Generator(device=source_basis.device).manual_seed(seed)
    best, first_four_best = None, None
    if strategy == 'qr_leverage':
        # Pivoted QR seeds a nonsingular square restriction. Greedy additions
        # maximize det(G+vv^T)/det(G)=1+v^T G^{-1}v. Sherman--Morrison updates
        # all row leverages in O(n*r+r*r) work per addition, without a ridge,
        # weighting, replacement, or source truncation. This is one deterministic
        # candidate; the final spectral gate remains unchanged.
        from scipy.linalg import qr
        pivots = qr(source_basis.detach().cpu().numpy().T, mode='economic', pivoting=True)[2]
        candidate = torch.as_tensor(pivots[:rank].copy(), device=source_basis.device, dtype=torch.long)
        rows = source_basis/math.sqrt(n)
        gram = rows[candidate].T@rows[candidate]
        inverse = torch.linalg.inv(gram)
        projected = rows@inverse
        scores = (projected*rows).sum(1)
        chosen = torch.zeros(n, dtype=torch.bool, device=source_basis.device)
        chosen[candidate] = True
        indices_list = list(candidate.unbind())
        for _ in range(budget-rank):
            index = torch.where(chosen, -torch.inf, scores).argmax()
            vector = rows[index]
            inverse_vector = inverse@vector
            cross = projected@vector
            denominator = 1+vector@inverse_vector
            inverse -= torch.outer(inverse_vector, inverse_vector)/denominator
            projected -= torch.outer(cross, inverse_vector)/denominator
            scores -= cross.square()/denominator
            chosen[index] = True
            indices_list.append(index)
        candidates = [torch.stack(indices_list)]
    else:
        candidates = (torch.randperm(n, generator=generator, device=source_basis.device)[:budget]
                      for _ in range(trials))
    for trial, candidate in enumerate(candidates):
        selected = source_basis[candidate]
        gram = selected.T @ selected / budget
        values = torch.linalg.eigvalsh((gram+gram.T)/2)
        condition = float(values[-1]/values[0]) if float(values[0]) > 0 else math.inf
        if best is None or condition < best[0]:
            best = condition, candidate, values
        if strategy == 'uniform' and trial == min(4, trials)-1:
            first_four_best = best[0]
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
    diagnostics = dict(source_rank=rank, selected_width=budget, selector=strategy+'_exact_isometry',
        seed=seed, selection_trials=trials if strategy == 'uniform' else 1, embedding_min=1.,
        first_four_best_condition=(float(first_four_best)
            if first_four_best is not None and math.isfinite(first_four_best) else None),
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
    checked at most eight updates apart when no horizon is prescribed. Fixed-
    horizon runs check loss/full-state finiteness at observations and at most
    256 updates apart; these checks cannot affect a finite fixed-horizon
    trajectory. Queries are evaluated only every ``observation_every`` updates
    and at the actual initial/terminal states.

    Return ``(state, predictions, report)``. Rows of ``predictions`` correspond
    to ``report['times']`` and ``report['observation_steps']``. A wall/step cap
    returns a partial trajectory with its actual terminal time and stop reason;
    it does not extrapolate to the requested horizon. The wall budget includes
    observations and is capped at 300 seconds. An already queued update block
    and the required terminal observation cannot be interrupted, so any overrun is
    reported. Prediction snapshots and reporting scalars stay on the simulation
    device until final export. Fixed-horizon finiteness flags are accumulated on
    device and checked before returning; RHS validity gates remain immediate.
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
    check_every = min(256 if horizon_steps is not None else 8, observation_every)
    dense_step = model.euler_step if type(model) is DeepDense else None
    synchronize(device)
    started = time.monotonic()
    baseline_bytes = torch.cuda.memory_allocated(device) if device.type == 'cuda' else None
    if device.type == 'cuda':
        torch.cuda.reset_peak_memory_stats(device)
    state = [value.detach().clone() for value in model.initial_state]
    if not all(bool(torch.isfinite(value).all()) for value in (inputs, labels, queries)):
        raise FloatingPointError('Euler data contain nonfinite entries')
    predictions, times, observation_steps, losses = [], [], [], []
    finite_checks, finite_locations = [], []
    observed_gram_minima = []
    loss_check_steps, loss_check_times, loss_checks = [], [], []
    steps, current, last_step = 0, 0., 0.
    training_seconds = loss_seconds = query_seconds = refresh_seconds = 0.

    def check_training_loss():
        nonlocal loss_seconds
        check_started = time.monotonic()
        state_finite = torch.stack([torch.isfinite(value).all() for value in state]).all()
        prediction = model.predict(state, inputs, inputs, labels)
        if prediction.shape != labels.shape:
            raise ValueError('Euler training prediction must have the label shape')
        loss = (prediction-labels).square().mean().detach()
        valid = state_finite & torch.isfinite(loss)
        finite_checks.append(valid)
        finite_locations.append(f'state/loss at step {steps}, t={current:.9g}')
        if horizon_steps is None and not bool(valid):
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
        query_valid = torch.isfinite(prediction).all()
        if horizon_steps is None and not bool(query_valid):
            raise FloatingPointError(f'Nonfinite Euler query prediction at step {steps}, t={current:.9g}')
        finite_checks.append(query_valid)
        finite_locations.append(f'query prediction at step {steps}, t={current:.9g}')
        predictions.append(prediction.detach().clone())
        synchronize(device)
        query_seconds += time.monotonic()-query_started
        times.append(current)
        observation_steps.append(steps)
        losses.append(loss)
        if getattr(model, 'readout_floor', None) is not None:
            gram = model._readout(state, inputs, labels)[-1]
            observed_gram_minima.append(torch.linalg.eigvalsh(gram)[0].detach())

    def stopping_reason(loss):
        if time.monotonic()-started >= seconds:
            return 'wall_time_cap'
        if horizon_steps is not None and steps == horizon_steps:
            return 'horizon'
        if horizon is None and loss_target is not None and bool(loss < loss_target):
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
            if dense_step is not None:
                dense_step(state, inputs, labels, last_step)
            else:
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
    export_started = time.monotonic()
    host_checks = torch.stack(finite_checks).cpu().numpy()
    if not host_checks.all():
        raise FloatingPointError('Nonfinite Euler '+finite_locations[np.flatnonzero(~host_checks)[0]])
    host_predictions = torch.stack(predictions).cpu().numpy()
    loss_checks = torch.stack(loss_checks).cpu().tolist()
    losses = torch.stack(losses).cpu().tolist()
    observed_gram_minima = (torch.stack(observed_gram_minima).cpu().tolist()
                           if observed_gram_minima else [])
    loss = loss_checks[-1]
    synchronize(device)
    export_seconds = time.monotonic()-export_started
    elapsed = time.monotonic()-started
    if elapsed >= seconds:
        reason = 'wall_time_cap'
    peak_bytes = torch.cuda.max_memory_allocated(device) if device.type == 'cuda' else None
    return state, host_predictions, dict(
        method='explicit_euler', update_kernel='dense_addmm' if dense_step is not None else 'generic_rhs',
        observation_storage='simulation device until final export', export_seconds=export_seconds,
        dtype=str(inputs.dtype), step=step, last_step=last_step,
        requested_horizon=horizon, actual_horizon=current, steps=steps,
        times=times, observation_steps=observation_steps, losses=losses,
        final_training_mse=loss, loss_target=loss_target,
        observed_feature_gram_minima=observed_gram_minima,
        loss_target_reached=(loss < loss_target if loss_target is not None else None),
        horizon_reached=(steps == horizon_steps if horizon_steps is not None else None),
        stop_reason=reason, complete=reason in ('horizon', 'loss_target'),
        max_steps=max_steps, observation_every=observation_every,
        loss_check_every_at_most=check_every, loss_check_steps=loss_check_steps,
        loss_check_times=loss_check_times, loss_checks=loss_checks,
        seconds=elapsed, wall_time_cap_seconds=seconds, within_wall_time_cap=elapsed <= seconds,
        training_seconds=training_seconds, training_loss_seconds=loss_seconds,
        query_seconds=query_seconds, query_refresh_seconds=refresh_seconds,
        query_timing_scope='whole sparse query batches after readout refresh; final CPU export timed separately',
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
    fused_error = 0.
    for depth in (1, 2, 5):
        for activation in DEEP_ACTIVATIONS:
            deep = DeepDense(11, 2, depth, activation, 17, device)
            deep.initial_state[1].copy_(torch.linspace(-.1, .1, 11, device=device, dtype=dtype))
            expected = [value.clone() for value in deep.initial_state]
            for _ in range(16):
                velocity = deep.rhs(expected, inputs, labels)
                for value, derivative in zip(expected, velocity):
                    value.add_(derivative, alpha=.003)
            actual, _, info = integrate_euler(deep, inputs, labels, queries, .003, 10.,
                                              horizon=.048, observation_every=5)
            error = max(float((a-b).abs().max()) for a, b in zip(actual, expected))
            fused_error = max(fused_error, error)
            assert error < 1e-12 and info['update_kernel'] == 'dense_addmm', (depth, activation, error)
            assert info['observation_steps'] == [0, 5, 10, 15, 16], info
    _, _, fixed = integrate_euler(model, inputs, labels, queries, .001, 10.,
                                  horizon=.32, observation_every=320)
    assert fixed['loss_check_steps'] == [0, 256, 320], fixed
    class AliasingModel:
        fixed_scalars = 0
        initial_state = [torch.zeros_like(labels)]

        def rhs(self, state, inputs, labels):
            return [torch.ones_like(state[0])]

        def predict(self, state, queries, inputs, labels):
            return state[0]  # Reporting must snapshot this mutable state alias.

    _, snapshots, _ = integrate_euler(AliasingModel(), inputs, labels, inputs, .01, 10.,
                                      horizon=.03, observation_every=1)
    np.testing.assert_allclose(snapshots, np.arange(4)[:, None]*np.ones((1, len(labels)))*.01,
                               rtol=0, atol=1e-14)
    return dict(manual_euler_max_abs=manual_error, terminal_query_max_abs=query_error,
                fused_dense_max_abs=fused_error,
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
def compression_pilot_main(argv):
    """Training-only horizon planning; no compressed model or test predictions."""
    from scipy.integrate import solve_ivp
    parser = argparse.ArgumentParser(description=compression_pilot_main.__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--digits', type=int, nargs=2, required=True)
    args = parser.parse_args(argv)
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    inputs, labels, _, _ = validation_data(64, 8, 0, 47, torch.device('cpu'),
                                           'digits', 'test', True, 0, args.digits)
    report = dict(source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        digits=args.digits, width=128, method='DOP853', rtol=1e-6, atol=1e-8,
        horizon_cap=4096., per_case_seconds=30., training_mse_target=.001,
        scored_predictions_used=False, cases=[])
    with torch.no_grad():
        for depth in (2, 3, 5, 10):
            for activation in ('tanh', 'gelu', 'silu'):
                model = DeepDense(128, 64, depth, activation, 601, torch.device('cpu'))
                shapes = [v.shape for v in model.initial_state]
                boundaries = np.cumsum([0]+[v.numel() for v in model.initial_state])
                initial = np.concatenate([v.numpy().reshape(-1) for v in model.initial_state])
                def unpack(value):
                    return [torch.from_numpy(value[left:right]).reshape(shape)
                            for left, right, shape in zip(boundaries[:-1], boundaries[1:], shapes)]
                started = time.monotonic()
                def rhs(t, value):
                    if time.monotonic()-started > 30.:
                        raise TimeoutError('Training-only pilot exceeded 30 seconds')
                    return np.concatenate([v.numpy().reshape(-1) for v in model.rhs(unpack(value), inputs, labels)])
                def fitted(t, value):
                    return float((model.predict(unpack(value), inputs)-labels).square().mean())-.001
                fitted.terminal, fitted.direction = True, -1
                case = dict(depth=depth, activation=activation)
                try:
                    solution = solve_ivp(rhs, (0., 4096.), initial, method='DOP853',
                                         rtol=1e-6, atol=1e-8, max_step=8., events=fitted)
                    case.update(success=bool(solution.success), fitted=bool(len(solution.t_events[0])),
                        time=float(solution.t[-1]), training_mse=fitted(solution.t[-1], solution.y[:, -1])+.001,
                        rhs_calls=solution.nfev, accepted_steps=len(solution.t)-1)
                    del solution
                except Exception as error:
                    case.update(success=False, fitted=False, error=f'{type(error).__name__}: {error}')
                case['seconds'] = time.monotonic()-started
                report['cases'].append(case)
                save_json(args.out/'report.json', report)
                print(json.dumps(case), flush=True)


def _cubic_residual_partition(times, residual_rms, horizon):
    """Frozen empirical flaring rule; interpolate log residual on a fixed trace."""
    times, residual_rms = np.asarray(times, dtype=float), np.asarray(residual_rms, dtype=float)
    if (not math.isfinite(horizon) or horizon <= 0 or times.ndim != 1
            or residual_rms.shape != times.shape or len(times) < 2
            or not np.isfinite(times).all() or not np.isfinite(residual_rms).all()
            or times[0] != 0 or times[-1] < horizon or np.any(np.diff(times) <= 0)
            or residual_rms[0] <= 0 or np.any(residual_rms < 0)):
        raise ValueError('Residual partition needs a positive horizon and finite nonnegative trace')
    logarithms = np.log(np.maximum(residual_rms, np.finfo(float).tiny))
    boundaries = [0.]
    while boundaries[-1] < horizon:
        log_rho = float(np.interp(boundaries[-1], times, logarithms))
        length = (1. if log_rho == logarithms[0] else
                  float(np.logaddexp(0., math.log(.1)+logarithms[0]-log_rho)/math.log1p(.1)))
        endpoint = min(float(horizon), boundaries[-1]+length)
        if endpoint <= boundaries[-1] or len(boundaries) > 100000:
            raise ArithmeticError('Residual partition failed to advance within its finite budget')
        boundaries.append(endpoint)
    return boundaries


@torch.no_grad()
def appendix_spectral_main(argv):
    """Three fixed-width full-spectrum source measurements, with no rescue runs."""
    parser = argparse.ArgumentParser(description=appendix_spectral_main.__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--worker-width', type=int, choices=(512, 1024, 2048, 4096, 8192),
                        help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    config = dict(widths=[args.worker_width] if args.worker_width else [512, 1024, 2048],
        depth=2, activation='tanh', reference_seed=901,
        dataset=dict(name='sphere', dimension=2, train_samples=8, test_samples=30,
                     undeclared_samples=30, seed=47, digit_pair=[1, 7], label_scale=1.),
        horizon=32., source_step=.125, time_degree=8, source_dtype='float32',
        coefficient_dtype='float64', source_rank=37, partition='new',
        relative_frobenius_tail_thresholds=[.01, .001], tf32=False,
        seconds_per_width_including_worker_startup=120., device=args.device,
        metric='minimum r with sqrt(sum(sigma[r:]**2))/||C_perp||_F <= tolerance',
        primary_matrix='actual top-layer h histories at common temporal holdouts after mandatory-span removal',
        auxiliary_matrix='all degree-8 Chebyshev coefficient blocks after mandatory-span removal',
        temporal_holdout='odd Chebyshev nodes, excluded from coefficient fitting',
        source_seed=_experiment_seed(901, 'logarithmic_source'),
        scope='Single-seed finite-width source spectra; no asymptotic rate or theorem certificate')
    args.out.mkdir(parents=True, exist_ok=False)
    save_json(args.out/'config.json', config)
    source_bytes = Path(__file__).read_bytes()
    report = dict(config=config, source_sha256=sha(source_bytes),
        command=[sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]],
        cwd=str(Path.cwd()), python=platform.python_version(), torch=torch.__version__,
        numpy=np.__version__, complete=False, cases=[])
    if args.worker_width is not None:
        (args.out/'source.py').write_bytes(source_bytes)
        device = torch.device(args.device)
        report.update(width=args.worker_width, spectra=[], history_spectra=[], status='inconclusive',
            hardware=torch.cuda.get_device_name(device) if device.type == 'cuda' else platform.processor())
        save_json(args.out/'report.json', report)
        started = time.monotonic()
        try:
            arrays = _experiment_data(config)
            report['data_sha256'] = {key: array_sha(value) for key, value in arrays.items()}
            inputs, labels, queries = [torch.as_tensor(arrays[key], device=device) for key in
                                      ('train_inputs', 'train_labels', 'query_inputs')]
            dense = DeepDense(args.worker_width, 2, 2, 'tanh', 901, device)
            sources, source_report = cubic_rollout_sources(dense, inputs, labels, queries,
                horizon=32., seconds=120., seed=config['source_seed'], ranks=(37,),
                partitions=('new',), step=.125, time_degree=8,
                full_spectra=report['spectra'], full_history_spectra=report['history_spectra'])
            report.update(sources=source_report, complete=True, status='completed',
                maximum_required_rank={str(tolerance): max(item['required_rank'][str(tolerance)]
                    for item in report['spectra']) for tolerance in (.01, .001)},
                maximum_temporal_holdout_rms=max(item['temporal_holdout_rms'] for item in report['spectra']),
                maximum_temporal_holdout_relative_rms=max(
                    item['temporal_holdout_relative_rms'] for item in report['spectra']),
                history_required_rank=report['history_spectra'][0]['required_rank'])
            del sources, dense
        except (RuntimeError, ValueError, ArithmeticError, TimeoutError) as error:
            report['error'] = f'{type(error).__name__}: {error}'
        report['seconds'] = time.monotonic()-started
        save_json(args.out/'report.json', report)
        print(json.dumps(dict(event='appendix_spectrum', width=args.worker_width,
            status=report['status'], seconds=report['seconds'],
            coefficient_ranks=report.get('maximum_required_rank'),
            history_ranks=report.get('history_required_rank'), error=report.get('error'))), flush=True)
        return 0 if report['complete'] else 1

    # Freeze all compared runs against this exact script even while other tasks
    # are editing unrelated entry points in the maintained executable.
    snapshot = args.out/'capture_trajectory_snapshot.py'
    snapshot.write_bytes(source_bytes)
    report['snapshot'] = str(snapshot.resolve())
    save_json(args.out/'report.json', report)
    for width in config['widths']:
        case_out = args.out/f'n{width}'
        command = [sys.executable, str(snapshot.resolve()), 'appendix-spectral',
                   '--out', str(case_out.resolve()), '--device', args.device,
                   '--worker-width', str(width)]
        case = dict(width=width, command=command, complete=False, status='inconclusive')
        started = time.monotonic()
        try:
            with (args.out/f'n{width}.log').open('w') as log:
                completed = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                    timeout=config['seconds_per_width_including_worker_startup'], check=False)
            case['exit_code'] = completed.returncode
        except subprocess.TimeoutExpired:
            case.update(exit_code=None, error='Hard 120-second per-width deadline; no retry')
        case['seconds'] = time.monotonic()-started
        if (case_out/'report.json').is_file():
            saved = json.loads((case_out/'report.json').read_text())
            if case.get('exit_code') == 0 and saved.get('complete'):
                case.update(complete=True, status='completed',
                    maximum_required_rank=saved['maximum_required_rank'],
                    history_required_rank=saved['history_required_rank'],
                    maximum_temporal_holdout_rms=saved['maximum_temporal_holdout_rms'],
                    maximum_temporal_holdout_relative_rms=saved['maximum_temporal_holdout_relative_rms'])
            case['result'] = saved
        report['cases'].append(case)
        save_json(args.out/'report.json', report)
        print(json.dumps({key: value for key, value in case.items() if key != 'result'}), flush=True)
    report['complete'] = all(case['complete'] for case in report['cases'])
    report['status'] = 'completed' if report['complete'] else 'inconclusive'

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})
    figure, axes = plt.subplots(2, 3, figsize=(13.2, 7.4), constrained_layout=True)
    colors = {512: '#2563eb', 1024: '#d97706', 2048: '#16856c'}
    families = [('h', 1), ('h', 2), ('delta', 1), ('delta', 2)]
    for ax, (family, layer) in zip(axes.flat, families):
        for case in report['cases']:
            for item in case.get('result', {}).get('spectra', []):
                if item['family'] == family and item['layer'] == layer:
                    singular = np.asarray(item['singular_values'])
                    denominator = item['projected_coefficient_frobenius']
                    if denominator > 0:
                        ax.loglog(np.arange(1, len(singular)+1), np.maximum(
                            singular/denominator, np.finfo(float).tiny),
                            color=colors[case['width']], label=f"n={case['width']}", lw=1.5)
        symbol = 'h' if family == 'h' else r'\delta'
        ax.set_title(rf'${symbol}^{{({layer})}}$ coefficient spectrum')
        ax.set_xlabel('Singular-value index')
        ax.set_ylabel(r'$\sigma_j/\|C_\perp\|_F$')
        ax.grid(True, alpha=.18)
        if ax.lines:
            ax.legend(frameon=False, fontsize=8)
    rank_ax, holdout_ax = axes[1, 1], axes[1, 2]
    complete = [case for case in report['cases'] if case['complete']]
    widths = [case['width'] for case in complete]
    for tolerance, marker, label in ((.01, 'o', '1% tail'), (.001, 's', '0.1% tail')):
        rank_ax.plot(widths, [case['maximum_required_rank'][str(tolerance)] for case in complete],
                     marker=marker, label=label)
    rank_ax.set(xlabel='Dense width n', ylabel='Maximum required rank',
                title='Worst rank across layers and families', xticks=config['widths'])
    rank_ax.legend(frameon=False)
    for family, layer in families:
        values = [next(item['temporal_holdout_relative_rms'] for item in case['result']['spectra']
                       if item['family'] == family and item['layer'] == layer) for case in complete]
        symbol = 'h' if family == 'h' else r'\delta'
        holdout_ax.semilogy(widths, values, marker='o', label=rf'${symbol}^{{({layer})}}$')
    holdout_ax.set(xlabel='Dense width n', ylabel='Temporal holdout relative RMS',
                   title='Degree-8 interpolation check', xticks=config['widths'])
    holdout_ax.legend(frameon=False, ncol=2)
    for ax in (rank_ax, holdout_ax):
        ax.grid(True, alpha=.18)
    figure.suptitle('Auxiliary coefficient spectra after mandatory-span removal; one seed, T=32')
    missing = [str(case['width']) for case in report['cases'] if not case['complete']]
    if missing:
        figure.supxlabel('Inconclusive widths: '+', '.join(missing))
    for suffix in ('png', 'pdf'):
        figure.savefig(args.out/f'coefficient_spectra.{suffix}', dpi=190)
    plt.close(figure)
    figure, axes = plt.subplots(1, 3, figsize=(13.2, 3.9), constrained_layout=True)
    for case in complete:
        history = case['result']['history_spectra'][0]
        singular = np.asarray(history['singular_values'])
        denominator = history['projected_history_frobenius']
        if denominator > 0:
            axes[0].loglog(np.arange(1, len(singular)+1), np.maximum(
                singular/denominator, np.finfo(float).tiny), color=colors[case['width']],
                label=f"n={case['width']}", lw=1.5)
    axes[0].set(xlabel='Singular-value index', ylabel=r'$\sigma_j/\|H_\perp\|_F$',
                title='Actual held-out top-layer h history')
    if axes[0].lines:
        axes[0].legend(frameon=False)
    for tolerance, marker, label in ((.01, 'o', '1% tail'), (.001, 's', '0.1% tail')):
        axes[1].plot(widths, [case['history_required_rank'][str(tolerance)] for case in complete],
                     marker=marker, label=label)
    axes[1].set(xlabel='Dense width n', ylabel='Required history rank',
                title='Relative Frobenius-tail criterion', xticks=config['widths'])
    axes[1].legend(frameon=False)
    for field, label, marker in (('original_history_rms', 'Before mandatory projection', 's'),
                                 ('projected_history_rms', 'After mandatory projection', 'o')):
        axes[2].semilogy(widths, [case['result']['history_spectra'][0][field] for case in complete],
                         marker=marker, label=label)
    axes[2].set(xlabel='Dense width n', ylabel='History RMS', title='Absolute history size',
                xticks=config['widths'])
    axes[2].legend(frameon=False, fontsize=8)
    for ax in axes:
        ax.grid(True, alpha=.18)
    figure.suptitle('Mandatory-projected dense source histories; circle, one seed, T=32')
    if missing:
        figure.supxlabel('Inconclusive widths: '+', '.join(missing))
    for suffix in ('png', 'pdf'):
        figure.savefig(args.out/f'source_spectra.{suffix}', dpi=190)
    plt.close(figure)
    report['artifacts'] = {name: sha((args.out/name).read_bytes()) for name in
                           ('config.json', 'source_spectra.png', 'source_spectra.pdf',
                            'coefficient_spectra.png', 'coefficient_spectra.pdf',
                            'capture_trajectory_snapshot.py')}
    save_json(args.out/'report.json', report)
    return 0 if report['complete'] else 1


def cubic_source_small_checks():
    """Tiny schedule and polynomial-coordinate checks, with no learning experiment."""
    times = np.arange(33, dtype=float)/8
    constant = _cubic_residual_partition(times, np.ones_like(times), 4.)
    if not np.allclose(constant, np.arange(5), atol=1e-13, rtol=0):
        raise AssertionError('Constant residual must give unit physical-time intervals')
    decaying = _cubic_residual_partition(times, np.exp(-times), 4.)
    rescaled = _cubic_residual_partition(times, 7*np.exp(-times), 4.)
    if not np.allclose(decaying, rescaled, atol=1e-13, rtol=0):
        raise AssertionError('Residual partition must be invariant under label-scale rescaling')
    if not (decaying[-1] == 4. and len(decaying) < len(constant)
            and np.all(np.diff(decaying) > 0)):
        raise AssertionError('Decaying residual must widen the untruncated early intervals')
    coordinate = -np.cos(np.linspace(0, np.pi, 17))
    design = np.polynomial.chebyshev.chebvander(coordinate, 8)
    coefficient = np.arange(27, dtype=float).reshape(9, 3)/27
    fitted = np.linalg.pinv(design[::2])@(design[::2]@coefficient)
    error = float(np.max(np.abs(design[1::2]@(fitted-coefficient))))
    if error > 1e-12:
        raise AssertionError('Nine fitting nodes must recover degree-eight polynomials')
    return dict(passed=True, constant_boundaries=constant, decaying_boundaries=decaying,
                label_scale_invariant=True, polynomial_holdout_max=error)


@torch.no_grad()
def cubic_rollout_sources(dense, inputs, labels, source_queries, horizon=32., seconds=120., seed=501,
                          ranks=(12, 6), partitions=('old', 'new'), *, step=.125,
                          time_degree=8, rollout_dtype=torch.float32,
                          coefficient_dtype=torch.float64, full_spectra=None,
                          full_history_spectra=None):
    """Paired empirical partitions, a shared dense teacher, and nested source ranks.

    Sources are returned as sources[partition][rank][family][layer].  The common
    check measures each dense field after removing its initialized mandatory
    span and the retained directions.  No finite-jet or source certificate is
    asserted, and shared teacher time is not a native single-method setup cost.
    Rollouts default to float32; all fitted coefficients use float64.
    When full_spectra is a list, append complete projected coefficient spectra
    from a direct SVD. These measurements never use the randomized source fit.
    full_history_spectra optionally receives the direct top-layer activation
    history spectrum at all common holdouts, before any polynomial fitting.
    """
    if (not math.isfinite(horizon) or horizon <= 0 or not math.isfinite(seconds)
            or seconds <= 0 or not math.isfinite(step) or step <= 0
            or len(labels) != len(inputs) or not len(labels)):
        raise ValueError('Paired source setup needs positive finite limits and training data')
    if (not isinstance(time_degree, (int, np.integer))
            or isinstance(time_degree, bool) or time_degree < 1):
        raise ValueError('Paired source time degree must be a positive integer')
    if rollout_dtype in ('float32', 'float64'):
        rollout_dtype = getattr(torch, rollout_dtype)
    if rollout_dtype not in (torch.float32, torch.float64):
        raise ValueError('Paired source rollout dtype must be float32 or float64')
    if coefficient_dtype not in (torch.float64, 'float64'):
        raise ValueError('Paired source coefficient dtype currently supports only float64')
    if full_spectra is not None and not isinstance(full_spectra, list):
        raise ValueError('full_spectra must be an output list or None')
    if full_history_spectra is not None and not isinstance(full_history_spectra, list):
        raise ValueError('full_history_spectra must be an output list or None')
    if (not ranks or any(not isinstance(rank, int) or rank < 1 for rank in ranks)
            or len(set(ranks)) != len(ranks) or not partitions
            or len(set(partitions)) != len(partitions) or set(partitions)-{'old', 'new'}):
        raise ValueError('Need distinct positive ranks and old/new partition names')
    svd_order = max(ranks)+8
    device, n = inputs.device, len(dense.initial_state[1])
    synchronize(device)
    started = time.monotonic()
    deadline = started+min(float(seconds), 120.)

    def remaining():
        synchronize(device)
        value = deadline-time.monotonic()
        if value <= 0:
            raise TimeoutError('Paired cubic source setup exceeded its total wall-clock cap')
        return value

    teacher = DeepDense.__new__(DeepDense)
    teacher.depth, teacher.activation = dense.depth, dense.activation
    teacher.initial_state = [value.to(dtype=rollout_dtype) for value in dense.initial_state]
    teacher.fixed_scalars = 0
    source_inputs, source_labels = inputs.to(dtype=rollout_dtype), labels.to(dtype=rollout_dtype)
    source_panel = torch.cat((source_inputs, source_queries.to(dtype=rollout_dtype)))
    trace_times = np.unique(np.r_[np.arange(0., horizon, step), float(horizon)])
    precursor_state, precursor_predictions, precursor_run = integrate(
        teacher, source_inputs, source_labels, source_inputs[:1], trace_times, step, remaining())
    del precursor_state, precursor_predictions
    residual_rms = np.sqrt(np.asarray(precursor_run['losses'], dtype=float))
    boundaries = {'old': [0., min(1., float(horizon))],
                  'new': _cubic_residual_partition(trace_times, residual_rms, horizon)}
    while boundaries['old'][-1] < horizon:
        boundaries['old'].append(min(2*boundaries['old'][-1], float(horizon)))
    intervals = {name: [left+(right-left)*(1-np.cos(np.linspace(0, np.pi, 2*time_degree+1)))/2
                       for left, right in zip(edges[:-1], edges[1:])]
                 for name, edges in boundaries.items()}
    fitting_times = np.unique(np.concatenate([nodes[::2] for panels in intervals.values()
                                              for nodes in panels]))
    common_times = (np.arange(129, dtype=float)+.5)*horizon/129
    common_times = common_times[~np.isclose(common_times[:, None], fitting_times[None, :],
                                           rtol=0, atol=1e-12).any(axis=1)]
    panel_times = np.unique(np.concatenate([nodes for panels in intervals.values() for nodes in panels]))
    # Odd degrees place the midpoint among holdouts. Reuse that node when a
    # common check coincides up to roundoff, avoiding a zero-length RK4 interval.
    distances = np.abs(common_times[:, None]-panel_times[None, :])
    nearest = distances.argmin(axis=1)
    common_times = np.where(distances[np.arange(len(common_times)), nearest] <= 1e-12,
                            panel_times[nearest], common_times)
    observation_times = np.unique(np.concatenate([common_times, panel_times]))
    common_indices = np.searchsorted(observation_times, common_times)
    fields = {name: [[] for _ in range(dense.depth)] for name in ('h', 'delta')}

    def observe(t, state):
        remaining()
        hs, gates = teacher.fields(state, source_panel)
        deltas = teacher.backward(state, [h[:, :len(labels)] for h in hs],
                                  [g[:, :len(labels)] for g in gates])
        for family, values in (('h', hs), ('delta', deltas)):
            for layer, value in enumerate(values):
                fields[family][layer].append(value.detach())

    shared_state, shared_predictions, shared_run = integrate(
        teacher, source_inputs, source_labels, source_inputs[:1], observation_times,
        step, remaining(), observer=observe)
    del shared_state, shared_predictions, teacher, source_inputs, source_labels, source_panel
    remaining()
    original = [value.double() for value in dense.initial_state]
    h0, _ = dense.fields(original, inputs.double())
    constant = torch.ones(n, 1, device=device, dtype=torch.float64)
    fit_intervals = {name: intervals[name] for name in partitions}
    sources = {name: {rank: {family: [] for family in fields} for rank in ranks}
               for name in fit_intervals}
    partition_reports = {}
    for name, panels in fit_intervals.items():
        partition_reports[name] = dict(
            boundaries=boundaries[name], interval_count=len(panels), degree=time_degree,
            fitting_node_count=len(np.unique(np.concatenate([nodes[::2] for nodes in panels]))),
            interval_check_node_count=len(np.unique(np.concatenate([nodes[1::2] for nodes in panels]))),
            fitting_seconds=0., svd_seconds=0., checking_seconds=0., svd_calls=0,
            fit_blocks=0, fit_output_scalars=0, svd_input_scalars=0,
            diagnostics={str(rank): {family: [] for family in fields} for rank in ranks})
    coordinate = -np.cos(np.linspace(0, np.pi, 2*time_degree+1))
    design = torch.as_tensor(np.polynomial.chebyshev.chebvander(coordinate, time_degree),
                             device=device, dtype=torch.float64)
    fitting_inverse = torch.linalg.pinv(design[::2])
    devices = [device.index] if device.type == 'cuda' else []
    for family in fields:
        for layer, observations in enumerate(fields[family]):
            remaining()
            values = torch.stack(observations).to(device=device, dtype=torch.float64)
            observations.clear()
            fields[family][layer] = []
            mandatory = values.new_empty((n, 0))
            if family == 'h':
                mandatory = h0[layer]
                if layer == dense.depth-1:
                    additions = [constant, h0[layer]]
                    if layer:
                        additions.append(original[layer+1]@h0[layer-1])
                    mandatory = torch.cat(additions, 1)
            elif layer == 0:
                mandatory = torch.cat((constant, original[0], h0[0]), 1)
            mandatory_basis = mandatory
            if mandatory.shape[1]:
                mandatory_basis, _ = _harmonic_source_basis(mandatory, mandatory[:, :0])
                mandatory_basis = mandatory_basis/math.sqrt(n)
            checked = values[common_indices].permute(1, 0, 2).reshape(n, -1)
            dense_square = float(checked.square().sum())
            for _ in range(2):
                checked -= mandatory_basis@(mandatory_basis.T@checked)
            residual_square = float(checked.square().sum())
            if full_history_spectra is not None and family == 'h' and layer == dense.depth-1:
                phase = time.monotonic()
                history_singular = torch.linalg.svdvals(checked, **(
                    dict(driver='gesvd') if device.type == 'cuda' else {}))
                remaining()
                if not bool(torch.isfinite(history_singular).all()):
                    raise ArithmeticError('Nonfinite full source-history spectrum')
                history_array = history_singular.cpu().numpy()
                tail_square = np.r_[np.cumsum(history_array[::-1]**2)[::-1], 0.]
                relative_tail = np.sqrt(tail_square/max(residual_square, 1e-300))
                full_history_spectra.append(dict(
                    family=family, layer=layer+1, history_shape=list(checked.shape),
                    observation_times=common_times.tolist(), observation_count=len(common_times),
                    columns_per_time=values.shape[2], mandatory_span_rank=int(mandatory_basis.shape[1]),
                    history_scope='actual dense activation histories at common holdouts after mandatory-span removal',
                    polynomial_fitting_used=False, singular_values=history_array.tolist(),
                    full_spectrum=True, svd_method='direct torch.linalg.svdvals',
                    svd_driver='gesvd' if device.type == 'cuda' else 'LAPACK default',
                    full_svd_seconds=time.monotonic()-phase,
                    numerical_rank=int((history_singular > max(checked.shape)*
                        torch.finfo(checked.dtype).eps*history_singular[0]).sum()),
                    original_history_frobenius=math.sqrt(dense_square),
                    projected_history_frobenius=math.sqrt(residual_square),
                    original_history_rms=math.sqrt(dense_square/checked.numel()),
                    projected_history_rms=math.sqrt(residual_square/checked.numel()),
                    projected_history_energy_fraction=residual_square/max(dense_square, 1e-300),
                    spectral_energy_relative_discrepancy=abs(float(tail_square[0])-
                        residual_square)/max(residual_square, 1e-300),
                    required_rank={str(tolerance): int(np.flatnonzero(relative_tail <= tolerance)[0])
                                   for tolerance in (.01, .001)}))
                del history_singular
                remaining()
            for partition, panels in fit_intervals.items():
                remaining()
                detail = partition_reports[partition]
                phase = time.monotonic()
                blocks, square, count, holdout_square = [], 0., 0, 0.
                for nodes in panels:
                    remaining()
                    indices = np.searchsorted(observation_times, nodes)
                    block = torch.einsum('kt,tnp->nkp', fitting_inverse, values[indices[::2]])
                    error = torch.einsum('tk,nkp->tnp', design[1::2], block)-values[indices[1::2]]
                    square += float(error.square().sum())
                    count += error.numel()
                    if full_spectra is not None:
                        holdout_square += float(values[indices[1::2]].square().sum())
                    blocks.append(block.flatten(1))
                source = torch.cat(blocks, 1)
                if full_spectra is not None:
                    original_coefficient_square = float(source.square().sum())
                for _ in range(2):
                    source -= mandatory_basis@(mandatory_basis.T@source)
                remaining()
                detail['fitting_seconds'] += time.monotonic()-phase
                detail['fit_blocks'] += len(panels)
                detail['fit_output_scalars'] += source.numel()
                if full_spectra is not None:
                    phase = time.monotonic()
                    exact_singular = torch.linalg.svdvals(source, **(
                        dict(driver='gesvd') if device.type == 'cuda' else {}))
                    remaining()
                    if not bool(torch.isfinite(exact_singular).all()):
                        raise ArithmeticError('Nonfinite full source spectrum')
                    singular_array = exact_singular.cpu().numpy()
                    coefficient_square = float(source.square().sum())
                    tail_square = np.r_[np.cumsum(singular_array[::-1]**2)[::-1], 0.]
                    relative_tail = np.sqrt(tail_square/max(coefficient_square, 1e-300))
                    full_spectra.append(dict(
                        partition=partition, family=family, layer=layer+1,
                        coefficient_shape=list(source.shape),
                        mandatory_span_rank=int(mandatory_basis.shape[1]),
                        singular_values=singular_array.tolist(), full_spectrum=True,
                        svd_method='direct torch.linalg.svdvals',
                        svd_driver='gesvd' if device.type == 'cuda' else 'LAPACK default',
                        full_svd_seconds=time.monotonic()-phase,
                        numerical_rank=int((exact_singular > max(source.shape)*
                            torch.finfo(source.dtype).eps*exact_singular[0]).sum()),
                        original_coefficient_frobenius=math.sqrt(original_coefficient_square),
                        projected_coefficient_frobenius=math.sqrt(coefficient_square),
                        projected_coefficient_energy_fraction=coefficient_square/max(
                            original_coefficient_square, 1e-300),
                        spectral_energy_relative_discrepancy=abs(float(tail_square[0])-
                            coefficient_square)/max(coefficient_square, 1e-300),
                        required_rank={str(tolerance): int(np.flatnonzero(
                            relative_tail <= tolerance)[0]) for tolerance in (.01, .001)},
                        temporal_holdout_rms=math.sqrt(square/count),
                        temporal_holdout_dense_rms=math.sqrt(holdout_square/count),
                        temporal_holdout_relative_rms=math.sqrt(square/max(holdout_square, 1e-300)),
                        common_check_dense_rms=math.sqrt(dense_square/checked.numel()),
                        common_check_after_mandatory_rms=math.sqrt(residual_square/checked.numel())))
                    del exact_singular
                    remaining()
                phase = time.monotonic()
                with torch.random.fork_rng(devices=devices):
                    torch.manual_seed(seed+layer+(100 if family == 'delta' else 0))
                    left, singular, _ = torch.svd_lowrank(source, q=min(svd_order, *source.shape), niter=2)
                remaining()
                detail['svd_seconds'] += time.monotonic()-phase
                detail['svd_calls'] += 1
                detail['svd_input_scalars'] += source.numel()
                available = int((singular > max(source.shape)*torch.finfo(source.dtype).eps*singular[0]).sum())
                phase = time.monotonic()
                for rank in ranks:
                    retained = left[:, :min(rank, available)].clone()
                    sources[partition][rank][family].append(retained)
                    source_error = source-retained@(retained.T@source)
                    error = checked-retained@(retained.T@checked)
                    error_square = float(error.square().sum())
                    detail['diagnostics'][str(rank)][family].append(dict(
                        rank=int(retained.shape[1]), available_rank=available,
                        mandatory_rank=int(mandatory_basis.shape[1]),
                        coefficient_shape=list(source.shape), randomized_svd_q=min(svd_order, *source.shape),
                        temporal_holdout_rms=math.sqrt(square/count),
                        residual_coefficient_relative_error=float(source_error.norm()/source.norm().clamp_min(1e-30)),
                        common_check=dict(coordinate_max=float(error.abs().max()),
                            rms=math.sqrt(error_square/error.numel()),
                            max_curve_rms=float(error.square().mean(0).sqrt().max()),
                            relative_rms=math.sqrt(error_square/max(dense_square, 1e-60)),
                            residual_relative_rms=math.sqrt(error_square/max(residual_square, 1e-60)))))
                    remaining()
                detail['checking_seconds'] += time.monotonic()-phase
                del blocks, source, left, singular, source_error, error, block
            del values, checked
    remaining()
    report = dict(
        horizon=float(horizon), rk4_step=step, source_flow_dtype=str(rollout_dtype),
        coefficient_dtype='torch.float64', chebyshev_degree=time_degree, svd_seed=int(seed),
        randomized_svd_q=svd_order, randomized_svd_niter=2, nested_ranks=list(ranks),
        precursor_run=precursor_run, precursor_times=trace_times.tolist(),
        precursor_residual_rms=residual_rms.tolist(), shared_source_run=shared_run,
        dense_rhs_calls=4*(precursor_run['steps']+shared_run['steps']),
        observation_count=len(observation_times), observation_times=observation_times.tolist(),
        common_check_times=common_times.tolist(), common_check_count=len(common_times),
        common_check_excluded_fit_collisions=129-len(common_times),
        common_check_scope='dense h/delta minus mandatory and retained projections; all neuron coordinates',
        partitions=partition_reports, training_count=len(inputs), passive_count=len(source_queries),
        passive_labels_used=False, scored_inputs_used=True, source_certificate=False,
        source_provenance='full-horizon dense RK4 rollout plus disposable residual precursor',
        source_observation_storage=str(device), coefficient_fitting_device=str(device),
        timing_scope='paired shared setup; not native single-method preprocessing latency',
        total_setup_seconds=time.monotonic()-started, seconds_cap=min(float(seconds), 120.))
    return sources, report


def deep_rollout_sources(dense, inputs, labels, calibration, horizon, rank, seed, seconds=180., step=.125):
    """Sources on training/passive inputs; caller records whether passive nodes are scored.

    Passive labels are never an argument. The unseen protocol uses disjoint
    calibration nodes; the declared-panel protocol permits the scored inputs.
    """
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
                fields[name][layer].append(value.detach())
    _, _, source_run = integrate(teacher, source_inputs, source_labels, source_inputs[:1],
                                 times, step, seconds, observer=observe)
    del teacher, source_inputs, source_labels, source_panel
    h0, _ = dense.fields(dense.initial_state, inputs)
    n, device = len(dense.initial_state[1]), inputs.device
    constant = torch.ones(n, 1, dtype=inputs.dtype, device=device)
    coefficients, checks = {name: [] for name in fields}, {name: [] for name in fields}
    for name in fields:
        for layer, observations in enumerate(fields[name]):
            values = torch.stack(observations).to(device=device, dtype=torch.float64)
            observations.clear()
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
    return coefficients, dict(horizon=horizon, rk4_step=step, chebyshev_degree=8,
        observation_count=len(times), boundaries=boundaries, dense_rhs_calls=4*source_run['steps'],
        source_run_seconds=source_run['seconds'], diagnostics=checks,
        training_count=len(inputs), unlabeled_calibration_count=len(calibration),
        scored_inputs_used=False, calibration_labels_used=False, source_certificate=False)


@torch.no_grad()
def compression_probe_main(argv):
    """One fixed-budget unseen-query or declared-panel comparison; no search."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--width', type=int, default=8192)
    parser.add_argument('--depth', type=int, default=3)
    parser.add_argument('--activation', choices=DEEP_ACTIVATIONS, default='tanh')
    parser.add_argument('--digits', type=int, nargs=2, default=(3, 8))
    parser.add_argument('--samples', type=int, default=8)
    parser.add_argument('--calibration', type=int, default=32)
    parser.add_argument('--panel-queries', type=int,
                        help='Score exactly these many passive setup inputs; no other calibration inputs')
    parser.add_argument('--budget', type=int, help='Given retained width; omit for the original logarithmic rule')
    parser.add_argument('--source-rank', type=int, help='Given rank per source family; omit for the original rule')
    parser.add_argument('--readout-floor', type=float,
                        help='Enable rank-safe compression, including budget<samples, with this fixed floor')
    parser.add_argument('--compare-legacy', action='store_true',
                        help='Pair old/new on identical sources; cap floor at initial compact Gram gap/8')
    parser.add_argument('--source-step', type=float, default=.125)
    parser.add_argument('--seed', type=int, default=601)
    parser.add_argument('--horizon', type=float, default=32.)
    parser.add_argument('--step', type=float, default=.003125)
    parser.add_argument('--per-run-seconds', type=float, default=180.)
    args = parser.parse_args(argv)
    if args.depth < 2 or args.width < 1 or args.samples < 2 or args.calibration < 1:
        parser.error('Need depth>=2, positive width/calibration and at least two samples')
    minimum_budget = 1 if args.readout_floor is not None else args.samples
    if (args.budget is not None and not minimum_budget <= args.budget < args.width
            or args.source_rank is not None and args.source_rank < 1):
        parser.error('Need positive budget<width (also budget>=samples without --readout-floor) and source rank')
    if args.readout_floor is not None and (not math.isfinite(args.readout_floor) or args.readout_floor <= 0):
        parser.error('Readout floor must be finite and strictly positive')
    if args.panel_queries is not None and args.panel_queries < 1:
        parser.error('Panel query count must be positive')
    if args.compare_legacy and args.readout_floor is None:
        parser.error('Legacy comparison requires a positive --readout-floor cap')
    if (not math.isfinite(args.horizon) or args.horizon <= 0 or not math.isfinite(args.step)
            or args.step <= 0 or not math.isclose(.5/(2*args.step), round(.5/(2*args.step)), abs_tol=1e-9)):
        parser.error('Need a positive horizon and a step whose double divides the 0.5 observation interval')
    if not math.isfinite(args.source_step) or args.source_step <= 0:
        parser.error('Need a positive finite source step')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    scale = (math.log(math.e*args.width)/math.log(math.e*4096))**2.5
    budget = args.budget if args.budget is not None else math.ceil(320*scale)
    rank = args.source_rank if args.source_rank is not None else math.ceil(12*scale)
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
        if args.panel_queries is not None:
            if args.panel_queries > len(pool):
                raise ValueError('Panel query count exceeds held-out pool')
            indices = permutation[:args.panel_queries]
            calibration = queries = pool[indices]
            query_truth = truth[indices]
        else:
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
                                                    args.horizon, rank, args.seed, step=args.source_step)
        source['scored_inputs_used'] = args.panel_queries is not None
        source['input_contract'] = ('declared_unlabeled_test_panel' if args.panel_queries is not None
                                    else 'disjoint_unlabeled_calibration')
        floor = args.readout_floor
        legacy = None
        if args.compare_legacy:
            legacy = DeepHarmonic(dense, inputs, labels, coefficients, budget=budget)
            floor = min(floor, legacy.diagnostics['initial_feature_gram_min']/8)
            if floor <= 0:
                raise ArithmeticError('Paired legacy comparison requires a positive initial Gram gap')
        compact = DeepHarmonic(dense, inputs, labels, coefficients, budget=budget,
                               readout_floor=floor)
        if legacy is not None:
            geometry_error = max(float((a-b).abs().max())
                for key in ('initial_state', 'metrics', 'metric_inverses')
                for a, b in zip(getattr(legacy, key), getattr(compact, key)))
            assert geometry_error < 1e-12
            assert not any(item['truncated'] for item in compact.diagnostics['source_truncations'])
            report['legacy_pairing'] = dict(initial_arrays_max_difference=geometry_error,
                initial_training_gram_min=legacy.diagnostics['initial_feature_gram_min'],
                floor=floor, floor_rule='min(requested_cap, initial_compact_training_Gram_min/8)')
        del coefficients
        synchronize(device)
        report['setup'] = dict(seconds=time.monotonic()-started, source=source,
            diagnostics=compact.diagnostics, peak_cuda_bytes=torch.cuda.max_memory_allocated(device)
            if device.type == 'cuda' else None)
        if report['setup']['seconds'] > 180:
            raise TimeoutError('Source compilation exceeded its 180-second budget')
        for name, model in ([('dense', dense), ('compact', compact)]
                            +([('legacy', legacy)] if legacy is not None else [])):
            moving = sum(v.numel() for v in model.initial_state)
            report[name+'_words'] = dict(moving=moving, fixed=model.fixed_scalars,
                                         total=moving+model.fixed_scalars)
        expected = ((3*args.depth-2)*budget**2+65*budget+args.samples
                    +int(args.readout_floor is not None))
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
        if legacy is not None:
            move(legacy, 'cpu')
        torch.save(dict(depth=compact.depth, activation=compact.activation,
                        initial_state=compact.initial_state, metrics=compact.metrics,
                        metric_inverses=compact.metric_inverses,
                        readout_floor=floor), args.out/'compiled_model.pt')
        report['checkpoint_sha256'] = sha((args.out/'compiled_model.pt').read_bytes())
        inputs, labels, queries = [v.float() for v in (inputs, labels, queries)]
        del calibration, pool, truth
        names = ['dense', 'compact', 'iid', 'small']+(['legacy'] if legacy is not None else [])
        for name in names:
            model = (dense if name == 'dense' else compact if name == 'compact' else legacy if name == 'legacy' else
                     DeepDense(args.width if name == 'iid' else small_width, 64, args.depth,
                               args.activation, args.seed+(10000 if name == 'iid' else 20000), device))
            move(model, device)
            words = sum(v.numel() for v in model.initial_state)+model.fixed_scalars
            for suffix, step in ([('_coarse', 2*args.step), ('', args.step)]
                                 if name in ('dense', 'compact', 'legacy') else [('', args.step)]):
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
                    report['final_deficit_energy'] = float(state[-1].square().mean())
                    report['final_actual_training_mse'] = info['final_training_mse']
                del state
                save_json(args.out/'report.json', report)
                print(json.dumps(dict(event='probe_done', model=name+suffix, seconds=info['seconds'],
                                      mse=info['final_training_mse'])), flush=True)
            move(model, 'cpu')
            if name in ('iid', 'small'):
                del model
        assert report['runs']['small']['total_model_words'] <= expected
        reference = arrays['dense'].astype(float)
        for name in [key for key in names if key != 'dense']:
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
            all_fitted=all(report['runs'][name]['final_training_mse'] < .01
                           for name in names),
            complete=True, scored_inputs_used_for_setup=args.panel_queries is not None,
            scored_labels_used_for_setup=False,
            retained_scope='current model arrays including all fixed metrics/inverses; data and workspaces separate')
        for value in report['comparisons'].values():
            value['ratio_to_dense_pair'] = value['max_time_rms']/variability
        report['accuracy_pass'] = report['comparisons']['compact']['ratio_to_dense_pair'] <= 3
        if legacy is not None:
            legacy_refinement = sum(trajectory_rms(arrays[name].astype(float), arrays[name+'_coarse'].astype(float))
                                    ['max_time_rms'] for name in ('dense', 'legacy'))
            agreement = trajectory_rms(arrays['compact'].astype(float), arrays['legacy'].astype(float))
            report.update(legacy_refinement_sum=legacy_refinement,
                legacy_numerical_gate_pass=bool(legacy_refinement < .1*variability),
                old_new_agreement=agreement,
                preservation_pass=bool(agreement['max_time_rms'] <= .01*variability),
                beats_matched_small=bool(report['comparisons']['compact']['max_time_rms']
                                        < report['comparisons']['small']['max_time_rms']))
        print(json.dumps({k: report[k] for k in ('storage_reduction', 'comparisons', 'all_fitted',
                                                'numerical_gate_pass', 'accuracy_pass')}), flush=True)
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        np.savez_compressed(args.out/'trajectories.npz', **arrays)
        save_json(args.out/'report.json', report)


@torch.no_grad()
def unified_case_main(argv):
    """Fixed tanh width comparison, with moving-state-matched controls."""
    parser = argparse.ArgumentParser(description=unified_case_main.__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--dataset', choices=('sphere2', 'sphere3', 'sphere10', 'digits17'), required=True)
    parser.add_argument('--width', type=int, required=True)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--horizon', type=float, default=32.)
    parser.add_argument('--step', type=float, default=.0015625)
    parser.add_argument('--per-run-seconds', type=float, default=120.)
    args = parser.parse_args(argv)
    if (args.width < 512 or args.horizon <= 0 or args.step <= 0
            or not math.isclose(.5/(2*args.step), round(.5/(2*args.step)), abs_tol=1e-9)):
        parser.error('Need width>=512, positive horizon, and doubled step dividing 0.5')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    d = int(args.dataset[6:]) if args.dataset.startswith('sphere') else 64
    rank = math.ceil(8*(math.log(math.e*args.width)/math.log(math.e*1024))**2.5)
    budget = max(192, 4*(max(d+9, 17)+3*rank))
    order = math.ceil(8*(args.width/1024)**.25)
    report = dict(config={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
        device=torch.cuda.get_device_name(device) if device.type == 'cuda' else 'CPU',
        complete=False, models={}, runs={}, comparisons={}, methods={}, errors={},
        source_rank=rank, compact_width=budget, legendre_order=order,
        scope=dict(samples=8, queries=30, dimension=d, depth=2, activation='tanh',
            controls_matched_to='moving scalars, not moving plus fixed',
            logarithmic_query_contract='inputs available at setup; labels withheld',
            harmonic_query_contract='independent sphere geometry; scored inputs excluded',
            source_initialization='full-horizon disposable dense RK4 rollout, not init-only',
            accuracy_scope='sampled-time RMS on 30 queries; not a continuum or asymptotic certificate'))
    requested_methods = ['legendre', 'logarithmic']+(['harmonic'] if d in (2, 3) else [])
    report['methods'] = {name: dict(status='inconclusive', numerical_gate_pass=False,
                                    accuracy_pass=False) for name in requested_methods}
    arrays, models = {}, {}
    started_case = time.monotonic()

    def persist():
        save_json(args.out/'report.json', report)
        np.savez_compressed(args.out/'trajectories.npz', **arrays)

    def move(model, destination, dtype=torch.float32):
        for key in ('initial_state', 'metrics', 'metric_inverses'):
            if hasattr(model, key):
                setattr(model, key, [v.to(device=destination, dtype=dtype) for v in getattr(model, key)])
        for key in ('first', 'matrix', 'degrees', 'weights', 'kernel', 'cross', 'train_inputs', 'query_inputs'):
            if hasattr(model, key):
                setattr(model, key, getattr(model, key).to(device=destination, dtype=dtype))

    def register(name, model, setup_seconds=None, **extra):
        moving = sum(v.numel() for v in model.initial_state)
        diagnostics = dict(getattr(model, 'diagnostics', {}))
        if 'runtime_dtype' in diagnostics:
            diagnostics['assembly_dtype'] = diagnostics['runtime_dtype']
            diagnostics['runtime_dtype'] = 'torch.float32'
        report['models'][name] = dict(moving=moving, fixed=int(model.fixed_scalars),
            total=moving+int(model.fixed_scalars), setup_seconds=setup_seconds,
            setup_timing_scope='construction, excluding CPU staging; null means not timed',
            diagnostics=diagnostics, **extra)
        move(model, 'cpu')
        models[name] = model

    try:
        inputs, labels, queries, truth = validation_data(d, 8, 30, 47, device,
            'digits' if d == 64 else 'toy', 'test', d == 64, 0, (1, 7))
        if d == 64:
            indices = np.random.default_rng(48).permutation(len(queries))[:30]
            queries, truth = queries[indices], truth[indices]
        for key, value in dict(train_inputs=inputs, train_labels=labels,
                               query_inputs=queries, query_labels=truth).items():
            arrays[key] = value.cpu().numpy()
        report['data_sha256'] = {key: array_sha(value) for key, value in arrays.items()}
        report['common_data_words'] = inputs.numel()+labels.numel()+queries.numel()
        t0 = time.monotonic()
        dense = DeepDense(args.width, d, 2, 'tanh', 601, device)
        synchronize(device)
        dense_setup = time.monotonic()-t0
        initial_features = dense.fields(dense.initial_state, inputs)[0][-1]
        initial_gram = initial_features.T@initial_features/args.width
        floor = min(1e-4, float(torch.linalg.eigvalsh(initial_gram/len(labels))[0])/8)
        if floor <= 0:
            raise ArithmeticError('Initialization training Gram is not positive definite')
        report['readout_floor'] = floor
        t0 = time.monotonic()
        model = FrozenNTK(dense, inputs, queries)
        synchronize(device)
        register('ntk', model, time.monotonic()-t0)
        t0 = time.monotonic()
        model = LegendreCompression(dense, inputs, labels, order)
        synchronize(device)
        register('legendre', model, time.monotonic()-t0)
        for name in ['logarithmic']+(['harmonic'] if d in (2, 3) else []):
            print(json.dumps(dict(event='setup_start', method=name, width=args.width)), flush=True)
            t0 = time.monotonic()
            try:
                if name == 'logarithmic':
                    sources, source_info = deep_rollout_sources(dense, inputs, labels, queries,
                        args.horizon, rank, 601, seconds=args.per_run_seconds, step=.125)
                    source_info.update(scored_inputs_used=True, input_contract='declared_unlabeled_test_panel')
                else:
                    sources, source_info = unified_harmonic_sources(dense, inputs, labels,
                        args.horizon, rank, 601, seconds=args.per_run_seconds, step=.125)
                model = DeepHarmonic(dense, inputs, labels, sources, budget,
                    readout_floor=floor if name == 'logarithmic' else None)
                del sources
                synchronize(device)
                elapsed = time.monotonic()-t0
                if elapsed > args.per_run_seconds:
                    raise TimeoutError(f'Complete {name} setup took {elapsed:.1f}s')
                register(name, model, elapsed, source=source_info)
                print(json.dumps(dict(event='setup_done', method=name, seconds=elapsed)), flush=True)
            except Exception as error:
                report['errors'][name] = f'{type(error).__name__}: {error}'
                report['methods'][name]['error'] = report['errors'][name]
            persist()
        compression_names = [name for name in ('legendre', 'harmonic', 'logarithmic') if name in models]
        for name in compression_names:
            moving = report['models'][name]['moving']
            small_width = math.isqrt(moving+(d+1)**2//4)-(d+1)//2
            while small_width**2+(d+1)*small_width > moving:
                small_width -= 1
            while (small_width+1)**2+(d+1)*(small_width+1) <= moving:
                small_width += 1
            register('small_'+name, DeepDense(small_width, d, 2, 'tanh', 20601, device),
                     width=small_width, matched_moving_budget=moving)
            try:
                register('lowrank_'+name, BudgetLoRA(dense, moving, 30601), matched_moving_budget=moving)
            except ValueError as error:
                report['errors']['lowrank_'+name] = str(error)
        register('dense', dense, dense_setup)
        register('iid', DeepDense(args.width, d, 2, 'tanh', 10601, device))
        del initial_features
        inputs, labels, queries = [v.float() for v in (inputs, labels, queries)]
        sequence = ['dense', 'iid']+compression_names+['ntk']
        sequence += [name for method in compression_names for name in ('small_'+method, 'lowrank_'+method)
                     if name in models]
        for name in sequence:
            model = models.pop(name)
            move(model, device)
            for suffix, step in ([('_coarse', 2*args.step), ('', args.step)]
                                 if name in ['dense']+compression_names else [('', args.step)]):
                key = name+suffix
                print(json.dumps(dict(event='run_start', model=key, width=args.width)), flush=True)
                try:
                    state, prediction, info = integrate_euler(model, inputs, labels, queries, step,
                        args.per_run_seconds, horizon=args.horizon,
                        max_steps=math.ceil(args.horizon/step), observation_every=round(.5/step))
                    report['runs'][key] = info
                    arrays[key] = prediction
                    arrays['times_'+key] = np.asarray(info['times'])
                    if info['complete'] and not suffix:
                        if name == 'dense':
                            features = model.fields(state, inputs)[0][-1].double()
                            gram = features.T@features/args.width
                            report['dense_feature_gram_relative_motion'] = float((gram-initial_gram).norm()/initial_gram.norm())
                            arrays['times'] = np.asarray(info['times'])
                        if name == 'legendre':
                            info['lift_drift'] = model.lift_diagnostics(state, inputs, labels)
                        if name == 'logarithmic':
                            info['training_constraint_max_abs'] = float((model.predict(state, inputs, inputs, labels)
                                                                         -labels+state[-1]).abs().max())
                    del state
                    print(json.dumps(dict(event='run_done', model=key, seconds=info['seconds'],
                        mse=info['final_training_mse'], complete=info['complete'])), flush=True)
                except Exception as error:
                    report['errors'][key] = f'{type(error).__name__}: {error}'
                    print(json.dumps(dict(event='run_error', model=key, error=report['errors'][key])), flush=True)
                persist()
            move(model, 'cpu')
            del model
        reference = arrays.get('dense')
        if reference is None or not report['runs'].get('dense', {}).get('complete'):
            raise RuntimeError('No complete dense reference; comparisons inconclusive')
        times = arrays['times']
        for name in sequence:
            if (not report['runs'].get(name, {}).get('complete') or arrays[name].shape != reference.shape
                    or not np.allclose(arrays['times_'+name], times, atol=1e-10, rtol=0)):
                continue
            error = arrays[name].astype(float)-reference.astype(float)
            curve = np.sqrt(np.mean(error**2, axis=1))
            report['comparisons'][name] = dict(max_time_rms=float(curve.max()), endpoint_rms=float(curve[-1]),
                mean_time_rms=float(np.trapz(curve, times)/args.horizon),
                test_mse=float(np.mean((arrays[name][-1]-arrays['query_labels'])**2)))
        variability = report['comparisons'].get('iid', {}).get('max_time_rms', 0.)
        if variability <= 1e-12:
            raise ArithmeticError('Missing or degenerate iid-dense benchmark')
        for value in report['comparisons'].values():
            value['ratio_to_dense_pair'] = value['max_time_rms']/variability
        for name in compression_names:
            moving, total = (report['models'][name][key] for key in ('moving', 'total'))
            result = dict(learned_reduction=report['models']['dense']['moving']/moving,
                storage_reduction=report['models']['dense']['total']/total,
                numerical_gate_pass=False, accuracy_pass=False, status='inconclusive')
            pairs = [(key, key+'_coarse') for key in ('dense', name)]
            if (name in report['comparisons'] and all(
                    report['runs'].get(b, {}).get('complete') and arrays[a].shape == arrays[b].shape
                    and np.allclose(arrays['times_'+a], arrays['times_'+b], atol=1e-10, rtol=0)
                    for a, b in pairs)):
                refinement = sum(trajectory_rms(arrays[a].astype(float), arrays[b].astype(float))['max_time_rms']
                                 for a, b in pairs)
                result.update(refinement_sum=refinement, numerical_threshold=.1*variability,
                    numerical_gate_pass=refinement < .1*variability,
                    accuracy_pass=report['comparisons'][name]['max_time_rms'] <= 3*variability)
                for control, field in [('small_', 'beats_small'), ('lowrank_', 'beats_lowrank')]:
                    result[field] = (report['comparisons'][name]['max_time_rms'] <
                        report['comparisons'][control+name]['max_time_rms']) if control+name in report['comparisons'] else None
                if result['numerical_gate_pass']:
                    result['status'] = 'pass' if result['accuracy_pass'] else 'fail'
            report['methods'][name] = result
        report['complete'] = True
        print(json.dumps(dict(methods=report['methods'], comparisons=report['comparisons'])), flush=True)
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        report['seconds'] = time.monotonic()-started_case
        persist()


@torch.no_grad()
def cubic_case_main(argv):
    """Paired geometric/flaring source comparison; identical autonomous runtime."""
    parser = argparse.ArgumentParser(description=cubic_case_main.__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--dataset', choices=('sphere2', 'sphere3', 'digits17'), required=True)
    parser.add_argument('--seed', type=int, default=601)
    parser.add_argument('--device', default='cuda:0')
    args = parser.parse_args(argv)
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device, width, horizon, step = torch.device(args.device), 4096, 32., .0015625
    d = int(args.dataset[6:]) if args.dataset.startswith('sphere') else 64
    names = ('old_full', 'new_full', 'old_small', 'new_small')
    report = dict(config={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
        device=torch.cuda.get_device_name(device) if device.type == 'cuda' else 'CPU',
        complete=False, models={}, runs={}, comparisons={}, methods={}, paired_comparisons={}, errors={},
        scope=dict(width=width, samples=8, queries=30, dimension=d, depth=2, activation='tanh',
            horizon=horizon, fine_step=step, coarse_step=2*step, observation_spacing=.5,
            source_initialization='shared full-horizon RK4 rollout; not initialization-only',
            new_rule='empirical residual-adapted flaring; not certified constants',
            input_contract='all 38 inputs available at setup; test labels withheld',
            accuracy_scope='finite recorded times and panel; not an asymptotic/continuum certificate'))
    arrays, models, started = {}, {}, time.monotonic()

    def persist():
        save_json(args.out/'report.json', report)
        np.savez_compressed(args.out/'trajectories.npz', **arrays)

    def move(model, destination):
        for key in ('initial_state', 'metrics', 'metric_inverses'):
            if hasattr(model, key):
                setattr(model, key, [v.to(device=destination, dtype=torch.float32)
                                    for v in getattr(model, key)])

    def register(name, model, elapsed, **extra):
        moving = sum(v.numel() for v in model.initial_state)
        report['models'][name] = dict(moving=moving, fixed=int(model.fixed_scalars),
            total=moving+int(model.fixed_scalars), assembly_seconds=elapsed,
            diagnostics=getattr(model, 'diagnostics', {}),
            diagnostics_scope='float64 assembly, before deployment cast',
            runtime_dtype='torch.float32', **extra)
        move(model, 'cpu')
        models[name] = model

    try:
        inputs, labels, queries, truth = validation_data(d, 8, 30, 47, device,
            'digits' if d == 64 else 'toy', 'test', d == 64, 0, (1, 7))
        if d == 64:
            indices = np.random.default_rng(48).permutation(len(queries))[:30]
            queries, truth = queries[indices], truth[indices]
        for key, value in dict(train_inputs=inputs, train_labels=labels,
                               query_inputs=queries, query_labels=truth).items():
            arrays[key] = value.cpu().numpy()
        report['data_sha256'] = {key: array_sha(value) for key, value in arrays.items()}
        report['common_data_words'] = inputs.numel()+labels.numel()+queries.numel()
        t0 = time.monotonic()
        dense = DeepDense(width, d, 2, 'tanh', args.seed, device)
        synchronize(device)
        dense_setup = time.monotonic()-t0
        features = dense.fields(dense.initial_state, inputs)[0][-1]
        gap = float(torch.linalg.eigvalsh(features.T@features/(width*len(labels)))[0])
        floor = min(1e-4, gap/8)
        if floor <= 0:
            raise ArithmeticError('Nonpositive initialized training Gram gap')
        report['readout_floor'] = floor
        del features
        print(json.dumps(dict(event='paired_source_start', dataset=args.dataset, seed=args.seed)), flush=True)
        source_started = time.monotonic()
        sources, report['sources'] = cubic_rollout_sources(dense, inputs, labels, queries,
                                                          horizon=horizon, seconds=120., seed=501)
        print(json.dumps(dict(event='paired_source_done', seconds=report['sources']['total_setup_seconds'])), flush=True)
        for name in names:
            partition, size = name.split('_')
            rank = 12 if size == 'full' else 6
            budget = 4*(max(d+9, 17)+3*rank)
            t0 = time.monotonic()
            try:
                model = DeepHarmonic(dense, inputs, labels, sources[partition][rank], budget,
                                     selection_seed=501, readout_floor=floor)
                if (model.diagnostics['branch'] == 'full_retention_uncompressed'
                        or any(v['truncated'] for v in model.diagnostics.get('source_truncations', []))):
                    raise ArithmeticError('Full retention or additional source truncation invalidates pairing')
                synchronize(device)
                elapsed = time.monotonic()-t0
                if time.monotonic()-source_started > 120:
                    raise TimeoutError('Paired source construction plus compact assembly exceeded 120 seconds')
                register(name, model, elapsed, source_rank=rank, compact_width=budget)
                print(json.dumps(dict(event='assembly_done', model=name, seconds=elapsed)), flush=True)
            except Exception as error:
                report['errors'][name] = f'{type(error).__name__}: {error}'
                report['methods'][name] = dict(status='inconclusive', error=report['errors'][name])
            persist()
        del sources
        register('dense', dense, dense_setup)
        t0 = time.monotonic()
        iid = DeepDense(width, d, 2, 'tanh', args.seed+10000, device)
        synchronize(device)
        register('iid', iid, time.monotonic()-t0)
        inputs, labels = inputs.float(), labels.float()
        panel = torch.cat((inputs, queries.float()))
        for name in ('dense', 'iid')+names:
            if name not in models:
                continue
            model = models.pop(name)
            move(model, device)
            for suffix, current_step in ([('', step)] if name == 'iid'
                                         else [('_coarse', 2*step), ('', step)]):
                key = name+suffix
                print(json.dumps(dict(event='run_start', model=key)), flush=True)
                try:
                    state, prediction, info = integrate_euler(model, inputs, labels, panel,
                        current_step, 120., horizon=horizon,
                        max_steps=round(horizon/current_step), observation_every=round(.5/current_step))
                    arrays[key], arrays['times_'+key] = prediction, np.asarray(info['times'])
                    report['runs'][key] = info
                    if getattr(model, 'readout_floor', None) is not None:
                        info['floor_active_at_observations'] = sum(v < floor for v in info['observed_feature_gram_minima'])
                        info['terminal_readout_constraint_max_abs'] = float(
                            (model.predict(state, inputs, inputs, labels)-labels+state[-1]).abs().max())
                    del state
                    print(json.dumps(dict(event='run_done', model=key, seconds=info['seconds'],
                        mse=info['final_training_mse'], complete=info['complete'])), flush=True)
                except Exception as error:
                    report['errors'][key] = f'{type(error).__name__}: {error}'
                    print(json.dumps(dict(event='run_error', model=key, error=report['errors'][key])), flush=True)
                persist()
            move(model, 'cpu')
            del model

        def aligned(name):
            return (report['runs'].get(name, {}).get('complete') and name in arrays
                and arrays[name].shape == arrays['dense'].shape
                and np.allclose(arrays['times_'+name], arrays['times_dense'], atol=1e-10, rtol=0))

        if not report['runs'].get('dense', {}).get('complete'):
            raise RuntimeError('No complete dense reference; comparisons inconclusive')
        for name in ('dense', 'iid')+names:
            if not aligned(name):
                continue
            value = trajectory_rms(arrays[name][:, 8:].astype(float), arrays['dense'][:, 8:].astype(float))
            value.pop('curve', None)
            value.update(full_panel_max_abs=float(np.max(np.abs(arrays[name].astype(float)-arrays['dense']))),
                test_mse=float(np.mean((arrays[name][-1, 8:]-arrays['query_labels'])**2)),
                training_mse_from_predictions=float(np.mean((arrays[name][-1, :8]-arrays['train_labels'])**2)))
            if aligned(name+'_coarse'):
                value['refinement_rms'] = trajectory_rms(arrays[name][:, 8:].astype(float),
                    arrays[name+'_coarse'][:, 8:].astype(float))['max_time_rms']
                value['full_panel_refinement_max_abs'] = float(np.max(np.abs(
                    arrays[name].astype(float)-arrays[name+'_coarse'])))
            report['comparisons'][name] = value
        variability = report['comparisons'].get('iid', {}).get('max_time_rms', 0.)
        if variability <= 1e-12:
            raise ArithmeticError('No nondegenerate iid-dense benchmark')
        dense_refinement = report['comparisons']['dense'].get('refinement_rms')
        for name, value in report['comparisons'].items():
            value['ratio_to_dense_pair'] = value['max_time_rms']/variability
            for field in ('endpoint_rms', 'full_panel_max_abs'):
                denominator = report['comparisons']['iid'][field]
                value[field+'_ratio_to_dense_pair'] = value[field]/denominator if denominator > 0 else None
            value['fitted_below_001'] = value['training_mse_from_predictions'] < .01
            if name not in names:
                continue
            result = dict(status='inconclusive', accuracy_pass=value['ratio_to_dense_pair'] <= 3,
                numerical_gate_pass=False,
                learned_reduction=report['models']['dense']['moving']/report['models'][name]['moving'],
                storage_reduction=report['models']['dense']['total']/report['models'][name]['total'])
            if dense_refinement is not None and 'refinement_rms' in value:
                refinement = dense_refinement+value['refinement_rms']
                result.update(refinement_sum=refinement, numerical_threshold=.1*variability,
                              numerical_gate_pass=refinement < .1*variability)
                if result['numerical_gate_pass']:
                    result['status'] = 'pass' if result['accuracy_pass'] else 'fail'
            report['methods'][name] = result
        for size in ('full', 'small'):
            old, new = ('old_'+size, 'new_'+size)
            comparison = dict(verdict='inconclusive')
            if all(report['methods'].get(name, {}).get('numerical_gate_pass') for name in (old, new)):
                a, b = (report['comparisons'][name] for name in (old, new))
                uncertainty = 2*(a['refinement_rms']+b['refinement_rms'])
                difference = a['max_time_rms']-b['max_time_rms']
                better = b['max_time_rms'] <= .8*a['max_time_rms'] and difference > uncertainty
                worse = b['max_time_rms'] >= 1.25*a['max_time_rms'] and -difference > uncertainty
                comparison.update(verdict='better' if better else 'worse' if worse else 'similar_observed_accuracy',
                    new_over_old=b['max_time_rms']/a['max_time_rms'], uncertainty=uncertainty)
            report['paired_comparisons'][size] = comparison
        report['smaller_budget_efficiency_signal'] = (
            report['methods'].get('new_small', {}).get('status') == 'pass'
            and report['methods'].get('old_small', {}).get('status') == 'fail'
            and report['methods'].get('old_full', {}).get('status') == 'pass')
        report['complete'] = True
        print(json.dumps(dict(comparisons=report['comparisons'], paired=report['paired_comparisons'])), flush=True)
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        report['seconds'] = time.monotonic()-started
        persist()


@torch.no_grad()
def cubic_budget_main(argv):
    """Requested low-dimensional sphere fits at approximately 2x/4x retained storage."""
    from concurrent.futures import ThreadPoolExecutor
    parser = argparse.ArgumentParser(description=cubic_budget_main.__doc__)
    parser.add_argument('--reference', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--devices', nargs=2, default=['cuda:0', 'cuda:1'])
    parser.add_argument('--partition', choices=('old', 'new'), default='old')
    parser.add_argument('--factors', type=int, nargs='+', choices=(2, 4), default=[2, 4])
    parser.add_argument('--selection-trials', type=int, default=4)
    args = parser.parse_args(argv)
    if len(args.factors) != len(set(args.factors)):
        parser.error('Storage factors must be distinct')
    if args.selection_trials < 1:
        parser.error('Need a positive coordinate-selection trial count')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    baseline = json.loads((args.reference/'report.json').read_text())
    with np.load(args.reference/'trajectories.npz') as saved:
        reference = {key: saved[key] for key in saved.files}
    assert baseline['config']['dataset'] in ('sphere2', 'sphere3') and baseline['config']['seed'] == 601
    dimension = baseline['scope']['dimension']
    assert dimension in (2, 3) and baseline['config']['dataset'] == f'sphere{dimension}'
    for name, digest in baseline['data_sha256'].items():
        assert array_sha(reference[name]) == digest
    report = dict(source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        reference=str(args.reference), reference_arrays_sha256=sha((args.reference/'trajectories.npz').read_bytes()),
        reference_report_sha256=sha((args.reference/'report.json').read_bytes()),
        python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
        scope=baseline['scope'], source_partition=args.partition, requested_factors=args.factors,
        selection_trials=args.selection_trials,
        complete=False, models={}, runs={}, errors={},
        numerical_qualification='same previously refined Euler step; no new-budget refinement runs',
        source_rank_qualification='nested ranks19/29 from one rank37 SVD; not nested with original rank20 SVD')
    arrays = {name: reference[name] for name in ('train_inputs', 'train_labels', 'query_inputs', 'query_labels')}
    started = time.monotonic()
    try:
        device = torch.device(args.devices[0])
        inputs, labels, queries = [torch.as_tensor(reference[name], device=device)
                                  for name in ('train_inputs', 'train_labels', 'query_inputs')]
        dense = DeepDense(4096, dimension, 2, 'tanh', 601, device)
        sources, report['sources'] = cubic_rollout_sources(dense, inputs, labels, queries,
            ranks=(29, 19), partitions=(args.partition,))
        np.testing.assert_allclose(report['sources']['observation_times'],
            baseline['sources']['observation_times'], atol=1e-12, rtol=0)
        models = []
        for factor, width, rank in ((2, 300, 19), (4, 424, 29)):
            if factor not in args.factors:
                continue
            t0 = time.monotonic()
            model = DeepHarmonic(dense, inputs, labels, sources[args.partition][rank], width,
                                 selection_seed=501, readout_floor=baseline['readout_floor'],
                                 selection_trials=args.selection_trials)
            assert model.diagnostics['widths'] == [width, width]
            assert not any(v['truncated'] for v in model.diagnostics['source_truncations'])
            assert all(v.shape[1] == rank for family in sources[args.partition][rank].values() for v in family)
            moving = sum(v.numel() for v in model.initial_state)
            total = moving+model.fixed_scalars
            assert total == 4*width**2+(dimension+1)*width+9
            report['models'][str(factor)] = dict(compact_width=width, source_rank=rank,
                moving=moving, fixed=model.fixed_scalars, total=total,
                storage_multiple=total/baseline['models']['old_full']['total'],
                assembly_seconds=time.monotonic()-t0, diagnostics=model.diagnostics,
                diagnostics_scope='float64 assembly; runtime float32')
            for key in ('initial_state', 'metrics', 'metric_inverses'):
                setattr(model, key, [v.to(device='cpu', dtype=torch.float32) for v in getattr(model, key)])
            models.append((factor, model))
        del dense, sources, inputs, labels, queries
        report['setup_seconds'] = time.monotonic()-started
        save_json(args.out/'report.json', report)

        def run(item, device_name):
            factor, model = item
            device = torch.device(device_name)
            for key in ('initial_state', 'metrics', 'metric_inverses'):
                setattr(model, key, [v.to(device) for v in getattr(model, key)])
            inputs, labels, queries = [torch.as_tensor(reference[name], device=device, dtype=torch.float32)
                                      for name in ('train_inputs', 'train_labels', 'query_inputs')]
            print(json.dumps(dict(event='budget_run_start', storage_factor=factor, device=device_name)), flush=True)
            state, prediction, info = integrate_euler(model, inputs, labels, torch.cat((inputs, queries)),
                .0015625, 120., horizon=32., max_steps=20480, observation_every=320)
            info['device'] = torch.cuda.get_device_name(device)
            info['floor_active_at_observations'] = sum(
                v < baseline['readout_floor'] for v in info['observed_feature_gram_minima'])
            if info['complete']:
                np.testing.assert_allclose(info['times'], reference['times_dense'], atol=1e-10, rtol=0)
                np.testing.assert_allclose(np.mean((prediction[:, :8].astype(float)-reference['train_labels'])**2, axis=1),
                                           info['losses'], atol=1e-6, rtol=2e-5)
                error = trajectory_rms(prediction[:, 8:].astype(float), reference['dense'][:, 8:].astype(float))
                error.pop('curve')
                error['endpoint_over_previous'] = error['endpoint_rms']/baseline['comparisons'][args.partition+'_full']['endpoint_rms']
                error['endpoint_over_dense_pair'] = error['endpoint_rms']/baseline['comparisons']['iid']['endpoint_rms']
                info['comparison'] = error
            del state
            print(json.dumps(dict(event='budget_run_done', storage_factor=factor, info=info.get('comparison'),
                                  seconds=info['seconds'], complete=info['complete'])), flush=True)
            return factor, prediction, info

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [(item[0], pool.submit(run, item, args.devices[int(item[0] == 4)])) for item in models]
            for factor, future in futures:
                try:
                    _, prediction, info = future.result()
                    arrays['budget_'+str(factor)] = prediction
                    arrays['times_'+str(factor)] = np.asarray(info['times'])
                    report['runs'][str(factor)] = info
                except Exception as error:
                    report['errors'][str(factor)] = f'{type(error).__name__}: {error}'
        report['complete'] = (len(report['runs']) == len(args.factors)
                              and all(v['complete'] for v in report['runs'].values()))
    except Exception as error:
        report['errors']['setup'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        report['seconds'] = time.monotonic()-started
        save_json(args.out/'report.json', report)
        np.savez_compressed(args.out/'trajectories.npz', **arrays)
    return 0 if report['complete'] else 1


@torch.no_grad()
def sphere_points_main(argv):
    """Bounded sphere3 additions, reusing the saved dense and Logarithmic runs."""
    from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
    parser = argparse.ArgumentParser(description=sphere_points_main.__doc__)
    parser.add_argument('--reference', type=Path, required=True)
    parser.add_argument('--logarithmic', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--devices', nargs=2, default=['cuda:0', 'cuda:1'])
    parser.add_argument('--tradeoff', action='store_true', help='Three dense sizes, Legendre orders, and Logarithmic budgets')
    parser.add_argument('--seed-check', action='store_true', help='Two more width-1446 dense seeds and one NTK fit')
    parser.add_argument('--harmonic-curve', action='store_true', help='Three smaller Harmonic budgets')
    parser.add_argument('--compression-larger', action='store_true',
                        help='Two larger learned-state budgets each for Harmonic and Logarithmic')
    parser.add_argument('--lowrank-curve', action='store_true', help='Width-4096 low-rank adapters at ranks 1, 4, 8, 20')
    parser.add_argument('--lowrank-legendre', action='store_true', help='Match Legendre ranks: reuse rank8, add ranks16/24/96')
    parser.add_argument('--dense-smaller', action='store_true', help='Two dense sizes within half/quarter of width1446 parameter count')
    parser.add_argument('--smallest-seed-check', action='store_true', help='Two more seeds for the width722 dense point')
    parser.add_argument('--dense-width', type=int, help='Add three dense seeds at one specified width')
    parser.add_argument('--dense-extra-seeds', type=int, nargs='+',
                        help='Add seeds10602/10603 at existing single-seed dense widths')
    parser.add_argument('--reference-seeds', action='store_true',
                        help='Only two new width4096 references, seeds602/603; reuse all other trajectories')
    parser.add_argument('--previous-points', type=Path, help='Previously measured Legendre/Harmonic points')
    args = parser.parse_args(argv)
    continuations = (args.tradeoff, args.seed_check, args.harmonic_curve, args.lowrank_curve,
                     args.lowrank_legendre, args.dense_smaller, args.smallest_seed_check,
                     args.dense_width is not None, args.dense_extra_seeds is not None,
                     args.compression_larger, args.reference_seeds)
    if sum(continuations) > 1:
        parser.error('Choose only one continuation mode')
    if any(continuations) and args.previous_points is None:
        parser.error('The requested continuation requires --previous-points')
    if args.dense_width is not None and not 1 <= args.dense_width <= 4096:
        parser.error('--dense-width must be between 1 and 4096')
    if args.dense_extra_seeds is not None and (len(set(args.dense_extra_seeds)) != len(args.dense_extra_seeds)
            or any(not 1 <= width < 4096 for width in args.dense_extra_seeds)):
        parser.error('--dense-extra-seeds requires distinct widths between 1 and 4095')
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    baseline = json.loads((args.reference/'report.json').read_text())
    logarithmic = json.loads((args.logarithmic/'report.json').read_text())
    with np.load(args.reference/'trajectories.npz') as saved:
        reference = {key: saved[key] for key in saved.files}
    assert baseline['config']['dataset'] == 'sphere3' and baseline['config']['seed'] == 601
    assert baseline['scope']['width'] == 4096 and baseline['scope']['samples'] == 8
    assert baseline['scope']['queries'] == 30 and baseline['scope']['depth'] == 2
    assert baseline['scope']['activation'] == 'tanh' and baseline['scope']['horizon'] == 32.
    assert baseline['scope']['fine_step'] == .0015625
    for name, digest in baseline['data_sha256'].items():
        assert array_sha(reference[name]) == digest
    assert logarithmic['complete'] and logarithmic['source_partition'] == 'new'
    assert logarithmic['reference_arrays_sha256'] == sha((args.reference/'trajectories.npz').read_bytes())
    benchmark = trajectory_rms(reference['iid'][:, 8:].astype(float),
                               reference['dense'][:, 8:].astype(float))['endpoint_rms']
    assert benchmark > 0
    report = dict(source_sha256=sha(Path(__file__).read_bytes()), command=sys.argv,
        python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
        reference=str(args.reference), logarithmic=str(args.logarithmic),
        reference_arrays_sha256=sha((args.reference/'trajectories.npz').read_bytes()),
        logarithmic_report_sha256=sha((args.logarithmic/'report.json').read_bytes()),
        scope={key: baseline['scope'][key] for key in ('width', 'samples', 'queries', 'dimension', 'depth',
            'activation', 'horizon', 'fine_step', 'observation_spacing', 'accuracy_scope')},
        tradeoff=args.tradeoff, seed_check=args.seed_check, harmonic_curve=args.harmonic_curve,
        compression_larger=args.compression_larger,
        lowrank_curve=args.lowrank_curve,
        lowrank_legendre=args.lowrank_legendre,
        dense_smaller=args.dense_smaller,
        smallest_seed_check=args.smallest_seed_check,
        dense_width=args.dense_width,
        dense_extra_seeds=args.dense_extra_seeds,
        reference_seeds=args.reference_seeds,
        dense_pair_endpoint_rms=benchmark,
        numerical_qualification='finite Euler comparison; no new order/budget-specific refinement',
        complete=False, models={}, runs={}, errors={}, points={})
    arrays = {name: reference[name] for name in ('train_inputs', 'train_labels', 'query_inputs', 'query_labels')}
    if args.previous_points is not None:
        previous = json.loads((args.previous_points/'report.json').read_text())
        assert previous['complete'] and previous['reference_arrays_sha256'] == report['reference_arrays_sha256']
        report['previous_points'] = str(args.previous_points)
        report['previous_report_sha256'] = sha((args.previous_points/'report.json').read_bytes())
        report['previous_arrays_sha256'] = sha((args.previous_points/'trajectories.npz').read_bytes())
        report['points'].update(previous['points'])
        if 'dense_seed_summary' in previous:
            report['dense_seed_summary'] = previous['dense_seed_summary']
        if 'dense_seed_summaries' in previous:
            report['dense_seed_summaries'] = previous['dense_seed_summaries']
        if 'lowrank_legendre_orders' in previous:
            report['lowrank_legendre_orders'] = previous['lowrank_legendre_orders']
    extra_seed_bases = {}
    if args.dense_extra_seeds is not None:
        prior_models, ancestor, seen = {}, previous, set()
        while True:
            prior_models.update(ancestor['models'])
            if not ancestor.get('previous_points'):
                break
            path = Path(ancestor['previous_points'])
            assert str(path.resolve()) not in seen
            seen.add(str(path.resolve()))
            assert sha((path/'report.json').read_bytes()) == ancestor['previous_report_sha256']
            ancestor = json.loads((path/'report.json').read_text())
        for width in args.dense_extra_seeds:
            matches = [name for name, point in report['points'].items()
                       if name.split('_')[0] == 'dense' and point['moving'] == width**2+4*width]
            assert len(matches) == 1, f'Expected one existing seed at width{width}'
            name = matches[0]
            assert prior_models[name]['width'] == width and prior_models[name]['seed'] == 10601
            extra_seed_bases[width] = name
    if args.lowrank_legendre:
        assert previous['models']['lowrank_8']['rank'] == 8
        assert previous['models']['lowrank_8']['seed'] == 30601
        report['lowrank_legendre_orders'] = {f'lowrank_{8*order}': order for order in (1, 2, 3, 12)}
    started = time.monotonic()

    def move(model, destination):
        for key in ('initial_state', 'metrics', 'metric_inverses'):
            if hasattr(model, key):
                setattr(model, key, [v.to(device=destination, dtype=torch.float32) for v in getattr(model, key)])
        for key in ('first', 'matrix', 'degrees', 'weights'):
            if hasattr(model, key):
                setattr(model, key, getattr(model, key).to(device=destination, dtype=torch.float32))
        for key in ('kernel', 'cross', 'train_inputs', 'query_inputs'):
            if hasattr(model, key):
                setattr(model, key, getattr(model, key).to(device=destination, dtype=torch.float32))

    def persist():
        report['seconds'] = time.monotonic()-started
        save_json(args.out/'report.json', report)
        np.savez_compressed(args.out/'trajectories.npz', **arrays)

    def run(name, model, device_name):
        device = torch.device(device_name)
        move(model, device)
        inputs, labels, queries = [torch.as_tensor(reference[key], device=device, dtype=torch.float32)
                                  for key in ('train_inputs', 'train_labels', 'query_inputs')]
        print(json.dumps(dict(event='point_run_start', method=name, device=device_name)), flush=True)
        state, prediction, info = integrate_euler(model, inputs, labels, torch.cat((inputs, queries)),
            .0015625, 120., horizon=32., max_steps=20480, observation_every=320)
        info['device'] = torch.cuda.get_device_name(device)
        if info['complete']:
            assert prediction.shape == (65, 38) and np.isfinite(prediction).all()
            np.testing.assert_allclose(info['times'], reference['times_dense'], atol=1e-10, rtol=0)
            np.testing.assert_allclose(np.mean((prediction[:, :8].astype(float)-reference['train_labels'])**2, axis=1),
                                       info['losses'], atol=1e-6, rtol=2e-5)
            error = trajectory_rms(prediction[:, 8:].astype(float), reference['dense'][:, 8:].astype(float))
            error.pop('curve')
            error['endpoint_over_dense_pair'] = error['endpoint_rms']/benchmark
            info['comparison'] = error
            if isinstance(model, LegendreCompression):
                info['lift_drift'] = model.lift_diagnostics(state, inputs, labels)
        print(json.dumps(dict(event='point_run_done', method=name, seconds=info['seconds'],
            complete=info['complete'], comparison=info.get('comparison'))), flush=True)
        return prediction, info

    try:
        device = torch.device(args.devices[0])
        inputs, labels = [torch.as_tensor(reference[key], device=device) for key in ('train_inputs', 'train_labels')]
        dense = DeepDense(4096, 3, 2, 'tanh', 601, device)
        models = {}
        if args.reference_seeds:
            specs = [dict(name=f'dense_reference{seed}', family='dense', width=4096, seed=seed)
                     for seed in (602, 603)]
            assert all(spec['name'] not in report['points'] for spec in specs)
            report['independent_references'] = {str(spec['seed']): spec['name'] for spec in specs}
        elif args.compression_larger:
            assert report['points']['harmonic']['moving'] == report['points']['logarithmic']['moving'] == 181480
            specs = []
            for factor in (2, 4):
                target = factor*181480
                width = math.isqrt(target-4)-2
                assert width**2+4*width+8 <= target < (width+1)**2+4*(width+1)+8
                rank = math.floor((width/4-17)/3)
                specs += [dict(name=f'{family}_n{width}', family=family, width=width, rank=rank,
                               target_moving_budget=target) for family in ('harmonic', 'logarithmic')]
            assert all(spec['name'] not in report['points'] for spec in specs)
            ranks = sorted({spec['rank'] for spec in specs}, reverse=True)
            try:
                harmonic_sources, report['harmonic_sources'] = unified_harmonic_sources(
                    dense, inputs, labels, 32., ranks[0], 601)
                assert all(v.shape == (4096, ranks[0]) for values in harmonic_sources.values() for v in values)
            except Exception as error:
                harmonic_sources = None
                report['errors']['harmonic_source_setup'] = f'{type(error).__name__}: {error}'
            try:
                queries = torch.as_tensor(reference['query_inputs'], device=device)
                log_sources, report['logarithmic_sources'] = cubic_rollout_sources(
                    dense, inputs, labels, queries, ranks=tuple(ranks), partitions=('new',))
                np.testing.assert_allclose(report['logarithmic_sources']['observation_times'],
                    baseline['sources']['observation_times'], atol=1e-12, rtol=0)
                del queries
            except Exception as error:
                log_sources = None
                report['errors']['logarithmic_source_setup'] = f'{type(error).__name__}: {error}'
        elif args.dense_extra_seeds is not None:
            specs = [dict(name=f'dense_n{width}_seed{seed}', family='dense', width=width, seed=seed)
                     for width in args.dense_extra_seeds for seed in (10602, 10603)]
            assert all(spec['name'] not in report['points'] for spec in specs)
        elif args.dense_width is not None:
            specs = [dict(name=f'dense_n{args.dense_width}_seed{seed}', family='dense',
                          width=args.dense_width, seed=seed) for seed in (10601, 10602, 10603)]
            assert all(spec['name'] not in report['points'] for spec in specs)
        elif args.smallest_seed_check:
            assert previous['models']['dense_32']['width'] == 722
            assert previous['models']['dense_32']['seed'] == 10601
            specs = [dict(name=f'dense_n722_seed{seed}', family='dense', width=722, seed=seed)
                     for seed in (10602, 10603)]
        elif args.dense_smaller:
            budget = previous['points']['dense_8']['moving']
            assert budget == 1446**2+4*1446
            assert min(v['moving'] for name, v in previous['points'].items()
                       if name.split('_')[0] == 'dense') == budget
            specs = [dict(name=f'dense_{8*divisor}', family='dense', seed=10601,
                          width=math.isqrt(budget//divisor+4)-2, divisor=8*divisor,
                          target_moving_budget=budget//divisor) for divisor in (2, 4)]
            for spec in specs:
                width, target = spec['width'], spec['target_moving_budget']
                assert width**2+4*width <= target < (width+1)**2+4*(width+1)
        elif args.lowrank_legendre:
            specs = [dict(name=f'lowrank_{rank}', family='lowrank', rank=rank) for rank in (16, 24, 96)]
        elif args.lowrank_curve:
            specs = [dict(name=f'lowrank_{rank}', family='lowrank', rank=rank) for rank in (1, 4, 8, 20)]
        elif args.harmonic_curve:
            specs = [dict(name=f'harmonic_{divisor}', family='harmonic', width=width, rank=rank)
                     for divisor, width, rank in ((2, 299, 19), (4, 210, 11), (8, 148, 6))]
            try:
                harmonic_sources, report['harmonic_sources'] = unified_harmonic_sources(
                    dense, inputs, labels, 32., 29, 601)
                assert all(v.shape == (4096, 29) for family in harmonic_sources.values() for v in family)
            except Exception as error:
                harmonic_sources = None
                report['errors']['harmonic_source_setup'] = f'{type(error).__name__}: {error}'
        elif args.seed_check:
            assert previous['models']['dense_8']['width'] == 1446
            assert previous['models']['dense_8']['seed'] == 10601
            specs = [dict(name=f'dense_seed{seed}', family='dense', width=1446, seed=seed)
                     for seed in (10602, 10603)]
            specs.append(dict(name='ntk', family='ntk'))
        elif args.tradeoff:
            specs = [dict(name=f'dense_{divisor}', family='dense', divisor=divisor,
                          width=math.isqrt(16793600//divisor+4)-2) for divisor in (2, 4, 8)]
            specs += [dict(name=f'legendre_{order}', family='legendre', order=order) for order in (1, 2, 3)]
            for divisor in (2, 4, 8):
                width = math.isqrt(181480//divisor-4)-2
                specs.append(dict(name=f'logarithmic_{divisor}', family='logarithmic', divisor=divisor,
                                  width=width, rank=math.floor((width/4-17)/3)))
            try:
                queries = torch.as_tensor(reference['query_inputs'], device=device)
                log_sources, report['logarithmic_sources'] = cubic_rollout_sources(dense, inputs, labels,
                    queries, ranks=(29, 19, 11, 6), partitions=('new',))
                np.testing.assert_allclose(report['logarithmic_sources']['observation_times'],
                    baseline['sources']['observation_times'], atol=1e-12, rtol=0)
                del queries
            except Exception as error:
                log_sources = None
                report['errors']['logarithmic_source_setup'] = f'{type(error).__name__}: {error}'
        else:
            specs = [dict(name='legendre', family='legendre', order=12),
                     dict(name='harmonic', family='harmonic', width=424, rank=29)]
        report['requested_models'] = specs
        for spec in specs:
            name, family = spec['name'], spec['family']
            t0 = time.monotonic()
            try:
                if family == 'dense':
                    model = DeepDense(spec['width'], 3, 2, 'tanh', spec.get('seed', 10601), device)
                    extra = dict(width=spec['width'], seed=spec.get('seed', 10601), divisor=spec.get('divisor'))
                    expected = (spec['width']**2+4*spec['width'], 0)
                elif family == 'ntk':
                    queries = torch.as_tensor(reference['query_inputs'], device=device)
                    model = FrozenNTK(dense, inputs, queries)
                    extra = dict(diagnostics=model.diagnostics, data_scalars=model.data_scalars,
                                 source_contract='initial dense kernel on the declared panel; no rollout')
                    expected = (8, 304)
                elif family == 'lowrank':
                    rank = spec['rank']
                    budget = 4096+min(rank, 3)*(4096+3)+2*4096*rank
                    model = BudgetLoRA(dense, budget, 30601)
                    assert model.rank_hidden == rank and model.rank_first == min(rank, 3)
                    extra = dict(width=4096, rank=rank, seed=30601, diagnostics=model.diagnostics,
                                 source_contract='coupled dense initialization only; zero low-rank increments')
                    expected = (budget, 16789504)
                elif family == 'legendre':
                    model = LegendreCompression(dense, inputs, labels, spec['order'])
                    extra = dict(order=spec['order'], source_contract='dense initialization only')
                    expected = (81922+65536*spec['order'], 16777216+2*spec['order'])
                else:
                    if family == 'harmonic':
                        if args.harmonic_curve or args.compression_larger:
                            if harmonic_sources is None:
                                raise RuntimeError('Shared Harmonic source setup failed')
                            sources = {key: [v[:, :spec['rank']] for v in values]
                                       for key, values in harmonic_sources.items()}
                            source_info = dict(shared_source='harmonic_sources', prefix_rank=spec['rank'],
                                diagnostics_scope=f"shared fit diagnostics concern rank{report['harmonic_sources']['requested_rank']}; "
                                                  'prefix source error not separately measured')
                        else:
                            sources, source_info = unified_harmonic_sources(dense, inputs, labels, 32., spec['rank'], 601)
                    else:
                        if log_sources is None:
                            raise RuntimeError('Shared Logarithmic source setup failed')
                        sources = log_sources['new'][spec['rank']]
                        source_info = dict(shared_source='logarithmic_sources', source_seed=501,
                            source_contract='full-horizon rollout, declared passive inputs, labels withheld')
                    model = DeepHarmonic(dense, inputs, labels, sources, spec['width'], selection_trials=64,
                        readout_floor=baseline['readout_floor'] if family == 'logarithmic' else None)
                    assert all(v.shape[1] == spec['rank'] for values in sources.values() for v in values)
                    del sources
                    assert model.diagnostics['widths'] == [spec['width']]*2
                    assert not any(v['truncated'] for v in model.diagnostics['source_truncations'])
                    extra = dict(compact_width=spec['width'], source_rank=spec['rank'], selection_trials=64, source=source_info,
                                 diagnostics=model.diagnostics, diagnostics_scope='float64 assembly; runtime float32')
                    expected = (spec['width']**2+4*spec['width']+8,
                                3*spec['width']**2+int(family == 'logarithmic'))
                synchronize(device)
                elapsed = time.monotonic()-t0
                if elapsed > 120.:
                    raise TimeoutError(f'{name} setup exceeded 120s')
                moving = sum(v.numel() for v in model.initial_state)
                assert (moving, model.fixed_scalars) == expected
                report['models'][name] = dict(moving=moving, fixed=model.fixed_scalars,
                    total=moving+model.fixed_scalars, setup_seconds=elapsed, **extra)
                move(model, 'cpu')
                models[name] = model
                print(json.dumps(dict(event='point_setup_done', method=name, seconds=elapsed)), flush=True)
            except Exception as error:
                report['errors'][name+'_setup'] = f'{type(error).__name__}: {error}'
            persist()
        del dense, inputs, labels
        if args.tradeoff or args.compression_larger:
            del log_sources
        if args.harmonic_curve or args.compression_larger:
            del harmonic_sources
        with ThreadPoolExecutor(max_workers=2) as pool:
            pending, remaining = {}, iter(models.items())
            def submit_next(device_name):
                item = next(remaining, None)
                if item is not None:
                    name, model = item
                    pending[pool.submit(run, name, model, device_name)] = (name, device_name)
            for device_name in args.devices:
                submit_next(device_name)
            while pending:
                finished, _ = wait(pending, return_when=FIRST_COMPLETED)
                for future in finished:
                    name, device_name = pending.pop(future)
                    try:
                        prediction, info = future.result()
                        arrays[name], arrays['times_'+name] = prediction, np.asarray(info['times'])
                        report['runs'][name] = info
                        if info['complete']:
                            report['points'][name] = {key: report['models'][name][key] for key in ('moving', 'fixed', 'total')}
                            report['points'][name].update(info['comparison'])
                    except Exception as error:
                        report['errors'][name] = f'{type(error).__name__}: {error}'
                    persist()
                    submit_next(device_name)
        report['points']['logarithmic'] = {key: logarithmic['models']['4'][key] for key in ('moving', 'fixed', 'total')}
        report['points']['logarithmic'].update(logarithmic['runs']['4']['comparison'])
        report['points']['dense'] = dict(moving=16793600, fixed=0, total=16793600,
                                        endpoint_rms=benchmark, endpoint_over_dense_pair=1.)
        report['complete'] = len(report['runs']) == len(specs) and all(v['complete'] for v in report['runs'].values())
        if args.seed_check and report['complete']:
            names = ['dense_8', 'dense_seed10602', 'dense_seed10603']
            errors = np.asarray([report['points'][name]['endpoint_rms'] for name in names])
            report['dense_seed_summary'] = dict(width=1446, seeds=[10601, 10602, 10603],
                names=names, endpoint_rms=errors.tolist(), mean_endpoint_rms=float(errors.mean()),
                sample_standard_deviation=float(errors.std(ddof=1)),
                standard_error=float(errors.std(ddof=1)/math.sqrt(len(errors))),
                scope='mean of per-seed RMS values; uncertainty over initialization only, conditional on fixed data and dense reference')
        summary_widths = (args.dense_extra_seeds or ([722] if args.smallest_seed_check else
                          [args.dense_width] if args.dense_width is not None else []))
        for width in summary_widths if report['complete'] else []:
            names = (['dense_32', 'dense_n722_seed10602', 'dense_n722_seed10603'] if args.smallest_seed_check
                     else [f'dense_n{width}_seed{seed}' for seed in (10601, 10602, 10603)])
            if args.dense_extra_seeds is not None:
                names[0] = extra_seed_bases[width]
            errors = np.asarray([report['points'][name]['endpoint_rms'] for name in names])
            summary = dict(width=width, seeds=[10601, 10602, 10603], names=names,
                endpoint_rms=errors.tolist(), mean_endpoint_rms=float(errors.mean()),
                sample_standard_deviation=float(errors.std(ddof=1)),
                standard_error=float(errors.std(ddof=1)/math.sqrt(len(errors))),
                scope='mean of per-seed RMS values; uncertainty over initialization only, conditional on fixed data and dense reference')
            inherited = report.get('dense_seed_summaries',
                                   [report['dense_seed_summary']] if 'dense_seed_summary' in report else [])
            assert all(group['width'] != width for group in inherited)
            report['dense_seed_summaries'] = inherited+[summary]
    finally:
        persist()
    print(json.dumps(dict(complete=report['complete'], points=report['points'], errors=report['errors'])), flush=True)
    return 0 if report['complete'] else 1


def sphere_points_plot_main(argv):
    """Check saved predictions and plot endpoint or maximum-recorded-time RMS."""
    parser = argparse.ArgumentParser(description=sphere_points_plot_main.__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--out', type=Path, help='Optional fresh destination; leave saved inputs unchanged')
    parser.add_argument('--metric', choices=('endpoint', 'max-time'), default='endpoint')
    parser.add_argument('--seed-statistic', choices=('mean', 'median'), default='mean',
                        help='Mean with SE bars, or median with observed min–max bars')
    parser.add_argument('--thin-dense', action='store_true',
                        help='Show alternate dense sizes, keeping both endpoints')
    parser.add_argument('--clean', action='store_true',
                        help='Short labels, no point annotations or footer; export a separate caption')
    parser.add_argument('--frozen-point', action='store_true',
                        help='Plot frozen features at the full-width trained-readout parameter count')
    parser.add_argument('--independent-references', action='store_true',
                        help='Pair the three stored dense seeds with references601/602/603')
    args = parser.parse_args(argv)
    destination = args.out if args.out is not None else args.run
    if args.out is not None:
        destination.mkdir(parents=True, exist_ok=False)
    metric = 'endpoint_rms' if args.metric == 'endpoint' else 'max_time_rms'
    figure_name = 'endpoint_points' if args.metric == 'endpoint' else 'max_time_points'
    if args.seed_statistic == 'median':
        figure_name += '_median'
    if args.thin_dense:
        figure_name += '_thinned'
    if args.clean:
        figure_name += '_clean'
    if args.frozen_point:
        figure_name += '_frozen_point'
    if args.independent_references:
        figure_name += '_paired'
    report = json.loads((args.run/'report.json').read_text())
    assert report['complete'] and not report['errors']
    reference_path, logarithmic_path = Path(report['reference']), Path(report['logarithmic'])
    assert sha((reference_path/'trajectories.npz').read_bytes()) == report['reference_arrays_sha256']
    def load_arrays(path):
        with np.load(path/'trajectories.npz') as saved:
            return {key: saved[key] for key in saved.files}
    reference, current, logarithmic = [load_arrays(path) for path in (reference_path, args.run, logarithmic_path)]
    chain, seen = [(report, current)], {str(args.run.resolve())}
    while chain[-1][0].get('previous_points'):
        parent = chain[-1][0]
        previous = Path(parent['previous_points'])
        assert str(previous.resolve()) not in seen
        seen.add(str(previous.resolve()))
        assert sha((previous/'trajectories.npz').read_bytes()) == parent['previous_arrays_sha256']
        assert sha((previous/'report.json').read_bytes()) == parent['previous_report_sha256']
        chain.append((json.loads((previous/'report.json').read_text()), load_arrays(previous)))
    model_info, run_arrays = {}, {}
    for earlier_report, earlier_arrays in reversed(chain):
        model_info.update(earlier_report['models'])
        run_arrays.update({name: earlier_arrays for name in earlier_report['runs']})
    model_info.update(dense=dict(width=4096), logarithmic=dict(compact_width=424))
    computed, predictions = {}, {}
    for name, point in report['points'].items():
        saved, key = ((reference, 'iid') if name == 'dense' else
                      (logarithmic, 'budget_4') if name == 'logarithmic' else
                      (run_arrays[name], name))
        prediction = saved[key]
        predictions[name] = prediction
        assert prediction.shape == (65, 38) and np.isfinite(prediction).all()
        times = saved['times_iid' if name == 'dense' else 'times_4' if name == 'logarithmic' else 'times_'+name]
        np.testing.assert_allclose(times, reference['times_dense'], atol=1e-10, rtol=0)
        for field in ('train_inputs', 'train_labels', 'query_inputs', 'query_labels'):
            np.testing.assert_array_equal(saved[field], reference[field])
        rms = trajectory_rms(prediction[:, 8:].astype(float), reference['dense'][:, 8:].astype(float))
        np.testing.assert_allclose(rms['endpoint_rms'], point['endpoint_rms'], atol=1e-14, rtol=1e-12)
        if 'max_time_rms' in point:
            np.testing.assert_allclose(rms['max_time_rms'], point['max_time_rms'], atol=1e-14, rtol=1e-12)
        computed[name] = dict(point, max_time_rms=rms['max_time_rms'])
        np.testing.assert_allclose(point['endpoint_over_dense_pair'],
            rms['endpoint_rms']/report['dense_pair_endpoint_rms'], atol=1e-14, rtol=1e-12)
        family, model = name.split('_')[0], model_info[name]
        if family == 'dense':
            width = model['width']
            expected = (width*width+4*width, 0)
        elif family == 'legendre':
            expected = (81922+65536*model['order'], 16777216+2*model['order'])
        elif family == 'ntk':
            expected = (8, 304)
        elif family == 'lowrank':
            rank = model['rank']
            expected = (4096+min(rank, 3)*(4096+3)+2*4096*rank, 16789504)
        else:
            width = model['compact_width']
            expected = (width*width+4*width+8, 3*width*width+int(family == 'logarithmic'))
        assert (point['moving'], point['fixed']) == expected
        assert point['total'] == point['moving']+point['fixed']
        if name in report['runs']:
            losses = np.mean((prediction[:, :8].astype(float)-reference['train_labels'])**2, axis=1)
            np.testing.assert_allclose(losses, report['runs'][name]['losses'], atol=1e-6, rtol=2e-5)
    summaries = report.get('dense_seed_summaries',
                           [report['dense_seed_summary']] if 'dense_seed_summary' in report else [])
    paired_scores, extra_reference_names, new_dense_pair = {}, set(), None
    if args.independent_references:
        if report.get('independent_references') != {'602': 'dense_reference602', '603': 'dense_reference603'}:
            parser.error('--independent-references requires the two saved reference-seed runs')
        references = {601: reference['dense']}
        for seed, name in report['independent_references'].items():
            assert model_info[name]['width'] == 4096 and model_info[name]['seed'] == int(seed)
            references[int(seed)] = predictions[name]
            extra_reference_names.add(name)
        for summary in summaries:
            for name, seed, reference_seed in zip(summary['names'], summary['seeds'], (601, 602, 603)):
                assert seed == reference_seed+10000
                score = trajectory_rms(predictions[name][:, 8:].astype(float),
                                       references[reference_seed][:, 8:].astype(float))
                score.pop('curve')
                paired_scores[name] = dict(score, candidate_seed=seed, reference_seed=reference_seed)
        new_dense_pair = trajectory_rms(references[602][:, 8:].astype(float),
                                        references[603][:, 8:].astype(float))
        new_dense_pair.pop('curve')
    plot_summaries, seed_replicates = {}, set()
    for summary in summaries:
        values = np.array([report['points'][name]['endpoint_rms'] for name in summary['names']])
        assert len(values) == 3 and summary['seeds'] == [10601, 10602, 10603]
        assert all(model_info[name]['width'] == summary['width'] for name in summary['names'])
        assert [model_info[name]['seed'] for name in summary['names']] == summary['seeds']
        np.testing.assert_allclose(values, summary['endpoint_rms'], atol=1e-14, rtol=1e-12)
        np.testing.assert_allclose(values.mean(), summary['mean_endpoint_rms'], atol=1e-14, rtol=1e-12)
        np.testing.assert_allclose(values.std(ddof=1)/math.sqrt(3), summary['standard_error'], atol=1e-14, rtol=1e-12)
        metric_values = np.array([paired_scores.get(name, computed[name])[metric] for name in summary['names']])
        plot_summaries[summary['names'][0]] = dict(width=summary['width'], metric=metric,
                            values=metric_values.tolist(), mean=float(metric_values.mean()),
                            median=float(np.median(metric_values)),
                            minimum=float(metric_values.min()), maximum=float(metric_values.max()),
                            standard_error=float(metric_values.std(ddof=1)/math.sqrt(3)),
                            names=summary['names'], seeds=summary['seeds'],
                            reference_seeds=[601, 602, 603] if args.independent_references else [601]*3,
                            scope=args.seed_statistic+(' of independent initialization-pair scores, conditional on fixed data'
                                if args.independent_references else
                                ' of individual-seed scores, conditional on fixed data and dense reference'))
        seed_replicates.update(summary['names'][1:])
    if args.independent_references:
        values = np.asarray([computed['dense'][metric], new_dense_pair[metric]])
        plot_summaries['dense'] = dict(width=4096, metric=metric, values=values.tolist(),
            mean=float(values.mean()), median=float(np.median(values)),
            minimum=float(values.min()), maximum=float(values.max()),
            standard_error=float(values.std(ddof=1)/math.sqrt(2)),
            seed_pairs=[[601, 10601], [602, 603]],
            scope=args.seed_statistic+' of two disjoint initialization pairs, conditional on fixed data')
    displayed = {name: dict(point) for name, point in computed.items()
                 if name not in seed_replicates and name not in extra_reference_names}
    if args.independent_references:
        for name, point in displayed.items():
            point.update(paired_scores.get(name, {}))
            point.pop('endpoint_over_dense_pair', None)
    for name, plot_summary in plot_summaries.items():
        displayed[name][metric] = plot_summary[args.seed_statistic]
    matched_orders = report.get('lowrank_legendre_orders')
    if matched_orders is not None:
        assert matched_orders == {f'lowrank_{8*order}': order for order in (1, 2, 3, 12)}
        for name, order in matched_orders.items():
            assert name in displayed and model_info[name]['rank'] == 8*order
            legendre_name = 'legendre' if order == 12 else f'legendre_{order}'
            assert model_info[legendre_name]['order'] == order
        displayed = {name: point for name, point in displayed.items()
                     if not name.startswith('lowrank_') or name in matched_orders}
    if args.thin_dense:
        dense_names = sorted((name for name in displayed if name.split('_')[0] == 'dense'),
                             key=lambda name: model_info[name]['width'])
        kept_dense = set(dense_names[::2] + dense_names[-1:])
        displayed = {name: point for name, point in displayed.items()
                     if name.split('_')[0] != 'dense' or name in kept_dense}
    shown_summaries = {name: summary for name, summary in plot_summaries.items() if name in displayed}
    if args.frozen_point:
        if 'ntk' not in displayed:
            parser.error('--frozen-point requires an existing frozen-features baseline')
        width = model_info['dense']['width']
        fixed_backbone = width*width+width*reference['train_inputs'].shape[1]
        displayed['ntk'].update(moving=width, fixed=fixed_backbone, total=width+fixed_backbone,
                                storage_representation='full frozen backbone and trained primal readout; predictions from dual Euler')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'pdf.fonttype': 42})
    figure, axis = plt.subplots(figsize=(8, 5.2) if args.clean else (10, 6.3))
    styles = dict(dense=('#666666', 'D'), legendre=('#4477AA', 's'),
                  logarithmic=('#228833', 'o'), harmonic=('#EE7733', '^'), lowrank=('#CC6677', 'v'))
    for family, (color, marker) in styles.items():
        points = sorted(((name, point) for name, point in displayed.items() if name.split('_')[0] == family),
                        key=lambda item: item[1]['moving'])
        if not points:
            continue
        target = axis
        label = 'Low rank' if family == 'lowrank' else family.capitalize()
        target.plot([point['moving'] for _, point in points], [point[metric] for _, point in points],
            color=color, marker=marker, ms=6, lw=1.2, label=label, zorder=3)
        for name, point in points:
            model = model_info[name]
            label_y = point[metric]
            label = (f"q={model['order']}" if family == 'legendre' else
                     f"n={model['width']}" if family == 'dense' else
                     f"rank {model['rank']}" if family == 'lowrank' else f"width {model['compact_width']}")
            if family == 'lowrank' and matched_orders is not None:
                label += f"\n(q={matched_orders[name]})"
            if name in plot_summaries:
                stats = plot_summaries[name]
                spread = ([[stats['median']-stats['minimum']], [stats['maximum']-stats['median']]]
                          if args.seed_statistic == 'median' else stats['standard_error'])
                target.errorbar(point['moving'], point[metric], yerr=spread,
                                color=color, fmt='none', capsize=4, lw=1.3, zorder=4)
                if len(shown_summaries) <= 2:
                    label += ('\nmedian, 3 seeds' if args.seed_statistic == 'median' else '\nmean ± SE, 3 seeds')
                if args.seed_statistic == 'median':
                    label_y = stats['maximum']
            if args.clean:
                continue
            offset = (0, -17) if family == 'logarithmic' else (0, 9)
            alignment = 'center'
            if family == 'logarithmic' and model['compact_width'] in (424, 600):
                offset, alignment = (10, 9), 'left'
            if family == 'lowrank' and matched_orders is not None:
                offset = (0, -30) if model['rank'] in (24, 96) else (0, 12)
            target.annotate(label, (point['moving'], label_y), xytext=offset,
                          textcoords='offset points', ha=alignment, fontsize=8, color=color)
    benchmark = displayed['dense'][metric]
    axis.axhline(benchmark, color='#777777', lw=1.1, ls=':', zorder=1,
                label='Dense–dense')
    if 'ntk' in displayed:
        if args.frozen_point:
            axis.plot(displayed['ntk']['moving'], displayed['ntk'][metric], color='#AA4499',
                      marker='o', ms=7, ls='none', zorder=3, label='Frozen features')
        else:
            axis.axhline(displayed['ntk'][metric], color='#AA4499', lw=1.3, ls='--', zorder=1,
                         label='Frozen features')
    xs = [v['moving'] for name, v in displayed.items() if name != 'ntk' or args.frozen_point]
    ys = [v[metric] for v in displayed.values()]
    axis.set(xscale='log', yscale='log', xlim=(min(xs)*.65, max(xs)*1.6),
             ylim=(min(ys)*.55, max(ys)*(1.5 if args.clean else 2.5)),
             xlabel='Learned state' if args.clean else 'Moving / learned scalars (including auxiliary state)')
    axis.set_ylabel(('Test RMS' if args.metric == 'endpoint' else 'Worst-time RMS') if args.clean else
                    'Endpoint test RMS versus the width-4096 reference' if args.metric == 'endpoint'
                    else 'Worst recorded-time test RMS vs. dense reference')
    figure.suptitle('3D sphere' if args.clean else
                   '3D sphere · width 4096 · 8 train / 30 test · two tanh layers', fontsize=12)
    axis.grid(which='major', alpha=.15)
    handles, labels = axis.get_legend_handles_labels()
    axis.legend(handles, labels, loc='best', fontsize=9 if args.clean else 8, framealpha=.95)
    caption_summaries = {name: value for name, value in shown_summaries.items()
                         if not args.independent_references or name != 'dense'}
    seeded_widths = ', '.join(str(v['width']) for v in sorted(caption_summaries.values(), key=lambda v: v['width']))
    seeded_groups = f'n={seeded_widths}' if len(caption_summaries) <= 3 else f'{len(caption_summaries)} dense sizes'
    caption = (f'3 seeds at {seeded_groups}; others have one. Error bars: SE conditional on the fixed data/reference.'
               if shown_summaries else 'Same Euler step and horizon; one initialization per size. Lines connect measurements, not fitted scaling laws.')
    if shown_summaries and args.seed_statistic == 'median':
        caption = f'Medians of 3 seeds: {seeded_groups}; others have one. Bars: observed min–max, not confidence intervals.'
    if args.independent_references:
        caption = (f'Dense: 3 independent initialization pairs at {seeded_groups}; width4096: 2 disjoint pairs. '
                   f'Centers: {args.seed_statistic}; other methods unchanged against reference601.')
    fixed_notes = []
    for family in styles:
        fixed = [point['fixed'] for name, point in displayed.items() if name.split('_')[0] == family]
        if fixed:
            amount = (str(max(fixed)) if max(fixed) < 10000 else
                      f'{min(fixed)/1e6:.3f}–{max(fixed)/1e6:.3f}M'
                      if round(min(fixed)/1e6, 3) != round(max(fixed)/1e6, 3) else f'{max(fixed)/1e6:.3f}M')
            fixed_notes.append(f'{"Low-rank" if family == "lowrank" else family.capitalize()} {amount}')
    caption += '\nAdditional fixed scalars: ' + '; '.join(fixed_notes) + '.'
    if 'ntk' in displayed:
        caption += ('\nFrozen features: 4,096 trained readout weights plus 16,789,504 frozen backbone weights; equivalent dual-Euler predictions.'
                    if args.frozen_point else
                    '\nDashed: equivalent to 4,096 trained readout weights on frozen dense features; accuracy reference, not a storage claim.')
    if matched_orders is not None:
        caption += '\nLow-rank controls match Legendre hidden-increment rank capacity: r = 8q; x shows actual moving storage.'
    if args.metric == 'max-time':
        caption += '\nMaximum over 65 saved times in [0, 32], not a continuous-time supremum; seed summaries use per-seed maxima.'
    if args.clean:
        detail = ['Compression of two-hidden-layer tanh networks on the unit sphere in three input dimensions, '
                  'with a width-4096 dense reference, 8 training points and 30 test inputs.',
                  ('Test RMS is measured at training time 32 against width-4096 references.'
                   if args.metric == 'endpoint' else
                   'Test RMS is maximized over 65 saved times in [0,32] against width-4096 references; '
                   'this is not a continuous-time supremum.'),
                  'All compared models use explicit Euler with step 0.0015625.',
                  'Learned state counts moving scalar coordinates, including auxiliary state, but excludes fixed coefficients.']
        order_fields = dict(dense='width', harmonic='compact_width', logarithmic='compact_width',
                            legendre='order', lowrank='rank')
        for family, field in order_fields.items():
            values = sorted(model_info[name][field] for name in displayed if name.split('_')[0] == family)
            if values:
                detail.append(f'{"Low-rank control" if family == "lowrank" else family.capitalize()} '
                              f'{"widths" if "width" in field else field+"s"}: '+', '.join(map(str, values))+'.')
        if args.independent_references:
            detail += [f'Dense widths {seeded_widths} pair stored seeds 10601,10602,10603 with large references '
                       f'601,602,603 respectively; centers are {args.seed_statistic}s of the three pair scores.',
                       f'The width-4096 point and dotted benchmark use the {args.seed_statistic} of exactly two disjoint '
                       'large-dense pairs: (601,10601) and (602,603).',
                       ('Bars show observed min--max, not confidence intervals.' if args.seed_statistic == 'median' else
                        'Bars show standard errors across pair scores.'),
                       'Only two large reference trajectories were newly trained. All other trajectories are reused. '
                       'Single-run compression and control scores retain their original coupled reference601. '
                       'Repetitions are independent conditional on the fixed data, but different widths reuse references '
                       'within each repetition and are not independent of each other.',
                       'Each pair score is computed before aggregation, including its temporal maximum for the worst-time plot.']
        elif shown_summaries:
            detail.append(f'Dense widths {seeded_widths} show '+
                          ('medians over three initializations with observed min--max bars, not confidence intervals.'
                           if args.seed_statistic == 'median' else
                           'means over three initializations with standard-error bars conditional on the fixed data and reference.'))
        detail += ['All other points use one initialization; lines connect measurements, not fitted scaling laws.',
                   f'The dotted dense--dense reference is {benchmark:.8g}.']
        if 'ntk' in displayed:
            detail.append('The frozen-features dot counts 4096 trained readout weights and retains the full frozen dense '
                          'backbone with 16789504 additional weights. Its unchanged predictions were computed using the '
                          'equivalent finite-panel dual Euler implementation, not a new primal training run.'
                          if args.frozen_point else
                          'The dashed frozen-features baseline is equivalent to training 4096 readout weights on the '
                          'frozen dense backbone; it is an accuracy reference without a horizontal storage coordinate.')
        fixed_details = []
        for family in styles:
            values = [point['fixed'] for name, point in displayed.items() if name.split('_')[0] == family]
            if values:
                count = str(min(values)) if min(values) == max(values) else f'{min(values)}--{max(values)}'
                fixed_details.append(f'{"low rank" if family == "lowrank" else family} {count}')
        detail.append('Additional fixed scalar counts: '+', '.join(fixed_details)+'.')
        if matched_orders is not None:
            detail.append('Low-rank hidden-increment capacities match Legendre via rank = 8 times order; '
                          'their actual learned-state counts are plotted.')
        detail += ['Harmonic and Logarithmic use empirical full-horizon dense-rollout initialization, not the certified '
                   'initialization-jet compiler. Harmonic uses 72 fixed sphere quadrature nodes independent of the scored inputs; '
                   'Logarithmic setup sees the test inputs, never their labels.',
                   'These are finite-step measurements without a new per-budget numerical refinement certificate.']
        caption = '\n'.join(detail)
        (destination/(figure_name+'.caption.txt')).write_text(caption+'\n')
        (destination/(figure_name+'.caption.tex')).write_text('\\caption{\n'+caption+'\n}\n')
        figure.tight_layout(rect=(0, 0, 1, 1))
    else:
        figure.text(.5, .02, caption, ha='center', fontsize=8)
        figure.tight_layout(rect=(0, .155 if args.metric == 'max-time' else .13 if matched_orders is not None else .105, 1, 1))
    for suffix in ('png', 'pdf'):
        figure.savefig(destination/(figure_name+'.'+suffix), dpi=180, bbox_inches='tight')
    plt.close(figure)
    check_name = 'point_check.json' if args.metric == 'endpoint' else 'max_time_point_check.json'
    if args.seed_statistic == 'median':
        check_name = check_name.replace('.json', '_median.json')
    if args.thin_dense:
        check_name = check_name.replace('.json', '_thinned.json')
    if args.clean:
        check_name = check_name.replace('.json', '_clean.json')
    if args.frozen_point:
        check_name = check_name.replace('.json', '_frozen_point.json')
    if args.independent_references:
        check_name = check_name.replace('.json', '_paired.json')
    save_json(destination/check_name, dict(status='PASS', points=computed, metric=metric,
        seed_statistic=args.seed_statistic, thin_dense=args.thin_dense, clean=args.clean,
        frozen_point=args.frozen_point,
        independent_references=args.independent_references,
        paired_comparisons=paired_scores, new_dense_pair=new_dense_pair,
        error_bars='observed minimum–maximum' if args.seed_statistic == 'median' else 'standard error of mean',
        dense_pair_rms=benchmark, dense_seed_summary=plot_summaries.get('dense_8'),
        dense_seed_summaries=plot_summaries,
        displayed_points=displayed, displayed_dense_seed_summaries=shown_summaries,
        legend_labels=labels, caption=caption, lowrank_legendre_orders=matched_orders,
        source_sha256=sha(Path(__file__).read_bytes()),
        trajectory_sha256=sha((args.run/'trajectories.npz').read_bytes()),
        scope='saved-array consistency, not a new numerical refinement certificate'))
    print(json.dumps(dict(status='PASS', output=str(destination/(figure_name+'.png')))), flush=True)


def cubic_summary_main(argv):
    """One saved-array consistency check and one paired-comparison figure."""
    parser = argparse.ArgumentParser(description=cubic_summary_main.__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    manifest = json.loads((args.root/'config.json').read_text())
    rows, checks = [], 0
    for case in manifest['plan']:
        path = args.root/case['name']
        report = json.loads((path/'report.json').read_text())
        assert report['source_sha256'] == manifest['source_sha256']
        checks += 1
        with np.load(path/'trajectories.npz') as saved:
            arrays = {name: saved[name] for name in saved.files}
        for name, run in report['runs'].items():
            if not run.get('complete'):
                continue
            np.testing.assert_allclose(arrays['times_'+name], np.arange(65)/2, atol=1e-10, rtol=0)
            assert arrays[name].shape == (65, 38) and np.isfinite(arrays[name]).all()
            loss = np.mean((arrays[name][:, :8].astype(float)-arrays['train_labels'])**2, axis=1)
            np.testing.assert_allclose(loss, run['losses'], atol=1e-6, rtol=2e-5)
            checks += 3
        for name, value in report['comparisons'].items():
            rms = trajectory_rms(arrays[name][:, 8:].astype(float), arrays['dense'][:, 8:].astype(float))
            for field in ('max_time_rms', 'endpoint_rms'):
                np.testing.assert_allclose(rms[field], value[field], atol=1e-12, rtol=1e-10)
            np.testing.assert_allclose(np.max(np.abs(arrays[name].astype(float)-arrays['dense'])),
                                       value['full_panel_max_abs'], atol=1e-12, rtol=1e-10)
            np.testing.assert_allclose(np.mean((arrays[name][-1, 8:]-arrays['query_labels'])**2),
                                       value['test_mse'], atol=1e-12, rtol=1e-10)
            checks += 4
            if name not in report['methods']:
                continue
            model, result = report['models'][name], report['methods'][name]
            q, d = model['compact_width'], report['scope']['dimension']
            assert model['moving'] == q*q+(d+1)*q+8
            assert model['fixed'] == 3*q*q+1 and model['total'] == model['moving']+model['fixed']
            assert not any(v['truncated'] for v in model['diagnostics']['source_truncations'])
            if 'refinement_rms' in value:
                refine = trajectory_rms(arrays[name][:, 8:].astype(float),
                                       arrays[name+'_coarse'][:, 8:].astype(float))['max_time_rms']
                np.testing.assert_allclose(refine, value['refinement_rms'], atol=1e-12, rtol=1e-10)
                total = refine+report['comparisons']['dense']['refinement_rms']
                assert result['numerical_gate_pass'] == (total < .1*report['comparisons']['iid']['max_time_rms'])
            checks += 5
        rows.append(dict(case=case['name'], report=report))
    args.out.mkdir(parents=True, exist_ok=False)
    plt.rcParams.update({'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False,
                         'pdf.fonttype': 42})
    figure, axes = plt.subplots(1, len(rows), figsize=(3*len(rows), 3.6), squeeze=False)
    colors = ('#5B6F9C', '#DA7740')
    for axis, row in zip(axes.flat, rows):
        report = row['report']
        for i, size in enumerate(('full', 'small')):
            for j, partition in enumerate(('old', 'new')):
                name = partition+'_'+size
                value = report['comparisons'].get(name, {}).get('ratio_to_dense_pair')
                x = i+(j-.5)*.28
                if value is None:
                    axis.text(x, .04, 'missing', rotation=90, transform=axis.get_xaxis_transform(), ha='center')
                    continue
                resolved = report['methods'].get(name, {}).get('numerical_gate_pass', False)
                axis.bar(x, value, width=.25, color=colors[j], alpha=1 if resolved else .35,
                         hatch=None if resolved else '//', label=partition.capitalize() if i == 0 else None)
                axis.text(x, value, f'{value:.2g}', ha='center', va='bottom', fontsize=8)
        axis.axhline(1, color='#777777', lw=.8)
        axis.axhline(3, color='#777777', lw=.8, ls=':')
        axis.set_yscale('log')
        axis.set_xticks((0, 1), ('Rank 12', 'Rank 6'))
        axis.set_title(row['case'].replace('_seed', '\nseed ').replace('digits17', 'Digits 1/7'))
        axis.grid(axis='y', alpha=.12)
    axes[0, 0].set_ylabel('Maximum-time test RMS / dense-pair RMS')
    axes[0, -1].legend(frameon=False, fontsize=8)
    figure.text(.5, .025, 'Same compact optimizer and retained size within each pair. '
        'Hatching: unresolved Euler refinement. Dotted line: accuracy threshold 3.', ha='center', fontsize=8)
    figure.tight_layout(rect=(0, .07, 1, 1))
    for suffix in ('png', 'pdf'):
        figure.savefig(args.out/('paired_sources.'+suffix), dpi=180, bbox_inches='tight')
    plt.close(figure)
    save_json(args.out/'summary.json', dict(checks_passed=checks, source_sha256=manifest['source_sha256'], cases=rows))
    print(json.dumps(dict(checks_passed=checks, cases=len(rows), output=str(args.out))), flush=True)


def compression_sweep_main(argv):
    """Run a frozen 1–24-case probe manifest, with one sequential worker per GPU."""
    from concurrent.futures import ThreadPoolExecutor
    import re
    import threading

    parser = argparse.ArgumentParser(description=compression_sweep_main.__doc__)
    parser.add_argument('--plan', type=Path, required=True,
                        help='JSON list of 1–24 {"name": "unique_case", "args": ["--width", "8192", ...]} objects')
    parser.add_argument('--devices', nargs='+', default=['cuda:0', 'cuda:1'])
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--case-seconds', type=float, default=1500.)
    parser.add_argument('--protocol', choices=('probe', 'unified', 'cubic'), default='probe')
    args = parser.parse_args(argv)
    if (len(set(args.devices)) != len(args.devices)
            or any(not re.fullmatch(r'cuda:(0|[1-9][0-9]*)', value) for value in args.devices)):
        parser.error('Need distinct explicit CUDA devices, e.g. cuda:0 cuda:1')
    if not math.isfinite(args.case_seconds) or args.case_seconds <= 0:
        parser.error('Need a positive finite per-case wall-clock cap')
    try:
        plan_bytes = args.plan.read_bytes()
        plan = json.loads(plan_bytes)
    except (OSError, ValueError) as error:
        parser.error(f'Cannot read plan: {error}')
    allowed = {'--width', '--depth', '--activation', '--digits', '--samples', '--calibration',
               '--budget', '--source-rank', '--source-step', '--seed', '--horizon', '--step',
               '--per-run-seconds', '--panel-queries', '--readout-floor', '--compare-legacy'}
    if args.protocol == 'unified':
        allowed = {'--width', '--dataset', '--horizon', '--step', '--per-run-seconds'}
    elif args.protocol == 'cubic':
        allowed = {'--dataset', '--seed'}
    if not isinstance(plan, list) or not 1 <= len(plan) <= 24:
        parser.error('Each sweep manifest must contain 1–24 cases')
    for case in plan:
        if (not isinstance(case, dict) or set(case) != {'name', 'args'}
                or not isinstance(case['name'], str)
                or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', case['name'])
                or not isinstance(case['args'], list)
                or any(not isinstance(v, str) or v.startswith('-') and v.split('=')[0] not in allowed
                       for v in case['args'])):
            parser.error('Each case needs a safe name and string probe args; --out/--device are assigned by the sweep')
    if len({case['name'] for case in plan}) != len(plan):
        parser.error('Case names must be unique')
    source = Path(__file__).resolve()
    source_hash = sha(source.read_bytes())
    args.out = args.out.resolve()
    args.out.mkdir(parents=True, exist_ok=False)
    save_json(args.out/'config.json', dict(plan=plan, plan_sha256=sha(plan_bytes),
        source_sha256=source_hash, command=sys.argv, executable=sys.executable,
        python=platform.python_version(), devices=args.devices, case_seconds=args.case_seconds))
    rows = [dict(name=case['name'], device=args.devices[i % len(args.devices)], status='pending',
                 outcome='inconclusive', report=str(args.out/case['name']/'report.json'),
                 log=str(args.out/(case['name']+'.log'))) for i, case in enumerate(plan)]
    summary = dict(source_sha256=source_hash, complete=False, cases=rows)
    lock = threading.Lock()

    def record(index=None, **values):
        with lock:
            if index is not None:
                rows[index].update(values)
            summary['complete'] = all(row['status'] not in ('pending', 'running') for row in rows)
            summary['status_counts'] = {status: sum(row['status'] == status for row in rows)
                                        for status in sorted({row['status'] for row in rows})}
            temporary = args.out/'summary.json.tmp'
            save_json(temporary, summary)
            temporary.replace(args.out/'summary.json')

    def worker(slot, device):
        for index in range(slot, len(plan), len(args.devices)):
            case = plan[index]
            command = [sys.executable, '-B', '-u', str(source),
                       {'unified': 'unified-case', 'cubic': 'cubic-case', 'probe': 'compression-probe'}[args.protocol],
                       '--out', str(args.out/case['name']), '--device', device, *case['args']]
            record(index, status='running', command=command)
            started = time.monotonic()
            result = dict(status='error', outcome='inconclusive', returncode=None)
            try:
                if sha(source.read_bytes()) != source_hash:
                    raise RuntimeError('Executable changed after sweep freeze; case not launched')
                with Path(rows[index]['log']).open('x') as log:
                    child = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                           timeout=args.case_seconds, check=False)
                result['returncode'] = child.returncode
                report = json.loads(Path(rows[index]['report']).read_text())
                for key in ('complete', 'error', 'storage_reduction', 'comparisons', 'all_fitted',
                            'numerical_gate_pass', 'accuracy_pass', 'dense_words', 'compact_words',
                            'legacy_numerical_gate_pass', 'preservation_pass', 'beats_matched_small',
                            'old_new_agreement', 'methods', 'models', 'errors', 'paired_comparisons'):
                    if key in report:
                        result[key] = report[key]
                if report.get('source_sha256') != source_hash or sha(source.read_bytes()) != source_hash:
                    raise RuntimeError('Executable hash changed during case; comparison invalid')
                if child.returncode == 0 and report.get('complete'):
                    result['status'] = 'complete'
                    if args.protocol in ('unified', 'cubic'):
                        result['outcome'] = 'reported_per_method'
                    if (report.get('all_fitted') and report.get('numerical_gate_pass')
                            and report.get('legacy_numerical_gate_pass', True)):
                        success = (report.get('accuracy_pass') and report.get('preservation_pass', True)
                                   and report.get('beats_matched_small', True))
                        result['outcome'] = 'pass' if success else 'fail'
                else:
                    result.setdefault('error', f'Incomplete probe; return code {child.returncode}')
            except subprocess.TimeoutExpired:
                result.update(status='timeout', error=f'Case exceeded {args.case_seconds:g} seconds')
            except Exception as error:
                result['error'] = f'{type(error).__name__}: {error}'
            result['seconds'] = time.monotonic()-started
            record(index, **result)
            print(json.dumps(dict(case=case['name'], **result)), flush=True)

    record()
    with ThreadPoolExecutor(max_workers=len(args.devices)) as executor:
        futures = [executor.submit(worker, slot, device) for slot, device in enumerate(args.devices)]
        for future in futures:
            future.result()
    print(json.dumps(dict(summary=str(args.out/'summary.json'), **summary['status_counts'])), flush=True)
    return 0 if all(row['status'] == 'complete' for row in rows) else 1


def unified_plot_main(argv):
    """Plot the frozen unified sweep from its own measured case reports only."""
    parser = argparse.ArgumentParser(description='Plot unified compression width comparisons')
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    datasets = ('sphere2', 'sphere3', 'sphere10', 'digits17')
    dataset_labels = ('Circle, d=2', 'Sphere, d=3', 'Sphere, d=10', 'Digits 1/7, d=64')
    short_labels = ('Circle', 'Sphere 3', 'Sphere 10', 'Digits 1/7')
    methods = ('legendre', 'harmonic', 'logarithmic')
    colors = dict(legendre='#9560A8', harmonic='#008C87', logarithmic='#D97835')
    records, seen = [], set()
    for path in sorted(args.root.glob('*/report.json')):
        report = json.loads(path.read_text())
        config = report.get('config', {})
        dataset, width = config.get('dataset'), config.get('width')
        if dataset not in datasets or not isinstance(width, int):
            continue
        if (dataset, width) in seen:
            raise ValueError(f'Duplicate dataset/width in sweep root: {dataset}, {width}')
        seen.add((dataset, width))
        records.append(dict(dataset=dataset, width=width, source=str(path), report=report))
    if not records:
        raise ValueError('No unified case reports found below the supplied root')
    records.sort(key=lambda item: (datasets.index(item['dataset']), item['width']))
    widths = sorted({record['width'] for record in records})
    cases = {(record['dataset'], record['width']): record['report'] for record in records}
    args.out.mkdir(parents=True, exist_ok=True)

    def finite(value):
        if value is None:
            return None
        value = float(value)
        return value if math.isfinite(value) else None

    def applicable(dataset, method):
        return method != 'harmonic' or dataset in ('sphere2', 'sphere3')

    def ratio(report, name):
        if not report.get('runs', {}).get(name, {}).get('complete', False):
            return None
        comparison = report.get('comparisons', {}).get(name, {})
        value = finite(comparison.get('ratio_to_dense_pair'))
        if value is None:
            numerator = finite(comparison.get('max_time_rms'))
            denominator = finite(report.get('comparisons', {}).get('iid', {}).get('max_time_rms'))
            if numerator is not None and denominator is not None and denominator > 0:
                value = numerator/denominator
        return value if value is not None and value >= 0 else None

    def resolved(report, method):
        return report.get('methods', {}).get(method, {}).get('numerical_gate_pass') is True

    def ratio_axis(axis):
        # A short linear interval retains exact zeros; larger ratios are logarithmic.
        axis.set_yscale('symlog', linthresh=1e-4, linscale=.3)
        axis.axhline(1, color='#72777D', lw=.8, zorder=0)
        axis.axhline(3, color='#72777D', lw=.8, ls=':', zorder=0)
        axis.grid(axis='y', alpha=.16)

    def save(figure, name):
        figure.savefig(args.out/(name+'.pdf'), bbox_inches='tight')
        figure.savefig(args.out/(name+'.png'), bbox_inches='tight', dpi=190)
        plt.close(figure)

    plt.rcParams.update({'font.size': 9, 'axes.titlesize': 10, 'axes.labelsize': 9,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'pdf.fonttype': 42, 'savefig.facecolor': 'white'})
    method_handles = [Line2D([], [], color=colors[name], lw=2, label=name.capitalize())
                      for name in methods]
    figure, axes = plt.subplots(2, 2, figsize=(10.3, 6.6), constrained_layout=False)
    for axis, dataset, label in zip(axes.flat, datasets, dataset_labels):
        ratio_axis(axis)
        for index, method in enumerate(methods):
            if not applicable(dataset, method):
                continue
            values = [ratio(cases.get((dataset, width), {}), method) for width in widths]
            axis.plot(widths, [np.nan if value is None else value for value in values],
                      color=colors[method], lw=1.7)
            for width, value in zip(widths, values):
                report = cases.get((dataset, width), {})
                if value is None:
                    axis.plot(width, .025+.025*index, marker='x', ms=5, color=colors[method],
                              transform=axis.get_xaxis_transform(), clip_on=False)
                else:
                    axis.plot(width, value, marker='o', ms=5.5, color=colors[method],
                              markerfacecolor=colors[method] if resolved(report, method) else 'white',
                              markeredgewidth=1.3)
        axis.set_ylim(bottom=0)
        axis.set_xscale('log', base=2)
        axis.set_xticks(widths, [str(width) for width in widths])
        axis.set_title(label, loc='left')
        axis.set_xlabel('Dense width n')
        axis.set_ylabel('Maximum-time RMS / dense-pair RMS')
    figure.legend(handles=method_handles, loc='upper center', ncol=3, frameon=False,
                  bbox_to_anchor=(.5, 1.005))
    figure.text(.5, .015, 'Solid grey: dense pair (1); dotted grey: accuracy threshold (3).  '
                 'Open circles: unresolved numerics; bottom crosses: missing.\n'
                 'Harmonic is evaluated only in d=2,3. Finite recorded times and 30 test inputs.',
                 ha='center', va='bottom', fontsize=8)
    figure.subplots_adjust(top=.91, bottom=.15, hspace=.42, wspace=.30)
    save(figure, 'unified_width_accuracy')

    # Select each method's largest width with a complete prediction comparison;
    # a failed numerical gate remains visible and does not change the selection.
    selected = {}
    roles = (('compression', '-', 'o'), ('small', '--', 's'),
             ('lowrank', ':', 'D'), ('ntk', '-.', '^'))
    role_labels = dict(compression='Compression', small='Matched small MLP',
                       lowrank='Matched low-rank', ntk='Initial NTK')
    figure, axes = plt.subplots(2, 3, figsize=(13.2, 7.0))
    for column, method in enumerate(methods):
        chosen = []
        for dataset in datasets:
            eligible = [width for width in widths if applicable(dataset, method)
                        and ratio(cases.get((dataset, width), {}), method) is not None]
            width = max(eligible) if eligible else None
            selected[dataset, method] = width
            chosen.append((width, cases.get((dataset, width), {})))
        labels = [f'{label}\nn={width}' if width is not None else label+'\n—'
                  for label, (width, _) in zip(short_labels, chosen)]
        for row in range(2):
            axis = axes[row, column]
            if row == 0:
                ratio_axis(axis)
            else:
                axis.set_yscale('symlog', linthresh=1e-5, linscale=.3)
                axis.axhline(.01, color='#72777D', ls=':', lw=.8)
                axis.grid(axis='y', alpha=.16)
            for role, linestyle, marker in roles:
                values = []
                for width, report in chosen:
                    name = method if role == 'compression' else 'ntk' if role == 'ntk' else role+'_'+method
                    value = (ratio(report, name) if row == 0 else
                        finite(report.get('runs', {}).get(name, {}).get('final_training_mse'))
                        if report.get('runs', {}).get(name, {}).get('complete') else None)
                    values.append(value)
                color = '#555D66' if role == 'ntk' else colors[method]
                axis.plot(range(4), [np.nan if value is None else value for value in values],
                          linestyle=linestyle, color=color, lw=1.5, alpha=.95)
                for index, value in enumerate(values):
                    if value is not None:
                        face = ('white' if role == 'compression' and not resolved(chosen[index][1], method)
                                else color)
                        axis.plot(index, value, marker=marker, color=color, markerfacecolor=face,
                                  ms=5, markeredgewidth=1.1)
                    elif applicable(datasets[index], method):
                        axis.plot(index, .025+.024*list(role_labels).index(role), marker='x', color=color,
                                  ms=4, transform=axis.get_xaxis_transform(), clip_on=False)
            axis.set_ylim(bottom=0)
            axis.set_xticks(range(4), labels, fontsize=8)
            axis.set_xlim(-.3, 3.3)
            if column == 0:
                axis.set_ylabel('Maximum-time RMS / dense-pair RMS' if row == 0 else 'Final training MSE')
            if row == 0:
                axis.set_title(method.capitalize(), color=colors[method], loc='left')
    role_handles = [Line2D([], [], color='#555D66', ls=style, marker=marker, ms=4,
                          label=role_labels[role]) for role, style, marker in roles]
    figure.legend(handles=role_handles, loc='upper center', ncol=4, frameon=False,
                  bbox_to_anchor=(.5, 1.005))
    figure.text(.5, .015, 'Largest complete width chosen separately for each compression and dataset; '
                 'all controls use that same case.\n'
                 'Open circles: unresolved compression numerics. Dotted training line: MSE 0.01. '
                 'Small and low-rank controls match moving state.',
                 ha='center', va='bottom', fontsize=8)
    figure.subplots_adjust(top=.91, bottom=.15, hspace=.38, wspace=.25)
    save(figure, 'unified_matched_controls')

    figure, axes = plt.subplots(2, 2, figsize=(10.3, 6.6))
    for axis, dataset, label in zip(axes.flat, datasets, dataset_labels):
        for name in ('dense',)+methods:
            if name != 'dense' and not applicable(dataset, name):
                continue
            color = '#444B53' if name == 'dense' else colors[name]
            for key, style in [('total', '-'), ('moving', '--')]:
                if name == 'dense' and key == 'moving':
                    continue
                values = [finite(cases.get((dataset, width), {}).get('models', {}).get(name, {}).get(key))
                          for width in widths]
                axis.plot(widths, [np.nan if value is None or value <= 0 else value for value in values],
                          color=color, ls=style, lw=1.7, marker='o', ms=3.5)
        axis.set_xscale('log', base=2)
        axis.set_yscale('log')
        if not any(np.any(np.asarray(line.get_ydata()) > 0) for line in axis.lines):
            axis.set_ylim(1, 10)
        axis.set_xticks(widths, [str(width) for width in widths])
        axis.grid(axis='y', alpha=.16)
        axis.set_title(label, loc='left')
        axis.set_xlabel('Dense width n')
        axis.set_ylabel('Stored scalar coordinates')
    figure.legend(handles=[Line2D([], [], color='#444B53', lw=2, label='Dense')]+method_handles,
                  loc='upper center', ncol=4, frameon=False, bbox_to_anchor=(.5, 1.005))
    figure.text(.5, .025, 'Solid: total retained model; dashed: moving state. '
                 'Fixed matrices and metrics are counted.\n'
                 'Common data, source construction, and workspace are excluded. '
                 'Harmonic/Logarithmic storage curves overlap in d=2,3.',
                 ha='center', va='bottom', fontsize=8)
    figure.subplots_adjust(top=.91, bottom=.15, hspace=.42, wspace=.30)
    save(figure, 'unified_state_storage')

    rows = []
    for record in records:
        report = record['report']
        for method in methods:
            if not applicable(record['dataset'], method):
                continue
            result = report.get('methods', {}).get(method, {})
            rows.append(dict(dataset=record['dataset'], width=record['width'], method=method,
                source_report=record['source'], complete_run=bool(report.get('runs', {}).get(method, {}).get('complete')),
                ratio_to_dense_pair=ratio(report, method), numerical_gate_pass=result.get('numerical_gate_pass'),
                accuracy_pass=result.get('accuracy_pass'), method_status=result.get('status', 'missing'),
                model=report.get('models', {}).get(method), comparison=report.get('comparisons', {}).get(method),
                controls={name: ratio(report, name) for name in ('small_'+method, 'lowrank_'+method, 'ntk')},
                errors=report.get('errors', {})))
    save_json(args.out/'figure_summary.json', dict(
        scope='Frozen finite-width empirical suite; finite recorded times and thirty scored inputs',
        source_root=str(args.root), plot_source_sha256=sha(Path(__file__).read_bytes()),
        numerical_threshold='dense plus compression step-refinement RMS < 0.1 times iid-dense RMS',
        accuracy_threshold='maximum-time test RMS <= 3 times iid-dense RMS',
        storage_scope='model tensors, excluding common data, source construction and integrator workspace',
        largest_complete_width={dataset: {method: selected[dataset, method] for method in methods}
                                for dataset in datasets}, cases=rows))
    print(json.dumps(dict(figures=str(args.out), case_reports=len(records), method_rows=len(rows))), flush=True)


def experiment_scaling_plot(argv):
    """Audit and plot a one-seed-per-width sweep using saved predictions only."""
    import ast
    import copy
    import io
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter

    parser = argparse.ArgumentParser(description=experiment_scaling_plot.__doc__)
    parser.add_argument('--runs', nargs='+', type=Path, required=True)
    parser.add_argument('--harmonic-probes', nargs='+', type=Path, default=[],
                        help='Include saved harmonic-order-probe candidates without modifying their reference runs')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--factor', type=float, default=1.,
                        help='Positive finite multiplier for both dense-pair accuracy thresholds (default: 1)')
    parser.add_argument('--fit-log-powers', action='store_true',
                        help='Overlay descriptive C(log n)^p fits with >=3 widths and no missing passing width')
    parser.add_argument('--families', nargs='+', choices=('legendre', 'harmonic', 'logarithmic'),
                        default=['legendre', 'harmonic', 'logarithmic'])
    args = parser.parse_args(argv)
    roots = [path.resolve() for path in args.runs]
    families = dict(legendre=('Legendre', '#d18624'), harmonic=('Harmonic', '#297c8e'),
                    logarithmic=('Logarithmic', '#9768b0'))
    families = {key: value for key, value in families.items() if key in args.families}

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def numerical_source(source):
        """Compare numerical definitions without executing saved source files."""
        definitions = {node.name: node for node in ast.parse(source).body
                       if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
        pending = ['DeepDense', 'DeepHarmonic', 'LegendreCompression',
                   'unified_harmonic_sources', 'cubic_rollout_sources',
                   'integrate_euler', 'integrate', 'validation_data',
                   '_experiment_data', '_experiment_seed', '_experiment_move']
        require(all(name in definitions for name in pending),
                'Saved source is missing a required numerical definition')
        checked = {}
        while pending:
            name = pending.pop()
            if name in checked:
                continue
            node = definitions[name]
            checked[name] = sha(ast.dump(node, include_attributes=False).encode())
            pending.extend(item.id for item in ast.walk(node)
                           if isinstance(item, ast.Name) and item.id in definitions
                           and item.id not in checked)
        return dict(sha256=sha(json.dumps(checked, sort_keys=True).encode()), definitions=checked)

    require(len(set(roots)) == len(roots), 'Duplicate input run')
    require(math.isfinite(args.factor) and args.factor > 0, '--factor must be finite and strictly positive')
    probe_paths = [value.resolve() for value in args.harmonic_probes]
    require(len(set(probe_paths)) == len(probe_paths), 'Duplicate Harmonic probe')
    probes, used_probes = [], set()
    for probe_path in probe_paths:
        probe_bytes = (probe_path/'report.json').read_bytes()
        probe = json.loads(probe_bytes)
        require(Path(probe['reference_run']).resolve() in roots,
                f'Harmonic probe reference is not an input run: {probe_path}')
        probes.append((probe_path, probe_bytes, probe))
    records, inputs, curves, common, seen = [], [], {}, None, set()
    numerical_sources, common_numerical = {}, None
    for root in roots:
        manifest_bytes = (root/'run.json').read_bytes()
        manifest = json.loads(manifest_bytes)
        config_bytes = (root/'config.json').read_bytes()
        config, identity = manifest['config'], manifest['identity']
        require(json.loads(config_bytes) == config, f'Saved config mismatch: {root}')
        source_bytes = (root/'source.py').read_bytes()
        require(sha(source_bytes) == manifest['source_sha256']
                == identity['source_sha256'], f'Saved source hash mismatch: {root}')
        source_hash = manifest['source_sha256']
        if source_hash not in numerical_sources:
            numerical_sources[source_hash] = numerical_source(source_bytes)
        numerical = numerical_sources[source_hash]
        if common_numerical is not None:
            differing = sorted(name for name in set(numerical['definitions']) | set(common_numerical['definitions'])
                               if numerical['definitions'].get(name) != common_numerical['definitions'].get(name))
            require(not differing, f'Input runs differ in numerical definitions {differing}: {root}')
        common_numerical = numerical
        require(sha(json.dumps(identity, sort_keys=True, allow_nan=False).encode())
                == manifest['fingerprint'], f'Identity fingerprint mismatch: {root}')
        contract = copy.deepcopy(config)
        contract.pop('plots', None)
        contract['methods']['oblivious']['frozen_features'].pop('plot', None)
        for key in ('output', 'reuse_completed'):
            contract['execution'].pop(key, None)
        devices = contract['execution']['devices']
        if devices != 'auto':
            require((devices.split(',') if isinstance(devices, str) else devices)
                    == identity['config']['execution']['devices'], f'Device mismatch: {root}')
        contract['execution']['devices'] = identity['config']['execution']['devices']
        require(contract == identity['config'], f'Saved identity/config mismatch: {root}')
        architecture = {key: value for key, value in config['model'].items() if key != 'width'}
        comparison_contract = dict(dataset=config['dataset'], training=config['training'],
            architecture=architecture, data_sha256=identity['data_sha256'],
            dataset_file_sha256=identity['dataset_file_sha256'], numerical_source_sha256=numerical['sha256'],
            tf32=config['execution']['tf32'])
        require(common is None or comparison_contract == common,
                f'Input runs differ in source, dataset, training, depth or activation: {root}')
        common = comparison_contract
        n, seeds = config['model']['width'], config['seeds']
        require(isinstance(n, int) and not isinstance(n, bool) and n > 0 and n not in seen,
                f'Invalid or duplicate width: {n}')
        require(len(seeds) == 1 and isinstance(seeds[0], int) and not isinstance(seeds[0], bool),
                f'Exactly one seed per width is required: {root}')
        seen.add(n)
        seed, iid_name = seeds[0], f'dense_{n}'
        require(n in config['methods']['oblivious']['dense']['widths'],
                f'Missing requested independent width-{n} dense pair: {root}')
        expected = {f'legendre_{q}': 'legendre'
                    for q in config['methods']['oblivious']['legendre']['orders']}
        for family in ('harmonic', 'logarithmic'):
            expected.update({f"{family}_{budget['width']}_r{budget['source_rank']}": family
                             for budget in config['methods']['non_oblivious'][family]['budgets']})
        row = dict(width=n, seed=seed, root=str(root), status='inconclusive',
            dense_learned=(config['model']['depth']-1)*n*n+n*(config['dataset']['dimension']+1),
            candidates=[], selected={}, selected_minimum={}, budget_search={},
            dense_pair=None, sources={}, errors={}, omissions=[])
        records.append(row)
        provenance = dict(root=str(root), run_sha256=sha(manifest_bytes),
            config_sha256=sha(config_bytes), source_sha256=manifest['source_sha256'],
            numerical_source_sha256=numerical['sha256'],
            fingerprint=manifest['fingerprint'], config=config)
        inputs.append(provenance)
        relative = manifest['repetitions'].get(str(seed))
        if relative is None:
            row['omissions'].append('No saved repetition location')
            row['candidates'] = [dict(name=name, family=family, factor=args.factor, status='inconclusive',
                                     reason='No saved repetition', moving=None, fixed=None, total=None)
                                 for name, family in expected.items()]
            continue
        path = (root/relative).resolve()
        require(path != root and path.is_relative_to(root), f'Invalid repetition path: {relative}')
        if not (path/'report.json').is_file() or not (path/'trajectories.npz').is_file():
            row['omissions'].append('Missing report or trajectories')
            row['candidates'] = [dict(name=name, family=family, factor=args.factor, status='inconclusive',
                                     reason='Missing report or trajectories', moving=None, fixed=None, total=None)
                                 for name, family in expected.items()]
            continue
        report_bytes, trajectory_bytes = (path/'report.json').read_bytes(), (path/'trajectories.npz').read_bytes()
        report = json.loads(report_bytes)
        require(report['seed'] == seed and report['seeds']['reference'] == seed
                and report['fingerprint'] == manifest['fingerprint']
                and report['source_sha256'] == manifest['source_sha256'], f'Run identity mismatch: {path}')
        require(sha(trajectory_bytes) == report['trajectories_sha256'], f'Trajectory hash mismatch: {path}')
        provenance.update(repetition=str(path), report_sha256=sha(report_bytes),
                          trajectories_sha256=sha(trajectory_bytes), seeds=report['seeds'])
        if 'reused_from' in report:
            provenance['reused_from'] = copy.deepcopy(report['reused_from'])
        search = report.get('budget_search', {})
        require(isinstance(search, dict), f'Invalid budget search metadata: {path}')
        row['budget_search'] = copy.deepcopy(search)
        for family in families:
            if family not in search:
                continue
            require(isinstance(search[family], dict)
                    and isinstance(search[family].get('requested', []), list),
                    f'Invalid requested budget list: {path}/{family}')
            for budget in (search[family].get('inherited_requested', [])
                           + search[family].get('requested', [])):
                keys = ('order',) if family == 'legendre' else ('width', 'source_rank')
                require(isinstance(budget, dict)
                        and all(isinstance(budget.get(key), int)
                                and not isinstance(budget[key], bool) and budget[key] > 0
                                for key in keys), f'Invalid requested budget: {path}/{family}')
                name = (f"legendre_{budget['order']}" if family == 'legendre'
                        else f"{family}_{budget['width']}_r{budget['source_rank']}")
                expected[name] = family
        row['sources'], row['errors'] = report.get('sources', {}), report.get('errors', {})
        with np.load(io.BytesIO(trajectory_bytes), allow_pickle=False) as saved:
            arrays = {key: saved[key] for key in saved.files}

        def array(name, ndim):
            value = arrays[name]
            require(value.ndim == ndim and value.dtype.kind in 'fiu' and np.isfinite(value).all(),
                    f'Invalid array {name}: {path}')
            return value.astype(float)

        train, query = array('train_inputs', 2), array('query_inputs', 2)
        targets, truth = array('train_labels', 1), array('query_labels', 1)
        require(len(train) == len(targets) == config['dataset']['train_samples']
                and len(query) == len(truth) == config['dataset']['test_samples']
                and train.shape[1] == query.shape[1] == config['dataset']['dimension'],
                f'Data shape mismatch: {path}')
        hash_keys = set(identity['data_sha256'])
        base_keys = {'train_inputs', 'train_labels', 'query_inputs', 'query_labels'}
        require(base_keys.issubset(hash_keys)
                and hash_keys.issubset(base_keys | {'extra_query_inputs', 'extra_query_labels'}),
                f'Unexpected dataset hash keys: {path}')
        require({key: array_sha(arrays[key]) for key in hash_keys}
                == report['data_sha256'] == identity['data_sha256'], f'Data hash mismatch: {path}')
        for probe_path, probe_bytes, probe in probes:
            if Path(probe['reference_run']).resolve() != root:
                continue
            probe_config_bytes = (probe_path/'config.json').read_bytes()
            probe_config = json.loads(probe_config_bytes)
            command_config = Path(probe['command'][probe['command'].index('--config')+1])
            if not command_config.is_absolute():
                command_config = Path(probe['cwd'])/command_config
            original_probe_config = command_config.read_bytes()
            require(sha(original_probe_config) == probe['config_sha256']
                    and json.loads(original_probe_config) == probe_config,
                    f'Harmonic probe config mismatch: {probe_path}')
            config_reference = Path(probe_config['reference_run'])
            if not config_reference.is_absolute():
                config_reference = Path(probe['cwd'])/config_reference
            request = probe['request']
            require(config_reference.resolve() == root
                    and probe_config['cases'][probe['case']] == request
                    and probe_config['compact_width'] == probe['compact_width']
                    and all(isinstance(value, int) and not isinstance(value, bool) and value > 0
                            for value in (probe['compact_width'], request['source_rank'],
                                          request['spatial_degree'], request['time_degree'])),
                    f'Harmonic probe request mismatch: {probe_path}')
            require(probe['original_report_sha256'] == sha(report_bytes)
                    and probe['original_trajectories_sha256'] == sha(trajectory_bytes)
                    and probe['training'] == config['training']
                    and probe['architecture'] == config['model']
                    and probe['environment']['tf32'] == config['execution']['tf32']
                    and probe['seeds'] == {key: report['seeds'][key] for key in
                                          ('reference', 'harmonic_source', 'harmonic_selector')},
                    f'Harmonic probe reference identity mismatch: {probe_path}')
            probe_source_bytes = (probe_path/'source.py').read_bytes()
            probe_source_hash = sha(probe_source_bytes)
            require(probe_source_hash == probe['source_sha256'],
                    f'Harmonic probe source hash mismatch: {probe_path}')
            if probe_source_hash not in numerical_sources:
                numerical_sources[probe_source_hash] = numerical_source(probe_source_bytes)
            require(numerical_sources[probe_source_hash] == numerical,
                    f'Harmonic probe numerical definitions differ: {probe_path}')
            probe_trajectory_bytes = (probe_path/'trajectories.npz').read_bytes()
            require(sha(probe_trajectory_bytes) == probe['trajectories_sha256'],
                    f'Harmonic probe trajectory hash mismatch: {probe_path}')
            with np.load(io.BytesIO(probe_trajectory_bytes), allow_pickle=False) as saved:
                probe_arrays = {key: saved[key] for key in saved.files}
            for key in ('train_inputs', 'train_labels', 'query_inputs', 'reference',
                        'times_reference', iid_name, probe_config['baseline_model']):
                require(key in arrays and key in probe_arrays
                        and array_sha(probe_arrays[key]) == array_sha(arrays[key]),
                        f'Harmonic probe changed reference array {key}: {probe_path}')
            name = (f"harmonic_{probe['compact_width']}_r{request['source_rank']}"
                    f"_s{request['spatial_degree']}_t{request['time_degree']}_{sha(probe_bytes)[:12]}")
            require(name not in expected, f'Duplicate Harmonic probe candidate: {probe_path}')
            expected[name] = 'harmonic'
            probe_provenance = dict(path=str(probe_path), name=name, case=probe['case'], request=request,
                report_sha256=sha(probe_bytes), config_sha256=probe['config_sha256'],
                config_snapshot_sha256=sha(probe_config_bytes), source_sha256=probe_source_hash,
                numerical_source_sha256=numerical['sha256'], trajectories_sha256=probe['trajectories_sha256'],
                reference_run=str(root), original_report_sha256=probe['original_report_sha256'],
                original_trajectories_sha256=probe['original_trajectories_sha256'],
                status=probe['status'], source=probe.get('source'), source_hashes=probe.get('source_hashes'))
            provenance.setdefault('harmonic_probes', []).append(probe_provenance)
            row.setdefault('harmonic_probes', []).append(name)
            used_probes.add(probe_path)
            if 'model' in probe:
                require(probe['initial_state_sha256'] == report['reference_initial_state_sha256']
                        and not any(item['truncated'] for item in probe['model']['diagnostics']['source_truncations']),
                        f'Harmonic probe initialization or truncation mismatch: {probe_path}')
                model = copy.deepcopy(probe['model'])
                model['moving'] = model.pop('learned')
                model.update(family='harmonic', width=probe['compact_width'],
                             source_rank=request['source_rank'], spatial_degree=request['spatial_degree'],
                             time_degree=request['time_degree'], provenance=probe_provenance)
                report['models'][name] = model
            if probe.get('run', {}).get('complete') is True and probe['status'] in ('pass', 'fail'):
                require('model' in probe and np.array_equal(probe_arrays['times'], arrays['times_reference']),
                        f'Harmonic probe completion or time mismatch: {probe_path}')
                report['runs'][name] = probe['run']
                arrays[name], arrays['times_'+name] = probe_arrays['prediction'], probe_arrays['times']
            else:
                report.setdefault('errors', {})[name] = probe.get('reason', 'Harmonic probe incomplete')
        checked = {}
        for name in ('reference', iid_name, *expected):
            model = report['models'].get(name)
            if model is None:
                continue
            require(all(isinstance(model.get(key), int) and not isinstance(model[key], bool)
                        and model[key] >= 0 for key in ('moving', 'fixed', 'total'))
                    and model['moving'] > 0 and model['total'] == model['moving']+model['fixed'],
                    f'Invalid storage counts: {path}/{name}')
            require(model['family'] == ('reference' if name == 'reference' else
                    'dense' if name == iid_name else expected[name]), f'Wrong model family: {path}/{name}')
            if name in ('reference', iid_name):
                require(model['moving'] == row['dense_learned'] and model['fixed'] == 0,
                        f'Dense storage mismatch: {path}/{name}')
            run = report['runs'].get(name, {})
            if run.get('complete') is not True:
                continue
            prediction, times = array(name, 2), array('times_'+name, 1)
            require(len(times) > 1 and times[0] == 0 and np.all(np.diff(times) > 0)
                    and np.isclose(times[-1], config['training']['horizon'], atol=1e-10, rtol=0)
                    and prediction.shape == (len(times), len(targets)+len(truth)),
                    f'Trajectory shape or time mismatch: {path}/{name}')
            run_times, losses = np.asarray(run['times']), np.asarray(run['losses'])
            require(run_times.shape == times.shape and np.allclose(run_times, times, atol=1e-10, rtol=0)
                    and losses.shape == times.shape and np.isfinite(losses).all()
                    and np.allclose(np.mean((prediction[:, :len(targets)]-targets)**2, axis=1),
                                    losses, atol=1e-6, rtol=2e-5), f'Run metadata mismatch: {path}/{name}')
            checked[name] = (prediction[:, len(targets):], times)
        for family in ('harmonic', 'logarithmic'):
            if family in row['sources']:
                saved_setup = dict(row['sources'][family]['effective_setup'])
                expected_setup = dict(_experiment_setup(config, family))
                saved_setup.setdefault('selection_strategy', 'uniform')
                expected_setup.setdefault('selection_strategy', 'uniform')
                require(saved_setup == expected_setup,
                        f'Source setup mismatch: {path}/{family}')
        paired = 'reference' in checked and iid_name in checked
        if paired:
            require(report['seeds'].get(iid_name) == _experiment_seed(seed, iid_name)
                    and report['seeds'][iid_name] != seed,
                    f'Independent dense-pair seed mismatch: {path}')
            reference, reference_times = checked['reference']
            for name, (prediction, times) in checked.items():
                require(times.shape == reference_times.shape
                        and np.allclose(times, reference_times, atol=1e-10, rtol=0),
                        f'Paired time grids differ: {path}/{name}')
            width_curves = {name: np.sqrt(np.mean((prediction-reference)**2, axis=1))
                            for name, (prediction, _) in checked.items()}
            require(all(np.isfinite(value).all() for value in width_curves.values()),
                    f'Nonfinite query RMS: {path}')
            curves[n] = (reference_times, width_curves)
            iid = width_curves[iid_name]
            row['dense_pair'] = dict(name=iid_name, endpoint_rms=float(iid[-1]),
                worst_recorded_rms=float(iid.max()), reference_seed=seed,
                independent_seed=report['seeds'][iid_name], moving=row['dense_learned'], fixed=0,
                total=row['dense_learned'])
            row['status'] = 'paired_reference_complete'
        else:
            row['omissions'].append('No complete reference and independent dense pair')
        for name, family in expected.items():
            model = report['models'].get(name, {})
            candidate = dict(name=name, family=family, factor=args.factor, status='inconclusive',
                **{key: model.get(key) for key in ('moving', 'fixed', 'total')}, model=model or None)
            row['candidates'].append(candidate)
            if name in report.get('skipped', {}):
                candidate.update(status='skipped', reason=report['skipped'][name])
                continue
            if not paired or name not in checked:
                candidate['reason'] = (report.get('errors', {}).get(name)
                    or report.get('errors', {}).get(family+'_setup')
                    or ('No complete paired benchmark' if not paired else 'Candidate not complete or not yet run'))
                continue
            curve = width_curves[name]
            endpoint, worst = float(curve[-1]), float(curve.max())
            endpoint_threshold, worst_threshold = args.factor*float(iid[-1]), args.factor*float(iid.max())
            endpoint_pass, worst_pass = endpoint <= endpoint_threshold, worst <= worst_threshold
            positive = (reference_times > 0) & (iid > 0)
            zero_later = (reference_times > 0) & (iid == 0)
            candidate.update(status='pass' if endpoint_pass and worst_pass else 'fail',
                endpoint_rms=endpoint, worst_recorded_rms=worst,
                endpoint_threshold=endpoint_threshold, worst_recorded_threshold=worst_threshold,
                endpoint_pass=bool(endpoint_pass), worst_recorded_pass=bool(worst_pass),
                endpoint_ratio=endpoint/float(iid[-1]) if iid[-1] > 0 else None,
                worst_recorded_ratio=worst/float(iid.max()) if iid.max() > 0 else None,
                pointwise_exceedance_fraction=float(np.mean(curve[positive] > iid[positive]))
                    if np.any(positive) else None,
                pointwise_factor_exceedance_fraction=float(np.mean(curve[positive] > args.factor*iid[positive]))
                    if np.any(positive) else None,
                pointwise_max_ratio=float(np.max(curve[positive]/iid[positive])) if np.any(positive) else None,
                pointwise_positive_benchmark_count=int(positive.sum()),
                pointwise_zero_benchmark_after_initial_count=int(zero_later.sum()),
                pointwise_zero_benchmark_after_initial_exceedances=int(np.sum(curve[zero_later] > 0)))
        for family in families:
            passing = [item for item in row['candidates'] if item['family'] == family and item['status'] == 'pass']
            if passing:
                chosen = min(passing, key=lambda item: (item['moving'], item['total'], item['name']))
                row['selected'][family] = chosen['name']
                row['selected_minimum'][family] = {
                    key: chosen[key] for key in ('name', 'moving', 'fixed', 'total')}
            else:
                row['omissions'].append(f'{family}: no complete candidate passes both {args.factor:g}x benchmark metrics')

    require(used_probes == set(probe_paths), 'Some Harmonic probes lacked a complete saved reference run')
    records.sort(key=lambda item: item['width'])
    show_legendre_guide = not any(row['budget_search'] for row in records)
    parent = args.out.resolve()/'plots'
    parent.mkdir(parents=True, exist_ok=True)
    index = 1
    while True:
        destination = parent/f'plot_{index:03d}'
        try:
            destination.mkdir()
            break
        except FileExistsError:
            index += 1
    caption = ('Each width uses one independent dense pair and its own reference on the same held-out query inputs. '
        'A candidate passes only when its endpoint RMS and maximum recorded RMS are each no larger than '
        f'{args.factor:g} times the corresponding dense-pair metric. The smallest tested passing moving state '
        'is selected per family; this is not a proven global minimum. Missing passing candidates are omitted. '
        'Incomplete runs and constructor failures are inconclusive; skipped larger candidates are not failures. '
        'Endpoint and maximum-error matching does not imply pointwise matching. The separately reported '
        'pointwise exceedance fraction and maximum pointwise ratio use the unscaled (1x) positive dense-pair '
        f'errors after the initial time; exceedance at {args.factor:g}x is also reported separately. Zero benchmarks '
        'after initialization are counted separately. Moving, fixed and total counts refer to retained model '
        'coordinates, excluding common data, integrator workspace and offline source construction. '
        'Logarithmic setup uses query inputs but not their labels. Candidate selection uses these query errors; '
        f'there is no independent post-selection test. {len(roots)} selected or tuned width points are not asymptotic proof. '
        'Finite recorded Euler trajectories are not a gradient-flow refinement certificate.')
    if probe_paths:
        caption += (' Additional Harmonic candidates use the separately recorded spatial and temporal source orders. '
                    'Their compact widths were not bracket-refined; selected points are the smallest tested passing sizes. '
                    'Earlier budget-search brackets refer only to their original source setup.')
    caption += (' Hollow storage markers identify construction-limited selected witnesses: '
                'the nearby smaller candidate was inconclusive, not a measured accuracy failure. '
                'Such passing witnesses remain included in descriptive fits.')
    if show_legendre_guide:
        caption += (' The dotted n^(5/4) guide is anchored at the first passing Legendre point '
                    'and is not a fitted exponent.')
    colors = {key: value[1] for key, value in families.items()}
    plt.rcParams.update({'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False,
                         'pdf.fonttype': 42, 'savefig.facecolor': 'white'})
    def save(figure, name):
        for suffix in ('png', 'pdf'):
            figure.savefig(destination/f'{name}.{suffix}', bbox_inches='tight', dpi=190)
        plt.close(figure)

    def selected(row, family):
        return next((item for item in row['candidates']
                     if item['name'] == row['selected'].get(family)), None)

    widths = [row['width'] for row in records]
    descriptive_fits = {}
    figure, axis = plt.subplots(figsize=(7.8, 5.3))
    axis.loglog(widths, [row['dense_learned'] for row in records], 'o-', color='#40566c', label='Dense')
    for family, (label, color) in families.items():
        points = [(row['width'], selected(row, family)) for row in records]
        points = [(width, point) for width, point in points if point is not None]
        if points:
            axis.loglog(widths, [selected(row, family)['moving'] if selected(row, family) else np.nan
                                for row in records],
                        'o-', color=color, label=label)
            for row in records:
                if (selected(row, family) is not None and row['budget_search'].get(family, {})
                        .get('bracket', {}).get('status') == 'inconclusive_lower'):
                    axis.plot(row['width'], selected(row, family)['moving'], 'o',
                              markerfacecolor='white', markeredgecolor=color, markeredgewidth=1.6, zorder=5)
        missing = []
        for row in records:
            if selected(row, family) is not None:
                continue
            completed = [p for p in row['candidates'] if p['family'] == family and p['status'] == 'fail']
            if completed:
                missing.append((row['width'], max(p['moving'] for p in completed)))
        if missing:
            axis.scatter([p[0] for p in missing], [p[1] for p in missing], marker='x', color=color,
                         label=f'{label}: no tested pass')
        if family == 'legendre' and points and show_legendre_guide:
            anchor_width, anchor = points[0]
            guide_widths = np.geomspace(min(widths), max(widths), 100)
            axis.loglog(guide_widths, anchor['moving']*(guide_widths/anchor_width)**1.25,
                        ':', color='#777777', label=r'$n^{5/4}$')
        if args.fit_log_powers and family in ('harmonic', 'logarithmic'):
            fit_points = [(width, point) for width, point in points if width > 1]
            included = [width for width, _ in fit_points]
            fit = dict(status='insufficient_passing_widths', count=len(fit_points), widths=included,
                       omitted_widths=[width for width in widths if width not in included],
                       model='moving = C * (natural_log(width)) ** p',
                       criterion='unweighted least squares of log(moving) against log(log(width))',
                       scope='Exploratory fit of selected candidates; neither unbiased scaling estimation nor asymptotic proof')
            descriptive_fits[family] = fit
            if len(fit_points) >= 3 and len(fit_points) < len(widths):
                fit['status'] = 'missing_passing_widths'
            if len(fit_points) >= 3 and len(fit_points) == len(widths):
                fit_widths = np.asarray(included, dtype=float)
                fit_storage = np.asarray([point['moving'] for _, point in fit_points], dtype=float)
                design = np.column_stack((np.ones(len(fit_points)), np.log(np.log(fit_widths))))
                log_constant, exponent = np.linalg.lstsq(design, np.log(fit_storage), rcond=None)[0]
                constant = float(np.exp(log_constant))
                fit.update(status='fitted', C=constant, p=float(exponent), log_C=float(log_constant),
                           log_space_rms=float(np.sqrt(np.mean((design@np.array([log_constant, exponent])
                                                               -np.log(fit_storage))**2))))
                fit_grid = np.geomspace(min(included), max(included), 150)
                axis.loglog(fit_grid, np.exp(log_constant+exponent*np.log(np.log(fit_grid))),
                            '--', color=color, alpha=.8,
                            label=f'{label} fit p={exponent:.2g} ({len(fit_points)} widths)')
    axis.set_xlabel('Dense width')
    axis.set_ylabel('Learned state')
    axis.set_xticks(widths, [str(width) for width in widths])
    axis.xaxis.set_minor_formatter(NullFormatter())
    dataset_label = ('Circle' if common['dataset']['name'] == 'sphere'
                     and common['dataset']['dimension'] == 2 else
                     'Digits '+ ' / '.join(map(str, common['dataset']['digit_pair']))
                     if common['dataset']['name'] == 'digits' else 'Width scaling')
    axis.set_title(f'{dataset_label} · {args.factor:g}× variability')
    axis.grid(alpha=.15)
    axis.legend(frameon=False)
    fit_counts = ', '.join(f"{families[family][0]} {fit['count']}/{len(widths)} widths"
                          for family, fit in descriptive_fits.items())
    figure.tight_layout()
    save(figure, 'storage_vs_width')
    largest = max(curves) if curves else None
    figure, axis = plt.subplots(figsize=(7.8, 5.1))
    if largest is None:
        axis.text(.5, .5, 'No complete reference and independent dense pair', transform=axis.transAxes, ha='center')
    else:
        times, width_curves = curves[largest]
        row = next(item for item in records if item['width'] == largest)
        axis.plot(times, width_curves[f'dense_{largest}'], '--', color='#40566c', label='Dense pair')
        for family, (label, color) in families.items():
            point = selected(row, family)
            if point:
                axis.plot(times, width_curves[point['name']], color=color, label=label)
        axis.legend(frameon=False)
        axis.set_title(f'n = {largest}')
    axis.set_xlabel('Training time')
    axis.set_ylabel('Test RMS')
    axis.set_ylim(bottom=0)
    axis.grid(alpha=.15)
    figure.tight_layout()
    save(figure, 'trajectory_errors')
    figure, axes = plt.subplots(1, 2, figsize=(10, 4.4))
    for axis, metric, label in zip(axes, ('endpoint_ratio', 'worst_recorded_ratio'),
                                   ('Endpoint / dense pair', 'Maximum / dense pair')):
        for family, (name, color) in families.items():
            points = [(row['width'], selected(row, family)) for row in records]
            points = [(width, point[metric]) for width, point in points
                      if point is not None and point[metric] is not None]
            if points:
                axis.plot([p[0] for p in points], [p[1] for p in points], 'o-', color=color, label=name)
        axis.axhline(1, color='#999999', ls=':', lw=1, label='Dense pair')
        axis.axhline(args.factor, color='#555555', ls='--', lw=1,
                     label=f'{args.factor:g}× threshold')
        axis.set_xscale('log')
        axis.set_xticks(widths, [str(width) for width in widths], rotation=30)
        axis.xaxis.set_minor_formatter(NullFormatter())
        axis.set_xlabel('Dense width')
        axis.set_ylabel(label)
        axis.set_ylim(bottom=0)
        axis.grid(alpha=.15)
    handles, labels = axes[0].get_legend_handles_labels()
    if handles:
        figure.legend(handles, labels, loc='upper center', ncol=3, frameon=False, fontsize=8)
    figure.tight_layout(rect=(0, 0, 1, .85 if handles else 1))
    save(figure, 'errors_vs_width')
    caption += (' Crosses mark the largest completed failing budget where no passing candidate was found; '
        'they are not passing sizes or lower bounds on a global optimum. Lines do not bridge missing passes. ')
    caption += (' Optional dashed curves fit C(log n)^p by unweighted least squares of log(moving state) '
        'against log(log n), with natural logarithms, at least three widths and a pass at every included width. '
        'They are exploratory fits to selected candidates, not unbiased scaling estimates or asymptotic proof. '
        'No exponent is fitted for a family with a missing passing width. Fit eligibility: '+fit_counts+'.'
        if args.fit_log_powers else ' No logarithmic-power trend law is fitted.')
    legendre_points = [(row['width'], selected(row, 'legendre')) for row in records
                       if selected(row, 'legendre') is not None]
    guide = (dict(exponent=1.25, anchor_width=legendre_points[0][0],
                  anchor_moving=legendre_points[0][1]['moving'], fitted=False)
             if legendre_points and show_legendre_guide else None)
    summary = dict(scope=caption, factor=args.factor, plot_source_sha256=sha(Path(__file__).read_bytes()),
        inputs=inputs, common_contract=common, numerical_sources=numerical_sources,
        widths=widths, expected_width_count=len(roots),
        available_width_count=len(records), complete_pair_width_count=len(curves),
        descriptive_log_power_fits=descriptive_fits,
        trajectory_figure_width=largest, records=records,
        figures={name: {suffix: str(destination/f'{name}.{suffix}') for suffix in ('png', 'pdf')}
                 for name in ('storage_vs_width', 'trajectory_errors', 'errors_vs_width')})
    if show_legendre_guide:
        summary['legendre_slope_guide'] = guide
    save_json(destination/'metrics.json', summary)
    (destination/'captions.txt').write_text(caption+'\n\n'+json.dumps(
        {str(row['width']): row['omissions'] for row in records}, indent=2)+'\n')
    print(json.dumps(dict(figures=str(destination), metrics=str(destination/'metrics.json'),
                         widths=widths, complete_pairs=len(curves))), flush=True)
    return 0


def experiment_plot(config):
    """Validate saved runs and plot paired test errors without training."""
    import copy
    import hashlib
    import io
    import json
    from pathlib import Path
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    output_root = Path(config['execution']['output']).resolve()
    options = config.get('plots', {})
    metrics = options.get('metrics', ['endpoint_rms', 'worst_recorded_rms'])
    aggregate, spread = options.get('aggregate', 'median'), options.get('spread', 'range')
    labels = dict(endpoint_rms='Endpoint test RMS from paired reference',
                  worst_recorded_rms='Worst recorded test RMS from paired reference',
                  test_truth_mse='Endpoint test MSE against target')
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    require(isinstance(metrics, list) and metrics and len(set(metrics)) == len(metrics)
            and all(metric in ('endpoint_rms', 'worst_recorded_rms') for metric in metrics), 'Invalid plot metrics')
    require(aggregate in ('mean', 'median') and spread in ('range', 'sd', 'none')
            and (spread != 'sd' or aggregate == 'mean'), 'Invalid plot aggregation')
    frozen_style = config.get('methods', {}).get('oblivious', {}).get('frozen_features', {}).get('plot', 'dashed')
    require(frozen_style in ('dashed', 'point'), 'Invalid frozen-features plot style')
    families = dict(dense=('Dense', '#40566c'), legendre=('Legendre', '#d18624'),
                    harmonic=('Harmonic', '#297c8e'), logarithmic=('Logarithmic', '#9768b0'),
                    low_rank=('Low rank', '#648d4f'), frozen_features=('Frozen features', '#777777'))
    methods = options.get('methods', list(families))
    run_paths = options.get('runs', [])
    require(isinstance(methods, list) and methods and len(set(methods)) == len(methods)
            and all(method in families for method in methods), 'Invalid plot methods')
    require(isinstance(run_paths, list) and all(isinstance(path, str) and path for path in run_paths),
            'plots.runs must be a list of nonempty paths')
    roots = [Path(path).resolve() for path in run_paths] if run_paths else [output_root]
    require(len(set(roots)) == len(roots), 'Duplicate input run')
    repetitions, inputs, common_contract = {}, [], None
    for root in roots:
        manifest_bytes = (root/'run.json').read_bytes()
        manifest = json.loads(manifest_bytes)
        saved_config = manifest['config']
        config_bytes = (root/'config.json').read_bytes()
        require(json.loads(config_bytes) == saved_config, f'Saved config mismatch: {root}')
        identity = manifest['identity']
        require(sha((root/'source.py').read_bytes()) == manifest['source_sha256']
                == identity['source_sha256'], f'Saved source hash mismatch: {root}')
        require(sha(json.dumps(identity, sort_keys=True, allow_nan=False).encode()) == manifest['fingerprint'],
                f'Identity fingerprint mismatch: {root}')
        # Execution placement and plotting options are not scientific settings.
        saved_contract = copy.deepcopy(saved_config)
        saved_contract.pop('plots')
        saved_contract['methods']['oblivious']['frozen_features'].pop('plot')
        for key in ('output', 'reuse_completed'):
            saved_contract['execution'].pop(key)
        devices = saved_contract['execution']['devices']
        if devices != 'auto':
            require((devices.split(',') if isinstance(devices, str) else devices)
                    == identity['config']['execution']['devices'], f'Saved device config mismatch: {root}')
        saved_contract['execution']['devices'] = identity['config']['execution']['devices']
        require(saved_contract == identity['config'], f'Saved identity/config mismatch: {root}')
        selected_settings = {}
        for method in methods:
            if method in ('harmonic', 'logarithmic'):
                settings = dict(saved_config['methods']['non_oblivious'][method])
                settings['setup'] = _experiment_setup(saved_config, method)
            else:
                settings = dict(saved_config['methods']['oblivious'][method])
                settings.pop('plot', None)
            selected_settings[method] = settings
        contract = dict(source_sha256=manifest['source_sha256'],
            **{key: saved_config[key] for key in ('dataset', 'model', 'training')},
            methods=selected_settings,
            execution={key: saved_config['execution'][key] for key in ('tf32', 'seconds_per_fit')},
            identity={key: identity[key] for key in ('dataset_file_sha256', 'data_sha256', 'python', 'torch', 'numpy')})
        require(common_contract is None or contract == common_contract,
                f'Input runs differ in source, data, training or selected method settings: {root}')
        common_contract = contract
        seeds, locations = saved_config['seeds'], manifest['repetitions']
        require(isinstance(seeds, list) and seeds and len(seeds) == len(set(seeds))
                and all(isinstance(seed, int) and not isinstance(seed, bool) and seed >= 0 for seed in seeds)
                and isinstance(locations, dict) and set(locations) <= {str(seed) for seed in seeds},
                f'Invalid requested repetitions: {root}')
        require(not set(map(str, seeds)) & set(repetitions), f'Duplicate repetition seeds across input runs: {root}')
        repetitions.update({str(seed): (root, manifest, locations.get(str(seed))) for seed in seeds})
        inputs.append(dict(root=str(root), run_sha256=sha(manifest_bytes), config_sha256=sha(config_bytes),
            source_sha256=manifest['source_sha256'], fingerprint=manifest['fingerprint'], seeds=seeds))
    rows, omissions, errors, provenance = [], [], {}, {}
    for seed, (root, manifest, relative) in repetitions.items():
        if relative is None:
            omissions.append(dict(seed=int(seed), reason='Missing repetition location'))
            continue
        path = (root/relative).resolve()
        require(path.is_relative_to(root) and path != root, f'Invalid repetition path: {relative}')
        if not (path/'report.json').is_file() or not (path/'trajectories.npz').is_file():
            omissions.append(dict(seed=int(seed), reason='Missing report or trajectories'))
            continue
        report_bytes = (path/'report.json').read_bytes()
        report = json.loads(report_bytes)
        require(report['seed'] == int(seed) and report['fingerprint'] == manifest['fingerprint']
                and report['source_sha256'] == manifest['source_sha256'], f'Run identity mismatch: {relative}')
        trajectory_bytes = (path/'trajectories.npz').read_bytes()
        require(hashlib.sha256(trajectory_bytes).hexdigest()
                == report['trajectories_sha256'], f'Trajectory hash mismatch: {relative}')
        require(report['seeds']['reference'] == int(seed), f'Paired reference seed mismatch: {relative}')
        provenance[seed] = dict(root=str(root), repetition=str(path), report_sha256=sha(report_bytes),
            trajectories_sha256=report['trajectories_sha256'], seeds=report['seeds'],
            fingerprint=report['fingerprint'], source_sha256=report['source_sha256'])
        errors[seed] = report.get('errors', {})
        with np.load(io.BytesIO(trajectory_bytes), allow_pickle=False) as saved:
            arrays = {name: saved[name] for name in saved.files}
        def array(name, dimensions):
            value = arrays[name]
            require(value.ndim == dimensions and value.dtype.kind in 'fiu'
                    and np.isfinite(value).all(), f'Invalid {name}: {relative}')
            return value.astype(float)
        train, query = array('train_inputs', 2), array('query_inputs', 2)
        targets, truth = array('train_labels', 1), array('query_labels', 1)
        data_hashes = {key: array_sha(arrays[key]) for key in
                       ('train_inputs', 'train_labels', 'query_inputs', 'query_labels')}
        require(data_hashes == report['data_sha256'] == manifest['identity']['data_sha256'],
                f'Data array hash mismatch: {relative}')
        require(len(targets) > 0 and len(truth) > 0 and len(train) == len(targets)
                and len(query) == len(truth) and train.shape[1] == query.shape[1] > 0,
                f'Data shape mismatch: {relative}')
        checked = {}
        for name, model in report['models'].items():
            if model['family'] not in (*methods, 'reference'):
                continue
            run = report['runs'].get(name, {})
            if run.get('complete') is not True:
                omissions.append(dict(seed=int(seed), model=name, reason='Incomplete model run'))
                continue
            prediction, times = array(name, 2), array('times_'+name, 1)
            require(len(times) > 0 and times[0] == 0 and np.all(np.diff(times) > 0)
                    and np.isclose(times[-1], manifest['config']['training']['horizon'], atol=1e-10, rtol=0)
                    and prediction.shape == (len(times), len(targets)+len(truth)),
                    f'Trajectory shape or time mismatch: {relative}/{name}')
            recorded_times, losses = np.asarray(run['times']), np.asarray(run['losses'])
            require(recorded_times.shape == times.shape and np.isfinite(recorded_times).all()
                    and np.allclose(times, recorded_times, atol=1e-10, rtol=0)
                    and losses.shape == times.shape and np.isfinite(losses).all()
                    and np.allclose(np.mean((prediction[:, :len(targets)]-targets)**2, axis=1),
                                    losses, atol=1e-6, rtol=2e-5),
                    f'Recorded times or training MSE mismatch: {relative}/{name}')
            require(model['family'] in (*families, 'reference')
                    and all(isinstance(model[key], int) and not isinstance(model[key], bool)
                            and model[key] >= 0 for key in ('moving', 'fixed', 'total'))
                    and model['moving'] > 0 and model['total'] == model['moving']+model['fixed'],
                    f'Invalid storage counts: {relative}/{name}')
            checked[name] = (prediction[:, len(targets):], times)
        for method in set(methods) & {'harmonic', 'logarithmic'}:
            if method in report.get('sources', {}):
                require(report['sources'][method]['effective_setup'] == _experiment_setup(manifest['config'], method),
                        f'Recorded source setup mismatch: {relative}/{method}')
        require(not set(report['runs'])-set(report['models']), f'Missing model metadata: {relative}')
        omissions.extend(dict(seed=int(seed), model=name, reason=reason)
                         for name, reason in report.get('errors', {}).items() if name not in report['models'])
        if 'reference' not in checked:
            omissions.append(dict(seed=int(seed), reason='No complete paired reference'))
            continue
        reference, reference_times = checked['reference']
        require(report['models']['reference']['family'] == 'reference', f'Invalid reference: {relative}')
        for name, (prediction, times) in checked.items():
            require(times.shape == reference_times.shape
                    and np.allclose(times, reference_times, atol=1e-10, rtol=0),
                    f'Paired time grids differ: {relative}/{name}')
            curve = np.sqrt(np.mean((prediction-reference)**2, axis=1))
            scores = dict(endpoint_rms=float(curve[-1]), worst_recorded_rms=float(curve.max()),
                          test_truth_mse=float(np.mean((prediction[-1]-truth)**2)))
            require(all(np.isfinite(value) for value in scores.values()), f'Nonfinite metrics: {relative}/{name}')
            rows.append(dict(seed=int(seed), name=name, model=report['models'][name], **scores))
    groups = {}
    for row in rows:
        model = row['model']
        if model['family'] != 'reference':
            key = (row['name'], model['family'], model['moving'], model['fixed'], model['total'])
            groups.setdefault(key, []).append(row)
    require(bool(groups), 'No complete models with a complete paired reference to plot')
    points = []
    for (name, family, moving, fixed, total), values in groups.items():
        point = dict(name=name, family=family, moving=moving, fixed=fixed, total=total,
                     count=len(values), requested=len(repetitions), seeds=[row['seed'] for row in values])
        for metric in labels:
            scores = np.asarray([row[metric] for row in values])
            point[metric] = dict(value=float(getattr(np, aggregate)(scores)),
                                 minimum=float(scores.min()), maximum=float(scores.max()),
                                 sample_sd=float(scores.std(ddof=1)) if len(scores) > 1 else None)
        points.append(point)

    def interval(score):
        if spread == 'range':
            return score['minimum'], score['maximum']
        if spread == 'sd' and score['sample_sd'] is not None:
            return score['value']-score['sample_sd'], score['value']+score['sample_sd']
        return None

    parent = output_root/'plots'
    parent.mkdir(parents=True, exist_ok=True)
    index = 1
    while True:
        destination = parent/f'plot_{index:03d}'
        try:
            destination.mkdir()
            break
        except FileExistsError:
            index += 1
    counts = [point['count'] for point in points]
    caption = (f'{aggregate.capitalize()} of per-repetition scores; {min(counts)}–{max(counts)} of '
               f'{len(repetitions)} requested repetitions per point. '
               'Each model is compared with its own repetition reference on held-out query inputs. '
               'Endpoint RMS uses the final recorded time; worst recorded RMS is the largest query RMS '
               'over the saved time grid. Test truth MSE uses the final query predictions. '
               + ('Bars show observed minimum–maximum ranges, not confidence intervals. ' if spread == 'range' else '')
               + ('Bars show mean plus/minus one sample standard deviation (ddof=1) of the individual '
                  'scores, not standard errors or confidence intervals; no SD bar is drawn for a single score. '
                  if spread == 'sd' else '')
               + 'Nonpositive scores and error bars reaching nonpositive values are omitted from logarithmic plots. '
               'Frozen-features learned state counts the primal readout; executed dual storage is '
               'reported separately in each model record in metrics.json. Fixed storage is listed below.\n')
    caption += '\nname | learned | fixed | total | repetitions\n'
    caption += '\n'.join(f"{p['name']} | {p['moving']} | {p['fixed']} | {p['total']} | {p['count']}/{p['requested']}"
                         for p in sorted(points, key=lambda p: (p['family'], p['moving'])))
    caption += '\n\nOmissions: '+json.dumps(omissions)+'\n'
    for metric in metrics:
        figure, axis = plt.subplots(figsize=(7.2, 4.8))
        for family, (label, color) in families.items():
            selected = sorted((p for p in points if p['family'] == family and p[metric]['value'] > 0),
                              key=lambda p: (p['moving'], p['name']))
            if not selected:
                continue
            if family == 'frozen_features' and frozen_style == 'dashed':
                score = selected[0][metric]
                axis.axhline(score['value'], color=color, label=label, linestyle='--', linewidth=1.5)
                bounds = interval(score)
                if bounds is not None and bounds[0] > 0:
                    axis.axhspan(*bounds, color=color, alpha=.08)
                continue
            style = 'None' if family == 'frozen_features' else '-'
            axis.plot([p['moving'] for p in selected], [p[metric]['value'] for p in selected],
                      color=color, label=label, linestyle=style, marker='o', markersize=4, linewidth=1.5)
            for p in selected:
                if p['count'] < p['requested']:
                    axis.annotate(f"{p['count']}/{p['requested']} seeds", (p['moving'], p[metric]['value']),
                                  xytext=(5, 7), textcoords='offset points', fontsize=7, color=color)
            if spread != 'none':
                for p in selected:
                    score = p[metric]
                    bounds = interval(score)
                    if bounds is not None and bounds[0] > 0:
                        axis.errorbar(p['moving'], score['value'],
                                      yerr=[[score['value']-bounds[0]], [bounds[1]-score['value']]],
                                      fmt='none', color=color, capsize=2, linewidth=.8)
        axis.set(xscale='log', yscale='log', xlabel='Learned state', ylabel='Test RMS',
                 title='Endpoint' if metric == 'endpoint_rms' else 'Worst over time')
        axis.grid(alpha=.17)
        if axis.lines:
            axis.legend(frameon=False, fontsize=9)
        else:
            axis.text(.5, .5, 'All recorded scores are zero', ha='center', transform=axis.transAxes)
        figure.tight_layout()
        for extension in ('png', 'pdf'):
            figure.savefig(destination/f'{metric}.{extension}', dpi=180)
        plt.close(figure)
    identity_fields = dict(source_sha256=common_contract['source_sha256'])
    if len(inputs) == 1:
        identity_fields['fingerprint'] = inputs[0]['fingerprint']
    plot_source = Path(__file__).read_bytes()
    (destination/'plot_source.py').write_bytes(plot_source)
    (destination/'plot_config.json').write_text(json.dumps(config, indent=2, allow_nan=False)+'\n')
    (destination/'metrics.json').write_text(json.dumps(dict(
        **identity_fields, input_runs=inputs, repetition_provenance=provenance,
        selected_methods=methods, comparison_contract=common_contract, plot_source_sha256=sha(plot_source),
        aggregate=aggregate, spread=spread, requested_repetitions=len(repetitions),
        points=points, runs=rows, omissions=omissions, errors=errors), indent=2, allow_nan=False)+'\n')
    (destination/'caption.txt').write_text(caption)
    print(json.dumps(dict(figures=str(destination), repetitions=len(repetitions), points=len(points))), flush=True)
    return 0


# The single configuration schema also supplies defaults and CLI options. Lists
# are replaced, dictionaries are merged; an empty order/budget list disables a method.
EXPERIMENT_DEFAULTS = {
    'dataset': dict(name='sphere', dimension=3, train_samples=8, test_samples=30,
                    seed=47, digit_pair=[1, 7], file=None, label_scale=1., undeclared_samples=0,
                    cache=None, download=False),
    'model': dict(width=4096, depth=2, activation='tanh'),
    'seeds': [601],
    'training': dict(solver='euler', step=.0015625, horizon=32., record_every=320, dtype='float32'),
    'methods': {
        'oblivious': dict(dense=dict(widths=[424, 4096], match_compressions=False), legendre=dict(orders=[3]),
                          low_rank=dict(ranks=[24], match_compressions=False),
                          frozen_features=dict(enabled=True, plot='dashed')),
        'non_oblivious': {
            'setup': dict(initializer='dense_rollout', rollout_solver='rk4', rollout_step=.125,
                          rollout_dtype='float32', coefficient_dtype='float64', time_degree=8,
                          selection_trials=64, condition_limit=16., selection_strategy='uniform'),
            'harmonic': dict(budgets=[dict(width=424, source_rank=29)], spatial_degree=5),
            'logarithmic': dict(budgets=[dict(width=424, source_rank=29)], test_inputs_at_setup=True,
                                panel_span=False)}},
    'execution': dict(devices='auto', tf32=False, seconds_per_fit=120., dense_seconds_per_fit=120., reuse_completed=True,
                      stop_after_match=False,
                      output='data/generated/compression_experiments/default'),
    'plots': dict(metrics=['endpoint_rms', 'worst_recorded_rms'], aggregate='median', spread='range',
                  runs=[], methods=['dense', 'legendre', 'harmonic', 'logarithmic', 'low_rank', 'frozen_features']),
}


def _experiment_matched_controls(config, n, d, panel_rank=None):
    """Select controls from requested learned-state counts, without model fitting.

    Explicit widths/ranks keep their order; additional choices are deduplicated.
    Matching counts moving coordinates only. Actual moving and fixed storage
    remain measured from each constructed model by the ordinary fit path.
    """
    oblivious = config['methods']['oblivious']
    controls = dict(dense={width: [] for width in oblivious['dense']['widths']},
                    low_rank={rank: [] for rank in oblivious['low_rank']['ranks']},
                    targets=[], skipped={})
    enabled = {family: oblivious[family].get('match_compressions', False)
               for family in ('dense', 'low_rank')}
    if not any(enabled.values()):
        return controls
    m, depth = config['dataset']['train_samples'], config['model']['depth']
    for order in oblivious['legendre']['orders']:
        controls['targets'].append(dict(model=f'legendre_{order}', family='legendre', order=order,
            moving_scalars=n*(d+1)+2*order*n*m+2*n*m+2))
    for family in ('harmonic', 'logarithmic'):
        for compact in config['methods']['non_oblivious'][family]['budgets']:
            width, rank = compact['width'], compact['source_rank']
            first_dimension = d
            if family == 'logarithmic' and config['methods']['non_oblivious'][family].get('panel_span', False):
                if panel_rank is None:
                    raise ValueError('Panel-span state matching requires the actual declared-panel rank')
                first_dimension = panel_rank
            controls['targets'].append(dict(model=f'{family}_{width}_r{rank}', family=family,
                width=width, source_rank=rank,
                moving_scalars=width*(first_dimension+1)+(depth-1)*width*width+m))

    def largest_fitting(budget, upper, size):
        lower = 0
        while lower < upper:
            middle = (lower+upper+1)//2
            if size(middle) <= budget:
                lower = middle
            else:
                upper = middle-1
        return lower

    dense_size = lambda width: width*(d+1)+(depth-1)*width*width
    low_rank_size = lambda rank: n+min(rank, n, d)*(n+d)+2*n*rank
    for target in controls['targets']:
        budget = target['moving_scalars']
        for family, size, upper in (
                ('dense', dense_size, budget//(d+1)), ('low_rank', low_rank_size, n)):
            if not enabled[family]:
                continue
            choice = largest_fitting(budget, upper, size)
            if not choice:
                controls['skipped'][f'{family}_match_{target["model"]}'] = (
                    f'{target["model"]} has {budget} moving scalars; '
                    f'the smallest {family} control requires {size(1)}')
                continue
            controls[family].setdefault(choice, []).append(dict(
                **target, unused_moving_scalars=budget-size(choice)))
    return controls


def _experiment_merge(base, patch, path='', schema=None):
    """Strict recursive merge; method-local setup overrides use the shared schema."""
    import copy
    if not isinstance(patch, dict):
        raise ValueError(f'{path or "configuration"} must be an object')
    schema = base if schema is None else schema
    result = copy.deepcopy(base)
    for key, value in patch.items():
        name = f'{path}.{key}' if path else key
        if key not in schema:
            if key == 'setup' and path in ('methods.non_oblivious.harmonic',
                                          'methods.non_oblivious.logarithmic'):
                setup_schema = EXPERIMENT_DEFAULTS['methods']['non_oblivious']['setup']
                result[key] = _experiment_merge(base.get(key, {}), value, name, schema=setup_schema)
                continue
            raise ValueError(f'Unknown configuration field: {name}')
        expected = schema[key]
        if isinstance(expected, dict):
            result[key] = _experiment_merge(base.get(key, {}), value, name, schema=expected)
            continue
        if name == 'execution.devices' and isinstance(value, list):
            valid = all(isinstance(v, str) for v in value) and bool(value)
        elif expected is None:
            valid = value is None or isinstance(value, str)
        elif isinstance(expected, bool):
            valid = isinstance(value, bool)
        elif isinstance(expected, (int, float)):
            valid = (not isinstance(value, bool) and isinstance(value, (int, float))
                     and math.isfinite(value) and (not isinstance(expected, int) or isinstance(value, int)))
        else:
            valid = isinstance(value, type(expected))
        if not valid:
            raise ValueError(f'Invalid type/value for {name}: {value!r}')
        if isinstance(expected, list):
            element = expected[0] if expected else ''  # Empty defaults describe string lists.
            for item in value:
                if isinstance(element, dict):
                    if not isinstance(item, dict) or set(item) != set(element):
                        raise ValueError(f'{name} entries require exactly {list(element)}')
                    _experiment_merge(element, item, name)
                elif type(item) is not type(element):
                    raise ValueError(f'Wrong element type in {name}: {item!r}')
        result[key] = copy.deepcopy(value)
    return result


def _experiment_leaves(tree, prefix=''):
    for key, value in tree.items():
        path = f'{prefix}.{key}' if prefix else key
        if isinstance(value, dict):
            yield from _experiment_leaves(value, path)
        else:
            yield path, value


def _experiment_config(argv, validate_run=True):
    """Generate overrides directly from the default tree, without a second argument list."""
    parser = argparse.ArgumentParser(description='Coupled, independently repeated compression experiments')
    parser.add_argument('--config', type=Path, help='Partial or complete JSON; paths are relative to cwd')
    parser.add_argument('--print-config', action='store_true', help='Print the resolved config without running')
    parser.add_argument('--worker-seed', type=int, help=argparse.SUPPRESS)
    parser.add_argument('--worker-device', help=argparse.SUPPRESS)
    parser.add_argument('--worker-out', type=Path, help=argparse.SUPPRESS)
    leaves = dict(_experiment_leaves(EXPERIMENT_DEFAULTS))
    for method in ('harmonic', 'logarithmic'):
        leaves.update(_experiment_leaves(EXPERIMENT_DEFAULTS['methods']['non_oblivious']['setup'],
                                        f'methods.non_oblivious.{method}.setup'))
    for path, default in leaves.items():
        options = dict(dest=path, default=argparse.SUPPRESS, help=f'default: {default!r}')
        if isinstance(default, bool):
            options['action'] = argparse.BooleanOptionalAction
        elif isinstance(default, list):
            options.update(nargs='*', metavar='VALUE')
        else:
            options['type'] = str if default is None or isinstance(default, str) else type(default)
        parser.add_argument('--'+path, **options)
    args = parser.parse_args(argv)
    try:
        config = _experiment_merge(EXPERIMENT_DEFAULTS,
            json.loads(args.config.read_text()) if args.config else {})
        overrides = {}
        for path, value in vars(args).items():
            if path not in leaves:
                continue
            default = leaves[path]
            if isinstance(default, list):
                if len(value) == 1 and value[0].lstrip().startswith('['):
                    value = json.loads(value[0])
                else:
                    element = default[0] if default else ''
                    cast = json.loads if isinstance(element, dict) else type(element)
                    value = [cast(item) for item in value]
            if path == 'execution.devices' and value.lstrip().startswith('['):
                value = json.loads(value)
            target = overrides
            parts = path.split('.')
            for key in parts[:-1]:
                target = target.setdefault(key, {})
            target[parts[-1]] = value
        config = _experiment_merge(config, overrides, schema=EXPERIMENT_DEFAULTS)
        if validate_run:
            _experiment_validate(config)
    except (ValueError, TypeError, OSError) as error:
        parser.error(str(error))
    return config, args


def _experiment_setup(config, method):
    group = config['methods']['non_oblivious']
    return _experiment_merge(group['setup'], group[method].get('setup', {}),
                             schema=EXPERIMENT_DEFAULTS['methods']['non_oblivious']['setup'])


def _experiment_validate(config):
    data, model, training = (config[key] for key in ('dataset', 'model', 'training'))
    oblivious, group = (config['methods'][key] for key in ('oblivious', 'non_oblivious'))
    positive = [data['train_samples'], data['test_samples'], data['label_scale'], model['width'],
                model['depth'], training['step'], training['horizon'], training['record_every'],
                config['execution']['seconds_per_fit']]
    if any(value <= 0 for value in positive):
        raise ValueError('Counts, step, horizon, label scale and time limit must be positive')
    if data['undeclared_samples'] < 0:
        raise ValueError('dataset.undeclared_samples must be nonnegative')
    if not config['seeds'] or len(set(config['seeds'])) != len(config['seeds']):
        raise ValueError('seeds must be a nonempty list of distinct integers')
    if any(seed < 0 or seed >= 2**63 for seed in config['seeds']) or not 0 <= data['seed'] < 2**32-1:
        raise ValueError('Invalid seed (repetitions: [0,2^63); data: [0,2^32-1))')
    if data['name'] not in ('sphere', 'digits', 'mnist', 'npz'):
        raise ValueError('dataset.name must be sphere, digits (raw 8x8), mnist (raw 28x28), or npz')
    if data['name'] in ('digits', 'mnist'):
        data['dimension'] = 784 if data['name'] == 'mnist' else 64
        if len(set(data['digit_pair'])) != 2 or any(v < 0 or v > 9 for v in data['digit_pair']):
            raise ValueError('Digits requires two different labels from 0 through 9')
        if data['name'] == 'mnist' and not data['cache']:
            raise ValueError('MNIST requires dataset.cache (use the current study generated-data directory)')
    elif data['name'] == 'npz':
        if not data['file']:
            raise ValueError('dataset.file is required for npz')
        with np.load(data['file'], allow_pickle=False) as arrays:
            if arrays['train_inputs'].ndim != 2:
                raise ValueError('NPZ train_inputs must have shape (samples, dimension)')
            data['dimension'] = int(arrays['train_inputs'].shape[1])
    if data['dimension'] < (2 if data['name'] == 'sphere' else 1):
        raise ValueError('Invalid input dimension (sphere toy requires dimension >= 2)')
    if model['activation'] not in DEEP_ACTIVATIONS:
        raise ValueError(f'activation must be one of {DEEP_ACTIVATIONS}')
    if training['solver'] != 'euler' or training['dtype'] not in ('float32', 'float64'):
        raise ValueError('Training supports Euler with float32 or float64')
    if config['execution']['seconds_per_fit'] > 120:
        raise ValueError('seconds_per_fit must be <= 120, matching the existing source-setup cap')
    if not 0 < config['execution']['dense_seconds_per_fit'] <= 300:
        raise ValueError('dense_seconds_per_fit must be positive and <= 300')
    for name, key in (('dense', 'widths'), ('legendre', 'orders'), ('low_rank', 'ranks')):
        values = oblivious[name][key]
        if len(set(values)) != len(values) or any(v < 1 for v in values):
            raise ValueError(f'{name}.{key} must be distinct positive integers')
    if any(rank > model['width'] for rank in oblivious['low_rank']['ranks']):
        raise ValueError('Low-rank ranks cannot exceed the dense width')
    restricted = (oblivious['legendre']['orders'] or oblivious['low_rank']['ranks']
                  or (oblivious['low_rank'].get('match_compressions', False)
                      and group['logarithmic']['budgets'])
                  or oblivious['frozen_features']['enabled'] or group['harmonic']['budgets'])
    if restricted and (model['depth'] != 2 or model['activation'] != 'tanh'):
        raise ValueError('Current Legendre, low_rank, frozen_features and Harmonic implementations require '
                         'depth=2, activation=tanh. Disable them to use other architectures.')
    if group['harmonic']['budgets'] and data['dimension'] not in (2, 3):
        raise ValueError('Harmonic currently supports dimension 2 or 3; disable it with budgets=[]')
    if group['harmonic']['spatial_degree'] < 0:
        raise ValueError('Harmonic spatial_degree must be nonnegative')
    if group['logarithmic']['budgets'] and not group['logarithmic']['test_inputs_at_setup']:
        raise ValueError('The current Logarithmic construction requires declared test inputs (never labels)')
    for name in ('harmonic', 'logarithmic'):
        method = group[name]
        budgets = [(v['width'], v['source_rank']) for v in method['budgets']]
        if len(set(budgets)) != len(budgets) or any(min(v) < 1 for v in budgets):
            raise ValueError(f'{name} requires distinct positive (width, source_rank) budgets')
        if any(width >= model['width'] or rank > model['width'] for width, rank in budgets):
            raise ValueError(f'{name} requires compact width < dense width and source_rank <= dense width')
        setup = _experiment_setup(config, name)
        if (setup['initializer'] != 'dense_rollout' or setup['rollout_solver'] != 'rk4'
                or setup['rollout_dtype'] not in ('float32', 'float64')
                or setup['coefficient_dtype'] != 'float64'):
            raise ValueError('Setup supports dense_rollout/RK4, float32/float64 rollout, float64 coefficients')
        if min(setup['rollout_step'], setup['time_degree'], setup['selection_trials']) <= 0 or setup['condition_limit'] < 1:
            raise ValueError('Setup orders/step/trials must be positive and condition_limit >= 1')
        if setup['selection_strategy'] not in ('uniform', 'qr_leverage'):
            raise ValueError('Setup selection_strategy must be uniform or qr_leverage')
    if (not config['plots']['metrics'] or set(config['plots']['metrics'])-{'endpoint_rms', 'worst_recorded_rms'}
            or not config['plots']['methods']
            or set(config['plots']['methods'])-set(EXPERIMENT_DEFAULTS['plots']['methods'])
            or len(set(config['plots']['methods'])) != len(config['plots']['methods'])
            or any(not path for path in config['plots']['runs'])
            or config['plots']['aggregate'] not in ('mean', 'median')
            or config['plots']['spread'] not in ('range', 'sd', 'none')
            or (config['plots']['spread'] == 'sd' and config['plots']['aggregate'] != 'mean')
            or oblivious['frozen_features']['plot'] not in ('dashed', 'point')):
        raise ValueError('Unsupported plot metric, aggregation, spread or frozen-feature style')
    if config['execution']['stop_after_match']:
        if model['width'] not in oblivious['dense']['widths']:
            raise ValueError('stop_after_match requires an independent dense comparator of the reference width')
        if oblivious['legendre']['orders'] != sorted(oblivious['legendre']['orders']):
            raise ValueError('stop_after_match requires ascending Legendre orders')
        for name in ('harmonic', 'logarithmic'):
            widths = [budget['width'] for budget in group[name]['budgets']]
            if widths != sorted(widths):
                raise ValueError('stop_after_match requires ascending compact widths')


def _experiment_data(config):
    data = config['dataset']
    extra = data.get('undeclared_samples', 0)
    if extra:
        if data['name'] == 'npz':
            with np.load(data['file'], allow_pickle=False) as archive:
                if {'extra_query_inputs', 'extra_query_labels'} & set(archive.files):
                    raise ValueError('Choose explicit NPZ extra queries or undeclared_samples, not both')
        # Draw disjoint panels together, before any fitting or budget selection.
        expanded = dict(config, dataset=dict(data, test_samples=data['test_samples']+extra,
                                            undeclared_samples=0))
        arrays = _experiment_data(expanded)
        rows = np.random.default_rng(data['seed']+2).permutation(data['test_samples']+extra)
        declared, unseen = rows[:data['test_samples']], rows[data['test_samples']:]
        for field in ('inputs', 'labels'):
            values = arrays['query_'+field]
            arrays['query_'+field] = values[declared]
            arrays['extra_query_'+field] = values[unseen]
        return arrays
    keys = ('train_inputs', 'train_labels', 'query_inputs', 'query_labels')
    extra_arrays = {}
    if data['name'] == 'mnist':
        from torchvision.datasets import MNIST
        arrays = []
        # Use the official train/test partition. Each requested binary subset is
        # balanced (the first digit gets one extra row for odd counts), then shuffled.
        for split, count in enumerate((data['train_samples'], data['test_samples'])):
            source = MNIST(root=data['cache'], train=split == 0, download=data['download'])
            targets = source.targets.numpy()
            rng = np.random.default_rng(data['seed']+split)
            selected = []
            for digit, wanted in zip(data['digit_pair'], ((count+1)//2, count//2)):
                candidates = np.flatnonzero(targets == digit)
                if len(candidates) < wanted:
                    raise ValueError('Requested MNIST subset exceeds an official split class count')
                selected.extend(rng.permutation(candidates)[:wanted])
            rows = rng.permutation(np.asarray(selected, dtype=int))
            values = source.data.numpy()[rows].reshape(count, 784).astype(np.float64)
            norms = np.linalg.norm(values, axis=1, keepdims=True)
            if np.any(norms == 0):
                raise ValueError('MNIST subset contains a zero-norm image')
            values /= norms
            arrays.extend((values, np.where(targets[rows] == data['digit_pair'][0], -1., 1.)))
    elif data['name'] == 'npz':
        with np.load(data['file'], allow_pickle=False) as archive:
            arrays = [np.array(archive[key], dtype=np.float64) for key in keys]
            extra_keys = {'extra_query_inputs', 'extra_query_labels'}
            present = extra_keys & set(archive.files)
            if present and present != extra_keys:
                raise ValueError('NPZ explicit extra queries require both inputs and labels')
            if present:
                extra_arrays = {key: np.array(archive[key], dtype=np.float64) for key in extra_keys}
                x, y = extra_arrays['extra_query_inputs'], extra_arrays['extra_query_labels']
                if x.ndim != 2 or x.shape[1] != data['dimension'] or y.shape != (len(x),):
                    raise ValueError('NPZ extra queries need shape (count, dimension) and one label per row')
                norms = np.linalg.norm(x, axis=1, keepdims=True)
                if np.any(norms == 0):
                    raise ValueError('NPZ extra queries must have nonzero norms')
                extra_arrays['extra_query_inputs'] = x/norms
                extra_arrays['extra_query_labels'] *= data['label_scale']
        for start, count in ((0, data['train_samples']), (2, data['test_samples'])):
            x, y = arrays[start:start+2]
            if x.ndim != 2 or y.shape != (len(x),) or len(x) < count:
                raise ValueError('NPZ needs enough rows and one scalar label per input in each split')
            rows = np.random.default_rng(data['seed']+start//2).permutation(len(x))[:count]
            arrays[start:start+2] = [x[rows], y[rows]]
        for index in (0, 2):
            norms = np.linalg.norm(arrays[index], axis=1, keepdims=True)
            if (arrays[index].shape[1] != data['dimension'] or np.any(norms == 0)):
                raise ValueError('NPZ inputs must have matching dimensions and nonzero norms')
            arrays[index] /= norms
    else:
        tensors = validation_data(data['dimension'], data['train_samples'], data['test_samples'],
            data['seed'], 'cpu', task='digits' if data['name'] == 'digits' else 'toy',
            raw_images=True, tuning_samples=0, digit_pair=tuple(data['digit_pair']))
        arrays = [value.numpy().astype(np.float64) for value in tensors]
        if len(arrays[2]) < data['test_samples']:
            raise ValueError('Requested test_samples exceeds the held-out dataset')
        if data['name'] == 'digits':
            rows = np.random.default_rng(data['seed']+1).permutation(len(arrays[2]))[:data['test_samples']]
            arrays[2:] = [v[rows] for v in arrays[2:]]
    arrays[1] *= data['label_scale']
    arrays[3] *= data['label_scale']
    if not all(np.isfinite(v).all() for v in arrays+list(extra_arrays.values())):
        raise ValueError('Dataset contains nonfinite values')
    return dict(zip(keys, arrays), **extra_arrays)


def feedback_scope_main(argv):
    """Frozen d=10 query paths and fixed-budget panel-size pilots."""
    parser = argparse.ArgumentParser(description=feedback_scope_main.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    phase = parser.add_mutually_exclusive_group()
    phase.add_argument('--prepare-only', action='store_true')
    phase.add_argument('--plot-only', action='store_true')
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text())
    out = Path(config['output']).resolve()
    out.mkdir(parents=True, exist_ok=True)
    config_hash = sha(json.dumps(config, sort_keys=True).encode())
    plan_path = out/'plan.json'
    if plan_path.exists():
        plan = json.loads(plan_path.read_text())
        if plan['config_sha256'] != config_hash:
            raise ValueError('Scope pilot output belongs to a different frozen configuration')
    else:
        if args.plot_only:
            raise FileNotFoundError('Prepare and run the scope pilot before plotting')
        base = _experiment_merge(EXPERIMENT_DEFAULTS, config['experiment'])
        _experiment_validate(base)
        if base['dataset']['name'] != 'sphere' or base['dataset']['dimension'] < 3:
            raise ValueError('Scope pilot requires the normalized sphere toy with dimension >= 3')
        if base['methods']['non_oblivious']['logarithmic']['panel_span']:
            raise ValueError('Controlled query-distance probe keeps the unprojected first layer')
        if not 0 < config['nearest_fraction'] < .5 or config['angle_count'] < 2:
            raise ValueError('Nearest-anchor paths require fraction in (0,.5) and at least two angles')
        source = Path(__file__).read_bytes()
        (out/'source.py').write_bytes(source)
        save_json(out/'config.json', config)
        plan = dict(config_sha256=config_hash, source_sha256=sha(source), cases=[],
            scope='One seed and dense pair; fixed budgets; no rescue selections or crossing fit. '
                  'The ambient dimension is 10 but the toy target uses only its first three coordinates. '
                  'Extra path inputs and all query labels are withheld from Logarithmic source setup.')
        for panel_size in config['panel_sizes']:
            case = _experiment_merge(base, dict(dataset=dict(test_samples=panel_size),
                execution=dict(output=str(out/f'p{panel_size}'))))
            if panel_size == config['path_panel_size']:
                arrays = _experiment_data(case)
                count, d = len(arrays['train_labels']), arrays['train_inputs'].shape[1]
                anchors = arrays['query_inputs'][:config['anchor_count']]
                if len(anchors) != config['anchor_count']:
                    raise ValueError('Not enough declared anchors')
                panel = np.concatenate((arrays['train_inputs'], arrays['query_inputs']))
                separation = np.arccos(np.clip(anchors@panel.T, -1., 1.))
                separation[np.arange(len(anchors)), count+np.arange(len(anchors))] = np.inf
                nearest = separation.min(axis=1)
                cap = min(config['maximum_angle'], config['nearest_fraction']*float(nearest.min()))
                angles = np.linspace(0., cap, config['angle_count'])
                rng, paths, tangent_vectors = np.random.default_rng(config['tangent_seed']), [], []
                for anchor in anchors:
                    for _ in range(config['directions_per_anchor']):
                        tangent = rng.normal(size=d)
                        tangent -= (tangent@anchor)*anchor
                        tangent /= np.linalg.norm(tangent)
                        paths.append(np.cos(angles)[:, None]*anchor+np.sin(angles)[:, None]*tangent)
                        tangent_vectors.append(tangent)
                paths = np.asarray(paths)
                nearest_indices = (paths.reshape(-1, d)@panel.T).argmax(axis=1).reshape(paths.shape[:2])
                expected = count+np.repeat(np.arange(len(anchors)), config['directions_per_anchor'])
                if not np.all(nearest_indices == expected[:, None]):
                    raise AssertionError('A generated path left its anchor Voronoi cell')
                target = lambda x: math.sqrt(d)*x[:, 0]+d**1.5*x[:, 0]*x[:, 1]*x[:, 2]
                scale = np.sqrt(np.mean(target(arrays['train_inputs'])**2))
                # Undo the established NPZ loader permutations to preserve the
                # original training/query order. Its extra rows retain file order.
                archive = {}
                for prefix, seed_offset in (('train', 0), ('query', 1)):
                    rows = np.random.default_rng(case['dataset']['seed']+seed_offset).permutation(len(arrays[prefix+'_labels']))
                    for field in ('inputs', 'labels'):
                        archive[prefix+'_'+field] = arrays[prefix+'_'+field][np.argsort(rows)]
                    archive[prefix+'_labels'] /= case['dataset']['label_scale']
                archive['extra_query_inputs'] = paths.reshape(-1, d)
                archive['extra_query_labels'] = target(archive['extra_query_inputs'])/scale
                np.savez_compressed(out/'controlled_queries.npz', **archive)
                case['dataset'].update(name='npz', file=str(out/'controlled_queries.npz'))
                loaded = _experiment_data(case)
                for key in arrays:
                    np.testing.assert_allclose(loaded[key], arrays[key], rtol=0, atol=1e-14)
                plan['paths'] = dict(angles=angles.tolist(), path_count=len(paths),
                    path_shape=list(paths.shape[:2]), row_order='path first, then angle',
                    declared_anchor_indices=list(range(len(anchors))),
                    tangent_seed=config['tangent_seed'], tangents=np.asarray(tangent_vectors).tolist(),
                    nearest_other_panel_angles=nearest.tolist(), angle_cap=cap,
                    anchor_is_nearest_at_every_sample=True,
                    cap_rule='common min(maximum_angle, nearest_fraction*minimum anchor separation)',
                    zero_angle_rule='includes the actual declared-anchor discrepancy; no subtraction',
                    arrays_sha256={key: array_sha(value) for key, value in loaded.items()})
            path = out/f'p{panel_size}_config.json'
            save_json(path, case)
            plan['cases'].append(dict(panel_size=panel_size, config=str(path), output=case['execution']['output']))
        save_json(plan_path, plan)
    if args.prepare_only:
        print(json.dumps(dict(prepared=str(plan_path), source=str(out/'source.py'))), flush=True)
        return 0
    if not args.plot_only:
        if sha(Path(__file__).read_bytes()) != plan['source_sha256']:
            raise RuntimeError('Run the frozen scope/source.py snapshot created during preparation')
        for case in plan['cases']:
            experiment_main(['--config', case['config']])

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    report = dict(plan=plan, cases=[], controlled_paths={}, errors={})
    path_arrays = None
    for case in plan['cases']:
        folder = Path(case['output'])
        manifest = json.loads((folder/'run.json').read_text())
        seed = manifest['config']['seeds'][0]
        attempt = folder/manifest['repetitions'][str(seed)]
        record = json.loads((attempt/'report.json').read_text())
        if sha((attempt/'trajectories.npz').read_bytes()) != record['trajectories_sha256']:
            raise RuntimeError('Scope trajectory hash mismatch')
        with np.load(attempt/'trajectories.npz', allow_pickle=False) as archive:
            arrays = {key: archive[key] for key in archive.files}
        training_count = len(arrays['train_labels'])
        width = manifest['config']['model']['width']
        baseline = trajectory_rms(arrays[f'dense_{width}'][:, training_count:].astype(float),
                                   arrays['reference'][:, training_count:].astype(float))
        row = dict(panel_size=case['panel_size'], complete=record['complete'], errors=record['errors'],
                   report=str(attempt/'report.json'), dense_pair=baseline, models={})
        source_info = record['sources'].get('logarithmic', {})
        if source_info and source_info['passive_count'] != case['panel_size']:
            raise AssertionError('Extra path queries leaked into source construction')
        for name, model in record['models'].items():
            if model['family'] != 'logarithmic' or not record['runs'].get(name, {}).get('complete'):
                continue
            metric = trajectory_rms(arrays[name][:, training_count:].astype(float),
                                    arrays['reference'][:, training_count:].astype(float))
            row['models'][name] = dict(**metric, width=model['width'],
                endpoint_ratio=metric['endpoint_rms']/baseline['endpoint_rms'],
                worst_recorded_ratio=metric['max_time_rms']/baseline['max_time_rms'])
        report['cases'].append(row)
        if not record['complete']:
            report['errors'][f'p{case["panel_size"]}'] = record['errors']
        if case['panel_size'] == config['path_panel_size']:
            path_arrays, path_record = arrays, record
    if path_arrays is not None:
        shape = tuple(plan['paths']['path_shape'])
        reference = path_arrays['extra_reference'][-1].astype(float).reshape(shape)
        names = [f'dense_{width}']+[name for name in path_record['models']
            if path_record['models'][name]['family'] == 'logarithmic']
        fig, ax = plt.subplots(figsize=(5.8, 3.6))
        for name in names:
            if not path_record['runs'].get(name, {}).get('complete'):
                continue
            error = path_arrays['extra_'+name][-1].astype(float).reshape(shape)-reference
            curve = np.sqrt(np.mean(error**2, axis=0))
            report['controlled_paths'][name] = dict(endpoint_rms_by_angle=curve.tolist(),
                zero_angle_rms=float(curve[0]), signed_error_by_path=error.tolist())
            ax.plot(plan['paths']['angles'], curve, marker='o', ms=3,
                    label='Independent dense pair' if name.startswith('dense_') else name.replace('logarithmic_', 'Log. '))
        ax.set(xlabel='Angular distance from declared anchor (radians)',
               ylabel='Endpoint RMS across six fixed paths', title='Controlled query paths · d=10, n=2048')
        ax.legend(frameon=False, fontsize=8)
        ax.grid(alpha=.15)
        fig.tight_layout()
        for suffix in ('png', 'pdf'):
            fig.savefig(out/f'controlled_query_paths.{suffix}', dpi=180)
        plt.close(fig)
    fig, axes = plt.subplots(1, 2, figsize=(8.3, 3.5))
    for axis, field, title in zip(axes, ('endpoint_ratio', 'worst_recorded_ratio'), ('Endpoint', 'Maximum recorded')):
        for name in sorted({name for row in report['cases'] for name in row['models']}):
            rows = [row for row in report['cases'] if name in row['models']]
            axis.plot([row['panel_size'] for row in rows], [row['models'][name][field] for row in rows],
                      'o-', label=name.replace('logarithmic_', 'Log. '))
        axis.axhline(1., color='grey', ls=':')
        axis.set(xlabel='Declared query-panel size', ylabel='RMS / independent dense-pair RMS', title=title,
                 xticks=config['panel_sizes'])
        axis.grid(alpha=.15)
        axis.legend(frameon=False, fontsize=8)
    fig.suptitle('Fixed compact widths on d=10 sphere inputs · one seed')
    fig.tight_layout()
    for suffix in ('png', 'pdf'):
        fig.savefig(out/f'fixed_budget_panel_size.{suffix}', dpi=180)
    plt.close(fig)
    report['complete'] = not report['errors']
    save_json(out/'report.json', report)
    print(json.dumps(dict(output=str(out), complete=report['complete'])), flush=True)
    return int(not report['complete'])


@torch.no_grad()
def appendix_transfer_main(argv):
    """One fixed counterfactual: freeze old-task compression, then change labels."""
    parser = argparse.ArgumentParser(description=appendix_transfer_main.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text())
    out = Path(config['output'])
    out.mkdir(parents=True, exist_ok=True)
    if (out/'report.json').exists():
        raise FileExistsError('Transfer output already exists; choose a fresh output directory')
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(config['device'])
    inputs, old_labels, queries, old_truth = validation_data(
        2, config['samples'], config['queries'], config['dataset_seed'], device)
    dense = DeepDense(config['width'], 2, config['depth'], config['activation'], config['seed'], device)
    initial_hashes = [array_sha(v.cpu().numpy()) for v in dense.initial_state]
    options = dict(horizon=config['horizon'], seconds=config['seconds'],
        seed=_experiment_seed(config['seed'], 'logarithmic_source'), ranks=(config['source_rank'],),
        partitions=('new',), step=config['rollout_step'], time_degree=config['time_degree'])
    report = dict(config=config, source_sha256=sha(Path(__file__).read_bytes()),
        initial_state_sha256=initial_hashes, models={}, sources={}, errors={},
        provenance='Old-task compact geometry and weights frozen before new-target sources are computed; '
                   'only label-dependent initial deficit is reset. Practical sources use full-horizon rollout.')
    arrays = dict(train_inputs=inputs.cpu().numpy(), query_inputs=queries.cpu().numpy(),
                  old_labels=old_labels.cpu().numpy(), old_truth=old_truth.cpu().numpy())
    save_json(out/'config.json', config)
    (out/'source.py').write_bytes(Path(__file__).read_bytes())
    started = time.monotonic()
    def persist():
        np.savez_compressed(out/'trajectories.npz', **arrays)
        report['trajectories_sha256'] = sha((out/'trajectories.npz').read_bytes())
        report['seconds'] = time.monotonic()-started
        save_json(out/'report.json', report)
    def construct(source, targets):
        h = dense.fields(dense.initial_state, inputs)[0][-1]
        gap = float(torch.linalg.eigvalsh(h.T@h/(config['width']*len(inputs)))[0])
        if gap <= 0:
            raise ArithmeticError('Nonpositive initialized feature gap')
        model = DeepHarmonic(dense, inputs, targets, source['new'][config['source_rank']], config['budget'],
            selection_seed=_experiment_seed(config['seed'], 'logarithmic_selector'),
            readout_floor=min(1e-4, gap/8), selection_trials=config['selection_trials'],
            condition_limit=config['condition_limit'])
        if any(v['truncated'] for v in model.diagnostics['source_truncations']):
            raise ArithmeticError('Extra constructor truncation: inconclusive')
        return model
    def frozen_hashes(model):
        return [array_sha(v.cpu().numpy()) for v in
                model.initial_state[:-1]+model.metrics+model.metric_inverses]
    try:
        print('transfer: compiling old-task sources', flush=True)
        sources, info = cubic_rollout_sources(dense, inputs, old_labels, queries, **options)
        report['sources']['old'] = info
        transferred = construct(sources, old_labels)
        del sources
        frozen = frozen_hashes(transferred)
        # This target is not a scaling/sign change of the source target.
        if config['target'] != 'cos(theta) + 0.5*sin(5*theta), normalized by training RMS':
            raise ValueError('Unknown transfer target')
        def target(x):
            angle = torch.atan2(x[:, 1], x[:, 0])
            return angle.cos()+.5*(5*angle).sin()
        scale = target(inputs).square().mean().sqrt()
        labels, truth = target(inputs)/scale, target(queries)/scale
        transferred.initial_state[-1] = labels.clone()
        assert frozen_hashes(transferred) == frozen
        report['transferred_geometry_unchanged'] = True
        report['old_new_label_cosine'] = float(old_labels@labels/(old_labels.norm()*labels.norm()))
        arrays.update(train_labels=labels.cpu().numpy(), query_labels=truth.cpu().numpy())
        print('transfer: compiling new-task positive control', flush=True)
        sources, info = cubic_rollout_sources(dense, inputs, labels, queries, **options)
        report['sources']['new'] = info
        rebuilt = construct(sources, labels)
        del sources
        iid_seed = _experiment_seed(config['seed'], f"dense_{config['width']}")
        iid = DeepDense(config['width'], 2, config['depth'], config['activation'], iid_seed, device)
        report['iid_seed'] = iid_seed
        for name, model, targets in [('replay', dense, old_labels), ('reference', dense, labels),
                ('independent_dense', iid, labels), ('transferred', transferred, labels),
                ('rebuilt', rebuilt, labels)]:
            _experiment_move(model, device, torch.float32)
            state, prediction, run = integrate_euler(model, inputs.float(), targets.float(),
                torch.cat((inputs, queries)).float(), config['step'], config['seconds'],
                horizon=config['horizon'], observation_every=config['record_every'])
            del state
            arrays[name], arrays['times_'+name] = prediction, np.asarray(run['times'])
            report['models'][name] = dict(run=run, learned=sum(v.numel() for v in model.initial_state),
                fixed=int(model.fixed_scalars), diagnostics=getattr(model, 'diagnostics', {}))
            if not run['complete']:
                report['errors'][name] = 'Inconclusive: '+run['stop_reason']
            persist()
            print(json.dumps(dict(model=name, complete=run['complete'], seconds=run['seconds'])), flush=True)
        if not report['errors']:
            m = len(inputs)
            reference = arrays['reference'][:, m:]
            metrics = {name: trajectory_rms(arrays[name][:, m:], reference)
                       for name in ('independent_dense', 'transferred', 'rebuilt', 'replay')}
            baseline = metrics['independent_dense']
            for name, metric in metrics.items():
                assert np.array_equal(arrays['times_'+name], arrays['times_reference'])
                metric.update(endpoint_ratio=metric['endpoint_rms']/baseline['endpoint_rms'],
                    worst_ratio=metric['max_time_rms']/baseline['max_time_rms'])
                metric['passes_3x'] = max(metric['endpoint_ratio'], metric['worst_ratio']) <= 3
            report['metrics'] = metrics
            import matplotlib.pyplot as plt
            fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
            names = ['transferred', 'rebuilt', 'replay']
            colors = ['#009E73', '#0072B2', '#D55E00']
            for name, color in zip(names, colors):
                axes[0].plot(arrays['times_reference'][1:], metrics[name]['curve'][1:],
                             label=name.capitalize(), color=color)
            axes[0].plot(arrays['times_reference'][1:], baseline['curve'][1:],
                         '--', color='black', label='Dense pair')
            axes[0].set(xlabel='Training time', ylabel='Test RMS', yscale='log', title='Changed target')
            positions = np.arange(len(names))
            axes[1].bar(positions-.18, [metrics[n]['endpoint_ratio'] for n in names], .36,
                        label='Endpoint', color='#0072B2')
            axes[1].bar(positions+.18, [metrics[n]['worst_ratio'] for n in names], .36,
                        label='Worst recorded', color='#E69F00')
            axes[1].set(xticks=positions, xticklabels=[n.capitalize() for n in names],
                        yscale='log', ylabel='Error / dense pair', title='Transfer vs replay')
            axes[1].axhline(1, color='black', linestyle='--', linewidth=1)
            axes[1].axhline(3, color='grey', linestyle=':', linewidth=1)
            for axis in axes:
                axis.grid(alpha=.16)
                axis.legend(frameon=False, fontsize=8)
            fig.tight_layout()
            for extension in ('png', 'pdf'):
                fig.savefig(out/f'appendix_transfer.{extension}', dpi=180)
            plt.close(fig)
        persist()
        print(json.dumps(report.get('metrics', report['errors'])), flush=True)
        return int(bool(report['errors']))
    except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
        report['errors']['setup'] = f'{type(error).__name__}: {error}'
        persist()
        raise


@torch.no_grad()
def feedback_pooled_transfer_main(argv):
    """Fixed-rank pooling of three non-target source tasks, against saved target curves."""
    import ast
    import io

    parser = argparse.ArgumentParser(description=feedback_pooled_transfer_main.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    args = parser.parse_args(argv)
    started = time.monotonic()
    config_bytes = args.config.read_bytes()
    config = json.loads(config_bytes)
    frozen = dict(width=1024, depth=2, activation='tanh', seed=901, samples=8, queries=30,
                  budget=256, source_rank=15, auxiliary_label_seeds=[4712, 4713],
                  selection_strategy='uniform', selection_trials=64, condition_limit=16,
                  horizon=32, step=.00625, record_every=80, rollout_step=.125, time_degree=8,
                  wall_budget_seconds=120, pass_factor=1, reproduction_factor=.1)
    if any(config[key] != value for key, value in frozen.items()):
        raise ValueError('Pooled-transfer design differs from the frozen bounded test')
    source_root = (ROOT/config['input']).resolve()
    out = (ROOT/config['output']).resolve()
    expected_root = ROOT/'data/generated/paper_appendix_pilots_20261009/transfer'
    if source_root != expected_root or not out.is_relative_to(expected_root.parent/'feedback'):
        raise ValueError('Pooled transfer must use its assigned saved inputs and feedback output')
    if out.exists():
        raise FileExistsError('Pooled-transfer output must be fresh')
    saved_bytes = (source_root/'report.json').read_bytes()
    saved = json.loads(saved_bytes)
    payload = (source_root/'trajectories.npz').read_bytes()
    old_source = (source_root/'source.py').read_bytes()
    if sha(payload) != saved['trajectories_sha256'] or sha(old_source) != saved['source_sha256']:
        raise ValueError('Saved transfer input hash mismatch')
    if saved['errors'] or any(not saved['models'][name]['run']['complete'] for name in
                             ('reference', 'independent_dense', 'transferred', 'rebuilt')):
        raise ValueError('Saved comparison contains an incomplete or failed required model')
    for key in ('width', 'depth', 'activation', 'seed', 'samples', 'queries', 'budget', 'source_rank',
                'selection_trials', 'condition_limit', 'horizon', 'step', 'record_every',
                'rollout_step', 'time_degree'):
        if config[key] != saved['config'][key]:
            raise ValueError(f'Saved transfer contract mismatch: {key}')
    with np.load(io.BytesIO(payload), allow_pickle=False) as raw:
        arrays = {key: raw[key] for key in raw.files}
    times = arrays['times_reference']
    for name in ('reference', 'independent_dense', 'transferred', 'rebuilt'):
        if not np.array_equal(arrays['times_'+name], times) or not np.isfinite(arrays[name]).all():
            raise ValueError(f'Invalid saved reference grid or values: {name}')
    if arrays['train_inputs'].shape != (8, 2) or arrays['query_inputs'].shape != (30, 2):
        raise ValueError('Expected the saved circle transfer panel')
    current_source = Path(__file__).read_bytes()
    old_tree, current_tree = ast.parse(old_source), ast.parse(current_source)
    compiler_match = {}
    for name in ('cubic_rollout_sources', '_cubic_residual_partition', 'integrate'):
        old_node = next(node for node in old_tree.body if isinstance(node, ast.FunctionDef) and node.name == name)
        current_node = next(node for node in current_tree.body if isinstance(node, ast.FunctionDef) and node.name == name)
        compiler_match[name] = ast.dump(old_node, include_attributes=False) == ast.dump(current_node, include_attributes=False)
    if not all(compiler_match[name] for name in ('_cubic_residual_partition', 'integrate')):
        raise ValueError('Source integration changed relative to the saved transfer baseline')
    # The current compiler has optional spectral instrumentation. Execute only
    # the hash-checked saved function so all three label tasks share the exact
    # compiler used by the original transfer trial, without importing its CLI.
    saved_compiler = next(node for node in old_tree.body
                          if isinstance(node, ast.FunctionDef) and node.name == 'cubic_rollout_sources')
    compiler_namespace = dict(globals())
    exec(compile(ast.Module(body=[saved_compiler], type_ignores=[]), str(source_root/'source.py'), 'exec'),
         compiler_namespace)
    compile_sources = compiler_namespace['cubic_rollout_sources']
    out.mkdir(parents=True)
    (out/'source.py').write_bytes(current_source)
    save_json(out/'config.json', config)
    report = dict(config=config, config_sha256=sha(config_bytes), source_sha256=sha(current_source),
        input_report_path=str(source_root/'report.json'), input_report_sha256=sha(saved_bytes),
        input_trajectories_sha256=sha(payload), input_source_sha256=sha(old_source),
        source_compiler_ast_matches_saved=compiler_match,
        executed_source_compiler='hash-checked saved cubic_rollout_sources function; current unchanged RK4 driver',
        sources={}, pooling={}, models={}, errors={},
        complete=False, status='inconclusive', source_label_tasks=[],
        provenance='Full-horizon RK4 sources for old labels and two fixed non-target label tasks. '
                   'No target labels enter any source rollout. Saved new-target dense/iid/rebuilt '
                   'curves are reused. This is not an initialization-only source construction.')
    source_arrays = {}
    device = torch.device(config['device'])
    deadline = started+config['wall_budget_seconds']

    def persist():
        np.savez_compressed(out/'trajectories.npz', **arrays)
        report['trajectories_sha256'] = sha((out/'trajectories.npz').read_bytes())
        if source_arrays:
            np.savez_compressed(out/'sources.npz', **source_arrays)
            report['sources_sha256'] = sha((out/'sources.npz').read_bytes())
        report['seconds'] = time.monotonic()-started
        save_json(out/'report.json', report)

    def remaining():
        synchronize(device)
        seconds = deadline-time.monotonic()
        if seconds <= 0:
            raise TimeoutError('Pooled transfer exhausted its total 120-second budget')
        return seconds

    def geometry(model):
        return [array_sha(value.detach().cpu().numpy()) for value in
                model.initial_state[:-1]+model.metrics+model.metric_inverses]

    try:
        torch.set_num_threads(1)
        torch.set_default_dtype(torch.float64)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        inputs, queries, old_labels, labels = [torch.as_tensor(arrays[key], device=device, dtype=torch.float64)
            for key in ('train_inputs', 'query_inputs', 'old_labels', 'train_labels')]
        dense = DeepDense(config['width'], 2, 2, 'tanh', config['seed'], device)
        initial_hashes = [array_sha(value.cpu().numpy()) for value in dense.initial_state]
        if initial_hashes != saved['initial_state_sha256']:
            raise ArithmeticError('Dense initialization differs from the saved transfer reference')
        report['initial_state_sha256'] = initial_hashes
        source_tasks = [('old', old_labels)]
        for seed in config['auxiliary_label_seeds']:
            generator = np.random.default_rng(seed)
            values = generator.choice(np.array([-1., 1.]), size=len(inputs))
            values /= np.sqrt(np.mean(values**2))
            if np.allclose(values, arrays['train_labels']) or np.allclose(values, -arrays['train_labels']):
                raise ArithmeticError('Auxiliary labels duplicate the target up to sign')
            arrays[f'auxiliary_labels_{seed}'] = values
            source_tasks.append((f'rademacher_{seed}', torch.as_tensor(values, device=device)))
        for name, task_labels in source_tasks:
            values = task_labels.cpu().numpy()
            report['source_label_tasks'].append(dict(name=name, labels=values.tolist(),
                labels_sha256=array_sha(values), training_rms=float(np.sqrt(np.mean(values**2))),
                target_label_cosine=float(task_labels@labels/(task_labels.norm()*labels.norm())),
                old_label_cosine=float(task_labels@old_labels/(task_labels.norm()*old_labels.norm())),
                equals_target=bool(torch.equal(task_labels, labels))))
        persist()
        rank = config['source_rank']
        compiled = []
        for name, task_labels in source_tasks:
            print(f'pooled transfer: compiling {name}', flush=True)
            source, info = compile_sources(dense, inputs, task_labels, queries,
                horizon=config['horizon'], seconds=remaining(),
                seed=_experiment_seed(config['seed'], 'logarithmic_source'), ranks=(rank,),
                partitions=('new',), step=config['rollout_step'], time_degree=config['time_degree'])
            blocks = source['new'][rank]
            for family in ('h', 'delta'):
                for layer, block in enumerate(blocks[family]):
                    if block.shape != (config['width'], rank) or not bool(torch.isfinite(block).all()):
                        raise ArithmeticError(f'Incomplete rank-{rank} source block: {name}/{family}/{layer}')
                    if float((block.T@block-torch.eye(rank, device=device)).abs().max()) > 1e-8:
                        raise ArithmeticError('Source columns are not orthonormal')
                    source_arrays[f'{name}_{family}_{layer+1}'] = block.cpu().numpy()
            compiled.append(blocks)
            report['sources'][name] = info
            persist()
        pooled = {family: [] for family in ('h', 'delta')}
        for family in pooled:
            for layer in range(2):
                remaining()
                concatenated = torch.cat([source[family][layer] for source in compiled], dim=1)
                left, singular, _ = torch.linalg.svd(concatenated, full_matrices=False)
                block = left[:, :rank].clone()
                pooled[family].append(block)
                source_arrays[f'pooled_{family}_{layer+1}'] = block.cpu().numpy()
                report['pooling'][f'{family}_{layer+1}'] = dict(
                    concatenated_shape=list(concatenated.shape), retained_rank=rank,
                    singular_values=singular.cpu().tolist(),
                    relative_frobenius_tail=float(singular[rank:].norm()/singular.norm()),
                    per_task_residual_frobenius=[float((source[family][layer]-block@(block.T@source[family][layer])).norm())
                                               for source in compiled],
                    orthonormality_max_abs=float((block.T@block-torch.eye(rank, device=device)).abs().max()))
        h = dense.fields(dense.initial_state, inputs)[0][-1]
        gap = float(torch.linalg.eigvalsh(h.T@h/(config['width']*len(inputs)))[0])
        if gap <= 0:
            raise ArithmeticError('Nonpositive initialized training-feature gap')
        floor = min(1e-4, gap/8)
        if not math.isclose(floor, saved['models']['transferred']['diagnostics']['readout_floor'], rel_tol=1e-10):
            raise ArithmeticError('Readout regularization differs from saved old-only transfer')
        for name, source in (('old_only', compiled[0]), ('pooled', pooled)):
            entry = dict(status='inconclusive')
            report['models'][name] = entry
            try:
                remaining()
                model = DeepHarmonic(dense, inputs, old_labels, source, config['budget'],
                    selection_seed=_experiment_seed(config['seed'], 'logarithmic_selector'),
                    readout_floor=floor, selection_trials=config['selection_trials'],
                    condition_limit=config['condition_limit'], selection_strategy='uniform')
                entry['diagnostics'] = model.diagnostics
                if any(value['truncated'] for value in model.diagnostics['source_truncations']):
                    raise ArithmeticError('Constructor applied an additional source truncation')
                before = geometry(model)
                model.initial_state[-1] = labels.clone()
                after = geometry(model)
                if before != after:
                    raise ArithmeticError('Resetting the label deficit changed frozen geometry')
                entry.update(geometry_sha256_before=before, geometry_sha256_after=after,
                    geometry_unchanged=True, learned=sum(value.numel() for value in model.initial_state),
                    fixed=int(model.fixed_scalars))
                _experiment_move(model, device, torch.float32)
                state, prediction, run = integrate_euler(model, inputs.float(), labels.float(),
                    torch.cat((inputs, queries)).float(), config['step'], remaining(),
                    horizon=config['horizon'], observation_every=config['record_every'])
                arrays[name], arrays['times_'+name] = prediction, np.asarray(run['times'])
                entry['run'] = run
                if not run['complete'] or not np.array_equal(arrays['times_'+name], times):
                    raise ArithmeticError('Compact rollout is incomplete or has a different observation grid')
                entry['status'] = 'complete'
                del state, model
            except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
                entry['reason'] = f'{type(error).__name__}: {error}'
                report['errors'][name] = entry['reason']
            persist()
            print(json.dumps(dict(model=name, status=entry['status'], reason=entry.get('reason'))), flush=True)
    except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
        report['errors']['setup'] = f'{type(error).__name__}: {error}'

    m = config['samples']
    reference = arrays['reference'][:, m:].astype(float)
    baseline = np.sqrt(np.mean((arrays['independent_dense'][:, m:].astype(float)-reference)**2, axis=1))
    metrics = {}
    if baseline[-1] <= 0 or baseline.max() <= 0:
        report['errors']['baseline'] = 'Saved dense-pair denominator is zero'
    else:
        for name in ('transferred', 'rebuilt', 'old_only', 'pooled'):
            if name not in arrays or not np.array_equal(arrays['times_'+name], times):
                continue
            error = np.sqrt(np.mean((arrays[name][:, m:].astype(float)-reference)**2, axis=1))
            if not np.isfinite(error).all():
                continue
            endpoint_ratio, maximum_ratio = float(error[-1]/baseline[-1]), float(error.max()/baseline.max())
            metrics[name] = dict(curve=error.tolist(), endpoint_rms=float(error[-1]),
                worst_recorded_rms=float(error.max()), endpoint_ratio=endpoint_ratio,
                worst_recorded_ratio=maximum_ratio, passes_1x=max(endpoint_ratio, maximum_ratio) <= 1)
        if 'old_only' in metrics:
            difference = np.sqrt(np.mean((arrays['old_only'][:, m:].astype(float)-
                                          arrays['transferred'][:, m:].astype(float))**2, axis=1))
            reproduction = dict(endpoint_ratio=float(difference[-1]/baseline[-1]),
                                worst_recorded_ratio=float(difference.max()/baseline.max()), threshold=.1)
            reproduction['pass'] = max(reproduction['endpoint_ratio'], reproduction['worst_recorded_ratio']) <= .1
            report['old_only_reproduction'] = reproduction
            if not reproduction['pass']:
                report['errors']['reproduction'] = 'Old-only rerun exceeded the frozen numerical-agreement gate'
        if 'old_only' in metrics and 'pooled' in metrics:
            report['pooling_comparison'] = {
                field: metrics['pooled'][field]/metrics['old_only'][field]
                for field in ('endpoint_rms', 'worst_recorded_rms')}
            report['pooling_comparison']['improves_both'] = all(
                metrics['pooled'][field] < metrics['old_only'][field]
                for field in ('endpoint_rms', 'worst_recorded_rms'))
        report['baseline'] = dict(endpoint_rms=float(baseline[-1]), worst_recorded_rms=float(baseline.max()),
                                  curve=baseline.tolist())
    report['metrics'] = metrics
    report['complete'] = not report['errors'] and all(
        report['models'].get(name, {}).get('status') == 'complete' for name in ('old_only', 'pooled'))
    report['status'] = ('pass' if metrics['pooled']['passes_1x'] else 'fail') if report['complete'] else 'inconclusive'
    persist()
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
    for name, label, color, style in (
            ('transferred', 'Old-only, saved', '#999999', ':'),
            ('old_only', 'Old-only, rerun', '#1b9970', '-'),
            ('pooled', 'Pooled non-target labels', '#eb6834', '-'),
            ('rebuilt', 'Target sources, saved', '#2a78d6', '--')):
        if name not in metrics:
            continue
        error = np.asarray(metrics[name]['curve'])
        valid = (times > 0) & (baseline > 0)
        axes[0].plot(times[1:], error[1:], color=color, linestyle=style, label=label)
        axes[1].plot(times[valid], error[valid]/baseline[valid], color=color, linestyle=style, label=label)
    axes[0].plot(times[1:], baseline[1:], color='black', linestyle=':', label='Dense pair, saved')
    axes[1].axhline(1, color='black', linestyle=':', label='Dense-pair ratio 1')
    for ax in axes:
        ax.set(xlabel='Training time', yscale='log')
        ax.grid(alpha=.15)
        ax.legend(frameon=False, fontsize=7)
    axes[0].set_ylabel('Declared-query prediction RMS')
    axes[1].set_ylabel('Pointwise RMS / saved dense-pair RMS')
    fig.suptitle(f"Fixed rank 15, compact width 256 · pooled transfer: {report['status']}", fontsize=10)
    fig.tight_layout()
    for extension in ('png', 'pdf'):
        fig.savefig(out/f'pooled_transfer.{extension}', dpi=200)
    plt.close(fig)
    (out/'caption.txt').write_text(
        'Three full-horizon source tasks use the old labels and fixed Rademacher labels from '
        'seeds 4712 and 4713. Each has unit training RMS; none uses the changed target labels. '
        'For each h/delta family and hidden layer, concatenate their orthonormal rank-15 source '
        'columns with equal weight and retain the first 15 left singular vectors. Old-only and '
        'pooled constructors both use width 256, 64 uniform coordinate candidates and condition '
        'cap 16. Only the label-dependent initial deficit is reset to the new target; retained '
        'weights and geometry are hash checked unchanged. The target-task dense reference, '
        'independent dense comparator and rebuilt positive control are saved curves, not rerun. '
        'The fidelity decision uses endpoint RMS and the ratio of separate recorded maxima, '
        'each at most 1; it does not require the plotted pointwise ratio to stay below 1. '
        'Initialization is omitted from ratio plots. The old-only rerun must agree with its '
        'saved curve to within 0.1 of the dense-pair endpoint and maximum RMS. All sources use '
        'RK4 step 1/8 to T=32, and compact deployment uses Euler step 1/160. This bounded '
        'single-seed label-pooling test gives no initialization-only or general-transfer guarantee.\n')
    report['seconds_including_plot'] = time.monotonic()-started
    save_json(out/'report.json', report)
    print(json.dumps(dict(output=str(out), status=report['status'], seconds=report['seconds_including_plot'],
                         comparison=report.get('pooling_comparison'), errors=report['errors'])), flush=True)
    return 0


@torch.no_grad()
def feedback_dense_pairs_main(argv):
    """Measured dense variability with the same independent seed pairs at every width."""
    parser = argparse.ArgumentParser(description=feedback_dense_pairs_main.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text())
    out = Path(config['output'])
    out.mkdir(parents=True, exist_ok=True)
    if (out/'report.json').exists():
        raise FileExistsError('Choose a fresh dense-pair output')
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(config['device'])
    data_config = _experiment_merge(EXPERIMENT_DEFAULTS, {'dataset': config['dataset']})
    arrays = _experiment_data(data_config)
    inputs, labels, queries = [torch.as_tensor(arrays[k], device=device, dtype=torch.float32)
                               for k in ('train_inputs', 'train_labels', 'query_inputs')]
    if len(config['seeds']) != len(config['partner_seeds']) or set(config['seeds']) & set(config['partner_seeds']):
        raise ValueError('Need disjoint equally sized reference and partner seed lists')
    source = Path(__file__).read_bytes()
    (out/'source.py').write_bytes(source)
    save_json(out/'config.json', config)
    report = dict(config=config, source_sha256=sha(source), pairs=[], runs={}, summary=[], errors={},
        scope='Three independent pairs per width. Same seed lists across widths. '
              'No compressed repetitions implied; fitted c/sqrt(n) is descriptive, not the pass threshold.')
    started = time.monotonic()
    def persist():
        np.savez_compressed(out/'trajectories.npz', **arrays)
        report['trajectories_sha256'] = sha((out/'trajectories.npz').read_bytes())
        report['seconds'] = time.monotonic()-started
        save_json(out/'report.json', report)
    for width in config['widths']:
        for seed, partner in zip(config['seeds'], config['partner_seeds']):
            keys = []
            for role, role_seed in (('reference', seed), ('partner', partner)):
                key = f'{role}_n{width}_seed{role_seed}'
                model = DeepDense(width, inputs.shape[1], config['depth'], config['activation'], role_seed, device)
                _experiment_move(model, device, torch.float32)
                state, prediction, run = integrate_euler(model, inputs, labels,
                    torch.cat((inputs, queries)), config['step'], config['seconds'],
                    horizon=config['horizon'], observation_every=config['record_every'])
                del model, state
                arrays[key], arrays['times_'+key] = prediction, np.asarray(run['times'])
                report['runs'][key] = run
                keys.append(key)
                if not run['complete']:
                    report['errors'][key] = run['stop_reason']
                persist()
            if not any(key in report['errors'] for key in keys):
                assert np.array_equal(arrays['times_'+keys[0]], arrays['times_'+keys[1]])
                metric = trajectory_rms(arrays[keys[0]][:, len(labels):], arrays[keys[1]][:, len(labels):])
                report['pairs'].append(dict(width=width, seed=seed, partner_seed=partner, **metric))
                print(json.dumps(dict(width=width, seed=seed, endpoint_rms=metric['endpoint_rms'],
                                      max_time_rms=metric['max_time_rms'])), flush=True)
                persist()
    for width in config['widths']:
        rows = [p for p in report['pairs'] if p['width'] == width]
        row = dict(width=width, count=len(rows))
        for metric in ('endpoint_rms', 'max_time_rms'):
            values = np.asarray([p[metric] for p in rows])
            row[metric] = dict(mean=float(values.mean()) if len(values) else None,
                              sd=float(values.std(ddof=1)) if len(values) > 1 else None,
                              values=values.tolist())
        report['summary'].append(row)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.4))
    for axis, metric, title in zip(axes, ('endpoint_rms', 'max_time_rms'), ('Endpoint', 'Worst recorded')):
        rows = [p for p in report['summary'] if p['count']]
        widths = np.asarray([p['width'] for p in rows])
        means = np.asarray([p[metric]['mean'] for p in rows])
        deviations = np.asarray([p[metric]['sd'] or 0 for p in rows])
        axis.errorbar(widths, means, yerr=[np.minimum(deviations, .95*means), deviations],
                      fmt='o-', capsize=3, label='Mean ± SD')
        for row in rows:
            axis.scatter(np.full(row['count'], row['width']), row[metric]['values'],
                         color='#0072B2', alpha=.4, s=14)
        coefficient = float(np.mean(means*np.sqrt(widths)))
        report.setdefault('descriptive_sqrt_fits', {})[metric] = coefficient
        axis.plot(widths, coefficient/np.sqrt(widths), '--', color='grey', label='Fitted c/√n')
        axis.set(xscale='log', yscale='log', xlabel='Dense width', ylabel='Dense-pair RMS', title=title)
        axis.grid(alpha=.15)
        axis.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    for extension in ('png', 'pdf'):
        fig.savefig(out/f'dense_pairs.{extension}', dpi=180)
    plt.close(fig)
    report['complete'] = not report['errors']
    persist()
    return int(bool(report['errors']))


def _experiment_seed(seed, role):
    # Stable under changes to method order, budgets, process scheduling, or Python's hash salt.
    value = int(sha(f'{seed}:{role}'.encode())[:15], 16)
    return value if value != seed else value+1


def _experiment_move(model, device, dtype):
    if isinstance(model, PanelSpanModel):
        _experiment_move(model.core, device, dtype)
        model.initial_state = model.core.initial_state
        model.input_basis = model.input_basis.to(device=device, dtype=dtype)
        return model
    for key in ('initial_state', 'metrics', 'metric_inverses'):
        if hasattr(model, key):
            setattr(model, key, [v.to(device=device, dtype=dtype) for v in getattr(model, key)])
    for key in ('first', 'matrix', 'degrees', 'weights', 'kernel', 'cross', 'train_inputs', 'query_inputs'):
        if hasattr(model, key):
            setattr(model, key, getattr(model, key).to(device=device, dtype=dtype))
    return model


@torch.no_grad()
def _experiment_repetition(config, seed, device_name, out, manifest):
    """One dense reference and freshly coupled models; no cross-repetition teacher reuse."""
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = config['execution']['tf32']
    torch.backends.cudnn.allow_tf32 = config['execution']['tf32']
    device, dtype = torch.device(device_name), getattr(torch, config['training']['dtype'])
    arrays = _experiment_data(config)
    if {key: array_sha(value) for key, value in arrays.items()} != manifest['identity']['data_sha256']:
        raise RuntimeError('Dataset changed after launch; refusing inconsistent repetitions')
    inputs, labels, queries = [torch.as_tensor(arrays[key], device=device) for key in
                              ('train_inputs', 'train_labels', 'query_inputs')]
    extra_queries = (torch.as_tensor(arrays['extra_query_inputs'], device=device)
                     if 'extra_query_inputs' in arrays else queries[:0])
    scored_queries = torch.cat((queries, extra_queries))
    model_config, training = config['model'], config['training']
    n, d = model_config['width'], inputs.shape[1]
    seconds = config['execution']['seconds_per_fit']
    started = time.monotonic()
    report = dict(seed=seed, fingerprint=manifest['fingerprint'], source_sha256=manifest['source_sha256'],
        complete=False, models={}, runs={}, sources={}, errors={}, skipped={}, seeds={'reference': seed},
        data_sha256={key: array_sha(value) for key, value in arrays.items()},
        device=device_name, hardware=torch.cuda.get_device_name(device) if device.type == 'cuda' else platform.processor(),
        scope=dict(initialization='Gaussian, zero readout; original canonical mean-field mobilities',
            comparisons='each model versus its own repetition dense reference, fixed dataset',
            accuracy='finite held-out RMS at common recorded Euler times; no GF refinement certificate',
            source_setup='full-horizon RK4 rollouts, empirical source-rank truncation, not initialization jets',
            queries='Logarithmic setup sees declared query inputs, never labels or the separate extra query panel',
            storage='retained model coordinates, common data/integrator/temporary setup excluded'))

    def persist():
        np.savez_compressed(out/'trajectories.npz', **arrays)
        report['trajectories_sha256'] = sha((out/'trajectories.npz').read_bytes())
        report['seconds'] = time.monotonic()-started
        save_json(out/'report.json', report)

    def role_seed(role):
        report['seeds'][role] = _experiment_seed(seed, role)
        return report['seeds'][role]

    def fit(name, model, family, setup_seconds=0., **details):
        print(json.dumps(dict(event='fit', seed=seed, model=name, device=device_name)), flush=True)
        moving, fixed = sum(v.numel() for v in model.initial_state), int(model.fixed_scalars)
        record = dict(family=family, moving=moving, fixed=fixed, total=moving+fixed,
            setup_seconds=setup_seconds, diagnostics=getattr(model, 'diagnostics', {}), **details)
        if family == 'frozen_features':
            record.update(moving=n, fixed=n*d+(model_config['depth']-1)*n*n,
                          total=n+n*d+(model_config['depth']-1)*n*n,
                          executed_dual_state=dict(moving=moving, fixed=fixed, data=model.data_scalars),
                          storage_basis='primal frozen dense features and width-n trained readout; equivalent dual Euler executed')
        report['models'][name] = record
        _experiment_move(model, device, dtype)
        fit_seconds = config['execution']['dense_seconds_per_fit'] if family in ('reference', 'dense') else seconds
        state, prediction, info = integrate_euler(model, inputs.to(dtype), labels.to(dtype),
            torch.cat((inputs, scored_queries)).to(dtype), training['step'], fit_seconds,
            horizon=training['horizon'], max_steps=math.ceil(training['horizon']/training['step']),
            observation_every=training['record_every'])
        arrays[name], arrays['times_'+name] = prediction[:, :len(inputs)+len(queries)], np.asarray(info['times'])
        if len(extra_queries):
            arrays['extra_'+name] = prediction[:, len(inputs)+len(queries):]
        report['runs'][name] = info
        if not info['complete']:
            report['errors'][name] = 'Inconclusive: '+info['stop_reason']
        print(json.dumps(dict(event='fit_done', seed=seed, model=name, seconds=info['seconds'],
                              complete=info['complete'], training_mse=info['final_training_mse'])), flush=True)
        del state
        persist()

    def build_fit(name, family, constructor, **details):
        t0 = time.monotonic()
        try:
            model = constructor()
            synchronize(device)
            elapsed = time.monotonic()-t0
            if elapsed > seconds:
                raise TimeoutError('Model assembly exceeded seconds_per_fit')
            fit(name, model, family, elapsed, **details)
        except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
            report['errors'][name] = f'{type(error).__name__}: {error}'
            print(json.dumps(dict(event='model_error', seed=seed, model=name, error=str(error))), flush=True)
            persist()

    def matched(name, remaining):
        comparator = f'dense_{n}'
        if not config['execution']['stop_after_match'] or not all(
                report['runs'].get(key, {}).get('complete') for key in (name, comparator)):
            return False
        reference = arrays['reference'][:, len(labels):].astype(float)
        error = np.sqrt(np.mean((arrays[name][:, len(labels):].astype(float)-reference)**2, axis=1))
        baseline = np.sqrt(np.mean((arrays[comparator][:, len(labels):].astype(float)-reference)**2, axis=1))
        passed = bool(error[-1] <= baseline[-1] and error.max() <= baseline.max())
        if passed:
            report['skipped'].update({key: f'Larger budget not needed after {name} matched both RMS criteria'
                                      for key in remaining})
            print(json.dumps(dict(event='budget_matched', seed=seed, model=name,
                                  endpoint_ratio=float(error[-1]/baseline[-1]) if baseline[-1] else None,
                                  worst_ratio=float(error.max()/baseline.max()) if baseline.max() else None)), flush=True)
            persist()
        return passed

    try:
        t0 = time.monotonic()
        dense = DeepDense(n, d, model_config['depth'], model_config['activation'], seed, device)
        synchronize(device)
        dense_seconds = time.monotonic()-t0
        report['reference_initial_state_sha256'] = [array_sha(v.cpu().numpy()) for v in dense.initial_state]
        # Keep the untouched float64 initialization for every source/constructor.
        runtime = DeepDense.__new__(DeepDense)
        runtime.depth, runtime.activation, runtime.fixed_scalars = dense.depth, dense.activation, 0
        runtime.initial_state = [v.to(dtype=dtype) for v in dense.initial_state]
        fit('reference', runtime, 'reference', dense_seconds, width=n)
        del runtime
        if not report['runs']['reference']['complete']:
            return 1
        oblivious = config['methods']['oblivious']
        panel_rank = None
        if config['methods']['non_oblivious']['logarithmic'].get('panel_span', False):
            panel_rank = int(torch.linalg.matrix_rank(torch.cat((inputs, queries)).double()))
        controls = _experiment_matched_controls(config, n, d, panel_rank=panel_rank)
        if any(oblivious[family].get('match_compressions', False) for family in ('dense', 'low_rank')):
            report['matched_controls'] = controls
            report['skipped'].update(controls['skipped'])
        for width, targets in controls['dense'].items():
            init_seed = role_seed(f'dense_{width}')
            build_fit(f'dense_{width}', 'dense', lambda: DeepDense(width, d, dense.depth,
                dense.activation, init_seed, device), width=width, initialization_seed=init_seed,
                **(dict(matched_compression_budgets=targets) if targets else {}))
        for index, order in enumerate(oblivious['legendre']['orders']):
            build_fit(f'legendre_{order}', 'legendre',
                      lambda: LegendreCompression(dense, inputs, labels, order), order=order)
            if matched(f'legendre_{order}', [f'legendre_{q}' for q in oblivious['legendre']['orders'][index+1:]]):
                break
        for rank, targets in controls['low_rank'].items():
            adapter_seed = role_seed(f'low_rank_{rank}')
            budget = n+min(rank, n, d)*(n+d)+2*n*rank
            build_fit(f'low_rank_{rank}', 'low_rank', lambda: BudgetLoRA(dense, budget, adapter_seed),
                      rank=rank, initialization_seed=adapter_seed,
                      **(dict(matched_compression_budgets=targets) if targets else {}))
        if oblivious['frozen_features']['enabled']:
            build_fit('frozen_features', 'frozen_features', lambda: FrozenNTK(dense, inputs, scored_queries))
        for family in ('harmonic', 'logarithmic'):
            method = config['methods']['non_oblivious'][family]
            if not method['budgets']:
                continue
            setup = _experiment_setup(config, family)
            ranks = sorted({v['source_rank'] for v in method['budgets']}, reverse=True)
            source_seed = role_seed(f'{family}_source')
            selector_seed = role_seed(f'{family}_selector')
            print(json.dumps(dict(event='source_setup', seed=seed, method=family)), flush=True)
            try:
                setup_dense, setup_inputs, setup_queries = dense, inputs, queries
                input_basis, panel_info = None, None
                if family == 'logarithmic' and method.get('panel_span', False):
                    setup_dense, input_basis, panel_info = _panel_span_dense(dense, inputs, queries)
                    setup_inputs, setup_queries = inputs@input_basis, queries@input_basis
                options = dict(seconds=seconds, step=setup['rollout_step'], time_degree=setup['time_degree'],
                    rollout_dtype=setup['rollout_dtype'], coefficient_dtype=setup['coefficient_dtype'])
                if family == 'harmonic':
                    source, info = unified_harmonic_sources(dense, inputs, labels,
                        training['horizon'], ranks[0], source_seed, spatial_degree=method['spatial_degree'], **options)
                    sources = {rank: {key: [v[:, :rank] for v in values] for key, values in source.items()}
                               for rank in ranks}
                    del source
                    info['prefix_diagnostics_scope'] = 'Source checks describe largest rank; smaller prefixes are not separately checked'
                    floor = None
                else:
                    sources, info = cubic_rollout_sources(setup_dense, setup_inputs, labels, setup_queries,
                        training['horizon'], seed=source_seed, ranks=tuple(ranks), partitions=('new',), **options)
                    sources = sources['new']
                    features = dense.fields(dense.initial_state, inputs)[0][-1]
                    gap = float(torch.linalg.eigvalsh(features.T@features/(n*len(labels)))[0])
                    if gap <= 0:
                        raise ArithmeticError('Initial normalized training feature Gram has no positive gap')
                    floor = min(1e-4, gap/8)
                    info['readout_floor'] = floor
                    if panel_info is not None:
                        info['panel_span'] = panel_info
                info['effective_setup'] = setup
                report['sources'][family] = info
                for index, budget in enumerate(method['budgets']):
                    width, rank = budget['width'], budget['source_rank']
                    name = f'{family}_{width}_r{rank}'

                    def construct():
                        model = DeepHarmonic(setup_dense, setup_inputs, labels, sources[rank], width,
                            selection_seed=selector_seed, readout_floor=floor,
                            selection_trials=setup['selection_trials'], condition_limit=setup['condition_limit'],
                            selection_strategy=setup['selection_strategy'])
                        if any(item['truncated'] for item in model.diagnostics['source_truncations']):
                            raise ArithmeticError('Budget requires extra constructor truncation; result inconclusive, not silently substituted')
                        return (PanelSpanModel(model, input_basis, panel_info)
                                if input_basis is not None else model)

                    build_fit(name, family, construct, width=width, source_rank=rank, shared_source=family,
                              source_seed=source_seed, selection_seed=selector_seed)
                    if matched(name, [f"{family}_{v['width']}_r{v['source_rank']}"
                                      for v in method['budgets'][index+1:]]):
                        break
                del sources
            except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
                report['errors'][family+'_setup'] = f'{type(error).__name__}: {error}'
                print(json.dumps(dict(event='source_error', seed=seed, method=family, error=str(error))), flush=True)
                persist()
        report['complete'] = not report['errors']
        return 0 if report['complete'] else 1
    finally:
        persist()


def _budget_search_next(observations, tolerance, minimum=1, start=None, maximum=None, sequential=False):
    """Choose a local width bracket or scan integer orders without monotonicity."""
    if sequential:
        # Integer-order searches must test every smaller order, not assume
        # monotone accuracy. An inconclusive order cannot certify a minimum.
        for q in range(minimum, maximum+1):
            status = observations.get(q, {}).get('status')
            bracket = dict(lower=q-1 if q > minimum else None,
                           upper=q if status == 'pass' else None,
                           ratio=q/(q-1) if status == 'pass' and q > minimum else None,
                           status=('minimum_order' if q == minimum else 'resolved_local')
                                  if status == 'pass' else 'expanding')
            if status == 'pass' or status is None:
                return (q if status is None else None), bracket
            if status != 'fail':
                bracket.update(status='inconclusive_order', order=q)
                return None, bracket
        return None, dict(lower=maximum, upper=None, ratio=None, status='no_passing_upper_at_cap')
    passed = sorted(q for q, value in observations.items() if value['status'] == 'pass')
    if not passed:
        if start is not None:
            q = min(maximum, 2*max(observations) if observations else start)
            bracket = dict(lower=None, upper=None, ratio=None,
                           status='expanding' if q not in observations else 'no_passing_upper_at_cap')
            return (q if q not in observations else None), bracket
        return None, dict(lower=None, upper=None, ratio=None, status='no_passing_upper')
    upper = passed[0]
    failed = [q for q, value in observations.items() if q < upper and value['status'] == 'fail']
    lower = max(failed, default=minimum-1)
    bracket = dict(lower=lower if failed else None, upper=upper,
                   ratio=upper/lower if failed else None, status='refining',
                   nonmonotone=any(q > upper and v['status'] == 'fail' for q, v in observations.items()))
    if upper == minimum or (failed and (upper <= lower+1 or upper/lower <= 1+tolerance)):
        bracket['status'] = 'minimum_order' if upper == minimum else 'resolved_local'
        return None, bracket
    # A failed constructor gives no accuracy bound. For the next proposal only,
    # move above it rather than spending the fit cap on its immediate neighbors.
    # Keep the reported lower crossing tied exclusively to measured failures.
    blocked = [q for q, value in observations.items()
               if lower < q < upper and value['status'] == 'inconclusive']
    proposal_lower = max(blocked, default=lower)
    if blocked and (upper <= proposal_lower+1 or upper/proposal_lower <= 1+tolerance):
        bracket.update(status='inconclusive_lower', construction_floor=proposal_lower)
        return None, bracket
    midpoint = (proposal_lower+upper)//2
    available = [q for q in range(max(minimum, proposal_lower+1), upper) if q not in observations]
    if not available:
        bracket['status'] = 'inconclusive_gap'
        return None, bracket
    return min(available, key=lambda q: (abs(q-midpoint), q)), bracket


@torch.no_grad()
def _budget_search_worker(out, device_name, plan):
    """Refine existing brackets, preserving the old source SVD maximum and seeds."""
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    manifest = json.loads((out/'run.json').read_text())
    if sha(Path(__file__).read_bytes()) != manifest['source_sha256']:
        raise RuntimeError('Budget-search source changed after launch')
    config = manifest['config']
    seed, n = config['seeds'][0], config['model']['width']
    source_max_ranks = plan.get('source_max_ranks_by_width', {}).get(
        str(n), plan.get('source_max_ranks', {}))
    if plan.get('restart_harmonic'):
        source_max_ranks = dict(source_max_ranks, harmonic=plan['restart_harmonic']['source_max_rank'])
    path = out/manifest['repetitions'][str(seed)]
    report = json.loads((path/'report.json').read_text())
    if sha((path/'trajectories.npz').read_bytes()) != report['trajectories_sha256']:
        raise RuntimeError('Reused trajectory hash mismatch')
    with np.load(path/'trajectories.npz', allow_pickle=False) as saved:
        arrays = {key: saved[key] for key in saved.files}
    torch.backends.cuda.matmul.allow_tf32 = config['execution']['tf32']
    torch.backends.cudnn.allow_tf32 = config['execution']['tf32']
    device = torch.device(device_name)
    dtype = getattr(torch, config['training']['dtype'])
    inputs, labels, queries = [torch.as_tensor(arrays[key], device=device) for key in
                              ('train_inputs', 'train_labels', 'query_inputs')]
    training, seconds = config['training'], config['execution']['seconds_per_fit']
    reference = arrays['reference'][:, len(labels):].astype(float)
    baseline = np.sqrt(np.mean((arrays[f'dense_{n}'][:, len(labels):].astype(float)-reference)**2, axis=1))
    thresholds = plan['factor']*np.array([baseline[-1], baseline.max()])
    started = time.monotonic()
    dense = DeepDense(n, inputs.shape[1], config['model']['depth'], config['model']['activation'], seed, device)
    if [array_sha(v.cpu().numpy()) for v in dense.initial_state] != report['reference_initial_state_sha256']:
        raise RuntimeError('Regenerated dense initialization differs from saved reference')

    def persist():
        np.savez_compressed(path/'trajectories.npz', **arrays)
        report['trajectories_sha256'] = sha((path/'trajectories.npz').read_bytes())
        report['seconds'] = time.monotonic()-started
        save_json(path/'report.json', report)

    def observed(family):
        values = {}
        for name, model in report['models'].items():
            if model['family'] != family:
                continue
            q = model['order' if family == 'legendre' else 'width']
            value = dict(name=name, status='inconclusive')
            if report['runs'].get(name, {}).get('complete'):
                if not np.array_equal(arrays['times_'+name], arrays['times_reference']):
                    raise RuntimeError('Candidate/reference time grids differ')
                error = np.sqrt(np.mean((arrays[name][:, len(labels):].astype(float)-reference)**2, axis=1))
                metrics = np.array([error[-1], error.max()])
                value.update(status='pass' if np.all(metrics <= thresholds) else 'fail',
                             endpoint_rms=float(metrics[0]), worst_recorded_rms=float(metrics[1]),
                             endpoint_ratio=float(metrics[0]/baseline[-1]),
                             worst_recorded_ratio=float(metrics[1]/baseline.max()))
            values[q] = value
        # Constructor failures may precede the creation of a model record.
        search = report['budget_search'][family]
        for request in search.get('inherited_requested', [])+search['requested']:
            q = request.get('order', request.get('width'))
            values.setdefault(q, dict(status='inconclusive', name=request['name']))
        return values

    for family in ('legendre', 'harmonic', 'logarithmic'):
        search = report['budget_search'][family]
        if family not in plan.get('families', ('legendre', 'harmonic', 'logarithmic')):
            search['bracket'] = dict(status='not_requested')
            continue
        source, floor, setup = None, None, None
        setup_dense, setup_inputs, setup_queries = dense, inputs, queries
        input_basis, panel_info = None, None
        expansion = dict(plan.get('expansion', {}).get(family, {}))
        if expansion and plan.get('cap_below_dense', False):
            expansion['maximum'] = min(expansion['maximum'], n-1)
            expansion['start'] = min(expansion['start'], expansion['maximum'])
        for _ in range(plan.get('max_new_by_width', {}).get(str(n), plan['max_new_per_family'])):
            observations = observed(family)
            q, search['bracket'] = _budget_search_next(observations, plan['width_tolerance'], **expansion)
            search['evaluations'] = observations
            persist()
            if q is None:
                break
            rank = max(1, math.floor((q/4-17)/3))
            if family != 'legendre' and plan.get('rank_rule') == 'cap_at_source':
                maximum_rank = max((v['source_rank'] for v in
                    config['methods']['non_oblivious'][family]['budgets']),
                    default=source_max_ranks.get(family, 0))
                if maximum_rank < 1:
                    raise ValueError('Capped rank proposals require a frozen source maximum')
                rank = min(rank, maximum_rank)
            if family != 'legendre' and plan.get('rank_rule') == 'interpolate_budgets':
                knots = sorted(plan.get('rank_knots', {}).get(family,
                    config['methods']['non_oblivious'][family]['budgets']),
                               key=lambda value: value['width'])
                if not knots or not knots[0]['width'] <= q <= knots[-1]['width']:
                    raise ValueError('Interpolated source ranks require a bracketing original budget ladder')
                rank = max(1, math.floor(np.interp(q, [v['width'] for v in knots],
                                                   [v['source_rank'] for v in knots])))
            name = f'legendre_{q}' if family == 'legendre' else f'{family}_{q}_r{rank}'
            request = dict(name=name, order=q) if family == 'legendre' else dict(name=name, width=q, source_rank=rank)
            search['requested'].append(request)
            report['skipped'].pop(name, None)
            persist()
            print(json.dumps(dict(event='refine_fit', width=n, family=family, q=q, device=device_name)), flush=True)
            try:
                if family != 'legendre' and source is None:
                    method = config['methods']['non_oblivious'][family]
                    if family == 'logarithmic' and method.get('panel_span', False):
                        setup_dense, input_basis, panel_info = _panel_span_dense(dense, inputs, queries)
                        setup_inputs, setup_queries = inputs@input_basis, queries@input_basis
                    maximum = max((v['source_rank'] for v in method['budgets']),
                                  default=source_max_ranks.get(family, 0))
                    if maximum < 1:
                        raise ValueError('Fresh spectral searches require a frozen source_max_ranks entry')
                    setup = _experiment_setup(config, family)
                    options = dict(seconds=seconds, step=setup['rollout_step'], time_degree=setup['time_degree'],
                                   rollout_dtype=setup['rollout_dtype'], coefficient_dtype=setup['coefficient_dtype'])
                    for role in ('source', 'selector'):
                        key = family+'_'+role
                        report['seeds'].setdefault(key, _experiment_seed(seed, key))
                    source_seed = report['seeds'][family+'_source']
                    old_info = report['sources'].get(family)
                    if family == 'harmonic':
                        source, info = unified_harmonic_sources(dense, inputs, labels, training['horizon'],
                            maximum, source_seed, spatial_degree=method['spatial_degree'], **options)
                        old_checks = old_info['diagnostics'] if old_info else None
                        new_checks = info['diagnostics']
                    else:
                        sources, info = cubic_rollout_sources(setup_dense, setup_inputs, labels, setup_queries, training['horizon'],
                            seed=source_seed, ranks=(maximum,), partitions=('new',), **options)
                        source = sources['new'][maximum]
                        if old_info:
                            floor = old_info['readout_floor']
                        else:
                            features = dense.fields(dense.initial_state, inputs)[0][-1]
                            gap = float(torch.linalg.eigvalsh(features.T@features/(n*len(labels)))[0])
                            if gap <= 0:
                                raise ArithmeticError('Initial normalized training feature Gram has no positive gap')
                            floor = min(1e-4, gap/8)
                        info['readout_floor'] = floor
                        if panel_info is not None:
                            info['panel_span'] = panel_info
                        old_checks = old_info['partitions']['new']['diagnostics'][str(maximum)] if old_info else None
                        new_checks = info['partitions']['new']['diagnostics'][str(maximum)]
                    if old_checks is not None:
                        for key in ('h', 'delta'):
                            for old, new in zip(old_checks[key], new_checks[key]):
                                np.testing.assert_allclose(new['residual_coefficient_relative_error'],
                                    old['residual_coefficient_relative_error'], rtol=1e-7, atol=1e-10)
                    info['effective_setup'] = setup
                    if old_info is None:
                        report['sources'][family] = info
                    search['source_reconstruction'] = dict(maximum_rank=maximum, report=info,
                        checks=('original initialization hashes and largest-rank source residuals match' if old_info
                                else 'new source from hash-verified initialization; frozen maximum rank for all prefixes'),
                        source_hashes={key: [array_sha(v.cpu().numpy()) for v in values]
                                       for key, values in source.items()})
                    if family == 'harmonic' and 'harmonic_source_replacement' in report:
                        if search['source_reconstruction']['source_hashes'] != report['harmonic_source_replacement']['source_hashes']:
                            raise AssertionError('Repaired Harmonic source hashes changed on reconstruction')
                t0 = time.monotonic()
                if family == 'legendre':
                    model = LegendreCompression(dense, inputs, labels, q)
                    details = dict(order=q)
                else:
                    if rank > maximum:
                        raise ValueError('Refinement would change original source SVD maximum')
                    prefix = {key: [v[:, :rank] for v in values] for key, values in source.items()}
                    model = DeepHarmonic(setup_dense, setup_inputs, labels, prefix, q,
                        selection_seed=report['seeds'][family+'_selector'], readout_floor=floor,
                        selection_trials=setup['selection_trials'], condition_limit=setup['condition_limit'],
                        selection_strategy=setup['selection_strategy'])
                    if any(item['truncated'] for item in model.diagnostics['source_truncations']):
                        raise ArithmeticError('Extra constructor truncation is not permitted')
                    if input_basis is not None:
                        model = PanelSpanModel(model, input_basis, panel_info)
                    details = dict(width=q, source_rank=rank, shared_source=family,
                                   source_seed=report['seeds'][family+'_source'],
                                   selection_seed=report['seeds'][family+'_selector'])
                synchronize(device)
                elapsed = time.monotonic()-t0
                if elapsed > seconds:
                    raise TimeoutError('Assembly exceeded per-fit cap')
                moving, fixed = sum(v.numel() for v in model.initial_state), int(model.fixed_scalars)
                report['models'][name] = dict(family=family, moving=moving, fixed=fixed, total=moving+fixed,
                    setup_seconds=elapsed, diagnostics=getattr(model, 'diagnostics', {}), **details)
                _experiment_move(model, device, dtype)
                state, prediction, info = integrate_euler(model, inputs.to(dtype), labels.to(dtype),
                    torch.cat((inputs, queries)).to(dtype), training['step'], seconds,
                    horizon=training['horizon'], max_steps=math.ceil(training['horizon']/training['step']),
                    observation_every=training['record_every'])
                arrays[name], arrays['times_'+name] = prediction, np.asarray(info['times'])
                report['runs'][name] = info
                if not info['complete']:
                    report['errors'][name] = 'Inconclusive: '+info['stop_reason']
                del state, model
            except (ValueError, RuntimeError, ArithmeticError, TimeoutError, AssertionError) as error:
                report['errors'][name] = f'{type(error).__name__}: {error}'
                # A failed common source check invalidates this family, not just q.
                if source is None or isinstance(error, AssertionError):
                    search['bracket']['status'] = 'source_inconclusive'
                    persist()
                    break
            observations = observed(family)
            print(json.dumps(dict(event='refine_result', width=n, family=family, q=q,
                                  **observations[q], error=report['errors'].get(name))), flush=True)
            persist()
        if search['bracket']['status'] != 'source_inconclusive':
            search['evaluations'] = observed(family)
            _, search['bracket'] = _budget_search_next(search['evaluations'], plan['width_tolerance'], **expansion)
            if search['bracket']['status'] in ('refining', 'expanding'):
                search['bracket']['status'] = 'evaluation_cap'
        print(json.dumps(dict(event='refinement_done', width=n, family=family, bracket=search['bracket'])), flush=True)
        persist()
        del source
    report['search_complete'] = True
    persist()
    return 0


@torch.no_grad()
def harmonic_order_probe_main(argv):
    """Change one source order against a saved dense pair, keeping compact size fixed."""
    parser = argparse.ArgumentParser(description=harmonic_order_probe_main.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--case', required=True)
    parser.add_argument('--device', default='cuda:0')
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text())
    request = config['cases'][args.case]
    root = Path(config['reference_run'])
    manifest = json.loads((root/'run.json').read_text())
    original_config = manifest['config']
    seed = original_config['seeds'][0]
    old_path = root/manifest['repetitions'][str(seed)]
    old = json.loads((old_path/'report.json').read_text())
    archive_bytes = (old_path/'trajectories.npz').read_bytes()
    if sha(archive_bytes) != old['trajectories_sha256']:
        raise ValueError('Saved reference trajectory hash mismatch')
    with np.load(old_path/'trajectories.npz', allow_pickle=False) as saved:
        arrays = {key: saved[key] for key in ('train_inputs', 'train_labels', 'query_inputs',
            'reference', 'times_reference', config['baseline_model'],
            f"dense_{original_config['model']['width']}")}
    out = Path(config['output'])/args.case
    out.mkdir(parents=True, exist_ok=False)
    (out/'source.py').write_bytes(Path(__file__).read_bytes())
    save_json(out/'config.json', config)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = original_config['execution']['tf32']
    torch.backends.cudnn.allow_tf32 = original_config['execution']['tf32']
    device = torch.device(args.device)
    training, architecture = original_config['training'], original_config['model']
    setup = _experiment_setup(original_config, 'harmonic')
    report = dict(case=args.case, request=request, compact_width=config['compact_width'],
        source_sha256=sha(Path(__file__).read_bytes()), config_sha256=sha(args.config.read_bytes()),
        reference_run=str(root.resolve()), original_report_sha256=sha((old_path/'report.json').read_bytes()),
        original_trajectories_sha256=sha(archive_bytes), status='inconclusive',
        command=sys.argv, cwd=str(Path.cwd()), training=training, architecture=architecture,
        seeds={k: old['seeds'][k] for k in ('reference', 'harmonic_source', 'harmonic_selector')},
        environment=dict(python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
            device=str(device), hardware=torch.cuda.get_device_name(device), threads=1,
            tf32=original_config['execution']['tf32']),
        scope='Finite Euler fixed-budget source-order diagnostic; offline full-horizon sources; '
              'no dense retraining or query-label use; not a theorem or all-time certificate')
    started = time.monotonic()
    save_json(out/'report.json', report)
    try:
        inputs, labels, queries = [torch.as_tensor(arrays[k], device=device) for k in
                                   ('train_inputs', 'train_labels', 'query_inputs')]
        dense = DeepDense(architecture['width'], inputs.shape[1], architecture['depth'],
                          architecture['activation'], seed, device)
        initial_hashes = [array_sha(v.cpu().numpy()) for v in dense.initial_state]
        if initial_hashes != old['reference_initial_state_sha256']:
            raise ArithmeticError('Regenerated initialization differs from saved reference')
        report['initial_state_sha256'] = initial_hashes
        source, info = unified_harmonic_sources(dense, inputs, labels, training['horizon'],
            request['source_rank'], old['seeds']['harmonic_source'], seconds=config['seconds_per_fit'],
            step=setup['rollout_step'], time_degree=request['time_degree'],
            spatial_degree=request['spatial_degree'], rollout_dtype=setup['rollout_dtype'],
            coefficient_dtype=setup['coefficient_dtype'])
        report['source'] = info
        report['source_hashes'] = {k: [array_sha(v.cpu().numpy()) for v in values]
                                   for k, values in source.items()}
        t0 = time.monotonic()
        model = DeepHarmonic(dense, inputs, labels, source, config['compact_width'],
            selection_seed=old['seeds']['harmonic_selector'], readout_floor=None,
            selection_trials=setup['selection_trials'], condition_limit=setup['condition_limit'],
            selection_strategy=setup['selection_strategy'])
        if any(v['truncated'] for v in model.diagnostics['source_truncations']):
            raise ArithmeticError('Extra source truncation is not allowed')
        synchronize(device)
        report['model'] = dict(learned=sum(v.numel() for v in model.initial_state),
            fixed=int(model.fixed_scalars), setup_seconds=time.monotonic()-t0,
            diagnostics=model.diagnostics)
        report['model']['total'] = report['model']['learned']+report['model']['fixed']
        dtype = getattr(torch, training['dtype'])
        _experiment_move(model, device, dtype)
        del source, dense
        state, prediction, run = integrate_euler(model, inputs.to(dtype), labels.to(dtype),
            torch.cat((inputs, queries)).to(dtype), training['step'], config['seconds_per_fit'],
            horizon=training['horizon'], observation_every=training['record_every'])
        del state, model
        report['run'] = run
        arrays.update(prediction=prediction, times=np.asarray(run['times']))
        if not run['complete'] or not np.array_equal(arrays['times'], arrays['times_reference']):
            raise ArithmeticError('Incomplete trajectory or mismatched reference time grid')
        m = len(labels)
        reference = arrays['reference'][:, m:].astype(float)
        baseline = np.sqrt(np.mean((arrays[f"dense_{architecture['width']}"][:, m:].astype(float)-reference)**2, axis=1))
        error = np.sqrt(np.mean((prediction[:, m:].astype(float)-reference)**2, axis=1))
        if not np.isfinite(error).all() or min(baseline[-1], baseline.max()) <= 0:
            raise ArithmeticError('Invalid error or dense-pair denominator')
        report['metrics'] = dict(endpoint_rms=float(error[-1]), worst_recorded_rms=float(error.max()),
            endpoint_ratio=float(error[-1]/baseline[-1]), worst_recorded_ratio=float(error.max()/baseline.max()),
            dense_endpoint_rms=float(baseline[-1]), dense_worst_recorded_rms=float(baseline.max()),
            final_training_mse=float(run['losses'][-1]))
        report['status'] = 'pass' if error[-1] <= baseline[-1] and error.max() <= baseline.max() else 'fail'
        if request.get('reproduction'):
            difference = np.sqrt(np.mean((prediction[:, m:].astype(float)-
                arrays[config['baseline_model']][:, m:].astype(float))**2, axis=1))
            report['reproduction'] = dict(bitwise_equal=bool(np.array_equal(prediction, arrays[config['baseline_model']])),
                endpoint_ratio=float(difference[-1]/baseline[-1]),
                worst_recorded_ratio=float(difference.max()/baseline.max()), threshold=0.01)
            if max(report['reproduction']['endpoint_ratio'], report['reproduction']['worst_recorded_ratio']) > 0.01:
                raise ArithmeticError('Baseline reproduction exceeded1% of the dense benchmark')
    except (ValueError, RuntimeError, ArithmeticError, TimeoutError, AssertionError) as error:
        report.update(status='inconclusive', reason=f'{type(error).__name__}: {error}')
    finally:
        np.savez_compressed(out/'trajectories.npz', **arrays)
        report['trajectories_sha256'] = sha((out/'trajectories.npz').read_bytes())
        report['seconds'] = time.monotonic()-started
        save_json(out/'report.json', report)
    print(json.dumps(dict(case=args.case, status=report['status'], metrics=report.get('metrics'),
                         reproduction=report.get('reproduction'), reason=report.get('reason'),
                         seconds=report['seconds'])), flush=True)
    return 0


@torch.no_grad()
def figure3_extend_main(argv):
    """Fixed-budget Figure 3 extension reusing its original dense reference."""
    parser = argparse.ArgumentParser(description=figure3_extend_main.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--prepare', action='store_true')
    action.add_argument('--worker', choices=('dense', 'compressions'))
    parser.add_argument('--device', default='cuda:0')
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text())
    out, root = Path(config['output']), Path(config['reference_run'])
    if args.prepare:
        out.mkdir(parents=True, exist_ok=False)
        (out/'source.py').write_bytes(Path(__file__).read_bytes())
        save_json(out/'config.json', config)
        print(json.dumps(dict(event='figure3_extension_prepared', output=str(out))), flush=True)
        return 0
    if config != json.loads((out/'config.json').read_text()) or sha(Path(__file__).read_bytes()) != sha((out/'source.py').read_bytes()):
        raise ValueError('Run workers using the frozen source.py and unchanged prepared config')
    manifest = json.loads((root/'run.json').read_text())
    original = manifest['config']
    path = root/manifest['repetitions']['903']
    old = json.loads((path/'report.json').read_text())
    archive = (path/'trajectories.npz').read_bytes()
    if sha(archive) != old['trajectories_sha256']:
        raise ValueError('Original trajectory archive changed')
    with np.load(path/'trajectories.npz', allow_pickle=False) as saved:
        arrays = {key: saved[key] for key in (*old['data_sha256'], 'reference', 'extra_reference', 'times_reference')}
    if any(array_sha(arrays[key]) != value for key, value in old['data_sha256'].items()):
        raise ValueError('Original data changed')
    training = original['training']
    if (original['seeds'] != [903] or original['model'] != dict(width=4096, depth=2, activation='tanh')
            or training != dict(solver='euler', step=.00625, horizon=32, record_every=80, dtype='float32')
            or original['execution']['tf32'] or not old['runs']['reference']['complete']):
        raise ValueError('Unexpected Figure 3 reference protocol')
    folder = out/args.worker
    folder.mkdir(exist_ok=False)
    report = dict(worker=args.worker, config=config, complete=False, models={}, runs={}, metrics={}, errors={},
        source_sha256=sha(Path(__file__).read_bytes()), original_trajectories_sha256=sha(archive),
        reference_initial_state_sha256=old['reference_initial_state_sha256'], data_sha256=old['data_sha256'],
        training=training, command=sys.argv, cwd=str(Path.cwd()))
    started = time.monotonic()

    def persist():
        np.savez_compressed(folder/'trajectories.npz', **arrays)
        report.update(seconds=time.monotonic()-started,
                      trajectories_sha256=sha((folder/'trajectories.npz').read_bytes()))
        save_json(folder/'report.json', report)

    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device, dtype = torch.device(args.device), torch.float32
    report['environment'] = dict(python=platform.python_version(), torch=torch.__version__,
        device=str(device), hardware=torch.cuda.get_device_name(device), tf32=False, threads=1)
    inputs, labels, queries, extra = [torch.as_tensor(arrays[key], device=device) for key in
        ('train_inputs', 'train_labels', 'query_inputs', 'extra_query_inputs')]
    scored = torch.cat((inputs, queries, extra)).to(dtype)
    reference, extra_reference = arrays['reference'].astype(float), arrays['extra_reference'].astype(float)
    m, p = len(inputs), len(queries)
    dense = DeepDense(4096, inputs.shape[1], 2, 'tanh', 903, device)
    if [array_sha(v.cpu().numpy()) for v in dense.initial_state] != old['reference_initial_state_sha256']:
        raise ArithmeticError('Dense initialization differs from saved coupled reference')
    persist()

    def fit(name, family, construct, **metadata):
        try:
            t0 = time.monotonic()
            model = construct()
            synchronize(device)
            report['models'][name] = dict(family=family, moving=sum(v.numel() for v in model.initial_state),
                fixed=int(model.fixed_scalars), setup_seconds=time.monotonic()-t0,
                diagnostics=getattr(model, 'diagnostics', {}), **metadata)
            report['models'][name]['total'] = report['models'][name]['moving']+report['models'][name]['fixed']
            if report['models'][name]['setup_seconds'] > config['seconds_per_fit']:
                raise TimeoutError('Per-model setup cap exceeded')
            _experiment_move(model, device, dtype)
            state, prediction, run = integrate_euler(model, inputs.to(dtype), labels.to(dtype), scored,
                training['step'], config['seconds_per_fit'], horizon=training['horizon'],
                max_steps=5120, observation_every=training['record_every'])
            del model, state
            report['runs'][name] = run
            arrays[name], arrays['extra_'+name] = prediction[:, :m+p], prediction[:, m+p:]
            arrays['times_'+name] = np.asarray(run['times'])
            if (not run['complete'] or not np.isfinite(prediction).all()
                    or arrays[name].shape != reference.shape or arrays['extra_'+name].shape != extra_reference.shape
                    or not np.array_equal(arrays['times_'+name], arrays['times_reference'])):
                raise ArithmeticError('Incomplete/nonfinite or mismatched trajectory')
            rms = np.sqrt(np.mean((arrays[name].astype(float)[:, m:]-reference[:, m:])**2, axis=1))
            extra_rms = np.sqrt(np.mean((arrays['extra_'+name].astype(float)-extra_reference)**2, axis=1))
            report['metrics'][name] = dict(endpoint_rms=float(rms[-1]), worst_recorded_rms=float(rms.max()),
                extra_endpoint_rms=float(extra_rms[-1]), extra_worst_recorded_rms=float(extra_rms.max()))
        except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
            report['errors'][name] = f'{type(error).__name__}: {error}'
        persist()
        print(json.dumps(dict(event='figure3_extension', name=name, metrics=report['metrics'].get(name),
                             error=report['errors'].get(name))), flush=True)

    if args.worker == 'dense':
        for width in config['dense_widths']:
            for seed in config['dense_seeds']:
                init_seed = _experiment_seed(seed, f'dense_{width}')
                fit(f'dense_{width}_seed{seed}', 'dense',
                    lambda: DeepDense(width, inputs.shape[1], 2, 'tanh', init_seed, device),
                    width=width, seed=seed, initialization_seed=init_seed)
    else:
        for order in config['legendre_orders']:
            fit(f'legendre_{order}', 'legendre', lambda: LegendreCompression(dense, inputs, labels, order), order=order)
        for rank in config['low_rank_ranks']:
            init_seed = _experiment_seed(903, f'low_rank_{rank}')
            budget = 4096+min(rank, inputs.shape[1])*int(4096+inputs.shape[1])+8192*rank
            fit(f'low_rank_{rank}', 'low_rank', lambda: BudgetLoRA(dense, budget, init_seed),
                rank=rank, initialization_seed=init_seed)
        try:
            setup = _experiment_setup(original, 'logarithmic')
            sources, info = cubic_rollout_sources(dense, inputs, labels, queries, training['horizon'],
                seconds=config['seconds_per_fit'], seed=old['seeds']['logarithmic_source'],
                ranks=tuple(item['source_rank'] for item in config['logarithmic_budgets']), partitions=('new',),
                step=setup['rollout_step'], time_degree=setup['time_degree'],
                rollout_dtype=setup['rollout_dtype'], coefficient_dtype=setup['coefficient_dtype'])
            report['source'] = info
            for item in config['logarithmic_budgets']:
                width, rank = item['width'], item['source_rank']

                def construct():
                    model = DeepHarmonic(dense, inputs, labels, sources['new'][rank], width,
                        selection_seed=old['seeds']['logarithmic_selector'],
                        readout_floor=old['sources']['logarithmic']['readout_floor'],
                        selection_trials=setup['selection_trials'], condition_limit=setup['condition_limit'],
                        selection_strategy=setup['selection_strategy'])
                    if any(v['truncated'] for v in model.diagnostics['source_truncations']):
                        raise ArithmeticError('Extra constructor source truncation is forbidden')
                    return model

                fit(f'logarithmic_{width}_r{rank}', 'logarithmic', construct, width=width, source_rank=rank)
        except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
            report['errors']['logarithmic_setup'] = f'{type(error).__name__}: {error}'
    report['complete'] = not report['errors']
    report['finished'] = True
    persist()
    print(json.dumps(dict(event='figure3_extension_done', worker=args.worker,
                         seconds=report['seconds'], errors=report['errors'])), flush=True)
    return 0


def logarithmic_order_probe_main(argv):
    """Bounded source/selector repair against a saved coupled dense pair."""
    parser = argparse.ArgumentParser(description=logarithmic_order_probe_main.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--case', required=True)
    parser.add_argument('--device', default='cuda:0')
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text())
    request = config['cases'][args.case]
    if (not 1 <= len(request['widths']) <= 2 or len(set(request['widths'])) != len(request['widths'])
            or any(not isinstance(q, int) or q < 1 for q in request['widths'])
            or request['widths'] != sorted(request['widths'], reverse=True)
            or not isinstance(request['source_rank'], int) or request['source_rank'] < 1):
        raise ValueError('Expected one or two decreasing positive widths and a positive source rank')
    root = Path(config['reference_run'])
    manifest = json.loads((root/'run.json').read_text())
    original = manifest['config']
    seed, architecture, training = original['seeds'][0], original['model'], original['training']
    path = root/manifest['repetitions'][str(seed)]
    old = json.loads((path/'report.json').read_text())
    archive = (path/'trajectories.npz').read_bytes()
    if sha(archive) != old['trajectories_sha256']:
        raise ValueError('Saved dense-pair archive hash mismatch')
    dense_name = f"dense_{architecture['width']}"
    with np.load(path/'trajectories.npz', allow_pickle=False) as saved:
        arrays = {key: saved[key] for key in ('train_inputs', 'train_labels', 'query_inputs',
            'reference', 'times_reference', dense_name, 'times_'+dense_name)}
    for name in ('reference', dense_name):
        if not old['runs'][name]['complete'] or not np.array_equal(arrays['times_'+name], arrays['times_reference']):
            raise ValueError('Incomplete or mismatched dense pair')
    out = Path(config['output'])/args.case
    out.mkdir(parents=True, exist_ok=False)
    (out/'source.py').write_bytes(Path(__file__).read_bytes())
    save_json(out/'config.json', config)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = original['execution']['tf32']
    torch.backends.cudnn.allow_tf32 = original['execution']['tf32']
    device = torch.device(args.device)
    setup = _experiment_setup(original, 'logarithmic')
    setup.update(time_degree=config['time_degree'], selection_strategy=config['selection_strategy'])
    report = dict(case=args.case, request=request, config=config, source_sha256=sha(Path(__file__).read_bytes()),
        reference_run=str(root.resolve()), original_report_sha256=sha((path/'report.json').read_bytes()),
        original_trajectories_sha256=sha(archive), training=training, architecture=architecture,
        seeds={key: old['seeds'][key] for key in ('reference', 'logarithmic_source', 'logarithmic_selector')},
        setup=setup, candidates=[], status='inconclusive', command=sys.argv, cwd=str(Path.cwd()),
        environment=dict(python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
            device=str(device), hardware=torch.cuda.get_device_name(device), threads=1,
            tf32=original['execution']['tf32']),
        scope='Finite Euler pilot; full-horizon empirical rollout sources; declared query inputs only; '
              'pass requires worst-recorded test RMS AND sampled full-panel maximum ratios <=1; '
              'endpoint is diagnostic; no certified compiler or all-time claim')
    started = time.monotonic()

    def persist():
        np.savez_compressed(out/'trajectories.npz', **arrays)
        report.update(seconds=time.monotonic()-started,
                      trajectories_sha256=sha((out/'trajectories.npz').read_bytes()))
        save_json(out/'report.json', report)

    persist()
    try:
        inputs, labels, queries = [torch.as_tensor(arrays[key], device=device) for key in
                                  ('train_inputs', 'train_labels', 'query_inputs')]
        dense = DeepDense(architecture['width'], inputs.shape[1], architecture['depth'],
                          architecture['activation'], seed, device)
        hashes = [array_sha(v.cpu().numpy()) for v in dense.initial_state]
        if hashes != old['reference_initial_state_sha256']:
            raise ArithmeticError('Regenerated dense initialization differs')
        report['initial_state_sha256'] = hashes
        sources, info = cubic_rollout_sources(dense, inputs, labels, queries, training['horizon'],
            seconds=config['seconds_per_fit'], seed=old['seeds']['logarithmic_source'],
            ranks=(request['source_rank'],), partitions=('new',), step=setup['rollout_step'],
            time_degree=setup['time_degree'], rollout_dtype=setup['rollout_dtype'],
            coefficient_dtype=setup['coefficient_dtype'])
        source = sources['new'][request['source_rank']]
        report['source'] = info
        report['source_hashes'] = {key: [array_sha(v.cpu().numpy()) for v in values]
                                   for key, values in source.items()}
        reference = arrays['reference'].astype(float)
        dense_error = arrays[dense_name].astype(float)-reference
        m = len(labels)
        dense_rms = np.sqrt(np.mean(dense_error[:, m:]**2, axis=1))
        dense_max = float(np.abs(dense_error).max())
        if min(dense_rms[-1], dense_rms.max(), dense_max) <= 0:
            raise ArithmeticError('Zero dense-pair denominator')
        report['dense_pair'] = dict(endpoint_rms=float(dense_rms[-1]),
            worst_recorded_rms=float(dense_rms.max()), panel_max=dense_max)
        for q in request['widths']:
            result = dict(width=q, source_rank=request['source_rank'], status='inconclusive')
            report['candidates'].append(result)
            try:
                t0 = time.monotonic()
                model = DeepHarmonic(dense, inputs, labels, source, q,
                    selection_seed=old['seeds']['logarithmic_selector'],
                    readout_floor=old['sources']['logarithmic']['readout_floor'],
                    selection_trials=setup['selection_trials'], condition_limit=setup['condition_limit'],
                    selection_strategy=setup['selection_strategy'])
                if any(v['truncated'] for v in model.diagnostics['source_truncations']):
                    raise ArithmeticError('Extra constructor source truncation is not allowed')
                synchronize(device)
                result.update(learned=sum(v.numel() for v in model.initial_state), fixed=int(model.fixed_scalars),
                    assembly_seconds=time.monotonic()-t0, diagnostics=model.diagnostics)
                result['total'] = result['learned']+result['fixed']
                if result['assembly_seconds'] > config['seconds_per_fit']:
                    raise TimeoutError('Assembly exceeded the per-fit cap')
                dtype = getattr(torch, training['dtype'])
                _experiment_move(model, device, dtype)
                state, prediction, run = integrate_euler(model, inputs.to(dtype), labels.to(dtype),
                    torch.cat((inputs, queries)).to(dtype), training['step'], config['seconds_per_fit'],
                    horizon=training['horizon'], max_steps=math.ceil(training['horizon']/training['step']),
                    observation_every=training['record_every'])
                del model, state
                arrays[f'q{q}'], arrays[f'times_q{q}'] = prediction, np.asarray(run['times'])
                result['run'] = run
                if (not run['complete'] or not np.isfinite(prediction).all()
                        or prediction.shape != reference.shape
                        or not np.array_equal(arrays[f'times_q{q}'], arrays['times_reference'])):
                    raise ArithmeticError('Incomplete/nonfinite trajectory or mismatched observation grid')
                error = prediction.astype(float)-reference
                rms = np.sqrt(np.mean(error[:, m:]**2, axis=1))
                result['metrics'] = dict(endpoint_rms=float(rms[-1]), worst_recorded_rms=float(rms.max()),
                    endpoint_ratio=float(rms[-1]/dense_rms[-1]),
                    worst_recorded_ratio=float(rms.max()/dense_rms.max()),
                    panel_max=float(np.abs(error).max()), panel_max_ratio=float(np.abs(error).max()/dense_max))
                result['status'] = ('pass' if max(result['metrics']['worst_recorded_ratio'],
                                                 result['metrics']['panel_max_ratio']) <= 1 else 'fail')
            except (ValueError, RuntimeError, ArithmeticError, TimeoutError) as error:
                result['reason'] = f'{type(error).__name__}: {error}'
            persist()
            print(json.dumps(dict(event='logarithmic_probe', case=args.case, width=q, status=result['status'],
                metrics=result.get('metrics'), reason=result.get('reason'))), flush=True)
            if result['status'] != 'pass':
                break
        passing = [v for v in report['candidates'] if v['status'] == 'pass']
        report['selected'] = min(passing, key=lambda v: v['learned']) if passing else None
        report['status'] = 'pass' if passing else report['candidates'][-1]['status']
    except (ValueError, RuntimeError, ArithmeticError, TimeoutError, AssertionError) as error:
        report.update(status='inconclusive', reason=f'{type(error).__name__}: {error}')
    finally:
        persist()
    print(json.dumps(dict(event='logarithmic_probe_done', case=args.case, status=report['status'],
                         seconds=report['seconds'], reason=report.get('reason'))), flush=True)
    return 0


def budget_search_main(argv):
    """Reuse dense pairs and adaptively refine one-seed compression budgets."""
    import copy
    from concurrent.futures import ThreadPoolExecutor
    parser = argparse.ArgumentParser(description=budget_search_main.__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--worker-index', type=int)
    args = parser.parse_args(argv)
    plan = json.loads(args.plan.read_text())
    families = plan.get('families', ['legendre', 'harmonic', 'logarithmic'])
    if (not isinstance(families, list) or not families or len(set(families)) != len(families)
            or any(family not in ('legendre', 'harmonic', 'logarithmic') for family in families)):
        raise ValueError('families must be a nonempty unique list of compression families')
    if plan.get('rank_rule', 'legacy') not in ('legacy', 'interpolate_budgets', 'cap_at_source'):
        raise ValueError('Unknown source-rank proposal rule')
    for family, knots in plan.get('rank_knots', {}).items():
        if (plan.get('rank_rule') != 'interpolate_budgets' or family not in ('harmonic', 'logarithmic')
                or len(knots) < 2 or any(set(knot) != {'width', 'source_rank'}
                    or any(not isinstance(v, int) or isinstance(v, bool) or v < 1
                           for v in knot.values()) for knot in knots)
                or any(a['width'] >= b['width'] or a['source_rank'] > b['source_rank']
                       for a, b in zip(knots, knots[1:]))):
            raise ValueError('Rank knots must be increasing positive widths with nondecreasing positive ranks')
        expansion = plan.get('expansion', {}).get(family, {})
        if not knots[0]['width'] <= expansion.get('start', 0) <= expansion.get('maximum', 0) <= knots[-1]['width']:
            raise ValueError('Rank knots must cover the planned expansion interval')
    out = Path(plan['output']).resolve()
    if args.worker_index is not None:
        index = args.worker_index
        n = json.loads((Path(plan['runs'][index])/'config.json').read_text())['model']['width']
        return _budget_search_worker(out/f'n{n}', plan['devices'][index % len(plan['devices'])], plan)
    if not (0 < plan['width_tolerance'] < 1 and plan['factor'] > 0
            and 1 <= plan['max_new_per_family'] <= 8 and len(set(plan['runs'])) == len(plan['runs'])):
        raise ValueError('Invalid bounded refinement plan')
    if any(not isinstance(value, int) or isinstance(value, bool) or not 1 <= value <= 8
           for value in plan.get('max_new_by_width', {}).values()):
        raise ValueError('Per-width request caps must be integers from1 to8')
    fresh_harmonic = plan.get('restart_harmonic')
    if fresh_harmonic is not None:
        if (plan.get('harmonic_probes') or plan.get('source_max_ranks_by_width')
                or set(fresh_harmonic) != {'spatial_degree', 'time_degree', 'source_max_rank'}
                or any(not isinstance(value, int) or isinstance(value, bool) or value < 1
                       for value in fresh_harmonic.values())):
            raise ValueError('Fresh Harmonic setup must specify one positive common order/rank configuration')
    for family, expansion in plan.get('expansion', {}).items():
        if family not in ('legendre', 'harmonic', 'logarithmic') or not (
                1 <= expansion['start'] <= expansion['maximum']):
            raise ValueError('Invalid bounded doubling interval')
        if expansion.get('sequential', False) and (family != 'legendre' or expansion['start'] != 1):
            raise ValueError('Sequential scans are for Legendre integer orders starting at1')
    out.mkdir(parents=True, exist_ok=False)
    source_bytes = Path(__file__).read_bytes()
    source_hash = sha(source_bytes)
    (out/'source.py').write_bytes(source_bytes)
    save_json(out/'plan.json', plan)
    for index, old_root in enumerate(map(Path, plan['runs'])):
        previous = json.loads((old_root/'run.json').read_text())
        # Old saved runs may predate optional selector/panel/dataset fields.
        # Fill defaults without changing their explicitly recorded settings.
        config = _experiment_merge(EXPERIMENT_DEFAULTS, previous['config'])
        seed, n = config['seeds'][0], config['model']['width']
        old_path = old_root/previous['repetitions'][str(seed)]
        report = json.loads((old_path/'report.json').read_text())
        trajectory_bytes = (old_path/'trajectories.npz').read_bytes()
        if (sha(trajectory_bytes) != report['trajectories_sha256']
                or sha((old_root/'source.py').read_bytes()) != report['source_sha256']
                or not all(report['runs'].get(key, {}).get('complete') for key in ('reference', f'dense_{n}'))):
            raise ValueError('Missing or inconsistent original paired trajectories')
        replacement = plan.get('harmonic_probes', {}).get(str(n))
        if fresh_harmonic is not None:
            removed = [name for name, model in report['models'].items() if model['family'] == 'harmonic']
            for key in ('models', 'runs', 'errors', 'skipped'):
                report[key] = {name: value for name, value in report.get(key, {}).items()
                               if not name.startswith('harmonic_')}
            report.get('budget_search', {}).pop('harmonic', None)
            report.get('sources', {}).pop('harmonic', None)
            report.pop('harmonic_source_replacement', None)
            method = config['methods']['non_oblivious']['harmonic']
            method.update(spatial_degree=fresh_harmonic['spatial_degree'], budgets=[])
            method.setdefault('setup', {})['time_degree'] = fresh_harmonic['time_degree']
            report['harmonic_fresh_setup'] = dict(settings=fresh_harmonic,
                excluded_old_candidates=removed,
                scope='Fresh common source configuration; no inherited Harmonic accuracy or constructor brackets')
        if replacement is not None:
            # A changed spatial basis invalidates old width failures. Start this
            # family's bracket from the checked repaired witness, not old orders.
            probe_path = Path(replacement)
            probe = json.loads((probe_path/'report.json').read_text())
            probe_bytes = (probe_path/'trajectories.npz').read_bytes()
            probe_config = json.loads((probe_path/'config.json').read_text())
            if (Path(probe['reference_run']).resolve() != old_root.resolve()
                    or probe['original_report_sha256'] != sha((old_path/'report.json').read_bytes())
                    or probe['original_trajectories_sha256'] != sha(trajectory_bytes)
                    or probe['trajectories_sha256'] != sha(probe_bytes)
                    or probe['source_sha256'] != sha((probe_path/'source.py').read_bytes())
                    or probe['request'] != probe_config['cases'][probe['case']]
                    or probe['compact_width'] != probe_config['compact_width']
                    or probe['initial_state_sha256'] != report['reference_initial_state_sha256']
                    or probe['training'] != config['training'] or probe['architecture'] != config['model']
                    or probe['seeds'] != {key: report['seeds'][key] for key in
                                         ('reference', 'harmonic_source', 'harmonic_selector')}
                    or probe['status'] != 'pass' or not probe.get('run', {}).get('complete')):
                raise ValueError('Repaired Harmonic witness differs from its saved reference')
            with np.load(old_path/'trajectories.npz', allow_pickle=False) as saved:
                merged = {key: saved[key] for key in saved.files}
            with np.load(probe_path/'trajectories.npz', allow_pickle=False) as saved:
                for key in ('train_inputs', 'train_labels', 'query_inputs', 'reference',
                            'times_reference', f'dense_{n}'):
                    np.testing.assert_array_equal(merged[key], saved[key])
                np.testing.assert_array_equal(merged['times_reference'], saved['times'])
                prediction, times = saved['prediction'], saved['times']
            removed = [name for name, model in report['models'].items() if model['family'] == 'harmonic']
            for key in ('models', 'runs', 'errors', 'skipped'):
                report[key] = {name: value for name, value in report.get(key, {}).items()
                               if not name.startswith('harmonic_')}
            report.get('budget_search', {}).pop('harmonic', None)
            q, rank = probe['compact_width'], probe['request']['source_rank']
            name = f'harmonic_{q}_r{rank}'
            method = config['methods']['non_oblivious']['harmonic']
            method.update(spatial_degree=probe['request']['spatial_degree'],
                          budgets=[dict(width=q, source_rank=rank)])
            if _experiment_setup(config, 'harmonic')['time_degree'] != probe['request']['time_degree']:
                raise ValueError('Temporal setup replacement is not supported')
            info = copy.deepcopy(probe['source'])
            info['effective_setup'] = _experiment_setup(config, 'harmonic')
            report['sources']['harmonic'] = info
            model = copy.deepcopy(probe['model'])
            model.update(family='harmonic', moving=model.pop('learned'), width=q, source_rank=rank,
                         shared_source='harmonic')
            report['models'][name], report['runs'][name] = model, probe['run']
            merged[name], merged['times_'+name] = prediction, times
            report['harmonic_source_replacement'] = dict(probe=str(probe_path.resolve()),
                report_sha256=sha((probe_path/'report.json').read_bytes()), request=probe['request'],
                source_hashes=probe['source_hashes'],
                excluded_old_order_candidates=removed, old_archive_sha256=sha(trajectory_bytes),
                scope='Old spatial-order failures are excluded from the new local width bracket')
        target = out/f'n{n}'
        relative = f'seed_{seed}/attempt_001'
        path = target/relative
        path.mkdir(parents=True)
        config['execution']['output'] = str(target)
        config['execution']['devices'] = plan['devices'][index % len(plan['devices'])]
        contract = copy.deepcopy(config)
        contract.pop('plots')
        contract['methods']['oblivious']['frozen_features'].pop('plot')
        for key in ('output', 'reuse_completed'):
            contract['execution'].pop(key)
        contract['execution']['devices'] = [config['execution']['devices']]
        identity = dict(config=contract, source_sha256=source_hash,
            dataset_file_sha256=previous['identity']['dataset_file_sha256'], data_sha256=report['data_sha256'],
            python=platform.python_version(), torch=torch.__version__, numpy=np.__version__)
        fingerprint = sha(json.dumps(identity, sort_keys=True, allow_nan=False).encode())
        reused = dict(root=str(old_root.resolve()), source_sha256=report['source_sha256'],
            report_sha256=sha((old_path/'report.json').read_bytes()), trajectories_sha256=sha(trajectory_bytes),
            names=list(report['runs']), previous_seconds=report['seconds'])
        old_search = report.get('budget_search', {})
        inherited = {family: copy.deepcopy(old_search.get(family, {}).get('inherited_requested', [])
                     +old_search.get(family, {}).get('requested', []))
                     for family in ('legendre', 'harmonic', 'logarithmic')}
        report.update(source_sha256=source_hash, fingerprint=fingerprint, reused_from=reused,
            search_complete=False, budget_search={family: dict(requested=[], evaluations={}, bracket={},
                inherited_requested=inherited[family],
                factor=plan['factor'], width_tolerance=plan['width_tolerance'])
                for family in ('legendre', 'harmonic', 'logarithmic')})
        manifest = dict(config=config, identity=identity, fingerprint=fingerprint, source_sha256=source_hash,
            repetitions={str(seed): relative}, command=sys.argv, reused_from=reused, search_plan=plan)
        (target/'source.py').write_bytes(source_bytes)
        if replacement is None:
            (path/'trajectories.npz').write_bytes(trajectory_bytes)
        else:
            np.savez_compressed(path/'trajectories.npz', **merged)
            report['trajectories_sha256'] = sha((path/'trajectories.npz').read_bytes())
        save_json(target/'run.json', manifest)
        save_json(target/'config.json', config)
        save_json(path/'report.json', report)
    def worker(slot):
        codes = []
        for index in range(slot, len(plan['runs']), len(plan['devices'])):
            command = [sys.executable, '-B', '-u', str(out/'source.py'), 'refine-budgets',
                       '--plan', str(out/'plan.json'), '--worker-index', str(index)]
            with (out/f'worker_{index}.log').open('w') as log:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                for line in process.stdout:
                    log.write(line)
                    log.flush()
                    print(line, end='', flush=True)
                code = process.wait()
                codes.append(code)
                print(json.dumps(dict(event='refinement_width_done', index=index, exit_code=code)), flush=True)
        return codes
    with ThreadPoolExecutor(max_workers=len(plan['devices'])) as pool:
        results = list(pool.map(worker, range(len(plan['devices']))))
    return int(any(code != 0 for codes in results for code in codes))


def experiment_main(argv, action='run'):
    """Run or plot from defaults < JSON < generated CLI overrides."""
    import copy
    import fcntl
    from concurrent.futures import ThreadPoolExecutor
    config, args = _experiment_config(argv, validate_run=action != 'plot')
    if args.print_config:
        print(json.dumps(config, indent=2))
        return 0
    out = Path(config['execution']['output']).resolve()
    config['execution']['output'] = str(out)
    if action == 'plot':
        return experiment_plot(config)
    if args.worker_seed is not None:
        manifest = json.loads((out/'run.json').read_text())
        if sha(Path(__file__).read_bytes()) != manifest['source_sha256']:
            raise RuntimeError('Executable changed after launch; refusing mixed-source experiments')
        return _experiment_repetition(config, args.worker_seed, args.worker_device, args.worker_out, manifest)
    devices = config['execution']['devices']
    if devices == 'auto':
        devices = [f'cuda:{i}' for i in range(torch.cuda.device_count())] or ['cpu']
    elif isinstance(devices, str):
        devices = devices.split(',')
    if not devices or len(set(devices)) != len(devices):
        raise ValueError('execution.devices must name distinct devices')
    for name in devices:
        device = torch.device(name)
        if device.type not in ('cpu', 'cuda') or (device.type == 'cuda' and
                (not torch.cuda.is_available() or device.index is None or device.index >= torch.cuda.device_count())):
            raise ValueError(f'Unavailable or unsupported device: {name}')
    source_hash = sha(Path(__file__).read_bytes())
    contract = copy.deepcopy(config)
    contract.pop('plots')
    contract['methods']['oblivious']['frozen_features'].pop('plot')
    for key in ('output', 'reuse_completed'):
        contract['execution'].pop(key)
    contract['execution']['devices'] = devices
    file_hash = sha(Path(config['dataset']['file']).read_bytes()) if config['dataset']['name'] == 'npz' else None
    identity = dict(config=contract, source_sha256=source_hash, dataset_file_sha256=file_hash,
                    data_sha256={key: array_sha(value) for key, value in _experiment_data(config).items()},
                    python=platform.python_version(), torch=torch.__version__, numpy=np.__version__)
    fingerprint = sha(json.dumps(identity, sort_keys=True, allow_nan=False).encode())
    out.mkdir(parents=True, exist_ok=True)
    with (out/'.runner.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if (out/'run.json').exists():
            manifest = json.loads((out/'run.json').read_text())
            if not config['execution']['reuse_completed'] or manifest['fingerprint'] != fingerprint:
                raise ValueError('Output contains a different experiment or reuse is disabled; choose a fresh execution.output')
        else:
            if set(p.name for p in out.iterdir())-{'.runner.lock'}:
                raise ValueError('Output is not empty and has no matching run.json; choose a fresh directory')
            manifest = dict(fingerprint=fingerprint, config=config, source_sha256=source_hash,
                identity=identity, repetitions={}, command=sys.argv, cwd=str(Path.cwd()),
                seed_policy='listed seed initializes the reference; role-hashed independent seeds; source rebuilt per repetition')
            (out/'source.py').write_bytes(Path(__file__).read_bytes())
            save_json(out/'config.json', config)
        jobs = []
        for seed in config['seeds']:
            previous = manifest['repetitions'].get(str(seed))
            if previous:
                try:
                    report = json.loads((out/previous/'report.json').read_text())
                    reusable = (report['complete'] and report['seed'] == seed
                        and report['fingerprint'] == fingerprint and report['source_sha256'] == source_hash
                        and report['trajectories_sha256'] == sha((out/previous/'trajectories.npz').read_bytes()))
                except (OSError, ValueError, KeyError):
                    reusable = False
                if reusable:
                    print(json.dumps(dict(event='reused', seed=seed, path=previous)), flush=True)
                    continue
            parent = out/f'seed_{seed}'
            parent.mkdir(exist_ok=True)
            attempt = parent/f'attempt_{len(list(parent.iterdir()))+1:03d}'
            attempt.mkdir(exist_ok=False)
            manifest['repetitions'][str(seed)] = str(attempt.relative_to(out))
            jobs.append((seed, attempt))
        save_json(out/'run.json', manifest)

        def worker(device_name, assigned):
            results = []
            for seed, attempt in assigned:
                command = [sys.executable, '-B', '-u', str(Path(__file__).resolve()), 'run',
                    '--config', str(out/'config.json'), '--worker-seed', str(seed),
                    '--worker-device', device_name, '--worker-out', str(attempt)]
                with (attempt/'run.log').open('w') as log:
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                               text=True, env=dict(os.environ, OMP_NUM_THREADS='1'))
                    for line in process.stdout:
                        log.write(line)
                        log.flush()
                        print(line, end='', flush=True)
                    results.append(process.wait())
            return results

        with ThreadPoolExecutor(max_workers=len(devices)) as pool:
            results = list(pool.map(lambda item: worker(*item),
                          [(device, jobs[i::len(devices)]) for i, device in enumerate(devices)]))
        return int(any(code != 0 for codes in results for code in codes))


def appendix_saved_plot(argv):
    """Render appendix scope, fixed-budget ratios and costs from existing runs only."""
    import io
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    parser = argparse.ArgumentParser(description=appendix_saved_plot.__doc__)
    parser.add_argument('--manifest', type=Path,
                        default=ROOT/'studies/paper_figure_drafts_20261009/figures.json')
    parser.add_argument('--spectra', type=Path,
                        default=ROOT/'data/generated/paper_appendix_pilots_20261009/spectral_history')
    parser.add_argument('--additional-spectra', type=Path, nargs='*', default=[],
                        help='Additional completed or inconclusive single-width spectral output folders')
    parser.add_argument('--output', type=Path,
                        default=ROOT/'data/generated/paper_appendix_pilots_20261009/figures')
    args = parser.parse_args(argv)
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    manifest_path = args.manifest.resolve()
    manifest_bytes = manifest_path.read_bytes()
    plan = json.loads(manifest_bytes)
    plot_source_hash = sha(Path(__file__).read_bytes())
    styles = {'legendre': ('Legendre, q=4', '#2a78d6', 'o'),
              'harmonic': ('Harmonic, width 512', '#1b9970', 'D'),
              'logarithmic': ('Logarithmic, width 512', '#eb6834', 's')}
    records, scope, ratios, costs = [], [], [], []

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def curve(arrays, name, train_count):
        prediction = arrays[name].astype(float)
        reference = arrays['reference'].astype(float)
        require(prediction.shape == reference.shape and np.isfinite(prediction).all(),
                f'Invalid prediction: {name}')
        require(np.array_equal(arrays['times_'+name], arrays['times_reference']),
                f'Unequal time grids: {name}')
        return np.sqrt(np.mean((prediction[:, train_count:]-reference[:, train_count:])**2, axis=1))

    def summary(value):
        return dict(count=len(value), mean_absolute_error=float(np.mean(value)),
                    endpoint_rms=float(np.sqrt(np.mean(value**2))))

    for task in plan['tasks']:
        task_contract = None
        for raw_root in task['roots']:
            root = Path(raw_root).resolve()
            allowed = ROOT/'data/generated/paper_figure_drafts_20261009'
            require(root.is_relative_to(allowed), f'Out-of-scope raw root: {root}')
            run_bytes = (root/'run.json').read_bytes()
            run = json.loads(run_bytes)
            config = run['config']
            require(json.loads((root/'config.json').read_text()) == config,
                    f'Config mismatch: {root}')
            source_hash = sha((root/'source.py').read_bytes())
            require(source_hash == run['source_sha256'] == run['identity']['source_sha256'],
                    f'Source hash mismatch: {root}')
            require(sha(json.dumps(run['identity'], sort_keys=True, allow_nan=False).encode())
                    == run['fingerprint'], f'Identity mismatch: {root}')
            require(len(config['seeds']) == 1, f'Expected one saved seed: {root}')
            seed, width = config['seeds'][0], config['model']['width']
            path = (root/run['repetitions'][str(seed)]).resolve()
            require(path.is_relative_to(root) and path != root, f'Invalid repetition: {path}')
            report_bytes = (path/'report.json').read_bytes()
            report = json.loads(report_bytes)
            payload = (path/'trajectories.npz').read_bytes()
            require(report['complete'] and not report['errors'], f'Incomplete saved run: {path}')
            require(report['fingerprint'] == run['fingerprint'] and report['seed'] == seed
                    and report['source_sha256'] == source_hash
                    and sha(payload) == report['trajectories_sha256'], f'Raw identity mismatch: {path}')
            with np.load(io.BytesIO(payload), allow_pickle=False) as saved:
                arrays = {key: saved[key] for key in saved.files}
            require({key: array_sha(arrays[key]) for key in run['identity']['data_sha256']}
                    == report['data_sha256'] == run['identity']['data_sha256'], f'Data hash mismatch: {path}')
            contract = dict(dataset=config['dataset'], training=config['training'],
                            data_sha256=report['data_sha256'], source_sha256=source_hash,
                            model={key: value for key, value in config['model'].items() if key != 'width'})
            require(task_contract is None or contract == task_contract,
                    f'Within-task comparison changed: {root}')
            task_contract = contract
            times = arrays['times_reference']
            require(np.isfinite(arrays['reference']).all() and np.isfinite(times).all()
                    and times[0] == 0 and np.all(np.diff(times) > 0)
                    and times[-1] == config['training']['horizon'], f'Invalid reference grid: {path}')
            train_count = len(arrays['train_labels'])
            iid = f'dense_{width}'
            baseline = curve(arrays, iid, train_count)
            require(baseline[-1] > 0 and baseline.max() > 0, f'Zero comparator: {path}')
            selected = {'legendre': 'legendre_4'}
            for family in ('harmonic', 'logarithmic'):
                candidates = [name for name, model in report['models'].items()
                              if model['family'] == family and model['width'] == 512]
                if candidates:
                    require(len(candidates) == 1, f'Ambiguous fixed budget: {path}/{family}')
                    selected[family] = candidates[0]
            provenance = dict(task=task['name'], width=width, seed=seed,
                              independent_seed=report['seeds'][iid], raw_root=str(root),
                              run_path=str(root/'run.json'), run_sha256=sha(run_bytes),
                              report_path=str(path/'report.json'), report_sha256=sha(report_bytes),
                              trajectories_path=str(path/'trajectories.npz'), trajectories_sha256=sha(payload),
                              source_path=str(root/'source.py'), source_sha256=source_hash,
                              data_sha256=report['data_sha256'])
            records.append(provenance)
            for family, name in selected.items():
                require(report['runs'][name]['complete'], f'Incomplete model: {path}/{name}')
                error = curve(arrays, name, train_count)
                model = report['models'][name]
                ratios.append(dict(task=task['name'], width=width, name=name, family=family,
                                   learned_scalars=model['moving'], fixed_scalars=model['fixed'],
                                   endpoint_rms=float(error[-1]), worst_recorded_rms=float(error.max()),
                                   iid_endpoint_rms=float(baseline[-1]), iid_worst_recorded_rms=float(baseline.max()),
                                   endpoint_ratio=float(error[-1]/baseline[-1]),
                                   worst_recorded_ratio=float(error.max()/baseline.max())))
            if width != 4096:
                continue
            log_name = selected['logarithmic']
            declared = np.concatenate((arrays['train_inputs'], arrays['query_inputs'])).astype(float)
            extra = arrays['extra_query_inputs'].astype(float)
            require(np.isfinite(declared).all() and np.isfinite(extra).all()
                    and np.all(np.linalg.norm(declared, axis=1) > 0)
                    and np.all(np.linalg.norm(extra, axis=1) > 0), 'Invalid angular-distance inputs')
            require(not any(tuple(row) in {tuple(value) for value in declared} for row in extra),
                    'Undeclared inputs overlap the declared input set')
            unit_declared = declared/np.linalg.norm(declared, axis=1)[:, None]
            unit_extra = extra/np.linalg.norm(extra, axis=1)[:, None]
            distance = np.arccos(np.clip((unit_extra@unit_declared.T).max(axis=1), -1, 1))
            row = dict(task=task['name'], title=task['title'], width=width, model=log_name,
                       nearest_input_set='training inputs plus declared query inputs; labels unused in distance',
                       declared_input_count=len(declared), distance_radians=distance.tolist(), models={})
            for name, label in ((log_name, 'Logarithmic'), (iid, 'Independent dense')):
                declared_error = np.abs(arrays[name][-1, train_count:].astype(float)
                                        -arrays['reference'][-1, train_count:].astype(float))
                extra_error = np.abs(arrays['extra_'+name][-1].astype(float)
                                     -arrays['extra_reference'][-1].astype(float))
                require(extra_error.shape == distance.shape and np.isfinite(extra_error).all(),
                        f'Invalid extra-query predictions: {name}')
                correlation = (float(np.corrcoef(distance, extra_error)[0, 1])
                               if np.std(distance) > 0 and np.std(extra_error) > 0 else None)
                row['models'][name] = dict(label=label, declared_absolute_error=declared_error.tolist(),
                    extra_absolute_error=extra_error.tolist(), declared=summary(declared_error),
                    extra=summary(extra_error), extra_distance_error_pearson=correlation)
            scope.append(row)
            for name in ['reference', *selected.values()]:
                model, runtime = report['models'][name], report['runs'][name]
                source = report['sources'].get(model.get('shared_source'), {})
                setup = source.get('total_setup_seconds', source.get('seconds', 0.))
                require(runtime['dtype'] == 'torch.float32', f'Unexpected payload dtype: {name}')
                require(model['total'] == model['moving']+model['fixed'], f'Invalid counts: {name}')
                require(config['model']['depth'] == 2, 'Arithmetic table currently covers two hidden layers')
                m, d, n = train_count, config['dataset']['dimension'], width
                if model['family'] == 'reference':
                    leading_macs = 3*n*n*m+2*n*d*m
                    arithmetic_formula = '3 n^2 m + 2 n d m + O(n m)'
                elif model['family'] == 'legendre':
                    q = model['order']
                    leading_macs = 2*n*n*m+8*q*n*m*m+2*n*d*m
                    arithmetic_formula = '2 n^2 m + 8 q n m^2 + 2 n d m + O(q n m + n m)'
                else:
                    k = model['width']
                    leading_macs = 10*k*k*m+2*k*d*m+5*k*m*m+d*m*m
                    arithmetic_formula = '10 k^2 m + 2 k d m + 5 k m^2 + d m^2 + O(k^2 + k m + m^3)'
                costs.append(dict(task=task['name'], name=name, family=model['family'],
                    offline_shared_source_seconds=setup, construction_seconds=model['setup_seconds'],
                    training_update_seconds=runtime['training_seconds'],
                    query_seconds=runtime['query_seconds'], query_refresh_seconds=runtime['query_refresh_seconds'],
                    query_with_refresh_seconds=runtime['query_seconds']+runtime['query_refresh_seconds'],
                    training_loss_seconds=runtime['training_loss_seconds'], export_seconds=runtime['export_seconds'],
                    runtime_wall_seconds=runtime['seconds'], observations=len(times),
                    inputs_per_query_batch=len(declared)+len(extra),
                    learned_payload_bytes=4*model['moving'], fixed_payload_bytes=4*model['fixed'],
                    leading_training_rhs_macs=leading_macs,
                    training_rhs_arithmetic=arithmetic_formula,
                    arithmetic_parameters=dict(n=n, d=d, m=m, q=model.get('order'), k=model.get('width')),
                    arithmetic_convention='one multiply-accumulate is one MAC; analytic leading product counts, not profiling',
                    arithmetic_exclusions='pointwise activation/scaling, lower-order vector work, compact m-cubed solve, setup and query work',
                    payload_definition='recorded retained scalars times four bytes; nominal float32 payload',
                    process_peak_cuda_bytes=runtime['process_peak_cuda_bytes'], peak_scope=runtime['peak_scope'],
                    source_timing_scope=source.get('timing_scope', 'shared family source setup' if source else 'none'),
                    hardware=report['hardware'], device=report['device']))

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'axes.titlesize': 9,
                         'axes.spines.top': False, 'axes.spines.right': False, 'pdf.fonttype': 42})

    def save(fig, name):
        for suffix in ('png', 'pdf'):
            fig.savefig(destination/f'{name}.{suffix}', dpi=220, bbox_inches='tight')
        plt.close(fig)

    fig = plt.figure(figsize=(10, 3.5))
    outer = fig.add_gridspec(1, 2, wspace=.32)
    for index, row in enumerate(scope):
        grid = outer[index].subgridspec(1, 2, width_ratios=(1, 3), wspace=.09)
        strip = fig.add_subplot(grid[0])
        ax = fig.add_subplot(grid[1], sharey=strip)
        for j, (name, model) in enumerate(row['models'].items()):
            color, marker = ('#eb6834', 'o') if j == 0 else ('#666666', 'x')
            declared_error = np.asarray(model['declared_absolute_error'])
            strip.scatter(np.full(len(declared_error), j), declared_error, c=color,
                          marker=marker, s=14, alpha=.5)
            strip.scatter(j, declared_error.mean(), c=color, marker='_', s=210, linewidths=2)
            ax.scatter(row['distance_radians'], model['extra_absolute_error'], c=color,
                       marker=marker, s=21, alpha=.7, label=model['label'])
        strip.set_xticks([0, 1], ['Log.', 'Dense'], fontsize=7)
        strip.set_xlim(-.6, 1.6)
        strip.set_title('Declared\ndistance = 0', fontsize=8)
        strip.set_ylabel('Endpoint absolute prediction error')
        ax.set_title(row['title']+' · undeclared inputs')
        ax.set_xlabel('Nearest declared-input angle (radians)')
        ax.tick_params(labelleft=False)
        strip.set_ylim(bottom=0)
        ax.legend(frameon=False, fontsize=7, loc='upper left')
    fig.subplots_adjust(bottom=.19, top=.81)
    fig.suptitle('Logarithmic width 512, dense width 4096 · observational scope comparison', y=.99, fontsize=10)
    save(fig, 'appendix_query_distance')

    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))
    for ax, task in zip(axes, plan['tasks']):
        for family, (label, color, marker) in styles.items():
            rows = sorted((row for row in ratios if row['task'] == task['name'] and row['family'] == family),
                          key=lambda row: row['width'])
            if not rows:
                continue
            for field, linestyle in (('endpoint_ratio', '-'), ('worst_recorded_ratio', '--')):
                ax.plot([row['width'] for row in rows], [row[field] for row in rows],
                        linestyle, color=color, marker=marker, markersize=4, linewidth=1.2,
                        label=label if field == 'endpoint_ratio' else None)
        ax.axhline(1, color='#777777', linewidth=.8, linestyle=':')
        ax.set_xticks([1024, 2048, 4096])
        ax.set_yscale('log')
        ax.set_title(task['title'])
        ax.set_xlabel('Dense reference width')
        ax.set_ylabel('Prediction RMS / respective dense-pair RMS')
        ax.legend(frameon=False, fontsize=7)
    fig.legend(handles=[Line2D([0], [0], color='black', label='Endpoint'),
                        Line2D([0], [0], color='black', linestyle='--', label='Ratio of separate recorded maxima')],
               loc='lower center', ncol=2, frameon=False, fontsize=8)
    fig.tight_layout(rect=(0, .08, 1, 1))
    save(fig, 'appendix_fixed_budget_ratios')

    fig, axes = plt.subplots(2, 1, figsize=(12.5, 4.8))
    for index, task in enumerate(plan['tasks']):
        rows = [row for row in costs if row['task'] == task['name']]
        names = [('Dense' if row['family'] == 'reference' else styles[row['family']][0])
                 for row in rows]
        ax = axes[index]
        ax.axis('off')
        ax.set_title(task['title']+' · n=4096 · recorded runtime and retained payload', pad=2)
        cells = [[name, f"{row['offline_shared_source_seconds']:.2f}",
                  f"{row['construction_seconds']:.2f}", f"{row['training_update_seconds']:.2f}",
                  f"{row['query_with_refresh_seconds']:.2f}", f"{row['learned_payload_bytes']/2**20:.3f}",
                  f"{row['fixed_payload_bytes']/2**20:.3f}",
                  f"{row['leading_training_rhs_macs']/1e6:.2f}",
                  f"{row['process_peak_cuda_bytes']/2**20:.1f}"] for name, row in zip(names, rows)]
        table = ax.table(cellText=cells,
            colLabels=['Model', 'Source\ns', 'Build\ns', 'Updates\ns', 'Queries\ns',
                       'Learned\nMiB', 'Fixed\nMiB', 'Leading\nM MAC/RHS', 'Process peak\nGPU MiB'],
            colWidths=[.20, .085, .085, .09, .09, .10, .10, .12, .13], cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(7)
        table.scale(1, 1.8)
    fig.tight_layout()
    save(fig, 'appendix_recorded_costs')

    spectral_root = args.spectra.resolve()
    require(spectral_root.is_relative_to(ROOT/'data/generated/paper_appendix_pilots_20261009'),
            f'Out-of-scope spectral root: {spectral_root}')
    spectral_bytes = (spectral_root/'report.json').read_bytes()
    spectral_report = json.loads(spectral_bytes)
    require(spectral_report['complete'], 'Incomplete saved spectral measurements')
    spectral_rows, spectral_inconclusive = [], []
    worker_paths = [(spectral_root/f"n{case['width']}"/'report.json', case['result'])
                    for case in spectral_report['cases']]
    for additional in args.additional_spectra:
        additional = additional.resolve()
        require(additional.is_relative_to(ROOT/'data/generated/paper_appendix_pilots_20261009/feedback'),
                f'Out-of-scope additional spectral root: {additional}')
        worker_paths.append((additional/'report.json', None))
    observed_widths = set()
    for worker_path, expected in worker_paths:
        worker_bytes = worker_path.read_bytes()
        worker = json.loads(worker_bytes)
        width = worker['width']
        require(width not in observed_widths, f'Duplicate spectral width: {width}')
        observed_widths.add(width)
        require(expected is None or worker == expected, f'Spectral worker mismatch: {worker_path}')
        require(all(worker['config'][key] == value for key, value in spectral_report['config'].items()
                    if key not in ('widths', 'device')), f'Changed spectral protocol: {worker_path}')
        if expected is None:
            require(worker['config']['widths'] == [width], f'Incorrect worker width config: {worker_path}')
            require(sha((worker_path.parent/'source.py').read_bytes()) == worker['source_sha256'],
                    f'Spectral source snapshot mismatch: {worker_path}')
        if not worker['complete']:
            spectral_inconclusive.append(dict(width=width, report_path=str(worker_path),
                report_sha256=sha(worker_bytes), status='inconclusive',
                reason=worker.get('error', 'Worker did not complete within the bounded attempt; no retry')))
            continue
        history = worker['history_spectra'][0]
        singular = np.asarray(history['singular_values'], dtype=float)
        denominator = history['projected_history_frobenius']
        require(history['full_spectrum'] and not history['polynomial_fitting_used']
                and len(singular) == min(history['history_shape'])
                and np.isfinite(singular).all() and np.all(singular >= 0)
                and np.all(np.diff(singular) <= 0) and denominator > 0,
                f'Invalid full saved history spectrum: {worker_path}')
        tail = np.sqrt(np.r_[np.cumsum(singular[::-1]**2)[::-1], 0.])/denominator
        require(abs(tail[0]-1) < 1e-8, f'Spectral energy mismatch: {worker_path}')
        tolerance = .01*math.sqrt(512/width)
        ranks = {str(tol): int(np.flatnonzero(tail <= tol)[0]) for tol in (.01, .001)}
        require(ranks == history['required_rank'], f'Fixed-tolerance rank mismatch: {worker_path}')
        spectral_rows.append(dict(width=width, tolerance=tolerance,
            shrinking_tolerance_rank=int(np.flatnonzero(tail <= tolerance)[0]),
            fixed_tolerance_ranks=ranks, mandatory_span_rank=history['mandatory_span_rank'],
            normalized_singular_values=(singular/denominator).tolist(),
            original_history_rms=history['original_history_rms'],
            projected_history_rms=history['projected_history_rms'],
            report_path=str(worker_path), report_sha256=sha(worker_bytes),
            seconds=worker['seconds'],
            maximum_temporal_holdout_relative_rms=worker['maximum_temporal_holdout_relative_rms']))
    spectral_rows.sort(key=lambda row: row['width'])
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.6))
    colors = ['#2563eb', '#d97706', '#16856c', '#8b5bb7', '#c44848']
    for row, color in zip(spectral_rows, colors):
        singular = row['normalized_singular_values']
        axes[0].loglog(np.arange(1, len(singular)+1), singular, color=color,
                       linewidth=1.2, label=f"n={row['width']}")
    axes[0].set(xlabel='Singular-value index', ylabel=r'$\sigma_j/\|H_\perp\|_F$',
                title='Saved dense activation histories', ylim=(1e-10, 1.5))
    widths = [row['width'] for row in spectral_rows]
    for tol, marker, label in (('0.01', 'o', '1% tail'), ('0.001', 's', '0.1% tail')):
        axes[1].plot(widths, [row['fixed_tolerance_ranks'][tol] for row in spectral_rows],
                     marker=marker, label=label)
    axes[1].plot(widths, [row['shrinking_tolerance_rank'] for row in spectral_rows],
                 marker='^', linestyle='--', color='#ad3b70', label=r'$0.01\sqrt{512/n}$ tail')
    axes[1].set(xlabel='Dense width n', ylabel='Required history rank',
                title='Relative Frobenius-tail tolerance', xscale='log', xticks=widths)
    axes[1].set_xticklabels([str(width) for width in widths])
    for field, label, marker in (('original_history_rms', 'Before projection', 's'),
                                 ('projected_history_rms', 'After projection', 'o')):
        axes[2].plot(widths, [row[field] for row in spectral_rows], marker=marker, label=label)
    axes[2].set(xlabel='Dense width n', ylabel='History RMS', title='Measured history size',
                xscale='log', xticks=widths)
    axes[2].set_xticklabels([str(width) for width in widths])
    for ax in axes:
        ax.legend(frameon=False, fontsize=7)
        ax.grid(alpha=.15)
    fig.suptitle('Circle pilot · empirical history ranks · no prediction-error guarantee', fontsize=10)
    if spectral_inconclusive:
        fig.supxlabel('Inconclusive: '+', '.join(str(row['width']) for row in spectral_inconclusive), fontsize=8)
    fig.tight_layout()
    save(fig, 'appendix_response_history_spectra')

    captions = [
        'Scope. At dense width n=4096 and largest saved Logarithmic width 512 (source rank 37 on '
        'circle, 32 on digits), each point is |f_model(T,x)-f_dense(T,x)| at T=32. The extra-input '
        'angle is min_z arccos(<x,z>/(||x|| ||z||)), where z ranges over the 8 training and 30 '
        'declared query inputs supplied to setup. Query labels do not enter setup or distance. '
        'Declared queries have distance zero and appear separately; horizontal marks show their '
        'mean absolute error. Undeclared inputs are disjoint from that set. The independent dense '
        'comparison uses the same input and reference prediction. This is an observational '
        'comparison, not a causal distance experiment or evidence of a monotone distance effect. '
        'Pearson correlations in saved metrics are descriptive, without inferential claims.',
        'Fixed choices. At each dense width, E(T)/E_iid(T) uses endpoint query RMS, and '
        'max_t E(t)/max_t E_iid(t) uses separate maxima over the 65 saved observation times. '
        'Here E(t) is RMS over the 30 declared queries relative to the coupled dense reference; '
        'E_iid(t) compares that reference with one independent dense initialization. Fixed compact '
        'width 512 and source ranks (circle 37, digits 32) are retained; Legendre order q=4 is '
        'fixed while its learned-state count grows with dense width. The dotted level is ratio 1. '
        'Lines connect observations only: no exponent, limiting ratio, asymptotic vanishing '
        'or continuous-time maximum is estimated. Each width uses its saved reference seed.',
        'Costs. Tables show saved timings at n=4096 on NVIDIA RTX 3090: offline source setup, model '
        'construction, actual Euler training updates, and query work including readout refresh. '
        'Query totals cover 65 batches, each containing 8 training, 30 declared and 30 undeclared '
        'inputs. Training-loss checks and final host export are separate fields in metrics. '
        'Zero source time means no offline source stage. Each source setup was shared across '
        'three compact budgets; the displayed full setup is not an apportioned or isolated '
        'single-model benchmark. Logarithmic setup includes its disposable precursor and dense '
        'full-horizon rollout. Model construction excludes the shared source stage. Dense uses '
        'the reference run. Dense and compression update kernels differ; recorded timings do '
        'not establish optimized algorithmic speedups. Tables convert retained scalar counts to '
        'nominal float32 payload bytes (four per scalar; 1 MiB=2^20 bytes), separating learned '
        'and fixed storage. Common data, workspace and source temporaries are excluded from '
        'payload counts. CUDA peak is allocated memory of the whole process, including resident '
        'references; it is not isolated model peak memory.',
        'Arithmetic counts. One multiply-accumulate is one MAC. For two hidden layers, training '
        'batch m, input dimension d, dense width n, compact width k and Legendre order q, the '
        'leading product counts per training RHS evaluation are: Dense, 3 n^2 m+2 n d m+O(n m); '
        'Legendre, 2 n^2 m+8 q n m^2+2 n d m+O(q n m+n m); Harmonic and Logarithmic, '
        '10 k^2 m+2 k d m+5 k m^2+d m^2+O(k^2+k m+m^3). The table evaluates the displayed '
        'polynomial terms in millions of MACs (10^6), with m=8 and q=4. The compact counts '
        'include retained metric products and duplicated training-Gram products; the additional '
        'm-by-m readout solve is represented only by its O(m^3) order, without a guessed '
        'constant. Legendre moment transport uses cumulative sums. Pointwise activations, '
        'scalings, lower-order work, source setup and query evaluations are excluded. These '
        'analytic classical-arithmetic counts are not measured hardware FLOPs, wall-time '
        'predictions or a claim of optimized speedup; dtype and per-step overhead also matter.',
        'Response-history spectra. H_perp is the saved top-layer activation-history matrix at '
        '128 held-out times and 38 declared inputs after projecting out its mandatory initialized '
        'span. The displayed rank is the smallest r with sqrt(sum_{j>r} sigma_j^2)/||H_perp||_F '
        '<= epsilon. Fixed tolerances 0.01 and 0.001 are supplemented by epsilon(n)=c/sqrt(n), '
        'where c=0.01 sqrt(512) is fixed, so epsilon(512)=0.01. This reference scale is not '
        'fitted to dense-pair prediction errors. The mandatory span remains additional. These '
        'empirical reconstruction ranks provide no prediction-error guarantee or prediction of '
        'Figure 2: a stability/propagation bound is absent. The spectrum display clips values '
        'below 10^-10; every rank calculation uses all saved singular values. '
        'Full saved singular values are reused; '
        'the plot command runs no SVD or rollout. Completed measured widths are '
        +', '.join(str(row['width']) for row in spectral_rows)+'. '
        +('Inconclusive bounded attempts: '+', '.join(str(row['width']) for row in spectral_inconclusive)+'. '
          if spectral_inconclusive else '')+
        'Degree-8 coefficient interpolation is auxiliary: its held-out relative RMS is '
        '10^-7 to 10^-6; the original coefficient-spectrum artifacts remain preserved.',
        'The scope, ratio and cost tables reuse the six existing single-seed Figure 2–4 runs; '
        'history spectra reuse completed saved single-seed source measurements, including explicitly '
        'requested width extensions when supplied. This plot command performs no fitting, new '
        'training, seed selection, numerical refinement or theorem certification.']
    (destination/'appendix_saved_captions.txt').write_text('\n\n'.join(captions)+'\n')
    save_json(destination/'appendix_saved_metrics.json', dict(
        manifest_path=str(manifest_path), manifest_sha256=sha(manifest_bytes),
        plot_source_path=str(Path(__file__).resolve()), plot_source_sha256=plot_source_hash,
        provenance=records, scope=scope, fixed_budget_ratios=ratios, recorded_costs=costs,
        history_spectra=spectral_rows, spectral_inconclusive=spectral_inconclusive,
        additional_spectral_reports=[str(path) for path, expected in worker_paths if expected is None],
        spectral_report_path=str(spectral_root/'report.json'),
        spectral_report_sha256=sha(spectral_bytes), shrinking_tolerance_constant=.01*math.sqrt(512),
        arithmetic_counts_status='analytic leading matrix-product counts; excluded terms stated in caption',
        fitted_exponents=None, new_experiments=False,
        figures=['appendix_query_distance', 'appendix_fixed_budget_ratios', 'appendix_recorded_costs',
                 'appendix_response_history_spectra']))
    print(json.dumps(dict(output=str(destination), saved_runs=len(records),
                          figures=4, new_experiments=False)), flush=True)
    return 0


def appendix_sweep_plot(argv):
    """Summarize the fixed appendix sweep, including incomplete and infeasible cases."""
    import io
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description=appendix_sweep_plot.__doc__)
    parser.add_argument('--factor', type=float, default=1.)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'data/generated/paper_appendix_pilots_20261009/figures')
    args = parser.parse_args(argv)
    factor = args.factor
    if not math.isfinite(factor) or factor <= 0:
        raise ValueError('Passing factor must be finite and positive')
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    study = ROOT/'studies/paper_appendix_pilots_20261009'
    generated = ROOT/'data/generated/paper_appendix_pilots_20261009'
    cases = ['dimension_d2', 'dimension_d3', 'dimension_d10', 'dimension_d64', 'dimension_d784',
             'architecture_depth3', 'architecture_depth4', 'architecture_silu', 'architecture_m16',
             'panel_p8', 'panel_p60']
    records = {}

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    for case in cases:
        config_path = study/(case+'.json')
        config_bytes = config_path.read_bytes()
        requested = json.loads(config_bytes)
        root = (ROOT/requested['execution']['output']).resolve()
        require(root.is_relative_to(generated), f'Out-of-scope output: {root}')
        row = dict(case=case, config=requested, config_path=str(config_path),
                   config_sha256=sha(config_bytes), raw_root=str(root), candidates=[],
                   status='pending', dense_final_training_mse=None, iid_final_training_mse=None,
                   baseline=None, minimum_tested_passing={}, errors={}, omissions=[])
        records[case] = row
        for family in ('logarithmic', 'harmonic'):
            for budget in requested['methods']['non_oblivious'][family]['budgets']:
                row['candidates'].append(dict(family=family, **budget,
                    name=f"{family}_{budget['width']}_r{budget['source_rank']}", status='pending'))
        if case == 'dimension_d784':
            preflight_path = study/'dimension_d784_preflight.json'
            preflight_bytes = preflight_path.read_bytes()
            preflight = json.loads(preflight_bytes)
            row['preflight'] = dict(path=str(preflight_path), sha256=sha(preflight_bytes), **preflight)
            row['candidates'].extend(dict(family='logarithmic', **budget,
                name=f"logarithmic_{budget['width']}_r{budget['source_rank']}")
                for budget in preflight['budgets'])
        if not (root/'run.json').is_file():
            row['omissions'].append('Saved run manifest unavailable')
            continue
        run_bytes = (root/'run.json').read_bytes()
        run = json.loads(run_bytes)
        config = run['config']
        source_hash = sha((root/'source.py').read_bytes())
        require(source_hash == run['source_sha256'] == run['identity']['source_sha256'],
                f'Source hash mismatch: {root}')
        require(json.loads((root/'config.json').read_text()) == config, f'Resolved config mismatch: {root}')
        require(sha(json.dumps(run['identity'], sort_keys=True, allow_nan=False).encode())
                == run['fingerprint'], f'Run identity mismatch: {root}')
        for section in ('dataset', 'model', 'training', 'methods'):
            def matches_subset(expected, actual):
                return (all(key in actual and matches_subset(value, actual[key]) for key, value in expected.items())
                        if isinstance(expected, dict) else expected == actual)
            require(matches_subset(requested[section], config[section]), f'Frozen config mismatch: {root}/{section}')
        require(len(config['seeds']) == 1 and config['seeds'] == requested['seeds'], f'Seed mismatch: {root}')
        seed = config['seeds'][0]
        row['provenance'] = dict(run_path=str(root/'run.json'), run_sha256=sha(run_bytes),
                                 source_path=str(root/'source.py'), source_sha256=source_hash)
        repetition = run['repetitions'].get(str(seed))
        if repetition is None:
            row['omissions'].append('Saved repetition unavailable')
            continue
        path = (root/repetition).resolve()
        require(path.is_relative_to(root) and path != root, f'Invalid repetition path: {path}')
        if not (path/'report.json').is_file() or not (path/'trajectories.npz').is_file():
            row['omissions'].append('Saved report or trajectory unavailable')
            continue
        report_bytes = (path/'report.json').read_bytes()
        report = json.loads(report_bytes)
        payload = (path/'trajectories.npz').read_bytes()
        if sha(payload) != report.get('trajectories_sha256') and not report.get('complete'):
            row['omissions'].append('Run is writing its next snapshot; no inconsistent arrays used')
            continue
        require(sha(payload) == report['trajectories_sha256'], f'Trajectory hash mismatch: {path}')
        require(report['seed'] == seed and report['source_sha256'] == source_hash
                and report['fingerprint'] == run['fingerprint'], f'Report identity mismatch: {path}')
        with np.load(io.BytesIO(payload), allow_pickle=False) as saved:
            arrays = {key: saved[key] for key in saved.files}
        require({key: array_sha(arrays[key]) for key in run['identity']['data_sha256']}
                == run['identity']['data_sha256'] == report['data_sha256'], f'Data hash mismatch: {path}')
        row['provenance'].update(report_path=str(path/'report.json'), report_sha256=sha(report_bytes),
            trajectories_path=str(path/'trajectories.npz'), trajectories_sha256=sha(payload),
            data_sha256=report['data_sha256'])
        row.update(errors=report['errors'], source_diagnostics=report['sources'],
                   status='complete' if report['complete'] else 'incomplete', seed=seed)
        m, p, d = (config['dataset'][field] for field in ('train_samples', 'test_samples', 'dimension'))
        require(arrays['train_inputs'].shape == (m, d) and arrays['query_inputs'].shape == (p, d)
                and arrays['train_labels'].shape == (m,) and arrays['query_labels'].shape == (p,),
                f'Data shape mismatch: {path}')
        iid = 'dense_'+str(config['model']['width'])
        row['dense_final_training_mse'] = report['runs'].get('reference', {}).get('final_training_mse')
        row['iid_final_training_mse'] = report['runs'].get(iid, {}).get('final_training_mse')
        complete = [name for name, runtime in report['runs'].items() if runtime.get('complete')]
        for name in complete:
            times = arrays['times_'+name]
            require(np.isfinite(arrays[name]).all() and arrays[name].shape == (len(times), m+p)
                    and np.isfinite(times).all() and times[0] == 0 and np.all(np.diff(times) > 0)
                    and times[-1] == config['training']['horizon']
                    and np.array_equal(times, arrays['times_reference']), f'Invalid saved grid/shape: {path}/{name}')
        if not all(name in complete for name in ('reference', iid)):
            row['omissions'].append('Complete dense pair unavailable')
            for candidate in row['candidates']:
                if candidate['status'] != 'infeasible':
                    candidate.update(status='inconclusive', reason='Complete dense pair unavailable')
            continue
        reference = arrays['reference'][:, m:].astype(float)
        baseline = np.sqrt(np.mean((arrays[iid][:, m:].astype(float)-reference)**2, axis=1))
        require(baseline[-1] > 0 and baseline.max() > 0, f'Zero dense-pair denominator: {path}')
        row['baseline'] = dict(endpoint_rms=float(baseline[-1]), worst_recorded_rms=float(baseline.max()),
                               independent_seed=report['seeds'][iid], recorded_times=len(baseline))
        for candidate in row['candidates']:
            name, family = candidate['name'], candidate['family']
            if candidate['status'] == 'infeasible':
                continue
            reason = (report['errors'].get(name) or report['errors'].get(family+'_setup')
                      or report.get('skipped', {}).get(name))
            if name not in complete or reason:
                candidate.update(status='inconclusive' if reason or name in report['runs'] else 'pending',
                                 reason=reason or 'Complete model unavailable')
                continue
            model = report['models'][name]
            error = np.sqrt(np.mean((arrays[name][:, m:].astype(float)-reference)**2, axis=1))
            endpoint_ratio, worst_ratio = float(error[-1]/baseline[-1]), float(error.max()/baseline.max())
            candidate.update(status='pass' if max(endpoint_ratio, worst_ratio) <= factor else 'fail',
                endpoint_rms=float(error[-1]), worst_recorded_rms=float(error.max()),
                endpoint_ratio=endpoint_ratio, worst_recorded_ratio=worst_ratio,
                learned_scalars=model['moving'], fixed_scalars=model['fixed'], total_scalars=model['total'],
                final_training_mse=report['runs'][name]['final_training_mse'])
        for family in ('logarithmic', 'harmonic'):
            passed = [candidate for candidate in row['candidates']
                      if candidate['family'] == family and candidate['status'] == 'pass']
            if passed:
                selected = min(passed, key=lambda item: item['learned_scalars'])
                completed = [candidate for candidate in row['candidates']
                             if candidate['family'] == family and 'learned_scalars' in candidate]
                selected['crossing_status'] = ('left_censored' if selected['width'] ==
                    min(candidate['width'] for candidate in row['candidates'] if candidate['family'] == family)
                    else 'tested_bracket' if len(completed) == len([
                        candidate for candidate in row['candidates'] if candidate['family'] == family])
                    else 'smaller_budgets_unresolved')
                row['minimum_tested_passing'][family] = selected

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'axes.titlesize': 9,
                         'axes.spines.top': False, 'axes.spines.right': False, 'pdf.fonttype': 42})
    colors = dict(logarithmic='#eb6834', harmonic='#1b9970')

    def save(fig, name):
        for suffix in ('png', 'pdf'):
            fig.savefig(destination/f'{name}.{suffix}', dpi=220, bbox_inches='tight')
        plt.close(fig)

    def storage(ax, case_names, labels, families):
        for j, family in enumerate(families):
            values = [records[case]['minimum_tested_passing'].get(family, {}).get('learned_scalars', np.nan)
                      for case in case_names]
            offset = (j-.5)*.08 if len(families) > 1 else 0
            ax.plot(np.arange(len(labels))+offset, values, color=colors[family], marker='o' if j == 0 else 'D',
                    markersize=5, linewidth=1.3, label=family.capitalize()+' learned')
            totals = [records[case]['minimum_tested_passing'].get(family, {}).get('total_scalars', np.nan)
                      for case in case_names]
            ax.plot(np.arange(len(labels))+offset, totals, color=colors[family], linestyle='--',
                    marker='o' if j == 0 else 'D', markersize=3, linewidth=.9,
                    label=family.capitalize()+' total')
            for i, case in enumerate(case_names):
                candidates = [candidate for candidate in records[case]['candidates'] if candidate['family'] == family]
                if np.isfinite(values[i]):
                    if records[case]['minimum_tested_passing'][family]['crossing_status'] == 'left_censored':
                        ax.annotate('≤', (i+offset, values[i]), xytext=(-10, -2),
                                    textcoords='offset points', color=colors[family])
                    unresolved = [str(candidate['width']) for candidate in candidates
                                  if candidate['status'] in ('inconclusive', 'pending', 'infeasible')]
                    if unresolved:
                        ax.text(i, .08+j*.1, ','.join(unresolved)+': inconcl.', color=colors[family],
                                ha='center', fontsize=7, rotation=30, transform=ax.get_xaxis_transform())
                    continue
                if not candidates:
                    continue
                states = {candidate['status'] for candidate in candidates}
                label = ('infeasible' if states == {'infeasible'} else
                         'no pass' if states == {'fail'} else 'inconclusive' if 'inconclusive' in states else 'pending')
                ax.text(i, .08+j*.1, label, color=colors[family], ha='center', fontsize=7,
                        rotation=30 if len(labels) > 4 else 0, transform=ax.get_xaxis_transform())
        ax.set_xticks(np.arange(len(labels)), labels)
        ax.set_xlim(-.35, len(labels)-.65)
        ax.set_yscale('log')
        ax.set_ylabel('Retained scalars')

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.7))
    dimension_cases = ['dimension_d'+str(d) for d in (2, 3, 10, 64, 784)]
    storage(axes[0], dimension_cases, ['2', '3', '10', '64', '784'], ['logarithmic', 'harmonic'])
    axes[0].set_xlabel('Input dimension d')
    axes[0].set_title('Storage vs dimension')
    axes[0].text(.02, .97, 'Harmonic tested only at d=2,3', transform=axes[0].transAxes,
                 va='top', fontsize=7, color='#555555')
    architecture_cases = ['dimension_d2', 'architecture_depth3', 'architecture_depth4',
                          'architecture_silu', 'architecture_m16']
    ax = axes[1]
    for field, label, marker, offset in (('endpoint_ratio', 'Endpoint', 'o', -.07),
                                       ('worst_recorded_ratio', 'Max/max recorded', 's', .07)):
        values = []
        for case in architecture_cases:
            candidate = next((candidate for candidate in records[case]['candidates']
                              if candidate['family'] == 'logarithmic' and candidate['width'] == 512), {})
            values.append(candidate.get(field, np.nan))
        ax.plot(np.arange(5)+offset, values, linestyle='none', marker=marker, markersize=5,
                color='#eb6834' if field == 'endpoint_ratio' else '#2a78d6', label=label)
    for i, case in enumerate(architecture_cases):
        candidate = next((candidate for candidate in records[case]['candidates']
                          if candidate['family'] == 'logarithmic' and candidate['width'] == 512), {})
        if 'endpoint_ratio' not in candidate:
            label = candidate.get('status', 'pending')
            if label == 'inconclusive' and 'condition' in candidate.get('reason', ''):
                label += '\ncondition >16'
            ax.text(i, .08, label, transform=ax.get_xaxis_transform(),
                    ha='center', fontsize=7, color='#9b3636')
    ax.axhline(factor, color='#777777', linewidth=1, linestyle=':', label=f'Passing ceiling {factor:g}')
    ax.set_yscale('log')
    ax.set_xticks(range(5), ['Baseline\nL=2, tanh, m=8', 'L=3', 'L=4', 'SiLU', 'm=16'], fontsize=7)
    ax.set_xlim(-.5, 4.5)
    ax.set_ylabel('RMS / dense pair')
    ax.set_title('Architecture robustness')
    ax.legend(frameon=False, fontsize=7, loc='upper left')
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, fontsize=7, loc='lower center', ncol=4)
    fig.tight_layout(rect=(0, .07, 1, 1))
    save(fig, 'appendix_dimensions_architecture')

    fig, ax = plt.subplots(figsize=(5.7, 4.0))
    panel_cases = ['panel_p8', 'dimension_d2', 'panel_p60']
    for width, color, marker in ((256, '#9472b0', 'o'), (512, '#eb6834', 's')):
        for field, style in (('endpoint_ratio', '-'), ('worst_recorded_ratio', '--')):
            values = [next((candidate.get(field, np.nan) for candidate in records[case]['candidates']
                            if candidate['family'] == 'logarithmic' and candidate['width'] == width), np.nan)
                      for case in panel_cases]
            ax.plot([8, 30, 60], values, color=color, marker=marker, linestyle=style,
                    label=f"width {width}, "+('endpoint' if field == 'endpoint_ratio' else 'max/max'))
    ax.axhline(factor, color='#777777', linewidth=1, linestyle=':', label=f'Passing ceiling {factor:g}')
    ax.set_xlabel('Declared queries')
    ax.set_ylabel('Query RMS / respective dense-pair RMS')
    ax.set_xticks([8, 30, 60])
    ax.set_yscale('log')
    ax.set_title('Fixed compact budgets · circle pilot')
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, fontsize=7, loc='lower center', ncol=2)
    ax.grid(axis='y', alpha=.15)
    fig.tight_layout(rect=(0, .14, 1, 1))
    save(fig, 'appendix_panel_ratios')

    captions = [
        'Dimension and architecture. Every case uses dense width n=2048, dataset seed 47, '
        'reference seed 901 and one independent dense comparator, with T=32 and 65 recorded '
        'Euler times. Let E(t) be prediction RMS over the declared query inputs relative to '
        'the coupled dense reference, and E_iid(t) the corresponding independent dense-pair RMS. '
        f'A candidate passes only if E(T)<={factor:g} E_iid(T) AND max_t E(t)<={factor:g} max_t E_iid(t). '
        'The dimension panel reports the smallest tested passing learned scalar count among '
        'compact widths 256 and 512 with source ranks 15 and 37. Solid lines count learned '
        'scalars; dashed lines include fixed retained storage for the same selected model. '
        'A ≤ annotation means the smallest grid budget passed, so the crossing is left-censored. '
        'Absent passing points leave the crossing open. This is a tested upper bound on sufficient storage, '
        'not an optimized minimum. Harmonic is tested only at d=2,3. At d=784 both compact '
        'widths are constructor-infeasible because the mandatory first-layer input-weight span '
        'has rank 784; no zero storage or accuracy failure is imputed. Other absent results '
        'are marked pending or inconclusive; completed inaccuracies remain failures.',
        'Inputs lie on the unit sphere. For d=2 the unnormalized target is sin(3 theta)+0.5 cos(5 theta), '
        'theta=atan2(x_2,x_1). For d>=3 it is sqrt(d) x_1+d^(3/2) x_1 x_2 x_3. '
        'Targets are divided by their training-set RMS. Thus the high-dimensional targets use '
        'only three coordinates; this sweep does not demonstrate increasing intrinsic target '
        'complexity. The architecture panel changes one baseline setting (two tanh hidden '
        'layers, eight training points): hidden depth 3, hidden depth 4, SiLU, or 16 training '
        'points. All use Logarithmic width 512 and source rank 37. The two displayed ratios '
        'use their respective endpoint and maximum-recorded dense-pair denominators. A small '
        'prediction ratio does not imply successful training: dense and compact final training '
        'MSEs are retained in the accompanying metrics, with the horizon unchanged.',
        'Panel size. On the circle, only declared query count p changes between 8,30,60, with '
        'the p=30 dimension baseline reused. Training data, initialization and the two compact '
        'budget candidates are fixed. The equally spaced query grids change with p. Labels '
        'never enter source setup. Both fixed compact widths 256 and 512 are shown through '
        'endpoint ratios (solid) and ratios of separate recorded maxima (dashed), using each '
        'case\'s own query panel and dense comparator. No selected-storage plateau is interpreted '
        'as an intrinsic size law. These circle data are not a higher-dimensional panel stress '
        'test; that replacement remains unmeasured. Missing or failed candidates are retained '
        'in metrics; no adaptive budget or source-rank search is used.',
        'All results are single-seed finite-discretization pilots using offline dense source '
        'rollouts and empirical source truncations. They do not establish a dimension-free '
        'theorem, an initialization-only compiler, a limiting scaling law, or a continuous-time bound.']
    (destination/'appendix_sweep_captions.txt').write_text('\n\n'.join(captions)+'\n')
    save_json(destination/'appendix_sweep_metrics.json', dict(
        plot_source_path=str(Path(__file__).resolve()), plot_source_sha256=sha(Path(__file__).read_bytes()),
        factor=factor, cases=records, fitted_exponents=None,
        dense_final_training_mse={case: row['dense_final_training_mse'] for case, row in records.items()},
        figures=['appendix_dimensions_architecture', 'appendix_panel_ratios']))
    print(json.dumps(dict(output=str(destination), cases=len(records),
                          complete=sum(row['status'] == 'complete' for row in records.values()))), flush=True)
    return 0


def paper_draft_plot(argv):
    """Render the three bounded paper drafts from hash-checked saved runs only."""
    import copy
    import io
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description=paper_draft_plot.__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    args = parser.parse_args(argv)
    manifest_path = args.manifest.resolve()
    manifest_bytes = manifest_path.read_bytes()
    plan = json.loads(manifest_bytes)
    factor = float(plan.get('factor', 1))
    if not math.isfinite(factor) or factor <= 0 or len(plan['tasks']) != 2:
        raise ValueError('Draft figures require two tasks and a finite positive factor')
    destination = Path(plan['output']).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    families = dict(legendre=('Legendre', '#2a78d6', 'o'),
                    harmonic=('Harmonic', '#1b9970', 'D'),
                    logarithmic=('Logarithmic', '#eb6834', 's'))
    control_styles = dict(dense=('Small dense', '#6e6e68', '^'),
                          low_rank=('Low rank', '#9274a5', 'v'),
                          frozen_features=('Frozen features', '#768da4', '*'))
    data_keys = ('train_inputs', 'train_labels', 'query_inputs', 'query_labels')
    tasks, curves = [], {}

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def expected_models(config):
        oblivious = config['methods']['oblivious']
        expected = {'reference': 'reference'}
        for family, field, prefix in (('dense', 'widths', 'dense'),
                                     ('legendre', 'orders', 'legendre'),
                                     ('low_rank', 'ranks', 'low_rank')):
            expected.update({f'{prefix}_{value}': family for value in oblivious[family][field]})
        if oblivious['frozen_features']['enabled']:
            expected['frozen_features'] = 'frozen_features'
        for family in families:
            if family != 'legendre':
                expected.update({f"{family}_{v['width']}_r{v['source_rank']}": family
                                 for v in config['methods']['non_oblivious'][family]['budgets']})
        return expected

    for task in plan['tasks']:
        result = dict(name=task['name'], title=task['title'], fixed_width=task['fixed_width'],
                      records=[], omissions=[])
        tasks.append(result)
        roots = [Path(value).resolve() for value in task['roots']]
        require(len(roots) == len(set(roots)), f"Duplicate roots: {task['name']}")
        contract, widths = None, set()
        for root in roots:
            if not (root/'run.json').is_file():
                result['omissions'].append(dict(root=str(root), reason='Run manifest not yet available'))
                continue
            run_bytes = (root/'run.json').read_bytes()
            manifest = json.loads(run_bytes)
            config, identity = manifest['config'], manifest['identity']
            require(json.loads((root/'config.json').read_text()) == config, f'Config mismatch: {root}')
            source_hash = sha((root/'source.py').read_bytes())
            require(source_hash == manifest['source_sha256'] == identity['source_sha256'],
                    f'Source hash mismatch: {root}')
            require(sha(json.dumps(identity, sort_keys=True, allow_nan=False).encode())
                    == manifest['fingerprint'], f'Identity fingerprint mismatch: {root}')
            identity_config = copy.deepcopy(config)
            identity_config.pop('plots', None)
            identity_config['methods']['oblivious']['frozen_features'].pop('plot', None)
            for key in ('output', 'reuse_completed'):
                identity_config['execution'].pop(key, None)
            devices = identity_config['execution']['devices']
            if devices != 'auto':
                require((devices.split(',') if isinstance(devices, str) else devices)
                        == identity['config']['execution']['devices'], f'Device mismatch: {root}')
            identity_config['execution']['devices'] = identity['config']['execution']['devices']
            require(identity_config == identity['config'], f'Config/identity mismatch: {root}')
            current = dict(dataset=config['dataset'], training=config['training'],
                           model={k: v for k, v in config['model'].items() if k != 'width'},
                           data_sha256=identity['data_sha256'], source_sha256=source_hash,
                           tf32=config['execution']['tf32'])
            require(contract is None or contract == current, f'Within-task comparison mismatch: {root}')
            contract = current
            n, seeds = config['model']['width'], config['seeds']
            require(isinstance(n, int) and n > 0 and n not in widths and len(seeds) == 1,
                    f'One unique width and one seed per root required: {root}')
            widths.add(n)
            seed, iid_name = seeds[0], f'dense_{n}'
            expected = expected_models(config)
            require(iid_name in expected, f'Missing independent width-{n} dense request: {root}')
            row = dict(width=n, seed=seed, root=str(root), models=[], selected={}, omissions=[],
                       requested_families=[family for family in families if family in expected.values()],
                       dense_learned=(config['model']['depth']-1)*n*n+n*(config['dataset']['dimension']+1),
                       dense_pair=None, provenance=dict(run_sha256=sha(run_bytes),
                           source_sha256=source_hash, fingerprint=manifest['fingerprint']))
            result['records'].append(row)
            relative = manifest['repetitions'].get(str(seed))
            if relative is None:
                row['omissions'].append('No saved repetition yet')
                continue
            path = (root/relative).resolve()
            require(path != root and path.is_relative_to(root), f'Invalid repetition path: {root}')
            if not all((path/file).is_file() for file in ('report.json', 'trajectories.npz')):
                row['omissions'].append('Report or trajectories not yet available')
                continue
            report_bytes = (path/'report.json').read_bytes()
            report = json.loads(report_bytes)
            trajectory_bytes = (path/'trajectories.npz').read_bytes()
            require(report['seed'] == seed and report['seeds']['reference'] == seed
                    and report['fingerprint'] == manifest['fingerprint']
                    and report['source_sha256'] == source_hash, f'Run identity mismatch: {path}')
            require(sha(trajectory_bytes) == report['trajectories_sha256'], f'Trajectory hash mismatch: {path}')
            row['provenance'].update(repetition=str(path), report_sha256=sha(report_bytes),
                                    trajectories_sha256=sha(trajectory_bytes))
            row.update(errors=report.get('errors', {}), skipped=report.get('skipped', {}),
                       sources=report.get('sources', {}), report_complete=report.get('complete', False))
            with np.load(io.BytesIO(trajectory_bytes), allow_pickle=False) as saved:
                arrays = {key: saved[key] for key in saved.files}

            def array(name, ndim):
                require(name in arrays, f'Missing array {name}: {path}')
                value = arrays[name]
                require(value.ndim == ndim and value.dtype.kind in 'fiu' and np.isfinite(value).all(),
                        f'Invalid array {name}: {path}')
                return value.astype(float)

            train, labels = array('train_inputs', 2), array('train_labels', 1)
            query, truth = array('query_inputs', 2), array('query_labels', 1)
            require(len(train) == len(labels) == config['dataset']['train_samples']
                    and len(query) == len(truth) == config['dataset']['test_samples']
                    and train.shape[1] == query.shape[1] == config['dataset']['dimension'],
                    f'Data shape mismatch: {path}')
            hash_keys = set(identity['data_sha256'])
            require(set(data_keys).issubset(hash_keys)
                    and hash_keys.issubset(set(data_keys) | {'extra_query_inputs', 'extra_query_labels'}),
                    f'Unexpected dataset hash keys: {path}')
            require({key: array_sha(arrays[key]) for key in hash_keys}
                    == report['data_sha256'] == identity['data_sha256'], f'Data hash mismatch: {path}')
            extra_count = 0
            if 'extra_query_inputs' in arrays or 'extra_query_labels' in arrays:
                extra, extra_labels = array('extra_query_inputs', 2), array('extra_query_labels', 1)
                require(len(extra) == len(extra_labels) > 0 and extra.shape[1] == train.shape[1],
                        f'Extra-query shape mismatch: {path}')
                declared = {tuple(value) for value in np.concatenate((train, query))}
                require(not any(tuple(value) in declared for value in extra),
                        f'Extra queries overlap training or declared-query inputs: {path}')
                extra_count = len(extra)
                extra_hashes = {key: array_sha(arrays[key])
                                for key in ('extra_query_inputs', 'extra_query_labels')}
                require('extra_data_sha256' not in report or report['extra_data_sha256'] == extra_hashes,
                        f'Extra-query hash mismatch: {path}')
                row['extra_query'] = dict(count=extra_count, data_sha256=extra_hashes,
                                         disjoint_from_training_and_declared_queries=True)
            for name, model in report['models'].items():
                require(name not in expected or model['family'] == expected[name],
                        f'Model family mismatch: {path}/{name}')
                expected[name] = model['family']
            checked, extra_checked = {}, {}
            for name, family in expected.items():
                model = report['models'].get(name)
                point = dict(name=name, family=family, status='unavailable', model=model)
                row['models'].append(point)
                reason = (report.get('errors', {}).get(name) or report.get('errors', {}).get(family+'_setup')
                          or report.get('skipped', {}).get(name))
                if model is None or not report['runs'].get(name, {}).get('complete') or reason:
                    point['reason'] = reason or 'Not complete or not yet run'
                    row['omissions'].append(f"{name}: {point['reason']}")
                    continue
                require(all(isinstance(model.get(k), int) and not isinstance(model[k], bool)
                            and model[k] >= 0 for k in ('moving', 'fixed', 'total'))
                        and model['moving'] > 0 and model['total'] == model['moving']+model['fixed'],
                        f'Invalid storage counts: {path}/{name}')
                point.update({key: model[key] for key in ('moving', 'fixed', 'total')})
                if name in ('reference', iid_name):
                    require(model['moving'] == row['dense_learned'] and model['fixed'] == 0,
                            f'Dense storage mismatch: {path}/{name}')
                prediction, times = array(name, 2), array('times_'+name, 1)
                run = report['runs'][name]
                run_times, losses = np.asarray(run['times']), np.asarray(run['losses'])
                require(len(times) > 1 and times[0] == 0 and np.all(np.diff(times) > 0)
                        and np.isclose(times[-1], config['training']['horizon'], atol=1e-10, rtol=0)
                        and prediction.shape == (len(times), len(train)+len(query))
                        and run_times.shape == times.shape and np.allclose(run_times, times, atol=1e-10, rtol=0)
                        and losses.shape == times.shape and np.isfinite(losses).all()
                        and np.allclose(np.mean((prediction[:, :len(train)]-labels)**2, axis=1),
                                        losses, atol=1e-6, rtol=2e-5), f'Trajectory/time/loss mismatch: {path}/{name}')
                checked[name] = (prediction[:, len(train):], times)
                point.update(status='complete', test_truth_mse=float(np.mean((prediction[-1, len(train):]-truth)**2)))
                if 'extra_'+name in arrays:
                    extra_prediction = array('extra_'+name, 2)
                    require(extra_count > 0 and extra_prediction.shape == (len(times), extra_count),
                            f'Extra prediction shape mismatch: {path}/{name}')
                    if 'times_extra_'+name in arrays:
                        extra_times = array('times_extra_'+name, 1)
                        require(extra_times.shape == times.shape and np.allclose(extra_times, times, atol=1e-10, rtol=0),
                                f'Extra time grid mismatch: {path}/{name}')
                    extra_checked[name] = extra_prediction
            if 'reference' not in checked:
                row['omissions'].append('No complete reference; all RMS comparisons unavailable')
                continue
            reference, times = checked['reference']
            width_curves, extra_curves = {}, {}
            for name, (prediction, model_times) in checked.items():
                require(model_times.shape == times.shape and np.allclose(model_times, times, atol=1e-10, rtol=0),
                        f'Paired time grids differ: {path}/{name}')
                width_curves[name] = np.sqrt(np.mean((prediction-reference)**2, axis=1))
                if name in extra_checked and 'reference' in extra_checked:
                    extra_curves[name] = np.sqrt(np.mean((extra_checked[name]-extra_checked['reference'])**2, axis=1))
            curves[(task['name'], n)] = (times, width_curves, extra_curves)
            if iid_name in width_curves:
                require(report['seeds'].get(iid_name) == _experiment_seed(seed, iid_name)
                        and report['seeds'][iid_name] != seed, f'Independent dense seed mismatch: {path}')
                baseline = width_curves[iid_name]
                row['dense_pair'] = dict(name=iid_name, endpoint_rms=float(baseline[-1]),
                                        worst_recorded_rms=float(baseline.max()),
                                        reference_seed=seed, independent_seed=report['seeds'][iid_name])
            else:
                row['omissions'].append('Independent dense run unavailable; passing budgets cannot be selected')
            for point in row['models']:
                name = point['name']
                if name not in width_curves:
                    continue
                curve = width_curves[name]
                point.update(endpoint_rms=float(curve[-1]), worst_recorded_rms=float(curve.max()))
                if name in extra_curves:
                    point.update(extra_endpoint_rms=float(extra_curves[name][-1]),
                                 extra_worst_recorded_rms=float(extra_curves[name].max()))
                if point['family'] in families and row['dense_pair']:
                    passed = curve[-1] <= factor*baseline[-1] and curve.max() <= factor*baseline.max()
                    point.update(status='pass' if passed else 'fail',
                                 endpoint_threshold=float(factor*baseline[-1]),
                                 worst_recorded_threshold=float(factor*baseline.max()))
            for family in families:
                if family not in row['requested_families']:
                    continue
                candidates = sorted((v for v in row['models'] if v['family'] == family),
                                    key=lambda v: (v.get('moving', math.inf), v['name']))
                passing = [v for v in row['models'] if v['family'] == family and v['status'] == 'pass']
                row.setdefault('tested_crossings', {})
                if passing:
                    chosen = min(passing, key=lambda v: (v['moving'], v['total'], v['name']))
                    row['selected'][family] = chosen['name']
                    below = [v for v in candidates if v.get('moving', math.inf) < chosen['moving']]
                    row['tested_crossings'][family] = dict(
                        status=('incomplete_grid' if any(v['status'] == 'unavailable' for v in candidates)
                                else 'left_censored' if not below else 'tested_bracket'),
                        passing_name=chosen['name'], passing_learned=chosen['moving'],
                        passing_total=chosen['total'],
                        smaller_tested=[dict(name=v['name'], status=v['status'], moving=v.get('moving')) for v in below],
                        interpolation=None,
                        interpretation='smallest tested passing budget; untested smaller budgets unresolved')
                else:
                    row['tested_crossings'][family] = dict(status='no_tested_pass', interpolation=None,
                        largest_completed_learned=max((v['moving'] for v in candidates if 'endpoint_rms' in v), default=None))
                    row['omissions'].append(f'{family}: no tested complete budget passes both criteria')
            if not extra_curves:
                row['omissions'].append('No paired undeclared-query predictions available')
        result['records'].sort(key=lambda row: row['width'])
        result['comparison_contract'] = contract

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'axes.titlesize': 9,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.linewidth': .6, 'pdf.fonttype': 42, 'savefig.facecolor': 'white'})

    def panels(ylabel, storage=False):
        fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.85), squeeze=False)
        for ax, task in zip(axes[0], tasks):
            ax.set_title(task['title'])
            ax.set_ylabel(ylabel)
            ax.set_yscale('log')
            ax.tick_params(labelsize=7)
            if storage:
                ax.set_xscale('log')
        return fig, axes[0]

    def save(fig, name):
        entries = {}
        for ax in fig.axes:
            handles, labels = ax.get_legend_handles_labels()
            entries.update(zip(labels, handles))
        if entries:
            fig.legend(list(entries.values()), list(entries), loc='lower center', ncol=4,
                       fontsize=6.5, frameon=False, handlelength=2.1, columnspacing=1.3)
        legend_rows = math.ceil(len(entries)/4)
        fig.tight_layout(pad=.6, w_pad=1.7, rect=(0, .065*legend_rows, 1, 1))
        for suffix in ('png', 'pdf'):
            fig.savefig(destination/f'{name}.{suffix}', dpi=240)
        plt.close(fig)

    def scored(row, family):
        return sorted((v for v in row['models'] if v['family'] == family and 'endpoint_rms' in v),
                      key=lambda v: (v['moving'], v['name']))

    def fixed(task):
        return next((row for row in task['records'] if row['width'] == task['fixed_width']), None)

    def empty(ax, message):
        ax.text(.5, .5, message, ha='center', va='center', transform=ax.transAxes, color='#777777')

    fig, axes = plt.subplots(2, 2, figsize=(7.8, 5.3), squeeze=False)
    for column, task in enumerate(tasks):
        rows = task['records']
        ns = [row['width'] for row in rows]
        for index, (field, ylabel) in enumerate((('moving', 'Learned scalars'), ('total', 'Total retained scalars'))):
            ax = axes[index, column]
            ax.set_title(task['title'] if index == 0 else '')
            ax.set_xlabel('Dense reference width')
            ax.set_ylabel(ylabel)
            ax.set_xscale('log')
            ax.set_yscale('log')
            if not rows:
                empty(ax, 'Runs not yet available')
                continue
            ax.plot(ns, [row['dense_learned'] for row in rows], ':', color='#777777',
                    label=r'Dense formula: $(L-1)n^2+n(d+1)$')
            missing = []
            for family, (label, color, marker) in families.items():
                if not any(family in row['requested_families'] for row in rows):
                    continue
                selected = [(row, next(v for v in row['models'] if v['name'] == row['selected'][family]))
                            for row in rows if family in row['selected']]
                shift = {'legendre': 1., 'harmonic': .985, 'logarithmic': 1.015}[family]
                ax.plot([row['width']*shift for row, _ in selected], [v[field] for _, v in selected],
                        color=color, marker=marker, markersize=4, linewidth=1.1, label=label)
                for row, value in selected:
                    if row['tested_crossings'][family]['status'] == 'left_censored':
                        ax.annotate('≤', (row['width']*shift, value[field]), xytext=(-9, -2),
                                    textcoords='offset points', fontsize=8, color=color)
                omitted = [str(row['width']) for row in rows
                           if family in row['requested_families'] and family not in row['selected']]
                if omitted:
                    missing.append(f"{label}: {', '.join(omitted)}")
            ax.set_xticks(ns, labels=[str(n) for n in ns])
            ax.minorticks_off()
            if missing:
                ax.text(.02, .96, 'No tested pass: '+'; '.join(missing),
                        transform=ax.transAxes, fontsize=6, color='#666666', va='top', wrap=True)
    save(fig, 'figure2_storage')

    fig, axes = plt.subplots(2, 2, figsize=(7.8, 5.5), squeeze=False)
    for ax, task, storage_field in ((axes[i, j], task, field)
                                   for i, field in enumerate(('moving', 'total'))
                                   for j, task in enumerate(tasks)):
        row = fixed(task)
        ax.set_xlabel('Learned scalars' if storage_field == 'moving' else 'Total retained scalars')
        ax.set_ylabel('Endpoint query RMS')
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_title(f"{task['title']}  ·  $n={task['fixed_width']}$")
        if row is None or (task['name'], row['width']) not in curves:
            empty(ax, 'Fixed-width reference not yet available')
            continue
        for family, (label, color, marker) in {**families, **control_styles}.items():
            values = [v for v in scored(row, family) if v['name'] != f"dense_{row['width']}" and v['endpoint_rms'] > 0]
            if values and family == 'frozen_features':
                ax.axhline(values[0]['endpoint_rms'], color=color, linewidth=1.1, linestyle='--', label=label)
                ax.plot(values[0][storage_field], values[0]['endpoint_rms'], marker=marker,
                        color=color, markersize=4, linestyle='none')
            elif values:
                ax.plot([v[storage_field] for v in values], [v['endpoint_rms'] for v in values],
                        color=color, marker=marker, markersize=4, linewidth=1.25,
                        linestyle='--' if family == 'frozen_features' else '-', label=label)
            if family == 'logarithmic':
                extra = [v for v in values if v.get('extra_endpoint_rms', 0) > 0]
                if extra:
                    ax.plot([v[storage_field] for v in extra], [v['extra_endpoint_rms'] for v in extra],
                            color=color, marker=marker, markerfacecolor='white', markeredgewidth=1,
                            markersize=4.5, linewidth=.8, linestyle=':', label='Log., undeclared')
        pair = row['dense_pair']
        if pair and pair['endpoint_rms'] > 0:
            ax.axhline(pair['endpoint_rms'], color='#333333', linewidth=.9, linestyle=':', label='Independent dense')
            ax.plot(row['dense_learned'], pair['endpoint_rms'], 'x', color='#333333', markersize=5)
        extra_pair = next((v for v in row['models'] if v['name'] == f"dense_{row['width']}"), {})
        if extra_pair.get('extra_endpoint_rms', 0) > 0:
            ax.axhline(extra_pair['extra_endpoint_rms'], color='#aaaaaa', linewidth=.7,
                       linestyle='-.', label='Dense, undeclared')
        missing = [label for family, (label, _, _) in families.items()
                   if family in row['requested_families'] and not scored(row, family)]
        if missing:
            ax.text(0, -.28, 'Unavailable: '+', '.join(missing), transform=ax.transAxes,
                    fontsize=6, color='#666666', va='top')
    save(fig, 'figure3_accuracy')

    fig, axes = panels(r'Query RMS ratio $E(t)/E_{\mathrm{iid}}(t)$')
    for ax, task in zip(axes, tasks):
        row = fixed(task)
        ax.set_xlabel('Training time')
        ax.set_title(f"{task['title']}  ·  $n={task['fixed_width']}$")
        if row is None or (task['name'], row['width']) not in curves:
            empty(ax, 'Fixed-width reference not yet available')
            continue
        times, width_curves, _ = curves[(task['name'], row['width'])]
        if not row['dense_pair']:
            empty(ax, 'Independent dense comparator unavailable')
            continue
        baseline = width_curves[row['dense_pair']['name']]
        valid = (times > 0) & (baseline > 0)
        choices = []
        row['trajectory_selection'] = {}
        for family, (label, color, _) in families.items():
            values = scored(row, family)
            if not values:
                continue
            passing_name = row['selected'].get(family)
            chosen = (next(v for v in values if v['name'] == passing_name) if passing_name else
                      min(values, key=lambda v: (max(v['endpoint_rms']/baseline[-1],
                                                    v['worst_recorded_rms']/baseline.max()), v['moving'])))
            row['trajectory_selection'][family] = dict(name=chosen['name'], moving=chosen['moving'],
                status=chosen['status'], total=chosen['total'],
                rule=('smallest tested passing budget from Figure 2' if passing_name else
                      'no tested pass: completed budget minimizing the larger endpoint and max/max ratio'))
            choices.append((chosen, label if passing_name else label+' (no pass)', color,
                            '-' if passing_name else '--'))
        target = next((v for v, _, _, _ in choices if v['family'] == 'logarithmic'),
                      choices[-1][0] if choices else None)
        controls = [v for family in ('dense', 'low_rank') for v in scored(row, family)
                    if v['name'] != f"dense_{row['width']}" and v['moving'] < row['dense_learned']]
        if target and controls:
            control = min(controls, key=lambda v: (abs(math.log(v['moving']/target['moving'])), v['name']))
            label, color, _ = control_styles[control['family']]
            choices.append((control, label, color, '--'))
            row['trajectory_selection']['matched_control'] = dict(name=control['name'],
                moving=control['moving'], target_name=target['name'], target_moving=target['moving'],
                rule='nearest learned-state count in logarithmic distance')
        frozen = scored(row, 'frozen_features')
        if frozen:
            choices.append((frozen[0], 'Frozen features', control_styles['frozen_features'][1], '--'))
            row['trajectory_selection']['frozen_features'] = dict(name=frozen[0]['name'], moving=frozen[0]['moving'])
        for point, label, color, style in choices:
            curve = width_curves[point['name']]
            ratio = np.divide(curve, baseline, out=np.full_like(curve, np.nan), where=valid)
            selection_key = 'matched_control' if point['family'] in ('dense', 'low_rank') else point['family']
            row['trajectory_selection'][selection_key].update(
                plotted_times=times[valid].tolist(), pointwise_ratios=ratio[valid].tolist())
            ax.plot(times, np.where(ratio > 0, ratio, np.nan), color=color,
                    linewidth=1.3, linestyle=style, label=label)
        if row['dense_pair']:
            row['trajectory_selection']['independent_dense'] = dict(name=row['dense_pair']['name'],
                                                                     moving=row['dense_learned'])
            ax.axhline(1, linestyle=':', color='#333333', linewidth=1.1, label='Dense-pair ratio 1')
    save(fig, 'figure4_training')

    captions = [
        f'Figure 2. Smallest tested learned state passing both finite-query RMS criteria. '
        f'At each reference width n, the endpoint RMS and maximum RMS over recorded times must each '
        f'be at most {factor:g} times the corresponding metric between two independently initialized '
        'dense width-n networks. With E(t) the declared-query RMS and E_iid(t) the dense-pair RMS, '
        'the criteria use E(T)/E_iid(T) and max_t E(t)/max_t E_iid(t), separately. '
        'Top panels count learned scalars; bottom panels include all fixed retained scalars. '
        'The ≤ annotation marks a passing lowest tested budget: the crossing is left-censored '
        'by the grid, and smaller untested budgets are unresolved. No-tested-pass widths are '
        'explicitly labelled; their crossing remains open. Lines connect tested widths; no '
        'crossing interpolation or growth exponent is fitted. Harmonic and Logarithmic markers '
        'are displaced horizontally by -1.5% and +1.5% to separate overlaps; underlying widths '
        'are identical. This is a tested-budget minimum, not a global minimum or an asymptotic '
        'scaling result. The dotted Dense formula line counts '
        'all learned scalars: (L-1)n^2+n(d+1), where L is hidden depth and d is input dimension.',
        'Figure 3. Endpoint prediction RMS to the coupled dense reference versus learned-state count '
        '(top) and total retained scalar count, including fixed state (bottom), at the stated fixed '
        'width. Hollow markers retain their query-scope meaning and do not encode storage. '
        'Filled compression markers use declared query inputs. Logarithmic '
        'setup sees these inputs but never their labels; Harmonic setup uses input geometry independently '
        'of scored query inputs. Hollow Logarithmic markers use entirely undeclared inputs, checked '
        'disjoint from both the training and declared-query panels, and their own dense reference '
        'predictions. The thin undeclared dense line uses the same extra panel. The independent-dense '
        'line is the observed RMS, without the selection multiplier. Small-dense and low-rank controls '
        'show their actual learned counts. The dashed frozen-feature line shows endpoint RMS; its '
        'marker counts the primal readout. Equivalent '
        'executed dual storage is recorded in each model record. Nonpositive scores are omitted on log axes.',
        'Figure 4. Pointwise ratio E(t)/E_iid(t) of declared-query prediction RMS to the dense '
        'reference throughout the recorded training trajectory at the stated fixed width. Each '
        'passing compression uses exactly the smallest tested passing budget from Figure 2. '
        'If no budget passes, the dashed curve labelled no pass uses the completed budget '
        'minimizing max{E(T)/E_iid(T), max_t E(t)/max_t E_iid(t)}; it is a failed candidate. '
        'One small-dense or low-rank control '
        'is chosen nearest in logarithmic learned-state '
        'distance to the selected Logarithmic model, or the last available compression. The independent '
        'dense-pair reference is the horizontal ratio 1. Initialization t=0 and every zero '
        'dense-pair denominator are omitted; zero ratios are omitted on logarithmic axes. '
        'The Figure 2 maximum criterion is a ratio of separate recorded maxima, not the maximum '
        'of this pointwise ratio. Endpoint and maximum-error matching do not imply pointwise matching.',
        'All panels are bounded drafts with one reference seed and one independent dense comparator '
        'per width. Selection uses the declared query errors, so they are not an independent '
        'post-selection test. Full-horizon offline spectral source construction is additional setup '
        'work. Finite recorded Euler trajectories are not a gradient-flow refinement certificate. '
        'Learned state counts evolving retained scalars; total storage includes fixed retained '
        'scalars. Both are plotted and listed below. Common data, integrator workspace and temporary source-construction '
        'storage are excluded. Missing and incomplete models and constructor errors are listed in metrics.json.']
    for task in tasks:
        excluded = [label for family, (label, _, _) in families.items()
                    if task['records'] and not any(family in row['requested_families'] for row in task['records'])]
        if excluded:
            captions.append(f"{task['title']}: {', '.join(excluded)} excluded by the configured experimental scope.")
        row = fixed(task)
        if row and row.get('trajectory_selection'):
            counts = '; '.join(f"{value['name']}: {value['moving']:,}"
                               for value in row['trajectory_selection'].values())
            captions.append(f"Figure 4, {task['title']}: learned-state counts in scalars are {counts}.")
    captions.append('task | reference width | model | learned | fixed additional | total retained')
    for task in tasks:
        for row in task['records']:
            for point in row['models']:
                if 'moving' in point:
                    captions.append(f"{task['name']} | {row['width']} | {point['name']} | "
                                    f"{point['moving']} | {point['fixed']} | {point['total']}")
    (destination/'captions.txt').write_text('\n\n'.join(captions)+'\n')
    save_json(destination/'metrics.json', dict(manifest=str(manifest_path), manifest_sha256=sha(manifest_bytes),
        plot_source_sha256=sha(Path(__file__).read_bytes()), factor=factor, tasks=tasks,
        selection='smallest tested learned state passing endpoint and maximum-recorded RMS independently',
        fitted_scaling_exponents=None, figures=['figure2_storage', 'figure3_accuracy', 'figure4_training']))
    print(json.dumps(dict(output=str(destination), tasks=len(tasks),
                          available_widths={task['name']: len(task['records']) for task in tasks})), flush=True)
    return 0


def restored_paper_plot(argv):
    """Restore Figures 2/3 from the named, validated saved trajectories; no training."""
    parser = argparse.ArgumentParser(description=restored_paper_plot.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--out', type=Path, help='Fresh figure destination; validators use its sibling directory')
    parser.add_argument('--scaling-only', action='store_true', help='Plot a fresh width-scaling repetition without Figure 3 inputs')
    args = parser.parse_args(argv)
    plan_bytes = args.config.read_bytes()
    plan = json.loads(plan_bytes)
    destination = args.out or Path(plan['output'])
    destination.mkdir(parents=True, exist_ok=False)
    validation = destination.parent/'validated_metrics'/destination.name
    validation.mkdir(parents=True, exist_ok=False)
    metrics, provenance = {}, {}
    for task in ('circle', 'digits'):
        output = validation/task
        options = ['--runs', *plan[task+'_runs'], '--out', str(output), '--factor', '3']
        experiment_scaling_plot(options+(['--fit-log-powers'] if task == 'circle' else []))
        path = output/'plots'/'plot_001'/'metrics.json'
        metrics[task] = json.loads(path.read_text())
        provenance[task] = dict(path=str(path), sha256=sha(path.read_bytes()))
    if not args.scaling_only:
        sphere_points_plot_main(['--run', plan['sphere_run'], '--out', str(validation/'sphere3'),
                                '--seed-statistic', 'median', '--thin-dense', '--clean', '--frozen-point'])
        path = validation/'sphere3'/'point_check_median_thinned_clean_frozen_point.json'
        sphere = json.loads(path.read_text())
        provenance['sphere3'] = dict(run=plan['sphere_run'], path=str(path), sha256=sha(path.read_bytes()))
        path = Path(plan['image_metrics'])
        assert sha(path.read_bytes()) == plan['image_metrics_sha256'], 'Saved image metrics changed'
        image_task = next(t for t in json.loads(path.read_text())['tasks'] if t['name'] == 'digits17')
        image_row = next(row for row in image_task['records'] if row['width'] == 4096)
        saved = image_row['provenance']
        for file, expected in ((Path(image_row['root'])/'run.json', saved['run_sha256']),
                               (Path(image_row['root'])/'source.py', saved['source_sha256']),
                               (Path(saved['repetition'])/'report.json', saved['report_sha256']),
                               (Path(saved['repetition'])/'trajectories.npz', saved['trajectories_sha256'])):
            assert sha(file.read_bytes()) == expected, f'Saved image input changed: {file}'
        provenance['image'] = dict(path=str(path), sha256=sha(path.read_bytes()), inputs=saved)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False,
                         'pdf.fonttype': 42, 'savefig.facecolor': 'white'})
    styles = dict(legendre=('Legendre', '#4477AA', 's'), harmonic=('Harmonic', '#EE7733', '^'),
                  logarithmic=('Logarithmic', '#228833', 'o'), dense=('Dense', '#666666', 'D'),
                  low_rank=('Low rank', '#CC6677', 'v'), frozen_features=('Frozen features', '#AA4499', '*'))

    def finish(figure, axes, name):
        handles = {}
        for axis in axes.flat:
            axis.grid(which='major', alpha=.14)
            hs, labels = axis.get_legend_handles_labels()
            handles.update(zip(labels, hs))
        figure.legend(handles.values(), handles.keys(), loc='upper center', ncol=4,
                      frameon=False, fontsize=8, bbox_to_anchor=(.5, 1))
        figure.tight_layout(rect=(0, 0, 1, .90), h_pad=2, w_pad=2)
        for suffix in ('png', 'pdf'):
            figure.savefig(destination/f'{name}.{suffix}', dpi=200, bbox_inches='tight')
        plt.close(figure)

    selections = {}
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.9), squeeze=False)
    for column, (task, title) in enumerate((('circle', 'Circle'), ('digits', '8×8 digits 1 / 7'))):
        rows = metrics[task]['records']
        selections[task] = []
        for row in rows:
            for family, name in row['selected'].items():
                point = next(p for p in row['candidates'] if p['name'] == name)
                bracket = row['budget_search'].get(family, {}).get('bracket', {})
                selections[task].append(dict(width=row['width'], family=family, point=point, bracket=bracket))
        for index, field in enumerate(('moving', 'total')):
            axis = axes[index, column]
            axis.set(xscale='log', yscale='log', xlabel='Dense reference width',
                     ylabel='Learned scalars' if index == 0 else 'Total retained scalars')
            if index == 0:
                axis.set_title(title+' · 3× criterion')
            ns = [row['width'] for row in rows]
            axis.plot(ns, [row['dense_learned'] for row in rows], ':', color='#666666', label='Dense formula')
            for family in ('legendre', 'harmonic', 'logarithmic'):
                points = [p for p in selections[task] if p['family'] == family]
                if not points:
                    continue
                label, color, marker = styles[family]
                axis.plot([p['width'] for p in points], [p['point'][field] for p in points],
                          color=color, marker=marker, ms=4.5, lw=1.1, label=label)
                for item in points:
                    point, bracket = item['point'], item['bracket']
                    lower = bracket.get('lower')
                    candidates = next(row['candidates'] for row in rows if row['width'] == item['width'])
                    failed = [p for p in candidates if p['family'] == family and p['status'] == 'fail'
                              and p.get('model', {}).get('order' if family == 'legendre' else 'width') == lower]
                    if bracket.get('status') == 'resolved_local' and failed:
                        axis.errorbar(item['width'], point[field],
                                      yerr=[[max(0, point[field]-failed[0][field])], [0]],
                                      fmt='none', color=color, capsize=3, lw=1)
                    elif bracket.get('status') != 'minimum_order':
                        axis.annotate('≤', (item['width'], point[field]), xytext=(-11, -3),
                                      textcoords='offset points', color=color, fontsize=10)
                if task == 'circle' and index == 0 and family in ('harmonic', 'logarithmic'):
                    fit = metrics[task]['descriptive_log_power_fits'][family]
                    if fit['status'] == 'fitted':
                        grid = np.geomspace(min(fit['widths']), max(fit['widths']), 150)
                        axis.plot(grid, fit['C']*np.log(grid)**fit['p'], '--', color=color, lw=1,
                                  label=f"{label} fit: p={fit['p']:.2f}")
            axis.set_xticks(ns, labels=[str(n) for n in ns], rotation=20 if task == 'circle' else 0)
            axis.minorticks_off()
            axis.set_xlim(min(ns)*.82, max(ns)*1.22)
            axis.set_ylim(min(p['point'][field] for p in selections[task])*.55,
                          max(row['dense_learned'] for row in rows)*1.8)
            missing = [str(row['width']) for row in rows if 'harmonic' not in row['selected']]
            note = ('Harmonic: no pass at '+', '.join(missing) if task == 'circle' and missing else
                    '≤  Logarithmic: lower budgets inconclusive' if task == 'digits' else '')
            axis.text(.03, .94, note,
                      transform=axis.transAxes, fontsize=7, va='top', color='#555555')
    finish(fig, axes, 'figure2_storage')

    if args.scaling_only:
        captions = [plan['scope'],
            'Figure 2: top row counts learned scalars, bottom row learned plus fixed retained scalars. '
            'Dense storage is (L-1)n²+n(d+1). Vertical bars are measured local failing/passing budget '
            'brackets, not statistical error bars; ≤ denotes an unresolved smaller-budget crossing. '
            'Nonmonotone and missing passing candidates remain recorded. The criterion compares '
            'endpoint RMS and maximum-recorded RMS separately, not their pointwise ratio at every time. '
            'Dashed circle curves fit C(log n)^p to measured passing learned budgets after the search; '
            'these single-repetition fits are descriptive, not established asymptotic exponents. '
            'No fit is inferred for the image points with unresolved lower budgets. Common data, '
            'temporary source assembly and solver workspace are excluded from retained model counts.']
        (destination/'captions.txt').write_text('\n\n'.join(captions)+'\n')
        save_json(destination/'metrics.json', dict(config=str(args.config), config_sha256=sha(plan_bytes),
            plot_source_sha256=sha(Path(__file__).read_bytes()), factor=3, provenance=provenance,
            figure2=selections, circle_fits=metrics['circle']['descriptive_log_power_fits'],
            image_fit=None, captions=captions, scope=plan['scope']))
        print(json.dumps(dict(figures=str(destination), validated_metrics=str(validation))), flush=True)
        return 0

    sphere_points = []
    for name, point in sphere['displayed_points'].items():
        family = {'lowrank': 'low_rank', 'ntk': 'frozen_features'}.get(name.split('_')[0], name.split('_')[0])
        sphere_points.append(dict(point, name=name, family=family))
    image_points = [dict(p) for p in image_row['models'] if p.get('endpoint_rms', 0) > 0]
    image_dense_summaries = {}
    if plan.get('image_dense_repeats'):
        path = Path(plan['image_dense_repeats'])
        assert sha(path.read_bytes()) == plan['image_dense_repeats_sha256'], 'Dense-repeat summary changed'
        repeated = json.loads(path.read_text())
        assert repeated['complete'] and repeated['provenance']['original_sha256']['trajectories'] == saved['trajectories_sha256']
        image_dense_summaries = repeated['models']
        for point in image_points:
            if point['family'] != 'dense':
                continue
            summary = image_dense_summaries[point['name']]
            assert summary['count'] == 3 and summary['moving'] == point['moving']
            for metric in ('endpoint_rms', 'worst_recorded_rms', 'extra_endpoint_rms', 'extra_worst_recorded_rms'):
                point[metric] = summary[metric]['mean']
        provenance['image_dense_repeats'] = dict(path=str(path), sha256=sha(path.read_bytes()),
                                               provenance=repeated['provenance'])
    image_pair = next(p['endpoint_rms'] for p in image_points if p['name'] == 'dense_4096')
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.9), squeeze=False)
    for column, (title, points, pair) in enumerate((
            ('3D sphere · n = 4096', sphere_points, sphere['dense_pair_rms']),
            ('8×8 digits 1 / 7 · n = 4096', image_points, image_pair))):
        for index, field in enumerate(('moving', 'total')):
            axis = axes[index, column]
            axis.set(xscale='log', yscale='log', ylabel='Endpoint query RMS',
                     xlabel='Learned scalars' if index == 0 else 'Total retained scalars')
            if index == 0:
                axis.set_title(title)
            for family, (label, color, marker) in styles.items():
                values = sorted([p for p in points if p['family'] == family], key=lambda p: p[field])
                if not values:
                    continue
                if family == 'frozen_features':
                    axis.axhline(values[0]['endpoint_rms'], color=color, ls='--', lw=1, label=label)
                    axis.plot(values[0][field], values[0]['endpoint_rms'], marker=marker, color=color, ms=5)
                else:
                    axis.plot([p[field] for p in values], [p['endpoint_rms'] for p in values],
                              color=color, marker=marker, ms=4.5, lw=1.1, label=label)
                if column == 0:
                    for point in values:
                        summary = sphere['displayed_dense_seed_summaries'].get(point['name'])
                        if summary:
                            axis.errorbar(point[field], point['endpoint_rms'], fmt='none', color=color,
                                          yerr=[[summary['median']-summary['minimum']],
                                                [summary['maximum']-summary['median']]], capsize=3, lw=1)
                if column == 1 and family == 'logarithmic':
                    extra = [p for p in values if p.get('extra_endpoint_rms', 0) > 0]
                    axis.plot([p[field] for p in extra], [p['extra_endpoint_rms'] for p in extra],
                              ':', marker=marker, mfc='white', color=color, ms=5, lw=.9, label='Log., undeclared')
                if column == 1 and family == 'dense' and image_dense_summaries:
                    for point in values:
                        deviation = image_dense_summaries[point['name']]['endpoint_rms']['sd']
                        axis.errorbar(point[field], point['endpoint_rms'], yerr=deviation,
                                      fmt='none', color=color, capsize=3, lw=1)
            axis.axhline(pair, color='#333333', ls=':', lw=1, label='Dense pair')
            if column == 1:
                extra_pair = next(p['extra_endpoint_rms'] for p in points if p['name'] == 'dense_4096')
                axis.axhline(extra_pair, color='#999999', ls='-.', lw=.7, label='Dense, undeclared')
            axis.set_xlim(min(p[field] for p in points)*.65, max(p[field] for p in points)*1.6)
            axis.set_ylim(min(p['endpoint_rms'] for p in points)*.55,
                          max(p['endpoint_rms'] for p in points)*1.7)
    finish(fig, axes, 'figure3_accuracy')
    captions = [
        'Figure 2. Smallest TESTED passing budgets under the restored 3× criterion. At each dense width n, '
        'E(t) is the RMS prediction difference on the declared query inputs from its coupled dense reference; '
        'E_iid(t) compares that reference with the independent width-n dense network. Passing requires both '
        'E(T) ≤ 3 E_iid(T) and max_t E(t) ≤ 3 max_t E_iid(t), with T=32 and 65 recorded times. '
        'Top: learned scalars; bottom: learned plus fixed retained scalars. The dense formula is '
        '(L−1)n²+n(d+1), with L=2 hidden layers and input dimension d=2 (circle) or 64 (images). '
        'Vertical bars span a measured failing lower candidate and the selected passing candidate; '
        'they are local tested brackets, not confidence intervals or global minima. Circle Harmonic/Logarithmic '
        'passing width brackets have upper/lower ratio ≤1.2. Harmonic at n=8192 is nonmonotone across budgets; '
        'no Harmonic pass is available at n=16384, and all failed/incomplete runs remain recorded. '
        'Legendre order 1 is the lowest allowed order; higher-order brackets remain discrete.',
        'Circle points reuse the original adaptive six-width measurements (n=512–16384, reference seeds '
        '701–706, Euler step 1/640). Dashed curves are descriptive fits of learned storage '
        'C(log n)^p to measured passing budgets only: Harmonic p=3.50871 from five widths, '
        'Logarithmic p=5.19661 from six. They are selected-budget summaries, not identified asymptotic laws; '
        'no interpolated budget is a measured model. Image points reuse dense seeds 901–903 at n=1024,2048,4096 '
        'and Euler step 0.00625. Refinement tried Logarithmic widths 128,192,224 with source ranks 5,10,13 '
        'using prefixes of each original maximum-rank source; every new constructor failed condition cap 16 '
        'before training. These are inconclusive gates, not accuracy failures. The passing width-256/rank-8 '
        'models retain 82,184 learned scalars each; ≤ marks upper bounds on unresolved minima. '
        'The image crossing is NOT resolved to 20%, and no exponent is fitted from the three image widths. '
        'Harmonic was outside this image pilot scope.',
        'Figure 3. Endpoint declared-query RMS against the coupled dense width-4096 reference versus '
        'learned scalars (top) and total retained scalars (bottom). The 3D-sphere panel restores exactly the '
        'saved screenshot trajectory chain: Legendre orders 1,2,3,12; Harmonic and Logarithmic widths '
        '148,210,299,424,600,850 (the last two source ranks are 44,65); low-rank capacities 8,16,24,96; '
        'the thinned small-dense controls; and frozen features. Sphere Euler step remains 1/640, '
        'reference seed 601. Small-dense medians and observed min–max bars use seeds 10601,10602,10603 '
        'against that SAME fixed reference and data; the width-4096 dense pair is a single pair. '
        'All compression points remain single saved runs: these are not three independently rebuilt '
        'compression repetitions, and no new higher-order training was performed. The image panel retains '
        'all saved width-4096 raw-image points and controls, including hollow Logarithmic markers for inputs '
        'entirely undeclared at setup; their dense comparison uses the same undeclared panel. '
        'Hollows encode query scope, not storage. Dotted dense-pair lines show actual RMS, without the 3× '
        'selection multiplier. Dashed frozen-feature lines retain their actual errors; markers count the '
        'primal readout and frozen backbone, with equivalent executed dual storage in the source records.',
        'Provenance: circle_width_scaling_20261009/adaptive and adaptive_16384; '
        'cubic_log_comparison_20261008/sphere3_compression_larger and its recorded dependencies; '
        'paper_figure_drafts_20261009/digits17_n4096 via the hash-checked feedback figure metrics; '
        'paper_appendix_pilots_20261009/restored/digits_budget for the bounded image refinement. '
        'All tasks use eight training and thirty declared query inputs. Harmonic/Logarithmic setup uses '
        'offline full-horizon dense-rollout source construction; Logarithmic setup sees declared inputs '
        'but never query labels. Circle/images use RK4 source step 0.125 with float64 coefficient setup. '
        'Selection uses declared query errors, not an independent post-selection test. Retained storage '
        'excludes common data, solver workspace and temporary offline source construction. These are '
        'finite recorded Euler results without a new continuous-time or per-budget refinement certificate.']
    if image_dense_summaries:
        captions.append('Figure 3 image-panel update: each dense point and the horizontal dense benchmark '
            'use mean endpoint RMS across the original model and two new independent initializations '
            '(repetition labels 903,904,905), all compared with the SAME saved reference903 and dataset. '
            'Bars show sample SD, not standard error. Compression curves are unchanged single runs; '
            'the sphere panel retains its previous median/min–max display. No new reference or '
            'compression training is implied by this conditional dense-only replication.')
    (destination/'captions.txt').write_text('\n\n'.join(captions)+'\n')
    save_json(destination/'metrics.json', dict(status='PASS', config=str(args.config),
        config_sha256=sha(plan_bytes), plot_source_sha256=sha(Path(__file__).read_bytes()), factor=3,
        provenance=provenance, figure2=selections, circle_fits=metrics['circle']['descriptive_log_power_fits'],
        image_fit=None, figure3=dict(sphere=sphere_points, sphere_dense_summaries=sphere['displayed_dense_seed_summaries'],
                                    images=image_points, image_dense_summaries=image_dense_summaries), captions=captions,
        scope='saved-array/hash checks and restored figures; no new training or numerical certificate'))
    print(json.dumps(dict(status='PASS', figures=str(destination), validated_metrics=str(validation))), flush=True)
    return 0


@torch.no_grad()
def dense_control_repeats_main(argv=None):
    """Repeat only dense controls against one unchanged saved image reference.

    First call with --config only to freeze a fresh output. Run its source.py
    with --seed/--device in separate workers, then call --summarize on CPU.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    action = parser.add_mutually_exclusive_group()
    action.add_argument('--seed', type=int)
    action.add_argument('--summarize', action='store_true')
    parser.add_argument('--device', default='cuda:0')
    args = parser.parse_args(argv)
    config_bytes = args.config.read_bytes()
    config = json.loads(config_bytes)
    out, original = Path(config['output']), Path(config['original_repetition'])
    if config['widths'] != [256, 384, 512, 598, 648, 738, 4096] or config['seeds'] != [904, 905]:
        raise ValueError('This bounded repeat plan requires the seven saved widths and seeds 904/905')
    if config['seconds_per_fit'] != 120:
        raise ValueError('The repeat plan requires a 120-second cap per fit')
    paths = dict(run=Path(config['original_run']), report=original/'report.json',
                 trajectories=original/'trajectories.npz')
    for name, path in paths.items():
        if sha(path.read_bytes()) != config['original_sha256'][name]:
            raise ValueError(f'Changed original input: {path}')
    old_manifest = json.loads(paths['run'].read_text())
    old_report = json.loads(paths['report'].read_text())
    with np.load(paths['trajectories'], allow_pickle=False) as archive:
        saved = {key: archive[key] for key in archive.files}
    training, model_config = old_manifest['config']['training'], old_manifest['config']['model']
    expected_training = dict(solver='euler', step=.00625, horizon=32, record_every=80, dtype='float32')
    if training != expected_training or model_config != dict(width=4096, depth=2, activation='tanh'):
        raise ValueError('Original model or training settings differ from the bounded plan')
    if (old_report['seed'] != 903 or not old_report['complete']
            or not old_report['runs']['reference']['complete']
            or old_manifest['config']['execution']['tf32']):
        raise ValueError('Expected complete seed-903 reference with TF32 disabled')
    data_hashes = {key: array_sha(saved[key]) for key in old_report['data_sha256']}
    if data_hashes != old_report['data_sha256'] or data_hashes != old_manifest['identity']['data_sha256']:
        raise ValueError('Original saved data hashes disagree')
    reference_times = saved['times_reference']
    if (not np.isfinite(reference_times).all() or len(reference_times) != 65
            or reference_times[0] != 0 or reference_times[-1] != 32
            or not np.array_equal(reference_times, old_report['runs']['reference']['times'])):
        raise ValueError('Unexpected original observation times')
    reference_hashes = {key: array_sha(saved[key]) for key in
                        ('reference', 'extra_reference', 'times_reference')}
    if not all(np.isfinite(saved[key]).all() for key in reference_hashes):
        raise ValueError('Nonfinite saved reference')
    source_hash = sha(Path(__file__).read_bytes())
    provenance = dict(original_sha256=config['original_sha256'], reference_seed=903,
        reference_array_sha256=reference_hashes, data_sha256=data_hashes,
        reference_initial_state_sha256=old_report['reference_initial_state_sha256'],
        config_sha256=sha(config_bytes), source_sha256=source_hash)
    if args.seed is None and not args.summarize:
        out.mkdir(parents=True, exist_ok=False)
        (out/'config.json').write_bytes(config_bytes)
        (out/'source.py').write_bytes(Path(__file__).read_bytes())
        save_json(out/'run.json', dict(config=config, **provenance,
            scope='Two additional dense initializations per width; fixed original data/reference; no new reference or compression training'))
        print(json.dumps(dict(event='prepared', output=str(out))), flush=True)
        return 0
    manifest = json.loads((out/'run.json').read_text())
    if manifest['config'] != config or any(manifest[key] != value for key, value in provenance.items()):
        raise ValueError('Config, source, or original provenance differs from the prepared run')
    if sha((out/'source.py').read_bytes()) != source_hash:
        raise ValueError('Prepared source snapshot changed')
    m, q = len(saved['train_labels']), len(saved['query_inputs'])

    def score(arrays, report, width, seed):
        name = f'dense_{width}'
        runtime = report['runs'][name]
        prediction, extra = arrays[name], arrays['extra_'+name]
        times = arrays['times_'+name]
        if (not runtime['complete'] or runtime['stop_reason'] != 'horizon'
                or runtime['steps'] != 5120 or runtime['step'] != .00625
                or runtime['dtype'] != 'torch.float32' or runtime['actual_horizon'] != 32
                or not np.array_equal(times, reference_times)
                or not np.array_equal(times, runtime['times'])
                or prediction.shape != saved['reference'].shape
                or extra.shape != saved['extra_reference'].shape
                or not np.isfinite(prediction).all() or not np.isfinite(extra).all()):
            raise ValueError(f'Incomplete or incompatible dense trajectory: seed={seed}, width={width}')
        initialization_seed = _experiment_seed(seed, name)
        if report['models'][name]['initialization_seed'] != initialization_seed:
            raise ValueError(f'Dense initialization seed mismatch: {seed}/{name}')
        declared = np.sqrt(np.mean((prediction[:, m:].astype(float)-saved['reference'][:, m:])**2, axis=1))
        undeclared = np.sqrt(np.mean((extra.astype(float)-saved['extra_reference'])**2, axis=1))
        values = dict(endpoint_rms=float(declared[-1]), worst_recorded_rms=float(declared.max()),
            extra_endpoint_rms=float(undeclared[-1]), extra_worst_recorded_rms=float(undeclared.max()),
            training_mse=runtime['final_training_mse'], seconds=runtime['seconds'],
            training_seconds=runtime['training_seconds'], setup_seconds=report['models'][name]['setup_seconds'])
        if not all(math.isfinite(value) for value in values.values()):
            raise ValueError(f'Nonfinite dense metric: {seed}/{name}')
        return dict(seed=seed, initialization_seed=initialization_seed, **values)

    if args.summarize:
        repetitions = [(903, saved, old_report)]
        worker_hashes = {}
        for seed in config['seeds']:
            folder = out/f'seed_{seed}'
            report = json.loads((folder/'report.json').read_text())
            payload = (folder/'trajectories.npz').read_bytes()
            if (not report['complete'] or report['errors'] or report['seed'] != seed
                    or report['provenance'] != provenance or sha(payload) != report['trajectories_sha256']):
                raise ValueError(f'Incomplete or changed worker: {folder}')
            with np.load(folder/'trajectories.npz', allow_pickle=False) as archive:
                arrays = {key: archive[key] for key in archive.files}
            repetitions.append((seed, arrays, report))
            worker_hashes[str(seed)] = dict(report_sha256=sha((folder/'report.json').read_bytes()),
                                           trajectories_sha256=sha(payload))
        models = {}
        for width in config['widths']:
            values = [score(arrays, report, width, seed) for seed, arrays, report in repetitions]
            statistics = {}
            for key in values[0].keys()-{'seed', 'initialization_seed'}:
                observations = np.asarray([row[key] for row in values], dtype=float)
                statistics[key] = dict(mean=float(observations.mean()), sd=float(observations.std(ddof=1)),
                                       values=observations.tolist())
            models[f'dense_{width}'] = dict(width=width, moving=width*(width+65), fixed=0,
                count=len(values), samples=values, **statistics)
        save_json(out/'summary.json', dict(complete=True, provenance=provenance,
            worker_sha256=worker_hashes, models=models, recorded_times=reference_times.tolist(),
            scope='Original plus two independent dense controls, conditional on one fixed reference and dataset; sample SD, not uncertainty over references; finite Euler results without a new refinement certificate'))
        print(json.dumps(dict(event='summarized', output=str(out/'summary.json'))), flush=True)
        return 0

    if args.seed not in config['seeds']:
        raise ValueError('Worker seed is outside the frozen plan')
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    inputs = torch.as_tensor(saved['train_inputs'], device=device, dtype=torch.float32)
    labels = torch.as_tensor(saved['train_labels'], device=device, dtype=torch.float32)
    queries = torch.as_tensor(np.concatenate((saved['train_inputs'], saved['query_inputs'],
                                              saved['extra_query_inputs'])), device=device, dtype=torch.float32)
    folder = out/f'seed_{args.seed}'
    folder.mkdir(exist_ok=False)
    arrays = {}
    report = dict(seed=args.seed, complete=False, provenance=provenance, models={}, runs={}, errors={},
        device=str(device), hardware=torch.cuda.get_device_name(device) if device.type == 'cuda' else platform.processor())

    def persist():
        np.savez_compressed(folder/'trajectories.npz', **arrays)
        report['trajectories_sha256'] = sha((folder/'trajectories.npz').read_bytes())
        save_json(folder/'report.json', report)

    persist()
    for width in config['widths']:
        name, started = f'dense_{width}', time.monotonic()
        initialization_seed = _experiment_seed(args.seed, name)
        try:
            model = DeepDense(width, inputs.shape[1], 2, 'tanh', initialization_seed, device)
            synchronize(device)
            setup_seconds = time.monotonic()-started
            initial_hashes = [array_sha(value.cpu().numpy()) for value in model.initial_state]
            _experiment_move(model, device, torch.float32)
            report['models'][name] = dict(width=width, family='dense', moving=width*(width+65), fixed=0,
                initialization_seed=initialization_seed, initial_float64_sha256=initial_hashes,
                setup_seconds=setup_seconds)
            state, prediction, runtime = integrate_euler(model, inputs, labels, queries, .00625,
                config['seconds_per_fit'], horizon=32, max_steps=5120, observation_every=80)
            arrays[name], arrays['extra_'+name] = prediction[:, :m+q], prediction[:, m+q:]
            arrays['times_'+name] = np.asarray(runtime['times'])
            report['runs'][name] = runtime
            metrics = score(arrays, report, width, args.seed)
            report['models'][name]['metrics'] = metrics
            del state, model
            print(json.dumps(dict(event='dense_repeat_done', width=width, **metrics)), flush=True)
        except (ValueError, RuntimeError, ArithmeticError) as error:
            report['errors'][name] = f'{type(error).__name__}: {error}'
            persist()
            raise
        persist()
    report['complete'] = not report['errors']
    persist()
    return int(not report['complete'])


def budget_seed_plot(argv):
    """Audit saved seed replications and plot tested passing storage."""
    import ast
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter
    parser = argparse.ArgumentParser(description=budget_seed_plot.__doc__)
    parser.add_argument('--runs', nargs='+', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--family', choices=('harmonic', 'logarithmic', 'legendre'), default='harmonic')
    fits = parser.add_mutually_exclusive_group()
    fits.add_argument('--fit-log-powers', action='store_true',
                        help='Fit mean and median learned storage to C(log n)^p when all >=3 widths are complete')
    fits.add_argument('--fit-width-powers', action='store_true',
                      help='Fit mean and median learned storage to C*n^p when all >=3 widths are complete')
    args = parser.parse_args(argv)
    roots = [root.resolve() for root in args.runs]
    family, family_label = args.family, args.family.capitalize()

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def numerical_source(source):
        """Audit numerical call graphs without executing saved source files."""
        definitions = {node.name: node for node in ast.parse(source).body
                       if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
        pending = ['DeepDense', 'DeepHarmonic', 'unified_harmonic_sources', 'cubic_rollout_sources',
                   'integrate_euler', 'integrate', 'validation_data',
                   '_experiment_data', '_experiment_seed', '_experiment_move', '_budget_search_next']
        if family == 'legendre':
            pending = ['DeepDense', 'LegendreCompression', 'integrate_euler',
                       '_experiment_seed', '_experiment_move']
        require(all(name in definitions for name in pending),
                'Saved source is missing a required numerical definition')
        checked = {}
        while pending:
            name = pending.pop()
            if name in checked:
                continue
            node = definitions[name]
            checked[name] = sha(ast.dump(node, include_attributes=False).encode())
            pending.extend(item.id for item in ast.walk(node)
                           if isinstance(item, ast.Name) and item.id in definitions
                           and item.id not in checked)
        return dict(sha256=sha(json.dumps(checked, sort_keys=True).encode()), definitions=checked)

    require(len(roots) == len(set(roots)) and len(roots) >= 6,
            'Supply distinct run roots: at least two widths, three seeds per width')
    rows, common, common_source, common_times, seen = [], None, None, None, set()
    numerical_sources, common_numerical, source_orders_by_width = {}, None, {}
    for root in roots:
        manifest = json.loads((root/'run.json').read_text())
        config = manifest['config']
        require(json.loads((root/'config.json').read_text()) == config, f'Config mismatch: {root}')
        require(len(config['seeds']) == 1, f'Expected one seed per root: {root}')
        n, seed = config['model']['width'], config['seeds'][0]
        require((n, seed) not in seen, f'Duplicate width/seed: {n}/{seed}')
        seen.add((n, seed))
        path = (root/manifest['repetitions'][str(seed)]).resolve()
        require(path.is_relative_to(root) and path != root, f'Invalid repetition path: {root}')
        report = json.loads((path/'report.json').read_text())
        source_bytes = (root/'source.py').read_bytes()
        source_hash = sha(source_bytes)
        archive_hash = sha((path/'trajectories.npz').read_bytes())
        require(source_hash == manifest['source_sha256'] == manifest['identity']['source_sha256']
                == report['source_sha256']
                and archive_hash == report['trajectories_sha256'], f'Source/archive hash mismatch: {root}')
        if source_hash not in numerical_sources:
            numerical_sources[source_hash] = numerical_source(source_bytes)
        numerical = numerical_sources[source_hash]
        require(common_numerical is None or numerical == common_numerical,
                f'Numerical source definitions differ: {root}')
        common_numerical = numerical
        if family == 'legendre' and manifest.get('reused_from'):
            reused = manifest['reused_from']
            reused_bytes = (Path(reused['root'])/'source.py').read_bytes()
            reused_hash = sha(reused_bytes)
            require(reused_hash == reused['source_sha256'], f'Reused source hash differs: {root}')
            if reused_hash not in numerical_sources:
                numerical_sources[reused_hash] = numerical_source(reused_bytes)
            require(numerical_sources[reused_hash] == numerical,
                    f'Reused Legendre/dense/Euler definitions differ: {root}')
        require(report['seed'] == report['seeds']['reference'] == seed
                and report['fingerprint'] == manifest['fingerprint'], f'Run identity mismatch: {root}')
        search, plan = report['budget_search'][family], manifest['search_plan']
        require(search['factor'] == plan['factor'] == 1, f'Expected strict 1x criteria: {root}')
        if family == 'legendre':
            require(plan['expansion'][family].get('sequential') is True
                    and plan['expansion'][family].get('minimum', 1) == 1
                    and plan['expansion'][family]['start'] == 1,
                    f'Expected sequential positive integer Legendre orders: {root}')
            source, source_orders, restart = None, None, None
            method, setup = {}, None
            search_contract = dict(expansion={key: value for key, value in plan['expansion'][family].items()
                                             if key != 'maximum'})
        else:
            require(search['width_tolerance'] == plan['width_tolerance'] == .2,
                    f'Expected 20% local width brackets: {root}')
            source = report.get('sources', {}).get(family)
            method = config['methods']['non_oblivious'][family]
            setup = _experiment_setup(config, family)
            source_ranks = plan.get('source_max_ranks_by_width', {}).get(str(n), plan.get('source_max_ranks', {}))
            restart = plan.get('restart_harmonic') if family == 'harmonic' else None
            source_rank = max((value['source_rank'] for value in method['budgets']),
                default=restart['source_max_rank'] if restart else source_ranks.get(family, 0))
            source_orders = (report.get('harmonic_fresh_setup', {}).get('settings')
                             if family == 'harmonic' else None)
            if source_orders is None:
                source_orders = dict(time_degree=setup['time_degree'], source_max_rank=source_rank)
                if family == 'harmonic':
                    source_orders['spatial_degree'] = method['spatial_degree']
            require(source_rank > 0 and (not restart or restart == source_orders),
                    f'Frozen source orders differ: {root}')
            require(source_rank == source_orders['source_max_rank'], f'Planned source rank differs: {root}')
            require(n not in source_orders_by_width or source_orders == source_orders_by_width[n],
                    f'Frozen source orders differ between seeds at width {n}: {root}')
            source_orders_by_width[n] = source_orders
            common_orders = {key: value for key, value in source_orders.items()
                             if family == 'harmonic' or key != 'source_max_rank'}
            search_contract = dict(source_orders=common_orders, rank_rule=plan['rank_rule'],
                expansion={key: value for key, value in plan['expansion'][family].items() if key != 'maximum'})
            if family in plan.get('rank_knots', {}):
                search_contract['rank_knots'] = plan['rank_knots'][family]
        contract = dict(dataset=config['dataset'], training=config['training'],
            numerical_source_sha256=numerical['sha256'],
            model={key: value for key, value in config['model'].items() if key != 'width'},
            data_sha256=report['data_sha256'], tf32=config['execution']['tf32'],
            method={key: value for key, value in method.items() if key not in ('budgets', 'setup')},
            setup=setup, search=search_contract)
        if family == 'legendre':
            contract.pop('setup')
        require(common is None or contract == common, f'Data/model/training/source settings differ: {root}')
        common = contract
        if source is not None:
            require(source['effective_setup'] == setup, f'Compiled source setup differs: {root}')
            if family == 'harmonic':
                require(source_orders == dict(spatial_degree=source['spatial_degree'],
                    time_degree=source['chebyshev_degree'], source_max_rank=source['requested_rank']),
                    f'Compiled source orders differ from frozen settings: {root}')
                settings = {key: source[key] for key in ('method', 'horizon', 'rk4_step', 'rollout_dtype',
                    'coefficient_dtype', 'chebyshev_degree', 'spatial_degree', 'geometry_sha256', 'geometry_count',
                    'observation_count', 'boundaries', 'requested_rank', 'effective_setup')}
            else:
                require(bool(source['nested_ranks']) and max(source['nested_ranks']) == source_rank
                        and all(0 < rank <= source_rank for rank in source['nested_ranks'])
                        and source['chebyshev_degree'] == source['partitions']['new']['degree'] == setup['time_degree']
                        and source['horizon'] == config['training']['horizon']
                        and source['rk4_step'] == setup['rollout_step']
                        and source['source_flow_dtype'] == 'torch.'+setup['rollout_dtype']
                        and source['coefficient_dtype'] == 'torch.'+setup['coefficient_dtype']
                        and not source['passive_labels_used'] and source['scored_inputs_used']
                        and method['test_inputs_at_setup'] and not method.get('panel_span', False),
                        f'Compiled logarithmic source settings differ from frozen settings: {root}')
                boundaries = np.asarray(source['partitions']['new']['boundaries'])
                require(np.isfinite(boundaries).all() and boundaries[0] == 0
                        and boundaries[-1] == source['horizon'] and np.all(np.diff(boundaries) > 0),
                        f'Invalid residual-clock partition: {root}')
                settings = {key: source[key] for key in ('horizon', 'rk4_step', 'source_flow_dtype',
                    'coefficient_dtype', 'chebyshev_degree', 'randomized_svd_niter',
                    'training_count', 'passive_count', 'passive_labels_used', 'scored_inputs_used',
                    'source_provenance', 'effective_setup')}
                settings['partition'] = 'new'
            require(common_source is None or settings == common_source, f'Compiled source settings differ: {root}')
            common_source = settings
        expansion = dict(plan['expansion'][family])
        if plan.get('cap_below_dense', False):
            expansion['maximum'] = min(expansion['maximum'], n-1)
            expansion['start'] = min(expansion['start'], expansion['maximum'])
        require(manifest.get('reused_from') == report.get('reused_from'), f'Reuse provenance differs: {root}')
        row = dict(width=n, seed=seed, root=str(root), family=family, source_sha256=source_hash,
            numerical_source_sha256=numerical['sha256'], source_orders=source_orders,
            trajectories_sha256=archive_hash, bracket=search['bracket'], errors=report.get('errors', {}),
            search_limits=dict(expansion=plan['expansion'][family], effective_expansion=expansion,
                max_new_requests=plan.get('max_new_by_width', {}).get(str(n), plan['max_new_per_family']),
                seconds_per_fit=config['execution']['seconds_per_fit']),
            continuation_provenance=dict(restart_harmonic=restart,
                harmonic_fresh_setup=report.get('harmonic_fresh_setup'), reused_from=report.get('reused_from'),
                inherited_requested=search.get('inherited_requested', []), requested=search['requested']),
            candidates=[], selected=None, status=search['bracket']['status'])
        if family == 'legendre':
            row.pop('source_orders')
        if family == 'logarithmic' and source is not None:
            row['source_partition_boundaries'] = source['partitions']['new']['boundaries']
        with np.load(path/'trajectories.npz', allow_pickle=False) as arrays:
            require(report['data_sha256'] == manifest['identity']['data_sha256']
                    and all(array_sha(arrays[key]) == value for key, value in report['data_sha256'].items()),
                    f'Data hash mismatch: {root}')
            times, m = arrays['times_reference'], len(arrays['train_labels'])
            if family == 'logarithmic' and source is not None:
                require(source['training_count'] == m and source['passive_count'] == len(arrays['query_inputs']),
                        f'Compiled source panel differs from saved data: {root}')
            require(np.isfinite(times).all() and times[0] == 0 and np.all(np.diff(times) > 0)
                    and np.isclose(times[-1], config['training']['horizon']), f'Invalid time grid: {root}')
            require(common_times is None or np.array_equal(times, common_times), f'Time grids differ: {root}')
            common_times = times.copy()
            shape = (len(times), m+len(arrays['query_inputs']))

            def prediction(name):
                require(report['runs'].get(name, {}).get('complete')
                        and arrays[name].shape == shape and np.isfinite(arrays[name]).all()
                        and np.array_equal(arrays['times_'+name], times), f'Incomplete/invalid {name}: {root}')
                return arrays[name][:, m:].astype(float)

            reference = prediction('reference')
            row['reference_initial_state_sha256'] = report['reference_initial_state_sha256']
            row['paired_trajectory_sha256'] = {key: array_sha(arrays[key])
                                               for key in ('reference', f'dense_{n}')}
            require(report['seeds'][f'dense_{n}'] == _experiment_seed(seed, f'dense_{n}')
                    and report['seeds'][f'dense_{n}'] != seed, f'Dense-pair seed mismatch: {root}')
            baseline = np.sqrt(np.mean((prediction(f'dense_{n}')-reference)**2, axis=1))
            thresholds = np.array([baseline[-1], baseline.max()])
            require(np.all(thresholds > 0), f'Zero dense-pair benchmark: {root}')
            row['dense_pair'] = dict(endpoint_rms=float(thresholds[0]), worst_recorded_rms=float(thresholds[1]))
            for name, model in report['models'].items():
                if model['family'] != family:
                    continue
                candidate = dict(name=name, q=model['order' if family == 'legendre' else 'width'],
                    learned=model['moving'], fixed=model['fixed'], total=model['total'], status='inconclusive')
                require(candidate['total'] == candidate['learned']+candidate['fixed'], f'Storage mismatch: {root}/{name}')
                depth, dimension = config['model']['depth'], arrays['train_inputs'].shape[1]
                if family == 'legendre':
                    q = candidate['q']
                    require(isinstance(q, int) and not isinstance(q, bool) and q >= 1 and depth == 2
                            and config['model']['activation'] == 'tanh'
                            and candidate['learned'] == n*(dimension+1)+2*q*n*m+2*n*m+2
                            and candidate['fixed'] == n*n+2*q,
                            f'Invalid Legendre order, architecture or storage: {root}/{name}')
                else:
                    candidate['rank'] = model['source_rank']
                    q = min(model['width'], n)
                    if family in plan.get('rank_knots', {}):
                        knots = plan['rank_knots'][family]
                        require(candidate['rank'] == max(1, math.floor(np.interp(model['width'],
                            [k['width'] for k in knots], [k['source_rank'] for k in knots]))),
                            f'Candidate differs from the frozen rank schedule: {root}/{name}')
                    require(candidate['learned'] == (depth-1)*q*q+q*(dimension+1)+m
                            and candidate['fixed'] == (2*depth-1)*q*q+int(family == 'logarithmic')
                            and 0 < candidate['rank'] <= source_rank,
                            f'Invalid learned/fixed storage or source rank: {root}/{name}')
                if report['runs'].get(name, {}).get('complete'):
                    errors = np.sqrt(np.mean((prediction(name)-reference)**2, axis=1))
                    metrics = np.array([errors[-1], errors.max()])
                    candidate.update(status='pass' if np.all(metrics <= thresholds) else 'fail',
                        endpoint_rms=float(metrics[0]), worst_recorded_rms=float(metrics[1]),
                        endpoint_ratio=float(metrics[0]/thresholds[0]), worst_recorded_ratio=float(metrics[1]/thresholds[1]))
                row['candidates'].append(candidate)
        recorded = {candidate['name'] for candidate in row['candidates']}
        row['candidates'] += [dict(name=request['name'], q=request['order' if family == 'legendre' else 'width'],
            **({} if family == 'legendre' else dict(rank=request['source_rank'])),
            status='inconclusive', reason=report.get('errors', {}).get(request['name'], 'No completed model'))
            for request in search.get('inherited_requested', [])+search['requested'] if request['name'] not in recorded]
        passing = [candidate for candidate in row['candidates'] if candidate['status'] == 'pass']
        row['selected'] = min(passing, key=lambda candidate: candidate['q']) if passing else None
        if family == 'legendre':
            observations = {candidate['q']: candidate for candidate in row['candidates']}
            row['q1'] = observations.get(1)
            row['minimum_order_certified'] = bool(row['selected'] and all(
                observations.get(q, {}).get('status') == 'fail' for q in range(1, row['selected']['q'])))
            if row['status'] in ('minimum_order', 'resolved_local'):
                require(row['minimum_order_certified'], f'Untested/inconclusive order below selected minimum: {root}')
        _, checked_bracket = _budget_search_next({candidate['q']: candidate for candidate in row['candidates']},
                                                plan['width_tolerance'], **expansion)
        if report.get('search_complete') and checked_bracket['status'] in ('refining', 'expanding'):
            checked_bracket['status'] = 'evaluation_cap'
        row['recomputed_bracket'] = checked_bracket
        if report.get('search_complete') and row['status'] != 'source_inconclusive':
            require(search['bracket'] == checked_bracket, f'Recomputed accuracy bracket differs: {root}')
        if not report.get('search_complete'):
            row['status'] = 'search_incomplete'
        rows.append(row)
    widths, seeds = sorted({row['width'] for row in rows}), sorted({row['seed'] for row in rows})
    require(len(widths) >= 2 and len(seeds) == 3 and len(seen) == len(widths)*len(seeds),
            'Expected the same three seeds at every width, with at least two widths')
    require(all(n > 1 for n in widths), 'Dense widths must exceed one for logarithmic axes and fits')
    resolved_statuses = ('minimum_order', 'resolved_local') if family == 'legendre' else ('resolved_local',)
    groups = []
    for n in widths:
        selected = [row for row in rows if row['width'] == n]
        complete = all(row['selected'] is not None and row['status'] in resolved_statuses
                       and (family != 'legendre' or row['minimum_order_certified']) for row in selected)
        values = [row['selected']['learned'] for row in selected if row['selected'] is not None]
        groups.append(dict(width=n, expected=3, available=len(values), complete=complete, learned_values=values,
            mean=float(np.mean(values)) if complete else None, sample_sd=float(np.std(values, ddof=1)) if complete else None,
            median=float(np.median(values)) if complete else None))
    unresolved = [f"n={row['width']}, seed {row['seed']}: {row['status']}" for row in rows
                  if row['selected'] is None or row['status'] not in resolved_statuses
                  or (family == 'legendre' and not row['minimum_order_certified'])]
    descriptive_fits = {}
    for statistic in ('mean', 'median'):
        fit = dict(status='not_requested',
            model=('learned_storage = C * width ** p' if args.fit_width_powers
                   else 'learned_storage = C * (natural_log(width)) ** p'),
            criterion='unweighted least squares of log(aggregated learned storage) against '
                      + ('log(width)' if args.fit_width_powers else 'log(log(width))'),
            aggregation='arithmetic mean' if statistic == 'mean' else 'median',
            requested_widths=widths, fitted_widths=[],
            incomplete_widths=[group['width'] for group in groups if not group['complete']],
            scope='Descriptive finite-range fit; no uncertainty or asymptotic scaling claim')
        descriptive_fits[statistic] = fit
        if not (args.fit_log_powers or args.fit_width_powers):
            continue
        fit['status'] = 'incomplete_widths' if unresolved else 'insufficient_widths'
        if unresolved or len(widths) < 3:
            continue
        storage = np.asarray([group[statistic] for group in groups], dtype=float)
        require(np.isfinite(storage).all() and np.all(storage > 0), 'Invalid aggregated learned storage')
        fit_coordinates = np.log(np.asarray(widths, dtype=float))
        if not args.fit_width_powers:
            fit_coordinates = np.log(fit_coordinates)
        design = np.column_stack((np.ones(len(widths)), fit_coordinates))
        log_constant, exponent = np.linalg.lstsq(design, np.log(storage), rcond=None)[0]
        residuals = np.log(storage)-design@np.array([log_constant, exponent])
        fit.update(status='fitted', fitted_widths=widths, count=len(widths),
            C=float(np.exp(log_constant)), p=float(exponent), log_C=float(log_constant),
            log_space_rms=float(np.sqrt(np.mean(residuals**2))), log_residuals=residuals.tolist())
    args.out.mkdir(parents=True, exist_ok=False)
    search_caption = ('Exact positive integer order search; every lower order must be a completed accuracy failure.'
                      if family == 'legendre' else '20% local width brackets.')
    scope = ((f'Smallest passing Legendre orders, certified by completed failures at every lower positive integer; '
              'both endpoint and maximum-recorded query RMS meet their paired dense benchmarks. '
              if family == 'legendre' else
              f'Smallest tested passing {family_label} models; 20% local width brackets, not confidence intervals or global minima. ')
             + 'Three initialization seeds on fixed data; finite Euler trajectories. '
             + ((('Descriptive C*n^p fits' if args.fit_width_powers else 'Descriptive C(log n)^p fits')
                 + ' use natural logs and require all supplied widths complete; '
                 'no uncertainty or asymptotic scaling claim.')
                if args.fit_log_powers or args.fit_width_powers else 'No exponent fitted.'))
    fit_key = 'descriptive_width_power_fits' if args.fit_width_powers else 'descriptive_log_power_fits'
    save_json(args.out/'metrics.json', dict(scope=scope, family=family, common=common,
        **({} if family == 'legendre' else dict(compiled_source=common_source,
                                               source_orders_by_width=source_orders_by_width)),
        numerical_sources=numerical_sources,
        recorded_times=common_times.tolist(), individuals=rows, groups=groups,
        **{fit_key: descriptive_fits}, unresolved=unresolved))
    continuation_caption = ''.join(
        f"The search at dense width {row['width']}, seed {row['seed']}, was extended with user approval "
        f"to compact-width cap {row['search_limits']['effective_expansion']['maximum']} and at most "
        f"{row['search_limits']['max_new_requests']} additional fits; other searches retain their original limits.\n"
        for row in rows if family == 'harmonic' and not row['continuation_provenance']['restart_harmonic']
        and row['continuation_provenance']['inherited_requested'])
    if family == 'legendre':
        source_caption = ('Moving storage is n(d+1)+2qnm+2nm+2; additional fixed storage is n^2+2q, '
                          'including the initial dense hidden mixer.\n')
    else:
        source_caption = ('Common spatial degree '+str(common['search']['source_orders']['spatial_degree'])+', '
                          if family == 'harmonic' else 'Residual-clock partitions rebuilt per seed; common ')
        source_caption += f"temporal degree {common['setup']['time_degree']}; source rank caps by dense width: "+', '.join(
            f"{n}: {source_orders_by_width[n]['source_max_rank']}" for n in widths)+'.\n'
    (args.out/'captions.txt').write_text(scope+'\n'+source_caption
        + continuation_caption
        + 'Faint curves: individual seeds. Blue squares: arithmetic mean. Orange diamonds: median.\n'
        + ('Mean and median are computed from learned storage. '
           'Sample SD is recorded in metrics.json; group summaries require all three certified minimum orders.\n'
           if family == 'legendre' else
           'Mean and median are computed from learned storage, not compact widths. '
           'Sample SD is recorded in metrics.json; group summaries require all three resolved crossings.\n')
        + 'The companion mean/median panels use logarithmic width and learned-storage axes. '
        'Dashed curves, when available, are descriptive fits, not uncertainty bands.\n'
        + ''.join(f"{statistic} fit: "+(f"C={fit['C']:.9g}, p={fit['p']:.9g}, "
            f"log-space RMS residual={fit['log_space_rms']:.9g}" if fit['status'] == 'fitted'
            else fit['status'])+'\n' for statistic, fit in descriptive_fits.items()))
    figure, axis = plt.subplots(figsize=(7.3, 4.8))
    for seed in seeds:
        samples = sorted((row for row in rows if row['seed'] == seed), key=lambda row: row['width'])
        axis.plot(widths, [row['selected']['learned'] if row['selected'] else np.nan for row in samples],
                  'o-', alpha=.35, linewidth=1.2, label=f'Seed {seed}')
    axis.plot(widths, [group['mean'] if group['complete'] else np.nan for group in groups],
              's-', color='#185b84', linewidth=2.5, markersize=7, label='Arithmetic mean')
    axis.plot(widths, [group['median'] if group['complete'] else np.nan for group in groups],
              'D--', color='#b75c22', linewidth=2, markersize=6, label='Median')
    axis.set(xscale='log', yscale='log', xlabel='Dense width n', ylabel='Learned state',
             title=f'{family_label}: three seeds')
    axis.set_xticks(widths, [str(n) for n in widths])
    axis.xaxis.set_minor_formatter(NullFormatter())
    axis.grid(alpha=.2)
    axis.legend(fontsize=8)
    figure.text(.02, .02, search_caption
                + ('\nUnresolved (group summaries withheld): '+ '; '.join(unresolved) if unresolved else ''), fontsize=8)
    figure.tight_layout(rect=(0, .08 if unresolved else .05, 1, 1))
    for extension in ('png', 'pdf'):
        figure.savefig(args.out/f'learned_state_by_seed.{extension}', dpi=180)
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(11.2, 4.6), sharey=True)
    for axis, statistic, label, color, marker in zip(axes, ('mean', 'median'),
            ('Arithmetic mean', 'Median'), ('#185b84', '#b75c22'), ('s', 'D')):
        for index, seed in enumerate(seeds):
            samples = sorted((row for row in rows if row['seed'] == seed), key=lambda row: row['width'])
            axis.plot(widths, [row['selected']['learned'] if row['selected'] else np.nan for row in samples],
                'o-', color='#777777', alpha=.25, linewidth=1, markersize=3,
                label='Individual seeds' if index == 0 else None)
        axis.plot(widths, [group[statistic] if group['complete'] else np.nan for group in groups],
                  marker+'-', color=color, linewidth=2, markersize=6, label=f'Observed {label.lower()}')
        fit = descriptive_fits[statistic]
        if fit['status'] == 'fitted':
            fit_grid = np.geomspace(min(widths), max(widths), 150)
            fit_values = fit_grid if args.fit_width_powers else np.log(fit_grid)
            fit_label = (rf"Fit: $n^{{{fit['p']:.3f}}}$" if args.fit_width_powers
                         else rf"Fit: $(\log n)^{{{fit['p']:.3f}}}$")
            axis.plot(fit_grid, fit['C']*fit_values**fit['p'], '--', color=color, linewidth=1.8,
                      label=fit_label)
        axis.set(xscale='log', yscale='log', xlabel='Dense width n',
                 title='Mean' if statistic == 'mean' else 'Median')
        axis.set_xticks(widths, [str(n) for n in widths])
        axis.xaxis.set_minor_formatter(NullFormatter())
        axis.tick_params(axis='x', labelsize=9)
        axis.grid(alpha=.2)
        axis.legend(fontsize=8, frameon=False)
    axes[0].set_ylabel('Learned state')
    figure.suptitle(f'{family_label}: three seeds')
    footer = ('Exact integer order search; descriptive finite-range summaries.' if family == 'legendre'
              else '20% local width brackets; descriptive finite-range summaries.')
    if (args.fit_log_powers or args.fit_width_powers) and descriptive_fits['mean']['status'] != 'fitted':
        footer += ' Fits withheld: '+descriptive_fits['mean']['status'].replace('_', ' ')+'.'
    if unresolved:
        footer += '\nIncomplete groups have no mean or median; see metrics.json for every unresolved run.'
    figure.text(.02, .02, footer, fontsize=8)
    figure.tight_layout(rect=(0, .10 if unresolved else .06, 1, .96))
    for extension in ('png', 'pdf'):
        figure.savefig(args.out/f'learned_state_mean_median.{extension}', dpi=180)
    plt.close(figure)
    if family == 'legendre' and not unresolved:
        orders = np.asarray([[next(row['selected']['q'] for row in rows
                                   if row['seed'] == seed and row['width'] == n)
                              for n in widths] for seed in seeds])
        figure, axis = plt.subplots(figsize=(7.3, 4.5))
        if np.all(orders == orders[0]):
            axis.plot(widths, orders[0], 'o-', color='#185b84', linewidth=2,
                      markersize=7, label='All three seeds')
        else:
            for index, values in enumerate(orders):
                axis.plot(widths, values, 'o-', color='#777777', alpha=.3,
                          label='Individual seeds' if index == 0 else None)
            axis.plot(widths, orders.mean(axis=0), 's-', color='#185b84', label='Mean')
            axis.plot(widths, np.median(orders, axis=0), 'D--', color='#b75c22', label='Median')
        axis.set(xscale='log', yscale='linear', xlabel='Dense width $n$',
                 ylabel='Minimum order $q$', title='Legendre: minimum order',
                 ylim=(max(0, orders.min()-.35), orders.max()+.35))
        axis.set_xticks(widths, [str(n) for n in widths])
        axis.set_yticks(range(int(orders.min()), int(orders.max())+1))
        axis.xaxis.set_minor_formatter(NullFormatter())
        axis.grid(alpha=.2)
        axis.legend(frameon=False)
        figure.tight_layout()
        for extension in ('png', 'pdf'):
            figure.savefig(args.out/f'minimum_order.{extension}', dpi=180)
        plt.close(figure)
    print(json.dumps(dict(event='budget_seed_plot', output=str(args.out), unresolved=unresolved)), flush=True)
    return 0


def trajectory_budget_plot(argv):
    """Rescore saved paired Digits trajectories with no separate endpoint test."""
    import csv
    import shlex
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter
    parser = argparse.ArgumentParser(description=trajectory_budget_plot.__doc__)
    parser.add_argument('--metrics', nargs=2, type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--fit-polylog', action='store_true',
                        help='Overlay descriptive C*(log n)^a fits to Logarithmic mean/median storage')
    parser.add_argument('--compare-exponents', nargs='+', type=float, default=[],
                        help='Overlay fixed polylog exponents with independently fitted prefactors')
    parser.add_argument('--hide-legendre', action='store_true', help='Show only Logarithmic storage')
    parser.add_argument('--y-scale', choices=('log', 'linear'), default='log')
    args = parser.parse_args(argv)
    if args.compare_exponents and (not args.fit_polylog
            or any(not math.isfinite(a) or a <= 0 for a in args.compare_exponents)):
        parser.error('--compare-exponents requires --fit-polylog and positive finite exponents')

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    inputs = [json.loads(path.read_text()) for path in args.metrics]
    require({item['family'] for item in inputs} == {'legendre', 'logarithmic'},
            'Supply one Legendre and one Logarithmic audit')
    audits = {item['family']: item for item in inputs}
    indexed = {family: {(row['width'], row['seed']): row for row in audit['individuals']}
               for family, audit in audits.items()}
    keys = set(indexed['legendre'])
    widths, seeds = sorted({n for n, _ in keys}), sorted({seed for _, seed in keys})
    require(len(widths) == 6 and len(seeds) == 3 and len(keys) == 18
            and keys == {(n, seed) for n in widths for seed in seeds}
            and keys == set(indexed['logarithmic'])
            and all(len(audit['individuals']) == 18 for audit in inputs),
            'Expected the same six widths and three seeds without duplicate rows')
    left, right = audits['legendre'], audits['logarithmic']
    require(all(left['common'][key] == right['common'][key]
                for key in ('dataset', 'training', 'model', 'data_sha256', 'tf32'))
            and left['recorded_times'] == right['recorded_times'],
            'Data, model, precision, training or recorded times differ')
    require(left['common']['dataset']['name'] == 'digits'
            and left['common']['dataset']['digit_pair'] == [1, 7]
            and left['common']['dataset']['train_samples'] == 8
            and left['common']['dataset']['test_samples'] == 30
            and len(left['recorded_times']) == 65,
            'Expected Digits 1 vs 7, eight training and thirty query inputs, 65 times')
    require(all(order == dict(time_degree=8, source_max_rank=32)
                for order in right['source_orders_by_width'].values()),
            'Expected the unchanged Logarithmic degree-eight, rank-32 source cap')
    for key in sorted(keys):
        a, b = indexed['legendre'][key], indexed['logarithmic'][key]
        require(all(field in a and field in b and a[field] == b[field] for field in
                    ('reference_initial_state_sha256', 'paired_trajectory_sha256', 'dense_pair')),
                f'Paired initialization, trajectory hashes or dense benchmarks differ: {key}')

    rows = []
    for family in ('legendre', 'logarithmic'):
        for key in sorted(keys):
            old = indexed[family][key]
            n, seed = key
            root = Path(old['root'])
            manifest = json.loads((root/'run.json').read_text())
            path = (root/manifest['repetitions'][str(seed)]).resolve()
            require(path.is_relative_to(root.resolve()) and path != root.resolve(),
                    f'Invalid repetition path: {root}')
            report = json.loads((path/'report.json').read_text())
            archive = path/'trajectories.npz'
            require(sha(archive.read_bytes()) == old['trajectories_sha256']
                    == report['trajectories_sha256'], f'Changed trajectory archive: {root}')
            require(sha((root/'source.py').read_bytes()) == old['source_sha256']
                    == manifest['source_sha256'] == report['source_sha256']
                    and report['reference_initial_state_sha256'] == old['reference_initial_state_sha256'],
                    f'Changed producer or initialization: {root}')
            row = dict(family=family, width=n, seed=seed, root=str(root),
                trajectories_sha256=old['trajectories_sha256'], source_sha256=old['source_sha256'],
                paired_trajectory_sha256=old['paired_trajectory_sha256'],
                reference_initial_state_sha256=old['reference_initial_state_sha256'],
                prior_search_status=old['status'], prior_joint_selected=old['selected'],
                candidates=[])
            with np.load(archive, allow_pickle=False) as arrays:
                require(all(array_sha(arrays[name]) == value
                            for name, value in left['common']['data_sha256'].items()),
                        f'Changed data arrays: {root}')
                times = arrays['times_reference']
                require(np.array_equal(times, left['recorded_times']), f'Changed time grid: {root}')
                m = len(arrays['train_labels'])
                shape = (len(times), m+len(arrays['query_inputs']))
                require(m == 8 and shape == (65, 38), f'Unexpected scored panel: {root}')

                def prediction(name):
                    require(report['runs'].get(name, {}).get('complete')
                            and arrays[name].shape == shape and np.isfinite(arrays[name]).all()
                            and np.array_equal(arrays['times_'+name], times),
                            f'Incomplete or invalid trajectory: {root}/{name}')
                    return arrays[name].astype(float)

                require(all(array_sha(arrays[name]) == value
                            for name, value in old['paired_trajectory_sha256'].items()),
                        f'Changed paired trajectories: {root}')
                reference = prediction('reference')
                dense_error = prediction(f'dense_{n}')-reference
                dense_rms = np.sqrt(np.mean(dense_error[:, m:]**2, axis=1))
                dense_panel_max = float(np.abs(dense_error).max())
                require(dense_rms[-1] > 0 and dense_rms.max() > 0 and dense_panel_max > 0,
                        f'Zero dense benchmark: {root}')
                require(np.allclose([dense_rms[-1], dense_rms.max()],
                    [old['dense_pair']['endpoint_rms'], old['dense_pair']['worst_recorded_rms']],
                    rtol=1e-12, atol=0), f'Changed dense RMS benchmark: {root}')
                row['dense_pair'] = dict(old['dense_pair'], panel_max_abs=dense_panel_max)
                require({name for name, model in report['models'].items() if model['family'] == family}
                        <= {point['name'] for point in old['candidates']},
                        f'Prior audit omitted a saved candidate: {root}')
                for point in old['candidates']:
                    candidate = dict(point, prior_joint_status=point['status'],
                        status='inconclusive', panel_status='inconclusive')
                    if report['runs'].get(point['name'], {}).get('complete'):
                        error = prediction(point['name'])-reference
                        errors = np.sqrt(np.mean(error[:, m:]**2, axis=1))
                        metrics = np.array([errors[-1], errors.max()])
                        require(np.allclose(metrics, [point['endpoint_rms'], point['worst_recorded_rms']],
                                            rtol=1e-12, atol=0),
                                f'Prior candidate RMS differs: {root}/{point["name"]}')
                        require(point['status'] == ('pass' if np.all(
                            metrics <= [dense_rms[-1], dense_rms.max()]) else 'fail'),
                            f'Prior joint status differs: {root}/{point["name"]}')
                        model = report['models'][point['name']]
                        require(point['learned'] == model['moving']
                                and point['fixed'] == model['fixed']
                                and point['total'] == point['learned']+point['fixed'] == model['total'],
                                f'Prior storage differs: {root}/{point["name"]}')
                        panel_max = float(np.abs(error).max())
                        candidate.update(status='pass' if errors.max() <= dense_rms.max() else 'fail',
                            endpoint_rms=float(errors[-1]), worst_recorded_rms=float(errors.max()),
                            endpoint_ratio=float(errors[-1]/dense_rms[-1]),
                            worst_recorded_ratio=float(errors.max()/dense_rms.max()),
                            panel_max_abs=panel_max, panel_max_ratio=panel_max/dense_panel_max,
                            panel_status='pass' if panel_max <= dense_panel_max else 'fail')
                    else:
                        require(point['status'] == 'inconclusive',
                                f'Previously scored trajectory is incomplete: {root}/{point["name"]}')
                    row['candidates'].append(candidate)
            for field, status in (('selected', 'status'), ('panel_selected', 'panel_status')):
                passing = [point for point in row['candidates'] if point[status] == 'pass']
                row[field] = min(passing, key=lambda point: (point['learned'], point['q'], point['name'])) if passing else None
            prior = row['prior_joint_selected']
            joint = [point for point in row['candidates'] if point['prior_joint_status'] == 'pass']
            require(prior is not None and joint and prior['name'] == min(
                joint, key=lambda point: (point['learned'], point['q'], point['name']))['name'],
                f'Prior joint selection differs: {root}')
            row['deltas_from_prior_joint'] = {field: dict(
                q=row[field]['q']-prior['q'], learned=row[field]['learned']-prior['learned'],
                learned_fraction=row[field]['learned']/prior['learned']-1)
                if row[field] else None for field in ('selected', 'panel_selected')}
            rows.append(row)
    groups = {}
    for selection in ('prior_joint_selected', 'selected', 'panel_selected'):
        groups[selection] = {}
        for family in ('legendre', 'logarithmic'):
            groups[selection][family] = []
            for n in widths:
                values = [row[selection]['learned'] for row in rows
                          if row['family'] == family and row['width'] == n and row[selection]]
                groups[selection][family].append(dict(width=n, available=len(values), learned_values=values,
                    mean=float(np.mean(values)) if len(values) == len(seeds) else None,
                    median=float(np.median(values)) if len(values) == len(seeds) else None))
    fits = None
    if args.fit_polylog:
        fits = {}
        x = np.log(np.log(np.asarray(widths, dtype=float)))
        for statistic in ('mean', 'median'):
            values = [group[statistic] for group in groups['selected']['logarithmic']]
            require(all(value is not None and value > 0 for value in values),
                    'Polylog fit requires all six positive aggregate storage values')
            y = np.log(np.asarray(values, dtype=float))
            exponent, intercept = np.polyfit(x, y, 1)
            residual = y-(intercept+exponent*x)
            variance = float(np.sum((y-y.mean())**2))
            fits[statistic] = dict(exponent=float(exponent), coefficient=float(np.exp(intercept)),
                log_space_r2=1-float(residual@residual)/variance if variance > 0 else None,
                widths=widths, storage=values, model='C*(log(n))^a',
                objective='unweighted least squares in log(storage) versus log(log(n))',
                scope='Descriptive finite-range fit to smallest tested passing budgets; not an asymptotic claim')
            if args.compare_exponents:
                fits[statistic]['fixed_exponent_comparisons'] = []
                for fixed in args.compare_exponents:
                    fixed_intercept = float(np.mean(y-fixed*x))
                    residual = y-(fixed_intercept+fixed*x)
                    fits[statistic]['fixed_exponent_comparisons'].append(dict(
                        exponent=fixed, coefficient=float(np.exp(fixed_intercept)),
                        log_space_r2=1-float(residual@residual)/variance if variance > 0 else None))
    caption = ('Digits 1 vs 7, six dense widths, three initialization seeds and unchanged paired dense '
        'trajectories. Selection minimizes learned storage among saved completed candidates whose maximum '
        'over 65 recorded times of RMS error on 30 query inputs is at most the corresponding dense-pair '
        'maximum RMS. There is no separate endpoint test. Solid curves show arithmetic mean and median '
        'of selected learned storage; faint curves show individual seeds. These are smallest tested '
        'passing states, not new searches or certified global minima. Fixed storage and offline source '
        'costs are additional. Logarithmic sources retain temporal degree 8 and maximum rank 32. '
        'No model was retrained. The separately recorded panel diagnostic '
        'compares maximum absolute error over all 65 times and 38 training-plus-query inputs to the '
        'same dense-pair maximum; its independently normalized criterion is not equivalent to RMS. '
        'Neither recorded-grid criterion certifies continuous time or unseen inputs.\n')
    caption += ('Dashed curves fit C*(log n)^a to Logarithmic storage by unweighted least squares '
        'in log storage versus log log n, over all six widths. Fits are descriptive, not asymptotic '
        'or minimum-budget guarantees. ' + '; '.join(
            f'{statistic}: a={fit["exponent"]:.6f}, log-space R^2={fit["log_space_r2"]:.6f}'
            for statistic, fit in fits.items()) + '.\n') if fits else 'No exponent was fitted.\n'
    if args.compare_exponents:
        caption += ('Additional dashed curves fix the exponent and independently optimize each '
            'prefactor under the same log-space least-squares objective; they are not anchored '
            'arbitrarily to an endpoint. ' + '; '.join(
                f'{statistic}, a={fit["exponent"]:g}: C={fit["coefficient"]:.9g}, '
                f'log-space R^2={fit["log_space_r2"]:.6f}'
                for statistic, values in fits.items()
                for fit in values['fixed_exponent_comparisons']) + '.\n')
    caption += (f'The x-axis is logarithmic and the y-axis is {args.y_scale}. '
                f'Legendre is {"hidden" if args.hide_legendre else "shown"}; '
                'axis choices do not change data, selection or fit objectives.\n')
    args.out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).read_bytes()
    (args.out/'source.py').write_bytes(source)
    provenance = dict(argv=['trajectory-budget-plot', *argv], cwd=os.getcwd(),
        source_path=str(Path(__file__).resolve()), source_sha256=sha(source), python=sys.version,
        numpy=np.__version__, matplotlib=matplotlib.__version__,
        command=shlex.join([sys.executable, '-B', str(Path(__file__).resolve()), 'trajectory-budget-plot', *argv]))
    save_json(args.out/'config.json', provenance)
    save_json(args.out/'metrics.json', dict(scope=caption.strip(), widths=widths, seeds=seeds,
        primary_criterion='max_time query_RMS / max_time dense_pair_query_RMS <= 1; no endpoint test',
        diagnostic_criterion='max_time_and_panel absolute_error / max_time_and_panel dense_pair_absolute_error <= 1',
        inputs=[dict(path=str(path.resolve()), sha256=sha(path.read_bytes())) for path in args.metrics],
        common=left['common'], recorded_times=left['recorded_times'],
        logarithmic_source_orders_by_width=right['source_orders_by_width'],
        paired_checks='Exact paired trajectory and initialization hashes, data/model/training/time contracts; '
            'every archive/producer hash and every completed candidate RMS recomputed against prior audit',
        individuals=rows, groups=groups, provenance=provenance, exponent_fit=fits, training_rerun=False))
    (args.out/'captions.txt').write_text(caption)
    with (args.out/'selection_table.csv').open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['family', 'width', 'seed', 'prior_joint_q', 'prior_joint_learned',
            'trajectory_rms_q', 'trajectory_rms_learned', 'trajectory_rms_ratio',
            'selected_panel_max_ratio', 'panel_max_q', 'panel_max_learned', 'learned_delta'])
        for row in rows:
            prior, selected, panel = row['prior_joint_selected'], row['selected'], row['panel_selected']
            writer.writerow([row['family'], row['width'], row['seed'], prior['q'], prior['learned'],
                *([selected['q'], selected['learned'], selected['worst_recorded_ratio'],
                   selected['panel_max_ratio']] if selected else [None]*4),
                *([panel['q'], panel['learned']] if panel else [None]*2),
                selected['learned']-prior['learned'] if selected else None])
    figure, axes = plt.subplots(1, 2, figsize=(10.5, 4.6), sharex=True, sharey=True)
    for axis, statistic in zip(axes, ('mean', 'median')):
        for family, color, marker in (('legendre', '#185b84', 's'), ('logarithmic', '#228833', 'o')):
            if args.hide_legendre and family == 'legendre':
                continue
            points = {(row['width'], row['seed']): row['selected'] for row in rows if row['family'] == family}
            for seed in seeds:
                axis.plot(widths, [points[n, seed]['learned'] if points[n, seed] else np.nan for n in widths],
                          color=color, alpha=.20, linewidth=.9)
            axis.plot(widths, [group[statistic] if group[statistic] is not None else np.nan
                for group in groups['selected'][family]], color=color, marker=marker,
                linewidth=2, markersize=5, label=family.capitalize())
        if fits:
            fit = fits[statistic]
            grid = np.geomspace(widths[0], widths[-1], 250)
            axis.plot(grid, fit['coefficient']*np.log(grid)**fit['exponent'],
                      color='#333333', linestyle='--', linewidth=1.7,
                      label=rf'Fit: $(\log n)^{{{fit["exponent"]:.2f}}}$', zorder=4)
            for i, comparison in enumerate(fit.get('fixed_exponent_comparisons', [])):
                axis.plot(grid, comparison['coefficient']*np.log(grid)**comparison['exponent'],
                          color=('#d97706', '#9b4897')[i % 2],
                          linestyle=(0, (6, 3)) if i % 2 == 0 else (0, (2, 2)), linewidth=1.6,
                          label=rf'Fixed: $(\log n)^{{{comparison["exponent"]:g}}}$', zorder=3)
        axis.set(xscale='log', yscale=args.y_scale, xlabel='Dense width n', title=statistic.capitalize())
        if args.y_scale == 'linear':
            axis.set_ylim(bottom=0)
            axis.yaxis.set_major_formatter('{x:,.0f}')
        axis.set_xticks(widths, [str(n) for n in widths])
        axis.xaxis.set_minor_formatter(NullFormatter())
        axis.tick_params(axis='x', labelsize=8)
        axis.grid(alpha=.2)
        axis.legend(fontsize=9, frameon=False)
    axes[0].set_ylabel('Learned scalars')
    figure.suptitle('Digits 1 vs 7')
    figure.text(.02, .02, 'Trajectory RMS only; smallest tested passing states. Fixed storage excluded.', fontsize=9)
    figure.tight_layout(rect=(0, .06, 1, .95))
    for extension in ('png', 'pdf'):
        figure.savefig(args.out/f'learned_state_comparison.{extension}', dpi=180)
    plt.close(figure)
    print(json.dumps(dict(event='trajectory_budget_plot', output=str(args.out),
        changed_selections=sum(row['selected']['name'] != row['prior_joint_selected']['name']
                               for row in rows if row['selected']))), flush=True)
    return 0


def figure3_extended_plot(argv):
    """Plot the saved sphere and extended Digits learned-budget curves."""
    import shlex
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    parser = argparse.ArgumentParser(description=figure3_extended_plot.__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    config = json.loads(args.config.read_text())
    previous_path = Path(config['previous_figure'])
    previous = json.loads(previous_path.read_text())
    sphere, sphere_summaries = previous['figure3']['sphere'], previous['figure3']['sphere_dense_summaries']
    old = {point['name']: point for point in previous['figure3']['images']}
    old_summaries = previous['figure3']['image_dense_summaries']
    root = Path(config['reference_run'])
    manifest = json.loads((root/'run.json').read_text())
    reference_path = root/manifest['repetitions']['903']
    reference_report = json.loads((reference_path/'report.json').read_text())
    require(sha((reference_path/'trajectories.npz').read_bytes()) == reference_report['trajectories_sha256'],
            'Saved reference archive changed')
    with np.load(reference_path/'trajectories.npz', allow_pickle=False) as arrays:
        references = {key: arrays[key].copy() for key in ('reference', 'extra_reference', 'times_reference')}
    require(references['reference'].shape == (65, 38) and references['extra_reference'].shape == (65, 30)
            and np.array_equal(references['times_reference'], np.linspace(0, 32, 65))
            and all(np.isfinite(value).all() for value in references.values()), 'Invalid saved reference')
    require(all(array_sha(value) == previous['provenance']['image_dense_repeats']
                ['provenance']['reference_array_sha256'][key] for key, value in references.items()),
            'Previous figure used a different Digits reference')
    new, errors, inputs = {}, {}, []
    metric_names = ('endpoint_rms', 'worst_recorded_rms', 'extra_endpoint_rms', 'extra_worst_recorded_rms')
    for worker in ('dense', 'compressions'):
        folder = Path(config['output'])/worker
        report = json.loads((folder/'report.json').read_text())
        archive = folder/'trajectories.npz'
        require(report.get('finished') and report['config'] == config
                and report['source_sha256'] == sha((Path(config['output'])/'source.py').read_bytes())
                and report['original_trajectories_sha256'] == reference_report['trajectories_sha256'],
                f'{worker} is unfinished or its producer/configuration/reference changed')
        require(sha(archive.read_bytes()) == report['trajectories_sha256'], f'Changed {worker} archive')
        inputs.append(dict(worker=worker, path=str(folder.resolve()),
            report_sha256=sha((folder/'report.json').read_bytes()),
            trajectories_sha256=report['trajectories_sha256'], source_sha256=report.get('source_sha256')))
        errors.update(report.get('errors', {}))
        with np.load(archive, allow_pickle=False) as arrays:
            require(all(np.array_equal(arrays[key], value) for key, value in references.items()),
                    f'{worker} reference or time arrays changed')
            for name, model in report['models'].items():
                if not report['runs'].get(name, {}).get('complete'):
                    errors.setdefault(name, 'No completed trajectory')
                    continue
                require(name in report['metrics'], f'Missing completed model metrics: {name}')
                prediction, extra = arrays[name], arrays['extra_'+name]
                require(prediction.shape == (65, 38) and extra.shape == (65, 30)
                        and np.isfinite(prediction).all() and np.isfinite(extra).all()
                        and np.array_equal(arrays['times_'+name], references['times_reference']),
                        f'Invalid predictions or observation grid: {name}')
                rms = np.sqrt(np.mean((prediction[:, 8:].astype(float)
                                      -references['reference'][:, 8:].astype(float))**2, axis=1))
                extra_rms = np.sqrt(np.mean((extra.astype(float)
                                            -references['extra_reference'].astype(float))**2, axis=1))
                score = dict(zip(metric_names, map(float, (rms[-1], rms.max(), extra_rms[-1], extra_rms.max()))))
                require(all(np.isclose(score[key], report['metrics'][name][key], rtol=1e-12, atol=0)
                            for key in metric_names), f'Recomputed RMS differs: {name}')
                require(model['moving'] > 0 and model['fixed'] >= 0
                        and model['moving']+model['fixed'] == model['total'], f'Invalid storage: {name}')
                require(name not in new, f'Duplicate new model: {name}')
                new[name] = dict(model, name=name, **score)
    points, dense_summaries = [], {}
    for width in config['display_dense_widths']:
        name = f'dense_{width}'
        if width not in config['dense_widths']:
            point, summary = dict(old[name]), old_summaries[name]
        else:
            names = [f'{name}_seed{seed}' for seed in config['dense_seeds']]
            if not all(key in new for key in names):
                errors[name] = 'Three completed dense initializations are required for a mean'
                continue
            samples = [new[key] for key in names]
            require(all(point['moving'] == width*(width+65) and point['fixed'] == 0 for point in samples),
                    f'Wrong dense storage: {width}')
            summary = dict(width=width, moving=samples[0]['moving'], fixed=0,
                count=len(samples), names=names, samples=samples)
            for metric in metric_names:
                values = [point[metric] for point in samples]
                summary[metric] = dict(mean=float(np.mean(values)), sd=float(np.std(values, ddof=1)), values=values)
            point = dict(name=name, family='dense', width=width, moving=summary['moving'],
                fixed=0, total=summary['moving'], **{key: summary[key]['mean'] for key in metric_names})
        require(summary['count'] == 3, f'Dense group is not a three-seed mean: {width}')
        points.append(point)
        dense_summaries[name] = summary
    for family, field in (('legendre', 'display_legendre_orders'), ('low_rank', 'display_low_rank_ranks')):
        for value in config[field]:
            name = f'{family}_{value}'
            if name in new or name in old:
                points.append(dict(new.get(name, old.get(name))))
            else:
                errors.setdefault(name, 'No completed requested model')
    points.append(dict(old['frozen_features']))
    for budget in config['logarithmic_budgets']:
        name = f"logarithmic_{budget['width']}_r{budget['source_rank']}"
        if name in new:
            points.append(dict(new[name]))
        else:
            errors.setdefault(name, 'No completed rebuilt Taylor model')
    require(any(point['family'] == 'logarithmic' for point in points), 'No completed rebuilt Taylor points')
    styles = dict(legendre=('Legendre', '#4477AA', 's'), harmonic=('Harmonic', '#EE7733', '^'),
        logarithmic=('Taylor', '#228833', 'o'), dense=('Dense', '#666666', 'D'),
        low_rank=('Low rank', '#CC6677', 'v'), frozen_features=('Frozen features', '#AA4499', '*'))
    pair = old['dense_4096']['endpoint_rms']
    sphere_pair = next(point['endpoint_rms'] for point in sphere if point['name'] == 'dense')
    nonfrozen = [point['moving'] for point in sphere+points if point['family'] != 'frozen_features']
    limits = (min(nonfrozen)*.75, max(nonfrozen)*1.3)
    with plt.rc_context({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False,
                         'pdf.fonttype': 42, 'savefig.facecolor': 'white'}):
        figure, axes = plt.subplots(1, 2, figsize=(11.8, 4.8), sharex=True)
        for column, (axis, title, data, baseline) in enumerate(zip(axes,
                ('3D sphere', 'Digits 1 vs 7'), (sphere, points), (sphere_pair, pair))):
            for family, (label, color, marker) in styles.items():
                selected = sorted([point for point in data if point['family'] == family],
                                  key=lambda point: point['moving'])
                if not selected:
                    continue
                if family == 'frozen_features':
                    axis.axhline(selected[0]['endpoint_rms'], color=color, linestyle='--', linewidth=1, label=label)
                    continue
                axis.plot([point['moving'] for point in selected], [point['endpoint_rms'] for point in selected],
                          color=color, marker=marker, markersize=4.5, linewidth=1.2, label=label)
                for point in selected:
                    summary = (sphere_summaries if column == 0 else dense_summaries).get(point['name'])
                    if summary:
                        deviation = ([[summary['median']-summary['minimum']],
                                      [summary['maximum']-summary['median']]] if column == 0
                                     else summary['endpoint_rms']['sd'])
                        axis.errorbar(point['moving'], point['endpoint_rms'], yerr=deviation,
                                      fmt='none', color=color, capsize=3, linewidth=1)
                if column == 1 and family == 'logarithmic':
                    axis.plot([point['moving'] for point in selected],
                              [point['extra_endpoint_rms'] for point in selected], ':', marker=marker,
                              markerfacecolor='white', color=color, markersize=5, linewidth=1,
                              label='Taylor, undeclared')
            axis.axhline(baseline, color='#333333', linestyle=':', linewidth=1, label='Dense benchmark')
            if column == 1:
                axis.axhline(old['dense_4096']['extra_endpoint_rms'], color='#999999', linestyle='-.',
                             linewidth=.8, label='Dense, undeclared')
            axis.set(xscale='log', yscale='log', xlabel='Learned scalars', title=title, xlim=limits)
            axis.grid(alpha=.15)
        axes[0].set_ylabel('Endpoint query RMS')
        legend = {}
        for axis in axes:
            handles, labels = axis.get_legend_handles_labels()
            legend.update(zip(labels, handles))
        figure.legend(legend.values(), legend.keys(), loc='upper center', ncol=5, frameon=False, fontsize=9)
        figure.tight_layout(rect=(0, 0, 1, .84))
        args.out.mkdir(parents=True, exist_ok=False)
        for extension in ('png', 'pdf'):
            figure.savefig(args.out/f'figure3_accuracy.{extension}', dpi=180)
        plt.close(figure)
    caption = ('Figure 3. Endpoint query RMS against each fixed width-4096 reference versus learned scalars. '
        'Only the learned-storage row is shown; both panels share horizontal limits. The sphere points '
        'and conditional dense medians/min-max bars are unchanged. Digits dense points show means and '
        'sample SD across the existing repetition labels 903, 904, 905 against saved reference 903. '
        'Displayed dense widths are '+', '.join(map(str, config['display_dense_widths']))+'. '
        'Compression curves are single runs, without imposed monotonicity. All displayed Digits Taylor '
        'points use one rebuilt maximum-rank-64 source with degree 8 and the declared nested ranks; '
        'old maximum-rank-32 Taylor points are not mixed into this curve. Uniform selection uses 64 trials, '
        'condition cap 16 and the original readout floor; setup uses full-horizon RK4 rollouts, not a '
        'certified initialization-only compiler. Hollow Taylor markers score the 30 inputs withheld '
        'from source setup; query labels are unused. Dashed frozen-feature baselines carry no budget '
        'marker. The dense benchmark is the unchanged single sphere pair or three-control Digits mean. '
        'Digits use Euler step 1/160 through time 32, with 65 observations; sphere retains its prior '
        'step 1/640. Fixed retained storage is additional and remains in metrics: Digits Legendre '
        '4096^2+2*order; Taylor 3*width^2+1; low rank and frozen features 17039360 scalars. '
        'Common data, solver workspace and temporary source construction are excluded. No new dense '
        'reference or continuous-time certificate is claimed.\n')
    if errors:
        caption += 'Unplotted requests or constructor failures: '+json.dumps(errors, sort_keys=True)+'.\n'
    source = Path(__file__).read_bytes()
    (args.out/'source.py').write_bytes(source)
    (args.out/'config.json').write_bytes(args.config.read_bytes())
    (args.out/'captions.txt').write_text(caption)
    save_json(args.out/'metrics.json', dict(scope=caption.strip(), config=config,
        config_sha256=sha(args.config.read_bytes()), previous_figure=str(previous_path.resolve()),
        previous_figure_sha256=sha(previous_path.read_bytes()), inputs=inputs,
        reference_array_sha256={key: array_sha(value) for key, value in references.items()},
        figure3=dict(sphere=sphere, sphere_dense_summaries=sphere_summaries,
                     images=points, image_dense_summaries=dense_summaries),
        rescored_models=new, errors=errors, shared_learned_limits=list(limits),
        source_sha256=sha(source), command=shlex.join([sys.executable, '-B', str(Path(__file__).resolve()),
            'figure3-extended-plot', *argv]), cwd=str(Path.cwd()),
        plot_validation='New archive hashes, reference equality, 65-time prediction grids and all four raw RMS scores'))
    print(json.dumps(dict(event='figure3_extended_plot', output=str(args.out),
                         completed_new_models=len(new), errors=errors)), flush=True)
    return 0


def trajectory_task_plot(argv):
    """Mean learned storage on the saved circle and digits tasks, with one RMS criterion."""
    import shlex
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter
    parser = argparse.ArgumentParser(description=trajectory_task_plot.__doc__)
    parser.add_argument('--toy-metrics', nargs=3, type=Path, required=True,
                        metavar=('LEGENDRE', 'HARMONIC', 'LOGARITHMIC'))
    parser.add_argument('--digits-metrics', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    digits = json.loads(args.digits_metrics.read_text())
    audits = [json.loads(path.read_text()) for path in args.toy_metrics]
    widths = digits['widths']
    rows, pairs = [], {}
    for family, audit in zip(('legendre', 'harmonic', 'logarithmic'), audits):
        require(audit.get('family', 'harmonic') == family, 'Toy audits must be Legendre, Harmonic, Logarithmic')
        common = audit['common']
        require(common['dataset']['name'] == 'sphere' and common['dataset']['dimension'] == 2
                and common['dataset']['train_samples'] == 8 and common['dataset']['test_samples'] == 30,
                'Expected the earlier eight-training, thirty-query circle task')
        require(all(common[key] == audits[0]['common'][key] for key in
                    ('dataset', 'model', 'training', 'data_sha256', 'tf32'))
                and common['training'] == digits['common']['training']
                and audit['recorded_times'] == digits['recorded_times'], 'Task protocols differ')
        for old in audit['individuals']:
            n, seed, root = old['width'], old['seed'], Path(old['root'])
            manifest = json.loads((root/'run.json').read_text())
            path = root/manifest['repetitions'][str(seed)]
            report = json.loads((path/'report.json').read_text())
            require(sha((path/'trajectories.npz').read_bytes()) == old['trajectories_sha256']
                    == report['trajectories_sha256'], 'Toy trajectory archive changed')
            require(sha((root/'source.py').read_bytes()) == old['source_sha256']
                    == manifest['source_sha256'], 'Toy producer changed')
            candidates = []
            with np.load(path/'trajectories.npz', allow_pickle=False) as arrays:
                require(all(array_sha(arrays[key]) == value for key, value in common['data_sha256'].items()),
                        'Toy data changed')
                times, reference = arrays['times_reference'], arrays['reference'].astype(float)
                require(np.array_equal(times, audit['recorded_times']) and reference.shape == (65, 38),
                        'Toy observation grid differs')
                pair = {key: array_sha(arrays[key]) for key in ('reference', f'dense_{n}', 'times_reference')}
                require((n, seed) not in pairs or pairs[n, seed] == pair, 'Toy dense pairs differ across methods')
                pairs[n, seed] = pair
                for name in ('reference', f'dense_{n}'):
                    require(report['runs'][name]['complete'] and np.isfinite(arrays[name]).all()
                            and np.array_equal(arrays['times_'+name], times), 'Incomplete toy dense pair')
                dense_rms = float(np.sqrt(np.mean((arrays[f'dense_{n}'].astype(float)[:, 8:]
                                                  -reference[:, 8:])**2, axis=1)).max())
                require(dense_rms > 0 and np.isclose(dense_rms, old['dense_pair']['worst_recorded_rms'],
                                                   rtol=1e-12, atol=0), 'Toy benchmark changed')
                for point in old['candidates']:
                    name = point['name']
                    if not report['runs'].get(name, {}).get('complete'):
                        continue
                    prediction = arrays[name].astype(float)
                    require(prediction.shape == reference.shape and np.isfinite(prediction).all()
                            and np.array_equal(arrays['times_'+name], times), 'Invalid toy candidate')
                    rms = float(np.sqrt(np.mean((prediction[:, 8:]-reference[:, 8:])**2, axis=1)).max())
                    require(np.isclose(rms, point['worst_recorded_rms'], rtol=1e-12, atol=0)
                            and point['learned'] == report['models'][name]['moving']
                            and point['fixed'] == report['models'][name]['fixed'], 'Toy score/storage changed')
                    candidates.append(dict(point, worst_recorded_ratio=rms/dense_rms,
                                           trajectory_pass=rms <= dense_rms))
            passing = [point for point in candidates if point['trajectory_pass']]
            require(passing, f'No tested trajectory-RMS pass for {family}/{n}/{seed}')
            rows.append(dict(family=family, width=n, seed=seed, root=str(root),
                archive_sha256=old['trajectories_sha256'], paired_trajectory_sha256=pair,
                prior_joint_selected=old['selected'], selected=min(passing, key=lambda p: p['learned']),
                candidates=candidates))
    toy_groups, toy_seeds = {}, sorted({row['seed'] for row in rows})
    for family in ('legendre', 'harmonic', 'logarithmic'):
        subset = [row for row in rows if row['family'] == family]
        require(len(toy_seeds) == 3 and len(subset) == len(widths)*3
                and {(row['width'], row['seed']) for row in subset}
                    == {(n, seed) for n in widths for seed in toy_seeds}, 'Incomplete toy mean')
        toy_groups[family] = [dict(width=n, mean=float(np.mean([
            row['selected']['learned'] for row in subset if row['width'] == n]))) for n in widths]
    panels = [('Toy circle (d = 2)', toy_groups), ('Digits 1 vs 7 (d = 64)', digits['groups']['selected'])]
    fits = {}
    figure, axes = plt.subplots(1, 2, figsize=(11.5, 4.5), sharex=True, sharey=True)
    for axis, (title, groups) in zip(axes, panels):
        fits[title] = {}
        for family, color, marker in (('legendre', '#185b84', 's'),
                                      ('harmonic', '#dd8822', '^'), ('logarithmic', '#228833', 'o')):
            if family not in groups:
                continue
            values = np.array([group['mean'] for group in groups[family]])
            axis.plot(widths, values, color=color, marker=marker, linewidth=2,
                      markersize=5, label=family.capitalize())
            if family != 'legendre':
                x, y = np.log(np.log(np.asarray(widths, dtype=float))), np.log(values)
                exponent, intercept = np.polyfit(x, y, 1)
                fit = dict(exponent=float(exponent), coefficient=float(np.exp(intercept)),
                    log_space_r2=float(1-np.sum((y-intercept-exponent*x)**2)/np.sum((y-y.mean())**2)))
                fits[title][family] = fit
                grid = np.geomspace(widths[0], widths[-1], 250)
                axis.plot(grid, fit['coefficient']*np.log(grid)**fit['exponent'],
                          color=color if family == 'harmonic' else '#333333', linestyle='--', linewidth=1.5,
                          label=rf'{family.capitalize()} fit: $(\log n)^{{{exponent:.2f}}}$')
        axis.set(xscale='log', yscale='log', xlabel='Dense width n', title=title)
        axis.set_xticks(widths, [str(n) for n in widths])
        axis.xaxis.set_minor_formatter(NullFormatter())
        axis.tick_params(axis='x', labelsize=8)
        axis.grid(alpha=.2)
        axis.legend(fontsize=8, frameon=False)
    axes[0].set_ylabel('Mean learned scalars')
    figure.text(.02, .02, 'Three seeds; trajectory RMS ≤ dense–dense. Fixed storage excluded.', fontsize=9)
    figure.tight_layout(rect=(0, .06, 1, 1))
    args.out.mkdir(parents=True, exist_ok=False)
    for extension in ('png', 'pdf'):
        figure.savefig(args.out/f'learned_state_mean_tasks.{extension}', dpi=180)
    plt.close(figure)
    source = Path(__file__).read_bytes()
    (args.out/'source.py').write_bytes(source)
    caption = ('Mean learned storage across three independently coupled repetitions on each task. '
        'Both panels select the smallest tested completed model with maximum-recorded query RMS '
        'no greater than the same dense-pair maximum; no separate endpoint requirement. Toy runs '
        'are re-scored from their saved arrays; the digits panel is unchanged. All six widths are '
        'included. Dashed curves are unweighted log-space fits to C*(log n)^a, not asymptotic or '
        'optimal-budget guarantees. Fixed storage and full-horizon empirical rollout setup are '
        'additional; no new training or time-step refinement. Circle sources retain their original '
        'width-dependent Logarithmic rank caps and fixed Harmonic spatial/source settings.\n')
    (args.out/'captions.txt').write_text(caption)
    save_json(args.out/'metrics.json', dict(scope=caption.strip(), widths=widths,
        toy_seeds=toy_seeds, digits_seeds=digits['seeds'], toy_individuals=rows,
        toy_groups=toy_groups, digits_groups=digits['groups']['selected'], fits=fits,
        inputs=[dict(path=str(p.resolve()), sha256=sha(p.read_bytes()))
                for p in [*args.toy_metrics, args.digits_metrics]],
        source_sha256=sha(source), command=shlex.join([sys.executable, '-B', str(Path(__file__).resolve()),
            'trajectory-task-plot', *argv]), cwd=str(Path.cwd()), training_rerun=False))
    print(json.dumps(dict(event='trajectory_task_plot', output=str(args.out), fits=fits)), flush=True)
    return 0


def budget_comparison_plot(argv):
    """Compare paired six-width, three-seed Legendre and Logarithmic audits."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter
    parser = argparse.ArgumentParser(description=budget_comparison_plot.__doc__)
    parser.add_argument('--metrics', nargs=2, type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    inputs = [json.loads(path.read_text()) for path in args.metrics]
    require({item['family'] for item in inputs} == {'legendre', 'logarithmic'},
            'Supply one Legendre and one Logarithmic metrics file')
    audits = {item['family']: item for item in inputs}
    indexed = {family: {(row['width'], row['seed']): row for row in audit['individuals']}
               for family, audit in audits.items()}
    keys = set(indexed['legendre'])
    widths, seeds = sorted({n for n, _ in keys}), sorted({seed for _, seed in keys})
    require(len(widths) == 6 and len(seeds) == 3 and len(keys) == 18
            and keys == {(n, seed) for n in widths for seed in seeds}
            and keys == set(indexed['logarithmic'])
            and all(len(audit['individuals']) == 18 for audit in inputs),
            'Expected identical six widths and three seeds without duplicate rows')
    left, right = audits['legendre'], audits['logarithmic']
    require(all(left['common'][key] == right['common'][key]
                for key in ('dataset', 'training', 'model', 'data_sha256', 'tf32'))
            and left['recorded_times'] == right['recorded_times'],
            'Data, model, precision, training or recorded times differ')
    for key in sorted(keys):
        a, b = indexed['legendre'][key], indexed['logarithmic'][key]
        require(all(field in a and field in b and a[field] == b[field] for field in
                    ('reference_initial_state_sha256', 'paired_trajectory_sha256', 'dense_pair')),
                f'Reference initialization, paired trajectory hashes or benchmarks differ: {key}')
    groups, fits = {}, {}
    for family, audit in audits.items():
        groups[family] = []
        for n in widths:
            rows = [indexed[family][n, seed] for seed in seeds]
            selected = [row['selected'] for row in rows if row['selected'] is not None]
            require(all(point['status'] == 'pass' and np.isfinite(point['learned'])
                        and point['learned'] > 0 for point in selected), 'Invalid passing learned state')
            complete = len(selected) == 3 and all(
                row['status'] in (('minimum_order', 'resolved_local') if family == 'legendre'
                                  else ('resolved_local',))
                and (family != 'legendre' or row['minimum_order_certified']) for row in rows)
            values = [point['learned'] for point in selected]
            groups[family].append(dict(width=n, available=len(values), complete=complete,
                mean=float(np.mean(values)) if len(values) == 3 else None,
                median=float(np.median(values)) if len(values) == 3 else None,
                interpretation='resolved' if complete else 'passing witnesses; lower budgets unresolved'))
        fit_key = 'descriptive_width_power_fits' if family == 'legendre' else 'descriptive_log_power_fits'
        fits[family] = audit.get(fit_key, {})
    caption = ('Same six dense widths and three paired seeds; both endpoint and maximum-recorded query RMS '
        'meet their own 1x dense-pair benchmarks. Solid curves summarize learned storage; faint curves show '
        'individual smallest tested passing witnesses. Filled markers require three resolved searches; '
        'hollow markers summarize three passing witnesses with unresolved lower budgets. Groups missing a '
        'passing witness have no mean or median. Legendre uses exact integer minima; Logarithmic uses 20% '
        'local width brackets, not global minima. Fixed retained storage and offline source costs are additional. '
        'Dashed fits, when available, are descriptive and require all six groups resolved.\n')
    figure, axes = plt.subplots(1, 2, figsize=(11.2, 4.8), sharex=True, sharey=True)
    for axis, statistic in zip(axes, ('mean', 'median')):
        for family, color, marker in (('legendre', '#185b84', 's'), ('logarithmic', '#228833', 'o')):
            for seed in seeds:
                axis.plot(widths, [indexed[family][n, seed]['selected']['learned']
                    if indexed[family][n, seed]['selected'] else np.nan for n in widths],
                    color=color, alpha=.18, linewidth=.9)
            values = [group[statistic] if group[statistic] is not None else np.nan for group in groups[family]]
            axis.plot(widths, values, color=color, linewidth=2, label=family.capitalize())
            for complete in (True, False):
                points = [group for group in groups[family]
                          if group['complete'] == complete and group[statistic] is not None]
                axis.plot([group['width'] for group in points], [group[statistic] for group in points],
                    linestyle='none', marker=marker, color=color, markersize=6,
                    markerfacecolor=color if complete else 'white', markeredgewidth=1.5,
                    label='Lower budget unresolved' if points and not complete else None)
            fit = fits[family].get(statistic, {})
            if fit.get('status') == 'fitted' and all(group['complete'] for group in groups[family]):
                require(fit['fitted_widths'] == widths, 'Descriptive fit does not cover all six widths')
                grid = np.geomspace(min(widths), max(widths), 150)
                coordinate = grid if family == 'legendre' else np.log(grid)
                axis.plot(grid, fit['C']*coordinate**fit['p'], '--', color=color, alpha=.75, linewidth=1.2,
                          label=(rf"Legendre fit: $n^{{{fit['p']:.3f}}}$" if family == 'legendre'
                                 else rf"Logarithmic fit: $(\log n)^{{{fit['p']:.3f}}}$"))
        axis.set(xscale='log', yscale='log', xlabel='Dense width n', title=statistic.capitalize())
        axis.set_xticks(widths, [str(n) for n in widths])
        axis.xaxis.set_minor_formatter(NullFormatter())
        axis.tick_params(axis='x', labelsize=9)
        axis.grid(alpha=.2)
        axis.legend(fontsize=8, frameon=False)
    axes[0].set_ylabel('Learned scalars')
    dataset = left['common']['dataset']
    title = (f"Digits {dataset['digit_pair'][0]} vs {dataset['digit_pair'][1]}"
             if dataset['name'] == 'digits' else 'Legendre and Logarithmic')
    figure.suptitle(title+': three seeds')
    figure.text(.02, .02, 'Both 1x RMS criteria; fixed storage excluded. Hollow markers: unresolved lower budgets.', fontsize=8)
    figure.tight_layout(rect=(0, .06, 1, .95))
    args.out.mkdir(parents=True, exist_ok=False)
    for extension in ('png', 'pdf'):
        figure.savefig(args.out/f'learned_state_comparison.{extension}', dpi=180)
    plt.close(figure)
    save_json(args.out/'comparison.json', dict(scope=caption.strip(), widths=widths, seeds=seeds,
        inputs=[dict(path=str(path.resolve()), sha256=sha(path.read_bytes())) for path in args.metrics],
        paired_checks='data/model/training/time grids, initialization and trajectory hashes, dense RMS benchmarks',
        groups=groups, source_descriptive_fits=fits,
        fit_drawn={family: all(group['complete'] for group in groups[family]) and
            any(fit.get('status') == 'fitted' for fit in fits[family].values()) for family in audits}))
    (args.out/'captions.txt').write_text(caption)
    print(json.dumps(dict(event='budget_comparison_plot', output=str(args.out))), flush=True)
    return 0


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'figure3-extend':
        sys.exit(figure3_extend_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'figure3-extended-plot':
        sys.exit(figure3_extended_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'trajectory-task-plot':
        sys.exit(trajectory_task_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'logarithmic-order-probe':
        sys.exit(logarithmic_order_probe_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'trajectory-budget-plot':
        sys.exit(trajectory_budget_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'budget-comparison-plot':
        sys.exit(budget_comparison_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'budget-seed-plot':
        sys.exit(budget_seed_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'harmonic-order-probe':
        sys.exit(harmonic_order_probe_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'dense-control-repeats':
        sys.exit(dense_control_repeats_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'restored-paper-plot':
        sys.exit(restored_paper_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'feedback-pooled-transfer':
        sys.exit(feedback_pooled_transfer_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'feedback-scope-pilot':
        sys.exit(feedback_scope_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'feedback-conditioning-followup':
        sys.exit(feedback_conditioning_followup_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'feedback-conditioning':
        sys.exit(feedback_conditioning_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'feedback-control-check':
        print(json.dumps(feedback_control_checks(), indent=2))
        sys.exit(0)
    if len(sys.argv) > 1 and sys.argv[1] == 'feedback-dense-pairs':
        sys.exit(feedback_dense_pairs_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'appendix-sweep-plot':
        sys.exit(appendix_sweep_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'appendix-spectral':
        sys.exit(appendix_spectral_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'appendix-saved-plot':
        sys.exit(appendix_saved_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'appendix-transfer':
        sys.exit(appendix_transfer_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'paper-draft-plot':
        sys.exit(paper_draft_plot(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'refine-budgets':
        sys.exit(budget_search_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == 'scaling-plot':
        sys.exit(experiment_scaling_plot(sys.argv[2:]))
    if len(sys.argv) == 1 or sys.argv[1] in ('run', 'plot'):
        sys.exit(experiment_main(sys.argv[2:] if len(sys.argv) > 1 else [],
                                 action=sys.argv[1] if len(sys.argv) > 1 else 'run'))
    if len(sys.argv) > 1 and sys.argv[1] == 'compression-pilot':
        compression_pilot_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'validate':
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
    elif len(sys.argv) > 1 and sys.argv[1] == 'compression-sweep':
        sys.exit(compression_sweep_main(sys.argv[2:]))
    elif len(sys.argv) > 1 and sys.argv[1] == 'unified-case':
        unified_case_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'cubic-case':
        cubic_case_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'cubic-check':
        print(json.dumps(cubic_source_small_checks(), indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == 'cubic-summary':
        cubic_summary_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'cubic-budget':
        sys.exit(cubic_budget_main(sys.argv[2:]))
    elif len(sys.argv) > 1 and sys.argv[1] == 'sphere-points':
        sys.exit(sphere_points_main(sys.argv[2:]))
    elif len(sys.argv) > 1 and sys.argv[1] == 'sphere-points-plot':
        sphere_points_plot_main(sys.argv[2:])
    elif len(sys.argv) > 1 and sys.argv[1] == 'unified-check':
        torch.set_num_threads(1)
        torch.set_default_dtype(torch.float64)
        print(json.dumps(dict(legendre=legendre_smoke_test(), baselines=unified_baseline_checks(),
                              harmonic=unified_harmonic_source_checks()), indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == 'panel-span-check':
        torch.set_num_threads(1)
        torch.set_default_dtype(torch.float64)
        print(json.dumps(panel_span_small_checks(), indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == 'unified-plot':
        unified_plot_main(sys.argv[2:])
    else:
        main()
