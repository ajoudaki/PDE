"""Isolated review of the frozen label-population run; writes only review outputs.

The executed learner definitions are exact AST selections from the frozen files.
This avoids executing unrelated legacy imports or reading other studies.
"""
import argparse
import ast
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import tarfile
import time
import types
import zipfile

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GEN = ROOT / 'data/generated/response_memory_use_cases_20261001'
RUN = GEN / 'stage2_label_index01'
DATA = GEN / 'stage2_data01'
OUT = GEN / 'stage2_label_review01'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(name, obj):
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(json.dumps(obj, indent=2, allow_nan=False) + '\n')


def load_definitions():
    scope = dict(np=np, torch=torch, math=math, time=time, Path=Path,
                 hashlib=hashlib, json=json)
    selected = [
        ('baseline_compact_flow.py', ['_activation', 'Flow', 'LowRankFlow']),
        ('input_field.py', ['InputFieldFlow']),
        ('stage2_index_experiment.py', ['TunedFactors']),
        ('stage2_label_index.py', ['sha', 'write', 'make', 'capture_checks', 'fit']),
    ]
    for filename, names in selected:
        tree = ast.parse((RUN / filename).read_text())
        body = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names]
        assert {n.name for n in body} == set(names)
        exec(compile(ast.Module(body=body, type_ignores=[]), str(RUN / filename), 'exec'), scope)
    return types.SimpleNamespace(**scope)


def provenance():
    hashes = {str(p.relative_to(ROOT)): sha(p) for folder in [RUN, DATA]
              for p in sorted(folder.rglob('*')) if p.is_file()}
    for name in ['STAGE2_LABEL_INDEX_PROTOCOL.md', 'stage2_label_index.py', 'input_field.py',
                 'baseline_compact_flow.py', 'stage2_index_experiment.py', 'MODEL_RECONCILIATION.md',
                 'STAGE2_DATA_PROTOCOL.md', 'stage2_data.py']:
        p = HERE / name
        hashes[str(p.relative_to(ROOT))] = sha(p)
    manifest = json.loads((RUN / 'manifest.json').read_text())
    for name, digest in manifest['sources'].items():
        assert sha(RUN / name) == sha(HERE / name) == digest, name
    dm = json.loads((DATA / 'manifest.json').read_text())
    assert dm['source_sha256'] == sha(HERE / 'stage2_data.py')
    assert dm['protocol_sha256'] == sha(HERE / 'STAGE2_DATA_PROTOCOL.md')
    for name, row in dm['sources'].items():
        p = DATA / 'raw' / name
        assert sha(p) == row['sha256']
        assert p.stat().st_size == row['bytes']
        expected = row['expected_checksum']
        if expected:
            actual = hashlib.md5(p.read_bytes()).hexdigest() if len(expected) == 32 else sha(p)
            assert actual == expected
    for name, row in dm['datasets'].items():
        assert sha(DATA / (name + '.npz')) == row['sha256']
    hashes[str(Path(__file__).relative_to(ROOT))] = sha(__file__)
    save('input_hashes.json', hashes)
    return dict(files_hashed=len(hashes), all_recorded_hashes_match=True,
                hash_manifest_sha256=sha(OUT / 'input_hashes.json'))


