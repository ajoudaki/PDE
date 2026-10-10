#!/usr/bin/env python3
"""Two bounded guarded Harmonic replays, reusing saved dense benchmarks.

Example: python -B check_readout_replay.py --case circle --device cuda:0
    --out ../../data/generated/paper_appendix_pilots_20261009/readout_circle

The timing comparison uses the valid float64 construction state. Deployment
defaults to the original float32; --dtype float64 is an explicit follow-up,
never an automatic retry. Replays never bypass a guard. Source
coefficients must be rebuilt by the original offline dense RK4 source rollout;
the scored dense reference and independent dense comparator are not retrained.
"""

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import sys
import time
import traceback

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np
import torch


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/generated/paper_appendix_pilots_20261009"
DRIVER = ROOT / "paper/figures/capture_trajectory.py"
CASES = {
    "circle": dict(
        run="figure4_three_seeds/circle/seed_905/attempt_001",
        config="figure4_three_seeds/circle/config.json", seed=905,
        name="harmonic_1024_r64", pair="dense_4096", dimension=2,
        source_key="harmonic", source_build_rank=64, source_rank=64,
        width=1024, source_seed=275866798499063659,
        selector_seed=1058463656146149852, time_degree=12,
        spatial_degree=25, step=.00625, record_every=80,
    ),
    "sphere": dict(
        run="figure3_paired_seeds/sphere/seed_602",
        config="figure3_paired_seeds/config.json", seed=602,
        name="harmonic_8", pair="dense_pair", dimension=3,
        source_key="harmonic_rank29", source_build_rank=29, source_rank=6,
        width=148, source_seed=602, selector_seed=502, time_degree=8,
        spatial_degree=5, step=.0015625, record_every=320,
    ),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def legacy_readout(features, metric, readout, deficit, labels):
    """Pre-guard Cholesky arithmetic; used only in the stationary benchmark."""
    normalized = features / math.sqrt(len(labels))
    gram = normalized.T @ (metric @ normalized)
    gram = (gram + gram.T) / 2
    factor, info = torch.linalg.cholesky_ex(gram)
    if int(info) != 0:
        raise ArithmeticError("Legacy benchmark Gram is not positive definite")
    correction = (labels - deficit) / math.sqrt(len(labels))
    correction = correction - normalized.T @ (metric @ readout)
    corrected = readout + normalized @ torch.cholesky_solve(
        correction[:, None], factor).flatten()
    return corrected, gram


def initial_gram_diagnostic(model, inputs, labels):
    features = model.fields(model.initial_state, inputs)[0][-1]
    normalized = features / math.sqrt(len(labels))
    gram = normalized.T @ (model.metrics[-1] @ normalized)
    values = torch.linalg.eigvalsh((gram + gram.T) / 2)
    tolerance = 32 * max(normalized.shape) * torch.finfo(gram.dtype).eps
    lo, hi = float(values[0]), float(values[-1])
    return dict(dtype=str(gram.dtype), smallest=lo, largest=hi,
                relative_rank_threshold=tolerance,
                required_smallest_above=tolerance * hi,
                passes_relative_rank_test=bool(lo > tolerance * hi))


def benchmark(ct, model, inputs, labels):
    """Two alternating rounds of 100 unchanged-state RHS calls per backend."""
    guarded = ct._unregularized_readout
    state = model.initial_state
    hashes_before = [ct.array_sha(v.cpu().numpy()) for v in state]
    result = dict(dtype=str(state[0].dtype), calls_per_batch=100,
                  rounds=2, warmup_calls_per_batch=3, batches=[],
                  scope="Stationary valid construction state; not deployment timing")
    try:
        expected = model.rhs(state, inputs, labels)  # Guard must pass first.
        ct._unregularized_readout = legacy_readout
        actual = model.rhs(state, inputs, labels)
        result["rhs_bitwise_equal"] = all(torch.equal(a, b) for a, b in zip(actual, expected))
        result["rhs_max_abs_difference"] = max(float((a-b).abs().max())
                                               for a, b in zip(actual, expected))
        for a, b in zip(actual, expected):
            torch.testing.assert_close(a, b, rtol=2e-11, atol=2e-12)
        del actual, expected
        for round_index, order in enumerate((("legacy", "guarded"), ("guarded", "legacy")), 1):
            for name in order:
                ct._unregularized_readout = legacy_readout if name == "legacy" else guarded
                for _ in range(3):
                    model.rhs(state, inputs, labels)
                ct.synchronize(inputs.device)
                started = time.perf_counter()
                for _ in range(100):
                    model.rhs(state, inputs, labels)
                ct.synchronize(inputs.device)
                elapsed = time.perf_counter() - started
                result["batches"].append(dict(round=round_index, backend=name,
                                               seconds=elapsed, seconds_per_rhs=elapsed/100))
    finally:
        ct._unregularized_readout = guarded
    require(hashes_before == [ct.array_sha(v.cpu().numpy()) for v in state],
            "Timing benchmark mutated the compact initial state")
    means = {name: float(np.mean([v["seconds_per_rhs"] for v in result["batches"]
                                 if v["backend"] == name])) for name in ("legacy", "guarded")}
    result.update(mean_seconds_per_rhs=means,
                  guarded_over_legacy=means["guarded"]/means["legacy"])
    return result


@torch.no_grad()
def replay(args, report, persist):
    case = CASES[args.case]
    folder, config_path = DATA / case["run"], DATA / case["config"]
    old_path, archive = folder / "report.json", folder / "trajectories.npz"
    old = json.loads(old_path.read_text())
    config = json.loads(config_path.read_text())
    report.update(original_config=config, original_source=old["sources"][case["source_key"]],
                  original_model=old["models"][case["name"]],
                  original_run=old["runs"][case["name"]],
                  inputs=dict(report=str(old_path), report_sha256=digest(old_path),
                              config=str(config_path), config_sha256=digest(config_path),
                              archive=str(archive), archive_sha256=digest(archive),
                              original_driver_sha256=old["source_sha256"]))
    require(report["inputs"]["archive_sha256"] == old["trajectories_sha256"],
            "Saved trajectory archive hash differs from its report")
    with np.load(archive, allow_pickle=False) as saved:
        arrays = {key: saved[key] for key in saved.files}
    spec = importlib.util.spec_from_file_location("readout_replay_driver", DRIVER)
    ct = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ct)
    data_hashes = {key: ct.array_sha(arrays[key]) for key in old["data_sha256"]}
    require(data_hashes == old["data_sha256"], "Saved data hash mismatch")
    report["data_sha256"] = data_hashes
    original_model, original_run = report["original_model"], report["original_run"]
    require(old["seed"] == case["seed"] and original_model["width"] == case["width"]
            and original_model["source_rank"] == case["source_rank"], "Saved case differs from frozen replay")
    require(original_model["diagnostics"]["readout_floor"] is None, "Replay requires an unregularized model")
    require(original_run["complete"] and original_run["dtype"] == "torch.float32"
            and original_run["step"] == case["step"]
            and original_run["observation_every"] == case["record_every"]
            and original_run["actual_horizon"] == 32., "Saved training settings differ from replay")
    source_info = report["original_source"]
    for key, expected in dict(requested_rank=case["source_build_rank"], rk4_step=.125,
                              chebyshev_degree=case["time_degree"], spatial_degree=case["spatial_degree"],
                              rollout_dtype="torch.float32", coefficient_dtype="torch.float64").items():
        require(source_info[key] == expected, f"Saved source setting differs: {key}")
    require(old["seeds"]["harmonic_source"] == case["source_seed"], "Source seed mismatch")
    selector_key = "harmonic_selector" if args.case == "circle" else "selector"
    require(old["seeds"][selector_key] == case["selector_seed"], "Selector seed mismatch")
    require(all(v["selection_trials"] == 64 for v in original_model["diagnostics"]["selection"]),
            "Saved selector trial count differs")
    require(original_model["diagnostics"]["condition_limit"] == 16.
            and original_model["diagnostics"]["selection_strategy"] == "uniform", "Selector settings differ")
    times = arrays["times_" + case["name"]]
    require(np.array_equal(times, np.linspace(0., 32., 65))
            and np.array_equal(times, arrays["times_reference"])
            and np.array_equal(times, arrays["times_" + case["pair"]]), "Saved time grids differ")
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(args.device)
    report["environment"] = dict(python=platform.python_version(), torch=torch.__version__,
                                 numpy=np.__version__, device=str(device), threads=1, tf32=False,
                                 hardware=torch.cuda.get_device_name(device) if device.type == "cuda"
                                 else platform.processor())
    inputs, labels, queries = [torch.as_tensor(arrays[key], device=device) for key in
                              ("train_inputs", "train_labels", "query_inputs")]
    require(inputs.shape == (8, case["dimension"]) and queries.shape == (30, case["dimension"]),
            "Unexpected saved input shapes")
    extra = torch.as_tensor(arrays["extra_query_inputs"], device=device) if "extra_query_inputs" in arrays else queries[:0]
    report["stage"] = "dense_initialization"
    persist()
    dense = ct.DeepDense(4096, case["dimension"], 2, "tanh", case["seed"], device)
    hashes = [ct.array_sha(v.cpu().numpy()) for v in dense.initial_state]
    report["reference_initial_state_sha256"] = hashes
    require(hashes == old["reference_initial_state_sha256"], "Regenerated dense initialization hash mismatch")
    report["stage"] = "source_rebuild"
    persist()
    source, report["source_rebuild"] = ct.unified_harmonic_sources(
        dense, inputs, labels, 32., case["source_build_rank"], case["source_seed"],
        seconds=120., step=.125, time_degree=case["time_degree"], spatial_degree=case["spatial_degree"],
        rollout_dtype=torch.float32, coefficient_dtype=torch.float64)
    # Rebuild the original maximum-rank randomized SVD before slicing its prefix.
    source = {key: [value[:, :case["source_rank"]] for value in values] for key, values in source.items()}
    report["retained_source_sha256"] = {key: [ct.array_sha(v.cpu().numpy()) for v in values]
                                       for key, values in source.items()}
    report["stage"] = "compact_construction"
    persist()
    model = ct.DeepHarmonic(dense, inputs, labels, source, case["width"],
                           selection_seed=case["selector_seed"], readout_floor=None,
                           selection_trials=64, condition_limit=16., selection_strategy="uniform")
    require(not any(v["truncated"] for v in model.diagnostics["source_truncations"]),
            "Unexpected extra constructor truncation")
    moving, fixed = sum(v.numel() for v in model.initial_state), int(model.fixed_scalars)
    require((moving, fixed, moving+fixed) == tuple(original_model[k] for k in ("moving", "fixed", "total")),
            "Reconstructed model storage differs from saved model")
    report["model"] = dict(moving=moving, fixed=fixed, total=moving+fixed, diagnostics=model.diagnostics)
    report["compact_initial_state_sha256_float64"] = [ct.array_sha(v.cpu().numpy()) for v in model.initial_state]
    report["stage"] = "stationary_float64_timing"
    persist()
    report["rhs_timing"] = benchmark(ct, model, inputs, labels)
    del source, dense
    checkpoint = args.out / "compact_float64.pt"
    torch.save(dict(
        initial_state=[v.cpu() for v in model.initial_state],
        metrics=[v.cpu() for v in model.metrics],
        metric_inverses=[v.cpu() for v in model.metric_inverses],
        depth=model.depth, activation=model.activation, fixed_scalars=model.fixed_scalars,
        diagnostics=model.diagnostics, case_config=case, data_sha256=data_hashes,
        driver_sha256=report["driver_sha256"],
        inputs=inputs.cpu(), labels=labels.cpu(), queries=queries.cpu(), extra_queries=extra.cpu()), checkpoint)
    report["compact_checkpoint"] = dict(path=str(checkpoint), sha256=digest(checkpoint),
                                        bytes=checkpoint.stat().st_size, dtype="float64")
    dtype = getattr(torch, args.dtype)
    ct._experiment_move(model, device, dtype)
    runtime_inputs, runtime_labels = inputs.to(dtype), labels.to(dtype)
    report["stage"] = args.dtype + "_initial_guard"
    report["initial_runtime_gram"] = initial_gram_diagnostic(model, runtime_inputs, runtime_labels)
    persist()
    model._readout(model.initial_state, runtime_inputs, runtime_labels)
    report["stage"] = "guarded_replay"
    report["replay_progress"] = dict(successful_rhs_calls=0, step=case["step"])
    persist()
    original_rhs = model.rhs

    def counted_rhs(state, batch, targets):
        value = original_rhs(state, batch, targets)
        report["replay_progress"]["successful_rhs_calls"] += 1
        return value

    model.rhs = counted_rhs
    state, prediction, report["run"] = ct.integrate_euler(
        model, runtime_inputs, runtime_labels, torch.cat((inputs, queries, extra)).to(dtype),
        case["step"], 120., horizon=32., max_steps=round(32./case["step"]),
        observation_every=case["record_every"])
    del state, model
    require(report["run"]["complete"] and np.array_equal(report["run"]["times"], times),
            "Guarded replay did not complete the original time grid")
    require(np.isfinite(prediction).all(), "Replay predictions are nonfinite")
    m, p = len(inputs), len(queries)
    predicted = prediction[:, :m+p]
    previous = arrays[case["name"]]
    reference = arrays["reference"][:, m:].astype(float)
    baseline = np.sqrt(np.mean((arrays[case["pair"]][:, m:].astype(float)-reference)**2, axis=1))
    difference = np.sqrt(np.mean((predicted[:, m:].astype(float)-previous[:, m:].astype(float))**2, axis=1))
    error = np.sqrt(np.mean((predicted[:, m:].astype(float)-reference)**2, axis=1))
    require(baseline[-1] > 0 and baseline.max() > 0, "Invalid saved dense-pair denominator")
    report["comparison"] = dict(
        bitwise_equal=bool(np.array_equal(predicted, previous)),
        prediction_max_abs_difference=float(np.max(np.abs(predicted.astype(float)-previous.astype(float)))),
        endpoint_query_rms_difference=float(difference[-1]), maximum_query_rms_difference=float(difference.max()),
        endpoint_difference_over_dense_pair=float(difference[-1]/baseline[-1]),
        maximum_difference_over_dense_pair=float(difference.max()/baseline.max()),
        endpoint_query_rms=float(error[-1]), maximum_query_rms=float(error.max()),
        endpoint_error_over_dense_pair=float(error[-1]/baseline[-1]),
        maximum_error_over_dense_pair=float(error.max()/baseline.max()),
        dense_pair_endpoint_rms=float(baseline[-1]), dense_pair_maximum_rms=float(baseline.max()))
    if len(extra):
        previous_extra = arrays["extra_" + case["name"]]
        report["comparison"]["extra_bitwise_equal"] = bool(np.array_equal(prediction[:, m+p:], previous_extra))
        report["comparison"]["extra_max_abs_difference"] = float(np.max(np.abs(prediction[:, m+p:].astype(float)-previous_extra.astype(float))))
    np.savez_compressed(args.out / "trajectories.npz", predictions=prediction, times=times)
    report.update(status="guarded_replay_complete", stage="complete",
                  trajectories_sha256=digest(args.out / "trajectories.npz"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=tuple(CASES), required=True)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--dtype", choices=("float32", "float64"), default="float32",
                        help="Original float32 or an explicit precision-only follow-up; no automatic retry")
    parser.add_argument("--out", type=Path, required=True, help="Fresh directory under this study's generated data")
    args = parser.parse_args()
    args.out = args.out.resolve()
    require(args.out.is_relative_to(DATA.resolve()), "Output must remain in this study's generated-data directory")
    args.out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    report = dict(case=args.case, case_config=CASES[args.case], status="running", stage="saved_input_validation",
                  command=sys.argv, cwd=str(Path.cwd()), driver=str(DRIVER), driver_sha256=digest(DRIVER),
                  harness_sha256=digest(Path(__file__)),
                  replay_config=dict(dtype=args.dtype, original_dtype="float32", horizon=32., seconds_per_source_and_fit=120.,
                                     readout_floor=None, selector_trials=64, condition_limit=16.,
                                     source_step=.125, source_dtype="float32", coefficient_dtype="float64"),
                  scope="Two frozen cases only; saved dense benchmarks reused; guards unchanged. "
                        "Timing uses float64 construction states; replay precision is explicit. "
                        "Completion is not a convergence certificate or a prediction-equivalence threshold.")

    def persist():
        report["seconds"] = time.monotonic() - started
        (args.out / "report.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")

    persist()
    try:
        replay(args, report, persist)
    except Exception as error:
        numerical_gate = isinstance(error, ArithmeticError) and any(
            phrase in str(error) for phrase in ("Training feature Gram", "Corrected training identity"))
        report.update(status="numerical_guard_rejected" if numerical_gate else "inconclusive",
                      error=dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc()))
    finally:
        persist()
    print(json.dumps({key: report.get(key) for key in ("case", "status", "stage", "seconds", "error")}), flush=True)
    return 0 if report["status"] == "guarded_replay_complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
