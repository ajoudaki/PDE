"""Two-layer tanh causal feature-response Euler law with particle quadrature.

This implements CANDIDATE_SYSTEM.md, not a learned dense neural matrix.
Independent populations use independent Gaussian seeds. Local tangents
differentiate formal primitives, never whitening seeds or global coefficients.
Run this module with --self-test for small deterministic consistency tests.
"""
from __future__ import annotations

import argparse
import json
import time
from typing import Any
import numpy as np

Array = np.ndarray
DEFAULT_INPUTS = np.array(
    [[1., 0.], [0., 1.], [2. / np.sqrt(5.), 1. / np.sqrt(5.)]], dtype=np.float64
)


def _activation(z: Array) -> tuple[Array, Array, Array]:
    h = np.tanh(z)
    gate = 1. - h * h
    return h, gate, -2. * h * gate


class _ColoredGaussianFamily:
    """PSD empirical Gram factor, with two-pass source Gram-Schmidt.

    Target Gaussian seed columns are never empirically orthogonalized.
    Small discarded innovations are an explicit numerical approximation.
    """
    def __init__(self, n: int, qmax: int, rng: np.random.Generator,
                 rank_rtol: float, rank_atol: float) -> None:
        self.n = n
        self.max_rank = min(n, qmax)
        self.basis = np.empty((n, self.max_rank), dtype=np.float64)
        self.seeds = np.empty((n, self.max_rank), dtype=np.float64)
        self.coefficients = np.zeros((qmax, self.max_rank), dtype=np.float64)
        self.rng, self.rank_rtol, self.rank_atol = rng, rank_rtol, rank_atol
        self.rank = self.count = 0
        self.records: list[dict[str, Any]] = []

    def append(self, queries: Array) -> Array:
        answers = np.empty((self.n, queries.shape[1]), dtype=np.float64)
        for column in range(queries.shape[1]):
            query = queries[:, column]
            raw_variance = float(query @ query / self.n)
            old_rank = self.rank
            if old_rank:
                basis = self.basis[:, :old_rank]
                coefficient = basis.T @ query / self.n
                residual = query - basis @ coefficient
                correction = basis.T @ residual / self.n
                coefficient += correction
                residual -= basis @ correction
            else:
                coefficient = np.empty(0, dtype=np.float64)
                residual = query.copy()
            innovation_variance = float(residual @ residual / self.n)
            retain = (innovation_variance > self.rank_atol + self.rank_rtol * raw_variance
                      and old_rank < self.max_rank)
            row = self.coefficients[self.count]
            row[:old_rank] = coefficient
            if retain:
                scale = np.sqrt(innovation_variance)
                self.basis[:, old_rank] = residual / scale
                self.seeds[:, old_rank] = self.rng.standard_normal(self.n)
                row[old_rank] = scale
                self.rank += 1
            answers[:, column] = self.seeds[:, :self.rank] @ row[:self.rank]
            self.records.append({
                "query_index": self.count, "raw_variance": raw_variance,
                "innovation_variance": innovation_variance, "retained": bool(retain),
                "retained_rank": self.rank,
                "discarded_variance": 0. if retain else innovation_variance,
                "diagonal_covariance_error":
                    abs(raw_variance - float(row[:self.rank] @ row[:self.rank])),
            })
            self.count += 1
        return answers

    def diagnostics(self, query_gram: Array) -> dict[str, Any]:
        coefficients = self.coefficients[:self.count, :self.rank]
        positive = [v["innovation_variance"] for v in self.records if v["retained"]]
        return {
            "query_count": self.count, "retained_rank": self.rank,
            "minimum_retained_innovation_variance": min(positive) if positive else 0.,
            "maximum_discarded_variance":
                max((v["discarded_variance"] for v in self.records), default=0.),
            "maximum_covariance_error":
                float(np.max(np.abs(coefficients @ coefficients.T - query_gram))),
            "rank_rtol": self.rank_rtol, "rank_atol": self.rank_atol,
            "queries": self.records,
        }


class _TangentHistory:
    """Packed active-coordinate triangular history, in float64."""
    def __init__(self, n: int, steps: int) -> None:
        m = 2
        self.buffer = np.empty(n * m * m * (steps + 1)**2, dtype=np.float64)
        self.lower: list[Array] = []
        self.upper: list[Array] = []
        offset = 0
        for k in range(steps + 1):
            for destination, dimension in ((self.lower, m*k), (self.upper, m*(k+1))):
                length = n * m * dimension
                destination.append(self.buffer[offset:offset+length].reshape(n, m, dimension))
                offset += length
        assert offset == self.buffer.size


