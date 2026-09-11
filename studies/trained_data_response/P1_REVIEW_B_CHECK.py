"""Independent deterministic algebra and boundary checks; no training."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import platform
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.optimize import brentq


def gate(z):
    return 1 / np.cosh(z) ** 2


def curvature(z):
    return -2 * np.tanh(z) * gate(z)


def field(w, A, c, weights, inputs, labels):
    n = c.size
    h = np.tanh(w @ inputs.T)
    z = A @ h
    H = np.tanh(z)
    delta = c[:, None] * gate(z)
    Q = A.T @ delta
    residual = c @ H / n - labels
    coeff = -2 * weights * residual
    raw_row = ((Q * gate(w @ inputs.T)) * coeff) @ inputs
    return raw_row / gate(w), (delta * coeff) @ h.T / n, H @ coeff


def flat(v):
    return np.concatenate([a.ravel() for a in v])


def run():
    w = np.array([[.1, -.6], [1.3, .4], [-.7, 1.1], [.9, -.2]])
    A = np.array([[.4, -.2, .1, .3], [.7, .1, -.3, .2],
                  [-.4, .5, .2, -.1], [.3, -.6, .8, .1]])
    c = np.array([.6, -.3, .2, -.7])
    xi = np.array([[.2, .4], [-.3, .1], [.5, -.2], [-.1, .3]])
    B = np.array([[.2, .1, -.3, .4], [-.1, .3, .2, -.2],
                  [.4, -.2, .1, .3], [.1, .2, -.4, -.1]])
    d = np.array([-.2, .4, .1, -.3])
    U = np.array([[1., 0.], [0., 1.], [.6, .8], [-.8, .6]])
    y = np.array([1., -1., .4, -.9])
    p = np.array([.5, .5, 0., 0.])
    signed = np.array([-.5, -.5, .35, .65])
    n = len(c)
    dw = gate(w) * xi
    eps = 1e-30
    direct = field(w + 1j * eps * dw, A + 1j * eps * B,
                   c + 1j * eps * d, p + 1j * eps * signed, U, y)
    derivative = tuple(a.imag / eps for a in direct)
    tangent_row = np.zeros_like(w)
    tangent_middle = np.zeros_like(A)
    tangent_readout = np.zeros_like(c)
    for a in range(2):
        h = np.tanh(w[:, a])
        z = A @ h
        H = np.tanh(z)
        delta = c * gate(z)
        Q = A.T @ delta
        dh = gate(w[:, a]) ** 2 * xi[:, a]
        dz = B @ h + A @ dh
        ddelta = d * gate(z) + c * curvature(z) * dz
        dQ = B.T @ delta + A.T @ ddelta
        df = (d @ H + delta @ dz) / n
        residual = c @ H / n - y[a]
        tangent_row[:, a] = -2 * p[a] * (df * Q + residual * dQ)
        tangent_middle += -2 * p[a] / n * (
            df * np.outer(delta, h) + residual * np.outer(ddelta, h)
            + residual * np.outer(delta, dh))
        tangent_readout += -2 * p[a] * (df * H + residual * gate(z) * dz)
    source = field(w, A, c, signed, U, y)
    tangent = tuple(a + b for a, b in zip(
        (tangent_row, tangent_middle, tangent_readout), source))
    tangent_error = float(np.linalg.norm(flat(derivative) - flat(tangent)))
    assert tangent_error < 1e-11

    u = np.array([-.8, .6])
    h = np.tanh(w @ u)
    z = A @ h
    delta = c * gate(z)
    dz = B @ h + A @ (gate(w @ u) * (dw @ u))
    exact_output = (d @ np.tanh(z) + delta @ dz) / n
    complex_output = ((c + 1j * eps * d) @ np.tanh(
        (A + 1j * eps * B) @ np.tanh((w + 1j * eps * dw) @ u)) / n).imag / eps
    output_error = float(abs(exact_output - complex_output))
    pairing_error = float(abs(delta @ (A @ (dw @ u)) / n
                              - (A.T @ delta) @ (dw @ u) / n))
    rank_pairing_error = float(abs(np.sum(np.outer(delta, h) / n * B)
                                   - delta @ (B @ h) / n))
    wrong_transpose_effect = float(np.linalg.norm((A - A.T) @ delta))
    assert max(output_error, pairing_error, rank_pairing_error) < 1e-11
    assert wrong_transpose_effect > .1

    initial_source = field(w, A, np.zeros(n), signed, U, y)
    expected_readout = 2 * np.tanh(A @ np.tanh(w @ U.T)) @ (signed * y)
    assert np.linalg.norm(initial_source[0]) == 0
    assert np.linalg.norm(initial_source[1]) == 0
    assert np.linalg.norm(initial_source[2] - expected_readout) < 1e-13
    assert np.linalg.norm(initial_source[2]) > .1

    def primitive(z):
        return z / 2 + np.sinh(2 * z) / 4
    clock_cases = [(-8., 100.), (8., -100.), (-1.2, -20.),
                   (1.2, 20.), (-.3, 1.5), (.3, -1.5), (0., 0.)]
    clock_results = []
    for g, X in clock_cases:
        if X == 0:
            j = g
        else:
            target = primitive(g) + X
            j = brentq(lambda z: primitive(z) - target, -12., 12., xtol=1e-14)
        lhs = np.cosh(j) ** 2
        rhs = np.cosh(g) ** 2 + 2 * abs(X)
        scaled_residual = abs(primitive(j) - primitive(g) - X) / (1 + abs(target if X else 0))
        assert lhs <= rhs + 1e-9
        assert abs(j - g) <= abs(X) + 1e-12
        assert scaled_residual < 1e-12
        assert abs(2 * np.sinh(j) * np.cosh(j) * gate(j) - 2 * np.tanh(j)) < 1e-12
        clock_results.append({'root': g, 'clock_shift': X, 'new_root': float(j),
                              'envelope_slack': float(rhs - lhs),
                              'scaled_equation_residual': float(scaled_residual)})

    S = np.array([[1., -3.], [.4, -1.2], [-.7, 2.1]])
    D = np.diag([.002, .7, 1.])
    E = S.T @ D
    Gamma = E @ S
    inverse = np.linalg.pinv(Gamma, rcond=1e-12)
    P = np.eye(3) - S @ inverse @ E
    R = np.diag(np.sqrt(np.diag(D)))
    G = R @ S
    raw_projector = np.eye(3) - G @ inverse @ G.T
    semigroup = np.eye(3) + S @ inverse @ (expm(-14 * Gamma) - np.eye(2)) @ E
    endpoint_errors = {'idempotence': float(np.linalg.norm(P @ P - P)),
                       'prediction_kernel': float(np.linalg.norm(E @ P)),
                       'synthesis_kernel': float(np.linalg.norm(P @ S)),
                       'raw_metric_conversion': float(np.linalg.norm(R @ P - raw_projector @ R)),
                       'semigroup': float(np.linalg.norm(expm(-14 * S @ E) - semigroup))}
    assert max(endpoint_errors.values()) < 1e-10

    epsilon = 1e-8
    ill_S = np.array([[1.], [math.sqrt(epsilon)]])
    ill_E = ill_S.T @ np.diag([epsilon, 1.])
    ill_Gamma = float((ill_E @ ill_S)[0, 0])
    t = 1 / ill_Gamma
    formula = np.eye(2) + ill_S @ ill_E * np.expm1(-2 * t * ill_Gamma) / ill_Gamma
    ill_error = float(np.linalg.norm(expm(-2 * t * ill_S @ ill_E) - formula))
    gain = float(np.linalg.norm(formula, 2))
    assert ill_error < 1e-7 and gain > 4000
    bad_S = np.array([[1.], [0.]])
    bad_E = np.array([[0., 1.]])
    assert np.linalg.norm(bad_E @ bad_S) == 0
    bad_gain = float(np.linalg.norm(expm(-20 * bad_S @ bad_E), 2))
    assert bad_gain > 20

    # Infinite example: s_k=2^-k, D_kk=4^-k, k>=1, S=(s,2s).
    ss = Fraction(1, 3)
    sDs = Fraction(1, 15)
    DsDs = Fraction(1, 63)
    gram_positive_eigenvalue = 5 * sDs
    pseudoinverse_coefficient = 1 / (25 * sDs)
    assert gram_positive_eigenvalue == Fraction(1, 3)
    assert pseudoinverse_coefficient == Fraction(3, 5)
    assert 15 * sDs == 1  # P=I-15 s (Ds)^*: exact idempotence.

    density = lambda z: math.exp(-z*z/2) / math.sqrt(2*math.pi)
    integrate = lambda fn: 2 * quad(lambda z: fn(z) * density(z), 0., 12.,
                                    epsabs=2e-13, epsrel=2e-13)[0]
    q = integrate(lambda z: math.tanh(z) ** 2)
    v = integrate(lambda z: math.tanh(math.sqrt(q) * z) ** 2)
    a0 = integrate(lambda z: (1 / math.cosh(z) ** 2) ** 4)
    r0 = integrate(lambda z: (1 / math.cosh(math.sqrt(q) * z) ** 2) ** 2)
    assert .392108947877 < q < .396376711612
    assert v > .233120735618 and a0 > .339792209687 and r0 > .631761866359
    base = Path('/home/amir/Codes/PDE/studies/trained_data_response')
    dependency_lines = (base / 'P1_DEPENDENCIES.md').read_text().splitlines(keepends=True)
    embedded = ''.join(dependency_lines[2676:2732])
    standalone = (base / 'P1_REFERENCE_CERTIFICATE.py').read_text()
    assert embedded == standalone

    return {'status': 'PASS', 'scope': 'fixed deterministic algebra; no training or parameter sweep',
            'complex_step_tangent_error': tangent_error, 'passive_prediction_error': output_error,
            'adjoint_pairing_error': pairing_error, 'rank_metric_pairing_error': rank_pairing_error,
            'wrong_transpose_effect': wrong_transpose_effect,
            'initial_zero_readout_source_norm': float(np.linalg.norm(initial_source[2])),
            'clock_envelope_cases': clock_results, 'compatible_endpoint_errors': endpoint_errors,
            'ill_conditioned_positive_metric': {'gamma': ill_Gamma, 'time': t, 'gain': gain,
                                                'exponential_identity_error': ill_error},
            'incompatible_nilpotent_gain': bad_gain,
            'infinite_noncoercive_example': {'s_norm_squared': str(ss), 's_D_s': str(sDs),
                'D_s_norm_squared': str(DsDs), 'gram_positive_eigenvalue': str(gram_positive_eigenvalue),
                'gram_pseudoinverse_coefficient': str(pseudoinverse_coefficient),
                'projection_correction_norm': 15 * math.sqrt(float(ss * DsDs))},
            'gaussian_quadrature': {'q': q, 'v': v, 'a0': a0, 'r0': r0,
                'two_sided_gaussian_tail_bound_beyond_12': 2 * density(12.) / 12.},
            'embedded_certificate_matches_standalone': True,
            'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}


if __name__ == '__main__':
    result = run()
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = Path(__file__).with_name('independent_checks_results.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