def independent_data():
    """Reconstruct each selected source row and split without calling stage2_data."""
    dm = json.loads((DATA / 'manifest.json').read_text())
    records = {}
    def read_idx(name):
        b = gzip.decompress((DATA / 'raw' / name).read_bytes())
        dims = b[3]
        shape = tuple(int.from_bytes(b[4+4*i:8+4*i], 'big') for i in range(dims))
        return np.frombuffer(b[4+4*dims:], dtype=np.uint8).reshape(shape)
    raw_splits = {}
    rng = np.random.default_rng(20261002)
    for prefix, destinations in [('train', [('train', 1024), ('val', 256)]), ('t10k', [('test', 1024)])]:
        x = read_idx(prefix + '-images-idx3-ubyte.gz').reshape(-1, 784)
        g = read_idx(prefix + '-labels-idx1-ubyte.gz')
        selected = rng.permutation(np.flatnonzero(np.isin(g, [0, 6])))
        pos = 0
        for split, count in destinations:
            ids = selected[pos:pos+count]; pos += count
            raw_splits[('fashion', split)] = (x[ids], np.where(g[ids] == 6, 1., -1.), ids,
                                             g[ids], np.zeros(count, dtype=int))
    with tarfile.open(DATA / 'raw/cal_housing.tgz') as archive:
        a = np.loadtxt(archive.extractfile('CaliforniaHousing/cal_housing.data'), delimiter=',')
    x = np.column_stack([a[:, 7], a[:, 2], a[:, 3]/a[:, 6], a[:, 4]/a[:, 6],
                         a[:, 5], a[:, 5]/a[:, 6], a[:, 1], a[:, 0]])
    selected = np.random.default_rng(20261002).permutation(len(a))
    pos = 0
    for split, count in [('train', 1024), ('val', 256), ('test', 1024)]:
        ids = selected[pos:pos+count]; pos += count
        raw_splits[('housing', split)] = (x[ids], a[ids, 8]/100000., ids,
                                         np.zeros(count, dtype=int), np.zeros(count, dtype=int))
    rng = np.random.default_rng(20261002)
    with zipfile.ZipFile(DATA / 'raw/har.zip') as outer:
        nested = [n for n in outer.namelist() if n.endswith('.zip')]
        archive = zipfile.ZipFile(io.BytesIO(outer.read(nested[0]))) if nested else outer
        def read_har(suffix):
            names = [n for n in archive.namelist() if n.endswith(suffix)]
            assert len(names) == 1
            return np.loadtxt(io.BytesIO(archive.read(names[0])))
        for pool in ['train', 'test']:
            x = read_har(f'{pool}/X_{pool}.txt')
            g = read_har(f'{pool}/y_{pool}.txt').astype(int)
            s = read_har(f'{pool}/subject_{pool}.txt').astype(int)
            validation_subjects = sorted(set(s))[-4:]
            destinations = [('test', np.arange(len(s)), 1024)] if pool == 'test' else [
                ('train', np.flatnonzero(~np.isin(s, validation_subjects)), 1024),
                ('val', np.flatnonzero(np.isin(s, validation_subjects)), 256)]
            for split, candidates, count in destinations:
                ids = rng.permutation(candidates)[:count]
                raw_splits[('har', split)] = (x[ids], np.where(g[ids] <= 3, 1., -1.), ids, g[ids], s[ids])
        if archive is not outer:
            archive.close()
    for domain in ['fashion', 'har', 'housing']:
        data = dict(np.load(DATA / (domain + '.npz')))
        tx, ty = raw_splits[(domain, 'train')][:2]
        mean = tx.astype(float).mean(0); std = np.maximum(tx.astype(float).std(0), .001)
        np.testing.assert_array_equal(data['input_mean'], mean)
        np.testing.assert_array_equal(data['input_std'], std)
        err = 0.
        for split in ['train', 'val', 'test']:
            x, y, ids, groups, subjects = raw_splits[(domain, split)]
            emb = np.column_stack([np.clip((x-mean)/std, -5, 5), np.ones(len(x))])
            emb /= np.sqrt(np.sum(emb*emb, axis=1, keepdims=True))
            target = np.tanh((y-ty.mean())/ty.std()) if domain == 'housing' else y
            for name, value in [('X', emb), ('y', target), ('index', ids), ('group', groups), ('subject', subjects)]:
                np.testing.assert_array_equal(data[name+'_'+split], value)
            err = max(err, float(np.max(np.abs(np.linalg.norm(emb, axis=1)-1))))
        if domain == 'har':
            sets = [set(data['subject_'+s]) for s in ['train', 'val', 'test']]
            assert all(not sets[i] & sets[j] for i in range(3) for j in range(i))
        y = data['y_train'].astype(np.float32)
        edges = np.quantile(y, [.25, .5, .75]) if domain == 'housing' else np.array([0.])
        groups = np.searchsorted(edges, y, side='right')
        counts = np.bincount(groups); p = counts/len(y)
        basis = np.eye(len(p))[groups]/np.sqrt(p)
        gram_error = float(np.max(np.abs(basis.T@basis/len(y)-np.eye(len(p)))))
        assert gram_error < 1e-12
        y64 = data['y_train']
        e64 = np.quantile(y64, [.25, .5, .75]) if domain == 'housing' else np.array([0.])
        assert np.array_equal(groups, np.searchsorted(e64, y64, side='right'))
        records[domain] = dict(arrays_bitwise_reproduced=True, maximum_norm_error=err,
                               counts=counts.tolist(), probabilities=p.tolist(), edges=edges.tolist(),
                               float64_gram_error=gram_error,
                               quantile_group_assignment_preserved_by_float32=True,
                               train_label_rms=float(np.sqrt(np.mean(y64**2))))
    save('data_checks.json', records)
    return records


