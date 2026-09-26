"""Independent migration/algebra audit; deliberately never integrates a trajectory.

Run with Python after scalar_ode.py and its circle_task helper are finalized.
The old sources are comparison inputs, not dependencies of scalar_ode.py.
"""

import ast
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import sys
from time import process_time
import traceback

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[1] / "data/generated/neural_response_memory_20260922/scalar_standalone01/checks"
CPU_CAP = 30.0


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def difference(left, right):
    left, right = np.asarray(left), np.asarray(right)
    if left.shape != right.shape:
        raise AssertionError((left.shape, right.shape))
    if not np.isfinite(left).all() or not np.isfinite(right).all():
        raise AssertionError("Nonfinite audit quantity")
    return float(np.max(np.abs(left - right))) if left.size else 0.0


def checked(error, tolerance=1e-11):
    if not np.isfinite(error) or error > tolerance:
        raise AssertionError(dict(error=float(error), tolerance=tolerance))
    return float(error)


def directions(angles):
    theta = np.deg2rad(np.asarray(angles, dtype=float))
    return np.vstack((np.cos(theta), np.sin(theta)))


def forward(weights, U):
    """Independent physical network calculation, with columns as inputs."""
    h1 = np.tanh(weights["w"] @ U)
    h2 = np.tanh(weights["W2"] @ h1)
    h3 = np.tanh(weights["W3"] @ h2)
    return dict(h1=h1, h2=h2, h3=h3, f=weights["c"] @ h3 / weights["c"].size)


def active(model, state):
    values = model.unpack(state)
    return np.concatenate([values[key][:, :model.M].ravel()
                           if key in ("h1", "h2", "h3") else values[key].ravel()
                           for key in model.names])


def independent_loss(state, width, U, labels):
    offset, weights = 0, {}
    for name, shape in (("w", (width, 2)), ("W2", (width, width)),
                        ("W3", (width, width)), ("c", (width,))):
        length = int(np.prod(shape))
        weights[name] = state[offset:offset + length].reshape(shape)
        offset += length
    assert offset == len(state)
    return float(np.mean((forward(weights, U)["f"] - labels)**2))


def task_checks(new):
    specifications = {
        "two_point": (np.array([10., 125.]), np.array([1., -1.])),
        "close_pairs": (np.array([-1., 1., 59., 61., 119., 121.]),
                        np.array([-1., 1., 1., -1., -1., 1.])),
        "quadrant_alternating": (5. + 10. * np.arange(8), (-1.)**np.arange(8)),
        "harmonic3_full": (7. + 30. * np.arange(12), None),
        "harmonic5_full": (7. + 22.5 * np.arange(16), None),
        "harmonic5_arc": (10. + 10. * np.arange(8), None),
    }
    results = {}
    for name, (angles, labels) in specifications.items():
        frequency = 3 if name == "harmonic3_full" else 5
        if labels is None:
            labels = np.sqrt(2.) * np.sin(frequency * np.deg2rad(angles))
        task = new.circle_task(name)
        errors = [difference(task["angles"], angles), difference(task["U"], directions(angles)),
                  difference(task["y"], labels)]
        checked(max(errors))
        checked(abs(float(np.mean(labels**2)) - 1.))
        antipodal_pairs = 0
        for j in range(len(angles)):
            for k in range(j):
                if np.linalg.norm(task["U"][:, j] + task["U"][:, k]) < 1e-12:
                    checked(abs(labels[j] + labels[k]))
                    antipodal_pairs += 1
        if name in ("two_point", "quadrant_alternating"):
            assert task["target_kind"] is None, (name, task["target_kind"])
        if name == "close_pairs":
            exact = np.tanh(3 * np.sin(3 * np.deg2rad(angles))
                            / np.sin(np.deg2rad(3.))) / np.tanh(3.)
            checked(difference(labels, exact))
        results[name] = dict(input_label_error=max(errors), training_rms=float(np.sqrt(np.mean(labels**2))),
                             antipodal_pairs=antipodal_pairs, target_kind=task["target_kind"])
    return results


