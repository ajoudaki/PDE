"""Independent p7 saved-state audit; no producer or main-analyzer imports."""
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
os.environ.setdefault('PYTHONDONTWRITEBYTECODE','1')

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
import torch

import suite_independent_check as independent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GEN = ROOT/'data/generated/gradient_flow_probe_dictionary_20260921'
PRIOR = GEN/'suite_independent01'
PRIOR_HASH = '4f4c18ca42c13bead253edec758e0ddac5a1f86a12859f4637a18ce973ee4b54'
TOL = 1e-10
independent.NEW_DIMS[7] = (26,46)


def token_for(path):
    return hashlib.sha256(str(Path(path).resolve()).encode()).hexdigest()[:24]


def historical_entries(manifest,case,method):
    if method == 'full' or not method.startswith('new'):
        name = method.replace('old_','ours_')
        cell = manifest['archive_cells'][case+'_'+name]
        return [cell[level] for level in ('primary','refined')]
    previous = json.loads((PRIOR/'cases'/(case+'.json')).read_text())
    if previous['checker_sha256'] != PRIOR_HASH:
        raise ValueError('unrecognized prior independent case source')
    row = next(row for row in previous['rows'] if row['method']==method)
    entries = []
    for directory in row['attempt_paths']:
        raw = Path(directory)/'arrays.npz'
        record = json.loads((PRIOR/'replays'/(token_for(raw)+'.json')).read_text())
        entries.append(dict(directory=directory,arrays_path=str(raw),
                            summary_path=str(Path(directory)/'summary.json'),
                            config_path=record['provenance']['config_path'],
                            config_sha256=record['provenance']['config_sha256'],
                            rtol=record['rtol'],atol=record['atol'],new=True,
                            key=case+'_'+method))
    return entries


def authenticate_historical(entry,case,method,manifest,source_cache):
    path = Path(entry['arrays_path'])
    token = token_for(path)
    record_path,endpoint_path = PRIOR/'replays'/(token+'.json'),PRIOR/'replays'/(token+'.npy')
    record = json.loads(record_path.read_text())
    errors = []
    check = lambda condition,message:independent.check(condition,message,errors)
    check(independent.sha(HERE/'suite_independent_check.py')==PRIOR_HASH,'prior checker source changed')
    check(record['identity']['checker_sha256']==PRIOR_HASH,'prior source binding mismatch')
    check(Path(record['identity']['path']).resolve()==path.resolve(),'historical path mismatch')
    check(record['identity']['size']==path.stat().st_size and
          record['identity']['mtime_ns']==path.stat().st_mtime_ns,'historical raw file identity changed')
    data = independent.MappedNPZ(path)
    check(record['raw_array_identity']==data.identity,'historical NPZ member identity changed')
    check(record['case']==case and record['method'].replace('ours_','old_')==method,
          'historical case/method mismatch')
    check(record['passed'] and not record['errors'],'historical replay did not pass')
    provenance = independent.sources(entry,case,manifest,source_cache)
    errors.extend(provenance['errors'])
    check(provenance['config_sha256']==record['provenance']['config_sha256'],
          'historical checked configuration changed')
    summary = json.loads(Path(entry['summary_path']).read_text())
    for field in ('status','loss','time','rtol','atol'):
        check(record[field]==summary[field],'historical summary changed '+field)
    endpoint = np.load(endpoint_path,allow_pickle=False)
    check(endpoint.shape==(8192,) and np.isfinite(endpoint).all(),'historical endpoint invalid')
    endpoint_error = independent.peak(endpoint-data['endpoint_prediction'])
    check(endpoint_error<=TOL,'historical independent endpoint differs from archived state endpoint')
    proof = dict(path=str(path),prior_record_path=str(record_path),
                 prior_record_sha256=independent.sha(record_path),
                 prior_endpoint_path=str(endpoint_path),prior_endpoint_sha256=independent.sha(endpoint_path),
                 endpoint_consistency_error=endpoint_error,errors=errors,passed=not errors,
                 current_provenance=provenance)
    return dict(record,passed=not errors,errors=errors),endpoint,proof


