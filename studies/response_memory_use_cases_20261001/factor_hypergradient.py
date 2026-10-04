"""Precommitted rank-eight feature-learning label-design control."""
import argparse
import hashlib
import json
import math
import os
import platform
import shutil
import sys
import time
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
import torch
from baseline_compact_flow import LowRankFlow
from hypergradient import FunctionalFlow, circle, plain, utc, write

HERE = Path(__file__).resolve().parent
SOURCES = ['factor_hypergradient.py', 'hypergradient.py',
           'baseline_compact_flow.py', 'FACTOR_HYPERGRADIENT_PROTOCOL.md',
           'HYPERGRADIENT_PROTOCOL.md']
torch.set_num_threads(1)
torch.backends.cuda.matmul.allow_tf32 = False
torch.backends.cudnn.allow_tf32 = False


class FunctionalLowRank(FunctionalFlow):
    """Exact LowRankFlow at depth two/tanh, with optional factor mobility."""
    def __init__(self, x, width, seed, factor_mobility=1., rank=8,
                 factor_seed=20260924):
        super().__init__(x, width, seed, 'dense')
        self.rank = rank
        self.factor_mobility = factor_mobility
        self.A0 = x.new_zeros((width, rank))
        rng = np.random.default_rng(factor_seed)
        self.B0 = x.new_tensor(rng.standard_normal((rank, width))/math.sqrt(rank))

    def initial(self):
        return self.w0, self.c0, self.A0, self.B0

    def apply(self, h, state, transpose=False, factors=None):
        _, _, A, B = state
        if transpose:
            return self.W0.T@h+B.T@(A.T@h)
        return self.W0@h+A@(B@h)

    def fields(self, state, x=None):
        x = self.x if x is None else x
        w, c, _, _ = state
        h1 = torch.tanh(w@x.T)
        h2 = torch.tanh(self.apply(h1, state))
        return h1, h2, c@h2/self.n

    def rhs(self, state, y):
        _, c, A, B = state
        h1, h2, f = self.fields(state)
        r = f-y
        delta2 = (1-h2.square())*c[:, None]
        delta1 = (1-h1.square())*self.apply(delta2, state, True)
        scale = -2*self.factor_mobility/(self.m*self.n)
        return ((-2/self.m)*(delta1*r)@self.x,
                (-2/self.m)*(h2@r),
                scale*(delta2*r)@(B@h1).T,
                scale*(A.T@(delta2*r))@h1.T)


def provenance(args, out):
    for source in SOURCES:
        shutil.copyfile(HERE/source, out/source)
    return dict(start_utc=utc(), argv=sys.argv, config=vars(args),
                sources={s: hashlib.sha256((HERE/s).read_bytes()).hexdigest()
                         for s in SOURCES}, python=sys.version,
                numpy=np.__version__, torch=torch.__version__,
                platform=platform.platform(), cpu_threads=torch.get_num_threads(),
                tf32=False, device=args.device,
                gpu=torch.cuda.get_device_name(args.device)
                    if args.device.startswith('cuda') else None)


