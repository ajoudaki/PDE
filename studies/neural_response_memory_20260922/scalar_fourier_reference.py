"""Float64 dense and history-population references for scalar Fourier tests.

Three hidden tanh layers, normalized circle inputs, f=c@h3/n, mean squared
loss, and parameter mobilities (n,1,1,n). These are validation solvers, not
the scalar closure: they deliberately retain neuron fields and matrices.
"""

from dataclasses import dataclass
from time import perf_counter

import numpy as np
from scipy.integrate import solve_ivp


@dataclass(frozen=True)
class Initialization:
    w: np.ndarray
    W20: np.ndarray
    W30: np.ndarray
    c: np.ndarray

    @property
    def width(self):
        return self.c.size


def initialize(width, seed=20260920):
    """Canonical sequential NumPy draws; supplied inputs already include 1/sqrt(d)."""
    if not isinstance(width, (int, np.integer)) or width < 1:
        raise ValueError("width must be a positive integer")
    rng = np.random.default_rng(seed)
    return Initialization(
        rng.standard_normal((width, 2)),
        rng.standard_normal((width, width)) / np.sqrt(width),
        rng.standard_normal((width, width)) / np.sqrt(width),
        rng.standard_normal(width) / width,
    )


def circle_inputs(angles, *, degrees=False):
    angles = np.asarray(angles, dtype=np.float64)
    if degrees:
        angles = np.deg2rad(angles)
    return np.column_stack((np.cos(angles), np.sin(angles)))


class DenseReference:
    """Canonical three-hidden-layer physical gradient flow."""

    kind = "dense"

    def __init__(self, inputs, labels, initialization):
        self.inputs = np.asarray(inputs, dtype=np.float64).copy()
        self.labels = np.asarray(labels, dtype=np.float64).copy()
        self.initialization = initialization
        self.n = initialization.width
        if self.inputs.ndim != 2 or self.inputs.shape[1] != 2:
            raise ValueError("inputs must have shape (M,2)")
        self.M = self.inputs.shape[0]
        if self.M == 0 or self.labels.shape != (self.M,):
            raise ValueError("labels must have shape (M,), M>0")
        if not all(np.isfinite(a).all() for a in (self.inputs, self.labels)):
            raise ValueError("nonfinite inputs or labels")
        self.names = ("w", "W2", "W3", "c")
        self.shapes = ((self.n, 2), (self.n, self.n), (self.n, self.n), (self.n,))
        self._set_slices()
        self.initial = self.pack(dict(w=initialization.w, W2=initialization.W20,
                                      W3=initialization.W30, c=initialization.c))

    def _set_slices(self):
        sizes = [int(np.prod(shape)) for shape in self.shapes]
        endpoints = np.cumsum([0] + sizes)
        self.slices = {name: slice(start, end) for name, start, end in
                       zip(self.names, endpoints[:-1], endpoints[1:])}
        self.dimension = int(endpoints[-1])

    def pack(self, values):
        return np.concatenate([np.asarray(values[name], dtype=np.float64).ravel()
                               for name in self.names])

    def unpack(self, state):
        state = np.asarray(state, dtype=np.float64)
        if state.shape != (self.dimension,):
            raise ValueError("state has wrong shape")
        return {name: state[self.slices[name]].reshape(shape)
                for name, shape in zip(self.names, self.shapes)}

    def physical(self, state):
        return self.unpack(state)

    def query_fields(self, state, inputs):
        weights = self.physical(state)
        inputs = np.asarray(inputs, dtype=np.float64)
        h1 = np.tanh(weights["w"] @ inputs.T)
        h2 = np.tanh(weights["W2"] @ h1)
        h3 = np.tanh(weights["W3"] @ h2)
        f = weights["c"] @ h3 / self.n
        return dict(h1=h1, h2=h2, h3=h3, f=f)

    def predict(self, state, inputs):
        return self.query_fields(state, inputs)["f"]

    def query_field_velocity(self, state, inputs):
        """Exact passive response chain rule from current physical velocities."""
        inputs = np.asarray(inputs, dtype=np.float64)
        weights = self.physical(state)
        velocity = self.physical_velocity(state)
        values = self.query_fields(state, inputs)
        dh1 = (1 - values["h1"]**2) * (velocity["w"] @ inputs.T)
        dh2 = (1 - values["h2"]**2) * (velocity["W2"] @ values["h1"] + weights["W2"] @ dh1)
        dh3 = (1 - values["h3"]**2) * (velocity["W3"] @ values["h2"] + weights["W3"] @ dh2)
        df = (velocity["c"] @ values["h3"] + weights["c"] @ dh3) / self.n
        return dict(h1=dh1, h2=dh2, h3=dh3, f=df)

    def fields(self, state):
        weights = self.physical(state)
        values = self.query_fields(state, self.inputs)
        residual = values["f"] - self.labels
        loss = float(np.mean(residual**2))
        delta3 = weights["c"][:, None] * (1 - values["h3"]**2)
        delta2 = (1 - values["h2"]**2) * (weights["W3"].T @ delta3)
        delta1 = (1 - values["h1"]**2) * (weights["W2"].T @ delta2)
        values.update(r=residual, loss=loss, rho=np.sqrt(loss), delta1=delta1,
                      delta2=delta2, delta3=delta3)
        return values

    def rhs(self, time, state):
        del time
        f = self.fields(state)
        return self.pack(dict(
            w=(-2 / self.M) * ((f["delta1"] * f["r"]) @ self.inputs),
            W2=(-2 / (self.M * self.n)) * ((f["delta2"] * f["r"]) @ f["h1"].T),
            W3=(-2 / (self.M * self.n)) * ((f["delta3"] * f["r"]) @ f["h2"].T),
            c=(-2 / self.M) * (f["h3"] @ f["r"]),
        ))

    def physical_velocity(self, state):
        return self.unpack(self.rhs(0., state))


