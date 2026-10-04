"""Independent bounded review: raw evidence audit, independent algebra, one replay."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import zipfile

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT / 'data/generated/response_memory_use_cases_20261001'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, data):
    path.write_text(json.dumps(data, indent=2, allow_nan=False) + '\n')


def audit(out):
    frozen = json.loads((HERE / 'STAGE2_INDEX_FREEZE.json').read_text())
    assert all(sha(ROOT / p) == h for p, h in frozen.items())
    evidence = {}
    def record(path):
        evidence[str(path.relative_to(ROOT))] = sha(path)
    for path in [HERE / 'STAGE2_INDEX_FREEZE.json', *[ROOT / p for p in frozen]]:
        record(path)
    for name in ['MODEL_RECONCILIATION.md', 'INPUT_FIELD_DERIVATION.md', 'input_field.py',
                 'baseline_compact_flow.py', 'STAGE2_DATA_PROTOCOL.md', 'stage2_data.py']:
        record(HERE / name)
    for path in [ROOT / 'paper/main.tex', ROOT / 'paper/results.tex']:
        record(path)
    dataset_dir = DATA / 'stage2_data01'
    manifest = json.loads((dataset_dir / 'manifest.json').read_text())
    record(dataset_dir / 'manifest.json')
    datasets = {}
    for domain in ['fashion', 'har', 'housing']:
        path = dataset_dir / (domain + '.npz')
        record(path)
        assert sha(path) == manifest['datasets'][domain]['sha256']
        datasets[domain] = dict(np.load(path))
    for name, meta in manifest['sources'].items():
        path = dataset_dir / 'raw' / name
        record(path)
        assert sha(path) == meta['sha256']
    # Rebuild every normalized stored row directly from retained raw source rows.
    import gzip
    def idx(name):
        blob = gzip.decompress((dataset_dir / 'raw' / name).read_bytes())
        dims = blob[3]
        shape = np.frombuffer(blob, dtype='>i4', offset=4, count=dims)
        return np.frombuffer(blob, dtype=np.uint8, offset=4 + 4 * dims).reshape(tuple(shape))
    fx = {p: idx(p + '-images-idx3-ubyte.gz').reshape(-1, 784) for p in ['train', 't10k']}
    fy = {p: idx(p + '-labels-idx1-ubyte.gz') for p in ['train', 't10k']}
    with tarfile.open(dataset_dir / 'raw/cal_housing.tgz') as archive:
        housing = np.loadtxt(archive.extractfile('CaliforniaHousing/cal_housing.data'), delimiter=',')
    # Raw order: longitude, latitude, age, rooms, bedrooms, population, households, income, value.
    hx = np.column_stack([housing[:, 7], housing[:, 2], housing[:, 3] / housing[:, 6],
                          housing[:, 4] / housing[:, 6], housing[:, 5], housing[:, 5] / housing[:, 6],
                          housing[:, 1], housing[:, 0]])
    with zipfile.ZipFile(dataset_dir / 'raw/har.zip') as outer:
        names = outer.namelist()
        archive = outer if any(n.endswith('train/X_train.txt') for n in names) else zipfile.ZipFile(io.BytesIO(outer.read(next(n for n in names if n.endswith('.zip')))))
        har = {}
        for pool in ['train', 'test']:
            har[pool] = {}
            for k, suffix in [('x', f'{pool}/X_{pool}.txt'), ('y', f'{pool}/y_{pool}.txt'), ('subject', f'{pool}/subject_{pool}.txt')]:
                name = next(n for n in archive.namelist() if n.endswith(suffix))
                har[pool][k] = np.loadtxt(io.BytesIO(archive.read(name)))
        if archive is not outer:
            archive.close()
    data_checks = {}
    for domain, data in datasets.items():
        sources, labels = {}, {}
        for split in ['train', 'val', 'test']:
            ids = data['index_' + split]
            assert len(set(ids.tolist())) == len(ids)
            if domain == 'fashion':
                pool = 't10k' if split == 'test' else 'train'
                sources[split] = fx[pool][ids].astype(np.float64)
                labels[split] = np.where(fy[pool][ids] == 6, 1., -1.)
                assert np.array_equal(data['group_' + split], fy[pool][ids])
                assert set(fy[pool][ids].tolist()) == {0, 6}
            elif domain == 'housing':
                sources[split] = hx[ids]
                labels[split] = housing[ids, 8] / 100000.
            else:
                pool = 'test' if split == 'test' else 'train'
                sources[split] = har[pool]['x'][ids]
                labels[split] = np.where(har[pool]['y'][ids] <= 3, 1., -1.)
                assert np.array_equal(data['subject_' + split], har[pool]['subject'][ids])
                assert np.array_equal(data['group_' + split], har[pool]['y'][ids])
        mean = sources['train'].mean(0)
        std = np.maximum(sources['train'].std(0), 1e-3)
        assert np.array_equal(mean, data['input_mean'])
        assert np.array_equal(std, data['input_std'])
        discrepancies = []
        for split in ['train', 'val', 'test']:
            z = np.column_stack([np.clip((sources[split] - mean) / std, -5, 5), np.ones(len(sources[split]))])
            z /= np.linalg.norm(z, axis=1, keepdims=True)
            discrepancy = float(np.max(np.abs(z - data['X_' + split])))
            assert discrepancy < 1e-12
            discrepancies.append(discrepancy)
            y = labels[split]
            if domain == 'housing':
                y = np.tanh((y - labels['train'].mean()) / labels['train'].std())
            assert np.array_equal(y, data['y_' + split])
            assert np.max(np.abs(np.linalg.norm(data['X_' + split], axis=1) - 1)) < 1e-12
        assert not set(data['index_train']) & set(data['index_val'])
        if domain == 'housing':
            assert not set(data['index_train']) & set(data['index_test'])
            assert not set(data['index_val']) & set(data['index_test'])
        if domain == 'har':
            groups = [set(data['subject_' + s]) for s in ['train', 'val', 'test']]
            assert all(not groups[i] & groups[j] for i in range(3) for j in range(i))
            assert groups[1] == set(sorted(set(har['train']['subject']))[-4:])
        data_checks[domain] = dict(maximum_raw_reconstruction_error=max(discrepancies))
    batches = {}
    max_metric_error = 0.
    for stage, count in [('pilot', 21), ('confirm', 48), ('adapt', 24), ('refine', 6)]:
        folder = DATA / f'stage2_index_{stage}_v1'
        batch = json.loads((folder / 'results.json').read_text())
        batches[stage] = batch
        assert len(batch) == count
        for path in folder.glob('*'):
            if path.is_file():
                record(path)
        saved_manifest = json.loads((folder / 'manifest.json').read_text())
        for name, expected in saved_manifest['sources'].items():
            assert sha(folder / name) == expected
            assert sha(HERE / name) == expected
        for i, result in enumerate(batch):
            fit = folder / f'fit_{i:03d}'
            for path in fit.iterdir():
                record(path)
            assert json.loads((fit / 'result.json').read_text()) == result
            assert json.loads((fit / 'config.json').read_text()) == result['config']
            assert result['status'] == 'complete' and result['finite']
            data = datasets[result['config']['domain']]
            assert result['data_sha256'] == sha(dataset_dir / (result['config']['domain'] + '.npz'))
            checkpoints = result['checkpoints']
            assert [c['time'] for c in checkpoints] == [16, 32, 64, 128]
            assert result['selected_index'] == min(range(4), key=lambda k: checkpoints[k]['val'])
            assert result['selected'] == checkpoints[result['selected_index']]
            predictions = np.load(fit / 'predictions.npz')
            assert np.array_equal(predictions['target'], data['y_test'].astype(np.float32))
            assert int(predictions['selected']) == result['selected_index']
            computed = np.sqrt(np.mean((predictions['predictions'].astype(np.float64) - predictions['target'])**2, axis=1))
            error = float(np.max(np.abs(computed - [r['test'] for r in checkpoints])))
            assert error < 2e-7
            max_metric_error = max(error, max_metric_error)
            config = result['config']; n = 128; d = data['X_train'].shape[1]
            expected_moving = n * (d + 1)
            if config['kind'] == 'field':
                expected_moving += 2 * n * config['C'] * config['q'] + 1
                assert result['dictionary_scalars'] == n*d + n*config['C'] + config['C'] + (config['C']**2 if config.get('refresh') else 0)
            elif config['kind'] == 'factor': expected_moving += 2*n*24
            elif config['kind'] == 'projected': expected_moving += n*24
            else: expected_moving += n*n
            assert result['moving_scalars'] == expected_moving
    selection = json.loads((HERE / 'STAGE2_INDEX_SELECTION.json').read_text())
    for domain in datasets:
        for kind in ['field', 'factor']:
            candidates = [r for r in batches['pilot'] if r['config']['domain'] == domain and r['config']['kind'] == kind]
            assert selection[domain][kind] == min(candidates, key=lambda r: r['selected']['val'])['config']
    trigger = {d: next(r['drift']['drift'] for r in batches['pilot'] if r['config'] == selection[d]['field']) for d in datasets}
    assert sum(v > .2 for v in trigger.values()) >= 2
    summary = []
    for domain in datasets:
        candidates = [r for r in batches['confirm'] + batches['adapt'] if r['config']['domain'] == domain]
        factors = {r['config']['seed']: r['selected']['test'] for r in candidates if r['config']['kind'] == 'factor'}
        for kind in ['field', 'retro', 'write', 'factor', 'projected', 'dense']:
            runs = [r for r in candidates if r['config'].get('refresh', r['config']['kind']) == kind]
            ratios = [r['selected']['test'] / factors[r['config']['seed']] for r in runs]
            summary.append(dict(domain=domain, kind=kind, median_rmse=float(np.median([r['selected']['test'] for r in runs])),
                paired_ratio=float(np.median(ratios)), wins=sum(x < 1 for x in ratios), times=[r['selected']['time'] for r in runs]))
    refinements = []
    for r in batches['refine']:
        c = r['config']
        base = next(v for v in batches['confirm'] if all(v['config'][k] == c[k] for k in ['domain', 'seed', 'kind']))
        pair = [v for v in batches['confirm'] if v['config']['domain'] == c['domain'] and v['config']['seed'] == 201 and v['config']['kind'] in ['field', 'factor']]
        gap = abs(pair[0]['selected']['test'] - pair[1]['selected']['test'])
        change = abs(r['selected']['test'] - base['selected']['test'])
        label_rms = float(np.sqrt(np.mean(datasets[c['domain']]['y_test']**2)))
        assert change < .01*label_rms and change < gap/3
        refinements.append(dict(domain=c['domain'], kind=c['kind'], change=change, gap=gap, label_rms=label_rms))
    oracle = []
    for folder_name in ['stage2_index_oracle_v1', 'stage2_index_analysis_v1', 'stage2_index_checks_v1', 'stage2_index_data_checks_v1']:
        for path in (DATA / folder_name).iterdir():
            if path.is_file(): record(path)
    for result in json.loads((DATA / 'stage2_index_oracle_v1/results.json').read_text()):
        domain = result['domain']; saved = np.load(DATA / 'stage2_index_oracle_v1' / (domain + '.npz'))
        assert result['source_data_sha256'] == sha(dataset_dir / (domain + '.npz'))
        for label in ['original', 'overlap', 'oracle']:
            for split in ['train', 'val', 'test']:
                err = float(np.sqrt(np.mean((saved[label + '_' + split] - datasets[domain]['y_' + split])**2)))
                assert abs(err - result['target_rmse'][label][split]) < 1e-14
        for pair, values in result['prediction_rms'].items():
            first, second = pair.split('_vs_')
            for split in ['train', 'val', 'test']:
                err = float(np.sqrt(np.mean((saved[first + '_' + split] - saved[second + '_' + split])**2)))
                assert abs(err - values[split]) < 1e-14
        oracle.append(dict(domain=domain, prediction_rms=result['prediction_rms'], target_rmse=result['target_rmse']))
    dump(out / 'source_evidence_hashes.json', evidence)
    dump(out / 'audit.json', dict(status='pass', fits=99, data=data_checks, max_recomputed_metric_error=max_metric_error,
        drift_trigger=trigger, rows=summary, refinements=refinements, oracle=oracle,
        fit_seconds=sum(r['seconds'] for rows in batches.values() for r in rows)))


def algebra(out):
    # Independent numerical calculations, using no author check functions.
    rng = np.random.default_rng(202610021)
    m,n,c,order = 41,9,4,3
    h = rng.normal(size=(n,m)); b = rng.normal(size=(n,m))
    values, v = np.linalg.eigh(h@h.T/m); v=v[:,-c:]; values=values[-c:]
    psi=h.T@v/np.sqrt(values)
    errors = {'instantaneous_projected_gradient': float(np.max(np.abs((b@psi/m)@(h@psi/m).T - (b@h.T/m)@v@v.T)))}
    old, _ = np.linalg.qr(rng.normal(size=(m,c)))
    new, _ = np.linalg.qr(rng.normal(size=(m,c)))
    unseen = new[:,0]-old@(old.T@new[:,0])
    errors['obstruction_old_coefficients'] = float(np.max(np.abs(old.T@unseen)))
    errors['obstruction_new_coefficient_identity'] = float(abs(unseen@new[:,0] - unseen@unseen))
    assert unseen@new[:,0] > .1
    # Quadrature tests independently use a moving input span, not only rotations.
    nodes, weights=np.polynomial.legendre.leggauss(120)
    tau=3.; xi=(nodes+1)*tau/2; weights=weights*tau/2
    input_modes,_=np.linalg.qr(rng.normal(size=(m,2*c))); input_modes*=np.sqrt(m)
    histories_h=[]; histories_b=[]; functions=[]
    for t in xi:
        ang=.7*t
        basis=np.cos(ang)*input_modes[:,:c]+np.sin(ang)*input_modes[:,c:]
        poly=np.polynomial.legendre.legvander(2*t/tau-1,order-1).ravel()
        functions.append(np.einsum('mc,j->mcj',basis,poly).reshape(m,-1))
        histories_h.append(rng.normal(size=(m,3)))
        histories_b.append(rng.normal(size=(m,2)))
    u=np.asarray(functions); hh=np.asarray(histories_h); bb=np.asarray(histories_b)
    mass=weights[:,None]/m
    norm=np.tile(tau/(2*np.arange(order)+1),c)
    gram=np.einsum('tmk,tml,tm->kl',u,u,np.broadcast_to(mass,(len(xi),m)))
    errors['moving_span_joint_orthogonality']=float(np.max(np.abs(gram-np.diag(norm))))
    hc=np.einsum('tmi,tmk,tm->ik',hh,u,np.broadcast_to(mass,(len(xi),m)))
    bc=np.einsum('tmi,tmk,tm->ik',bb,u,np.broadcast_to(mass,(len(xi),m)))
    hp=np.einsum('ik,tmk->tmi',hc/norm,u);bp=np.einsum('ik,tmk->tmi',bc/norm,u)
    integral=lambda a,b: np.einsum('tmi,tmj,tm->ij',a,b,np.broadcast_to(mass,(len(xi),m)))
    tail=integral(bb-bp,hh-hp)
    errors['moving_span_product_tail']=float(np.max(np.abs(integral(bb,hh)-(bc/norm)@hc.T-tail)))
    bound=np.sqrt(np.sum((bb-bp)**2*mass[:,:,None]))*np.sqrt(np.sum((hh-hp)**2*mass[:,:,None]))
    assert np.linalg.norm(tail) <= bound
    # Gauge counterexample including the required zero-backward unit prefix.
    angle=2*np.pi*xi/tau
    forward=np.array([weights@np.cos(angle),weights@np.sin(angle)])
    backward=np.array([weights@((xi>1)*np.cos(angle)),weights@((xi>1)*np.sin(angle))])
    errors['prefix_compatible_gauge_forward_zero']=float(np.max(np.abs(forward)))
    errors['prefix_compatible_gauge_reconstruction_zero']=float(abs(backward@forward/tau))
    # Exact unprojected interaction here is tau-1=2, despite near-zero reconstruction.
    assert max(errors.values()) < 1e-10
    dump(out/'algebra.json',dict(status='pass',errors=errors,prefix_compatible_exact_interaction=tau-1,
        prefix_compatible_backward_moment_norm=float(np.linalg.norm(backward)),tail_frobenius=float(np.linalg.norm(tail)),tail_bound=float(bound)))


def replay(out):
    import stage2_index_experiment as experiment
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    torch.cuda.set_device(0)
    path=DATA/'stage2_index_confirm_v1/fit_000'
    config=json.loads((path/'config.json').read_text())
    assert config == dict(kind='field',C=8,q=3,seed=201,domain='fashion')
    folder=out/'fashion_seed201_replay';folder.mkdir()
    dump(folder/'config.json',config)
    made=[];original_make=experiment.make
    def capture(*args,**kwargs):
        model=original_make(*args,**kwargs);made.append(model);return model
    experiment.make=capture
    result=experiment.fit(config,DATA/'stage2_data01/fashion.npz',folder,'cuda:0')
    expected=json.loads((path/'result.json').read_text())
    a=np.load(folder/'predictions.npz')['predictions'];b=np.load(path/'predictions.npz')['predictions']
    discrepancy=float(np.max(np.abs(a-b)))
    assert discrepancy < 2e-5 and result['selected_index']==expected['selected_index']
    model=made[0]
    initial_error=float((model.basis.T@model.basis/model.M-torch.eye(model.C,device='cuda:0')).abs().max())
    experiment.refresh_info(model,'write')
    refreshed_error=float((model.basis.T@model.basis/model.M-torch.eye(model.C,device='cuda:0')).abs().max())
    evaluated=torch.tanh(model.dictionary_first@model.inputs.T).T@model.dictionary_vectors/model.dictionary_values.sqrt()
    evaluated=evaluated@model.dictionary_rotation
    evaluation_error=float((evaluated-model.basis).abs().max())
    assert initial_error < 1e-5 and refreshed_error < 1e-5 and evaluation_error < 1e-5
    dump(out/'replay.json',dict(status='pass',config=config,maximum_prediction_absolute_error=discrepancy,
        selected_test=result['selected']['test'],selected_time=result['selected']['time'],seconds=result['seconds'],
        initial_float32_gram_error=initial_error,refreshed_float32_gram_error=refreshed_error,
        refreshed_evaluable_basis_error=evaluation_error,torch=torch.__version__,numpy=np.__version__,
        device=torch.cuda.get_device_name(),threads=1,tf32=False,command=sys.argv,
        source_sha256=sha(__file__),input_config_sha256=sha(path/'config.json')))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);parser.add_argument('--replay',action='store_true')
    args=parser.parse_args()
    if args.replay:
        assert args.out.exists()
        replay(args.out)
    else:
        args.out.mkdir(parents=True,exist_ok=False)
        audit(args.out);algebra(args.out)
    print('PASS',args.out)
