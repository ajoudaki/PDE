"""Independent finite backpropagation and Gaussian oracles for the MLP recipe."""
from fractions import Fraction as F
import unittest

import mfp_expr as ex
from mfp_finite import evaluate_finite
from mlp_derivative_example import build_mlp, compile_examples


class MLPExampleTests(unittest.TestCase):
    def test_cubic_forward_and_first_gradient_against_explicit_arrays(self):
        p, net, grad, obs = build_mlp("cubic")
        w1 = [F(1, 2), F(-2, 3)]
        w2 = [[F(1, 3), F(2, 5)], [F(-1, 4), F(3, 7)]]
        w3 = [F(4, 5), F(-3, 2)]
        n = len(w1)
        h1 = [x**3 for x in w1]
        z2 = [sum(row[j]*h1[j] for j in range(n)) for row in w2]
        h2 = [x**3 for x in z2]
        prediction = sum(w3[i]*h2[i] for i in range(n))/n
        # Direct finite differential of f: delta2=W3*phi'(z2),
        # n*grad_W1 f=phi'(W1)*(W2.T delta2).
        delta2 = [w3[i]*3*z2[i]**2 for i in range(n)]
        b1 = [3*w1[j]**2*sum(w2[i][j]*delta2[i] for i in range(n)) for j in range(n)]
        g2 = [[delta2[i]*h1[j]/n for j in range(n)] for i in range(n)]
        first = sum(x*x for x in b1)/n
        full = first + sum(x*x for row in g2 for x in row) + sum(x*x for x in h2)/n
        def finite(node):
            return evaluate_finite(node,n,{net["W1"]:w1,net["W3"]:w3},{net["W2"]:w2})
        self.assertEqual(finite(net["f"]), prediction)
        self.assertEqual(finite(grad[net["W1"]]), tuple(b1))
        self.assertEqual(finite(obs["first_layer_derivative_energy"]), first)
        self.assertEqual(finite(obs["all_parameter_metric_norm"]), full)
        # An output derivative along its metric gradient is that same scalar.
        self.assertEqual(finite(p.directional(net["f"],grad)), full)

    def test_generic_gaussian_covariance_and_derivative_moments(self):
        dag = compile_examples()["first_layer_derivative_energy"]
        self.assertEqual(len(dag.expectations),3)
        q, derivative2, derivative1 = dag.expectations
        g, z = ex.symbol("r_W1"), ex.symbol("g_W2_F_1")
        self.assertEqual(q.integrand,ex.phi(g)**2)
        self.assertEqual(q.covariance,((ex.const(1),),))
        self.assertEqual(derivative2.integrand,ex.phi(z,1)**2)
        self.assertEqual(derivative2.covariance,((q.symbol,),))
        self.assertEqual(derivative1.integrand,ex.phi(g,1)**2)
        self.assertEqual(dag.output,derivative1.symbol*derivative2.symbol)

    def test_closed_gaussian_specializations(self):
        # Identity: q1=q2=s1=s2=1. Cubic: q1=15, q2=15*15^3,
        # s1=9*E[G^4]=27, s2=9*3*15^2=6075.
        for activation,first,full in (("identity",1,3),("cubic",164025,305775)):
            with self.subTest(activation=activation):
                dags=compile_examples(activation)
                self.assertEqual(dags["mean_first_layer_derivative"].output,ex.const(0))
                self.assertEqual(dags["first_layer_derivative_energy"].output,ex.const(first))
                self.assertEqual(dags["all_parameter_metric_norm"].output,ex.const(full))
                self.assertTrue(all(not dag.expectations for dag in dags.values()))

    def test_generic_mean_gradient_vanishes_for_centered_readout(self):
        self.assertEqual(compile_examples()["mean_first_layer_derivative"].output,ex.const(0))


if __name__ == "__main__":
    unittest.main()
