"""Read-only comparison to the relocated independent finite-jet reference."""
import sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / 'code'), str(ROOT)]
from pde import Parameters, TANH, forward, kernel
from studies.mfp_gaussian_calculus.depth.model import DepthState
from studies.mfp_gaussian_calculus.depth.finite_width_jet import feature_ascent_jet

def oracle(order, z):
    t = np.tanh(z)
    return (t, 1 - t*t, -2*t*(1-t*t), -2*(1-t*t)*(1-3*t*t))[order]

rng = np.random.default_rng(57)
x = np.sqrt(2.0) * np.array([[1, 0.6, -1], [0, 0.8, 0]])
channel = np.array([0.7, -0.9, 1.2])
for depth in (1, 2, 3, 5):
    n = 3
    weights = (rng.normal(size=(n, 2)),) + tuple(rng.normal(size=(n, n))/np.sqrt(n) for _ in range(depth-1))
    a = rng.normal(size=n)
    state = Parameters(weights, a)
    reference_state = DepthState(weights[0] @ x / np.sqrt(2.0), tuple(np.sqrt(n)*w for w in weights[1:]), a)
    reference = feature_ascent_jet(reference_state, x.T@x/2, channel, oracle, order=1).derivatives
    np.testing.assert_allclose(reference[0], channel @ forward(state, x, TANH).output, atol=1e-13, rtol=1e-12)
    np.testing.assert_allclose(reference[1], channel @ kernel(state, x, TANH) @ channel, atol=1e-13, rtol=1e-12)
    print('PASS relocated independent jet output and kernel, depth', depth)
