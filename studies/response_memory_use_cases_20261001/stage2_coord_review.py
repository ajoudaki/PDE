"""Independent frozen-input review: no producer training or scoring calls.

Run with --out data/generated/response_memory_use_cases_20261001/stage2_coord_review01.
Optional --replay runs one full Fashion AB fit using autograd and row-oriented
forward evaluation, with independent streamed phase-difference moments.
"""
import argparse
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys
import time

for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
import torch

torch.set_num_threads(1)
torch.backends.cuda.matmul.allow_tf32 = False
torch.backends.cudnn.allow_tf32 = False
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GEN = ROOT/'data/generated/response_memory_use_cases_20261001'
MANIFEST = HERE/'STAGE2_COORD_FROZEN_MANIFEST.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def dump(path, value):
    Path(path).write_text(json.dumps(value, indent=2)+'\n')


def norm(x):
    return float(np.linalg.norm(x))


def relative(x, y):
    return norm(x-y)/max(norm(y), 1e-30)


def independent_coefficients(count, dt, q):
    # Gaussian quadrature, independent of producer's Legendre antiderivative.
    nodes, weights = np.polynomial.legendre.leggauss(max(20, q))
    mid = (np.arange(count)+.5)*dt
    t = mid[:, None]+dt/2*nodes
    vals = np.polynomial.legendre.legvander(2*t/(count*dt)-1, q-1)
    return (dt/2*np.einsum('itq,t->qi', vals, weights)
            *np.sqrt((2*np.arange(q)+1)/(count*dt))[:, None])