def cpu_oracles(mod):
    rng = np.random.default_rng(860214)
    checks = []
    def close(name, a, b, atol=2e-12, rtol=2e-12):
        a, b = torch.as_tensor(a), torch.as_tensor(b)
        torch.testing.assert_close(a, b, atol=atol, rtol=rtol, check_dtype=False)
        checks.append(dict(check=name, maximum_absolute_error=float((a-b).abs().max())))
    x = rng.normal(size=(11, 5)); x /= np.linalg.norm(x, axis=1, keepdims=True)
    query = rng.normal(size=(7, 5))
    settings = dict(width=13, depth=2, activation='tanh', seed=4501,
                    device='cpu', dtype=torch.float64, hidden_gain=1., readout_std=1.)
    for C, groups in [(2, np.array([0]*3+[1]*8)), (4, np.array([0]+[1]*2+[2]*3+[3]*5))]:
        p = np.bincount(groups)/len(groups)
        basis = np.eye(C)[groups]/np.sqrt(p)
        y = rng.normal(size=len(x))
        def grouped(field):
            return torch.stack([math.sqrt(p[c])*field[:, groups == c].mean(1) for c in range(C)], 1)
        for q in [1, 6, 12]:
            model = mod.InputFieldFlow(x, y, basis, order=q, **settings)
            h0 = torch.tanh(model.w@model.inputs.T)
            close('prefix_group_means', model.moments[1][0], grouped(h0))
            close('prefix_backward_zero', model.moments[0], torch.zeros_like(model.moments[0]))
            if q > 1:
                close('prefix_higher_forward_zero', model.moments[1][1:], torch.zeros_like(model.moments[1][1:]))
            close('zero_readout', model.c, torch.zeros_like(model.c))
            close('initial_clock', model.s, 0.)
            with torch.no_grad():
                model.c.copy_(torch.from_numpy(rng.normal(size=model.n)))
                for field in model.moments:
                    field.copy_(torch.from_numpy(rng.normal(scale=.04, size=field.shape)))
                model.s.fill_(.73)
            A, B = model.moments
            W = model.matrices[0] - sum((2*j+1)*A[j]@B[j].T for j in range(q))*2/(model.n*(1+model.s))
            left, right = model._factors()[0]
            close('matrix_factor_normalization', W, model.matrices[0]+left@right.T)
            close('actual_transpose', model._apply(0, torch.eye(model.n, dtype=torch.float64), model._factors(), True), W.T)
            w = model.w.clone().requires_grad_(); c = model.c.clone().requires_grad_()
            wm = W.clone().requires_grad_()
            z1 = w@model.inputs.T; h1 = z1.tanh(); z2 = wm@h1; h2 = z2.tanh()
            pred = c@h2/model.n; residual = pred-model.labels
            loss = residual.square().mean(); rho = loss.detach().sqrt()
            dw, dc, dz2 = torch.autograd.grad(loss, (w, c, z2))
            rd = dz2.detach()*(model.M*model.n/2)
            velocities = model.rhs()
            close('first_layer_mobility_n', velocities[0], -model.n*dw)
            close('readout_mobility_n', velocities[1], -model.n*dc)
            close('prediction_materialized', model.predict(x), pred.detach())
            for field, source, actual in [(A, grouped(rd), velocities[2]),
                                           (B, rho*grouped(h1.detach()), velocities[3])]:
                expected = torch.stack([source-rho/(1+model.s)*(j*field[j]+sum((2*k+1)*field[k] for k in range(j)))
                                        for j in range(q)])
                close('raw_grouped_source_and_transport', actual, expected)
            close('clock_rho', velocities[-1], rho)
            # Neither labels nor addresses are evaluated in a query forward pass.
            before = model.predict(query)
            saved_y, saved_basis = model.labels.clone(), model.basis.clone()
            model.labels.fill_(float('nan')); model.basis.fill_(float('nan'))
            close('query_label_and_address_independence', model.predict(query), before, atol=0, rtol=0)
            model.labels.copy_(saved_y); model.basis.copy_(saved_basis)
            model.labels.copy_(model.predict(x))
            for v in model.rhs():
                close('zero_residual_stationarity', v, torch.zeros_like(v), atol=1e-14)
            model.labels.copy_(saved_y)
            snapshot = [v.clone() for v in model.state]
            rhs = model.rhs()
            model.step(.0003)
            for actual, initial, v in zip(model.state, snapshot, rhs):
                close('simultaneous_euler', actual, initial+.0003*v)
        # The omitted part is the within-group covariance, not an unweighted mean.
        f = rng.normal(size=(7, len(x))); g = rng.normal(size=(9, len(x)))
        fp = f@basis/len(x); gp = g@basis/len(x)
        ft = f-fp@basis.T; gt = g-gp@basis.T
        omitted = f@g.T/len(x)-fp@gp.T
        close('orthogonal_product_tail_identity', omitted, ft@gt.T/len(x))
        assert np.linalg.norm(omitted) <= np.sqrt(np.mean(np.sum(ft*ft, 0))*np.mean(np.sum(gt*gt, 0)))+1e-12
    # A complete sample-indicator basis restores the original 1/m exactly.
    y = rng.normal(size=len(x)); basis = math.sqrt(len(x))*np.eye(len(x))
    for q in [1, 3]:
        field = mod.InputFieldFlow(x, y, basis, order=q, **settings)
        sample = mod.Flow(x, y, order=q, **settings); sample.c.zero_()
        for _ in range(5):
            close('complete_indicator_prediction', field.predict(query), sample.predict(query))
            close('complete_indicator_first_weight', field.w, sample.w)
            close('complete_indicator_readout', field.c, sample.c)
            for a, b in zip(field.moments, sample.moments):
                close('complete_indicator_raw_scaling', a, b/math.sqrt(len(x)))
            field.step(.02); sample.step(.02)
    for rate in [.25, 4.]:
        model = mod.TunedFactors(x, y, rank=4, factor_seed=14501, factor_rate=rate, **settings)
        with torch.no_grad():
            for value in model.state:
                value.add_(torch.from_numpy(rng.normal(scale=.1, size=value.shape)))
        w, c, a, b = [v.clone().requires_grad_() for v in model.state]
        h = torch.tanh((model.matrices[0]+a@b)@torch.tanh(w@model.inputs.T))
        loss = (c@h/model.n-model.labels).square().mean()
        gradients = torch.autograd.grad(loss, (w, c, a, b))
        for actual, gradient, mobility in zip(model.rhs(), gradients, [model.n, model.n, rate, rate]):
            close('factor_mobility', actual, -mobility*gradient)
    result = dict(assertions=len(checks), maximum_absolute_error=max(v['maximum_absolute_error'] for v in checks),
                  checks=checks, all_pass=True)
    save('cpu_oracles.json', result)
    return {k:v for k,v in result.items() if k != 'checks'}


