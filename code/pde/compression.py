"""Numerical Dense, Legendre, Harmonic and Taylor cores; see code/COMPRESSION.md.

Inputs are rows v=x/sqrt(d), not raw x. Loss is mean((f-y)**2).
No experiment archive, filesystem writes or global settings are used at
runtime. Harmonic/Taylor numerical source setup is NOT a certified global
initialization-only continuation compiler.
"""
from __future__ import annotations

import math
from numbers import Integral
import numpy as np
import torch

DEEP_ACTIVATIONS = ('tanh', 'atan', 'gelu', 'silu', 'softplus', 'erf')


def _integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, Integral) or value < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return int(value)


def _positive(value, name):
    if isinstance(value, bool) or not math.isfinite(float(value)) or value <= 0:
        raise ValueError(f'{name} must be finite and positive')
    return float(value)


def _finite(values):
    if any(not isinstance(v, torch.Tensor) or v.dtype != torch.float64
           or not bool(torch.isfinite(v).all()) for v in values):
        raise ValueError('All tensors must be finite float64 arrays')


def _data(state, inputs, labels=None):
    _finite([*state, inputs] + ([] if labels is None else [labels]))
    if (inputs.ndim != 2 or inputs.shape[1] != state[0].shape[1]
            or any(v.device != state[0].device for v in [*state, inputs])):
        raise ValueError('Inputs/state must have compatible shapes and devices')
    if labels is not None and (not len(inputs) or labels.shape != (len(inputs),)
                               or labels.device != inputs.device):
        raise ValueError('Training labels must match a nonempty input batch')


class Dense:
    """Equal-width finite reference, arbitrary hidden depth, one activation.

    State order is [W1, w, W2, ..., WL]. Initialization uses variances
    1, 1/n and either zero readout (compression convention) or 1/n**2 (book small readout).
    Torch seed/draw order is explicit; no global RNG is changed.
    """

    def __init__(self, width, dimension, depth=2, activation='tanh', seed=0,
                 device='cpu', readout='zero'):
        width, dimension = _integer(width, 'width'), _integer(dimension, 'dimension')
        self.depth = _integer(depth, 'depth')
        if activation not in DEEP_ACTIVATIONS or readout not in ('zero', 'small_gaussian'):
            raise ValueError('Unsupported activation or readout initialization')
        self.activation, self.width, self.dimension = activation, width, dimension
        generator = torch.Generator(device=device).manual_seed(seed)
        draw = lambda *shape: torch.randn(*shape, generator=generator,
                                          device=device, dtype=torch.float64)
        first = draw(width, dimension)
        hidden = [draw(width, width)/math.sqrt(width) for _ in range(self.depth-1)]
        w = torch.zeros(width, device=device, dtype=torch.float64)
        if readout == 'small_gaussian':
            w = draw(width)/width
        self.initial_state = [first, w, *hidden]
        self.provenance = dict(model='finite_dense', depth=self.depth, activation=activation,
                               readout_initialization=readout, seed=int(seed))

    def fields(self, state, inputs):
        _data(state, inputs)
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

    def predict(self, state, queries, inputs=None, labels=None):
        return state[1]@self.fields(state, queries)[0][-1]/self.width

    def rhs(self, state, inputs, labels):
        _data(state, inputs, labels)
        hs, gates = self.fields(state, inputs)
        deltas = self.backward(state, hs, gates)
        c, scale = labels-state[1]@hs[-1]/self.width, 2/len(labels)
        return [scale*(deltas[0]*c)@inputs, scale*hs[-1]@c] + [
            scale/self.width*(deltas[j]*c)@hs[j-1].T for j in range(1, self.depth)]