def oracle_checks():
    # Import only implementation functions being compared, not author checks.
    import stage2_coord_experiment as impl
    import stage2_coord_curriculum as curr
    from history_probe import interval_coefficients
    rng = np.random.default_rng(872093)
    errors = {}
    N, n, m, dt = 5, 4, 3, .173
    h, b = rng.normal(size=(2, N, n, m))
    def pairing(hh, bb):
        return -2*dt/(m*n)*np.einsum('ina,ija->nj', bb, hh)
    exact = pairing(h, b)
    centered_h, centered_b = h-h.mean(0), b-b.mean(0)
    mean = -2*dt*N/(m*n)*b.mean(0)@h.mean(0).T
    errors['centered_decomposition'] = relative(exact, mean+pairing(centered_h, centered_b))
    permutations = list(itertools.permutations(range(N)))
    writes = np.array([pairing(h, b[list(p)]) for p in permutations])
    errors['permutation_expectation'] = relative(writes.mean(0), mean)
    observed_var = np.mean(np.sum((writes-mean)**2, axis=(1, 2)))
    formula_var = (2*dt/(m*n))**2/(N-1)*sum(
        norm(B@H.T)**2 for B in centered_b for H in centered_h)
    errors['permutation_variance'] = abs(observed_var-formula_var)/formula_var
    errors['simultaneous_permutation'] = max(relative(pairing(h[list(p)], b[list(p)]), exact)
                                               for p in permutations)
    errors['double_reversal'] = relative(pairing(h, b[::-1][::-1]), exact)
    bounds = []
    for q in (1, 2, 3, 8, 16):
        C = independent_coefficients(N, dt, q)
        errors[f'interval_q{q}'] = norm(C-interval_coefficients(np.full(N, dt), q))
        H = np.einsum('ki,ina->kna', C, h)
        D = np.einsum('ki,ina->kna', C, b)
        DR = np.einsum('ki,ina->kna', C, b[::-1])
        errors[f'reflection_q{q}'] = relative(DR, (-1.)**np.arange(q)[:, None, None]*D)
        edit = 4/(m*n)*np.einsum('kna,kja->nj', D[1::2], H[1::2])
        target = pairing(h, b[::-1])-exact
        ht = dt*np.sum(((h-h[::-1])/2)**2, axis=(0, 1))-np.sum(H[1::2]**2, axis=(0, 1))
        bt = dt*np.sum(((b-b[::-1])/2)**2, axis=(0, 1))-np.sum(D[1::2]**2, axis=(0, 1))
        bound = 4/(m*n)*np.sqrt(ht.clip(0)*bt.clip(0)).sum()
        actual = norm(target-edit)
        assert actual <= bound+1e-12
        bounds.append(dict(kind='reflection', q=q, actual=actual, bound=float(bound)))
    # Independent phase-swap construction, including its nonzero q1 operation.
    h, b = rng.normal(size=(2, 14, n, m)); K = len(h)//2
    direct = pairing(h, np.roll(b, K, axis=0))-pairing(h, b)
    dh, db = h[:K]-h[K:], b[:K]-b[K:]
    errors['phase_swap_identity'] = relative(direct, -pairing(dh, db))
    for q in (1, 4, 8, 16):
        C = independent_coefficients(K, dt, q)
        H = np.einsum('ki,ina->kna', C, dh)
        D = np.einsum('ki,ina->kna', C, db)
        edit = 2/(m*n)*np.einsum('kna,kja->nj', D, H)
        ht = dt*np.sum(dh**2, axis=(0, 1))-np.sum(H**2, axis=(0, 1))
        bt = dt*np.sum(db**2, axis=(0, 1))-np.sum(D**2, axis=(0, 1))
        bound = 2/(m*n)*np.sqrt(ht.clip(0)*bt.clip(0)).sum()
        actual = norm(direct-edit)
        assert actual <= bound+1e-12
        bounds.append(dict(kind='phase_swap', q=q, actual=actual, bound=float(bound)))
        if q == 1:
            errors['phase_mean_identity'] = relative(edit, 2*dt*K/(m*n)*db.mean(0)@dh.mean(0).T)
    # All mobilities and residual normalization, including zero weights.
    x = rng.normal(size=(9, 3)); x /= np.linalg.norm(x, axis=1, keepdims=True)
    f = impl.new_model(dict(X_train=x, y_train=rng.normal(size=9)), 6, 717, 'cpu')
    f.c.copy_(torch.tensor(rng.normal(size=6)))
    for label, lam in [('uniform', np.full(9, 1/9)), ('phase', np.r_[np.full(4, .25), np.zeros(5)])]:
        pars = [p.clone().requires_grad_() for p in f.state]
        X = torch.tensor(x)
        pred = (X@pars[0].T).tanh().matmul(pars[1].T).tanh()@pars[2]/6
        loss = (torch.tensor(lam)*(pred-f.labels).square()).sum()
        grads = torch.autograd.grad(loss, pars)
        actual = curr.weighted_fields(f, torch.tensor(lam))[2]
        errors[label+'_autograd'] = max(relative(v.numpy(), (-s*g).detach().numpy())
            for v, g, s in zip(actual, grads, (6, 1, 6)))
    stationary = impl.new_model(dict(X_train=x, y_train=np.zeros(9)), 6, 718, 'cpu')
    errors['zero_residual_velocity'] = max(float(v.abs().max()) for v in impl.fields(stationary)[2])
    wa, wb = curr.phase_weights(np.arange(9)<4, 'cpu')
    for name in ('joint', 'AB', 'BA', 'alternating'):
        W = curr.schedule_weights(name, 64, wa, wb)
        errors['exposure_'+name] = relative(W.sum(0).numpy(), (32*(wa+wb)).numpy())
    E = torch.tensor(rng.normal(size=(7, 7)))
    sign, iso, _ = impl.controls(E, 291)
    errors['left_gram'] = relative((sign@sign.T).numpy(), (E@E.T).numpy())
    errors['right_gram'] = relative((sign.T@sign).numpy(), (E.T@E).numpy())
    errors['spectrum'] = relative(torch.linalg.svdvals(iso).numpy(), torch.linalg.svdvals(E).numpy())
    assert max(errors.values()) < 1e-10, errors
    return dict(errors=errors, bounds=bounds)


