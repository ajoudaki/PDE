"""Exact finite-width checks using dense backpropagation and power series.

The oracle does not call Program gradient/directional/jets or mfp_expr.diff.
Its degree-two series multiply by ordinary coefficient convolution, and the
ODE coefficients follow theta[1] = V(theta[0]), theta[2] = V(theta)[1]/2.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import unittest

from pde import mfp_expr as ex
from pde.mfp_finite import evaluate_finite
from scripts.example_mfp_kernel_jets import build_example, compile_example


def quadratic_specialization(dag):
    """Evaluate generic activation atoms at phi(z)=z**2, after compilation."""
    def replace_phi(node):
        if node.op in ("const", "symbol"):
            return node
        values = [replace_phi(x) for x in node.args]
        if node.op == "phi":
            return (values[0]**2 if node.value == 0 else
                    2*values[0] if node.value == 1 else
                    ex.const(2) if node.value == 2 else ex.const(0))
        if node.op == "pow":
            return values[0]**node.value
        if node.op == "add":
            return sum(values, ex.const(0))
        result = ex.const(1)
        for value in values:
            result = result*value
        return result
    def no_integrals_left(expression):
        raise AssertionError("Polynomial specialization retained an integral")
    evaluated = {}
    for atom in dag.expectations:
        integrand = ex.substitute(replace_phi(atom.integrand), evaluated)
        covariance = {(a,b):ex.substitute(atom.covariance[i][j], evaluated)
                      for i,a in enumerate(atom.coordinates)
                      for j,b in enumerate(atom.coordinates)}
        evaluated[atom.symbol] = ex.gaussian_expectation(
            integrand, atom.coordinates, covariance, no_integrals_left)
    return ex.expand(ex.substitute(dag.output, evaluated))



@dataclass(frozen=True)
class Series:
    """Coefficients of 1, t, t**2; exact and factorial-normalized."""
    c: tuple

    def __post_init__(self):
        object.__setattr__(self, "c", tuple(F(value) for value in self.c))
        if len(self.c) != 3:
            raise ValueError("Three coefficients are required")

    @staticmethod
    def of(value):
        return value if isinstance(value, Series) else Series((value, 0, 0))

    def __add__(self, other):
        other = self.of(other)
        return Series(tuple(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Series(tuple(-value for value in self.c))

    def __sub__(self, other):
        return self + -self.of(other)

    def __mul__(self, other):
        other = self.of(other)
        return Series(tuple(sum(self.c[j] * other.c[k-j] for j in range(k+1))
                            for k in range(3)))

    __rmul__ = __mul__

    def __truediv__(self, divisor):
        return self * (F(1) / divisor)


def _fixture(n=2):
    """Actual stored weights, with no implicit matrix rescaling."""
    return {
        "U": (F(1, 2), F(-2, 3), F(3, 5))[:n],
        "V": (F(-3, 4), F(4, 5), F(2, 7))[:n],
        "W3": (F(2, 3), F(-3, 7), F(1, 4))[:n],
        "W2": tuple(tuple(F((-1)**(i+j) * (i+2*j+1), i+j+5)
                          for j in range(n)) for i in range(n)),
    }


PARAMETERS = dict(alpha=F(2, 3), beta=F(-3, 5), gamma=F(4, 7),
                  y1=F(5, 6), y2=F(-2, 5))


def _forward(state, parameters):
    n = len(state["U"])
    alpha, beta, gamma = (parameters[name] for name in ("alpha", "beta", "gamma"))
    z1 = [[alpha*u for u in state["U"]],
          [beta*u + gamma*v for u, v in zip(state["U"], state["V"])]]
    h1 = [[z*z for z in row] for row in z1]
    z2 = [[sum(state["W2"][i][j] * h[j] for j in range(n))
           for i in range(n)] for h in h1]
    h2 = [[z*z for z in row] for row in z2]
    f = [sum(w*h for w, h in zip(state["W3"], row))/n for row in h2]
    residual = [f[a] - parameters[f"y{a+1}"] for a in range(2)]
    return dict(z1=z1, h1=h1, z2=z2, h2=h2, f=f, residual=residual,
                loss=sum(r*r for r in residual)/4,
                kernel=sum(h2[0][i]*h2[1][i] for i in range(n))/n)


def _dense_flow(state, parameters):
    """Direct chain rule for L=sum_a(f_a-y_a)^2/4 and phi(z)=z*z.

    delta2 and delta1 are ordinary partial derivatives df_a/dz_a^(ell).
    U,V,W3 have mobility n, while W2 has mobility one.
    """
    n = len(state["U"])
    forward = _forward(state, parameters)
    delta2 = [[state["W3"][i]*2*forward["z2"][a][i]/n
               for i in range(n)] for a in range(2)]
    delta1 = [[2*forward["z1"][a][j]
               * sum(state["W2"][i][j]*delta2[a][i] for i in range(n))
               for j in range(n)] for a in range(2)]
    r = forward["residual"]
    return {
        "U": tuple(-F(n, 2)*(r[0]*parameters["alpha"]*delta1[0][j]
                               + r[1]*parameters["beta"]*delta1[1][j])
                   for j in range(n)),
        "V": tuple(-F(n, 2)*r[1]*parameters["gamma"]*delta1[1][j]
                   for j in range(n)),
        "W3": tuple(-sum(r[a]*forward["h2"][a][i] for a in range(2))/2
                    for i in range(n)),
        "W2": tuple(tuple(-sum(r[a]*delta2[a][i]*forward["h1"][a][j]
                                for a in range(2))/2 for j in range(n))
                    for i in range(n)),
    }


def _map_state(function, *states):
    n = len(states[0]["U"])
    result = {name: tuple(function(*(state[name][i] for state in states))
                          for i in range(n)) for name in ("U", "V", "W3")}
    result["W2"] = tuple(tuple(function(*(state["W2"][i][j] for state in states))
                               for j in range(n)) for i in range(n))
    return result


def _oracle_jets(state, parameters, moving=True):
    velocity = _dense_flow(state, parameters)
    straight_path = _map_state(lambda x, v: Series((x, v, 0)), state, velocity)
    if moving:
        field_on_path = _dense_flow(straight_path, parameters)
        path = _map_state(lambda x, v: Series((x.c[0], x.c[1], v.c[1]/2)),
                          straight_path, field_on_path)
    else:
        path = straight_path
    return _forward(path, parameters)["kernel"].c


def _quadratic_derivative(order, value):
    return (value*value if order == 0 else 2*value if order == 1
            else F(2) if order == 2 else F(0))


def _evaluator(network, parameter_nodes, state, values):
    def evaluate(node):
        return evaluate_finite(
            node, len(state["U"]),
            {network[name]: state[name] for name in ("U", "V", "W3")},
            {network["W2"]: state["W2"]},
            {parameter_nodes[name]: value for name, value in values.items()},
            activation=_quadratic_derivative,
        )
    return evaluate


def _finite_flow(network, flow, evaluate, n):
    result = {name: evaluate(flow[network[name]]) for name in ("U", "V", "W3")}
    represented = flow[network["W2"]]
    if represented.base is not None:
        raise AssertionError("The matrix velocity must be a pure rank sum")
    # Decode the documented represented matrix c*u*v.T/n, without differentiating.
    terms = [(evaluate(c), evaluate(u), evaluate(v)) for c, u, v in represented.terms]
    result["W2"] = tuple(tuple(sum(c*u[i]*v[j]/n for c, u, v in terms)
                               for j in range(n)) for i in range(n))
    return result


class SymbolicKernelJetsFiniteTests(unittest.TestCase):
    def test_all_trainable_blocks_and_loss_match_dense_backpropagation(self):
        for n in (2, 3):
            with self.subTest(width=n):
                _, parameters, network, flow = build_example("quadratic")
                state = _fixture(n)
                evaluate = _evaluator(network, parameters, state, PARAMETERS)
                self.assertEqual(set(flow), {network[k] for k in ("U", "V", "W2", "W3")})
                expected = _dense_flow(state, PARAMETERS)
                self.assertEqual(_finite_flow(network, flow, evaluate, n), expected)
                for block in ("U", "V", "W3"):
                    self.assertTrue(all(value != 0 for value in expected[block]))
                self.assertTrue(all(value != 0 for row in expected["W2"] for value in row))
                self.assertEqual(evaluate(network["loss"]), _forward(state, PARAMETERS)["loss"])

    def test_moving_jets_match_exact_ode_and_differ_from_straight_path(self):
        for activation in ("quadratic", "symbolic"):
            for n in (2, 3):
                with self.subTest(activation=activation, width=n):
                    program, parameters, network, flow = build_example(activation)
                    state = _fixture(n)
                    evaluate = _evaluator(network, parameters, state, PARAMETERS)
                    moving = tuple(evaluate(jet) for jet in program.jets(
                        network["kernel12"], flow, order=2, moving=True))
                    straight = tuple(evaluate(jet) for jet in program.jets(
                        network["kernel12"], flow, order=2, moving=False))
                    self.assertEqual(moving, _oracle_jets(state, PARAMETERS))
                    self.assertEqual(straight, _oracle_jets(state, PARAMETERS, moving=False))
                    self.assertEqual(moving[:2], straight[:2])
                    self.assertNotEqual(moving[2], straight[2])
                    self.assertTrue(all(isinstance(value, F) for value in moving))

    def test_symbolic_labels_and_zero_geometry(self):
        program, parameters, network, flow = build_example("symbolic")
        jets = program.jets(network["kernel12"], flow, order=2, moving=True)
        state = _fixture()
        label_change = dict(PARAMETERS, y1=F(-7, 4), y2=F(3, 8))
        evaluated = []
        for values in (PARAMETERS, label_change):
            evaluate = _evaluator(network, parameters, state, values)
            actual = tuple(evaluate(jet) for jet in jets)
            self.assertEqual(actual, _oracle_jets(state, values))
            evaluated.append(actual)
        self.assertEqual(evaluated[0][0], evaluated[1][0])
        self.assertNotEqual(evaluated[0][1], evaluated[1][1])
        self.assertNotEqual(evaluated[0][2], evaluated[1][2])
        zero_geometry = dict(label_change, alpha=F(0), beta=F(0), gamma=F(0))
        evaluate = _evaluator(network, parameters, state, zero_geometry)
        self.assertEqual(tuple(evaluate(jet) for jet in jets), (F(0), F(0), F(0)))
        self.assertEqual(_finite_flow(network, flow, evaluate, 2),
                         _map_state(lambda _: F(0), state))
        self.assertEqual(evaluate(network["loss"]),
                         (zero_geometry["y1"]**2 + zero_geometry["y2"]**2)/4)


class KernelGaussianTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results = {activation: compile_example(activation)
                       for activation in ("symbolic", "identity", "quadratic")}
        cls.alpha, cls.beta, cls.gamma, cls.y1, cls.y2 = [
            ex.symbol("s_" + name) for name in ("alpha", "beta", "gamma", "y1", "y2")]

    def test_first_jet_and_label_structure(self):
        y1, y2 = self.y1, self.y2
        for activation, dags in self.results.items():
            with self.subTest(activation=activation):
                self.assertEqual(dags[1].output, ex.const(0))
                for dag in dags:
                    for atom in dag.expectations:
                        self.assertFalse({y1, y2} & ex.symbols(atom.integrand))
                        self.assertFalse(any({y1, y2} & ex.symbols(c)
                                             for row in atom.covariance for c in row))
                second = dags[2].output
                zero = {y1: 0, y2: 0}
                c11 = ex.substitute(ex.diff(ex.diff(second, y1), y1)/2, zero)
                c12 = ex.substitute(ex.diff(ex.diff(second, y1), y2), zero)
                c22 = ex.substitute(ex.diff(ex.diff(second, y2), y2)/2, zero)
                self.assertEqual(ex.expand(second-c11*y1**2-c12*y1*y2-c22*y2**2), ex.const(0))

    def test_identity_independent_gaussian_target(self):
        g11, g12, g22 = self.alpha**2, self.alpha*self.beta, self.beta**2+self.gamma**2
        dags = self.results["identity"]
        self.assertEqual(dags[0].output, g12)
        # Independent linear-flow Gaussian identity for the half-mean-loss clock.
        expected = ex.const(9)/4*(g11*self.y1+g12*self.y2)*(g12*self.y1+g22*self.y2)
        self.assertEqual(ex.expand(dags[2].output-expected), ex.const(0))

    def test_quadratic_initial_kernel_and_compact_polynomial(self):
        g11, g12, g22 = self.alpha**2, self.alpha*self.beta, self.beta**2+self.gamma**2
        dags = self.results["quadratic"]
        # Two successive Gaussian fourth-moment identities give this initial kernel.
        expected = 9*g11**2*g22**2 + 2*(g11*g22+2*g12**2)**2
        self.assertEqual(ex.expand(dags[0].output-expected), ex.const(0))
        s = g11*g22
        A = 5815*s**2+11746*s*g12**2+16702*g12**4
        B = (4542*s**4+14636*s**3*g12**2+30788*s**2*g12**4
             +13856*s*g12**6+4704*g12**8)
        # Regression equality for the documented compact result; this check alone
        # is not an independent derivation of the long second-jet polynomial.
        expected = A*(g11**4*self.y1**2+g22**4*self.y2**2)+B*self.y1*self.y2
        self.assertEqual(ex.expand(dags[2].output-expected), ex.const(0))

    def test_generic_atoms_specialize_to_direct_quadratic_program(self):
        # Different compilation paths; their source-rule implementation is shared.
        for generic, polynomial in zip(self.results["symbolic"], self.results["quadratic"]):
            self.assertEqual(ex.expand(quadratic_specialization(generic)-polynomial.output), ex.const(0))


if __name__ == "__main__":
    unittest.main()
