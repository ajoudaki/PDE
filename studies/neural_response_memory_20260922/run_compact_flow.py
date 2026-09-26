"""Configurable MLP/compression experiments and dataset preparation.

Run --config experiment_configs.json --experiment circle_baselines --out FRESH.
Use --prepare-only to export data, or --summarize RUN to rescore saved predictions.
Legacy --data NPZ ... and model/solver flags remain supported.
"""
import argparse
import csv
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import struct
import subprocess
import sys
import time
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
import torch
from compact_flow import Flow, FrozenFlow
from frozen_dictionary import OLD_RANKS

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MODEL = dict(width=2048, depth=3, activation='relu', seed=20260920,
             hidden_gain=1., readout_std=None, dtype='float32')
OPTIMIZER = dict(step=.0625, target_rms=.05, max_seconds=60., max_steps=60000, block=8)
KINDS = ('dense', 'closure', 'dictionary_old', 'dictionary_flow', 'gaussian', 'orthogonal')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rms(value):
    value = float(np.sqrt(np.mean(np.asarray(value, dtype=np.float64)**2)))
    return value if np.isfinite(value) else None


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def data_path(value, base):
    path = Path(value)
    return path if path.is_absolute() else base/path


def load_npz(path):
    with np.load(path, allow_pickle=False) as d: arrays = {k: d[k].copy() for k in d.files}
    for old, new in [('train_inputs', 'inputs'), ('train_labels', 'labels'),
                     ('validation_inputs', 'test_inputs'), ('validation_labels', 'test_labels')]:
        if new not in arrays and old in arrays: arrays[new] = arrays.pop(old)
    return arrays


def mnist_data(spec, base):
    """Official cached IDX files; balanced seeded train selection, separate test split."""
    root = data_path(spec['cache'], base)
    arrays, hashes = [], {}
    for filename, magic in [('train-images-idx3-ubyte', 2051), ('train-labels-idx1-ubyte', 2049),
                            ('t10k-images-idx3-ubyte', 2051), ('t10k-labels-idx1-ubyte', 2049)]:
        paths = [folder/(filename+suffix) for folder in (root, root/'MNIST/raw', root/'raw') for suffix in ('', '.gz')]
        path = next((p for p in paths if p.is_file()), None)
        if path is None: raise FileNotFoundError(f'MNIST cache lacks {filename}: {root}')
        payload = gzip.open(path, 'rb').read() if path.suffix == '.gz' else path.read_bytes()
        got, count = struct.unpack('>II', payload[:8])
        if got != magic: raise ValueError(f'Incorrect IDX format: {path}')
        shape = (count, *struct.unpack('>II', payload[8:16])) if magic == 2051 else (count,)
        arrays.append(np.frombuffer(payload, dtype=np.uint8, offset=16 if magic == 2051 else 8).reshape(shape))
        hashes[str(path.resolve())] = sha(path)
    train, train_digits, test, test_digits = arrays
    digits = spec.get('digits', [3, 8])
    if len(digits) != 2 or len(set(digits)) != 2 or any(d not in range(10) for d in digits):
        raise ValueError('Scalar-output MNIST uses two distinct digits')
    rng = np.random.default_rng(spec.get('seed', 20260924))
    count = spec.get('samples_per_class', 50)
    if not isinstance(count, int) or count < 1: raise ValueError('Positive samples_per_class required')
    ids = np.concatenate([rng.choice(np.flatnonzero(train_digits == d), count, replace=False) for d in digits])
    rng.shuffle(ids)
    test_ids = np.flatnonzero(np.isin(test_digits, digits))
    if 'test_per_class' in spec:
        count_test = spec['test_per_class']
        if not isinstance(count_test, int) or count_test < 1: raise ValueError('Positive test_per_class required')
        test_ids = np.concatenate([rng.choice(np.flatnonzero(test_digits == d), count_test, replace=False) for d in digits])
    def scale(images, indices):
        x = images[indices].reshape(len(indices), -1).astype(np.float64)
        if spec.get('normalization', 'l2') == 'l2':
            norms = np.linalg.norm(x, axis=1, keepdims=True)
            if np.any(norms == 0): raise ValueError('Cannot normalize zero image')
            return x/norms
        if spec['normalization'] == 'pixels': return x/255.
        raise ValueError('MNIST normalization must be l2 or pixels')
    return dict(inputs=scale(train, ids), labels=np.where(train_digits[ids] == digits[0], -1., 1.),
                test_inputs=scale(test, test_ids), test_labels=np.where(test_digits[test_ids] == digits[0], -1., 1.),
                train_ids=ids, test_ids=test_ids), hashes


