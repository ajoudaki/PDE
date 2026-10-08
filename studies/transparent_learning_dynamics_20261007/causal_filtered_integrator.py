"""Residual-filtered numerical integration of the full causal law.

Derived from the frozen causal_panel_simulator.py; old evidence is untouched.
Only the step's deterministic training force changes. Raw residuals, all
learned writes, directed frozen-coefficient tangents, and passive roles remain
separate. This is a first-order integrator, not a new continuous model.
"""
from __future__ import annotations
import time
from typing import Any
import numpy as np
from causal_panel_simulator import (
    DEFAULT_INPUTS, _ColoredGaussianFamily, _activation, _TangentHistory,
    estimate_memory_bytes, _record_gram, _history_sum, _add_tangent_history,
    _flat_gram, replay_frozen_coefficients as _original_replay,
)
Array = np.ndarray


def filter_deficit(kernel, deficit, step):
    matrix = np.eye(len(deficit)) + step*kernel
    result = np.linalg.solve(matrix, deficit)
    defect = float(np.max(abs(matrix@result-deficit)))
    if not np.isfinite(result).all() or defect > 1e-10*(1+float(np.max(abs(deficit)))):
        raise FloatingPointError("Filtered residual solve failed")
    return result, defect


def simulate_population(
    labels: Array | tuple[float, ...] = (0.15, -0.15), *,
    dt: float = 0.4, steps: int = 60, population_size: int = 1024, seed: int = 0,
    input_vectors: Array | None = None,
    learned_forward_memory: bool = True, learned_backward_memory: bool = True,
    reciprocal_correction: bool = True, learned_middle_memory: bool | None = None,
    rank_rtol: float = 1e-12, rank_atol: float = 0.,
    memory_limit_mb: float = 3072., return_fields: bool = False,
    integrator: str = "filtered",
) -> dict[str, Any]:
    """Run Euler or residual-filtered steps of the same full causal flow.

    Input rows have shape [p,d], are normalized, and their first m rows have
    labels. C,D,R arrays have shape [steps+1,steps+1,p,p], with evaluated
    sample first and driving sample second. Formal primitive probes freeze
    the deterministic population coefficients, as in the frozen simulator.
    """
    if integrator not in ("euler", "filtered"):
        raise ValueError("Unknown integrator")
    if integrator == "filtered" and (not learned_forward_memory or not learned_backward_memory
            or not reciprocal_correction or learned_middle_memory is False):
        raise ValueError("Filtered-kernel claim is restricted to the full model")
    started = time.perf_counter()
    y = np.asarray(labels, dtype=np.float64)
    if y.ndim != 1 or len(y) < 1 or not np.all(np.isfinite(y)):
        raise ValueError("labels must be a nonempty finite one-dimensional array")
    if not isinstance(steps, (int, np.integer)) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    if not isinstance(population_size, (int, np.integer)) or population_size < 1:
        raise ValueError("population_size must be a positive integer")
    if not np.isfinite(dt) or dt <= 0:
        raise ValueError("dt must be positive and finite")
    if (not np.isfinite(rank_rtol) or not np.isfinite(rank_atol)
            or rank_rtol < 0 or rank_atol < 0):
        raise ValueError("Rank tolerances must be finite and nonnegative")
    if not np.isfinite(memory_limit_mb) or memory_limit_mb <= 0:
        raise ValueError("memory_limit_mb must be positive and finite")
    vectors = np.asarray(DEFAULT_INPUTS if input_vectors is None else input_vectors,
                         dtype=np.float64)
    m = len(y)
    if (vectors.ndim != 2 or vectors.shape[0] < m or vectors.shape[1] < 1
            or not np.all(np.isfinite(vectors))):
        raise ValueError("input_vectors must be a finite [p,d] array with p>=m and d>=1")
    if not np.allclose(np.sum(vectors*vectors, axis=1), 1., atol=1e-12, rtol=1e-12):
        raise ValueError("Every input must be normalized")
    p, d = vectors.shape
    if learned_middle_memory is not None:
        learned_forward_memory = learned_backward_memory = bool(learned_middle_memory)
    memory = estimate_memory_bytes(population_size, steps, training_size=m,
                                   panel_size=p, input_dimension=d,
                                   return_fields=return_fields)
    if memory["estimated_total"] > memory_limit_mb*1024**2:
        raise MemoryError(
            f"Estimated array memory {memory['estimated_total']/1024**2:.1f} MiB "
            f"exceeds {memory_limit_mb:.1f} MiB; reduce program/population size")

    n, s = population_size, steps+1
    learning_step = dt*(2./m)
    input_gram = vectors @ vectors.T
    streams = np.random.SeedSequence(seed).spawn(3)
    root_rng, eta_rng, xi_rng = (np.random.default_rng(v) for v in streams)
    z1 = root_rng.standard_normal((n, d)) @ vectors.T
    w = np.zeros(n, dtype=np.float64)
    z1_tangent = np.zeros((n, p, m*s), dtype=np.float64)
    w_tangent = np.zeros((n, m*s), dtype=np.float64)
    tangents = _TangentHistory(n, steps, m)
    eta_family = _ColoredGaussianFamily(n, p*s, eta_rng, rank_rtol, rank_atol)
    xi_family = _ColoredGaussianFamily(n, p*s, xi_rng, rank_rtol, rank_atol)
    h1_history = np.empty((s, n, p), dtype=np.float64)
    h2_history, d1_history, d2_history = (np.empty_like(h1_history) for _ in range(3))
    C1 = np.zeros((s, s, p, p), dtype=np.float64)
    C2, D1, D2, Rh, Rd = (np.zeros_like(C1) for _ in range(5))
    f = np.zeros((s, p), dtype=np.float64)
    residual = np.zeros((s, m), dtype=np.float64)
    write_deficit = np.zeros_like(residual)
    solve_defect = np.zeros(s)
    fields = None
    if return_fields:
        fields = {name: np.empty((s, n, p), dtype=np.float64)
                  for name in ("z1", "z2", "b1", "eta", "xi")}
        fields["w"] = np.empty((s, n), dtype=np.float64)
    timing = {"sampling_seconds": 0., "upper_tangent_seconds": 0.,
              "lower_tangent_seconds": 0.}
    maximum_field = np.zeros(s)
    maximum_response = np.zeros(s)
    active = np.arange(m)
    passive = np.arange(m, p)

    for k in range(s):
        previous_dimension, current_dimension = m*k, m*(k+1)
        h1, gate1, curvature1 = _activation(z1)
        h1_history[k] = h1
        h1_tangent = gate1[:, :, None]*z1_tangent[:, :, :previous_dimension]
        tangents.lower[k][...] = h1_tangent[:, :m, :]
        if k:
            Rh[k, :k, :, :m] = h1_tangent.mean(axis=0).reshape(p, k, m).transpose(1, 0, 2)
        _record_gram(C1, h1_history, k)

        tick = time.perf_counter()
        eta = eta_family.append(h1)
        timing["sampling_seconds"] += time.perf_counter()-tick
        forward_coefficients = np.zeros((k, p, m))
        if reciprocal_correction:
            forward_coefficients += Rh[k, :k, :, :m]
        if learned_forward_memory:
            forward_coefficients += learning_step*C1[k, :k, :, :m]*write_deficit[:k, None, :]
        z2 = eta.copy()
        if k:
            z2 += _history_sum(forward_coefficients, d2_history[:k, :, :m])

        tick = time.perf_counter()
        z2_tangent = np.zeros((n, p, current_dimension))
        z2_tangent[:, active, previous_dimension+active] = 1.
        _add_tangent_history(z2_tangent, forward_coefficients, tangents.upper)
        h2, gate2, curvature2 = _activation(z2)
        h2_history[k] = h2
        d2 = gate2*w[:, None]
        d2_history[k] = d2
        delta2_tangent = (
            curvature2[:, :, None]*w[:, None, None]*z2_tangent
            + gate2[:, :, None]*w_tangent[:, None, :current_dimension])
        tangents.upper[k][...] = delta2_tangent[:, :m, :]
        Rd[k, :k+1, :, :m] = delta2_tangent.mean(axis=0).reshape(
            p, k+1, m).transpose(1, 0, 2)
        if len(passive):
            Rd[k, k, passive, passive] = np.mean(w[:, None]*curvature2[:, m:], axis=0)
        timing["upper_tangent_seconds"] += time.perf_counter()-tick
        f[k] = np.mean(w[:, None]*h2, axis=0)
        residual[k] = y-f[k, :m]
        _record_gram(C2, h2_history, k)
        _record_gram(D2, d2_history, k)

        tick = time.perf_counter()
        xi = xi_family.append(d2)
        timing["sampling_seconds"] += time.perf_counter()-tick
        backward_coefficients = np.zeros((k+1, p, m))
        if reciprocal_correction:
            backward_coefficients += Rd[k, :k+1, :, :m]
        if learned_backward_memory and k:
            backward_coefficients[:k] += (
                learning_step*D2[k, :k, :, :m]*write_deficit[:k, None, :])
        b1 = xi+_history_sum(backward_coefficients, h1_history[:k+1, :, :m])
        if reciprocal_correction and len(passive):
            b1[:, m:] += Rd[k, k, passive, passive][None, :]*h1[:, m:]
        d1 = gate1*b1
        d1_history[k] = d1
        _record_gram(D1, d1_history, k)
        current_kernel = C2[k, k, :m, :m] + C1[k, k, :m, :m]*D2[k, k, :m, :m]
        current_kernel += input_gram[:m, :m]*D1[k, k, :m, :m]
        if integrator == "filtered":
            write_deficit[k], solve_defect[k] = filter_deficit(current_kernel, residual[k], learning_step)
        else:
            write_deficit[k] = residual[k]

        tick = time.perf_counter()
        b1_tangent = np.zeros((n, m, current_dimension))
        b1_tangent[:, active, previous_dimension+active] = 1.
        _add_tangent_history(b1_tangent, backward_coefficients[:, :m, :m],
                             tangents.lower)
        delta1_tangent = (
            curvature1[:, :m, None]*b1[:, :m, None]
            * z1_tangent[:, :m, :current_dimension]
            + gate1[:, :m, None]*b1_tangent)
        timing["lower_tangent_seconds"] += time.perf_counter()-tick

        if fields is not None:
            for name, value in (("z1", z1), ("z2", z2), ("b1", b1),
                                ("eta", eta), ("xi", xi), ("w", w)):
                fields[name][k] = value
        maximum_field[k] = max(float(np.max(np.abs(v))) for v in (z1, z2, b1, w))
        maximum_response[k] = max(float(np.max(np.abs(Rh[k]))),
                                  float(np.max(np.abs(Rd[k]))))
        if not (np.all(np.isfinite(f[k])) and np.isfinite(maximum_field[k])
                and np.isfinite(maximum_response[k])):
            raise FloatingPointError(f"Nonfinite field/response at step {k}, time {k*dt}")
        if k < steps:
            force = input_gram[:, :m]*write_deficit[k][None, :]
            z1 += learning_step*(d1[:, :m] @ force.T)
            z1_tangent[:, :, :current_dimension] += learning_step*np.matmul(force, delta1_tangent)
            w += learning_step*(h2[:, :m] @ write_deficit[k])
            w_tangent[:, :current_dimension] += learning_step*np.matmul(
                write_deficit[k], gate2[:, :m, None]*z2_tangent[:, :m, :])

    if fields is not None:
        fields.update({"h1": h1_history, "h2": h2_history,
                       "delta1": d1_history, "delta2": d2_history})
    current = np.arange(s)
    kernel = C2[current, current]+C1[current, current]*D2[current, current]
    kernel += input_gram[None, :, :]*D1[current, current]
    frozen_f = np.zeros_like(f)
    initial_kernel = C2[0, 0]
    for k in range(steps):
        fixed_deficit = y-frozen_f[k, :m]
        if integrator == "filtered":
            fixed_deficit, _ = filter_deficit(initial_kernel[:m, :m], fixed_deficit, learning_step)
        frozen_f[k+1] = frozen_f[k]+learning_step*(initial_kernel[:, :m] @ fixed_deficit)
    frozen_limit = initial_kernel[:, :m] @ np.linalg.pinv(
        initial_kernel[:m, :m], hermitian=True, rcond=1e-12) @ y
    parity = 0
    if m == 2:
        parity = 1 if np.isclose(y[0], y[1], atol=1e-14, rtol=1e-12) else (
            -1 if np.isclose(y[0], -y[1], atol=1e-14, rtol=1e-12) else 0)
    diagnostics = {
        "integrator": integrator, "filter_solve_defect": solve_defect,
        "eta": eta_family.diagnostics(_flat_gram(C1)),
        "xi": xi_family.diagnostics(_flat_gram(D2)),
        "memory_bytes": memory,
        "maximum_absolute_field": maximum_field,
        "maximum_absolute_response": maximum_response,
        "feature_gram_drift": {
            "layer1": np.linalg.norm(C1[current, current]-C1[0, 0], axis=(1, 2)),
            "layer2": np.linalg.norm(C2[current, current]-C2[0, 0], axis=(1, 2)),
        },
        "frozen_feature_discrete_prediction": frozen_f,
        "frozen_feature_limit": frozen_limit,
        "frozen_feature_limit_training_residual": y-frozen_limit[:m],
        "frozen_feature_deviation": np.linalg.norm(f-frozen_f, axis=1),
        "initial_top_training_gram_eigenvalues": np.linalg.eigvalsh(initial_kernel[:m, :m]),
        "symmetry": {
            "label_exchange_parity": parity,
            "training_prediction_defect": f[:, 0]-parity*f[:, 1] if parity else None,
            "layer1_training_diagonal_defect": (
                C1[current, current, 0, 0]-C1[current, current, 1, 1]) if m == 2 else None,
            "layer2_training_diagonal_defect": (
                C2[current, current, 0, 0]-C2[current, current, 1, 1]) if m == 2 else None,
            "interpretation": "Finite-quadrature defects; not forced to zero. Two-sample fields are absent for m!=2.",
        },
        "timing": timing,
        "kernel_diagnostic_is_gradient_kernel": bool(
            learned_forward_memory and learned_backward_memory and reciprocal_correction),
    }
    diagnostics["timing"]["total_seconds"] = time.perf_counter()-started
    return {
        "time": dt*np.arange(s, dtype=np.float64), "f": f, "c": residual,
        "write_deficit": write_deficit,
        "C": {"layer1": C1, "layer2": C2}, "D": {"layer1": D1, "layer2": D2},
        "R": {"h": Rh, "delta": Rd}, "kernel_diagnostic": kernel,
        "diagnostics": diagnostics, "fields": fields,
        "config": {
            "labels": y.copy(), "dt": float(dt), "steps": int(steps),
            "population_size": int(n), "seed": int(seed), "input_vectors": vectors.copy(),
            "input_gram": input_gram, "training_size": m, "panel_size": p, "input_dimension": d,
            "learned_forward_memory": bool(learned_forward_memory),
            "learned_backward_memory": bool(learned_backward_memory),
            "reciprocal_correction": bool(reciprocal_correction),
            "rank_rtol": float(rank_rtol), "rank_atol": float(rank_atol),
            "dtype": "float64", "integrator": integrator,
        },
    }