def audit_results(mod, data_records):
    results = json.loads((RUN / 'results.json').read_text())
    completion = json.loads((RUN / 'completion.json').read_text())
    expected = {(d, s, k, 1/64) for d in ['fashion', 'har', 'housing'] for s in range(4501, 4505)
                for k in ['population_q1', 'population_matched', 'factor']}
    expected |= {(d, 4501, k, 1/128) for d in ['fashion', 'har', 'housing'] for k in ['population_matched', 'factor']}
    assert len(results) == len(expected) == completion['fits'] == 42
    assert {(r['domain'], r['seed'], r['kind'], r['dt']) for r in results} == expected
    assert len(list(RUN.glob('fit_*/result.json'))) == 42
    max_metric_error = 0.; costs = {}; per_fit = []
    for i, row in enumerate(results):
        folder = RUN / f'fit_{i:03d}'
        assert json.loads((folder/'result.json').read_text()) == row
        data = dict(np.load(DATA/(row['domain']+'.npz')))
        pred = dict(np.load(folder/'predictions.npz'))
        assert pred['predictions'].shape == (4, 1024)
        assert np.isfinite(pred['predictions']).all()
        np.testing.assert_array_equal(pred['target'], data['y_test'])
        assert row['data_sha256'] == sha(DATA/(row['domain']+'.npz'))
        assert [r['time'] for r in row['checkpoints']] == [16, 32, 64, 128]
        for j, cp in enumerate(row['checkpoints']):
            assert all(np.isfinite(cp[k]) for k in ['train', 'val', 'test'])
            actual = float(np.sqrt(np.mean((pred['predictions'][j].astype(float)-data['y_test'])**2)))
            err = abs(actual-cp['test']); max_metric_error=max(max_metric_error, err)
            assert err < 2e-7
        index = min(range(4), key=lambda j: row['checkpoints'][j]['val'])
        assert index == row['selected_index'] and row['selected'] == row['checkpoints'][index]
        training = {k: torch.tensor(data[k], dtype=torch.float32) for k in ['X_train','y_train']}
        model = mod.make(training, row['domain'], row['seed'], row['kind'], 'cpu')
        assert row['moving_scalars'] == sum(v.numel() for v in model.state)
        assert row['base_scalars'] == model.n**2 == 65536
        expected_basis = model.basis.numel() if row['kind'] != 'factor' else 0
        assert row['cached_basis_scalars'] == expected_basis
        if row['kind'] != 'factor':
            meta, expected_meta = row['addresses'], model.address_metadata
            for key in ['C','q','probabilities','edges','group_counts']:
                assert meta[key] == expected_meta[key], key
            assert meta['gram_error'] < 1e-5 and expected_meta['gram_error'] < 1e-5
            assert meta['q']*meta['C'] == (meta['C'] if row['kind']=='population_q1' else 24)
        else:
            assert row['addresses'] is None
        costs[(row['domain'],row['kind'])] = [row[k] for k in ['moving_scalars','base_scalars','cached_basis_scalars']]
        per_fit.append(dict(fit=folder.name, domain=row['domain'],seed=row['seed'],kind=row['kind'],dt=row['dt'],
                            selected_index=index,selected=row['selected']))
    groups={}; refinement=[]
    for domain in ['fashion','har','housing']:
        def get(kind, seed, dt=1/64):
            return next(r for r in results if (r['domain'],r['kind'],r['seed'],r['dt'])==(domain,kind,seed,dt))
        matched = np.array([get('population_matched',s)['selected']['test'] for s in range(4501,4505)])
        factor = np.array([get('factor',s)['selected']['test'] for s in range(4501,4505)])
        q1 = np.array([get('population_q1',s)['selected']['test'] for s in range(4501,4505)])
        improvement = (factor-matched)/factor
        groups[domain] = dict(matched_test=matched.tolist(),factor_test=factor.tolist(),q1_test=q1.tolist(),
                              paired_fractional_improvements=improvement.tolist(),
                              median_paired_fractional_improvement=float(np.median(improvement)),
                              paired_wins=int(np.sum(improvement>0)),
                              domain_gate=bool(np.median(improvement)>=.05 and np.sum(improvement>0)>=3))
        advantage = abs(factor[0]-matched[0])
        for kind in ['population_matched','factor']:
            coarse, fine = get(kind,4501), get(kind,4501,1/128)
            change=abs(coarse['selected']['test']-fine['selected']['test'])
            refinement.append(dict(domain=domain,kind=kind,selected_test_rmse_absolute_change=change,
                                   same_selected_time=coarse['selected']['time']==fine['selected']['time'],
                                   fraction_training_label_rms=change/data_records[domain]['train_label_rms'],
                                   fraction_absolute_seed4501_gap=change/advantage,
                                   rms_gate=bool(change<.01*data_records[domain]['train_label_rms']),
                                   gap_gate=bool(change<advantage/3)))
    positive = sum(v['domain_gate'] for v in groups.values()) >= 2 and all(
        v['median_paired_fractional_improvement'] >= -.05 for v in groups.values())
    result=dict(fits=42,checkpoint_records=168,metrics_recomputed=168,max_saved_test_metric_error=max_metric_error,
                all_grid_checkpoint_hash_and_cost_checks_pass=True,primary_gate=positive,domains=groups,
                refinement=refinement,all_refinement_gates_pass=all(r['rms_gate'] and r['gap_gate'] for r in refinement),
                costs=[dict(domain=d,kind=k,moving=v[0],base=v[1],basis=v[2]) for (d,k),v in costs.items()],
                per_fit=per_fit,original_capture_checks=json.loads((RUN/'capture_checks.json').read_text()))
    save('result_audit.json',result)
    return {k:v for k,v in result.items() if k not in ['per_fit','costs']}


