"""Independent CPU checks, no training; uses full raw-coordinate autograd."""
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "studies/neural_response_memory_20260922"
sys.path.insert(0, str(SOURCE))
from factor_control_engine import FactorEngine, FactorState, error_ratio, heun_trial

torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
dtype = torch.float64
results = []
for n, d, rank, count in [(5, 2, 3, 4), (11, 3, 5, 7), (17, 2, 7, 8)]:
    rng = np.random.default_rng(176 + n)
    x = rng.standard_normal((count, d))
    labels = rng.standard_normal(count)
    engine = FactorEngine(d, n, rank, x / np.sqrt(d), labels)
    initial = engine.initial_state()
    state = FactorState(*(torch.tensor(rng.standard_normal(z.shape), dtype=dtype)
                          for z in initial.tensors()))
    # Canonical raw W1, W3; physical inputs x independently divide by sqrt(d).
    w, c, A, B = [z.clone().requires_grad_() for z in state.tensors()]
    raw_x = torch.tensor(x, dtype=dtype)
    actual_middle = engine.W0 + A @ B
    predicted = (torch.tanh(torch.tanh(raw_x @ w.T / np.sqrt(d))
                             @ actual_middle.T) @ c) / n
    loss = ((predicted - torch.tensor(labels, dtype=dtype)) ** 2).sum() / count
    gradients = torch.autograd.grad(loss, (w, c, A, B, actual_middle), retain_graph=True)
    rhs = engine.rhs(state)
    errors = {}
    for name, actual, grad, mobility in zip(state.names(), rhs.tensors(), gradients[:4], (n, n, 1, 1)):
        error = float((actual + mobility * grad).abs().max())
        errors[name] = error
        torch.testing.assert_close(actual, -mobility * grad, rtol=2e-12, atol=2e-13)
    errors['prediction'] = float((engine.predict(state, x/np.sqrt(d))-predicted).abs().max())
    errors['loss'] = abs(float(engine.loss(state))-float(loss))
    induced = rhs.A @ state.B + state.A @ rhs.B
    G = gradients[-1]
    target_induced = -G @ state.B.T @ state.B - state.A @ state.A.T @ G
    torch.testing.assert_close(induced, target_induced, rtol=2e-12, atol=2e-13)
    errors['induced_velocity'] = float((induced-target_induced).abs().max())
    dissipation = sum(float((g*v).sum()) for g,v in zip(gradients[:4], rhs.tensors()))
    expected_dissipation = -sum(float(v.square().sum())/m for v,m in zip(rhs.tensors(), (n,n,1,1)))
    assert abs(dissipation-expected_dissipation) <= 1e-11*max(1,abs(dissipation))
    probe = torch.tensor(rng.standard_normal((n, 6)), dtype=dtype)
    M = engine.W0+state.A@state.B
    torch.testing.assert_close(engine.apply_hidden(state,probe),M@probe,rtol=2e-13,atol=2e-13)
    torch.testing.assert_close(engine.apply_hidden(state,probe,transpose=True),M.T@probe,rtol=2e-13,atol=2e-13)
    init_rng = np.random.default_rng(20260920)
    np.testing.assert_array_equal(initial.w.numpy(), init_rng.standard_normal((n,d)))
    np.testing.assert_array_equal(engine.W0.numpy(), init_rng.standard_normal((n,n))/np.sqrt(n))
    np.testing.assert_array_equal(initial.c.numpy(), init_rng.standard_normal(n)/n)
    np.testing.assert_array_equal(initial.A.numpy(), np.zeros((n,rank)))
    np.testing.assert_array_equal(initial.B.numpy(), np.random.default_rng(20260924).standard_normal((rank,n))/np.sqrt(rank))
    # Explicit full-matrix Heun/Euler difference is independent of low-rank norm helper.
    step, rtol, atol = 0.013, 6.25e-5, 6.25e-7
    euler = state.add_scaled(rhs, step)
    candidate, ratio = heun_trial(engine,state,step,rtol,atol)
    other_rhs = engine.rhs(euler)
    for z, s, k1, k2 in zip(candidate.tensors(),state.tensors(),rhs.tensors(),other_rhs.tensors()):
        torch.testing.assert_close(z,s+(step/2)*(k1+k2),rtol=0,atol=0)
    coord_ratios=[]
    for s,e,h in zip(state.tensors(),euler.tensors(),candidate.tensors()):
        coord_ratios.append(float((h-e).square().mean().sqrt())/(atol+rtol*max(1,float(s.square().mean().sqrt()),float(h.square().mean().sqrt()))))
    correction_error=float((candidate.A@candidate.B-euler.A@euler.B).norm())
    correction_scale=max(1,float((state.A@state.B).norm()),float((candidate.A@candidate.B).norm()))
    dense_ratio=max(*coord_ratios,correction_error/(atol+rtol*correction_scale))
    assert abs(ratio-dense_ratio) <= 1e-9*max(1,dense_ratio)
    errors['controller_ratio_absolute'] = abs(ratio-dense_ratio)
    results.append(dict(n=n,d=d,rank=rank,samples=count,max_abs_errors=errors,
                        loss=float(loss),energy_derivative=dissipation,controller_ratio=ratio))

result = {'status':'PASS','scope':'deterministic CPU algebra only; no trajectories trained',
          'cases':results,'source_sha256':{name:hashlib.sha256((SOURCE/name).read_bytes()).hexdigest()
                  for name in ['factor_control_engine.py','run_factor_control.py','test_factor_control.py']}}
out=ROOT/'data/generated/neural_response_memory_20260922/factor_audit01/engine_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