class Checker(independent.Checker):
    @torch.no_grad()
    def new_basis(self,order):
        if order != 7:
            return super().new_basis(order)
        if order not in self.basis_cache:
            from pde.observable_torch_p1 import TensorState
            from new_dictionary_p7 import raw_features
            from new_dictionary_p45 import raw_features as raw_p5
            initial = TensorState(*(self.initial[k] for k in ('w','c','M')))
            raw1,raw2,meta = raw_features(initial,7)
            old1,old2,_ = raw_p5(initial,5)
            if not torch.equal(raw1[:,:14],old1) or not torch.equal(raw2[:,:24],old2):
                raise ValueError('inherited p5 raw prefix changed')
            bases,diagnostics = [],[]
            for raw in (raw1,raw2):
                gram = raw.T@raw/2048
                regular = (gram+gram.T)/2+torch.eye(raw.shape[1],device=raw.device,dtype=raw.dtype)/65536
                chol = torch.linalg.cholesky(regular)
                inverse_transpose = torch.linalg.solve(chol.T,torch.eye(
                    len(chol),device=chol.device,dtype=chol.dtype))
                basis = raw@inverse_transpose
                eig = torch.linalg.eigvalsh(regular)
                diagnostics.append(dict(condition=float(eig[-1]/eig[0]),
                    triangular_relative_residual=float(torch.linalg.norm(basis@chol.T-raw)/torch.linalg.norm(raw)),
                    raw_prefix_exact=True,raw_shape=list(raw.shape)))
                bases.append(basis)
            self.basis_cache[7] = (bases,diagnostics,meta)
        return self.basis_cache[7]

    def replay(self,entry,case,method):
        token = token_for(entry['arrays_path'])
        record_path = self.args.out/'replays'/(token+'.json')
        source_hash = independent.sha(Path(__file__))
        if record_path.exists():
            prior = json.loads(record_path.read_text())
            if prior.get('p7_checker_sha256') != source_hash:
                raise ValueError('stale p7 checker replay cache')
        record,endpoint = super().replay(entry,case,method)
        config = json.loads(Path(entry['config_path']).read_text())
        required = ('new_dictionary_p7.py','p7_gaussian_check.py','p7_run.py',
                    'P7_PROTOCOL.md','P7_DICTIONARY_SPEC.md')
        for name in required:
            path = str((HERE/name).relative_to(ROOT))
            independent.check(path in config['source_hashes'],
                              'missing p7 executed/configuration dependency '+path,record['errors'])
        record['passed'] = not record['errors']
        record['p7_checker_sha256'] = source_hash
        independent.save(record_path,record)
        return record,endpoint

    def historical(self,entry,case,method):
        record,endpoint,proof = authenticate_historical(entry,case,method,self.manifest,self.source_cache)
        independent.save(self.args.out/'historical_bindings'/(token_for(entry['arrays_path'])+'.json'),proof)
        return record,endpoint

    def row(self,case,method,entries,attempts,references,full_delta):
        reasons = []
        if len(attempts)<2:
            reasons.append('fewer than two numerical attempts')
        if method=='new_p7' and len(attempts)>2:
            if len(attempts)!=3:
                reasons.append('more than one permitted extra attempt')
            if not (all(item[0]['status']=='fitted' for item in attempts[:2]) and
                    independent.endpoint_delta(attempts[0][1],attempts[1][1])>.01):
                reasons.append('extra attempt did not satisfy frozen trigger')
        selected,paths = attempts[-2:],[entry['directory'] for entry in entries[-2:]]
        full_valid = all(record['passed'] and record['status']=='fitted' for record,_ in references) and full_delta<=.01
        if not full_valid:
            reasons.append('dense reference numerical/replay gate failed')
        row = dict(case=case,method=method,attempt_paths=[entry['directory'] for entry in entries],
                   selected_paths=paths,full_refinement_max=full_delta,reference_valid=full_valid,reasons=reasons)
        if len(selected)==2:
            row['refinement_max'] = independent.endpoint_delta(selected[0][1],selected[1][1])
            if row['refinement_max']>.01:
                reasons.append('selected-pair maximum discrepancy exceeds .01')
            for level,(record,pred),(_,ref),path in zip(('primary','refined'),selected,references,paths):
                if record['status']!='fitted':
                    reasons.append(level+' status '+record['status'])
                if not record['passed']:
                    reasons.append(level+' independent replay/provenance failed')
                fine,coarse = independent.metric(pred,ref),independent.metric(pred[::2],ref[::2])
                for key,value in fine.items():
                    row[level+'_'+key] = value
                    row[level+'_'+key+'_grid4096'] = coarse[key]
                    row[level+'_'+key+'_grid_change'] = abs(value-coarse[key])
                row[level+'_path'] = path
                for key in ('rtol','atol','loss','time','status'):
                    row[level+'_'+key] = record[key]
        if case+'_'+method.replace('old_','ours_') in self.manifest['known_invalid_archive_cells']:
            reasons.append('inherited unresolved numerical cell')
        row['valid'] = not reasons
        return row

    def run_case(self,case):
        refs = [self.historical(entry,case,'full') for entry in historical_entries(self.manifest,case,'full')]
        full_delta = independent.endpoint_delta(refs[0][1],refs[1][1])
        rows = []
        entries = independent.new_entries(case,'new_p7',self.args.new_roots)
        attempts = [self.replay(entry,case,'new_p7') for entry in entries]
        rows.append(self.row(case,'new_p7',entries,attempts,refs,full_delta))
        for method in ('new_p5','old_p3','gaussian_p3','orthogonal_p3'):
            entries = historical_entries(self.manifest,case,method)
            attempts = [self.historical(entry,case,method) for entry in entries]
            rows.append(self.row(case,method,entries,attempts,refs,full_delta))
        comparisons = []
        new = rows[0]
        for old in rows[1:]:
            valid = new['valid'] and old['valid']
            winners = [None,None]
            if valid:
                winners = ['new_p7' if new[level+'_rms']<old[level+'_rms'] else
                           old['method'] if new[level+'_rms']>old[level+'_rms'] else 'tie'
                           for level in ('primary','refined')]
            comparisons.append(dict(case=case,new_method='new_p7',other_method=old['method'],
                new_vectors=72,other_vectors=38 if old['method']=='new_p5' else 45,
                valid=valid,primary_winner=winners[0],refined_winner=winners[1],
                resolved=valid and winners[0]==winners[1] and winners[0]!='tie',
                reasons=[] if valid else list(dict.fromkeys(new['reasons']+old['reasons']))))
        result = dict(case=case,rows=rows,comparisons=comparisons,
                      checker_sha256=independent.sha(Path(__file__)),
                      manifest_sha256=independent.sha(HERE/'SUITE_MANIFEST.json'))
        independent.save(self.args.out/'cases'/(case+'.json'),result)
        print(json.dumps(dict(completed_case=case,p7_valid=rows[0]['valid'],remaining_seconds=self.remaining())),flush=True)
        return result


