"""Fixed initial-response-basis approximation of canonical dense gradient flow.

Frozen basis policy (2026-09-25, before algebra or fitting checks): for each
layer form TRAINING-ONLY columns [h_a, delta_a, hdot_a] in that group order and
sample order; append c0 on layer 3. Center and empirical-RMS-normalize these
marks. Form the ordered feature bank [marks, pairwise products i<=j in
lexicographic order, individual cubic powers]. Center/RMS-normalize each
feature again. Keep the constant first and leading left singular vectors of
this one feature bank, oriented by the largest-magnitude entry of each right
singular vector. If the bank is genuinely rank deficient, twice-orthogonalize
Gaussian vectors generated with seed 20260925+layer until complete; report
their count. All dependence thresholds use 64*machine_epsilon times the
relevant dimension. The feature bank is independent of requested rank, hence
ranks 4,8,12,16 are nested; width32 uses the identical policy. Rank16 at width16
is only an implementation control. No passive input enters basis selection.

Approximation: replace EACH vector multiplication by its projection, and each
initialized operator action by its same-operator projection. This is not exact
Galerkin projection of the whole composed vector field. The fixed tensors
encode actual initialized forward/adjoint correlations in the retained
subspaces; complement leakage is discarded. No response-memory/P truncation
is used. Dynamic first-weight coefficients are included solely for decoding.

Runtime state: dw, B2, B3, c, h1, h2, h3 are ordinary mode coefficients.
Q^T Q/n=I, W_l=W_l0+Q_l B_l Q_prev^T/n, w=w0+Q1 dw. initialize temporarily
sets .decoder; the caller MUST detach it before fitting. No neuron arrays or
initialized matrix actions occur in rhs. Full rank is a control, not evidence
of compression. decode reconstructs arrays for validation only; its nonlinear
network output can differ from the internally evolved passive response.

Finite-horizon statement: for the exact polynomial response lift F, its
linear reconstruction Psi, and the coefficient law G, a common bounded
region with Lipschitz constant Lambda gives
 error(t) <= exp(Lambda*t)*initial_projection_error
             + integral exp(Lambda*(t-s))*||F(Psi*z)-Psi*G(z)|| ds.
This conditional bound separates source and stability errors; no rank-small
error or width-uniform convergence is asserted. Product defects can separately
be certified by fourth-order initial feature Grams, and operator leakage by
the Gram of W0 Q_prev-Q C, without runtime neuron arrays. Those optional
certificates are not computed by this bounded implementation.
"""

from time import perf_counter

import numpy as np


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
