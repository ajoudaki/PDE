"""Exploratory empirical random-direction source recurrence, not a limit solver.

All history is retained. There is no trainable representative-by-representative
connector. See directional_solver_spec.md for the frozen-coefficient convention.
"""
from __future__ import annotations

import argparse
import copy
from dataclasses import asdict, dataclass
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.linalg import solve_triangular
from scipy.special import roots_hermitenorm


class NumericalFailure(RuntimeError):
    """A numerical validity gate failed; no completed step is committed."""


def _integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return int(value)


def _finite(array, name):
    if not np.all(np.isfinite(array)):
        raise NumericalFailure(f"nonfinite {name}")


def _directions(value):
    array = np.asarray(value, dtype=np.float64)
    if array.ndim != 2 or array.shape[1] != 2 or len(array) == 0:
        raise ValueError("directions must have shape (m, 2), m >= 1")
    if not np.all(np.isfinite(array)) or not np.allclose(
        np.sum(array * array, axis=1), 1, rtol=0, atol=1e-10
    ):
        raise ValueError("directions must be finite unit circle vectors")
    return array


@dataclass(frozen=True)
class SolverConfig:
    representatives: int
    h: float
    noise: float
    seed: int
    directions: list
    weights: list
    labels: list
    precision: str = "float64"

    def __post_init__(self):
        _integer(self.representatives, "representatives")
        _integer(self.seed, "seed", 0)
        if self.precision not in ("float32", "float64"):
            raise ValueError("precision must be float32 or float64")
        for name in ("h", "noise"):
            value = getattr(self, name)
            if isinstance(value, bool) or not np.isfinite(value) or value <= 0:
                raise ValueError(f"{name} must be finite and positive")
        if not np.isfinite(self.h * self.noise):
            raise ValueError("h * noise is not representable")
        dtype = np.dtype(self.precision)
        if dtype.type(self.noise * self.noise) <= 0 or not np.isfinite(dtype.type(self.noise * self.noise)):
            raise ValueError("noise variance is not representable in selected precision")
        directions = _directions(self.directions)
        weights, labels = np.asarray(self.weights, float), np.asarray(self.labels, float)
        if weights.shape != (len(directions),) or labels.shape != weights.shape:
            raise ValueError("weights and labels must match the direction count")
        if not np.all(np.isfinite(weights)) or np.any(weights < 0) or not np.isclose(weights.sum(), 1, rtol=0, atol=1e-12):
            raise ValueError("weights must be finite, nonnegative and sum to one")
        if not np.all(np.isfinite(labels)):
            raise ValueError("labels must be finite")
        # Own the configuration inputs; JSON-compatible numerical values.
        active = weights > 0
        object.__setattr__(self, "directions", directions[active].tolist())
        object.__setattr__(self, "weights", weights[active].tolist())
        object.__setattr__(self, "labels", labels[active].tolist())
        omega = dtype.type(self.h) * weights[active].astype(dtype)
        if np.any(omega <= 0) or not np.all(np.isfinite(1 / np.sqrt(omega))):
            raise ValueError("weighted source-probe scales are not representable")


def covariance_extension(old_fields, new_fields, factor, innovations, new_innovations, noise):
    """Extend an uncentered empirical Gram, preserving the old factor literally.

    Returns (extended factor, new Gaussian sources, validity diagnostics).
    All operands use a single selected floating precision. No jitter is added.
    """
    p, j = old_fields.shape
    m = new_fields.shape[1]
    cross = old_fields.T @ new_fields / p
    clean = new_fields.T @ new_fields / p
    covariance = clean + np.eye(m, dtype=new_fields.dtype) * noise**2
    solved = solve_triangular(factor, cross, lower=True, check_finite=False) if j else cross.copy()
    schur = covariance - solved.T @ solved
    schur = (schur + schur.T) * 0.5
    _finite(schur, "source Schur complement")
    minimum = float(np.linalg.eigvalsh(schur)[0])
    scale = max(float(np.linalg.norm(covariance, ord=2)), noise**2)
    tolerance = 64 * np.finfo(new_fields.dtype).eps * max(1, j + m) * scale
    if minimum < noise**2 - tolerance or minimum <= 0:
        raise NumericalFailure(
            f"covariance floor failed: min={minimum:.17g}, floor={noise**2:.17g}, roundoff allowance={tolerance:.17g}"
        )
    try:
        block = np.linalg.cholesky(schur)
    except np.linalg.LinAlgError as exc:
        raise NumericalFailure("source Schur Cholesky failed") from exc
    extended = np.zeros((j + m, j + m), dtype=new_fields.dtype)
    extended[:j, :j] = factor
    extended[j:, :j] = solved.T
    extended[j:, j:] = block
    sources = innovations @ solved + new_innovations @ block.T
    _finite(sources, "Gaussian source extension")
    return extended, sources, {"minimum_schur": minimum, "floor_roundoff_allowance": tolerance}