class PopulationReference(DenseReference):
    """Original activity-clock P-mode population closure, evaluated directly."""

    kind = "population"

    def __init__(self, inputs, labels, initialization, order=1):
        super().__init__(inputs, labels, initialization)
        if not isinstance(order, (int, np.integer)) or order < 1:
            raise ValueError("order must be a positive integer")
        self.P = int(order)
        self.degrees = np.arange(self.P, dtype=np.float64)
        self.mode_weights = 2 * self.degrees + 1
        h1 = np.tanh(initialization.w @ self.inputs.T)
        h2 = np.tanh(initialization.W20 @ h1)
        self.names = ("w", "c", "A2", "B2", "A3", "B3", "L")
        moment_shape = (self.P, self.n, self.M)
        self.shapes = ((self.n, 2), (self.n,), moment_shape, moment_shape,
                       moment_shape, moment_shape, ())
        self._set_slices()
        initial = dict(w=initialization.w, c=initialization.c, L=1.)
        for layer, h in ((2, h1), (3, h2)):
            initial["A" + str(layer)] = np.zeros(moment_shape)
            initial["B" + str(layer)] = np.zeros(moment_shape)
            initial["B" + str(layer)][0] = h
        self.initial = self.pack(initial)

    def physical(self, state):
        values = self.unpack(state)
        physical = dict(w=values["w"], c=values["c"])
        factor = -2 / (self.M * self.n * float(values["L"]))
        for layer in (2, 3):
            A, B = values["A" + str(layer)], values["B" + str(layer)]
            correction = np.einsum("k,kia,kja->ij", self.mode_weights, A, B)
            physical["W" + str(layer)] = getattr(self.initialization, "W" + str(layer) + "0") + factor * correction
        return physical

    def transport(self, moments, source, rho, length):
        weighted = self.mode_weights[:, None, None] * moments
        lower = np.zeros_like(moments)
        lower[1:] = np.cumsum(weighted[:-1], axis=0)
        return source[None] - (rho / length) * (self.degrees[:, None, None] * moments + lower)

    def rhs(self, time, state):
        del time
        values, f = self.unpack(state), self.fields(state)
        velocity = dict(w=(-2 / self.M) * ((f["delta1"] * f["r"]) @ self.inputs),
                        c=(-2 / self.M) * (f["h3"] @ f["r"]), L=f["rho"])
        for layer in (2, 3):
            for prefix, source in (("A", f["delta" + str(layer)] * f["r"]),
                                    ("B", f["rho"] * f["h" + str(layer - 1)])):
                name = prefix + str(layer)
                velocity[name] = self.transport(values[name], source, f["rho"], float(values["L"]))
        return self.pack(velocity)

    def physical_velocity(self, state):
        values = self.unpack(state)
        velocity = self.unpack(self.rhs(0., state))
        result = dict(w=velocity["w"], c=velocity["c"])
        length = float(values["L"])
        factor = -2 / (self.M * self.n * length)
        for layer in (2, 3):
            A, B = values["A" + str(layer)], values["B" + str(layer)]
            dA, dB = velocity["A" + str(layer)], velocity["B" + str(layer)]
            result["W" + str(layer)] = factor * (
                np.einsum("k,kia,kja->ij", self.mode_weights, dA, B)
                + np.einsum("k,kia,kja->ij", self.mode_weights, A, dB)
                - float(velocity["L"]) / length
                * np.einsum("k,kia,kja->ij", self.mode_weights, A, B))
        return result


