"""Scalar contraction closure with direct passive outputs and hidden Grams.

Two or more tanh hidden layers, original activity clock, arbitrary finite P.
Only the symbolic tree algebra is imported from scalar_fourier_engine: there
are no angular fields, quadrature or Fourier coordinates in this model.
Compiler/evaluator use neuron arrays once. ScalarRuntime stores none.
"""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
import time
import numpy as np

from scalar_fourier_engine import (
    Templates, ScalarFourierSystem, CompilationLimit, node, field, size,
    canonical, differentiated_sites, nonconstant, primitive, one, add, scale,
    product, average, initialized_action, merge,
)


class DirectTemplates(Templates):
    """Exact finite-P response lift; third A/B field index encodes k*M+a."""

    def __init__(self, inputs, query_inputs, depth=2, order=1):
        super().__init__(np.asarray(inputs).T)
        self.depth, self.P = int(depth), int(order)
        both = np.concatenate((inputs, query_inputs), axis=0)
        self.gram = both @ both.T

    def moment(self, kind, layer, a, k=0):
        return super().moment(kind, layer, a + self.M*k)

    def endpoint(self, kind, layer, a):
        return add(*(scale(self.moment(kind, layer, a, k), 2*k+1, lp=1)
                     for k in range(self.P)))

    def matrix(self, layer, v, transpose=False):
        target = layer-1 if transpose else layer
        out = initialized_action(target, v)
        for a in range(self.M):
            for k in range(self.P):
                local = self.moment('B' if transpose else 'A', layer, a, k)
                pair = self.moment('A' if transpose else 'B', layer, a, k)
                out = add(out, scale(product(local, average(product(pair, v))),
                                     self.factor*(2*k+1), lp=1))
        return out

    @lru_cache(None)
    def delta(self, layer, a):
        if layer == self.depth:
            return product(primitive('c', layer), self.gate(layer, a))
        return product(self.gate(layer, a),
                       self.matrix(layer+1, self.delta(layer+1, a), True))

    def matrix_dot(self, layer, v):
        # Differentiating sum_k (2k+1) A_k B_k^T/L cancels transport:
        # Wdot=-2/M sum_a [r delta Bbar^T + rho Abar(h-Bbar)^T]/n.
        out = {}
        for a in range(self.M):
            A, B = self.endpoint('A', layer, a), self.endpoint('B', layer, a)
            pB = average(product(B, v))
            ph = average(product(primitive('h', layer-1, a), v))
            out = add(out,
                      scale(product(self.delta(layer, a), pB), self.factor, drive=a),
                      scale(product(A, ph), self.factor, drive=-1),
                      scale(product(A, pB), -self.factor, drive=-1))
        return out

    def rhs(self, species):
        if species in self.cache:
            return self.cache[species]
        kind, layer, index = species
        if kind == 'h':
            out = self.h_dot(layer, index)
        elif kind == 'c':
            out = add(*(scale(primitive('h', self.depth, a), self.factor, drive=a)
                        for a in range(self.M)))
        elif kind in ('A', 'B'):
            k, a = divmod(index, self.M)
            source = (scale(self.delta(layer, a), drive=a) if kind == 'A'
                      else scale(primitive('h', layer-1, a), drive=-1))
            out = add(source, scale(self.moment(kind, layer, a, k), -k, drive=-1, lp=1),
                      *(scale(self.moment(kind, layer, a, j), -(2*j+1),
                              drive=-1, lp=1) for j in range(k)))
        else:
            raise KeyError(species)
        self.cache[species] = out
        return out


class FieldEvaluator:
    """Only initialization/audits use arrays; each edge is the actual W0."""

    def __init__(self, fields, weights):
        self.fields = fields
        self.weights = weights
        self.n = len(next(iter(fields.values())))
        self.cache, self.means = {}, {}

    def rooted(self, tree):
        if tree not in self.cache:
            value = np.ones(self.n)
            for species in tree[1]:
                value *= self.fields[species]
            if np.any(value):
                for child in tree[2]:
                    W = self.weights[max(tree[0], child[0])-2]
                    value *= (W if tree[0] > child[0] else W.T) @ self.rooted(child)
            self.cache[tree] = value
        return self.cache[tree]

    def tree(self, tree):
        if tree not in self.means:
            self.means[tree] = float(np.mean(self.rooted(tree)))
        return self.means[tree]

    def expression(self, expression, residual, rho, length):
        result = np.zeros(self.n)
        for (root, forest, cosine, sine, drive, power), coeff in expression.items():
            assert cosine == sine == 0
            value = coeff*self.rooted(root)
            for tree in forest:
                value = value*self.tree(tree)
            result += value*(rho if drive == -1 else residual[drive] if drive >= 0 else 1)/length**power
        return result


