"""Particle approximation of the exact inverse-free L=2 OMFP DAG.

This is an exploratory implementation of equations (3.1)--(3.3) in the
established fixed-h identification.  It explicitly carries the source
Jacobians used by rho and sigma.  Monte Carlo Schur complements are clipped
only at roundoff scale; runs reporting material clipping are rejected.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.hermite import hermgauss


@dataclass(frozen=True)
class SinPower:
    power: int
    lam: float
    scale: float

    def phi(self, x: np.ndarray) -> np.ndarray:
        return (x + self.lam * np.sin(x**self.power)) / self.scale

    def d1(self, x: np.ndarray) -> np.ndarray:
        p = self.power
        return (1 + self.lam * p * x ** (p - 1) * np.cos(x**p)) / self.scale

    def d2(self, x: np.ndarray) -> np.ndarray:
        p = self.power
        return (
            self.lam
            * (
                p * (p - 1) * x ** (p - 2) * np.cos(x**p)
                - p**2 * x ** (2 * p - 2) * np.sin(x**p)
            )
            / self.scale
        )


def scale(power: int, lam: float, order: int = 256) -> float:
    x, w = hermgauss(order)
    g = math.sqrt(2) * x
    y = g + lam * np.sin(g**power)
    return float(math.sqrt(np.dot(w, y * y) / math.sqrt(math.pi)))


def conditional_coordinate(
    covariance: np.ndarray,
    history: np.ndarray,
    innovation: np.ndarray,
) -> tuple[np.ndarray, float]:
    """Sample the last coordinate given already sampled prior coordinates."""
    s = covariance.shape[0] - 1
    if s == 0:
        variance = float(covariance[0, 0])
        return math.sqrt(max(variance, 0.0)) * innovation, min(variance, 0.0)
    old = covariance[:s, :s]
    cross = covariance[s, :s]
    coef = np.linalg.pinv(old, rcond=1e-11) @ cross
    variance = float(covariance[s, s] - cross @ coef)
    scale_v = max(1.0, float(covariance[s, s]))
    clipped = min(variance, 0.0)
    if variance < -1e-5 * scale_v:
        raise FloatingPointError(f"material negative Schur complement {variance}")
    return history @ coef + math.sqrt(max(variance, 0.0)) * innovation, clipped


def run_dag(act: SinPower, h: float, steps: int, particles: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    lower_u = rng.standard_normal(particles)
    top_a0 = rng.standard_normal(particles)
    lower_innov = rng.standard_normal((particles, steps))
    top_innov = rng.standard_normal((particles, steps + 1))

    hs: list[np.ndarray] = []
    cs: list[np.ndarray] = []
    ys: list[np.ndarray] = []
    chi_hist = np.empty((particles, 0))
    xi_hist = np.empty((particles, 0))
    # Formal source Jacobians.  Column k means partial w.r.t. coordinate k.
    du = np.zeros((particles, steps))
    dc_hist: list[np.ndarray] = []
    dh_hist: list[np.ndarray] = []
    q = np.zeros((steps + 1, steps + 1))
    k = np.zeros((steps, steps))
    clipped_total = 0.0
    dy_hist: list[np.ndarray] = []

    for s in range(steps + 1):
        h_s = act.phi(lower_u)
        dh_s = act.d1(lower_u)[:, None] * du
        hs.append(h_s)
        dh_hist.append(dh_s.copy())
        for r in range(s + 1):
            q[s, r] = q[r, s] = float(np.mean(h_s * hs[r]))

        xi_s, clipped = conditional_coordinate(
            q[: s + 1, : s + 1], xi_hist, top_innov[:, s]
        )
        clipped_total += abs(clipped)
        xi_hist = np.column_stack((xi_hist, xi_s))

        z_s = xi_s.copy()
        dz = np.zeros((particles, steps + 1))
        dz[:, s] = 1.0
        for r in range(s):
            rho_sr = float(np.mean(dh_s[:, r]))
            coeff = rho_sr + h * q[r, s]
            z_s += coeff * cs[r]
            dz += coeff * dc_hist[r]

        a_s = top_a0.copy()
        da = np.zeros((particles, steps + 1))
        for r in range(s):
            a_s += h * ys[r]
        if s:
            da = h * np.sum(np.stack(dy_hist, axis=0), axis=0)

        y_s = act.phi(z_s)
        dy_s = act.d1(z_s)[:, None] * dz
        ys.append(y_s)
        dy_hist.append(dy_s)

        if s == steps:
            terminal = float(np.mean(a_s * y_s))
            return {
                "F": terminal,
                "Q_terminal": float(q[s, s]),
                "max_Q": float(np.max(np.diag(q[: s + 1, : s + 1]))),
                "clipped_schur": clipped_total,
            }

        c_s = a_s * act.d1(z_s)
        dc_s = da * act.d1(z_s)[:, None] + a_s[:, None] * act.d2(z_s)[:, None] * dz
        cs.append(c_s)
        dc_hist.append(dc_s)
        for r in range(s + 1):
            k[s, r] = k[r, s] = float(np.mean(c_s * cs[r]))

        chi_s, clipped = conditional_coordinate(
            k[: s + 1, : s + 1], chi_hist, lower_innov[:, s]
        )
        clipped_total += abs(clipped)
        chi_hist = np.column_stack((chi_hist, chi_s))

        b_s = chi_s.copy()
        db = np.zeros((particles, steps))
        db[:, s] = 1.0
        for r in range(s + 1):
            sigma_sr = float(np.mean(dc_s[:, r]))
            b_s += sigma_sr * hs[r]
            db += sigma_sr * dh_hist[r]
        for r in range(s):
            b_s += h * k[s, r] * hs[r]
            db += h * k[s, r] * dh_hist[r]

        old_u = lower_u
        old_du = du.copy()
        lower_u = old_u + h * b_s * act.d1(old_u)
        du = old_du + h * (
            db * act.d1(old_u)[:, None]
            + b_s[:, None] * act.d2(old_u)[:, None] * old_du
        )

    raise AssertionError("unreachable")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--power", type=int, default=3)
    parser.add_argument("--lam", type=float, default=0.25)
    parser.add_argument("--particles", type=int, default=200_000)
    parser.add_argument("--rho", type=float, default=0.02)
    parser.add_argument("--times", nargs="+", type=int, default=[1, 2, 3, 4])
    parser.add_argument("--seeds", type=int, default=3)
    args = parser.parse_args()
    act = SinPower(args.power, args.lam, scale(args.power, args.lam))
    rows = []
    for t in args.times:
        h = args.rho / t
        for seed in range(args.seeds):
            fine = run_dag(act, h, 2 * t, args.particles, 1009 * seed + 17)
            coarse = run_dag(act, 2 * h, t, args.particles, 1009 * seed + 17)
            rows.append(
                {
                    "t": t,
                    "seed": seed,
                    "h": h,
                    "fine": fine,
                    "coarse": coarse,
                    "delta": fine["F"] - coarse["F"],
                }
            )
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
