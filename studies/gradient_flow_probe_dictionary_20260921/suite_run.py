"""Frozen derivative dictionaries on the eleven-case n2048 archive suite."""
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import numpy as np
import torch

import comparison_run as inherited
from new_dictionary import build as build_low
from new_dictionary_p45 import build as build_high

ROOT, HERE = inherited.ROOT, inherited.HERE
sha, save_json = inherited.sha, inherited.save_json
METHODS = ('new_p5', 'new_p3', 'new_p1')


def hashes():
    paths = {HERE/'SUITE_PROTOCOL.md', HERE/'SUITE_MANIFEST.json'}
    for module in list(sys.modules.values()):
        value = getattr(module, '__file__', None)
        if value:
            path = Path(value).resolve()
            if path.suffix == '.py' and any(base in path.parents for base in
                    (ROOT/'code', HERE, inherited.OLD)):
                paths.add(path)
    return {str(path.relative_to(ROOT)): sha(path) for path in sorted(paths)}


def construct(initial, method):
    p = int(method[-1])
    return (build_high if p == 5 else build_low)(initial, p, block_size=256)


@torch.no_grad()
def preflight(initial, manifest, directory, device):
    checks = {}
    for method in METHODS:
        engine, state, metadata = construct(initial, method)
        assert (engine.K1, engine.K2) == {1:(2,4), 3:(6,12), 5:(14,24)}[int(method[-1])]
        assert torch.equal(state.w, initial.w) and torch.equal(state.c, initial.c)
        assert torch.allclose(state.M, engine.b2.T @ (initial.M @ engine.b1)/2048,
                              rtol=0, atol=1e-12)
        checks[method] = metadata
    for name in manifest['cases']:
        for level in ('primary', 'refined'):
            path = manifest['archive_cells'][name+'_full'][level]['arrays_path']
            other = inherited.read_initial(path, device)
            deltas = {k:float((getattr(initial,k)-getattr(other,k)).abs().max())
                      for k in ('w','c','M')}
            assert max(deltas.values()) == 0
            checks[name+'_'+level] = deltas
    save_json(directory/'validation.json', dict(passed=True, checks=checks,
                                                 source_hashes=hashes()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, default=HERE/'SUITE_MANIFEST.json')
    parser.add_argument('--device', required=True)
    parser.add_argument('--worker', type=int, choices=(0,1), default=0)
    parser.add_argument('--level', type=int, choices=(0,1,2), default=0)
    parser.add_argument('--budget', type=float, default=400)
    parser.add_argument('--cases', nargs='+')
    parser.add_argument('--only', nargs='+', choices=METHODS)
    parser.add_argument('--preflight', action='store_true')
    args = parser.parse_args()
    if not 0 < args.budget <= 400:
        parser.error('budget must be in (0,400]')
    manifest = json.loads(args.manifest.read_text())
    assert manifest['width'] == 2048 and manifest['network_seed'] == 20260920
    assert list(manifest['new_orders']) == [1,3,5] and len(manifest['cases']) == 11
    if args.cases and not set(args.cases).issubset(manifest['cases']):
        parser.error('unknown case')
    if args.level == 2 and not (args.cases and args.only):
        parser.error('extra attempts require explicit gated case/method selection')
    inherited.setup(args.device)
    start = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=not args.preflight)
    config_path = args.out/f'config_worker{args.worker}.json'
    if config_path.exists():
        raise FileExistsError(config_path)
    initial_path = Path(manifest['archive_cells']['quadrant_grouped_full']['refined']['arrays_path'])
    initial = inherited.read_initial(initial_path, args.device)
    assert initial.w.shape == (2048,2) and initial.c.shape == (2048,)
    assert initial.M.shape == (2048,2048)
    rtol, atol = 6.25e-5/4**args.level, 6.25e-7/4**args.level
    selected = args.cases or [name for index,name in enumerate(manifest['cases'])
                             if index % 2 == args.worker]
    methods = args.only or METHODS
    schedule = [name+'_'+method for method in methods for name in selected]
    config = dict(cases=manifest['cases'], assigned_cases=selected,
        execution_schedule=schedule, width=2048, network_seed=20260920,
        threshold=1e-3, methods=list(methods), orders=[int(m[-1]) for m in methods],
        device=args.device, gpu=torch.cuda.get_device_name(args.device), dtype='float64',
        rtol=rtol, atol=atol, level=args.level, worker=args.worker,
        worker_limit_seconds=args.budget, integration_worker_limit_seconds=args.budget-5,
        per_trajectory_limit_seconds=180, max_time=10000, max_steps=30000,
        initial_step=.05, max_step=2, min_step=1e-7, block_size=256,
        endpoint_nodes=8192, circle_nodes=2048,
        manifest_path=str(args.manifest.resolve()), manifest_sha256=sha(args.manifest),
        initial_archive=str(initial_path.relative_to(ROOT)), initial_archive_sha256=sha(initial_path),
        initial_array_sha256={k:hashlib.sha256(getattr(initial,k).cpu().numpy().tobytes()).hexdigest()
                              for k in ('w','c','M')},
        torch=str(torch.__version__), numpy=np.__version__, python=sys.version,
        source_hashes=hashes(), command=sys.argv, cwd=str(Path.cwd()),
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(config_path, config)
    if args.preflight:
        preflight(initial, manifest, args.out, args.device)
        seconds = time.monotonic()-start
        assert seconds <= args.budget
        save_json(args.out/'completion.json', dict(seconds=seconds, passed=True))
        print(json.dumps(dict(preflight='PASS',seconds=seconds)),flush=True)
        return
    results = {}
    for method in methods:
        if time.monotonic()-start >= args.budget-5:
            break
        engine, state, metadata = construct(initial, method)
        for name in selected:
            if time.monotonic()-start >= args.budget-5:
                break
            key = name+'_'+method
            save_json(args.out/(key+'_dictionary.json'), metadata)
            results[key] = inherited.trajectory(engine,state,manifest['cases'][name],
                args.out/key,rtol,atol,start,args.budget-5)
            results[key]['declared_executed'] = True
            save_json(args.out/f'results_worker{args.worker}.json',results)
    torch.cuda.synchronize(args.device)
    completion = dict(seconds=time.monotonic()-start,
        fitted=sum(r['status']=='fitted' for r in results.values()),total=len(results),
        expected=len(schedule), not_attempted=[k for k in schedule if k not in results],
        exit_status=0, finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(args.out/f'completion_worker{args.worker}.json',completion)
    print(json.dumps(completion),flush=True)


if __name__ == '__main__':
    main()
