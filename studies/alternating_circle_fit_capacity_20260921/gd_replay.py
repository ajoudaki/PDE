#!/usr/bin/env python3
"""Read-only independent audit of frozen GD campaign; never starts training."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
BENCHMARK_HASH = "521421ddc8a3918e9ab5373d1959425499a80a55cbe8796fe025adf008b482af"
PROTOCOL_HASH = "794723de3bdfcb9a95e1d906bf6b2b3486f561f854ae22284f30d623753f5a8f"
SEEDS = (20260921, 20260922, 20260923)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def arrays(path):
    with np.load(path, allow_pickle=False) as archive:
        return {k: archive[k].copy() for k in archive.files}


def fields(state, u, fixed, n):
    h = np.tanh(state["W"] @ u.T)
    if "A" in state:
        z = state["A"] @ h
    else:
        s = fixed["B1"].T @ h / n
        z = fixed["B2"] @ (state["M"] @ s)
    j = np.tanh(z)
    return h, j, state["c"] @ j / n


def gradient(state, u, y, fixed, n):
    h, j, f = fields(state, u, fixed, n)
    r = f - y
    e = (state["c"] / n)[:, None] * (1 - j * j)
    if "A" in state:
        middle, s, d = "A", h, e
        back = state[middle].T @ d
    else:
        middle, s = "M", fixed["B1"].T @ h / n
        d = fixed["B2"].T @ e
        back = fixed["B1"] @ (state[middle].T @ d) / n
    scale = 2 / len(y)
    grad = {"W": scale * ((back * (1 - h * h)) * r) @ u,
            middle: scale * (d * r) @ s.T,
            "c": scale * (j @ r) / n}
    q = n * np.sum(grad["W"] ** 2) + np.sum(grad[middle] ** 2) + n * np.sum(grad["c"] ** 2)
    return grad, float(q), f


def fit(pred, y):
    mse = float(np.mean((pred - y) ** 2))
    return mse, int(np.count_nonzero(y * pred <= 0)), bool(mse <= .001 and np.all(y * pred > 0))


def near(a, b, atol=2e-10, rtol=2e-11):
    return bool(np.all(np.isfinite(a)) and np.all(np.isfinite(b)) and
                np.allclose(a, b, atol=atol, rtol=rtol))


def audit_attempt(job, deadline):
    path = Path(job["output"])
    record = json.loads((path / "record.json").read_text())
    cfg, errors = record["config"], []
    check = lambda condition, label: errors.append(label) if not condition else None
    n, m, seed = cfg["width"], cfg["m"], cfg["seed"]
    middle = "A" if cfg["model"] == "network" else "M"
    for key in ("model", "width", "m", "seed", "gain", "eta_max", "device"):
        check(cfg[key] == job[key], "job_config_" + key)
    constants = dict(max_accepted_steps=30000, max_forward_evals=90000,
                     max_physical_clock=10000.0, max_seconds=75.0,
                     export_reserve_seconds=5.0, fit_mse=.001, armijo=1e-4,
                     armijo_slack=1e-14, max_halvings=30, gradient_floor=1e-28,
                     threads=1, circle_points=8192)
    for key, value in constants.items():
        check(cfg[key] == value, "frozen_config_" + key)
    check(seed in SEEDS and m in (30, 62, 126, 254), "seed_size_membership")
    check(record["block_mobilities"] == [n, 1, n], "mobilities")
    check(record["environment"]["deterministic_algorithms"] and
          not record["environment"]["tf32"] and
          not record["environment"]["cudnn_tf32"] and
          record["environment"]["torch_threads"] == 1, "arithmetic_policy")
    check(record["environment"]["source_sha256"][str((STUDY / "gd_benchmark.py").relative_to(ROOT))]
          == BENCHMARK_HASH, "benchmark_frozen_hash")
    for relative, expected in record["environment"]["source_sha256"].items():
        check(digest(ROOT / relative) == expected, "source_hash_" + relative)
    for name, expected in record["outputs_sha256"].items():
        check(digest(path / name) == expected, "artifact_hash_" + name)
    provenance = record["provenance"]
    check(digest(provenance["freeze_path"]) == provenance["freeze_sha256"], "protocol_hash")
    check(provenance["freeze_sha256"] == PROTOCOL_HASH, "pretraining_protocol_hash")
    check(digest(provenance["config_path"]) == provenance["config_sha256"], "config_hash")
    supplied = json.loads(Path(provenance["config_path"]).read_text())
    for key, value in supplied.items():
        check(value == cfg[key], "config_file_" + key)

    data, initial = arrays(path / "dataset.npz"), arrays(path / "initial.npz")
    theta = 2 * np.pi * np.arange(m) / m
    x = np.column_stack((np.cos(theta), np.sin(theta)))
    y = (-1.0) ** np.arange(m)
    check(near(data["u"], x / np.sqrt(2), atol=1e-15, rtol=0), "data_u")
    check(np.array_equal(data["y"], y), "data_y")
    check(near(data["x"], x, atol=1e-15, rtol=0), "data_x")
    check(len(data["circle_u"]) == 8192, "circle_count")
    circle_theta = 2 * np.pi * np.arange(8192) / 8192
    circle_u = np.column_stack((np.cos(circle_theta), np.sin(circle_theta))) / np.sqrt(2)
    check(near(data["circle_u"], circle_u, atol=2e-15, rtol=0), "circle_u")
    rng = np.random.default_rng(seed)
    w0 = rng.standard_normal((n, 2))
    a0 = rng.standard_normal((n, n)) / np.sqrt(n)
    c0 = rng.standard_normal(n) / n
    gain = 1. if cfg["gain"] == "primary" else m / 2
    w0 *= gain
    check(np.array_equal(initial["W"], w0), "initial_W_exact")
    check(np.array_equal(initial["c"], c0), "initial_c_exact")
    check(record["first_weight_gain"] == gain, "gain")
    if middle == "A":
        check(np.array_equal(initial["A"], a0), "initial_A_exact")
        fixed = {}
    else:
        check(np.array_equal(initial["A_source"], a0), "source_A_exact")
        h = np.tanh(w0)
        upper = np.tanh(a0 @ h)
        reverse = np.tanh(a0.T @ upper)
        raw1, raw2 = np.column_stack((np.ones(n), h, reverse)), np.column_stack((np.ones(n), upper))
        l1 = np.linalg.cholesky(raw1.T @ raw1 / n + np.eye(5) / 4096)
        l2 = np.linalg.cholesky(raw2.T @ raw2 / n + np.eye(3) / 4096)
        b1, b2 = np.linalg.solve(l1, raw1.T).T, np.linalg.solve(l2, raw2.T).T
        d0 = b2.T @ a0 @ b1 / n
        for key, value in (("B1", b1), ("B2", b2), ("M", d0), ("D", d0),
                           ("rawB1", raw1), ("rawB2", raw2), ("L1", l1), ("L2", l2)):
            check(near(initial[key], value, atol=3e-11, rtol=3e-11), "dictionary_" + key)
        fixed = initial
    check(record["trainable_scalar_count"] == sum(initial[k].size for k in ("W", middle, "c")), "trainable_count")
    check(record["frozen_feature_scalar_count"] == (0 if middle == "A" else 8192), "frozen_count")

    predictions = arrays(path / "predictions.npz")
    max_pred = 0.
    recomputed = {}
    for label in ("initial", "best", "final"):
        if time.perf_counter() > deadline:
            raise TimeoutError("Independent 200-second replay budget exhausted")
        saved = initial if label == "initial" else arrays(path / (label + ".npz"))
        state = {k: saved[k] for k in ("W", middle, "c")}
        grad, q, pred = gradient(state, data["u"], y, fixed, n)
        circle = np.concatenate([fields(state, circle_u[i:i+512], fixed, n)[2]
                                 for i in range(0, 8192, 512)])
        for suffix, value in (("train", pred), ("circle", circle)):
            error = float(np.max(np.abs(value - predictions[label + "_" + suffix])))
            max_pred = max(max_pred, error)
            check(error <= 1e-8, label + "_" + suffix + "_prediction")
        mse, signs, fitted = fit(pred, y)
        diag = record["diagnostics"][label]
        check(abs(mse - diag["mse"]) <= 1e-9, label + "_mse")
        check(signs == diag["sign_errors"], label + "_sign_errors")
        check(near(q, diag["gradient"]["physical_Q"], atol=1e-12, rtol=2e-8), label + "_Q")
        for key, value in grad.items():
            check(near(np.linalg.norm(value), diag["gradient"]["canonical_blocks"][key],
                       atol=1e-11, rtol=2e-8), label + "_gradient_" + key)
            check(near(np.linalg.norm(state[key]), diag["parameter_norms"][key]), label + "_norm_" + key)
        recomputed[label] = dict(mse=mse, sign_errors=signs, fit=fitted, physical_Q=q)
    check(recomputed["best"]["fit"] == record["fit"], "fit_status")

    trace = [json.loads(line) for line in (path / "trace.jsonl").read_text().splitlines()]
    check(len(trace) == record["accepted_steps"] + 1, "trace_length")
    clock, rejects, forwards, best, last_eta = 0., 0, 1, trace[0]["mse"], None
    check(trace[0]["accepted_step"] == 0 and trace[0]["physical_clock"] == 0, "initial_trace")
    for index, entry in enumerate(trace[1:], 1):
        previous = trace[index-1]["mse"]
        eta, halvings = entry["eta"], entry["halvings"]
        first = min(cfg["eta_max"], cfg["eta_max"] if last_eta is None else 2*last_eta, 10000-clock)
        q = entry["gradient_from_previous"]["physical_Q"]
        block = entry["gradient_from_previous"]["canonical_blocks"]
        q_from_norms = n*block["W"]**2 + block[middle]**2 + n*block["c"]**2
        check(math.isfinite(q) and q >= 1e-28 and near(q, q_from_norms, atol=1e-20, rtol=2e-12), f"trace_Q_{index}")
        check(entry["accepted_step"] == index and 0 <= halvings <= 30, f"trace_step_{index}")
        check(entry["previous_mse"] == previous, f"trace_previous_{index}")
        check(entry["eta_first"] == first and eta == first * 2.**(-halvings), f"trace_eta_{index}")
        threshold = previous - 1e-4*eta*q + 1e-14*max(1., previous)
        check(near(entry["armijo_threshold"], threshold, atol=2e-15, rtol=2e-15), f"trace_threshold_{index}")
        check(entry["mse"] <= threshold, f"trace_armijo_{index}")
        clock += eta
        rejects += halvings
        forwards += halvings + 1
        best = min(best, entry["mse"])
        check(entry["physical_clock"] == clock and entry["best_mse"] == best, f"trace_clock_best_{index}")
        check(entry["forward_evaluations"] == forwards and entry["rejected_trials_total"] == rejects
              and entry["rejected_trials"] == halvings, f"trace_counts_{index}")
        last_eta = eta
    pending = record["unfinished_line_search"]
    unfinished_rejects = 0 if pending is None else pending["rejected_trials"]
    check(record["rejected_trials"] == rejects + unfinished_rejects, "total_rejections")
    check(record["forward_evaluations"] == forwards + unfinished_rejects, "total_forward_evaluations")
    check(record["physical_clock"] == clock, "total_clock")
    check(abs(recomputed["best"]["mse"] - best) <= 1e-9, "best_state_matches_trace")
    check(abs(recomputed["final"]["mse"] - trace[-1]["mse"]) <= 1e-9, "final_state_matches_trace")
    check(record["nonfinite_rejected_trials"] == 0, "nonfinite_trials")
    check(record["accepted_steps"] <= 30000 and record["forward_evaluations"] <= 90000
          and clock <= 10000 and record["elapsed_seconds_before_final_record_write"] <= 75,
          "attempt_budgets")
    if record["status"] == "gradient_floor":
        check(record["diagnostics"]["final"]["gradient"]["physical_Q"] < 1e-28, "floor_stop")
    if record["status"] == "fit_reached":
        check(recomputed["final"]["fit"], "fit_stop")
    if record["status"] == "physical_clock_limit":
        check(clock >= 10000, "clock_stop")
    if record["status"] == "step_limit":
        check(record["accepted_steps"] == 30000, "step_stop")
    if record["status"] == "evaluation_limit":
        check(record["forward_evaluations"] == 90000, "evaluation_stop")
    check(record["status"] in ("fit_reached", "gradient_floor", "physical_clock_limit",
          "step_limit", "evaluation_limit", "time_limit"), "valid_terminal_status")
    check(record["numerical_valid"] and record["budget_respected"] and job["returncode"] == 0,
          "producer_validity")

    pairs = arrays(path / "gd_step_pairs.npz")
    pair_records = json.loads(str(pairs["record"]))
    check([e["accepted_step"] for e in pair_records] == record["saved_step_pairs"], "pair_indices")
    expected_steps = sorted(set(i for i in (1, 10, 100, 1000, record["accepted_steps"])
                                if 1 <= i <= record["accepted_steps"]))
    check([e["accepted_step"] for e in pair_records] == expected_steps, "pair_coverage")
    max_step = 0.
    for entry in pair_records:
        index, prefix = entry["accepted_step"], entry["prefix"]
        before = {k: pairs[prefix + "_before_" + k] for k in ("W", middle, "c")}
        after = {k: pairs[prefix + "_after_" + k] for k in ("W", middle, "c")}
        grad, q, pred = gradient(before, data["u"], y, fixed, n)
        for key in before:
            expected = before[key] - entry["eta"] * (1 if key == middle else n) * grad[key]
            max_step = max(max_step, float(np.max(np.abs(after[key] - expected))))
            check(near(after[key], expected), f"pair_{index}_update_{key}")
        check(near(q, entry["gradient_from_previous"]["physical_Q"], atol=1e-12, rtol=2e-8), f"pair_{index}_Q")
        check(abs(np.mean((pred-y)**2) - entry["previous_mse"]) <= 1e-9, f"pair_{index}_previous_loss")
        after_mse = float(np.mean((fields(after, data["u"], fixed, n)[2] - y)**2))
        check(abs(after_mse - entry["mse"]) <= 1e-9, f"pair_{index}_after_loss")
        check({k: v for k, v in entry.items() if k != "prefix"} == trace[index], f"pair_{index}_trace_record")
        # The logged halvings must genuinely fail the preceding trial scales.
        for halving in range(entry["halvings"]):
            eta = entry["eta_first"] * 2.**(-halving)
            trial = {k: before[k] - eta*(1 if k == middle else n)*grad[k] for k in before}
            trial_loss = float(np.mean((fields(trial, data["u"], fixed, n)[2]-y)**2))
            threshold = entry["previous_mse"] - 1e-4*eta*q + 1e-14*max(1., entry["previous_mse"])
            check(trial_loss > threshold - 1e-10, f"pair_{index}_rejected_scale_{halving}")
    return dict(output=str(path), passed=not errors, failures=errors,
                record_sha256=digest(path / "record.json"), pair_count=len(pair_records),
                max_prediction_error=max_pred, max_step_error=max_step,
                status=record["status"], fit=recomputed["best"]["fit"],
                best=recomputed["best"], final=recomputed["final"],
                accepted_steps=record["accepted_steps"], physical_clock=clock,
                seed=seed, model=cfg["model"], width=n, m=m, gain=cfg["gain"], eta_max=cfg["eta_max"]), trace


def campaign_checks(campaign, results, traces):
    errors, reproductions = [], []
    check = lambda condition, label: errors.append(label) if not condition else None
    jobs = campaign["jobs"]
    check(len(jobs) <= 51, "attempt_count")
    spent = sum(j["process_wall_seconds"] for j in jobs)
    check(near(spent, campaign["spent_worker_seconds"], atol=1e-9, rtol=0) and spent <= 2500, "worker_budget")
    check(all(j["process_wall_seconds"] <= 85 and j["supervisor_failure"] is None for j in jobs), "worker_individual_caps")
    cumulative, index = 0., 0
    while index < len(jobs):
        group = [jobs[index]]
        if jobs[index]["stage"] != "reproduction" and jobs[index]["seed"] == SEEDS[0] and index + 1 < len(jobs):
            following = jobs[index+1]
            if all(following[k] == jobs[index][k] for k in ("stage","model","width","m","gain","eta_max")):
                group.append(following)
        check(cumulative + 85*len(group) <= 2500, f"reservation_at_job_{index}")
        check(len({j["device"] for j in group}) == len(group), f"distinct_devices_at_job_{index}")
        cumulative += sum(j["process_wall_seconds"] for j in group)
        index += len(group)
    by_output = {r["output"]: r for r in results}
    def selection(stage, model, width, m, gain, eta):
        return [j for j in jobs if (j["stage"], j["model"], j["width"], j["m"], j["gain"], j["eta_max"])
                == (stage, model, width, m, gain, eta)]
    def successes(group):
        return sum(by_output[j["output"]]["fit"] for j in group)
    selected = None
    expected_ladder = []
    for m in (30, 62, 126, 254):
        dense, closure = selection("ladder", "network", 55, m, "rescue", 1.), selection("ladder", "closure", 1024, m, "rescue", 1.)
        if not dense and not closure:
            break
        check(sorted(j["seed"] for j in dense) == list(SEEDS) and sorted(j["seed"] for j in closure) == list(SEEDS), f"ladder_seeds_{m}")
        candidate = successes(dense) == 0 and successes(closure) >= 2
        expected_ladder.append(dict(m=m, dense55_fits=successes(dense), closure_fits=successes(closure), candidate=candidate))
        if candidate:
            selected = m
            break
    check(expected_ladder == campaign["ladder"], "ladder_gate_records")
    if campaign["status"] == "complete":
        chosen = selected if selected is not None else 254
        check(campaign["selected_m"] == chosen and campaign["candidate_found"] == (selected is not None), "selected_case")
        for stage, specs in (("size_control", [("network", 105, "rescue", 1.)]),
                             ("step_sensitivity", [(k,n,"rescue",.5) for k,n in (("network",55),("network",105),("closure",1024))]),
                             ("canonical_control", [(k,n,"primary",1.) for k,n in (("network",55),("network",105),("closure",1024))])):
            for kind, n, gain, eta in specs:
                group = selection(stage, kind, n, chosen, gain, eta)
                check(sorted(j["seed"] for j in group) == list(SEEDS), f"{stage}_{n}_seeds")
        for n in (55, 105):
            dense_stage = "ladder" if n == 55 else "size_control"
            strong = all(successes(selection(cs, "closure", 1024, chosen, "rescue", eta)) >= 2 and
                         successes(selection(ds, "network", n, chosen, "rescue", eta)) == 0
                         for cs, ds, eta in (("ladder", dense_stage, 1.), ("step_sensitivity", "step_sensitivity", .5)))
            check(campaign[f"width{n}_separation_both_caps"] == strong, f"width{n}_separation")
        repeats = [j for j in jobs if j["stage"] == "reproduction"]
        check(len(repeats) == 6, "reproduction_count")
        for repeat in repeats:
            original = next(j for j in jobs if j["output"] == repeat["original_output"])
            peers = [j for j in jobs if j["stage"] == original["stage"] and all(j[k] == original[k]
                    for k in ("model", "width", "m", "gain", "eta_max"))]
            winners = [j for j in peers if by_output[j["output"]]["fit"]]
            expected_seed = min(j["seed"] for j in (winners or peers))
            check(repeat["seed"] == expected_seed, "reproduction_seed_" + Path(repeat["output"]).name)
            check(all(repeat[k] == original[k] for k in ("model","width","m","seed","gain","eta_max","device")), "reproduction_settings")
            a, b = by_output[original["output"]], by_output[repeat["output"]]
            endpoint_pass = a["fit"] == b["fit"] and abs(a["final"]["mse"]-b["final"]["mse"]) <= 1e-6
            censored = (a["status"] == "time_limit" or b["status"] == "time_limit") and a["accepted_steps"] != b["accepted_steps"]
            ta, tb = traces[original["output"]], traces[repeat["output"]]
            prefix_error = max(abs(x["mse"]-y["mse"]) for x,y in zip(ta,tb))
            prefix_step_match = all(x.get("eta") == y.get("eta") and x["physical_clock"] == y["physical_clock"] for x,y in zip(ta,tb))
            reproductions.append(dict(original=original["output"], repeated=repeat["output"], endpoint_pass=endpoint_pass,
                                      time_censored=censored, shared_steps=min(len(ta),len(tb))-1,
                                      shared_trace_max_mse_error=prefix_error, shared_eta_clock_equal=prefix_step_match))
            check(endpoint_pass or censored, "reproduction_uncensored_endpoint")
            check(prefix_error <= 1e-9 and prefix_step_match, "reproduction_shared_prefix")
            declared = next(r for r in campaign["reproductions"] if r["original_output"] == original["output"])
            check(declared["passed"] == endpoint_pass and declared["time_censored"] == censored,
                  "reproduction_declared_classification")
            check(abs(declared["mse_difference"] - abs(a["final"]["mse"]-b["final"]["mse"])) <= 2e-9,
                  "reproduction_declared_mse_difference")
    for relative, expected in campaign["source_hashes"].items():
        check(digest(ROOT / relative) == expected, "campaign_source_" + relative)
    return dict(passed=not errors, failures=errors, spent_worker_seconds=spent,
                selected_m=campaign["selected_m"], ladder=expected_ladder,
                reproductions=reproductions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign", type=Path, default=ROOT / "data/generated/alternating_circle_fit_capacity_20260921/gd_run01")
    parser.add_argument("--output", type=Path, default=ROOT / "data/generated/alternating_circle_fit_capacity_20260921/gd_check_scratch/replay.json")
    args = parser.parse_args()
    start = time.perf_counter()
    campaign_path = args.campaign / "run_record.json"
    campaign_hash = digest(campaign_path)
    campaign = json.loads(campaign_path.read_text())
    if campaign["status"] not in ("complete", "budget_limited", "stopped_with_error"):
        raise SystemExit("Wait for a terminal campaign record before independent replay")
    if digest(STUDY / "gd_benchmark.py") != BENCHMARK_HASH:
        raise SystemExit("Frozen producer source hash mismatch")
    results, traces = [], {}
    for job in campaign["jobs"]:
        result, trace = audit_attempt(job, start + 200)
        results.append(result)
        traces[job["output"]] = trace
    checks = campaign_checks(campaign, results, traces)
    report = dict(passed=all(r["passed"] for r in results) and checks["passed"],
                  elapsed_seconds=time.perf_counter()-start, command=sys.argv,
                  checker_sha256=digest(__file__), run_record_sha256=campaign_hash,
                  campaign_checks=checks, attempts=results,
                  training_performed=False, independent_compute_limit_seconds=200,
                  limitations=["Only retained step pairs have full parameter replay; remaining accepted steps have complete trace arithmetic audit.",
                               "Finite gradient-floor stops are precision-limited, not convergence certificates."])
    if digest(campaign_path) != campaign_hash:
        raise RuntimeError("Campaign record changed during replay")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(json.dumps(dict(passed=report["passed"], attempts=len(results), elapsed_seconds=report["elapsed_seconds"], output=str(args.output))))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
