"""Independent finite-width algebra checks for the scalar Fourier compiler.

The direct oracle below is used only in validation; it is not available to the
scalar solver.  Tests deliberately use nonzero history fields so that the
denominator derivative and the history closure's velocity are exercised.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np


def direct_lifted_rhs(U, labels, W20, W30, fields, L, query_U=None):
    """Independent P=1 polynomial response lift, with column-major batches.

    fields has c[n], h1/h2/h3[n,M], A2/B2/A3/B3[n,M] and optional
    qh1/qh2/qh3[n,Q].  W1 is not needed to differentiate the lifted responses.
    """
    n, m = fields["h1"].shape
    h1, h2, h3 = (fields[f"h{k}"] for k in (1, 2, 3))
    c = fields["c"]
    A2, B2, A3, B3 = (fields[k] for k in ("A2", "B2", "A3", "B3"))
    W2 = W20 - 2.0 / (m * n * L) * A2 @ B2.T
    W3 = W30 - 2.0 / (m * n * L) * A3 @ B3.T
    f = c @ h3 / n
    r = f - labels
    rho = np.sqrt(np.mean(r * r))
    d3 = c[:, None] * (1.0 - h3 * h3)
    d2 = (1.0 - h2 * h2) * (W3.T @ d3)
    d1 = (1.0 - h1 * h1) * (W2.T @ d2)
    out = {
        "c": -2.0 / m * h3 @ r,
        "A2": d2 * r[None, :],
        "B2": rho * h1,
        "A3": d3 * r[None, :],
        "B3": rho * h2,
    }
    W1dot = -2.0 / m * (d1 * r[None, :]) @ U.T
    W2dot = -2.0 / (m * n * L) * (
        out["A2"] @ B2.T + A2 @ out["B2"].T - rho / L * A2 @ B2.T
    )
    W3dot = -2.0 / (m * n * L) * (
        out["A3"] @ B3.T + A3 @ out["B3"].T - rho / L * A3 @ B3.T
    )
    out["h1"] = (1.0 - h1 * h1) * (W1dot @ U)
    out["h2"] = (1.0 - h2 * h2) * (W2dot @ h1 + W2 @ out["h1"])
    out["h3"] = (1.0 - h3 * h3) * (W3dot @ h2 + W3 @ out["h2"])
    if query_U is not None:
        qh1, qh2, qh3 = (fields[f"qh{k}"] for k in (1, 2, 3))
        out["qh1"] = (1.0 - qh1 * qh1) * (W1dot @ query_U)
        out["qh2"] = (1.0 - qh2 * qh2) * (W2dot @ qh1 + W2 @ out["qh1"])
        out["qh3"] = (1.0 - qh3 * qh3) * (W3dot @ qh2 + W3 @ out["qh2"])
    return out, {
        "L": rho, "r": r, "rho": rho, "f": f,
        "W1dot": W1dot, "W2dot": W2dot, "W3dot": W3dot,
        "W2": W2, "W3": W3,
    }


def generic_fields(seed=441, n=3, m=2, q=16):
    rng = np.random.default_rng(seed)
    fields = {"c": rng.normal(0, 0.3, n)}
    for layer in (1, 2, 3):
        fields[f"h{layer}"] = rng.uniform(-0.7, 0.7, (n, m))
        fields[f"qh{layer}"] = rng.uniform(-0.7, 0.7, (n, q))
    for key in ("A2", "B2", "A3", "B3"):
        fields[key] = rng.normal(0, 0.2, (n, m))
    return rng, fields


def check_reference():
    from scalar_fourier_reference import (
        DenseReference, PopulationReference, circle_inputs, initialize,
    )
    rng = np.random.default_rng(119)
    U = circle_inputs([10.0, 125.0], degrees=True)
    labels = np.array([1.0, -1.0])
    init = initialize(4)
    model = PopulationReference(U, labels, init, order=1)
    values = model.unpack(model.initial.copy())
    for name in ("A2", "B2", "A3", "B3"):
        values[name] += rng.normal(0, 0.12, values[name].shape)
    values["L"] = np.array(1.7)
    state = model.pack(values)
    physical = model.physical(state)
    training = model.fields(state)
    query_U = circle_inputs(np.linspace(0, 2 * np.pi, 16, endpoint=False))
    query = model.query_fields(state, query_U)
    fields = {name: training[name] for name in ("h1", "h2", "h3")}
    fields["c"] = physical["c"]
    for name in ("A2", "B2", "A3", "B3"):
        fields[name] = values[name][0]
    for name in ("h1", "h2", "h3"):
        fields["q" + name] = query[name]
    direct, extra = direct_lifted_rhs(
        U.T, labels, init.W20, init.W30, fields, float(values["L"]), query_U.T,
    )
    reference = model.unpack(model.rhs(0.0, state))
    errors = {}
    errors["c"] = float(np.max(np.abs(direct["c"] - reference["c"])))
    for name in ("A2", "B2", "A3", "B3"):
        errors[name] = float(np.max(np.abs(direct[name] - reference[name][0])))
    physical_velocity = model.physical_velocity(state)
    for name, key in (("W1dot", "w"), ("W2dot", "W2"), ("W3dot", "W3")):
        errors[name] = float(np.max(np.abs(extra[name] - physical_velocity[key])))
    for inputs, prefix in ((U, ""), (query_U, "q")):
        derivative = model.query_field_velocity(state, inputs)
        for name in ("h1", "h2", "h3"):
            errors[prefix + name] = float(np.max(np.abs(direct[prefix + name] - derivative[name])))
    eps = 1e-6
    direction = model.rhs(0.0, state)
    plus = model.physical(state + eps * direction)
    minus = model.physical(state - eps * direction)
    errors["physical_centered_difference"] = max(
        float(np.max(np.abs((plus[k] - minus[k]) / (2 * eps) - physical_velocity[k])))
        for k in physical_velocity
    )
    dense = DenseReference(U, labels, init)
    initial_pop = model.physical_velocity(model.initial)
    initial_dense = dense.physical_velocity(dense.initial)
    errors["initial_dense_matching"] = max(
        float(np.max(np.abs(initial_pop[k] - initial_dense[k]))) for k in initial_dense
    )
    assert max(errors.values()) < 1e-7, errors
    return errors


def _compiler_fields(fields):
    from scalar_fourier_engine import field
    result = {field("c", 3): fields["c"][:, None]}
    m = fields["h1"].shape[1]
    for layer in (1, 2, 3):
        for a in range(m):
            result[field("h", layer, a)] = fields[f"h{layer}"][:, a, None]
        result[field("h", layer)] = fields[f"qh{layer}"]
    for name in ("A2", "B2", "A3", "B3"):
        for a in range(m):
            result[field(name[0], int(name[1]), a)] = fields[name][:, a, None]
    return result


def check_templates():
    from scalar_fourier_engine import DiagramEvaluator, Templates, field
    rng, fields = generic_fields()
    n, m = fields["h1"].shape
    theta = np.arange(fields["qh1"].shape[1]) * 2 * np.pi / fields["qh1"].shape[1]
    training_angles = np.deg2rad([10., 125.])
    U = np.stack((np.cos(training_angles), np.sin(training_angles)))
    query_U = np.stack((np.cos(theta), np.sin(theta)))
    labels = np.array([1., -1.])
    W20 = rng.normal(size=(n, n)) / np.sqrt(n)
    W30 = rng.normal(size=(n, n)) / np.sqrt(n)
    L = 1.4
    expected, extra = direct_lifted_rhs(U, labels, W20, W30, fields, L, query_U)
    evaluator = DiagramEvaluator(_compiler_fields(fields), W20, W30, theta)
    templates = Templates(U)
    errors, counts = {}, {}
    for name, value in expected.items():
        if name == "c":
            entries = [(field("c", 3), value[:, None])]
        elif name.startswith("qh"):
            entries = [(field("h", int(name[-1])), value)]
        else:
            entries = [(field(name[0], int(name[-1]), a), value[:, a, None]) for a in range(m)]
        for species, target in entries:
            expression = templates.rhs(species)
            actual = evaluator.expression(expression, extra["r"], extra["rho"], L)
            errors[str(species)] = float(np.max(np.abs(actual - target)))
            counts[str(species)] = len(expression)
    assert max(errors.values()) < 2e-11, errors
    return {"max_absolute_errors": errors, "template_terms": counts}


def check_compiled():
    import copy
    from scalar_fourier_engine import (
        DiagramEvaluator, ScalarFourierSystem, canonical, field, node, has_query, size,
    )
    from scalar_fourier_reference import initialize
    angles = np.deg2rad([10., 125.])
    U = np.stack((np.cos(angles), np.sin(angles)))
    model = ScalarFourierSystem(U, np.array([1., -1.]), K=5, J=2)
    rng, fields = generic_fields(q=32)
    n = fields["c"].size
    W20 = rng.normal(size=(n, n)) / np.sqrt(n)
    W30 = rng.normal(size=(n, n)) / np.sqrt(n)
    theta = np.arange(32) * 2 * np.pi / 32
    ev = DiagramEvaluator(_compiler_fields(fields), W20, W30, theta)
    weights = np.stack((np.ones(32), np.cos(theta), np.sin(theta),
                        np.cos(2 * theta), np.sin(2 * theta)), axis=1)
    z = np.zeros(model.dimension)
    z[:model.ntrain] = [ev.tree(t)[0] for t in model.training_patterns]
    Q = z[model.ntrain:-1].reshape(model.nangular, model.nweights)
    for index, pattern in enumerate(model.angular_patterns):
        Q[index] = ev.angular_integrand(pattern) @ weights / 32
    z[-1] = 1.4
    r = model.training_output(z) - model.y
    rho = np.sqrt(np.mean(r * r))
    actual = model.rhs(0., z)
    direct = np.zeros_like(z)
    direct_Q = direct[model.ntrain:-1].reshape(Q.shape)
    for angular, rows in ((False, model.training_rows), (True, model.angular_rows)):
        for row_index, row in enumerate(rows):
            for coefficient, train_indices, angle_index, drive, power in row:
                term = coefficient / z[-1] ** power
                term *= rho if drive == -1 else r[drive] if drive >= 0 else 1.
                for factor in train_indices:
                    term *= z[factor]
                if angular:
                    direct_Q[row_index] += term * Q[angle_index]
                else:
                    direct[row_index] += term
    direct[-1] = rho
    all_rows_error = float(np.max(np.abs(actual - direct)))
    assert all_rows_error < 2e-11

    # Rebuild output product rules independently of _compile_row.  Decide each
    # entire monomial's retention from its actual connected components, then
    # evaluate it directly on neuron fields before angular integration.
    oracle, extras = direct_lifted_rhs(U, model.y, W20, W30, fields, z[-1],
                                     np.stack((np.cos(theta), np.sin(theta))))
    row_errors, full_errors, omitted_counts = {}, {}, {}
    for sample in (0, 1, -1):
        angular = sample == -1
        total = np.zeros(32)
        retained = np.zeros(32)
        omitted = 0
        for species, remaining in ((field("c", 3), field("h", 3, sample)),
                                   (field("h", 3, sample), field("c", 3))):
            for (root, forest, cc, ss, drive, power), coefficient in model.templates.rhs(species).items():
                joined = node(root[0], root[1] + (remaining,), root[2])
                components = (joined,) + forest
                angle_components = tuple(t for t in components if has_query(t))
                train_components = tuple(t for t in components if not has_query(t))
                keep = all(size(t) <= model.K for t in train_components)
                if angular:
                    keep = keep and 2 + cc + ss + sum(size(t) for t in angle_components) <= model.K
                else:
                    assert not angle_components and cc == ss == 0
                value = np.full(32, coefficient / z[-1] ** power)
                value *= rho if drive == -1 else r[drive] if drive >= 0 else 1.
                value *= np.cos(theta) ** cc * np.sin(theta) ** ss
                for tree in components:
                    value *= ev.tree(tree)
                total += value
                if keep:
                    retained += value
                else:
                    omitted += 1
        if angular:
            expected_full = (oracle["c"] @ fields["qh3"] + fields["c"] @ oracle["qh3"]) / n
            expected_cut = actual[model.ntrain:-1].reshape(Q.shape)[model.angular_output_index]
            row_errors[str(sample)] = float(np.max(np.abs(retained @ weights / 32 - expected_cut)))
        else:
            expected_full = (oracle["c"] @ fields["h3"][:, sample]
                             + fields["c"] @ oracle["h3"][:, sample]) / n
            row_errors[str(sample)] = float(abs(retained[0] - actual[model.output_indices[sample]]))
        full_errors[str(sample)] = float(np.max(np.abs(total - expected_full)))
        omitted_counts[str(sample)] = omitted
    assert max(row_errors.values()) < 2e-11, row_errors
    assert max(full_errors.values()) < 2e-11, full_errors
    assert min(omitted_counts.values()) > 0

    # Same angle is retained for disconnected neuron components.
    qtree = canonical(node(1, [field("h", 1)]))
    old = fields["qh1"]
    fields["qh1"] = np.broadcast_to(np.cos(theta), old.shape)
    angle_ev = DiagramEvaluator(_compiler_fields(fields), W20, W30, theta)
    joint = float(np.mean(angle_ev.angular_integrand(((qtree, qtree), 0, 0))))
    separate = float(np.mean(angle_ev.tree(qtree)) ** 2)
    assert abs(joint - 0.5) < 1e-14 and abs(separate) < 1e-14
    fields["qh1"] = old

    # An edge average uses the actual matrix with the exact 1/n factor.
    edge = node(2, [field("A", 2, 0)], [node(1, [field("B", 2, 1)])])
    edge_value = float(ev.tree(edge)[0])
    edge_direct = float(fields["A2"][:, 0] @ W20 @ fields["B2"][:, 1] / n)
    assert abs(edge_value - edge_direct) < 1e-13

    # No compiler, diagram list, physical input array or neuron field is needed
    # for evaluation of the finite scalar ODE after initialization.
    runtime = copy.copy(model)
    for key in ("templates", "U", "training_patterns", "angular_patterns",
                "training_index", "angular_index", "training_rows", "angular_rows"):
        delattr(runtime, key)
    autonomy_error = float(np.max(np.abs(runtime.rhs(0., z) - actual)))
    assert autonomy_error == 0.
    stationary = z.copy()
    stationary[model.output_indices] = model.y
    stationarity = float(np.max(np.abs(runtime.rhs(0., stationary))))
    assert stationarity == 0.

    # Initialization quadrature is separate from runtime and can be refined.
    init = initialize(4)
    z256 = model.initialize(init.w, init.W20, init.W30, init.c, quadrature=256)
    z512 = model.initialize(init.w, init.W20, init.W30, init.c, quadrature=512)
    quad_error = float(np.max(np.abs(z256 - z512)))
    q0 = model.fourier_coefficients(z512)
    qdot = model.fourier_coefficients(model.rhs(0., z512))
    even_error = float(max(np.max(np.abs(q0[[0, 3, 4]])),
                           np.max(np.abs(qdot[[0, 3, 4]]))))
    assert quad_error < 1e-10 and even_error < 1e-12
    nstate = model.dimension
    other_init = initialize(7)
    other_z = model.initialize(other_init.w, other_init.W20, other_init.W30, other_init.c, 256)
    assert other_z.size == nstate
    return dict(all_compiled_rows_max_error=all_rows_error,
                independent_retained_output_row_errors=row_errors,
                independent_full_output_row_errors=full_errors,
                whole_monomial_omission_counts=omitted_counts,
                same_angle_cosine_square=joint, incorrectly_factored_value=separate,
                initialized_edge_error=abs(edge_value - edge_direct),
                autonomy_error=autonomy_error, zero_residual_max_velocity=stationarity,
                quadrature_256_to_512_max_error=quad_error,
                even_output_mode_and_velocity_max_error=even_error,
                width_independent_dimension=nstate, statistics=model.statistics())


def main():
    import argparse
    import hashlib
    parser = argparse.ArgumentParser()
    default = Path(__file__).resolve().parents[2] / "data/generated/neural_response_memory_20260922/scalar_fourier01/algebra_checks.json"
    parser.add_argument("--output", type=Path, default=default)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f"Refusing to overwrite existing evidence: {args.output}")
    started = time.process_time()
    result = {
        "status": "PASS",
        "scope": "finite-width algebra and implementation checks; no training accuracy claim",
        "reference": check_reference(),
        "exact_templates": check_templates(),
        "finite_compiler": check_compiled(),
    }
    result["cpu_seconds"] = time.process_time() - started
    result["source_sha256"] = {
        name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ("scalar_fourier_engine.py", "scalar_fourier_reference.py", "check_scalar_fourier.py")
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as evidence:
        evidence.write(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "cpu_seconds": result["cpu_seconds"],
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