def dataset(spec, base=HERE):
    kind = spec['kind']; hashes = {}
    fields = dict(npz={'path'}, mnist={'cache', 'digits', 'seed', 'samples_per_class', 'test_per_class', 'normalization'},
                  circle={'queries', 'query_offset', 'case', 'span_degrees', 'start_degrees', 'angles_degrees', 'labels', 'samples', 'frequency', 'phase', 'region_span_degrees'},
                  sphere={'samples', 'queries', 'seed', 'z_min', 'sampling', 'target', 'frequency', 'region_z_min'})
    if kind not in fields or set(spec)-fields[kind]-{'kind', 'name'}: raise ValueError('Unknown dataset kind/setting')
    if kind == 'npz':
        path = data_path(spec['path'], base); data = load_npz(path); hashes[str(path.resolve())] = sha(path)
    elif kind == 'mnist': data, hashes = mnist_data(spec, base)
    elif kind == 'circle':
        q = spec.get('queries', 8192)
        if not isinstance(q, int) or q < 1: raise ValueError('Positive queries required')
        query_angle = (np.arange(q)+spec.get('query_offset', .5))*2*np.pi/q
        if 'case' in spec and any(k in spec for k in ('angles_degrees', 'labels', 'samples', 'frequency', 'phase', 'span_degrees', 'start_degrees')):
            raise ValueError('A named circle case supplies its own training points and labels')
        if 'angles_degrees' in spec and 'samples' in spec: raise ValueError('Use literal angles or a sample count')
        literal = spec
        if 'case' in spec:
            cases = {}
            for filename in ('activation_circle_cases.json', 'compact_extra_circle_cases.json'):
                path = HERE/filename; hashes[str(path)] = sha(path)
                for key, value in json.loads(path.read_text()).items():
                    name = key.split('__')[-1]
                    selected = {k: value[k] for k in ('angles_degrees', 'labels')}
                    if name in cases and cases[name] != selected: raise ValueError('Ambiguous legacy circle case')
                    cases[name] = selected
            literal = cases[spec['case']]
        span = np.deg2rad(spec.get('span_degrees', 360.)); start = np.deg2rad(spec.get('start_degrees', 0.))
        if not 0 < span <= 2*np.pi: raise ValueError('Circle span must lie in (0,360]')
        if 'angles_degrees' in literal: angle = np.deg2rad(literal['angles_degrees'])
        else:
            m = spec.get('samples', 64)
            if not isinstance(m, int) or m < 1: raise ValueError('Positive samples required')
            angle = start+(np.arange(m)+.5)*span/m
        points = lambda a: np.column_stack((np.cos(a), np.sin(a)))
        target = lambda a: np.sqrt(2)*np.sin(spec.get('frequency', 24)*a+spec.get('phase', 0.))
        data = dict(inputs=points(angle), labels=np.asarray(literal['labels'], dtype=float) if 'labels' in literal else target(angle),
                    test_inputs=points(query_angle), region=(query_angle-start) % (2*np.pi) < np.deg2rad(spec.get('region_span_degrees', 90.)))
        if 'labels' not in literal: data['test_labels'] = target(query_angle)
    elif kind == 'sphere':
        m, q = spec.get('samples', 64), spec.get('queries', 8192)
        if any(not isinstance(v, int) or v < 1 for v in (m, q)): raise ValueError('Positive sample/query counts required')
        rng = np.random.default_rng(spec.get('seed', 20260926)); z_min = spec.get('z_min', -1.)
        if not -1 <= z_min < 1: raise ValueError('Sphere z_min must lie in [-1,1)')
        make = lambda z, a: np.column_stack((np.sqrt(1-z*z)*np.cos(a), np.sqrt(1-z*z)*np.sin(a), z))
        sampling = spec.get('sampling', 'uniform_z')
        if sampling not in ('normal', 'uniform_z'): raise ValueError('Unknown sphere sampling')
        if sampling == 'normal':
            if z_min != -1: raise ValueError('Normal-direction sampling uses the whole sphere')
            x = rng.standard_normal((m, 3)); x /= np.linalg.norm(x, axis=1, keepdims=True)
        else:
            u, v = rng.random((2, m)); x = make(z_min+(1-z_min)*u, 2*np.pi*v)
        i = np.arange(q); query = make(1-2*(i+.5)/q, i*np.pi*(3-np.sqrt(5)))
        name = spec.get('target', 'oscillatory')
        if name == 'xy': target = lambda a: np.sqrt(15)*a[:, 0]*a[:, 1]
        elif name == 'xyz': target = lambda a: np.sqrt(105)*np.prod(a, axis=1)
        elif name == 'oscillatory': target = lambda a: np.sin(spec.get('frequency', 6)*np.pi*a[:, 0])*np.sin(spec.get('frequency', 6)*np.pi*a[:, 1])
        else: raise ValueError('Unknown sphere target: '+name)
        truth, y = target(query), target(x)
        if name == 'oscillatory':
            scale = np.sqrt(np.mean(truth**2))
            if scale == 0: raise ValueError('Zero sphere target scale')
            truth, y = truth/scale, y/scale
        data = dict(inputs=x, labels=y, test_inputs=query, test_labels=truth, region=query[:, 2] >= spec.get('region_z_min', .5))
    else: raise ValueError('Unknown dataset kind: '+kind)
    x, y, query = (data[k] for k in ('inputs', 'labels', 'test_inputs'))
    if x.ndim != 2 or min(x.shape) < 1 or y.shape != (len(x),) or query.ndim != 2 or len(query) < 1 or query.shape[1] != x.shape[1]:
        raise ValueError('Expected nonempty inputs (M,d), labels (M,), test_inputs (Q,d)')
    if not all(np.isfinite(a).all() for a in (x, y, query)): raise ValueError('Nonfinite dataset')
    if 'test_labels' in data and (data['test_labels'].shape != (len(query),) or not np.isfinite(data['test_labels']).all()):
        raise ValueError('Invalid test labels')
    if 'region' in data and (data['region'].shape != (len(query),) or data['region'].dtype != bool): raise ValueError('Invalid query region mask')
    return data, hashes


