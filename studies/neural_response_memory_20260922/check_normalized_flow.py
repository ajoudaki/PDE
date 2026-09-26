"""Independent LayerNorm gradient/reconstruction checks and bounded width probes."""
import argparse
import json
from pathlib import Path
import numpy as np
import torch
from torch.nn import functional as F
from compact_flow import Flow


def gradient_checks():
    torch.set_num_threads(1)
    rng = np.random.default_rng(930)
    x, y = rng.normal(size=(5, 3)), rng.normal(size=5)
    maximum, count = 0., 0
    def close(a, b):
        nonlocal maximum, count
        torch.testing.assert_close(a, b, atol=2e-10, rtol=2e-10)
        maximum = max(maximum, float((a-b).abs().max().detach())); count += 1
    for norm in ['before', 'after']:
        for act in ['relu', 'gelu', 'selu']:
            for depth in [1, 3, 10]:
                for order in [None, 1, 3]:
                    model = Flow(x, y, width=11, depth=depth, activation=act,
                                 order=order, normalization=norm, device='cpu', dtype=torch.float64)
                    with torch.no_grad():
                        model.c.copy_(torch.tensor(rng.normal(size=11), dtype=torch.float64))
                        if order is not None:
                            model.s.fill_(.7)
                            for v in model.moments:
                                v.add_(torch.tensor(rng.normal(size=tuple(v.shape)), dtype=torch.float64)*.03)
                    factors = model._factors()
                    matrices = [w.clone() if factors is None else w+factors[i][0]@factors[i][1].T
                                for i, w in enumerate(model.matrices)]
                    params = [v.detach().clone().requires_grad_(True) for v in [model.w,*matrices,model.c]]
                    h = torch.tensor(x.T, dtype=torch.float64)
                    for w in params[:-1]:
                        z = w@h
                        ln = lambda q: F.layer_norm(q.T, (model.n,), eps=model.norm_eps).T
                        if norm == 'before': z = ln(z)
                        h = getattr(F, act)(z)
                        if norm == 'after': h = ln(h)
                    prediction = params[-1]@h/model.n
                    loss = (prediction-torch.tensor(y)).square().mean()
                    grads = torch.autograd.grad(loss, params)
                    close(model.predict(x), prediction.detach())
                    velocities = model.rhs()
                    close(velocities[0], -model.n*grads[0])
                    close(velocities[1 if order is not None else -1], -model.n*grads[-1])
                    if order is None:
                        for actual, expected in zip(velocities[1:-1], grads[1:-1]): close(actual, -expected)
                    # Queries must not use cross-sample normalization statistics.
                    close(model.predict(x), torch.cat([model.predict(x[i:i+1]) for i in range(len(x))]))
    return dict(assertions=count, max_absolute_error=maximum)


def coordinates(device, out):
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    rng = np.random.default_rng(20260925)
    x = rng.normal(size=(32,3)); x /= np.linalg.norm(x,axis=1,keepdims=True)
    y = np.sqrt(15)*x[:,0]*x[:,1]
    rows = []
    for depth in [10,20]:
        for norm in ['before','after']:
            for n in [256,512,1024]:
                m = Flow(x,y,width=n,depth=depth,activation='gelu',normalization=norm,device=device)
                initial = [v.clone() for v in m._forward(m.inputs,None)[0]]
                fit = m.fit(step=1/128, max_steps=256, block=8, target_rms=1e-10, max_seconds=10)
                assert fit['steps']==256 and np.isfinite(fit['rms']), fit
                final = m._forward(m.inputs,None)[0]
                rows.append(dict(depth=depth,normalization=norm,width=n,physical_time=2.,**{
                    'feature_rms':[float(v.square().mean().sqrt().cpu()) for v in final],
                    'feature_change_rms':[float((v-u).square().mean().sqrt().cpu()) for u,v in zip(initial,final)],
                    'train_rms':fit['rms']}))
                print(json.dumps(rows[-1]),flush=True)
                del m
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(rows,indent=2)+'\n')


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--device'); p.add_argument('--out',type=Path)
    a=p.parse_args()
    if a.device: coordinates(a.device,a.out)
    else: print(json.dumps(gradient_checks()))
