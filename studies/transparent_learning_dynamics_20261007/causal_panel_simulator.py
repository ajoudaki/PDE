"""Finite-panel causal feature-response Euler law with particle quadrature.

Generalizes the frozen two-training-sample implementation without changing its
equations. The first m input rows train; all remaining rows are passive.
Population size is quadrature size, not dense-network width. Full response
history is retained; storage grows quadratically with steps and training size.
"""
from __future__ import annotations

import time
from typing import Any

import numpy as np

from causal_population_simulator import (
    DEFAULT_INPUTS, _ColoredGaussianFamily, _activation,
)

Array = np.ndarray


class _TangentHistory:
    """Packed active-source and active-evaluation histories."""

    def __init__(self, n: int, steps: int, m: int) -> None:
        self.buffer = np.empty(n * m * m * (steps + 1)**2, dtype=np.float64)
        self.lower: list[Array] = []
        self.upper: list[Array] = []
        offset = 0
        for k in range(steps + 1):
            for destination, dimension in ((self.lower, m*k),
                                            (self.upper, m*(k+1))):
                length = n * m * dimension
                destination.append(self.buffer[offset:offset+length].reshape(n, m, dimension))
                offset += length
        assert offset == self.buffer.size


def estimate_memory_bytes(population_size: int, steps: int, *,
                          training_size: int = 2, panel_size: int = 3,
                          input_dimension: int = 2,
                          return_fields: bool = False) -> dict[str, int]:
    """Conservative array estimate, excluding BLAS/interpreter overhead."""
    n, m, p, d, s = (population_size, training_size, panel_size,
                     input_dimension, steps+1)
    rank = min(n, p*s)
    parts = {
        "tangent_history": 8*n*m*m*s*s,
        "primal_history": 8*4*s*n*p,
        "optional_fields": 8*s*n*(5*p+1) if return_fields else 0,
        "gaussian_factors": 8*(4*n*rank + 2*p*s*rank),
        "moment_histories": 8*6*s*s*p*p,
        "covariance_diagnostic_temporaries": 8*4*(p*s)**2,
        "working_allowance": 8*12*n*p*m*s,
        "input_initialization_allowance": 8*(n*d+p*d+p*p),
    }
    parts["estimated_total"] = sum(parts.values())
    return parts


def _record_gram(destination: Array, history: Array, k: int) -> None:
    block = np.matmul(history[k].T, history[:k+1]) / history.shape[1]
    destination[k, :k+1] = block
    destination[:k+1, k] = block.transpose(0, 2, 1)


def _history_sum(coefficients: Array, history: Array) -> Array:
    count, n, m = history.shape
    p = coefficients.shape[1]
    if count == 0:
        return np.zeros((n, p), dtype=np.float64)
    left = history.transpose(1, 0, 2).reshape(n, count*m)
    right = coefficients.transpose(0, 2, 1).reshape(count*m, p)
    return left @ right


def _add_tangent_history(destination: Array, coefficients: Array,
                         history: list[Array]) -> None:
    for j, coefficient in enumerate(coefficients):
        prior = history[j]
        q = prior.shape[2]
        if q and np.any(coefficient):
            destination[:, :, :q] += np.matmul(coefficient, prior)


def _flat_gram(history: Array) -> Array:
    s, _, p, _ = history.shape
    return history.transpose(0, 2, 1, 3).reshape(s*p, s*p)


