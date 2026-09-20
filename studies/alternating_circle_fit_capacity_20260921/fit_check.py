#!/usr/bin/env python3
"""Independent NumPy fit replay and finite deterministic representation controls.

The forward equations and acceptance rule were frozen before producer inspection.
This is not a training script.  Generated controls are deliberately structured
weights, unrelated to any Gaussian initialization or optimization trajectory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np


THRESHOLD = 1e-3


def circle(m):
    if m < 2 or m % 2:
        raise ValueError("m must be even and at least two")
    theta = 2 * np.pi * np.arange(m, dtype=np.float64) / m
    x = np.column_stack((np.cos(theta), np.sin(theta)))
    return x, x / np.sqrt(2), (-1.0) ** np.arange(m)


def array(z, name, dtype=np.float64):
    z = np.asarray(z)
    if z.dtype.kind not in "fiu" or not np.isfinite(z).all():
        raise ValueError(f"{name} must be finite real numeric data")
    return np.asarray(z, dtype=dtype)


def dense_forward(W, A, c, U, *, dtype=np.float64):
    W, A, c, U = (array(z, name, dtype) for z, name in
                   ((W, "W"), (A, "A"), (c, "c"), (U, "U")))
    n = len(c)
    if W.shape != (n, 2) or A.shape != (n, n) or U.ndim != 2 or U.shape[1] != 2:
        raise ValueError("dense shape mismatch")
    return (c / n) @ np.tanh(A @ np.tanh(W @ U.T))


def closure_forward(W, M, c, B1, B2, U, *, dtype=np.float64):
    W, M, c, B1, B2, U = (array(z, name, dtype) for z, name in
        ((W, "W"), (M, "M"), (c, "c"), (B1, "B1"), (B2, "B2"), (U, "U")))
    n = len(c)
    if (W.shape != (n, 2) or B1.shape[0] != n or B2.shape[0] != n
            or M.shape != (B2.shape[1], B1.shape[1])
            or U.ndim != 2 or U.shape[1] != 2):
        raise ValueError("closure shape mismatch")
    h1 = np.tanh(W @ U.T)
    return (c / n) @ np.tanh(B2 @ (M @ ((B1.T @ h1) / n)))


def metrics(prediction, labels):
    prediction, labels = array(prediction, "prediction"), array(labels, "labels")
    if prediction.shape != labels.shape or labels.ndim != 1 or not len(labels):
        raise ValueError("prediction/label shape mismatch")
    mse = float(np.mean((prediction - labels) ** 2))
    errors = int(np.count_nonzero(prediction * labels <= 0))
    return dict(mse=mse, sign_errors=errors, minimum_signed_margin=float(np.min(prediction * labels)),
                maximum_absolute_error=float(np.max(np.abs(prediction - labels))),
                fit=bool(mse <= THRESHOLD and errors == 0))


def norms(z):
    z = array(z, "norm argument")
    result = dict(euclidean_or_frobenius=float(np.linalg.norm(z)),
                  maximum_absolute_entry=float(np.max(np.abs(z))))
    if z.ndim == 2:
        result["operator_2"] = float(np.linalg.norm(z, ord=2))
        result["operator_infinity"] = float(np.linalg.norm(z, ord=np.inf))
    return result


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")


def finite_witness(m, n):
    q = m // 2
    if m % 4 != 2 or n < q:
        raise ValueError("this witness requires m=4k+2 and n>=m/2")
    x, U, labels = circle(m)
    tau = np.pi * (np.arange(q, dtype=np.float64) - 0.5) / q
    scale = 8 * np.sqrt(2) / np.sin(np.pi / (2 * q))
    W, A, v = np.zeros((n, 2)), np.zeros((n, n)), np.zeros(n)
    W[:q] = scale * np.column_stack((-np.sin(tau), np.cos(tau)))
    A[np.arange(q), np.arange(q)] = 1
    hidden = np.tanh(A @ np.tanh(W @ U.T))
    v[:q], _, rank, singular_values = np.linalg.lstsq(hidden[:q].T, labels, rcond=None)
    c = n * v
    prediction = dense_forward(W, A, c, U)
    sign_basis = np.where(np.arange(q)[:, None] >= np.arange(q)[None, :], 1.0, -1.0)
    ideal = np.tanh(1.0) * sign_basis
    perturbation = hidden[:q, :q].T - ideal
    report = dict(m=m, n=n, active_neurons=q, dtype="float64", device="cpu",
        control_kind="explicit representation witness, not Gaussian training",
        first_weight_row_norm=scale, minimum_first_preactivation_magnitude=float(np.min(np.abs(W[:q] @ U.T))),
        least_squares_rank=int(rank), singular_value_minimum=float(singular_values[-1]),
        singular_value_maximum=float(singular_values[0]),
        half_design_condition_2=float(np.linalg.cond(hidden[:q, :q].T)),
        perturbation_operator_infinity=float(np.linalg.norm(perturbation, ord=np.inf)),
        analytic_invertibility_bound=2 * q * math.exp(-16) / math.tanh(1),
        norms={name: norms(z) for name, z in (("W", W), ("A", A), ("c", c), ("v", v))},
        antipodal_prediction_error=float(np.max(np.abs(prediction[:q] + prediction[q:]))),
        **metrics(prediction, labels))
    if not report["fit"] or rank != q or report["analytic_invertibility_bound"] >= 1:
        raise AssertionError("finite witness failed")
    arrays = dict(x=x, U=U, labels=labels, W=W, A=A, c=c, v=v,
                  prediction=prediction, tau=tau, record=np.asarray(json.dumps(report)))
    return arrays, report


def gradient_preflight():
    """No parameter updates: compare autograd and maintained Euclidean gradients."""
    import torch
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "code"))
    from pde.finite_network import Parameters, forward, loss_gradients
    rng = np.random.default_rng(90731)
    n, m = 7, 10
    x, U, y = circle(m)
    W = rng.standard_normal((n, 2)) * 0.4
    A = rng.standard_normal((n, n)) / np.sqrt(n)
    v = rng.standard_normal(n) * 0.2
    tw, ta, tv = [torch.tensor(z, dtype=torch.float64, requires_grad=True) for z in (W, A, v)]
    output = tv @ torch.tanh(ta @ torch.tanh(tw @ torch.tensor(U.T)))
    objective = torch.mean((output - torch.tensor(y)) ** 2)
    objective.backward()
    p = Parameters((W, A), n*v)
    raw = loss_gradients(p, x.T, y)
    # c=n*v, hence dL/dv=n*dL/dc.
    errors = {name: float(np.max(np.abs(a.detach().numpy() - b))) for name, a, b in
              (("W", tw.grad, raw.weights[0]), ("A", ta.grad, raw.weights[1]),
               ("v", tv.grad, n*raw.readout))}
    numpy_prediction = dense_forward(W, A, n*v, U)
    errors["maintained_prediction"] = float(np.max(np.abs(forward(p, x.T).output-numpy_prediction)))
    errors["torch_prediction"] = float(np.max(np.abs(output.detach().numpy()-numpy_prediction)))
    if max(errors.values()) > 1e-12:
        raise AssertionError(f"gradient/forward preflight failed: {errors}")
    return dict(maximum_absolute_errors=errors, passed=True, no_training_steps=True)


def closure_preflight():
    """Independent forward/autograd check at fixed arbitrary finite marks."""
    import torch
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "code"))
    from pde.observable_torch_p1 import ClosureEngine
    rng = np.random.default_rng(90732)
    n = 11
    _, U, y = circle(10)
    B1, B2 = rng.normal(size=(n, 5)), rng.normal(size=(n, 3))
    W, M, v = rng.normal(size=(n, 2)), rng.normal(size=(3, 5)), rng.normal(size=n)*0.2
    engine = ClosureEngine(B1, W, B2, M, device="cpu", dtype=torch.float64)
    state, data = engine.state(W, n*v, M), engine.prepare_data(U, y)
    independent = closure_forward(W, M, n*v, B1, B2, U)
    tw, tm, tv = [torch.tensor(z, dtype=torch.float64, requires_grad=True) for z in (W, M, v)]
    hidden1 = torch.tanh(tw @ torch.tensor(U.T))
    features = torch.tensor(B1.T) @ hidden1 / n
    output = tv @ torch.tanh(torch.tensor(B2) @ (tm @ features))
    torch.mean((output-torch.tensor(y))**2).backward()
    velocity = engine.rhs(state, data, implementation="reference")
    errors = dict(maintained_prediction=float(np.max(np.abs(engine.predict(state, data.inputs).numpy()-independent))),
                  torch_prediction=float(np.max(np.abs(output.detach().numpy()-independent))))
    for name, gradient, expected in (("W", tw.grad, -velocity.w/n),
                                     ("M", tm.grad, -velocity.M), ("v", tv.grad, -velocity.c)):
        errors[name] = float(torch.max(torch.abs(gradient-expected)))
    if max(errors.values()) > 1e-12:
        raise AssertionError(f"closure preflight failed: {errors}")
    return dict(maximum_absolute_errors=errors, passed=True, no_training_steps=True,
                physical_mobilities_in_W_M_c=[n, 1, n])


def make_witnesses(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    records = []
    for m, n in ((30, 55), (62, 55), (126, 63), (254, 127)):
        arrays, report = finite_witness(m, n)
        path = output / f"witness_m{m}_n{n}.npz"
        np.savez(path, **arrays)
        report.update(artifact=str(path.resolve()), sha256=sha256(path))
        records.append(report)
    summary = dict(frozen_forward="bias-free two-hidden tanh; U=x/sqrt(2); c/n readout",
                   acceptance=dict(mse_at_most=THRESHOLD, sign_errors=0),
                   witnesses=records, gradient_preflight=gradient_preflight(),
                   counts=dict(dense55=55**2+3*55, closure_trainable=3*1024+15,
                               closure_minimal_predictor=11*1024+15, dense105=105**2+3*105))
    save_json(output / "witness_summary.json", summary)
    print(json.dumps(summary, indent=2, allow_nan=False))


def replay_file(path):
    """Initial raw schema; producer-specific key adaptation may be added later."""
    path = Path(path)
    with np.load(path, allow_pickle=False) as saved:
        U, labels = array(saved["U"], "U"), array(saved["labels"], "labels")
        x_expected, U_expected, labels_expected = circle(len(labels))
        if not np.allclose(U, U_expected, atol=2e-14, rtol=0) or not np.array_equal(labels, labels_expected):
            raise AssertionError("artifact is not the specified ordered alternating circle dataset")
        W, c = saved["W"], saved["c"]
        if "A" in saved:
            prediction = dense_forward(W, saved["A"], c, U)
            model_kind = "dense"
        else:
            prediction = closure_forward(W, saved["M"], c, saved["B1"], saved["B2"], U)
            model_kind = "closure"
        difference = None
        higher_precision = None
        if "prediction" in saved:
            difference = float(np.max(np.abs(prediction - array(saved["prediction"], "saved prediction"))))
            if difference > 1e-8:
                if model_kind == "dense":
                    accurate = dense_forward(W, saved["A"], c, U, dtype=np.longdouble)
                else:
                    accurate = closure_forward(W, saved["M"], c, saved["B1"], saved["B2"], U,
                                               dtype=np.longdouble)
                higher_precision = dict(arithmetic="numpy.longdouble", mantissa_bits=np.finfo(np.longdouble).nmant,
                    saved_prediction_maximum_difference=float(np.max(np.abs(accurate-saved["prediction"]))),
                    float64_prediction_maximum_difference=float(np.max(np.abs(accurate-prediction))),
                    **metrics(accurate, labels))
                # A tolerance exceedance is evidence needing diagnosis, not an
                # automatic assertion of either a fit or a failed artifact.
        if "v" in saved and not np.allclose(saved["v"], c / len(c), atol=2e-14, rtol=2e-14):
            raise AssertionError("stored c and optimized v do not satisfy c=n*v")
        report = dict(artifact=str(path.resolve()), sha256=sha256(path), model_kind=model_kind,
                      m=len(labels), n=len(c), saved_prediction_maximum_difference=difference,
                      saved_prediction_within_tolerance=difference is None or difference <= 1e-8,
                      higher_precision_resolution=higher_precision,
                      **metrics(prediction, labels))
    return report


def load_npz(path):
    with np.load(path, allow_pickle=False) as saved:
        return {key: np.array(saved[key], copy=True) for key in saved.files}


def check_finite_initialization(initial, config):
    """Regenerate Gaussian draws and p=1 finite-carrier marks independently."""
    n, m, seed = int(config["width"]), int(config["m"]), int(config["seed"])
    rng = np.random.default_rng(seed)
    W = rng.standard_normal((n, 2)) * (1 if config["gain"] == "primary" else m/2)
    A = rng.standard_normal((n, n)) / np.sqrt(n)
    c = rng.standard_normal(n) / n
    differences = {"W": float(np.max(np.abs(initial["W"]-W))),
                   "c": float(np.max(np.abs(initial["c"]-c)))}
    if config["model"] == "network":
        differences["A"] = float(np.max(np.abs(initial["A"]-A)))
    else:
        differences["A_source"] = float(np.max(np.abs(initial["A_source"]-A)))
        h = np.tanh(W)
        upper = np.tanh(A @ h)
        reverse = np.tanh(A.T @ upper)
        raw1 = np.column_stack((np.ones(n), h, reverse))
        raw2 = np.column_stack((np.ones(n), upper))
        ridge = 1/4096
        L1 = np.linalg.cholesky(raw1.T @ raw1/n + ridge*np.eye(5))
        L2 = np.linalg.cholesky(raw2.T @ raw2/n + ridge*np.eye(3))
        B1 = np.linalg.solve(L1, raw1.T).T
        B2 = np.linalg.solve(L2, raw2.T).T
        D = B2.T @ (A @ B1)/n
        for name, expected in (("rawB1", raw1), ("rawB2", raw2), ("L1", L1),
                               ("L2", L2), ("B1", B1), ("B2", B2), ("D", D), ("M", D)):
            differences[name] = float(np.max(np.abs(initial[name]-expected)))
    if max(differences.values()) > 2e-10:
        raise AssertionError(f"initialization replay failed: {differences}")
    return differences


def replay_attempt(path):
    """Producer-schema adapter added only after the independent oracle freeze."""
    path = Path(path)
    record = json.loads((path / "record.json").read_text())
    config = record["config"]
    if not record.get("outputs_sha256") or "diagnostics" not in record:
        raise ValueError(f"attempt is incomplete: {path}")
    for name, digest in record["outputs_sha256"].items():
        if Path(name).name != name or sha256(path / name) != digest:
            raise AssertionError(f"raw output hash mismatch: {path / name}")
    data, initial = load_npz(path / "dataset.npz"), load_npz(path / "initial.npz")
    prediction_archive = load_npz(path / "predictions.npz")
    m, n = int(config["m"]), int(config["width"])
    x, U, y = circle(m)
    if (not np.array_equal(data["y"], y) or not np.allclose(data["u"], U, atol=2e-14, rtol=0)
            or not np.allclose(data["x"], x, atol=2e-14, rtol=0)):
        raise AssertionError("producer dataset differs from the specified circle")
    initialization = check_finite_initialization(initial, config)
    reports = {}
    for phase in ("initial", "final", "best", "optimizer_terminal", "pre_polish_best", "polish_candidate"):
        checkpoint = path / f"{phase}.npz"
        if not checkpoint.exists():
            continue
        state = initial if phase == "initial" else load_npz(checkpoint)
        if len(state["c"]) != n:
            raise AssertionError("checkpoint width differs from record")

        def evaluate(dtype=np.float64):
            if config["model"] == "network":
                return dense_forward(state["W"], state["A"], state["c"], data["u"], dtype=dtype)
            if config["model"] != "closure":
                raise ValueError("unsupported producer model")
            return closure_forward(state["W"], state["M"], state["c"], initial["B1"],
                                   initial["B2"], data["u"], dtype=dtype)

        prediction = evaluate()
        result = metrics(prediction, y)
        result["weight_norms"] = {key: norms(state[key]) for key in ("W", "c", "A" if config["model"] == "network" else "M")}
        if phase in record["diagnostics"]:
            reported = record["diagnostics"][phase]
            saved = array(prediction_archive[phase+"_train"], phase+"_train")
            prediction_error = float(np.max(np.abs(prediction-saved)))
            loss_error = abs(result["mse"]-reported["mse"])
            result.update(saved_prediction_maximum_difference=prediction_error,
                          reported_mse_absolute_difference=loss_error,
                          reported_sign_errors_match=reported["sign_errors"] == result["sign_errors"],
                          reported_mse=reported["mse"])
            result["within_tolerances"] = (prediction_error <= 1e-8 and loss_error <= 1e-9
                                            and result["reported_sign_errors_match"])
            if not result["within_tolerances"]:
                accurate = evaluate(np.longdouble)
                result["higher_precision_resolution"] = dict(
                    arithmetic="numpy.longdouble", mantissa_bits=np.finfo(np.longdouble).nmant,
                    saved_prediction_maximum_difference=float(np.max(np.abs(accurate-saved))),
                    float64_prediction_maximum_difference=float(np.max(np.abs(accurate-prediction))),
                    **metrics(accurate, y))
        reports[phase] = result
    return dict(attempt=str(path.resolve()), record_sha256=sha256(path / "record.json"),
                config=config, output_hashes_pass=True, initialization_maximum_differences=initialization,
                states=reports, claimed_fit=record.get("fit"), independently_replayed_fit=reports["best"]["fit"],
                claimed_fit_matches=record.get("fit") == reports["best"]["fit"],
                all_scored_states_within_tolerances=all(reports[k]["within_tolerances"] for k in ("initial", "final", "best")))


def high_precision_prediction(path, digits):
    """Treat each stored binary64 input/weight as its exact real value."""
    import mpmath as mp
    path = Path(path)
    record = json.loads((path / "record.json").read_text())
    state, data = load_npz(path / "best.npz"), load_npz(path / "dataset.npz")
    initial = load_npz(path / "initial.npz")
    n = len(state["c"])
    with mp.workdps(digits):
        # mp.mpf(float) preserves the binary float's exact rational value;
        # conversion through a shortened decimal string would change inputs.
        W, U, c = (mp.matrix(array(z, name).tolist()) for z, name in
                   ((state["W"], "W"), (data["u"], "u"), (state["c"], "c")))
        h1 = (W*U.T).apply(mp.tanh)
        if record["config"]["model"] == "network":
            h2 = (mp.matrix(state["A"].tolist())*h1).apply(mp.tanh)
        else:
            B1, B2, M = (mp.matrix(z.tolist()) for z in (initial["B1"], initial["B2"], state["M"]))
            h2 = (B2*(M*(B1.T*h1/n))).apply(mp.tanh)
        prediction = c.T*h2/n
        values = [prediction[0, j] for j in range(len(data["y"]))]
        residual = [v-mp.mpf(float(y)) for v, y in zip(values, data["y"])]
        mse = mp.fsum(v*v for v in residual)/len(residual)
        errors = sum(v*mp.mpf(float(y)) <= 0 for v, y in zip(values, data["y"]))
        result = dict(digits=digits, mse=float(mse), mse_decimal=mp.nstr(mse, digits),
                      sign_errors=errors, max_abs_error=float(max(abs(v) for v in residual)),
                      fit=bool(mse <= mp.mpf("0.001") and errors == 0),
                      predictions_decimal=[mp.nstr(v, digits) for v in values])
    return values, result


def adjudicate_attempt(path, output, low_digits=60, high_digits=90):
    import mpmath as mp
    started = time.monotonic()
    path, output = Path(path).resolve(), Path(output).resolve()
    ordinary = replay_attempt(path)
    low_values, low = high_precision_prediction(path, low_digits)
    high_values, high = high_precision_prediction(path, high_digits)
    with mp.workdps(high_digits):
        difference = max(abs(a-b) for a, b in zip(low_values, high_values))
        stable = bool(difference < mp.mpf("1e-40") and low["fit"] == high["fit"]
                      and low["sign_errors"] == high["sign_errors"])
        discrepancy = mp.nstr(difference, high_digits)
    evidence = output.parent / ("precise_"+path.name+".json")
    evidence_data = dict(attempt=str(path), record_sha256=ordinary["record_sha256"],
                         best_sha256=sha256(path/"best.npz"), dataset_sha256=sha256(path/"dataset.npz"),
                         exact_input_interpretation="stored binary64 weights and dataset values interpreted as exact reals",
                         original_float64_replay=ordinary, low_precision=low, high_precision=high,
                         precision_comparison_max_abs_difference=discrepancy,
                         stable_to_higher_precision=stable, elapsed_seconds=time.monotonic()-started)
    save_json(evidence, evidence_data)
    entry = dict(resolved=stable, fit=high["fit"], checked_fit=high["fit"], mse=high["mse"],
                 sign_errors=high["sign_errors"], max_abs_error=high["max_abs_error"],
                 record_sha256=ordinary["record_sha256"], method=f"mpmath at {low_digits} and {high_digits} decimal digits",
                 precision_digits=[low_digits, high_digits], stable_to_higher_precision=stable,
                 maximum_precision_difference=discrepancy, evidencepath=str(evidence),
                 original_double_tolerances_pass=ordinary["all_scored_states_within_tolerances"],
                 explanation="Higher-precision evaluation resolves the fit classification of the saved best weights; original float64 prediction-reproduction failures remain recorded. This is numerical precision stabilization, not an interval-arithmetic certificate.")
    entries = json.loads(output.read_text()) if output.exists() else {}
    entries[str(path)] = entry
    save_json(output, entries)
    return entry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    witness = sub.add_parser("witness")
    witness.add_argument("--output", required=True, type=Path)
    preflight = sub.add_parser("closure-preflight")
    preflight.add_argument("--output", required=True, type=Path)
    replay = sub.add_parser("replay")
    replay.add_argument("artifacts", nargs="+", type=Path)
    replay.add_argument("--output", type=Path)
    campaign = sub.add_parser("replay-campaign")
    campaign.add_argument("root", type=Path)
    campaign.add_argument("--output", type=Path, required=True)
    campaign.add_argument("--max-seconds", type=float, default=300)
    precise = sub.add_parser("adjudicate")
    precise.add_argument("attempts", nargs="+", type=Path)
    precise.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.command == "witness":
        make_witnesses(args.output)
    elif args.command == "closure-preflight":
        result = closure_preflight()
        save_json(args.output, result)
        print(json.dumps(result, indent=2, allow_nan=False))
    elif args.command == "replay-campaign":
        started = time.monotonic()
        reports = []
        for record in sorted(args.root.rglob("record.json")):
            if time.monotonic()-started > args.max_seconds:
                raise TimeoutError("independent replay budget exhausted")
            reports.append(replay_attempt(record.parent))
            print(json.dumps({"attempt": str(record.parent), "mse": reports[-1]["states"]["best"]["mse"],
                              "consistent": reports[-1]["all_scored_states_within_tolerances"]}), flush=True)
        save_json(args.output, dict(elapsed_seconds=time.monotonic()-started, attempts=reports))
    elif args.command == "adjudicate":
        for attempt in args.attempts:
            print(json.dumps(adjudicate_attempt(attempt, args.output), indent=2, allow_nan=False), flush=True)
    else:
        reports = [replay_file(path) for path in args.artifacts]
        if args.output is not None:
            save_json(args.output, reports)
        print(json.dumps(reports, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
