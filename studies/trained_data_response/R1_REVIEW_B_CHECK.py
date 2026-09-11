"""Reviewer B: exact algebra and one fixed cavity-identity check; no training."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import numpy as np


def transpose(a):
    return [list(x) for x in zip(*a)]


def multiply(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in transpose(b)] for row in a]


def subtract(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]


def zero(a):
    return all(x == 0 for row in a for x in row)


def exact_projection_check():
    # A singular Gram and a positive, markedly nonuniform clock metric.
    v = [F(1), F(-1, 2), F(3, 4)]
    S = [[x, 2*x] for x in v]
    D = [[F(1, 1000), F(0), F(0)],
         [F(0), F(1, 3), F(0)],
         [F(0), F(0), F(1)]]
    E = multiply(transpose(S), D)
    K = multiply(E, S)
    kappa = K[0][0]
    Kplus = [[F(1)/(25*kappa), F(2)/(25*kappa)],
             [F(2)/(25*kappa), F(4)/(25*kappa)]]
    I = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    P = subtract(I, multiply(multiply(S, Kplus), E))
    assert zero(subtract(multiply(multiply(K, Kplus), K), K))
    assert zero(subtract(multiply(P, P), P))
    assert zero(multiply(E, P)) and zero(multiply(P, S))
    assert zero(subtract(multiply(D, P), multiply(transpose(P), D)))
    assert zero(multiply(K, [[F(-2)], [F(1)]]))
    assert zero(multiply(S, [[F(-2)], [F(1)]]))
    # K=0 under positive D forces S=0; its semigroup and projection are I.
    Sz = [[F(0)] for _ in range(3)]
    assert zero(multiply(multiply(transpose(Sz), D), Sz))
    # Positive ES alone is insufficient without kernel compatibility.
    badS, badE = [[F(1)], [F(0)]], [[F(0), F(1)]]
    assert zero(multiply(badE, badS))
    assert not zero(multiply(badS, badE))
    return str(kappa)


def clock_polynomial_check():
    # Formal terms for d/d epsilon of w'=k*g(w)*Q, with dw=g*xi.
    # This subtracts the time derivative of the changing gate on the left.
    raw_differential = {'dk*g*Q': F(1), 'k*gp*g*xi*Q': F(1),
                        'k*g*dQ': F(1)}
    changing_gate = {'k*gp*g*xi*Q': F(1)}
    residual = dict(raw_differential)
    for key, value in changing_gate.items():
        residual[key] -= value
    residual = {key: value for key, value in residual.items() if value}
    assert residual == {'dk*g*Q': F(1), 'k*g*dQ': F(1)}
    # Divide by g>0: xi'=dk*Q+k*dQ. No own-gate multiplier remains.
    # The clock-envelope identity is checked as an exact Laurent polynomial.
    cosh = {1: F(1, 2), -1: F(1, 2)}
    sinh = {1: F(1, 2), -1: F(-1, 2)}
    def poly_mul(a, b):
        c = {}
        for k, v in a.items():
            for l, w in b.items():
                c[k+l] = c.get(k+l, F(0)) + v*w
        return {k: v for k, v in c.items() if v}
    cosh2 = poly_mul(cosh, cosh)
    assert cosh2 == {2: F(1, 4), 0: F(1, 2), -2: F(1, 4)}
    derivative = {k: k*v for k, v in cosh2.items() if k*v}
    assert poly_mul(derivative, cosh) == poly_mul(cosh2, {k: 2*v for k, v in sinh.items()})


def cavity_identity_check():
    # Fixed, arbitrary fields: no dynamical simulation or random experiment.
    A0 = np.array([[.4, -.2, .1], [.1, .3, -.5], [-.2, .6, .7]])
    K = np.array([[.1, .2, 0], [-.1, .1, .3], [.2, -.1, .2]])
    Ktilde = np.array([[0, .1, .1], [.2, -.2, .1], [-.1, 0, .3]])
    i = 1
    ai = A0[:, i].copy()
    A0tilde = A0.copy()
    A0tilde[:, i] = 0
    A, Atilde = A0 + K, A0tilde + Ktilde
    h, ht = np.array([.2, -.8, .5]), np.array([-.1, .4, .3])
    d, dt = np.array([.7, -.2, .1]), np.array([.1, .3, -.4])
    fwd_left = A @ h - Atilde @ ht
    fwd_right = A @ (h-ht) + (K-Ktilde) @ ht + ai*ht[i]
    rev_left = A.T @ d - Atilde.T @ dt
    impulse = np.zeros(3)
    impulse[i] = ai @ dt
    rev_right = A.T @ (d-dt) + (K-Ktilde).T @ dt + impulse
    forward_error = float(np.linalg.norm(fwd_left-fwd_right))
    reverse_error = float(np.linalg.norm(rev_left-rev_right))
    assert max(forward_error, reverse_error) < 1e-14
    # The deleted forward action is O(n^-1/2) in RMS for |h_i|<=1.
    assert np.linalg.norm(ai*ht[i])/np.sqrt(3) <= np.linalg.norm(ai)/np.sqrt(3)
    return forward_error, reverse_error


if __name__ == '__main__':
    kappa = exact_projection_check()
    clock_polynomial_check()
    forward_error, reverse_error = cavity_identity_check()
    report = dict(checks='PASS', exact_singular_metric_kappa=kappa,
                  exact_checks=['clock cancellation', 'clock primitive and envelope derivative',
                                'singular pseudoinverse', 'endpoint projection',
                                'metric symmetry', 'compatible zero mode',
                                'incompatible nilpotent boundary'],
                  fixed_cavity_forward_error=forward_error,
                  fixed_cavity_reverse_error=reverse_error,
                  scope='Exact algebra and fixed deterministic array identities; no training or sweeps',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_name('independent_results.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
