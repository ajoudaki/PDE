"""Ordered scalar hierarchies of orders two through six.

T1=f, T2=Theta and T_P is fixed. Optional local signatures carry passive
readouts without feedback. The structured BDF adapter changes only the exact
Newton linear algebra; SciPy's BDF stepping and error control are inherited.
"""

from dataclasses import dataclass
from numbers import Integral
from types import MappingProxyType

import numpy as np
from scipy.integrate import BDF
from scipy.linalg import lu_factor, lu_solve
from scipy.sparse import csc_matrix


def _order(value):
    if isinstance(value, bool) or not isinstance(value, Integral) or not 2 <= value <= 6:
        raise ValueError("order must be an integer from two through six")
    return int(value)


def _infer_order(coefficients):
    degrees = [int(name[1:]) for name in coefficients
               if isinstance(name, str) and name.startswith("T") and name[1:].isdigit()]
    if not degrees:
        raise ValueError("coefficients must contain T1 through TP")
    return _order(max(degrees))


def _last(tensor, vector):
    return np.tensordot(tensor, vector, axes=([-1], [0]))


def _owned_readonly(value):
    value = np.array(value, copy=True)
    value.setflags(write=False)
    return value


class ScalarHierarchy:
    """The original full tensor chain, with T_P omitted from moving state."""

    def __init__(self, coefficients, labels, order=None, with_signatures=True):
        self.order = _infer_order(coefficients) if order is None else _order(order)
        if not isinstance(with_signatures, (bool, np.bool_)):
            raise ValueError("with_signatures must be boolean")
        self.with_signatures = bool(with_signatures)
        labels = np.asarray(labels)
        if labels.ndim != 1 or not len(labels) or not np.isfinite(labels).all():
            raise ValueError("labels must be a finite nonempty vector")
        self.M, self.alpha = len(labels), 2/len(labels)
        self.names = tuple("T"+str(j) for j in range(1, self.order+1))
        values = {name: np.asarray(coefficients[name]) for name in self.names}
        self.dtype = np.result_type(labels.dtype, *(value.dtype for value in values.values()), np.float64)
        self.labels = _owned_readonly(np.asarray(labels, dtype=self.dtype))
        for j, name in enumerate(self.names, 1):
            if values[name].shape != (self.M,)*j or not np.isfinite(values[name]).all():
                raise ValueError("invalid tensor "+name)
        self.terminal_name = self.names[-1]
        self.terminal = _owned_readonly(np.asarray(values[self.terminal_name], dtype=self.dtype))
        self.training_slices, self.signature_slices = {}, {}
        start = 0
        for j, name in enumerate(self.names[:-1], 1):
            self.training_slices[name] = slice(start, start+self.M**j)
            start += self.M**j
        self.training_size = start
        self.signature_names = tuple("sigma"+str(k) for k in range(1, self.order)) if self.with_signatures else ()
        for k, name in enumerate(self.signature_names, 1):
            self.signature_slices[name] = slice(start, start+self.M**k)
            start += self.M**k
        self.size = start
        self._initial = np.concatenate([np.asarray(values[name], dtype=self.dtype).reshape(-1)
                                        for name in self.names[:-1]]
                                       + [np.zeros(self.size-self.training_size, dtype=self.dtype)])
        self._prepare_jacobian_pattern()

    def _state(self, state):
        state = np.asarray(state)
        if state.shape != (self.size,):
            raise ValueError("incorrect scalar state shape")
        return state

    def initial_state(self):
        return self._initial.copy()

    def training_state(self, state):
        return self._state(state)[:self.training_size]

    def tensors(self, state):
        state = self._state(state)
        values = {name:state[self.training_slices[name]].reshape((self.M,)*j)
                  for j, name in enumerate(self.names[:-1], 1)}
        values[self.terminal_name] = self.terminal
        return values

    def signatures(self, state):
        state = self._state(state)
        return {name:state[self.signature_slices[name]].reshape((self.M,)*k)
                for k, name in enumerate(self.signature_names, 1)}

    def unpack(self, state):
        return {**self.tensors(state), **self.signatures(state)}

    def reset_signatures(self, state):
        """Preserve integrated training tensors bit for bit; zero local history."""
        result = self._state(state).copy()
        result[self.training_size:] = 0
        return result

    def rhs(self, time, state):
        state = self._state(state)
        values = self.tensors(state)
        velocity = -self.alpha*(values["T1"]-self.labels)
        result = np.empty(self.size, dtype=np.result_type(state.dtype, self.dtype))
        for j in range(1, self.order):
            result[self.training_slices["T"+str(j)]] = _last(values["T"+str(j+1)], velocity).reshape(-1)
        previous = np.array(1., dtype=result.dtype)
        for name, signature in self.signatures(state).items():
            result[self.signature_slices[name]] = np.multiply.outer(velocity, previous).reshape(-1)
            previous = signature
        return result

    __call__ = rhs

    def _prepare_jacobian_pattern(self):
        m, rows, columns, blocks = self.M, [], [], []
        for j in range(1, self.order):
            own = self.training_slices["T"+str(j)]
            count = m**j
            row = np.repeat(np.arange(own.start, own.stop), m)
            rows.append(row); columns.append(np.tile(np.arange(m), count))
            blocks.append(("feedback", "T"+str(j+1)))
            if j+1 < self.order:
                after = self.training_slices["T"+str(j+1)]
                rows.append(row); columns.append(np.arange(after.start, after.stop))
                blocks.append(("transport", count))
        for k, name in enumerate(self.signature_names, 1):
            own = self.signature_slices[name]
            count = m**(k-1)
            row = np.arange(own.start, own.stop)
            rows.append(row); columns.append(np.repeat(np.arange(m), count))
            previous = "sigma"+str(k-1) if k > 1 else None
            blocks.append(("signature_feedback", previous))
            if previous is not None:
                before = self.signature_slices[previous]
                rows.append(row); columns.append(np.tile(np.arange(before.start, before.stop), m))
                blocks.append(("signature_transport", count))
        self._jac_rows, self._jac_columns = np.concatenate(rows), np.concatenate(columns)
        self._jac_blocks = tuple(blocks)

    def jac(self, time, state):
        values = self.unpack(state)
        velocity = -self.alpha*(values["T1"]-self.labels)
        entries = []
        for kind, argument in self._jac_blocks:
            if kind == "feedback":
                entries.append(-self.alpha*values[argument].reshape(-1))
            elif kind == "transport":
                entries.append(np.tile(velocity, argument))
            elif kind == "signature_feedback":
                previous = np.ones(1) if argument is None else values[argument].reshape(-1)
                entries.append(-self.alpha*np.tile(previous, self.M))
            else:
                entries.append(np.repeat(velocity, argument))
        return csc_matrix((np.concatenate(entries), (self._jac_rows, self._jac_columns)),
                          shape=(self.size, self.size))

    def linearize(self, state):
        """Own every coefficient needed by a cached Newton linear solve."""
        state = self._state(state)
        tensors = self.tensors(state)
        return JacobianSnapshot(self.M, self.order, self.size, self.alpha,
            MappingProxyType(self.training_slices.copy()), MappingProxyType(self.signature_slices.copy()),
            MappingProxyType({name:_owned_readonly(value) for name, value in tensors.items() if name != "T1"}),
            MappingProxyType({name:_owned_readonly(value) for name, value in self.signatures(state).items()}),
            _owned_readonly(-self.alpha*(tensors["T1"]-self.labels)))


