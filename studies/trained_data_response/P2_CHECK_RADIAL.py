"""Deterministic supplied-state identities; no optimization trajectory."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output).resolve()
    root = Path(__file__).resolve().parents[2]
    allowed = root/'data/generated/trained_data_response'
    assert allowed in out.parents and out != allowed
    out.mkdir(parents=True, exist_ok=False)
    # Fixed correlated directions and conflicting labels at a repeated input.
    u = np.array([[1., 0.], [.6, .8], [.6, .8], [-.8, .6]])
    y = np.array([1., -.7, .4, -1.2])
    p = np.array([.11, .23, .29, .37])
    w = np.array([[.2, -.4], [1.1, .3], [-.8, .6], [4., -3.]])
    A = np.array([[.2, -.1, .4, .1], [.3, .7, -.2, .4],
                  [-.5, .1, .6, -.2], [.1, -.3, .2, .5]])
    c = np.array([.25, -.4, .15, .31])
    n = len(c)
    z1 = w@u.T
    h1 = np.tanh(z1)
    z2 = A@h1
    h2 = np.tanh(z2)
    residual = c@h2/n-y
    d2 = c[:, None]/np.cosh(z2)**2
    Q = A.T@d2
    dw = -2*((p*residual)*Q/np.cosh(z1)**2)@u
    dA = -2*((p*residual)*d2)@h1.T/n
    dc = -2*h2@(p*residual)

    radial = 2*np.sum(w*dw, axis=1)
    explicit = -4*np.sum((p*residual)*Q*z1/np.cosh(z1)**2, axis=1)
    bound = 2*np.sum(p*np.abs(residual*Q), axis=1)
    radial_error = float(np.max(np.abs(radial-explicit)))
    assert radial_error < 1e-14
    assert np.all(radial <= bound+1e-14)

    def direct_loss(W, M, C):
        predictions = C@np.tanh(M@np.tanh(W@u.T))/n
        return np.sum(p*(predictions-y)**2)

    # Complex-step differentiation of the scalar loss is independent of
    # the hand-derived radial and gradient contractions above.
    h = 1e-25
    loss_derivative = direct_loss(w+1j*h*dw, A+1j*h*dA, c+1j*h*dc).imag/h
    dissipation = -(np.sum(dw**2)/n+np.sum(dA**2)+np.sum(dc**2)/n)
    energy_error = float(abs(loss_derivative-dissipation))
    assert energy_error < 1e-12
    result = dict(result='PASS', scope='supplied-state identities only; no training',
                  radial_identity_error=radial_error,
                  radial_upper_bound_slack=(bound-radial).tolist(),
                  unhalved_loss_metric_error=energy_error,
                  nonzero_readout=True, correlated_and_repeated_inputs=True,
                  python=platform.python_version(), numpy=np.__version__,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
