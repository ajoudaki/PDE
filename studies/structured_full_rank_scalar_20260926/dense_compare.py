"""Dense two-hidden-tanh comparison core; no experiment runs on import.

Inputs ``u`` have shape (m, 2) and unit Euclidean norm, already incorporating
the maintained book's x/sqrt(d) normalization. No further sqrt(2) is applied.
The unhalved training loss is mean((f-y)**2), f=c@h2/n, and mobilities are
(n, 1, n). Every initialized W is materialized and then trained as a fully
unrestricted dense matrix: this module implements no response-memory closure.

At a fixed seed, w and c are identical for every initialization method.
Each block/method uses its own SeedSequence([seed, fixed_stream_code]).
No global RNG, Python hash, target-dependent normalization, or implicit
reset of readout weights is used.

Fastfood uses normalized H and W=S H G Pi H B, with iid G_j~N(0,1),
independent sign B, uniform permutation Pi, and S_i=chi_n/||G||_2 with
independent chi_n draws. Before S, every row norm is ||G||_2/sqrt(n), so
the final row norms are chi_n/sqrt(n), the Gaussian row-norm law. Thus
E[||W||_F**2/n]=1 without normalizing the realized sample to a fixed norm.
This does not assert a Gaussian joint matrix law or Gaussian training law.
All other initializers likewise have expected mean squared singular value 1;
orthogonal/sign initializers have that value exactly.

Functions do not mutate supplied states. Integration is fixed-step Heun or
RK4, with the last step shortened to hit time_cap. Target checks occur at
EVERY accepted step, regardless of history sampling. The recorded first
target is the first accepted grid time, with its preceding time bracket;
it is not an exact continuous-time crossing. Refinement is the caller's
responsibility. Motion diagnostics are relative to integrate's input state.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from numbers import Integral, Real
from typing import Callable

import numpy as np


METHODS = (
    "gaussian", "gaussian_control", "hd", "hdhd", "fastfood",
    "reflection4", "diagonal",
)
_MIDDLE_STREAMS = {
    "gaussian": 101, "gaussian_control": 102, "hd": 201,
    "hdhd": 202, "fastfood": 203, "reflection4": 204, "diagonal": 205,
}


@dataclass(frozen=True)
class State:
    """Weights or velocity: w (n,2), W (n,n), c (n,), float64 arrays."""

    w: np.ndarray
    W: np.ndarray
    c: np.ndarray

    @property
    def width(self) -> int:
        return int(self.c.size)

    def copy(self) -> "State":
        return State(self.w.copy(), self.W.copy(), self.c.copy())


@dataclass(frozen=True)
class ForwardPass:
    z1: np.ndarray
    z2: np.ndarray
    h1: np.ndarray
    h2: np.ndarray
    output: np.ndarray


@dataclass(frozen=True)
class IntegrationResult:
    state: State
    history: dict[str, np.ndarray]
    first_target_time: float | None
    first_target_mse: float | None
    first_target_bracket: tuple[float, float] | None
    first_target_step: int | None
    stop_reason: str
    steps: int
    time: float
    motion: dict[str, float]
    loss_increase_count: int
    max_mse_increase: float


def _integer(value, name: str, *, minimum: int = 1) -> int:
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral):
        raise ValueError(f"{name} must be an integer >= {minimum}")
    if value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return int(value)


def _real(value, name: str, *, positive: bool = False) -> float:
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite real number")
    value = float(value)
    if not np.isfinite(value) or value < 0 or (positive and value == 0):
        qualifier = "positive" if positive else "nonnegative"
        raise ValueError(f"{name} must be finite and {qualifier}")
    return value


def _rng(seed: int, stream: int) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence([seed, stream]))


def _signs(rng: np.random.Generator, n: int) -> np.ndarray:
    return (2 * rng.integers(0, 2, size=n) - 1).astype(np.float64)


@lru_cache(maxsize=8)
def _hadamard(n: int) -> np.ndarray:
    if n & (n - 1):
        raise ValueError("Hadamard initializers require a power-of-two width")
    H = np.ones((1, 1), dtype=np.float64)
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    H /= np.sqrt(n)
    H.flags.writeable = False
    return H


def initialize(width: int, seed: int, method: str) -> State:
    """Draw dense initial weights, preserving matched outer blocks by seed.

    ``hd`` means H D (right independent sign diagonal). ``hdhd`` means
    D1 H D2 H D3 with all three sign diagonals iid and independent.
    ``reflection4`` has exactly four uniformly selected negative central
    signs and independent outer signs, and requires width >= 4.
    Gaussian and Gaussian-control matrices are independent of each other.
    """
    n = _integer(width, "width")
    seed = _integer(seed, "seed", minimum=0)
    if method not in METHODS:
        raise ValueError(f"method must be one of {METHODS}")
    w = _rng(seed, 1).standard_normal((n, 2))
    c = _rng(seed, 2).standard_normal(n) / n
    rng = _rng(seed, _MIDDLE_STREAMS[method])
    if method in ("gaussian", "gaussian_control"):
        W = rng.standard_normal((n, n)) / np.sqrt(n)
    elif method == "diagonal":
        W = np.diag(_signs(rng, n))
    else:
        H = _hadamard(n)
        if method == "hd":
            W = H * _signs(rng, n)[None, :]
        elif method in ("hdhd", "reflection4"):
            d1, d3 = _signs(rng, n), _signs(rng, n)
            if method == "hdhd":
                d2 = _signs(rng, n)
            else:
                if n < 4:
                    raise ValueError("reflection4 requires width >= 4")
                d2 = np.ones(n)
                d2[rng.choice(n, size=4, replace=False)] = -1.0
            W = d1[:, None] * ((H * d2[None, :]) @ H) * d3[None, :]
        else:  # fastfood
            g = rng.standard_normal(n)
            while np.linalg.norm(g) == 0.0:  # only an exact-zero guard
                g = rng.standard_normal(n)
            permutation = rng.permutation(n)
            b = _signs(rng, n)
            s = np.sqrt(rng.chisquare(n, size=n)) / np.linalg.norm(g)
            right = H[permutation, :] * b[None, :]
            W = s[:, None] * ((H * g[None, :]) @ right)
    return State(np.ascontiguousarray(w), np.ascontiguousarray(W), c)


def _check_state(state: State) -> None:
    if not isinstance(state, State):
        raise TypeError("state must be State")
    if not all(isinstance(x, np.ndarray) and x.dtype == np.float64
               for x in (state.w, state.W, state.c)):
        raise ValueError("state arrays must be NumPy float64 arrays")
    if state.c.ndim != 1 or state.width < 1:
        raise ValueError("c must be a nonempty vector")
    n = state.width
    if state.w.shape != (n, 2) or state.W.shape != (n, n):
        raise ValueError("state shapes must be w=(n,2), W=(n,n), c=(n,)")
    if not _finite_state(state):
        raise ValueError("state arrays must be finite")


def _finite_state(state: State) -> bool:
    return all(np.all(np.isfinite(x)) for x in (state.w, state.W, state.c))


def _inputs(u) -> np.ndarray:
    raw = np.asarray(u)
    if raw.dtype.kind not in "iuf":
        raise ValueError("u must contain real numbers")
    u = np.ascontiguousarray(raw, dtype=np.float64)
    if u.ndim != 2 or u.shape[1] != 2 or u.shape[0] < 1:
        raise ValueError("u must have shape (m,2), with m >= 1")
    if not np.all(np.isfinite(u)):
        raise ValueError("u must be finite")
    if not np.allclose(np.sum(u * u, axis=1), 1.0, rtol=1e-12, atol=1e-12):
        raise ValueError("u rows must already be unit Euclidean vectors")
    return u


def _labels(y, m: int) -> np.ndarray:
    raw = np.asarray(y)
    if raw.dtype.kind not in "iuf":
        raise ValueError("y must contain real numbers")
    y = np.ascontiguousarray(raw, dtype=np.float64)
    if y.shape != (m,) or not np.all(np.isfinite(y)):
        raise ValueError("y must be a finite vector with shape (m,)")
    return y


def _forward(state: State, u: np.ndarray) -> ForwardPass:
    z1 = state.w @ u.T
    h1 = np.tanh(z1)
    z2 = state.W @ h1
    h2 = np.tanh(z2)
    output = (state.c @ h2) / state.width
    return ForwardPass(z1, z2, h1, h2, output)


def forward(state: State, u) -> ForwardPass:
    """Evaluate the dense network on normalized row-wise circle inputs."""
    _check_state(state)
    return _forward(state, _inputs(u))


def _sech_squared(z: np.ndarray) -> np.ndarray:
    # Mathematically 1-tanh(z)**2; stable after tanh rounds to +/-1.
    with np.errstate(under="ignore"):
        e = np.exp(-np.abs(z))
        return (2.0 * e / (1.0 + e * e)) ** 2


def _rhs(state: State, u: np.ndarray, y: np.ndarray,
         fields: ForwardPass | None = None) -> State:
    if fields is None:
        fields = _forward(state, u)
    r = fields.output - y
    delta2 = state.c[:, None] * _sech_squared(fields.z2)
    delta1 = _sech_squared(fields.z1) * (state.W.T @ delta2)
    m, n = y.size, state.width
    delta2_r = delta2 * r[None, :]
    wdot = (-2.0 / m) * ((delta1 * r[None, :]) @ u)
    Wdot = (-2.0 / (m * n)) * (delta2_r @ fields.h1.T)
    cdot = (-2.0 / m) * (fields.h2 @ r)
    return State(wdot, Wdot, cdot)


def rhs(state: State, u, y) -> State:
    """Exact canonical GF RHS, with unrestricted dense W velocity."""
    _check_state(state)
    u = _inputs(u)
    return _rhs(state, u, _labels(y, u.shape[0]))


def _add(state: State, velocity: State, step: float) -> State:
    return State(state.w + step * velocity.w,
                 state.W + step * velocity.W,
                 state.c + step * velocity.c)


def _step(state: State, u: np.ndarray, y: np.ndarray, dt: float,
          method: str, fields: ForwardPass | None = None) -> State:
    k1 = _rhs(state, u, y, fields)
    if method == "heun":
        k2 = _rhs(_add(state, k1, dt), u, y)
        return State(state.w + (dt / 2) * (k1.w + k2.w),
                     state.W + (dt / 2) * (k1.W + k2.W),
                     state.c + (dt / 2) * (k1.c + k2.c))
    k2 = _rhs(_add(state, k1, dt / 2), u, y)
    k3 = _rhs(_add(state, k2, dt / 2), u, y)
    k4 = _rhs(_add(state, k3, dt), u, y)
    return State(state.w + (dt / 6) * (k1.w + 2*k2.w + 2*k3.w + k4.w),
                 state.W + (dt / 6) * (k1.W + 2*k2.W + 2*k3.W + k4.W),
                 state.c + (dt / 6) * (k1.c + 2*k2.c + 2*k3.c + k4.c))


def heun_step(state: State, u, y, dt: float) -> State:
    """One simultaneous explicit-trapezoidal (Heun) step, no mutation."""
    _check_state(state)
    u = _inputs(u)
    return _step(state, u, _labels(y, u.shape[0]),
                 _real(dt, "dt", positive=True), "heun")


def rk4_step(state: State, u, y, dt: float) -> State:
    """One classical fourth-order Runge--Kutta step, no mutation."""
    _check_state(state)
    u = _inputs(u)
    return _step(state, u, _labels(y, u.shape[0]),
                 _real(dt, "dt", positive=True), "rk4")


def _motion(state: State, initial: State, fields: ForwardPass,
            initial_fields: ForwardPass) -> dict[str, float]:
    h1_motion = float(np.sqrt(np.mean((fields.h1 - initial_fields.h1)**2)))
    h2_motion = float(np.sqrt(np.mean((fields.h2 - initial_fields.h2)**2)))
    return {
        "w_motion_rms": float(np.sqrt(np.mean((state.w - initial.w)**2))),
        "W_motion_frobenius_over_sqrt_n": float(
            np.linalg.norm(state.W - initial.W) / np.sqrt(state.width)),
        "c_motion_rms": float(np.sqrt(np.mean((state.c - initial.c)**2))),
        "h1_motion_rms": h1_motion,
        "h2_motion_rms": h2_motion,
        "h1_relative_motion": h1_motion / max(
            float(np.sqrt(np.mean(initial_fields.h1**2))), np.finfo(float).tiny),
        "h2_relative_motion": h2_motion / max(
            float(np.sqrt(np.mean(initial_fields.h2**2))), np.finfo(float).tiny),
    }


def motion(state: State, initial: State, u) -> dict[str, float]:
    """Weight and training-feature motions relative to a chosen reference.

    w/c RMS is per entry; W uses Frobenius/sqrt(n), matching its initial
    order-one operator scale. Hidden RMS is per neuron/sample entry.
    """
    _check_state(state)
    _check_state(initial)
    if state.width != initial.width:
        raise ValueError("state and initial must have equal width")
    u = _inputs(u)
    return _motion(state, initial, _forward(state, u), _forward(initial, u))


def initializer_diagnostics(state: State, *, spectral: bool = False) -> dict[str, float]:
    """Normalization diagnostics; optionally pay for a full dense SVD."""
    _check_state(state)
    row_norm2 = np.sum(state.W * state.W, axis=1)
    result = {
        "mean_squared_singular_value": float(np.mean(row_norm2)),
        "row_norm_min": float(np.sqrt(np.min(row_norm2))),
        "row_norm_max": float(np.sqrt(np.max(row_norm2))),
        "entry_mean": float(np.mean(state.W)),
        "entry_variance": float(np.var(state.W)),
        "w_rms": float(np.sqrt(np.mean(state.w**2))),
        "stored_c_rms": float(np.sqrt(np.mean(state.c**2))),
    }
    if spectral:
        singular = np.linalg.svd(state.W, compute_uv=False)
        result.update(singular_max=float(singular[0]),
                      singular_min=float(singular[-1]),
                      singular_std=float(np.std(singular)))
    return result


def integrate(state: State, u, y, *, time_cap: float, dt: float,
              target_train_mse: float | None = None, check_interval: int = 10,
              method: str = "heun", max_steps: int | None = None,
              stop_at_target: bool = True,
              callback: Callable[[float, State, float], None] | None = None,
              observation_times: tuple[float, ...] = ()) -> IntegrationResult:
    """Run dense GF with explicit time/step/target stops, returning scalars.

    ``check_interval`` counts accepted steps and only controls history
    sampling. The initial and final accepted states are always recorded.
    ``first_target_bracket`` encloses the first observed grid crossing;
    fixed-step errors and possible within-step crossings are not certified.
    ``nonfinite`` returns the last finite state, never the failed trial.
    ``max_steps`` permits a hard caller budget; otherwise the time cap is
    the hard budget. No wall-clock stopping or target-dependent step size.
    ``callback(time, state, mse)`` is called initially and after EVERY
    accepted step, including a target-triggering step. It must not mutate
    state; use state.copy() to retain a rare snapshot. Optional ordered
    ``observation_times`` shorten steps to hit requested times exactly.
    """
    _check_state(state)
    u = _inputs(u)
    y = _labels(y, u.shape[0])
    time_cap = _real(time_cap, "time_cap")
    dt = _real(dt, "dt", positive=True)
    check_interval = _integer(check_interval, "check_interval")
    if method not in ("heun", "rk4"):
        raise ValueError("method must be 'heun' or 'rk4'")
    if callback is not None and not callable(callback):
        raise TypeError("callback must be callable or None")
    observation_times = tuple(_real(t, "observation time") for t in observation_times)
    if any(b <= a for a, b in zip(observation_times, observation_times[1:])):
        raise ValueError("observation_times must be strictly increasing")
    if any(t <= 0 or t > time_cap for t in observation_times):
        raise ValueError("observation_times must lie in (0,time_cap]")
    if target_train_mse is not None:
        target_train_mse = _real(target_train_mse, "target_train_mse")
    if max_steps is None:
        max_steps = int(np.ceil(time_cap / dt)) + len(observation_times) + 1
    else:
        max_steps = _integer(max_steps, "max_steps", minimum=0)
    initial = state.copy()
    current = state.copy()
    initial_fields = fields = _forward(current, u)
    mse = float(np.mean((fields.output - y)**2))
    if not np.isfinite(mse):
        raise ValueError("initial training MSE is not finite")
    rows: list[dict[str, float]] = []

    def record(t: float, step: int) -> None:
        rows.append({
            "time": t, "step": float(step), "train_mse": mse,
            "output_rms": float(np.sqrt(np.mean(fields.output**2))),
            "residual_rms": float(np.sqrt(mse)),
            "stored_c_rms": float(np.sqrt(np.mean(current.c**2))),
            **_motion(current, initial, fields, initial_fields),
        })

    t, steps = 0.0, 0
    first_time = first_mse = first_bracket = first_step = None
    increases, max_increase = 0, 0.0
    observation_index = 0
    record(t, steps)
    if callback is not None:
        callback(t, current, mse)
    if target_train_mse is not None and mse <= target_train_mse:
        first_time, first_mse, first_bracket, first_step = 0.0, mse, (0.0, 0.0), 0
    stop_reason = "time_cap"
    if first_time is not None and stop_at_target:
        stop_reason = "target"
    else:
        while t < time_cap:
            if steps >= max_steps:
                stop_reason = "max_steps"
                break
            next_stop = time_cap
            if observation_index < len(observation_times):
                next_stop = observation_times[observation_index]
            step_size = min(dt, next_stop - t)
            next_t = min(next_stop, t + step_size)
            if next_t <= t:
                stop_reason = "time_resolution"
                break
            with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
                trial = _step(current, u, y, step_size, method, fields)
                trial_fields = _forward(trial, u)
                trial_mse = float(np.mean((trial_fields.output - y)**2))
            if not _finite_state(trial) or not np.isfinite(trial_mse):
                stop_reason = "nonfinite"
                break
            increase = trial_mse - mse
            if increase > 1e-12 * max(1.0, mse):
                increases += 1
                max_increase = max(max_increase, increase)
            previous_t = t
            current, fields, mse = trial, trial_fields, trial_mse
            t, steps = next_t, steps + 1
            if (observation_index < len(observation_times)
                    and t == observation_times[observation_index]):
                observation_index += 1
            hit = target_train_mse is not None and mse <= target_train_mse
            if hit and first_time is None:
                first_time, first_mse = t, mse
                first_bracket, first_step = (previous_t, t), steps
            if steps % check_interval == 0:
                record(t, steps)
            if callback is not None:
                callback(t, current, mse)
            if hit and stop_at_target:
                stop_reason = "target"
                break
    if rows[-1]["step"] != steps:
        record(t, steps)
    history = {key: np.asarray([row[key] for row in rows], dtype=np.float64)
               for key in rows[0]}
    history["step"] = history["step"].astype(np.int64)
    return IntegrationResult(
        state=current, history=history, first_target_time=first_time,
        first_target_mse=first_mse, first_target_bracket=first_bracket,
        first_target_step=first_step, stop_reason=stop_reason, steps=steps,
        time=t, motion=_motion(current, initial, fields, initial_fields),
        loss_increase_count=increases, max_mse_increase=max_increase,
    )