def dense_checks(new, old, rng):
    n, U, y = 7, directions([10., 77., 125.]), np.array([1., -.6, -1.])
    initial = new.initialize(n, seed=20260920)
    reference = old.initialize(n, seed=20260920)
    init_error = max(difference(getattr(initial, key), getattr(reference, key))
                     for key in ("w", "W20", "W30", "c"))
    checked(init_error, 0.)
    dense = new.DenseReference(U.T, y, initial)
    prior = old.DenseReference(U.T, y, reference)
    checked(difference(dense.initial, prior.initial), 0.)
    checked(difference(new.circle_inputs([10., 77., 125.], degrees=True), U.T))
    mobility = np.concatenate((np.full(2 * n, n), np.ones(2 * n * n), np.full(n, n)))
    migration, gradient = [], []
    for magnitude in (0., .07):
        state = dense.initial + magnitude * rng.normal(size=dense.dimension)
        velocity = dense.rhs(0., state)
        migration.append(checked(difference(velocity, prior.rhs(0., state))))
        gradient_vector = -velocity / mobility
        for _ in range(5):
            direction = rng.normal(size=dense.dimension)
            direction /= np.linalg.norm(direction)
            epsilon = 2e-6
            numeric = (independent_loss(state + epsilon * direction, n, U, y)
                       - independent_loss(state - epsilon * direction, n, U, y)) / (2 * epsilon)
            gradient.append(checked(abs(numeric - np.dot(gradient_vector, direction)), 2e-8))
    return dict(initialization_error=init_error, rhs_errors=migration,
                independent_directional_gradient_errors=gradient)


