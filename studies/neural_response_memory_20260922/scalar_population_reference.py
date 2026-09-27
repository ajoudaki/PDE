"""Independent float64 population reference for scalar compression checks.

This module retains neuron fields and materializes hidden matrices. It is a
validation reference, not a scalar closure. Inputs have two coordinates and
are used at their supplied scale. Hidden depth counts tanh layers; output is
``c @ h[-1] / n``; loss is mean squared error; mobilities are n for first
weights/readout and 1 for hidden matrices. No Fourier representation is used.

The population state uses the original residual-activity clock, the constant
forward/zero-backward prefix of length one, and raw shifted-Legendre moments.
Only NumPy is required beyond Python's standard library.
"""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Initialization:
    """First matrix, tuple of initialized hidden links, and stored readout."""

    w: np.ndarray
    W0: tuple
    c: np.ndarray

    def __post_init__(self):
        w = np.asarray(self.w, dtype=np.float64).copy()
        c = np.asarray(self.c, dtype=np.float64).copy()
        hidden = tuple(np.asarray(v, dtype=np.float64).copy() for v in self.W0)
        if c.ndim != 1 or c.size < 1 or w.shape != (c.size, 2):
            raise ValueError("initialization requires w:(n,2), c:(n,), n>0")
        if any(v.shape != (c.size, c.size) for v in hidden):
            raise ValueError("each initialized hidden link must have shape (n,n)")
        if not all(np.isfinite(v).all() for v in (w, c) + hidden):
            raise ValueError("initialization must be finite")
        for v in (w, c) + hidden:
            v.setflags(write=False)
        object.__setattr__(self, "w", w)
        object.__setattr__(self, "W0", hidden)
        object.__setattr__(self, "c", c)

    @property
    def width(self):
        return self.c.size

    @property
    def depth(self):
        return len(self.W0) + 1


def initialize(width, seed=20260920, depth=2):
    """Sequential canonical draws: w, hidden links in order, then c.

    Entry variances are 1, 1/n, and 1/n**2 respectively. The returned
    initialization is independent of the number of retained history modes.
    """
    for name, value in (("width", width), ("depth", depth)):
        if not isinstance(value, (int, np.integer)) or value < 1:
            raise ValueError(f"{name} must be a positive integer")
    rng = np.random.default_rng(seed)
    w = rng.standard_normal((width, 2))
    hidden = tuple(rng.standard_normal((width, width)) / np.sqrt(width)
                   for _ in range(depth - 1))
    c = rng.standard_normal(width) / width
    return Initialization(w, hidden, c)


