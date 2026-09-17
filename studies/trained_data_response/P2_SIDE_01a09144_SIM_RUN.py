"""One user-authorized finite reference simulation plus solver refinement.

No maintained API or population surrogate is used. All blocks train by the
exact stored-weight physical GF. See the frozen adjacent SIM_PLAN.json.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

import numpy as np
import scipy
from scipy.integrate import solve_ivp


def main():
    started = time.monotonic()
    study = Path(__file__).resolve().parent
    root = study.parent.parent
    plan_path = study/'P2_SIDE_01a09144_SIM_PLAN.json'
    plan_bytes = plan_path.read_bytes()
    plan = json.loads(plan_bytes)
    out = root/plan['run']
    assert not out.exists(), 'Fresh run directory required.'
    out.mkdir(parents=True)
    (out/plan_path.name).write_bytes(plan_bytes)
    (out/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    os.environ['MPLCONFIGDIR'] = str(out/'matplotlib_cache')
    n = plan['model']['width']
    rng = np.random.default_rng(plan['seed'])
    w0 = rng.standard_normal((n, 2))
    A0 = rng.standard_normal((n, n))/np.sqrt(n)
    c0 = rng.standard_normal(n)/n
    U = np.array(plan['model']['normalized_inputs'])
    labels = np.array(plan['model']['labels'])
    weights = np.array(plan['model']['probabilities'])
    initial = np.concatenate([w0.ravel(), A0.ravel(), c0, [0.]])

    def unpack(state):
        return (state[:2*n].reshape(n, 2),
                state[2*n:2*n+n*n].reshape(n, n), state[2*n+n*n:-1])

    def forward(state):
        w, A, c = unpack(state)
        h1 = np.tanh(w@U.T)
        h2 = np.tanh(A@h1)
        f = c@h2/n
        return h1, h2, f

    def rhs(t, state):
        if time.monotonic()-started > plan['budget']['wall_seconds']:
            raise TimeoutError('Preregistered wall budget exhausted.')
        w, A, c = unpack(state)
        h1, h2, f = forward(state)
        residual = f-labels
        delta2 = c[:, None]*(1-h2*h2)
        backward = A.T@delta2
        dw = -2*((weights*residual)*backward*(1-h1*h1))@U
        dA = -2*((weights*residual)*delta2)@h1.T/n
        dc = -2*h2@(weights*residual)
        dissipation = np.sum(dw*dw)/n+np.sum(dA*dA)+np.sum(dc*dc)/n
        return np.concatenate([dw.ravel(), dA.ravel(), dc, [dissipation]])

    def loss(state):
        return np.sum(weights*(forward(state)[2]-labels)**2)

    def check_energy_direction(state):
        velocity = rhs(0., state)
        actual = np.imag(loss(state+1e-25j*velocity))/1e-25
        expected = -velocity[-1]
        error = float(abs(actual-expected)/max(1., abs(expected)))
        assert error < plan['validity']['RHS_loss_complex_step_relative_error_max']
        return error

    rhs_check = check_energy_direction(initial)
    landmarks = np.array([0., .005, .1, .5, 1., 2., 5., 10., 20., 40.])
    times = np.unique(np.concatenate([np.linspace(0., 40., 201), landmarks]))
    h10, h20, f0 = forward(initial)
    initial_rms = np.array([np.sqrt(np.mean(h10*h10)), np.sqrt(np.mean(h20*h20))])
    columns = ['time', 'loss', 'prediction_1', 'prediction_2',
               'hidden1_rms_displacement', 'hidden2_rms_displacement',
               'hidden1_relative_displacement', 'hidden2_relative_displacement',
               'first_weight_raw_displacement', 'middle_weight_raw_displacement',
               'readout_raw_displacement', 'energy_balance_error']

    def observations(solution):
        rows = []
        for t, state in zip(times, solution.y.T):
            w, A, c = unpack(state)
            h1, h2, f = forward(state)
            rms = np.array([np.sqrt(np.mean((h1-h10)**2)),
                            np.sqrt(np.mean((h2-h20)**2))])
            L = float(np.sum(weights*(f-labels)**2))
            rows.append([t, L, *f, *rms, *(rms/initial_rms),
                         np.linalg.norm(w-w0)/np.sqrt(n), np.linalg.norm(A-A0),
                         np.linalg.norm(c-c0)/np.sqrt(n), L+state[-1]-loss(initial)])
        return np.array(rows)

    solutions, observations_by_run, records = [], [], []
    for name in ['primary', 'refinement']:
        tick = time.monotonic()
        solver = plan['solver']
        solution = solve_ivp(rhs, (0., 40.), initial.copy(), method=solver['method'],
                             rtol=solver[name+'_rtol'], atol=solver[name+'_atol'],
                             max_step=solver['max_step'], t_eval=times)
        assert solution.success, solution.message
        assert np.isfinite(solution.y).all()
        observed = observations(solution)
        energy_error = float(np.max(np.abs(observed[:, -1]))/max(1., loss(initial)))
        loss_increase = float(max(0., np.max(np.diff(observed[:, 1]))))
        assert energy_error <= plan['validity']['normalized_energy_balance_error_max']
        assert loss_increase <= plan['validity']['sampled_loss_increase_max']
        rhs_error_final = check_energy_direction(solution.y[:, -1])
        with (out/(name+'.csv')).open('w', newline='') as handle:
            writer = csv.writer(handle)
            writer.writerow(columns)
            writer.writerows(observed)
        indices = np.array([np.flatnonzero(times == t)[0] for t in landmarks])
        np.savez_compressed(out/(name+'_states.npz'), times=landmarks,
                            states=solution.y[:, indices], width=n,
                            normalized_inputs=U, labels=labels)
        record = dict(name=name, seconds=time.monotonic()-tick, nfev=solution.nfev,
                      message=solution.message, energy_error=energy_error,
                      sampled_loss_increase=loss_increase, rhs_final_error=rhs_error_final)
        records.append(record)
        solutions.append(solution)
        observations_by_run.append(observed)
        print(json.dumps(record), flush=True)

    metric_gap = float(np.max(np.abs(observations_by_run[0][:, 1:-1]
                                      -observations_by_run[1][:, 1:-1])))
    assert metric_gap <= plan['validity']['refinement_max_abs_metric_difference']
    observed = observations_by_run[1]
    final_rms = observed[-1, 4:6]
    if np.all(final_rms >= .05):
        outcome = 'visible_both_layers_in_this_single_finite_run'
    elif np.all(final_rms <= .005):
        outcome = 'tiny_both_layers_in_this_single_finite_run'
    else:
        outcome = 'mixed_or_intermediate_in_this_single_finite_run'

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False})
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.0), constrained_layout=True)
    ax[0].semilogy(times, np.maximum(observed[:, 1], 1e-30), color='#354da1', lw=2)
    ax[0].set(xlabel='Physical training time', ylabel='Mean squared loss',
              title='Training on the two reference inputs', xlim=(0, 40))
    ax[1].plot(times, observed[:, 4], label='Hidden layer 1', color='#087e8b', lw=2)
    ax[1].plot(times, observed[:, 5], label='Hidden layer 2', color='#ca5b36', lw=2)
    ax[1].set(xlabel='Physical training time', ylabel='RMS change from initial activations',
              title='Same neurons, averaged over both inputs', xlim=(0, 40), ylim=(0, None))
    ax[1].legend(frameon=False)
    for axis in ax:
        axis.grid(alpha=.17)
    fig.suptitle(f'Exact model, numerical GF · width {n} · seed {plan["seed"]}', fontsize=13)
    fig.savefig(out/'hidden_motion.png', dpi=180)
    fig.savefig(out/'hidden_motion.pdf')
    plt.close(fig)
    summary = dict(result='VALID_EXPLORATORY_RUN', outcome=outcome,
                   plan_sha256=hashlib.sha256(plan_bytes).hexdigest(),
                   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   command=[sys.executable, '-B', str(Path(__file__).resolve())],
                   cwd=str(root), seed=plan['seed'], width=n,
                   initial_activation_rms=initial_rms.tolist(),
                   initial_predictions=f0.tolist(), rhs_initial_error=rhs_check,
                   solver_records=records, refinement_max_absolute_metric_gap=metric_gap,
                   final=dict(zip(columns, map(float, observed[-1]))),
                   landmarks=[dict(zip(columns, map(float, observed[np.flatnonzero(times == t)[0]])))
                              for t in landmarks],
                   environment=dict(python=platform.python_version(), numpy=np.__version__,
                                    scipy=scipy.__version__, matplotlib=matplotlib.__version__,
                                    platform=platform.platform(), threads=1,
                                    max_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
                   seconds=time.monotonic()-started,
                   limitations=plan['claim_scope'])
    summary['output_hashes'] = {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in out.iterdir() if p.is_file()}
    (out/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
