"""Independent raw-state replay for the frozen eleven-case suite.

No producer engine, trajectory routine or suite_analyze imports. The already
frozen raw-feature builders are used only to identify the new fixed bases;
ridge normalization, projection, forward evaluation and metrics are separate.
Every completed trajectory and case is saved before the next is started.
"""
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
import sys
import time
import zipfile
import numpy as np
import torch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'code'))
TOL = 1e-10
NEW_DIMS = {1:(2,4), 3:(6,12), 5:(14,24)}
OLD_DIMS = {1:(5,3), 3:(35,10), 5:(128,21)}


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(obj, indent=2, allow_nan=False)+'\n')
    tmp.replace(path)


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024), b''):
            result.update(block)
    return result.hexdigest()


class MappedNPZ:
    """Read ZIP_STORED NPY arrays in place, including dense state histories."""
    def __init__(self, path):
        self.path = Path(path)
        self.arrays = {}
        self.identity = {}
        with zipfile.ZipFile(path) as z, self.path.open('rb') as f:
            for info in z.infolist():
                if info.compress_type != zipfile.ZIP_STORED:
                    raise ValueError('Expected uncompressed numeric NPZ: '+str(path))
                f.seek(info.header_offset)
                header = struct.unpack('<4s5H3I2H', f.read(30))
                f.seek(header[-2]+header[-1], 1)
                version = np.lib.format.read_magic(f)
                reader = (np.lib.format.read_array_header_1_0 if version == (1,0)
                          else np.lib.format.read_array_header_2_0)
                shape, fortran, dtype = reader(f)
                if fortran or dtype.hasobject:
                    raise ValueError('Unexpected array storage')
                key = info.filename.removesuffix('.npy')
                self.arrays[key] = np.memmap(path, mode='r', dtype=dtype,
                                             shape=shape, offset=f.tell())
                self.identity[key] = dict(shape=list(shape), dtype=str(dtype),
                    crc32=info.CRC, size=info.file_size)

    def __getitem__(self, key):
        return self.arrays[key]


def peak(x):
    return float(np.max(np.abs(x))) if np.size(x) else 0.


def metric(a, b):
    device=torch.device('cuda',torch.cuda.current_device())
    d=torch.tensor(np.asarray(a),device=device,dtype=torch.float64)-torch.tensor(
        np.asarray(b),device=device,dtype=torch.float64)
    return dict(rms=float(torch.sqrt(torch.mean(d*d))), l1=float(torch.mean(abs(d))),
                mse=float(torch.mean(d*d)), max_abs=float(torch.max(abs(d))))


def endpoint_delta(a,b):
    device=torch.device('cuda',torch.cuda.current_device())
    left=torch.tensor(np.asarray(a),device=device,dtype=torch.float64)
    right=torch.tensor(np.asarray(b),device=device,dtype=torch.float64)
    return float((left-right).abs().max())


def check(condition, message, errors):
    if not condition:
        errors.append(message)


@torch.no_grad()
def predict(w, c, middle, inputs, b1=None, b2=None):
    """Direct bias-free physical forward map, with independent association."""
    n = len(w)
    parts = []
    for j in range(0, len(inputs), 512):
        first = torch.tanh(inputs[j:j+512] @ w.T)
        if b1 is None:
            second = torch.tanh(first @ middle.T)
        else:
            coordinates = (first @ b1)/n
            second = torch.tanh((coordinates @ middle.T) @ b2.T)
        parts.append((second @ c)/n)
    return torch.cat(parts)


