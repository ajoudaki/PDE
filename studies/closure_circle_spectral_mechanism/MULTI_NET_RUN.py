"""Fixed 48-job actual dense-network extension; see frozen MULTI_NET_PLAN.md."""
import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import traceback

import numpy as np
import torch

import NET_RUN as base

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / 'data/generated/closure_circle_spectral_mechanism'
OUT = GENERATED / 'network_comparison_multi_001'
CHECK_OUT = GENERATED / 'multi_worker_checks_001'
CASES = {
    'triple_d20': 'cf1bfe2d79f5d8dcd5fc7a2fbf7e61b2c3bb9afba04c6477c4173df96cd65e0b',
    'triple_d40': '2dc8ae649f3b688d147f2e5a77f1ae1f1c8e69fe51b57280299074ebb21559e6',
    'triple_d60': '63501efd8bacedf926a6d6c808099b6f55852641a3de932238c2664268f3e4f6',
    'quad_d15': '70b46f4041348fe1b248356a77927a00ce415a30dbe2643fd378967d9652c269',
    'quad_d30': '4ccd4bba3cb837ef307304b6973753cd827edf16a4a74bf4f144b169d308cd61',
    'quad_d45': '0a176591e90e346de83969de105c6389f476d4302a705024ecacc83e1a4b40fa',
}
SEEDS = [1729, 2718, 3141]
SOURCE_PATHS = [HERE / 'MULTI_NET_PLAN.md', HERE / 'MULTI_NET_RUN.py',
                HERE / 'NET_PLAN.md', HERE / 'NET_RUN.py',
                ROOT / 'code/pde/finite_network.py']
sha, write_json, Network, setup = base.sha, base.write_json, base.Network, base.setup


def source_hashes():
    return {str(p.relative_to(ROOT)): sha(p) for p in SOURCE_PATHS}


def case_paths():
    return {case: GENERATED / 'campaign_001' / (case + '_N1_main') / 'config.json'
            for case in CASES}


def input_hashes():
    result = {str(p.relative_to(ROOT)): sha(p) for p in case_paths().values()}
    for case, path in case_paths().items():
        if result[str(path.relative_to(ROOT))] != CASES[case]:
            raise RuntimeError('closure input identity mismatch: ' + case)
    return result


def config(case, n, seed, variant='main'):
    original = json.loads(case_paths()[case].read_text())
    cfg = {key: original[key] for key in
           ['name', 'kind', 'delta', 'rotation', 'amplitude', 'angles_degrees', 'labels']}
    if cfg['name'] != case:
        raise RuntimeError('case identity mismatch')
    cfg.update(id=f'{case}_n{n}_s{seed}_{variant}', width=n, seed=seed,
               h=.01 if variant == 'half' else .02,
               dtype='float64' if variant == 'precision' else 'float32',
               variant=variant, retain_state=True, t_final=120, obs_dt=10,
               closure_config_sha256=CASES[case],
               closure_config_path=str(case_paths()[case].relative_to(ROOT)))
    return cfg


def configs():
    main = [config(case, n, seed) for case in CASES
            for n in [1024, 4096] for seed in SEEDS]
    controls = [config(case, n, 1729, variant) for case in CASES
                for n, variant in [(4096, 'half'), (1024, 'precision')]]
    return main + controls


def resource_limits(out, scientific=False):
    used = sum(p.stat().st_size for p in out.rglob('*') if p.is_file())
    if used > 4 * 2**30:
        raise RuntimeError('4GiB campaign output cap')
    if shutil.disk_usage(out).free < 10 * 2**30:
        raise RuntimeError('10GiB minimum free disk reached')
    if scientific:
        clock = json.loads((out / 'clock.json').read_text())
        if time.monotonic() - clock['monotonic_start'] > 1200:
            raise RuntimeError('1200-second scientific campaign cap')
    return used


