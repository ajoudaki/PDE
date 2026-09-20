"""Independent deterministic CUDA preflight; no optimization trajectory."""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
import matched_network_benchmark as producer
from benchmark import ClosureEngine, NetworkEngine, torch


EXPECTED = {
    1: (5, 3, 3087, 55, 3190, 11279, 105, 11340),
    3: (35, 10, 3422, 58, 3538, 49502, 221, 49504),
    5: (128, 21, 5760, 75, 5850, 158336, 397, 158800),
}


def close(actual, expected, *, atol=1e-11, rtol=1e-10):
    if actual.shape != expected.shape:
        raise AssertionError((actual.shape, expected.shape))
    residual = (actual-expected).abs()
    tolerance = atol + rtol*expected.abs()
    if not bool(torch.isfinite(actual).all()) or bool((residual > tolerance).any()):
        raise AssertionError(f"residual {float(residual.max())} exceeds tolerance")
    return float(residual.max())


def perturbed(engine, state):
    """Nondegenerate derivative probe, specified without integrating a flow."""
    def pattern(array, amplitude):
        return array + amplitude*torch.arange(array.numel(), device=array.device,
                         dtype=array.dtype).reshape(array.shape).sin()
    return engine.state(pattern(state.w, .03), pattern(state.c, .15),
                        pattern(state.M, .01/math.sqrt(len(state.w))))


def autograd_check(engine, state, inputs, labels):
    data = engine.prepare_data(inputs, labels,
        probabilities=torch.arange(1, len(inputs)+1, device=inputs.device,
                                   dtype=inputs.dtype)/(len(inputs)*(len(inputs)+1)/2))
    w, c, middle = [getattr(state, k).clone().requires_grad_() for k in ('w','c','M')]
    first = torch.tanh(inputs @ w.T)
    second = torch.tanh(first @ middle.T)
    output = second @ c / len(c)
    loss = torch.sum(data.probabilities*(output-data.labels)**2)
    gradients = torch.autograd.grad(loss, (w,c,middle))
    rhs = engine.rhs(state, data)
    result = {'prediction':close(engine.predict(state, inputs), output.detach()),
              'loss':close(engine.loss(state,data).reshape(1),loss.detach().reshape(1))}
    for name, gradient, mobility in zip(('w','c','M'),gradients,(len(c),len(c),1)):
        result[name] = close(getattr(rhs,name), -mobility*gradient)
    return result


def independent_raw(initial, order, dimension):
    """Chebyshev cos(k acos(x)) values with independently enumerated powers."""
    lower = torch.tanh(initial.w)
    upper = torch.tanh(initial.M @ lower)
    reverse = torch.tanh(initial.M.T @ upper)
    coordinates = torch.cat((lower,reverse),1) if dimension == 4 else upper
    powers = sorted((p for p in itertools.product(range(order+1), repeat=dimension)
                     if sum(p)<=order), key=lambda p:(sum(p),tuple(-x for x in p)))
    angles = torch.acos(coordinates)
    columns = [torch.cos(angles*torch.tensor(power,device=coordinates.device,
                    dtype=coordinates.dtype)).prod(1) for power in powers]
    if order == 5 and dimension == 4:
        one = torch.ones(len(initial.w),device=coordinates.device,dtype=coordinates.dtype)
        columns.extend((one*math.sin(1.),one*math.cos(1.)))
    return torch.stack(columns,1)


