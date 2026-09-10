"""One deterministic derivative check; no training or population experiment."""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
from pde.finite_network import Parameters
from pde.finite_jets import finite_flow_jets


def derivative(j, z):
    h = np.tanh(z)
    d = 1 - h*h
    return (h, d, -2*h*d, -2*d*d + 4*h*h*d)[j]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    n = 5
    angles = np.array([0, np.pi/5, -np.pi/5, np.pi/7, 1.3])
    X = np.sqrt(2)*np.stack([np.cos(angles), np.sin(angles)])
    y = np.array([1, (1-np.sqrt(5))/4, (1-np.sqrt(5))/4])
    p = y/3
    w1 = np.sin(np.arange(10).reshape(n, 2)+0.4)
    w2 = np.cos(np.arange(25).reshape(n, n)*0.7+0.2)/np.sqrt(n)
    state = Parameters((w1, w2), np.zeros(n))
    jet = finite_flow_jets(state, X[:, :3], y, (derivative,)*2, order=3)
    z1 = w1@X/np.sqrt(2)
    h1 = np.tanh(z1)
    e = 1-h1*h1
    z2 = w2@h1
    h2 = np.tanh(z2)
    d = 1-h2*h2
    G = X.T@X/2
    Q = h1.T@h1/n
    K = h2.T@h2/n
    S = h2[:, :3]@p
    U = S[:, None]*d
    B = e*(w2.T@U)
    T = B[:, :3]@(p[:, None]*G[:3])
    A = e*T
    M = U[:, :3]@(p[:, None]*Q[:3])
    R = M+w2@A
    E = d*R
    J = 4*(S@E)/n+(4/3)*(h2.T@(E[:, :3]@p))/n
    V = U.T@U/n
    D = B.T@B/n
    hidden = G*D+Q*V
    K2 = 4*hidden+2*(E.T@h2+h2.T@E)/n
    g1 = (2/3)*K[:, :3]@y
    g2 = -(2/3)**2/2*K[:, :3]@K[:3, :3]@y
    g3 = (2/3)**3/6*K[:, :3]@K[:3, :3]@K[:3, :3]@y
    # Recompute passive output jets from the independently stored weight jets.
    c = jet.parameter_coefficients
    z12 = c[2].weights[0]@X/np.sqrt(2)
    h12 = e*z12
    z22 = w2@h12+c[2].weights[1]@h1
    h22 = d*z22
    f3 = (c[3].readout@h2+c[1].readout@h22)/n
    energy = p@hidden[:3, :3]@p
    beta = (p@J[:3])/(2*np.mean(S*S))
    errors = {
        'zero_hidden_linear': max(np.max(np.abs(c[1].weights[0])), np.max(np.abs(c[1].weights[1]))),
        'linear_moving_residual': np.max(np.abs(jet.output_coefficients[1]-g1[:3])),
        'quadratic_moving_residual': np.max(np.abs(jet.output_coefficients[2]-g2[:3])),
        'first_hidden_quadratic': np.max(np.abs(z12-2*T)),
        'second_hidden_quadratic': np.max(np.abs(z22-2*R)),
        'cubic_train_and_passive': np.max(np.abs(f3-g3-J)),
        'cubic_maintained_producer': np.max(np.abs(f3[:3]-jet.output_coefficients[3])),
        'kernel_route': np.max(np.abs(J-(2/3)*K2[:, :3]@p)),
        'positive_training_contraction': abs(p@J[:3]-(16/3)*energy),
        'matched_loss_cubic_cancels': abs(p@(J[:3]-beta*g1[:3])),
    }
    assert max(errors.values()) < 1e-11, errors
    assert beta > 0 and energy > 0
    # A nonzero finite readout creates nonzero initialized hidden blocks.
    small_readout = np.array([-2, -1, 0, 1, 2], dtype=float)/25
    delta2 = small_readout[:, None]*d[:, :3]
    delta1 = e[:, :3]*(w2.T@delta2)
    finite_hidden_trace = np.trace(G[:3,:3]*(delta1.T@delta1/n)+Q[:3,:3]*(delta2.T@delta2/n))
    assert finite_hidden_trace > 0
    root = Path(__file__).resolve().parents[2]
    sources = [Path(__file__).resolve(), root/'code/pde/finite_jets.py', root/'code/pde/finite_network.py']
    report = {
        'claim': 'finite deterministic algebra only; no Gaussian or trajectory inference',
        'python': platform.python_version(), 'numpy': np.__version__,
        'errors': {k: float(v) for k,v in errors.items()},
        'beta': float(beta), 'hidden_energy': float(energy),
        'finite_nonzero_readout_hidden_trace': float(finite_hidden_trace),
        'source_sha256': {str(f.relative_to(root)): hashlib.sha256(f.read_bytes()).hexdigest() for f in sources},
        'status': 'PASS',
    }
    text = json.dumps(report, indent=2)
    (args.output/'result.json').write_text(text+'\n')
    print(text)


if __name__ == '__main__':
    main()
