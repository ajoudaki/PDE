"""Initialization-only polynomial output potential with scalar gradient flow.

Neuron arrays are used by ``initialize`` only. Detach ``model.decoder`` before
evolution; it is a separate terminal parameter decoder, never read by ``rhs``.
The canonical mobility is whitened before selecting active gradient/curvature
directions. Passive inputs do not participate in basis selection or evolution.
"""
from itertools import product
from time import perf_counter
import resource

import numpy as np


def _shapes(n):
    return ((n, 2), (n, n), (n, n), (n,))


def _pack(parts):
    return np.concatenate([np.asarray(a).ravel() for a in parts])


def _unpack(theta, n):
    result, start = [], 0
    for shape in _shapes(n):
        stop = start + int(np.prod(shape))
        result.append(np.asarray(theta)[start:stop].reshape(shape))
        start = stop
    return tuple(result)


def mobility_sqrt(n):
    return _pack((np.full((n, 2), np.sqrt(n)), np.ones((n, n)),
                  np.ones((n, n)), np.full(n, np.sqrt(n))))


def output_gradient_hvp(theta, n, input_vector, direction=None):
    """f, Euclidean parameter gradient, and optional exact parameter HVP."""
    w, W2, W3, c = _unpack(theta, n)
    u = np.asarray(input_vector, dtype=float)
    h1 = np.tanh(w @ u)
    h2 = np.tanh(W2 @ h1)
    h3 = np.tanh(W3 @ h2)
    a1, a2, a3 = 1-h1*h1, 1-h2*h2, 1-h3*h3
    d3 = c*a3
    b2 = W3.T @ d3
    d2 = a2*b2
    b1 = W2.T @ d2
    d1 = a1*b1
    gradient = _pack((np.outer(d1, u), np.outer(d2, h1),
                      np.outer(d3, h2), h3))/n
    value = float(c @ h3/n)
    if direction is None:
        return value, gradient, None
    dw, dW2, dW3, dc = _unpack(direction, n)
    dh1 = a1*(dw @ u)
    dh2 = a2*(dW2 @ h1 + W2 @ dh1)
    dh3 = a3*(dW3 @ h2 + W3 @ dh2)
    dd3 = dc*a3 - 2*c*h3*dh3
    dd2 = -2*h2*dh2*b2 + a2*(dW3.T @ d3 + W3.T @ dd3)
    dd1 = -2*h1*dh1*b1 + a1*(dW2.T @ d2 + W2.T @ dd2)
    hvp = _pack((np.outer(dd1, u),
                 np.outer(dd2, h1)+np.outer(d2, dh1),
                 np.outer(dd3, h2)+np.outer(d3, dh2), dh3))/n
    return value, gradient, hvp


def _orthonormalize(columns, relative_tolerance=1e-11):
    basis, rejected = [], 0
    for column in columns:
        original_norm = np.linalg.norm(column)
        if original_norm == 0:
            rejected += 1
            continue
        v = column.copy()/original_norm
        for _ in range(2):
            for q in basis:
                v -= q*np.dot(q, v)
        norm = np.linalg.norm(v)
        if norm <= relative_tolerance:
            rejected += 1
        else:
            basis.append(v/norm)
    if not basis:
        raise ValueError("All active initialization gradients vanished")
    return np.column_stack(basis), rejected