def solve_reference(model, horizon=40., *, target_mse=1e-3, rtol=1e-7,
                    atol=1e-9, stop_at_target=True, max_step=np.inf,
                    wall_seconds=120., initial=None):
    """DOP853 with a training-loss event and callable continuous interpolation."""
    start = perf_counter()

    def rhs(time, state):
        if perf_counter() - start > wall_seconds:
            raise TimeoutError(f"{model.kind} solver exceeded {wall_seconds}s")
        return model.rhs(time, state)

    def target_event(time, state):
        del time
        return model.fields(state)["loss"] - target_mse

    target_event.direction = -1
    target_event.terminal = bool(stop_at_target)
    result = solve_ivp(rhs, (0., float(horizon)), model.initial if initial is None else initial,
                       method="DOP853", rtol=rtol, atol=atol, dense_output=True,
                       events=target_event, max_step=max_step)
    result.wall_seconds = perf_counter() - start
    result.target_hit = bool(len(result.t_events[0]))
    result.final_loss = model.fields(result.y[:, -1])["loss"]
    result.model_kind = model.kind
    result.state_dimension = model.dimension
    return result


def algebra_checks():
    """Independent directional-gradient and reconstruction-derivative checks."""
    inputs = circle_inputs([10., 125.], degrees=True)
    labels = np.array([1., -1.])
    initial = initialize(5)
    dense = DenseReference(inputs, labels, initial)
    pop = PopulationReference(inputs, labels, initial, order=2)
    dense_vel = dense.physical_velocity(dense.initial)
    pop_vel = pop.physical_velocity(pop.initial)
    initial_velocity_error = max(float(np.max(np.abs(dense_vel[k] - pop_vel[k]))) for k in dense_vel)
    epsilon = 1e-6
    velocity = dense.rhs(0., dense.initial)
    observed = (dense.fields(dense.initial + epsilon * velocity)["loss"]
                - dense.fields(dense.initial - epsilon * velocity)["loss"]) / (2 * epsilon)
    expected = -sum(float(np.sum(v**2)) / (dense.n if k in ("w", "c") else 1.)
                    for k, v in dense_vel.items())
    gradient_error = abs(observed - expected)
    rng = np.random.default_rng(917)
    state = pop.initial + 0.02 * rng.standard_normal(pop.dimension)
    state[pop.slices["L"]] = 1.2
    direction = pop.rhs(0., state)
    plus, minus = pop.physical(state + epsilon * direction), pop.physical(state - epsilon * direction)
    analytic = pop.physical_velocity(state)
    reconstruction_error = max(float(np.max(np.abs((plus[k] - minus[k]) / (2 * epsilon) - analytic[k])))
                               for k in analytic)
    queries = circle_inputs([0.4, 1.8, 3.2])
    response_plus = pop.query_fields(state + epsilon * direction, queries)
    response_minus = pop.query_fields(state - epsilon * direction, queries)
    response_analytic = pop.query_field_velocity(state, queries)
    response_error = max(float(np.max(np.abs((response_plus[k] - response_minus[k]) / (2 * epsilon)
                                             - response_analytic[k]))) for k in response_analytic)
    result = dict(initial_velocity_max_error=initial_velocity_error,
                  dense_loss_directional_derivative_error=gradient_error,
                  population_reconstruction_derivative_max_error=reconstruction_error,
                  passive_response_derivative_max_error=response_error)
    if (initial_velocity_error > 1e-12 or gradient_error > 1e-7
            or reconstruction_error > 1e-7 or response_error > 1e-7):
        raise AssertionError(result)
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(algebra_checks(), indent=2))
