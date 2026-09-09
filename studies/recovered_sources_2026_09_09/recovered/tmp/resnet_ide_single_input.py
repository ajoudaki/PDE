#!/usr/bin/env python3
"""Independent particle and Eulerian simulations of the one-input ResNet IDE."""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass

import numpy as np


XI = 1.0
LABEL = 0.0
ETA = 1.0
T_FINAL = 0.50
OUTPUT_DT = 0.01
TIME_STEP = 0.004


def feature_values(alpha, omega, beta, x):
    """Phi, d_x Phi, and the three raw-parameter derivatives."""
    amp = np.tanh(alpha)
    slope = np.tanh(omega)
    bias = np.tanh(beta)
    inner = slope * x + bias
    act = np.tanh(inner)
    sech2_inner = 1.0 - act * act
    phi = amp * act
    dphi_dx = amp * sech2_inner * slope
    grad_alpha = (1.0 - amp * amp) * act
    grad_omega = amp * sech2_inner * (1.0 - slope * slope) * x
    grad_beta = amp * sech2_inner * (1.0 - bias * bias)
    return phi, dphi_dx, grad_alpha, grad_omega, grad_beta


@dataclass
class Sweep:
    x: np.ndarray
    r: np.ndarray
    output: float
    loss: float


def particle_sweep(theta: np.ndarray) -> Sweep:
    layers = theta.shape[0]
    ds = 1.0 / layers
    x = np.empty(layers + 1)
    x[0] = XI
    dbar = np.empty(layers)
    for k in range(layers):
        a, w, b = theta[k].T
        phi, dphi_dx, *_ = feature_values(a, w, b, x[k])
        x[k + 1] = x[k] + ds * float(np.mean(phi))
        dbar[k] = float(np.mean(dphi_dx))
    r = np.empty(layers + 1)
    r[-1] = 1.0
    for k in range(layers - 1, -1, -1):
        r[k] = r[k + 1] * (1.0 + ds * dbar[k])
    output = float(x[-1])
    return Sweep(x=x, r=r, output=output, loss=0.5 * (output - LABEL) ** 2)


def particle_rhs(theta: np.ndarray):
    sweep = particle_sweep(theta)
    a = theta[..., 0]
    w = theta[..., 1]
    b = theta[..., 2]
    x = sweep.x[:-1, None]
    _, _, ga, gw, gb = feature_values(a, w, b, x)
    coefficient = -ETA * (sweep.output - LABEL) * sweep.r[1:, None]
    velocity = np.stack(
        (coefficient * ga, coefficient * gw, coefficient * gb), axis=-1
    )
    return velocity, sweep


def simulate_particles(width: int, layers: int, seed: int, targets: np.ndarray):
    rng = np.random.default_rng(seed)
    theta = rng.normal(size=(layers, width, 3))
    theta[..., 0] += 2.0
    theta[..., 1] += 2.0
    records = []
    t = 0.0
    records.append(particle_sweep(theta))
    for target in targets[1:]:
        while t < target - 1e-14:
            dt = min(TIME_STEP, target - t)
            k1, _ = particle_rhs(theta)
            predictor = theta + dt * k1
            k2, _ = particle_rhs(predictor)
            theta += 0.5 * dt * (k1 + k2)
            t += dt
        records.append(particle_sweep(theta))
    return {
        "output": np.array([r.output for r in records]),
        "loss": np.array([r.loss for r in records]),
        "theta": theta,
        "min": float(theta.min()),
        "max": float(theta.max()),
    }