class Legendre:
    """Direct complete-trajectory moments; no lifted features or residual division.

    State: [W1, w, tau, bar_delta2, bar_h1, ..., bar_deltaL, bar_h(L-1)].
    Each moment array has shape (order, width, samples). Fixed initial hidden
    mixers act by low-rank corrections in both directions; no moving dense
    hidden matrix is formed. The physical clock starts at tau=1.
    """

    def __init__(self, dense, inputs, labels, order):
        self.order = _integer(order, 'order')
        _data(dense.initial_state, inputs, labels)
        if bool(dense.initial_state[1].ne(0).any()):
            raise ValueError('Legendre requires the complete-trajectory zero initial readout')
        self.depth, self.activation = dense.depth, dense.activation
        self.width, self.samples = dense.width, len(inputs)
        self.mixers = [v.detach().clone() for v in dense.initial_state[2:]]
        first, w = dense.initial_state[:2]
        self.initial_state = [first.detach().clone(), w.detach().clone(), first.new_ones(())]
        hs, _ = dense.fields(dense.initial_state, inputs)
        for j in range(self.depth-1):
            backward = first.new_zeros((self.order, self.width, self.samples))
            forward = torch.zeros_like(backward)
            forward[0] = hs[j]
            self.initial_state.extend((backward, forward))
        self.provenance = dict(model='direct_compact_legendre', order=self.order,
                               initialization_only=True, depth=self.depth,
                               activation=self.activation, accuracy_certificate=False)

    @staticmethod
    def _columns(value):
        return value.permute(1, 0, 2).reshape(value.shape[1], -1)

    def factors(self, state, layer):
        """Hidden layer number is 2..L; returns W=W0+left@right.T."""
        if not 2 <= layer <= self.depth:
            raise ValueError('Hidden layer number must be in 2..L')
        j = layer-2
        degrees = torch.arange(self.order, dtype=state[0].dtype, device=state[0].device)
        left = (-2/(self.samples*self.width))*self._columns(
            (2*degrees+1)[:, None, None]*state[3+2*j])
        right = self._columns(state[4+2*j]/state[2])
        return left, right

    def apply_hidden(self, state, layer, value, transpose=False):
        left, right = self.factors(state, layer)
        matrix = self.mixers[layer-2]
        return (matrix.T@value+right@(left.T@value) if transpose
                else matrix@value+left@(right.T@value))

    def fields(self, state, inputs):
        _data(state, inputs)
        if state[2].ndim != 0 or float(state[2]) <= 0:
            raise ValueError('Legendre clock must be a positive scalar')
        hs, gates = [], []
        z = state[0]@inputs.T
        for j in range(self.depth):
            if j:
                z = self.apply_hidden(state, j+1, hs[-1])
            h, gate = _deep_activation(z, self.activation)
            hs.append(h)
            gates.append(gate)
        return hs, gates

    def predict(self, state, queries, inputs=None, labels=None):
        return state[1]@self.fields(state, queries)[0][-1]/self.width

    def _transport(self, moments, endpoint, rho, tau):
        j = torch.arange(self.order, dtype=moments.dtype, device=moments.device)[:, None, None]
        weighted = (2*j+1)*moments
        lower = torch.cat((torch.zeros_like(weighted[:1]), weighted[:-1].cumsum(0)), 0)
        return endpoint[None]-(rho/tau)*(j*moments+lower)

    def rhs(self, state, inputs, labels):
        _data(state, inputs, labels)
        if len(inputs) != self.samples:
            raise ValueError('Legendre training sample count is fixed at initialization')
        hs, gates = self.fields(state, inputs)
        deltas = [None]*self.depth
        deltas[-1] = state[1][:, None]*gates[-1]
        for j in range(self.depth-2, -1, -1):
            deltas[j] = gates[j]*self.apply_hidden(state, j+2, deltas[j+1], transpose=True)
        residual = state[1]@hs[-1]/self.width-labels
        rho = torch.linalg.vector_norm(residual)/math.sqrt(len(labels))
        scale = -2/len(labels)
        result = [scale*(deltas[0]*residual)@inputs, scale*hs[-1]@residual, rho]
        for j in range(self.depth-1):
            result.extend((self._transport(state[3+2*j], deltas[j+1]*residual, rho, state[2]),
                           self._transport(state[4+2*j], rho*hs[j], rho, state[2])))
        return result


