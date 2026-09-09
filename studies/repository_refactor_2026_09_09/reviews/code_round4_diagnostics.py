"""Bounded independent audit cases; no original input is written.

Run from this snapshot root with PYTHONPATH=code and python -B.
Only Python's standard library, NumPy, and the snapshot package are used.
"""

from collections import Counter
from copy import deepcopy
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import ast
import importlib.util
import math
from pathlib import Path
import sys
import unittest

import numpy as np

from pde import (
    ARCTAN, IDENTITY, TANH, Activation, Parameters, backward, flow_velocity,
    forward, gaussian_moment, gd_step, kernel, kernel_blocks, loss, loss_gradients,
)


COUNTS = Counter()
ERRORS = {}


def arrays(state):
    return state.weights + (state.readout,)


def compare(name, actual, expected, rtol=3e-12, atol=3e-14):
    a, b = np.asarray(actual), np.asarray(expected)
    ERRORS[name] = max(ERRORS.get(name, 0.0), float(np.max(np.abs(a - b))))
    np.testing.assert_allclose(a, b, rtol=rtol, atol=atol)


def scalar_forward(weights, readout, inputs, functions, injection=None):
    """Independent scalar loops, supporting complex-step differentiation."""
    n, d, m = len(readout), len(inputs), len(inputs[0])
    zs, hs = [[] for _ in weights], [[] for _ in weights]
    outputs = []
    for a in range(m):
        h = [inputs[j][a] for j in range(d)]
        for ell, w in enumerate(weights):
            z = [sum(w[i][j] * h[j] for j in range(len(h))) for i in range(n)]
            if ell == 0:
                z = [v / math.sqrt(d) for v in z]
            if injection is not None and injection[:2] == (ell, a):
                z[injection[2]] += injection[3]
            h = [functions[ell](v) for v in z]
            zs[ell].append(z)
            hs[ell].append(h)
        outputs.append(sum(readout[i] * h[i] for i in range(n)) / n)
    return [np.array(z).T for z in zs], [np.array(h).T for h in hs], np.array(outputs)


def determinant(a):
    """Leibniz formula, independent of Schur elimination."""
    total = Q(0)
    for p in permutations(range(len(a))):
        inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
        term = Q((-1) ** inversions)
        for i, j in enumerate(p):
            term *= a[i][j]
        total += term
    return total


def psd_by_principal_minors(a):
    return all(determinant([[a[i][j] for j in subset] for i in subset]) >= 0
               for size in range(1, len(a) + 1)
               for subset in combinations(range(len(a)), size))


def latent_moment(a, powers):
    """Expand X=A Z as a polynomial; integrate independent Z coordinates."""
    rank = len(a[0])
    polynomial = {(0,) * rank: Q(1)}
    for row, power in zip(a, powers):
        for _ in range(power):
            next_polynomial = {}
            for monomial, coefficient in polynomial.items():
                for j, factor in enumerate(row):
                    if factor:
                        exponent = list(monomial)
                        exponent[j] += 1
                        exponent = tuple(exponent)
                        next_polynomial[exponent] = next_polynomial.get(exponent, Q(0)) + coefficient * factor
            polynomial = next_polynomial
    total = Q(0)
    for exponent, coefficient in polynomial.items():
        if any(p % 2 for p in exponent):
            continue
        for p in exponent:
            coefficient *= math.prod(range(1, p, 2))
        total += coefficient
    return total