class EulerianSolver:
    def __init__(self, grid_size: int, layers: int):
        self.grid_size = grid_size
        self.layers = layers
        self.ds = 1.0 / layers
        self.a_edges = np.linspace(-4.0, 8.0, grid_size + 1)
        self.w_edges = np.linspace(-4.0, 8.0, grid_size + 1)
        self.b_edges = np.linspace(-6.0, 6.0, grid_size + 1)
        self.a = 0.5 * (self.a_edges[:-1] + self.a_edges[1:])
        self.w = 0.5 * (self.w_edges[:-1] + self.w_edges[1:])
        self.b = 0.5 * (self.b_edges[:-1] + self.b_edges[1:])
        self.da = float(self.a_edges[1] - self.a_edges[0])
        self.dw = float(self.w_edges[1] - self.w_edges[0])
        self.db = float(self.b_edges[1] - self.b_edges[0])
        self.dv = self.da * self.dw * self.db
        self.aa = self.a[:, None, None]
        self.ww = self.w[None, :, None]
        self.bb = self.b[None, None, :]
        gauss = np.exp(
            -0.5
            * (
                (self.aa - 2.0) ** 2
                + (self.ww - 2.0) ** 2
                + self.bb**2
            )
        ) / ((2.0 * math.pi) ** 1.5)
        gauss /= float(np.sum(gauss) * self.dv)
        self.q = np.repeat(gauss[None, ...], layers, axis=0)

    def sweep(self, q: np.ndarray) -> Sweep:
        x = np.empty(self.layers + 1)
        x[0] = XI
        dbar = np.empty(self.layers)
        for k in range(self.layers):
            phi, dphi_dx, *_ = feature_values(
                self.aa, self.ww, self.bb, x[k]
            )
            x[k + 1] = x[k] + self.ds * float(np.sum(q[k] * phi) * self.dv)
            dbar[k] = float(np.sum(q[k] * dphi_dx) * self.dv)
        r = np.empty(self.layers + 1)
        r[-1] = 1.0
        for k in range(self.layers - 1, -1, -1):
            r[k] = r[k + 1] * (1.0 + self.ds * dbar[k])
        output = float(x[-1])
        return Sweep(x=x, r=r, output=output, loss=0.5 * output**2)

    @staticmethod
    def add_flux(rhs, q, v, axis, spacing):
        # Second-order MUSCL reconstruction with a minmod limiter.  This is
        # materially less diffusive than first-order upwinding for the smooth
        # Gaussian density while retaining a conservative face flux.
        slope = np.zeros_like(q)
        previous = [slice(None)] * q.ndim
        middle = [slice(None)] * q.ndim
        following = [slice(None)] * q.ndim
        previous[axis] = slice(0, -2)
        middle[axis] = slice(1, -1)
        following[axis] = slice(2, None)
        previous = tuple(previous)
        middle = tuple(middle)
        following = tuple(following)
        backward = q[middle] - q[previous]
        forward = q[following] - q[middle]
        limited = np.where(
            backward * forward > 0.0,
            np.sign(backward) * np.minimum(np.abs(backward), np.abs(forward)),
            0.0,
        )
        slope[middle] = limited

        left = [slice(None)] * q.ndim
        right = [slice(None)] * q.ndim
        left[axis] = slice(0, -1)
        right[axis] = slice(1, None)
        left = tuple(left)
        right = tuple(right)
        face_v = 0.5 * (v[left] + v[right])
        q_left = np.maximum(q[left] + 0.5 * slope[left], 0.0)
        q_right = np.maximum(q[right] - 0.5 * slope[right], 0.0)
        flux = (
            np.maximum(face_v, 0.0) * q_left
            + np.minimum(face_v, 0.0) * q_right
        )
        rhs[left] -= flux / spacing
        rhs[right] += flux / spacing

    def rhs(self, q: np.ndarray):
        sweep = self.sweep(q)
        va = np.empty_like(q)
        vw = np.empty_like(q)
        vb = np.empty_like(q)
        residual = sweep.output - LABEL
        for k in range(self.layers):
            _, _, grad_a, grad_w, grad_b = feature_values(
                self.aa, self.ww, self.bb, sweep.x[k]
            )
            coefficient = -ETA * residual * sweep.r[k + 1]
            va[k] = coefficient * grad_a
            vw[k] = coefficient * grad_w
            vb[k] = coefficient * grad_b
        result = np.zeros_like(q)
        self.add_flux(result, q, va, 1, self.da)
        self.add_flux(result, q, vw, 2, self.dw)
        self.add_flux(result, q, vb, 3, self.db)
        cfl_rate = float(
            np.max(np.abs(va) / self.da + np.abs(vw) / self.dw + np.abs(vb) / self.db)
        )
        dissipation = float(
            np.sum(q * (va * va + vw * vw + vb * vb))
            * self.dv
            * self.ds
            / ETA
        )
        return result, sweep, cfl_rate, dissipation

    def simulate(self, targets: np.ndarray):
        q = self.q.copy()
        t = 0.0
        records = [self.sweep(q)]
        dissipations = []
        min_density = float(q.min())
        max_cfl = 0.0
        for target in targets[1:]:
            while t < target - 1e-14:
                k1, _, rate1, diss1 = self.rhs(q)
                dt = min(TIME_STEP, target - t)
                if rate1 > 0.0:
                    dt = min(dt, 0.25 / rate1)
                predictor = q + dt * k1
                k2, _, rate2, diss2 = self.rhs(predictor)
                q += 0.5 * dt * (k1 + k2)
                t += dt
                min_density = min(min_density, float(predictor.min()), float(q.min()))
                max_cfl = max(max_cfl, dt * rate1, dt * rate2)
                dissipations.append((t, 0.5 * (diss1 + diss2)))
            records.append(self.sweep(q))
        self.q = q
        masses = np.sum(q, axis=(1, 2, 3)) * self.dv
        return {
            "output": np.array([r.output for r in records]),
            "loss": np.array([r.loss for r in records]),
            "q": q,
            "mass_error": float(np.max(np.abs(masses - 1.0))),
            "min_density": min_density,
            "max_cfl": max_cfl,
            "dissipation": dissipations,
        }

    def beta_marginal(self, q: np.ndarray, depth_index: int):
        return np.sum(q[depth_index], axis=(0, 1)) * self.da * self.dw


