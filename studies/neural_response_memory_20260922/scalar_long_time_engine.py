"""Stiff integration helpers for the unchanged scalar derivative hierarchy.

Only sample-indexed scalar arrays occur here.  The analytic Jacobian retains
the original training-state layout; passive signature recentering transports
the candidate's own coefficients and never consults a dense network.
"""

import numpy as np
from scipy.optimize import brentq
from scipy.sparse import csc_matrix

from scalar_circle_probe_engine import SignatureHierarchy


class StiffSignatureHierarchy(SignatureHierarchy):
    """Existing equations and layout, with their exact sparse Jacobian."""

    def __init__(self, coefficients, labels, order=4):
        super().__init__(coefficients, labels, order)
        m = self.M
        rows, columns, blocks = [], [], []
        for name, next_name in zip(self.training.all_names[:-1],
                                   self.training.all_names[1:]):
            state_slice = self.training.slices[name]
            count = state_slice.stop - state_slice.start
            row = np.repeat(np.arange(state_slice.start, state_slice.stop), m)
            rows.append(row)
            columns.append(np.tile(np.arange(m), count))
            blocks.append(("feedback", next_name))
            if next_name in self.training.slices:
                next_slice = self.training.slices[next_name]
                rows.append(row)
                columns.append(np.arange(next_slice.start, next_slice.stop))
                blocks.append(("transport", count))
        for degree, name in enumerate(self.signature_names, 1):
            state_slice = self.signature_slices[name]
            tail_count = m ** (degree - 1)
            row = np.arange(state_slice.start, state_slice.stop)
            rows.append(row)
            columns.append(np.repeat(np.arange(m), tail_count))
            previous = self.signature_names[degree - 2] if degree > 1 else None
            blocks.append(("signature_feedback", previous))
            if degree > 1:
                previous_slice = self.signature_slices[previous]
                rows.append(row)
                columns.append(np.tile(np.arange(previous_slice.start,
                                                  previous_slice.stop), m))
                blocks.append(("signature_transport", tail_count))
        self._jac_rows = np.concatenate(rows)
        self._jac_columns = np.concatenate(columns)
        self._jac_blocks = tuple(blocks)

    def jac(self, time, state):
        """Return d(rhs)/d(state), preserving every ordered tensor index."""
        values = self.unpack(state)
        alpha = 2 / self.M
        velocity = -alpha * (values["f"] - self.labels)
        entries = []
        for kind, argument in self._jac_blocks:
            if kind == "feedback":
                entries.append(-alpha * values[argument].reshape(-1))
            elif kind == "transport":
                entries.append(np.tile(velocity, argument))
            elif kind == "signature_feedback":
                tail = np.ones(1) if argument is None else values[argument].reshape(-1)
                entries.append(-alpha * np.tile(tail, self.M))
            else:
                entries.append(np.repeat(velocity, argument))
        return csc_matrix((np.concatenate(entries),
                           (self._jac_rows, self._jac_columns)),
                          shape=(self.size, self.size))


def recenter_coefficients(coefficients, signatures):
    """Transport passive anchors by local z/I/J, using OLD anchors throughout.

    Q (or the highest supplied coefficient) is returned unchanged.  Other
    results use long double, or complex long double for Fourier coefficients,
    where the platform provides it.  Training tensors should instead retain
    their directly integrated values at a restart.
    """
    names = tuple(name for name in ("f", "Theta", "C", "Q")
                  if name in coefficients)
    if names not in (("f", "Theta"), ("f", "Theta", "C"),
                     ("f", "Theta", "C", "Q")):
        raise ValueError("coefficients must contain contiguous f/Theta[/C/Q] blocks")
    z = np.asarray(signatures["z"])
    if z.ndim != 1 or not len(z):
        raise ValueError("z must be a nonempty vector")
    m, count = len(z), len(np.asarray(coefficients["f"]))
    signature_names = ("z", "I", "J")[:len(names) - 1]
    sig = {}
    for degree, name in enumerate(signature_names, 1):
        value = np.asarray(signatures[name])
        if value.shape != (m,) * degree or not np.isfinite(value).all():
            raise ValueError("invalid local signature " + name)
        sig[degree] = np.asarray(value, dtype=np.longdouble)
    old = {}
    for degree, name in enumerate(names):
        value = np.asarray(coefficients[name])
        if value.shape != (count,) + (m,) * degree or not np.isfinite(value).all():
            raise ValueError("invalid passive coefficient " + name)
        old[degree] = value
    result = {}
    last = len(names) - 1
    for degree, name in enumerate(names):
        if degree == last:
            result[name] = coefficients[name]
            continue
        dtype = np.result_type(*(value.dtype for value in old.values()), np.longdouble)
        value = np.array(old[degree], dtype=dtype, copy=True)
        for extra in range(1, last - degree + 1):
            source = np.asarray(old[degree + extra], dtype=dtype)
            axes = tuple(range(source.ndim - extra, source.ndim))
            value += np.tensordot(source, sig[extra],
                                  axes=(axes, tuple(range(extra))))
        result[name] = value
    return result


