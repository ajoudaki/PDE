"""Deterministic algebra checks; no training experiment or accuracy certificate.

Run from the repository root:
    python studies/transparent_learning_dynamics_20261007/polar_identity_check.py

Tests rectangular and rank-deficient maps, nondiagonal SPD layer metrics,
the specified (not metric-adjoint) backward gates, readout correction,
the polar vector field, and the rotating coactivation tensors.
"""

import numpy as np
from scipy.linalg import block_diag, polar, solve_sylvester


def product(table, left, right):
    return np.einsum("ijk,j,k->i", table, left, right)


def functional(table, unit, value, fun):
    multiplication = np.einsum("ikj,k->ij", table, value)
    spectrum, vectors = np.linalg.eig(multiplication)
    result = vectors @ (fun(spectrum) * np.linalg.solve(vectors, unit))
    return np.real_if_close(result, tol=1000).real


def rotate_table(table, frame):
    return np.einsum("ai,abc,bj,ck->ijk", frame, table, frame, frame)


def runtime(maps, metrics, readout, deficit, labels, inputs, m):
    values = [inputs]
    preactivations = []
    for layer_map in maps:
        z = layer_map @ values[-1]
        preactivations.append(z)
        values.append(np.sin(z))
    train = values[-1][:, :m]
    gram = train.T @ metrics[-1] @ train
    adjusted = readout + train @ np.linalg.solve(
        gram, labels - deficit - train.T @ metrics[-1] @ readout
    )
    backwards = [None] * len(maps)
    signal = adjusted[:, None]
    for layer in reversed(range(len(maps))):
        backwards[layer] = np.cos(preactivations[layer]) * signal
        if layer:
            signal = np.linalg.solve(
                metrics[layer], maps[layer].T @ metrics[layer + 1] @ backwards[layer]
            )
    velocities = []
    kernel = train.T @ metrics[-1] @ train
    for layer in range(len(maps)):
        source = values[layer][:, :m]
        target = backwards[layer][:, :m]
        velocities.append(
            (2 / m) * (target * deficit) @ source.T @ metrics[layer]
        )
        kernel += (target.T @ metrics[layer + 1] @ target) * (
            source.T @ metrics[layer] @ source
        )
    readout_velocity = (2 / m) * train @ deficit
    deficit_velocity = -(2 / m) * kernel @ deficit
    return {
        "values": values,
        "backwards": backwards,
        "maps_dot": velocities,
        "readout_dot": readout_velocity,
        "deficit_dot": deficit_velocity,
        "adjusted": adjusted,
        "prediction": adjusted @ metrics[-1] @ values[-1],
        "kernel": kernel,
    }


def initialize(maps, metrics, readout):
    dims = [metrics[0].shape[0]] + [matrix.shape[0] for matrix in maps]
    offsets = np.cumsum([0] + dims)
    blocks = [slice(offsets[j], offsets[j + 1]) for j in range(len(dims))]
    whitening = block_diag(*[np.linalg.cholesky(metric).T for metric in metrics])
    inverse = np.linalg.inv(whitening)
    dimension = sum(dims)
    table = np.einsum("ia,aj,ak->ijk", whitening, inverse, inverse)
    unit = whitening @ np.ones(dimension)
    masks = []
    for block in blocks:
        mask = np.zeros(dimension)
        mask[block] = 1
        masks.append(whitening @ mask)
    frames = [np.eye(dimension)]
    stretches, grams, tables, units, rotated_masks = [], [], [table], [unit], [masks]
    for layer, layer_map in enumerate(maps):
        physical = np.eye(dimension)
        physical[blocks[layer + 1], blocks[layer]] = layer_map
        shear = whitening @ physical @ inverse
        frame, stretch = polar(shear @ frames[-1])
        frames.append(frame)
        stretches.append(stretch)
        grams.append(stretch @ stretch)
        tables.append(rotate_table(table, frame))
        units.append(frame.T @ unit)
        rotated_masks.append([frame.T @ mask for mask in masks])
    embedded_readout = np.zeros(dimension)
    embedded_readout[blocks[-1]] = readout
    return {
        "blocks": blocks,
        "whitening": whitening,
        "frames": frames,
        "stretches": stretches,
        "grams": grams,
        "tables": tables,
        "units": units,
        "masks": rotated_masks,
        "rho": frames[-1].T @ whitening @ embedded_readout,
    }


