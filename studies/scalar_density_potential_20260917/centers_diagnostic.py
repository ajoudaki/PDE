"""Exact scalar-field quadrature diagnostic; see centers_diagnostic_plan.md."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.special import roots_hermitenorm


def normal_rule(n):
    z, p = roots_hermitenorm(n)
    return z, p / np.sqrt(2 * np.pi)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    source = Path(__file__).read_bytes()
    (out / 'source.py').write_bytes(source)
    z, p = normal_rule(128)
    nu = p @ np.tanh(z) ** 2
    tau = p @ np.tanh(np.sqrt(nu) * z) ** 2
    eta = 1 / 4096
    m0 = nu * (1 - tau) / np.sqrt((nu + eta) * (tau + eta))
    angles = np.deg2rad([60., 126., 99.])
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    weights = np.array([3 / 8, 1 / 8, 1 / 2])
    sw = np.sqrt(weights)
    labels = np.array([1., 1., -1.])
    metadata = dict(source_sha256=hashlib.sha256(source).hexdigest(),
                    python=platform.python_version(), numpy=np.__version__,
                    scipy=scipy.__version__, machine=platform.machine(),
                    angles_degrees=[60, 126, 99], weights=weights.tolist(),
                    labels=labels.tolist(), nu=float(nu), tau=float(tau),
                    M0=float(m0), grids=[24, 32, 48], time_cap=200,
                    wall_cap_seconds=90, rhs_cap=30000)
    (out / 'metadata.json').write_text(json.dumps(metadata, indent=2))
    summaries = []

    def run(n, tighter=False):
        nodes, p2 = normal_rule(n)
        g1, g2 = np.meshgrid(nodes, nodes, indexing='ij')
        g = np.column_stack((g1.ravel(), g2.ravel()))
        p1 = np.outer(p2, p2).ravel()
        b1 = np.tanh(g[:, 0]) / np.sqrt(nu + eta)
        b2 = np.tanh(np.sqrt(nu) * nodes) / np.sqrt(tau + eta)
        count = len(g)
        cosine = inputs @ inputs.T
        calls = 0

        def fields(state, diagnostics=False):
            w = state[:2 * count].reshape(-1, 2)
            c = state[2 * count:-1]
            m = state[-1]
            h1 = np.tanh(w @ inputs.T)
            gate1 = 1 - h1 ** 2
            a = (p1 * b1) @ h1
            h2 = np.tanh(b2[:, None] * m * a)
            gate2 = 1 - h2 ** 2
            f = (p2 * c) @ h2
            r = f - labels
            d = (p2 * b2 * c) @ gate2
            dw = -2 * b1[:, None] * m * (gate1 * (weights * r * d)) @ inputs
            dc = -2 * h2 @ (weights * r)
            dm = -2 * (weights * r * d) @ a
            velocity = np.r_[dw.ravel(), dc, dm]
            if not diagnostics:
                return velocity, (weights * r) @ r
            lower_motion = dw @ inputs.T
            da = (p1 * b1) @ (gate1 * lower_motion)
            ds = dm * a + m * da
            dh = gate2 * b2[:, None] * ds
            dd = (p2 * b2 * dc) @ gate2
            dd += (p2 * b2 ** 2 * c) @ (-2 * h2 * gate2 * ds)
            df = (p2 * dc) @ h2 + (p2 * c) @ dh
            dg1 = -2 * h1 * gate1 * lower_motion
            lower_weight = p1 * b1 ** 2
            q = cosine * (gate1.T @ (lower_weight[:, None] * gate1))
            crossq = dg1.T @ (lower_weight[:, None] * gate1)
            dq = cosine * (crossq + crossq.T)
            gram = h2.T @ (p2[:, None] * h2)
            cross = dh.T @ (p2[:, None] * h2)
            dgram = cross + cross.T
            v = a * d
            dv = da * d + a * dd
            theta = gram + np.outer(v, v) + m ** 2 * np.outer(d, d) * q
            dtheta = dgram + np.outer(dv, v) + np.outer(v, dv)
            dtheta += 2 * m * dm * np.outer(d, d) * q
            dtheta += m ** 2 * (np.outer(dd, d) + np.outer(d, dd)) * q
            dtheta += m ** 2 * np.outer(d, d) * dq
            weighting = np.outer(sw, sw)
            gram, dgram = gram * weighting, dgram * weighting
            theta, dtheta = theta * weighting, dtheta * weighting
            residual, dr = sw * r, sw * df
            loss = residual @ residual
            speed2 = p1 @ np.sum(dw ** 2, axis=1) + p2 @ dc ** 2 + dm ** 2
            row = [loss]
            for metric, derivative in ((gram, dgram), (theta, dtheta)):
                correction = np.linalg.solve(metric, residual)
                potential = residual @ correction
                derivative_phi = 2 * dr @ correction - correction @ derivative @ correction
                row.extend([potential, derivative_phi, derivative_phi / potential,
                            np.linalg.cond(metric)])
            row.extend([2 * residual @ dr + speed2,
                        np.linalg.norm(dr + 2 * theta @ residual),
                        np.sqrt(p2 @ c ** 2), m])
            return velocity, np.array(row), (gram, dgram, theta, dtheta), speed2

        def rhs(t, state):
            nonlocal calls
            calls += 1
            if calls > 30000 or time.monotonic() - started > 85:
                raise RuntimeError('Precommitted resource cap reached')
            return fields(state)[0]

        def done(t, state):
            return fields(state)[1] - 1e-10

        done.terminal = True
        done.direction = -1
        initial = np.r_[g.ravel(), np.zeros(n), m0]
        times = np.r_[0., np.geomspace(1e-5, 200, 600)]
        suffix = f'{n}_tight' if tighter else str(n)
        rtol, atol = (2e-9, 2e-11) if tighter else (2e-8, 2e-10)
        try:
            solution = solve_ivp(rhs, (0, 200), initial, method='DOP853',
                                 rtol=rtol, atol=atol, t_eval=times, events=done)
            values = np.vstack([fields(state, True)[1] for state in solution.y.T])
            header = ('time,loss,read_potential,read_derivative,read_logslope,read_condition,'
                      'full_potential,full_derivative,full_logslope,full_condition,'
                      'energy_defect,residual_equation_defect,readout_norm,M')
            np.savetxt(out / f'grid_{suffix}.csv', np.column_stack((solution.t, values)),
                       delimiter=',', header=header, comments='')
            retained = int(np.argmin(np.abs(solution.t - 10)))
            state = solution.y[:, retained]
            vel, _, mats, speed2 = fields(state, True)
            step = 1e-5 / max(1., np.sqrt(speed2))
            plus = fields(state + step * vel, True)[2]
            minus = fields(state - step * vel, True)[2]
            errors = [float(np.linalg.norm((plus[k] - minus[k]) / (2 * step) - mats[k + 1]) /
                            max(np.linalg.norm(mats[k + 1]), 1e-8)) for k in (0, 2)]
            np.savez_compressed(out / f'grid_{suffix}_states.npz',
                                initial=initial, interior=state, final=solution.y[:, -1],
                                times=[0, solution.t[retained], solution.t[-1]])
            peaks = {}
            for name, slope_column, condition_column in (('read', 3, 4), ('full', 7, 8)):
                valid = (values[:, 0] > 1e-8) & (values[:, condition_column] < 1e10)
                indices = np.flatnonzero(valid)
                if len(indices):
                    index = indices[np.argmax(values[indices, slope_column])]
                    peaks[name] = dict(slope=float(values[index, slope_column]),
                                       time=float(solution.t[index]),
                                       loss=float(values[index, 0]))
                else:
                    peaks[name] = None
            result = dict(n=n, tight=tighter, success=solution.success,
                          message=solution.message, rhs_calls=calls,
                          rtol=rtol, atol=atol, final_time=float(solution.t[-1]),
                          final_loss=float(values[-1, 0]), peaks=peaks,
                          initial_read_identity=float(values[0, 2] + 4 * values[0, 0]),
                          initial_full_identity=float(values[0, 6] + 4 * values[0, 0]),
                          max_energy_defect=float(np.max(np.abs(values[:, 9]))),
                          max_residual_equation_defect=float(np.max(values[:, 10])),
                          metric_derivative_relative_errors=errors)
        except Exception as error:
            result = dict(n=n, tight=tighter, success=False, error=repr(error), rhs_calls=calls)
        summaries.append(result)
        (out / 'summary.json').write_text(json.dumps(summaries, indent=2))
        print(json.dumps(result), flush=True)
        return result

    for grid in (24, 32, 48):
        run(grid)
        if time.monotonic() - started > 85:
            break
    repeat = False
    if len(summaries) == 3 and all(row['success'] for row in summaries):
        for name in ('read', 'full'):
            a, b = summaries[1]['peaks'][name], summaries[2]['peaks'][name]
            if a and b and min(a['slope'], b['slope']) > 1e-4:
                close_slope = abs(a['slope'] - b['slope']) <= .2 * max(a['slope'], b['slope'])
                close_time = abs(a['time'] - b['time']) <= max(.02, .1 * max(a['time'], b['time']))
                repeat |= close_slope and close_time
    if repeat and time.monotonic() - started < 85:
        run(48, tighter=True)
    print(json.dumps(dict(total_seconds=time.monotonic() - started)), flush=True)


if __name__ == '__main__':
    main()