def frozen_kernel_endpoint(coefficients, labels, target=1e-6, time_cap=1e9):
    """First target-loss crossing of the unchanged order-two spectral flow.

    Negative eigenvalues are retained.  The spectral loss is convex in time,
    so its minimum supplies a first-crossing bracket even for an indefinite
    symmetric kernel.  z is the exact time integral of -2(f-y)/M, evaluated
    with expm1 and the analytic zero-eigenvalue limit.
    """
    labels = np.asarray(labels, dtype=float)
    f0 = np.asarray(coefficients["f"], dtype=float)
    theta = np.asarray(coefficients["Theta"], dtype=float)
    if (labels.ndim != 1 or not len(labels) or f0.shape != labels.shape
            or theta.shape != (len(labels), len(labels))
            or not all(np.isfinite(a).all() for a in (labels, f0, theta))):
        raise ValueError("finite f/labels vectors and a matching kernel are required")
    if not np.array_equal(theta, theta.T):
        raise ValueError("spectral endpoint requires an exactly symmetric stored kernel")
    if not np.isfinite(target) or target <= 0 or not np.isfinite(time_cap) or time_cap < 0:
        raise ValueError("target must be positive and time_cap finite and nonnegative")
    m, alpha = len(labels), 2 / len(labels)
    eigenvalues, vectors = np.linalg.eigh(theta)
    residual0 = f0 - labels
    components = vectors.T @ residual0
    weights = components ** 2
    active = weights > 0

    def spectral_loss(t):
        with np.errstate(over="ignore", invalid="ignore"):
            terms = weights[active] * np.exp(-2 * alpha * eigenvalues[active] * t)
        return float(np.sum(terms) / m)

    def derivative_sign(t):
        # Positive scaling preserves the derivative's zeros and avoids overflow.
        nonzero = active & (eigenvalues != 0)
        if not np.any(nonzero):
            return 0.
        lam = eigenvalues[nonzero]
        logs = np.log(weights[nonzero]) + np.log(np.abs(lam)) - 2 * alpha * lam * t
        return float(-np.sum(np.sign(lam) * np.exp(logs - np.max(logs))))

    initial_loss = float(np.mean(residual0 ** 2))
    status, stop = "time_cap", float(time_cap)
    if initial_loss <= target:
        status, stop = "fitted", 0.
    elif time_cap > 0 and derivative_sign(0.) < 0:
        minimum = float(time_cap)
        if derivative_sign(time_cap) > 0:
            minimum = float(brentq(derivative_sign, 0., time_cap,
                                   xtol=1e-12, rtol=1e-14))
        if spectral_loss(minimum) <= target:
            stop = float(brentq(lambda t: spectral_loss(t) - target,
                                0., minimum, xtol=1e-12, rtol=1e-14))
            status = "fitted"
    if stop == 0:
        train_f, z = f0.copy(), np.zeros(m)
    else:
        with np.errstate(over="ignore", invalid="ignore"):
            exponent = -alpha * eigenvalues[active] * stop
            train_f = labels + vectors[:, active] @ (np.exp(exponent) * components[active])
            integral = np.empty(np.count_nonzero(active))
            lam = eigenvalues[active]
            nonzero = lam != 0
            integral[nonzero] = np.expm1(exponent[nonzero]) / lam[nonzero]
            integral[~nonzero] = -alpha * stop
            z = vectors[:, active] @ (integral * components[active])
    return dict(time=stop, status=status, train_f=train_f, z=z,
                state=np.concatenate((train_f, z)),
                loss=float(np.mean((train_f-labels)**2)),
                eigenvalues=eigenvalues,
                eigen_residual=float(np.max(np.abs(theta @ vectors - vectors * eigenvalues))),
                orthogonality_residual=float(np.max(np.abs(vectors.T @ vectors-np.eye(m)))),
                integral_identity_residual=float(np.max(np.abs(f0 + theta @ z - train_f))))
