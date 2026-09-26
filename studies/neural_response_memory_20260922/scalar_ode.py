"""Standalone scalar response-basis ODE with physical validation references.

Requires only NumPy, SciPy, and the Python standard library. The network has
three hidden tanh layers, no biases, output c @ h3 / width, mean squared loss,
and parameter mobilities (width, 1, 1, width). Circle inputs have unit norm;
do not apply another input normalization. Initialization draws and the frozen
response feature/SVD policy are copied from the original study implementation.

ResponseBasisSystem uses column-oriented inputs (2, samples), whereas
DenseReference and PopulationReference use row-oriented inputs (samples, 2).
The scalar state contains mode coefficients, not neuron weights. Its fixed
basis is selected from training inputs only. Call detach_decoder() immediately
after initialize(); physical decoding is for validation and can disagree with
the internal scalar readout at reduced rank. Full rank is an implementation
control, not evidence of compression or of a total-storage advantage.

Each multiplication and initialized operator action is projected separately;
the method is not a Galerkin projection of the whole composed vector field.
The frozen bank contains centered/RMS-normalized initial responses, backward
fields and response velocities, c0 on layer 3, pairwise products, and cubes.
The constant mode is exact; SVD orientation/completion and feature ordering
are unchanged. No neuron arrays or initialized matrix actions enter its RHS.

PopulationReference is the original activity-clock history closure. Its
clock rate is the training residual RMS and its P-mode moment equations are
unchanged; it retains physical initialization arrays and is a baseline, not
a compressed scalar solver. Only finite-width numerical validation is claimed.
"""

from __future__ import annotations

import os
for _thread_variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_variable] = "1"

from dataclasses import dataclass
from time import perf_counter

import numpy as np
from scipy.integrate import DOP853
from scipy.optimize import brentq

@dataclass(frozen=True)
class Initialization:
    w: np.ndarray
    W20: np.ndarray
    W30: np.ndarray
    c: np.ndarray

    @property
    def width(self):
        return self.c.size



def initialize(width, seed=20260920):
    """Canonical sequential NumPy draws; supplied inputs already include 1/sqrt(d)."""
    if not isinstance(width, (int, np.integer)) or width < 1:
        raise ValueError("width must be a positive integer")
    rng = np.random.default_rng(seed)
    return Initialization(
        rng.standard_normal((width, 2)),
        rng.standard_normal((width, width)) / np.sqrt(width),
        rng.standard_normal((width, width)) / np.sqrt(width),
        rng.standard_normal(width) / width,
    )



def circle_inputs(angles, *, degrees=False):
    angles = np.asarray(angles, dtype=np.float64)
    if degrees:
        angles = np.deg2rad(angles)
    return np.column_stack((np.cos(angles), np.sin(angles)))



class DenseReference:
    """Canonical three-hidden-layer physical gradient flow."""

    kind = "dense"

    def __init__(self, inputs, labels, initialization):
        self.inputs = np.asarray(inputs, dtype=np.float64).copy()
        self.labels = np.asarray(labels, dtype=np.float64).copy()
        self.initialization = initialization
        self.n = initialization.width
        if self.inputs.ndim != 2 or self.inputs.shape[1] != 2:
            raise ValueError("inputs must have shape (M,2)")
        self.M = self.inputs.shape[0]
        if self.M == 0 or self.labels.shape != (self.M,):
            raise ValueError("labels must have shape (M,), M>0")
        if not all(np.isfinite(a).all() for a in (self.inputs, self.labels)):
            raise ValueError("nonfinite inputs or labels")
        self.names = ("w", "W2", "W3", "c")
        self.shapes = ((self.n, 2), (self.n, self.n), (self.n, self.n), (self.n,))
        self._set_slices()
        self.initial = self.pack(dict(w=initialization.w, W2=initialization.W20,
                                      W3=initialization.W30, c=initialization.c))

    def _set_slices(self):
        sizes = [int(np.prod(shape)) for shape in self.shapes]
        endpoints = np.cumsum([0] + sizes)
        self.slices = {name: slice(start, end) for name, start, end in
                       zip(self.names, endpoints[:-1], endpoints[1:])}
        self.dimension = int(endpoints[-1])

    def pack(self, values):
        return np.concatenate([np.asarray(values[name], dtype=np.float64).ravel()
                               for name in self.names])

    def unpack(self, state):
        state = np.asarray(state, dtype=np.float64)
        if state.shape != (self.dimension,):
            raise ValueError("state has wrong shape")
        return {name: state[self.slices[name]].reshape(shape)
                for name, shape in zip(self.names, self.shapes)}

    def physical(self, state):
        return self.unpack(state)

    def query_fields(self, state, inputs):
        weights = self.physical(state)
        inputs = np.asarray(inputs, dtype=np.float64)
        h1 = np.tanh(weights["w"] @ inputs.T)
        h2 = np.tanh(weights["W2"] @ h1)
        h3 = np.tanh(weights["W3"] @ h2)
        f = weights["c"] @ h3 / self.n
        return dict(h1=h1, h2=h2, h3=h3, f=f)

    def predict(self, state, inputs):
        return self.query_fields(state, inputs)["f"]

    def query_field_velocity(self, state, inputs):
        """Exact passive response chain rule from current physical velocities."""
        inputs = np.asarray(inputs, dtype=np.float64)
        weights = self.physical(state)
        velocity = self.physical_velocity(state)
        values = self.query_fields(state, inputs)
        dh1 = (1 - values["h1"]**2) * (velocity["w"] @ inputs.T)
        dh2 = (1 - values["h2"]**2) * (velocity["W2"] @ values["h1"] + weights["W2"] @ dh1)
        dh3 = (1 - values["h3"]**2) * (velocity["W3"] @ values["h2"] + weights["W3"] @ dh2)
        df = (velocity["c"] @ values["h3"] + weights["c"] @ dh3) / self.n
        return dict(h1=dh1, h2=dh2, h3=dh3, f=df)

    def fields(self, state):
        weights = self.physical(state)
        values = self.query_fields(state, self.inputs)
        residual = values["f"] - self.labels
        loss = float(np.mean(residual**2))
        delta3 = weights["c"][:, None] * (1 - values["h3"]**2)
        delta2 = (1 - values["h2"]**2) * (weights["W3"].T @ delta3)
        delta1 = (1 - values["h1"]**2) * (weights["W2"].T @ delta2)
        values.update(r=residual, loss=loss, rho=np.sqrt(loss), delta1=delta1,
                      delta2=delta2, delta3=delta3)
        return values

    def rhs(self, time, state):
        del time
        f = self.fields(state)
        return self.pack(dict(
            w=(-2 / self.M) * ((f["delta1"] * f["r"]) @ self.inputs),
            W2=(-2 / (self.M * self.n)) * ((f["delta2"] * f["r"]) @ f["h1"].T),
            W3=(-2 / (self.M * self.n)) * ((f["delta3"] * f["r"]) @ f["h2"].T),
            c=(-2 / self.M) * (f["h3"] @ f["r"]),
        ))

    def physical_velocity(self, state):
        return self.unpack(self.rhs(0., state))



