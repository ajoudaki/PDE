"""Bounded algebra checks; no trajectory integration or scientific fitting."""

from hashlib import sha256
import json
from pathlib import Path
from time import process_time

import numpy as np

from scalar_fourier_reference import DenseReference, circle_inputs, initialize
from scalar_response_basis import ResponseBasisSystem, decode


def _active_velocity(model, state):
    values = model.unpack(model.rhs(0., state))
    return np.concatenate([values[name].ravel() if name not in ("h1", "h2", "h3")
                           else values[name][:, :model.M].ravel() for name in model.names])


def run_checks():
    start = process_time()
    U = circle_inputs([10., 125.], degrees=True).T
    query = circle_inputs([30., 60., 90.], degrees=True).T
    labels = np.array([1., -1.])
    init = initialize(16)
    dense = DenseReference(U.T, labels, init)
    rng = np.random.default_rng(631931)
    results, models, decoders = {}, {}, {}
    for rank in (4, 8, 12, 16):
        model = ResponseBasisSystem(U, labels, query, rank)
        z = model.initialize(init.w, init.W20, init.W30, init.c)
        decoder = model.detach_decoder()
        assert not hasattr(model, "decoder")
        models[rank], decoders[rank] = model, decoder
        errors = []
        for layer in (1, 2, 3):
            a = rng.normal(size=rank)
            errors.append(np.max(np.abs(model.product(layer, model.constants[layer-1], a) - a)))
        constant_error = float(max(errors))
        assert constant_error < 1e-11, constant_error
        active = ResponseBasisSystem(U, labels, None, rank)
        active_z = active.initialize(init.w, init.W20, init.W30, init.c)
        active_decoder = active.detach_decoder()
        basis_passive_error = max(float(np.max(np.abs(decoder[name] - active_decoder[name])))
                                  for name in ("Q1", "Q2", "Q3"))
        passive_error = float(np.max(np.abs(_active_velocity(model, z)
                                            - _active_velocity(active, active_z))))
        altered = model.unpack(z.copy())
        for name in ("h1", "h2", "h3"):
            altered[name][:, model.M:] += rng.normal(size=(rank, model.J - model.M))
        passive_perturbation_error = float(np.max(np.abs(
            _active_velocity(model, model.pack(altered)) - _active_velocity(model, z))))
        assert max(basis_passive_error, passive_error, passive_perturbation_error) < 1e-11
        perturb = z.copy()
        perturb[model.slices["B3"]] += .01 * rng.normal(size=rank * rank)
        nonlinear_feedback = float(np.linalg.norm(_active_velocity(model, perturb)
                                                   - _active_velocity(model, z)))
        assert nonlinear_feedback > 1e-8
        baseline = model.rhs(0., z)
        active_before_decoder_poison = active.rhs(0., active_z)
        for value in active_decoder.values():
            if isinstance(value, np.ndarray):
                value[:] = np.nan
        assert np.array_equal(active.rhs(0., active_z), active_before_decoder_poison)
        # Strict whitelist: no basis, initialization or neuron arrays survive.
        permitted_arrays = {"U", "y", "Uall", "C2", "C3", "initial"}
        actual_arrays = {key for key, value in vars(model).items() if isinstance(value, np.ndarray)}
        assert actual_arrays == permitted_arrays, actual_arrays
        assert all(t.shape == (rank, rank, rank) for t in model.products)
        assert all(e.shape == (rank,) for e in model.constants)
        assert np.array_equal(model.rhs(0., z), baseline)
        results[str(rank)] = dict(constant_product_error=constant_error,
                                  passive_basis_error=basis_passive_error,
                                  passive_rhs_error=passive_error,
                                  passive_perturbation_error=passive_perturbation_error,
                                  nonlinear_feedback_norm=nonlinear_feedback,
                                  statistics=model.statistics())
    for rank in (4, 8, 12):
        nesting_error = max(float(np.max(np.abs(decoders[rank][name]
                                                 - decoders[16][name][:, :rank])))
                            for name in ("Q1", "Q2", "Q3"))
        assert nesting_error < 1e-12, nesting_error
        results[str(rank)]["nested_basis_error"] = nesting_error

    model, decoder = models[16], decoders[16]
    initial_output_error = float(np.max(np.abs(model.outputs(model.initial)
        - dense.predict(dense.initial, model.Uall.T))))
    assert initial_output_error < 1e-12, initial_output_error
    Q1, Q2, Q3 = (decoder[name] for name in ("Q1", "Q2", "Q3"))
    fullrank_errors = []
    decoder_errors = []
    output_velocity_errors = []
    for magnitude in (0., .02):
        physical = dense.unpack(dense.initial.copy())
        for name in physical:
            physical[name] += magnitude * rng.normal(size=physical[name].shape)
        state = dense.pack(physical)
        fields = dense.query_fields(state, model.Uall.T)
        values = dict(dw=Q1.T @ (physical["w"] - init.w) / 16,
                      B2=Q2.T @ (physical["W2"] - init.W20) @ Q1 / 16,
                      B3=Q3.T @ (physical["W3"] - init.W30) @ Q2 / 16,
                      c=Q3.T @ physical["c"] / 16,
                      h1=Q1.T @ fields["h1"] / 16,
                      h2=Q2.T @ fields["h2"] / 16,
                      h3=Q3.T @ fields["h3"] / 16)
        z = model.pack(values)
        observed = model.unpack(model.rhs(0., z))
        velocity = dense.physical_velocity(state)
        response_velocity = dense.query_field_velocity(state, model.Uall.T)
        expected = dict(dw=Q1.T @ velocity["w"] / 16,
                        B2=Q2.T @ velocity["W2"] @ Q1 / 16,
                        B3=Q3.T @ velocity["W3"] @ Q2 / 16,
                        c=Q3.T @ velocity["c"] / 16,
                        h1=Q1.T @ response_velocity["h1"] / 16,
                        h2=Q2.T @ response_velocity["h2"] / 16,
                        h3=Q3.T @ response_velocity["h3"] / 16)
        error = max(float(np.max(np.abs(observed[name] - expected[name])))
                    for name in expected)
        fullrank_errors.append(error)
        decoded = decode(z, decoder)
        decoder_errors.append(max(float(np.max(np.abs(decoded[name] - physical[name])))
                                  for name in decoded))
        output_velocity_errors.append(float(np.max(np.abs(
            observed["c"] @ values["h3"] + values["c"] @ observed["h3"]
            - response_velocity["f"]))))
    assert max(fullrank_errors + decoder_errors + output_velocity_errors) < 1e-10
    # The exact activation lift has loss dissipation with canonical mobility.
    v = model.unpack(model.initial)
    dv = model.unpack(model.rhs(0., model.initial))
    residual = model.training_output(model.initial) - labels
    df = dv["c"] @ v["h3"] + v["c"] @ dv["h3"]
    actual_loss_velocity = float((2 / model.M) * np.dot(residual, df[:model.M]))
    exact_velocity = dense.physical_velocity(dense.initial)
    expected_loss_velocity = -sum(float(np.sum(value**2)) / (16 if name in ("w", "c") else 1.)
                                  for name, value in exact_velocity.items())
    assert abs(actual_loss_velocity - expected_loss_velocity) < 1e-11
    cpu_seconds = process_time() - start
    assert cpu_seconds <= 100.
    results["fullrank"] = dict(initial_output_error=initial_output_error,
                               rhs_errors=fullrank_errors, decoder_errors=decoder_errors,
                               output_velocity_errors=output_velocity_errors,
                               loss_dissipation_error=abs(actual_loss_velocity - expected_loss_velocity))
    results["cpu_seconds"] = cpu_seconds
    results["status"] = "PASS"
    results["scope"] = "algebra-only; no trajectory integration or fitting"
    results["source_sha256"] = {name: sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        for name in ("scalar_response_basis.py", "scalar_response_basis_checks.py")}
    root = Path(__file__).resolve().parents[2]
    output = root / "data/generated/neural_response_memory_20260922/scalar_variants01/basis_checks"
    output.mkdir(parents=True, exist_ok=True)
    (output / "algebra_checks.json").write_text(json.dumps(results, indent=2) + "\n")
    np.savez_compressed(output / "algebra_initial_states.npz",
                        **{f"rank{rank}": m.initial for rank, m in models.items()})
    return results


if __name__ == "__main__":
    result = run_checks()
    print(json.dumps({"status": result["status"], "cpu_seconds": result["cpu_seconds"],
                      "fullrank": result["fullrank"]}, indent=2))