def geometric_rhs(state, inputs, labels, deficit, m):
    tables, units, masks = state["tables"], state["units"], state["masks"]
    stretches = state["stretches"]
    depth = len(stretches)
    dimension = len(units[0])
    panel = inputs.shape[1]
    embed = np.zeros((dimension, panel))
    embed[state["blocks"][0]] = inputs
    values = [state["whitening"] @ embed]
    preactivations = []
    for layer in range(1, depth + 1):
        z = stretches[layer - 1] @ values[-1]
        h = np.column_stack([
            z[:, a] + product(
                tables[layer], masks[layer][layer],
                functional(tables[layer], units[layer], z[:, a], np.sin) - z[:, a],
            ) for a in range(panel)
        ])
        preactivations.append(z)
        values.append(h)
    final = np.column_stack([
        product(tables[-1], masks[-1][-1], values[-1][:, a])
        for a in range(panel)
    ])
    train = final[:, :m]
    adjusted = state["rho"] + train @ np.linalg.solve(
        train.T @ train, labels - deficit - train.T @ state["rho"]
    )
    selected = [None] * depth
    signal = np.repeat(adjusted[:, None], panel, axis=1)
    for layer in reversed(range(1, depth + 1)):
        gated = np.column_stack([
            signal[:, a] + product(
                tables[layer], masks[layer][layer], product(
                    tables[layer],
                    functional(tables[layer], units[layer],
                               preactivations[layer - 1][:, a], np.cos) - units[layer],
                    signal[:, a],
                ),
            ) for a in range(panel)
        ])
        selected[layer - 1] = np.column_stack([
            product(tables[layer], masks[layer][layer], gated[:, a])
            for a in range(panel)
        ])
        signal = stretches[layer - 1] @ gated
    forces, gram_dot, table_dot, mask_dot, unit_dot = [], [], [], [], []
    spins = [np.zeros((dimension, dimension))]
    kernel = train.T @ train
    for layer in range(1, depth + 1):
        source = np.column_stack([
            product(tables[layer - 1], masks[layer - 1][layer - 1],
                    values[layer - 1][:, a]) for a in range(m)
        ])
        target = selected[layer - 1][:, :m]
        force = (2 / m) * (target * deficit) @ source.T
        forces.append(force)
        kernel += (target.T @ target) * (source.T @ source)
        stretch, gram = stretches[layer - 1], state["grams"][layer - 1]
        previous = spins[-1]
        spin = solve_sylvester(
            stretch, stretch,
            force - force.T + stretch @ previous + previous @ stretch,
        )
        spins.append(spin)
        gd = stretch @ force + force.T @ stretch + gram @ previous - previous @ gram
        symmetric = (force + force.T) / 2
        midpoint = (spin + previous) / 2
        alternate = stretch @ symmetric + symmetric @ stretch + gram @ midpoint - midpoint @ gram
        np.testing.assert_allclose(gd, alternate, atol=2e-10, rtol=2e-10)
        gram_dot.append(gd)
        table = tables[layer]
        table_dot.append(
            -np.einsum("ia,ajk->ijk", spin, table)
            + np.einsum("iak,aj->ijk", table, spin)
            + np.einsum("ija,ak->ijk", table, spin)
        )
        mask_dot.append([-spin @ mask for mask in masks[layer]])
        unit_dot.append(-spin @ units[layer])
    return {
        "values": values, "selected": selected, "forces": forces,
        "prediction": adjusted @ final, "kernel": kernel,
        "deficit_dot": -(2 / m) * kernel @ deficit,
        "gram_dot": gram_dot, "table_dot": table_dot,
        "mask_dot": mask_dot, "unit_dot": unit_dot,
        "rho_dot": (2 / m) * train @ deficit - spins[-1] @ state["rho"],
        "spins": spins,
    }