class PopulationReference(DenseReference):
    """Original activity-clock P-mode population closure, evaluated directly."""

    kind = "population"

    def __init__(self, inputs, labels, initialization, order=1):
        super().__init__(inputs, labels, initialization)
        if not isinstance(order, (int, np.integer)) or order < 1:
            raise ValueError("order must be a positive integer")
        self.P = int(order)
        self.degrees = np.arange(self.P, dtype=np.float64)
        self.mode_weights = 2 * self.degrees + 1
        h1 = np.tanh(initialization.w @ self.inputs.T)
        h2 = np.tanh(initialization.W20 @ h1)
        self.names = ("w", "c", "A2", "B2", "A3", "B3", "L")
        moment_shape = (self.P, self.n, self.M)
        self.shapes = ((self.n, 2), (self.n,), moment_shape, moment_shape,
                       moment_shape, moment_shape, ())
        self._set_slices()
        initial = dict(w=initialization.w, c=initialization.c, L=1.)
        for layer, h in ((2, h1), (3, h2)):
            initial["A" + str(layer)] = np.zeros(moment_shape)
            initial["B" + str(layer)] = np.zeros(moment_shape)
            initial["B" + str(layer)][0] = h
        self.initial = self.pack(initial)

    def physical(self, state):
        values = self.unpack(state)
        physical = dict(w=values["w"], c=values["c"])
        factor = -2 / (self.M * self.n * float(values["L"]))
        for layer in (2, 3):
            A, B = values["A" + str(layer)], values["B" + str(layer)]
            correction = np.einsum("k,kia,kja->ij", self.mode_weights, A, B)
            physical["W" + str(layer)] = getattr(self.initialization, "W" + str(layer) + "0") + factor * correction
        return physical

    def transport(self, moments, source, rho, length):
        weighted = self.mode_weights[:, None, None] * moments
        lower = np.zeros_like(moments)
        lower[1:] = np.cumsum(weighted[:-1], axis=0)
        return source[None] - (rho / length) * (self.degrees[:, None, None] * moments + lower)

    def rhs(self, time, state):
        del time
        values, f = self.unpack(state), self.fields(state)
        velocity = dict(w=(-2 / self.M) * ((f["delta1"] * f["r"]) @ self.inputs),
                        c=(-2 / self.M) * (f["h3"] @ f["r"]), L=f["rho"])
        for layer in (2, 3):
            for prefix, source in (("A", f["delta" + str(layer)] * f["r"]),
                                    ("B", f["rho"] * f["h" + str(layer - 1)])):
                name = prefix + str(layer)
                velocity[name] = self.transport(values[name], source, f["rho"], float(values["L"]))
        return self.pack(velocity)

    def physical_velocity(self, state):
        values = self.unpack(state)
        velocity = self.unpack(self.rhs(0., state))
        result = dict(w=velocity["w"], c=velocity["c"])
        length = float(values["L"])
        factor = -2 / (self.M * self.n * length)
        for layer in (2, 3):
            A, B = values["A" + str(layer)], values["B" + str(layer)]
            dA, dB = velocity["A" + str(layer)], velocity["B" + str(layer)]
            result["W" + str(layer)] = factor * (
                np.einsum("k,kia,kja->ij", self.mode_weights, dA, B)
                + np.einsum("k,kia,kja->ij", self.mode_weights, A, dB)
                - float(velocity["L"]) / length
                * np.einsum("k,kia,kja->ij", self.mode_weights, A, B))
        return result



def _feature_basis(h, delta, hdot, rank, layer, initial_c=None):
    """Return the frozen basis and its deterministic construction metadata."""
    n = h.shape[0]
    eps = np.finfo(float).eps
    def normalize(columns):
        columns = np.asarray(columns, dtype=float).copy()
        columns -= np.mean(columns, axis=0, keepdims=True)
        norms = np.linalg.norm(columns, axis=0) / np.sqrt(n)
        threshold = 64 * eps * max(columns.shape)
        for j in range(columns.shape[1]):
            if norms[j] > threshold:
                columns[:, j] /= norms[j]
            else:
                columns[:, j] = 0.
        return columns

    marks = np.column_stack((h, delta, hdot))
    if initial_c is not None:
        marks = np.column_stack((marks, initial_c))
    marks = normalize(marks)
    features = [marks]
    features.extend((marks[:, j] * marks[:, k])[:, None]
                    for j in range(marks.shape[1]) for k in range(j, marks.shape[1]))
    features.append(marks**3)
    seeds = normalize(np.column_stack(features))
    threshold = 64 * eps * max(seeds.shape)
    left, singular, right = np.linalg.svd(seeds, full_matrices=False)
    singular_threshold = (64 * eps * max(seeds.shape) * singular[0]
                          if singular.size and singular[0] else threshold)
    directions = [np.ones(n)]
    seed_modes = gaussian_modes = 0

    def append(candidate):
        v = np.asarray(candidate, dtype=float).copy()
        initial_norm = np.linalg.norm(v) / np.sqrt(n)
        for _ in range(2):
            for q in directions:
                v -= q * np.dot(q, v) / n
        length = np.linalg.norm(v) / np.sqrt(n)
        if length <= 64 * eps * n * max(1., initial_norm):
            return False
        directions.append(v / length)
        return True

    for j, value in enumerate(singular):
        if len(directions) == rank or value <= singular_threshold:
            break
        sign = 1. if right[j, np.argmax(np.abs(right[j]))] >= 0 else -1.
        if append(sign * np.sqrt(n) * left[:, j]):
            seed_modes += 1
    rng = np.random.default_rng(20260925 + layer)
    for _ in range(4 * n):
        if len(directions) == rank:
            break
        if append(rng.standard_normal(n)):
            gaussian_modes += 1
    if len(directions) != rank:
        raise ArithmeticError("Deterministic basis completion failed")
    Q = np.column_stack(directions)
    return Q, dict(feature_bank_columns=seeds.shape[1], seed_modes=seed_modes,
                   gaussian_modes=gaussian_modes,
                   orthogonality_error=float(np.max(np.abs(Q.T @ Q / n - np.eye(rank)))))