def parent_fields(parent, state, query_inputs):
    """Lift an independently evolved population state for initialization/audit."""
    q = parent.unpack(state)
    all_inputs = np.concatenate((parent.inputs, query_inputs), axis=0)
    h = parent.query_fields(state, all_inputs)['h']
    fields = {field('c', parent.depth): q['c']}
    for layer, values in enumerate(h, 1):
        for a in range(len(all_inputs)):
            fields[field('h', layer, a)] = values[:, a]
    for layer in range(2, parent.depth+1):
        for k in range(parent.P):
            for a in range(parent.M):
                for kind in ('A', 'B'):
                    fields[field(kind, layer, k*parent.M+a)] = q[f'{kind}{layer}'][k, :, a]
    return FieldEvaluator(fields, parent.initialization.W0)


@dataclass
class ScalarRuntime:
    """Scalar-only autonomous solver, independent of width after construction."""
    table: dict
    labels: np.ndarray
    output_indices: np.ndarray
    query_indices: np.ndarray
    gram_indices: np.ndarray
    caps: np.ndarray
    initial: np.ndarray
    clip: bool = True

    @property
    def dimension(self):
        return len(self.initial)

    def reported(self, z):
        q = np.asarray(z)[:-1]
        return np.clip(q, -self.caps, self.caps) if self.clip else q

    def rhs(self, t, z):
        q = np.r_[self.reported(z), 1.]
        residual = q[self.output_indices]-self.labels
        rho = np.linalg.norm(residual)/np.sqrt(len(self.labels))
        tab = self.table
        drive = np.r_[1., rho, residual]
        products = np.ones(len(tab['coefficients']))
        for column in tab['indices'].T:
            products *= q[column]
        values = tab['coefficients']*products*drive[tab['drives']]/z[-1]**tab['powers']
        return np.r_[np.bincount(tab['rows'], weights=values, minlength=len(q)-1), rho]

    def observables(self, z):
        q = self.reported(z)
        return dict(train=q[self.output_indices], test=q[self.query_indices],
                    grams=q[self.gram_indices], clock=float(z[-1]))

    def array_bytes(self):
        return sum(a.nbytes for a in self.table.values()) + sum(
            a.nbytes for a in (self.labels, self.output_indices, self.query_indices,
                              self.gram_indices, self.caps, self.initial))


