"""Streaming adaptive integration of the same unrestricted dense network.

This is a numerical time integrator, not a model reduction. It stores every
entry of w, W and c and evaluates exactly the canonical dense RHS used by
dense_compare.py. Initial states come from that module without modification.

SciPy's RK45 (Dormand--Prince 5(4)) or RK23 supplies the stages, embedded
error estimator, acceptance controller and dense interpolant. The sole
solver customization is an error norm: maximum scaled RMS over w, W and c,
so the n**2 middle entries cannot dilute errors in the outer blocks.
Absolute tolerance for W entries is atol/sqrt(n); w/c use atol. Relative
tolerance is componentwise, as in SciPy. This is local error control, not
an a priori global error certificate; whole-circle tolerance refinement
remains necessary.

No full trajectory is retained. A first downward MSE crossing is located
inside the first accepted crossing step using the SciPy dense interpolant
and Brent root finding. The returned state lies at that boundary (nudged
minimally forward if floating rounding leaves its MSE above the threshold).
Both the accepted-step bracket and interpolated stopping time are returned.
All physical-time values use the original canonical training clock.

Callers must select one BLAS thread before importing NumPy/SciPy and provide
their own campaign budget. A deadline is an absolute time.time() timestamp.
No training or benchmark runs on import.
"""

from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Callable

import numpy as np
import scipy
from scipy.integrate import RK23, RK45
from scipy.optimize import brentq

import dense_compare as dense


@dataclass(frozen=True)
class WideResult:
    state: dense.State
    time: float
    train_mse: float
    history: dict[str, np.ndarray]
    nfev: int
    nsteps: int
    nreject: int
    stop_reason: str
    first_target_time: float | None
    first_target_bracket: tuple[float, float] | None
    max_loss_rise: float
    wall_seconds: float
    settings: dict


class _DeadlineReached(Exception):
    pass


class _BlockErrorNorm:
    """Override the inspected SciPy 1.13 RK error-norm hook only."""

    def __init__(self, *args, block_slices, **kwargs):
        self.block_slices = block_slices
        self.error_evaluations = 0
        self.last_error_norm = 0.0
        super().__init__(*args, **kwargs)

    def _estimate_error_norm(self, K, h, scale):
        self.error_evaluations += 1
        error = self._estimate_error(K, h)
        norms = []
        for sl in self.block_slices:
            scaled = error[sl] / scale[sl]
            norms.append(float(np.linalg.norm(scaled) / np.sqrt(scaled.size)))
        self.last_error_norm = max(norms)
        if not np.isfinite(self.last_error_norm):
            return np.inf
        return self.last_error_norm


class _BlockRK45(_BlockErrorNorm, RK45):
    pass


class _BlockRK23(_BlockErrorNorm, RK23):
    pass


def pack(state: dense.State) -> np.ndarray:
    """Copy the full state into a contiguous SciPy state vector."""
    n = state.width
    result = np.empty(n*n+3*n, dtype=np.float64)
    result[:2*n] = state.w.ravel()
    result[2*n:2*n+n*n] = state.W.ravel()
    result[-n:] = state.c
    return result


def unpack(values: np.ndarray, width: int) -> dense.State:
    """Views into a full dense state vector, with no compression."""
    n = width
    return dense.State(values[:2*n].reshape(n,2),
                       values[2*n:2*n+n*n].reshape(n,n), values[-n:])


def flat_rhs(values: np.ndarray, width: int, u: np.ndarray,
             labels: np.ndarray) -> np.ndarray:
    """Canonical dense RHS, writing the middle derivative directly to output.

    This avoids an extra n-by-n temporary and copy but does not approximate
    its rank-m contraction or restrict the trained W in any way.
    """
    state = unpack(values, width)
    fields = dense._forward(state, u)
    residual = fields.output-labels
    delta2 = state.c[:,None] * dense._sech_squared(fields.z2)
    delta1 = dense._sech_squared(fields.z1) * (state.W.T @ delta2)
    answer = np.empty_like(values)
    velocity = unpack(answer,width)
    m = len(labels)
    np.matmul((delta1*residual[None,:]),u,out=velocity.w)
    velocity.w[...] *= -2.0/m
    np.matmul((delta2*residual[None,:]),fields.h1.T,out=velocity.W)
    velocity.W[...] *= -2.0/(m*width)
    np.matmul(fields.h2,residual,out=velocity.c)
    velocity.c[...] *= -2.0/m
    return answer