def inputs_and_hashes():
    frozen = read(MANIFEST)
    hashes = {str(MANIFEST.relative_to(ROOT)): sha(MANIFEST)}
    for name, expected in frozen['source_hashes'].items():
        assert sha(HERE/name) == expected, ('changed source', name)
    allowed = list(frozen['evidence_verification'])+[
        'stage2_coord_analysis01', 'stage2_coord_checks01', 'stage2_coord_checks02',
        'stage2_coord_curriculum_analysis01', 'stage2_coord_curriculum_checks01', 'stage2_data01']
    for name in allowed:
        for path in sorted((GEN/name).rglob('*')):
            if path.is_file():
                hashes[str(path.relative_to(ROOT))] = sha(path)
    for path in [HERE/name for name in frozen['source_hashes']]+[
        HERE/'MODEL_RECONCILIATION.md', HERE/'baseline_compact_flow.py', HERE/'STAGE2_DATA_PROTOCOL.md',
        HERE/'stage2_data.py', ROOT/'paper/main.tex', ROOT/'paper/results.tex']:
        hashes[str(path.relative_to(ROOT))] = sha(path)
    counts = {}
    for name, meta in frozen['evidence_verification'].items():
        folder = GEN/name
        manifest, completion = read(folder/'manifest.json'), read(folder/'completion.json')
        assert sha(folder/'manifest.json') == meta['manifest_sha256']
        assert sha(folder/'completion.json') == meta['completion_sha256']
        for source, expected in manifest['source_hashes'].items():
            assert sha(folder/source) == expected
        for archive, expected in completion['output_hashes'].items():
            assert sha(folder/archive) == expected
        for name_or_path, expected in manifest['input_hashes'].items():
            data_path = ROOT/name_or_path if '/' in name_or_path else GEN/'stage2_data01'/(name_or_path+'.npz')
            assert sha(data_path) == expected
        counts[name] = dict(archives=len(completion['output_hashes']), solves=completion['solves'],
                           seconds=completion['seconds'])
    return dict(frozen_manifest_sha256=sha(MANIFEST), hashes=hashes, counts=counts)