class DenseReference:
    """Canonical physical gradient flow, with arbitrary positive hidden depth."""

    kind = "dense"

    def __init__(self, inputs, labels, initialization):
        self.inputs = self._inputs(inputs).copy()
        self.labels = np.asarray(labels, dtype=np.float64).copy()
        self.M = self.inputs.shape[0]
        if self.M == 0 or self.labels.shape != (self.M,):
            raise ValueError("training inputs/labels require M>0 and labels:(M,)")
        if not np.isfinite(self.labels).all():
            raise ValueError("labels must be finite")
        self.initialization = initialization
        self.n = initialization.width
        self.depth = initialization.depth
        self.layers = tuple(range(2, self.depth + 1))
        self.names = ("w", "c") + tuple(f"W{layer}" for layer in self.layers)
        self.shapes = ((self.n, 2), (self.n,)) + ((self.n, self.n),) * len(self.layers)
        self._set_slices()
        values = dict(w=initialization.w, c=initialization.c)
        values.update({f"W{layer}": W for layer, W in zip(self.layers, initialization.W0)})
        self.initial = self.pack(values)

    @staticmethod
    def _inputs(inputs):
        inputs = np.asarray(inputs, dtype=np.float64)
        if inputs.ndim != 2 or inputs.shape[1] != 2:
            raise ValueError("inputs must have shape (M,2)")
        if not np.isfinite(inputs).all():
            raise ValueError("inputs must be finite")
        return inputs

    def _set_slices(self):
        ends = np.cumsum([0] + [int(np.prod(shape)) for shape in self.shapes])
        self.slices = {name: slice(int(start), int(end)) for name, start, end in
                       zip(self.names, ends[:-1], ends[1:])}
        self.dimension = int(ends[-1])

    def pack(self, values):
        """Pack named state blocks; names/shapes/slices describe the layout."""
        blocks = []
        for name, shape in zip(self.names, self.shapes):
            value = np.asarray(values[name], dtype=np.float64)
            if value.shape != shape:
                raise ValueError(f"{name} must have shape {shape}")
            blocks.append(value.ravel())
        return np.concatenate(blocks)

    def unpack(self, state):
        """Return views of a flat state; this does not modify its contents."""
        state = np.asarray(state, dtype=np.float64)
        if state.shape != (self.dimension,):
            raise ValueError(f"state must have shape ({self.dimension},)")
        return {name: state[self.slices[name]].reshape(shape)
                for name, shape in zip(self.names, self.shapes)}

    def physical(self, state):
        values = self.unpack(state)
        return dict(w=values["w"], c=values["c"],
                    hidden=tuple(values[f"W{layer}"] for layer in self.layers))

    def _query_physical(self, weights, inputs):
        h = [np.tanh(weights["w"] @ inputs.T)]
        for W in weights["hidden"]:
            h.append(np.tanh(W @ h[-1]))
        return dict(h=tuple(h), f=weights["c"] @ h[-1] / self.n)

    def query_fields(self, state, inputs):
        """Return h:(depth tuples of n-by-q arrays), f:(q,) at passive inputs."""
        return self._query_physical(self.physical(state), self._inputs(inputs))

    def predict(self, state, inputs):
        return self.query_fields(state, inputs)["f"]

    def fields(self, state):
        """Current training fields; delta excludes the residual and 1/n."""
        weights = self.physical(state)
        values = self._query_physical(weights, self.inputs)
        h = values["h"]
        r = values["f"] - self.labels
        delta = [None] * self.depth
        delta[-1] = weights["c"][:, None] * (1 - h[-1]**2)
        for link in range(self.depth - 2, -1, -1):
            delta[link] = (1 - h[link]**2) * (weights["hidden"][link].T @ delta[link + 1])
        loss = float(np.mean(r**2))
        values.update(r=r, loss=loss, rho=float(np.sqrt(loss)), delta=tuple(delta))
        return values

    def rhs(self, time, state):
        del time
        fields = self.fields(state)
        r, h, delta = fields["r"], fields["h"], fields["delta"]
        velocity = dict(w=(-2 / self.M) * ((delta[0] * r) @ self.inputs),
                        c=(-2 / self.M) * (h[-1] @ r))
        for link, layer in enumerate(self.layers):
            velocity[f"W{layer}"] = (-2 / (self.M * self.n)) * ((delta[link + 1] * r) @ h[link].T)
        return self.pack(velocity)

    def physical_velocity(self, state):
        return self.physical(self.rhs(0., state))

    def query_field_velocity(self, state, inputs):
        """Exact query chain rule using the current physical weight velocity."""
        inputs = self._inputs(inputs)
        weights = self.physical(state)
        velocity = self.physical_velocity(state)
        fields = self._query_physical(weights, inputs)
        h = fields["h"]
        dh = [(1 - h[0]**2) * (velocity["w"] @ inputs.T)]
        for link, W in enumerate(weights["hidden"]):
            dz = velocity["hidden"][link] @ h[link] + W @ dh[-1]
            dh.append((1 - h[link + 1]**2) * dz)
        df = (velocity["c"] @ h[-1] + weights["c"] @ dh[-1]) / self.n
        return dict(h=tuple(dh), f=df)