def simulate_population(
    labels: Array | tuple[float, ...] = (0.15, -0.15), *,
    dt: float = 0.4, steps: int = 60, population_size: int = 1024, seed: int = 0,
    input_vectors: Array | None = None,
    learned_forward_memory: bool = True, learned_backward_memory: bool = True,
    reciprocal_correction: bool = True, learned_middle_memory: bool | None = None,
    rank_rtol: float = 1e-12, rank_atol: float = 0.,
    memory_limit_mb: float = 3072., return_fields: bool = False,
) -> dict[str, Any]:
    """Run a fixed Euler program on m training and p-m passive inputs.

    Input rows have shape [p,d], are normalized, and their first m rows have
    labels. C,D,R arrays have shape [steps+1,steps+1,p,p], with evaluated
    sample first and driving sample second. Formal primitive probes freeze
    the deterministic population coefficients, as in the frozen simulator.
    """
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
            forward_coefficients += learning_step*C1[k, :k, :, :m]*residual[:k, None, :]
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
                learning_step*D2[k, :k, :, :m]*residual[:k, None, :])
        b1 = xi+_history_sum(backward_coefficients, h1_history[:k+1, :, :m])
        if reciprocal_correction and len(passive):
            b1[:, m:] += Rd[k, k, passive, passive][None, :]*h1[:, m:]
        d1 = gate1*b1
        d1_history[k] = d1
        _record_gram(D1, d1_history, k)

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
            force = input_gram[:, :m]*residual[k][None, :]
            z1 += learning_step*(d1[:, :m] @ force.T)
            z1_tangent[:, :, :current_dimension] += learning_step*np.matmul(force, delta1_tangent)
            w += learning_step*(h2[:, :m] @ residual[k])
            w_tangent[:, :current_dimension] += learning_step*np.matmul(
                residual[k], gate2[:, :m, None]*z2_tangent[:, :m, :])

    if fields is not None:
        fields.update({"h1": h1_history, "h2": h2_history,
                       "delta1": d1_history, "delta2": d2_history})
    current = np.arange(s)
    kernel = C2[current, current]+C1[current, current]*D2[current, current]
    kernel += input_gram[None, :, :]*D1[current, current]
    frozen_f = np.zeros_like(f)
    initial_kernel = C2[0, 0]
    for k in range(steps):
        frozen_f[k+1] = frozen_f[k]+learning_step*(
            initial_kernel[:, :m] @ (y-frozen_f[k, :m]))
    frozen_limit = initial_kernel[:, :m] @ np.linalg.pinv(
        initial_kernel[:m, :m], hermitian=True, rcond=1e-12) @ y
    parity = 0
    if m == 2:
        parity = 1 if np.isclose(y[0], y[1], atol=1e-14, rtol=1e-12) else (
            -1 if np.isclose(y[0], -y[1], atol=1e-14, rtol=1e-12) else 0)
    diagnostics = {
        "eta": eta_family.diagnostics(_flat_gram(C1)),
        "xi": xi_family.diagnostics(_flat_gram(D2)),
        "memory_bytes": memory,
        "maximum_absolute_field": maximum_field,
        "maximum_absolute_response": maximum_response,
        "feature_gram_drift": {
            "layer1": np.linalg.norm(C1[current, current]-C1[0, 0], axis=(1, 2)),
            "layer2": np.linalg.norm(C2[current, current]-C2[0, 0], axis=(1, 2)),
        },
        "frozen_feature_euler_prediction": frozen_f,
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
            "dtype": "float64",
        },
    }


def replay_frozen_coefficients(
    result: dict[str, Any], *, eta_probe: tuple[int, int, float] | None = None,
    xi_probe: tuple[int, int, float] | None = None,
) -> dict[str, Array]:
    """Replay formal primitive perturbations, freezing c,C,D,R and covariances."""
    fields = result["fields"]
    if fields is None:
        raise ValueError("Replay requires return_fields=True")
    cfg = result["config"]
    n, steps = cfg["population_size"], cfg["steps"]
    m, p = len(cfg["labels"]), len(cfg["input_vectors"])
    s, step = steps+1, cfg["dt"]*(2./m)
    fixed_c = result["c"]
    C1, D2 = result["C"]["layer1"], result["D"]["layer2"]
    Rh, Rd = result["R"]["h"], result["R"]["delta"]
    z1, w = fields["z1"][0].copy(), np.zeros(n)
    h1_hist = np.empty((s, n, p))
    h2_hist, d2_hist = np.empty_like(h1_hist), np.empty_like(h1_hist)
    f = np.empty((s, p))
    passive = np.arange(m, p)
    for probe in (eta_probe, xi_probe):
        if probe is not None and not (0 <= probe[0] < s and 0 <= probe[1] < p):
            raise ValueError("Probe index is outside the program")
    for k in range(s):
        h1, gate1, _ = _activation(z1)
        h1_hist[k] = h1
        z2 = fields["eta"][k].copy()
        if eta_probe is not None and eta_probe[0] == k:
            z2[:, eta_probe[1]] += eta_probe[2]
        if k:
            up = np.zeros((k, p, m))
            if cfg["reciprocal_correction"]:
                up += Rh[k, :k, :, :m]
            if cfg["learned_forward_memory"]:
                up += step*C1[k, :k, :, :m]*fixed_c[:k, None, :]
            z2 += _history_sum(up, d2_hist[:k, :, :m])
        h2, gate2, _ = _activation(z2)
        h2_hist[k] = h2
        d2_hist[k] = gate2*w[:, None]
        f[k] = np.mean(w[:, None]*h2, axis=0)
        xi = fields["xi"][k].copy()
        if xi_probe is not None and xi_probe[0] == k:
            xi[:, xi_probe[1]] += xi_probe[2]
        down = np.zeros((k+1, p, m))
        if cfg["reciprocal_correction"]:
            down += Rd[k, :k+1, :, :m]
        if cfg["learned_backward_memory"] and k:
            down[:k] += step*D2[k, :k, :, :m]*fixed_c[:k, None, :]
        b1 = xi+_history_sum(down, h1_hist[:k+1, :, :m])
        if cfg["reciprocal_correction"] and len(passive):
            b1[:, m:] += Rd[k, k, passive, passive][None, :]*h1[:, m:]
        if k < steps:
            force = cfg["input_gram"][:, :m]*fixed_c[k][None, :]
            z1 += step*((gate1[:, :m]*b1[:, :m]) @ force.T)
            w += step*(h2[:, :m] @ fixed_c[k])
    return {"h1": h1_hist, "h2": h2_hist, "delta2": d2_hist, "f": f}