def coordinate_metric(source_basis, budget, seed=0, trials=16, condition_limit=16.):
    """Uniform candidate restrictions with measured conditioning; not BSS."""
    n, rank = source_basis.shape
    budget, trials = _integer(budget, 'budget'), _integer(trials, 'trials')
    condition_limit = _positive(condition_limit, 'condition_limit')
    if not rank <= budget <= n:
        raise ValueError(f'Budget {budget} must lie between source rank {rank} and width {n}')
    generator = torch.Generator(device=source_basis.device).manual_seed(seed)
    best = None
    for _ in range(trials):
        indices = torch.randperm(n, device=source_basis.device, generator=generator)[:budget]
        selected = source_basis[indices]
        gram = selected.T@selected/budget
        eig = torch.linalg.eigvalsh((gram+gram.T)/2)
        condition = float(eig[-1]/eig[0]) if float(eig[0]) > 0 else math.inf
        if best is None or condition < best[0]:
            best = condition, indices, eig
    condition, indices, eig = best
    if not math.isfinite(condition) or condition > condition_limit:
        raise ArithmeticError(f'Source restriction condition {condition:g} exceeds {condition_limit:g}')
    selected = source_basis[indices]
    diagonal = torch.full((budget,), 1/(budget*float(eig[0])),
                          dtype=source_basis.dtype, device=source_basis.device)
    identity = torch.eye(rank, dtype=source_basis.dtype, device=source_basis.device)
    gram = selected.T@(diagonal[:, None]*selected)
    inverse = torch.linalg.solve((gram+gram.T)/2, identity)
    weighted = diagonal[:, None]*selected
    metric = torch.diag(diagonal)+weighted@(inverse@inverse-inverse)@weighted.T
    metric_inverse = torch.diag(diagonal.reciprocal())+selected@(identity-inverse)@selected.T
    metric, metric_inverse = (metric+metric.T)/2, (metric_inverse+metric_inverse.T)/2
    error = float((selected.T@metric@selected-identity).abs().max())
    if error > 1e-8:
        raise ArithmeticError('Source metric lost its isometry in finite precision')
    return indices, metric, metric_inverse, diagonal, dict(
        selector='uniform_exact_isometry', source_rank=rank, selected_width=budget,
        embedding_max=condition, source_isometry_error=error, trials=trials, seed=seed)