class PopulationReference(DenseReference):
    """Original activity-clock population closure, evaluated without lifting.

    Internal state blocks are w,c,A2,B2,...,L. Each moment block has shape
    (P,n,M). Physical dictionaries contain w,c,hidden, with one matrix per
    hidden link. h and delta tuples are indexed by hidden layer, starting at 0.
    """

    kind = "population"

    def __init__(self, inputs, labels, initialization, order=1):
        super().__init__(inputs, labels, initialization)
        if not isinstance(order, (int, np.integer)) or order < 1:
            raise ValueError("order must be a positive integer")
        self.P = int(order)
        self.degrees = np.arange(self.P, dtype=np.float64)
        self.mode_weights = 2 * self.degrees + 1
        h = self._query_physical(dict(w=initialization.w, c=initialization.c,
                                     hidden=initialization.W0), self.inputs)["h"]
        moments = tuple(name for layer in self.layers for name in (f"A{layer}", f"B{layer}"))
        moment_shape = (self.P, self.n, self.M)
        self.names = ("w", "c") + moments + ("L",)
        self.shapes = ((self.n, 2), (self.n,)) + (moment_shape,) * len(moments) + ((),)
        self._set_slices()
        values = dict(w=initialization.w, c=initialization.c, L=1.)
        for link, layer in enumerate(self.layers):
            values[f"A{layer}"] = np.zeros(moment_shape, dtype=np.float64)
            values[f"B{layer}"] = np.zeros(moment_shape, dtype=np.float64)
            values[f"B{layer}"][0] = h[link]
        self.initial = self.pack(values)

    @staticmethod
    def _length(values):
        length = float(values["L"])
        if not np.isfinite(length) or length <= 0:
            raise ValueError("history length L must be finite and positive")
        return length

    def _cross_moment(self, A, B):
        return np.einsum("k,kia,kja->ij", self.mode_weights, A, B)

    def physical(self, state):
        values = self.unpack(state)
        factor = -2 / (self.M * self.n * self._length(values))
        hidden = tuple(W0 + factor * self._cross_moment(values[f"A{layer}"], values[f"B{layer}"])
                       for layer, W0 in zip(self.layers, self.initialization.W0))
        return dict(w=values["w"], c=values["c"], hidden=hidden)

    def transport(self, moments, source, rho, length):
        """All-mode raw Legendre transport: source - rho/L*(k*T_k+lower)."""
        lower = np.zeros_like(moments)
        lower[1:] = np.cumsum(self.mode_weights[:-1, None, None] * moments[:-1], axis=0)
        return source[None] - (rho / length) * (self.degrees[:, None, None] * moments + lower)

    def rhs(self, time, state):
        del time
        values = self.unpack(state)
        fields = self.fields(state)
        r, rho, h, delta = fields["r"], fields["rho"], fields["h"], fields["delta"]
        length = self._length(values)
        velocity = dict(w=(-2 / self.M) * ((delta[0] * r) @ self.inputs),
                        c=(-2 / self.M) * (h[-1] @ r), L=rho)
        for link, layer in enumerate(self.layers):
            velocity[f"A{layer}"] = self.transport(values[f"A{layer}"], delta[link + 1] * r, rho, length)
            velocity[f"B{layer}"] = self.transport(values[f"B{layer}"], rho * h[link], rho, length)
        return self.pack(velocity)

    def physical_velocity(self, state):
        """Differentiate reconstruction by its full product/quotient rule."""
        values = self.unpack(state)
        velocity = self.unpack(self.rhs(0., state))
        length = self._length(values)
        factor = -2 / (self.M * self.n * length)
        hidden = []
        for layer in self.layers:
            A, B = values[f"A{layer}"], values[f"B{layer}"]
            dA, dB = velocity[f"A{layer}"], velocity[f"B{layer}"]
            hidden.append(factor * (self._cross_moment(dA, B) + self._cross_moment(A, dB)
                                   - float(velocity["L"]) / length * self._cross_moment(A, B)))
        return dict(w=velocity["w"], c=velocity["c"], hidden=tuple(hidden))