def run_case(dims, rank_deficient, seed):
    rng = np.random.default_rng(seed)
    metrics = [np.eye(dims[0])]
    for width in dims[1:]:
        raw = rng.normal(size=(width, width))
        metrics.append(np.eye(width) + raw @ raw.T / width)
    maps = [rng.normal(size=(right, left)) / np.sqrt(left)
            for left, right in zip(dims[:-1], dims[1:])]
    if rank_deficient:
        maps[-1][1] = maps[-1][0]
    m, panel = 2, 4
    inputs = rng.normal(size=(dims[0], panel))
    inputs /= np.linalg.norm(inputs, axis=0)
    readout = rng.normal(size=dims[-1]) / 5
    labels, deficit = rng.normal(size=(2, m)) / 10
    direct = runtime(maps, metrics, readout, deficit, labels, inputs, m)
    state = initialize(maps, metrics, readout)
    geometric = geometric_rhs(state, inputs, labels, deficit, m)
    errors = {}
    for key in ["prediction", "kernel", "deficit_dot"]:
        errors[key] = np.max(np.abs(direct[key] - geometric[key]))
        np.testing.assert_allclose(direct[key], geometric[key], atol=2e-9, rtol=2e-9)
    for layer in range(1, len(dims)):
        embedded = np.zeros_like(geometric["selected"][layer - 1])
        embedded[state["blocks"][layer]] = direct["backwards"][layer - 1]
        expected = state["frames"][layer].T @ state["whitening"] @ embedded
        np.testing.assert_allclose(expected, geometric["selected"][layer - 1],
                                   atol=2e-9, rtol=2e-9)
        raw_velocity = np.zeros((sum(dims), sum(dims)))
        raw_velocity[state["blocks"][layer], state["blocks"][layer - 1]] = direct["maps_dot"][layer - 1]
        expected_force = (
            state["frames"][layer].T @ state["whitening"] @ raw_velocity
            @ np.linalg.inv(state["whitening"]) @ state["frames"][layer - 1]
        )
        np.testing.assert_allclose(expected_force, geometric["forces"][layer - 1],
                                   atol=2e-9, rtol=2e-9)
    step = 2e-6
    plus = initialize([a + step * da for a, da in zip(maps, direct["maps_dot"])],
                      metrics, readout + step * direct["readout_dot"])
    minus = initialize([a - step * da for a, da in zip(maps, direct["maps_dot"])],
                       metrics, readout - step * direct["readout_dot"])
    derivative_errors = []
    for layer in range(1, len(dims)):
        for field, derivative in [("grams", "gram_dot"), ("tables", "table_dot"),
                                  ("units", "unit_dot")]:
            index = layer - 1 if field == "grams" else layer
            actual = (plus[field][index] - minus[field][index]) / (2 * step)
            expected = geometric[derivative][layer - 1]
            derivative_errors.append(np.max(np.abs(actual - expected)))
            np.testing.assert_allclose(actual, expected, atol=3e-8, rtol=3e-6)
        for j in range(len(dims)):
            actual = (plus["masks"][layer][j] - minus["masks"][layer][j]) / (2 * step)
            np.testing.assert_allclose(actual, geometric["mask_dot"][layer - 1][j],
                                       atol=3e-8, rtol=3e-6)
    actual = (plus["rho"] - minus["rho"]) / (2 * step)
    np.testing.assert_allclose(actual, geometric["rho_dot"], atol=3e-8, rtol=3e-6)
    # Passive columns never enter a driving sum or the correction Gram.
    training_only = geometric_rhs(state, inputs[:, :m], labels, deficit, m)
    for field in ["gram_dot", "table_dot", "rho_dot", "deficit_dot"]:
        for a, b in zip(geometric[field], training_only[field]):
            np.testing.assert_allclose(a, b, atol=2e-10, rtol=2e-10)
    print({"widths": dims, "rank_deficient": rank_deficient,
           "maximum_identity_error": float(max(errors.values())),
           "maximum_polar_derivative_error": float(max(derivative_errors))})


if __name__ == "__main__":
    run_case([2, 3, 4], False, 17)
    run_case([2, 4, 3], True, 23)
    run_case([3, 2, 4, 3], True, 41)
    print("PASS: deterministic local identities only; not a convergence or statistical test.")
