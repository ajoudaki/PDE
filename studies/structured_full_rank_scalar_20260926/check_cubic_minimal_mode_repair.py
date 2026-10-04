"""Deterministic coefficient checks; no training integration."""
import importlib.util
import json
import pathlib
import sys
import time

import numpy as np
from scipy.integrate import quad

ROOT = pathlib.Path('/home/amir/Codes/PDE')
SOURCE = ROOT/'studies/structured_full_rank_scalar_20260926/cubic_minimal_mode_repair.py'
spec = importlib.util.spec_from_file_location('minimal_mode', SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

rng = np.random.default_rng(20260930)
n, m = 48, 3
angles = np.array([0., .7, 1.8])
inputs = np.stack((np.cos(angles), np.sin(angles)), axis=1)
labels = np.array([.5, -.3, .8])
w, W = rng.normal(size=(n, 2)), rng.normal(size=(n, n))/np.sqrt(n)
model = module.initialize(w, W, inputs, labels)
query = module.query_coefficients(w, W, inputs, inputs, labels)
coefficient = module.bounded_gram_coefficients(w, W, inputs, labels, inputs)
(inputs, _, first, H, q, d, basis, gamma, beta,
 metadata) = module._coefficient_workspace(w, W, inputs, labels)
v = rng.normal(size=model.p)*.15
theta = rng.normal(size=(m, model.p))*.1
state = np.concatenate((v, theta.ravel()))

dw = np.einsum('ai,ain,ak->nk', theta, beta, inputs)
dW = np.einsum('ai,ain,ak->nk', theta, gamma, first)/n
L = d*((q*(inputs @ dw.T)) @ W.T+first @ dW.T)
readout = v @ basis
direct = (H+L) @ readout/n
rhs = model.rhs(0., state)
vdot, thetadot = model.unpack(rhs)
dw_dot = np.einsum('ai,ain,ak->nk', thetadot, beta, inputs)
dW_dot = np.einsum('ai,ain,ak->nk', thetadot, gamma, first)/n
L_dot = d*((q*(inputs @ dw_dot.T)) @ W.T+first @ dW_dot.T)
direct_derivative = ((H+L) @ (vdot @ basis)+L_dot @ readout)/n
residual = direct-labels
kernel = model.kernel(state)

checks = dict(
    state_size=model.size,
    expected_size=(m+1)**2,
    initial_output_error=float(np.max(np.abs(model.training_prediction(model.initial_state())))),
    direct_prediction_error=float(np.max(np.abs(direct-model.training_prediction(state)))),
    query_alias_error=float(np.max(np.abs(direct-model.predict(state, query)))),
    direct_derivative_error=float(np.max(np.abs(direct_derivative+model.alpha*kernel @ residual))),
    kernel_min_eigenvalue=float(np.linalg.eigvalsh(kernel)[0]),
    energy_identity_error=float(abs(2*v @ model.readout_gram @ vdot+2*model.alpha*residual @ direct)),
    mode_orthogonality=metadata['mode_orthogonality'],
    gate_G_error=float(np.max(np.abs(coefficient['G']-model.readout_gram))),
    gate_S_error=float(np.max(np.abs(coefficient['S']-model.response_gram))),
    gate_query_B_error=float(np.max(np.abs(coefficient['query_B']-query.response))),
    gate_initial_feature_error=float(np.max(np.abs(coefficient['R0'].T @ coefficient['G'] @ coefficient['R0']-H @ H.T/n))),
    gate_querydiag_error=float(np.max(np.abs(coefficient['querydiag']-np.diag(H @ H.T/n)))),
)

# Independent numerical one-dimensional outer integration of the analytic
# inner two integrals, with arbitrary positive rates and labels.
rates = np.array([.7, 1.1, 2.3])
amplitudes = np.array([.5, -.4, 1.2])
integral_errors = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            def integrand(t):
                inner = amplitudes[j]*amplitudes[k]/rates[k]*(
                    -np.expm1(-rates[j]*t)/rates[j]
                    + np.expm1(-(rates[j]+rates[k])*t)/(rates[j]+rates[k]))
                return -amplitudes[i]*np.exp(-rates[i]*t)*inner
            numerical, _ = quad(integrand, 0., np.inf, epsabs=1e-12, epsrel=1e-12)
            exact = -np.prod(amplitudes[[i,j,k]])/(
                rates[i]*(rates[i]+rates[j])*(rates[i]+rates[j]+rates[k]))
            integral_errors.append(abs(numerical-exact))
checks['terminal_integral_error'] = float(max(integral_errors))

# Mode selection must be invariant under a positive label rescaling.
rescaled = module._coefficient_workspace(w, W, inputs, labels*.03)[6]
checks['mode_amplitude_invariance_error'] = float(np.max(np.abs(rescaled-basis)))
zero_model = module.initialize(w, W, inputs, np.zeros(m))
checks['zero_labels_state_size'] = zero_model.size
checks['zero_labels_stationary_error'] = float(np.max(np.abs(zero_model.rhs(0.,zero_model.initial_state()))))

for name, value in checks.items():
    if name.endswith('_error'):
        assert value < 1e-10, (name, value)
assert checks['kernel_min_eigenvalue'] > 0
assert checks['state_size'] == checks['expected_size']

# Constructor-only timing at intended reference width and m=3.
started = time.monotonic()
n = 1024
w = np.random.default_rng(np.random.SeedSequence([1,1])).normal(size=(n,2))
W = np.random.default_rng(np.random.SeedSequence([1,101])).normal(size=(n,n))/np.sqrt(n)
large = module.bounded_gram_coefficients(w, W, inputs, labels, inputs)
checks['width_1024_constructor_seconds'] = time.monotonic()-started
checks['width_1024_coefficient_shapes'] = {key: list(value.shape) for key,value in large.items() if isinstance(value,np.ndarray)}
checks['width_1024_mode_metadata'] = large['mode_metadata']
print(json.dumps(checks, indent=2))
output = ROOT/'data/generated/structured_full_rank_scalar_20260926/cubic_minimal_mode_20260930'/f'check_{time.time_ns()}'
output.mkdir(parents=True,exist_ok=False)
(output/'check.json').write_text(json.dumps(checks,indent=2)+'\n')
