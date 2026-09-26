"""Bounded p4/p5 extension; original trajectory producer is unchanged."""
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
from new_dictionary_p45 import build, raw_features
from new_dictionary import raw_features as previous_raw

ROOT, HERE, ARCHIVE = inherited.ROOT, inherited.HERE, inherited.ARCHIVE
CASES, METHODS = inherited.CASES, ('new_p4', 'new_p5')
sha, save_json = inherited.sha, inherited.save_json


def hashes():
    paths = {HERE/'P45_PROTOCOL.md', HERE/'P45_DERIVATION_ROUTE.md',
             HERE/'P45_ALGEBRA_CHECK.md', HERE/'P45_IMPLEMENTATION_CHECK.md'}
    for module in list(sys.modules.values()):
        value = getattr(module, '__file__', None)
        if value:
            path = Path(value).resolve()
            if path.suffix == '.py' and any(base in path.parents for base in
                        (ROOT/'code', HERE, inherited.OLD)):
                paths.add(path)
    return {str(path.relative_to(ROOT)): sha(path) for path in sorted(paths)}


@torch.no_grad()
def preflight(initial, directory, device):
    checks = {}
    old = previous_raw(initial, 3)
    for p in (4, 5):
        engine, state, metadata = build(initial, p, block_size=256)
        low, up, _ = raw_features(initial, p)
        assert torch.equal(low[:, :6], old[0])
        assert torch.equal(up[:, :12], old[1])
        assert (engine.K1, engine.K2) == {4:(6,12), 5:(14,24)}[p]
        assert torch.equal(state.w, initial.w) and torch.equal(state.c, initial.c)
        checks[f'new_p{p}'] = metadata
    other = inherited.read_initial(ARCHIVE/'scaling_width4096_refined01/two_outliers_alternating_full/arrays.npz', device)
    for key in ('w','c','M'):
        checks['shared_initial_'+key] = float((getattr(initial,key)-getattr(other,key)).abs().max())
        assert checks['shared_initial_'+key] == 0
    save_json(directory/'validation.json', dict(passed=True, checks=checks, source_hashes=hashes()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--device', required=True)
    parser.add_argument('--worker', type=int, choices=(0,1), default=0)
    parser.add_argument('--level', type=int, choices=(0,1,2), default=0)
    parser.add_argument('--budget', type=float, default=400)
    parser.add_argument('--only', nargs='+', choices=METHODS)
    parser.add_argument('--preflight', action='store_true')
    args = parser.parse_args()
    if not 0 < args.budget <= 400:
        parser.error('budget must be in (0,400]')
    inherited.setup(args.device)
    start = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=not args.preflight)
    config_path = args.out/f'config_worker{args.worker}.json'
    if config_path.exists():
        raise FileExistsError(config_path)
    initial_path = ARCHIVE/'scaling_width4096_refined01/quadrant_pairs_full/arrays.npz'
    initial = inherited.read_initial(initial_path, args.device)
    rtol, atol = 6.25e-5/4**args.level, 6.25e-7/4**args.level
    config = dict(cases=CASES, width=4096, network_seed=20260920, threshold=1e-3,
        methods=args.only or METHODS, orders=[4,5], device=args.device,
        gpu=torch.cuda.get_device_name(args.device), dtype='float64', rtol=rtol, atol=atol,
        level=args.level, worker=args.worker, worker_limit_seconds=args.budget,
        per_trajectory_limit_seconds=180, max_time=10000, max_steps=30000,
        initial_step=.05, max_step=2, min_step=1e-7, block_size=256,
        initial_archive=str(initial_path.relative_to(ROOT)), initial_archive_sha256=sha(initial_path),
        initial_array_sha256={k:hashlib.sha256(getattr(initial,k).cpu().numpy().tobytes()).hexdigest() for k in ('w','c','M')},
        torch=str(torch.__version__), numpy=np.__version__, python=sys.version,
        source_hashes=hashes(), command=sys.argv, cwd=str(Path.cwd()),
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(config_path, config)
    if args.preflight:
        preflight(initial, args.out, args.device)
        seconds = time.monotonic()-start
        assert seconds <= args.budget
        save_json(args.out/'completion.json', dict(seconds=seconds, passed=True))
        print(json.dumps(dict(preflight='PASS', seconds=seconds)), flush=True)
        return
    name, case = list(CASES.items())[args.worker]
    results = {}
    for method in args.only or METHODS:
        if time.monotonic()-start >= args.budget:
            break
        p = int(method[-1])
        engine, state, metadata = build(initial, p, block_size=256)
        key = name+'_'+method
        save_json(args.out/(key+'_dictionary.json'), metadata)
        results[key] = inherited.trajectory(engine,state,case,args.out/key,rtol,atol,start,args.budget)
        results[key]['declared_executed'] = True
        save_json(args.out/f'results_worker{args.worker}.json', results)
    torch.cuda.synchronize(args.device)
    completion = dict(seconds=time.monotonic()-start,
        fitted=sum(r['status']=='fitted' for r in results.values()),total=len(results),
        expected=len(args.only or METHODS), exit_status=0,
        finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(args.out/f'completion_worker{args.worker}.json', completion)
    print(json.dumps(completion),flush=True)


if __name__ == '__main__':
    main()