class _JetCompiler:
    """Small multivariate monomial arithmetic used only during initialization."""
    def __init__(self, rank, degree):
        self.rank, self.degree = rank, degree
        self.exponents = np.array(sorted(
            (a for a in product(range(degree+1), repeat=rank) if sum(a) <= degree),
            key=lambda a: (sum(a), a)), dtype=np.int16)
        self.lookup = {tuple(a): i for i, a in enumerate(self.exponents)}
        self.count = len(self.exponents)
        self.shifts = []
        for k in range(rank):
            pairs = []
            for i, a in enumerate(self.exponents):
                b = a.copy()
                b[k] += 1
                if sum(b) <= degree:
                    pairs.append((i, self.lookup[tuple(b)]))
            self.shifts.append(tuple(np.array(a, dtype=int) for a in zip(*pairs)))
        pairs = []
        for i, a in enumerate(self.exponents):
            for j, b in enumerate(self.exponents):
                if sum(a+b) <= degree:
                    pairs.append((i, j, self.lookup[tuple(a+b)]))
        self.left, self.right, self.target = (np.array(a, dtype=int) for a in zip(*pairs))

    def multiply(self, a, b):
        out = np.zeros_like(a)
        np.add.at(out, (np.arange(len(a))[:, None], self.target[None, :]),
                  a[:, self.left]*b[:, self.right])
        return out

    def affine_action(self, weight, directions, h):
        out = weight @ h
        for k, (source, target) in enumerate(self.shifts):
            out[:, target] += directions[k] @ h[:, source]
        return out

    def tanh(self, a):
        h0 = np.tanh(a[:, 0])
        gate = 1-h0*h0
        delta = a.copy()
        delta[:, 0] = 0.
        out = gate[:, None]*delta
        out[:, 0] = h0
        if self.degree >= 2:
            square = self.multiply(delta, delta)
            out -= (h0*gate)[:, None]*square
        if self.degree >= 3:
            cube = self.multiply(square, delta)
            out += (gate*(3*h0*h0-1)/3)[:, None]*cube
        return out

    def forward(self, theta0, directions, n, u):
        weights = _unpack(theta0, n)
        split = [_unpack(directions[:, k], n) for k in range(self.rank)]
        h = np.zeros((2, self.count))
        h[:, 0] = u
        for layer in range(3):
            h = self.tanh(self.affine_action(weights[layer],
                          [s[layer] for s in split], h))
        out = weights[3] @ h/n
        for k, (source, target) in enumerate(self.shifts):
            out[target] += split[k][3] @ h[:, source]/n
        return out