def prepare(out):
    if out != OUT:
        raise ValueError('assigned campaign namespace required')
    if out.exists():
        raise FileExistsError(out)
    inputs = input_hashes()
    sources = source_hashes()
    cfgs = configs()
    assert len(cfgs) == 48 and len({c['id'] for c in cfgs}) == 48
    out.mkdir()
    resource_limits(out)
    archive = out / 'source_archive'
    archive.mkdir()
    archived = {}
    for source, digest in {**sources, **inputs}.items():
        target = archive / source.replace('/', '__')
        shutil.copyfile(ROOT / source, target)
        if sha(target) != digest:
            raise RuntimeError('source archive identity mismatch')
        archived[source] = dict(path=str(target.relative_to(out)), sha256=digest)
    manifest = dict(schema_version=1, configs=cfgs, conditional_wide=[],
                    source_hashes=sources, input_hashes=inputs, archived_sources=archived,
                    cwd=str(ROOT), command=sys.argv, final_time=120,
                    limits=dict(scientific_wall_seconds=1200, job_wall_seconds=120,
                                output_bytes=4 * 2**30, free_bytes=10 * 2**30),
                    environment={k: os.environ.get(k) for k in
                                 ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS',
                                  'MKL_NUM_THREADS', 'CUBLAS_WORKSPACE_CONFIG']})
    write_json(out / 'manifest.json', manifest)
    (out / 'manifest.sha256').write_text(sha(out / 'manifest.json') + '\n')
    print(json.dumps(dict(prepared=str(out), jobs=len(cfgs),
                          manifest_sha256=sha(out / 'manifest.json'))), flush=True)


def verify_identity(out):
    if sha(out / 'manifest.json') != (out / 'manifest.sha256').read_text().strip():
        raise RuntimeError('manifest changed after freeze')
    manifest = json.loads((out / 'manifest.json').read_text())
    if source_hashes() != manifest['source_hashes']:
        raise RuntimeError('producer or frozen plan changed after preparation')
    if input_hashes() != manifest['input_hashes']:
        raise RuntimeError('closure inputs changed after preparation')
    return manifest


def worker_check(device, out):
    # Reuse exact NET_RUN checks while recording only the frozen execution inputs.
    base.source_hashes = source_hashes
    base.checks(device, out)


def checked_wait(processes, logs, timeout, on_poll=None):
    start = time.monotonic()
    reason = None
    try:
        while True:
            codes = [p.poll() for p in processes]
            if any(c not in [None, 0] for c in codes):
                raise RuntimeError('worker failure')
            if time.monotonic() - start > timeout:
                raise RuntimeError(f'{timeout}-second supervisor wall cap')
            if on_poll is not None:
                on_poll()
            if all(c is not None for c in codes):
                break
            time.sleep(.2)
    except BaseException as exc:
        reason = repr(exc)
        for p in processes:
            if p.poll() is None:
                p.terminate()
    finally:
        for p in processes:
            try:
                p.wait(timeout=5)
            except subprocess.TimeoutExpired:
                p.kill()
                p.wait()
        for log in logs:
            log.close()
    return [p.returncode for p in processes], reason


def check_batch(out):
    if out != CHECK_OUT:
        raise ValueError('assigned check namespace required')
    out.mkdir(exist_ok=False)
    start = time.monotonic()
    processes, logs = [], []
    for gpu in [0, 1]:
        log = (out / f'cuda{gpu}.log').open('x')
        logs.append(log)
        processes.append(subprocess.Popen(
            [sys.executable, '-B', str(Path(__file__).resolve()), '--check',
             '--device', f'cuda:{gpu}', '--output', str(out / f'cuda{gpu}')],
            stdout=log, stderr=subprocess.STDOUT, cwd=ROOT, env=os.environ.copy()))
    codes, reason = checked_wait(processes, logs, 120)
    passed = not reason and codes == [0, 0]
    write_json(out / 'batch.json', dict(passed=passed, exit_codes=codes, stop_reason=reason,
                                       elapsed=time.monotonic() - start,
                                       source_hashes=source_hashes(), command=sys.argv))
    print(json.dumps(dict(checks_passed=passed, elapsed=time.monotonic() - start)), flush=True)
    if not passed:
        raise RuntimeError('worker checks incomplete or failed')


@torch.no_grad()
def run_job(out, cfg, device):
    manifest = verify_identity(out)
    if cfg not in manifest['configs']:
        raise RuntimeError('unregistered configuration')
    directory = out / cfg['id']
    directory.mkdir()
    begun, monotonic_start = time.time(), time.monotonic()
    write_json(directory / 'started.json', dict(wall_start=begun,
               monotonic_start=monotonic_start, pid=os.getpid(), config=cfg))
    write_json(directory / 'config.json', cfg)
    with (directory / 'job.log').open('x') as job_log:
        with contextlib.redirect_stdout(job_log), contextlib.redirect_stderr(job_log):
            print(json.dumps(dict(event='started', device=device, config=cfg)), flush=True)
            try:
                result = train_and_save(out, directory, cfg, device, manifest, monotonic_start)
                print(json.dumps(dict(event='complete', **result)), flush=True)
            except BaseException as exc:
                failure = dict(error=repr(exc), traceback=traceback.format_exc(),
                               config=cfg, elapsed=time.monotonic() - monotonic_start)
                write_json(directory / 'failure.json', failure)
                print(json.dumps(failure), flush=True)
                raise
    print(json.dumps(result), flush=True)


