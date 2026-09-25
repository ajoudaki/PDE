"""Ordinary scalar contraction closure with one passive, fixed input.

This reuses the exact P=1 tree generator, but it has no angular diagrams,
Fourier coordinates or quadrature.  A passive input supplies activation species
only.  The residuals, activity clock and history sources use training inputs.
Neuron arrays and initialized matrices are used only by ``initialize``.
"""
from collections import deque
from functools import lru_cache
import time

import numpy as np

from scalar_fourier_engine import (
    DiagramEvaluator, ScalarFourierSystem, Templates, canonical, field, node,
)


@lru_cache(None)
def contains_sample(tree, sample):
    return (any(f[0] == "h" and f[2] == sample for f in tree[1])
            or any(contains_sample(child, sample) for child in tree[2]))


class ScalarPointSystem(ScalarFourierSystem):
    """Compile the reachable ordinary-tree dictionary at a fixed cutoff.

    ``U`` is (2,M); ``test_U`` is either one length-two input or None.  The
    parent's ``training_patterns`` name denotes all ordinary scalar types,
    including passive-containing types here.  ``output_indices`` always names
    training outputs only; ``point_index`` names the optional passive output.
    """

    def __init__(self, U, y, test_U, K, max_patterns=6000, max_terms=2000000,
                 compile_seconds=120., max_memory_bytes=2*1024**3):
        self.U, self.y = np.asarray(U, float).copy(), np.asarray(y, float).copy()
        if self.y.ndim != 1 or not self.y.size or self.U.shape != (2, self.y.size):
            raise ValueError("U must have shape (2,M) and y shape (M,), M>0")
        self.test_U = None if test_U is None else np.asarray(test_U, float).copy()
        if self.test_U is not None and self.test_U.shape != (2,):
            raise ValueError("test_U must be one length-two input or None")
        if not (np.isfinite(self.U).all() and np.isfinite(self.y).all()
                and (self.test_U is None or np.isfinite(self.test_U).all())):
            raise ValueError("Inputs and labels must be finite")
        if int(K) != K or K < 3:
            raise ValueError("K must be an integer at least 3")
        self.M, self.K, self.J = self.y.size, int(K), 0
        self.nweights = 1
        self.point_sample = self.M if self.test_U is not None else None
        self.training_patterns, self.angular_patterns = [], []
        self.training_index, self.angular_index = {}, {}
        self.training_rows, self.angular_rows = [], []
        self.dropped_terms = self.generated_terms = self.retained_terms = 0
        self.compile_started = time.monotonic()
        self.max_patterns, self.max_terms = max_patterns, max_terms
        self.compile_seconds, self.max_memory_bytes = compile_seconds, max_memory_bytes
        self.templates = Templates(self.U)
        # Extend only the input Gram lookup.  Templates.M and all source loops
        # remain the original M; no residual or history belongs to the point.
        if self.test_U is not None:
            all_U = np.column_stack((self.U, self.test_U))
            self.templates.gram = all_U.T @ all_U
        self._pending = deque()
        self.output_indices = []
        for a in range(self.M):
            output = canonical(node(3, [field("c", 3), field("h", 3, a)]))
            self.output_indices.append(self._register(output, False))
        self.point_index = None
        if self.test_U is not None:
            output = canonical(node(3, [field("c", 3), field("h", 3, self.M)]))
            self.point_index = self._register(output, False)
        self.angular_output_index = self.energy_index = None
        while self._pending:
            angular, index = self._pending.popleft()
            if angular:
                raise AssertionError("A fixed-input closure has no angular block")
            self.training_rows[index] = self._compile_row(self.training_patterns[index], False)
            self._check_limit()
        self.compile_time = time.monotonic() - self.compile_started
        self.ntrain, self.nangular = len(self.training_patterns), 0
        self.nscalar = self.ntrain
        self.dimension = self.nscalar + 1
        self.train_table = self._table(self.training_rows, False)

    def statistics(self):
        result = super().statistics()
        passive = (sum(contains_sample(t, self.point_sample) for t in self.training_patterns)
                   if self.point_sample is not None else 0)
        result.update(training_only_patterns=len(self.training_patterns)-passive,
                      passive_patterns=passive, ordinary_patterns=len(self.training_patterns),
                      has_passive_point=self.test_U is not None, angular_patterns=0,
                      quadrature_nodes=0)
        return result

    def initialize(self, W1, W20, W30, c):
        started = time.monotonic()
        W1, W20, W30, c = map(np.asarray, (W1, W20, W30, c))
        n = c.size
        if (W1.shape != (n, 2) or W20.shape != (n, n)
                or W30.shape != (n, n) or c.shape != (n,)):
            raise ValueError("Inconsistent initial network shapes")
        all_U = self.U if self.test_U is None else np.column_stack((self.U, self.test_U))
        h1 = np.tanh(W1 @ all_U)
        h2 = np.tanh(W20 @ h1)
        h3 = np.tanh(W30 @ h2)
        fields = {field("c", 3): c[:, None]}
        for layer, h in enumerate((h1, h2, h3), 1):
            for a in range(all_U.shape[1]):
                fields[field("h", layer, a)] = h[:, a, None]
        for a in range(self.M):
            for layer, h in ((2, h1), (3, h2)):
                fields[field("A", layer, a)] = np.zeros((n, 1))
                fields[field("B", layer, a)] = h[:, a, None]
        # Every field has a fixed input label and a single column.  The dummy
        # length-one angular argument is unused by ordinary tree evaluation.
        evaluator = DiagramEvaluator(fields, W20, W30, np.zeros(1))
        z = np.empty(self.dimension)
        z[:-1] = [evaluator.tree(t)[0] for t in self.training_patterns]
        z[-1] = 1.
        self.initialization_seconds = time.monotonic() - started
        return z

    def rhs(self, t, z):
        del t
        q = np.r_[z[:-1], 1.]
        residual = q[self.output_indices] - self.y
        rho = np.linalg.norm(residual) / np.sqrt(self.M)
        drive = np.r_[1., rho, residual]
        values = self._values(self.train_table, q, drive, z[-1])
        out = np.empty_like(z)
        out[:-1] = np.bincount(self.train_table["rows"], weights=values,
                              minlength=self.nscalar)
        out[-1] = rho
        return out

    def point_output(self, z):
        if self.point_index is None:
            raise ValueError("No passive point was included")
        return np.asarray(z)[self.point_index]

    def fourier_coefficients(self, z):
        raise NotImplementedError("This closure contains no Fourier coordinates")

    def circle_output(self, z, theta):
        raise NotImplementedError("This closure retains one fixed passive input only")