@dataclass(frozen=True)
class JacobianSnapshot:
    M: int
    order: int
    size: int
    alpha: float
    training_slices: object
    signature_slices: object
    tensors: object
    signatures: object
    velocity: np.ndarray

    __array_priority__ = 10000

    def factor(self, gamma):
        return SchurFactor(self, gamma)

    def __rmul__(self, gamma):
        if not np.isscalar(gamma):
            return NotImplemented
        return _ScaledJacobian(self, gamma)


@dataclass(frozen=True)
class _ScaledJacobian:
    snapshot: JacobianSnapshot
    gamma: object


class _StructuredIdentity:
    def __sub__(self, scaled):
        if not isinstance(scaled, _ScaledJacobian):
            return NotImplemented
        return scaled


class SchurFactor:
    """Exact tensor elimination, with only an M-by-M matrix factorization."""

    def __init__(self, snapshot, gamma):
        if not np.isscalar(gamma) or not np.isfinite(gamma):
            raise ValueError("gamma must be a finite scalar")
        self.snapshot, self.gamma = snapshot, gamma
        self.dtype = np.result_type(snapshot.velocity.dtype,
                                   *(value.dtype for value in snapshot.tensors.values()), gamma)
        self.w = np.asarray(gamma*snapshot.velocity, dtype=self.dtype)
        coefficient = np.zeros((snapshot.M, snapshot.M), dtype=self.dtype)
        for j in range(2, snapshot.order+1):
            term = snapshot.tensors["T"+str(j)]
            # The first and LAST axes remain free. Intermediate indices keep
            # their original order, with no symmetry or complex conjugation.
            while term.ndim > 2:
                term = np.tensordot(term, self.w, axes=([-2], [0]))
            coefficient += term
        self.schur = np.eye(snapshot.M, dtype=self.dtype)+snapshot.alpha*gamma*coefficient
        self.lu = lu_factor(self.schur)

    def solve(self, rhs):
        rhs = np.asarray(rhs)
        if rhs.ndim == 2 and rhs.shape[0] == self.snapshot.size:
            return np.column_stack([self.solve(rhs[:, column]) for column in range(rhs.shape[1])])
        if rhs.shape != (self.snapshot.size,):
            raise ValueError("Newton right-hand side has incorrect shape")
        snap = self.snapshot
        dtype = np.result_type(rhs.dtype, self.dtype)
        blocks = {name:rhs[part].reshape((snap.M,)*j)
                  for j, (name, part) in enumerate(snap.training_slices.items(), 1)}
        forcing = np.array(blocks["T1"], dtype=dtype, copy=True)
        for j in range(2, snap.order):
            term = blocks["T"+str(j)]
            while term.ndim > 1:
                term = _last(term, self.w)
            forcing += term
        if np.iscomplexobj(forcing) and not np.iscomplexobj(self.schur):
            delta_f = lu_solve(self.lu, forcing.real)+1j*lu_solve(self.lu, forcing.imag)
        else:
            delta_f = lu_solve(self.lu, forcing)
        result = np.empty(snap.size, dtype=dtype)
        result[snap.training_slices["T1"]] = delta_f
        next_delta = None
        for j in range(snap.order-1, 1, -1):
            value = blocks["T"+str(j)]-snap.alpha*self.gamma*_last(snap.tensors["T"+str(j+1)], delta_f)
            if next_delta is not None:
                value = value+_last(next_delta, self.w)
            result[snap.training_slices["T"+str(j)]] = value.reshape(-1)
            next_delta = value
        previous_delta = None
        for k, (name, part) in enumerate(snap.signature_slices.items(), 1):
            value = np.array(rhs[part].reshape((snap.M,)*k), dtype=dtype, copy=True)
            if k == 1:
                value -= snap.alpha*self.gamma*delta_f
            else:
                value -= snap.alpha*self.gamma*np.multiply.outer(delta_f, snap.signatures["sigma"+str(k-1)])
                value += np.multiply.outer(self.w, previous_delta)
            result[part] = value.reshape(-1)
            previous_delta = value
        return result


