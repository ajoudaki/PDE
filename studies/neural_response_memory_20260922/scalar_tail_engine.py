"""Initialized boundary closures of the exact P=1 scalar tree hierarchy.

The constructor compiles an ordinary scalar dictionary.  Initialization alone
uses neuron fields and the realized initialized matrices.  Runtime uses scalar
coefficient tables, boundary constants, and (for tangent tails) M accumulated
residuals.  No training trajectory is used to construct a coefficient.
"""
from __future__ import annotations

from collections import defaultdict, deque
from functools import lru_cache
import resource
import time

import numpy as np

from scalar_fourier_engine import (
    CompilationLimit, Templates, canonical, differentiated_sites, field, merge,
    node, nonconstant, size,
)


@lru_cache(None)
def a_occurrences(tree):
    return (sum(f[0] == "A" for f in tree[1])
            + sum(a_occurrences(child) for child in tree[2]))


class _InitialTreeJets:
    """Value and first directional derivatives, never a runtime object."""

    def __init__(self, fields, W20, W30):
        self.fields = fields
        self.weights = {2: W20, 3: W30}
        self.shape = next(iter(fields.values())).shape
        self.cache = {}

    @staticmethod
    def multiply(left, right):
        out = np.empty_like(left)
        out[:, 0] = left[:, 0] * right[:, 0]
        out[:, 1:] = (left[:, 1:] * right[:, :1]
                      + left[:, :1] * right[:, 1:])
        return out

    def rooted(self, tree):
        if tree not in self.cache:
            value = np.zeros(self.shape)
            value[:, 0] = 1.
            for species in tree[1]:
                value = self.multiply(value, self.fields[species])
            if np.any(value):
                for child in tree[2]:
                    W = self.weights[max(tree[0], child[0])]
                    message = ((W if tree[0] > child[0] else W.T)
                               @ self.rooted(child))
                    value = self.multiply(value, message)
            self.cache[tree] = value
        return self.cache[tree]

    def tree(self, tree):
        return self.rooted(tree).mean(axis=0)


def _initial_field_jets(U, Utest, W1, W20, W30, c):
    """Columns are value, M unit residual directions, unit rho direction."""
    n, M = W1.shape[0], U.shape[1]
    all_U = np.column_stack((U, Utest))
    h1 = np.tanh(W1 @ all_U)
    h2 = np.tanh(W20 @ h1)
    h3 = np.tanh(W30 @ h2)
    hs = (h1, h2, h3)
    gates = tuple(1. - h * h for h in hs)
    d3 = c[:, None] * gates[2][:, :M]
    d2 = gates[1][:, :M] * (W30.T @ d3)
    d1 = gates[0][:, :M] * (W20.T @ d2)
    fields = {}
    for layer, h in enumerate(hs, 1):
        for a in range(all_U.shape[1]):
            jet = np.zeros((n, M + 2))
            jet[:, 0] = h[:, a]
            fields[field("h", layer, a)] = jet
    cj = np.zeros((n, M + 2))
    cj[:, 0] = c
    cj[:, 1:M + 1] = -2. / M * h3[:, :M]
    fields[field("c", 3)] = cj
    for layer, h, delta in ((2, h1, d2), (3, h2, d3)):
        for a in range(M):
            aj = np.zeros((n, M + 2))
            aj[:, a + 1] = delta[:, a]
            fields[field("A", layer, a)] = aj
            bj = np.zeros((n, M + 2))
            bj[:, 0] = h[:, a]
            bj[:, -1] = h[:, a]
            fields[field("B", layer, a)] = bj
    for a in range(M):
        dw = -2. / M * np.outer(d1[:, a], U[:, a])
        dW2 = -2. / (M * n) * np.outer(d2[:, a], h1[:, a])
        dW3 = -2. / (M * n) * np.outer(d3[:, a], h2[:, a])
        dh1 = gates[0] * (dw @ all_U)
        dh2 = gates[1] * (dW2 @ h1 + W20 @ dh1)
        dh3 = gates[2] * (dW3 @ h2 + W30 @ dh2)
        for layer, dh in enumerate((dh1, dh2, dh3), 1):
            for b in range(all_U.shape[1]):
                fields[field("h", layer, b)][:, a + 1] = dh[:, b]
    return fields


