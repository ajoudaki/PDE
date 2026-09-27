"""Exact shared-core-once evaluation of the existing selective scalar ODE.

Only zero-boundary evaluation is supported. Retained equations, coefficients,
term order within each row, clipping and penalty are unchanged. The training
core is evaluated once; each passive query retains its own original rows.
"""
from __future__ import annotations

import numpy as np

from circle_tasks import directions
from run_true_aggregate_selective import SharedQueryClosure


class FastSharedQueryClosure(SharedQueryClosure):
    def __init__(self, template, angles):
        super().__init__(template, angles)
        if template.boundary != 'zero':
            raise ValueError('Exact core-once evaluator supports zero boundary only')
        size = len(template.trees)
        core_map = np.full(size, -1, dtype=np.int64)
        passive_map = np.full(size, -1, dtype=np.int64)
        core_map[self.core_ids] = np.arange(self.ncore)
        passive_map[self.passive_ids] = np.arange(self.npassive)
        self._core_terms = np.flatnonzero(core_map[template.row_index] >= 0)
        self._passive_terms = np.flatnonzero(passive_map[template.row_index] >= 0)
        ci, pi = self._core_terms, self._passive_terms
        if np.any(core_map[template.child_index[ci]] < 0):
            raise ValueError('Training-core row has a passive child')
        self._core_rows = core_map[template.row_index[ci]]
        self._core_children = core_map[template.child_index[ci]]
        self._passive_rows = passive_map[template.row_index[pi]]
        self._passive_indices = (self._passive_rows[None, :] +
            self.npassive*np.arange(len(self.angles))[:, None]).ravel()
        self._query_dots = {fid: directions(self.angles)@template.u[b]
                           for (_, b), fid in template.C.items()}

    def rhs(self, at, state):
        model = self.template
        core, passive, clock = self.unpack(state)
        count, size = len(self.angles), len(model.trees)
        raw = np.empty((count, size))
        raw[:, self.core_ids] = core
        raw[:, self.passive_ids] = passive
        q = np.clip(raw, -1., 1.)
        fields = np.ones((count, len(model.field_names)))
        residual = 2*q[:, model.Fids[:model.m]]-model.labels/clock
        fields[:, model.R] = residual
        fields[:, model.sig] = np.sqrt(np.mean(residual*residual, axis=1))
        for fid, values in self._query_dots.items():
            fields[:, fid] = values
        for key, index in model.sids.items():
            fields[:, model.s[key]] = q[:, index]
        for key, (a, b) in model.tids.items():
            fields[:, model.t[key]] = q[:, a]-q[:, b]

        def coefficient(key):
            power, indices = key
            return clock**power*np.prod(fields[:, indices], axis=1)

        for key, terms in model.Dpacked.items():
            fields[:, model.D[key]] = sum(c*coefficient(ck)*q[:, index]
                                         for c, ck, index in terms)
        coefficients = np.column_stack([coefficient(key) for key in model.coeff_keys])
        ci, pi = self._core_terms, self._passive_terms
        core_weights = model.values[ci]*coefficients[0, model.coeff_index[ci]]
        core_values = q[0, self.core_ids]
        core_result = np.bincount(self._core_rows,
            weights=core_weights*core_values[self._core_children], minlength=self.ncore)
        core_envelope = np.bincount(self._core_rows,
            weights=np.abs(core_weights), minlength=self.ncore)
        weights = model.values[pi]*coefficients[:, model.coeff_index[pi]]
        passive_result = np.bincount(self._passive_indices,
            weights=(weights*q[:, model.child_index[pi]]).ravel(),
            minlength=count*self.npassive).reshape(count, self.npassive)
        envelope = np.bincount(self._passive_indices,
            weights=np.abs(weights).ravel(),
            minlength=count*self.npassive).reshape(count, self.npassive)
        output = np.empty_like(state)
        dcore, dpassive, _ = self.unpack(output)
        dcore[:] = core_result-core_envelope*(core-core_values)
        dpassive[:] = passive_result-envelope*(passive-q[:, self.passive_ids])
        output[-1] = fields[0, model.sig]*clock
        return output

    def check_exact_rhs(self, states):
        """Compare directly against the previously used vectorized evaluator."""
        reports = []
        for state in states:
            original = SharedQueryClosure.rhs(self, 0., state)
            optimized = self.rhs(0., state)
            maximum = float(np.max(np.abs(original-optimized)))
            scale = max(1., float(np.max(np.abs(original))))
            if maximum/scale > 1e-13:
                raise ValueError(f'Core-once RHS changed: {maximum/scale}')
            reports.append({'max_absolute_error': maximum,
                'scaled_error': maximum/scale,
                'bitwise_equal': bool(np.array_equal(original, optimized))})
        return reports