def resolve(raw):
    unknown = set(raw)-{'model', 'optimizer', 'methods', 'datasets', 'device'}
    if unknown: raise ValueError('Unknown experiment fields: '+str(sorted(unknown)))
    for key, defaults in [('model', MODEL), ('optimizer', OPTIMIZER)]:
        if set(raw.get(key, {}))-set(defaults): raise ValueError('Unknown '+key+' setting')
    config = dict(model={**MODEL, **raw.get('model', {})}, optimizer={**OPTIMIZER, **raw.get('optimizer', {})},
                  methods=raw.get('methods', [{'kind': 'dense'}, *[dict(kind='closure', order=p) for p in (1, 2, 3)]]),
                  datasets=raw['datasets'], device=raw.get('device', 'cuda:0'))
    names = []
    for method in config['methods']:
        if set(method)-{'kind', 'order', 'ranks', 'basis_seed', 'id'}: raise ValueError('Unknown method setting')
        kind = method['kind']
        if kind not in KINDS: raise ValueError('Unknown method: '+kind)
        if kind == 'dense' and set(method)-{'kind', 'id'}: raise ValueError('Dense accepts only kind/id')
        if kind == 'closure' and set(method)-{'kind', 'order', 'id'}: raise ValueError('Closure accepts kind/order/id')
        if kind in ('dictionary_old', 'dictionary_flow') and set(method)-{'kind', 'order', 'id'}: raise ValueError('Historical dictionaries accept kind/order/id')
        order = method.get('order', 1)
        if isinstance(order, bool) or not isinstance(order, int) or order < 1: raise ValueError('Positive integer order required')
        if kind == 'dictionary_old' and order not in OLD_RANKS: raise ValueError('Old dictionary orders: '+str(list(OLD_RANKS)))
        if kind == 'dictionary_flow' and order > 7: raise ValueError('Gradient-flow dictionary orders: 1..7')
        if kind in ('gaussian', 'orthogonal'):
            seed = method.get('basis_seed', 7319)
            if isinstance(seed, bool) or not isinstance(seed, int) or not 0 <= seed <= 2**64-2-100000: raise ValueError('Invalid basis_seed')
            if 'ranks' in method:
                if 'order' in method: raise ValueError('Random bases use ranks or historical order, not both')
                ranks = [method['ranks']]*config['model']['depth'] if isinstance(method['ranks'], int) else method['ranks']
                if len(ranks) != config['model']['depth'] or any(isinstance(r, bool) or not isinstance(r, int) or r < 1 for r in ranks): raise ValueError('One positive rank per hidden layer required')
                if kind == 'orthogonal' and max(ranks) > config['model']['width']: raise ValueError('Orthogonal rank exceeds width')
            elif config['model']['depth'] != 2 or order not in OLD_RANKS: raise ValueError('Supply random ranks outside historical depth-two orders')
            elif kind == 'orthogonal' and max(OLD_RANKS[order]) > config['model']['width']: raise ValueError('Orthogonal rank exceeds width')
        names.append(method.get('id', 'dense' if kind == 'dense' else f'{kind}_P{order}'))
    if not names or len(set(names)) != len(names): raise ValueError('Use distinct nonempty method IDs')
    if sum(m['kind'] == 'dense' for m in config['methods']) > 1: raise ValueError('Use one dense reference per experiment')
    data_names = [s['name'] for s in config['datasets']]
    if not data_names or len(set(data_names)) != len(data_names): raise ValueError('Use distinct nonempty dataset names')
    for name in [*names, *data_names]:
        if not isinstance(name, str) or not name or Path(name).name != name or name in ('.', '..'): raise ValueError('Names must be simple path components')
    if config['model']['dtype'] not in ('float32', 'float64'): raise ValueError('dtype must be float32 or float64')
    m, o = config['model'], config['optimizer']
    if isinstance(m['seed'], bool) or not isinstance(m['seed'], int) or m['seed'] < 0: raise ValueError('Use a nonnegative integer model seed')
    for key, value in [('width', m['width']), ('depth', m['depth']), ('max_steps', o['max_steps']), ('block', o['block'])]:
        if isinstance(value, bool) or not isinstance(value, int) or value < 1: raise ValueError('Positive integer '+key+' required')
    for key in ('step', 'target_rms', 'max_seconds'):
        if not math.isfinite(o[key]) or o[key] <= 0: raise ValueError('Positive finite '+key+' required')
    activations = m['activation'] if isinstance(m['activation'], list) else [m['activation']]*m['depth']
    if len(activations) != m['depth'] or any(v not in ('relu', 'gelu', 'selu', 'tanh', 'sigmoid', 'silu') for v in activations): raise ValueError('Use a supported activation or one per hidden layer')
    if m['hidden_gain'] != 'unit_moment' and (not math.isfinite(m['hidden_gain']) or m['hidden_gain'] <= 0): raise ValueError('Invalid hidden_gain')
    if m['readout_std'] is not None and (not math.isfinite(m['readout_std']) or m['readout_std'] <= 0): raise ValueError('Invalid readout_std')
    return config


