"""Frozen CONTROL_CANDIDATE pilot; study-owned implementation, no maintained API.

No autograd tape or dense learned matrix is retained for a memory branch.
Run with CUDA_VISIBLE_DEVICES=0 and --device cuda:0 after GPU allocation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import time
from dataclasses import dataclass

import numpy as np
import torch


DTYPE = torch.float64


def scalar(x):
    return float(x.detach().cpu())


def source_sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def features(x, w1, w2, w):
    h1 = torch.tanh(x @ w1.T / math.sqrt(x.shape[1]))
    h2 = torch.tanh(h1 @ w2.T)
    return h1, h2, h2 @ w / len(w)


@dataclass
class Model:
    x: torch.Tensor
    y: torch.Tensor
    q: int = 0
    base: torch.Tensor | None = None

    def __post_init__(self):
        self.m, self.d = self.x.shape
        if self.q:
            self.weights = torch.arange(self.q, device=self.x.device,
                                        dtype=DTYPE) * 2 + 1
            self.tri = torch.tril(self.weights.expand(self.q, -1), diagonal=-1)
            self.tri = self.tri + torch.diag(torch.arange(
                self.q, device=self.x.device, dtype=DTYPE))

    def evaluate(self, s, x=None):
        if x is None:
            x = self.x
        if not self.q:
            return features(x, *s[:3])
        w1, w, hm, bm, tau = s[:5]
        n = w.numel()
        h1 = torch.tanh(x @ w1.T / math.sqrt(self.d))
        hf = hm.reshape(-1, n)
        bf = bm.reshape(-1, n)
        wt = self.weights.repeat(self.m)
        z2 = h1 @ self.base.T - 2 / (n * self.m * tau) * (
            (h1 @ hf.T * wt) @ bf)
        h2 = torch.tanh(z2)
        return h1, h2, h2 @ w / n

    def rhs(self, s, u):
        h1, h2, f = self.evaluate(s)
        if self.q:
            w1, w, hm, bm, tau = s[:5]
        else:
            w1, w2, w = s[:3]
        n = w.numel()
        drive = u * (f - self.y)
        d2 = (1 - h2.square()) * w
        if self.q:
            hf, bf = hm.reshape(-1, n), bm.reshape(-1, n)
            wt = self.weights.repeat(self.m)
            back = d2 @ self.base - 2 / (n * self.m * tau) * (
                (d2 @ bf.T * wt) @ hf)
        else:
            back = d2 @ w2
        d1 = (1 - h1.square()) * back
        dw1 = -2 / self.m * ((drive[:, None] * d1).T @ self.x) / math.sqrt(self.d)
        dw = -2 / self.m * (drive @ h2)
        if not self.q:
            dw2 = -2 / (n * self.m) * ((drive[:, None] * d2).T @ h1)
            return [dw1, dw2, dw]
        rho = drive.square().mean().sqrt()
        dhm = rho * h1[:, None, :] - rho / tau * torch.einsum(
            'jk,akn->ajn', self.tri, hm)
        dbm = (drive[:, None] * d2)[:, None, :] - rho / tau * torch.einsum(
            'jk,akn->ajn', self.tri, bm)
        # No division by the residual in the evolved physical/moment state.
        # This guarded ratio is used only for nonnegative diagnostic energies.
        credit = drive[:, None] * d2 / rho.clamp_min(torch.finfo(DTYPE).tiny)
        hstar = (hm * self.weights[None, :, None]).sum(1) / tau
        bstar = (bm * self.weights[None, :, None]).sum(1) / tau
        ddh = rho * (h1 - hstar).square().sum(1)
        ddb = rho * (credit - bstar).square().sum(1)
        deb = rho * credit.square().sum(1)
        deh = rho * h1.square().sum(1)
        return [dw1, dw, dhm, dbm, rho, ddh, ddb, deb, deh]

    def start(self, checkpoint):
        if not self.q:
            return [v.clone() for v in checkpoint]
        w1, _, w = checkpoint
        h1 = torch.tanh(self.x @ w1.T / math.sqrt(self.d))
        hm = torch.zeros(self.m, self.q, w.numel(), dtype=DTYPE, device=w.device)
        hm[:, 0] = h1
        zeros = torch.zeros(self.m, dtype=DTYPE, device=w.device)
        return [w1.clone(), w.clone(), hm, torch.zeros_like(hm),
                torch.ones((), dtype=DTYPE, device=w.device),
                zeros.clone(), zeros.clone(), zeros.clone(), h1.square().sum(1)]


def heun(model, s, u, dt, k1=None):
    if k1 is None:
        k1 = model.rhs(s, u)
    pred = [x + dt * k for x, k in zip(s, k1)]
    k2 = model.rhs(pred, u)
    out = [x + 0.5 * dt * (a + b) for x, a, b in zip(s, k1, k2)]
    return out, pred


def error_ratio(a, euler, old, atol, rtol):
    # Maximum block RMS error with a block RMS absolute/relative scale.
    ratios = torch.stack([
        (x - z).square().mean().sqrt() /
        (atol + rtol * torch.maximum(x.square().mean().sqrt(),
                                     y.square().mean().sqrt()))
        for x, z, y in zip(a, euler, old)])
    return scalar(ratios.max())


def control(t, frequency, device, old_only=False):
    if old_only:
        return torch.ones(8, device=device, dtype=DTYPE)
    mean = 0.15 if t < 12 else 0.35
    if frequency:
        phase = (t % 12) * frequency / 12
        burst = 1.0 if phase % 1 < 0.5 else -1.0
    else:
        burst = 0.0
    lam = mean + 0.1 * burst
    return torch.tensor([2 * lam] * 8 + [2 * (1 - lam)] * 8,
                        device=device, dtype=DTYPE)


def observation_times(frequency):
    base = np.linspace(0, 24, 193)
    events = np.linspace(0, 24, 4 * frequency + 1) if frequency else np.array([0, 12, 24])
    return sorted(set(np.round(np.concatenate([base, events]), 12).tolist()))


def integrate(model, initial, xquery, checkpoint_features, frequency, deadline,
              name, output, old_only=False, refine=False):
    max_step = 1 / (128 if refine else 64)
    atol, rtol = (2.5e-9, 2.5e-7) if refine else (1e-8, 1e-6)
    terminal = 80.0 if old_only else 24.0
    times = list(np.linspace(0, terminal, 641)) if old_only else observation_times(frequency)
    events = [0, terminal] if old_only else observation_times(frequency)
    stops = sorted(set(times + events))
    s = [v.clone() for v in initial]
    t, dt, accepts, rejects = 0.0, 1e-3, 0, 0
    save_t, predictions, metrics = [], [], []
    start_wall = time.monotonic()
    last_log = start_wall

    def save():
        h1, h2, f = model.evaluate(s, xquery)
        train_h1, train_h2, train_f = model.evaluate(s)
        row = dict(time=t, mse=scalar((train_f - model.y).square().mean()))
        if checkpoint_features is not None:
            row['feature_motion'] = max(scalar((train_h1 - checkpoint_features[0]).square().mean().sqrt()),
                                        scalar((train_h2 - checkpoint_features[1]).square().mean().sqrt()))
        if model.q:
            dh, db, eb, eh = [v.clamp_min(0) for v in s[5:9]]
            row.update(tau=scalar(s[4]), forward_error=scalar((dh.sum() / eh.sum().clamp_min(1e-300)).sqrt()),
                       backward_error=scalar((db.sum() / eb.sum().clamp_min(1e-300)).sqrt()) if scalar(eb.sum()) > 0 else None,
                       source_bound=scalar(2 / (model.m * initial[1].numel()) * (dh * db).sqrt().sum()))
        save_t.append(t)
        predictions.append(f.detach().cpu().numpy())
        metrics.append(row)

    save()
    fitted = False
    for stop in stops[1:]:
        while t < stop - 2e-12:
            now = time.monotonic()
            if now >= deadline:
                raise TimeoutError(f'Aggregate budget exhausted in {name} at time {t}')
            if now - last_log >= 20:
                print(json.dumps(dict(event='progress', name=name, physical_time=t,
                                      accepted=accepts, elapsed=now-start_wall)), flush=True)
                last_log = now
            h = min(dt, max_step, stop - t)
            # The midpoint is in the current constant-control segment because
            # all switch events are stops. This avoids endpoint roundoff flips.
            u = control(t + h / 2, frequency, model.x.device, old_only)
            k1 = model.rhs(s, u)
            trial, euler = heun(model, s, u, h, k1)
            err = error_ratio(trial, euler, s, atol, rtol)
            if not math.isfinite(err):
                raise FloatingPointError(f'Nonfinite error in {name}')
            if err > 1:
                rejects += 1
                dt = max(h * 0.9 / math.sqrt(err), 1e-12)
                continue
            if old_only:
                mse = scalar((model.evaluate(trial)[2] - model.y).square().mean())
                if mse <= 1e-3:
                    lo, hi = 0.0, h
                    for _ in range(28):
                        mid = (lo + hi) / 2
                        candidate, _ = heun(model, s, u, mid, k1)
                        loss = scalar((model.evaluate(candidate)[2] - model.y).square().mean())
                        if loss <= 1e-3:
                            hi = mid
                        else:
                            lo = mid
                    s, _ = heun(model, s, u, hi, k1)
                    t += hi
                    accepts += 1
                    fitted = True
                    save()
                    break
            s = trial
            t += h
            accepts += 1
            dt = min(max_step, h * min(2.0, 0.9 / math.sqrt(max(err, 1e-12))))
        if fitted:
            break
        t = stop
        save()
    result = dict(name=name, frequency=frequency, q=model.q, refine=refine,
                  elapsed=time.monotonic()-start_wall, accepted=accepts,
                  rejected=rejects, fitted=fitted, metrics=metrics,
                  tolerances=dict(atol=atol, rtol=rtol, max_step=max_step))
    np.savez_compressed(output / f'{name}.npz', time=np.array(save_t),
                        predictions=np.array(predictions))
    (output / f'{name}.json').write_text(json.dumps(result, indent=2))
    torch.save([v.detach().cpu() for v in s], output / f'{name}_terminal.pt')
    print(json.dumps(dict(event='completed', name=name, elapsed=result['elapsed'],
                          accepted=accepts, mse=metrics[-1]['mse'])), flush=True)
    return s, result


def check_rhs():
    generator = torch.Generator().manual_seed(7001)
    x = torch.randn(3, 2, dtype=DTYPE, generator=generator)
    y = torch.randn(3, dtype=DTYPE, generator=generator)
    checkpoint = [torch.randn(5, 2, dtype=DTYPE, generator=generator),
                  torch.randn(5, 5, dtype=DTYPE, generator=generator) / math.sqrt(5),
                  torch.randn(5, dtype=DTYPE, generator=generator)]
    mod = Model(x, y, 3, checkpoint[1])
    s = mod.start(checkpoint)
    s[2] += 0.1 * torch.randn(s[2].shape, dtype=DTYPE, generator=generator)
    s[3] += 0.1 * torch.randn(s[3].shape, dtype=DTYPE, generator=generator)
    s[4] += 0.8
    u = torch.tensor([0.2, 1.4, 0.0], dtype=DTYPE)
    vel = mod.rhs(s, u)
    w1, w, hm, bm, tau = s[:5]
    dhm, dbm, drho = vel[2:5]
    wt = mod.weights.repeat(mod.m)
    hf, bf = hm.reshape(-1, 5), bm.reshape(-1, 5)
    dhf, dbf = dhm.reshape(-1, 5), dbm.reshape(-1, 5)
    update = -2 / (5 * 3 * tau) * (bf.T @ (wt[:, None] * hf))
    w2 = checkpoint[1] + update
    analytic = -2 / (5 * 3 * tau) * (dbf.T @ (wt[:, None] * hf) + bf.T @ (wt[:, None] * dhf)) - update * drho / tau
    h1, h2, f = features(x, w1, w2, w)
    d2 = (1 - h2.square()) * w
    drive = u * (f - y)
    rho = drive.square().mean().sqrt()
    b = drive[:, None] * d2 / rho
    hs = (hm * mod.weights[None, :, None]).sum(1) / tau
    bs = (bm * mod.weights[None, :, None]).sum(1) / tau
    dense_velocity = -2 / 15 * ((drive[:, None] * d2).T @ h1)
    defect = 2 * rho / 15 * ((b - bs).T @ (h1 - hs))
    err = scalar((analytic - dense_velocity - defect).abs().max())
    pause = max(scalar(v.abs().max()) for v in mod.rhs(s, torch.zeros(3, dtype=DTYPE)))
    assert err < 1e-12, err
    assert pause == 0, pause
    return dict(product_defect_max_error=err, zero_drive_max_velocity=pause)


def frozen_kernel(checkpoint, x, xquery):
    w1, w2, w = checkpoint
    n = len(w)
    h1, h2, f = features(x, w1, w2, w)
    q1, q2, fq = features(xquery, w1, w2, w)
    d2 = (1-h2.square()) * w
    d1 = (d2 @ w2) * (1-h1.square())
    e2 = (1-q2.square()) * w
    e1 = (e2 @ w2) * (1-q1.square())
    kxx = h2 @ h2.T/n + (d1 @ d1.T/n) * (x @ x.T/x.shape[1]) + (d2 @ d2.T/n) * (h1 @ h1.T/n)
    kqx = q2 @ h2.T/n + (e1 @ d1.T/n) * (xquery @ x.T/x.shape[1]) + (e2 @ d2.T/n) * (q1 @ h1.T/n)
    return [v.detach().cpu().numpy() for v in (kxx, kqx, f, fq)]


def kernel_run(checkpoint, x, y, xquery, frequency, output):
    from scipy.linalg import expm
    kxx, kqx, f0, fq0 = frozen_kernel(checkpoint, x, xquery)
    residual0 = f0-y.cpu().numpy()
    coeff = np.zeros(x.shape[0])
    times = observation_times(frequency)
    pred = [fq0.copy()]
    for left, right in zip(times, times[1:]):
        u = control((left+right)/2, frequency, 'cpu').numpy()
        mat = np.zeros((len(u)+1, len(u)+1))
        mat[:-1, :-1] = -2/len(u) * u[:, None] * kxx
        mat[:-1, -1] = -2/len(u) * u * residual0
        coeff = (expm((right-left)*mat) @ np.r_[coeff, 1])[:-1]
        pred.append(fq0 + kqx @ coeff)
    np.savez_compressed(output / f'ntk_N{frequency}.npz', time=times,
                        predictions=pred)


def compare(output):
    summary = dict()
    averaged = np.load(output / 'dense_average.npz')
    for frequency in (2, 8, 32):
        dense = np.load(output / f'dense_N{frequency}.npz')
        t, truth = dense['time'], dense['predictions']
        row = dict()
        for label in ('q3', 'q7', 'ntk'):
            path = output / f'{label}_N{frequency}.npz'
            if not path.exists():
                continue
            pred = np.load(path)
            assert np.allclose(pred['time'], t)
            errors = np.sqrt(np.mean((pred['predictions']-truth)**2, axis=1))
            row[label] = dict(max_prediction_rms=float(errors.max()),
                              terminal_prediction_rms=float(errors[-1]))
            jp = output / f'{label}_N{frequency}.json'
            if jp.exists():
                metrics = json.loads(jp.read_text())['metrics']
                row[label]['max_feature_motion'] = max(v.get('feature_motion', 0) for v in metrics)
                row[label]['terminal_backward_error'] = metrics[-1].get('backward_error')
                row[label]['max_backward_error'] = max(v.get('backward_error') or 0 for v in metrics)
                row[label]['terminal_forward_error'] = metrics[-1].get('forward_error')
                row[label]['terminal_source_bound'] = metrics[-1].get('source_bound')
        avg_pred = np.stack([np.interp(t, averaged['time'], averaged['predictions'][:, j])
                             for j in range(truth.shape[1])], axis=1)
        row['averaged_control'] = dict(max_prediction_rms=float(np.sqrt(np.mean((avg_pred-truth)**2, axis=1)).max()))
        summary[str(frequency)] = row
    (output / 'comparison.json').write_text(json.dumps(summary, indent=2))
    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--device', default='cpu')
    p.add_argument('--output', type=pathlib.Path, required=True)
    p.add_argument('--check-only', action='store_true')
    args = p.parse_args()
    checks = check_rhs()
    print(json.dumps(dict(event='algebra_checks', **checks)), flush=True)
    if args.check_only:
        return
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    deadline = started + 20*60
    config = dict(seed=20261002, n=512, m=16, d=3, L=2,
                  device=args.device, torch=torch.__version__,
                  source_sha256=source_sha(__file__),
                  candidate_sha256=source_sha(pathlib.Path(__file__).with_name('CONTROL_CANDIDATE.md')),
                  max_fits=12, gpu_seconds=1200, rhs_checks=checks)
    (args.output / 'config.json').write_text(json.dumps(config, indent=2))
    torch.set_num_threads(1)
    generator = torch.Generator(device='cpu').manual_seed(20261002)
    old_angles = -math.pi/2+(np.arange(8)+0.5)*math.pi/16
    new_angles = (np.arange(8)+0.5)*math.pi/16
    angles = np.r_[old_angles, new_angles]
    def to_x(a):
        return torch.tensor(np.stack([math.sqrt(2)*np.cos(a), math.sqrt(2)*np.sin(a), np.ones_like(a)], axis=1), dtype=DTYPE, device=args.device)
    x = to_x(angles)
    y = torch.tensor(np.sin(2*angles)+0.4*np.cos(3*angles), dtype=DTYPE, device=args.device)
    queries = np.r_[-math.pi/2+(np.arange(256)+0.5)*math.pi/512,
                    (np.arange(256)+0.5)*math.pi/512]
    xquery = to_x(queries)
    checkpoint = [torch.randn(512, 3, dtype=DTYPE, generator=generator).to(args.device),
                  (torch.randn(512, 512, dtype=DTYPE, generator=generator)/math.sqrt(512)).to(args.device),
                  torch.zeros(512, dtype=DTYPE, device=args.device)]
    fit_count = 0
    status = dict(completed=False, fit_count=0)
    try:
        pretrain = Model(x[:8], y[:8])
        fit_count += 1
        checkpoint, pre = integrate(pretrain, checkpoint, xquery, None, 0,
                                    deadline, 'old_pretrain', args.output, old_only=True)
        if not pre['fitted']:
            status['failure'] = 'Old-task fit gate failed at t=80; no further trajectories.'
            return
        checkpoint_features = features(x, *checkpoint)[:2]
        for frequency in (2, 8, 32):
            for q in (0, 3, 7):
                model = Model(x, y, q, checkpoint[1] if q else None)
                name = f'{"dense" if not q else "q"+str(q)}_N{frequency}'
                fit_count += 1
                integrate(model, model.start(checkpoint), xquery, checkpoint_features,
                          frequency, deadline, name, args.output)
            kernel_run(checkpoint, x, y, xquery, frequency, args.output)
        model = Model(x, y)
        fit_count += 1
        integrate(model, model.start(checkpoint), xquery, checkpoint_features,
                  0, deadline, 'dense_average', args.output)
        summary = compare(args.output)
        chosen = max(((summary[str(n)][f'q{q}']['max_prediction_rms'], n, q)
                      for n in (2, 8, 32) for q in (3, 7)))
        _, frequency, q = chosen
        model = Model(x, y, q, checkpoint[1])
        fit_count += 1
        integrate(model, model.start(checkpoint), xquery, checkpoint_features,
                  frequency, deadline, f'q{q}_N{frequency}_refined', args.output, refine=True)
        coarse = np.load(args.output / f'q{q}_N{frequency}.npz')['predictions']
        fine = np.load(args.output / f'q{q}_N{frequency}_refined.npz')['predictions']
        status['numerical_sensitivity'] = dict(q=q, frequency=frequency,
            max_prediction_rms=float(np.sqrt(np.mean((coarse-fine)**2, axis=1)).max()))
        status['completed'] = True
    except Exception as exc:
        status['failure'] = f'{type(exc).__name__}: {exc}'
        raise
    finally:
        status.update(fit_count=fit_count, elapsed=time.monotonic()-started)
        (args.output / 'status.json').write_text(json.dumps(status, indent=2))
        print(json.dumps(dict(event='terminal', **status)), flush=True)


if __name__ == '__main__':
    main()