def sources(entry, case, manifest, cache):
    config_path = Path(entry['config_path'])
    token = (str(config_path), case, entry.get('key'))
    if token in cache:
        return cache[token]
    config = json.loads(config_path.read_text())
    errors, records = [], {}
    if entry.get('config_sha256'):
        check(sha(config_path)==entry['config_sha256'], 'configuration hash mismatch', errors)
    deps = entry.get('executed_producer_dependency_hashes', config['source_hashes'])
    for p, expected in deps.items():
        path = ROOT/p
        current = sha(path) if path.is_file() else None
        records[p] = dict(expected=expected, actual=current)
        # Four archived dense references predate the later width-only wrapper
        # extension. Accept only the exact archived bytes, bound to that
        # configuration's recorded HEAD and digest; never waive a mismatch.
        recovered = None
        if current!=expected and p=='studies/random_dictionary_learned_circle_20260920/scaling_benchmark.py':
            proofs = ROOT/'data/generated/gradient_flow_probe_dictionary_20260921/suite_inventory01/sourceproofs'
            evidence_path = proofs/'git_retrieval.json'
            if evidence_path.exists():
                for evidence in json.loads(evidence_path.read_text()):
                    candidate = Path(evidence['saved_path'])
                    if (evidence['head']==config['head'] and evidence['path']==p and
                            evidence['exit_code']==0 and candidate.is_file() and
                            sha(candidate)==expected==evidence['sha256']):
                        recovered = str(candidate)
                        records[p]['archived_source_path'] = recovered
                        records[p]['archived_source_sha256'] = expected
        check(current==expected or recovered is not None, 'executed source differs: '+p, errors)
        check(config['source_hashes'].get(p)==expected,
              'configuration lacks dependency digest: '+p, errors)
    check(config['width']==2048 and config['network_seed']==20260920,
          'width or network seed mismatch', errors)
    check(config['cases'][case]==manifest['cases'][case], 'case definition mismatch', errors)
    check(config['threshold']==.001, 'threshold mismatch', errors)
    check(config['dtype']=='float64', 'dtype mismatch', errors)
    check(config['endpoint_nodes']==8192 and config['circle_nodes']==2048,
          'grid sizes mismatch', errors)
    for key in ('rtol','atol'):
        check(config[key]==entry[key], key+' configuration mismatch', errors)
    if entry.get('new'):
        check(config['manifest_sha256']==sha(HERE/'SUITE_MANIFEST.json'),
              'manifest hash mismatch', errors)
        check(config['rtol']==6.25e-5/4**config['level'], 'new tolerance policy mismatch', errors)
        check(config['atol']==config['rtol']/100, 'new absolute tolerance mismatch', errors)
        check(config['max_time']==10000 and config['max_steps']==30000,
              'new integration limits mismatch', errors)
        check(config['initial_step']==.05 and config['max_step']==2 and config['min_step']==1e-7,
              'new step settings mismatch', errors)
        check(case in config['assigned_cases'], 'case not assigned to saved worker', errors)
        check(entry['key'] in config['execution_schedule'], 'cell not scheduled', errors)
        ledger_path=config_path.with_name(config_path.name.replace('config_','results_'))
        if ledger_path.exists():
            ledger=json.loads(ledger_path.read_text())
            check(entry['key'] in ledger,'new cell absent from execution ledger',errors)
            if entry['key'] in ledger:
                summary=json.loads(Path(entry['summary_path']).read_text())
                check(ledger[entry['key']].get('declared_executed') is True,
                      'new ledger cell not declared executed',errors)
                for k in ('status','loss','time','rtol','atol'):
                    check(ledger[entry['key']][k]==summary[k],'new ledger/summary mismatch '+k,errors)
        else:
            errors.append('new execution ledger missing')
    result = dict(errors=errors, config_path=str(config_path), config_sha256=sha(config_path),
                  source_hashes=records)
    cache[token] = result
    return result


def new_entries(case, method, roots):
    result = []
    key = case+'_'+method
    for directory in roots:
        raw = directory/key
        if not (raw/'summary.json').is_file():
            continue
        matches = []
        for cp in directory.glob('config_worker*.json'):
            config = json.loads(cp.read_text())
            if key in config.get('execution_schedule', []):
                matches.append((cp,config))
        if len(matches)!=1:
            raise ValueError('Cannot bind cell to one executed configuration: '+str(raw))
        cp,cfg = matches[0]
        result.append(dict(directory=str(raw), arrays_path=str(raw/'arrays.npz'),
            summary_path=str(raw/'summary.json'), config_path=str(cp),
            rtol=cfg['rtol'], atol=cfg['atol'], new=True, key=key))
    result.sort(key=lambda x:-x['rtol'])
    if len({x['rtol'] for x in result})!=len(result):
        raise ValueError('Duplicate attempts at same tolerance: '+key)
    return result