class ResponseBasisSystem:
    """Autonomous scalar modal-response system, with detached validation decoder."""

    kind = "response_basis"

    def __init__(self, U, y, Utest, rank, *, preparation_seconds=180.,
                 max_memory_bytes=3 * 1024**3):
        self.U = np.asarray(U, dtype=float).copy()
        self.y = np.asarray(y, dtype=float).copy()
        if (self.y.ndim != 1 or not self.y.size
                or self.U.shape != (2, self.y.size)):
            raise ValueError("U must have shape (2,M), y shape (M,), M>0")
        query = np.empty((2, 0)) if Utest is None else np.asarray(Utest, dtype=float)
        if query.ndim != 2 or query.shape[0] != 2:
            raise ValueError("Utest must have shape (2,Q), or be None")
        if (not np.isfinite(self.U).all() or not np.isfinite(self.y).all()
                or not np.isfinite(query).all()):
            raise ValueError("Nonfinite input")
        if int(rank) != rank or rank < 1:
            raise ValueError("rank must be a positive integer")
        self.rank, self.M = int(rank), self.y.size
        self.Uall = np.column_stack((self.U, query))
        self.J = self.Uall.shape[1]
        self.preparation_seconds = float(preparation_seconds)
        self.max_memory_bytes = int(max_memory_bytes)
        r = self.rank
        self.names = ("dw", "B2", "B3", "c", "h1", "h2", "h3")
        self.shapes = ((r, 2), (r, r), (r, r), (r,), (r, self.J),
                       (r, self.J), (r, self.J))
        endpoints = np.cumsum([0] + [int(np.prod(shape)) for shape in self.shapes])
        self.slices = {name: slice(int(lo), int(hi)) for name, lo, hi in
                       zip(self.names, endpoints[:-1], endpoints[1:])}
        self.dimension = int(endpoints[-1])

    def pack(self, values):
        return np.concatenate([np.asarray(values[name], dtype=float).ravel()
                               for name in self.names])

    def unpack(self, state):
        state = np.asarray(state, dtype=float)
        if state.shape != (self.dimension,):
            raise ValueError("State has wrong shape")
        return {name: state[self.slices[name]].reshape(shape)
                for name, shape in zip(self.names, self.shapes)}

    def initialize(self, w, W20, W30, c):
        start = perf_counter()
        w, W20, W30, c = [np.asarray(v, dtype=float) for v in (w, W20, W30, c)]
        n, r = c.size, self.rank
        if (w.shape != (n, 2) or W20.shape != (n, n) or W30.shape != (n, n)
                or c.shape != (n,) or r > n):
            raise ValueError("Inconsistent initialization shapes or rank exceeds width")
        if not all(np.isfinite(v).all() for v in (w, W20, W30, c)):
            raise ValueError("Nonfinite initialization")
        self.width = n
        # All basis data are calculated using active columns only.
        h1 = np.tanh(w @ self.U)
        h2 = np.tanh(W20 @ h1)
        h3 = np.tanh(W30 @ h2)
        residual = c @ h3 / n - self.y
        delta3 = c[:, None] * (1 - h3**2)
        delta2 = (1 - h2**2) * (W30.T @ delta3)
        delta1 = (1 - h1**2) * (W20.T @ delta2)
        dw = (-2 / self.M) * ((delta1 * residual) @ self.U.T)
        dW2 = (-2 / (self.M * n)) * ((delta2 * residual) @ h1.T)
        dW3 = (-2 / (self.M * n)) * ((delta3 * residual) @ h2.T)
        dh1 = (1 - h1**2) * (dw @ self.U)
        dh2 = (1 - h2**2) * (dW2 @ h1 + W20 @ dh1)
        dh3 = (1 - h3**2) * (dW3 @ h2 + W30 @ dh2)
        bases, metadata = [], []
        for layer, (h, delta, hdot) in enumerate(
                ((h1, delta1, dh1), (h2, delta2, dh2), (h3, delta3, dh3)), 1):
            Q, info = _feature_basis(h, delta, hdot, r, layer,
                                    initial_c=c if layer == 3 else None)
            bases.append(Q)
            metadata.append(info)
        Q1, Q2, Q3 = bases
        self.C2, self.C3 = Q2.T @ W20 @ Q1 / n, Q3.T @ W30 @ Q2 / n
        self.products = tuple(np.einsum("ni,nj,nk->ijk", Q, Q, Q, optimize=True) / n
                              for Q in bases)
        self.constants = tuple(Q.T @ np.ones(n) / n for Q in bases)
        h1all = np.tanh(w @ self.Uall)
        h2all = np.tanh(W20 @ h1all)
        h3all = np.tanh(W30 @ h2all)
        values = dict(dw=np.zeros((r, 2)), B2=np.zeros((r, r)), B3=np.zeros((r, r)),
                      c=Q3.T @ c / n, h1=Q1.T @ h1all / n,
                      h2=Q2.T @ h2all / n, h3=Q3.T @ h3all / n)
        self.initial = self.pack(values)
        self.basis_metadata = metadata
        self.initial_projection_errors = dict(
            c=float(np.linalg.norm(c - Q3 @ values["c"]) / np.sqrt(n)),
            **{name: np.linalg.norm(exact - Q @ values[name], axis=0).tolist()
               for name, exact, Q in (("h1", h1all, Q1), ("h2", h2all, Q2),
                                       ("h3", h3all, Q3))})
        # Normalize all response error entries consistently to the empirical norm.
        for name in ("h1", "h2", "h3"):
            self.initial_projection_errors[name] = (
                np.asarray(self.initial_projection_errors[name]) / np.sqrt(n)).tolist()
        self.operator_leakage = {
            "W2_forward": float(np.linalg.norm(W20 @ Q1 - Q2 @ self.C2) / np.sqrt(n)),
            "W2_reverse": float(np.linalg.norm(W20.T @ Q2 - Q1 @ self.C2.T) / np.sqrt(n)),
            "W3_forward": float(np.linalg.norm(W30 @ Q2 - Q3 @ self.C3) / np.sqrt(n)),
            "W3_reverse": float(np.linalg.norm(W30.T @ Q3 - Q2 @ self.C3.T) / np.sqrt(n)),
        }
        self.decoder = dict(Q1=Q1.copy(), Q2=Q2.copy(), Q3=Q3.copy(),
                            w0=w.copy(), W20=W20.copy(), W30=W30.copy(),
                            width=n, rank=r, query_count=self.J)
        self.initialization_seconds = perf_counter() - start
        self.fixed_coefficient_bytes = sum(v.nbytes for v in
            (self.C2, self.C3, self.U, self.y, self.Uall, *self.products, *self.constants))
        if self.initialization_seconds > self.preparation_seconds:
            raise TimeoutError("Response-basis preparation time cap exceeded")
        if self.fixed_coefficient_bytes > self.max_memory_bytes:
            raise MemoryError("Response-basis coefficient storage cap exceeded")
        return self.initial.copy()

    def detach_decoder(self):
        decoder = self.decoder
        del self.decoder
        return decoder

    def product(self, layer, a, b):
        a, b = np.asarray(a), np.asarray(b)
        if a.ndim == b.ndim == 1:
            return np.einsum("ijk,j,k->i", self.products[layer - 1], a, b)
        if a.ndim == 1:
            a = a[:, None]
        if b.ndim == 1:
            b = b[:, None]
        return np.einsum("ijk,ja,ka->ia", self.products[layer - 1], a, b)

    def outputs(self, state):
        values = self.unpack(state)
        return values["c"] @ values["h3"]

    def training_output(self, state):
        return self.outputs(state)[:self.M]

    def rhs(self, time, state):
        del time
        v = self.unpack(state)
        h1, h2, h3, c = (v[key] for key in ("h1", "h2", "h3", "c"))
        residual = c @ h3[:, :self.M] - self.y
        M2, M3 = self.C2 + v["B2"], self.C3 + v["B3"]
        D1 = self.constants[0][:, None] - self.product(1, h1, h1)
        D2 = self.constants[1][:, None] - self.product(2, h2, h2)
        D3 = self.constants[2][:, None] - self.product(3, h3, h3)
        delta3 = self.product(3, c, D3[:, :self.M])
        delta2 = self.product(2, D2[:, :self.M], M3.T @ delta3)
        delta1 = self.product(1, D1[:, :self.M], M2.T @ delta2)
        factor = -2 / self.M
        dw = factor * ((delta1 * residual) @ self.U.T)
        dB2 = factor * ((delta2 * residual) @ h1[:, :self.M].T)
        dB3 = factor * ((delta3 * residual) @ h2[:, :self.M].T)
        dc = factor * (h3[:, :self.M] @ residual)
        dh1 = self.product(1, D1, dw @ self.Uall)
        dh2 = self.product(2, D2, dB2 @ h1 + M2 @ dh1)
        dh3 = self.product(3, D3, dB3 @ h2 + M3 @ dh2)
        return self.pack(dict(dw=dw, B2=dB2, B3=dB3, c=dc,
                              h1=dh1, h2=dh2, h3=dh3))

    def statistics(self):
        return dict(kind=self.kind, rank=self.rank, width=getattr(self, "width", None),
                    training_inputs=self.M, passive_inputs=self.J - self.M,
                    state_dimension=self.dimension, dimension=self.dimension,
                    initialization_seconds=getattr(self, "initialization_seconds", None),
                    fixed_coefficient_bytes=getattr(self, "fixed_coefficient_bytes", None),
                    basis_metadata=getattr(self, "basis_metadata", None),
                    initial_projection_errors=getattr(self, "initial_projection_errors", None),
                    operator_leakage=getattr(self, "operator_leakage", None),
                    has_attached_decoder=hasattr(self, "decoder"),
                    full_rank_control=getattr(self, "width", None) == self.rank)