def check(args, out):
    if args.device != 'cpu':
        raise ValueError('Validation is precommitted to CPU')
    result = provenance(args, out)
    x, y = circle(8, .13, 'cpu', torch.float64)
    query, target = circle(32, .37, 'cpu', torch.float64)
    functional = FunctionalLowRank(x, 32, 201)
    source = LowRankFlow(x, y, width=32, depth=2, activation='tanh',
                         rank=8, factor_seed=20260924, seed=201, device='cpu',
                         dtype=torch.float64, hidden_gain=1., readout_std=1.)
    source.c.zero_()
    state = functional.initial()
    rows = []
    for step in range(32):
        with torch.no_grad():
            state = tuple(s+ds/32 for s, ds in zip(state, functional.rhs(state, y)))
            source.step(1/32)
        if step in (0, 31):
            errors = [float((a-b).abs().max()) for a, b in zip(state, source.state)]
            pred_error = float((functional.predict(state, query)-source.predict(query)).abs().max())
            rows.append(dict(steps=step+1, state_errors=errors,
                             prediction_error=pred_error))
            assert max(errors+[pred_error]) <= 1e-10, rows[-1]
    result['source_parity'] = rows
    velocities = []
    # Nonzero, nonsymmetric A and c expose all update paths independently.
    generator = torch.Generator().manual_seed(109)
    for mobility in (.25, 1., 4.):
        model = FunctionalLowRank(x, 32, 201, mobility)
        p = [v.detach().clone().requires_grad_() for v in model.initial()]
        with torch.no_grad():
            p[1].add_(torch.randn(p[1].shape, generator=generator, dtype=p[1].dtype)*.2)
            p[2].add_(torch.randn(p[2].shape, generator=generator, dtype=p[2].dtype)*.03)
        w, c, A, B = p
        h1 = torch.tanh(w@x.T)
        h2 = torch.tanh((model.W0+A@B)@h1)
        pred = c@h2/model.n
        gradients = torch.autograd.grad((pred-y).square().mean(), p)
        actual = model.rhs(tuple(p), y)
        errors = [float((a+mu*g).abs().max())
                  for a, mu, g in zip(actual, (model.n, model.n, mobility, mobility), gradients)]
        assert max(errors) <= 1e-10, errors
        velocities.append(dict(factor_mobility=mobility, errors=errors))
    result['independent_autograd_velocity'] = velocities
    model = FunctionalLowRank(x, 32, 201)
    def loss(labels):
        return (model.predict(model.solve(labels, 1/32, 1.), query)-target).square().mean()
    labels = y.clone().requires_grad_()
    direction = torch.arange(1, 9, dtype=torch.float64)
    direction /= direction.norm()
    exact = float(torch.autograd.grad(loss(labels), labels)[0]@direction)
    fd = []
    with torch.no_grad():
        for epsilon in (1e-4, 5e-5):
            approx = float((loss(y+epsilon*direction)-loss(y-epsilon*direction))/(2*epsilon))
            error = abs(approx-exact)/max(abs(exact), 1e-12)
            assert error <= 1e-4, (epsilon, exact, approx, error)
            fd.append(dict(epsilon=epsilon, finite_difference=approx, relative_error=error))
    result.update(directional_hypergradient=dict(autograd=exact, differences=fd),
                  status='pass', inner_solves=7, end_utc=utc())
    write(out/'checks.json', result)
    print(json.dumps(plain(result)), flush=True)


