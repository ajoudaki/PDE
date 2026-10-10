"""Small deterministic algebra/operation checks, not approximation experiments."""
import math
import unittest

import numpy as np
import torch

import compression_core as c


class CompressionChecks(unittest.TestCase):
    def setUp(self):
        self.inputs = torch.tensor([[1., 0.], [.6, .8]], dtype=torch.float64)
        self.labels = torch.tensor([.1, -.08], dtype=torch.float64)
        self.queries = torch.tensor([[0., 1.], [-.8, .6]], dtype=torch.float64)

    def close(self, left, right, atol=2e-11, rtol=2e-10):
        torch.testing.assert_close(left, right, atol=atol, rtol=rtol)

    def selected(self, depth=3):
        dense = c.Dense(48, 2, depth=depth, seed=17)
        sources, report = c.initial_jets(dense, self.inputs, self.labels, self.queries, rank=1)
        selected = c.Selected(dense, self.inputs, self.labels, sources, budget=32, source_info=report)
        return dense, selected

    def test_dense_autograd_mobilities_all_activations(self):
        for activation in c.DEEP_ACTIVATIONS:
            for depth in (1, 2, 3):
                with self.subTest(activation=activation, depth=depth):
                    model = c.Dense(7, 2, depth, activation, seed=12, readout='small_gaussian')
                    state = [v.clone().requires_grad_() for v in model.initial_state]
                    loss = (model.predict(state, self.inputs)-self.labels).square().mean()
                    gradients = torch.autograd.grad(loss, state)
                    velocity = model.rhs(state, self.inputs, self.labels)
                    mobility = [7, 7]+[1]*(depth-1)
                    for v, g, rate in zip(velocity, gradients, mobility):
                        self.close(v, -rate*g)
                    dissipation = sum((v.square()/rate).sum() for v, rate in zip(velocity, mobility))
                    derivative = sum((v*g).sum() for v, g in zip(velocity, gradients))
                    self.close(derivative, -dissipation)

    def test_readout_conventions_and_rng(self):
        before = torch.random.get_rng_state().clone()
        zero = c.Dense(9, 2, seed=7)
        small = c.Dense(9, 2, seed=7, readout='small_gaussian')
        self.assertTrue(torch.equal(before, torch.random.get_rng_state()))
        self.close(zero.initial_state[0], small.initial_state[0])
        self.close(zero.initial_state[2], small.initial_state[2])
        self.assertEqual(float(zero.initial_state[1].norm()), 0.)
        self.assertGreater(float(small.initial_state[1].norm()), 0.)
        for constructor in (lambda: c.Legendre(small, self.inputs, self.labels, 2),
                            lambda: c.Selected(small, self.inputs, self.labels, budget=9)):
            with self.assertRaises(ValueError):
                constructor()

    def test_legendre_projection_and_transport(self):
        dense = c.Dense(3, 2, seed=4)
        model = c.Legendre(dense, self.inputs, self.labels, 4)
        nodes, weights = np.polynomial.legendre.leggauss(12)
        def moments(tau):
            x = tau*(nodes+1)/2
            history = np.stack((1+x+2*x*x, x*x*x), axis=1)
            polynomials = np.polynomial.legendre.legvander(nodes, 3)
            return torch.tensor(np.einsum('x,xj,xk->jk', weights*tau/2, polynomials, history))[:, :, None]
        tau, rho, eps = 1.7, .23, 1e-6
        endpoint = torch.tensor([[1+tau+2*tau*tau], [tau**3]], dtype=torch.float64)
        velocity = model._transport(moments(tau), rho*endpoint, rho, tau)
        finite_difference = rho*(moments(tau+eps)-moments(tau-eps))/(2*eps)
        self.close(velocity, finite_difference, atol=3e-9)
        projected_pair = sum((2*j+1)*moments(tau)[j]@moments(tau)[j].T/tau for j in range(4))
        x = tau*(nodes+1)/2
        history = np.stack((1+x+2*x*x, x*x*x), axis=1)
        exact_pair = torch.tensor(np.einsum('x,xi,xj->ij', weights*tau/2, history, history))
        self.close(projected_pair, exact_pair)

    def test_legendre_initialization_and_reconstruction(self):
        dense = c.Dense(8, 2, depth=3, activation='atan', seed=9)
        model = c.Legendre(dense, self.inputs, self.labels, 3)
        dense_rhs = dense.rhs(dense.initial_state, self.inputs, self.labels)
        velocity = model.rhs(model.initial_state, self.inputs, self.labels)
        self.close(velocity[0], dense_rhs[0])
        self.close(velocity[1], dense_rhs[1])
        self.close(velocity[2], self.labels.square().mean().sqrt())
        generator = torch.Generator().manual_seed(5)
        state = [v+.01*torch.randn(v.shape, generator=generator, dtype=v.dtype) for v in model.initial_state]
        reference = state[:2]
        for layer in range(2, 4):
            left, right = model.factors(state, layer)
            matrix = model.mixers[layer-2]+left@right.T
            reference.append(matrix)
            value = torch.randn(8, 3, generator=generator, dtype=torch.float64)
            self.close(model.apply_hidden(state, layer, value), matrix@value)
            self.close(model.apply_hidden(state, layer, value, transpose=True), matrix.T@value)
        self.close(model.predict(state, self.queries), dense.predict(reference, self.queries))
        expected = 8*3+1+2*2*2*8*3
        self.assertEqual(c.storage(model)['moving'], expected)

    def test_legendre_nonzero_residual_defect_identity(self):
        dense = c.Dense(6, 2, depth=3, seed=11)
        model = c.Legendre(dense, self.inputs, self.labels, 3)
        generator = torch.Generator().manual_seed(29)
        state = tuple(v+.03*torch.randn(v.shape, generator=generator, dtype=v.dtype)
                      for v in model.initial_state)
        velocity = tuple(model.rhs(state, self.inputs, self.labels))
        hs, gates = model.fields(state, self.inputs)
        deltas = [None]*3
        deltas[-1] = state[1][:, None]*gates[-1]
        for j in (1, 0):
            deltas[j] = gates[j]*model.apply_hidden(state, j+2, deltas[j+1], transpose=True)
        residual = state[1]@hs[-1]/6-self.labels
        rho = residual.square().mean().sqrt()
        self.assertGreater(float(rho), 0)
        weights = torch.tensor([1., 3., 5.], dtype=torch.float64)[:, None, None]
        for layer in (2, 3):
            def reconstructed(*s):
                left, right = model.factors(s, layer)
                return model.mixers[layer-2]+left@right.T
            _, derivative = torch.autograd.functional.jvp(reconstructed, state, velocity)
            j = layer-2
            backward_error = deltas[j+1]*residual/rho-(weights*state[3+2*j]).sum(0)/state[2]
            forward_error = hs[j]-(weights*state[4+2*j]).sum(0)/state[2]
            expected = -(2/(2*6))*(deltas[j+1]*residual)@hs[j].T
            expected += (2*rho/(2*6))*backward_error@forward_error.T
            self.close(derivative, expected)

    def test_bss_metric_and_budgeted_metric(self):
        generator = torch.Generator().manual_seed(41)
        mandatory = torch.cat((torch.ones(64, 1, dtype=torch.float64),
                                torch.randn(64, 3, generator=generator, dtype=torch.float64)), 1)
        basis, _ = c._harmonic_source_basis(mandatory, mandatory[:, :0])
        for selector in (lambda: c._harmonic_bss_metric(basis),
                         lambda: c.coordinate_metric(basis, 24, seed=3)):
            indices, metric, inverse, diagonal, info = selector()
            self.assertLess(len(indices), 64)
            self.close(basis[indices].T@metric@basis[indices], torch.eye(4, dtype=torch.float64))
            self.close(metric@inverse, torch.eye(len(indices), dtype=torch.float64))
            self.close(metric.sum(), torch.tensor(1., dtype=torch.float64))
            factor = info['embedding_max']
            self.assertGreater(float(torch.linalg.eigvalsh(metric-torch.diag(diagonal)/factor).min()), -1e-11)
            self.assertGreater(float(torch.linalg.eigvalsh(torch.diag(diagonal)-metric).min()), -1e-11)
        with self.assertRaises(ValueError):
            c.coordinate_metric(basis, 2)

    def test_selected_compressed_pairing_and_training_identity(self):
        _, model = self.selected()
        self.assertTrue(all(width < 48 for width in model.diagnostics['widths']))
        for key in ('initialized_feature_errors', 'paired_forward_action_errors', 'paired_reverse_action_errors'):
            self.assertLess(max(model.diagnostics[key]), 2e-11)
        state = c.step(model, model.initial_state, self.inputs, self.labels, .02)
        state[-1] = .37*self.labels
        state[1] = state[1]+.03
        self.close(model.predict(state, self.inputs, self.inputs, self.labels), self.labels-state[-1])
        # Ordinary transpose is not substituted for the metric adjoint.
        v, u = state[0], torch.ones((state[2].shape[0], 2), dtype=torch.float64)
        adjoint_u = model.metric_inverses[0]@state[2].T@model.metrics[1]@u
        self.close((state[2]@v* (model.metrics[1]@u)).sum(), (v*(model.metrics[0]@adjoint_u)).sum())

    def test_selected_energy_identity_at_compressed_nonzero_state(self):
        _, model = self.selected()
        state, _ = c.rollout(model, self.inputs, self.labels, [.05], step_size=.01)
        velocity = model.rhs(state, self.inputs, self.labels)
        norm2 = (velocity[0]*(model.metrics[0]@velocity[0])).sum()
        norm2 += velocity[1]@model.metrics[-1]@velocity[1]
        for j in range(1, model.depth):
            norm2 += torch.trace(model.metrics[j]@velocity[j+1]@model.metric_inverses[j-1]@velocity[j+1].T)
        energy_derivative = (2/len(self.labels))*state[-1]@velocity[-1]
        self.close(energy_derivative, -norm2)
        kernel = model.kernel(state, self.inputs, self.labels)[0]
        self.close(kernel, kernel.T)
        self.assertGreaterEqual(float(torch.linalg.eigvalsh(kernel).min()), -1e-12)

    def test_selected_rejects_dependent_training_features(self):
        # Duplicate and distinct antipodal inputs both give dependent tanh
        # features. Some singular Grams nevertheless pass cholesky_ex.
        for seed in (0, 1, 10):
            for second in ((1., 0.), (-1., 0.), (0., 0.), (1., 1e-10)):
                with self.subTest(seed=seed, second=second):
                    dense = c.Dense(12, 2, seed=seed)
                    inputs = torch.tensor([[1., 0.], second], dtype=torch.float64)
                    with self.assertRaisesRegex(ArithmeticError, 'rank deficient'):
                        c.Selected(dense, inputs, self.labels, budget=12)

    def test_selected_gram_check_is_relative_and_repeated(self):
        dense = c.Dense(12, 2, depth=1, seed=0)
        dense.initial_state[0] *= 1e-6
        model = c.Selected(dense, self.inputs, self.labels, budget=12)
        state = [v.clone() for v in model.initial_state]
        state[-1].zero_()
        self.close(model.predict(state, self.inputs, self.inputs, self.labels), self.labels)
        state[0].zero_()
        with self.assertRaisesRegex(ArithmeticError, 'rank deficient'):
            model.predict(state, self.inputs, self.inputs, self.labels)

    def test_full_retention_vector_field_matches_dense_on_compatible_state(self):
        dense = c.Dense(9, 2, depth=3, activation='softplus', seed=4)
        model = c.Selected(dense, self.inputs, self.labels, budget=9)
        state = tuple(v+.003 for v in dense.initial_state)
        deficit = self.labels-dense.predict(state, self.inputs)
        dense_rhs = dense.rhs(state, self.inputs, self.labels)
        selected_rhs = model.rhs([*state, deficit], self.inputs, self.labels)
        for a, b in zip(dense_rhs, selected_rhs[:-1]):
            self.close(a, b)
        _, f_dot = torch.autograd.functional.jvp(lambda *v: dense.predict(v, self.inputs), state, tuple(dense_rhs))
        self.close(selected_rhs[-1], -f_dot)

    def test_origin_jet_span_by_independent_autodiff(self):
        for depth, activation in ((2, 'tanh'), (3, 'softplus')):
            dense = c.Dense(10, 2, depth=depth, activation=activation, seed=8)
            sources, report = c.initial_jets(dense, self.inputs, self.labels, self.queries, rank=10)
            state = tuple(dense.initial_state)
            panel = torch.cat((self.inputs, self.queries))
            def fields(*theta):
                hs, gates = dense.fields(theta, panel)
                deltas = dense.backward(theta, [h[:, :2] for h in hs], [g[:, :2] for g in gates])
                return tuple(hs+deltas)
            def first_derivative(*theta):
                flow = tuple(dense.rhs(theta, self.inputs, self.labels))
                return torch.autograd.functional.jvp(fields, theta, flow, create_graph=True)[1]
            flow = tuple(dense.rhs(state, self.inputs, self.labels))
            first, second = torch.autograd.functional.jvp(first_derivative, state, flow)
            initial = fields(*state)
            for index in range(2*depth):
                family, j = ('h', index) if index < depth else ('delta', index-depth)
                pieces = [sources[family][j]]
                if family == 'h':
                    pieces.append(initial[j][:, :2])
                    if j == depth-1:
                        pieces.extend((torch.ones(10, 1, dtype=torch.float64), state[j+1]@initial[j-1][:, :2]))
                elif j == 0:
                    pieces.extend((torch.ones(10, 1, dtype=torch.float64), state[0], initial[0][:, :2]))
                generators = torch.cat(pieces, 1)
                basis, _ = c._harmonic_source_basis(generators, generators[:, :0])
                for derivative in (first[index], second[index]):
                    self.close(derivative, basis@(basis.T@derivative)/10, atol=1e-10)
            self.assertTrue(report['initialization_only'])
            self.assertEqual(report['dense_rhs_calls'], 0)

    def test_harmonic_quadrature_projection(self):
        for dimension in (2, 3):
            nodes, weights, spatial = c._unified_harmonic_geometry(dimension, 4)
            self.close(nodes.square().sum(1), torch.ones(len(nodes), dtype=torch.float64))
            self.close(spatial.T@(weights[:, None]*spatial), torch.eye(spatial.shape[1], dtype=torch.float64))
            coefficients = torch.arange(spatial.shape[1], dtype=torch.float64).cos()
            self.close((coefficients@spatial.T)@(weights[:, None]*spatial), coefficients)

    def test_all_three_method_rollouts_and_source_provenance(self):
        dense = c.Dense(48, 2, depth=3, seed=17)
        harmonic = c.harmonic(dense, self.inputs, self.labels, horizon=.04, step_size=.01,
                             rank=1, time_degree=2, spatial_degree=2, budget=32)
        taylor = c.taylor(dense, self.inputs, self.labels, self.queries, source_mode='rollout',
                         horizon=.04, step_size=.01, rank=1, time_degree=2, budget=32)
        for model in (c.Legendre(dense, self.inputs, self.labels, 3), harmonic, taylor):
            final, predictions = c.rollout(model, self.inputs, self.labels, [0., .02, .04],
                                          step_size=.01, queries=self.queries)
            self.assertEqual(predictions.shape, (3, 2))
            self.assertTrue(bool(torch.isfinite(predictions).all()))
            self.assertGreater(float(predictions[-1].norm()), 0.)
            self.assertEqual(len(final), len(model.initial_state))
        for model in (harmonic, taylor):
            source = model.provenance['source']
            self.assertFalse(source['initialization_only'])
            self.assertFalse(source['source_certificate'])
            self.assertFalse(source['stored_network_trajectory'])
            self.assertFalse(source['passive_labels_used'])
            self.assertGreater(source['dense_rhs_calls'], 0)
            self.assertNotIn('sources', vars(model))
            self.assertNotIn('dense', vars(model))

    def test_zero_labels_stationary_including_clock(self):
        dense = c.Dense(24, 2, seed=5)
        labels = torch.zeros_like(self.labels)
        for model in (dense, c.Legendre(dense, self.inputs, labels, 3),
                      c.taylor(dense, self.inputs, labels, self.queries, rank=1, budget=18)):
            velocity = model.rhs(model.initial_state, self.inputs, labels)
            self.assertTrue(all(bool(v.eq(0).all()) for v in velocity))
            final, _ = c.rollout(model, self.inputs, labels, [.1], step_size=.01)
            self.assertTrue(all(torch.equal(a, b) for a, b in zip(final, model.initial_state)))

    def test_step_schemes_restart_and_ownership(self):
        dense = c.Dense(7, 2, seed=8)
        before = [v.clone() for v in dense.initial_state]
        for method in ('euler', 'heun', 'rk4'):
            final, _ = c.rollout(dense, self.inputs, self.labels, [.02, .04], step_size=.01, method=method)
            middle, _ = c.rollout(dense, self.inputs, self.labels, [.02], step_size=.01, method=method)
            resumed, _ = c.rollout(dense, self.inputs, self.labels, [.04], step_size=.01,
                                  method=method, state=middle, start_time=.02)
            self.assertTrue(all(torch.equal(a, b) for a, b in zip(final, resumed)))
        self.assertTrue(all(torch.equal(a, b) for a, b in zip(before, dense.initial_state)))
        with self.assertRaises(ValueError):
            c.step(dense, before, self.inputs, self.labels, 0)

    def test_singular_selected_gram_rejected(self):
        dense = c.Dense(12, 2, seed=1)
        repeated = self.inputs[:1].repeat(2, 1)
        with self.assertRaises(ArithmeticError):
            c.Selected(dense, repeated, self.labels, budget=12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