def preflight(device, out):
    started = time.monotonic()
    out.mkdir(parents=True,exist_ok=False)
    producer.setup(device)
    before = producer.producer_hashes()
    specs = producer.specifications()
    assert list(producer.CASES) == ['quadrant_alternating','two_outliers_alternating']
    assert producer.WIDTH == 1024 and producer.SEED == 20260920
    net = NetworkEngine(2,1024,20260920,device=device,dtype=torch.float64,block_size=256)
    initial = net.initial_state()
    angles = torch.tensor(producer.CASES['two_outliers_alternating']['angles_degrees'],
                          device=device,dtype=torch.float64)*(math.pi/180)
    inputs = torch.stack((angles.cos(),angles.sin()),1)
    labels = producer.CASES['two_outliers_alternating']['labels']
    results = {'counts':{},'small_networks':{},'dictionary':{}}
    for order,(k1,k2,trained,train_width,train_count,total,total_width,total_count) in EXPECTED.items():
        ours = specs[f'ours_p{order}']
        assert ours['dictionary_dimensions'] == [k1,k2]
        assert ours['trainable_parameters'] == trained == 3*1024+k1*k2
        assert ours['model_parameters'] == total == 1024*(k1+k2)+trained
        results['counts'][str(order)] = dict(trainable=trained,total=total)
        for match,budget,width,count in [('trainable',trained,train_width,train_count),
                                         ('total',total,total_width,total_count)]:
            spec = specs[f'small_{match}_p{order}']
            assert spec['width'] == width and spec['trainable_parameters'] == count
            assert count == width**2+3*width and (width-1)**2+3*(width-1)<budget<=count
            engine,state = producer.small_network(initial,width)
            assert sum(getattr(state,name).numel() for name in ('w','c','M')) == count
            coupling = {
                'w':close(state.w,initial.w[:width],atol=0,rtol=0),
                'c':close(state.c,initial.c[:width]*(1024/width),atol=0,rtol=0),
                'M':close(state.M,initial.M[:width,:width]*math.sqrt(1024/width),atol=0,rtol=0),
            }
            for name in ('w','c','M'):
                assert getattr(state,name).data_ptr() != getattr(initial,name).data_ptr()
                assert getattr(state,name).data_ptr() != getattr(engine.initial,name).data_ptr()
            observations = engine.observations(state,inputs)
            assert float(observations['rms1']) == float(observations['rms2']) == 0.
            results['small_networks'][f'{match}_p{order}'] = dict(width=width,
                count=count,coupling_residuals=coupling,initial_hidden_rms=[0.,0.],
                gradient_residuals=autograd_check(engine,perturbed(engine,state),inputs,labels))
        closure,state = producer.build(initial,order,'ours')
        assert state.w.shape == (1024,2) and state.c.shape == (1024,)
        assert state.M.shape == (k2,k1)
        populations = []
        for basis,dimension in ((closure.b1,4),(closure.b2,2)):
            raw = independent_raw(initial,order,dimension)
            ridge = 1/(1024*(order+1)**2)
            gram = raw.T @ raw / 1024
            cholesky = torch.linalg.cholesky(gram+ridge*torch.eye(raw.shape[1],
                                        device=device,dtype=torch.float64))
            residual = close(cholesky @ basis.T,raw.T,atol=1e-8,rtol=0)
            spectrum = torch.linalg.eigvalsh(gram)
            condition = float((spectrum[-1]+ridge)/(spectrum[0]+ridge))
            assert condition <= 1e10
            populations.append(dict(raw_shape=list(raw.shape),triangular_residual=residual,
                                    ridge_condition=condition))
        action_residual = close(state.M,closure.b2.T @ initial.M @ closure.b1 / 1024)
        obs = closure.observations(state,inputs,include_grams=False)
        assert float(obs['rms1']) == float(obs['rms2']) == 0.
        results['dictionary'][str(order)] = dict(populations=populations,
            action_residual=action_residual,initial_hidden_rms=[0.,0.])
    # Complete bases make the closure exactly the dense physical network.
    dense = NetworkEngine(2,11,7319,device=device,dtype=torch.float64,block_size=3)
    dense_initial = dense.initial_state()
    basis = math.sqrt(11)*torch.eye(11,device=device,dtype=torch.float64)
    closure = ClosureEngine(basis,dense_initial.w,basis,dense_initial.M,
                            device=device,dtype=torch.float64,block_size=3)
    dense_state = perturbed(dense,dense_initial)
    closure_state = closure.state(dense_state.w,dense_state.c,dense_state.M)
    dense_data = dense.prepare_data(inputs,labels)
    closure_data = closure.prepare_data(inputs,labels)
    dense_rhs = dense.rhs(dense_state,dense_data)
    closure_rhs = closure.rhs(closure_state,closure_data)
    results['full_basis_identity'] = {'width':11,
        'prediction':close(closure.predict(closure_state,inputs),dense.predict(dense_state,inputs)),
        **{name:close(getattr(closure_rhs,name),getattr(dense_rhs,name)) for name in ('w','c','M')}}
    after = producer.producer_hashes()
    assert before == after, 'checked sources changed during preflight'
    torch.cuda.synchronize(device)
    record = dict(status='PASS',training_run=False,device=device,
        gpu=torch.cuda.get_device_name(device),torch=str(torch.__version__),
        python=sys.version,command=sys.argv,source_hashes=before,
        seconds=time.monotonic()-started,checks=results)
    (out/'preflight.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status='PASS',training_run=False,seconds=record['seconds'],
                         output=str(out/'preflight.json'))),flush=True)


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