class Checker:
    def __init__(self, args, manifest):
        self.args, self.manifest = args, manifest
        self.start = args._started
        self.source_cache = {}
        self.basis_cache = {}
        path = manifest['archive_cells']['quadrant_grouped_full']['refined']['arrays_path']
        raw = MappedNPZ(path)
        self.initial = {k:torch.tensor(np.array(raw[k][0]), device=args.device)
                        for k in ('w','c','M')}
        self.initial_hash = {k:hashlib.sha256(np.asarray(raw[k][0]).tobytes()).hexdigest()
                             for k in ('w','c','M')}

    def remaining(self):
        return self.args.budget-(time.monotonic()-self.start)

    def tensor(self, x):
        return torch.tensor(np.array(x), device=self.args.device)

    @torch.no_grad()
    def new_basis(self, order):
        if order not in self.basis_cache:
            from pde.observable_torch_p1 import TensorState
            from new_dictionary import raw_features as low
            from new_dictionary_p45 import raw_features as high
            raw1,raw2,metadata = (high if order==5 else low)(
                TensorState(*(self.initial[k] for k in ('w','c','M'))),order)
            result, diagnostics = [], []
            eta = 1/(1024*(order+1)**2)
            for raw in (raw1,raw2):
                gram = raw.T@raw/2048
                gram = (gram+gram.T)/2
                regular = gram+eta*torch.eye(gram.shape[0],device=gram.device,dtype=gram.dtype)
                lower = torch.linalg.cholesky(regular)
                # Right multiplication by an independently solved factor.
                inverse_transpose = torch.linalg.solve(lower.T, torch.eye(
                    len(lower),device=lower.device,dtype=lower.dtype))
                b = raw@inverse_transpose
                eig = torch.linalg.eigvalsh(regular)
                diagnostics.append(dict(condition=float(eig[-1]/eig[0]),
                    triangular_relative_residual=float(torch.linalg.norm(b@lower.T-raw)/torch.linalg.norm(raw))))
                result.append(b)
            self.basis_cache[order] = (result, diagnostics, metadata)
        return self.basis_cache[order]

    @torch.no_grad()
    def replay(self, entry, case, method):
        path = Path(entry['arrays_path'])
        token = hashlib.sha256(str(path.resolve()).encode()).hexdigest()[:24]
        record_path = self.args.out/'replays'/(token+'.json')
        endpoint_path = self.args.out/'replays'/(token+'.npy')
        identity = dict(path=str(path), size=path.stat().st_size, mtime_ns=path.stat().st_mtime_ns,
                        checker_sha256=sha(Path(__file__)))
        if record_path.exists():
            prior = json.loads(record_path.read_text())
            if prior['identity']!=identity:
                raise ValueError('Refusing stale replay cache: '+str(path))
            return prior, np.load(endpoint_path,allow_pickle=False)
        if self.remaining()<4:
            raise TimeoutError('Reservation nearly exhausted before next trajectory')
        begin = time.monotonic()
        data = MappedNPZ(path)
        summary = json.loads(Path(entry['summary_path']).read_text())
        provenance = sources(entry,case,self.manifest,self.source_cache)
        errors = list(provenance['errors'])
        check(summary['rtol']==entry['rtol'] and summary['atol']==entry['atol'],
              'summary numerical tolerances mismatch',errors)
        if entry.get('new'):
            config=json.loads(Path(entry['config_path']).read_text())
            check(config['initial_array_sha256']==self.initial_hash,
                  'configuration initial-array hashes mismatch common carrier',errors)
        case_def = self.manifest['cases'][case]
        angle = np.array(case_def['angles_degrees'])*(math.pi/180)
        expected_inputs = np.stack((np.cos(angle),np.sin(angle)),axis=1)
        check(peak(data['training_inputs']-expected_inputs)<1e-14, 'training inputs mismatch',errors)
        check(np.array_equal(data['labels'],case_def['labels']), 'labels mismatch',errors)
        for prefix,count in (('circle',2048),('endpoint',8192)):
            a = np.arange(count)*(2*math.pi/count)
            check(peak(data[prefix+'_angles']-a)<1e-14, prefix+' angles mismatch',errors)
            check(peak(data[prefix+'_inputs']-np.stack((np.cos(a),np.sin(a)),axis=1))<1e-14,
                  prefix+' input grid mismatch', errors)
        for k,v in data.arrays.items():
            # Histories are checked one state at a time below to bound RAM.
            if k not in ('w','c','M'):
                check(bool(np.isfinite(v).all()), 'nonfinite '+k,errors)
        times, losses, snapshots = data['times'],data['losses'],data['snapshot_times']
        count = len(snapshots)
        check(times[0]==0 and len(times)==len(losses) and np.all(np.diff(times)>0),
              'invalid accepted time/loss trace',errors)
        check(len(data['accepted_steps'])==len(times)-1 and
              peak(np.diff(times)-data['accepted_steps'])<1e-10,'accepted step trace mismatch',errors)
        check(len(data['local_error_ratios'])==len(times)-1 and
              np.all(data['local_error_ratios']<=1+1e-12), 'local error controller mismatch',errors)
        check(summary['steps']==len(times)-1 and abs(summary['time']-times[-1])<1e-12,
              'summary time/step mismatch',errors)
        check(abs(summary['loss']-losses[-1])<TOL and abs(summary['initial_loss']-losses[0])<TOL,
              'summary loss mismatch',errors)
        crossing = np.flatnonzero(losses<=.001)
        fitted = summary['status']=='fitted'
        check((not fitted and len(crossing)==0) or
              (fitted and len(crossing)==1 and crossing[0]==len(losses)-1),
              'not first saved accepted threshold crossing',errors)
        check(snapshots[0]==0 and abs(snapshots[-1]-times[-1])<1e-12,
              'snapshot endpoints mismatch',errors)
        for k in ('w','c','M'):
            check(len(data[k])==count, 'snapshot count mismatch '+k,errors)
        n = 2048
        check(data['w'].shape==(count,n,2) and data['c'].shape==(count,n),
              'state width/input dimensions mismatch',errors)
        init_deltas = {}
        for k in ('w','c'):
            init_deltas[k] = float((self.tensor(data[k][0])-self.initial[k]).abs().max())
            check(init_deltas[k]==0, 'initial '+k+' differs from common dense state',errors)
        b1=b2=None
        basis_errors, basis_diagnostics = {}, []
        if method=='full':
            check(data['M'].shape==(count,n,n), 'dense middle shape mismatch',errors)
            init_deltas['M'] = float((self.tensor(data['M'][0])-self.initial['M']).abs().max())
            check(init_deltas['M']==0, 'dense initial middle mismatch',errors)
        else:
            order = int(method[-1])
            expected = (NEW_DIMS if method.startswith('new') else OLD_DIMS)[order]
            check(data['b1'].shape==(n,expected[0]) and data['b2'].shape==(n,expected[1]) and
                  data['M'].shape==(count,expected[1],expected[0]), 'dictionary dimensions mismatch',errors)
            b1,b2 = self.tensor(data['b1']),self.tensor(data['b2'])
            check(np.array_equal(data['p1'],np.full(n,1/n)) and
                  np.array_equal(data['p2'],np.full(n,1/n)), 'population weights mismatch',errors)
            check(np.array_equal(data['g'],data['w'][0]),'frozen g differs from initial read-in',errors)
            projection = b2.T@(self.initial['M']@b1)/n
            init_deltas['projected_M'] = float((projection-self.tensor(data['M'][0])).abs().max())
            check(init_deltas['projected_M']<=TOL, 'projected initial middle mismatch',errors)
            check(np.array_equal(data['D'],data['M'][0]), 'D differs from initial M',errors)
            if method.startswith('new'):
                bases,basis_diagnostics,meta = self.new_basis(order)
                for i,(actual,expected_basis) in enumerate(zip((b1,b2),bases),1):
                    basis_errors['b'+str(i)] = float((actual-expected_basis).abs().max())
                check(max(basis_errors.values())<=TOL, 'new basis reconstruction mismatch',errors)
                check(all(x['condition']<=1e10 and x['triangular_relative_residual']<=1e-8
                          for x in basis_diagnostics), 'new ridge numerical gate',errors)
                mp = Path(entry['directory']).parent/(case+'_'+method+'_dictionary.json')
                saved_meta = json.loads(mp.read_text())
                for k in ('K1','K2','p','normalized_probes','physical_probe_scale','raw_column_rescaling'):
                    check(saved_meta[k]==meta[k], 'new raw metadata mismatch '+k,errors)
                check(saved_meta['eta']==1/(1024*(order+1)**2), 'new ridge eta mismatch',errors)
                check(saved_meta['retained_initial_readout'] and not saved_meta['retained_dense_background'],
                      'initial readout/dense-background metadata mismatch',errors)
        circle = self.tensor(data['circle_inputs'])
        training = self.tensor(data['training_inputs'])
        labels = self.tensor(data['labels']).to(torch.float64)
        snapshot_errors, loss_errors = [], []
        replay_endpoint = None
        for j in range(count):
            if self.remaining()<.4:
                raise TimeoutError('Reservation exhausted within unfinished trajectory')
            state = [self.tensor(data[k][j]) for k in ('w','c','M')]
            check(all(bool(torch.isfinite(x).all()) for x in state), 'nonfinite state snapshot',errors)
            prediction = predict(*state,circle,b1,b2).cpu().numpy()
            snapshot_errors.append(peak(prediction-data['circle_predictions'][j]))
            loss = float(torch.mean((predict(*state,training,b1,b2)-labels)**2))
            i = int(np.argmin(abs(times-snapshots[j])))
            check(abs(times[i]-snapshots[j])<1e-10,'snapshot absent from accepted time trace',errors)
            loss_errors.append(abs(loss-float(losses[i])))
            if j==count-1:
                replay_endpoint = predict(*state,self.tensor(data['endpoint_inputs']),b1,b2).cpu().numpy()
        endpoint_error = peak(replay_endpoint-data['endpoint_prediction'])
        check(max(snapshot_errors,default=0)<=TOL,'snapshot prediction replay exceeds tolerance',errors)
        check(max(loss_errors,default=0)<=TOL,'training loss replay exceeds tolerance',errors)
        check(endpoint_error<=TOL,'endpoint prediction replay exceeds tolerance',errors)
        result = dict(identity=identity, case=case, method=method, errors=errors, passed=not errors,
            status=summary['status'], loss=summary['loss'], time=summary['time'], rtol=entry['rtol'],
            atol=entry['atol'], snapshots=count, first_crossing_record_verified=not any('crossing' in e for e in errors),
            snapshot_prediction_max=max(snapshot_errors,default=0), snapshot_training_loss_max=max(loss_errors,default=0),
            endpoint_prediction_max=endpoint_error, initialization_deltas=init_deltas,
            basis_errors=basis_errors, basis_diagnostics=basis_diagnostics,
            raw_array_identity=data.identity, provenance=provenance,
            seconds=time.monotonic()-begin)
        endpoint_path.parent.mkdir(parents=True,exist_ok=True)
        np.save(endpoint_path,replay_endpoint,allow_pickle=False)
        save(record_path,result)
        return result,replay_endpoint

    def run_case(self,case):
        full = self.manifest['archive_cells'][case+'_full']
        reference = [self.replay(full[level],case,'full') for level in ('primary','refined')]
        full_delta = endpoint_delta(reference[0][1],reference[1][1])
        full_valid = all(x[0]['passed'] and x[0]['status']=='fitted' for x in reference) and full_delta<=.01
        rows = []
        methods = [f'{family}_p{p}' for family in ('new','ours','gaussian','orthogonal') for p in (1,3,5)]
        for method in methods:
            if method.startswith('new'):
                entries = new_entries(case,method,self.args.new_roots)
            else:
                item = self.manifest['archive_cells'][case+'_'+method]
                entries = [item[l] for l in ('primary','refined')]
            attempts = [self.replay(entry,case,method) for entry in entries]
            reasons = []
            if len(attempts)>2:
                check(len(attempts)==3,'more than one extra numerical attempt',reasons)
                check(all(x[0]['status']=='fitted' for x in attempts[:2]) and
                      endpoint_delta(attempts[0][1],attempts[1][1])>.01,
                      'extra numerical attempt did not satisfy frozen gate',reasons)
            if len(attempts)<2:
                reasons.append('fewer than two attempted numerical levels')
            selected = attempts[-2:]
            selected_entries = entries[-2:]
            row = dict(case=case,method=method.replace('ours_','old_'),attempt_paths=[e['directory'] for e in entries],
                       selected_paths=[e['directory'] for e in selected_entries],reasons=reasons,
                       full_refinement_max=full_delta,reference_valid=full_valid)
            if not full_valid:
                reasons.append('dense reference numerical/replay gate failed')
            if len(selected)==2:
                delta = endpoint_delta(selected[0][1],selected[1][1])
                row['refinement_max'] = delta
                if delta>.01:
                    reasons.append('model selected-pair maximum discrepancy exceeds .01')
                for level,(record,pred),(_,ref),entry in zip(('primary','refined'),selected,reference,selected_entries):
                    if record['status']!='fitted':
                        reasons.append(level+' status '+record['status'])
                    if not record['passed']:
                        reasons.append(level+' independent replay/provenance failure')
                    fine,coarse = metric(pred,ref),metric(pred[::2],ref[::2])
                    for k,value in fine.items():
                        row[level+'_'+k] = value
                        row[level+'_'+k+'_grid4096'] = coarse[k]
                        row[level+'_'+k+'_grid_change'] = abs(value-coarse[k])
                    row[level+'_path'] = entry['directory']
                    for k in ('rtol','atol','loss','time','status'):
                        row[level+'_'+k] = record[k]
            if case+'_'+method in self.manifest['known_invalid_archive_cells']:
                reasons.append('inherited unresolved numerical cell retained')
            row['valid'] = not reasons
            rows.append(row)
        result = dict(case=case,rows=rows,full_refinement_max=full_delta,
                      checker_sha256=sha(Path(__file__)),manifest_sha256=sha(HERE/'SUITE_MANIFEST.json'))
        save(self.args.out/'cases'/(case+'.json'),result)
        print(json.dumps(dict(completed_case=case,valid=sum(r['valid'] for r in rows),
                              remaining_seconds=self.remaining())),flush=True)
        return result


