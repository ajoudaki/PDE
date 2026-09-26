"""Bounded initialization/local algebra checks; no training trajectory is run."""
import argparse
import json
from pathlib import Path
from time import process_time

import numpy as np

from scalar_fourier_reference import DenseReference, circle_inputs, initialize
from scalar_polynomial_potential import (
    PolynomialPotentialSystem, _pack, mobility_sqrt, output_gradient_hvp,
)


def checks():
    started = process_time()
    initial = initialize(16, 20260920)
    U = circle_inputs([10., 125.], degrees=True).T
    Utest = circle_inputs([30., 60., 90.], degrees=True).T
    y = np.array([1., -1.])
    dense = DenseReference(U.T, y, initial)
    theta0 = dense.initial
    sqrtD = mobility_sqrt(16)
    rng = np.random.default_rng(31709)
    direction = rng.normal(size=theta0.size)
    direction /= np.linalg.norm(direction)
    step = 1e-5
    hvp_error, gradient_error = 0., 0.
    for u in np.column_stack((U, Utest)).T:
        value, gradient, hvp = output_gradient_hvp(theta0, 16, u, sqrtD*direction)
        plus = output_gradient_hvp(theta0+step*sqrtD*direction, 16, u)
        minus = output_gradient_hvp(theta0-step*sqrtD*direction, 16, u)
        gradient_error = max(gradient_error, abs((plus[0]-minus[0])/(2*step)
                                                -np.dot(sqrtD*gradient, direction)))
        hvp_error = max(hvp_error, float(np.max(np.abs(
            sqrtD*(plus[1]-minus[1])/(2*step)-sqrtD*hvp))))
    if gradient_error > 1e-8 or hvp_error > 1e-7:
        raise AssertionError((gradient_error, hvp_error))

    active_grads = np.array([sqrtD*output_gradient_hvp(theta0, 16, u)[1] for u in U.T])
    residual0 = dense.predict(theta0, U.T)-y
    whitened_velocity = -(2/len(y))*(residual0 @ active_grads)
    mobility_error = float(np.max(np.abs(sqrtD*whitened_velocity-dense.rhs(0., theta0))))
    active_hvp = np.array([sqrtD*output_gradient_hvp(theta0, 16, u,
                                        sqrtD*whitened_velocity)[2] for u in U.T])
    whitened_acceleration = -(2/len(y))*(
        (active_grads @ whitened_velocity) @ active_grads + residual0 @ active_hvp)
    expected_first, expected_second = [], []
    all_inputs = np.column_stack((U, Utest)).T
    for u in all_inputs:
        _, gradient, hvp = output_gradient_hvp(theta0, 16, u, sqrtD*whitened_velocity)
        expected_first.append(np.dot(sqrtD*gradient, whitened_velocity))
        expected_second.append(np.dot(sqrtD*gradient, whitened_acceleration)
                               +np.dot(whitened_velocity, sqrtD*hvp))
    variants = {}
    for mode, degree in (("gradient", 1), ("gradient", 2),
                         ("curvature", 2), ("curvature", 3)):
        model = PolynomialPotentialSystem(U, y, Utest, mode, degree)
        z0 = model.initialize(initial.w, initial.W20, initial.W30, initial.c)
        decoder = model.__dict__.pop("decoder")
        z = rng.normal(size=model.dimension)*.1
        gradients = model.output_gradients(z)
        residual = model.training_output(z)-y
        velocity = model.rhs(0., z)
        loss_derivative = (2/len(y))*residual @ (gradients[:len(y)] @ velocity)
        loss_identity_error = abs(loss_derivative+np.dot(velocity, velocity))
        finite_gradients = np.column_stack([
            (model.outputs(z+step*np.eye(model.dimension)[k])
             -model.outputs(z-step*np.eye(model.dimension)[k]))/(2*step)
            for k in range(model.dimension)])
        gradient_table_error = float(np.max(np.abs(gradients-finite_gradients)))
        initial_output_error = float(np.max(np.abs(model.outputs(z0)-dense.predict(theta0, all_inputs))))
        first_error = float(np.max(np.abs(model.output_gradients(z0) @ model.rhs(0., z0)
                                          -expected_first)))
        g0 = model.output_gradients(z0)
        v0 = model.rhs(0., z0)
        hessian_times_v = (model.output_gradients(step*v0)-model.output_gradients(-step*v0))/(2*step)
        acceleration = -(2/len(y))*((g0[:len(y)] @ v0) @ g0[:len(y)]
                                    + residual0 @ hessian_times_v[:len(y)])
        second_error = float(np.max(np.abs(g0 @ acceleration+hessian_times_v @ v0
                                           -expected_second)))
        Q = decoder["parameter_directions"]/sqrtD[:, None]
        local_direction = rng.normal(size=model.dimension)
        local_direction /= np.linalg.norm(local_direction)
        small = .005*local_direction
        local_state = theta0+decoder["parameter_directions"] @ small
        jet_output_error = float(np.max(np.abs(model.outputs(small)-dense.predict(local_state, all_inputs))))
        cubic_error = None
        if degree == 3:
            h = .002
            values = [dense.predict(theta0+decoder["parameter_directions"] @ (a*h*local_direction), all_inputs)
                      for a in (2, 1, -1, -2)]
            expected_third = (values[0]-2*values[1]+2*values[2]-values[3])/(2*h**3)
            poly_values = [model.outputs(a*h*local_direction) for a in (2, 1, -1, -2)]
            actual_third = (poly_values[0]-2*poly_values[1]+2*poly_values[2]-poly_values[3])/(2*h**3)
            cubic_error = float(np.max(np.abs(expected_third-actual_third)))
            if cubic_error > 2e-4:
                raise AssertionError(("cubic coefficient", cubic_error))

        # A duplicate training query and an unrelated passive query cannot alter
        # active coefficients or the basis. The duplicate output is identical.
        comparison = PolynomialPotentialSystem(U, y, np.column_stack((U[:, 0], Utest[:, 2])), mode, degree)
        comparison.initialize(initial.w, initial.W20, initial.W30, initial.c)
        other_decoder = comparison.__dict__.pop("decoder")
        passive_independence_error = max(
            float(np.max(np.abs(comparison.coefficients[:len(y)]-model.coefficients[:len(y)]))),
            float(np.max(np.abs(other_decoder["parameter_directions"]-decoder["parameter_directions"]))),
            float(np.max(np.abs(comparison.rhs(0., z)-model.rhs(0., z)))))
        duplicate_error = float(np.max(np.abs(comparison.coefficients[0]-comparison.coefficients[len(y)])))
        decoded0 = model.decode(z0, decoder)
        decoder_error = float(np.max(np.abs(_pack(tuple(decoded0[k] for k in ("w", "W2", "W3", "c")))-theta0)))
        # Runtime must work without initialization inputs, the decoder, or basis.
        saved = {key: model.__dict__.pop(key) for key in ("U", "Utest")}
        stripped_error = float(np.max(np.abs(model.rhs(0., z)-velocity)))
        model.__dict__.update(saved)
        if (mobility_error > 1e-12 or initial_output_error > 1e-12 or first_error > 1e-11
                or loss_identity_error > 1e-11 or gradient_table_error > 1e-8
                or passive_independence_error > 1e-12 or duplicate_error > 1e-12
                or decoder_error > 1e-12 or stripped_error != 0
                or (mode == "curvature" and second_error > 1e-9)):
            raise AssertionError((mode, degree, locals()))
        variants[f"{mode}_degree{degree}"] = dict(
            **model.statistics(), initial_output_error=initial_output_error,
            initial_velocity_error=first_error, initial_second_derivative_error=second_error,
            gradient_table_error=gradient_table_error, loss_dissipation_error=loss_identity_error,
            local_jet_output_error=jet_output_error, cubic_derivative_fd_error=cubic_error,
            passive_independence_error=passive_independence_error, duplicate_input_error=duplicate_error,
            decoder_initial_error=decoder_error, stripped_runtime_error=stripped_error)
        if process_time()-started > 100.:
            raise TimeoutError("Potential algebra checks exceeded 100 CPU seconds")
    return dict(status="PASS", cpu_seconds=process_time()-started,
                mobility_velocity_error=mobility_error, gradient_fd_error=gradient_error,
                whitened_hvp_fd_error=hvp_error, variants=variants)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = checks()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result, indent=2))
