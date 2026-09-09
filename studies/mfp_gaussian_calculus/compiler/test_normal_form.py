from fractions import Fraction

import numpy as np

from .l2_b1_base import initialization_normal_form
from .l2_b1_correction import first_correction_normal_form
from .normal_form import (
    PhiFactor,
    PolynomialActivation,
    add,
    atom,
    atom_inventory,
    evaluate_polynomial,
    evaluate_quadrature,
    maximum_activation_derivative,
    mul,
    power,
)


def test_initial_ntk_constant_linear_quadratic() -> None:
    state = initialization_normal_form()
    constant = PolynomialActivation([2])
    linear = PolynomialActivation([0, 1])
    quadratic = PolynomialActivation([0, 0, 1])

    assert evaluate_polynomial(state.ntk, constant, {"q_0": 1}) == 4
    assert evaluate_polynomial(state.ntk, linear, {"q_0": 1}) == 3
    assert evaluate_polynomial(state.ntk, quadratic, {"q_0": 1}) == 111
    assert evaluate_polynomial(state.ntk, linear, {"q_0": 3}) == 9


def test_multivariate_wick_atom() -> None:
    rho = Fraction(2, 5)
    sixth = atom(
        [[1, rho, rho], [rho, 1, rho], [rho, rho, 1]],
        [PhiFactor(0), PhiFactor(1), PhiFactor(2)],
    )
    quadratic = PolynomialActivation([0, 0, 1])
    expected = 1 + 6 * rho**2 + 8 * rho**3
    assert evaluate_polynomial(sixth, quadratic, {}) == expected


def test_inventory_is_dependency_first() -> None:
    state = initialization_normal_form()
    inventory = atom_inventory(state.ntk)
    assert {item.tag for item in inventory} == {"q_1", "d_1", "q_2", "d_2"}
    assert maximum_activation_derivative(state.ntk) == 1


def test_first_correction_constant_linear_affine_quadratic_cubic() -> None:
    state = first_correction_normal_form()
    constant = PolynomialActivation([2])
    linear = PolynomialActivation([0, 1])
    affine = PolynomialActivation([1, 1])
    quadratic = PolynomialActivation([0, 0, 1])
    cubic = PolynomialActivation([0, 0, 0, 1])

    assert evaluate_polynomial(state.correction, constant, {"q_0": 1}) == 0
    assert evaluate_polynomial(state.ntk, linear, {"q_0": 1}) == 3
    assert evaluate_polynomial(state.correction, linear, {"q_0": 1}) == 48
    assert evaluate_polynomial(state.correction, linear, {"q_0": 3}) == 48 * 9
    assert evaluate_polynomial(state.ntk, affine, {"q_0": 1}) == 6
    assert evaluate_polynomial(state.correction, affine, {"q_0": 1}) == 112
    assert evaluate_polynomial(state.ntk, quadratic, {"q_0": 1}) == 111
    assert (
        evaluate_polynomial(state.tangent_branch, quadratic, {"q_0": 1})
        == 30_744
    )
    assert (
        evaluate_polynomial(state.straight_line_branch, quadratic, {"q_0": 1})
        == 92_232
    )
    assert (
        evaluate_polynomial(state.hessian_branch, quadratic, {"q_0": 1})
        == 375_180
    )
    assert (
        evaluate_polynomial(state.correction, quadratic, {"q_0": 1})
        == 1_685_184
    )
    # This activates every derivative through phi'''; the quadratic control
    # annihilates the highest-order atom family.
    assert evaluate_polynomial(state.ntk, cubic, {"q_0": 1}) == 305_775
    assert (
        evaluate_polynomial(state.correction, cubic, {"q_0": 1})
        == 154_118_008_098_000
    )
    assert maximum_activation_derivative(state.correction) == 3


def test_all_correction_atoms_are_literal_univariate_expectations() -> None:
    state = first_correction_normal_form()
    inventory = atom_inventory(add(state.ntk, state.correction))
    assert len(inventory) == 17
    assert all(len(item.covariance) == 1 for item in inventory)


def test_independent_canonical_formula_map_is_structurally_identical() -> None:
    """Rebuild equations (3.1)--(3.7) of the canonical note verbatim."""

    s = first_correction_normal_form()
    q = s.q0
    c = add(s.Q, mul(q, s.d))
    tau = add(
        s.e0,
        mul(2, c, s.p1),
        mul(3, power(c, 2), s.e12),
        mul(power(q, 2), s.m4, s.D, s.z_phi2_sq),
    )
    response_alpha = add(
        s.D,
        s.z_phi_phi2,
        mul(c, add(s.z_phi1_phi3, s.z_phi2_sq)),
    )
    k = add(s.D, response_alpha)
    kappa = add(
        mul(3, power(q, 2), s.D, s.mA),
        mul(3, power(q, 3), s.D, s.mB),
    )
    h_star = add(
        mul(power(c, 2), s.y14),
        mul(s.Q, tau),
        mul(2, power(q, 2), s.m4, power(s.D, 2)),
        mul(
            q,
            add(
                mul(3, power(q, 2), power(s.D, 2), s.n21),
                mul(power(k, 2), s.aX),
                mul(tau, s.d),
                mul(2, q, s.D, k, s.mA),
            ),
        ),
    )
    s_star = add(
        mul(3, power(c, 2), s.p1),
        mul(3, power(q, 2), s.m4, s.D, s.z_phi_phi2),
        mul(3, power(q, 2), s.D, s.mA, add(s.D, s.z_phi_phi2)),
        mul(3, power(c, 3), s.p3),
        mul(3, c, power(q, 2), s.m4, s.D, s.z_phi1_phi3),
        mul(
            3,
            power(q, 2),
            c,
            s.D,
            s.mA,
            add(s.z_phi1_phi3, s.z_phi2_sq),
        ),
        mul(kappa, s.D),
    )
    assert c == s.alpha
    assert tau == s.b2
    assert k == s.c
    assert h_star == s.hessian_branch
    assert s_star == s.straight_line_branch
    assert add(mul(4, h_star), mul(2, s_star)) == s.correction


def test_quadrature_sine_and_tanh_regressions() -> None:
    state = first_correction_normal_form()

    def sine_derivative(order, x):
        return (np.sin(x), np.cos(x), -np.sin(x), -np.cos(x))[order % 4]

    def tanh_derivative(order, x):
        t = np.tanh(x)
        values = (
            t,
            1.0 - t * t,
            -2.0 * t * (1.0 - t * t),
            -2.0 * (1.0 - t * t) * (1.0 - 3.0 * t * t),
        )
        return values[order]

    sine_a = evaluate_quadrature(state.ntk, sine_derivative, {"q_0": 1.0}, order=32)
    sine_c = evaluate_quadrature(
        state.correction, sine_derivative, {"q_0": 1.0}, order=32
    )
    assert abs(sine_a - 1.0) < 1.0e-12
    assert abs(sine_c - (-1.88699982730593)) < 1.0e-10

    # tanh needs a larger Hermite rule because its nearest complex poles slow
    # spectral convergence.  These are quadrature regressions, not proof data.
    tanh_a = evaluate_quadrature(state.ntk, tanh_derivative, {"q_0": 1.0}, order=160)
    tanh_c = evaluate_quadrature(
        state.correction, tanh_derivative, {"q_0": 1.0}, order=160
    )
    assert abs(tanh_a - 0.78304956672598) < 1.0e-10
    assert abs(tanh_c - (-1.74687216213466)) < 1.0e-6
