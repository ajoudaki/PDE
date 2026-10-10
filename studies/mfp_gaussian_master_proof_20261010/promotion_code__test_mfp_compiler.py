"""Exact deterministic oracles for finite AD and the Gaussian compiler.

Run with ``PYTHONPATH=code python -m unittest discover -s code/tests -p 'test_mfp_*.py'``.
The finite reference network uses ordinary arrays and an independent polynomial
ring for perturbations. It never calls the compiler's differentiation or its
Gaussian integration rules. No sampling or training experiment is performed.
"""
from fractions import Fraction as F
from math import factorial
import unittest

from pde import mfp_expr as ex
from pde.gaussian_moments import gaussian_moment
from pde.mfp_compiler import Node, Program, ProgramError
from pde.mfp_finite import evaluate_finite
from scripts.example_mfp_calculus import gradient_update


class Polynomial:
    """Independent finite polynomial in t, used only for exact Taylor oracles."""

    def __init__(self, coefficients):
        self.c = tuple(map(F, coefficients))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Polynomial) else Polynomial((value,))

    def __add__(self, other):
        other = self.coerce(other)
        return Polynomial(self[k] + other[k] for k in range(max(len(self.c), len(other.c))))

    __radd__ = __add__

    def __mul__(self, other):
        other = self.coerce(other)
        result = [F(0)] * (len(self.c) + len(other.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                result[i + j] += a * b
        return Polynomial(result)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (F(1) / other)

    def __pow__(self, order):
        result = Polynomial((1,))
        for _ in range(order):
            result = result * self
        return result

    def __getitem__(self, degree):
        return self.c[degree] if degree < len(self.c) else F(0)


def average(values):
    return sum(values, F(0)) / len(values)


def matvec(matrix, vector, transpose=False):
    n = len(vector)
    return [sum(((matrix[j][i] if transpose else matrix[i][j]) * vector[j]
                 for j in range(n)), F(0)) for i in range(n)]


def direct_loss(x, matrix, scalar):
    """O = mean((W.T (Wx)^3)^2) + mean((Wx)^3)^2 + s mean((Wx)^3)."""
    h = [z**3 for z in matvec(matrix, x)]
    v = matvec(matrix, h, transpose=True)
    return average([a**2 for a in v]) + average(h)**2 + scalar * average(h)


def direct_gradients(x, matrix, scalar):
    """Every raw-coordinate derivative from its exact t coefficient."""
    n = len(x)
    vector_gradient = []
    for i in range(n):
        perturbed = [Polynomial((a, int(i == j))) for j, a in enumerate(x)]
        vector_gradient.append(direct_loss(perturbed, matrix, scalar)[1])
    matrix_gradient = []
    for i in range(n):
        row = []
        for j in range(n):
            perturbed = [[Polynomial((a, int(i == k and j == l)))
                          for l, a in enumerate(values)] for k, values in enumerate(matrix)]
            row.append(direct_loss(x, perturbed, scalar)[1])
        matrix_gradient.append(row)
    scalar_gradient = direct_loss(x, matrix, Polynomial((scalar, 1)))[1]
    return vector_gradient, matrix_gradient, scalar_gradient


def cubic(order, value):
    return F(0) if order > 3 else factorial(3) // factorial(3 - order) * value**(3 - order)


def setup_network():
    p = Program()
    lower, upper = p.vector_type("lower"), p.vector_type("upper")
    x, s = p.root("x", lower), p.parameter("s")
    w = p.matrix("W", lower, upper)
    h = p.phi(w @ x)
    v = w.T @ h
    output = p.mean(v**2) + p.mean(h)**2 + s * p.mean(h)
    return p, x, w, s, output


class FiniteInterpreterTests(unittest.TestCase):
    def setUp(self):
        self.p, self.x, self.w, self.s, self.output = setup_network()
        self.xv = [F(1, 3), F(-2, 5)]
        self.wv = [[F(1, 2), F(-1, 3)], [F(2, 3), F(1, 5)]]
        self.sv = F(1, 7)

    def evaluate(self, output, roots=None, matrices=None, parameters=None, activation=cubic):
        return evaluate_finite(output, 2, {self.x: self.xv} if roots is None else roots,
                               {self.w: self.wv} if matrices is None else matrices,
                               {self.s: self.sv} if parameters is None else parameters, activation)

    def test_exact_reused_transpose_network(self):
        actual = self.evaluate(self.output)
        self.assertIsInstance(actual, F)
        self.assertEqual(actual, direct_loss(self.xv, self.wv, self.sv))

    def test_scalar_broadcast_mean_and_freeze(self):
        output = self.p.mean(self.p.freeze(self.x) * (self.s + 2))
        self.assertEqual(self.evaluate(output), average(self.xv) * (self.sv + 2))
        self.assertEqual(self.evaluate(self.p.broadcast(self.s, self.x.kind)), (self.sv,) * 2)
        self.assertEqual(self.evaluate(self.p.coerce(3)), F(3))

    def test_freeze_declares_independent_seed_data_not_primal_derivatives(self):
        ordinary = self.p.mean(self.x**2)
        frozen = self.p.mean(self.p.freeze(self.x)**2)
        direction = {self.x: self.p.one(self.x.kind)}
        self.assertEqual(self.evaluate(ordinary), self.evaluate(frozen))
        self.assertEqual(self.evaluate(self.p.directional(ordinary, direction)), 2 * average(self.xv))
        self.assertEqual(self.evaluate(self.p.directional(frozen, direction)), 0)

    def test_invalid_width_and_output(self):
        for width in (0, -1, 2.0, True):
            with self.subTest(width=width), self.assertRaises(ProgramError):
                evaluate_finite(self.output, width, {}, {})
        with self.assertRaises(ProgramError):
            evaluate_finite(3, 2, {}, {})

    def test_missing_data_and_activation(self):
        for arguments in (dict(roots={}), dict(matrices={}), dict(parameters={}), dict(activation=None)):
            with self.subTest(arguments=arguments), self.assertRaises(ProgramError):
                self.evaluate(self.output, **arguments)

    def test_invalid_shapes_and_values(self):
        for roots in ({self.x: [1]}, {self.x: [1, float("inf")]}, {self.s: [1, 2]}):
            with self.subTest(roots=roots), self.assertRaises(ProgramError):
                self.evaluate(self.output, roots=roots)
        for matrices in ({self.w: [[1, 2]]}, {self.w: [[1], [2]]}, {self.w: [[1, 2], [3, "4"]]}):
            with self.subTest(matrices=matrices), self.assertRaises(ProgramError):
                self.evaluate(self.output, matrices=matrices)
        with self.assertRaises(ProgramError):
            self.evaluate(self.output, parameters={self.s: float("nan")})
        with self.assertRaises(ProgramError):
            self.evaluate(self.output, activation=lambda order, x: None)
        with self.assertRaises(ProgramError):
            self.evaluate(Node(self.p, -1, "inverse", None))

    def test_represented_rank_one_actions_both_orientations(self):
        left = self.p.root("u", self.w.target)
        right = self.p.root("v", self.w.source)
        test = self.p.root("q", self.w.target)
        u, v, q = [F(2), F(-3)], [F(1, 2), F(4)], [F(3), F(-1)]
        represented = self.w + self.p.rank_one(left, right, self.s)
        dense = [[self.wv[i][j] + self.sv * u[i] * v[j] / 2
                  for j in range(2)] for i in range(2)]
        roots = {self.x: self.xv, left: u, right: v, test: q}
        self.assertEqual(self.evaluate(represented @ self.x, roots=roots), tuple(matvec(dense, self.xv)))
        self.assertEqual(self.evaluate(represented.T @ test, roots=roots), tuple(matvec(dense, q, True)))

    def test_frozen_derivatives_and_jets_against_independent_polynomial(self):
        p, x, w, s = self.p, self.x, self.w, self.s
        dx, ds = -(x**2), s**2 + p.mean(x)
        dw = p.rank_one(w @ x, x)
        directions = {x: dx, w: dw, s: ds}
        dxv = [-a**2 for a in self.xv]
        dsv = self.sv**2 + average(self.xv)
        left = matvec(self.wv, self.xv)
        dwv = [[left[i] * self.xv[j] / 2 for j in range(2)] for i in range(2)]
        reference = direct_loss([Polynomial((a, d)) for a, d in zip(self.xv, dxv)],
                                [[Polynomial((self.wv[i][j], dwv[i][j])) for j in range(2)] for i in range(2)],
                                Polynomial((self.sv, dsv)))
        derivatives = p.derivatives(self.output, directions, 3)
        jets = p.jets(self.output, directions, 3)
        for order in range(4):
            with self.subTest(order=order):
                self.assertEqual(self.evaluate(derivatives[order]), factorial(order) * reference[order])
                self.assertEqual(self.evaluate(jets[order]), reference[order])
        self.assertEqual(self.evaluate(p.directional(self.output, directions)), reference[1])

    def test_normalized_vector_matrix_and_scalar_gradients(self):
        p, x, w, s = self.p, self.x, self.w, self.s
        gradients = p.gradient(self.output, vectors=[x], matrices=[w], scalars=[s])
        gx, gw, gs = direct_gradients(self.xv, self.wv, self.sv)
        self.assertEqual(self.evaluate(gradients[x]), tuple(2 * a for a in gx))
        self.assertEqual(self.evaluate(gradients[s]), gs)
        probe = p.root("probe", x.kind)
        for j in range(2):
            roots = {x: self.xv, probe: [F(int(i == j)) for i in range(2)]}
            actual_column = self.evaluate(gradients[w] @ probe, roots=roots)
            self.assertEqual(actual_column, tuple(gw[i][j] for i in range(2)))

    def test_fixed_updates_equal_direct_ambient_updates(self):
        p, x, w, s = self.p, self.x, self.w, self.s
        eta, mx, mw = F(1, 100), F(3, 2), F(2, 3)
        states = p.gradient_descent(self.output, [x], [w], steps=2, step_size=eta,
                                    mobilities={x: mx, w: mw})
        xv, wv = self.xv[:], [row[:] for row in self.wv]
        for _ in range(2):
            gx, gw, _ = direct_gradients(xv, wv, self.sv)
            xv = [a - eta * mx * 2 * g for a, g in zip(xv, gx)]
            wv = [[wv[i][j] - eta * mw * gw[i][j] for j in range(2)] for i in range(2)]
        self.assertEqual(self.evaluate(states[x]), tuple(xv))
        self.assertEqual(self.evaluate(p.at(self.output, states)), direct_loss(xv, wv, self.sv))
        probe = p.root("update_probe", x.kind)
        for j in range(2):
            roots = {x: self.xv, probe: [F(int(i == j)) for i in range(2)]}
            self.assertEqual(self.evaluate(states[w] @ probe, roots=roots), tuple(wv[i][j] for i in range(2)))

    def test_simultaneous_substitution_does_not_revisit_replacements(self):
        y = self.p.root("y", self.x.kind)
        output = self.p.at(self.x + y, {self.x: y, y: self.x * 2})
        self.assertEqual(self.evaluate(output, roots={self.x: [1, 2], y: [3, 4]}), (F(5), F(8)))

    def test_current_gradient_differs_from_history_pullback(self):
        p, x = self.p, self.x
        eta = F(1, 10)
        loss = p.mean(x*x)
        state = p.gradient_descent(loss, vectors=[x], step_size=eta)
        current = p.at(p.gradient(loss, vectors=[x])[x], state)
        pullback = p.gradient(p.at(loss, state), vectors=[x])[x]
        scale = 1-2*eta  # x_new=scale*x and loss_after=scale**2*mean(x*x).
        self.assertEqual(self.evaluate(current), tuple(2*scale*v for v in self.xv))
        self.assertEqual(self.evaluate(pullback), tuple(2*scale**2*v for v in self.xv))
        self.assertNotEqual(self.evaluate(current), self.evaluate(pullback))

    def test_frobenius_contraction_against_dense_gradient(self):
        p, x, w = self.p, self.x, self.w
        gradients = p.gradient(self.output, vectors=[x], matrices=[w])
        gx, gw, _ = direct_gradients(self.xv, self.wv, self.sv)
        norm = p.frobenius(gradients[w], gradients[w])
        self.assertEqual(self.evaluate(norm), sum(g**2 for row in gw for g in row))
        velocity = {x: -gradients[x], w: -gradients[w]}
        self.assertEqual(self.evaluate(p.directional(self.output, velocity)),
                         -2 * sum(g**2 for g in gx) - sum(g**2 for row in gw for g in row))
        with self.assertRaises(ProgramError):
            p.frobenius(p.represented(w), gradients[w])

    def test_curve_jets_against_independent_polynomial(self):
        p, x, w, s = self.p, self.x, self.w, self.s
        a, b = x**2, -x
        dw = p.rank_one(w @ x, x)
        coefficients = {x: (a, b), w: (dw,), s: (s**2, p.mean(x))}
        left = matvec(self.wv, self.xv)
        reference = direct_loss(
            [Polynomial((v, v**2, -v)) for v in self.xv],
            [[Polynomial((self.wv[i][j], left[i] * self.xv[j] / 2)) for j in range(2)] for i in range(2)],
            Polynomial((self.sv, self.sv**2, average(self.xv))))
        jets = p.curve_jets(self.output, coefficients, 3)
        for order in range(4):
            with self.subTest(order=order):
                self.assertEqual(self.evaluate(jets[order]), reference[order])

    def test_moving_matrix_vector_flow_against_direct_second_derivative(self):
        # L=mean((Wx)^2), xdot=-2 W.T z, Wdot=-2 z x.T/n, z=Wx.
        p, x, w = self.p, self.x, self.w
        loss = p.mean((w @ x)**2)
        gradient = p.gradient(loss, vectors=[x], matrices=[w])
        second = p.derivatives(loss, {x: -gradient[x], w: -gradient[w]}, 2, moving=True)[2]
        xv, wv, n = self.xv, self.wv, 2
        z = matvec(wv, xv)
        dx = [-2 * value for value in matvec(wv, z, transpose=True)]
        dw = [[-2 * z[i] * xv[j] / n for j in range(n)] for i in range(n)]
        dz = [a + b for a, b in zip(matvec(dw, xv), matvec(wv, dx))]
        ddx = [-2 * (a + b) for a, b in zip(matvec(dw, z, True), matvec(wv, dz, True))]
        ddw = [[-2 * (dz[i] * xv[j] + z[i] * dx[j]) / n for j in range(n)] for i in range(n)]
        ddz = [a + 2 * b + c for a, b, c in zip(matvec(ddw, xv), matvec(dw, dx), matvec(wv, ddx))]
        expected = 2 * average([a**2 + b * c for a, b, c in zip(dz, z, ddz)])
        self.assertEqual(self.evaluate(second), expected)


class FrozenSeedTests(unittest.TestCase):
    def test_vector_updates_keep_the_initial_seed_and_physical_partial(self):
        p = Program()
        x = p.root("x", p.vector_type("neurons"))
        seed = p.freeze(x)
        loss = p.inner(x, seed)
        eta, values = F(1, 10), [F(1), F(2)]
        for steps in (0, 1, 2, 3):
            with self.subTest(steps=steps):
                state = p.gradient_descent(loss, vectors=[x], steps=steps, step_size=eta)
                # The exact enlarged-space update is x_k=x_0-k*eta*b, b=x_0.
                expected = tuple((1-steps*eta)*value for value in values)
                self.assertEqual(evaluate_finite(state[x], 2, {x: values}, {}), expected)
                self.assertEqual(evaluate_finite(p.at(seed, state), 2, {x: values}, {}), tuple(values))
                partial = p.directional(state[x], {x: p.one(x.kind)})
                self.assertEqual(evaluate_finite(partial, 2, {x: values}, {}), (F(1), F(1)))
                # Seed and initial state share Gaussian values, despite the
                # seed being independent for the preceding physical partial.
                self.assertEqual(p.compile(p.mean(state[x]**2)).output,
                                 ex.const((1-steps*eta)**2))

    def test_scalar_and_nested_seeds_require_an_explicit_new_snapshot(self):
        p = Program()
        x = p.root("x", p.vector_type("neurons"))
        s = p.parameter("s")
        value = s+p.mean(x)
        seed = p.freeze(value)
        nested = p.freeze(seed+value)
        state = {x: 2*x, s: 3*s}
        def finite(node):
            return evaluate_finite(node, 2, {x: [1, 3]}, {}, {s: F(2)})
        self.assertEqual(finite(p.at(seed, state)), F(4))
        self.assertEqual(finite(p.at(nested, state)), F(8))
        self.assertEqual(finite(p.freeze(p.at(value, state))), F(10))
        # An ordinary occurrence still updates next to the fixed seed.
        self.assertEqual(finite(p.at(value+seed, state)), F(14))

    def test_matrix_updates_keep_frozen_rank_factors_from_the_initial_matrix(self):
        p = Program()
        lower, upper = p.vector_type("lower"), p.vector_type("upper")
        x = p.root("x", lower)
        W = p.matrix("W", lower, upper)
        initial_action = W @ x
        left, right = p.freeze(initial_action), p.freeze(x)
        coefficient = p.freeze(p.mean(initial_action**2))
        loss = coefficient*p.inner(left, W @ right)
        xv = [F(1, 3), F(-2, 5)]
        wv = [[F(1, 2), F(-1, 3)], [F(2, 3), F(1, 5)]]
        n, eta = len(xv), F(1, 10)
        u = matvec(wv, xv)
        c = average([value**2 for value in u])
        # The ordinary dense Frobenius gradient is the fixed c*u*xv.T/n.
        dense_gradient = [[c*u[i]*xv[j]/n for j in range(n)] for i in range(n)]
        probe = p.root("probe", lower)
        for steps in (0, 1, 2, 3):
            with self.subTest(steps=steps):
                state = p.gradient_descent(loss, matrices=[W], steps=steps, step_size=eta)
                expected = [[wv[i][j]-steps*eta*dense_gradient[i][j]
                             for j in range(n)] for i in range(n)]
                for j in range(n):
                    basis = [F(int(i == j)) for i in range(n)]
                    actual = evaluate_finite(state[W] @ probe, n, {x: xv, probe: basis}, {W: wv})
                    self.assertEqual(actual, tuple(expected[i][j] for i in range(n)))
                self.assertEqual(evaluate_finite(state[W].T @ left, n, {x: xv}, {W: wv}),
                                 tuple(matvec(expected, u, transpose=True)))
                self.assertEqual(evaluate_finite(p.at(loss, state), n, {x: xv}, {W: wv}),
                                 c*average([a*b for a, b in zip(u, matvec(expected, xv))]))

    def test_moving_and_curve_jets_hold_seed_fixed(self):
        p = Program()
        x = p.root("x", p.vector_type("neurons"))
        seed = p.freeze(x)
        output = p.mean(x**2)
        values = [F(1), F(2)]
        moving = p.jets(output, {x: -seed}, order=3, moving=True)
        curve = p.curve_jets(output, {x: (-seed,)}, order=3)
        # The exact path is x(t)=x_0-t*b with fixed b=x_0.
        expected = (average([v*v for v in values]),
                    -2*average([v*v for v in values]),
                    average([v*v for v in values]), F(0))
        for jets in (moving, curve):
            self.assertEqual(tuple(evaluate_finite(j, 2, {x: values}, {}) for j in jets), expected)
            self.assertEqual(tuple(p.compile(j).output for j in jets),
                             tuple(ex.const(v) for v in (1, -2, 1, 0)))

    def test_frozen_matrix_action_retains_formal_source_response(self):
        p = Program()
        lower, upper = p.vector_type("lower"), p.vector_type("upper")
        W = p.matrix("W", lower, upper)
        seed = p.freeze(W @ p.one(lower))
        direction = p.rank_one(p.one(upper), p.one(lower))
        unchanged_seed = p.at(seed, {W: W+direction})
        physical = p.directional(p.mean(unchanged_seed), {W: direction})
        self.assertEqual(p.compile(physical).output, ex.const(0))
        back = W.T @ unchanged_seed
        dag = p.compile(p.inner(back, back))
        # Frozen physical data still came from the original W: the reused
        # transpose has source variance one and response coefficient one.
        self.assertEqual(dag.output, ex.const(2))
        calls = [row for row in dag.trace if row["rule"] == "matrix source and response"]
        self.assertEqual(calls[-1]["response"][0]["coefficient"], "1")


class GaussianCompilerTests(unittest.TestCase):
    def test_numeric_moments_agree_with_maintained_rational_api(self):
        # Independent maintained recurrence also validates each rational PSD law.
        laws = (((2, F(-1, 3)), (F(-1, 3), 3)),
                ((1, -1), (-1, 1)), ((0, 0), (0, 2)))
        for covariance in laws:
            p = Program()
            kind = p.vector_type("neurons")
            x, y = p.roots(kind, ("x", "y"), covariance)
            for powers in ((0, 0), (1, 3), (2, 2), (4, 2), (3, 2)):
                with self.subTest(covariance=covariance, powers=powers):
                    dag = p.compile(p.mean(x**powers[0] * y**powers[1]))
                    self.assertEqual(dag.output, ex.const(gaussian_moment(covariance, powers)))
                    self.assertFalse(dag.expectations)

    def test_gradient_update_example_has_exact_saved_derivative_formula(self):
        eta = ex.symbol("s_eta")
        self.assertEqual(ex.expand(gradient_update().output), ex.expand(15 + (3-15*eta)**2))

    def matrix_setup(self):
        p = Program()
        a, b = p.vector_type("a"), p.vector_type("b")
        w = p.matrix("W", a, b)
        return p, a, b, w

    def assert_constant_limit(self, dag, expected):
        self.assertEqual(dag.output, ex.const(expected))
        self.assertFalse(dag.expectations)

    def test_generic_activation_transpose_response_formula(self):
        p, a, _, w = self.matrix_setup()
        z = w @ p.one(a)
        output = p.mean((w.T @ p.phi(z))**2)
        dag = p.compile(output, preactivations=[z])
        self.assertEqual(len(dag.expectations), 2)
        second_moment, derivative_mean = dag.expectations
        g = ex.symbol("g_W_F_1")
        self.assertEqual(second_moment.integrand, ex.phi(g)**2)
        self.assertEqual(derivative_mean.integrand, ex.phi(g, 1))
        self.assertEqual(second_moment.covariance, ((ex.const(1),),))
        self.assertEqual(derivative_mean.covariance, ((ex.const(1),),))
        self.assertEqual(dag.output, second_moment.symbol + derivative_mean.symbol**2)

    def test_linear_and_cubic_transpose_response_limits(self):
        # E[Z^2] + E[1]^2 = 2; E[Z^6] + E[3Z^2]^2 = 15 + 9 = 24.
        for power, expected in ((1, 2), (3, 24)):
            with self.subTest(power=power):
                p, a, _, w = self.matrix_setup()
                z = w @ p.one(a)
                self.assert_constant_limit(p.compile(p.mean((w.T @ z**power)**2)), expected)

    def test_wishart_chain_moments(self):
        p, a, _, w = self.matrix_setup()
        ones, vector = p.one(a), p.one(a)
        for expected in (1, 2, 5):
            vector = w.T @ (w @ vector)
            self.assert_constant_limit(p.compile(p.inner(ones, vector)), expected)

    def test_reusing_a_matrix_differs_from_an_independent_matrix(self):
        p, a, b, w = self.matrix_setup()
        v = p.matrix("V", a, b)
        z = w @ p.one(a)
        self.assert_constant_limit(p.compile(p.mean((w.T @ z)**2)), 2)
        self.assert_constant_limit(p.compile(p.mean((v.T @ z)**2)), 1)
        with self.assertRaises(ProgramError):
            p.matrix("W", a, b)

    def test_duplicate_queries_keep_distinct_singular_source_symbols(self):
        p, a, _, w = self.matrix_setup()
        ones = p.one(a)
        y1, y2 = w @ ones, w @ ones
        dag = p.compile(p.mean((w.T @ (y1**2 * y2))**2))
        self.assert_constant_limit(dag, 24)
        names = [source["name"] for source in dag.sources]
        self.assertIn("g_W_F_1", names)
        self.assertIn("g_W_F_2", names)
        response = [record for record in dag.trace if record["rule"] == "matrix source and response"][-1]["response"]
        self.assertEqual([item["coefficient"] for item in response], ["2", "1"])
        self.assertNotEqual(response[0]["formal_derivative"], response[1]["formal_derivative"])
        self.assert_constant_limit(p.compile(p.mean((y1 - y2)**2)), 0)

    def test_correlated_shifted_roots_and_independent_tuples(self):
        p = Program()
        a = p.vector_type("a")
        x, y = p.roots(a, ["x", "y"], [[2, F(1, 2)], [F(1, 2), 3]], means=[1, -2])
        z = p.root("z", a)
        self.assert_constant_limit(p.compile(p.mean(x * y)), F(-3, 2))
        self.assert_constant_limit(p.compile(p.mean((x - 1)**2 * (y + 2)**2)), F(13, 2))
        self.assert_constant_limit(p.compile(p.mean(x * z)), 0)

    def test_singular_root_covariance(self):
        p = Program()
        a = p.vector_type("a")
        x, y = p.roots(a, ["x", "y"], [[1, 1], [1, 1]])
        self.assert_constant_limit(p.compile(p.mean((x - y)**2)), 0)
        self.assert_constant_limit(p.compile(p.mean(x**2 * y**2)), 3)

    def test_root_covariance_rejects_text_even_if_numerically_parseable(self):
        p = Program()
        kind = p.vector_type("neurons")
        with self.assertRaises(ProgramError):
            p.root("x", kind, variance="1")
        x = p.root("x", kind, variance=F(1, 2))
        self.assert_constant_limit(p.compile(p.mean(x*x)), F(1, 2))

    def test_moving_flow_second_derivative_differs_from_frozen_direction(self):
        # xdot=-x^3 and O=mean(x^2): O'=-2 mean(x^4), O''=8 mean(x^6).
        # The second frozen Frechet derivative is only 2 mean(x^6).
        p = Program()
        a = p.vector_type("a")
        x = p.root("x", a)
        loss, output = p.mean(x**4) / 4, p.mean(x**2)
        velocity = -p.gradient(loss, vectors=[x])[x]
        moving = p.derivatives(output, {x: velocity}, 2, moving=True)
        frozen = p.derivatives(output, {x: velocity}, 2)
        xv = [F(1), F(-2), F(3)]
        self.assertEqual(evaluate_finite(moving[1], 3, {x: xv}, {}), -2 * average([v**4 for v in xv]))
        self.assertEqual(evaluate_finite(moving[2], 3, {x: xv}, {}), 8 * average([v**6 for v in xv]))
        self.assertEqual(evaluate_finite(frozen[2], 3, {x: xv}, {}), 2 * average([v**6 for v in xv]))
        self.assert_constant_limit(p.compile(moving[2]), 120)
        self.assert_constant_limit(p.compile(frozen[2]), 30)
        self.assert_constant_limit(p.compile(p.jets(output, {x: velocity}, 2, moving=True)[2]), 60)

    def test_cross_type_gaussian_roots_and_matrix_calls(self):
        p, a, b, w = self.matrix_setup()
        x, y = p.root("x", a, variance=2), p.root("y", b, variance=3)
        self.assert_constant_limit(p.compile(p.mean((w @ x + y)**2)), 5)

    def test_declared_linear_preactivation_alias(self):
        p = Program()
        a = p.vector_type("a")
        x, y = p.roots(a, ["x", "y"], [[1, F(1, 2)], [F(1, 2), 2]])
        z = x + 2 * y
        dag = p.compile(p.mean(p.phi(z)**2), preactivations=[z])
        self.assertEqual(len(dag.expectations), 1)
        moment = dag.expectations[0]
        self.assertEqual(moment.covariance, ((ex.const(11),),))
        self.assertEqual(moment.integrand, ex.phi(moment.coordinates[0])**2)

    def test_initialization_normal_form_rejects_nonlinear_or_shifted_arguments(self):
        p = Program()
        a = p.vector_type("a")
        x = p.root("x", a)
        for z in (x**2, x + 1):
            with self.subTest(node=z.index), self.assertRaises(ProgramError):
                p.compile(p.mean(p.phi(z)), preactivations=[z])
        with self.assertRaises(ProgramError):
            p.compile(p.mean(p.phi(x + 1)), preactivations=[x])

    def test_zero_dimensional_integral_keeps_output_polynomial(self):
        p = Program()
        kind = p.vector_type("neurons")
        s = p.parameter("s")
        dag = p.compile(p.mean(p.phi(p.broadcast(s, kind))))
        self.assertEqual(len(dag.expectations), 1)
        atom = dag.expectations[0]
        self.assertEqual(atom.coordinates, ())
        self.assertEqual(atom.covariance, ())
        self.assertEqual(atom.integrand, ex.phi(ex.symbol("s_s")))
        self.assertEqual(dag.output, atom.symbol)

    def test_causal_scalar_feedback_and_frozen_source_coefficients(self):
        p, a, _, w = self.matrix_setup()
        z = w @ p.one(a)
        c = p.mean(p.phi(z))
        v = w.T @ (c * p.phi(z))
        dag = p.compile(p.inner(v, v))
        g = ex.symbol("g_W_F_1")
        by_integrand = {node.integrand: node.symbol for node in dag.expectations}
        mean_phi = by_integrand[ex.phi(g)]
        q = by_integrand[ex.phi(g)**2]
        derivative = by_integrand[ex.phi(g, 1)]
        self.assertEqual(dag.output, ex.expand(mean_phi**2 * (q + derivative**2)))
        calls = [row for row in dag.trace if row["rule"] == "matrix source and response"]
        self.assertEqual(calls[-1]["response"][0]["formal_derivative"], ex.render(mean_phi * ex.phi(g, 1)))

    def test_nested_nonlinear_graph_stays_a_general_integral(self):
        p = Program()
        kind = p.vector_type("neurons")
        x = p.root("x", kind)
        first = p.mean(p.phi(x))
        dag = p.compile(p.mean(p.phi(first * p.phi(x))))
        self.assertEqual(len(dag.expectations), 2)
        one, two = dag.expectations
        self.assertEqual(two.integrand, ex.phi(one.symbol * ex.phi(ex.symbol("r_x"))))
        self.assertEqual(dag.output, two.symbol)
        self.assertEqual(two.covariance, ((ex.const(1),),))

    def test_linear_alias_does_not_replace_formal_source_slots(self):
        p, a, _, w = self.matrix_setup()
        x = p.root("x", a)
        y1, y2 = w @ x, w @ x
        z = y1 + y2
        dag = p.compile(p.inner(x, w.T @ p.phi(z)), preactivations=[z])
        atom = next(node for node in dag.expectations
                    if node.integrand == ex.phi(node.coordinates[0], 1))
        self.assertEqual(atom.covariance, ((ex.const(4),),))
        self.assertEqual(dag.output, 2 * atom.symbol)
        calls = [row for row in dag.trace if row["rule"] == "matrix source and response"]
        self.assertEqual(len(calls[-1]["response"]), 2)
        self.assertNotEqual(calls[-1]["response"][0]["source"], calls[-1]["response"][1]["source"])
        self.assertNotIn(ex.render(atom.coordinates[0]), calls[-1]["response"][0]["formal_derivative"])
        self.assertIn("g_W_F_1", calls[-1]["response"][0]["formal_derivative"])
        self.assertIn("g_W_F_2", calls[-1]["response"][0]["formal_derivative"])

    def test_two_layer_forward_backward_reuse(self):
        p, lower, middle, w = self.matrix_setup()
        upper = p.vector_type("upper")
        v = p.matrix("V", middle, upper)
        z = v @ (w @ p.one(lower))
        back = w.T @ (v.T @ z)
        self.assert_constant_limit(p.compile(p.inner(back, back)), 3)

    def test_optimizer_rejects_random_step_coefficients(self):
        p = Program()
        kind = p.vector_type("neurons")
        x = p.root("x", kind)
        loss = p.mean(x**2)
        with self.assertRaises(ProgramError):
            p.gradient_descent(loss, [x], step_size=p.mean(x))
        self.assertEqual(p.compile(p.directional(3, {})).output, ex.const(0))
        self.assertEqual(p.compile(p.at(3, {})).output, ex.const(3))

    def test_unsupported_types_directions_and_nonlinear_operations(self):
        p, a, b, w = self.matrix_setup()
        x, y = p.root("x", a), p.root("y", b)
        operations = [lambda: x + y, lambda: w @ y, lambda: w.T @ x,
                      lambda: p.matrix("square", a, a), lambda: p.mean(1),
                      lambda: p.phi(1), lambda: p.phi(x, -1), lambda: x / x,
                      lambda: x**F(1, 2), lambda: p.rank_one(x, x),
                      lambda: p.directional(p.mean(x), {w: w}),
                      lambda: p.directional(p.mean(x), {x: y}),
                      lambda: p.at(x, {x: y}), lambda: p.derivatives(x, {}, -1),
                      lambda: p.gradient_descent(p.mean(x), [x], steps=-1),
                      lambda: p.roots(a, ["bad1", "bad2"], [[1, 2], [2, 1]])]
        for operation in operations:
            with self.subTest(operation=operations.index(operation)), self.assertRaises(ProgramError):
                operation()
        q = Program()
        c = q.vector_type("c")
        with self.assertRaises(ProgramError):
            x + q.root("other", c)


if __name__ == "__main__":
    unittest.main()
