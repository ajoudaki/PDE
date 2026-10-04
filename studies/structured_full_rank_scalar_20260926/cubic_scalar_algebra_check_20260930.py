"""Finite-array algebra checks only; this script does not train a network.

Checks initial tangent contractions, the changing-kernel coefficient,
positive completion, and the cubic arbitrary-query decoder derivative.
"""
import json
from pathlib import Path

import numpy as np


def features(w, middle, inputs):
    x = np.tanh(inputs @ w.T)
    h = np.tanh(x @ middle.T)
    return x, h


def kernel(w, middle, readout, inputs):
    n = len(readout)
    x, h = features(w, middle, inputs)
    delta2 = (1 - h * h) * readout[None, :]
    delta1 = (delta2 @ middle) * (1 - x * x)
    return (h @ h.T / n + (inputs @ inputs.T) * (delta1 @ delta1.T / n)
            + (delta2 @ delta2.T / n) * (x @ x.T / n))


def run():
    rng = np.random.default_rng(4132)
    n, block, m = 12, 3, 3
    angles = np.array([0.0, 0.73, 1.86, 2.31])
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    count = len(inputs)
    w = rng.standard_normal((n, 2))
    middle = np.zeros((n, n))
    for start in range(0, n, block):
        middle[start:start+block, start:start+block] = (
            rng.standard_normal((block, block)) / np.sqrt(block))
    x, h = features(w, middle, inputs)
    gamma = (1 - h * h)[:, None, :] * h[None, :, :]
    beta = (gamma @ middle) * (1 - x * x)[:, None, :]
    tw = beta[..., None] * inputs[:, None, None, :]
    tm = gamma[..., :, None] * x[:, None, None, :] / n
    direct = (np.einsum("abij,cdij->abcd", tw, tw) / n
              + np.einsum("abij,cdij->abcd", tm, tm))
    factored = ((inputs @ inputs.T)[:, None, :, None]
                * np.einsum("abi,cdi->abcd", beta, beta) / n
                + np.einsum("abi,cdi->abcd", gamma, gamma) / n
                * (x @ x.T / n)[:, None, :, None])
    z = rng.standard_normal(m) * 0.4
    anti = rng.standard_normal((m, m)) * 0.05
    anti = (anti - anti.T) / 2
    j = np.outer(z, z) / 2 + anti
    alpha = 2 / m
    dw = alpha**2 * np.einsum("ab,abij->ij", j, tw[:m, :m])
    dm = alpha**2 * np.einsum("ab,abij->ij", j, tm[:m, :m])
    c1 = -alpha * z @ h[:m]
    k0 = h @ h.T / n
    mat = alpha**2 * np.einsum("bc,aqbc->qa", j, factored[:, :, :m, :m])
    positive = alpha**2 * np.einsum(
        "d,b,qdab->qa", z, z, factored[:, :m, :, :m])
    k2 = mat + mat.T + positive
    scaling = []
    for amp in [0.16, 0.08, 0.04, 0.02]:
        exact = kernel(w + amp**2 * dw, middle + amp**2 * dm,
                       amp * c1, inputs)
        err = float(np.linalg.norm(exact - k0 - amp**2 * k2))
        scaling.append({"amplitude": amp, "kernel_remainder": err,
                        "remainder_div_amplitude4": err / amp**4})
    ktrain = k0[:m, :m]
    mtrain = mat[:m, :m]
    completed = ((np.eye(m) + np.linalg.solve(ktrain, mtrain)).T
                 @ ktrain @ (np.eye(m) + np.linalg.solve(ktrain, mtrain))
                 + positive[:m, :m])
    completion_identity = np.linalg.norm(
        completed - (ktrain + k2[:m, :m]
                     + mtrain.T @ np.linalg.solve(ktrain, mtrain)))

    residual = rng.standard_normal(m)
    pdot = np.einsum("a,bc->abc", residual, j)
    decoder_dot = np.empty(count)
    for q in range(count):
        linear = k0[q, :m] @ residual
        feature = 0.0
        tangent = 0.0
        for a in range(m):
            for b in range(m):
                for c in range(m):
                    feature += pdot[a, b, c] * (
                        factored[a, q, b, c] + factored[q, a, b, c])
                    tangent += (pdot[a, b, c] + pdot[a, c, b]) * factored[q, b, a, c]
        decoder_dot[q] = -alpha * (linear + alpha**2 * (feature + tangent))
    expected_dot = -alpha * (k0[:, :m] + k2[:, :m]) @ residual
    result = {
        "kind": "algebra verification only; no ODE integration or training",
        "width": n, "block_size": block, "training_inputs": m,
        "tangent_gram_max_abs_gap": float(np.max(np.abs(direct-factored))),
        "kernel_expansion": scaling,
        "psd_completion_identity_gap": float(completion_identity),
        "psd_completion_min_eigenvalue": float(np.linalg.eigvalsh(completed)[0]),
        "passive_decoder_derivative_max_abs_gap": float(np.max(np.abs(decoder_dot-expected_dot))),
    }
    assert result["tangent_gram_max_abs_gap"] < 1e-12
    assert result["psd_completion_identity_gap"] < 1e-12
    assert result["psd_completion_min_eigenvalue"] >= -1e-12
    assert result["passive_decoder_derivative_max_abs_gap"] < 1e-12
    for before, after in zip(scaling, scaling[1:]):
        assert 14 < before["kernel_remainder"] / after["kernel_remainder"] < 18
    target = Path(__file__).parents[2] / "data/generated/structured_full_rank_scalar_20260926/cubic_scalar_algebra_20260930.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
