"""Independent, no-training checks for this one broad-ridge probe."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/broad_ridge_canonical_probe_20260921/check"
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)


def load_file(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def maxerr(a, b):
    return float(np.max(np.abs(np.asarray(a) - np.asarray(b))))


def independent_dense(W, A, c, X, y):
    """Columns are raw Gaussian inputs; all derivatives are ordinary ones."""
    n, d = W.shape
    m = X.shape[1]
    h = np.tanh(W @ X / np.sqrt(d))
    s = np.tanh(A @ h)
    f = c @ s / n
    r = f - y
    delta2 = c[:, None] * (1 - s * s)
    delta1 = (A.T @ delta2) * (1 - h * h)
    gW = 2 * ((delta1 * r) @ X.T) / (m * n * np.sqrt(d))
    gA = 2 * ((delta2 * r) @ h.T) / (m * n)
    gc = 2 * (s @ r) / (m * n)
    return f, (gW, gA, gc), (-n * gW, -gA, -n * gc)


def independent_closure(W, M, c, B1, B2, X, y=None):
    """Factorized check, independently derived from the effective dense map."""
    n, d = W.shape
    m = X.shape[1]
    h = np.tanh(W @ X / np.sqrt(d))
    q = B1.T @ h / n
    s = np.tanh(B2 @ (M @ q))
    f = c @ s / n
    if y is None:
        return f
    r = f - y
    delta2 = c[:, None] * (1 - s * s)
    pulled = B2.T @ delta2
    delta1 = (B1 @ (M.T @ pulled) / n) * (1 - h * h)
    vW = -2 * ((delta1 * r) @ X.T) / (m * np.sqrt(d))
    vM = -2 * ((pulled * r) @ q.T) / (m * n)
    vc = -2 * (s @ r) / m
    return f, (vW, vM, vc)


def independent_basis(W, A, ridge):
    n = W.shape[0]
    H = np.tanh(W)
    U = np.tanh(A @ H)
    R = np.tanh(A.T @ U)
    bases, features, grams = [], [], []
    for F in (np.column_stack((np.ones(n), H, R)),
              np.column_stack((np.ones(n), U))):
        G = F.T @ F / n
        L = np.linalg.cholesky(G + ridge * np.eye(G.shape[0]))
        B = np.linalg.solve(L, F.T).T
        bases.append(B)
        features.append(F)
        grams.append((G, L))
    return bases, features, grams


def independent_target(d=64, K=768, seed=2026092101):
    rng = np.random.default_rng(seed)
    V = rng.standard_normal((d, K))
    V /= np.linalg.norm(V, axis=0)
    signs = rng.choice(np.array([-1.0, 1.0]), K)
    a = signs - V.T @ np.linalg.solve(V @ V.T, V @ signs)
    a *= np.sqrt(K) / np.linalg.norm(a)
    return V, a


def core_checks():
    finite = load_file(ROOT / "code/pde/finite_network.py", "finite_oracle")
    rng = np.random.default_rng(712903)
    n, d, m = 11, 3, 7
    W = rng.standard_normal((n, d))
    A = rng.standard_normal((n, n)) / np.sqrt(n)
    c = rng.standard_normal(n) / n
    X = rng.standard_normal((d, m))
    y = rng.standard_normal(m)
    f, grads, rhs = independent_dense(W, A, c, X, y)
    parameters = finite.Parameters((W, A), c)
    maintained_grad = finite.loss_gradients(parameters, X, y)
    maintained_rhs = finite.flow_velocity(parameters, X, y)
    metrics = {
        "dense_forward_maintained_max_abs": maxerr(f, finite.forward(parameters, X).output),
        "dense_gradient_maintained_max_abs": max(maxerr(a, b) for a, b in zip(
            grads, (*maintained_grad.weights, maintained_grad.readout))),
        "dense_rhs_maintained_max_abs": max(maxerr(a, b) for a, b in zip(
            rhs, (*maintained_rhs.weights, maintained_rhs.readout))),
    }
    wt, at, ct = (torch.tensor(p, requires_grad=True) for p in (W, A, c))
    xt, yt = torch.tensor(X), torch.tensor(y)
    ft = ct @ torch.tanh(at @ torch.tanh(wt @ xt / np.sqrt(d))) / n
    torch.mean((ft - yt) ** 2).backward()
    metrics["dense_gradient_autograd_max_abs"] = max(
        maxerr(g, t.grad.numpy()) for g, t in zip(grads, (wt, at, ct)))

    ridge = 1 / 4096
    (B1, B2), _, grams = independent_basis(W, A, ridge)
    M = B2.T @ A @ B1 / n
    effective = B2 @ M @ B1.T / n
    f2, dg, dr = independent_dense(W, effective, c, X, y)
    gM = B2.T @ dg[1] @ B1 / n
    f_factorized, r_factorized = independent_closure(W, M, c, B1, B2, X, y)
    metrics["closure_factorized_forward_max_abs"] = maxerr(f_factorized, f2)
    metrics["closure_factorized_rhs_max_abs"] = max(
        maxerr(a, b) for a, b in zip(r_factorized, (dr[0], -gM, dr[2])))
    wt, mt, ct = (torch.tensor(p, requires_grad=True) for p in (W, M, c))
    b1, b2 = torch.tensor(B1), torch.tensor(B2)
    ft = ct @ torch.tanh(b2 @ mt @ b1.T @ torch.tanh(wt @ xt / np.sqrt(d)) / n) / n
    torch.mean((ft - yt) ** 2).backward()
    metrics["closure_forward_autograd_max_abs"] = maxerr(f2, ft.detach().numpy())
    metrics["closure_gradient_autograd_max_abs"] = max(
        maxerr(g, t.grad.numpy()) for g, t in zip((dg[0], gM, dg[2]), (wt, mt, ct)))
    P1, P2 = B1 @ B1.T / n, B2 @ B2.T / n
    metrics["initial_effective_contraction_max_abs"] = maxerr(effective, P2 @ A @ P1)
    metrics["closure_rhs_contraction_max_abs"] = maxerr(
        B2 @ (-gM) @ B1.T / n, P2 @ dr[1] @ P1)
    gram_errors = []
    for B, (_, L) in zip((B1, B2), grams):
        inverse = np.linalg.solve(L, np.eye(L.shape[0]))
        gram_errors.append(maxerr(B.T @ B / n, np.eye(L.shape[0]) - ridge * inverse @ inverse.T))
    metrics["ridge_gram_identity_max_abs"] = max(gram_errors)
    metrics["ridge_operator_max_eigenvalue"] = max(float(np.linalg.eigvalsh(P)[-1]) for P in (P1, P2))

    # Independent central directional differences detect loss/normalization errors.
    finite_difference_errors = []
    for block, (theta, grad) in enumerate(zip((W, M, c), (dg[0], gM, dg[2]))):
        direction = rng.standard_normal(theta.shape)
        direction /= np.linalg.norm(direction)
        vals = []
        for sign in (-1, 1):
            ps = [W.copy(), M.copy(), c.copy()]
            ps[block] += sign * 1e-5 * direction
            prediction = independent_dense(ps[0], B2 @ ps[1] @ B1.T / n, ps[2], X, y)[0]
            vals.append(np.mean((prediction - y) ** 2))
        finite_difference_errors.append(abs((vals[1] - vals[0]) / 2e-5 - np.sum(grad * direction)))
    metrics["closure_gradient_finite_difference_max_abs"] = float(max(finite_difference_errors))
    eta = 0.017
    stepped = finite.gd_step(parameters, X, y, eta)
    metrics["simultaneous_gd_max_abs"] = max(maxerr(got, p + eta * v) for got, p, v in zip(
        (*stepped.weights, stepped.readout), (W, A, c), rhs))

    V, a = independent_target()
    metrics["target_direction_norm_max_abs"] = maxerr(np.linalg.norm(V, axis=0), 1)
    metrics["target_linear_cancellation_l2"] = float(np.linalg.norm(V @ a))
    metrics["target_coefficient_l2"] = float(np.linalg.norm(a))
    metrics["counts"] = {
        "closure_trainable": 1024 * 65 + 129 * 65,
        "closure_stored": 1024 * 65 + 129 * 65 + 1024 * (129 + 65),
        "dense244": 244 * (244 + 65),
        "dense492": 492 * (492 + 65),
        "dense1024": 1024 * (1024 + 65),
    }
    for name, value in metrics.items():
        if name.endswith("max_abs"):
            assert value < (1e-8 if "finite_difference" in name else 1e-11), (name, value)
    assert metrics["target_linear_cancellation_l2"] < 1e-10
    assert metrics["ridge_operator_max_eigenvalue"] <= 1 + 1e-12
    return metrics


def producer_checks():
    producer = load_file(Path(__file__).with_name("probe.py"), "study_producer_check")
    rng = np.random.default_rng(841771)
    n, d, m = 11, 3, 7
    W = rng.standard_normal((n, d))
    A = rng.standard_normal((n, n)) / np.sqrt(n)
    c = rng.standard_normal(n) / n
    X, y = rng.standard_normal((d, m)), rng.standard_normal(m)
    bases, _, _ = independent_basis(W, A, 1 / 4096)
    B1, B2 = bases
    metrics = {}
    for kind in ("dense", "closure"):
        middle = A if kind == "dense" else B2.T @ A @ B1 / n
        blocks = (W, middle, c)
        state = np.concatenate([a.ravel() for a in blocks])
        model = dict(n=n, d=d, kind=kind, shapes=tuple(a.shape for a in blocks), B1=B1, B2=B2)
        if kind == "dense":
            expected_f, _, expected_rhs = independent_dense(W, A, c, X, y)
        else:
            expected_f, expected_rhs = independent_closure(W, middle, c, B1, B2, X, y)
        metrics[f"{kind}_forward_max_abs"] = maxerr(producer.forward(state, model, X / np.sqrt(d)), expected_f)
        metrics[f"{kind}_rhs_max_abs"] = maxerr(producer.rhs(0, state, model, X / np.sqrt(d), y),
                                                np.concatenate([a.ravel() for a in expected_rhs]))
    assert max(metrics.values()) < 1e-11
    return metrics


def data_checks(path):
    with np.load(path) as archive:
        data = {key: archive[key] for key in archive.files}
    V, a = independent_target()
    metrics = {"V_reproduction_max_abs": maxerr(V, data["V"]),
               "a_reproduction_max_abs": maxerr(a, data["a"]),
               "linear_cancellation_l2": float(np.linalg.norm(data["V"] @ data["a"]))}
    def target(X):
        return a @ np.tanh(V.T @ X) / np.sqrt(a.size)
    Xcal = np.random.default_rng(2026092102).standard_normal((64, 32768))
    metrics["calibration_X_max_abs"] = maxerr(Xcal, data["X_calibration"])
    rawcal = np.concatenate([target(Xcal[:, j:j + 2048]) for j in range(0, 32768, 2048)])
    C = 1 / np.sqrt(np.mean(rawcal ** 2))
    metrics["calibration_C_max_abs"] = abs(float(data["C"]) - C)
    metrics["calibration_y_max_abs"] = maxerr(C * rawcal, data["y_calibration"])
    metrics["calibration_rms_max_abs"] = abs(float(data["calibration_rms"]) - 1 / C)
    for split, seed in (("train", 2026092103), ("passive", 2026092104)):
        X = np.random.default_rng(seed).standard_normal((64, 2048))
        metrics[f"{split}_X_max_abs"] = maxerr(X, data[f"X_{split}"])
        metrics[f"{split}_U_max_abs"] = maxerr(X / 8, data[f"U_{split}"])
        metrics[f"{split}_y_max_abs"] = maxerr(C * target(X), data[f"y_{split}"])
        metrics[f"{split}_label_mean"] = float(np.mean(data[f"y_{split}"]))
        metrics[f"{split}_label_rms"] = float(np.sqrt(np.mean(data[f"y_{split}"] ** 2)))
    for key, value in metrics.items():
        if key.endswith("max_abs"):
            assert value < 1e-10, (key, value)
    assert metrics["linear_cancellation_l2"] < 1e-10
    metrics["sha256"] = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    return data, metrics


def model_source_checks():
    producer = load_file(Path(__file__).with_name("probe.py"), "study_producer_source_check")
    metrics = {}
    for name in ("closure1024", "width244", "width492", "width1024"):
        model = producer.build_model(name)
        n, d = model["n"], model["d"]
        rng = np.random.default_rng(20260921)
        W = rng.standard_normal((n, d))
        A = rng.standard_normal((n, n)) / np.sqrt(n)
        c = rng.standard_normal(n) / n
        errors = [maxerr(value, model[key]) for value, key in ((W, "W0"), (A, "A0"), (c, "c0"))]
        middle = A
        if model["kind"] == "closure":
            (B1, B2), Fs, grams = independent_basis(W, A, 1 / 4096)
            middle = B2.T @ A @ B1 / n
            errors.extend([maxerr(B1, model["B1"]), maxerr(B2, model["B2"]), maxerr(middle, model["M0"])])
            errors.extend(maxerr(F, model[f"F{i}"]) for i, F in enumerate(Fs, 1))
            errors.extend(maxerr(L, model[f"L{i}"]) for i, (_, L) in enumerate(grams, 1))
        errors.append(maxerr(np.concatenate([value.ravel() for value in (W, middle, c)]), model["initial_state"]))
        metrics[name] = {"reproduction_max_abs": max(errors), "state_scalars": model["initial_state"].size}
        assert max(errors) < 1e-10, (name, max(errors))
    return metrics


def artifact_checks(run_path, data):
    run_path = Path(run_path)
    with np.load(run_path / "source.npz") as archive:
        source = {key: archive[key] for key in archive.files}
    result = json.loads((run_path / "result.json").read_text())
    W0, A0, c0 = (source[k] for k in ("W0", "A0", "c0"))
    n, d = W0.shape
    closure = "B1" in source
    metrics = {"name": run_path.name, "n": n, "closure": closure}
    rng = np.random.default_rng(20260921)
    regenerated = (rng.standard_normal((n, d)), rng.standard_normal((n, n)) / np.sqrt(n),
                   rng.standard_normal(n) / n)
    metrics["canonical_source_max_abs"] = max(maxerr(a, b) for a, b in zip((W0, A0, c0), regenerated))
    if closure:
        (B1, B2), Fs, grams = independent_basis(W0, A0, 1 / 4096)
        M0 = B2.T @ A0 @ B1 / n
        metrics["basis_max_abs"] = max(maxerr(B1, source["B1"]), maxerr(B2, source["B2"]))
        metrics["feature_max_abs"] = max(maxerr(F, source[f"F{i}"]) for i, F in enumerate(Fs, 1))
        metrics["cholesky_max_abs"] = max(maxerr(L, source[f"L{i}"]) for i, (_, L) in enumerate(grams, 1))
        metrics["M0_max_abs"] = maxerr(M0, source["M0"])
        middle0 = source["M0"]
        B1, B2 = source["B1"], source["B2"]
    else:
        middle0 = A0
    initial = np.concatenate([v.ravel() for v in (W0, middle0, c0)])
    metrics["initial_state_max_abs"] = max(maxerr(initial, source[k]) for k in ("state0", "initial_state"))
    metrics["trainable_scalars"] = initial.size
    metrics["stored_model_scalars"] = initial.size + (B1.size + B2.size if closure else 0)

    def unpack(state):
        nw, na = W0.size, middle0.size
        assert state.size == nw + na + c0.size
        return state[:nw].reshape(W0.shape), state[nw:nw + na].reshape(middle0.shape), state[nw + na:]

    def evaluate(state, split, velocity=False):
        W, middle, c = unpack(state)
        X, y = data[f"X_{split}"], data[f"y_{split}"]
        if closure:
            return independent_closure(W, middle, c, B1, B2, X, y if velocity else None)
        if velocity:
            f, _, rhs = independent_dense(W, middle, c, X, y)
            return f, rhs
        return c @ np.tanh(middle @ np.tanh(W @ X / np.sqrt(d))) / n

    metric_errors = []
    def check_reported(state, row, losses):
        blocks = unpack(state)
        names = ("W", "M" if closure else "A", "c")
        for name, block, old in zip(names, blocks, (W0, middle0, c0)):
            metric_errors.extend((abs(float(np.sqrt(np.mean((block - old) ** 2))) - row["block_rms_motion"][name]),
                abs(float(np.linalg.norm(block - old) / np.linalg.norm(old)) - row["block_relative_frobenius_motion"][name])))
        norms, oldnorms = np.linalg.norm(blocks[0], axis=1), np.linalg.norm(W0, axis=1)
        expected_norms = dict(median=np.median(norms), maximum=norms.max(),
            median_ratio_to_initial=np.median(norms / oldnorms), maximum_ratio_to_initial=np.max(norms / oldnorms),
            median_statistic_ratio=np.median(norms) / np.median(oldnorms), maximum_statistic_ratio=norms.max() / oldnorms.max())
        metric_errors.extend(abs(float(v) - row["W_row_norms"][k]) for k, v in expected_norms.items())
        metric_errors.extend(abs(value - row[f"mse_{split}"]) for split, value in losses.items())

    errors_f, errors_loss = [], []
    with np.load(run_path / "checkpoints.npz") as checkpoints:
        times, states = checkpoints["times"], checkpoints["states"]
        assert len(times) == len(states) == len(result["checkpoints"])
        for i, (time, state, row) in enumerate(zip(times, states, result["checkpoints"])):
            assert float(time) == row["t"]
            losses = {}
            for split in ("train", "passive"):
                prediction = evaluate(state, split)
                errors_f.append(maxerr(prediction, checkpoints[f"{split}_prediction"][i]))
                losses[split] = float(np.mean((prediction - data[f"y_{split}"]) ** 2))
                errors_loss.append(abs(losses[split] - checkpoints[f"{split}_loss"][i]))
            check_reported(state, row, losses)
        metrics["checkpoints_checked"] = len(times)
        if len(times):
            assert times[0] == 0 and maxerr(states[0], initial) < 1e-12
    with np.load(run_path / "final.npz") as final:
        assert float(final["time"]) == result["final"]["t"]
        losses = {}
        for split in ("train", "passive"):
            prediction = evaluate(final["state"], split)
            errors_f.append(maxerr(prediction, final[f"{split}_prediction"]))
            losses[split] = float(np.mean((prediction - data[f"y_{split}"]) ** 2))
        check_reported(final["state"], result["final"], losses)
        _, rhs = evaluate(final["state"], "train", True)
        rhs = np.concatenate([v.ravel() for v in rhs])
        metrics["final_rhs_max_abs"] = maxerr(rhs, final["rhs"])
        metrics["final_rhs_relative_l2"] = float(np.linalg.norm(rhs - final["rhs"]) / max(np.linalg.norm(rhs), 1e-300))
        metrics["final_time"] = float(final["time"])
    # Initial physical RHS is checked directly against the producer as well.
    producer = load_file(Path(__file__).with_name("probe.py"), "study_producer_artifact_check")
    model = dict(n=n, d=d, kind="closure" if closure else "dense", shapes=(W0.shape, middle0.shape, c0.shape))
    if closure:
        model.update(B1=B1, B2=B2)
    _, rhs = evaluate(initial, "train", True)
    metrics["initial_rhs_producer_max_abs"] = maxerr(np.concatenate([v.ravel() for v in rhs]),
        producer.rhs(0, initial, model, data["U_train"], data["y_train"]))
    metrics["saved_prediction_max_abs"] = max(errors_f, default=0)
    metrics["saved_loss_max_abs"] = max(errors_loss, default=0)
    metrics["reported_metric_max_abs"] = max(metric_errors, default=0)
    accepted = np.atleast_2d(np.loadtxt(run_path / "accepted.csv", delimiter=",", skiprows=1))
    assert np.isfinite(accepted).all() and accepted[-1, 0] == metrics["final_time"]
    assert np.all(np.diff(accepted[:, 0]) > 0)
    increase = float(max(0, np.max(np.diff(accepted[:, 1]), initial=0)))
    metrics["maximum_accepted_loss_increase"] = increase
    metrics["accepted_loss_summary_max_abs"] = abs(increase - result["maximum_accepted_loss_increase"])
    for key, value in metrics.items():
        if key.endswith("max_abs"):
            assert value < 1e-9, (run_path.name, key, value)
    return metrics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--producer", action="store_true")
    parser.add_argument("--data", type=Path)
    parser.add_argument("--runs", type=Path, nargs="*", default=[])
    parser.add_argument("--output", type=Path, default=OUT,
                        help="fresh output directory; existing directories are never overwritten")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = {"core": core_checks()}
    if args.producer:
        result["producer"] = producer_checks()
    if args.data:
        data, result["data"] = data_checks(args.data)
        result["model_sources"] = model_source_checks()
        result["runs"] = [artifact_checks(path, data) for path in args.runs]
    elif args.runs:
        parser.error("--runs requires --data")
    (args.output / "checks.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