def compare(args, manifest):
    independent = {}
    for path in (args.out/'cases').glob('*.json'):
        for row in json.loads(path.read_text())['rows']:
            independent[(row['case'],row['method'])] = row
    other = []
    for path in args.compare:
        obj = json.loads(path.read_text())
        other.extend(obj if isinstance(obj,list) else obj['rows'])
    errors, differences = [], []
    for row in other:
        key = (row['case'],row['method'])
        if key not in independent:
            errors.append('Missing independent case/method '+str(key))
            continue
        own = independent[key]
        check(row['valid']==own['valid'], 'validity disagreement '+str(key), errors)
        for field in ('refinement_max','full_refinement_max'):
            if field in own and row.get(field) is not None:
                d = abs(own[field]-row[field]);differences.append(d)
                check(d<=TOL, 'metric disagreement '+str(key)+' '+field, errors)
        for level in ('primary','refined'):
            for met in ('rms','l1','mse','max_abs'):
                for suffix in ('','_grid4096','_grid_change'):
                    field = level+'_'+met+suffix
                    if field in own:
                        d=abs(own[field]-row[field]);differences.append(d)
                        check(d<=TOL,'metric disagreement '+str(key)+' '+field,errors)
            field=level+'_path'
            if field in own:
                check(Path(own[field]).resolve()==Path(row[field]).resolve(),
                      'selected path disagreement '+str(key)+' '+level,errors)
    result = dict(passed=not errors,errors=errors,rows_compared=len(other),
                  maximum_metric_discrepancy=max(differences,default=0),
                  independent_rows=len(independent),checker_sha256=sha(Path(__file__)),
                  comparison_file_hashes={str(p):sha(p) for p in args.compare})
    save(args.out/'comparison.json',result)
    print(json.dumps(result),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--new-roots',type=Path,nargs='+',default=[])
    p.add_argument('--cases',nargs='+')
    p.add_argument('--device',default='cuda:0')
    p.add_argument('--budget',type=float,default=100)
    p.add_argument('--compare',type=Path,nargs='+')
    args=p.parse_args()
    manifest=json.loads((HERE/'SUITE_MANIFEST.json').read_text())
    if args.compare:
        compare(args,manifest);return
    if not 0<args.budget<=100:
        p.error('Every GPU invocation must reserve at most100 seconds')
    if not args.new_roots:
        p.error('--new-roots required for replay')
    if args.cases and not set(args.cases)<=set(manifest['cases']):
        p.error('Only the frozen eleven cases are allowed')
    begin=time.monotonic()
    args._started=begin
    completed=[]
    status='complete'
    exception=None
    try:
        torch.set_num_threads(1)
        torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False
        torch.set_float32_matmul_precision('highest')
        torch.cuda.set_device(args.device)
        checker=Checker(args,manifest)
        for case in args.cases or manifest['cases']:
            checker.run_case(case)
            completed.append(case)
    except TimeoutError as exc:
        status='reservation_stop'
        print(str(exc),flush=True)
    except Exception as exc:
        status='failure'
        exception=repr(exc)
        raise
    finally:
        if torch.cuda.is_initialized():
            torch.cuda.synchronize(args.device)
        result=dict(status=status,exception=exception,seconds=time.monotonic()-begin,completed=completed,
                    reservation=args.budget,command=sys.argv,checker_sha256=sha(Path(__file__)))
        number=len(list(args.out.glob('completion_*.json')))+1
        save(args.out/f'completion_{number:03d}.json',result)
        print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
