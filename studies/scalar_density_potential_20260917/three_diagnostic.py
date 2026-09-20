"""Bounded diagnostic specified in three_diagnostic_plan.md; not a proof."""
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


def gaussian(n):
    x, p = roots_hermitenorm(n)
    return x, p / np.sqrt(2 * np.pi)


def constants(n):
    x, p = gaussian(n)
    nu = p @ np.tanh(x) ** 2
    tau = p @ np.tanh(np.sqrt(nu) * x) ** 2
    return float(nu), float(tau)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).read_bytes()
    (out / 'source.py').write_bytes(source)
    started = time.monotonic()
    nu, tau = constants(128)
    eta = 1 / 4096
    initial_m = nu * (1 - tau) / np.sqrt((nu + eta) * (tau + eta))
    inputs = np.array([[0.5, np.sqrt(0.75)], [0.5, -np.sqrt(0.75)], [-1., 0.]])
    labels = np.array([1., 1., -1.])
    weights = np.array([0.25, 0.25, 0.5])
    metadata = dict(source_sha256=hashlib.sha256(source).hexdigest(),
                    numpy=np.__version__, scipy=scipy.__version__,
                    python=platform.python_version(), machine=platform.machine(),
                    constants128=[nu, tau], constants192=constants(192),
                    M0=initial_m, input_normalized=inputs.tolist(),
                    labels=labels.tolist(), weights=weights.tolist(),
                    rtol=2e-8, atol=2e-10, rhs_cap=30000,
                    time_cap=1000, wall_cap_seconds=90, grids=[16, 24, 32])
    (out / 'metadata.json').write_text(json.dumps(metadata, indent=2))
    summaries = []
    for n in metadata['grids']:
        nodes, p2 = gaussian(n)
        g1, g2 = np.meshgrid(nodes, nodes, indexing='ij')
        g = np.column_stack((g1.ravel(), g2.ravel()))
        p1 = np.outer(p2, p2).ravel()
        b1 = np.tanh(g[:, 0]) / np.sqrt(nu + eta)
        b2 = np.tanh(np.sqrt(nu) * nodes) / np.sqrt(tau + eta)
        lower_count = len(g)
        evaluations = 0

        def fields(state):
            w = state[:2 * lower_count].reshape(-1, 2)
            c = state[2 * lower_count:-1]
            m = state[-1]
            h1 = np.tanh(w @ inputs.T)
            a = (p1 * b1) @ h1
            h2 = np.tanh(b2[:, None] * m * a)
            f = (p2 * c) @ h2
            r = f - labels
            d = (p2 * b2 * c) @ (1 - h2 ** 2)
            dw = -2 * b1[:, None] * m * ((1 - h1 ** 2) * (weights * r * d)) @ inputs
            dc = -2 * h2 @ (weights * r)
            dm = -2 * (weights * r * d) @ a
            velocity = np.concatenate((dw.ravel(), dc, [dm]))
            da = (p1 * b1) @ ((1 - h1 ** 2) * (dw @ inputs.T))
            dh2 = (1 - h2 ** 2) * b2[:, None] * (dm * a + m * da)
            df = (p2 * dc) @ h2 + (p2 * c) @ dh2
            loss = (weights * r) @ r
            speed2 = p1 @ np.sum(dw ** 2, axis=1) + p2 @ dc ** 2 + dm ** 2
            lossdot = 2 * (weights * r) @ df
            folded_h = np.column_stack((-h2[:, 2], h2[:, 0]))
            folded_dh = np.column_stack((-dh2[:, 2], dh2[:, 0]))
            folded_r = np.array([-f[2] - 1, f[0] - 1])
            folded_dr = np.array([-df[2], df[0]])
            gram = folded_h.T @ (p2[:, None] * folded_h)
            cross = folded_dh.T @ (p2[:, None] * folded_h)
            gramdot = cross + cross.T
            correction = np.linalg.solve(gram, folded_r)
            potential = folded_r @ correction
            potentialdot = 2 * folded_dr @ correction - correction @ gramdot @ correction
            diag = np.array([loss, potential, potentialdot, potentialdot / potential,
                             np.linalg.cond(gram), np.sqrt(p2 @ c ** 2), m,
                             -folded_r[0], -folded_r[1], -a[2], a[0],
                             lossdot, speed2, lossdot + speed2,
                             np.max(np.abs(f[0] - f[1]))])
            return velocity, diag

        def rhs(t, state):
            nonlocal evaluations
            evaluations += 1
            if evaluations > 30000 or time.monotonic() - started > 85:
                raise RuntimeError('Precommitted resource cap reached')
            return fields(state)[0]

        def done(t, state):
            return fields(state)[1][0] - 1e-10

        done.terminal = True
        done.direction = -1
        state0 = np.concatenate((g.ravel(), np.zeros(n), [initial_m]))
        times = np.r_[0., np.geomspace(1e-4, 1000., 500)]
        try:
            solution = solve_ivp(rhs, (0., 1000.), state0, method='DOP853',
                                 rtol=2e-8, atol=2e-10, t_eval=times, events=done)
            diagnostics = np.vstack([fields(q)[1] for q in solution.y.T])
            header = 'time,loss,potential,potentialdot,logslope,gram_condition,readout_norm,M,error_axis,error_pair,a_axis,a_pair,lossdot,speed2,energy_defect,symmetry_defect'
            np.savetxt(out / f'grid_{n}.csv', np.column_stack((solution.t, diagnostics)),
                       delimiter=',', header=header, comments='')
            np.savez_compressed(out / f'grid_{n}_endpoint.npz', state=solution.y[:, -1],
                                time=solution.t[-1], p1=p1, p2=p2, b1=b1, b2=b2)
            valid = (diagnostics[:, 0] > 1e-8) & (diagnostics[:, 4] < 1e10)
            candidates = np.flatnonzero(valid)
            peak = candidates[np.argmax(diagnostics[valid, 3])]
            row = dict(n=n, success=solution.success, message=solution.message,
                       rhs_evaluations=evaluations, final_sample_time=float(solution.t[-1]),
                       final_sample_loss=float(diagnostics[-1, 0]),
                       initial_slope_defect=float(diagnostics[0, 2] + 4 * diagnostics[0, 0]),
                       max_energy_defect=float(np.max(np.abs(diagnostics[:, 13]))),
                       max_symmetry_defect=float(np.max(np.abs(diagnostics[:, 14]))),
                       max_valid_logslope=float(diagnostics[peak, 3]),
                       peak_time=float(solution.t[peak]), peak_loss=float(diagnostics[peak, 0]),
                       final_readout_norm=float(diagnostics[-1, 5]),
                       final_M=float(diagnostics[-1, 6]))
        except Exception as exc:
            row = dict(n=n, success=False, error=repr(exc), rhs_evaluations=evaluations)
        summaries.append(row)
        (out / 'summary.json').write_text(json.dumps(summaries, indent=2))
        print(json.dumps(row), flush=True)
        if time.monotonic() - started > 85:
            break
    print(json.dumps(dict(total_seconds=time.monotonic() - started)), flush=True)


if __name__ == '__main__':
    main()