def integrate(state: dense.State, u, y, *, time_cap: float,
              rtol: float = 1e-5, atol: float = 1e-8,
              target_train_mse: float | None = 1e-6,
              method: str = "RK45", first_step: float = .05,
              max_step: float = 10.0, max_steps: int = 1_000_000,
              deadline: float | None = None,
              callback: Callable[[float, dense.State, float], None] | None = None,
              history_interval: float = 1.0) -> WideResult:
    """Integrate until a refined target crossing, time cap or explicit budget.

    callback(time,state,mse) runs initially and after each accepted step;
    on a crossing it receives the refined boundary state instead of the
    post-crossing endpoint. Callbacks must not mutate state. To retain a
    state independently, call state.copy(). A callback may raise to enforce
    a caller-specific budget. Integration errors remain explicit in
    stop_reason; `target` alone denotes a checked boundary crossing.
    """
    started = time.monotonic()
    dense._check_state(state)
    u = dense._inputs(u)
    y = dense._labels(y,len(u))
    time_cap = dense._real(time_cap,"time_cap")
    rtol = dense._real(rtol,"rtol",positive=True)
    atol = dense._real(atol,"atol",positive=True)
    first_step = dense._real(first_step,"first_step",positive=True)
    max_step = dense._real(max_step,"max_step",positive=True)
    max_steps = dense._integer(max_steps,"max_steps",minimum=0)
    history_interval = dense._real(history_interval,"history_interval",positive=True)
    if method not in ("RK45","RK23"):
        raise ValueError("method must be RK45 or RK23")
    if target_train_mse is not None:
        target_train_mse = dense._real(target_train_mse,"target_train_mse")
    if deadline is not None and not np.isfinite(deadline):
        raise ValueError("deadline must be a finite UNIX timestamp")
    if callback is not None and not callable(callback):
        raise TypeError("callback must be callable")
    n = state.width
    values = pack(state)
    current = unpack(values,n)

    def mse_at(vector):
        output = dense._forward(unpack(vector,n),u).output
        return float(np.mean((output-y)**2))

    mse = mse_at(values)
    if not np.isfinite(mse):
        raise ValueError("initial training MSE is nonfinite")
    history_rows = [(0.0,mse,0.0,0.0)]
    if callback is not None:
        callback(0.0,current,mse)
    stop_reason = "time_cap"
    first_target_time = None
    bracket = None
    t,nsteps,max_rise = 0.0,0,0.0
    solver = None
    settings = {"method":method,"rtol":rtol,"atol_w":atol,"atol_W":atol/np.sqrt(n),
                "atol_c":atol,"error_norm":"maximum of per-block scaled RMS",
                "max_step":max_step,"first_step":first_step,"time_cap":time_cap,
                "target_train_mse":target_train_mse,"scipy_version":scipy.__version__,
                "threshold_method":"SciPy dense interpolant plus bracketed Brent root",
                "full_dense_state_entries":len(values)}
    if target_train_mse is not None and mse <= target_train_mse:
        stop_reason,first_target_time,bracket = "target",0.0,(0.0,0.0)
    elif deadline is not None and time.time() >= deadline:
        stop_reason = "deadline"
    elif max_steps == 0:
        stop_reason = "max_steps"
    elif time_cap > 0:
        block_slices = (slice(0,2*n),slice(2*n,2*n+n*n),slice(2*n+n*n,None))
        tolerance = np.full(values.shape,atol,dtype=np.float64)
        tolerance[block_slices[1]] /= np.sqrt(n)

        def function(time_value, vector):
            if deadline is not None and time.time() >= deadline:
                raise _DeadlineReached()
            return flat_rhs(vector,n,u,y)

        cls = _BlockRK45 if method=="RK45" else _BlockRK23
        try:
            solver = cls(function,0.0,values,time_cap,rtol=rtol,atol=tolerance,
                         max_step=max_step,first_step=min(first_step,max_step,time_cap),
                         block_slices=block_slices)
        except _DeadlineReached:
            stop_reason = "deadline"
        if solver is not None:
            while solver.status == "running":
                if nsteps >= max_steps:
                    stop_reason = "max_steps"
                    break
                old_t,old_mse = t,mse
                try:
                    with np.errstate(over="ignore",invalid="ignore",divide="ignore"):
                        message = solver.step()
                except _DeadlineReached:
                    stop_reason = "deadline"
                    break
                if solver.status == "failed":
                    stop_reason = "solver_failed"
                    settings["solver_message"] = message
                    break
                trial_mse = mse_at(solver.y)
                if not np.isfinite(trial_mse) or not np.all(np.isfinite(solver.y)):
                    stop_reason = "nonfinite"
                    break
                nsteps += 1
                max_rise = max(max_rise,trial_mse-old_mse)
                t,mse,values = float(solver.t),trial_mse,solver.y
                current = unpack(values,n)
                crossed = target_train_mse is not None and mse <= target_train_mse
                if crossed:
                    bracket = (old_t,t)
                    interpolant = solver.dense_output()
                    time_tolerance = max(1e-12,8*np.finfo(float).eps*max(1.0,abs(t)))
                    root = brentq(lambda at:mse_at(interpolant(at))-target_train_mse,
                                  old_t,t,xtol=time_tolerance,rtol=8*np.finfo(float).eps)
                    refined_values = interpolant(root)
                    refined_mse = mse_at(refined_values)
                    # Preserve <= semantics when a correctly located root
                    # evaluates just above the threshold due to rounding.
                    for _ in range(4):
                        if refined_mse <= target_train_mse:
                            break
                        root = min(t,root+max(time_tolerance,1e-9*(t-old_t)))
                        refined_values = interpolant(root)
                        refined_mse = mse_at(refined_values)
                    if (not np.isfinite(refined_mse) or refined_mse>target_train_mse
                            or abs(refined_mse-target_train_mse)>max(1e-12,1e-6*target_train_mse)):
                        stop_reason = "event_refinement_failed"
                        break
                    t,mse,values = float(root),refined_mse,refined_values
                    current = unpack(values,n)
                    first_target_time = t
                    stop_reason = "target"
                if t-history_rows[-1][0]>=history_interval or crossed or solver.status=="finished":
                    history_rows.append((t,mse,t-old_t,solver.last_error_norm))
                if callback is not None:
                    callback(t,current,mse)
                if crossed:
                    break
    if history_rows[-1][0] != t:
        history_rows.append((t,mse,0.0,solver.last_error_norm if solver is not None else 0.0))
    history_array = np.asarray(history_rows,dtype=np.float64)
    history = {name:history_array[:,j] for j,name in enumerate(
        ("time","train_mse","step_size","error_norm"))}
    nfev = solver.nfev if solver is not None else 0
    nreject = max(0,solver.error_evaluations-nsteps) if solver is not None else 0
    return WideResult(current,t,mse,history,nfev,nsteps,nreject,stop_reason,
                      first_target_time,bracket,max_rise,time.monotonic()-started,settings)