class ScalarTailSystem:
    """Finite initialized-frozen or initialized-tangent boundary closure."""

    def __init__(self, U, y, Utest, K, mode="frozen", max_patterns=12000,
                 max_boundary=50000, max_terms=5000000, compile_seconds=180.,
                 max_memory_bytes=3 * 1024**3):
        self.U, self.y = np.asarray(U, float).copy(), np.asarray(y, float).copy()
        self.Utest = np.asarray(Utest, float).copy()
        if self.Utest.ndim == 1:
            self.Utest = self.Utest[:, None]
        if (self.y.ndim != 1 or not self.y.size
                or self.U.shape != (2, self.y.size)
                or self.Utest.ndim != 2 or self.Utest.shape[0] != 2):
            raise ValueError("Expected U=(2,M), y=(M,), Utest=(2,Q)")
        if not all(np.isfinite(x).all() for x in (self.U, self.y, self.Utest)):
            raise ValueError("Inputs and labels must be finite")
        if int(K) != K or K < 3 or mode not in ("frozen", "tangent"):
            raise ValueError("K must be an integer >=3; mode is frozen or tangent")
        self.M, self.Q, self.K, self.mode = self.y.size, self.Utest.shape[1], int(K), mode
        self.max_patterns, self.max_boundary, self.max_terms = max_patterns, max_boundary, max_terms
        self.compile_seconds, self.max_memory_bytes = compile_seconds, max_memory_bytes
        self.compile_started = time.monotonic()
        self.training_patterns, self.boundary_patterns = [], []
        self.training_index, self.boundary_index = {}, {}
        self.training_rows, self._pending = [], deque()
        self.generated_terms = self.retained_terms = self.pruned_terms = 0
        self.templates = Templates(self.U)
        all_U = np.column_stack((self.U, self.Utest))
        self.templates.gram = all_U.T @ all_U
        self.all_output_indices = []
        for a in range(self.M + self.Q):
            tree = canonical(node(3, [field("c", 3), field("h", 3, a)]))
            self.all_output_indices.append(self._register(tree))
        self.output_indices = self.all_output_indices[:self.M]
        while self._pending:
            index = self._pending.popleft()
            self.training_rows[index] = self._compile_row(self.training_patterns[index])
            self._check_limit()
        self.nscalar = self.ntrain = len(self.training_patterns)
        self.nboundary = len(self.boundary_patterns)
        self.length_index = self.nscalar
        self.dimension = self.nscalar + 1 + (self.M if mode == "tangent" else 0)
        self._pack_table()
        self.templates = None
        self.training_rows = None
        self.compile_time = time.monotonic() - self.compile_started
        self._check_limit()
        self.initialized = False

    def statistics(self):
        result = dict(K=self.K, mode=self.mode, live_patterns=len(self.training_patterns),
                      boundary_patterns=len(self.boundary_patterns),
                      generated_terms=self.generated_terms, retained_terms=self.retained_terms,
                      structurally_pruned_terms=self.pruned_terms,
                      dimension=getattr(self, "dimension", None),
                      compile_seconds=getattr(self, "compile_time", time.monotonic() - self.compile_started),
                      initialization_seconds=getattr(self, "initialization_seconds", None),
                      peak_rss_bytes=1024 * resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if hasattr(self, "table"):
            result["coefficient_array_bytes"] = sum(x.nbytes for x in self.table.values())
        if hasattr(self, "boundary_values"):
            result["boundary_array_bytes"] = self.boundary_values.nbytes + self.boundary_slopes.nbytes
        return result

    def _check_limit(self):
        reason = None
        if len(self.training_patterns) > self.max_patterns:
            reason = "live-pattern cap"
        elif len(self.boundary_patterns) > self.max_boundary:
            reason = "boundary-pattern cap"
        elif self.retained_terms > self.max_terms:
            reason = "retained-term cap"
        elif 1024 * resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > self.max_memory_bytes:
            reason = "memory cap"
        elif time.monotonic() - self.compile_started > self.compile_seconds:
            reason = "preparation time cap"
        if reason:
            raise CompilationLimit(reason, self.statistics())

    def _register(self, tree):
        if size(tree) <= self.K:
            if tree not in self.training_index:
                self.training_index[tree] = len(self.training_patterns)
                self.training_patterns.append(tree)
                self.training_rows.append(None)
                self._pending.append(self.training_index[tree])
                self._check_limit()
            return self.training_index[tree]
        if tree not in self.boundary_index:
            self.boundary_index[tree] = len(self.boundary_patterns)
            self.boundary_patterns.append(tree)
            self._check_limit()
        return -self.boundary_index[tree] - 1

    def _compile_row(self, tree):
        terms = defaultdict(float)
        zero_count = 1 if self.mode == "frozen" else 2
        for remainder, species, count in differentiated_sites(tree):
            for (root, forest, cc, ss, drive, lp), coefficient in self.templates.rhs(species).items():
                self.generated_terms += 1
                if self.generated_terms % 512 == 0:
                    self._check_limit()
                if cc or ss:
                    raise AssertionError("Fixed positive sample IDs must not have angular powers")
                joined = canonical(merge(remainder, root))
                trees = forest + ((joined,) if nonconstant(joined) else ())
                if any(size(t) > self.K and a_occurrences(t) >= zero_count for t in trees):
                    self.pruned_terms += 1
                    continue
                indices = tuple(sorted(self._register(t) for t in trees))
                terms[(indices, drive, lp)] += count * coefficient
        row = [(c, indices, drive, lp) for (indices, drive, lp), c in terms.items() if c != 0.]
        self.retained_terms += len(row)
        return row

    def _pack_table(self):
        arity = max((len(term[1]) for row in self.training_rows for term in row), default=0)
        count = self.retained_terms
        one_index = self.nscalar + self.nboundary
        table = dict(indices=np.full((count, arity), one_index, dtype=np.int32),
                     rows=np.empty(count, dtype=np.int32), coefficients=np.empty(count),
                     drives=np.empty(count, dtype=np.int32), powers=np.empty(count, dtype=np.int32))
        k = 0
        for i, row in enumerate(self.training_rows):
            for coefficient, indices, drive, lp in row:
                table["indices"][k, :len(indices)] = [j if j >= 0 else self.nscalar - j - 1 for j in indices]
                table["rows"][k] = i
                table["coefficients"][k] = coefficient
                table["drives"][k] = drive + 2
                table["powers"][k] = lp
                k += 1
        self.table = table

    def initialize(self, W1, W20, W30, c):
        started = time.monotonic()
        W1, W20, W30, c = (np.asarray(x, float) for x in (W1, W20, W30, c))
        n = c.size
        if (W1.shape != (n, 2) or W20.shape != (n, n)
                or W30.shape != (n, n) or c.shape != (n,)):
            raise ValueError("Inconsistent initialization shapes")
        if not all(np.isfinite(x).all() for x in (W1, W20, W30, c)):
            raise ValueError("Nonfinite initialization")
        fields = _initial_field_jets(self.U, self.Utest, W1, W20, W30, c)
        evaluator = _InitialTreeJets(fields, W20, W30)
        z = np.zeros(self.dimension)
        for i, tree in enumerate(self.training_patterns):
            z[i] = evaluator.tree(tree)[0]
            if i % 256 == 0:
                self._check_limit()
        z[self.length_index] = 1.
        self.boundary_values = np.empty(self.nboundary)
        self.boundary_slopes = np.zeros((self.nboundary, self.M + 1))
        for i, tree in enumerate(self.boundary_patterns):
            jet = evaluator.tree(tree)
            self.boundary_values[i] = jet[0]
            if self.mode == "tangent":
                self.boundary_slopes[i] = jet[1:]
            if i % 256 == 0:
                self._check_limit()
        self.initialization_seconds = time.monotonic() - started
        self._check_limit()
        self.initialized = True
        return z

    def boundary(self, z):
        if self.mode == "frozen":
            return self.boundary_values
        accumulators = np.r_[z[self.length_index + 1:], z[self.length_index] - 1.]
        return self.boundary_values + self.boundary_slopes @ accumulators

    def rhs(self, t, z):
        del t
        if not self.initialized:
            raise RuntimeError("Initialize the fixed scalar coefficients first")
        residual = self.training_output(z) - self.y
        rho = np.linalg.norm(residual) / np.sqrt(self.M)
        drive = np.r_[1., rho, residual]
        q = np.r_[z[:self.nscalar], self.boundary(z), 1.]
        tab = self.table
        values = (tab["coefficients"] * np.prod(q[tab["indices"]], axis=1)
                  * drive[tab["drives"]] / np.power(z[self.length_index], tab["powers"]))
        out = np.empty_like(z)
        out[:self.nscalar] = np.bincount(tab["rows"], weights=values, minlength=self.nscalar)
        out[self.length_index] = rho
        if self.mode == "tangent":
            out[self.length_index + 1:] = residual
        return out

    def training_output(self, z):
        return np.asarray(z)[self.output_indices]

    def outputs(self, z):
        return np.asarray(z)[self.all_output_indices]