class DirectionalSolver:
    """Two separate statistical populations; mutable only through step()."""

    schema_version = 1
    history_names = ("H", "Hdot", "D", "Ddot", "Rminus", "Rplus", "Eminus", "Eplus", "Bminus", "Bplus")
    array_names = history_names + (
        "g", "w", "c", "v_w", "v_c", "Lminus", "Lplus", "gamma", "omega", "call_times", "call_directions",
        "training_predictions", "training_residuals", "step_response_max", "step_minimum_schur",
        "step_floor_allowance",
    )
    stream_names = ("root", "plus_gaussian", "minus_gaussian", "plus_probe", "minus_probe")

    def __init__(self, config):
        self.config = SolverConfig(**asdict(config)) if isinstance(config, SolverConfig) else SolverConfig(**config)
        self.dtype = np.dtype(self.config.precision)
        self.p = self.config.representatives
        self.u = np.asarray(self.config.directions, dtype=self.dtype)
        self.weights = np.asarray(self.config.weights, dtype=self.dtype)
        self.labels = np.asarray(self.config.labels, dtype=self.dtype)
        self.m = len(self.u)
        self.steps = 0
        self.rngs = dict(zip(self.stream_names, [np.random.default_rng(s) for s in np.random.SeedSequence(self.config.seed).spawn(5)]))
        self.g = self.rngs["root"].standard_normal((self.p, 2)).astype(self.dtype)
        self.w, self.v_w = self.g.copy(), np.zeros_like(self.g)
        self.c, self.v_c = np.zeros(self.p, dtype=self.dtype), np.zeros(self.p, dtype=self.dtype)
        for name in self.history_names:
            setattr(self, name, np.empty((self.p, 0), dtype=self.dtype))
        self.Lminus, self.Lplus = np.empty((0, 0), dtype=self.dtype), np.empty((0, 0), dtype=self.dtype)
        self.gamma = np.empty(0, dtype=self.dtype)
        self.omega = np.empty(0, dtype=self.dtype)
        # Physical times are bookkeeping, stored in float64 even for float32 state.
        self.call_times, self.call_directions = np.empty(0), np.empty((0, 2), dtype=self.dtype)
        self.training_predictions, self.training_residuals = np.empty((0, self.m), dtype=self.dtype), np.empty((0, self.m), dtype=self.dtype)
        self.step_response_max, self.step_minimum_schur = np.empty(0), np.empty((0, 2))
        self.step_floor_allowance = np.empty((0, 2))

    @property
    def time(self):
        return self.steps * self.config.h

    @property
    def calls(self):
        return self.H.shape[1]

    def rng_state(self):
        return {name: copy.deepcopy(rng.bit_generator.state) for name, rng in self.rngs.items()}

    def _normal(self, name):
        return self.rngs[name].standard_normal((self.p, self.m)).astype(self.dtype)

    def _probe(self, name):
        signs = (2 * self.rngs[name].integers(0, 2, (self.p, self.m), dtype=np.int8) - 1).astype(self.dtype)
        return signs / np.sqrt(self.config.h * self.weights)

    def step(self):
        """One physical Euler step; all right sides use the preceding state.

        Failed updates restore the random streams and leave completed state intact.
        Tangents differentiate coordinates with every empirical coefficient frozen.
        """
        before_rng = self.rng_state()
        try:
            with np.errstate(over="raise", invalid="raise", divide="raise"):
                updated = self._prepare_step()
        except (FloatingPointError, NumericalFailure, np.linalg.LinAlgError) as exc:
            for name, state in before_rng.items():
                self.rngs[name].bit_generator.state = state
            raise NumericalFailure(f"step {self.steps}, t={self.time}: {exc}") from exc
        for name, value in updated.items():
            setattr(self, name, value)
        self.steps += 1
        return self.training_predictions[-1].copy()

    def _prepare_step(self):
        j, p = self.calls, self.p
        x, xdot = self.w @ self.u.T, self.v_w @ self.u.T
        h = np.tanh(x)
        dh, ddh = 1 - h * h, -2 * h * (1 - h * h)
        hdot = dh * xdot
        hh = self.H.T @ h / p
        alpha = (self.omega[:, None] * self.Rminus.T) @ hdot / p
        fcoef = alpha + self.gamma[:, None] * hh
        eplus = self._normal("plus_gaussian")
        lplus, bplus, check_plus = covariance_extension(self.H, h, self.Lplus, self.Eplus, eplus, self.config.noise)
        rplus = self._probe("plus_probe")
        z, zdot = bplus + self.D @ fcoef, rplus + self.Ddot @ fcoef
        v = np.tanh(z)
        dv, ddv = 1 - v * v, -2 * v * (1 - v * v)
        d = self.c[:, None] * dv
        ddot = self.v_c[:, None] * dv + self.c[:, None] * ddv * zdot
        prediction = np.mean(self.c[:, None] * v, axis=0)
        residual = prediction - self.labels
        gamma = -2 * self.config.h * self.weights * residual
        # Remove the analytically known current-coordinate tangent pointwise.
        ddot_for_old = self.v_c[:, None] * dv + self.c[:, None] * ddv * (self.Ddot @ fcoef)
        beta = (self.omega[:, None] * self.Rplus.T) @ ddot_for_old / p
        dd = self.D.T @ d / p
        # Current formal source coordinates stay distinct under singular clean Grams.
        bcoef = np.vstack((beta + self.gamma[:, None] * dd, np.diag(np.mean(self.c[:, None] * ddv, axis=0))))
        eminus = self._normal("minus_gaussian")
        lminus, bminus, check_minus = covariance_extension(self.D, d, self.Lminus, self.Eminus, eminus, self.config.noise)
        rminus = self._probe("minus_probe")
        hall, hdotall = np.hstack((self.H, h)), np.hstack((self.Hdot, hdot))
        q, qdot = bminus + hall @ bcoef, rminus + hdotall @ bcoef
        updated = {
            "w": self.w + ((dh * q) * gamma) @ self.u,
            "v_w": self.v_w + ((ddh * xdot * q + dh * qdot) * gamma) @ self.u,
            "c": self.c + v @ gamma,
            "v_c": self.v_c + (dv * zdot) @ gamma,
            "Lplus": lplus, "Lminus": lminus,
            "gamma": np.concatenate((self.gamma, gamma)),
            "omega": np.concatenate((self.omega, self.config.h * self.weights)),
            "call_times": np.concatenate((self.call_times, np.full(self.m, self.time))),
            "call_directions": np.vstack((self.call_directions, self.u)),
            "training_predictions": np.vstack((self.training_predictions, prediction)),
            "training_residuals": np.vstack((self.training_residuals, residual)),
            "step_response_max": np.append(self.step_response_max, max(
                np.max(np.abs(alpha), initial=0), np.max(np.abs(beta), initial=0),
                np.max(np.abs(fcoef), initial=0), np.max(np.abs(bcoef), initial=0))),
            "step_minimum_schur": np.vstack((self.step_minimum_schur, [check_plus["minimum_schur"], check_minus["minimum_schur"]])),
            "step_floor_allowance": np.vstack((self.step_floor_allowance, [check_plus["floor_roundoff_allowance"], check_minus["floor_roundoff_allowance"]])),
        }
        for name, block in zip(self.history_names, (h, hdot, d, ddot, rminus, rplus, eminus, eplus, bminus, bplus)):
            updated[name] = np.hstack((getattr(self, name), block))
        for name, array in updated.items():
            _finite(array, name)
        assert updated["H"].shape == (p, j + self.m)
        return updated

    def _passive_fields(self, directions):
        u = _directions(directions).astype(self.dtype)
        h = np.tanh(self.w @ u.T)
        hdot = (1 - h * h) * (self.v_w @ u.T)
        cross = self.H.T @ h / self.p
        alpha = (self.omega[:, None] * self.Rminus.T) @ hdot / self.p
        shift = self.D @ (alpha + self.gamma[:, None] * cross)
        solved = solve_triangular(self.Lplus, cross, lower=True, check_finite=False) if self.calls else cross.copy()
        mean = self.Eplus @ solved
        # Query the clean action, conditional on noisy training source history.
        variance = np.mean(h * h, axis=0) - np.sum(solved * solved, axis=0)
        scale = max(float(np.max(np.mean(h * h, axis=0))), self.config.noise**2)
        tolerance = 64 * np.finfo(self.dtype).eps * max(1, self.calls) * scale
        _finite(variance, "passive conditional variance")
        if np.min(variance) < -tolerance:
            raise NumericalFailure("significantly negative passive conditional variance")
        # Only roundoff-negative marginal variances may be set to zero; report it.
        return h, shift, mean, np.maximum(variance, 0), int(np.count_nonzero(variance < 0))

    def predict(self, directions, order):
        """Read-only, deterministic one-dimensional normal Gauss-Hermite query."""
        order = _integer(order, "quadrature order")
        _, shift, mean, variance, _ = self._passive_fields(directions)
        nodes, weights = roots_hermitenorm(order)
        nodes = nodes.astype(self.dtype)
        weights = (weights / np.sqrt(2 * np.pi)).astype(self.dtype)
        expected = np.zeros_like(mean)
        center, scale = mean + shift, np.sqrt(variance)
        for node, weight in zip(nodes, weights):
            expected += weight * np.tanh(center + scale * node)
        prediction = np.mean(self.c[:, None] * expected, axis=0)
        _finite(prediction, "passive prediction")
        return prediction

    def paired_hidden_draws(self, directions, draws, seed):
        """Finite joint-query Monte Carlo samples, with explicit independent seed.

        Tuple order is all initial directions then all current directions.
        Returns paired preactivations, hidden activations, backward fields and
        empirical moments. D belongs to upper representatives, Q to lower ones;
        their matching row numbers do not pair neurons across populations.
        This integrates neither empirical-population nor query-sampling error.
        """
        draws, seed = _integer(draws, "draws"), _integer(seed, "query seed", 0)
        u = _directions(directions).astype(self.dtype)
        h, shift, _, _, _ = self._passive_fields(directions)
        h0 = np.tanh(self.g @ u.T)
        fields = np.hstack((h0, h))
        # Identical clean fields are the same Gaussian action, even at finite s.
        unique_fields, inverse = np.unique(fields, axis=1, return_inverse=True)
        cross = self.H.T @ unique_fields / self.p
        solved = solve_triangular(self.Lplus, cross, lower=True, check_finite=False) if self.calls else cross.copy()
        clean_gram = unique_fields.T @ unique_fields / self.p
        covariance = clean_gram - solved.T @ solved
        covariance = (covariance + covariance.T) * 0.5
        _finite(covariance, "joint conditional covariance")
        eigenvalues, eigenvectors = np.linalg.eigh(covariance)
        tolerance = 64 * np.finfo(self.dtype).eps * max(1, self.calls, len(eigenvalues)) * max(float(np.linalg.norm(clean_gram, ord=2)), self.config.noise**2)
        if eigenvalues[0] < -tolerance:
            raise NumericalFailure(f"joint conditional covariance is not positive semidefinite: {eigenvalues[0]}")
        factor = eigenvectors * np.sqrt(np.maximum(eigenvalues, 0))[None, :]
        center = self.Eplus @ solved
        _finite(center, "joint conditional mean")
        plus_seed, minus_seed = np.random.SeedSequence(seed).spawn(2)
        noise = np.random.default_rng(plus_seed).standard_normal((draws, self.p, len(eigenvalues))).astype(self.dtype)
        clean_sources = (center[None, :, :] + noise @ factor.T)[:, :, inverse]
        z = clean_sources + np.hstack((np.zeros_like(shift), shift))[None, :, :]
        _finite(z, "joint preactivation query")
        initial_z, current_z = z[:, :, :len(u)], z[:, :, len(u):]
        initial, current = np.tanh(initial_z), np.tanh(current_z)
        # Evaluate the clean reverse action for the same current upper draw.
        hdot = (1 - h * h) * (self.v_w @ u.T)
        hh = self.H.T @ h / self.p
        alpha = (self.omega[:, None] * self.Rminus.T) @ hdot / self.p
        fcoef = alpha + self.gamma[:, None] * hh
        zdot_old = self.Ddot @ fcoef
        backward_upper = self.c[None, :, None] * (1 - current * current)
        backward_lower = np.empty_like(backward_upper)
        minus_rng = np.random.default_rng(minus_seed)
        reverse_clips = 0
        reverse_minimum = float("inf")
        for draw_index in range(draws):
            d = backward_upper[draw_index]
            gate = 1 - current[draw_index] * current[draw_index]
            curvature = -2 * current[draw_index] * gate
            ddot_old = self.v_c[:, None] * gate + self.c[:, None] * curvature * zdot_old
            beta_old = (self.omega[:, None] * self.Rplus.T) @ ddot_old / self.p
            beta_diagonal = np.mean(self.c[:, None] * curvature, axis=0)
            dd = self.D.T @ d / self.p
            unique_d, d_inverse = np.unique(d, axis=1, return_inverse=True)
            dcross = self.D.T @ unique_d / self.p
            dsolved = solve_triangular(self.Lminus, dcross, lower=True, check_finite=False) if self.calls else dcross.copy()
            dclean_gram = unique_d.T @ unique_d / self.p
            dcovariance = dclean_gram - dsolved.T @ dsolved
            dcovariance = (dcovariance + dcovariance.T) * 0.5
            _finite(dcovariance, "passive reverse conditional covariance")
            deigenvalues, deigenvectors = np.linalg.eigh(dcovariance)
            dtolerance = 64 * np.finfo(self.dtype).eps * max(1, self.calls, len(deigenvalues)) * max(float(np.linalg.norm(dclean_gram, ord=2)), self.config.noise**2)
            if deigenvalues[0] < -dtolerance:
                raise NumericalFailure("significantly negative passive reverse conditional covariance")
            reverse_clips += int(np.count_nonzero(deigenvalues < 0))
            reverse_minimum = min(reverse_minimum, float(deigenvalues[0]))
            dfactor = deigenvectors * np.sqrt(np.maximum(deigenvalues, 0))[None, :]
            dnoise = minus_rng.standard_normal((self.p, len(deigenvalues))).astype(self.dtype)
            source = (self.Eminus @ dsolved + dnoise @ dfactor.T)[:, d_inverse]
            backward_lower[draw_index] = source + self.H @ (beta_old + self.gamma[:, None] * dd) + h * beta_diagonal
        _finite(backward_lower, "passive reverse query")
        return {
            "initial_preactivation": initial_z, "current_preactivation": current_z,
            "initial_hidden": initial, "current_hidden": current,
            "conditional_covariance": covariance[np.ix_(inverse, inverse)],
            "roundoff_eigenvalue_clips": int(np.count_nonzero(eigenvalues < 0)),
            "minimum_conditional_eigenvalue_before_clipping": float(eigenvalues[0]),
            "upper_D": backward_upper, "lower_Q": backward_lower,
            "lower_initial_H": h0, "lower_current_H": h,
            "reverse_roundoff_eigenvalue_clips": reverse_clips,
            "minimum_reverse_eigenvalue_before_clipping": reverse_minimum,
            "cross_hidden_moment": np.einsum("dpi,dpj->ij", initial, current) / (draws * self.p),
            "hidden_motion_squared": np.mean((current - initial)**2, axis=(0, 1)),
        }

    def diagnostics(self, order=None, full=True):
        """Read-only diagnostics, with optional O(P J² + J³) global products.

        Use full=False between checkpoints to retain the total recurrence cost.
        Loss timestamps are explicit; no random numbers are consumed.
        """
        reconstruction, k_squared = None, None
        if full:
            reconstruction, grams = {}, {}
            for sign, fields in (("plus", self.H), ("minus", self.D)):
                gram = fields.T @ fields / self.p
                grams[sign] = gram
                covariance = gram + np.eye(self.calls, dtype=self.dtype) * self.config.noise**2
                factor = getattr(self, "L" + sign)
                denominator = max(float(np.linalg.norm(covariance)), np.finfo(self.dtype).tiny)
                reconstruction[sign] = float(np.linalg.norm(factor @ factor.T - covariance) / denominator)
            k_squared = float(np.sum((self.gamma[:, None] * self.gamma[None, :]) * grams["plus"] * grams["minus"], dtype=np.float64))
        norms = {
            "w_motion_rms": float(np.sqrt(np.mean(np.sum((self.w - self.g)**2, axis=1), dtype=np.float64))),
            "c_rms": float(np.sqrt(np.mean(self.c * self.c, dtype=np.float64))),
            "rank_factor_hs_squared": k_squared,
            "w_tangent_rms": float(np.sqrt(np.mean(np.sum(self.v_w * self.v_w, axis=1), dtype=np.float64))),
            "c_tangent_rms": float(np.sqrt(np.mean(self.v_c * self.v_c, dtype=np.float64))),
        }
        if not all(v is None or np.isfinite(v) for v in norms.values()):
            raise NumericalFailure("nonfinite norm diagnostic")
        result = {
            "status": "exploratory_finite_process", "steps": self.steps, "calls": self.calls,
            "full_diagnostics": bool(full),
            "physical_time": self.time, "precision": self.config.precision,
            "representatives_per_population": self.p, "source_noise": self.config.noise,
            "state_array_bytes": sum(getattr(self, name).nbytes for name in self.array_names),
            "configuration_and_rng_json_bytes": len(json.dumps({"config": asdict(self.config), "rng_state": self.rng_state()}, sort_keys=True).encode("utf-8")),
            "derived_data_law_array_bytes": self.u.nbytes + self.weights.nbytes + self.labels.nbytes,
            "source_history_bytes": sum(getattr(self, name).nbytes for name in self.history_names),
            "covariance_factor_bytes": self.Lminus.nbytes + self.Lplus.nbytes,
            "covariance_reconstruction_relative_frobenius": reconstruction,
            "minimum_schur_eigenvalue": None if not self.steps else float(np.min(self.step_minimum_schur)),
            "maximum_floor_roundoff_allowance": None if not self.steps else float(np.max(self.step_floor_allowance)),
            "maximum_response_coefficient": float(np.max(self.step_response_max, initial=0)), **norms,
        }
        if self.steps:
            result.update({
                "last_training_call_physical_time": (self.steps - 1) * self.config.h,
                "last_training_call_predictions": self.training_predictions[-1].tolist(),
                "last_training_call_residuals": self.training_residuals[-1].tolist(),
                "last_training_call_loss": float(np.dot(self.weights, self.training_residuals[-1]**2)),
            })
        if order is not None:
            prediction = self.predict(self.config.directions, order)
            result.update({
                "passive_quadrature_order": order, "passive_predictions": prediction.tolist(),
                "passive_training_loss": float(np.dot(self.weights, (prediction - self.labels)**2)),
                "passive_roundoff_variance_clips": self._passive_fields(self.config.directions)[-1],
            })
        return result

    def save(self, path):
        """Write an exclusive checkpoint; overwriting prior evidence is rejected."""
        metadata = {"schema_version": self.schema_version, "config": asdict(self.config), "steps": self.steps, "rng_state": self.rng_state(), "numpy_version": np.__version__, "scipy_version": scipy.__version__}
        arrays = {name: getattr(self, name) for name in self.array_names}
        with Path(path).open("xb") as stream:
            np.savez(stream, metadata=np.asarray(json.dumps(metadata, sort_keys=True)), **arrays)

    @classmethod
    def load(cls, path):
        with np.load(path, allow_pickle=False) as archive:
            metadata = json.loads(str(archive["metadata"]))
            if metadata["schema_version"] != cls.schema_version:
                raise ValueError("unsupported checkpoint schema")
            if not isinstance(metadata.get("rng_state"), dict) or set(metadata["rng_state"]) != set(cls.stream_names):
                raise ValueError("checkpoint must contain every random stream exactly once")
            solver = cls(metadata["config"])
            solver.steps = _integer(metadata["steps"], "saved steps", 0)
            for name in cls.array_names:
                setattr(solver, name, archive[name].copy())
        for name, state in metadata["rng_state"].items():
            solver.rngs[name].bit_generator.state = state
        solver._validate_checkpoint()
        return solver

    def _validate_checkpoint(self):
        j = self.steps * self.m
        expected = {name: (self.p, j) for name in self.history_names}
        expected.update({"g": (self.p, 2), "w": (self.p, 2), "v_w": (self.p, 2), "c": (self.p,), "v_c": (self.p,), "Lplus": (j, j), "Lminus": (j, j), "gamma": (j,), "omega": (j,), "call_times": (j,), "call_directions": (j, 2), "training_predictions": (self.steps, self.m), "training_residuals": (self.steps, self.m), "step_response_max": (self.steps,), "step_minimum_schur": (self.steps, 2), "step_floor_allowance": (self.steps, 2)})
        float64_metadata = {"call_times", "step_response_max", "step_minimum_schur", "step_floor_allowance"}
        for name, shape in expected.items():
            array = getattr(self, name)
            dtype = np.dtype("float64") if name in float64_metadata else self.dtype
            if array.shape != shape or array.dtype != dtype:
                raise ValueError(f"invalid checkpoint {name} shape or dtype")
            _finite(array, f"checkpoint {name}")
        for sign in ("plus", "minus"):
            factor = getattr(self, "L" + sign)
            if np.any(np.triu(factor, 1) != 0) or np.any(np.diag(factor) <= 0):
                raise ValueError("invalid saved covariance factor")
        if not np.array_equal(self.call_times, np.repeat(np.arange(self.steps) * self.config.h, self.m)) or not np.array_equal(self.call_directions, np.tile(self.u, (self.steps, 1))):
            raise ValueError("checkpoint call records disagree with configuration")
        if not np.array_equal(self.omega, np.tile(self.config.h * self.weights, self.steps)):
            raise ValueError("checkpoint probe weights disagree with configuration")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--config", type=Path, help="JSON SolverConfig")
    source.add_argument("--resume", type=Path, help="complete NPZ checkpoint")
    parser.add_argument("--steps", type=int, required=True, help="additional physical Euler steps")
    parser.add_argument("--order", type=int, required=True, help="passive normal Gauss-Hermite order")
    parser.add_argument("--output", type=Path, required=True, help="fresh study generated-data directory")
    parser.add_argument("--checkpoint-every", type=int, default=0)
    args = parser.parse_args(argv)
    _integer(args.steps, "steps", 0)
    _integer(args.order, "order")
    _integer(args.checkpoint_every, "checkpoint interval", 0)
    generated_root = Path(__file__).resolve().parents[2] / "data/generated/population_flow_computation"
    if not args.output.resolve().is_relative_to(generated_root.resolve()):
        parser.error("outputs must be in data/generated/population_flow_computation/")
    args.output.mkdir(parents=True, exist_ok=False)
    solver = DirectionalSolver.load(args.resume) if args.resume else DirectionalSolver(json.loads(args.config.read_text()))
    started = time.perf_counter()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_path = args.resume or args.config
    provenance = {
        "source_sha256": source_hash, "input_path": str(input_path.resolve()),
        "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
        "argv": sys.argv if argv is None else argv, "cwd": os.getcwd(),
        "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        "platform": platform.platform(), "machine": platform.machine(), "config": asdict(solver.config),
        "threads": {name: os.environ.get(name) for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        "steps_requested": args.steps, "starting_steps": solver.steps, "passive_quadrature_order": args.order,
    }
    (args.output / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    status, failure = 0, None
    try:
        with (args.output / "diagnostics.jsonl").open("x") as stream:
            stream.write(json.dumps(solver.diagnostics(args.order)) + "\n")
            for step_index in range(args.steps):
                solver.step()
                stream.write(json.dumps(solver.diagnostics(args.order, full=step_index == args.steps - 1)) + "\n")
                stream.flush()
                if args.checkpoint_every and solver.steps % args.checkpoint_every == 0:
                    solver.save(args.output / f"checkpoint_{solver.steps:06d}.npz")
    except (NumericalFailure, FloatingPointError) as exc:
        status, failure = 1, str(exc)
    solver.save(args.output / "final_state.npz")
    final = {"exit_status": status, "failure": failure, "wall_seconds": time.perf_counter() - started, "completed_steps": solver.steps, "physical_time": solver.time, "checkpoint_bytes": (args.output / "final_state.npz").stat().st_size, "checkpoint_sha256": hashlib.sha256((args.output / "final_state.npz").read_bytes()).hexdigest()}
    (args.output / "outcome.json").write_text(json.dumps(final, indent=2) + "\n")
    print(json.dumps(final))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
