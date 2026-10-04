#!/usr/bin/env python3
"""Study-owned, reproducible delayed-training-credit significance screen."""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys
import time
import urllib.request

import numpy as np
import torch
from torch.utils.checkpoint import checkpoint

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parent.parent
OUT = ROOT / 'data/generated/response_memory_delayed_training_credit_20261002'
DTYPE = torch.float64


def save_json(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare_data():
    OUT.mkdir(parents=True, exist_ok=True)
    archives = []
    for name in ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz']:
        path = OUT / name
        if not path.exists():
            urllib.request.urlretrieve(
                'https://storage.googleapis.com/cvdf-datasets/mnist/' + name,
                path)
        archives.append({'name': name, 'sha256': sha(path)})
    with gzip.open(OUT / 'train-images-idx3-ubyte.gz', 'rb') as f:
        magic, count, rows, cols = struct.unpack('>IIII', f.read(16))
        assert (magic, rows, cols) == (2051, 28, 28)
        images = np.frombuffer(f.read(), dtype=np.uint8).reshape(count, 28, 28)
    with gzip.open(OUT / 'train-labels-idx1-ubyte.gz', 'rb') as f:
        magic, count2 = struct.unpack('>II', f.read(8))
        assert magic == 2049 and count == count2
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    rng = np.random.default_rng(20261002)
    pools = {k: rng.permutation(np.flatnonzero(labels == k)) for k in [3, 8]}
    result, offsets = {}, {3: 0, 8: 0}
    for split, size in [('train', 128), ('val', 512), ('test', 2048)]:
        ids = np.concatenate([pools[k][offsets[k]:offsets[k] + size // 2]
                              for k in [3, 8]])
        for k in [3, 8]:
            offsets[k] += size // 2
        y = np.where(labels[ids] == 3, -1., 1.)
        source = np.ones(size)
        strips = np.empty(size)
        for k in [-1., 1.]:
            positions = np.flatnonzero(y == k)
            if split == 'train':
                a, b = positions[:32], positions[32:]
                source[b] = -1
                strips[a] = rng.permutation(np.tile([-1., 1.], 16))
                strips[b] = k
            else:
                strips[positions] = rng.permutation(
                    np.tile([-1., 1.], len(positions) // 2))
        gray = images[ids].astype(np.float64).reshape(size, 14, 2, 14, 2)
        gray = gray.mean(axis=(2, 4)) / 127.5 - 1
        strip = np.broadcast_to(strips[:, None, None], (size, 14, 2))
        x = np.concatenate([gray, strip], axis=2).reshape(size, 224).copy()
        result.update({split + '_x': x, split + '_y': y,
                       split + '_ids': ids, split + '_strip': strips,
                       split + '_source': source})
    assert len(np.unique(np.concatenate([result[s + '_ids']
                                        for s in ['train', 'val', 'test']]))) == 2688
    np.savez_compressed(OUT / 'dataset.npz', **result)
    save_json('dataset_provenance.json', {'archives': archives, 'split_seed': 20261002,
                                        'dataset_sha256': sha(OUT / 'dataset.npz')})
    return result


class Dense:
    def __init__(self, n, data, device='cuda:0', seed=0):
        self.n, self.d, self.m = n, 224, 128
        self.x = torch.as_tensor(data['train_x'], dtype=DTYPE, device=device)
        self.y = torch.as_tensor(data['train_y'], dtype=DTYPE, device=device)
        self.source = torch.as_tensor(data['train_source'], dtype=DTYPE, device=device)
        self.eval_data = {s: (torch.as_tensor(data[s + '_x'], dtype=DTYPE, device=device),
                              torch.as_tensor(data[s + '_y'], dtype=DTYPE, device=device))
                          for s in ['val', 'test']}
        gen = torch.Generator(device='cpu').manual_seed(seed)
        a = torch.randn(n, self.d, generator=gen, dtype=DTYPE).to(device)
        b = torch.randn(n, n, generator=gen, dtype=DTYPE).to(device) / math.sqrt(n)
        w = torch.zeros(n, dtype=DTYPE, device=device)
        self.initial = (a, b, w)
        self.h0, self.g0, _ = self.forward(self.initial, self.x)

    def forward(self, state, x):
        a, b, w = state
        h = torch.tanh(x @ a.T / math.sqrt(self.d))
        g = torch.tanh(h @ b.T)
        return h, g, g @ w / self.n

    def rhs(self, state, u, t):
        a, b, w = state
        h, g, f = self.forward(state, self.x)
        window = min(int(t / 5), 15)
        phase = (t - 5 * window) / 5
        contrast = u[window % 8] * math.sin(math.pi * phase)**2
        if window >= 8:
            contrast = -contrast
        r = (f - self.y) * (1 + self.source * contrast)
        delta = (1 - g.square()) * w
        ell = (1 - h.square()) * (delta @ b)
        da = -2 / self.m * ((r[:, None] * ell).T @ self.x) / math.sqrt(self.d)
        db = -2 / (self.m * self.n) * ((r[:, None] * delta).T @ h)
        dw = -2 / self.m * (r @ g)
        return da, db, dw

    def chunk(self, state, u, start, steps, dt):
        for k in range(start, start + steps):
            rhs = self.rhs(state, u, k * dt)
            trial = tuple(x + dt * dx for x, dx in zip(state, rhs))
            rhs2 = self.rhs(trial, u, (k + 1) * dt)
            state = tuple(x + (dt / 2) * (v + w)
                          for x, v, w in zip(state, rhs, rhs2))
        return state

    def run(self, u, dt=.05, horizon=80., differentiate=False):
        state = tuple(x.clone() for x in self.initial)
        count = round(horizon / dt)
        assert abs(count * dt - horizon) < 1e-10
        for start in range(0, count, 20):
            steps = min(20, count - start)
            if differentiate:
                def fn(a, b, w, controls, start=start, steps=steps):
                    return self.chunk((a, b, w), controls, start, steps, dt)
                state = checkpoint(fn, *state, u, use_reentrant=False,
                                   preserve_rng_state=False)
            else:
                state = self.chunk(state, u, start, steps, dt)
        return state

    def metrics(self, state):
        with torch.no_grad():
            h, g, f = self.forward(state, self.x)
            result = {'train_mse': (f - self.y).square().mean().item(),
                      'h_rms_movement': (h - self.h0).square().mean().sqrt().item(),
                      'g_rms_movement': (g - self.g0).square().mean().sqrt().item()}
            predictions = {'train': f.cpu().numpy()}
            for name, (x, y) in self.eval_data.items():
                _, _, p = self.forward(state, x)
                result[name + '_mse'] = (p - y).square().mean().item()
                result[name + '_accuracy'] = ((p >= 0) == (y >= 0)).double().mean().item()
                predictions[name] = p.cpu().numpy()
        return result, predictions

    def gradient(self, dt=.05, horizon=80.):
        torch.cuda.reset_peak_memory_stats()
        start = time.monotonic()
        u = torch.zeros(8, dtype=DTYPE, device=self.x.device, requires_grad=True)
        state = self.run(u, dt=dt, horizon=horizon, differentiate=True)
        xv, yv = self.eval_data['val']
        objective = (self.forward(state, xv)[2] - yv).square().mean()
        grad, = torch.autograd.grad(objective, u)
        torch.cuda.synchronize()
        result, predictions = self.metrics(state)
        result.update({'gradient': grad.detach().cpu().tolist(),
                       'elapsed_seconds': time.monotonic() - start,
                       'peak_allocated_bytes': torch.cuda.max_memory_allocated(),
                       'width': self.n, 'dt': dt, 'horizon': horizon})
        return result, predictions

    def evaluate(self, controls, dt=.05):
        start = time.monotonic()
        with torch.no_grad():
            u = torch.as_tensor(controls, dtype=DTYPE, device=self.x.device)
            state = self.run(u, dt=dt)
            torch.cuda.synchronize()
            result, predictions = self.metrics(state)
        result.update({'controls': list(controls), 'elapsed_seconds': time.monotonic() - start,
                       'dt': dt})
        return result, predictions


def announce(label, result):
    print(json.dumps({'event': label, 'result': result}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-only', action='store_true')
    parser.add_argument('--audit', action='store_true')
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    data = (dict(np.load(OUT / 'dataset.npz')) if (OUT / 'dataset.npz').exists()
            else prepare_data())
    if args.data_only:
        announce('data_ready', {'sha256': sha(OUT / 'dataset.npz')})
        return
    assert torch.cuda.is_available()
    torch.set_num_threads(2)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    save_json('environment.json', {'python': sys.version, 'torch': torch.__version__,
                                  'numpy': np.__version__, 'cuda': torch.version.cuda,
                                  'gpu': torch.cuda.get_device_name(), 'dtype': str(DTYPE),
                                  'producer_sha256': sha(Path(__file__)),
                                  'protocol_sha256': sha(STUDY / 'PROTOCOL.md'),
                                  'command': sys.argv, 'seed': 0,
                                  'CUDA_VISIBLE_DEVICES': os.environ.get('CUDA_VISIBLE_DEVICES')})
    target = Dense(512, data)
    if args.audit:
        reference = json.loads((OUT / 'first_discriminator.json').read_text())
        fine, pred = target.gradient(dt=.025)
        np.savez_compressed(OUT / 'fine_predictions.npz', **pred)
        g0 = np.array(reference['dense']['gradient'])
        fine['relative_gradient_change'] = float(np.linalg.norm(np.array(fine['gradient']) - g0)
                                                  / np.linalg.norm(g0))
        baseline = np.load(OUT / 'dense_predictions.npz')['val']
        fine['val_prediction_rms_change'] = float(np.sqrt(np.mean((pred['val'] - baseline)**2)))
        save_json('fine_audit.json', fine)
        announce('fine_audit', fine)
        return
    results = {}
    results['dense'], pred = target.gradient()
    np.savez_compressed(OUT / 'dense_predictions.npz', **pred)
    save_json('dense_gradient.json', results['dense'])
    announce('dense_gradient', results['dense'])
    direction = np.ones(8) / np.sqrt(8)
    eps = .001
    plus, _ = target.evaluate(eps * direction)
    minus, _ = target.evaluate(-eps * direction)
    analytic = float(np.array(results['dense']['gradient']) @ direction)
    finite = (plus['val_mse'] - minus['val_mse']) / (2 * eps)
    results['directional_check'] = {'epsilon': eps, 'analytic': analytic,
                                    'finite_difference': finite,
                                    'relative_error': abs(analytic - finite) / max(abs(analytic), abs(finite), 1e-14),
                                    'plus': plus, 'minus': minus}
    save_json('directional_check.json', results['directional_check'])
    announce('directional_check', results['directional_check'])
    proxy = Dense(128, data)
    results['proxy'], pred = proxy.gradient()
    np.savez_compressed(OUT / 'proxy_predictions.npz', **pred)
    save_json('proxy_gradient.json', results['proxy'])
    announce('proxy_gradient', results['proxy'])
    for method in ['dense', 'proxy']:
        g = np.array(results[method]['gradient'])
        controls = -.25 * g / np.max(np.abs(g))
        result, pred = target.evaluate(controls)
        results[method + '_intervention'] = result
        np.savez_compressed(OUT / (method + '_intervention_predictions.npz'), **pred)
        save_json(method + '_intervention.json', result)
        announce(method + '_intervention', result)
    baseline = results['dense']['test_mse']
    dense_gain = baseline - results['dense_intervention']['test_mse']
    proxy_gain = baseline - results['proxy_intervention']['test_mse']
    results['decision'] = {'baseline_test_mse': baseline,
                           'exact_relative_test_gain': dense_gain / baseline,
                           'proxy_relative_test_gain': proxy_gain / baseline,
                           'proxy_recovery': proxy_gain / dense_gain if dense_gain != 0 else None,
                           'numerical_basic_pass': results['directional_check']['relative_error'] <= .02,
                           'physical_gates_pass': results['dense']['train_mse'] < .02
                             and results['dense']['h_rms_movement'] > .1
                             and results['dense']['g_rms_movement'] > .1,
                           'significance_distinction': dense_gain / baseline >= .05
                             and proxy_gain <= .5 * dense_gain}
    save_json('first_discriminator.json', results)
    announce('FIRST_DISCRIMINATOR', results['decision'])


if __name__ == '__main__':
    main()
