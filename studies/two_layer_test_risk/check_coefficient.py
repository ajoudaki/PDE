#!/usr/bin/env python3
"""Fixed-model diagnostic Gaussian quadrature; no certified integration error.

Only preregistered (Hermite order, circle-angle count) pairs are accepted.
All expectations use float64 normalized tensor Gauss--Hermite rules.  The
first Gaussian has two coordinates; upper training coordinates have three,
and one independent conditional Gaussian supplies a passive input.  Matrix
reuse is evaluated by exact covariance/response formulas before quadrature.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time
import traceback

# Keep numerical libraries within the preregistered one-thread budget.
for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tensor_rule(order, dimension):
    nodes, weights = np.polynomial.hermite.hermgauss(order)
    nodes = np.sqrt(2.0) * nodes
    weights = weights / np.sqrt(np.pi)
    mesh = np.meshgrid(*([nodes] * dimension), indexing="ij")
    points = np.stack([v.ravel() for v in mesh], axis=1)
    wm = np.meshgrid(*([weights] * dimension), indexing="ij")
    mass = np.prod(np.stack(wm, axis=0), axis=0).ravel()
    return points, mass


def gram(values, weights, other=None):
    return values.T @ (weights[:, None] * (values if other is None else other))


def upper_moments(upper, weights, p):
    H = np.tanh(upper)
    d = 1.0 - H * H
    dd = -2.0 * H * d
    S = H @ p
    U = S[:, None] * d
    V = gram(U, weights)
    ddgram = gram(d, weights)
    # coeff_U[j,i] is E partial_{Y_j} U_i, with named coordinates held fixed.
    coeff_U = p[:, None] * ddgram + np.diag((weights * S) @ dd)
    return H, d, dd, S, U, V, ddgram, coeff_U


def prepare(h, e, first_weights, G, Q, upper, upper_weights, p):
    H, d, dd, S, U, V, ddgram, coeff_U = upper_moments(upper, upper_weights, p)
    mu_U = h @ coeff_U
    ee = gram(e, first_weights)
    D = ee * V + gram(e * mu_U, first_weights)
    F = (Q * V + G * D) @ p
    A1 = float(p @ (G * D) @ p)
    A2 = float(p @ (Q * V) @ p)
    return dict(h=h, e=e, first_weights=first_weights, G=G, Q=Q,
                H=H, d=d, dd=dd, S=S, U=U, V=V, ddgram=ddgram,
                upper_weights=upper_weights, mu_U=mu_U, ee=ee, D=D,
                p=p, F=F, A1=A1, A2=A2)


def passive_coefficient(state, x):
    h, e, fw, G, Q = (state[k] for k in ("h", "e", "first_weights", "G", "Q"))
    H, d, dd, S, uw = (state[k] for k in ("H", "d", "dd", "S", "upper_weights"))
    p = state["p"]
    active = np.flatnonzero(p)
    da = d[:, active]
    C = gram(da, uw * H[:, x] * S)
    # mu_Fa for F_a=H_x d_a retains both partials, including when a=x.
    mu_F = (h[:, x, None] * state["ddgram"][x, active][None, :]
            + h[:, active] * ((uw * H[:, x]) @ dd[:, active])[None, :])
    response = gram(e[:, active] * mu_F, fw,
                    e[:, active] * state["mu_U"][:, active])
    sub = np.ix_(active, active)
    Bmatrix = Q[sub] * C + G[sub] * (state["ee"][sub] * C + response)
    pa = p[active]
    B = float(pa @ Bmatrix @ pa)
    F = float(state["F"][x])
    J = 4.0 * F + (4.0 / 3.0) * B
    a = float(2.0 * np.dot(uw, S * H[:, x]))
    return dict(a=a, J=J, F=F, B=B)


def symmetry_error(values):
    n = len(values)
    v = np.asarray(values)
    return dict(reflection=float(np.max(np.abs(v - v[(-np.arange(n)) % n]))),
                antipodal=float(np.max(np.abs(v + np.roll(v, n // 2)))))


def compute(order, angles):
    train_angles = np.array([0.0, np.pi / 5.0, -np.pi / 5.0])
    unit_train = np.stack((np.cos(train_angles), np.sin(train_angles)), axis=1)
    y = np.array([1.0, (1.0 - np.sqrt(5.0)) / 4.0,
                  (1.0 - np.sqrt(5.0)) / 4.0])
    p3 = y / 3.0
    first_points, fw = tensor_rule(order, 2)
    ztrain = first_points @ unit_train.T
    htrain = np.tanh(ztrain)
    etrain = 1.0 - htrain * htrain
    Qtrain = gram(htrain, fw)
    Gtrain = unit_train @ unit_train.T
    # Symmetry-adapted square root.  Swapping the two symmetric training
    # examples is the sign flip of the third independent Gaussian.  This
    # avoids mistaking orientation error of finite GH rules for broken parity.
    q0 = Qtrain[0, 0]
    q1 = 0.5 * (Qtrain[0, 1] + Qtrain[0, 2])
    qd = 0.5 * (Qtrain[1, 1] + Qtrain[2, 2])
    qc = Qtrain[1, 2]
    b = q1 / np.sqrt(q0)
    c = np.sqrt(0.5 * (qd + qc) - b * b)
    d = np.sqrt(0.5 * (qd - qc))
    L = np.array([[np.sqrt(q0), 0.0, 0.0], [b, c, d], [b, c, -d]])
    root_error = float(np.max(np.abs(L @ L.T - Qtrain)))
    if root_error > 1e-13:
        raise ArithmeticError(f"Training covariance square-root error {root_error}")
    nodes3, uw3 = tensor_rule(order, 3)
    upper3 = nodes3 @ L.T
    training = prepare(htrain, etrain, fw, Gtrain, Qtrain, upper3, uw3, p3)
    train_coeff = [passive_coefficient(training, a) for a in range(3)]
    Jtrain = np.array([r["J"] for r in train_coeff])
    atrain = np.array([r["a"] for r in train_coeff])
    ES2 = float(np.dot(uw3, training["S"] ** 2))
    expected_pJ = (16.0 / 3.0) * (training["A1"] + training["A2"])
    pJ = float(np.dot(p3, Jtrain))
    identity_error = abs(pJ - expected_pJ) / max(1.0, abs(pJ), abs(expected_pJ))
    pa_error = abs(float(np.dot(p3, atrain)) - 2.0 * ES2)
    if identity_error > 1e-9 or pa_error > 1e-9:
        raise ArithmeticError(f"Training contraction gate failed: {identity_error}, {pa_error}")
    beta = pJ / (2.0 * ES2)
    print(json.dumps(dict(phase="training", order=order, ES2=ES2,
                          A1=training["A1"], A2=training["A2"], pJ=pJ,
                          expected_pJ=expected_pJ, identity_error=identity_error,
                          beta=beta)), flush=True)

    nodes4, uw4 = tensor_rule(order, 4)
    upper_base = nodes4[:, :3] @ L.T
    p4 = np.r_[p3, 0.0]
    rows = []
    min_cov_eig = np.inf
    max_cov_error = 0.0
    min_cond_var = np.inf
    for k in range(angles):
        alpha = 2.0 * np.pi * k / angles
        u = np.array([np.cos(alpha), np.sin(alpha)])
        unit = np.vstack((unit_train, u))
        h = np.column_stack((htrain, np.tanh(first_points @ u)))
        e = 1.0 - h * h
        Q = gram(h, fw)
        eig = np.linalg.eigvalsh(Q)
        min_cov_eig = min(min_cov_eig, float(eig[0]))
        tol = 1e-12 * max(1.0, float(eig[-1]))
        if eig[0] < -tol:
            raise ArithmeticError(f"Non-PSD covariance at angle {alpha}: {eig}")
        coef = np.linalg.solve(L, Q[:3, 3])
        conditional_variance = float(Q[3, 3] - np.dot(coef, coef))
        min_cond_var = min(min_cond_var, conditional_variance)
        if conditional_variance < -tol:
            raise ArithmeticError(f"Negative conditional variance {conditional_variance}")
        # Clip only roundoff-sized negative residuals at duplicate/antipodal inputs.
        sd = np.sqrt(max(0.0, conditional_variance))
        upper = np.column_stack((upper_base, nodes4[:, :3] @ coef + sd * nodes4[:, 3]))
        reconstructed_Q = np.empty((4, 4))
        reconstructed_Q[:3, :3] = L @ L.T
        reconstructed_Q[:3, 3] = L @ coef
        reconstructed_Q[3, :3] = reconstructed_Q[:3, 3]
        reconstructed_Q[3, 3] = np.dot(coef, coef) + sd * sd
        max_cov_error = max(max_cov_error, float(np.max(np.abs(Q - reconstructed_Q))))
        state = prepare(h, e, fw, unit @ unit.T, Q, upper, uw4, p4)
        coeff = passive_coefficient(state, 3)
        coeff.update(alpha=float(alpha), teacher=float(np.cos(3.0 * alpha)),
                     matched_J=coeff["J"] - beta * coeff["a"],
                     min_cov_eigenvalue=float(eig[0]),
                     conditional_variance=conditional_variance)
        rows.append(coeff)
        if k % 16 == 0:
            print(json.dumps(dict(phase="circle", completed=k + 1, total=angles)), flush=True)

    a = np.array([r["a"] for r in rows])
    J = np.array([r["J"] for r in rows])
    matched = J - beta * a
    teacher = np.array([r["teacher"] for r in rows])
    CJ = float(2.0 * np.mean(teacher * J))
    Cclock = float(2.0 * beta * np.mean(teacher * a))
    C = float(2.0 * np.mean(teacher * matched))
    symmetry = dict(a=symmetry_error(a), J=symmetry_error(J),
                    matched_J=symmetry_error(matched))
    result = dict(order=order, angles=angles, coefficient=C,
                  raw_risk_coefficient=CJ, clock_subtraction=Cclock,
                  beta=beta, ES2=ES2, A1=training["A1"], A2=training["A2"],
                  pJ=pJ, expected_pJ=expected_pJ, training_identity_error=identity_error,
                  training_initial_speed_identity_error=pa_error,
                  training_covariance=Qtrain.tolist(),
                  input_gram_eigenvalues=np.linalg.eigvalsh(Gtrain).tolist(),
                  activation_gram_eigenvalues=np.linalg.eigvalsh(Qtrain).tolist(),
                  upper_min_cov_eigenvalue=min_cov_eig,
                  min_conditional_variance=min_cond_var,
                  max_covariance_reconstruction_error=max_cov_error,
                  training_root_error=root_error, symmetry_errors=symmetry,
                  training_coefficients=train_coeff,
                  angles_rows=rows,
                  numerical_claim="diagnostic only; no certified integration error")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, required=True)
    parser.add_argument("--angles", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if (args.order, args.angles) not in ((12, 64), (20, 128), (28, 128)):
        parser.error("resolution is outside the preregistered set")
    args.output.mkdir(parents=True, exist_ok=False)
    resource.setrlimit(resource.RLIMIT_CPU, (300, 305))
    signal.signal(signal.SIGXCPU, lambda signum, frame: (_ for _ in ()).throw(
        TimeoutError("Five CPU minute per-run limit reached")))
    root = Path(__file__).resolve().parents[2]
    used = [Path(__file__).resolve(), root / "AGENTS.md", root / "RESEARCH_WORKFLOW.md",
            root / "studies/two_layer_test_risk/README.md", root / "docs/NOTATION.md",
            root / "docs/global_nonlinear.md"]
    meta = dict(status="running", command=[sys.executable, *sys.argv], cwd=str(Path.cwd()),
                source_hashes={str(p.relative_to(root)): sha256(p) for p in used},
                git_head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
                environment=dict(python=sys.version, numpy=np.__version__, platform=platform.platform(),
                                 machine=platform.machine(), processor=platform.processor(),
                                 precision="float64", seed="none; deterministic quadrature",
                                 threads={k: os.environ[k] for k in os.environ if k.endswith("NUM_THREADS")}),
                configuration=dict(order=args.order, angles=args.angles, cpu_limit_seconds=300),
                claim="numerical diagnostic only")
    (args.output / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
    start_wall, start_cpu = time.monotonic(), time.process_time()
    exit_status = 0
    try:
        result = compute(args.order, args.angles)
        result_path = args.output / "result.json"
        result_path.write_text(json.dumps(result, indent=2) + "\n")
        meta.update(status="completed", result_sha256=sha256(result_path))
        print(json.dumps({k: v for k, v in result.items() if k != "angles_rows"}, indent=2), flush=True)
    except Exception:
        exit_status = 1
        meta.update(status="failed", error=traceback.format_exc())
        traceback.print_exc()
    finally:
        meta.update(exit_status=exit_status, elapsed_seconds=time.monotonic() - start_wall,
                    cpu_seconds=time.process_time() - start_cpu,
                    peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        (args.output / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
        print(json.dumps(meta), flush=True)
    return exit_status


if __name__ == "__main__":
    raise SystemExit(main())