class StructuredBDF(BDF):
    """SciPy BDF with its step implementation unchanged and exact small solves.

    The constructor evaluates the ordinary sparse Jacobian once, letting the
    base constructor follow its sparse allocation path. Before the first
    step, matrix arithmetic is replaced by immutable snapshot descriptors.
    Each cached factor owns its original snapshot AND gamma, including when
    SciPy deliberately reuses a factor after reducing its trial step size.
    """

    def __init__(self, model, t0, y0, t_bound, **kwargs):
        if not isinstance(model, ScalarHierarchy):
            raise TypeError("StructuredBDF requires a ScalarHierarchy")
        if kwargs.pop("vectorized", False):
            raise ValueError("StructuredBDF does not accept a vectorized RHS")
        forbidden = {"jac", "jac_sparsity"}.intersection(kwargs)
        if forbidden:
            raise ValueError("StructuredBDF supplies "+", ".join(sorted(forbidden)))
        self.model = model
        super().__init__(model.rhs, t0, y0, t_bound, jac=model.jac, **kwargs)
        self.J = model.linearize(self.y)
        self.jac = self._snapshot_jacobian
        self.I = _StructuredIdentity()
        self.lu = self._structured_factor
        self.solve_lu = lambda factor, rhs:factor.solve(rhs)

    def _snapshot_jacobian(self, time, state):
        self.njev += 1
        return self.model.linearize(state)

    def _structured_factor(self, matrix):
        if not isinstance(matrix, _ScaledJacobian):
            raise TypeError("unexpected BDF Newton-matrix representation")
        self.nlu += 1
        return matrix.snapshot.factor(matrix.gamma)


def recenter_coefficients(coefficients, signatures):
    """Transport OLD passive T anchors by local ordered signatures exactly.

    Tj_new=sum_k T(j+k)_old:sigma_k, contracting the last k axes. T_P is
    returned unchanged. Float/complex extended precision is used at this
    boundary. Directly integrated training tensors must instead be preserved.
    """
    order = _infer_order(coefficients)
    z = np.asarray(signatures["sigma1"])
    if z.ndim != 1 or not len(z):
        raise ValueError("sigma1 must be a nonempty vector")
    m = len(z)
    first = np.asarray(coefficients["T1"])
    if first.ndim != 1 or not len(first):
        raise ValueError("T1 must have one nonempty passive-output axis")
    count = len(first)
    old = {j:np.asarray(coefficients["T"+str(j)]) for j in range(1, order+1)}
    for j, value in old.items():
        if value.shape != (count,)+(m,)*(j-1) or not np.isfinite(value).all():
            raise ValueError("invalid passive tensor T"+str(j))
    sig = {}
    for k in range(1, order):
        value = np.asarray(signatures["sigma"+str(k)])
        if value.shape != (m,)*k or not np.isfinite(value).all():
            raise ValueError("invalid local signature sigma"+str(k))
        sig[k] = value
    dtype = np.result_type(*(value.dtype for value in (*old.values(), *sig.values())), np.longdouble)
    result = {}
    for j in range(1, order):
        value = np.array(old[j], dtype=dtype, copy=True)
        for k in range(1, order-j+1):
            source = np.asarray(old[j+k], dtype=dtype)
            value += np.tensordot(source, np.asarray(sig[k], dtype=dtype),
                axes=(tuple(range(source.ndim-k, source.ndim)), tuple(range(k))))
        result["T"+str(j)] = value
    result["T"+str(order)] = coefficients["T"+str(order)]
    return result