def scalar_checks(new, old, old_reference, rng):
    n, U, y = 16, directions([10., 77., 125.]), np.array([1., -.6, -1.])
    query = directions([12.5, 57.5, 102.5, 157.5])
    initial = new.initialize(n, seed=20260920)
    dense = new.DenseReference(U.T, y, initial)
    models, decoders, results = {}, {}, {}
    for rank in (1, 4, 8, 12, 16):
        model = new.ResponseBasisSystem(U, y, query, rank)
        prior = old.ResponseBasisSystem(U, y, query, rank)
        args = (initial.w, initial.W20, initial.W30, initial.c)
        z, prior_z = model.initialize(*args), prior.initialize(*args)
        decoder, prior_decoder = model.detach_decoder(), prior.detach_decoder()
        assert not hasattr(model, "decoder")
        models[rank], decoders[rank] = model, decoder
        errors = [difference(z, prior_z)]
        errors.extend(difference(getattr(model, key), getattr(prior, key)) for key in ("C2", "C3"))
        errors.extend(difference(a, b) for a, b in zip(model.products, prior.products))
        errors.extend(difference(a, b) for a, b in zip(model.constants, prior.constants))
        errors.extend(difference(decoder[key], prior_decoder[key]) for key in decoder)
        checked(max(errors))
        state_errors, decoder_errors, dissipations = [], [], []
        for magnitude in (0., .03, .10):
            state = z + magnitude * rng.normal(size=model.dimension)
            velocity = model.rhs(0., state)
            state_errors.append(checked(difference(velocity, prior.rhs(0., state))))
            decoded, original = new.decode(state, decoder), old.decode(state, prior_decoder)
            decoder_errors.append(checked(max(difference(decoded[key], original[key]) for key in decoded)))
            v, dv = model.unpack(state), model.unpack(velocity)
            residual = v["c"] @ v["h3"][:, :model.M] - y
            df = dv["c"] @ v["h3"][:, :model.M] + v["c"] @ dv["h3"][:, :model.M]
            actual = 2 * np.dot(residual, df) / model.M
            expected = -sum(float(np.sum(dv[key]**2)) for key in ("dw", "B2", "B3", "c"))
            dissipations.append(checked(abs(actual - expected) / max(1., abs(expected)), 2e-10))
        only = new.ResponseBasisSystem(U, y, None, rank)
        only_z = only.initialize(*args)
        only_decoder = only.detach_decoder()
        basis_error = checked(max(difference(decoder[key], only_decoder[key]) for key in ("Q1", "Q2", "Q3")))
        passive_error = checked(difference(active(model, model.rhs(0., z)), active(only, only.rhs(0., only_z))))
        perturbed = z + .03 * rng.normal(size=model.dimension)
        altered = model.unpack(perturbed.copy())
        for key in ("h1", "h2", "h3"):
            altered[key][:, model.M:] += rng.normal(size=(rank, model.J - model.M))
        passive_nonzero_error = checked(difference(active(model, model.rhs(0., perturbed)),
                                                    active(model, model.rhs(0., model.pack(altered)))))
        before = only.rhs(0., only_z)
        for value in only_decoder.values():
            if isinstance(value, np.ndarray):
                value[:] = np.nan
        checked(difference(before, only.rhs(0., only_z)), 0.)
        allowed = {"U", "y", "Uall", "C2", "C3", "initial"}
        present = {key for key, value in vars(model).items() if isinstance(value, np.ndarray)}
        assert present == allowed, present
        assert all(value.shape == (rank, rank, rank) for value in model.products)
        assert all(value.shape == (rank,) for value in model.constants)
        results[str(rank)] = dict(coefficient_error=max(errors), rhs_errors=state_errors,
                                  decoder_errors=decoder_errors, relative_loss_dissipation_errors=dissipations,
                                  passive_basis_error=basis_error, passive_initial_rhs_error=passive_error,
                                  passive_nonzero_rhs_error=passive_nonzero_error,
                                  detached_decoder_poison_error=0., runtime_array_whitelist=sorted(present))
    for rank in (1, 4, 8, 12):
        results[str(rank)]["nested_basis_error"] = checked(max(
            difference(decoders[rank][key], decoders[16][key][:, :rank]) for key in ("Q1", "Q2", "Q3")))
    model, decoder = models[16], decoders[16]
    Q1, Q2, Q3 = (decoder[key] for key in ("Q1", "Q2", "Q3"))
    fullrank = []
    for magnitude in (0., .02, .07):
        state = dense.initial + magnitude * rng.normal(size=dense.dimension)
        weights = dense.unpack(state)
        fields = forward(weights, model.Uall)
        lift = dict(dw=Q1.T @ (weights["w"] - initial.w) / n,
                    B2=Q2.T @ (weights["W2"] - initial.W20) @ Q1 / n,
                    B3=Q3.T @ (weights["W3"] - initial.W30) @ Q2 / n,
                    c=Q3.T @ weights["c"] / n,
                    h1=Q1.T @ fields["h1"] / n, h2=Q2.T @ fields["h2"] / n,
                    h3=Q3.T @ fields["h3"] / n)
        lifted = model.pack(lift)
        dv = dense.unpack(dense.rhs(0., state))
        dh1 = (1 - fields["h1"]**2) * (dv["w"] @ model.Uall)
        dh2 = (1 - fields["h2"]**2) * (dv["W2"] @ fields["h1"] + weights["W2"] @ dh1)
        dh3 = (1 - fields["h3"]**2) * (dv["W3"] @ fields["h2"] + weights["W3"] @ dh2)
        expected = dict(dw=Q1.T @ dv["w"] / n, B2=Q2.T @ dv["W2"] @ Q1 / n,
                        B3=Q3.T @ dv["W3"] @ Q2 / n, c=Q3.T @ dv["c"] / n,
                        h1=Q1.T @ dh1 / n, h2=Q2.T @ dh2 / n, h3=Q3.T @ dh3 / n)
        rhs_error = checked(difference(model.rhs(0., lifted), model.pack(expected)), 2e-10)
        decoded = new.decode(lifted, decoder)
        decode_error = checked(max(difference(decoded[key], weights[key]) for key in decoded), 2e-10)
        output_error = checked(difference(model.outputs(lifted), fields["f"]), 2e-10)
        fullrank.append(dict(magnitude=magnitude, rhs_error=rhs_error, decoder_error=decode_error,
                             output_error=output_error))
    return dict(ranks=results, fullrank=fullrank)