class Selected(Dense):
    """Shared Harmonic/Taylor metric-adjoint, corrected-readout optimizer.

    State is [W1, w, B2, ..., BL, c], c=y-f on training inputs. Uses an
    actual positive-definite Gram solve: no ridge, pseudoinverse or floor.
    Source bases and the dense model are not retained by the constructed model.
    """

    @torch.no_grad()
    def __init__(self, dense, inputs, labels, sources=None, *, budget=None,
                 seed=0, trials=16, condition_limit=16., source_info=None):
        _data(dense.initial_state, inputs, labels)
        original = dense.initial_state
        if bool(original[1].ne(0).any()):
            raise ValueError('Selected models require the complete-trajectory zero initial readout')
        self.depth, self.activation = dense.depth, dense.activation
        self.dimension, self.width = dense.dimension, dense.width
        n = dense.width
        if budget is not None:
            budget = _integer(budget, 'budget')
        self.provenance = dict(model='selected_metric_deficit',
                               source={} if source_info is None else source_info.copy(),
                               accuracy_certificate=False, depth=self.depth,
                               activation=self.activation)
        if budget is not None and budget >= n:
            self.metrics = [torch.eye(n, dtype=original[0].dtype, device=original[0].device)/n
                            for _ in range(self.depth)]
            self.metric_inverses = [n*n*v for v in self.metrics[:-1]]
            self.initial_state = [v.clone() for v in original]+[labels.clone()]
            self.diagnostics = dict(branch='full_retention', widths=[n]*self.depth)
        else:
            if sources is None or set(sources) != {'h', 'delta'} or any(
                    len(sources[name]) != self.depth for name in sources):
                raise ValueError('Need h/delta source matrix lists, one entry per layer')
            for values in sources.values():
                _finite(values)
                if any(v.ndim != 2 or v.shape[0] != n or v.device != original[0].device for v in values):
                    raise ValueError('Source matrices must be (dense width, coefficients) on the model device')
            h0, _ = dense.fields(original, inputs)
            constant = original[0].new_ones((n, 1))
            bases, selections, errors = [], [], []
            for j in range(self.depth):
                mandatory = ([constant, h0[j], original[j+1]@h0[j-1]] if j
                             else [constant, original[0], h0[0]])
                optional = [sources['h'][j], sources['delta'][j]]
                if j:
                    optional.append(original[j+1]@sources['h'][j-1])
                if j+1 < self.depth:
                    optional.append(original[j+2].T@sources['delta'][j+1])
                basis, error = _harmonic_source_basis(torch.cat(mandatory, 1), torch.cat(optional, 1))
                selection = (_harmonic_bss_metric(basis) if budget is None else
                             coordinate_metric(basis, budget, seed+j, trials, condition_limit))
                bases.append(basis)
                selections.append(selection)
                errors.append(error)
            self.metrics = [s[1] for s in selections]
            self.metric_inverses = [s[2] for s in selections[:-1]]
            indices = [s[0] for s in selections]
            selected = [b[i] for b, i in zip(bases, indices)]
            mixers = [selected[j]@(bases[j].T@original[j+1]@bases[j-1]/n)
                      @(selected[j-1].T@self.metrics[j-1]) for j in range(1, self.depth)]
            self.initial_state = [original[0][indices[0]].clone(), original[1][indices[-1]].clone(),
                                  *mixers, labels.clone()]
            hs, _ = self.fields(self.initial_state, inputs)
            maximum = lambda v: float(v.abs().max()) if v.numel() else 0.
            forward_errors, reverse_errors = [], []
            for j, mixer in enumerate(mixers, 1):
                forward_errors.append(maximum(mixer@sources['h'][j-1][indices[j-1]]
                    -(original[j+1]@sources['h'][j-1])[indices[j]]))
                reverse_errors.append(maximum(self.metric_inverses[j-1]@mixer.T
                    @self.metrics[j]@sources['delta'][j][indices[j]]
                    -(original[j+1].T@sources['delta'][j])[indices[j-1]]))
            self.diagnostics = dict(branch='selected', widths=[len(i) for i in indices],
                source_ranks=[b.shape[1] for b in bases], selections=[s[-1] for s in selections],
                mandatory_errors=errors,
                paired_forward_action_errors=forward_errors, paired_reverse_action_errors=reverse_errors,
                initialized_feature_errors=[float((h-h0[j][indices[j]]).abs().max()) for j, h in enumerate(hs)])
        self._readout(self.initial_state, inputs, labels)  # Reject deficient training Grams now.

    def backward(self, state, hs, gates, readout=None):
        deltas = [None]*self.depth
        deltas[-1] = (state[1] if readout is None else readout)[:, None]*gates[-1]
        for j in range(self.depth-2, -1, -1):
            deltas[j] = gates[j]*(self.metric_inverses[j]@(state[j+2].T@(self.metrics[j+1]@deltas[j+1])))
        return deltas

    def _readout(self, state, inputs, labels):
        _data(state, inputs, labels)
        if state[-1].shape != labels.shape:
            raise ValueError('Selected deficit must have one coordinate per training label')
        hs, gates = self.fields(state, inputs)
        normalized = hs[-1]/math.sqrt(len(labels))
        gram = normalized.T@(self.metrics[-1]@normalized)
        gram = (gram+gram.T)/2
        # Cholesky success alone can accept an exactly singular Gram after
        # roundoff. Use a scale-relative numerical-rank check at every state.
        eigenvalues = torch.linalg.eigvalsh(gram)
        tolerance = 32*max(normalized.shape)*torch.finfo(gram.dtype).eps
        if (not bool(torch.isfinite(eigenvalues).all())
                or float(eigenvalues[0]) <= tolerance*float(eigenvalues[-1])):
            raise ArithmeticError('Training feature Gram is numerically rank deficient; no regularization is applied')
        factor, info = torch.linalg.cholesky_ex(gram)
        if int(info) != 0:
            raise ArithmeticError('Training feature Gram must be positive definite; no regularization is applied')
        correction = (labels-state[-1])/math.sqrt(len(labels))-normalized.T@(self.metrics[-1]@state[1])
        readout = state[1]+normalized@torch.cholesky_solve(correction[:, None], factor).flatten()
        prediction = hs[-1].T@(self.metrics[-1]@readout)
        target = labels-state[-1]
        scale = torch.stack((labels.abs().max(), state[-1].abs().max(),
                             target.abs().max(), prediction.abs().max())).max()
        error = (prediction-target).abs().max()
        if (not bool(torch.isfinite(prediction).all())
                or float(error) > 4*tolerance*float(scale)):
            raise ArithmeticError('Corrected training identity lost in finite precision; no regularization is applied')
        return readout, hs, gates, gram

    def kernel(self, state, inputs, labels):
        readout, hs, gates, _ = self._readout(state, inputs, labels)
        deltas = self.backward(state, hs, gates, readout)
        kernel = hs[-1].T@(self.metrics[-1]@hs[-1])
        kernel = kernel+(deltas[0].T@(self.metrics[0]@deltas[0]))*(inputs@inputs.T)
        for j in range(1, self.depth):
            kernel = kernel+(deltas[j].T@(self.metrics[j]@deltas[j]))*(hs[j-1].T@self.metrics[j-1]@hs[j-1])
        return kernel, hs, deltas

    def rhs(self, state, inputs, labels):
        kernel, hs, deltas = self.kernel(state, inputs, labels)
        scale, deficit = 2/len(labels), state[-1]
        updates = [scale*(deltas[0]*deficit)@inputs, scale*hs[-1]@deficit]
        for j in range(1, self.depth):
            updates.append(scale*(deltas[j]*deficit)@(self.metrics[j-1]@hs[j-1]).T)
        return updates+[-scale*kernel@deficit]

    def predict(self, state, queries, inputs, labels):
        w = self._readout(state, inputs, labels)[0]
        return (self.metrics[-1]@w)@self.fields(state, queries)[0][-1]


