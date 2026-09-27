#!/usr/bin/env python3
"""Capture genuine shared-time circle predictions for the paper's Figure 3.

This replays the original float64 adaptive-Heun dense/lifted-Legendre models.
The two closure modules are loaded from the study's preserved, hash-checked
legacy ZIP, without changing or importing other studies. Training/query data
come from the portable paper bundle. All output goes to a fresh --out folder;
publication of its checked response_memory_source.npz is a separate step.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import types
import zipfile

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
LEGACY = ROOT / "studies/neural_response_memory_20260922/legacy_experiments.zip"
HASHES = {
    "moment_engine.py": "ebf39cf377f1eb0f5dea64fa1ab946fddcb11a662b2368472017abef9237acd9",
    "orthogonal_moment_engine.py": "32f80cf35c44b5015821fa8c8726bb8ff3bc6f7eb3e1b7abe9ee62ea8f529909",
}
INITIAL_HASHES = {
    "w": "da24d2b86aed45dfa6e7442e24bfcb968ec28fcfbcfb2f5f07ac066601fffd63",
    "c": "460ee22d13695cbe3226805bf5b24b124100e32be5717737508c79d8679b0db6",
    "M": "559c9ad62fd9feab4fb4671e854b86ec975240a12aa8792873824ebe2344b3f9",
}


def sha(value):
    return hashlib.sha256(value).hexdigest()


def array_sha(value):
    return sha(np.ascontiguousarray(value).tobytes())


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def load_legacy(out):
    with zipfile.ZipFile(LEGACY) as archive:
        for name, expected in HASHES.items():
            source = archive.read(name)
            if sha(source) != expected:
                raise RuntimeError(f"Archived solver hash mismatch: {name}")
            if out is not None:
                (out / name).write_bytes(source)
            module = types.ModuleType(name[:-3])
            module.__file__ = str(LEGACY) + "/" + name
            sys.modules[module.__name__] = module
            exec(compile(source, module.__file__, "exec"), module.__dict__)
    return sys.modules["moment_engine"], sys.modules["orthogonal_moment_engine"]


def rms(x):
    return x.square().mean().sqrt()


def dense_fields(state, inputs):
    w, c, matrix = state
    h1 = (w @ inputs.T).tanh()
    h2 = (matrix @ h1).tanh()
    return h1, h2, c @ h2 / len(c)


def dense_rhs(state, inputs, labels):
    w, c, matrix = state
    h1, h2, f = dense_fields(state, inputs)
    residual = f - labels
    delta2 = c[:, None] * (1 - h2.square())
    delta1 = (matrix.T @ delta2) * (1 - h1.square())
    return [(-2 / len(labels)) * (delta1 * residual) @ inputs,
            (-2 / len(labels)) * (h2 @ residual),
            (-2 / (len(c) * len(labels))) * (delta2 * residual) @ h1.T]


def small_checks(base, orthogonal):
    """Independent loss-gradient and reconstructed-matrix checks."""
    rng = np.random.default_rng(712)
    inputs = torch.tensor(rng.normal(size=(3, 2)))
    labels = torch.tensor(rng.normal(size=3))
    engine = orthogonal.MomentEngine(2, 9, 3, inputs, labels, lifted=True)
    state = engine.initial_state()
    state.A += torch.tensor(rng.normal(scale=.03, size=tuple(state.A.shape)))
    state.B += torch.tensor(rng.normal(scale=.03, size=tuple(state.B.shape)))
    left, right = engine.delta_factors(state)
    matrix = engine.W0 + left @ right.T
    state.h1 = (state.w @ inputs.T).tanh()
    state.h2 = (matrix @ state.h1).tanh()
    state.rho = rms(state.c @ state.h2 / engine.n - labels)
    dense = [v.detach().clone().requires_grad_() for v in (state.w, state.c, matrix)]
    loss = (dense_fields(dense, inputs)[2] - labels).square().mean()
    gradients = torch.autograd.grad(loss, dense)
    oracle = [-mobility * g for mobility, g in zip((9, 9, 1), gradients)]
    actual = dense_rhs(dense, inputs, labels)
    maximum = max(float((x-y).abs().max()) for x, y in zip(oracle, actual))
    velocity = engine.rhs(state)
    maximum = max(maximum, float((velocity.w-actual[0]).abs().max()),
                  float((velocity.c-actual[1]).abs().max()))
    dl, dr = engine._derivative_factors(state, velocity)
    dh1 = (1-state.h1.square()) * (velocity.w @ inputs.T)
    dh2 = (1-state.h2.square()) * (matrix @ dh1 + (dl @ dr.T) @ state.h1)
    maximum = max(maximum, float((dh1-velocity.h1).abs().max()),
                  float((dh2-velocity.h2).abs().max()))
    assert maximum < 1e-12, maximum
    prediction = engine.predict(state, inputs)
    assert torch.allclose(prediction, dense_fields(dense, inputs)[2], atol=1e-14, rtol=1e-14)
    return {"independent_gradient_and_matrix_max_abs": maximum}


@torch.no_grad()
def capture(order, level, arrays, schedule, args, base, orthogonal):
    started = time.monotonic()
    name = f"{'dense' if order == 0 else 'memory_' + str(order)}_level{level}"
    inputs = torch.tensor(arrays["train_inputs"], device=args.device)
    labels = torch.tensor(arrays["train_labels"], device=args.device)
    angles = arrays["history_angles"]
    queries = torch.tensor(np.column_stack((np.cos(angles), np.sin(angles))), device=args.device)
    engine = orthogonal.MomentEngine(2, 2048, max(1, order), inputs, labels,
                                    device=args.device, lifted=True)
    state = engine.initial_state()
    for key, value in (("w", state.w), ("c", state.c), ("M", engine.W0)):
        assert array_sha(value.cpu().numpy()) == INITIAL_HASHES[key], key
    initial_matrix = engine.W0
    if order == 0:
        state = [state.w, state.c, initial_matrix.clone()]
    rtol, atol = 6.25e-5 / 4**level, 6.25e-7 / 4**level

    def predict(s):
        chunks = []
        for q in queries.split(256 if order == 0 else 512):
            pred = dense_fields(s, q)[2] if order == 0 else engine.predict(s, q)
            chunks.append(pred.cpu().numpy())
        return np.concatenate(chunks)

    def loss(s):
        pred = (dense_fields(s, inputs)[2] if order == 0 else s.c @ s.h2 / 2048)
        return float((pred-labels).square().mean())

    def trial(s, step):
        if order == 0:
            first = dense_rhs(s, inputs, labels)
            euler = [v+step*f for v, f in zip(s, first)]
            second = dense_rhs(euler, inputs, labels)
            candidate = [v+.5*step*(f+g) for v, f, g in zip(s, first, second)]
            ratios = [rms(c-b)/(atol+rtol*torch.maximum(rms(a), rms(c)))
                      for a, b, c in zip(s[:2], euler[:2], candidate[:2])]
            scale = torch.maximum((s[2]-initial_matrix).norm(),
                                  (candidate[2]-initial_matrix).norm()).clamp_min(1.)
            ratios.append((candidate[2]-euler[2]).norm()/(atol+rtol*scale))
        else:
            first = engine.rhs(s)
            euler = s.add_scaled(first, step)
            second = engine.rhs(euler)
            candidate = base.linear_combination((1., step/2, step/2), (s, first, second))
            ratios = [rms(c-b)/(atol+rtol*torch.maximum(rms(a), rms(c)).clamp_min(1.))
                      for a, b, c in zip(s.tensors(), euler.tensors(), candidate.tensors())]
            lc, rc = engine.delta_factors(candidate)
            le, re = engine.delta_factors(euler)
            l0, r0 = engine.delta_factors(s)
            numerator = base.factor_frobenius(torch.cat((lc-le, le), 1), torch.cat((rc, rc-re), 1))
            scale = torch.maximum(base.factor_frobenius(l0, r0), base.factor_frobenius(lc, rc)).clamp_min(1.)
            ratios.append(numerator/(atol+rtol*scale))
        return candidate, float(torch.stack(ratios).max())

    t, step, accepted, rejected = 0., .05, 0, 0
    observed, predictions, losses, physical_losses, drift = [0.], [predict(state)], [loss(state)], [], []
    current_loss = losses[0]
    last_report = time.monotonic()
    for target in schedule[1:]:
        while t < target - 1e-12:
            if time.monotonic()-started > args.per_run_seconds or accepted+rejected >= 30000:
                np.savez_compressed(args.out/(name+"_partial.npz"), times=observed, predictions=predictions)
                raise RuntimeError(f"Resource cap in {name} at t={t}; partial data retained")
            h = min(step, 2., float(target)-t)
            if h < 1e-9:
                raise RuntimeError(f"Step underflow in {name}")
            candidate, error = trial(state, h)
            next_loss = loss(candidate)
            finite = math.isfinite(error) and math.isfinite(next_loss)
            decreasing = order != 0 or next_loss <= current_loss*(1+1e-8)+1e-12
            if not finite or error > 1 or not decreasing:
                rejected += 1
                step = h*(max(.1, min(.5, .9/math.sqrt(max(error, 1e-16)))) if finite else .1)
                continue
            state, current_loss = candidate, next_loss
            t = float(target) if abs(t+h-target) < 1e-12 else t+h
            accepted += 1
            step = h*max(.5, min(2., .9/math.sqrt(max(error, 1e-16))))
            if time.monotonic()-last_report > 20:
                print(json.dumps(dict(event="progress", model=name, t=t, steps=accepted)), flush=True)
                last_report = time.monotonic()
        observed.append(float(target))
        predictions.append(predict(state))
        losses.append(current_loss)
        if order:
            physical_losses.append(float((engine.predict(state, inputs)-labels).square().mean()))
            diag = engine.lift_diagnostics(state)
            drift.append({k:float(v) for k,v in diag.items()})
    observed, predictions = np.asarray(observed), np.asarray(predictions)
    assert np.array_equal(observed, schedule)
    assert predictions.shape == (len(schedule), 2048) and np.isfinite(predictions).all()
    result = dict(model=name, order=order, level=level, rtol=rtol, atol=atol,
                  accepted=accepted, rejected=rejected, last_time=t, final_loss=current_loss,
                  seconds=time.monotonic()-started, prediction_sha256=array_sha(predictions),
                  max_activation_drift=max((max(d['h1_max'], d['h2_max']) for d in drift), default=0.))
    np.savez_compressed(args.out/(name+".npz"), times=observed, predictions=predictions,
                        losses=losses, physical_losses=physical_losses)
    save_json(args.out/(name+".json"), result)
    print(json.dumps(dict(event="complete", **result)), flush=True)
    return predictions, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', type=Path, default=HERE/'response_memory_source.npz')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', default='cuda:1')
    parser.add_argument('--per-run-seconds', type=float, default=300.)
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    base, orthogonal = load_legacy(args.out)
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    checks = small_checks(base, orthogonal)
    save_json(args.out/'operator_checks.json', checks)
    if args.check_only:
        print(json.dumps(checks)); return
    if not args.device.startswith('cuda') or not torch.cuda.is_available():
        raise RuntimeError('Full capture requires an explicitly available CUDA device')
    with np.load(args.bundle, allow_pickle=False) as source:
        arrays = {k:source[k].copy() for k in source.files if k != 'metadata_json'}
        meta = json.loads(str(source['metadata_json']))
    schedule = np.unique(np.concatenate(([0.], np.geomspace(.5, 80., 32), [1., 2., 5., 10., 20., 40., 80.])))
    assert len(schedule) == 39 and schedule[-1] == 80.
    report = dict(protocol='One fixed task, four models, two resolutions; no tuning or endpoint stopping',
                  task='quadrant_pairs', width=2048, hidden_layers=2, activation='tanh',
                  seed=20260920, dtype='float64', query_count=2048, common_times=schedule.tolist(),
                  solver='adaptive explicit Heun, original per-model error controllers and lifted closure',
                  sensitivity='RMS(dense coarse-fine) + RMS(closure coarse-fine); not an error certificate',
                  archive_replay_gate='At old checkpoints, each model RMS change <= 5e-6 + 2 times old combined sensitivity',
                  per_model_seconds=args.per_run_seconds, maximum_model_runs=8,
                  python=platform.python_version(), numpy=np.__version__, torch=torch.__version__,
                  device=args.device, gpu=torch.cuda.get_device_name(args.device),
                  git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                  command=sys.argv, base_bundle_sha256=sha(args.bundle.read_bytes()),
                  capture_source_sha256=sha(Path(__file__).read_bytes()), legacy_sources=HASHES,
                  initialization_hashes=INITIAL_HASHES, operator_checks=checks,
                  train_inputs_sha256=array_sha(arrays['train_inputs']),
                  train_labels_sha256=array_sha(arrays['train_labels']),
                  history_angles_sha256=array_sha(arrays['history_angles']))
    save_json(args.out/'protocol.json', report)
    results, runs = {}, []
    for order in (0, 1, 3, 7):
        for level in ((1, 2) if order == 0 else (0, 1)):
            results[order, level], row = capture(order, level, arrays, schedule, args, base, orthogonal)
            runs.append(row)
    old_times = arrays['common_times'].copy()
    indices = np.array([np.flatnonzero(schedule == t)[0] for t in old_times])
    replay = {}
    for order in (0, 1, 3, 7):
        key = 'common_dense' if order == 0 else f'common_memory_{order}'
        fine = results[order, 2 if order == 0 else 1]
        change = np.sqrt(np.mean((fine[indices]-arrays[key])**2, axis=1))
        sensitivity = (np.maximum.reduce([arrays[f'common_sensitivity_{p}'] for p in (1,3,7)])
                       if order == 0 else arrays[f'common_sensitivity_{order}'])
        gate = 5e-6 + 2*sensitivity
        replay[key] = dict(times=old_times.tolist(), rms_change=change.tolist(),
                           allowed_change=gate.tolist(), passed=bool(np.all(change <= gate)))
    report.update(runs=runs, archive_replay=replay, complete=True)
    save_json(args.out/'report.json', report)
    if not all(x['passed'] for x in replay.values()):
        raise RuntimeError('Archive replay gate failed; capture retained but bundle not published')
    arrays['common_times'] = schedule
    arrays['common_dense'], arrays['common_dense_coarse'] = results[0,2], results[0,1]
    dense_sensitivity = np.sqrt(np.mean((results[0,2]-results[0,1])**2, axis=1))
    for p in (1,3,7):
        fine, coarse = results[p,1], results[p,0]
        arrays[f'common_memory_{p}'], arrays[f'common_memory_{p}_coarse'] = fine, coarse
        arrays[f'common_rms_{p}'] = np.sqrt(np.mean((fine-results[0,2])**2, axis=1))
        arrays[f'common_sensitivity_{p}'] = dense_sensitivity + np.sqrt(np.mean((fine-coarse)**2, axis=1))
    meta['trajectory_previous'] = meta['trajectory']
    meta['trajectory'] = dict(case='quadrant_pairs', width=2048, hidden_layers=2, query_count=2048,
                             common_times=schedule.tolist(), displayed_times=[0,5,20,80],
                             metric='RMS versus freshly replayed fine dense reference at identical physical times',
                             sensitivity=report['sensitivity'],
                             note='New genuine checkpoints; no interpolated predictions. Endpoint figures unchanged.')
    meta['trajectory_capture'] = report
    np.savez_compressed(args.out/'response_memory_source.npz', **arrays,
                        metadata_json=np.array(json.dumps(meta, allow_nan=False)))
    print(json.dumps(dict(event='checked_bundle', checkpoints=len(schedule), out=str(args.out))), flush=True)


if __name__ == '__main__':
    main()