def raw_audit():
    metadata = read(MANIFEST)
    datasets = {d:dict(np.load(GEN/'stage2_data01'/(d+'.npz'))) for d in ('fashion','housing','har')}
    raw_rows, archive_checks = [], []
    for run in metadata['evidence_verification']:
        folder = GEN/run
        for row in read(folder/'results.json'):
            raw_rows.append(dict(run=run, **row))
            endpoint = row.get('schedule', 'endpoint')
            name = f"{row['domain']}_seed{row['seed']}_{endpoint}"
            if 'edits' not in row:
                assert row == read(folder/f"{row['domain']}_seed{row['seed']}_{row['arm']}.json")
                continue
            assert row == read(folder/(name+'.json'))
            z = np.load(folder/(name+'.npz'))
            data = datasets[row['domain']]
            X = torch.tensor(data['X_test'])
            y = data['y_test']; n = row['n']
            w1, w2, w3 = [torch.tensor(z[k]) for k in ('first','hidden','readout')]
            h = (X@w1.T).tanh()
            def predict(E):
                return ((h@(w2+E).T).tanh()@w3/n).numpy()
            baseline = predict(torch.zeros_like(w2))
            predkey = 'test_baseline' if 'schedule' in row else 'baseline_pred_test'
            max_pred_error = norm(baseline-z[predkey])/np.sqrt(len(y))
            max_score_error = abs(np.mean((baseline-y)**2)-row['base']['test_mse'])
            count = 0
            for k in z.files:
                if k.startswith('test_pred_'):
                    method = k.removeprefix('test_pred_')
                    max_score_error = max(max_score_error, abs(np.mean((z[k]-y)**2)-row['edits'][method]['test_mse']))
                    # Recompute every saved edit's function, independently of Flow.
                    reconstructed = predict(torch.tensor(z['edit_'+method]))
                    max_pred_error = max(max_pred_error, norm(reconstructed-z[k])/np.sqrt(len(y)))
                    count += 1
            coeff_error = 0.
            if 'schedule' in row:
                H, D = z['phase_difference_h_q8'], z['phase_difference_b_q8']
                for q in (1, 8):
                    edit = 2/(row['m']*n)*np.einsum('kia,kja->ij', D[:q], H[:q])
                    coeff_error = max(coeff_error, relative(edit, z['edit_swap_q'+str(q)]))
                coeff_error = max(coeff_error, relative(z['edit_swap']-z['edit_swap_q1'], z['edit_swap_centered']))
            else:
                for q in (4, 8, 16, 32):
                    if 'h_q'+str(q) not in z.files:
                        continue
                    H, D = z['h_q'+str(q)], z['b_q'+str(q)]
                    edit = 4/(row['m']*n)*np.einsum('kia,kja->ij', D[1::2], H[1::2])
                    if 'edit_reverse_q'+str(q) in z.files:
                        coeff_error = max(coeff_error, relative(edit, z['edit_reverse_q'+str(q)]))
            assert max_pred_error < 1e-11 and max_score_error < 1e-11 and coeff_error < 1e-10
            archive_checks.append(dict(run=run, case=name, scores=count, max_prediction_rms_error=max_pred_error,
                max_mse_error=max_score_error, max_coefficient_reconstruction_error=coeff_error))
    # Recalculate registered quantities directly from the per-case evidence.
    fixed, curriculum = {}, {}
    def relmse(r, k):
        return r['edits'][k]['test_mse']/r['base']['test_mse']-1
    def contrast(r):
        e = r['edits']
        matched = np.median([e[f'swap_sign_{j}']['test_mse'] for j in range(5)])-np.median([e[f'within_sign_{j}']['test_mse'] for j in range(5)])
        return (e['swap']['test_mse']-e['within']['test_mse']-matched)/r['base']['test_mse']
    for domain in datasets:
        rr = [r for r in raw_rows if r['run']=='stage2_coord_confirm01' and r['domain']==domain]
        damage = np.array([relmse(r, 'reverse') for r in rr])
        sign = np.array([np.median([relmse(r, f'sign_{j}') for j in range(5)]) for r in rr])
        remainder = np.array([abs(r['edits']['reverse']['train_nonlinear_remainder'])/abs(r['edits']['reverse']['train_mse']-r['base']['train_mse']) for r in rr])
        fixed[domain] = dict(damage=damage.tolist(), median_damage=float(np.median(damage)),
            median_excess=float(np.median(damage-sign)), median_remainder_fraction=float(np.median(remainder)),
            positive_seeds=int((damage>0).sum()), gate=bool(np.all(damage>0) and np.median(damage)>=.1 and np.median(damage-sign)>=.05 and np.median(remainder)>=.5))
        cr = [r for r in raw_rows if r['run']=='stage2_coord_curriculum01' and r['domain']==domain]
        lookup = {(r['seed'],r['schedule']):r for r in cr}
        values, centered, ratios = [], [], []
        for seed in (3401,3402,3403,3404):
            values.append((contrast(lookup[seed,'AB'])+contrast(lookup[seed,'BA']))/2-contrast(lookup[seed,'joint']))
            centered.append(np.mean([relmse(lookup[seed,s],'swap_centered') for s in ('AB','BA')]))
            for s in ('AB','BA'):
                r = lookup[seed,s]; b = r['base']['test_mse']
                ratios.append(abs(r['edits']['swap_q1']['test_mse']-b)/abs(r['edits']['swap']['test_mse']-b))
        curriculum[domain] = dict(F=values, median_F=float(np.median(values)),
            centered=centered, median_centered=float(np.median(centered)),
            phase_q1_ratios=ratios, median_q1_ratio=float(np.median(ratios)),
            gate=bool(all(v>0 for v in values) and np.median(values)>=.05 and np.median(centered)>=.02 and np.median(ratios)<.5))
    return dict(archives=archive_checks, fixed=fixed, curriculum=curriculum,
        total_archives=len(archive_checks), total_reconstructed_edit_predictions=sum(v['scores'] for v in archive_checks),
        max_invariant_error=max(max(r['invariants'].values()) for r in raw_rows if 'invariants' in r),
        feature_motion_range=[min(r['feature_motion'] for r in raw_rows if 'feature_motion' in r),max(r['feature_motion'] for r in raw_rows if 'feature_motion' in r)],
        nonlinearity_range=[min(r['nonlinearity'] for r in raw_rows if 'nonlinearity' in r),max(r['nonlinearity'] for r in raw_rows if 'nonlinearity' in r)])