def algebra_checks():
    """Bounded local checks, no integration or training campaign.

    Freeze width 5, depths 1/2/3, orders 1/2, seed 719, and central-difference
    step 1e-6. Fail above 1e-7 for derivatives or 1e-12 for algebraic identities.
    Perturbed memory states exercise all transport and reconstruction terms.
    """
    inputs = np.array([[1., 0.], [.3, .8], [-.6, .4]])
    labels = np.array([1., -.7, .2])
    queries = np.array([[.2, -.9], [.8, .3], [-.4, -.5], [.1, .2]])
    rng = np.random.default_rng(719)
    epsilon = 1e-6
    errors = dict(initial_velocity=0., dense_gradient=0., reconstruction_derivative=0.,
                  query_derivative=0., defect_identity=0., zero_residual=0.)

    def blocks(values):
        return (values["w"], values["c"]) + values["hidden"]

    def maximum(arrays):
        return max((float(np.max(np.abs(v))) for v in arrays), default=0.)

    for depth in (1, 2, 3):
        initial = initialize(5, seed=719, depth=depth)
        dense = DenseReference(inputs, labels, initial)
        dv = dense.physical_velocity(dense.initial)
        dense_direction = rng.standard_normal(dense.dimension)
        observed = (dense.fields(dense.initial + epsilon * dense_direction)["loss"]
                    - dense.fields(dense.initial - epsilon * dense_direction)["loss"]) / (2 * epsilon)
        direction = dense.physical(dense_direction)
        expected = -sum(float(np.sum(v * d)) / mobility for v, d, mobility in
                        zip(blocks(dv), blocks(direction), (dense.n, dense.n) + (1,) * (depth - 1)))
        errors["dense_gradient"] = max(errors["dense_gradient"], abs(observed - expected))
        for order in (1, 2):
            pop = PopulationReference(inputs, labels, initial, order=order)
            pv = pop.physical_velocity(pop.initial)
            errors["initial_velocity"] = max(errors["initial_velocity"], maximum(
                a - b for a, b in zip(blocks(dv), blocks(pv))))
            state = pop.initial + .04 * rng.standard_normal(pop.dimension)
            state[pop.slices["L"]] = 1.3
            direction = pop.rhs(0., state)
            plus, minus = pop.physical(state + epsilon * direction), pop.physical(state - epsilon * direction)
            analytic = pop.physical_velocity(state)
            errors["reconstruction_derivative"] = max(errors["reconstruction_derivative"], maximum(
                (a - b) / (2 * epsilon) - v for a, b, v in zip(blocks(plus), blocks(minus), blocks(analytic))))
            plus = pop.query_fields(state + epsilon * direction, queries)
            minus = pop.query_fields(state - epsilon * direction, queries)
            analytic_fields = pop.query_field_velocity(state, queries)
            errors["query_derivative"] = max(errors["query_derivative"], maximum(
                (a - b) / (2 * epsilon) - v for a, b, v in zip(
                    plus["h"] + (plus["f"],), minus["h"] + (minus["f"],),
                    analytic_fields["h"] + (analytic_fields["f"],))))
            values, fields = pop.unpack(state), pop.fields(state)
            for link, layer in enumerate(pop.layers):
                uP = np.einsum("k,kia->ia", pop.mode_weights, values[f"A{layer}"]) / float(values["L"])
                hP = np.einsum("k,kia->ia", pop.mode_weights, values[f"B{layer}"]) / float(values["L"])
                source = fields["delta"][link + 1] * fields["r"]
                dense_velocity = -2 / (pop.M * pop.n) * (source @ fields["h"][link].T)
                defect = 2 / (pop.M * pop.n) * ((source - fields["rho"] * uP) @ (fields["h"][link] - hP).T)
                errors["defect_identity"] = max(errors["defect_identity"], maximum(
                    [analytic["hidden"][link] - dense_velocity - defect]))
            zero = PopulationReference(inputs, pop.predict(pop.initial, inputs), initial, order=order)
            errors["zero_residual"] = max(errors["zero_residual"], maximum([zero.rhs(0., zero.initial)]))
    for name, error in errors.items():
        threshold = 1e-7 if name in ("dense_gradient", "reconstruction_derivative", "query_derivative") else 1e-12
        if not np.isfinite(error) or error > threshold:
            raise AssertionError(errors)
    return errors


if __name__ == "__main__":
    print(algebra_checks())