@torch.no_grad()
def raw_prediction(state, inputs, bases=None):
    """Reconstruct the saved formula directly, without either engine predictor."""
    w,c,middle = state
    values = []
    for start in range(0,len(inputs),256):
        hidden = torch.tanh(inputs[start:start+256] @ w.T)
        if bases is None:
            second = torch.tanh(hidden @ middle.T)
        else:
            b1,b2 = bases
            moments = hidden @ b1 / len(w)
            second = torch.tanh((moments @ middle.T) @ b2.T)
        values.append(second @ c / len(c))
    return torch.cat(values)


def replay(device, out, roots):
    """Replay raw saved states, then independently compare selected endpoints."""
    started = time.monotonic()
    out.mkdir(parents=True,exist_ok=False)
    producer.setup(device)
    before = producer.producer_hashes()
    reference = NetworkEngine(2,1024,20260920,device=device,dtype=torch.float64)
    initial = reference.initial_state()
    cases = producer.CASES
    specifications = producer.specifications()
    attempts, endpoint_arrays, configurations, failures = [], {}, [], []
    def tensor(value):
        return torch.as_tensor(value,device=device,dtype=torch.float64)
    def require(condition, explanation):
        if not condition:
            raise AssertionError(explanation)
    for root in roots:
        configs = sorted(root.glob('config_worker*.json'))
        require(bool(configs),f'no configurations: {root}')
        for config_path in configs:
            config = json.loads(config_path.read_text())
            require(config['network_seed']==20260920 and config['width']==1024,'initialization contract')
            level = config['level']
            require(config['rtol']==6.25e-5/4**level and config['atol']==6.25e-7/4**level,'tolerances')
            require(config['models']==specifications,'specification mismatch')
            require(config['cases']==cases and config['case'] in cases,'case mismatch')
            require(config['circle_nodes']==2048 and config['endpoint_nodes']==8192,'grid counts')
            require(config['threshold']==.001 and config['max_time']==10000. and config['max_steps']==30000,'stopping contract')
            require(config['protocol_sha256']==file_hash(producer.PROTOCOL),'protocol hash')
            for name,digest in config['source_hashes'].items():
                require(file_hash(producer.ROOT/name)==digest,f'source changed: {name}')
            completion_path = root/f"completion_worker{config['worker']}.json"
            completion = json.loads(completion_path.read_text())
            require(completion['exit_status']==0 and completion['planned_cells']==config['selected_cells'],'worker completion')
            configurations.append(dict(path=str(config_path),sha256=file_hash(config_path),
                completion_path=str(completion_path),completion_sha256=file_hash(completion_path),
                actual_worker_seconds=completion['seconds'],level=level))
            case = config['case']
            case_angles = tensor(cases[case]['angles_degrees'])*(math.pi/180)
            training_inputs = torch.stack((case_angles.cos(),case_angles.sin()),1)
            labels = tensor(cases[case]['labels'])
            for cell in config['selected_cells']:
                name = cell[len(case)+1:]
                require(name in specifications and cell.startswith(case+'_'),'unexpected cell')
                key = (case,name,level)
                require(key not in endpoint_arrays,'duplicate case/model/level')
                endpoint_arrays[key] = None
                directory = root/cell
                summary_path = directory/'summary.json'
                summary = json.loads(summary_path.read_text())
                attempt = dict(case=case,model=name,level=level,status=summary['status'],
                    path=str(directory),summary_sha256=file_hash(summary_path),replay_pass=False)
                attempts.append(attempt)
                if not (directory/'arrays.npz').exists():
                    attempt['failure'] = 'No raw checkpoint; attempt retained as invalid.'
                    failures.append(dict(case=case,model=name,level=level,reason=attempt['failure']))
                    continue
                try:
                    with np.load(directory/'arrays.npz',allow_pickle=False) as archive:
                        arrays = {name:archive[name] for name in archive.files}
                        for arrayname in arrays:
                            require(np.isfinite(arrays[arrayname]).all(),f'nonfinite array {arrayname}')
                        spec = specifications[name]
                        width = spec['width']
                        snapshots = len(arrays['snapshot_times'])
                        require(arrays['w'].shape==(snapshots,width,2),'w shape')
                        require(arrays['c'].shape==(snapshots,width),'c shape')
                        shape = tuple(reversed(spec['dictionary_dimensions'])) if spec['method']=='ours' else (width,width)
                        require(arrays['M'].shape==(snapshots,*shape),'M shape')
                        require(snapshots>=1 and arrays['snapshot_times'][0]==0,'initial checkpoint')
                        require(abs(arrays['snapshot_times'][-1]-summary['time'])<=1e-10,'final checkpoint time')
                        require(len(arrays['times'])==len(arrays['losses'])==summary['steps']+1,'trace lengths')
                        require(len(arrays['accepted_steps'])==summary['steps'],'accepted step count')
                        require(np.all(np.diff(arrays['times'])>0),'strictly increasing time')
                        require(np.max(np.abs(np.diff(arrays['times'])-arrays['accepted_steps']),initial=0.)<=1e-9,'accepted time increments')
                        require(np.all(arrays['local_error_ratios']<=1.),'accepted local error ratios')
                        require(np.all((arrays['accepted_steps']>0)&(arrays['accepted_steps']<=2.)),'accepted step bounds')
                        require(np.max(np.diff(arrays['losses']),initial=-np.inf)<=1e-8*np.max(arrays['losses'])+1e-12,'loss monotonicity')
                        require(abs(arrays['times'][-1]-summary['time'])<=1e-10,'trace time')
                        require(abs(arrays['losses'][-1]-summary['loss'])<=1e-12,'summary loss')
                        count = 2*width+width+shape[0]*shape[1]
                        require(count==spec['trainable_parameters']==summary['actual_trainable_parameters'],'trainable count')
                        bases = None
                        state0 = tuple(tensor(arrays[k][0]) for k in ('w','c','M'))
                        if spec['method']=='ours':
                            bases = tensor(arrays['b1']),tensor(arrays['b2'])
                            require(sum(b.numel() for b in bases)+count==spec['model_parameters'],'model count')
                            close(state0[0],initial.w,atol=0,rtol=0)
                            close(state0[1],initial.c,atol=0,rtol=0)
                            close(tensor(arrays['g']),initial.w,atol=0,rtol=0)
                            close(tensor(arrays['D']),state0[2],atol=0,rtol=0)
                            close(tensor(arrays['p1']),torch.full((1024,),1/1024,device=device,dtype=torch.float64),atol=0,rtol=0)
                            close(tensor(arrays['p2']),torch.full((1024,),1/1024,device=device,dtype=torch.float64),atol=0,rtol=0)
                            dictionary_checks = []
                            for basis,dimension in zip(bases,(4,2)):
                                raw = independent_raw(initial,spec['p'],dimension)
                                require(basis.shape==raw.shape,'basis shape')
                                ridge = 1/(1024*(spec['p']+1)**2)
                                gram = raw.T@raw/1024
                                lower = torch.linalg.cholesky(gram+ridge*torch.eye(raw.shape[1],device=device,dtype=torch.float64))
                                residual = close(lower@basis.T,raw.T,atol=1e-8,rtol=0)
                                eigenvalues = torch.linalg.eigvalsh(gram)
                                condition = float((eigenvalues[-1]+ridge)/(eigenvalues[0]+ridge))
                                require(condition<=1e10,'ridge condition')
                                dictionary_checks.append(dict(triangular_residual=residual,ridge_condition=condition))
                            close(state0[2],bases[1].T@initial.M@bases[0]/1024,atol=1e-10,rtol=0)
                            attempt['dictionary_checks'] = dictionary_checks
                            expected_bytes = 8*(2*1024*sum(spec['dictionary_dimensions'])+7*1024+2*shape[0]*shape[1])
                        else:
                            close(state0[0],initial.w[:width],atol=0,rtol=0)
                            close(state0[1],initial.c[:width]*(1024/width),atol=0,rtol=0)
                            close(state0[2],initial.M[:width,:width]*math.sqrt(1024/width),atol=0,rtol=0)
                            expected_bytes = 16*count
                        require(summary['actual_model_parameters']==spec['model_parameters'],'recorded model count')
                        require(summary['retained_bytes']==expected_bytes,'engine retained bytes')
                        close(tensor(arrays['training_inputs']),training_inputs,atol=1e-14,rtol=0)
                        close(tensor(arrays['labels']),labels,atol=0,rtol=0)
                        grids = {}
                        for prefix,size in (('circle',2048),('endpoint',8192)):
                            angles = torch.arange(size,device=device,dtype=torch.float64)*(2*math.pi/size)
                            grid = torch.stack((angles.cos(),angles.sin()),1)
                            close(tensor(arrays[prefix+'_angles']),angles,atol=0,rtol=0)
                            close(tensor(arrays[prefix+'_inputs']),grid,atol=0,rtol=0)
                            grids[prefix]=grid
                        prediction_error = 0.
                        for index in range(snapshots):
                            state = tuple(tensor(arrays[k][index]) for k in ('w','c','M'))
                            prediction_error = max(prediction_error,close(raw_prediction(state,grids['circle'],bases),
                                tensor(arrays['circle_predictions'][index]),atol=1e-10,rtol=0))
                        final_state = tuple(tensor(arrays[k][-1]) for k in ('w','c','M'))
                        endpoint = raw_prediction(final_state,grids['endpoint'],bases)
                        endpoint_error = close(endpoint,tensor(arrays['endpoint_prediction']),atol=1e-10,rtol=0)
                        initial_loss = torch.mean((raw_prediction(state0,training_inputs,bases)-labels)**2)
                        final_loss = torch.mean((raw_prediction(final_state,training_inputs,bases)-labels)**2)
                        require(abs(float(initial_loss)-arrays['losses'][0])<=1e-10,'initial loss replay')
                        require(abs(float(final_loss)-arrays['losses'][-1])<=1e-10,'final loss replay')
                        require(abs(float(initial_loss)-summary['initial_loss'])<=1e-10,'initial summary loss')
                        if summary['status']=='fitted':
                            require(float(final_loss)<=.001+1e-10,'fit threshold')
                            require(np.all(arrays['losses'][:-1]>.001),'first recorded threshold crossing')
                        endpoint_arrays[key]=endpoint.cpu().numpy()
                        attempt.update(replay_pass=True,actual_trainable=count,
                            actual_model=spec['model_parameters'],retained_bytes=expected_bytes,
                            max_snapshot_prediction_residual=prediction_error,
                            endpoint_prediction_residual=endpoint_error,
                            initial_loss=float(initial_loss),final_loss=float(final_loss),
                            arrays_sha256=file_hash(directory/'arrays.npz'))
                except (AssertionError,ValueError,RuntimeError,KeyError) as exc:
                    attempt['failure']=f'{type(exc).__name__}: {exc}'
                    failures.append(dict(case=case,model=name,level=level,reason=attempt['failure']))
    selections = {}
    for case in cases:
        for name in specifications:
            cells = sorted((a for a in attempts if a['case']==case and a['model']==name),key=lambda a:a['level'])
            chosen = cells[-2:]
            key = case+'/'+name
            valid = len(chosen)==2 and all(a['replay_pass'] and a['status']=='fitted' for a in chosen)
            difference = None
            if valid:
                endpoints = [endpoint_arrays[(case,name,a['level'])] for a in chosen]
                difference = float(np.max(np.abs(endpoints[1]-endpoints[0])))
                valid = difference<=.01
            selections[key]=dict(case=case,model=name,selected_levels=[a['level'] for a in chosen],
                selected_statuses=[a['status'] for a in chosen],
                selected_paths=[a['path'] for a in chosen],
                refinement_maximum=difference,valid=valid)
    def metrics(left,right,stride):
        delta = left[::stride]-right[::stride]
        return dict(l1=float(np.mean(np.abs(delta))),rms=float(np.sqrt(np.mean(delta**2))),
                    squared_rms=float(np.mean(delta**2)),sampled_maximum=float(np.max(np.abs(delta))))
    comparisons=[]
    for case in cases:
        full = selections[case+'/full']
        for order in (1,3,5):
            ours = selections[f'{case}/ours_p{order}']
            for match in ('trainable','total'):
                small = selections[f'{case}/small_{match}_p{order}']
                valid = full['valid'] and ours['valid'] and small['valid']
                record = dict(case=case,p=order,match=match,valid=valid,levels=[])
                for position in range(2):
                    if any(len(item['selected_levels'])!=2 for item in (full,ours,small)):
                        continue
                    keys = [(case,item['model'],item['selected_levels'][position]) for item in (full,ours,small)]
                    if any(endpoint_arrays.get(key) is None for key in keys):
                        continue
                    reference_values,ours_values,small_values = [endpoint_arrays[key] for key in keys]
                    record['levels'].append(dict(position=position,
                        numeric_levels=dict(zip(('full','ours','small'),[key[2] for key in keys])),
                        ours_8192=metrics(ours_values,reference_values,1),
                        small_8192=metrics(small_values,reference_values,1),
                        ours_4096=metrics(ours_values,reference_values,2),
                        small_4096=metrics(small_values,reference_values,2)))
                signs=[item['ours_8192']['rms']<item['small_8192']['rms'] for item in record['levels']]
                reverse=[item['ours_8192']['rms']>item['small_8192']['rms'] for item in record['levels']]
                record['decision']=('ours_lower' if len(signs)==2 and all(signs) else
                    'small_lower' if len(reverse)==2 and all(reverse) else 'inconclusive') if valid else 'inconclusive'
                comparisons.append(record)
    require(before==producer.producer_hashes(),'checker sources changed during replay')
    torch.cuda.synchronize(device)
    report=dict(status='PASS' if not failures else 'FAIL',training_run=False,
        checked_attempts=len(attempts),replayed_attempts=sum(a['replay_pass'] for a in attempts),
        failures=failures,source_hashes=before,configurations=configurations,attempts=attempts,
        selections=selections,comparisons=comparisons,device=device,
        gpu=torch.cuda.get_device_name(device),torch=str(torch.__version__),python=sys.version,
        command=sys.argv,seconds=time.monotonic()-started)
    (out/'independent.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'],training_run=False,checked=report['checked_attempts'],
        replayed=report['replayed_attempts'],failures=failures,seconds=report['seconds'])),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--device',default='cuda:1')
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--runs',type=Path,nargs='+',help='Replay finished run roots; never train.')
    args = parser.parse_args()
    if args.runs:
        replay(args.device,args.out,args.runs)
    else:
        preflight(args.device,args.out)


if __name__ == '__main__':
    main()