def gpu_replay(mod):
    torch.cuda.set_device('cuda:0')
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    started=time.perf_counter()
    checks=mod.capture_checks('cuda:0')
    out=OUT/'housing_seed4501_population_matched_replay';out.mkdir(exist_ok=False)
    result=mod.fit(DATA/'housing.npz',4501,'population_matched',1/64,'cuda:0',out)
    reference=json.loads((RUN/'fit_029/result.json').read_text())
    a=np.load(out/'predictions.npz')['predictions'];b=np.load(RUN/'fit_029/predictions.npz')['predictions']
    diff=float(np.max(np.abs(a-b)))
    assert diff<2e-5
    assert result['selected_index']==reference['selected_index']
    assert time.perf_counter()-started < 180
    report=dict(device=torch.cuda.get_device_name(),capture_checks=checks,full_fits=1,
                prediction_maximum_absolute_difference=diff,bitwise_identical_predictions=bool(np.array_equal(a,b)),
                checkpoint_metric_maximum_absolute_difference=max(abs(x[k]-y[k]) for x,y in zip(result['checkpoints'],reference['checkpoints'])
                                                                 for k in ['train','val','test']),
                seconds=time.perf_counter()-started,tf32=False,cpu_threads=torch.get_num_threads())
    save('gpu_replay.json',report)
    return report


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--gpu-only',action='store_true');args=parser.parse_args()
    torch.set_num_threads(1)
    mod=load_definitions()
    if args.gpu_only:
        print(json.dumps(gpu_replay(mod),indent=2));return
    summary=dict(torch=torch.__version__,numpy=np.__version__,cpu_threads=torch.get_num_threads(),provenance=provenance())
    summary['data']=independent_data()
    summary['cpu']=cpu_oracles(mod)
    summary['results']=audit_results(mod,summary['data'])
    save('summary.json',summary)
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
