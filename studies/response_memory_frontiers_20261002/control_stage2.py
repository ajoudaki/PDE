"""Frozen stage-two control gate. Study-owned code; no maintained API changes."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import pathlib
import time
import numpy as np
import torch
from control_pilot import DTYPE, Model, features, scalar, source_sha, frozen_kernel, check_rhs

POLICIES = ('P2', 'P32', 'NP', 'SAFE')
OBS = np.arange(385, dtype=float) / 16


def control(t, policy, device):
    mean = .15 if t < 12 else .35
    if policy == 'SAFE':
        lam = .65
    elif policy == 'AVG':
        lam = mean
    elif policy == 'NP':
        signs = (1, 1, 1, -1, -1, 1, -1, -1)
        if t >= 12:
            signs = signs[::-1]
        lam = mean + .1 * signs[min(7, int((t % 12) / 1.5))]
    else:
        periods = int(policy[1:])
        phase = (t % 12) * periods / 12
        lam = mean + (.1 if phase % 1 < .5 else -.1)
    return torch.tensor([2*lam]*8 + [2*(1-lam)]*8, dtype=DTYPE, device=device)


def truncated_sum(left, right, rank):
    """Best Frobenius rank-r approximation of A B^T via thin QR/small SVD."""
    a, b = torch.cat(left, 1), torch.cat(right, 1)
    qa, ra = torch.linalg.qr(a, mode='reduced')
    qb, rb = torch.linalg.qr(b, mode='reduced')
    u, s, vh = torch.linalg.svd(ra @ rb.T, full_matrices=False)
    r = min(rank, len(s))
    return qa @ u[:, :r], s[:r], qb @ vh[:r].T


class LowRank:
    q = 0
    def __init__(self, x, y, base, rank):
        self.x, self.y, self.base, self.rank = x, y, base, rank
        self.m, self.d = x.shape

    def start(self, checkpoint):
        w1, _, w = checkpoint
        empty = w.new_empty((len(w), 0))
        return [w1.clone(), w.clone(), empty, w.new_empty(0), empty.clone()]

    def evaluate(self, s, x=None):
        if x is None:
            x = self.x
        w1, w, u, sv, v = s
        h1 = torch.tanh(x @ w1.T / math.sqrt(self.d))
        h2 = torch.tanh(h1 @ self.base.T + (h1 @ v * sv) @ u.T)
        return h1, h2, h2 @ w / len(w)

    def rhs(self, s, weight):
        w1, w, u, sv, v = s
        h1, h2, f = self.evaluate(s)
        drive = weight * (f-self.y)
        d2 = (1-h2.square())*w
        back = d2 @ self.base + (d2 @ u * sv) @ v.T
        d1 = (1-h1.square()) * back
        dw1 = -2/self.m * ((drive[:, None]*d1).T @ self.x) / math.sqrt(self.d)
        dw = -2/self.m * (drive @ h2)
        b = -2/(len(w)*self.m) * (drive[:, None]*d2).T
        return dw1, dw, b, h1.T

    def step(self, s, weight, dt):
        w1, w, u, sv, v = s
        a, b, l1, r1 = self.rhs(s, weight)
        up, sp, vp = truncated_sum([u*sv, dt*l1], [v, r1], self.rank)
        pred = [w1+dt*a, w+dt*b, up, sp, vp]
        c, d, l2, r2 = self.rhs(pred, weight)
        un, sn, vn = truncated_sum([u*sv, dt/2*l1, dt/2*l2], [v, r1, r2], self.rank)
        return [w1+dt/2*(a+c), w+dt/2*(b+d), un, sn, vn]


def step(model, s, u, dt):
    if isinstance(model, LowRank):
        return model.step(s, u, dt)
    k1 = model.rhs(s, u)
    pred = [v+dt*k for v, k in zip(s, k1)]
    k2 = model.rhs(pred, u)
    return [v+dt/2*(a+b) for v, a, b in zip(s, k1, k2)]


def checks():
    torch.set_num_threads(1)
    out = check_rhs()
    g = torch.Generator().manual_seed(10421)
    rand = lambda *shape: torch.randn(*shape, dtype=DTYPE, generator=g)
    left, right = [rand(9, 3), rand(9, 4)], [rand(9, 3), rand(9, 4)]
    full = sum(a@b.T for a, b in zip(left, right))
    u, s, v = truncated_sum(left, right, 4)
    uf, sf, vf = torch.linalg.svd(full, full_matrices=False)
    ref = (uf[:, :4]*sf[:4])@vf[:4]
    out['incremental_svd_error'] = scalar(((u*s)@v.T-ref).abs().max())
    x, y = rand(4, 3), rand(4)
    checkpoint = [rand(7, 3), rand(7, 7)/math.sqrt(7), rand(7)]
    dense = Model(x, y)
    lr = LowRank(x, y, checkpoint[1], 7)
    sd, sl = dense.start(checkpoint), lr.start(checkpoint)
    weight = torch.tensor([0., .4, 1., 2.], dtype=DTYPE)
    for _ in range(3):
        sd, sl = step(dense, sd, weight, .03), step(lr, sl, weight, .03)
    physical = [sl[0], checkpoint[1]+(sl[2]*sl[3])@sl[4].T, sl[1]]
    out['uncapped_heun_error'] = max(scalar((a-b).abs().max()) for a, b in zip(sd, physical))
    # An independent autograd check of all canonical dense mobilities.
    differentiable = [v.clone().requires_grad_() for v in checkpoint]
    loss = (weight*(features(x, *differentiable)[2]-y).square()).mean()
    grads = torch.autograd.grad(loss, differentiable)
    rhs = dense.rhs(checkpoint, weight)
    out['autograd_dense_error'] = max(scalar((vel+mob*grad).abs().max())
        for vel, mob, grad in zip(rhs, (7, 1, 7), grads))
    # Exposure equality and exact event resolution on the universal mesh.
    exposure = {}
    for policy in (*POLICIES, 'AVG'):
        weights = np.array([control((a+b)/2, policy, 'cpu').numpy()
                            for a, b in zip(OBS, OBS[1:])])
        exposure[policy] = (weights.sum(0)/16).tolist()
    out['exposure'] = exposure
    assert max(out[k] for k in ('incremental_svd_error', 'uncapped_heun_error', 'autograd_dense_error')) < 1e-11
    assert np.allclose(exposure['P2'], exposure['P32'])
    assert np.allclose(exposure['P2'], exposure['NP'])
    assert np.allclose(exposure['P2'], exposure['AVG'])
    return out


def dataset(device):
    import sklearn
    from sklearn.datasets import load_digits
    data = load_digits()
    rng = np.random.default_rng(20261003)
    groups = {k: [] for k in ('old_train', 'new_train', 'old_query', 'new_query')}
    for digit in (3, 8):
        ids = rng.permutation(np.flatnonzero(data.target == digit))
        for key, part in zip(groups, (ids[:4], ids[4:8], ids[8:72], ids[72:136])):
            groups[key].extend(part.tolist())
    xx, yy = {}, {}
    for key, ids in groups.items():
        ims = data.images[ids].copy()
        if key.startswith('new'):
            ims = np.rot90(ims, axes=(1, 2))
        flat = ims.reshape(len(ids), -1).copy()
        flat *= math.sqrt(64)/np.linalg.norm(flat, axis=1, keepdims=True)
        xx[key] = torch.tensor(flat, dtype=DTYPE, device=device)
        yy[key] = torch.tensor(np.where(data.target[ids] == 3, -1., 1.), dtype=DTYPE, device=device)
    assert len(set(sum(groups.values(), []))) == 272
    manifest = dict(indices=groups, sklearn=sklearn.__version__,
                    raw_sha256=hashlib.sha256(data.images.tobytes()+data.target.tobytes()).hexdigest(),
                    source_description=data.DESCR)
    return (torch.cat([xx['old_train'], xx['new_train']]),
            torch.cat([yy['old_train'], yy['new_train']]),
            torch.cat([xx['old_query'], xx['new_query']]),
            torch.cat([yy['old_query'], yy['new_query']]), manifest)


def sync(device):
    if str(device).startswith('cuda'):
        torch.cuda.synchronize(device)


def integrate(model, initial, xquery, h1checkpoint, policy, dt, name, output, deadline, pretrain=False):
    sync(model.x.device)
    if model.x.is_cuda:
        torch.cuda.reset_peak_memory_stats(model.x.device)
        initial_allocated = torch.cuda.memory_allocated(model.x.device)
    else:
        initial_allocated = 0
    started = time.monotonic()
    # Caller supplies an owned branch start. Updates are out of place; avoid
    # retaining a redundant initial branch throughout the resource measurement.
    s = initial
    initial = None
    times = np.arange(1281)/16 if pretrain else OBS
    ts, preds, rows = [], [], []
    t, count, fitted = 0., 0, False
    last_log = started
    def save():
        h1, _, f = model.evaluate(s)
        row = dict(time=t, mse=scalar((f-model.y).square().mean()))
        if h1checkpoint is not None:
            row['h1_motion'] = scalar((h1-h1checkpoint).square().mean().sqrt())
        if model.q:
            dh, db, eb, eh = [v.clamp_min(0) for v in s[5:9]]
            row.update(forward_error=scalar((dh.sum()/eh.sum().clamp_min(1e-300)).sqrt()),
                       backward_error=scalar((db.sum()/eb.sum().clamp_min(1e-300)).sqrt()) if scalar(eb.sum()) > 0 else None,
                       tau=scalar(s[4]))
        ts.append(t)
        preds.append(model.evaluate(s, xquery)[2].detach().cpu().numpy())
        rows.append(row)
    save()
    for stop in times[1:]:
        while t < stop-1e-12:
            now = time.monotonic()
            if now >= deadline:
                raise TimeoutError(f'1200-second aggregate cap at {name}, t={t}')
            if now-last_log >= 20:
                print(json.dumps(dict(event='progress', name=name, t=t, elapsed=now-started)), flush=True)
                last_log = now
            h = min(dt, stop-t)
            weight = torch.ones(model.m, dtype=DTYPE, device=model.x.device) if pretrain else control(t+h/2, policy, model.x.device)
            s = step(model, s, weight, h)
            t += h
            count += 1
            if pretrain and scalar((model.evaluate(s)[2]-model.y).square().mean()) <= .001:
                fitted = True
                break
        save()
        if fitted:
            break
    sync(model.x.device)
    peak = torch.cuda.max_memory_allocated(model.x.device) if model.x.is_cuda else 0
    result = dict(name=name, policy=policy, dt=dt, steps=count, fitted=fitted,
                  elapsed=time.monotonic()-started, metrics=rows,
                  start_cuda_allocated=initial_allocated, peak_cuda_allocated=peak,
                  peak_increment=peak-initial_allocated)
    arr = np.array(preds)
    if not np.isfinite(arr).all():
        raise FloatingPointError(f'Nonfinite predictions in {name}')
    np.savez_compressed(output/f'{name}.npz', time=ts, predictions=arr)
    (output/f'{name}.json').write_text(json.dumps(result, indent=2))
    torch.save([v.detach().cpu() for v in s], output/f'{name}_terminal.pt')
    print(json.dumps(dict(event='completed', name=name, elapsed=result['elapsed'], steps=count,
                          mse=rows[-1]['mse'], peak_cuda_allocated=peak)), flush=True)
    return s, result


def kernel_run(checkpoint, x, y, xquery, policy, output):
    from scipy.linalg import expm
    kxx, kqx, f0, fq0 = frozen_kernel(checkpoint, x, xquery)
    residual = f0-y.cpu().numpy()
    coeff = np.zeros(len(residual))
    predictions = [fq0]
    cache = {}
    for left, right in zip(OBS, OBS[1:]):
        weight = control((left+right)/2, policy, 'cpu').numpy()
        key = tuple(weight)
        if key not in cache:
            mat = np.zeros((len(weight)+1, len(weight)+1))
            mat[:-1, :-1] = -2/len(weight)*weight[:, None]*kxx
            mat[:-1, -1] = -2/len(weight)*weight*residual
            cache[key] = expm((right-left)*mat)
        coeff = (cache[key] @ np.r_[coeff, 1])[:-1]
        predictions.append(fq0+kqx@coeff)
    np.savez_compressed(output/f'NTK_{policy}.npz', time=OBS, predictions=predictions)


def analyze(output):
    def load(name):
        data = np.load(output/f'{name}.npz')
        assert np.array_equal(data['time'], OBS)
        return data['predictions']
    labels = np.load(output/'query_labels.npy')
    start = load('dense_P2_fine')[0]
    def metric(pred):
        c = float(np.sqrt(np.mean((pred[:, :128]-start[:128])**2, axis=1)).max())
        rmse = np.sqrt(np.mean((pred[:, 128:]-labels[128:])**2, axis=1))
        return dict(C=c, J=float(np.trapz(rmse, OBS)/24))
    methods = ('dense', 'q3', 'svd47', 'NTK', 'average')
    metrics = {method: {} for method in methods}
    errors, refinement, mechanism, timings = {}, {}, {}, {}
    for policy in POLICIES:
        truth = load(f'dense_{policy}_fine')
        errors[policy] = {}
        for method in methods:
            if method == 'NTK':
                pred = load(f'NTK_{policy}')
            elif method == 'average':
                pred = load('dense_SAFE_fine' if policy == 'SAFE' else 'dense_AVG_fine')
            else:
                pred = load(f'{method}_{policy}_fine')
                coarse = load(f'{method}_{policy}_coarse')
                refinement[f'{method}_{policy}'] = float(np.sqrt(np.mean((pred-coarse)**2, axis=1)).max())
                timing = json.loads((output/f'{method}_{policy}_fine.json').read_text())
                timings[f'{method}_{policy}'] = {key: timing[key] for key in
                    ('elapsed', 'steps', 'start_cuda_allocated', 'peak_cuda_allocated', 'peak_increment')}
            metrics[method][policy] = metric(pred)
            errors[policy][method] = float(np.sqrt(np.mean((pred-truth)**2, axis=1)).max())
        dense_rows = json.loads((output/f'dense_{policy}_fine.json').read_text())['metrics']
        mem_rows = json.loads((output/f'q3_{policy}_fine.json').read_text())['metrics']
        mechanism[policy] = dict(dense_h1_motion=max(v['h1_motion'] for v in dense_rows),
                                 q3_h1_motion=max(v['h1_motion'] for v in mem_rows),
                                 q3_credit_error=mem_rows[-1]['backward_error'],
                                 q3_forward_error=mem_rows[-1]['forward_error'])
    refinement['dense_AVG'] = float(np.sqrt(np.mean((load('dense_AVG_fine')-load('dense_AVG_coarse'))**2, axis=1)).max())
    selections = {}
    oracle_feasible = [p for p in POLICIES if metrics['dense'][p]['C'] <= .25]
    oracle_j = min((metrics['dense'][p]['J'] for p in oracle_feasible), default=math.inf)
    for method in methods:
        feasible = [p for p in POLICIES if metrics[method][p]['C'] <= .25]
        chosen = min(feasible, key=lambda p: metrics[method][p]['J']) if feasible else None
        selections[method] = dict(policy=chosen, predicted_feasible=feasible)
        if chosen:
            actual = metrics['dense'][chosen]
            selections[method].update(dense_C=actual['C'], dense_J=actual['J'], regret=actual['J']-oracle_j)
    numeric = max(refinement.values()) <= .003
    cs = [v['C'] for v in metrics['dense'].values()]
    js = [v['J'] for v in metrics['dense'].values()]
    nontrivial = min(cs) <= .23 and max(cs) >= .27 and max(js)-min(js) >= .03
    witnesses = [p for p in POLICIES if errors[p]['q3'] <= .02 and
                 mechanism[p]['q3_credit_error'] >= .30 and
                 min(mechanism[p]['dense_h1_motion'], mechanism[p]['q3_h1_motion']) >= .10]
    mem, lr = selections['q3'], selections['svd47']
    mem_useful = bool(mem['policy'] and mem['dense_C'] <= .25 and mem['regret'] <= .02)
    lr_bad = bool(not lr['policy'] or lr['dense_C'] >= .27 or lr['regret'] >= .05)
    lr_matches = bool(lr['policy'] and mem['policy'] and lr['dense_C'] <= .25 and
                      lr['regret'] <= mem['regret']+1e-12 and
                      max(errors[p]['svd47'] for p in POLICIES) <= .02)
    result = dict(metrics=metrics, errors=errors, refinements=refinement,
                  mechanism=mechanism, selections=selections, timings=timings,
                  gates=dict(numerical_validity=numeric, nontrivial_menu=nontrivial,
                             same_policy_witnesses=witnesses, memory_choice_useful=mem_useful,
                             distinctive_decision_advantage=bool(numeric and nontrivial and mem_useful and lr_bad),
                             generic_low_rank_sufficient=lr_matches))
    (output/'analysis.json').write_text(json.dumps(result, indent=2, allow_nan=False))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='cpu')
    parser.add_argument('--output', type=pathlib.Path, required=True)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--analyze-only', action='store_true')
    args = parser.parse_args()
    if args.analyze_only:
        print(json.dumps(analyze(args.output), indent=2))
        return
    validation = checks()
    print(json.dumps(dict(event='checks', **validation)), flush=True)
    if args.check_only:
        return
    args.output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    deadline = started+1200
    x, y, xquery, yquery, manifest = dataset(args.device)
    (args.output/'dataset.json').write_text(json.dumps(manifest, indent=2))
    np.save(args.output/'query_labels.npy', yquery.cpu().numpy())
    here = pathlib.Path(__file__).parent
    config = dict(seed=20261003, n=512, m=16, q=3, rank=47, d=64, device=args.device,
                  torch=torch.__version__, checks=validation, max_fits=27, seconds_cap=1200,
                  hashes={name: source_sha(here/name) for name in
                          ('control_stage2.py', 'control_pilot.py', 'CONTROL_STAGE2_PREREG.md')},
                  moving_scalars=dict(dense=512*64+512*512+512,
                      q3=512*64+512+2*16*3*512+1, q3_optional_diagnostics=64,
                      svd47=512*64+512+(2*512+1)*47), shared_hidden_checkpoint_scalars=512*512)
    (args.output/'config.json').write_text(json.dumps(config, indent=2))
    generator = torch.Generator().manual_seed(20261003)
    checkpoint = [torch.randn(512, 64, dtype=DTYPE, generator=generator).to(args.device),
                  (torch.randn(512, 512, dtype=DTYPE, generator=generator)/math.sqrt(512)).to(args.device),
                  torch.zeros(512, dtype=DTYPE, device=args.device)]
    status = dict(completed=False, fit_count=0)
    try:
        model = Model(x[:8], y[:8])
        status['fit_count'] += 1
        checkpoint, pre = integrate(model, checkpoint, xquery, None, None, 1/128,
                                    'old_pretrain', args.output, deadline, pretrain=True)
        if not pre['fitted']:
            status['failure'] = 'Pretrain fit gate failed; no expansion.'
            return
        h1checkpoint = features(x, *checkpoint)[0]
        # Control tables and kernels are computed before any new policy outcome.
        for policy in POLICIES:
            kernel_run(checkpoint, x, y, xquery, policy, args.output)
        tables = {policy: [control((a+b)/2, policy, 'cpu').tolist()
                           for a, b in zip(OBS, OBS[1:])] for policy in (*POLICIES, 'AVG')}
        (args.output/'controls.json').write_text(json.dumps(dict(times=OBS.tolist(), values=tables), indent=2))
        for policy in POLICIES:
            for label in ('dense', 'q3', 'svd47'):
                model = (LowRank(x, y, checkpoint[1], 47) if label == 'svd47' else
                         Model(x, y, 3, checkpoint[1]) if label == 'q3' else Model(x, y))
                for resolution, dt in (('coarse', 1/64), ('fine', 1/128)):
                    if status['fit_count'] >= 27:
                        raise RuntimeError('Hard trajectory count exceeded')
                    status['fit_count'] += 1
                    integrate(model, model.start(checkpoint), xquery, h1checkpoint,
                              policy, dt, f'{label}_{policy}_{resolution}', args.output, deadline)
        model = Model(x, y)
        for resolution, dt in (('coarse', 1/64), ('fine', 1/128)):
            status['fit_count'] += 1
            integrate(model, model.start(checkpoint), xquery, h1checkpoint, 'AVG', dt,
                      f'dense_AVG_{resolution}', args.output, deadline)
        result = analyze(args.output)
        status.update(completed=True, gates=result['gates'])
    except Exception as exc:
        status['failure'] = f'{type(exc).__name__}: {exc}'
        raise
    finally:
        sync(args.device)
        status['elapsed'] = time.monotonic()-started
        (args.output/'status.json').write_text(json.dumps(status, indent=2))
        print(json.dumps(dict(event='terminal', **status)), flush=True)


if __name__ == '__main__':
    main()