def estimate_memory_bytes(population_size: int, steps: int, *,
                          return_fields: bool = False) -> dict[str, int]:
    """Conservative array estimate; BLAS/interpreter overhead is not included."""
    n, m, p, s = population_size, 2, 3, steps + 1
    q = p*s
    rank = min(n, q)
    parts = {
        "tangent_history": 8*n*m*m*s*s,
        "primal_history": 8*4*s*n*p,
        "optional_fields": 8*s*n*(5*p+1) if return_fields else 0,
        "gaussian_factors": 8*(4*n*rank + 2*q*rank),
        "moment_histories": 8*6*s*s*p*p,
        "working_allowance": 8*12*n*p*m*s,
    }
    parts["estimated_total"] = sum(parts.values())
    return parts


def _record_gram(destination: Array, history: Array, k: int) -> None:
    block = np.einsum("na,jnb->jab", history[k], history[:k+1], optimize=False)
    block /= history.shape[1]
    destination[k, :k+1] = block
    destination[:k+1, k] = block.transpose(0, 2, 1)


def _history_sum(coefficients: Array, history: Array) -> Array:
    return np.einsum("jab,jnb->na", coefficients, history, optimize=False)


def _add_tangent_history(destination: Array, coefficients: Array,
                         history: list[Array]) -> None:
    for j, coefficient in enumerate(coefficients):
        prior = history[j]
        q = prior.shape[2]
        if q and np.any(coefficient):
            destination[:, :, :q] += np.einsum("ab,nbq->naq", coefficient, prior,
                                               optimize=False)


def _flat_gram(history: Array) -> Array:
    s, _, p, _ = history.shape
    return history.transpose(0, 2, 1, 3).reshape(s*p, s*p)