def run(args, out):
    if args.device != 'cuda:1':
        raise ValueError('GPU1 is exclusively allocated to this control')
    check_result = json.loads(Path(args.checks).read_text())
    if check_result['status'] != 'pass':
        raise ValueError('Validation must pass before fitting')
    result = provenance(args, out)
    for name, digest in check_result['sources'].items():
        if result['sources'].get(name) != digest:
            raise ValueError('Source changed after validation: '+name)
    torch.cuda.set_device(args.device)
    torch.cuda.synchronize(args.device)
    started = time.monotonic()
    solves = int(check_result['inner_solves'])
    def solve(model, labels, dt):
        nonlocal solves
        if solves >= 180 or time.monotonic()-started >= 300:
            raise RuntimeError('Precommitted compute cap reached')
        solves += 1
        return model.solve(labels, dt, 8.)
    x, y = circle(8, .13, args.device, torch.float32)
    outer, target = circle(32, .37, args.device, torch.float32)
    test, test_y = circle(256, .71, args.device, torch.float32)
    result['validation'] = check_result
    result['designs'] = []
    result['baselines'] = []
    write(out/'run.json', result)
    try:
        for seed in (201, 202):
            dense = FunctionalFlow(x, 512, seed, 'dense')
            with torch.no_grad():
                baseline = dense.predict(solve(dense, y, 1/32), test)
                baseline_refined = dense.predict(solve(dense, y, 1/64), test)
                E0 = float((baseline-test_y).square().mean())
                E0r = float((baseline_refined-test_y).square().mean())
            result['baselines'].append(dict(seed=seed, dense_test_mse=E0,
                                           refined_dense_test_mse=E0r))
            for mobility in (.25, 1., 4.):
                torch.cuda.empty_cache()
                torch.cuda.reset_peak_memory_stats(args.device)
                model = FunctionalLowRank(x, 512, seed, mobility)
                labels = y.clone().requires_grad_()
                optimizer = torch.optim.Adam([labels], lr=.05)
                row = dict(seed=seed, factor_mobility=mobility, rank=8, width=512,
                           factor_seed=20260924, T=8., dt=1/32, outer_steps=24,
                           adam_lr=.05, moving_coordinates=19*512,
                           fixed_weight_coordinates=512**2, start_utc=utc(),
                           initial_labels=plain(y), outer_loss_history=[])
                design_started = time.monotonic()
                for iteration in range(24):
                    optimizer.zero_grad(set_to_none=True)
                    state = solve(model, labels, 1/32)
                    prediction = model.predict(state, outer)
                    loss = (prediction-target).square().mean()
                    if not bool(torch.isfinite(loss)):
                        raise FloatingPointError('Nonfinite outer loss')
                    loss.backward()
                    if not bool(torch.isfinite(labels.grad).all()):
                        raise FloatingPointError('Nonfinite label hypergradient')
                    if iteration == 0:
                        row['initial_gradient'] = plain(labels.grad)
                    row['outer_loss_history'].append(float(loss.detach()))
                    optimizer.step()
                    with torch.no_grad():
                        labels.clamp_(-3, 3)
                    del state, prediction, loss
                labels = labels.detach()
                with torch.no_grad():
                    trained = solve(model, labels, 1/32)
                    if not all(bool(torch.isfinite(v).all()) for v in trained):
                        raise FloatingPointError('Nonfinite final factor state')
                    own_test = model.predict(trained, test)
                    own_outer = model.predict(trained, outer)
                    movement = [float((a-b).square().mean().sqrt()) for a, b in
                                zip(model.fields(trained)[:2], model.fields(model.initial())[:2])]
                    prediction = dense.predict(solve(dense, labels, 1/32), test)
                    refined = dense.predict(solve(dense, labels, 1/64), test)
                    E = float((prediction-test_y).square().mean())
                    Er = float((refined-test_y).square().mean())
                torch.cuda.synchronize(args.device)
                improvement = E0-E
                row.update(status='ok', labels=plain(labels), dense_test_mse=E,
                           dense_error_ratio=E/E0, original_dense_test_mse=E0,
                           refined_dense_test_mse=Er, refined_dense_error_ratio=Er/E0r,
                           refined_original_dense_test_mse=E0r,
                           dense_mse_refinement_difference=abs(Er-E),
                           refinement_sensitivity_fraction=abs(Er-E)/improvement if improvement>0 else None,
                           improvement_persists_on_refinement=Er<E0r,
                           own_outer_mse=float((own_outer-target).square().mean()),
                           own_test_mse=float((own_test-test_y).square().mean()),
                           surrogate_dense_prediction_rms=float((own_test-prediction).square().mean().sqrt()),
                           hidden_activation_movement_rms=movement,
                           seconds=time.monotonic()-design_started,
                           peak_allocated_bytes=torch.cuda.max_memory_allocated(args.device),
                           peak_reserved_bytes=torch.cuda.max_memory_reserved(args.device),
                           end_utc=utc(), cumulative_inner_solves=solves)
                result['designs'].append(row)
                write(out/f'seed{seed}_mobility{mobility:g}.json', row)
                result.update(cumulative_inner_solves=solves, seconds=time.monotonic()-started)
                write(out/'run.json', result)
                print(json.dumps({k: row[k] for k in ('seed', 'factor_mobility',
                      'dense_test_mse', 'dense_error_ratio', 'refined_dense_error_ratio',
                      'own_test_mse', 'seconds', 'cumulative_inner_solves')}), flush=True)
                del model, optimizer, labels, trained
        result['status'] = 'complete'
    except Exception as exc:
        result.update(status='failed', error=repr(exc))
        if 'row' in locals():
            row.update(status='failed', error=repr(exc), labels=plain(labels),
                       cumulative_inner_solves=solves, end_utc=utc())
            write(out/'failed_design.json', row)
        raise
    finally:
        torch.cuda.synchronize(args.device)
        result.update(end_utc=utc(), cumulative_inner_solves=solves,
                      gpu_process_seconds=time.monotonic()-started)
        write(out/'run.json', result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=('check', 'run'), required=True)
    parser.add_argument('--device', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--checks')
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    (check if args.mode == 'check' else run)(args, out)