def replay(device):
    # One original seed/configuration. Uses torch autograd instead of the
    # producer's manually coded velocities; zero inactive gradients are exact.
    started = time.perf_counter()
    data = dict(np.load(GEN/'stage2_data01/fashion.npz'))
    n, m, N, dt, seed = 256, 512, 1024, 1/16, 3401
    rng = np.random.default_rng(seed)
    W1 = torch.tensor(rng.standard_normal((n,data['X_train'].shape[1])), device=device, requires_grad=True)
    W2 = torch.tensor(rng.standard_normal((n,n))/np.sqrt(n), device=device, requires_grad=True)
    w = torch.zeros(n, dtype=torch.float64, device=device, requires_grad=True)
    initial_W2 = W2.detach().clone()
    X = torch.tensor(data['X_train'][:m], device=device)
    y = torch.tensor(data['y_train'][:m], device=device)
    coordinate = (data['X_train'][:m,:-1]/data['X_train'][:m,-1:]).mean(1)
    mask = coordinate<=np.median(coordinate)
    wa = torch.tensor(mask/mask.sum(), device=device); wb = torch.tensor((~mask)/(~mask).sum(), device=device)
    K = N//2
    hA = torch.empty((K,m,n), dtype=torch.float64, device=device)
    bA = torch.empty_like(hA)
    swap = torch.zeros((n,n), dtype=torch.float64, device=device)
    C = torch.tensor(independent_coefficients(K, dt, 8), device=device)
    H = torch.zeros((8,m,n), dtype=torch.float64, device=device); D = torch.zeros_like(H)
    actual_write = torch.zeros_like(swap)
    for i in range(N):
        if time.perf_counter()-started>285:
            raise RuntimeError('Independent replay cap reached')
        lam = wa if i<K else wb
        h = (X@W1.T).tanh(); h2 = (h@W2.T).tanh(); r = h2@w/n-y
        loss = (lam*r.square()).sum()
        grads = torch.autograd.grad(loss, (W1,W2,w))
        with torch.no_grad():
            b = m*(lam*r)[:,None]*w[None,:]*(1-h2.square())
            actual_write.add_(b.T@h, alpha=-2*dt/(m*n))
            if i<K:
                hA[i].copy_(h); bA[i].copy_(b)
            else:
                j = i-K; dh = hA[j]-h; db = bA[j]-b
                swap.add_(db.T@dh, alpha=2*dt/(m*n))
                H.add_(C[:,j,None,None]*dh); D.add_(C[:,j,None,None]*db)
            for param, gradient, mobility in zip((W1,W2,w),grads,(n,1,n)):
                param.add_(gradient, alpha=-dt*mobility)
    saved = np.load(GEN/'stage2_coord_curriculum01/fashion_seed3401_AB.npz')
    errors = {name:relative(param.detach().cpu().numpy(),saved[name]) for name,param in zip(('first','hidden','readout'),(W1,W2,w))}
    errors['exact_update'] = relative(actual_write.cpu().numpy(),(W2-initial_W2).detach().cpu().numpy())
    errors['swap'] = relative(swap.cpu().numpy(),saved['edit_swap'])
    errors['phase_h_q8'] = relative(H.permute(0,2,1).cpu().numpy(), saved['phase_difference_h_q8'])
    errors['phase_b_q8'] = relative(D.permute(0,2,1).cpu().numpy(), saved['phase_difference_b_q8'])
    q1 = 2/(m*n)*D[0].T@H[0]
    q8 = 2/(m*n)*torch.einsum('kai,kaj->ij',D,H)
    errors['swap_q1'] = relative(q1.cpu().numpy(),saved['edit_swap_q1'])
    errors['swap_q8'] = relative(q8.cpu().numpy(),saved['edit_swap_q8'])
    test_x = torch.tensor(data['X_test'],device=device)
    with torch.no_grad():
        test_h = (test_x@W1.T).tanh()
        pred = (test_h@W2.T).tanh()@w/n
    errors['test_prediction_rms'] = norm(pred.cpu().numpy()-saved['test_baseline'])/np.sqrt(len(pred))
    assert max(errors.values())<1e-9, errors
    return dict(case='fashion_seed3401_AB', device=device, full_fits=1, errors=errors,
                seconds=time.perf_counter()-started, description='Independent autograd trainer and quadrature, row-oriented forward pass')


