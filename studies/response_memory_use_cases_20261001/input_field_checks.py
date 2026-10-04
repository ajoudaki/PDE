"""Small deterministic CPU checks; no fit campaign."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
import torch
from baseline_compact_flow import Flow
from input_field import InputFieldFlow, fourier, grid, circle, teacher, internal_matrix, make_model, set_batch


@torch.no_grad()
def run():
    torch.set_num_threads(1)
    torch.manual_seed(733)
    errors = []
    def close(a, b):
        errors.append(float((a-b).abs().max()))
        torch.testing.assert_close(a, b, atol=1e-10, rtol=1e-10)
    m, n, q = 7, 12, 4
    theta = grid(m); x, y = circle(theta), teacher(theta, 'A')
    close(x.square().sum(dim=1), torch.ones(m,dtype=torch.float64))
    raw_x=math.sqrt(2)*torch.stack((theta.cos(),theta.sin()),dim=-1)
    close(x,raw_x/math.sqrt(2))
    kw = dict(width=n, depth=2, activation='tanh', seed=811, device='cpu', dtype=torch.float64, readout_std=1.)
    sample = Flow(x, y, order=q, **kw); sample.c.zero_()
    field = InputFieldFlow(x, y, math.sqrt(m)*torch.eye(m, dtype=torch.float64), order=q, **kw)
    for k in range(12):
        close(sample.predict(x), field.predict(x)); close(internal_matrix(sample), internal_matrix(field))
        a, b = sample.rhs(), field.rhs()
        for index in (0, 1, 4): close(a[index], b[index])
        for index in (2, 3): close(a[index]/math.sqrt(m), b[index])
        for A, B in zip(sample.moments, field.moments): close(A/math.sqrt(m), B)
        sample.step(.0125); field.step(.0125)
    p = fourier(grid(128), 17)
    close(p.T@p/128, torch.eye(17, dtype=torch.float64))
    # Product projection in L2(input probability x clock Lebesgue measure).
    nt, nx, C, q, tau = 16, 32, 5, 3, 2.3
    nodes, weights = np.polynomial.legendre.leggauss(nt)
    wt = torch.tensor(weights*tau/2, dtype=torch.float64)
    leg = torch.tensor(np.polynomial.legendre.legvander(nodes, q-1), dtype=torch.float64)
    psi = fourier(grid(nx), C)
    h = torch.randn(nt, nx, 4, dtype=torch.float64)
    d = torch.randn(nt, nx, 3, dtype=torch.float64)
    def project(v):
        moments = torch.einsum('t,txa,xc,tj->cja', wt, v, psi, leg)/nx
        projected = torch.einsum('cja,xc,tj,j->txa', moments, psi, leg,
                                 (2*torch.arange(q, dtype=torch.float64)+1)/tau)
        return moments, projected
    hm, hp = project(h); dm, dp = project(d)
    full = torch.einsum('t,txa,txb->ab', wt, d, h)/nx
    retained = torch.einsum('cja,cjb,j->ab', dm, hm, (2*torch.arange(q, dtype=torch.float64)+1)/tau)
    tail = torch.einsum('t,txa,txb->ab', wt, d-dp, h-hp)/nx
    close(full-retained, tail)
    # Short Euler refinement checks the same autonomous ODE, not fitting quality.
    theta = grid(16)
    predictions = []
    for dt in (1/32, 1/64, 1/128):
        f = make_model('field', n=16, seed=733, device='cpu', dtype=torch.float64,
                       theta=theta, name='A', count=9, order=3, prefix_nodes=64)
        for _ in range(round(2/dt)): f.step(dt)
        predictions.append(f.predict(circle(theta)))
    coarse = float((predictions[0]-predictions[1]).square().mean().sqrt())
    fine = float((predictions[1]-predictions[2]).square().mean().sqrt())
    assert 1.7 < coarse/fine < 2.3, (coarse, fine)
    # Resume from moving coordinates and the fixed initialized matrix. New
    # observations are supplied once; no earlier input/label arrays are needed.
    restarted=make_model('field', n=16, seed=733, device='cpu', dtype=torch.float64,
                         theta=grid(3), name='A', count=9, order=3, prefix_nodes=64)
    for target, source in zip(restarted.state,f.state): target.copy_(source)
    for _ in range(6):
        fresh=2*math.pi*torch.rand(5,dtype=torch.float64)
        for model in [f,restarted]:
            set_batch(model,fresh,teacher(fresh,'A'));model.step(1/128)
        for a,b in zip(f.state,restarted.state):close(a,b)
    close(f.predict(circle(theta)),restarted.predict(circle(theta)))
    # Explicitly demonstrate finite-batch product bias; same-index covariance survives.
    a = torch.tensor([1., 2., 4.], dtype=torch.float64)
    b = torch.tensor([3., -1., 5.], dtype=torch.float64)
    product_of_means = float(a.mean()*b.mean())
    one_draw_product_mean = float((a*b).mean())
    assert abs(product_of_means-one_draw_product_mean) > .1
    return dict(status='pass', assertions=len(errors)+3, maximum_error=max(errors),restartability='pass',
                normalization='canonical raw norm sqrt(d), API row norm one',
                euler_prediction_differences=[coarse, fine], euler_ratio=coarse/fine,
                stochastic_product_counterexample=dict(product_of_means=product_of_means,
                                                       mean_product=one_draw_product_mean))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--out', type=Path, required=True)
    args=parser.parse_args(); started=time.perf_counter()
    result=run(); result.update(seconds=time.perf_counter()-started, command=sys.argv,
                               torch=torch.__version__, numpy=np.__version__,
                               hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                                       for p in [Path(__file__), Path(__file__).with_name('input_field.py'),
                                                 Path(__file__).with_name('baseline_compact_flow.py')]})
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x') as stream: json.dump(result, stream, indent=2)
    print(json.dumps(result, indent=2))
