"""Deterministic finite-dimensional checks of the cost-section identities.

These are algebra checks, not a training experiment, timing benchmark,
floating-point stability theorem, or validation of the analytic error bounds.
Run with Python 3 and NumPy; no files are written.
"""

import json
import platform

import numpy as np


RNG = np.random.default_rng(20261006)
ERRORS = {}


def check(name, actual, expected):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    scale = max(1.0, float(np.max(np.abs(expected))))
    ERRORS[name] = error / scale
    assert error <= 2e-11 * scale, (name, error, scale)


def truncated_product(a, b, order):
    return np.convolve(a, b)[: order + 1]


def jet_actions():
    n, m, batch, order = 7, 3, 2, 6
    u = RNG.normal(size=(order, n, m))
    h = RNG.normal(size=(order, n, m))
    x = RNG.normal(size=(order + 1, n, batch))
    weights = np.zeros((order + 1, n, n))
    for s in range(1, order + 1):
        weights[s] = sum(u[i] @ h[s - 1 - i].T for i in range(s)) / s
    materialized = np.zeros_like(x)
    direct = np.zeros_like(x)
    cached = np.zeros_like(x)
    contractions = np.einsum("jnm,knb->jkmb", h, x)
    for s in range(1, order + 1):
        materialized[s] = sum(weights[a] @ x[s - a] for a in range(1, s + 1))
        for i in range(s):
            combined = np.zeros((m, batch))
            for j in range(s - i):
                k = s - 1 - i - j
                direct[s] += u[i] @ (h[j].T @ x[k]) / (i + j + 1)
                combined += contractions[j, k] / (i + j + 1)
            cached[s] += u[i] @ combined
    check("jet_direct_vs_materialized", direct, materialized)
    check("jet_cached_vs_materialized", cached, materialized)
    transposed = np.zeros_like(x)
    for s in range(1, order + 1):
        for i in range(s):
            for j in range(s - i):
                k = s - 1 - i - j
                transposed[s] += h[j] @ (u[i].T @ x[k]) / (i + j + 1)
    expected = np.zeros_like(x)
    for s in range(1, order + 1):
        expected[s] = sum(weights[a].T @ x[s - a] for a in range(1, s + 1))
    check("jet_transpose_vs_materialized", transposed, expected)


def temporal_compilation():
    order, degree, nodes = 10, 5, 13
    c, u, v = 0.7, 0.31, 0.43
    series = np.zeros(order + 1)
    for j in range(1, order + 1):
        series[j] = c * (((-1) ** (j + 1)) * u**j + v**j) / j
    explicit = np.zeros((order + 1, order + 1))
    explicit[0, 0] = 1
    for k in range(1, order + 1):
        explicit[:, k] = truncated_product(explicit[:, k - 1], series, order)
    recurrence = np.zeros_like(explicit)
    recurrence[0, 0] = 1
    for k in range(1, order + 1):
        for j in range(order):
            previous = recurrence[j - 1, k] if j else 0.0
            recurrence[j + 1, k] = (
                k * c * (u + v) * recurrence[j, k - 1]
                - (u - v) * j * recurrence[j, k]
                + u * v * (j - 1) * previous
            ) / (j + 1)
    check("continuation_power_recurrence", recurrence, explicit)
    xi = np.linspace(0, 0.6, nodes)
    quadrature = RNG.normal(size=(degree + 1, nodes))
    powers = xi[:, None] ** np.arange(order + 1)[None, :]
    e = quadrature @ powers
    b = e @ recurrence
    jets = RNG.normal(size=(order + 1, 4))
    reconstructed_nodes = powers @ (explicit @ jets)
    check("compiled_temporal_projection", b @ jets, quadrature @ reconstructed_nodes)
    # Reordering finite temporal/spatial sums preserves paired linear images.
    mixer = RNG.normal(size=(6, 4))
    check("paired_source_projection", (b @ jets) @ mixer.T, b @ (jets @ mixer.T))


def metric_identities():
    q, rank = 9, 4
    p = RNG.normal(size=(q, rank))
    d = np.diag(np.exp(RNG.normal(scale=0.2, size=q)))
    gram = p.T @ d @ p
    gi = np.linalg.inv(gram)
    metric = d + d @ p @ (gi @ gi - gi) @ p.T @ d
    inverse = np.linalg.inv(d) + p @ (np.eye(rank) - gi) @ p.T
    check("metric_inverse", metric @ inverse, np.eye(q))
    check("metric_selected_adjoint", p.T @ metric, gi @ p.T @ d)
    check("metric_selected_isometry", p.T @ metric @ p, np.eye(rank))
    assert np.linalg.eigvalsh(metric).min() > 0