def decode(state, decoder):
    """Reconstruct physical arrays for validation, never for coefficient RHS."""
    r, J, n = int(decoder["rank"]), int(decoder["query_count"]), int(decoder["width"])
    shapes = ((r, 2), (r, r), (r, r), (r,), (r, J), (r, J), (r, J))
    names = ("dw", "B2", "B3", "c", "h1", "h2", "h3")
    state = np.asarray(state, dtype=float)
    offset, values = 0, {}
    for name, shape in zip(names, shapes):
        length = int(np.prod(shape))
        values[name] = state[offset:offset + length].reshape(shape)
        offset += length
    if offset != state.size:
        raise ValueError("State and decoder dimensions disagree")
    Q1, Q2, Q3 = (decoder[name] for name in ("Q1", "Q2", "Q3"))
    return dict(w=decoder["w0"] + Q1 @ values["dw"],
                W2=decoder["W20"] + Q2 @ values["B2"] @ Q1.T / n,
                W3=decoder["W30"] + Q3 @ values["B3"] @ Q2.T / n,
                c=Q3 @ values["c"])



def create(Utrain, y, Utest, rank):
    return ResponseBasisSystem(Utrain, y, Utest, rank)


def physical_outputs(weights, inputs):
    """Evaluate decoded weights on column-oriented inputs of shape (2, J)."""
    inputs = np.asarray(inputs, dtype=float)
    if inputs.ndim != 2 or inputs.shape[0] != 2:
        raise ValueError("inputs must have shape (2,J)")
    if not np.isfinite(inputs).all():
        raise ValueError("Nonfinite prediction inputs")
    h = np.tanh(weights["w"] @ inputs)
    h = np.tanh(weights["W2"] @ h)
    h = np.tanh(weights["W3"] @ h)
    return weights["c"] @ h / len(weights["c"])


