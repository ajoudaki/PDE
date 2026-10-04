"""Independent deterministic and raw-archive audit; no scientific training.

Run with the campaign's Python and a fresh --output directory. Tiny RHS/JVP
and Heun fixtures are numerical verification only. All audit outputs remain
inside this study's generated namespace.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import importlib
import json
import os
from pathlib import Path
import sys

for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(name, '1')
import numpy as np
import torch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT/'code'))
from pde.finite_torch import NetworkEngine
from neuron_sampling_multidata import prepare_witness, build_sampler


def error(actual, expected, tolerance=3e-12):
    actual, expected = np.asarray(actual), np.asarray(expected)
    value = float(np.max(np.abs(actual-expected)))
    np.testing.assert_allclose(actual, expected, rtol=tolerance, atol=tolerance)
    return value


def unit_rows(rng, count, dimension):
    values = rng.normal(size=(count, dimension))
    return values/np.linalg.norm(values, axis=1, keepdims=True)


def automatic_jets(d, m):
    """Differentiate the scalar dense loss, then its gradient-flow vector."""
    rng = np.random.default_rng(773000+100*d+m)
    n = 19
    A = rng.normal(size=(n, d))
    M = rng.normal(size=(n, n))/np.sqrt(n)
    U = unit_rows(rng, m, d)
    labels = rng.uniform(-.2, .2, size=m)
    probes = unit_rows(rng, 11, d)
    witness = prepare_witness(A, M, U, labels, setup_probes=probes)
    tensor = lambda value: torch.tensor(value, dtype=torch.float64)
    inputs, target, panel = tensor(U), tensor(labels), tensor(witness['probes'])
    initial = tuple(tensor(value).requires_grad_() for value in (A, M, np.zeros(n)))

    def gradient_flow(A, M, w):
        h = torch.tanh(A @ inputs.T)
        g = torch.tanh(M @ h)
        prediction = w @ g/n
        loss = ((prediction-target)**2).mean()
        gradients = torch.autograd.grad(loss, (A, M, w), create_graph=True)
        return -n*gradients[0], -gradients[1], -n*gradients[2]

    velocity = gradient_flow(*initial)
    _, acceleration = torch.autograd.functional.jvp(gradient_flow, initial, velocity)

    def query_fields(A, M, w):
        h = torch.tanh(A @ panel.T)
        g = torch.tanh(M @ h)
        return h, g

    def backward_fields(A, M, w):
        h = torch.tanh(A @ inputs.T)
        g = torch.tanh(M @ h)
        delta = w[:, None]*(1-g*g)
        return delta, M.T @ delta

    # At zero readout, A'=M'=0, so the field Hessian term vanishes.
    _, second_fields = torch.autograd.functional.jvp(query_fields, initial, acceleration)
    _, backward_first = torch.autograd.functional.jvp(backward_fields, initial, velocity)
    sources = {name: value for name, value, _ in witness['groups1']+witness['groups2']}
    return dict(d=d, m=m, errors={
        'h2': error(sources['h2'], second_fields[0].detach()),
        'g2': error(sources['g2'], second_fields[1].detach()),
        'delta1': error(witness['delta_dot'], backward_first[0].detach()),
        'reverse_delta1': error(witness['reverse'], backward_first[1].detach()),
        'W_h2': error(sources['W_h2'], M @ second_fields[0].detach().numpy()),
    })


def sampler_checks(d, m):
    rng = np.random.default_rng(774000+100*d+m)
    n, N = 29, 20
    A = rng.normal(size=(n, d))
    M = rng.normal(size=(n, n))/np.sqrt(n)
    U = unit_rows(rng, m, d)
    labels = rng.uniform(-.2, .2, size=m)
    probes = unit_rows(rng, 12, d)
    witness = prepare_witness(A, M, U, labels, setup_probes=probes)
    sampler = build_sampler(A, M, U, labels, N, setup_probes=probes,
                            basis_rank=8, witness=witness)
    actual_count = sum(sampler[key].size for key in ('A', 'B', 'w', 'mu', 'nu'))+U.size+labels.size
    expected_count = N*N+(d+3)*N+m*(d+1)
    assert actual_count == expected_count == sampler['diagnostics']['total_retained_scalar_count']
    assert set(sampler) == {'A', 'B', 'w', 'mu', 'nu', 'selected_first', 'selected_second', 'diagnostics'}
    assert sampler['A'].shape == (N, d)
    assert np.all(sampler['w'] == 0)
    mu, nu, B = (sampler[key] for key in ('mu', 'nu', 'B'))
    for mass in (mu, nu):
        assert np.all(mass > 0) and abs(mass.sum()-1) < 3e-14
    u, v = rng.normal(size=N), rng.normal(size=N)
    Bstar = B.T*nu[None, :]/mu[:, None]
    adjoint_error = error(np.dot(nu*(B @ u), v), np.dot(mu*u, Bstar @ v))
    rejected = []
    for name, arguments in (
        ('labels', dict(labels=labels+.01, setup_probes=probes)),
        ('setup_probes', dict(labels=labels, setup_probes=np.roll(probes, 1, axis=0))),
    ):
        try:
            build_sampler(A, M, U, arguments['labels'], N, basis_rank=8,
                setup_probes=arguments['setup_probes'], witness=witness)
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('mismatched witness accepted: '+name)
    return dict(d=d, m=m, selected_width=N, total_retained_scalar_count=actual_count,
                weighted_adjoint_error=adjoint_error, mismatched_witness_rejected=rejected,
                final_optimizer_success=[sampler['diagnostics'][f'cubature{k}']['fits'][-1]['success'] for k in (1,2)])


def original_witness_equivalence():
    from neuron_sampling_setup import prepare_witness as original_witness
    rng = np.random.default_rng(775999)
    A = rng.normal(size=(31, 2))
    M = rng.normal(size=(31, 31))/np.sqrt(31)
    U = np.array([[1., 0.], [.6, .8]])
    labels = np.array([.2, -.1])
    theta = np.pi*np.arange(32)/32
    probes = np.column_stack((np.cos(theta), np.sin(theta)))
    old = original_witness(A, M, U, labels, probe_count=32)
    new = prepare_witness(A, M, U, labels, setup_probes=probes)
    maximum = 0.
    for key in ('probes', 'H', 'Z', 'G', 'delta_dot', 'reverse'):
        maximum = max(maximum, error(new[key], old[key], tolerance=0.))
    for key in ('groups1', 'groups2'):
        for (name1, source1, weight1), (name2, source2, weight2) in zip(old[key], new[key]):
            assert (name1, weight1) == (name2, weight2)
            maximum = max(maximum, error(source1, source2, tolerance=0.))
    return dict(bitwise_original_circle_witness=True, maximum_error=maximum)


def runtime_checks(module, d, m, out):
    rng = np.random.default_rng(775000+100*d+m)
    tensor = lambda value: torch.tensor(value, dtype=torch.float64)
    inputs = tensor(unit_rows(rng, m, d))
    target = tensor(rng.uniform(-.2, .2, m))
    engine = NetworkEngine(d, 13, 776000+100*d+m, device='cpu', dtype=torch.float64)
    state = engine.initial_state()
    state.c.copy_(tensor(rng.uniform(-.3, .3, 13)))
    data = engine.prepare_data(inputs, target)
    s = module.Batch(state.w[None], state.M[None], state.c[None])
    errors = {}
    for name, actual, expected in (
        ('rhs', module.rhs(s, inputs, target), engine.rhs(state, data)),
        ('heun', module.heun(s, inputs, target, .017), engine.heun_step(state, data, .017)),
    ):
        errors[name] = max(error(a.detach()[0], b) for a,b in zip(actual.arrays(), (expected.w, expected.M, expected.c)))
    A = tensor(rng.normal(size=(1, 5, d))).requires_grad_()
    K = tensor(rng.normal(size=(1, 4, 5))*.2).requires_grad_()
    w = tensor(rng.normal(size=(1, 4))*.2).requires_grad_()
    mu = tensor([[.05, .1, .2, .25, .4]])
    nu = tensor([[.1, .2, .3, .4]])
    h = torch.tanh(A @ inputs.T)
    g = torch.tanh(K @ (mu[:, :, None]*h))
    prediction = ((nu*w)[:, :, None]*g).sum(dim=1)
    gradients = torch.autograd.grad(((prediction-target)**2).mean(), (A, K, w))
    oracle = (-gradients[0]/mu[:, :, None],
              -gradients[1]/(nu[:, :, None]*mu[:, None, :]), -gradients[2]/nu)
    actual = module.rhs(module.Batch(A, K, w), inputs, target, (mu, nu))
    errors['nonuniform_autograd'] = max(error(a.detach(), b.detach()) for a,b in zip(actual.arrays(), oracle))
    # Use a square model for the experiment's retained restart format.
    initial = module.Batch(A.detach().clone(), tensor(rng.normal(size=(1,5,5))*.2),
                           tensor(rng.normal(size=(1,5))*.2))
    masses = (mu, mu.flip(dims=(1,)))
    uninterrupted, first = initial.clone(), initial.clone()
    with torch.no_grad():
        for _ in range(8):
            uninterrupted = module.heun(uninterrupted, inputs, target, .011, masses)
        for _ in range(4):
            first = module.heun(first, inputs, target, .011, masses)
        filename = out/f'restart_fixture_d{d}_m{m}.npz'
        np.savez(filename, U=inputs.numpy(), labels=target.numpy(), time=np.array(.044),
            model_indices=np.array([2]), model_2_A=first.A[0].numpy(),
            model_2_K=first.M[0].numpy(), model_2_w=first.w[0].numpy(),
            model_2_mu=masses[0][0].numpy(), model_2_nu=masses[1][0].numpy())
        restarted, restart_masses, restart_U, restart_y, restart_time = module.load_reduced_restart(filename, 2)
        assert restart_time == .044
        for _ in range(4):
            restarted = module.heun(restarted, restart_U, restart_y, .011, restart_masses)
    errors['retained_file_restart'] = max(error(a,b,tolerance=0.) for a,b in zip(uninterrupted.arrays(), restarted.arrays()))
    produced, setup_A, setup_M = module.make_dense(13, 776000+100*d+m, 'cpu', torch.float64, d)
    errors['initialization_A'] = error(setup_A, engine.initial.w)
    errors['initialization_M'] = error(setup_M, engine.initial.M)
    assert tuple(produced.A.shape) == (2,13,d) and bool((produced.w == 0).all())
    return dict(d=d, m=m, errors=errors)


def audit_archives(run_roots):
    """Compute every number directly from arrays, without runner validation."""
    rows, manifests = [], []
    for root in map(Path, run_roots):
        root = root.resolve()
        if not root.is_relative_to(ROOT/'data/generated/closure_sampling_20261003'):
            raise ValueError('run root outside this study')
        provenance = json.loads((root/'provenance.json').read_text())
        for source, digest in provenance['source_hashes'].items():
            assert hashlib.sha256((root/'sources'/source).read_bytes()).hexdigest() == digest
        config = json.loads((root/'config.resolved.json').read_text())
        for kind in ('input', 'resolved'):
            assert hashlib.sha256((root/f'config.{kind}.json').read_bytes()).hexdigest() == provenance[f'config_{kind}_sha256']
        manifests.append(dict(root=str(root), source_archive_hashes_verified=True,
                              config_hashes_verified=True, source_hashes=provenance['source_hashes']))
        for path in sorted(root.glob('*/record.json')):
            record = json.loads(path.read_text())
            case_root = path.parent
            for name, digest in record.items():
                if name.endswith('_sha256'):
                    assert hashlib.sha256((case_root/name[:-7]).read_bytes()).hexdigest() == digest
            with np.load(case_root/'observations.npz', allow_pickle=False) as archive:
                arrays = {name: archive[name] for name in archive.files}
            times, predictions = arrays['times'], arrays['predictions']
            U, labels, panel = (arrays[name] for name in ('U', 'labels', 'panel'))
            dataset = config['datasets'][record['dataset_id']]
            for actual, key in ((U, 'U'), (labels, 'labels'), (panel, 'query_panel')):
                np.testing.assert_array_equal(actual, dataset[key])
            n, d, m = record['n'], record['d'], record['m']
            assert U.shape == (m, d) and len(labels) == m
            assert predictions.shape == (len(times), len(record['model_names']), len(panel))
            assert times[0] == 0 and times[-1] == record['last_time'] and np.all(np.diff(times)>0)
            assert np.all(predictions[0] == 0) and np.all(arrays['training_predictions'][0] == 0)
            assert all(np.isfinite(value).all() for value in arrays.values())
            residuals = np.sqrt(np.mean((arrays['training_predictions']-labels)**2, axis=-1))
            residual_error = error(residuals, arrays['residual_rms'])
            discrepancy = predictions-predictions[:, :1]
            primary = np.sqrt(np.mean(np.max(np.abs(discrepancy), axis=0)**2, axis=-1))
            common = times <= min(config['horizon'], times[-1])+1e-10
            common_primary = np.sqrt(np.mean(np.max(np.abs(discrepancy[common]), axis=0)**2, axis=-1))
            sup_rms = np.max(np.sqrt(np.mean(discrepancy**2, axis=-1)), axis=0)
            endpoint = np.sqrt(np.mean(discrepancy[-1]**2, axis=-1))
            supremum = np.max(np.abs(discrepancy), axis=(0, 2))
            for index, metrics in enumerate(record['metrics']):
                for key, values in (('rms_of_time_sup', primary), ('sup_of_time_rms', sup_rms),
                                    ('endpoint_rms', endpoint), ('sup_panel_time', supremum)):
                    error(metrics[key], values[index])
                    error(metrics['root_scaled'][key], np.sqrt(n)*values[index])
                    expected_ratio = values[index]/values[1] if values[1] else None
                    if expected_ratio is None:
                        assert metrics['ratio_to_dense_copy'][key] is None
                    else:
                        error(metrics['ratio_to_dense_copy'][key], expected_ratio)
            tail_mask = times >= times[-1]-config['tail_window']-1e-10
            tail = np.max(np.abs(predictions[tail_mask]-predictions[-1]), axis=(0, 2))
            settled = (residuals[-1]<=config['fit_tolerance']) & (tail<=config['settlement_tolerance'])
            settled &= times[-1]>=config['tail_window']-1e-10
            np.testing.assert_array_equal(record['settled'], settled)
            error(record['last_ten_time_change'], tail)
            restart_error, total_counts, construction_valid, diagnostic_summary = 0., [], [], []
            expected_keys = {'U', 'labels', 'time', 'model_indices'}
            with np.load(case_root/'reduced_restart.npz', allow_pickle=False) as restart:
                np.testing.assert_array_equal(restart['U'], U)
                np.testing.assert_array_equal(restart['labels'], labels)
                assert float(restart['time']) == times[-1]
                np.testing.assert_array_equal(restart['model_indices'], np.arange(2, 2+len(record['samplers'])))
                for j, spec in enumerate(record['samplers'], start=2):
                    prefix, N = f'model_{j}_', spec['width']
                    expected_keys.update(prefix+name for name in ('A', 'K', 'w', 'mu', 'nu'))
                    A, K, w, mu, nu = (restart[prefix+name] for name in ('A', 'K', 'w', 'mu', 'nu'))
                    assert [value.shape for value in (A,K,w,mu,nu)] == [(N,d),(N,N),(N,),(N,),(N,)]
                    count = sum(value.size for value in (A,K,w,mu,nu))+U.size+labels.size
                    assert count == N*N+(d+3)*N+m*(d+1) == spec['total']
                    if 'coefficient_multiplier' in spec:
                        budget = 2550*spec['coefficient_multiplier']*(np.log(n)/np.log(512))**4
                        assert count <= budget+1e-9
                        assert N == n or (N+1)**2+(d+3)*(N+1)+m*(d+1) > budget-1e-9
                    total_counts.append(count)
                    for mass in (mu, nu):
                        assert np.all(mass>0) and abs(mass.sum()-1)<2e-8
                    for query, target in ((panel,predictions[-1,j]), (U,arrays['training_predictions'][-1,j])):
                        actual = (nu*w) @ np.tanh(K @ (mu[:,None]*np.tanh(A @ query.T)))
                        restart_error = max(restart_error,error(actual,target,tolerance=2e-11))
                    diagnostics = record['sampler_diagnostics'][j-2]
                    valid = all(diagnostics[f'cubature{k}']['fits'][-1]['success'] and
                                diagnostics[f'frame{k}']['discarded_directions'] == 0 for k in (1,2))
                    construction_valid.append(valid)
                    diagnostic_summary.append(dict(model_index=j, name=spec['name'],
                        priority_rank=[diagnostics[f'basis{k}']['priority_rank'] for k in (1,2)],
                        retained_rank=[diagnostics[f'basis{k}']['retained_rank'] for k in (1,2)],
                        g0_projection_relative_frobenius=diagnostics['basis2']['source_residuals']['g0']['relative_frobenius'],
                        h0_projection_relative_frobenius=diagnostics['basis1']['source_residuals']['h0']['relative_frobenius'],
                        final_optimizer_success=[diagnostics[f'cubature{k}']['fits'][-1]['success'] for k in (1,2)],
                        final_optimizer_status=[diagnostics[f'cubature{k}']['fits'][-1]['status'] for k in (1,2)],
                        discarded_frame_directions=[diagnostics[f'frame{k}']['discarded_directions'] for k in (1,2)]))
                assert set(restart.files) == expected_keys
            with np.load(case_root/'initial_setup.npz', allow_pickle=False) as initial:
                np.testing.assert_array_equal(initial['setup_directions'], dataset['setup_probes'])
                np.testing.assert_array_equal(initial['setup_probes'], np.concatenate((U,dataset['setup_probes'])))
                assert np.all(initial['dense_w']==0)
                for j, spec in enumerate(record['samplers'],start=2):
                    prefix = f'model_{j}_'
                    np.testing.assert_array_equal(initial[prefix+'A'],initial['reference_setup_A0'][initial[prefix+'selected_first']])
                    assert np.all(initial[prefix+'w']==0)
                    error(initial[prefix+'K'],initial[prefix+'B']/initial[prefix+'mu'][None,:],tolerance=0.)
            rows.append(dict(run_root=str(root),case_id=case_root.name,dataset_id=record['dataset_id'],
                stage=config['stage'],seed=record['seed'],n=n,d=d,m=m,
                primary=primary.tolist(),common_initial_horizon_primary=common_primary.tolist(),
                primary_scaled=(np.sqrt(n)*primary).tolist(),settled=settled.tolist(),
                retained_counts=total_counts, construction_valid=construction_valid,
                setup_failure_count=len(record['setup_failures']), setup_failures=record['setup_failures'],
                diagnostic_summary=diagnostic_summary,last_time=float(times[-1]),
                residual_recomputation_error=residual_error,restart_prediction_error=restart_error,
                query_rank=int(np.linalg.matrix_rank(panel)),
                maximum_absolute_setup_query_inner_product=float(np.max(np.abs(panel@np.asarray(dataset['setup_probes']).T)))))
    return dict(manifests=manifests,cases=rows,completed_case_count=len(rows),
                maximum_restart_prediction_error=max((row['restart_prediction_error'] for row in rows),default=0.))


def verify_priority_projection(run_roots):
    """Independently reconstruct saturated rank16 priorities from initialization."""
    from pde.finite_network import initialize
    result = []
    wanted = {'circle8_smooth', 'embedded_circle8_d3', 'embedded_circle8_d5'}
    for root in map(Path, run_roots):
        config = json.loads((root/'config.resolved.json').read_text())
        for dataset_id in sorted(wanted.intersection(config['datasets'])):
            record_path = root/f'{dataset_id}_n2048_s9411'/'record.json'
            if not record_path.is_file():
                continue
            record = json.loads(record_path.read_text())
            if not record['samplers']:
                continue
            dataset = config['datasets'][dataset_id]
            U, setup = (np.asarray(dataset[key]) for key in ('U', 'setup_probes'))
            n, d, m = record['n'], record['d'], record['m']
            initial = initialize(n, 2, d, seed=record['seed'])
            A, M = initial.weights
            H = np.tanh(A @ np.concatenate((U,setup)).T)
            Z = M @ H
            G = np.tanh(Z)
            priority = np.concatenate((G[:,:m], Z[:,:m]),axis=1)
            basis, singular, _ = np.linalg.svd(priority,full_matrices=False)
            resolved = int(np.sum(singular>1e-10*max(singular[0],1.)))
            assert resolved == 16
            Q = basis[:,:16]
            defect = float(np.linalg.norm(G-Q@(Q.T@G))/np.linalg.norm(G))
            expected = record['sampler_diagnostics'][0]['basis2']['source_residuals']['g0']['relative_frobenius']
            error(defect,expected,tolerance=3e-13)
            result.append(dict(dataset_id=dataset_id,n=n,d=d,m=m,seed=record['seed'],
                full_priority_rank=resolved,rank_budget=16,
                independently_recomputed_g0_projection_relative_frobenius=defect,
                stored_g0_projection_relative_frobenius=expected,
                recomputation_error=abs(defect-expected)))
    return result


def audit_resume_prefixes(pairs):
    results = []
    for original, resumed in pairs:
        original, resumed = Path(original), Path(resumed)
        for failure in sorted(original.glob('*/failure.json')):
            partial_path = failure.parent/'partial_observations.npz'
            complete_path = resumed/failure.parent.name/'observations.npz'
            if not partial_path.is_file() or not complete_path.is_file():
                continue
            with np.load(partial_path,allow_pickle=False) as partial, np.load(complete_path,allow_pickle=False) as complete:
                indices = np.searchsorted(complete['times'],partial['times'])
                np.testing.assert_array_equal(complete['times'][indices],partial['times'])
                for name in ('U','labels','panel'):
                    np.testing.assert_array_equal(partial[name],complete[name])
                differences, bitwise = {}, {}
                for name in ('predictions','training_predictions','residual_rms','feature_motion'):
                    differences[name] = error(partial[name],complete[name][indices],tolerance=2e-12)
                    bitwise[name] = bool(np.array_equal(partial[name],complete[name][indices]))
                results.append(dict(case_id=failure.parent.name,original_root=str(original),
                    resumed_root=str(resumed),partial_observation_count=len(indices),
                    last_partial_observation_time=float(partial['times'][-1]),
                    complete_time=float(complete['times'][-1]),maximum_differences=differences,
                    bitwise_equal=bitwise))
    return results


def audit_refinement_pairs(pairs):
    checks = []
    for coarse_path, fine_path in pairs:
        coarse_path, fine_path = Path(coarse_path), Path(fine_path)
        coarse_record = json.loads((coarse_path/'record.json').read_text())
        fine_record = json.loads((fine_path/'record.json').read_text())
        assert all(coarse_record[key] == fine_record[key] for key in ('dataset_id','n','seed','d','m'))
        assert abs(2*fine_record['dt']-coarse_record['dt'])<1e-14
        with np.load(coarse_path/'observations.npz',allow_pickle=False) as archive:
            coarse = {key:archive[key] for key in archive.files}
        with np.load(fine_path/'observations.npz',allow_pickle=False) as archive:
            fine = {key:archive[key] for key in archive.files}
        for key in ('U','labels'):
            np.testing.assert_array_equal(coarse[key],fine[key])
        assert fine['times'][-1] >= coarse['times'][-1]-1e-10
        assert len(fine['panel']) >= 2*len(coarse['panel'])
        assert np.max(np.diff(fine['times'])) <= np.max(np.diff(coarse['times']))/2+1e-10
        times = np.searchsorted(fine['times'],coarse['times'])
        np.testing.assert_array_equal(coarse['times'],fine['times'][times])
        distance = np.max(np.abs(coarse['panel'][:,None]-fine['panel'][None]),axis=2)
        queries = np.argmin(distance,axis=1)
        assert len(set(queries)) == len(queries)
        error(coarse['panel'],fine['panel'][queries],tolerance=1e-12)
        common_models = [name for name in coarse_record['model_names'] if name in fine_record['model_names']]
        with np.load(coarse_path/'initial_reduced_runtime.npz',allow_pickle=False) as cinit, np.load(fine_path/'initial_reduced_runtime.npz',allow_pickle=False) as finit:
            for name in common_models:
                ci, fi = coarse_record['model_names'].index(name),fine_record['model_names'].index(name)
                if ci<2:
                    continue
                for key in ('A','K','w','mu','nu'):
                    np.testing.assert_array_equal(cinit[f'model_{ci}_{key}'],finit[f'model_{fi}_{key}'])
        with np.load(coarse_path/'initial_setup.npz',allow_pickle=False) as cinit, np.load(fine_path/'initial_setup.npz',allow_pickle=False) as finit:
            for key in ('setup_directions','dense_A','dense_w'):
                np.testing.assert_array_equal(cinit[key],finit[key])
        final_mask = fine['times']<=coarse['times'][-1]+1e-10
        model_checks = []
        for name in common_models:
            ci, fi = coarse_record['model_names'].index(name),fine_record['model_names'].index(name)
            same_point_error = float(np.max(np.abs(coarse['predictions'][:,ci]-fine['predictions'][times,fi][:,queries])))
            coarse_difference = coarse['predictions'][:,ci]-coarse['predictions'][:,0]
            fine_difference = fine['predictions'][final_mask,fi]-fine['predictions'][final_mask,0]
            metric = lambda e:float(np.sqrt(np.mean(np.max(np.abs(e),axis=0)**2)))
            coarse_metric, fine_shared_metric = metric(coarse_difference),metric(fine_difference[:,queries])
            fine_full_metric = metric(fine_difference)
            threshold = max(1e-4,.05*coarse_metric)
            metric_change = abs(coarse_metric-fine_shared_metric)
            model_checks.append(dict(model=name,same_point_prediction_change=same_point_error,
                common_query_primary_change=metric_change,extra_panel_primary_change=abs(fine_full_metric-fine_shared_metric),
                threshold=threshold,passed=same_point_error<=threshold and metric_change<=threshold))
        checks.append(dict(coarse=str(coarse_path),fine=str(fine_path),
            initialized_reduced_states_bitwise_equal=True,setup_directions_bitwise_equal=True,
            common_horizon=float(coarse['times'][-1]),models=model_checks,
            passed=all(row['passed'] for row in model_checks)))
    return checks


def audit_worker_intervals(roots):
    intervals = []
    for root in map(Path,roots):
        status = json.loads((root/'status.json').read_text())
        if 'wall_seconds' not in status:
            raise ValueError('worker is not finished: '+str(root))
        start = (root/'provenance.json').stat().st_mtime
        end = (root/'status.json').stat().st_mtime
        intervals.append(dict(root=str(root),start_unix=start,end_unix=end,
            start_utc=datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),
            end_utc=datetime.datetime.fromtimestamp(end,datetime.timezone.utc).isoformat(),
            worker_wall_seconds=status['wall_seconds'],
            timer_start_difference_from_provenance_seconds=end-status['wall_seconds']-start,
            peak_gpu_allocated=status['peak_gpu_allocated']))
    merged = []
    for interval in sorted(intervals,key=lambda row:row['start_unix']):
        a,b=interval['start_unix'],interval['end_unix']
        if merged and a<=merged[-1][1]:
            merged[-1][1]=max(merged[-1][1],b)
        else:
            merged.append([a,b])
    total=sum(b-a for a,b in merged)
    return dict(intervals=intervals,merged_intervals=merged,active_worker_union_seconds=total,
        limit_seconds=1500.,within_time_limit=total<=1500.,
        maximum_gpu_allocation_bytes=max(row['peak_gpu_allocated'] for row in intervals),
        within_allocation_limit=all(row['peak_gpu_allocated']<=8*2**30 for row in intervals),
        timing_method='provenance mtime through final status mtime; excludes idle gaps and avoids double-counting concurrent workers')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--skip-runtime', action='store_true')
    parser.add_argument('--runs', nargs='*', default=[])
    parser.add_argument('--archives-only', action='store_true')
    parser.add_argument('--source-defects', action='store_true')
    parser.add_argument('--resume-pair', nargs=2, action='append', default=[])
    parser.add_argument('--refinement-pair', nargs=2, action='append', default=[])
    parser.add_argument('--budget-roots', nargs='*', default=[])
    args = parser.parse_args()
    out = Path(args.output).resolve()
    if not out.is_relative_to(ROOT/'data/generated/closure_sampling_20261003'):
        raise ValueError('audit output must be inside this study generated namespace')
    out.mkdir(parents=True, exist_ok=False)
    sources = [HERE/'neuron_sampling_setup.py', HERE/'neuron_sampling_multidata.py',
               HERE/'gpu_sampling_experiment.py', HERE/'gpu_rms_growth_experiment.py',
               ROOT/'code/pde/finite_network.py', ROOT/'code/pde/finite_torch.py',
               ROOT/'code/pde/observable_torch_p1.py', Path(__file__)]
    if not args.skip_runtime:
        sources.append(HERE/'gpu_multidata_experiment.py')
    source_hashes = {}
    for path in sources:
        relative = str(path.relative_to(ROOT))
        data = path.read_bytes()
        source_hashes[relative] = hashlib.sha256(data).hexdigest()
        destination = out/'sources'/relative
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_bytes(data)
    torch.set_num_threads(1)
    cases = [(2, 2), (2, 4), (2, 8), (3, 4), (5, 8)]
    result = {}
    if not args.archives_only:
        result.update(original_witness_equivalence=original_witness_equivalence(),
                      jets=[automatic_jets(d,m) for d,m in cases],
                      samplers=[sampler_checks(d,m) for d,m in [(3,4), (5,8)]])
    if not args.skip_runtime and not args.archives_only:
        module = importlib.import_module('gpu_multidata_experiment')
        result['runtime'] = [runtime_checks(module, d, m, out) for d,m in cases]
    if args.runs:
        result['archives'] = audit_archives(args.runs)
        if args.source_defects:
            result['priority_projection_checks'] = verify_priority_projection(args.runs)
    if args.resume_pair:
        result['resume_prefix_checks'] = audit_resume_prefixes(args.resume_pair)
    if args.refinement_pair:
        result['refinement_checks'] = audit_refinement_pairs(args.refinement_pair)
    if args.budget_roots:
        result['worker_budget'] = audit_worker_intervals(args.budget_roots)
    for path in sources:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source_hashes[str(path.relative_to(ROOT))]
    result['source_hashes'] = source_hashes
    result['command'] = sys.argv
    result['python'] = sys.executable
    result['torch'] = torch.__version__
    result['numpy'] = np.__version__
    result['result'] = 'PASS'
    (out/'deterministic_checks.json').write_text(json.dumps(result, indent=2)+'\n')
    if args.archives_only:
        print(json.dumps(dict(result=result['result'], output=str(out),
            completed_case_count=result.get('archives',{}).get('completed_case_count'),
            maximum_restart_prediction_error=result.get('archives',{}).get('maximum_restart_prediction_error')),indent=2))
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