@torch.no_grad()
def step(model, state, inputs, labels, step_size, method='rk4'):
    """One simultaneous numerical ODE step, returning independent tensors."""
    h = _positive(step_size, 'step_size')
    if method not in ('euler', 'heun', 'rk4'):
        raise ValueError('method must be euler, heun or rk4')
    k1 = model.rhs(state, inputs, labels)
    add = lambda rate, scale: [v+scale*k for v, k in zip(state, rate)]
    if method == 'euler':
        result = add(k1, h)
    elif method == 'heun':
        k2 = model.rhs(add(k1, h), inputs, labels)
        result = [v+h*(a+b)/2 for v, a, b in zip(state, k1, k2)]
    else:
        k2 = model.rhs(add(k1, h/2), inputs, labels)
        k3 = model.rhs(add(k2, h/2), inputs, labels)
        k4 = model.rhs(add(k3, h), inputs, labels)
        result = [v+h*(a+2*b+2*c+d)/6 for v, a, b, c, d in zip(state, k1, k2, k3, k4)]
    _finite(result)
    return result


@torch.no_grad()
def rollout(model, inputs, labels, times, *, step_size, queries=None, state=None, start_time=0., method='rk4'):
    """Return final state and optional predictions; never store weight history.

    Times are finite and nondecreasing, beginning no earlier than start_time.
    Pass a previous final state and its physical start_time to continue.
    """
    h = _positive(step_size, 'step_size')
    times = [float(t) for t in times]
    current = float(start_time)
    if (not math.isfinite(current) or current < 0 or any(not math.isfinite(t) or t < current for t in times)
            or any(b < a for a, b in zip(times, times[1:]))):
        raise ValueError('Observation times must be finite, nondecreasing and >= start_time >= 0')
    state = [v.detach().clone() for v in (model.initial_state if state is None else state)]
    _data(state, inputs, labels)
    predictions = []
    for target in times:
        while current < target:
            dt = min(h, target-current)
            if current+dt == current:
                raise ArithmeticError('Step is below clock resolution')
            state = step(model, state, inputs, labels, dt, method)
            current = min(current+dt, target)
        if queries is not None:
            prediction = model.predict(state, queries, inputs, labels)
            _finite([prediction])
            predictions.append(prediction.detach().clone())
    return state, (torch.stack(predictions) if predictions else None)