class FitSolution:
    """Accepted DOP853 trajectory with interpolation confined to its interval.

    ``t`` and ``y`` contain accepted endpoints, including an event state
    interpolated within an accepted step when target stopping is requested.
    A failed RHS trial never replaces an accepted endpoint. If constructing
    the last dense interpolant itself fails, that segment is unavailable;
    its two accepted endpoints remain accessible through ``sol`` and ``y``.
    ``interpolation_to`` gives the end of the continuously covered interval.
    """

    def __init__(self, times, states, interpolants, *, success, status, message,
                 nfev, target_times, target_states, wall_seconds):
        self.t = np.asarray(times, dtype=float)
        self.y = np.column_stack(states)
        self.interpolants = list(interpolants)
        self.success = bool(success)
        self.status = int(status)
        self.message = str(message)
        self.nfev = int(nfev)
        self.njev = 0
        self.nlu = 0
        self.t_events = [np.asarray(target_times, dtype=float)]
        self.y_events = [np.asarray(target_states, dtype=float).reshape(
            len(target_times), self.y.shape[0])]
        self.target_hit = bool(target_times)
        self.wall_seconds = float(wall_seconds)
        self.interpolation_to = float(self.t[0])
        for i, interpolant in enumerate(self.interpolants):
            if interpolant is None:
                break
            self.interpolation_to = float(self.t[i + 1])

    def sol(self, times):
        """Evaluate accepted dense output; raise instead of extrapolating."""
        requested = np.asarray(times, dtype=float)
        if requested.ndim > 1:
            raise ValueError("Interpolation times must be scalar or one-dimensional")
        flat = requested.reshape(-1)
        if (not np.isfinite(flat).all() or np.any(flat < self.t[0])
                or np.any(flat > self.t[-1])):
            raise ValueError("Interpolation outside the accepted trajectory is forbidden")
        values = np.empty((self.y.shape[0], flat.size), dtype=float)
        for j, time in enumerate(flat):
            endpoint = int(np.searchsorted(self.t, time, side="left"))
            if endpoint < self.t.size and self.t[endpoint] == time:
                values[:, j] = self.y[:, endpoint]
                continue
            segment = endpoint - 1
            interpolant = self.interpolants[segment]
            if interpolant is None:
                raise ValueError("Dense interpolation is unavailable on this accepted segment")
            values[:, j] = interpolant(float(time))
        return values[:, 0] if requested.ndim == 0 else values


def fit(rhs, initial, output, labels, *, target_mse=.001, horizon=1000.,
        rtol=1e-7, atol=1e-9, stop_at_target=True, wall_seconds=30.,
        max_step=np.inf, state_limit=1e8):
    """Fit arbitrary labels using DOP853 and a decreasing training-loss event.

    ``output(state)`` must return one prediction per label. The same DOP853
    steps and dense-interpolant event root are used as in ``solve_ivp``.
    Return ``(solution, final_state, record)``. On success, final_state is the
    first target state if reached, otherwise the accepted horizon endpoint.
    On failure, it is always the last accepted endpoint. ``record`` exposes
    evaluation/target times separately, and never presents a rejected RHS
    trial as an accepted state. No parameter, decoder or neuron arrays are
    used by this generic integration wrapper.
    """
    started = perf_counter()
    initial = np.asarray(initial, dtype=float).copy()
    labels = np.asarray(labels, dtype=float).copy()
    if initial.ndim != 1 or not initial.size or not np.isfinite(initial).all():
        raise ValueError("initial must be a nonempty finite state vector")
    if labels.ndim != 1 or not labels.size or not np.isfinite(labels).all():
        raise ValueError("labels must be a nonempty finite vector")
    for name, value in (("horizon", horizon), ("wall_seconds", wall_seconds),
                        ("state_limit", state_limit), ("rtol", rtol), ("atol", atol)):
        if not np.isscalar(value) or not np.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be a finite positive scalar")
    if not np.isfinite(target_mse) or target_mse < 0:
        raise ValueError("target_mse must be finite and nonnegative")
    if not np.isscalar(max_step) or np.isnan(max_step) or max_step <= 0:
        raise ValueError("max_step must be positive")
    if np.max(np.abs(initial)) > state_limit:
        raise ValueError("Initial state exceeds the configured state limit")

    def prediction(state):
        values = np.asarray(output(state), dtype=float)
        if values.shape != labels.shape or not np.isfinite(values).all():
            raise ValueError("Training output must be finite with the same shape as labels")
        return values

    def loss(state):
        with np.errstate(over="raise", invalid="raise"):
            return float(np.mean((prediction(state) - labels)**2))

    evaluations = 0
    last_trial_time = 0.

    def checked(time, state):
        nonlocal evaluations, last_trial_time
        if perf_counter() - started > wall_seconds:
            raise TimeoutError("Per-solve wall budget exceeded")
        if not np.isfinite(state).all() or np.max(np.abs(state)) > state_limit:
            raise FloatingPointError("Nonfinite/excessive state in RHS trial")
        evaluations += 1
        last_trial_time = float(time)
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            value = np.asarray(rhs(time, state), dtype=float)
        if value.shape != initial.shape or not np.isfinite(value).all():
            raise FloatingPointError("Nonfinite or incorrectly shaped derivative")
        return value

    times, states, interpolants = [0.], [initial.copy()], []
    target_times, target_states = [], []
    success, status, message = False, -1, "Integration did not start"
    failure = None
    accepted_steps = 0
    termination_reason = "numerical_failure"
    initial_loss = None
    try:
        initial_loss = loss(initial)
        previous_event = initial_loss - target_mse
        if previous_event <= 0:
            target_times.append(0.)
            target_states.append(initial.copy())
        if target_times and stop_at_target:
            success, status = True, 1
            message = "Training target already satisfied at initialization"
            termination_reason = "target"
        else:
            solver = DOP853(checked, 0., initial, float(horizon), rtol=rtol,
                            atol=atol, max_step=max_step)
            while solver.status == "running":
                step_message = solver.step()
                if solver.status == "failed":
                    message = str(step_message)
                    break
                # Commit immediately after a successful step, before extra
                # RHS calls needed to construct the DOP853 interpolant.
                accepted_steps += 1
                times.append(float(solver.t))
                states.append(solver.y.copy())
                interpolants.append(None)
                dense_step = solver.dense_output()
                interpolants[-1] = dense_step
                current_event = loss(solver.y) - target_mse
                if not target_times and previous_event > 0 and current_event <= 0:
                    epsilon = np.finfo(float).eps
                    target_time = float(brentq(
                        lambda time: loss(dense_step(time)) - target_mse,
                        times[-2], times[-1], xtol=4 * epsilon, rtol=4 * epsilon))
                    target_state = np.asarray(dense_step(target_time)).copy()
                    target_times.append(target_time)
                    target_states.append(target_state)
                    if stop_at_target:
                        if target_time == times[-2]:
                            times.pop()
                            states.pop()
                            interpolants.pop()
                        else:
                            times[-1] = target_time
                            states[-1] = target_state.copy()
                        success, status = True, 1
                        message = "A training-target termination event occurred"
                        termination_reason = "target"
                        break
                previous_event = current_event
            else:
                if solver.status == "finished":
                    success, status = True, 0
                    message = "The solver reached the end of the integration interval"
                    termination_reason = "horizon"
    except (TimeoutError, FloatingPointError, ValueError, OverflowError, RuntimeError) as exc:
        failure = repr(exc)
        message = str(exc)
        termination_reason = "timeout" if isinstance(exc, TimeoutError) else "numerical_failure"

    elapsed = perf_counter() - started
    solution = FitSolution(times, states, interpolants, success=success,
                           status=status, message=message, nfev=evaluations,
                           target_times=target_times, target_states=target_states,
                           wall_seconds=elapsed)
    if success and target_times:
        final_time, final = target_times[0], target_states[0].copy()
    else:
        final_time, final = times[-1], states[-1].copy()
    record = dict(success=success, message=message, reached_target=bool(target_times),
                  target_time=target_times[0] if target_times else None,
                  fit_time=float(final_time), evaluation_time=float(final_time),
                  integrated_to=float(times[-1]), interpolation_to=solution.interpolation_to,
                  initial_mse=initial_loss, nfev=evaluations, accepted_steps=accepted_steps,
                  solver_seconds=elapsed, termination_reason=termination_reason,
                  final_state_is_accepted=True, last_state_is_accepted=True,
                  last_accepted_time=float(times[-1]), last_rhs_trial_time=last_trial_time,
                  target_mse=float(target_mse), horizon=float(horizon),
                  rtol=float(rtol), atol=float(atol), wall_limit_seconds=float(wall_seconds),
                  state_limit=float(state_limit))
    try:
        final_output = prediction(final)
        final_loss = loss(final)
        record.update(training_output=final_output.tolist(), training_mse=final_loss,
                      training_rms=float(np.sqrt(final_loss)))
        solution.final_loss = final_loss
    except (ValueError, FloatingPointError, OverflowError) as exc:
        record.update(training_output=None, training_mse=None, training_rms=None,
                      endpoint_output_error=repr(exc))
        solution.final_loss = None
    if failure is not None:
        record["error"] = failure
    return solution, final, record