@torch.no_grad()
def train_and_save(out, directory, cfg, device, manifest, begun):
    def limits():
        resource_limits(out, scientific=True)
        if time.monotonic() - begun > 120:
            raise RuntimeError('120-second per-job wall cap including diagnostics')

    limits()
    dtype, n = getattr(torch, cfg['dtype']), cfg['width']
    net = Network.initialize(n, cfg['seed'], device, dtype)
    initial_hash = hashlib.sha256()
    for array in net.arrays():
        initial_hash.update(array.tobytes())
    theta = 2 * np.pi * np.arange(1440) / 1440
    stop_theta = 2 * np.pi * np.arange(512) / 512
    motion_theta = 2 * np.pi * np.arange(128) / 128
    u = net.tensor_inputs(np.deg2rad(cfg['angles_degrees']))
    y = torch.as_tensor(cfg['labels'], device=device, dtype=dtype)
    um = net.tensor_inputs(motion_theta)
    h10, h20, _ = net.fields(u)
    hm10, hm20, _ = net.fields(um)
    times, losses, predictions, train_predictions = [], [], [], []
    common = None
    max_increase = 0.
    steps_per_obs = int(round(10 / cfg['h']))
    for obs in range(13):
        limits()
        t = obs * 10.
        p = net.predict(stop_theta)
        ft = net.fields(u)[2].cpu().numpy().astype(float)
        loss = float(np.mean((ft - np.array(cfg['labels']))**2))
        if not all(torch.isfinite(a).all().item() for a in net.state()):
            raise RuntimeError('nonfinite stored state')
        if not np.all(np.isfinite(p)) or not np.all(np.isfinite(ft)) or not np.isfinite(loss):
            raise RuntimeError('nonfinite output')
        if losses:
            max_increase = max(max_increase, loss - losses[-1])
        if max_increase > 1e-6:
            raise RuntimeError('recorded loss increased beyond allowance')
        times.append(t)
        losses.append(loss)
        predictions.append(p)
        train_predictions.append(ft)
        if t == 100:
            common = net.predict(theta)
        print(json.dumps(dict(event='observation', T=t, loss=loss,
                              elapsed=time.monotonic() - begun)), flush=True)
        if t == 120:
            break
        for _ in range(steps_per_obs):
            net.step(u, y, cfg['h'])
    dense = net.predict(theta)
    h1, h2, _ = net.fields(u)
    hm1, hm2, _ = net.fields(um)
    drift_old = float(np.max(abs(predictions[10] - predictions[8])))
    drift_new = float(np.max(abs(predictions[12] - predictions[10])))
    settle_tol = .002 * max(1., float(np.max(abs(predictions[-1]))))
    settled = losses[-1] <= 1e-6 and drift_old <= settle_tol and drift_new <= settle_tol
    odd = float(np.max(abs(dense[:720] + dense[720:])))
    tol = 2e-5 if dtype == torch.float32 else 1e-10
    if odd > tol or not np.all(np.isfinite(dense)) or not np.all(np.isfinite(common)):
        raise RuntimeError('dense output validity failed')
    limits()
    W, V, c = net.arrays()
    np.savez(directory / 'state.npz', W=W, V=V, c=c)
    with np.load(directory / 'state.npz', allow_pickle=False) as state:
        replay_net = Network((state['W'], state['V'], state['c']), device, dtype)
    replay = float(np.max(abs(replay_net.predict(theta) - dense)))
    del replay_net
    if replay > tol:
        raise RuntimeError('final disk replay failed')
    np.savez_compressed(directory / 'observations.npz',
        theta=theta, stop_theta=stop_theta, motion_theta=motion_theta,
        dense_predictions=dense, common_T100=common, times=times, loss=losses,
        predictions=predictions, train_predictions=train_predictions,
        gram1_initial=(h10.T @ h10 / n).cpu().numpy(),
        gram2_initial=(h20.T @ h20 / n).cpu().numpy(),
        gram1_final=(h1.T @ h1 / n).cpu().numpy(),
        gram2_final=(h2.T @ h2 / n).cpu().numpy(),
        motion1_circle=float(torch.mean((hm1 - hm10)**2).sqrt()),
        motion2_circle=float(torch.mean((hm2 - hm20)**2).sqrt()))
    outputs = {name: sha(directory / name)
               for name in ['state.npz', 'observations.npz', 'config.json']}
    limits()
    record = dict(status='complete', config=cfg, settled=bool(settled),
        final_time=120., final_loss=losses[-1], stop_reason='fixed_T120',
        checks=dict(oddness=odd, max_loss_increase=max_increase, disk_replay=replay,
                    settled_drift_80_100=drift_old, settled_drift_100_120=drift_new,
                    settled_tolerance=settle_tol, finite_states=True),
        source_hashes=manifest['source_hashes'], input_hashes=manifest['input_hashes'],
        manifest_sha256=sha(out / 'manifest.json'),
        initial_weight_sha256=initial_hash.hexdigest(), outputs=outputs,
        elapsed=time.monotonic() - begun,
        environment=dict(torch=torch.__version__, numpy=np.__version__, device=device,
            python=sys.executable, gpu=torch.cuda.get_device_name(torch.device(device)),
            tf32=False, dtype=cfg['dtype'], command=sys.argv))
    write_json(directory / 'record.json', record)
    return dict(id=cfg['id'], seconds=record['elapsed'], T=120.,
                loss=losses[-1], settled=bool(settled))