def supplementary():
    started = time.perf_counter()
    fixed = read(GEN/'stage2_coord_confirm01/results.json')
    fine = read(GEN/'stage2_coord_refine01/results.json')
    curriculum = read(GEN/'stage2_coord_curriculum01/results.json')
    curriculum_fine = read(GEN/'stage2_coord_curriculum_refine01/results.json')
    old_summary = read(GEN/'stage2_coord_analysis01/summary.json')
    current_summary = read(GEN/'stage2_coord_curriculum_analysis01/summary.json')
    errors = []
    reflection = []
    for reference in old_summary['reflection']:
        folder = GEN/reference['run']; domain = reference['domain']; n = reference['n']
        z = np.load(folder/f"{domain}_seed{reference['seed']}_endpoint.npz")
        X = torch.tensor(np.load(GEN/'stage2_data01'/(domain+'.npz'))['X_test'])
        W1, W2, w = [torch.tensor(z[k]) for k in ('first','hidden','readout')]
        h = (X@W1.T).tanh(); vals = {}
        for q in (4,8,16,32):
            if 'h_q'+str(q) not in z.files:
                continue
            H, D = z['h_q'+str(q)], z['b_q'+str(q)]
            E = 4/(512*n)*np.einsum('kia,kja->ij',D[1::2],H[1::2])
            pred = ((h@(W2+torch.tensor(E)).T).tanh()@w/n).numpy()
            vals[str(q)] = dict(relative_edit_error=relative(E,z['edit_reverse']),
                prediction_rms_error=norm(pred-z['test_pred_reverse'])/np.sqrt(len(pred)))
            for key, value in vals[str(q)].items():
                errors.append(abs(value-reference['modes'][str(q)][key]))
        reflection.append(dict(run=reference['run'],domain=domain,seed=reference['seed'],modes=vals))
    def contrast(r):
        e = r['edits']; b = r['base']['test_mse']
        return (e['swap']['test_mse']-e['within']['test_mse']-np.median([e[f'swap_sign_{j}']['test_mse'] for j in range(5)])+np.median([e[f'within_sign_{j}']['test_mse'] for j in range(5)]))/b
    refinement = []
    for domain in ('fashion','housing','har'):
        cr = next(r for r in fixed if r['domain']==domain and r['seed']==3201)
        fr = next(r for r in fine if r['domain']==domain)
        cp = np.load(GEN/f'stage2_coord_confirm01/{domain}_seed3201_endpoint.npz')['baseline_pred_test']
        fp = np.load(GEN/f'stage2_coord_refine01/{domain}_seed3201_endpoint.npz')['baseline_pred_test']
        effect = cr['edits']['reverse']['test_mse']-cr['base']['test_mse']
        effect_f = fr['edits']['reverse']['test_mse']-fr['base']['test_mse']
        recomputed = dict(domain=domain,prediction_rms_discrepancy=norm(cp-fp)/np.sqrt(len(cp)),
            coarse_effect=effect,fine_effect=effect_f,absolute_effect_change=abs(effect-effect_f))
        reported = next(r for r in old_summary['step_refinement'] if r['domain']==domain)
        errors.extend(abs(v-reported[k]) for k,v in recomputed.items() if k!='domain')
        refinement.append(recomputed)
        cr = {r['schedule']:r for r in curriculum if r['domain']==domain and r['seed']==3401}
        fr = {r['schedule']:r for r in curriculum_fine if r['domain']==domain}
        report = next(r for r in current_summary['refinement'] if r['domain']==domain)
        errors.append(abs(abs(contrast(cr['AB'])-contrast(cr['joint']))-report['contrast_effect']))
        errors.append(abs(abs(contrast(fr['AB'])-contrast(fr['joint'])-contrast(cr['AB'])+contrast(cr['joint']))-report['contrast_step_change']))
        for s in ('joint','AB'):
            cp = np.load(GEN/f'stage2_coord_curriculum01/{domain}_seed3401_{s}.npz')['test_baseline']
            fp = np.load(GEN/f'stage2_coord_curriculum_refine01/{domain}_seed3401_{s}.npz')['test_baseline']
            e = norm(cp-fp)/np.sqrt(len(cp))
            errors.append(abs(e-next(v['prediction_rms'] for v in report['checks'] if v['schedule']==s)))
    # Test the word "isotropic" by examining the QR factors actually used.
    # Rotationally uniform Q has E[Q_11]=0 and each sign occurs equally often.
    gen = torch.Generator().manual_seed(623047)
    first_entries = []
    for _ in range(1000):
        Q = torch.linalg.qr(torch.randn((8,8),generator=gen,dtype=torch.float64)).Q
        first_entries.append(float(Q[0,0]))
    errors_max = max(errors)
    assert errors_max<1e-10, errors_max
    return dict(seconds=time.perf_counter()-started,summary_max_error=errors_max,
        reflection=reflection,refinement=refinement,
        curriculum_q8_max_error=max(r['compression']['8']['relative_edit_error'] for r in curriculum),
        curriculum_q16_max_error=max(r['compression']['16']['relative_edit_error'] for r in curriculum),
        curriculum_sequential_q16_max_error=max(r['compression']['16']['relative_edit_error'] for r in curriculum if r['schedule'] in ('AB','BA')),
        qr_diagnostic=dict(samples=1000,dimension=8,first_entry_mean=float(np.mean(first_entries)),
                           first_entry_positive_count=sum(v>0 for v in first_entries)),source_sha256=sha(__file__))