# Standalone task generation, experiments, serialization and prediction.
# These helpers do not change the numerical model above.
import argparse
import hashlib
import json
import platform
import resource
import signal
import sys
import time
from pathlib import Path

TASK_NAMES = ('two_point', 'close_pairs', 'quadrant_alternating',
              'harmonic3_full', 'harmonic5_full', 'harmonic5_arc')


def circle_task(name):
    """Fixed, odd-compatible tasks. U contains normalized input columns."""
    target_kind = None
    if name == 'two_point':
        angles = np.array([10., 125.]); y = np.array([1., -1.])
    elif name == 'close_pairs':
        angles = np.array([-1., 1., 59., 61., 119., 121.])
        y = np.array([-1., 1., 1., -1., -1., 1.]); target_kind = 'close_pairs'
    elif name == 'quadrant_alternating':
        angles = 5. + 10*np.arange(8); y = (-1.)**np.arange(8)
    elif name == 'harmonic3_full':
        angles = 7. + 30*np.arange(12); target_kind = 'harmonic3'
        y = target_values(target_kind, angles)
    elif name == 'harmonic5_full':
        angles = 7. + 22.5*np.arange(16); target_kind = 'harmonic5'
        y = target_values(target_kind, angles)
    elif name == 'harmonic5_arc':
        angles = 10. + 10*np.arange(8); target_kind = 'harmonic5'
        y = target_values(target_kind, angles)
    else:
        raise ValueError('Unknown task: '+name)
    return dict(angles=angles, U=circle_inputs(angles, degrees=True).T,
                y=y, target_kind=target_kind)


def target_values(kind, degrees):
    radians = np.deg2rad(degrees)
    if kind == 'close_pairs':
        return np.tanh(3*np.sin(3*radians)/np.sin(np.deg2rad(3)))/np.tanh(3)
    if kind in ('harmonic3','harmonic5'):
        return np.sqrt(2)*np.sin(int(kind[-1])*radians)
    raise ValueError('This task has no asserted whole-circle target')


def _rms(a):
    return float(np.sqrt(np.mean(np.asarray(a)**2)))


def _json(path, value):
    with Path(path).open('x') as f:
        json.dump(value, f, indent=2, allow_nan=False)
        f.write('\n')


def _array_hash(arrays):
    h = hashlib.sha256()
    for key, value in sorted(arrays.items()):
        a=np.ascontiguousarray(value)
        h.update(key.encode()); h.update(str(a.shape).encode()); h.update(a.tobytes())
    return h.hexdigest()


