"""Independent raw-moment reconstruction of saved higher-order runs.

Does not import the experiment producer. Uses a materialized middle matrix
and the manuscript's unnormalized moments for the velocity audit.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from threadpoolctl import threadpool_limits


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fields(a, w, middle, inputs):
    h = np.tanh(a @ inputs)
    g = np.tanh(middle @ h)
    d = w[:, None] * (1 - g*g)
    ell = (1 - h*h) * (middle.T @ d)
    return h, g, d, ell, w @ g / len(w)


def matrix_from_raw(w0, forward, backward, clock):
    q, n, m = forward.shape
    result = w0.copy()
    for j in range(q):
        result -= 2*(2*j+1)/(m*n*clock) * (backward[j] @ forward[j].T)
    return result


def raw_matrix_velocity(forward, backward, h, d, residual, clock):
    q, n, m = forward.shape
    rho = np.linalg.norm(residual)/np.sqrt(m)
    result = np.zeros((n, n))
    for j in range(q):
        lower_h = sum(((2*i+1)*forward[i] for i in range(j)), np.zeros_like(h))
        lower_d = sum(((2*i+1)*backward[i] for i in range(j)), np.zeros_like(d))
        hdot = rho*h - rho/clock*(j*forward[j]+lower_h)
        ddot = d*residual - rho/clock*(j*backward[j]+lower_d)
        result -= 2*(2*j+1)/(m*n*clock)*(ddot @ forward[j].T + backward[j] @ hdot.T)
        result += 2*(2*j+1)*rho/(m*n*clock**2)*(backward[j] @ forward[j].T)
    return result


def check_run(run, output):
    begin = time.perf_counter()
    source = Path(__file__).resolve()
    taskfile = source.parent/'circle_task_inputs.json'
    tasks = {t['case']: t for t in json.loads(taskfile.read_text())['tasks'][:2]}
    initialization = np.load(run/'initialization.npz')
    w0 = initialization['w0']
    results = json.loads((run/'results.json').read_text())
    # Producer stores a list of case/order records.
    records = results['results']
    audits = []
    def require(name, error, tolerance, row):
        row[name] = float(error)
        if not np.isfinite(error) or error > tolerance:
            raise AssertionError((name, error, tolerance, row))

    for record in records:
        case = record['case']
        order = int(record['order'])
        directory = run/case/f'q{order}'/record['selected']
        task = tasks[case]
        inputs = np.asarray(task['normalized_inputs_u']).T
        labels = np.asarray(task['labels'])
        curves = np.load(directory/'curves.npz')
        queries = np.stack((np.cos(curves['angles']), np.sin(curves['angles'])))
        statefiles = [directory/'endpoint_states.npz'] + sorted(directory.glob('handoff_*.npz'))
        for path in statefiles:
            saved = np.load(path)
            endpoint = path.name == 'endpoint_states.npz'
            a = saved['closure_a' if endpoint else 'a']
            w = saved['closure_readout' if endpoint else 'readout']
            clock = float(saved['clock'][0])
            forward = saved['keys']*clock
            backward = -saved['values']/2
            middle = matrix_from_raw(w0, forward, backward, clock)
            h, g, d, ell, prediction = fields(a, w, middle, inputs)
            residual = prediction-labels
            q, n, m = forward.shape
            row = dict(case=case, order=order, state=path.name, sha256=digest(path))
            require('order_error', abs(q-order), 0, row)
            if endpoint:
                require('train_residual_error', np.max(np.abs(residual-curves['closure_residual'][-1])), 2e-10, row)
                outputs = []
                for start in range(0, queries.shape[1], 256):
                    outputs.append(w @ np.tanh(middle @ np.tanh(a @ queries[:, start:start+256]))/n)
                require('circle_output_error', np.max(np.abs(np.concatenate(outputs)-curves['closure_output'])), 2e-10, row)
            else:
                require('handoff_residual_error', np.max(np.abs(residual-saved['residual'])), 2e-10, row)
                weights = (2*np.arange(q)+1)[:, None, None]
                key = np.sum(weights*forward, axis=0)/clock
                value = -2*np.sum(weights*backward, axis=0)
                matrix = 2/m*(g.T @ g/n + (inputs.T @ inputs)*(ell.T @ ell/n)
                              + (d.T @ d/n)*(h.T @ key/n))
                drift = np.sum((d.T @ value/n)*(h.T @ (h-key)/n), axis=1)/(m*np.sqrt(m)*clock)
                require('training_matrix_error', np.max(np.abs(matrix-saved['matrix'])), 2e-10, row)
                require('training_drift_error', np.max(np.abs(drift-saved['drift'])), 2e-10, row)
                # Complete derivative via the raw moment equations, without the
                # endpoint-sum cancellation used by the producer.
                middle_dot = raw_matrix_velocity(forward, backward, h, d, residual, clock)
                adot = -2/m*(ell*residual) @ inputs.T
                wdot = -2/m*g @ residual
                direct_velocity = wdot @ g/n + np.sum(d*(middle_dot @ h), axis=0)/n
                direct_velocity += np.sum(ell*(adot @ inputs), axis=0)/n
                response_velocity = -saved['matrix'] @ residual + np.linalg.norm(residual)*saved['drift']
                require('raw_velocity_error', np.max(np.abs(direct_velocity-response_velocity)), 2e-10, row)
                # Fixed nontraining query subset checks the passive response.
                indices = np.array([17, 381, 1429, 2671, 4095, 6049, 8111])
                u = queries[:, indices]
                qh, qg, qd, qell, qprediction = fields(a, w, middle, u)
                cmatrix = 2/m*(qg.T @ g/n+(u.T @ inputs)*(qell.T @ ell/n)
                               +(qd.T @ d/n)*(qh.T @ key/n))
                bvector = np.sum((qd.T @ value/n)*(qh.T @ (h-key)/n), axis=1)/(m*np.sqrt(m)*clock)
                require('query_output_error', np.max(np.abs(qprediction-saved['query_f'][indices])), 2e-10, row)
                require('query_matrix_error', np.max(np.abs(cmatrix-saved['query_c'][indices])), 2e-10, row)
                require('query_drift_error', np.max(np.abs(bvector-saved['query_b'][indices])), 2e-10, row)
                qvelocity = wdot @ qg/n + np.sum(qd*(middle_dot @ qh), axis=0)/n
                qvelocity += np.sum(qell*(adot @ u), axis=0)/n
                require('raw_query_velocity_error', np.max(np.abs(qvelocity+cmatrix @ residual-np.linalg.norm(residual)*bvector)), 2e-10, row)
            audits.append(row)
    payload = dict(passed=True, run=str(run.resolve()), source_sha256=digest(source),
                   task_sha256=digest(taskfile), checks=audits,
                   wall_seconds=time.perf_counter()-begin)
    output.mkdir(parents=True, exist_ok=False)
    (output/'checks.json').write_text(json.dumps(payload, indent=2)+'\n')
    (output/source.name).write_bytes(source.read_bytes())
    print(json.dumps(dict(passed=True, states=len(audits), wall_seconds=payload['wall_seconds'])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    with threadpool_limits(limits=2):
        check_run(arguments.run, arguments.output)