def storage(model, state=None):
    """Tensor entries only; fixed/current/initial copies exclude data and stages."""
    current = model.initial_state if state is None else state
    fixed = [*getattr(model, 'mixers', []), *getattr(model, 'metrics', []),
             *getattr(model, 'metric_inverses', [])]
    return dict(moving=sum(v.numel() for v in current), fixed=sum(v.numel() for v in fixed),
                retained_initial_copy=sum(v.numel() for v in model.initial_state),
                bytes_per_scalar=8, excludes='data, Python objects, stages, source compiler scratch')


def _truncate_sources(dense, inputs, blocks, rank):
    """Truncate base families first; initialized images are formed afterward."""
    rank = _integer(rank, 'rank')
    original, n = dense.initial_state, dense.width
    h0, _ = dense.fields(original, inputs)
    constant = original[0].new_ones((n, 1))
    sources, diagnostics = {k: [] for k in blocks}, {k: [] for k in blocks}
    for family in ('h', 'delta'):
        for j, pieces in enumerate(blocks[family]):
            source = torch.cat(pieces, 1)
            original_scale = source.norm()
            mandatory = source[:, :0]
            if family == 'h':
                mandatory = h0[j]
                if j == dense.depth-1:
                    additions = [constant, h0[j]]
                    if j:
                        additions.append(original[j+1]@h0[j-1])
                    mandatory = torch.cat(additions, 1)
            elif j == 0:
                mandatory = torch.cat((constant, original[0], h0[0]), 1)
            if mandatory.shape[1]:
                basis, _ = _harmonic_source_basis(mandatory, source[:, :0])
                basis = basis/math.sqrt(n)
                for _ in range(2):
                    source = source-basis@(basis.T@source)
            left, singular, _ = torch.linalg.svd(source, full_matrices=False)
            # Removing an exactly mandatory source can leave only roundoff.
            # Scale the rank test before that removal as well as afterward.
            tol = max(source.shape)*torch.finfo(source.dtype).eps*torch.maximum(singular[0], original_scale)
            available = int((singular > tol).sum())
            retained = left[:, :min(rank, available)].clone()
            error = source-retained@(retained.T@source)
            sources[family].append(retained)
            diagnostics[family].append(dict(rank=retained.shape[1], available_rank=available,
                coefficient_columns=source.shape[1], relative_coefficient_error=float(
                    error.norm()/source.norm().clamp_min(torch.finfo(source.dtype).tiny))))
    return sources, diagnostics