class PolynomialPotentialSystem:
    def __init__(self, U, y, Utest, rank_mode="gradient", degree=2,
                 preparation_seconds=180., max_memory_bytes=3*1024**3):
        self.U = np.asarray(U, dtype=float).copy()
        self.y = np.asarray(y, dtype=float).copy()
        self.Utest = (np.empty((2, 0)) if Utest is None
                      else np.asarray(Utest, dtype=float).copy())
        if self.Utest.ndim == 1:
            self.Utest = self.Utest[:, None]
        if (self.y.ndim != 1 or not self.y.size or self.U.shape != (2, len(self.y))
                or self.Utest.ndim != 2 or self.Utest.shape[0] != 2):
            raise ValueError("Expected active/passive inputs (2,M)/(2,Q), labels (M,)")
        if not all(np.isfinite(a).all() for a in (self.U, self.y, self.Utest)):
            raise ValueError("Nonfinite input or label")
        if rank_mode not in ("gradient", "curvature") or degree not in (1, 2, 3):
            raise ValueError("Unsupported rank mode or degree")
        self.rank_mode, self.degree = rank_mode, int(degree)
        self.M = len(self.y)
        self.noutputs = self.M+self.Utest.shape[1]
        self.preparation_seconds = float(preparation_seconds)
        self.max_memory_bytes = int(max_memory_bytes)

    def _check_preparation(self, started):
        if perf_counter()-started > self.preparation_seconds:
            raise TimeoutError("Polynomial-potential preparation exceeded time cap")
        if 1024*resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > self.max_memory_bytes:
            raise MemoryError("Polynomial-potential preparation exceeded RSS cap")

    def initialize(self, w, W20, W30, c):
        started = perf_counter()
        arrays = tuple(np.asarray(a, dtype=float) for a in (w, W20, W30, c))
        n = arrays[-1].size
        if any(a.shape != shape for a, shape in zip(arrays, _shapes(n))):
            raise ValueError("Inconsistent initialization shapes")
        if not all(np.isfinite(a).all() for a in arrays):
            raise ValueError("Nonfinite initialization")
        theta0, sqrtD = _pack(arrays), mobility_sqrt(n)
        gradients = [sqrtD*output_gradient_hvp(theta0, n, u)[1] for u in self.U.T]
        columns = list(gradients)
        if self.rank_mode == "curvature":
            for u in self.U.T:
                for g in gradients:
                    columns.append(sqrtD*output_gradient_hvp(theta0, n, u, sqrtD*g)[2])
                    self._check_preparation(started)
        Q, self.rejected_directions = _orthonormalize(columns)
        self.dimension = Q.shape[1]
        parameter_directions = sqrtD[:, None]*Q
        compiler = _JetCompiler(self.dimension, self.degree)
        coefficients = []
        for u in np.column_stack((self.U, self.Utest)).T:
            coefficients.append(compiler.forward(theta0, parameter_directions, n, u))
            self._check_preparation(started)
        self.exponents = compiler.exponents
        self.coefficients = np.array(coefficients)
        self.gradient_coefficients = np.zeros((self.noutputs, self.dimension, compiler.count))
        for j, exponent in enumerate(self.exponents):
            for k, power in enumerate(exponent):
                if power:
                    lower = exponent.copy()
                    lower[k] -= 1
                    self.gradient_coefficients[:, k, compiler.lookup[tuple(lower)]] += power*self.coefficients[:, j]
        self.decoder = dict(theta0=theta0, parameter_directions=parameter_directions, width=n)
        self.initialization_seconds = perf_counter()-started
        self.basis_orthogonality_error = float(np.max(np.abs(Q.T @ Q-np.eye(self.dimension))))
        self.initial = np.zeros(self.dimension)
        self._check_preparation(started)
        return self.initial.copy()

    def _monomials(self, z):
        z = np.asarray(z, dtype=float)
        if z.shape != (self.dimension,):
            raise ValueError("Scalar state has wrong shape")
        return np.prod(np.power(z[None, :], self.exponents), axis=1)

    def outputs(self, z):
        return self.coefficients @ self._monomials(z)

    def output_gradients(self, z):
        return np.einsum("irk,k->ir", self.gradient_coefficients, self._monomials(z))

    def training_output(self, z):
        return self.outputs(z)[:self.M]

    def rhs(self, t, z):
        del t
        monomials = self._monomials(z)
        residual = self.coefficients[:self.M] @ monomials-self.y
        gradients = np.einsum("irk,k->ir", self.gradient_coefficients[:self.M], monomials)
        return -(2/self.M)*(residual @ gradients)

    def statistics(self):
        tables = (self.coefficients, self.gradient_coefficients, self.exponents)
        return dict(kind="polynomial_potential", rank_mode=self.rank_mode,
                    degree=self.degree, dimension=self.dimension,
                    output_count=self.noutputs, monomials=len(self.exponents),
                    polynomial_coefficients=int(self.coefficients.size),
                    fixed_table_entries=int(sum(a.size for a in tables)),
                    fixed_table_bytes=int(sum(a.nbytes for a in tables)),
                    decoder_attached="decoder" in self.__dict__,
                    initialization_seconds=self.initialization_seconds,
                    basis_orthogonality_error=self.basis_orthogonality_error,
                    rejected_directions=self.rejected_directions,
                    peak_rss_bytes=1024*resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    @staticmethod
    def decode(z, decoder):
        theta = decoder["theta0"]+decoder["parameter_directions"] @ np.asarray(z)
        return dict(zip(("w", "W2", "W3", "c"), _unpack(theta, int(decoder["width"]))))


def create(Utrain, y, Utest, rank_mode="gradient", degree=2, **kwargs):
    return PolynomialPotentialSystem(Utrain, y, Utest, rank_mode, degree, **kwargs)


def decode(z, decoder):
    return PolynomialPotentialSystem.decode(z, decoder)