def population_checks(new, old, rng):
    """Check original P1/P3 transport and any bundled copies, without fitting."""
    U, y, initial = directions([10., 77., 125.]), np.array([1., -.6, -1.]), old.initialize(7)
    dense = old.DenseReference(U.T, y, initial)
    results = {}
    for order in (1, 3):
        model = old.PopulationReference(U.T, y, initial, order=order)
        initial_error = checked(max(difference(model.physical_velocity(model.initial)[key],
                                               dense.physical_velocity(dense.initial)[key])
                                    for key in ("w", "W2", "W3", "c")))
        moment = rng.normal(size=(order, 7, y.size))
        source = rng.normal(size=(7, y.size))
        rho, length = .7, 1.4
        explicit = np.empty_like(moment)
        for k in range(order):
            lower = sum(((2 * j + 1) * moment[j] for j in range(k)), np.zeros_like(source))
            explicit[k] = source - rho / length * (k * moment[k] + lower)
        transport_error = checked(difference(model.transport(moment, source, rho, length), explicit))
        state = model.initial + .02 * rng.normal(size=model.dimension)
        state[model.slices["L"]] = 1.3
        velocity = model.rhs(0., state)
        epsilon = 1e-6
        plus, minus = model.physical(state + epsilon * velocity), model.physical(state - epsilon * velocity)
        analytic = model.physical_velocity(state)
        reconstruction_error = checked(max(difference((plus[key] - minus[key]) / (2 * epsilon), analytic[key])
                                             for key in analytic), 2e-8)
        migration = None
        if hasattr(new, "PopulationReference"):
            copy = new.PopulationReference(U.T, y, new.initialize(7), order=order)
            migration = checked(max(difference(copy.initial, model.initial),
                                    difference(copy.rhs(0., state), velocity)))
        results[str(order)] = dict(initial_dense_velocity_error=initial_error,
                                   explicit_moment_transport_error=transport_error,
                                   reconstruction_derivative_error=reconstruction_error,
                                   standalone_migration_error=migration)
    return results


def run_checks():
    start = process_time()
    results = dict(scope="Algebra and task generation only; no trajectory integration or fitting")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    try:
        new = load("audited_scalar_ode", "scalar_ode.py")
        old = load("audit_old_basis", "scalar_response_basis.py")
        reference = load("audit_old_reference", "scalar_fourier_reference.py")
        tree = ast.parse((HERE / "scalar_ode.py").read_text())
        imports = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
        imports += [alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names]
        assert not any(name and name.startswith("scalar_") for name in imports), imports
        rng = np.random.default_rng(917631931)
        for name, check in (("tasks", lambda: task_checks(new)),
                            ("dense", lambda: dense_checks(new, reference, rng)),
                            ("scalar", lambda: scalar_checks(new, old, reference, rng)),
                            ("population", lambda: population_checks(new, reference, rng))):
            results[name] = check()
            if process_time() - start > CPU_CAP:
                raise TimeoutError("Independent audit exceeded 30 CPU seconds")
        results["status"] = "PASS"
    except Exception as exc:
        results.update(status="FAIL", error=repr(exc), traceback=traceback.format_exc())
    results["cpu_seconds"] = process_time() - start
    results["cpu_cap_seconds"] = CPU_CAP
    filenames = ("scalar_ode.py", "scalar_response_basis.py", "scalar_fourier_reference.py",
                 "check_scalar_standalone.py", "SCALAR_STANDALONE_PROTOCOL.md")
    results["source_sha256"] = {name: sha256((HERE / name).read_bytes()).hexdigest()
                                for name in filenames if (HERE / name).exists()}
    results["environment"] = dict(python=sys.version, numpy=np.__version__,
                                  threads={key: os.environ.get(key) for key in
                                           ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")})
    (OUTPUT / "independent_algebra.json").write_text(json.dumps(results, indent=2) + "\n")
    return results


if __name__ == "__main__":
    result = run_checks()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)
