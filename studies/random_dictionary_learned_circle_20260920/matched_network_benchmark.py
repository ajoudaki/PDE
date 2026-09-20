"""Width-1024 closure versus two separately parameter-matched exact networks."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time

from benchmark import ROOT, NetworkEngine, setup, save_json, torch, np
from diverse_benchmark import trajectory, THRESHOLD, MAX_TIME, MAX_STEPS, SNAPSHOTS
from diverse_cases import CASES_V2
from scaling_dictionary import build, dictionary_metadata, DIMENSIONS

WIDTH, SEED = 1024, 20260920
ORDERS = (1, 3, 5)
CASES = {name: CASES_V2[name] for name in
         ('quadrant_alternating', 'two_outliers_alternating')}
PROTOCOL = Path(__file__).with_name('MATCHED_NETWORK_PROTOCOL.md')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def matched_width(budget):
    """Smallest integer width whose actual scalar count covers the budget."""
    width = max(1, (math.isqrt(9 + 4*budget)-3)//2)
    while width*width + 3*width < budget:
        width += 1
    assert (width-1)**2 + 3*(width-1) < budget <= width**2 + 3*width
    return width


def specifications():
    specs = {'full': dict(method='full', p=None, width=WIDTH,
                         trainable_parameters=WIDTH**2+3*WIDTH,
                         model_parameters=WIDTH**2+3*WIDTH)}
    for order in ORDERS:
        k1, k2 = DIMENSIONS[order]
        train = 3*WIDTH + k1*k2
        total = WIDTH*(k1+k2) + train
        shared = dict(p=order, dictionary_dimensions=[k1,k2],
                      dictionary_vectors=k1+k2, closure_trainable_parameters=train,
                      closure_model_parameters=total)
        specs[f'ours_p{order}'] = dict(**shared, method='ours', width=WIDTH,
                                       trainable_parameters=train, model_parameters=total)
        for match, budget in (('trainable',train),('total',total)):
            width = matched_width(budget)
            count = width**2 + 3*width
            specs[f'small_{match}_p{order}'] = dict(**shared,
                method=f'small_{match}', width=width, matched_budget=budget,
                trainable_parameters=count, model_parameters=count,
                excess_parameters=count-budget, excess_fraction=count/budget-1)
    return specs


def producer_hashes():
    paths = {Path(__file__).resolve(), PROTOCOL.resolve()}
    for module in list(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename:
            path = Path(filename).resolve()
            if path.suffix == '.py' and (path.is_relative_to(ROOT/'code'/'pde')
                    or path.parent == Path(__file__).resolve().parent):
                paths.add(path)
    return {str(path.relative_to(ROOT)):digest(path) for path in sorted(paths)}


@torch.no_grad()
def small_network(initial, width):
    """Canonical Gaussian marginal, coupled through a fixed neuron prefix."""
    n = len(initial.w)
    if not 1 <= width <= n:
        raise ValueError('small width must be within the reference width')
    engine = NetworkEngine(2, width, SEED, device=initial.w.device,
                           dtype=torch.float64, block_size=256)
    state = engine.state(initial.w[:width], initial.c[:width]*(n/width),
                         initial.M[:width,:width]*math.sqrt(n/width))
    # Fresh-object initialization only: observations must use the coupled origin.
    engine.initial = state.clone()
    engine._initial_versions = engine._versions()
    return engine, engine.initial_state()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--worker', type=int, choices=(0,1), required=True)
    parser.add_argument('--device', required=True)
    parser.add_argument('--level', type=int, choices=(0,1,2,3), required=True)
    parser.add_argument('--budget', type=float, required=True)
    parser.add_argument('--only-cells', nargs='+')
    args = parser.parse_args()
    if not 0 < args.budget <= 600:
        raise ValueError('worker reservation must be at most600 seconds')
    if (args.level >= 2) != bool(args.only_cells):
        raise ValueError('extra numerical levels require explicit selected cells only')
    device = setup(args.device)
    args.out.mkdir(parents=True, exist_ok=True)
    config_path = args.out/f'config_worker{args.worker}.json'
    if config_path.exists():
        raise FileExistsError(config_path)
    case = list(CASES)[args.worker]
    specs = specifications()
    cells = [f'{case}_{name}' for name in specs]
    if args.only_cells:
        if len(set(args.only_cells)) != len(args.only_cells) or not set(args.only_cells)<=set(cells):
            raise ValueError('selected cells outside this case or duplicated')
        cells = [cell for cell in cells if cell in args.only_cells]
    if any((args.out/cell).exists() for cell in cells):
        raise FileExistsError('refusing to overwrite an existing trajectory')
    rtol, atol = 6.25e-5/4**args.level, 6.25e-7/4**args.level
    config = dict(cases=CASES, case=case, width=WIDTH, network_seed=SEED,
        orders=list(ORDERS), models=specs, selected_cells=cells, level=args.level,
        coupling='fixed_prefix_canonical_rescaling', threshold=THRESHOLD,
        dtype='float64', rtol=rtol, atol=atol, step=.05, max_step=2.,
        max_time=MAX_TIME, max_steps=MAX_STEPS, snapshot_times=SNAPSHOTS,
        circle_nodes=2048, endpoint_nodes=8192, worker=args.worker,
        worker_limit_seconds=args.budget, per_trajectory_limit_seconds=180,
        training_run=True, device=device, gpu=torch.cuda.get_device_name(device),
        torch=str(torch.__version__), numpy=np.__version__, python=sys.version,
        command=sys.argv, cwd=str(Path.cwd()), source_hashes=producer_hashes(),
        protocol_path=str(PROTOCOL.relative_to(ROOT)), protocol_sha256=digest(PROTOCOL),
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(config_path, config)
    start = time.monotonic()
    net = NetworkEngine(2, WIDTH, SEED, device=device, dtype=torch.float64, block_size=256)
    initial = net.initial_state()
    results = {}
    for key in cells:
        name = key[len(case)+1:]
        spec = specs[name]
        directory = args.out/key
        if time.monotonic()-start >= args.budget:
            directory.mkdir()
            result = dict(status='not_run_budget', loss=None, time=None, seconds=0,
                          rtol=rtol, atol=atol)
            save_json(directory/'summary.json', result)
        else:
            try:
                if name == 'full':
                    engine, state = net, initial
                elif spec['method'] == 'ours':
                    engine, state = build(initial, spec['p'], 'ours')
                    meta = dictionary_metadata(initial,spec['p'],'ours',bases=(engine.b1,engine.b2))
                    save_json(args.out/f'dictionary_worker{args.worker}_{name}.json',meta)
                    if any(x['ridge_condition']>1e10 or x['triangular_solve_residual']>1e-8
                           for x in meta['populations']):
                        raise ValueError('dictionary numerical gate failed')
                else:
                    engine, state = small_network(initial, spec['width'])
                actual = sum(getattr(state,k).numel() for k in ('w','c','M'))
                assert actual == spec['trainable_parameters']
                actual_total = actual + (engine.b1.numel()+engine.b2.numel()
                                         if spec['method']=='ours' else 0)
                assert actual_total == spec['model_parameters']
                result = trajectory(engine,state,CASES[case],directory,rtol,atol,start,args.budget)
                result.update(model=name, model_specification=spec,
                              actual_trainable_parameters=actual,
                              actual_model_parameters=actual_total)
                save_json(directory/'summary.json',result)
            except (ValueError,RuntimeError) as exc:
                if directory.exists():
                    raise
                directory.mkdir()
                result = dict(status='initialization_failure',loss=None,time=None,seconds=0,
                    reason=f'{type(exc).__name__}: {exc}',rtol=rtol,atol=atol)
                save_json(directory/'summary.json',result)
        results[key] = result
        save_json(args.out/f'results_worker{args.worker}.json',results)
    torch.cuda.synchronize(device)
    completion = dict(exit_status=0,training_run=True,seconds=time.monotonic()-start,
        fitted=sum(x['status']=='fitted' for x in results.values()),total=len(results),
        planned_cells=cells,finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(args.out/f'completion_worker{args.worker}.json',completion)
    print(json.dumps(completion),flush=True)


if __name__ == '__main__':
    main()
