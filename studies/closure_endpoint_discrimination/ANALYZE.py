"""Frozen-contract endpoint diagnostics; reads this study's saved trajectories only.

Public interfaces: analyze_screen(inputs_path, job_dirs_by_order) and
analyze_confirmation(manifest_or_path). No simulation or checkpoint mutation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from itertools import combinations

import numpy as np

THRESHOLDS = dict(visible_rms=.075, visible_max=.15, plateau_max=.005,
                  plateau_loss=.0005, drift100_max=.01, quadrature_max=.025,
                  step_precision_max=.002, control_loss=.001,
                  uncertainty_factor=5., train_loss=.005, train_pair_rms=.02,
                  worse_rmse=.025, max_loss_increase=1e-5, gram_psd=1e-5)


def _jsonable(value):
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, float) and not np.isfinite(value):
        return None
    return value


def _read_npz(path):
    with np.load(path, allow_pickle=False) as source:
        return {key: source[key].copy() for key in source.files}


def load_inputs(path):
    inputs = _read_npz(path)
    m = len(inputs['labels'])
    for key in ('train_u', 'probabilities', 'train_theta', 'circle_theta',
                'dense_theta', 'gap_mask', 'gap_dense_mask'):
        if key not in inputs:
            raise ValueError(f'Missing input array {key}')
    if inputs['train_u'].shape != (m, 2):
        raise ValueError('Training direction shape is not (m,2)')
    if not all(np.all(np.isfinite(v)) for v in inputs.values()
               if np.issubdtype(v.dtype, np.number)):
        raise ValueError('Nonfinite input data')
    w = inputs['probabilities']
    if np.any(w <= 0) or not np.allclose(w, 1 / m, rtol=0, atol=1e-14):
        raise ValueError('The frozen training law requires positive uniform unit weights')
    for name in ('circle', 'dense'):
        theta = inputs[f'{name}_theta']
        steps = np.diff(np.r_[theta, theta[0] + 2 * np.pi])
        if not np.allclose(steps, 2*np.pi/len(theta), rtol=0, atol=1e-10):
            raise ValueError(f'{name} panel is not uniformly spaced')
        degrees = np.mod(np.rad2deg(theta), 360)
        expected = ((degrees > 104) & (degrees < 166)) | ((degrees > 284) & (degrees < 346))
        mask_key = 'gap_mask' if name == 'circle' else 'gap_dense_mask'
        if not np.array_equal(inputs[mask_key].astype(bool), expected):
            raise ValueError(f'{name} panel gap differs from the frozen gap')
    if not np.allclose(inputs['train_u'], np.column_stack((np.cos(inputs['train_theta']),
                        np.sin(inputs['train_theta']))), rtol=0, atol=1e-12):
        raise ValueError('Training angle/direction mismatch')
    return inputs


def load_job(directory, inputs):
    directory = Path(directory)
    record = json.loads((directory / 'record.json').read_text())
    arrays = _read_npz(directory / 'trajectories.npz')
    config = record.get('config', record)
    return dict(directory=str(directory), record=record, config=config, arrays=arrays,
                validation=validate_job(arrays, record, inputs))


def _index(job, time):
    times = job['arrays']['times']
    matches = np.flatnonzero(np.isclose(times, time, rtol=0, atol=1e-7))
    if len(matches) != 1:
        raise ValueError(f'{job["directory"]}: expected one snapshot at {time}, found {len(matches)}')
    return int(matches[0])


def _time(job):
    return float(job['arrays']['times'][-1])


def _curve(job, inputs, time=None, dense=False):
    if dense:
        array = job['arrays']['dense_predictions']
        return array[-1] if array.ndim == 2 else array
    index = -1 if time is None else _index(job, time)
    return job['arrays']['predictions'][index, len(inputs['labels']):]


def _train(job, inputs, time=None):
    index = -1 if time is None else _index(job, time)
    return job['arrays']['predictions'][index, :len(inputs['labels'])]


def _loss(job, time=None):
    return float(job['arrays']['loss'][-1 if time is None else _index(job, time)])


def _norms(delta, mask):
    delta = np.asarray(delta)
    return dict(gap_rms=float(np.sqrt(np.mean(delta[mask]**2))),
                gap_max=float(np.max(np.abs(delta[mask]))),
                circle_rms=float(np.sqrt(np.mean(delta**2))),
                circle_max=float(np.max(np.abs(delta))))


def _visible(metrics):
    return metrics['gap_rms'] >= THRESHOLDS['visible_rms'] and metrics['gap_max'] >= THRESHOLDS['visible_max']


def validate_job(arrays, record, inputs):
    failures, diagnostics = [], {}
    required = ('times', 'predictions', 'loss', 'grams', 'rms', 'movement', 'dense_predictions')
    missing = [name for name in required if name not in arrays]
    if missing:
        return dict(passed=False, failures=[f'Missing arrays: {missing}'], diagnostics={})
    if not all(np.all(np.isfinite(v)) for v in arrays.values()
               if np.issubdtype(v.dtype, np.number)):
        failures.append('nonfinite_saved_data')
    times, predictions = arrays['times'], arrays['predictions']
    m, c, d, k = len(inputs['labels']), len(inputs['circle_theta']), len(inputs['dense_theta']), len(times)
    shapes = dict(predictions=(k,m+c), loss=(k,), grams=(k,2,m,m), rms=(k,2), movement=(k,2))
    for name, shape in shapes.items():
        if arrays[name].shape != shape:
            failures.append(f'{name}_shape:{arrays[name].shape}!={shape}')
    if arrays['dense_predictions'].shape not in ((d,), (1,d)):
        failures.append(f'dense_predictions_shape:{arrays["dense_predictions"].shape}')
    if failures:
        return dict(passed=False, failures=failures, diagnostics=diagnostics)
    if k == 0 or np.any(np.diff(times) <= 0):
        failures.append('nonincreasing_or_empty_times')
    if abs(float(record.get('last_time', times[-1])) - times[-1]) > 1e-7:
        failures.append('record_time_disagrees')
    if record.get('status') in ('failed', 'error'):
        failures.append('worker_failed')
    dtype = str(record.get('config', {}).get('dtype', 'float64'))
    arithmetic_tol = 1e-5 if '32' in dtype else 1e-10
    expected_loss = np.sum((predictions[:,:m]-inputs['labels'])**2*inputs['probabilities'], axis=1)
    diagnostics['loss_identity_error'] = float(np.max(np.abs(expected_loss-arrays['loss'])))
    diagnostics['max_loss_increase'] = float(max(0., np.max(np.diff(arrays['loss'])))) if k > 1 else 0.
    grams = arrays['grams']
    diagnostics['gram_symmetry_error'] = float(np.max(np.abs(grams-np.swapaxes(grams,-1,-2))))
    diagnostics['gram_min_eigenvalue'] = float(np.min(np.linalg.eigvalsh((grams+np.swapaxes(grams,-1,-2))/2)))
    diagnostics['rms_gram_error'] = float(np.max(np.abs(arrays['rms']**2-np.mean(np.diagonal(grams,axis1=-2,axis2=-1),axis=-1))))
    diagnostics['movement_triangle_excess'] = float(max(0., np.max(arrays['movement']-arrays['rms']-arrays['rms'][0])))
    diagnostics['oddness_error'] = float(np.max(np.abs(predictions[:,m:m+c//2]+predictions[:,m+c//2:])))
    dense = arrays['dense_predictions'].reshape(-1)
    diagnostics['dense_oddness_error'] = float(np.max(np.abs(dense[:d//2]+dense[d//2:])))
    # Compare equal angular coordinates between the final two passive panels.
    distance = np.abs(np.angle(np.exp(1j*(inputs['circle_theta'][:,None]-inputs['dense_theta'][None,:]))))
    nearest = np.argmin(distance, axis=1)
    if np.max(distance[np.arange(c),nearest]) < 1e-10:
        diagnostics['dense_snapshot_error'] = float(np.max(np.abs(dense[nearest]-predictions[-1,m:])))
    else:
        failures.append('dense_panel_does_not_contain_observation_panel')
    for key in ('loss_identity_error', 'gram_symmetry_error', 'rms_gram_error',
                'movement_triangle_excess', 'oddness_error', 'dense_oddness_error', 'dense_snapshot_error'):
        if diagnostics.get(key, 0.) > arithmetic_tol:
            failures.append(key)
    if diagnostics['gram_min_eigenvalue'] < -THRESHOLDS['gram_psd']:
        failures.append('gram_psd')
    if diagnostics['max_loss_increase'] > THRESHOLDS['max_loss_increase']:
        failures.append('loss_increase')
    checks = record.get('checks', {})
    for key in ('all_finite', 'unit_uniform_probabilities', 'checkpoint_state_exact'):
        if key in checks and checks[key] is not True:
            failures.append(f'worker:{key}')
    if float(checks.get('checkpoint_prediction_replay_error', 0.)) > arithmetic_tol:
        failures.append('worker:checkpoint_prediction_replay_error')
    return dict(passed=not failures, failures=failures, diagnostics=diagnostics,
                arithmetic_tolerance=arithmetic_tol, worker_checks=checks)


def settling(job, inputs, time=None, require_100=False):
    time = _time(job) if time is None else float(time)
    result = dict(time=time, passed=False, windows=[], missing=[])
    for start, end in ((time-50,time-25),(time-25,time)):
        try:
            a,b = _curve(job, inputs, start), _curve(job, inputs, end)
            drift = float(np.max(np.abs(b-a)))
            loss_change = abs(_loss(job,end)-_loss(job,start))
            result['windows'].append(dict(start=start,end=end,circle_max=drift,
                                          loss_change=loss_change,
                                          passed=drift<.005 and loss_change<.0005))
        except ValueError as error:
            result['missing'].append(str(error))
    if require_100:
        try:
            delta = _curve(job, inputs, time)-_curve(job, inputs, time-100)
            result['drift100'] = _norms(delta, inputs['gap_mask'].astype(bool))
            result['drift100']['passed'] = result['drift100']['circle_max'] <= .01
        except ValueError as error:
            result['missing'].append(str(error))
    result['passed'] = (time >= 100 and not result['missing'] and len(result['windows'])==2
                        and all(w['passed'] for w in result['windows'])
                        and (not require_100 or result.get('drift100',{}).get('passed',False)))
    return result


def analyze_screen(inputs_path, job_dirs_by_order):
    inputs = load_inputs(inputs_path)
    jobs = {int(order):load_job(path,inputs) for order,path in job_dirs_by_order.items()}
    mask = inputs['gap_dense_mask'].astype(bool)
    pairs = {}
    for a,b in ((1,3),(3,5)):
        if a not in jobs or b not in jobs:
            pairs[f'{a}-{b}'] = dict(provisional=False, missing=True)
            continue
        values = _norms(_curve(jobs[a],inputs,dense=True)-_curve(jobs[b],inputs,dense=True),mask)
        valid = jobs[a]['validation']['passed'] and jobs[b]['validation']['passed']
        pairs[f'{a}-{b}'] = dict(**values, visible=_visible(values), provisional=_visible(values) and valid,
                                 times=[_time(jobs[a]),_time(jobs[b])], correctness_passed=valid)
    qualifying = [key for key,pair in pairs.items() if pair['provisional']]
    result = dict(kind='screen', grid_points=len(mask), thresholds=THRESHOLDS,
                  pairs=pairs, provisional=bool(qualifying),
                  pairchosen=[int(x) for x in qualifying[0].split('-')] if qualifying else None,
                  validation={str(n):j['validation'] for n,j in jobs.items()},
                  stopinfo={str(n):settling(j,inputs) for n,j in jobs.items()},
                  interpretation='Exploratory endpoint screen; unequal times and unresolved settling cannot establish final separation.')
    return _jsonable(result)


def analyze_confirmation(manifest_or_path):
    manifest = (json.loads(Path(manifest_or_path).read_text())
                if isinstance(manifest_or_path,(str,Path)) else manifest_or_path)
    inputs = load_inputs(manifest['inputs_path'])
    jobs = {name:load_job(path if isinstance(path,str) else path['path'],inputs)
            for name,path in manifest['jobs'].items()}
    selected = tuple(int(n) for n in manifest['pair'])
    if selected not in ((1,3),(3,5)):
        raise ValueError('Confirmation pair must be adjacent in (1,3,5)')
    required = [f'cl_N{n}_main' for n in (1,3,5)]
    required += [f'cl_N{n}_{role}' for n in selected for role in ('fine','half')]
    required += ['net_n8192_s11','net_n8192_s29','net_n8192_s47','net_n4096_s11',
                 'net_n8192_s11_half','net_n4096_s11_double']
    missing = [name for name in required if name not in jobs]
    time = float(manifest.get('common_time', min(_time(j) for j in jobs.values())))
    common_final = all(abs(_time(j)-time)<1e-7 for j in jobs.values())
    validation = {name:job['validation'] for name,job in jobs.items()}
    settled = {name:settling(job,inputs,time,True) for name,job in jobs.items()}
    mask = inputs['gap_dense_mask'].astype(bool)
    mask720 = inputs['gap_mask'].astype(bool)
    controls = {}

    def control(name, a, b, category, tolerance=None):
        if a not in jobs or b not in jobs:
            return
        values = _norms(_curve(jobs[a],inputs,dense=True)-_curve(jobs[b],inputs,dense=True),mask)
        values.update(a=a,b=b,category=category,loss_change=abs(_loss(jobs[a])-_loss(jobs[b])))
        values['passed'] = (tolerance is None or (values['circle_max']<=tolerance and values['loss_change']<=.001))
        values['circle_max_tolerance'] = tolerance
        controls[name] = values

    finest = {}
    for n in selected:
        finest[n] = f'cl_N{n}_finest' if f'cl_N{n}_finest' in jobs else f'cl_N{n}_fine'
        previous = f'cl_N{n}_fine' if finest[n].endswith('_finest') else f'cl_N{n}_main'
        control(f'quadrature_N{n}', previous, finest[n], 'quadrature', .025)
        # Retain the larger earlier change visibly when one extra refinement was executed.
        if finest[n].endswith('_finest'):
            control(f'earlier_quadrature_N{n}',f'cl_N{n}_main',f'cl_N{n}_fine','earlier_quadrature')
        control(f'step_N{n}',f'cl_N{n}_main',f'cl_N{n}_half','step',.002)
    control('network_step','net_n8192_s11','net_n8192_s11_half','step',.002)
    control('network_precision','net_n4096_s11','net_n4096_s11_double','precision',.002)
    control('network_width','net_n8192_s11','net_n4096_s11','width')
    seed_names = ['net_n8192_s11','net_n8192_s29','net_n8192_s47']
    for a,b in combinations(seed_names,2):
        control(f'seeds_{a}_{b}',a,b,'seed_spread')
    for name,gate in settled.items():
        if 'drift100' in gate:
            controls[f'drift100_{name}'] = dict(gate['drift100'],category='remaining_drift',a=name,b=name,
                                                loss_change=None,circle_max_tolerance=.01)
    uncertainty_controls = {name:value for name,value in controls.items() if value['category']!='earlier_quadrature'}
    uncertainty = {}
    for metric in ('gap_rms','gap_max'):
        key = max(uncertainty_controls,key=lambda k:uncertainty_controls[k][metric],default=None)
        uncertainty[metric] = dict(value=uncertainty_controls[key][metric] if key else None,witness=key)
    numerical_passed = not missing and all(v['passed'] for v in controls.values())
    correctness = manifest.get('correctness',{})
    if isinstance(correctness,str):
        correctness=json.loads(Path(correctness).read_text())
    correctness_passed = correctness.get('passed') is True and all(v['passed'] for v in validation.values())
    all_settled = common_final and all(v['passed'] for v in settled.values())
    first_stops = []
    for name,job in jobs.items():
        first = job['record'].get('first_plateau_time',job['record'].get('first_stop_time'))
        if first is not None:
            first_stops.append(float(first))
    earliest = manifest.get('minimum_common_time')
    if earliest is None and len(first_stops)==len(jobs):
        earliest=max(first_stops)+100
    horizon_rule_passed = earliest is not None and time >= float(earliest)-1e-7 and time<=1600
    if earliest is None:
        missing.append('minimum_common_time (latest first plateau or initial cap +100)')
    references = None
    if all(name in jobs for name in seed_names):
        seed_curves=np.stack([_curve(jobs[name],inputs,dense=True) for name in seed_names])
        seed_train=np.stack([_train(jobs[name],inputs) for name in seed_names])
        references=dict(curve=np.mean(seed_curves,axis=0),train=np.mean(seed_train,axis=0),
                        seed_min=np.min(seed_curves,axis=0),seed_max=np.max(seed_curves,axis=0),
                        loss_mean=float(np.mean([_loss(jobs[name]) for name in seed_names])),
                        loss_by_seed={name:_loss(jobs[name]) for name in seed_names},
                        maximum_pointwise_seed_range=float(np.max(np.ptp(seed_curves,axis=0))))
    pairs={}
    for a,b in ((1,3),(3,5)):
        key=f'{a}-{b}'
        an,bn=f'cl_N{a}_main',f'cl_N{b}_main'
        if an not in jobs or bn not in jobs:
            pairs[key]=dict(validated_separation=False,missing=True)
            continue
        metrics=_norms(_curve(jobs[an],inputs,dense=True)-_curve(jobs[bn],inputs,dense=True),mask)
        pair=dict(main=metrics,main_visible=_visible(metrics),selected=(a,b)==selected,
                  main_train_rms=float(np.sqrt(np.mean((_train(jobs[an],inputs)-_train(jobs[bn],inputs))**2))),
                  main_losses={str(a):_loss(jobs[an]),str(b):_loss(jobs[bn])})
        try:
            previous=_norms(_curve(jobs[an],inputs,time-100)-_curve(jobs[bn],inputs,time-100),mask720)
            pair.update(previous100=previous,previous100_visible=_visible(previous))
        except ValueError as error:
            pair.update(previous100_visible=False,previous100_missing=str(error))
        pair['refined_visible']=False
        pair['refined_previous100_visible']=False
        if (a,b)==selected and finest[a] in jobs and finest[b] in jobs:
            refined=_norms(_curve(jobs[finest[a]],inputs,dense=True)-_curve(jobs[finest[b]],inputs,dense=True),mask)
            pair.update(refined=refined,refined_names=[finest[a],finest[b]],refined_visible=_visible(refined))
            try:
                previous=_norms(_curve(jobs[finest[a]],inputs,time-100)-_curve(jobs[finest[b]],inputs,time-100),mask720)
                pair.update(refined_previous100=previous,refined_previous100_visible=_visible(previous))
            except ValueError as error:
                pair['refined_previous100_missing']=str(error)
        pair['uncertainty_margin_passed'] = bool(pair.get('refined')) and all(
            uncertainty[metric]['value'] is not None and
            min(metrics[metric],pair['refined'][metric]) > 5*uncertainty[metric]['value']
            for metric in ('gap_rms','gap_max'))
        pair['validated_separation'] = (pair['selected'] and correctness_passed and numerical_passed
            and all_settled and horizon_rule_passed and not missing and pair['main_visible']
            and pair['previous100_visible'] and pair['refined_visible']
            and pair['refined_previous100_visible'] and pair['uncertainty_margin_passed'])
        pair['off_support_selection'] = False
        if references is not None:
            error_a=_norms(_curve(jobs[an],inputs,dense=True)-references['curve'],mask)
            error_b=_norms(_curve(jobs[bn],inputs,dense=True)-references['curve'],mask)
            pair['network_errors']={str(a):error_a,str(b):error_b}
            pair['higher_order_gap_rmse_excess']=error_b['gap_rms']-error_a['gap_rms']
            train_curves=[_train(jobs[an],inputs),_train(jobs[bn],inputs)] + [
                _train(jobs[name],inputs) for name in seed_names]
            loss_values=[_loss(jobs[an]),_loss(jobs[bn])] + [_loss(jobs[name]) for name in seed_names]
            if (a,b)==selected and all(finest[n] in jobs for n in selected):
                train_curves += [_train(jobs[finest[n]],inputs) for n in selected]
                loss_values += [_loss(jobs[finest[n]]) for n in selected]
            max_train_pair=max(float(np.sqrt(np.mean((x-y)**2))) for x,y in combinations(train_curves,2))
            pair['matched_training_fit']=dict(max_loss=max(loss_values),max_pair_rms=max_train_pair,
                                               passed=max(loss_values)<.005 and max_train_pair<.02)
            pair['off_support_selection']=pair['validated_separation'] and pair['matched_training_fit']['passed']
            # A conservative propagation bound: two closure and two reference error changes.
            u=uncertainty['gap_rms']['value']
            pair['higher_order_error_uncertainty_bound']=None if u is None else 4*u
            pair['higher_order_worse']=bool(pair['validated_separation'] and u is not None and
                pair['higher_order_gap_rmse_excess']>=.025 and pair['higher_order_gap_rmse_excess']>5*4*u)
        pairs[key]=pair
    result=dict(kind='confirmation',thresholds=THRESHOLDS,common_time=time,common_final=common_final,
                minimum_common_time=earliest,horizon_rule_passed=horizon_rule_passed,
                selected_pair=list(selected),missing=missing,correctness=correctness,
                correctness_passed=correctness_passed,validation=validation,settling=settled,
                all_settled=all_settled,numerical_controls=controls,numerical_passed=numerical_passed,
                uncertainty=uncertainty,adjacent_pairs=pairs,
                validated_separation=any(p.get('validated_separation',False) for p in pairs.values()),
                off_support_selection=any(p.get('off_support_selection',False) for p in pairs.values()),
                reference={k:v for k,v in (references or {}).items() if k not in ('curve','train','seed_min','seed_max')},
                endpoint_grid_points=len(mask),persistence_and_drift_grid_points=len(mask720))
    result['continue_for_settling']=not all_settled
    result['stop_recommendation']='validated_success' if result['validated_separation'] else (
        'correctness_failure' if not correctness_passed else 'continue_or_unresolved_within_frozen_caps')
    return _jsonable(result)


def main():
    parser=argparse.ArgumentParser()
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--screen-config')
    mode.add_argument('--manifest')
    parser.add_argument('--out',required=True)
    args=parser.parse_args()
    if args.screen_config:
        config=json.loads(Path(args.screen_config).read_text())
        result=analyze_screen(config['inputs_path'],config['jobs'])
    else:
        result=analyze_confirmation(args.manifest)
    destination=Path(args.out)
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':
    main()