def harmonic_normalizations():
    # Odd dimensions make the integration weight polynomial: Gauss-Legendre
    # is an independent exact-in-real-arithmetic oracle at this finite degree.
    nodes, weights = np.polynomial.legendre.leggauss(64)
    for dimension in (3, 5, 7):
        angular_weight = weights * (1 - nodes**2) ** ((dimension - 3) // 2)
        angular_weight /= angular_weight.sum()
        base_norm = 1.0
        for ell in range(5):
            if ell:
                base_norm *= (2 * (ell - 1) + dimension - 1) / (2 * (ell - 1) + dimension)
            lam = ell + (dimension - 2) / 2
            previous = np.zeros_like(nodes)
            current = np.ones_like(nodes)
            predicted = base_norm
            for degree in range(6):
                observed = np.sum(angular_weight * (1 - nodes**2) ** ell * current**2)
                check(f"harmonic_norm_d{dimension}_ell{ell}_s{degree}", observed, predicted)
                following = (
                    2 * (degree + lam) * nodes * current
                    - (degree + 2 * lam - 1) * previous
                ) / (degree + 1)
                predicted *= (degree + 2 * lam) * (degree + lam) / (
                    (degree + 1) * (degree + lam + 1)
                )
                previous, current = current, following


def legendre_execution():
    n, m, order, batch = 8, 3, 5, 2
    features = RNG.normal(size=(m, order, n))
    responses = RNG.normal(size=(m, order, n))
    weights = 2 * np.arange(order) + 1
    naive = np.zeros_like(features)
    streamed = np.zeros_like(features)
    for a in range(m):
        running = np.zeros(n)
        for j in range(order):
            naive[a, j] = sum(
                (weights[i] * features[a, i] for i in range(j)), start=np.zeros(n)
            )
            streamed[a, j] = running
            running += weights[j] * features[a, j]
    check("legendre_prefix_sums", streamed, naive)
    initial = RNG.normal(size=(n, n))
    x = RNG.normal(size=(n, batch))
    scale = -2 / (m * n * 1.7)
    reconstructed = initial.copy()
    streamed_action = initial @ x
    for a in range(m):
        for j in range(order):
            reconstructed += scale * weights[j] * np.outer(responses[a, j], features[a, j])
            streamed_action += scale * weights[j] * np.outer(responses[a, j], features[a, j] @ x)
    check("legendre_factor_action", streamed_action, reconstructed @ x)


def harmonic_runtime():
    m, d, widths = 3, 4, [6, 7, 5]
    features = [RNG.normal(size=(q, m)) for q in widths]
    signals = [RNG.normal(size=(q, m)) for q in widths]
    metrics = []
    for q in widths:
        a = RNG.normal(size=(q, q))
        metrics.append(np.eye(q) + a.T @ a / q)
    inputs = RNG.normal(size=(d, m))
    inputs /= np.linalg.norm(inputs, axis=0)
    residual = RNG.normal(size=m)
    da = 2 / m * (signals[0] * residual) @ inputs.T
    db = [
        2 / m * (signals[j] * residual) @ (metrics[j - 1] @ features[j - 1]).T
        for j in range(1, len(widths))
    ]
    dw = 2 / m * features[-1] @ residual
    gram = features[-1].T @ metrics[-1] @ features[-1]
    gram += (signals[0].T @ metrics[0] @ signals[0]) * (inputs.T @ inputs)
    for j in range(1, len(widths)):
        gram += (signals[j].T @ metrics[j] @ signals[j]) * (
            features[j - 1].T @ metrics[j - 1] @ features[j - 1]
        )
    action = features[-1].T @ metrics[-1] @ dw
    action += np.sum(signals[0] * (metrics[0] @ da @ inputs), axis=0)
    for j in range(1, len(widths)):
        action += np.sum(signals[j] * (metrics[j] @ db[j - 1] @ features[j - 1]), axis=0)
    check("harmonic_matrix_free_gram_action", action, 2 / m * gram @ residual)
    v = features[-1] / np.sqrt(m)
    top_metric = metrics[-1]
    w = RNG.normal(size=widths[-1])
    y = RNG.normal(size=m)
    feature_gram = v.T @ top_metric @ v
    corrected = w + v @ np.linalg.solve(
        feature_gram, (y - residual) / np.sqrt(m) - v.T @ top_metric @ w
    )
    effective = top_metric @ corrected
    query = RNG.normal(size=widths[-1])
    check("harmonic_inference_cache", effective @ query, corrected @ top_metric @ query)
    check("harmonic_training_interpolation", effective @ features[-1], y - residual)


def main():
    jet_actions()
    temporal_compilation()
    metric_identities()
    harmonic_normalizations()
    legendre_execution()
    harmonic_runtime()
    print(json.dumps({
        "status": "PASS",
        "seed": 20261006,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "relative_error_tolerance": 2e-11,
        "normalized_max_errors": ERRORS,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