class IndependentAudit(unittest.TestCase):
    def test_finite_gaussian_conditioning_constraints(self):
        # Compare the two-sided formula to a separate flattened linear system.
        n = 4
        directions = np.array([[1., 0., 0., 0.], [1., 1., 0., 0.],
                               [1., 0., 1., 0.], [1., 0., 0., 1.]])
        w = np.arange(16, dtype=float).reshape(4, 4) / 13 - .4
        for kv, ku in product((0, 1, 2, 4), repeat=2):
            v, u = directions[:, :kv], directions[::-1, :ku]
            y, r = w @ v, w.T @ u
            vp = np.linalg.solve(v.T @ v, v.T) if kv else np.zeros((0, n))
            up = np.linalg.solve(u.T @ u, u.T) if ku else np.zeros((0, n))
            pv, pu = v @ vp, u @ up
            mean = y @ vp + up.T @ r.T @ (np.eye(n) - pv)
            compare("conditioning forward constraints", mean @ v, y) if kv else None
            compare("conditioning transpose constraints", mean.T @ u, r) if ku else None
            def observations(a):
                return np.r_[(a @ v).ravel(), (a.T @ u).ravel()]
            basis = np.eye(n*n).reshape(n*n, n, n)
            h = np.stack([observations(a) for a in basis], axis=1)
            answer = observations(w)
            flat_mean = np.linalg.lstsq(h, answer, rcond=None)[0]
            compare("conditioning mean", mean.ravel(), flat_mean)
            null_projector = np.eye(n*n) - np.linalg.pinv(h) @ h
            compare("conditioning covariance", np.kron(np.eye(n) - pu, np.eye(n) - pv) / n,
                    null_projector / n)
            COUNTS["conditioning transcripts"] += 1
        # Section 1: row-sum observation, g(y)=y^2-1, reused transpose.
        y = w @ np.ones(n)
        g = y*y - 1
        mean = np.outer(y, np.ones(n)) / n
        p = np.eye(n) - np.ones((n, n)) / n
        compare("one-call response", mean.T @ g, np.full(n, y @ g / n))
        compare("one-call covariance", p @ (np.eye(n) * (g @ g / n)) @ p,
                (g @ g / n) * p)

    def test_scalar_oracle_all_finite_dynamics(self):
        # Non-unit norms, one zero, duplicates, opposites and dependent columns.
        x = np.array([[0, 1, -1, 1, 2, .3, -.6],
                      [0, .2, -.2, .2, .4, 1.1, -2.2],
                      [0, -.5, .5, -.5, -1, .7, -1.4],
                      [0, 0, 0, 0, 0, 0, 0]], dtype=float)
        y = np.array([.8, -.2, .5, .9, -1.2, .4, -.7])
        nonlinear = Activation("quadratic", lambda z: .2 + z + .1 * z*z,
                                lambda z: 1 + .2*z)
        choices = (ARCTAN, nonlinear, TANH, IDENTITY)
        functions = (np.arctan, lambda z: .2 + z + .1*z*z, np.tanh, lambda z: z)
        epsilon = 1e-30
        for n, depth in ((1, 1), (2, 4), (3, 5), (1, 7)):
            weights = tuple(np.array([[(((i+1)*3 + (j+1)*5 + ell*2) % 13 - 6) / 23
                                        for j in range(4 if ell == 0 else n)] for i in range(n)])
                            for ell in range(depth))
            state = Parameters(weights, np.array([(i+1)/5 - .41 for i in range(n)]))
            activations = tuple(choices[ell % 4] for ell in range(depth))
            funcs = tuple(functions[ell % 4] for ell in range(depth))
            zs, hs, f = scalar_forward(weights, state.readout, x, funcs)
            actual = forward(state, x, activations)
            for z, h, az, ah in zip(zs, hs, actual.preactivations, actual.hidden):
                compare("preactivation", az, z)
                compare("hidden", ah, h)
            compare("forward", actual.output, f)
            r = f - y
            compare("loss", loss(state, x, y, activations), sum(v*v for v in r) / len(y))
            deltas = backward(state, x, activations)
            for ell in range(depth):
                oracle = np.zeros((n, len(y)))
                for a in range(len(y)):
                    for i in range(n):
                        _, _, injected = scalar_forward(weights, state.readout, x, funcs,
                                                         (ell, a, i, 1j * epsilon))
                        oracle[i, a] = n * injected[a].imag / epsilon
                        COUNTS["preactivation directions"] += 1
                compare("backward", deltas[ell], oracle)
            kappas = np.array([.17 + (ell + 1) / 9 for ell in range(depth + 1)])
            mobility = kappas.copy()
            mobility[[0, -1]] *= n
            gs = arrays(loss_gradients(state, x, y, activations))
            vs = arrays(flow_velocity(state, x, y, activations, kappas=kappas))
            step = .037
            updated = arrays(gd_step(state, x, y, step, activations, kappas=kappas))
            kb = kernel_blocks(state, x, activations, kappas=kappas)
            fdot = np.zeros(len(y))
            energy = 0.0
            for ell, block in enumerate(arrays(state)):
                jacobian = []
                for index in np.ndindex(block.shape):
                    changed = [b.astype(complex) for b in arrays(state)]
                    changed[ell][index] += 1j * epsilon
                    _, _, perturbed = scalar_forward(changed[:-1], changed[-1], x, funcs)
                    jacobian.append(perturbed.imag / epsilon)
                    COUNTS["parameter directions"] += 1
                j = np.array(jacobian).T
                grad = (2 * (j.T @ r) / len(y)).reshape(block.shape)
                velocity = -mobility[ell] * grad
                compare("gradient", gs[ell], grad)
                compare("flow", vs[ell], velocity)
                compare("GD", updated[ell], block + step * velocity)
                compare("kernel block", kb[ell], mobility[ell] * j @ j.T)
                self.assertGreaterEqual(np.linalg.eigvalsh(kb[ell])[0], -1e-13)
                fdot += j @ velocity.reshape(-1)
                energy += np.sum(velocity**2) / mobility[ell]
                COUNTS["kernel blocks"] += 1
            total = kernel(state, x, activations, kappas=kappas)
            compare("total kernel", total, sum(kb))
            compare("output flow identity", fdot, -2 * total @ r / len(y))
            compare("energy identity", energy, 4 * r @ total @ r / len(y)**2)
            compare("loss directional derivative", 2 * r @ fdot / len(y), -energy)
            for old, new in zip(arrays(state), updated):
                self.assertFalse(np.shares_memory(old, new))
            COUNTS["finite network cases"] += 1

    def test_exact_psd_against_all_principal_minors(self):
        matrices = []
        for entries in product((-1, 0, 1), repeat=6):
            a, b, c, d, e, f = entries
            matrices.append([[a, b, c], [b, d, e], [c, e, f]])
        tiny = Q(1, 10**60)
        for offset in (-tiny, Q(0), tiny):
            a = [[1, 1, 0], [1, 1 + offset, 0], [0, 0, 0]]
            matrices.extend([[a[i][j] for j in p] for i in p] for p in permutations(range(3)))
        # All proper principal minors positive, determinant negative.
        matrices.append([[1, Q(-3, 4), Q(-3, 4)],
                         [Q(-3, 4), 1, Q(-3, 4)], [Q(-3, 4), Q(-3, 4), 1]])
        for a in matrices:
            expected = psd_by_principal_minors(a)
            COUNTS["PSD accepted matrices" if expected else "PSD rejected matrices"] += 1
            for powers in ([0, 0, 0], [1, 0, 0], [2, 0, 0]):
                if expected:
                    self.assertIsInstance(gaussian_moment(a, powers), Q)
                else:
                    with self.assertRaises(ValueError):
                        gaussian_moment(a, powers)
                COUNTS["PSD API checks"] += 1

    def test_exact_moments_by_independent_latent_expansion(self):
        factors = (
            [[Q(1), Q(0)], [Q(-2), Q(0)], [Q(0), Q(0)]],
            [[Q(1), Q(1, 2)], [Q(-1, 3), Q(2)], [Q(2), Q(-1)]],
            [[Q(0), Q(0)], [Q(1, 7), Q(0)], [Q(-1), Q(2, 3)]],
            [[Q(1), Q(0), Q(1, 3)], [Q(0), Q(2), Q(-1)],
             [Q(1), Q(-1), Q(0)], [Q(0), Q(0), Q(0)]],
        )
        for a in factors:
            sigma = [[sum(u*v for u, v in zip(row, other)) for other in a] for row in a]
            cap = 8 if len(a) == 3 else 6
            for powers in product(range(cap + 1), repeat=len(a)):
                if sum(powers) > cap:
                    continue
                saved = deepcopy(sigma)
                value = gaussian_moment(sigma, powers)
                self.assertEqual(value, latent_moment(a, powers))
                self.assertIsInstance(value, Q)
                self.assertEqual(sigma, saved)
                COUNTS["exact latent moment cases"] += 1

    def test_callback_buffers_readonly_inputs_and_aliases(self):
        scratch = np.empty((2, 3))
        captured = []
        def value(z):
            captured.append(z)
            z *= z
            np.copyto(scratch, z)
            return scratch
        def derivative(z):
            captured.append(z)
            z *= 2
            np.copyto(scratch, z)
            return scratch
        buffered = Activation("buffered_square", value, derivative)
        pure = Activation("square", lambda z: z*z, lambda z: 2*z)
        base = np.array([[.1, .2], [.3, .4]])
        state = Parameters((base.T, base), base[0])
        self.assertTrue(np.shares_memory(state.weights[0], base))
        self.assertTrue(np.shares_memory(state.readout, base))
        x = np.array([[1., 0., -1.], [.2, .3, -.2]])[:, ::-1]
        y = np.array([1., -.4, .2])
        rates = np.array([.3, 1.1, .7])
        saved = tuple(a.copy() for a in (*arrays(state), x, y, rates))
        for a in (*arrays(state), x, y, rates):
            a.flags.writeable = False
        operations = (
            lambda a: (forward(state, x, a).output,),
            lambda a: backward(state, x, a),
            lambda a: (loss(state, x, y, a),),
            lambda a: arrays(loss_gradients(state, x, y, a)),
            lambda a: arrays(flow_velocity(state, x, y, a, kappas=rates)),
            lambda a: arrays(gd_step(state, x, y, .2, a, kappas=rates)),
            lambda a: (kernel_blocks(state, x, a, kappas=rates),),
            lambda a: (kernel(state, x, a, kappas=rates),),
        )
        for operation in operations:
            actual, expected = operation(buffered), operation(pure)
            frozen = [np.array(a, copy=True) for a in actual]
            for a, b in zip(actual, expected):
                compare("buffer callbacks", a, b)
            scratch.fill(999)
            for private in captured:
                private.fill(-999)
            for a, b in zip(actual, frozen):
                np.testing.assert_array_equal(a, b)
            COUNTS["ownership API cases"] += 1
        for original, copy in zip((*arrays(state), x, y, rates), saved):
            np.testing.assert_array_equal(original, copy)
        def unused(z):
            raise AssertionError("zero step evaluated callback")
        poison = Activation("unused", unused, unused)
        zero = gd_step(state, x, y, 0, poison, kappas=rates)
        for result, original in zip(arrays(zero), arrays(state)):
            np.testing.assert_array_equal(result, original)
            self.assertFalse(np.shares_memory(result, original))
        for bad_kwargs in ({"inputs": np.empty((2, 0))}, {"labels": [0]},
                           {"kappas": [1, 0, 1]}, {"activation": [poison]}):
            kwargs = dict(inputs=x, labels=y, kappas=rates, activation=poison)
            kwargs.update(bad_kwargs)
            with self.assertRaises(ValueError):
                gd_step(state, eta=0, **kwargs)

    def test_float64_binary_scale_extremes(self):
        # All raw contractions/Grams are exact powers of two in range.
        for exponent in (-537, -500, -10, 0, 10, 500, 511):
            weight = math.ldexp(1., exponent)
            rate = math.ldexp(1., max(-1022, min(1023, -2 * exponent)))
            state = Parameters(([[weight]],), [0.])
            actual = kernel_blocks(state, [[1., -1.]], IDENTITY, kappas=[1., rate])
            exact = float(Q.from_float(rate) * Q.from_float(weight)**2)
            np.testing.assert_array_equal(actual[1], exact * np.array([[1., -1.], [-1., 1.]]))
            COUNTS["binary scale cases"] += 1
        # Scaled MSE is finite even when one residual square would overflow.
        state = Parameters(([[0.]],), [0.])
        big = math.ldexp(1., 512)
        self.assertEqual(loss(state, [[1., 1.]], [big, 0.], IDENTITY), math.ldexp(1., 1023))
        # Raw-matmul overflow/underflow remains a documented limitation.
        with np.errstate(all="ignore"):
            with self.assertRaises(ValueError):
                forward(Parameters(([[math.ldexp(1., 1023)]],), [0.]), [[4.]], IDENTITY)
            vanished = kernel_blocks(Parameters(([[math.ldexp(1., -538)]],), [0.]),
                                     [[1.]], IDENTITY, kappas=[1., math.ldexp(1., 1023)])
            self.assertEqual(vanished[1, 0, 0], 0.)

    def test_gaussian_module_without_numpy_or_package_initialization(self):
        # Direct standalone loading with a guard on imports made by this module.
        import builtins
        original = builtins.__import__
        observed = []
        def guarded(name, *args, **kwargs):
            observed.append(name)
            if name.split('.')[0] in {"numpy", "pde"}:
                raise AssertionError("standalone Gaussian module imported " + name)
            return original(name, *args, **kwargs)
        spec = importlib.util.spec_from_file_location("audited_gaussian", "code/pde/gaussian_moments.py")
        module = importlib.util.module_from_spec(spec)
        builtins.__import__ = guarded
        try:
            spec.loader.exec_module(module)
            self.assertEqual(module.gaussian_moment([[1, -1], [-1, 1]], [3, 3]), -15)
        finally:
            builtins.__import__ = original
        self.assertTrue(observed)
        # Actual implementation imports: no external research/data dependencies.
        for path in sorted(Path("code/pde").glob("*.py")):
            tree = ast.parse(path.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.assertIn(alias.name.split('.')[0], sys.stdlib_module_names | {"numpy"})
            COUNTS["implementation modules inspected"] += 1


if __name__ == "__main__":
    result = unittest.main(verbosity=2, exit=False)
    print("CASE_COUNTS", dict(sorted(COUNTS.items())))
    print("MAX_ABSOLUTE_ERRORS", dict(sorted(ERRORS.items())))
    raise SystemExit(not result.result.wasSuccessful())