def simulate_population(
    labels: Array | tuple[float, float] = (0.15, -0.15), *,
    dt: float = 0.4, steps: int = 60, population_size: int = 1024, seed: int = 0,
    input_vectors: Array | None = None,
    learned_forward_memory: bool = True, learned_backward_memory: bool = True,
    reciprocal_correction: bool = True, learned_middle_memory: bool | None = None,
    rank_rtol: float = 1e-12, rank_atol: float = 0.,
    memory_limit_mb: float = 3072., return_fields: bool = False,
) -> dict[str, Any]:
    """Compute K Euler steps, including states at zero and K*dt.

    f has shape [K+1,3]; c has shape [K+1,2].
    C[layer], D[layer], R[h or delta] have shape [K+1,K+1,3,3].
    C[k,j,a,b] is the empirical expectation of h_a^k*h_b^j.
    R_h[k,j,a,b] is E[partial_xi_b^j h1_a^k]; R_delta is
    E[partial_eta_b^j delta2_a^k]. Future responses are zero.

    learned_middle_memory=False disables BOTH learned memory directions.
    reciprocal_correction=False removes BOTH reciprocal corrections and
    recomputes the modified circuit's tangents. One-direction memory switches
    are exposed but need not correspond to a gradient-trained dense model.

    Population size is a quadrature parameter, not dense-network width.
    Expectations, finite Euler steps and discarded numerical innovations are
    separate approximations; no convergence rate is asserted by this code.
    """
    started = time.perf_counter()
    y = np.asarray(labels, dtype=np.float64)
    if y.shape != (2,) or not np.all(np.isfinite(y)):
        raise ValueError("Require two finite training labels, with no passive label")
    if not isinstance(steps, (int, np.integer)) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    if not isinstance(population_size, (int, np.integer)) or population_size < 1:
        raise ValueError("population_size must be a positive integer")
    if not np.isfinite(dt) or dt <= 0:
        raise ValueError("dt must be positive and finite")
    if rank_rtol < 0 or rank_atol < 0:
        raise ValueError("Rank tolerances must be nonnegative")
    if not np.isfinite(memory_limit_mb) or memory_limit_mb <= 0:
        raise ValueError("memory_limit_mb must be positive and finite")
    vectors = np.asarray(DEFAULT_INPUTS if input_vectors is None else input_vectors,
                         dtype=np.float64)
    if vectors.shape != (3, 2) or not np.all(np.isfinite(vectors)):
        raise ValueError("input_vectors must be a finite [3,2] array")
    if not np.allclose(np.sum(vectors*vectors, axis=1), 1., atol=1e-12, rtol=1e-12):
        raise ValueError("Every input must be normalized")
    if learned_middle_memory is not None:
        learned_forward_memory = learned_backward_memory = bool(learned_middle_memory)
    memory = estimate_memory_bytes(population_size, steps, return_fields=return_fields)
    if memory["estimated_total"] > memory_limit_mb*1024**2:
        raise MemoryError(
            f"Estimated array memory {memory['estimated_total']/1024**2:.1f} MiB "
            f"exceeds {memory_limit_mb:.1f} MiB; reduce program/population size")

    n, m, p, s = population_size, 2, 3, steps+1
    learning_step = dt*(2./m)
    input_gram = vectors @ vectors.T
    streams = np.random.SeedSequence(seed).spawn(3)
    root_rng, eta_rng, xi_rng = (np.random.default_rng(v) for v in streams)
    z1 = root_rng.standard_normal((n, 2)) @ vectors.T
    w = np.zeros(n, dtype=np.float64)
    z1_tangent = np.zeros((n, p, m*s), dtype=np.float64)
    w_tangent = np.zeros((n, m*s), dtype=np.float64)
    tangents = _TangentHistory(n, steps)
    eta_family = _ColoredGaussianFamily(n, p*s, eta_rng, rank_rtol, rank_atol)
    xi_family = _ColoredGaussianFamily(n, p*s, xi_rng, rank_rtol, rank_atol)
    h1_history = np.empty((s, n, p), dtype=np.float64)
    h2_history = np.empty_like(h1_history)
    d1_history = np.empty_like(h1_history)
    d2_history = np.empty_like(h1_history)
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
        for a in range(m):
            z2_tangent[:, a, previous_dimension+a] = 1.
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
        # Passive eta has only its current direct gate-curvature derivative.
        Rd[k, k, m, m] = np.mean(w*curvature2[:, m])
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
        if reciprocal_correction:
            b1[:, m] += Rd[k, k, m, m]*h1[:, m]
        d1 = gate1*b1
        d1_history[k] = d1
        _record_gram(D1, d1_history, k)

        tick = time.perf_counter()
        b1_tangent = np.zeros((n, m, current_dimension))
        for a in range(m):
            b1_tangent[:, a, previous_dimension+a] = 1.
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
            z1_tangent[:, :, :current_dimension] += learning_step*np.einsum(
                "ab,nbq->naq", force, delta1_tangent, optimize=False)
            w += learning_step*(h2[:, :m] @ residual[k])
            w_tangent[:, :current_dimension] += learning_step*np.einsum(
                "b,nbq->nq", residual[k], gate2[:, :m, None]*z2_tangent[:, :m, :],
                optimize=False)

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
            "layer1_training_diagonal_defect":
                C1[current, current, 0, 0]-C1[current, current, 1, 1],
            "layer2_training_diagonal_defect":
                C2[current, current, 0, 0]-C2[current, current, 1, 1],
            "interpretation": "Finite-quadrature defects; not forced to zero.",
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
            "input_gram": input_gram,
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
    """Formal local probe replay, freezing c,C,D,R and primitive covariance.

    A probe (time_index,sample_index,amount) adds amount to that primitive
    in every quadrature row. Requires return_fields=True. This utility is not
    a new self-consistent trajectory.
    """
    fields = result["fields"]
    if fields is None:
        raise ValueError("Replay requires return_fields=True")
    cfg = result["config"]
    n, steps, m, p = cfg["population_size"], cfg["steps"], 2, 3
    s, step = steps+1, cfg["dt"]*(2./m)
    fixed_c = result["c"]
    C1, D2 = result["C"]["layer1"], result["D"]["layer2"]
    Rh, Rd = result["R"]["h"], result["R"]["delta"]
    z1, w = fields["z1"][0].copy(), np.zeros(n)
    h1_hist = np.empty((s, n, p))
    h2_hist, d2_hist = np.empty_like(h1_hist), np.empty_like(h1_hist)
    f = np.empty((s, p))
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
        if cfg["reciprocal_correction"]:
            b1[:, m] += Rd[k, k, m, m]*h1[:, m]
        if k < steps:
            force = cfg["input_gram"][:, :m]*fixed_c[k][None, :]
            z1 += step*((gate1[:, :m]*b1[:, :m]) @ force.T)
            w += step*(h2[:, :m] @ fixed_c[k])
    return {"h1": h1_hist, "h2": h2_hist, "delta2": d2_hist, "f": f}