@torch.no_grad()
def initial_jets(dense, inputs, labels, queries=None, *, rank=8):
    """Exact through order two at zero readout, then optional rank truncation.

    These finite origin jets do not implement global analytic continuation.
    The forward coefficients cover the declared panel; backward coefficients
    cover only training inputs. Supports the same depth/activations as Dense.
    """
    _data(dense.initial_state, inputs, labels)
    if bool(dense.initial_state[1].ne(0).any()):
        raise ValueError('Origin jets require zero initial readout')
    panel = inputs if queries is None else torch.cat((inputs, queries))
    _data(dense.initial_state, panel)
    state, m, n = dense.initial_state, len(labels), dense.width
    hs, gates = dense.fields(state, panel)
    train_h, train_g = [h[:, :m] for h in hs], [g[:, :m] for g in gates]
    w_first = (2/m)*train_h[-1]@labels
    c_first = (-2/(m*n))*train_h[-1].T@(train_h[-1]@labels)
    w_second = (2/m)*train_h[-1]@c_first
    delta_first = dense.backward(state, train_h, train_g, w_first)
    delta_second = dense.backward(state, train_h, train_g, w_second)
    first_second = (2/m)*(delta_first[0]*labels)@inputs
    hidden_second = [(2/(m*n))*(delta_first[j]*labels)@train_h[j-1].T
                     for j in range(1, dense.depth)]
    h_second = [gates[0]*(first_second@panel.T)]
    for j in range(1, dense.depth):
        h_second.append(gates[j]*(hidden_second[j-1]@hs[j-1]+state[j+1]@h_second[j-1]))
    blocks = dict(h=[[torch.cat((h, hh/2), 1)] for h, hh in zip(hs, h_second)],
                  delta=[[torch.cat((d, dd/2), 1)] for d, dd in zip(delta_first, delta_second)])
    sources, diagnostics = _truncate_sources(dense, inputs, blocks, rank)
    return sources, dict(method='order_two_origin_jets', initialization_only=True,
        dense_rhs_calls=0, jet_order=2, source_rank_cap=int(rank), source_certificate=False,
        passive_labels_used=False, declared_passive_count=len(panel)-m, diagnostics=diagnostics)


@torch.no_grad()
def empirical_sources(dense, inputs, labels, *, kind, horizon, step_size,
                      rank=8, time_degree=4, spatial_degree=3, queries=None):
    """Offline finite-horizon dense RK4 source fitting, one interval at a time.

    Harmonic: Chebyshev time / real sphere harmonics, d=2 or 3, fixed geometry.
    Taylor: piecewise time-polynomial surrogate on declared query inputs.
    This numerical Taylor source is fitted in a Chebyshev basis, not obtained
    from certified Taylor derivatives. No weights or fields from older panels
    are kept; coefficient blocks persist only until one final exact SVD.
    """
    if kind not in ('harmonic', 'taylor'):
        raise ValueError('kind must be harmonic or taylor')
    _data(dense.initial_state, inputs, labels)
    horizon, h = _positive(horizon, 'horizon'), _positive(step_size, 'step_size')
    degree, rank = _integer(time_degree, 'time_degree'), _integer(rank, 'rank')
    if bool(dense.initial_state[1].ne(0).any()):
        raise ValueError('Compressed source setup requires zero initial readout')
    device = inputs.device
    if kind == 'harmonic':
        if queries is not None:
            raise ValueError('Harmonic source geometry does not take scored query inputs')
        panel, weights, spatial = _unified_harmonic_geometry(inputs.shape[1], spatial_degree)
        panel, weights, spatial = [v.to(device) for v in (panel, weights, spatial)]
        gram_error = float((spatial.T@(weights[:, None]*spatial)-torch.eye(
            spatial.shape[1], device=device, dtype=torch.float64)).abs().max())
        if gram_error > 1e-11:
            raise ArithmeticError('Sphere quadrature lost harmonic orthonormality')
    else:
        panel = inputs if queries is None else torch.cat((inputs, queries))
        _data(dense.initial_state, panel)
        weights = spatial = None
    boundaries = [0., min(1., horizon)]
    while boundaries[-1] < horizon:
        boundaries.append(min(2*boundaries[-1], horizon))
    coordinate = -np.cos(np.linspace(0, np.pi, 2*degree+1))
    design = torch.as_tensor(np.polynomial.chebyshev.chebvander(coordinate, degree),
                             dtype=torch.float64, device=device)
    inverse = torch.linalg.inv(design[::2])
    blocks = {name: [[] for _ in range(dense.depth)] for name in ('h', 'delta')}
    errors = {name: [0.]*dense.depth for name in blocks}
    state, current, count = [v.clone() for v in dense.initial_state], 0., 0
    for left, right in zip(boundaries[:-1], boundaries[1:]):
        times = left+(right-left)*(coordinate+1)/2
        times[0], times[-1] = left, right
        snapshots = {name: [[] for _ in range(dense.depth)] for name in blocks}
        for target in times:
            while current < target:
                dt = min(h, float(target)-current)
                if current+dt == current:
                    raise ArithmeticError('Source step is below clock resolution')
                state = step(dense, state, inputs, labels, dt, 'rk4')
                current = min(current+dt, float(target))
                count += 1
            hs, gates = dense.fields(state, panel)
            if kind == 'harmonic':
                deltas = dense.backward(state, hs, gates)
            else:
                deltas = dense.backward(state, [v[:, :len(labels)] for v in hs],
                                         [v[:, :len(labels)] for v in gates])
            for name, values in (('h', hs), ('delta', deltas)):
                for j, value in enumerate(values):
                    snapshots[name][j].append(value)
        for name in blocks:
            for j in range(dense.depth):
                values = torch.stack(snapshots[name][j])
                projected = values@(weights[:, None]*spatial) if kind == 'harmonic' else values
                coefficient = torch.einsum('kt,tnp->nkp', inverse, projected[::2])
                fitted = torch.einsum('tk,nkp->tnp', design[1::2], coefficient)
                if kind == 'harmonic':
                    fitted = fitted@spatial.T
                errors[name][j] = max(errors[name][j], float((fitted-values[1::2]).abs().max()))
                blocks[name][j].append(coefficient.flatten(1))
        del snapshots
    sources, diagnostics = _truncate_sources(dense, inputs, blocks, rank)
    report = dict(method=kind+'_piecewise_chebyshev_dense_rollout', initialization_only=False,
        source_certificate=False, horizon=horizon, rk4_step=h, dense_rhs_calls=4*count,
        time_degree=degree, source_rank_cap=rank, boundaries=boundaries,
        stored_network_trajectory=False, field_storage='one temporal interval',
        passive_labels_used=False, declared_passive_count=(len(panel)-len(inputs) if kind == 'taylor' else 0),
        source_geometry_uses_scored_inputs=kind == 'taylor',
        heldout_coordinate_max=errors, diagnostics=diagnostics,
        diagnostic_scope='interleaved time nodes and finite source panel; no continuum accuracy bound')
    if kind == 'harmonic':
        report.update(spatial_degree=spatial_degree, spatial_modes=spatial.shape[1],
                      quadrature_nodes=len(panel), spatial_gram_error=gram_error)
    return sources, report