def construct(config, method, data):
    model = dict(config['model']); model['dtype'] = getattr(torch, model['dtype'])
    kind = method['kind']; order = method.get('order', 1)
    args = (data['inputs'], data['labels'])
    if kind in ('dense', 'closure'):
        return Flow(*args, **model, order=None if kind == 'dense' else order, device=config['device'], normalization='none')
    return FrozenFlow(*args, **model, kind=kind, order=order, ranks=method.get('ranks'),
                      basis_seed=method.get('basis_seed', 7319), device=config['device'], normalization='none')


def summarize(root):
    rows = []
    for folder in sorted(p.parent for p in root.glob('*/data.npz')):
        data = load_npz(folder/'data.npz'); records = []
        for path in sorted(folder.glob('*.json')):
            if path.name == 'provenance.json': continue
            r = json.loads(path.read_text()); file = folder/(r['model']+'.npz')
            if sha(file) != r['predictions_sha256'] or sha(folder/'data.npz') != r['data_sha256']: raise ValueError('Changed prediction/data archive')
            with np.load(file) as d: records.append((r, d['prediction'].copy(), d['test_prediction'].copy()))
        reference = next((v for v in records if v[0]['method']['kind'] == 'dense'), None)
        for r, train, query in records:
            if reference is not None and r['config'] != reference[0]['config']: raise ValueError('Mismatched dense configuration')
            train_rms = rms(train-data['labels']); dense_rms = rms(reference[1]-data['labels']) if reference else None
            rows.append(dict(dataset=folder.name, model=r['model'], train_rms=train_rms, dense_train_rms=dense_rms,
                             test_rms_vs_dense=rms(query-reference[2]) if reference else None,
                             test_rms_vs_target=rms(query-data['test_labels']) if 'test_labels' in data else None,
                             fitted_pair=all(v is not None and v <= r['config']['optimizer']['target_rms'] for v in (train_rms, dense_rms)),
                             status=r['fit']['status'], seconds=r['total_seconds']))
            for label, mask in [('region', data.get('region')), ('outside', ~data['region'] if 'region' in data else None)]:
                rows[-1][label+'_rms_vs_dense'] = rms((query-reference[2])[mask]) if reference and mask is not None and mask.any() else None
    if not rows: raise ValueError('No model records to summarize')
    with (root/'rms.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    print('| Dataset | Model | Train RMS | Test RMS vs dense | Both fitted |')
    print('|---|---|---:|---:|---|')
    fmt = lambda v: '—' if v is None else f'{v:.6f}'
    for r in rows: print(f"| {r['dataset']} | {r['model']} | {fmt(r['train_rms'])} | {fmt(r['test_rms_vs_dense'])} | {r['fitted_pair']} |")
    return rows


def run(config, out, base, prepare_only=False):
    torch.set_num_threads(1); torch.backends.cuda.matmul.allow_tf32 = False
    if torch.device(config['device']).type == 'cuda' and not prepare_only: torch.cuda.set_device(config['device'])
    prepared = [(spec, *dataset(spec, base)) for spec in config['datasets']]
    # Reject unsupported historical formulas before spending time on any model.
    for spec, data, _ in prepared:
        for method in config['methods']:
            if method['kind'] in ('dictionary_old', 'dictionary_flow'):
                m = config['model']
                if (m['depth'] != 2 or data['inputs'].shape[1] != 2 or m['activation'] != 'tanh'
                        or m['hidden_gain'] != 1 or m['readout_std'] not in (None, 1/m['width'])):
                    raise ValueError(f"{method['kind']} requires 2D/two hidden tanh layers and historical initialization; dataset {spec['name']}")
    out.mkdir(parents=True, exist_ok=False)
    source_paths = [HERE/n for n in ('compact_flow.py', 'frozen_dictionary.py', 'run_compact_flow.py')]
    source_paths += [ROOT/'code/pde'/n for n in ('observable_initialization.py', 'observable_words.py')]
    head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True)
    write_json(out/'config.json', dict(config=config, command=shlex.join([sys.executable, *sys.argv]),
               git_head=head.stdout.strip() if head.returncode == 0 else None, cwd=os.getcwd(),
               source_sha256={str(p): sha(p) for p in source_paths}, torch=torch.__version__, numpy=np.__version__,
               gpu=torch.cuda.get_device_name(config['device']) if not prepare_only and torch.device(config['device']).type == 'cuda' else None,
               threads=torch.get_num_threads(), tf32=False))
    for spec, data, hashes in prepared:
        folder = out/spec['name']; folder.mkdir(); np.savez(folder/'data.npz', **data)
        write_json(folder/'provenance.json', dict(dataset=spec, source_sha256=hashes))
        if prepare_only: continue
        dense = None
        for method in sorted(config['methods'], key=lambda m: m['kind'] != 'dense'):
            started = time.perf_counter(); kind = method['kind']; order = method.get('order', 1)
            name = method.get('id', 'dense' if kind == 'dense' else f'{kind}_P{order}')
            model = construct(config, method, data); fit = model.fit(**config['optimizer'])
            if not np.isfinite(fit['rms']): fit['rms'] = None
            prediction = model.predict(data['inputs']).cpu().numpy().astype(np.float64)
            query = data['test_inputs']
            curve = np.concatenate([model.predict(query[i:i+512]).cpu().numpy() for i in range(0, len(query), 512)]).astype(np.float64)
            if kind == 'dense': dense = curve.copy()
            file = folder/(name+'.npz'); np.savez(file, prediction=prediction, test_prediction=curve)
            record = dict(model=name, method=method, config=config, fit=fit, train_rms=rms(prediction-data['labels']),
                          test_rms_vs_dense=rms(curve-dense) if dense is not None else None,
                          test_rms_vs_target=rms(curve-data['test_labels']) if 'test_labels' in data else None,
                          basis_ranks=[b.shape[1] for b in model.bases] if isinstance(model, FrozenFlow) else None,
                          data_sha256=sha(folder/'data.npz'), predictions_sha256=sha(file), total_seconds=time.perf_counter()-started)
            write_json(folder/(name+'.json'), record)
            print(json.dumps(dict(dataset=spec['name'], model=name, train_rms=record['train_rms'], seconds=record['total_seconds'])), flush=True)
            del model
    if not prepare_only: summarize(out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config', type=Path); p.add_argument('--experiment', nargs='+')
    p.add_argument('--out', type=Path); p.add_argument('--device'); p.add_argument('--prepare-only', action='store_true')
    p.add_argument('--summarize', type=Path); p.add_argument('--data', type=Path, nargs='+')
    for name, kind in [('width', int), ('depth', int), ('activation', str), ('seed', int), ('hidden-gain', str), ('readout-std', float)]:
        p.add_argument('--'+name, type=kind)
    for name, kind in [('step', float), ('target-rms', float), ('seconds', float), ('max-steps', int)]: p.add_argument('--'+name, type=kind)
    p.add_argument('--orders', type=int, nargs='+')
    a = p.parse_args()
    if a.summarize is not None: summarize(a.summarize); return
    if a.out is None: p.error('--out is required')
    if a.config:
        if a.data or a.orders or any(getattr(a, k) is not None for k in ('width', 'depth', 'activation', 'seed', 'hidden_gain', 'readout_std', 'step', 'target_rms', 'seconds', 'max_steps')):
            p.error('With --config, put model/solver/data settings in the config')
        raw = json.loads(a.config.read_text()); base = a.config.resolve().parent
        if 'experiments' in raw:
            if set(raw) != {'experiments'}: p.error('Unknown catalog fields')
            if not a.experiment: p.error('Select catalog entries explicitly with --experiment NAME ...')
            selected = a.experiment
            if len(set(selected)) != len(selected) or any(not n or Path(n).name != n or n in ('.', '..') for n in selected): p.error('Use distinct simple experiment names')
            jobs = [(a.out/name, raw['experiments'][name]) for name in selected]
        else:
            if a.experiment: p.error('--experiment requires an experiments catalog')
            jobs = [(a.out, raw)]
    else:
        if a.experiment: p.error('--experiment requires --config')
        if not a.data: p.error('Supply --config or --data')
        model = {k: getattr(a, k) for k in MODEL if hasattr(a, k) and getattr(a, k) is not None}
        if 'hidden_gain' in model and model['hidden_gain'] != 'unit_moment': model['hidden_gain'] = float(model['hidden_gain'])
        optimizer = {k: getattr(a, k) for k in ('step', 'target_rms', 'max_steps') if getattr(a, k) is not None}
        if a.seconds is not None: optimizer['max_seconds'] = a.seconds
        methods = [dict(kind='dense') if k == 0 else dict(kind='closure', order=k, id=f'P{k}') for k in (a.orders or [0, 1, 2, 3])]
        jobs = [(a.out, dict(model=model, optimizer=optimizer, methods=methods,
                 datasets=[dict(name=v.stem, kind='npz', path=str(v.resolve())) for v in a.data]))]; base = Path.cwd()
    configs = [(out, resolve(raw)) for out, raw in jobs]
    for out, config in configs:
        if a.device: config['device'] = a.device
        run(config, out, base, a.prepare_only)


if __name__ == '__main__': main()