def run_self_tests() -> dict[str, Any]:
    started, checks = time.perf_counter(), []
    sampler = _ColoredGaussianFamily(32, 4, np.random.default_rng(3), 1e-12, 0.)
    query = np.random.default_rng(4).standard_normal((32, 2))
    first = sampler.append(query)
    dependent = sampler.append(np.column_stack((2*query[:, 0]-query[:, 1], np.zeros(32))))
    np.testing.assert_allclose(dependent[:, 0], 2*first[:, 0]-first[:, 1], atol=1e-12)
    np.testing.assert_array_equal(dependent[:, 1], np.zeros(32))
    assert sampler.rank == 2
    checks.append("PSD sampler: dependent and zero queries")
    zero = simulate_population((0., 0.), steps=3, population_size=48, return_fields=True)
    np.testing.assert_array_equal(zero["f"], np.zeros((4, 3)))
    np.testing.assert_array_equal(zero["D"]["layer2"], np.zeros((4, 4, 3, 3)))
    assert zero["diagnostics"]["xi"]["retained_rank"] == 0
    np.testing.assert_allclose(zero["fields"]["h2"],
        np.broadcast_to(zero["fields"]["h2"][0], (4, 48, 3)), atol=2e-12)
    checks.append("zero-label stationary singular program")
    for variant in ("full", "no_reciprocal", "no_middle"):
        result = simulate_population(
            (0.15, -0.1), dt=0.2, steps=4, population_size=64, seed=9,
            reciprocal_correction=variant != "no_reciprocal",
            learned_middle_memory=variant != "no_middle", return_fields=True)
        fields = result["fields"]
        replay = replay_frozen_coefficients(result)
        np.testing.assert_allclose(replay["h1"], fields["h1"], atol=2e-12, rtol=2e-12)
        np.testing.assert_allclose(replay["delta2"], fields["delta2"], atol=2e-12, rtol=2e-12)
        for k in range(5):
            prediction = 0.2*np.einsum(
                "jab,jb->a", result["C"]["layer2"][k, :k, :, :2], result["c"][:k])
            np.testing.assert_allclose(result["f"][k], prediction, atol=2e-12, rtol=2e-12)
            _, _, curvature = _activation(fields["z2"][k])
            expected = np.diag(np.mean(fields["w"][k, :, None]*curvature, axis=0))
            np.testing.assert_allclose(result["R"]["delta"][k, k], expected, atol=2e-12)
        epsilon = 1e-5
        for family, observable, name in (("xi", "h1", "h"), ("eta", "delta2", "delta")):
            plus = replay_frozen_coefficients(result, **{family+"_probe": (0, 0, epsilon)})
            minus = replay_frozen_coefficients(result, **{family+"_probe": (0, 0, -epsilon)})
            observed = ((plus[observable]-minus[observable])/(2*epsilon)).mean(axis=1)
            np.testing.assert_allclose(observed, result["R"][name][:, 0, :, 0],
                                       atol=3e-9, rtol=3e-7)
        passive = replay_frozen_coefficients(result, eta_probe=(0, 2, epsilon))
        np.testing.assert_allclose(passive["h2"][:, :, :2], fields["h2"][:, :, :2], atol=2e-12)
        checks.append(variant+": replay, output history, curvature, frozen-coefficient probes")
    try:
        simulate_population(steps=20, population_size=100, memory_limit_mb=0.001)
    except MemoryError:
        checks.append("pre-allocation memory guard")
    else:
        raise AssertionError("Memory guard failed")
    return {"passed": checks, "seconds": time.perf_counter()-started}


def _json_default(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--steps", type=int, default=30)
    parser.add_argument("--dt", type=float, default=0.4)
    parser.add_argument("--population-size", type=int, default=1024)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--labels", type=float, nargs=2, default=(0.15, -0.15))
    parser.add_argument("--no-reciprocal", action="store_true")
    parser.add_argument("--no-learned-middle", action="store_true")
    parser.add_argument("--memory-limit-mb", type=float, default=3072.)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(run_self_tests(), default=_json_default, indent=2))
        return
    result = simulate_population(
        args.labels, dt=args.dt, steps=args.steps, population_size=args.population_size,
        seed=args.seed, reciprocal_correction=not args.no_reciprocal,
        learned_middle_memory=not args.no_learned_middle, memory_limit_mb=args.memory_limit_mb)
    if args.output:
        np.savez_compressed(
            args.output, time=result["time"], f=result["f"], c=result["c"],
            C1=result["C"]["layer1"], C2=result["C"]["layer2"],
            D1=result["D"]["layer1"], D2=result["D"]["layer2"],
            Rh=result["R"]["h"], Rdelta=result["R"]["delta"],
            kernel_diagnostic=result["kernel_diagnostic"],
            config_json=json.dumps(result["config"], default=_json_default),
            diagnostics_json=json.dumps(result["diagnostics"], default=_json_default))
    print(json.dumps({
        "final_prediction": result["f"][-1], "final_training_residual": result["c"][-1],
        "frozen_feature_limit": result["diagnostics"]["frozen_feature_limit"],
        "elapsed_seconds": result["diagnostics"]["timing"]["total_seconds"],
        "estimated_memory_mib": result["diagnostics"]["memory_bytes"]["estimated_total"]/1024**2,
        "eta_rank": result["diagnostics"]["eta"]["retained_rank"],
        "xi_rank": result["diagnostics"]["xi"]["retained_rank"],
        "eta_covariance_error": result["diagnostics"]["eta"]["maximum_covariance_error"],
        "xi_covariance_error": result["diagnostics"]["xi"]["maximum_covariance_error"],
    }, default=_json_default, indent=2))


if __name__ == "__main__":
    main()