def harmonic(dense, inputs, labels, *, horizon, step_size, rank=8,
             time_degree=4, spatial_degree=3, budget=None, seed=0, trials=16, condition_limit=16.):
    """Compile empirical Harmonic sources and discard them after selection."""
    sources, report = empirical_sources(dense, inputs, labels, kind='harmonic', horizon=horizon,
        step_size=step_size, rank=rank, time_degree=time_degree, spatial_degree=spatial_degree)
    return Selected(dense, inputs, labels, sources, budget=budget, seed=seed,
                    trials=trials, condition_limit=condition_limit, source_info=report)


def taylor(dense, inputs, labels, queries, *, source_mode='jets', rank=8,
           horizon=None, step_size=None, time_degree=4, budget=None,
           seed=0, trials=16, condition_limit=16.):
    """Finite-panel selected runtime; low-order origin jets or empirical rollout."""
    if source_mode == 'jets':
        sources, report = initial_jets(dense, inputs, labels, queries, rank=rank)
    elif source_mode == 'rollout':
        if horizon is None or step_size is None:
            raise ValueError('Rollout source mode requires horizon and step_size')
        sources, report = empirical_sources(dense, inputs, labels, kind='taylor', queries=queries,
            horizon=horizon, step_size=step_size, rank=rank, time_degree=time_degree)
    else:
        raise ValueError('source_mode must be jets or rollout')
    return Selected(dense, inputs, labels, sources, budget=budget, seed=seed,
                    trials=trials, condition_limit=condition_limit, source_info=report)


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
    """Sparsity-nine barrier selector and full positive metric."""
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