def replay_frozen_coefficients(result, **probes):
    # Formal local derivatives freeze the effective write coefficients,
    # not just the raw residual. No response of a population mean is inserted.
    mapped = dict(result)
    mapped["c"] = result["write_deficit"]
    return _original_replay(mapped, **probes)


def self_test():
    from causal_panel_simulator import simulate_population as original
    rng = np.random.default_rng(17)
    vectors = rng.normal(size=(7, 3))
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    y = np.array([.3, -.2, .4, -.1])
    args = dict(dt=.2, steps=4, population_size=31, seed=11,
                input_vectors=vectors, return_fields=True)
    old = original(y, **args)
    euler = simulate_population(y, integrator="euler", **args)
    euler_error = max(np.max(abs(old[key][part]-euler[key][part]))
                      for key in ("C", "D", "R", "fields") for part in old[key])
    assert euler_error < 1e-12
    full = simulate_population(y, **args)
    replay = replay_frozen_coefficients(full)
    replay_error = max(np.max(abs(replay[key]-(full["f"] if key=="f" else full["fields"][key])))
                       for key in ("h1","h2","delta2","f"))
    probe_error = 0.
    for family,observable,response in (("xi","h1","h"),("eta","delta2","delta")):
        for j,b in ((0,0),(1,3),(1,4),(2,6)):
            eps=1e-5
            plus=replay_frozen_coefficients(full,**{family+"_probe":(j,b,eps)})
            minus=replay_frozen_coefficients(full,**{family+"_probe":(j,b,-eps)})
            measured=((plus[observable]-minus[observable])/(2*eps)).mean(1)
            probe_error=max(probe_error,float(np.max(abs(measured-full["R"][response][:,j,:,b]))))
            if b>=4:
                assert np.array_equal(plus["f"][:,:4],replay["f"][:,:4])
    reconstruction=np.zeros_like(full["f"])
    for k in range(5):
        reconstruction[k]=.1*np.einsum("jab,jb->a",full["C"]["layer2"][k,:k,:,:4],
                                        full["write_deficit"][:k])
    history_error=float(np.max(abs(reconstruction-full["f"])))
    assert replay_error<1e-12 and probe_error<1e-8 and history_error<1e-12
    zero=simulate_population(np.zeros(4),**args)
    assert not np.any(zero["f"])
    return dict(euler_equivalence=float(euler_error),replay=float(replay_error),
                primitive_probe=probe_error,history_identity=history_error)


if __name__=="__main__":
    import json
    print(json.dumps(self_test(),indent=2))

