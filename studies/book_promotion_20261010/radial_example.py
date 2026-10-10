"""Two tiny experiments for the offline multi-experiment radial explorer."""
import argparse
import hashlib
import json
from pathlib import Path

import torch

from compression_core import Dense, Legendre, harmonic, taylor, rollout
from data_core import toy_data
from radial_explorer import make_case, write_explorer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='new output directory')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    times = [0., .02, .04]
    cases = []
    for count, seed in ((3, 47), (4, 48)):
        data = toy_data(dimension=2, train_samples=count, query_samples=96,
                        seed=seed, label_scale=.1)
        x, y, q = [torch.as_tensor(a, dtype=torch.float64) for a in
                   (data.train_inputs, data.train_labels, data.query_inputs)]
        queries = torch.cat([q, x])
        dense = Dense(64, 2, depth=2, seed=17)
        models = [
            ('dense32', Dense(32, 2, depth=2, seed=17), dict(kind='network', width=32, seed=17)),
            ('dense64', dense, dict(kind='network', width=64, seed=17)),
            ('dense64-seed18', Dense(64, 2, depth=2, seed=18), dict(kind='network', width=64, seed=18)),
            ('legendre', Legendre(dense, x, y, order=3), {}),
            ('harmonic', harmonic(dense, x, y, horizon=.04, step_size=.01,
                                  rank=1, time_degree=2, spatial_degree=2, budget=48), {}),
            ('taylor', taylor(dense, x, y, queries, source_mode='jets', rank=1, budget=48), {}),
        ]
        records = []
        for name, model, metadata in models:
            _, predictions = rollout(model, x, y, times, step_size=.01, queries=queries)
            records.append(dict(id=name, name=name, times=times,
                                curves=predictions[:, :len(q)].numpy(),
                                trainPredictions=predictions[:, len(q):].numpy(),
                                settled=False, provenance=model.provenance, **metadata))
        case = make_case(f'toy-{count}', f'Toy circle: {count} training inputs',
                         data.query_inputs, data.train_inputs, data.train_labels, records,
                         train_ids=data.train_ids, query_ids=data.query_ids, provenance=data.provenance)
        case['notes'] = ('Short operational example, not a fitted endpoint or accuracy study. '
                         'Compression models share the width-64 seed-17 Dense initialization; '
                         'other Dense variants demonstrate the selectors only.')
        cases.append(case)
        (args.out/f'toy-{count}.json').write_text(json.dumps(case, allow_nan=False)+'\n')
    bundle = dict(cases=cases, defaultCase=cases[0]['id'])
    (args.out/'experiments.json').write_text(json.dumps(bundle, allow_nan=False)+'\n')
    write_explorer(args.out/'explorer.html', bundle)
    write_explorer(args.out/'empty_explorer.html', {'cases': []})
    sources = [Path(__file__), *[Path(__file__).with_name(n) for n in
               ('compression_core.py', 'data_core.py', 'radial_explorer.py', 'radial_explorer.html')]]
    manifest = dict(purpose='Operational multi-experiment viewer check; no scientific campaign',
                    settings=dict(times=times, step_size=.01, depth=2, label_scale=.1, queries=96),
                    source_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
                    outputs={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in args.out.iterdir()})
    (args.out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(args.out/'explorer.html')


if __name__ == '__main__':
    main()