def worker(out, assignment, device):
    setup(device)
    for cfg in json.loads(assignment.read_text()):
        run_job(out, cfg, device)


def assignments(cfgs):
    # Static cost scheduling uses only declared width, dtype and step count.
    # Within each priority, original manifest order is retained.
    def cost(cfg):
        precision_factor = 4 if cfg['dtype'] == 'float64' else 1
        return cfg['width']**2 * (.02 / cfg['h']) * precision_factor
    queues, loads = [[], []], [0, 0]
    for cfg in sorted(cfgs, key=lambda cfg: -cost(cfg)):
        gpu = min(range(2), key=lambda index: loads[index])
        queues[gpu].append(cfg)
        loads[gpu] += cost(cfg)
    return queues


def wave(out):
    manifest = verify_identity(out)
    check = json.loads((CHECK_OUT / 'batch.json').read_text())
    if not check['passed'] or check['source_hashes'] != manifest['source_hashes']:
        raise RuntimeError('matching frozen worker checks required')
    if (out / 'clock.json').exists() or (out / 'main_batch.json').exists():
        raise RuntimeError('campaign has already launched; no retries')
    resource_limits(out)
    queues = assignments(manifest['configs'])
    processes, logs = [], []
    start = time.monotonic()
    write_json(out / 'clock.json', dict(start=time.time(), monotonic_start=start,
                                      command=sys.argv))
    for gpu in [0, 1]:
        assignment = out / f'main_assignment{gpu}.json'
        write_json(assignment, queues[gpu])
        log = (out / f'main_worker{gpu}.log').open('x')
        logs.append(log)
        processes.append(subprocess.Popen(
            [sys.executable, '-B', str(Path(__file__).resolve()), '--worker',
             str(assignment), '--output', str(out), '--device', f'cuda:{gpu}'],
            stdout=log, stderr=subprocess.STDOUT, cwd=ROOT, env=os.environ.copy()))

    def poll():
        resource_limits(out, scientific=True)
        for cfg in manifest['configs']:
            directory = out / cfg['id']
            started = directory / 'started.json'
            if started.exists() and not (directory / 'record.json').exists():
                state = json.loads(started.read_text())
                if time.monotonic() - state['monotonic_start'] > 120:
                    raise RuntimeError('per-job supervisor wall cap: ' + cfg['id'])

    codes, reason = checked_wait(processes, logs, 1200, poll)
    completed = [c['id'] for c in manifest['configs'] if (out / c['id'] / 'record.json').exists()]
    missing = [c['id'] for c in manifest['configs'] if c['id'] not in completed]
    if missing and reason is None:
        reason = 'registered jobs incomplete'
    used = sum(p.stat().st_size for p in out.rglob('*') if p.is_file())
    result = dict(wave='main', exit_codes=codes, elapsed=time.monotonic() - start,
                  stop_reason=reason, completed=completed, missing=missing,
                  output_bytes=used, source_hashes=manifest['source_hashes'],
                  manifest_sha256=sha(out / 'manifest.json'))
    write_json(out / 'main_batch.json', result)
    print(json.dumps(result), flush=True)
    if reason or any(codes):
        raise RuntimeError('fixed campaign incomplete')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=lambda value: Path(value).resolve(), required=True)
    parser.add_argument('--device', default='cpu')
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--prepare', action='store_true')
    action.add_argument('--check-batch', action='store_true')
    action.add_argument('--check', action='store_true')
    action.add_argument('--wave', action='store_true')
    action.add_argument('--worker', type=Path)
    args = parser.parse_args()
    if args.prepare:
        prepare(args.output)
    elif args.check_batch:
        check_batch(args.output)
    elif args.check:
        worker_check(args.device, args.output)
    elif args.worker:
        worker(args.output, args.worker, args.device)
    elif args.wave:
        wave(args.output)