def run_self_tests() -> dict[str, Any]:
    """Tiny deterministic tests only; never launches a research cohort."""
    from causal_population_simulator import simulate_population as original

    checks: dict[str, float] = {}
    old = original((.15, -.1), dt=.2, steps=4, population_size=31,
                   seed=9, return_fields=True)
    new = simulate_population((.15, -.1), dt=.2, steps=4, population_size=31,
                              seed=9, return_fields=True)
    comparisons = [(new["f"], old["f"]), (new["c"], old["c"])]
    for name in ("C", "D", "R", "fields"):
        comparisons.extend((new[name][key], old[name][key]) for key in old[name])
    checks["original_two_sample_max_error"] = max(float(np.max(abs(a-b))) for a, b in comparisons)
    assert checks["original_two_sample_max_error"] < 2e-10

    vectors = np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.],
                        [1., 1., 1.], [2., 1., -1.], [-1., 2., 1.], [1., -1., 2.]])
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    y = np.array([.15, -.1, .08, -.04])
    maximum_probe = maximum_replay = maximum_history = 0.
    for variant in ("full", "no_reciprocal", "no_middle"):
        result = simulate_population(y, dt=.2, steps=4, population_size=31,
            seed=17, input_vectors=vectors, return_fields=True,
            reciprocal_correction=variant != "no_reciprocal",
            learned_middle_memory=variant != "no_middle")
        fields = result["fields"]
        replay = replay_frozen_coefficients(result)
        for name in ("h1", "h2", "delta2", "f"):
            expected = result["f"] if name == "f" else fields[name]
            maximum_replay = max(maximum_replay, float(np.max(abs(replay[name]-expected))))
        for k in range(5):
            predicted = .1*np.einsum("jab,jb->a", result["C"]["layer2"][k, :k, :, :4], result["c"][:k])
            maximum_history = max(maximum_history, float(np.max(abs(predicted-result["f"][k]))))
            _, _, curvature = _activation(fields["z2"][k])
            expected = np.diag(np.mean(fields["w"][k, :, None]*curvature, axis=0))
            np.testing.assert_allclose(result["R"]["delta"][k, k], expected, atol=2e-12)
        epsilon = 1e-5
        for family, observable, response in (("xi", "h1", "h"), ("eta", "delta2", "delta")):
            for j, b in ((0, 0), (1, 3), (2, 4), (1, 6)):
                plus = replay_frozen_coefficients(result, **{family+"_probe": (j, b, epsilon)})
                minus = replay_frozen_coefficients(result, **{family+"_probe": (j, b, -epsilon)})
                measured = ((plus[observable]-minus[observable])/(2*epsilon)).mean(axis=1)
                expected = result["R"][response][:, j, :, b]
                maximum_probe = max(maximum_probe, float(np.max(abs(measured-expected))))
                np.testing.assert_allclose(measured, expected, atol=3e-9, rtol=3e-7)
                if b >= 4:
                    np.testing.assert_array_equal(plus["h2"][:, :, :4], replay["h2"][:, :, :4])
                    np.testing.assert_array_equal(plus["f"][:, :4], replay["f"][:, :4])
        assert not np.any(result["R"]["h"][:, :, :, 4:])
    checks.update(general_panel_probe_max_error=maximum_probe,
                  general_panel_replay_max_error=maximum_replay,
                  general_panel_readout_history_max_error=maximum_history)
    assert maximum_replay < 2e-12 and maximum_history < 2e-12
    zero = simulate_population(np.zeros(4), dt=.2, steps=2, population_size=23,
                               input_vectors=vectors, return_fields=True)
    np.testing.assert_array_equal(zero["f"], np.zeros((3, 7)))
    assert zero["diagnostics"]["xi"]["retained_rank"] == 0
    for m, p, d in ((1, 1, 1), (4, 4, 3)):
        inputs = np.ones((p, d)) if d == 1 else vectors[:p]
        result = simulate_population(np.zeros(m), dt=.2, steps=0,
                                     population_size=7, input_vectors=inputs)
        assert result["f"].shape == (1, p)
    try:
        simulate_population(y, steps=4, population_size=31,
                            input_vectors=vectors, memory_limit_mb=.001)
    except MemoryError:
        pass
    else:
        raise AssertionError("Memory guard failed")
    return {"passed": True, **checks}


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if not args.self_test:
        parser.error("Use --self-test; research cohorts require an explicit external driver")
    print(json.dumps(run_self_tests(), indent=2))