class ScalarCompiler(ScalarFourierSystem):
    """Reuse ordinary-tree grammar and table packing, with no angular block."""

    def __init__(self, inputs, labels, query_inputs, cutoff, *, order=1, depth=2,
                 max_patterns=12000, max_terms=1000000, compile_seconds=60.,
                 max_memory_bytes=int(1.5*1024**3), include_grams=True):
        self.inputs = np.asarray(inputs, float)
        self.query_inputs = np.asarray(query_inputs, float).reshape(-1, self.inputs.shape[1])
        self.U, self.y = self.inputs.T, np.asarray(labels, float)
        if self.inputs.shape != (len(self.y), 2) or not len(self.y):
            raise ValueError('Require nonempty circle inputs (m,2) and labels (m,)')
        if not all(np.isfinite(x).all() for x in (self.inputs, self.y, self.query_inputs)):
            raise ValueError('Nonfinite data')
        if cutoff < 3 or int(cutoff) != cutoff or order < 1 or int(order) != order or depth < 2:
            raise ValueError('Require integer K>=3,P>=1 and depth>=2')
        self.M, self.K, self.P, self.depth, self.J = len(self.y), int(cutoff), int(order), int(depth), 0
        self.training_patterns, self.angular_patterns = [], []
        self.training_index, self.angular_index = {}, {}
        self.training_rows, self.angular_rows = [], []
        self.dropped_terms = self.generated_terms = self.retained_terms = 0
        self.compile_started = time.monotonic()
        self.max_patterns, self.max_terms = max_patterns, max_terms
        self.compile_seconds, self.max_memory_bytes = compile_seconds, max_memory_bytes
        self.templates = DirectTemplates(self.inputs, self.query_inputs, self.depth, self.P)
        self._pending = deque()
        indices = [self._register(canonical(node(self.depth, [
            field('c', self.depth), field('h', self.depth, a)])), False)
            for a in range(self.M+len(self.query_inputs))]
        self.output_indices = np.array(indices[:self.M], dtype=np.int32)
        self.query_indices = np.array(indices[self.M:], dtype=np.int32)
        self.gram_indices = np.empty((self.depth, self.M, self.M), dtype=np.int32)
        if include_grams:
            for layer in range(1, self.depth+1):
                for a in range(self.M):
                    for b in range(a, self.M):
                        index = self._register(canonical(node(layer, [
                            field('h', layer, a), field('h', layer, b)])), False)
                        self.gram_indices[layer-1, a, b] = self.gram_indices[layer-1, b, a] = index
        else:
            self.gram_indices = np.empty((self.depth, 0, 0), dtype=np.int32)
        while self._pending:
            angular, index = self._pending.popleft()
            assert not angular
            self.training_rows[index] = self._compile_row(self.training_patterns[index], False)
            self._check_limit()
        self.ntrain, self.nangular = len(self.training_patterns), 0
        self.dimension = self.ntrain+1
        self.train_table = self._table(self.training_rows, False)
        self.compile_time = time.monotonic()-self.compile_started

    def _compile_row(self, tree, angular=False):
        assert not angular
        terms = defaultdict(float)
        for rem, species, count in differentiated_sites(tree):
            for (root, forest, cc, ss, drive, lp), coef in self.templates.rhs(species).items():
                self.generated_terms += 1
                if self.generated_terms % 512 == 0:
                    self._check_limit()
                assert cc == ss == 0
                # Grade is independent of root choice. Prune before canonical
                # relabeling; this saves most work at low cutoff exactly.
                if size(rem)+size(root)-1 > self.K or any(size(t)>self.K for t in forest):
                    self.dropped_terms += 1
                    continue
                joined = canonical(merge(rem, root))
                trees = tuple(sorted(forest+((joined,) if nonconstant(joined) else ())))
                terms[(trees, drive, lp)] += count*coef
        row = []
        for (trees, drive, lp), coef in terms.items():
            if coef:
                row.append((coef, tuple(self._register(t, False) for t in trees), -1, drive, lp))
        self.retained_terms += len(row)
        return row

    def initialize(self, parent, horizon, *, clip=True):
        if parent.P != self.P or parent.depth != self.depth:
            raise ValueError('Parent/scalar P or depth mismatch')
        evaluator = parent_fields(parent, parent.initial, self.query_inputs)
        z = np.r_[[evaluator.tree(t) for t in self.training_patterns], 1.]
        caps, bounds = self.certified_caps(parent, horizon)
        if np.any(abs(z[:-1]) > caps*(1+1e-12)):
            raise AssertionError('Initial aggregate violates its certified bound')
        runtime = ScalarRuntime(
            {k:v.copy() for k,v in self.train_table.items()}, self.y.copy(),
            self.output_indices.copy(), self.query_indices.copy(),
            self.gram_indices.copy(), caps, z, clip)
        return runtime, bounds

    def certified_caps(self, parent, horizon):
        """Data-only all-order tanh bounds, tightened per tree by |W0| actions.

        ||c||^2 <= ||c0||^2+n*mean(y^2)*T, |f|<=||c||/sqrt(n).
        B_k entries <=L; A_{ell,k} entries <=sqrt(m)*(L-1)*B_delta[ell].
        The shifted Legendre polynomials satisfy |p_k|<=1 on their interval.
        """
        if horizon < 0:
            raise ValueError('Negative horizon')
        n, M, depth = parent.n, parent.M, parent.depth
        Y = np.sqrt(np.mean(self.y**2))
        c_norm = np.sqrt(np.dot(parent.initialization.c, parent.initialization.c)+n*Y*Y*horizon)
        rho_cap = c_norm/np.sqrt(n)+Y
        activity = horizon*rho_cap
        length = 1+activity
        delta = {depth:c_norm}
        for layer in range(depth, 1, -1):
            Wbound = np.linalg.norm(parent.initialization.W0[layer-2])+2*length*delta[layer]/np.sqrt(n)
            delta[layer-1] = Wbound*delta[layer]
        # Component c bound can also use |cdot_i|<=2rho.
        c_max = min(c_norm, np.max(abs(parent.initialization.c))+2*activity)
        fields = {}
        for tree in self.training_patterns:
            def visit(t):
                for kind, layer, index in t[1]:
                    fields[(kind, layer, index)] = np.full(n,
                        1. if kind == 'h' else c_max if kind == 'c' else
                        length if kind == 'B' else np.sqrt(M)*activity*delta[layer])
                for child in t[2]:
                    visit(child)
            visit(tree)
        positive = FieldEvaluator(fields, tuple(abs(W) for W in parent.initialization.W0))
        caps = np.array([max(positive.tree(t), np.finfo(float).tiny)
                         for t in self.training_patterns])
        if not np.isfinite(caps).all():
            raise FloatingPointError('Certified caps overflowed')
        return caps, dict(horizon=horizon, c_norm=c_norm, c_max=c_max, rho=rho_cap,
                          length=length, delta=delta, min_cap=float(caps.min()),
                          max_cap=float(caps.max()))