def histogram_density(values: np.ndarray, edges: np.ndarray):
    counts, _ = np.histogram(values, bins=edges)
    return counts / (values.size * np.diff(edges))


def approximate_hist_w1(density_a, density_b, edges):
    widths = np.diff(edges)
    cdf_a = np.cumsum(density_a * widths)
    cdf_b = np.cumsum(density_b * widths)
    return float(np.sum(np.abs(cdf_a - cdf_b) * widths))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()

    started = time.time()
    targets = np.arange(0.0, T_FINAL + 0.5 * OUTPUT_DT, OUTPUT_DT)
    layers = 24 if not args.quick else 12
    fine_grid = 23 if not args.quick else 13
    coarse_grid = 17 if not args.quick else 9
    widths = [256, 1024, 4096] if not args.quick else [64, 256]
    seeds = [17, 29, 43] if not args.quick else [17]

    fine_solver = EulerianSolver(fine_grid, layers)
    fine = fine_solver.simulate(targets)
    coarse_solver = EulerianSolver(coarse_grid, layers)
    coarse = coarse_solver.simulate(targets)

    particle_results = {}
    largest_sample = None
    for width in widths:
        runs = []
        for seed in seeds:
            run = simulate_particles(width, layers, seed, targets)
            runs.append(run)
            if width == widths[-1] and seed == seeds[0]:
                largest_sample = run
        outputs = np.stack([r["output"] for r in runs])
        losses = np.stack([r["loss"] for r in runs])
        particle_results[str(width)] = {
            "output_mean": outputs.mean(axis=0),
            "output_std": outputs.std(axis=0),
            "loss_mean": losses.mean(axis=0),
            "loss_std": losses.std(axis=0),
            "final_abs_output_error": float(abs(outputs.mean(axis=0)[-1] - fine["output"][-1])),
        }

    mid = layers // 2
    beta_pde = fine_solver.beta_marginal(fine["q"], mid)
    beta_particles = histogram_density(
        largest_sample["theta"][mid, :, 2], fine_solver.b_edges
    )
    beta_w1 = approximate_hist_w1(beta_pde, beta_particles, fine_solver.b_edges)

    loss_delta = np.diff(fine["loss"])
    dissipation_integral = 0.0
    previous_time = 0.0
    for current_time, dissipation in fine["dissipation"]:
        dissipation_integral += (current_time - previous_time) * dissipation
        previous_time = current_time
    dissipation_balance_error = abs(
        fine["loss"][-1] - (fine["loss"][0] - dissipation_integral)
    )
    payload = {
        "configuration": {
            "input": XI,
            "label": LABEL,
            "eta": ETA,
            "T": T_FINAL,
            "layers": layers,
            "fine_parameter_grid": fine_grid,
            "coarse_parameter_grid": coarse_grid,
            "particle_widths": widths,
            "seeds": seeds,
            "initial_law": "N((2,2,0), I_3)",
        },
        "time": targets,
        "eulerian_fine": {
            "output": fine["output"],
            "loss": fine["loss"],
            "mass_error": fine["mass_error"],
            "min_density": fine["min_density"],
            "max_cfl": fine["max_cfl"],
        },
        "eulerian_coarse": {
            "output": coarse["output"],
            "loss": coarse["loss"],
            "final_output_difference_from_fine": float(
                abs(coarse["output"][-1] - fine["output"][-1])
            ),
        },
        "particles": particle_results,
        "beta_marginal": {
            "centers": fine_solver.b,
            "pde": beta_pde,
            "particles": beta_particles,
            "histogram_w1": beta_w1,
            "depth": mid / layers,
            "width": widths[-1],
        },
        "audits": {
            "max_positive_loss_increment": float(max(0.0, loss_delta.max())),
            "integrated_dissipation": float(dissipation_integral),
            "loss_dissipation_balance_error": float(dissipation_balance_error),
            "final_fine_output": float(fine["output"][-1]),
            "final_fine_loss": float(fine["loss"][-1]),
            "initial_fine_output": float(fine["output"][0]),
            "initial_fine_loss": float(fine["loss"][0]),
            "particle_parameter_min": largest_sample["min"],
            "particle_parameter_max": largest_sample["max"],
            "runtime_seconds": time.time() - started,
        },
    }

    def convert(value):
        if isinstance(value, np.ndarray):
            return [round(float(x), 10) for x in value]
        if isinstance(value, np.floating):
            return float(value)
        raise TypeError(type(value).__name__)

    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, default=convert, indent=2)


if __name__ == "__main__":
    main()
