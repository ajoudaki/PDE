"""Hash-verified postprocessing of the predeclared sparse-circle campaign.

run(campaign, out) reads completed raw records and writes a fresh summary plus
one compact derived-curves NPZ per record. No training or checkpoint mutation.
All relative distances state their reference; no fitted gain or clock changes
are applied to baselines. Equal-loss frozen times are separately labelled.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.optimize import brentq, minimize_scalar

from NTK import kernel

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def rms(value):
    return float(np.sqrt(np.mean(np.asarray(value)**2)))


def spectrum(f):
    f = np.asarray(f, float)
    coeff = np.fft.rfft(f)/len(f)
    power = abs(coeff)**2
    power[1:] *= 2
    if len(f) % 2 == 0:
        power[-1] /= 2
    return coeff, power


def power_metrics(power):
    power = np.asarray(power, float)
    modes = np.arange(len(power))
    energy = float(power.sum())
    if energy <= 1e-30:
        return dict(energy=energy, k_rms=0., k99=0, mode1_fraction=0.,
                    tail_ge3=0., tail_ge5=0., tail_ge7=0., even_fraction=0., mean_fraction=0.)
    return dict(energy=energy, k_rms=float(np.sqrt((modes*modes)@power/energy)),
                k99=int(np.searchsorted(np.cumsum(power), .99*energy)),
                mode1_fraction=float(power[1]/energy),
                tail_ge3=float(power[3:].sum()/energy),
                tail_ge5=float(power[5:].sum()/energy),
                tail_ge7=float(power[7:].sum()/energy),
                even_fraction=float(power[2::2].sum()/energy),
                mean_fraction=float(power[0]/energy))


def spectral_metrics(f):
    return power_metrics(spectrum(f)[1])


def distance(a, b, amplitude=1.):
    a, b = np.asarray(a), np.asarray(b)
    ra, rb = rms(a), rms(b)
    floor = max(abs(amplitude)*1e-12, 1e-15)
    return dict(rms=rms(a-b), max=float(np.max(abs(a-b))),
                relative_rms=rms(a-b)/max(rb, floor),
                reference_rms=rb,
                normalized_shape_rms=rms(a/max(ra, floor)-b/max(rb, floor)))


class FrozenKernel:
    """Exact symmetric solution for weighted full-MSE GF, zero initial output.

    Relative eigenvalue rank threshold 1e-12; inconsistent t=infinity requests
    raise ValueError. Finite time retains all positive numerical eigenvalues.
    """
    def __init__(self, gram, cross, labels, weights):
        self.gram, self.cross = np.asarray(gram), np.asarray(cross)
        self.labels, self.weights = np.asarray(labels), np.asarray(weights)
        if (np.any(self.weights <= 0) or not np.isclose(self.weights.sum(), 1.)
                or self.gram.shape != (len(self.labels), len(self.labels))):
            raise ValueError('invalid frozen problem')
        self.root = np.sqrt(self.weights)
        symmetric = self.root[:, None]*self.gram*self.root[None, :]
        self.eigenvalues, self.vectors = np.linalg.eigh(symmetric)
        scale = max(float(self.eigenvalues[-1]), 1e-300)
        if self.eigenvalues[0] < -1e-10*scale:
            raise ValueError('non-PSD frozen Gram')
        self.eigenvalues = np.maximum(self.eigenvalues, 0)
        self.positive = self.eigenvalues > 1e-12*scale
        self.coordinates = self.vectors.T @ (self.root*self.labels)
        self.null_loss = float(np.sum(self.coordinates[~self.positive]**2))
        self.rank = int(self.positive.sum())
        self.condition = (float(self.eigenvalues[-1]/self.eigenvalues[0])
                          if np.all(self.positive) else None)

    def coefficients(self, t):
        if np.isinf(t):
            if self.null_loss > 1e-18*max(1., float(self.labels@self.labels)):
                raise ValueError('frozen labels cannot interpolate at numerical rank')
            factors = np.zeros_like(self.eigenvalues)
            factors[self.positive] = 1/self.eigenvalues[self.positive]
        else:
            if t < 0 or not np.isfinite(t):
                raise ValueError('time must be nonnegative')
            factors = np.full_like(self.eigenvalues, 2*t)
            active = self.eigenvalues > 0
            factors[active] = -np.expm1(-2*t*self.eigenvalues[active])/self.eigenvalues[active]
        return self.root*(self.vectors @ (factors*self.coordinates))

    def predict(self, t):
        return self.cross @ self.coefficients(t)

    def train(self, t):
        return self.gram @ self.coefficients(t)

    def loss(self, t):
        return float(np.sum(self.coordinates**2*np.exp(-4*self.eigenvalues*t)))

    def matched_time(self, target_loss):
        if target_loss >= self.loss(0):
            return 0.
        if target_loss <= self.null_loss or target_loss <= 0:
            return None
        right = 1.
        for _ in range(80):
            if self.loss(right) <= target_loss:
                return float(brentq(lambda t: self.loss(t)-target_loss, 0., right,
                                    xtol=1e-10, rtol=1e-12))
            right *= 2
        return None


def kernel_geometry(matrix):
    matrix = np.asarray(matrix, float)
    fourier = np.fft.ifft(np.fft.fft(matrix, axis=0), axis=1)
    total = float(np.sum(abs(fourier)**2))
    off = fourier.copy()
    np.fill_diagonal(off, 0)
    return dict(offdiagonal_fraction=float(np.sum(abs(off)**2)/total) if total else 0.,
                frobenius=float(np.sqrt(total)), trace=float(np.trace(matrix)),
                min_eigenvalue=float(np.linalg.eigvalsh((matrix+matrix.T)/2)[0]))


def effective_rank(singular):
    singular = np.asarray(singular, float)
    mass = singular**2
    total = mass.sum()
    probability = mass/total if total else mass
    nonzero = probability > 0
    return dict(frobenius=float(np.sqrt(total)),
                stable_rank=float(total/mass[0]) if total else 0.,
                entropy_rank=float(np.exp(-np.sum(probability[nonzero]*np.log(probability[nonzero])))) if total else 0.,
                energy99_rank=int(np.searchsorted(np.cumsum(probability), .99)+1) if total else 0,
                singular_values=singular.tolist())


def fit_templates(f, config):
    theta = 2*np.pi*np.arange(len(f))/len(f)
    train, test = np.arange(0, len(f), 2), np.arange(1, len(f), 2)
    amplitude = config['amplitude']
    results, curves = {}, {}
    for limit in [1, 3, 5, 9]:
        design = np.column_stack([fun(m*theta) for m in range(1, limit+1, 2)
                                  for fun in [np.cos, np.sin]])
        parameters = np.linalg.lstsq(design[train], f[train], rcond=None)[0]
        fitted = design @ parameters
        key = f'odd_through_{limit}'
        results[key] = dict(whole=distance(fitted, f, amplitude),
                            heldout=distance(fitted[test], f[test], amplitude),
                            fit=distance(fitted[train], f[train], amplitude),
                            coefficients=parameters.tolist())
        curves['template_'+key] = fitted
    if config['kind'] == 'pair':
        midpoint, separation = np.deg2rad([config['rotation'], config['delta']])
        def curve(kappa):
            return amplitude*np.tanh(kappa*np.sin(theta-midpoint))/np.tanh(kappa*np.sin(separation/2))
        def objective(log_kappa):
            return np.mean((curve(np.exp(log_kappa))[train]-f[train])**2)
        # Predeclared compact interval; a coarse full-interval scan plus local
        # refinement avoids assuming that the nonlinear objective is unimodal.
        grid = np.linspace(np.log(.02), np.log(30), 101)
        values = np.array([objective(v) for v in grid])
        candidates = [(values[0], grid[0]), (values[-1], grid[-1])]
        for j in range(1, len(grid)-1):
            if values[j] <= values[j-1] and values[j] <= values[j+1]:
                fit = minimize_scalar(objective, bounds=(grid[j-1], grid[j+1]), method='bounded')
                candidates.append((fit.fun, fit.x))
        _, selected = min(candidates)
        kappa = float(np.exp(selected)); fitted = curve(kappa)
        results['normalized_tanh_sine'] = dict(kappa=kappa,
            at_boundary=bool(kappa <= .02001 or kappa >= 29.999),
            whole=distance(fitted, f, amplitude), heldout=distance(fitted[test], f[test], amplitude),
            fit=distance(fitted[train], f[train], amplitude))
        curves['template_normalized_tanh_sine'] = fitted
    return results, curves


def compare_records(left, right, arrays):
    a, b = arrays[left['id']], arrays[right['id']]
    amplitude = right['config']['amplitude']
    result = dict(left=left['id'], right=right['id'],
                  common_T100=distance(a['learned_T100'], b['learned_T100'], amplitude),
                  final=distance(a['learned_final'], b['learned_final'], amplitude),
                  both_matched_fit=left['matched_fit'] and right['matched_fit'],
                  both_settled=left['settled'] and right['settled'],
                  left_time=left['final_time'], right_time=right['final_time'])
    for clock in ['T100', 'final']:
        sa, sb = left['spectra'][clock], right['spectra'][clock]
        result[clock+'_k_rms_change'] = sa['k_rms']-sb['k_rms']
        result[clock+'_k_rms_relative_change'] = sa['k_rms']/sb['k_rms']-1 if sb['k_rms'] else None
        result[clock+'_tail_changes'] = {key: sa[key]-sb[key] for key in ['tail_ge3','tail_ge5','tail_ge7']}
    return result


def run(campaign, out):
    start = time.perf_counter()
    campaign, out = Path(campaign).resolve(), Path(out).resolve()
    if not out.is_relative_to(campaign) or out == campaign:
        raise ValueError('analysis output must be a fresh subdirectory of this campaign')
    out.mkdir(exist_ok=False)
    manifest_path = campaign/'manifest.json'
    manifest = json.loads(manifest_path.read_text()); manifest_hash = sha(manifest_path)
    for source, expected in manifest['sources'].items():
        if sha(source) != expected:
            raise ValueError('changed campaign source: '+source)
    configs = {c['id']: c for c in manifest['configurations']}
    records, arrays, skipped, failures, input_hashes = {}, {}, [], {}, {}
    true_cache = {}
    circle_angles = 2*np.pi*np.arange(128)/128
    true_circle = kernel(circle_angles[:,None]-circle_angles[None,:])
    for name, config in configs.items():
        directory = campaign/name
        record_path = directory/'record.json'
        if not record_path.exists():
            skipped.append(name)
            if (directory/'failure.json').exists():
                failures[name] = json.loads((directory/'failure.json').read_text())
            continue
        record = json.loads(record_path.read_text())
        if record['status'] != 'complete':
            failures[name] = record
            continue
        if record['config'] != config or record['manifest_sha256'] != manifest_hash:
            raise ValueError('configuration or manifest mismatch: '+name)
        if record['source_sha256'] != manifest['sources'][str(HERE/'ENGINE.py')]:
            raise ValueError('engine source mismatch: '+name)
        for filename, expected in record['outputs'].items():
            if sha(directory/filename) != expected:
                raise ValueError('raw hash mismatch: '+name+'/'+filename)
        input_hashes[name] = dict(record=sha(record_path), **record['outputs'])
        with np.load(directory/'observations.npz', allow_pickle=False) as saved:
            raw = {k: saved[k] for k in saved.files}
        if not all(np.all(np.isfinite(v)) for v in raw.values()):
            raise ValueError('nonfinite raw arrays: '+name)
        f = raw['dense_predictions']; times = raw['times']; y = raw['labels']; w = raw['weights']
        theta = 2*np.pi*np.arange(len(f))/len(f)
        matches = np.flatnonzero(np.isclose(times,100,rtol=0,atol=1e-10))
        if len(matches) != 1:
            raise ValueError('missing unique common time 100: '+name)
        j100 = int(matches[0]); f100 = raw['predictions'][j100]
        loss = np.sum(w[None,:]*(raw['train_predictions']-y)**2, axis=1)
        if np.max(abs(loss-raw['loss'])) > 1e-11 or abs(times[-1]-record['last_time']) > 1e-10:
            raise ValueError('raw loss or clock mismatch: '+name)
        expected_angles = np.deg2rad(config['angles_degrees'])
        if (not np.array_equal(y, np.asarray(config['labels']))
                or np.max(abs(raw['angles']-expected_angles)) > 1e-14
                or not np.allclose(w,np.ones(len(y))/len(y),rtol=0,atol=1e-15)):
            raise ValueError('raw data mismatch: '+name)
        if (np.max(abs(f[::2]-raw['predictions'][-1])) > 1e-10
                or np.max(abs(raw['prediction']-f)) > 1e-10
                or np.max(abs(raw['train_prediction']-raw['train_predictions'][-1])) > 1e-10):
            raise ValueError('saved panel mismatch: '+name)
        cache_key = (tuple(expected_angles), tuple(y), tuple(w), len(f))
        if cache_key not in true_cache:
            gram = kernel(expected_angles[:,None]-expected_angles[None,:])
            cross = kernel(theta[:,None]-expected_angles[None,:])
            true_cache[cache_key] = FrozenKernel(gram,cross,y,w)
        true = true_cache[cache_key]
        own = FrozenKernel(raw['frozen_kernel_train'],raw['frozen_kernel_cross'],y,w)
        own_inf, true_inf = own.predict(np.inf), true.predict(np.inf)
        own_final, true_final = own.predict(times[-1]), true.predict(times[-1])
        own100, true100 = own.predict(100.), true.predict(100.)
        spectrum_final, spectrum_coarse = spectral_metrics(f), spectral_metrics(f[::2])
        grid_relative = abs(spectrum_final['k_rms']-spectrum_coarse['k_rms'])/max(spectrum_final['k_rms'],1e-15)
        coeff, power = spectrum(f)
        coarse_power = spectrum(f[::2])[1]
        grid_power_l1 = float(np.sum(abs(power/max(power.sum(),1e-300)
             -np.pad(coarse_power/max(coarse_power.sum(),1e-300),(0,len(power)-len(coarse_power))))))
        templates, template_curves = fit_templates(f,config)
        amp = config['amplitude']
        initial_blocks, final_blocks = raw['kernel_circle_initial'], raw['kernel_circle_final']
        geometry = {}
        for clock, blocks in [('initial',initial_blocks),('final',final_blocks)]:
            geometry[clock] = {key:kernel_geometry(value) for key,value in
                [('total',blocks.sum(0)),('w',blocks[0]),('c',blocks[1]),('M',blocks[2])]}
        hidden = {}
        for layer in [1,2]:
            hidden[str(layer)] = {clock:power_metrics(raw[f'hidden{layer}_power_{clock}'])
                                  for clock in ['initial','current','motion']}
            hidden[str(layer)].update(motion_rms_training=float(raw[f'hidden{layer}_motion_rms_training']),
                                      motion_rms_circle=float(raw[f'hidden{layer}_motion_rms_circle']),
                                      gram_initial=raw[f'hidden{layer}_gram_initial'].tolist(),
                                      gram_final=raw[f'hidden{layer}_gram_current'].tolist())
        own_match, true_match = own.matched_time(loss[-1]), true.matched_time(loss[-1])
        item = dict(id=name,config=config,final_time=float(times[-1]),settled=bool(record['settled']),
            stop_reason=record['stop_reason'],final_loss=float(loss[-1]),
            relative_final_loss=float(loss[-1]/amp**2),matched_fit=bool(loss[-1]/amp**2 <= 1e-4),
            relative_T100_loss=float(loss[j100]/amp**2),
            spectra=dict(final=spectrum_final,T100=spectral_metrics(f100),coarse_final=spectrum_coarse,
                         true_ntk_endpoint=spectral_metrics(true_inf),own_frozen_endpoint=spectral_metrics(own_inf)),
            grid_k_rms_relative_difference=float(grid_relative),grid_normalized_power_L1=grid_power_l1,
            grid_valid=bool(max(grid_relative,grid_power_l1) <= .005),
            grid_tail_changes={key:abs(spectrum_final[key]-spectrum_coarse[key]) for key in ['tail_ge3','tail_ge5','tail_ge7']},
            amplitude=dict(max_abs=float(np.max(abs(f))),rms=rms(f),max_over_label=float(np.max(abs(f))/amp),
                           overshoot=float(max(0.,np.max(abs(f))/amp-1))),
            final_drift=dict(last20=float(np.max(abs(raw['predictions'][-1]-raw['predictions'][-3]))),
                             preceding20=float(np.max(abs(raw['predictions'][-3]-raw['predictions'][-5])))),
            versus_true_ntk=dict(endpoint=distance(f,true_inf,amp),same_final_time=distance(f,true_final,amp),
                                common_T100=distance(f100,true100[::2],amp)),
            versus_own_frozen=dict(endpoint=distance(f,own_inf,amp),same_final_time=distance(f,own_final,amp),
                                  common_T100=distance(f100,own100[::2],amp)),
            initial_kernel=dict(train_relative_rms=distance(own.gram,true.gram,1.)['relative_rms'],
                                circle_relative_frobenius=float(np.linalg.norm(initial_blocks.sum(0)-true_circle)/np.linalg.norm(true_circle)),
                                own_rank=own.rank,own_condition=own.condition,true_rank=true.rank,true_condition=true.condition),
            matched_loss_frozen_times=dict(own=own_match,true_ntk=true_match),
            templates=templates,kernel_geometry=geometry,hidden=hidden,
            projected_a_spectrum={clock:power_metrics(raw['a_power_'+clock]) for clock in ['initial','current','motion']},
            M=dict(initial=effective_rank(raw['singular_values_initial']),final=effective_rank(raw['singular_values_final'])),
            source_checks=record['checks'])
        validity_failures=[]
        if np.max(np.diff(loss)) > 1e-6*max(1,amp**2):
            validity_failures.append('significant_saved_loss_increase')
        if not item['grid_valid']:
            validity_failures.append('Fourier_grid_refinement_exceeds_0.005')
        if record['checks']['replay_max']>1e-12:
            validity_failures.append('producer_restart_replay_failed')
        if record['checks']['gram_min_eigenvalue'] < -1e-8:
            validity_failures.append('hidden_Gram_PSD_failed')
        if min(geometry[s]['total']['min_eigenvalue'] for s in ['initial','final']) < -1e-8:
            validity_failures.append('circle_tangent_PSD_failed')
        item['validity_failures']=validity_failures
        item['valid']=not validity_failures
        derived = dict(angles1440=theta,learned_final=f,learned_T100=f100,
            ntk_endpoint=true_inf,ntk_T100=true100,ntk_final_time=true_final,
            own_frozen_endpoint=own_inf,own_frozen_T100=own100,own_frozen_final_time=own_final,
            modes=np.arange(len(power)),learned_power=power,
            learned_coefficients=coeff,ntk_power=spectrum(true_inf)[1],own_frozen_power=spectrum(own_inf)[1],
            times=times,loss=loss,train_predictions=raw['train_predictions'],
            k_rms_time=np.array([spectral_metrics(v)['k_rms'] for v in raw['predictions']]),
            true_ntk_loss_time=np.array([true.loss(t) for t in times]),
            own_frozen_loss_time=np.array([own.loss(t) for t in times]),
            kernel_circle_initial=initial_blocks,kernel_circle_final=final_blocks,
            kernel_fourier_initial=np.fft.ifft(np.fft.fft(initial_blocks.sum(0),axis=0),axis=1),
            kernel_fourier_final=np.fft.ifft(np.fft.fft(final_blocks.sum(0),axis=0),axis=1),
            **{k:raw[k] for k in raw if k.startswith('hidden') and '_power_' in k},**template_curves)
        for label,model,match in [('own',own,own_match),('true_ntk',true,true_match)]:
            if match is not None:
                matched = model.predict(match)
                item['versus_own_frozen' if label=='own' else 'versus_true_ntk']['equal_final_training_loss'] = distance(f,matched,amp)
                derived[label+'_equal_final_training_loss'] = matched
        arrays[name],records[name] = derived,item
        np.savez_compressed(out/(name+'.npz'),**derived)
        item['derived_file'] = name+'.npz'
        item['derived_sha256'] = sha(out/item['derived_file'])

    controls, order_comparisons, rotations, amplitudes = [],[],[],[]
    for name,item in records.items():
        c = item['config']
        main_name = f"{c['name']}_N{c['order']}_main"
        if c['control'] != 'main' and main_name in records:
            comparison = compare_records(item,records[main_name],arrays)
            comparison.update(control=c['control'],threshold=.02 if c['control']=='fine' else .002)
            comparison['common_T100_valid'] = comparison['common_T100']['relative_rms'] <= comparison['threshold']
            comparison['settled_endpoint_valid'] = (comparison['both_settled'] and comparison['both_matched_fit']
                                                   and comparison['final']['relative_rms'] <= comparison['threshold'])
            controls.append(comparison)
    by_main = {}
    for comparison in controls:
        by_main.setdefault(comparison['right'],[]).append(comparison)
    for name,item in records.items():
        c = item['config']
        if c['control'] != 'main':
            continue
        available = by_main.get(name,[])
        item['available_controls'] = [v['control'] for v in available]
        item['complete_control_axes'] = set(item['available_controls']) == {'fine','half'}
        variation = max([v['final']['relative_rms'] for v in available]+[0.])
        item['own_initial_explanation'] = dict(
            discrepancy=item['versus_own_frozen']['endpoint']['relative_rms'],
            control_variation=variation,
            both_hidden_motions_over_002=all(item['hidden'][str(l)]['motion_rms_training']>.02 for l in [1,2]))
        evidence = (item['valid'] and item['matched_fit'] and item['versus_own_frozen']['endpoint']['relative_rms']>.05
                    and item['own_initial_explanation']['both_hidden_motions_over_002']
                    and item['versus_own_frozen']['endpoint']['relative_rms']>5*variation)
        item['own_initial_explanation']['classification'] = (
            'disfavored_with_controls' if evidence and item['complete_control_axes']
            and all(v['settled_endpoint_valid'] for v in available)
            else 'candidate_feature_adaptation_numerically_unresolved' if evidence
            else 'criterion_not_met')
        _,pp = spectrum(arrays[name]['learned_final'])
        cutoff_tail = float(pp[c['order']+1:].sum()/pp.sum())
        coarse = spectrum(arrays[name]['learned_final'][::2])[1]
        uncertainty = abs(cutoff_tail-float(coarse[c['order']+1:].sum()/coarse.sum()))
        for cc in available:
            other = arrays[cc['left']]['learned_power']
            uncertainty = max(uncertainty,abs(cutoff_tail-float(other[c['order']+1:].sum()/other.sum())))
        item['above_order_angular_tail'] = dict(fraction=cutoff_tail,measured_uncertainty=uncertainty,
            exceeds_threshold=bool(cutoff_tail>1e-4 and cutoff_tail>10*uncertainty),
            complete_controls=item['complete_control_axes'])
        for higher in [2,3,5]:
            if higher <= c['order']:
                continue
            other_name = f"{c['name']}_N{higher}_main"
            if other_name in records:
                order_comparisons.append(compare_records(records[other_name],item,arrays))
        if c['kind']=='pair' and c['rotation']==0:
            other_name = f"pair_d{c['delta']}_r45_N{c['order']}_main"
            if other_name in records:
                other=records[other_name]
                rotation=dict(base=name,rotated=other_name,both_settled=item['settled'] and other['settled'],
                              both_matched_fit=item['matched_fit'] and other['matched_fit'])
                for clock,key in [('final','learned_final'),('T100','learned_T100')]:
                    rotated=arrays[other_name][key]; shift=len(rotated)//8
                    rotation[clock]=distance(np.roll(rotated,-shift),arrays[name][key],c['amplitude'])
                error_controls=by_main.get(name,[])+by_main.get(other_name,[])
                numerical=max([v['final']['relative_rms'] for v in error_controls]+[0.])
                rotation['measured_control_variation']=numerical
                rotation['exceeds_significance_margin']=bool(rotation['final']['relative_rms']>.02
                                                            and rotation['final']['relative_rms']>5*numerical)
                rotation['control_coverage_complete']=bool(by_main.get(name) and by_main.get(other_name))
                rotations.append(rotation)
        if c['amplitude']==.2 and c['kind']=='pair':
            other_name=f"pair_d{c['delta']}_r45_N{c['order']}_main"
            if other_name in records:
                amplitudes.append(dict(low=name,unit=other_name,
                    normalized_endpoint=distance(arrays[name]['learned_final']/.2,arrays[other_name]['learned_final']),
                    normalized_common_T100=distance(arrays[name]['learned_T100']/.2,arrays[other_name]['learned_T100']),
                    both_matched_fit=item['matched_fit'] and records[other_name]['matched_fit']))

    frequency=[]
    for case in sorted({item['config']['name'] for item in records.values()}):
        ids=[f'{case}_N{n}_main' for n in [1,3,5]]
        if not all(name in records for name in ids):
            continue
        rr=[records[name] for name in ids]
        kk=[r['spectra']['final']['k_rms'] for r in rr]
        uncertainty=[max([abs(c['final_k_rms_change']) for c in by_main.get(name,[])]+[0.]) for name in ids]
        transitions=[]
        for j in [0,1]:
            change=kk[j+1]-kk[j]; margin=3*(uncertainty[j]+uncertainty[j+1])
            transitions.append(dict(low=[1,3][j],high=[3,5][j],relative_change=change/kk[j],
                                    control_margin=margin,above_5_percent=change>=.05*kk[j] and change>margin,
                                    reversed_5_percent=change<=-.05*kk[j] and -change>margin))
        coverage=all(r.get('complete_control_axes',False) for r in rr)
        valid=all(r['matched_fit'] and r['valid'] for r in rr)
        controls_valid=all(c['settled_endpoint_valid'] for name in ids for c in by_main.get(name,[]))
        direction=('increasing' if all(t['above_5_percent'] for t in transitions)
                   else 'contains_significant_reversal' if any(t['reversed_5_percent'] for t in transitions)
                   else 'inconclusive_or_near_tie')
        frequency.append(dict(case=case,k_rms=kk,transitions=transitions,matched_fit=valid,
            complete_controls=coverage,controls_valid=controls_valid,observed_direction=direction,
            classification=direction if valid and coverage and controls_valid else 'numerically_unresolved_'+direction))
    summary=dict(records=records,controls=controls,order_comparisons=order_comparisons,
        rotations=rotations,amplitude_comparisons=amplitudes,hypotheses=dict(frequency=frequency),
        skipped=skipped,failures=failures,completed_records=len(records),manifest_sha256=manifest_hash,
        input_hashes=input_hashes,source_sha256={str(p):sha(p) for p in [HERE/'ANALYZE.py',HERE/'NTK.py',HERE/'PLAN.md']},
        normalization='All relative curve RMS errors divide by reference curve RMS; shape errors separately normalize each curve by RMS. No gains fitted to a baseline.',
        comparison_scope='Final means each run own saved time; matched_fit requires relative training MSE<=1e-4; settled comparisons separately require both stopping gates.',
        elapsed_seconds=time.perf_counter()-start,
        environment=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),
                         threads={k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']}),
        command=[sys.executable,*sys.argv])
    with (out/'summary.json').open('x') as handle:
        json.dump(summary,handle,indent=2,allow_nan=False)
    print(json.dumps(dict(completed=len(records),skipped=len(skipped),failures=len(failures),
                         elapsed=summary['elapsed_seconds'],output=str(out))),flush=True)
    return summary


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--campaign',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();run(args.campaign,args.output)