def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',type=Path,required=True)
    p.add_argument('--replay',action='store_true');p.add_argument('--supplement',action='store_true')
    p.add_argument('--device',default='cuda:1')
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    started=time.perf_counter()
    if a.replay:
        result = replay(a.device);dump(a.out/'replay.json',result);print(json.dumps(result,indent=2));return
    if a.supplement:
        result=supplementary();dump(a.out/'supplementary.json',result)
        print(json.dumps({k:v for k,v in result.items() if k not in ('reflection','refinement')},indent=2));return
    inputs=inputs_and_hashes();dump(a.out/'input_hashes.json',inputs)
    oracles=oracle_checks();dump(a.out/'oracles.json',oracles)
    raw=raw_audit();dump(a.out/'raw_audit.json',raw)
    assert sha(MANIFEST)==inputs['frozen_manifest_sha256'], 'Manifest changed during review'
    result=dict(seconds=time.perf_counter()-started,source_sha256=sha(__file__),
        frozen_manifest_sha256=sha(MANIFEST),oracles_max_error=max(oracles['errors'].values()),
        full_fits=0,total_archives=raw['total_archives'],scores_reconstructed=raw['total_reconstructed_edit_predictions'],
        max_prediction_error=max(v['max_prediction_rms_error'] for v in raw['archives']),
        max_score_error=max(v['max_mse_error'] for v in raw['archives']),
        fixed=raw['fixed'],curriculum=raw['curriculum'])
    dump(a.out/'completion.json',result);print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
