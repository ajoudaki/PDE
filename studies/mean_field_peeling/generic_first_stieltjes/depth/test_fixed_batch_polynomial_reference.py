"""Independent exact gates for the joint fixed-H/fixed-B GNF candidate."""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from ..b2.contracted_gnf_polynomial_reference import (
    evaluate_contracted_directional_gnf,
)
from ..compiler.normal_form import PolynomialActivation
from .fixed_batch_polynomial_reference import (
    evaluate_fixed_depth_batch_polynomial_gnf,
)
from .gnf_audit_reference import evaluate_depth_b1_audit_recurrence
from .test_exact_depth_program import polynomial_oracle


F = Fraction


def test_h2_reduces_blockwise_to_accepted_fixed_batch_gnf() -> None:
    q0 = [[1, F(1, 3)], [F(1, 3), F(4, 3)]]
    c = [F(2, 3), F(-1, 4)]
    for coefficients in ([1], [0, 1], [1, 1], [0, 0, 1], [0, 0, 0, 1]):
        activation = PolynomialActivation(coefficients)
        joint = evaluate_fixed_depth_batch_polynomial_gnf(q0, c, 2, activation)
        accepted = evaluate_contracted_directional_gnf(q0, c, activation)
        assert joint.ntk == accepted.ntk
        assert joint.straight_line == accepted.straight_line
        assert joint.hessian_readout == accepted.hessian_readout
        assert joint.hessian_layers[2] == accepted.hessian_middle
        assert joint.hessian_layers[1] == accepted.hessian_first
        assert joint.correction == accepted.correction

    # The same blockwise comparison at B=3 checks that the implementation is
    # genuinely batch-dynamic, rather than a hard-coded two-index expansion.
    q3 = [
        [1, F(1, 5), F(-1, 7)],
        [F(1, 5), F(4, 3), F(1, 6)],
        [F(-1, 7), F(1, 6), F(5, 4)],
    ]
    c3 = [F(2, 5), F(-1, 3), F(3, 7)]
    activation = PolynomialActivation([0, 0, 1])
    joint = evaluate_fixed_depth_batch_polynomial_gnf(q3, c3, 2, activation)
    accepted = evaluate_contracted_directional_gnf(q3, c3, activation)
    assert joint.ntk == accepted.ntk
    assert joint.straight_line == accepted.straight_line
    assert joint.hessian_readout == accepted.hessian_readout
    assert joint.hessian_layers[2] == accepted.hessian_middle
    assert joint.hessian_layers[1] == accepted.hessian_first
    assert joint.correction == accepted.correction


def test_b1_reduces_to_independently_contracted_depth_recurrence() -> None:
    q0 = F(3, 2)
    activations = ([0, 1], [1, 1], [0, 0, 1], [0, 1, F(1, 10)])
    for hidden_layers in (1, 2, 3, 4):
        for coefficients in activations:
            activation = PolynomialActivation(coefficients)
            joint = evaluate_fixed_depth_batch_polynomial_gnf(
                [[q0]], [1], hidden_layers, activation
            )
            accepted = evaluate_depth_b1_audit_recurrence(
                float(q0),
                hidden_layers,
                polynomial_oracle([float(value) for value in coefficients]),
                quadrature_order=48,
            )
            np.testing.assert_allclose(
                [float(joint.ntk), float(joint.straight_line), float(joint.hessian_square), float(joint.correction)],
                [accepted.ntk, accepted.straight_line, accepted.hessian_square, accepted.correction],
                rtol=3.0e-11,
                atol=3.0e-8,
            )


def test_h3_b2_nonlinear_exact_fixture_and_singular_b1_collapse() -> None:
    # This is the first gate lying strictly beyond both accepted axes:
    # H=3, B=2, nondegenerate Q0, both channel coordinates active, phi=x+x^2/10.
    q0 = [[1, F(1, 3)], [F(1, 3), F(4, 3)]]
    c = [F(2, 3), F(-1, 4)]
    activation = PolynomialActivation([0, 1, F(1, 10)])
    result = evaluate_fixed_depth_batch_polynomial_gnf(q0, c, 3, activation)
    assert result.ntk == F(307537184532813623, 164025000000000000)
    assert result.correction == F(
        68550715812209572302778459455166819,
        1261134404296875000000000000000000,
    )
    assert result.parity_cross_max == 0
    assert result.parity_response_max == 0

    # Exact batch-permutation equivariance and channel homogeneity are
    # sensitive to a silent transpose in any response matrix.
    permuted = evaluate_fixed_depth_batch_polynomial_gnf(
        [[q0[1][1], q0[1][0]], [q0[0][1], q0[0][0]]],
        [c[1], c[0]],
        3,
        activation,
    )
    assert permuted.ntk == result.ntk
    assert permuted.correction == result.correction
    scale = F(-7, 5)
    scaled = evaluate_fixed_depth_batch_polynomial_gnf(
        q0, [scale * value for value in c], 3, activation
    )
    assert scaled.ntk == scale**2 * result.ntk
    assert scaled.correction == scale**4 * result.correction

    # An inactive second channel must not leak through a nonzero input
    # correlation.  Compare to the separately contracted B=1 evaluator.
    single = evaluate_fixed_depth_batch_polynomial_gnf(q0, [1, 0], 3, activation)
    single_accepted = evaluate_depth_b1_audit_recurrence(
        1.0, 3, polynomial_oracle([0, 1, 0.1]), quadrature_order=48
    )
    np.testing.assert_allclose(
        [float(single.ntk), float(single.correction)],
        [single_accepted.ntk, single_accepted.correction],
        rtol=3.0e-11,
        atol=3.0e-8,
    )

    # With repeated inputs, both nonzero channel entries collapse exactly to
    # the accepted B=1 recurrence with effective channel sum lambda.
    repeated_q = F(5, 4)
    repeated_c = [F(2, 3), F(-1, 5)]
    repeated_scale = sum(repeated_c)
    repeated = evaluate_fixed_depth_batch_polynomial_gnf(
        [[repeated_q, repeated_q], [repeated_q, repeated_q]],
        repeated_c,
        3,
        PolynomialActivation([0, 0, 1]),
    )
    accepted = evaluate_depth_b1_audit_recurrence(
        float(repeated_q), 3, polynomial_oracle([0, 0, 1]), quadrature_order=48
    )
    np.testing.assert_allclose(
        [float(repeated.ntk), float(repeated.correction)],
        [repeated_scale**2 * accepted.ntk, repeated_scale**4 * accepted.correction],
        rtol=5.0e-12,
        atol=2.0e-5,
    )


def test_deep_linear_closed_form_at_arbitrary_batch() -> None:
    q0 = [
        [1, F(1, 5), F(-1, 7)],
        [F(1, 5), F(4, 3), F(1, 6)],
        [F(-1, 7), F(1, 6), F(5, 4)],
    ]
    c = [F(2, 5), F(-1, 3), F(3, 7)]
    qeff = sum(c[a] * q0[a][b] * c[b] for a in range(3) for b in range(3))
    for hidden_layers in (1, 2, 3, 4):
        result = evaluate_fixed_depth_batch_polynomial_gnf(
            q0, c, hidden_layers, PolynomialActivation([0, 1])
        )
        assert result.ntk == (hidden_layers + 1) * qeff
        assert result.correction == (
            F(2, 3)
            * hidden_layers
            * (hidden_layers + 1) ** 2
            * (hidden_layers + 2)
            * qeff**2
        )