def prepare(args,manifest):
    cache,proofs = {},[]
    for case in manifest['cases']:
        for method in ('full','new_p5','old_p3','gaussian_p3','orthogonal_p3'):
            for entry in historical_entries(manifest,case,method):
                _,_,proof = authenticate_historical(entry,case,method,manifest,cache)
                proofs.append(proof)
    result = dict(passed=all(proof['passed'] for proof in proofs),historical_trajectories=len(proofs),
                  errors=[dict(path=proof['path'],errors=proof['errors']) for proof in proofs if proof['errors']],
                  bindings=proofs,checker_sha256=independent.sha(Path(__file__)),GPU_used=False)
    independent.save(args.out/'preparation.json',result)
    print(json.dumps({key:result[key] for key in ('passed','historical_trajectories','errors','GPU_used')}))


def compare(args):
    own = {}
    for path in (args.out/'cases').glob('*.json'):
        for row in json.loads(path.read_text())['rows']:
            own[(row['case'],row['method'])] = row
    errors,deltas,covered = [],[],set()
    for path in args.compare:
        obj = json.loads(path.read_text())
        rows = obj if isinstance(obj,list) else obj['rows']
        for other in rows:
            key = other['case'],other['method'].replace('ours_','old_')
            if key not in own:
                continue
            row = own[key]
            covered.add(key)
            independent.check(row['valid']==other['valid'],'validity mismatch '+str(key),errors)
            for field in ('full_refinement_max','refinement_max'):
                if field in row and other.get(field) is not None:
                    delta=abs(row[field]-other[field]);deltas.append(delta)
                    independent.check(delta<=TOL,'metric mismatch '+str(key)+' '+field,errors)
            for level in ('primary','refined'):
                field=level+'_path'
                if field in row:
                    independent.check(Path(row[field]).resolve()==Path(other[field]).resolve(),
                                      'selected path mismatch '+str(key)+' '+field,errors)
                for metric in ('rms','l1','mse','max_abs'):
                    for suffix in ('','_grid4096','_grid_change'):
                        field=level+'_'+metric+suffix
                        if field in row:
                            delta=abs(row[field]-other[field]);deltas.append(delta)
                            independent.check(delta<=TOL,'metric mismatch '+str(key)+' '+field,errors)
    missing = [key for key in own if key[1]=='new_p7' and key not in covered]
    errors.extend('p7 row missing from main comparison '+str(key) for key in missing)
    result = dict(passed=not errors,errors=errors,compared_rows=len(covered),
                  maximum_metric_discrepancy=max(deltas,default=0),
                  comparison_hashes={str(path):independent.sha(path) for path in args.compare},
                  checker_sha256=independent.sha(Path(__file__)))
    independent.save(args.out/'comparison.json',result)
    print(json.dumps(result))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--new-roots',type=Path,nargs='+',default=[])
    parser.add_argument('--cases',nargs='+')
    parser.add_argument('--device',default='cuda:0')
    parser.add_argument('--budget',type=float,default=95)
    parser.add_argument('--prepare',action='store_true')
    parser.add_argument('--compare',type=Path,nargs='+')
    args=parser.parse_args()
    manifest=json.loads((HERE/'SUITE_MANIFEST.json').read_text())
    if args.prepare:
        prepare(args,manifest);return
    if args.compare:
        compare(args);return
    if not 0<args.budget<=100:
        parser.error('GPU audit budget must be positive and at most100 seconds')
    if not args.new_roots:
        parser.error('--new-roots required')
    if args.cases and not set(args.cases)<=set(manifest['cases']):
        parser.error('only frozen eleven cases allowed')
    args._started=time.monotonic()
    status,completed,exception='complete',[],None
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
        status,exception='failure',repr(exc)
        raise
    finally:
        if torch.cuda.is_initialized():
            torch.cuda.synchronize(args.device)
        result=dict(status=status,exception=exception,seconds=time.monotonic()-args._started,
                    completed=completed,reservation=args.budget,command=sys.argv,
                    checker_sha256=independent.sha(Path(__file__)))
        number=len(list(args.out.glob('completion_*.json')))+1
        independent.save(args.out/f'completion_{number:03d}.json',result)
        print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