def _provenance():
    source=Path(__file__).resolve()
    protocol=source.with_name('SCALAR_STANDALONE_PROTOCOL.md')
    import scipy
    return dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                protocol_sha256=hashlib.sha256(protocol.read_bytes()).hexdigest() if protocol.exists() else None,
                python=sys.version,numpy=np.__version__,scipy=scipy.__version__,
                platform=platform.platform(),command=sys.argv,cwd=os.getcwd(),
                threads={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')})


def _fields(weights, U):
    h1=np.tanh(weights['w']@U); h2=np.tanh(weights['W2']@h1)
    h3=np.tanh(weights['W3']@h2)
    d3=weights['c'][:,None]*(1-h3*h3)
    d2=(weights['W3'].T@d3)*(1-h2*h2)
    d1=(weights['W2'].T@d2)*(1-h1*h1)
    return (h1,h2,h3),(d1,d2,d3)


def _representation_diagnostics(weights, initial, decoder, U):
    """Post-fit projection tests only. No dense quantity trains the candidate."""
    bases=[decoder['Q'+str(i)] for i in (1,2,3)]
    original=dict(w=initial.w,W2=initial.W20,W3=initial.W30,c=initial.c)
    hs,ds=_fields(weights,U); h0,_=_fields(original,U)
    result={'hidden':[], 'middle':[]}
    for Q,h,d,old in zip(bases,hs,ds,h0):
        project=lambda v:Q@(Q.T@v)/Q.shape[0]
        result['hidden'].append(dict(movement_rms=_rms(h-old),
            activation_escape_rms=_rms(h-project(h)),
            movement_escape_rms=_rms((h-old)-project(h-old)),
            backward_escape_relative=float(np.linalg.norm(d-project(d))/max(np.linalg.norm(d),1e-30))))
    for layer in (2,3):
        D=weights['W'+str(layer)]-original['W'+str(layer)]
        Q=bases[layer-1]; prev=bases[layer-2]; n=Q.shape[0]; rank=Q.shape[1]
        projection=Q@(Q.T@D@prev)@prev.T/n**2
        singular=np.linalg.svd(D,compute_uv=False); norm=float(np.linalg.norm(D))
        outside=float(np.linalg.norm(D-projection))
        tail=float(np.linalg.norm(singular[rank:]))
        result['middle'].append(dict(increment_frobenius=norm,fixed_span_error=outside,
            fixed_span_relative=outside/max(norm,1e-30),best_rank_error=tail,
            best_rank_relative=tail/max(norm,1e-30)))
    return result


def _save_scalar_tables(folder, model, decoder):
    arrays=dict(U=model.U,y=model.y,Uall=model.Uall,C2=model.C2,C3=model.C3,
                initial=model.initial)
    for i in range(3):
        arrays['product'+str(i+1)]=model.products[i]
        arrays['constant'+str(i+1)]=model.constants[i]
    np.savez_compressed(folder/'runtime_tables.npz',**arrays)
    np.savez_compressed(folder/'decoder.npz',**decoder)


def _alarm(signum, frame):
    raise TimeoutError('Preparation exceeded its 30-second cap')


def run_group(out, task, width=64, seed=20260920,
              models=('dense','pop1','pop3','scalar12','scalar24','scalar40'),
              refined=False, regression=False, horizon=1000., wall_seconds=30.):
    """Train one matched group, retaining dense interpolants only in memory."""
    for name in models:
        if name == 'dense':
            continue
        prefix = 'scalar' if name.startswith('scalar') else 'pop' if name.startswith('pop') else ''
        suffix = name[len(prefix):] if prefix else ''
        if not suffix.isdecimal() or int(suffix) < 1:
            raise ValueError('Model names must be dense, scalar<RANK>, or pop<ORDER>')
        if prefix == 'scalar' and int(suffix) > width:
            raise ValueError('Scalar rank cannot exceed width')
    group_start=time.perf_counter(); cpu_start=time.process_time()
    out=Path(out); out.mkdir(parents=True,exist_ok=False)
    data=circle_task(task); U,y=data['U'],data['y']
    passive=np.array([30.,60.,90.]) if regression else np.array([12.5,57.5,102.5,157.5])
    queries=circle_inputs(passive,degrees=True).T
    circle_degrees=(np.arange(4096)+.5)*360/4096
    circle_U=circle_inputs(circle_degrees,degrees=True).T
    initial=initialize(width,seed)
    initialization=dict(w=initial.w,W20=initial.W20,W30=initial.W30,c=initial.c)
    np.savez_compressed(out/'inputs.npz',**initialization,U=U,y=y,angles=data['angles'],
                        passive_degrees=passive,circle_degrees=circle_degrees)
    provenance=_provenance(); provenance['initialization_sha256']=_array_hash(initialization)
    _json(out/'config.json',dict(task=task,width=width,seed=seed,models=list(models),
          refined=refined,regression=regression,horizon=horizon,wall_seconds=wall_seconds,
          target_kind=data['target_kind'],provenance=provenance))
    dense_cache=None; records={}
    for name in models:
        cell_start=time.perf_counter(); folder=out/name; folder.mkdir()
        rt,at=(1e-9,1e-11) if refined else (1e-7,1e-9)
        prep=time.perf_counter(); decoder=None
        old_handler=signal.signal(signal.SIGALRM,_alarm); signal.alarm(30)
        try:
            if name.startswith('scalar'):
                rank=int(name[6:])
                model=ResponseBasisSystem(U,y,queries,rank,preparation_seconds=30.)
                z0=model.initialize(initial.w,initial.W20,initial.W30,initial.c)
                decoder=model.detach_decoder(); train=model.training_output
                output=model.outputs
            else:
                model=(DenseReference(U.T,y,initial) if name=='dense' else
                       PopulationReference(U.T,y,initial,order=int(name[3:])))
                z0=model.initial.copy(); train=lambda z:model.predict(z,U.T)
                output=lambda z:model.predict(z,np.column_stack((U,queries)).T)
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024>3*1024**3:
                raise MemoryError('3GiB preparation RSS cap')
            prep_seconds=time.perf_counter()-prep
        except Exception as exc:
            rec=dict(success=False,reached_target=False,phase='preparation',error=repr(exc),
                     preparation_seconds=time.perf_counter()-prep,model=name)
            _json(folder/'result.json',rec); records[name]=rec
            continue
        finally:
            signal.alarm(0); signal.signal(signal.SIGALRM,old_handler)
        sol,final,rec=fit(model.rhs,z0,train,y,horizon=horizon,rtol=rt,atol=at,
                          wall_seconds=wall_seconds)
        rec.update(model=name,task=task,width=width,seed=seed,refined=refined,
                   preparation_seconds=prep_seconds,state_count=len(z0),
                   phase='integration',provenance=provenance)
        weights=decode(final,decoder) if decoder is not None else model.physical(final)
        values=output(final)
        decoded=physical_outputs(weights,np.column_stack((U,queries)))
        curve=physical_outputs(weights,circle_U)
        rec.update(outputs=values.tolist(),decoded_outputs=decoded.tolist(),
                   decoded_training_rms=_rms(decoded[:len(y)]-y),
                   internal_decoder_rms=_rms(decoded-values))
        rec['feature_movement_rms']=[_rms(a-b) for a,b in zip(
            _fields(weights,U)[0],_fields(dict(w=initial.w,W2=initial.W20,W3=initial.W30,c=initial.c),U)[0])]
        if data['target_kind'] is not None:
            target=target_values(data['target_kind'],circle_degrees)
            rec['target_circle_rms']=_rms(curve-target)
        else: target=np.full_like(circle_degrees,np.nan)
        if task=='harmonic5_arc':
            inside=(circle_degrees%180>=10)&(circle_degrees%180<=80)
            rec['target_inside_rms']=_rms((curve-target)[inside])
            rec['target_outside_rms']=_rms((curve-target)[~inside])
        if name=='dense':
            dense_cache=(model,sol,final,rec,curve.copy(),values.copy(),weights)
        elif dense_cache is not None:
            dm,ds,df,dr,dc,dv,dw=dense_cache
            err=curve-dc
            rec.update(circle_dense_rms=_rms(err),circle_dense_max=float(np.max(np.abs(err))),
                       passive_dense_rms=_rms(values[len(y):]-dv[len(y):]),
                       passive_dense_max=float(np.max(np.abs(values[len(y):]-dv[len(y):]))),
                       comparison_fitted=bool(rec['success'] and rec['reached_target'] and dr['success'] and dr['reached_target']))
            rec['good_agreement']=bool(rec['comparison_fitted'] and rec['decoded_training_rms']<=.05 and rec['circle_dense_rms']<=.05)
            common=min(rec['evaluation_time'],dr['evaluation_time'],sol.interpolation_to,ds.interpolation_to)
            if common>=0:
                candidate=output(sol.sol(common))
                reference=dm.predict(ds.sol(common),np.column_stack((U,queries)).T)
                rec['common_time']=float(common)
                rec['common_time_passive_rms']=_rms(candidate[len(y):]-reference[len(y):])
                np.savez_compressed(folder/'common_time.npz',time=common,candidate=candidate,reference=reference)
            if task=='harmonic5_arc':
                rec['dense_inside_rms']=_rms(err[inside]); rec['dense_outside_rms']=_rms(err[~inside])
            if decoder is not None:
                rec['dense_fixed_basis_diagnostics']=_representation_diagnostics(dw,initial,decoder,U)
        if decoder is not None:
            rec['statistics']=model.statistics();_save_scalar_tables(folder,model,decoder)
        else:
            rec['fixed_initialization_bytes']=sum(v.nbytes for v in initialization.values())
        np.savez_compressed(folder/'weights.npz',**weights)
        np.savez_compressed(folder/'checkpoint.npz',initial=z0,final=final)
        np.savez_compressed(folder/'predictions.npz',training=values[:len(y)],passive=values[len(y):],
             decoded_training=decoded[:len(y)],decoded_passive=decoded[len(y):],circle=curve,target=target)
        trace_end=min(rec['evaluation_time'],sol.interpolation_to)
        trace_times=np.linspace(0,trace_end,121)
        trace_values=np.array([output(sol.sol(t)) for t in trace_times])
        np.savez_compressed(folder/'trace.npz',times=trace_times,outputs=trace_values)
        rec['cell_wall_seconds']=time.perf_counter()-cell_start
        rec['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
        _json(folder/'result.json',rec); records[name]=rec
        print(json.dumps({k:rec.get(k) for k in ('task','seed','model','termination_reason',
              'training_rms','decoded_training_rms','circle_dense_rms','good_agreement','solver_seconds')}),flush=True)
        if name!='dense': del sol,model
    _json(out/'group.json',dict(worker_wall_seconds=time.perf_counter()-group_start,
          worker_cpu_seconds=time.process_time()-cpu_start,models=list(records),provenance=provenance))
    return records


def self_check():
    """Small deterministic algebra tests; no original modules or neural fits."""
    start=time.process_time(); init=initialize(7,193);U=circle_inputs([10,125],degrees=True).T
    y=np.array([.7,-1.2]);query=circle_inputs([60],degrees=True).T
    dense=DenseReference(U.T,y,init); z=dense.initial;v=dense.rhs(0,z); eps=1e-6
    observed=(dense.fields(z+eps*v)['loss']-dense.fields(z-eps*v)['loss'])/(2*eps)
    velocity=dense.unpack(v)
    expected=-sum(np.sum(a*a)/(7 if k in ('w','c') else 1) for k,a in velocity.items())
    dense_error=abs(observed-expected)
    assert dense_error<1e-7
    errors=[]
    for rank in (1,4,7):
        model=ResponseBasisSystem(U,y,query,rank);a=model.initialize(init.w,init.W20,init.W30,init.c)
        model.detach_decoder();d=model.rhs(0,a);s=model.unpack(a);ds=model.unpack(d)
        outdot=ds['c']@s['h3'][:,:2]+s['c']@ds['h3'][:,:2]
        observed=2*np.mean((model.training_output(a)-y)*outdot)
        expected=-sum(np.sum(ds[k]**2) for k in ('dw','B2','B3','c'))
        errors.append(abs(observed-expected));assert errors[-1]<1e-10
    for order in (1,3):
        pop=PopulationReference(U.T,y,init,order)
        pv=pop.physical_velocity(pop.initial)
        assert max(np.max(np.abs(pv[k]-velocity[k])) for k in velocity)<1e-12
    for task in TASK_NAMES:
        data=circle_task(task);assert abs(_rms(data['y'])-1)<1e-12
        assert np.max(np.abs(np.sum(data['U']**2,axis=0)-1))<1e-12
    return dict(status='PASS',dense_directional_error=dense_error,
                loss_dissipation_max=max(errors),cpu_seconds=time.process_time()-start)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('self-check')
    train=sub.add_parser('fit');train.add_argument('--task',choices=TASK_NAMES,default='two_point')
    train.add_argument('--width',type=int,default=64);train.add_argument('--seed',type=int,default=20260920)
    train.add_argument('--models',nargs='+',default=['dense','scalar12','scalar24','scalar40'])
    train.add_argument('--out',type=Path,required=True);train.add_argument('--refined',action='store_true')
    train.add_argument('--horizon',type=float,default=1000.);train.add_argument('--wall-seconds',type=float,default=30.)
    pred=sub.add_parser('predict');pred.add_argument('--model',type=Path,required=True)
    pred.add_argument('--angles',type=float,nargs='+');pred.add_argument('--circle',type=int)
    pred.add_argument('--out',type=Path)
    a=p.parse_args()
    if a.command=='self-check':print(json.dumps(self_check(),indent=2))
    elif a.command=='fit':run_group(a.out,a.task,a.width,a.seed,a.models,a.refined,
                                    horizon=a.horizon,wall_seconds=a.wall_seconds)
    else:
        if (a.angles is None)==(a.circle is None):p.error('Specify exactly one of --angles or --circle')
        if a.circle is not None and a.circle < 1:p.error('--circle must be positive')
        degrees=np.array(a.angles) if a.angles is not None else (np.arange(a.circle)+.5)*360/a.circle
        with np.load(a.model,allow_pickle=False) as archive:weights=dict(archive)
        outputs=physical_outputs(weights,circle_inputs(degrees,degrees=True).T)
        if a.out is not None:
            with a.out.open('xb') as handle:np.savez_compressed(handle,degrees=degrees,outputs=outputs)
        else:print(json.dumps(dict(degrees=degrees.tolist(),outputs=outputs.tolist())))


if __name__=='__main__':main()
