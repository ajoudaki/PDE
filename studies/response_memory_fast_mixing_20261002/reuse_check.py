"""Preregistered Gaussian-probe reuse check, CPU float64 only."""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"
import argparse
import hashlib
import json
import platform
from pathlib import Path
import time
import numpy as np


def hadamard(x):
    x = np.array(x, dtype=np.float64, copy=True)
    n = x.shape[-1]
    if n < 1 or n & (n - 1):
        raise ValueError("last dimension must be a positive power of two")
    width = 1
    while width < n:
        view = x.reshape(*x.shape[:-1], -1, 2, width)
        left, right = view[..., 0, :].copy(), view[..., 1, :].copy()
        view[..., 0, :] = left + right
        view[..., 1, :] = left - right
        width *= 2
    return x / np.sqrt(n)


def quarter_circle(n):
    probability = (np.arange(n) + 0.5) / n
    left = np.zeros(n)
    right = np.full(n, 2.0)
    for _ in range(60):
        middle = (left + right) / 2
        cdf = (middle * np.sqrt(np.maximum(0.0, 4 - middle**2)) / 2
               + 2 * np.arcsin(middle / 2)) / np.pi
        left = np.where(cdf < probability, middle, left)
        right = np.where(cdf >= probability, middle, right)
    singular = (left + right) / 2
    return singular / np.sqrt(np.mean(singular**2))


class FastMixer:
    """W=D_left H diag(sign*s) P H D_right, exact stored adjoint."""
    def __init__(self, singular, seed):
        self.n = len(singular)
        rng = np.random.default_rng(seed)
        self.left = rng.choice([-1., 1.], self.n)
        self.right = rng.choice([-1., 1.], self.n)
        self.middle = rng.choice([-1., 1.], self.n) * singular[rng.permutation(self.n)]
        self.permutation = rng.permutation(self.n)
        self.inverse = np.argsort(self.permutation)

    def forward(self, x):
        z = hadamard(x * self.right)
        return hadamard(z[..., self.permutation] * self.middle) * self.left

    def transpose(self, x):
        z = hadamard(x * self.left) * self.middle
        return hadamard(z[..., self.inverse]) * self.right


def gaussian_moments(order):
    x, weights = np.polynomial.hermite.hermgauss(order)
    x = np.sqrt(2) * x
    weights = weights / np.sqrt(np.pi)
    response = np.tanh(x)
    return float(weights @ response**2), float(weights @ (x * response))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    v128, a128 = gaussian_moments(128)
    v, a = gaussian_moments(256)
    quadrature_error = max(abs(v - v128), abs(a - a128))
    if quadrature_error > 1e-9:
        raise RuntimeError(f"quadrature failed: {quadrature_error}")
    rows = []
    arrays = {}
    for n in (128, 256, 512, 1024):
        probe = np.random.default_rng(6101 + n).standard_normal((128, n))
        spectral_rng = np.random.default_rng(6201 + n)
        normal_s = np.abs(spectral_rng.standard_normal(n))
        normal_s /= np.sqrt(np.mean(normal_s**2))
        spectra = {"flat": np.ones(n), "quarter_circle": quarter_circle(n),
                   "gaussian_diagonal": normal_s}
        energies = {}
        for case in (*spectra, "dense_gaussian"):
            if time.monotonic() - started > 600:
                raise RuntimeError("CPU budget exhausted")
            if case == "dense_gaussian":
                matrix = spectral_rng.standard_normal((n, n))
                matrix /= np.linalg.norm(matrix, axis=1, keepdims=True)
                forward = lambda x: x @ matrix.T
                transpose = lambda x: x @ matrix
            else:
                mixer = FastMixer(spectra[case], 6301 + n)
                forward, transpose = mixer.forward, mixer.transpose
                matrix = forward(np.eye(n)).T
            forward_error = np.linalg.norm(forward(probe) - probe @ matrix.T) / np.linalg.norm(probe @ matrix.T)
            transpose_error = np.linalg.norm(transpose(probe) - probe @ matrix) / np.linalg.norm(probe @ matrix)
            covariance = matrix @ matrix.T
            diagonal_error = float(np.max(np.abs(np.diag(covariance) - 1)))
            fourth = float(np.sum(covariance**2) / n)
            np.fill_diagonal(covariance, 0)
            max_off_diagonal = float(np.max(np.abs(covariance)))
            leading = v + a**2 * (fourth - 1)
            remainder = max(0., (v - a**2) * max_off_diagonal**2 * (fourth - 1))
            energy = np.mean(transpose(np.tanh(forward(probe)))**2, axis=1)
            mean, se = float(np.mean(energy)), float(np.std(energy, ddof=1) / np.sqrt(len(energy)))
            discrepancy = max(leading - mean, mean - leading - remainder, 0.)
            passed = bool(max(forward_error, transpose_error, diagonal_error) < 1e-12
                          and discrepancy <= 4 * se + 1e-9)
            record = dict(n=n, case=case, count=len(probe), mean=mean, standard_error=se,
                          leading=leading, remainder_bound=remainder, fourth_moment=fourth,
                          max_off_diagonal=max_off_diagonal, forward_error=float(forward_error),
                          transpose_error=float(transpose_error), diagonal_error=diagonal_error,
                          pass_validity=passed)
            rows.append(record)
            energies[case] = energy
            arrays[f"{case}_{n}"] = energy
            print(json.dumps(record), flush=True)
        gap = energies["quarter_circle"] - energies["flat"]
        arrays[f"paired_gap_{n}"] = gap
    np.savez(args.out / "probe_energies.npz", **arrays)
    gap_pass = any(np.mean(arrays[f"paired_gap_{n}"]) > 5 * np.std(arrays[f"paired_gap_{n}"], ddof=1) / np.sqrt(128)
                   for n in (512, 1024))
    sources = [Path(__file__), Path(__file__).with_name("REUSE_PROTOCOL.md")]
    report = dict(status="pass" if all(r["pass_validity"] for r in rows) and gap_pass else "fail_or_inconclusive",
                  claim_scope="Gaussian-probe return energy only; not trained-model universality",
                  v=v, a=a, quadrature_error=quadrature_error, gap_pass=bool(gap_pass),
                  cases=rows, elapsed_seconds=time.monotonic()-started,
                  environment=dict(python=platform.python_version(), numpy=np.__version__, platform=platform.platform()),
                  source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources})
    (args.out / "metrics.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
