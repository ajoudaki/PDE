"""Pure saved-stage assessment of the frozen long continuation.

``analyse_stage(output, target)`` returns JSON-serializable evidence and never
writes files or runs trajectories. The supervisor exclusively writes the returned
object to ``stage_analysis_{target:06d}.json``. Matrix RMS always means ||A||F/m.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import sys

import numpy as np

sys.dont_write_bytecode = True
STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/wide_network_closure_comparison"
PLAN = STUDY / "LONG_20260914_PLAN.md"
PLAN_SHA256 = "e3ff7a4462d6ddf17c6cb287c76875edd56a6c933bd6b7b2f83ba3dfa25aebc8"
STAGES = (40, 80, 160, 320, 640, 1280, 2560, 5120, 10240)
WIDTHS, SEEDS = (2048, 8192), (11, 29, 47)
PANELS = {"data": slice(0, 16), "circle": slice(16, 144)}
CONTROL_PAIRS = (
    ("network_time", "arcs30_n8192_s11_halfstep", "arcs30_n8192_s11"),
    ("network_precision", "arcs30_n2048_s11_float64", "arcs30_n2048_s11"),
    ("N3_time", "arcs30_N3_halfstep", "arcs30_N3"),
    ("N5_fine_time", "arcs30_N5_fine_halfstep", "arcs30_N5_fine"),
)
QUADRATURE_PAIRS = (
    ("N3_quadrature", "arcs30_N3", "arcs30_N3_refined"),
    ("N5_quadrature_1024_2048", "arcs30_N5", "arcs30_N5_refined"),
    ("N5_quadrature_2048_4096", "arcs30_N5_refined", "arcs30_N5_fine"),
)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def scoped_path(value, base=ROOT):
    path = (base / value).resolve()
    require(any(path.is_relative_to(root) for root in
                (STUDY, GENERATED, ROOT / "code", ROOT / "docs")),
            "recorded path outside this study and maintained sources: " + str(value))
    return path


def check_hashes(mapping, base=ROOT):
    require(isinstance(mapping, dict) and bool(mapping), "missing hash manifest")
    result = {}
    for name, expected in mapping.items():
        # Historical records sometimes name a flat study source by basename.
        candidate_base = STUDY if base == ROOT and Path(name).parent == Path(".") else base
        path = scoped_path(name, candidate_base)
        result[name] = sha(path)
        require(result[name] == expected, "checksum mismatch: " + name)
    return result


def load_arrays(path):
    with np.load(path, allow_pickle=False) as archive:
        return {key: archive[key].copy() for key in archive.files}


def matrix_rms(value):
    return np.linalg.norm(value, axis=(-2, -1)) / value.shape[-1]


def curve_summary(curve, times, **metadata):
    curve = np.asarray(curve, dtype=float)
    i = int(np.argmax(curve))
    return dict(metadata, curve=curve.tolist(), maximum=float(curve[i]),
                maximum_time=float(times[i]), initial=float(curve[0]),
                terminal=float(curve[-1]), minimum=float(np.min(curve)),
                range=float(np.ptp(curve)))


def expected_configs():
    network = {f"arcs30_n{width}_s{seed}": dict(width=width, seed=seed,
               dtype="float32", kind="primary", step=.01)
               for width in WIDTHS for seed in SEEDS}
    network.update(arcs30_n8192_s11_halfstep=dict(width=8192, seed=11,
        dtype="float32", kind="time_control", step=.005),
        arcs30_n2048_s11_float64=dict(width=2048, seed=11,
        dtype="float64", kind="precision_control", step=.01))
    closure = {}
    for order, suffix, q, p, step, kind in (
        (1, "", 1024, 512, "1/200", "primary"),
        (3, "", 1024, 512, "1/200", "primary"),
        (5, "", 1024, 512, "1/200", "primary"),
        (3, "_refined", 2048, 1024, "1/200", "quadrature_control"),
        (3, "_halfstep", 1024, 512, "1/400", "time_control"),
        (5, "_refined", 2048, 1024, "1/200", "quadrature_control"),
        (5, "_fine", 4096, 2048, "1/200", "quadrature_control"),
        (5, "_fine_halfstep", 4096, 2048, "1/400", "time_control")):
        closure[f"arcs30_N{order}{suffix}"] = dict(order=order,
            initialization_nodes=q, population_nodes=p, step=step,
            refined=q > 1024, kind=kind)
    return {"network": network, "closure": closure}


def validate_manifest(output, manifest):
    require(sha(PLAN) == PLAN_SHA256 == manifest.get("plan_sha256"),
            "frozen long plan checksum mismatch")
    source = scoped_path(manifest["source_run"])
    require(source == GENERATED / "ARC30_20260914_v1", "unexpected replay source")
    for filename, field in (("arc30_campaign.json", "source_campaign_sha256"),
                            ("final_verification.json", "source_verification_sha256")):
        require(sha(source / filename) == manifest.get(field),
                "archived campaign provenance checksum mismatch: " + filename)
    input_hash = sha(output / "inputs.npz")
    require(input_hash == manifest.get("inputs_sha256") == sha(source / "inputs.npz"),
            "input checksum mismatch")
    if manifest.get("inputs_json_sha256"):
        require(sha(output / "inputs.json") == manifest["inputs_json_sha256"],
                "input metadata checksum mismatch")
    inputs = load_arrays(output / "inputs.npz")
    for key, shape in {"times": (206,), "circle": (128, 2),
        "arcs30_inputs": (16, 2), "arcs30_labels": (16,),
        "arcs30_probabilities": (16,)}.items():
        require(key in inputs and inputs[key].shape == shape and
                np.isfinite(inputs[key]).all(), "invalid inputs: " + key)
    require(np.array_equal(inputs["arcs30_probabilities"], np.full(16, 1 / 16)),
            "training probabilities are not the frozen equal weights")
    require(inputs["times"][0] == 0 and inputs["times"][-1] == 40 and
            np.all(np.diff(inputs["times"]) > 0), "invalid bootstrap times")
    checks = {"producer_hashes": check_hashes(manifest.get("producer_hashes"))}
    expected = expected_configs()
    for family in ("network", "closure"):
        configs = manifest[family + "_configs"]
        names = [row.get("name", row.get("id")) for row in configs]
        require(len(names) == 8 and set(names) == set(expected[family]),
                "frozen configuration count/menu mismatch: " + family)
        for name, config in zip(names, configs):
            require(config.get("case") == "arcs30", "configuration law mismatch")
            for key, value in expected[family][name].items():
                equal = (Fraction(str(config.get(key))) == Fraction(str(value))
                         if key == "step" else config.get(key) == value)
                require(equal, f"frozen configuration mismatch: {name}/{key}")
    return inputs, source, checks


def validate_replay(run, source, atol):
    old = source / run["family"] / run["name"]
    old_record = read(old / "record.json")
    for filename, field in (("gram.npy", "gram_sha256"),
                            ("observations.npz", "observations_sha256")):
        require(sha(old / filename) == old_record.get(field),
                "archived replay output checksum mismatch: " + str(old / filename))
    old_arrays = load_arrays(old / "observations.npz")
    errors, passed = {}, True
    for key, reference in old_arrays.items():
        actual = run["arrays"].get(key)
        require(actual is not None and actual.shape == reference.shape,
                "missing replay observable: " + key)
        errors[key] = float(np.max(np.abs(actual - reference)))
        passed &= bool(np.allclose(actual, reference, atol=atol, rtol=1e-9))
    old_gram = np.load(old / "gram.npy", mmap_mode="r", allow_pickle=False)
    max_gram_error = 0.
    for start in range(0, len(old_gram), 8):
        a, b = run["gram"][start:start + 8], old_gram[start:start + 8]
        max_gram_error = max(max_gram_error, float(np.max(np.abs(a - b))))
        passed &= bool(np.allclose(a, b, atol=atol, rtol=1e-9))
    field = ("initial_float64_block_hashes" if run["family"] == "network"
             else "initialization_array_sha256")
    current = run["record"].get(field)
    initialization_passed = bool(current) and current == old_record.get(field)
    if run["family"] == "closure":
        initialization_passed &= (run["record"].get("fixed_signature_initial") ==
                                  old_record.get("fixed_signature_initial"))
    passed &= initialization_passed
    require(passed, "archived trajectory or initialization replay mismatch")
    return dict(passed=True, absolute_tolerance=atol, relative_tolerance=1e-9,
                scalar_maximum_errors=errors, gram_maximum_error=max_gram_error,
                initialization_hashes_match=True, archived_record_sha256=sha(old / "record.json"),
                exact_observations_and_grams=max([max_gram_error, *errors.values()]) == 0.)


def load_run(output, family, config, target, times, inputs, source):
    name = config.get("name", config.get("id"))
    folder = output / family / name / f"stage_{target:06d}"
    record_path = folder / "record.json"
    record = read(record_path)
    require(record.get("status") == "complete", "stage is not complete")
    require(record.get("target") == target, "recorded stage target mismatch")
    require(record.get("config", record.get("configuration")) == config,
            "recorded frozen configuration mismatch")
    expected_step = (Fraction(str(config["step"])) if target == 40 else
                     Fraction(1, 40) if config["kind"] == "time_control" else Fraction(1, 20))
    actual_step = Fraction(str(record.get("step", record.get("step_size"))))
    require(actual_step == expected_step, "recorded integration step mismatch")
    duration = target if target == 40 else target // 2
    expected_steps = int(Fraction(duration) / expected_step)
    require(record.get("actual_steps", record.get("steps_completed")) == expected_steps,
            "recorded integration step count mismatch")
    require(record.get("plan_sha256") == PLAN_SHA256, "run plan checksum mismatch")
    require(record.get("inputs_sha256") == sha(output / "inputs.npz"),
            "run input checksum mismatch")
    sources = check_hashes(record.get("source_hashes"))
    hashes = {}
    checkpoint_file = record.get("checkpoint_file")
    require(isinstance(checkpoint_file, str) and Path(checkpoint_file).name == checkpoint_file,
            "checkpoint_file must be a filename")
    for filename, field in (("gram.npy", "gram_sha256"),
        ("observations.npz", "observations_sha256"), (checkpoint_file, "checkpoint_sha256")):
        hashes[field] = sha(folder / filename)
        require(hashes[field] == record.get(field), "stage output checksum mismatch: " + filename)
    count = len(times)
    require(record.get("completed_observations", record.get("gram_completed_observations")) == count,
            "recorded observation count mismatch")
    require(record.get("validation", {}).get("passed") is True,
            "worker validation absent or failed")
    arrays = load_arrays(folder / "observations.npz")
    shapes = {"times": (count,), "loss": (count,), "mean_prediction": (count,),
              "data_predictions": (count, 16), "predictions": (count, 128),
              "raw_rms": (count, 2), "second_moments": (count, 2),
              "initial_second_moments": (count, 2), "cross_moments": (count, 2),
              "motion_rms": (count, 2)}
    for key, shape in shapes.items():
        require(key in arrays and arrays[key].shape == shape and np.isfinite(arrays[key]).all(),
                "invalid scalar/prediction array: " + key)
    require(all(np.isfinite(a).all() for a in arrays.values()), "nonfinite extra observable")
    require(np.array_equal(arrays["times"], times), "stage observation schedule mismatch")
    require(np.all(arrays["loss"] >= 0), "negative squared loss")
    matrices = np.load(folder / "gram.npy", mmap_mode="r", allow_pickle=False)
    require(matrices.shape == (count, 2, 144, 144) and matrices.dtype == np.float64,
            "Gram shape/dtype mismatch")
    if "gram_shape" in record:
        require(record["gram_shape"] == list(matrices.shape), "recorded Gram shape mismatch")
    tolerance = 2e-6 if config.get("dtype") == "float32" else 2e-11
    q, y = inputs["arcs30_probabilities"], inputs["arcs30_labels"]
    identities = dict(loss=float(np.max(np.abs(arrays["loss"] -
        np.sum(q * (arrays["data_predictions"] - y) ** 2, axis=1)))),
        mean_prediction=float(np.max(np.abs(arrays["mean_prediction"] - arrays["data_predictions"] @ q))),
        raw_rms=float(np.max(np.abs(arrays["raw_rms"] ** 2 - arrays["second_moments"]))),
        paired_motion=float(np.max(np.abs(arrays["motion_rms"] ** 2 -
            (arrays["second_moments"] + arrays["initial_second_moments"] - 2 * arrays["cross_moments"])))),
        initial_second_moments_constant=float(np.max(np.abs(arrays["initial_second_moments"] -
            arrays["initial_second_moments"][0]))))
    asymmetry = maximum_entry = trace_rms_error = trace_second_error = 0.
    for start in range(0, count, 8):
        block = matrices[start:start + 8]
        require(np.isfinite(block).all(), "nonfinite Gram entry")
        asymmetry = max(asymmetry, float(np.max(np.abs(block - block.swapaxes(-1, -2)))))
        maximum_entry = max(maximum_entry, float(np.max(np.abs(block))))
        trace = np.diagonal(block[:, :, :16, :16], axis1=2, axis2=3) @ q
        trace_rms_error = max(trace_rms_error,
            float(np.max(np.abs(trace - arrays["raw_rms"][start:start + 8] ** 2))))
        trace_second_error = max(trace_second_error,
            float(np.max(np.abs(trace - arrays["second_moments"][start:start + 8]))))
    min_eigenvalues = [float(np.linalg.eigvalsh((g + g.T) / 2)[0]) for g in matrices[-1]]
    validation = dict(passed=True, scalar_identity_errors=identities,
        maximum_asymmetry=asymmetry, maximum_absolute_entry=maximum_entry,
        maximum_diagonal_rms_squared_error=trace_rms_error,
        maximum_diagonal_second_moment_error=trace_second_error,
        endpoint_minimum_eigenvalues=min_eigenvalues, scalar_tolerance=tolerance,
        symmetry_bound_psd_tolerance=2e-11, worker_validation=record["validation"])
    require(max(identities.values()) <= tolerance, "scalar identity tolerance exceeded")
    require(max(trace_rms_error, trace_second_error) <= tolerance, "Gram/raw-RMS identity failed")
    require(asymmetry <= 2e-11 and maximum_entry <= 1 + 2e-11,
            "Gram symmetry/entry bound failed")
    require(min(min_eigenvalues) >= -2e-11, "endpoint Gram PSD tolerance exceeded")
    if family == "closure":
        require(record.get("fixed_marks_verified") is True and
                bool(record.get("fixed_signature_initial")) and
                record["fixed_signature_initial"] == record.get("fixed_signature_final"),
                "frozen closure marks mismatch")
    run = dict(name=name, family=family, config=config, record=record, arrays=arrays,
               gram=matrices, folder=folder)
    if target == 40:
        require(record.get("replay", {}).get("passed") is True, "worker replay absent or failed")
        replay_tolerance = tolerance if family == "network" else 1e-10
        validation["replay"] = validate_replay(run, source, replay_tolerance)
        require(np.max(np.abs(arrays["motion_rms"][0])) <= tolerance,
                "nonzero bootstrap initial motion")
        initial = matrices[0].copy()
    else:
        previous = output / family / name / f"stage_{target // 2:06d}"
        previous_record = read(previous / "record.json")
        require(previous_record.get("status") == "complete", "previous checkpoint stage incomplete")
        require(record.get("prior_checkpoint_sha256") == previous_record.get("checkpoint_sha256") ==
                sha(previous / previous_record["checkpoint_file"]), "checkpoint continuity hash mismatch")
        previous_arrays = load_arrays(previous / "observations.npz")
        require(sha(previous / "observations.npz") == previous_record.get("observations_sha256") and
                sha(previous / "gram.npy") == previous_record.get("gram_sha256"),
                "previous shared-endpoint output checksum mismatch")
        require(set(previous_arrays) == set(arrays), "observable set changed across checkpoint")
        continuity_errors = {}
        for key in arrays:
            continuity_errors[key] = float(np.max(np.abs(arrays[key][0] - previous_arrays[key][-1])))
            require(np.array_equal(arrays[key][0], previous_arrays[key][-1]),
                    "checkpoint shared observation differs: " + key)
        previous_gram = np.load(previous / "gram.npy", mmap_mode="r", allow_pickle=False)
        require(np.array_equal(matrices[0], previous_gram[-1]), "checkpoint shared Gram differs")
        bootstrap = output / family / name / "stage_000040"
        bootrecord = read(bootstrap / "record.json")
        require(sha(bootstrap / "gram.npy") == bootrecord.get("gram_sha256"),
                "bootstrap initial Gram checksum mismatch")
        field = "initial_float64_block_hashes" if family == "network" else "initialization_array_sha256"
        require(bool(record.get(field)) and record.get(field) == bootrecord.get(field),
                "initialization signature changed since bootstrap")
        if family == "closure":
            require(record["fixed_signature_initial"] == bootrecord["fixed_signature_initial"],
                    "frozen mark signature changed since bootstrap")
        initial = np.load(bootstrap / "gram.npy", mmap_mode="r", allow_pickle=False)[0].copy()
        validation["checkpoint_continuity"] = dict(passed=True,
            scalar_maximum_errors=continuity_errors, gram_exact=True,
            previous_record_sha256=sha(previous / "record.json"))
    run["initial"] = initial
    differences = np.diff(arrays["loss"])
    allowed = np.maximum(1e-4, .01 * arrays["loss"][:-1])
    increases = [dict(start=float(times[i]), end=float(times[i + 1]),
        increase=float(differences[i]), threshold=float(allowed[i]),
        substantial=bool(differences[i] > allowed[i])) for i in np.flatnonzero(differences > 0)]
    status = dict(name=name, family=family, configuration=config, status="complete",
        record_sha256=sha(record_path), source_hashes=sources, **hashes,
        completed_observations=count, validation=validation,
        loss_increases=increases, substantial_loss_increase=any(r["substantial"] for r in increases),
        loss_curve=arrays["loss"].tolist(), loss_initial=float(arrays["loss"][0]),
        loss_terminal=float(arrays["loss"][-1]),
        loss_fractional_change=float(arrays["loss"][-1] / arrays["loss"][0] - 1)
            if arrays["loss"][0] else None)
    return run, status


def gram_comparisons(left_run, right_run, times, **metadata):
    rows = []
    for layer, (panel, selected), observable in itertools.product(
            range(2), PANELS.items(), ("G", "DeltaG")):
        difference = left_run["gram"][:, layer, selected, selected] - right_run["gram"][:, layer, selected, selected]
        if observable == "DeltaG":
            difference = difference - (left_run["initial"][layer, selected, selected] -
                                       right_run["initial"][layer, selected, selected])
        rows.append(curve_summary(matrix_rms(difference), times, **metadata,
            layer=layer + 1, panel=panel, observable=observable))
    return rows


def scalar_comparisons(left_run, right_run, times, **metadata):
    rows = [curve_summary(np.abs(left_run["arrays"]["loss"] - right_run["arrays"]["loss"]),
        times, **metadata, observable="loss", panel=None, layer=None)]
    for panel, key in (("data", "data_predictions"), ("circle", "predictions")):
        difference = left_run["arrays"][key] - right_run["arrays"][key]
        rows.append(curve_summary(np.sqrt(np.mean(difference ** 2, axis=1)), times,
                                 **metadata, observable="predictions", panel=panel, layer=None))
    return rows


def mean_run(runs):
    # Float64 sums retain each method's own initial mean for DeltaG.
    return dict(gram=sum(r["gram"] for r in runs) / len(runs),
        initial=np.mean([r["initial"] for r in runs], axis=0),
        arrays={key: np.mean([r["arrays"][key] for r in runs], axis=0)
                for key in ("loss", "data_predictions", "predictions")})


def window_indices(times, target):
    # The bootstrap keeps all 206 raw values; its descriptive windows use the
    # same 11-point pattern as later stages and never authorize a settled stop.
    scheduled = np.linspace(target / 2, target, 21)
    indices = []
    for t in scheduled:
        matched = np.flatnonzero(times == t)
        require(len(matched) == 1, "missing quarter-window scheduled time")
        indices.append(int(matched[0]))
    return (np.array(indices[:11]), np.array(indices[10:]))


def settling_checks(runs, comparisons, times, target):
    windows = window_indices(times, target)
    loss_rows, gram_rows, error_rows = [], [], []
    for wi, selected in enumerate(windows):
        common = dict(window=wi + 1, start=float(times[selected[0]]),
                      end=float(times[selected[-1]]), count=len(selected))
        for run in runs.values():
            loss = run["arrays"]["loss"][selected]
            variation, threshold = float(np.ptp(loss)), max(1e-4, .05 * float(np.mean(loss)))
            loss_rows.append(dict(common, name=run["name"], family=run["family"],
                observable="loss", variation=variation, threshold=threshold,
                passed=variation <= threshold, mean=float(np.mean(loss)),
                initial=float(loss[0]), terminal=float(loss[-1]),
                fractional_change=float(loss[-1] / loss[0] - 1) if loss[0] else None,
                threshold_ratio=variation / threshold))
            for layer, (panel, panel_slice) in itertools.product(range(2), PANELS.items()):
                values = run["gram"][selected, layer, panel_slice, panel_slice]
                distances = matrix_rms(values - values[5])
                bound = 2 * float(np.max(distances))
                endpoint = float(matrix_rms(values[-1] - values[0]))
                norm = float(matrix_rms(values[0]))
                gram_rows.append(dict(common, name=run["name"], family=run["family"],
                    observable="G", layer=layer + 1, panel=panel,
                    variation_bound=bound, threshold=.005, passed=bound <= .005,
                    midpoint_time=float(times[selected[5]]), midpoint_distance_curve=distances.tolist(),
                    endpoint_change=endpoint, relative_endpoint_change=endpoint / norm if norm else None,
                    threshold_ratio=bound / .005))
        for comparison in comparisons:
            values = np.asarray(comparison["curve"])[selected]
            variation = float(np.ptp(values))
            metadata = {k: comparison[k] for k in ("closure", "width", "layer", "panel", "observable")}
            error_rows.append(dict(common, **metadata, variation=variation,
                threshold=.002, passed=variation <= .002, initial=float(values[0]),
                terminal=float(values[-1]), threshold_ratio=variation / .002))
    rows = loss_rows + gram_rows + error_rows
    failures = [row for row in rows if not row["passed"]]
    expected_count = 32 + 128 + 256
    complete = len(loss_rows) == 32 and len(gram_rows) == 128 and len(error_rows) == 256
    return dict(eligible=target >= 160, passed=complete and not failures,
        expected_condition_count=expected_count, condition_count=len(rows),
        passed_condition_count=sum(row["passed"] for row in rows), failed_condition_count=len(failures),
        complete=complete, loss_windows=loss_rows, gram_windows=gram_rows,
        error_windows=error_rows, failures=failures,
        maximum_witness=max(rows, key=lambda r: r["threshold_ratio"]) if rows else None)


def previous_evidence(output, target):
    results, links = [], []
    for previous in STAGES:
        if previous >= target:
            break
        path = output / f"stage_analysis_{previous:06d}.json"
        result = read(path)
        require(result.get("target") == previous and result.get("status") == "complete",
                "previous stage analysis is invalid/incomplete")
        require(result.get("source_sha256") == sha(__file__) and result.get("plan_sha256") == PLAN_SHA256,
                "previous analysis source/plan changed")
        require(result.get("completed_run_count") == 16,
                "previous stage analysis is missing runs")
        results.append(result)
        links.append(dict(target=previous, file=path.name, sha256=sha(path)))
    return results, links


def cumulative_rows(current, previous, table):
    def key(row):
        return tuple(row.get(k) for k in ("control_kind", "left", "reference", "observable", "layer", "panel"))
    combined = {key(row): dict(row, maximum_stage=None) for row in current}
    for result in previous:
        for row in result[table]:
            k = key(row)
            require(k in combined, "previous control/quadrature menu changed")
            if row["maximum"] > combined[k]["maximum"]:
                combined[k] = dict(row, maximum_stage=result["target"])
    return list(combined.values())


def analyse_stage(output, target):
    """Assess one complete common stage, preserving failures as returned evidence.

    No returned ``settled`` recommendation can bypass missing runs, provenance,
    array validation, cumulative numerical controls, or either late-time window.
    The root supervisor handles the frozen horizon and resource stop separately.
    """
    output, target = Path(output).resolve(), int(target)
    require(output.parent == GENERATED.resolve() and output.name.startswith("LONG_"),
            "output must be this study's LONG_* generated directory")
    require(target in STAGES, "target is outside the frozen stage menu")
    result = dict(format="long-20260914-stage-analysis-v1", target=target,
        created_utc=datetime.now(timezone.utc).isoformat(), source_sha256=sha(__file__),
        plan_sha256=PLAN_SHA256, status="incomplete", completed_run_count=0,
        expected_run_count=16, validation_pass=False, stop_recommended=None,
        provenance_errors=[], runs=[], times=[], comparisons=[], scalar_comparisons=[],
        numerical_controls=[], quadrature_comparisons=[], frozen_initial_baselines=[],
        seed_diagnostics=[], width_diagnostics=[], loss_curves=[],
        thresholds=dict(loss_absolute=1e-4, loss_fraction=.05, gram_variation=.005,
            gram_error_range=.002, numerical_control=.002, minimum_settled_target=160),
        interpretation="Finite saved-time evidence of apparent settling at declared tolerances; no asymptotic claim.",
        numerical_coverage_limit="N1 has no dedicated closure time control; N3/N5 controls do not rigorously bound other orders or resolutions. Quadrature gaps qualify identification and accuracy but do not block computed-system settling.")
    try:
        manifest_path = output / "long_campaign.json"
        manifest = read(manifest_path)
        result["campaign_sha256"] = sha(manifest_path)
        inputs, source, provenance = validate_manifest(output, manifest)
        result["provenance_checks"] = provenance
        result["inputs_sha256"] = sha(output / "inputs.npz")
        times = inputs["times"] if target == 40 else np.linspace(target / 2, target, 21)
        result["times"] = times.tolist()
    except (OSError, ValueError, KeyError, TypeError) as error:
        result["provenance_errors"].append(str(error))
        result["stop_recommended"] = "numerically_unresolved"
        return result
    runs = {}
    for family in ("network", "closure"):
        for config in manifest[family + "_configs"]:
            name = config.get("name", config.get("id"))
            try:
                run, status = load_run(output, family, config, target, times, inputs, source)
                runs[name] = run
                result["runs"].append(status)
            except (OSError, ValueError, KeyError, TypeError) as error:
                result["runs"].append(dict(name=name, family=family, configuration=config,
                    status="validation_failed_or_incomplete", error=str(error)))
    result["completed_run_count"] = len(runs)
    result["validation_pass"] = len(runs) == 16
    result["loss_curves"] = [dict(name=name, family=run["family"], curve=run["arrays"]["loss"].tolist())
                             for name, run in runs.items()]
    if len(runs) != 16:
        result["stop_recommended"] = "numerically_unresolved"
        return result
    result["status"] = "complete"
    means = {width: mean_run([runs[f"arcs30_n{width}_s{seed}"] for seed in SEEDS]) for width in WIDTHS}
    for width, mean in means.items():
        result["loss_curves"].append(dict(name=f"arcs30_n{width}_mean", family="network_seed_mean",
                                          width=width, curve=mean["arrays"]["loss"].tolist()))
    for name, run in runs.items():
        if run["family"] != "closure":
            continue
        for width, mean in means.items():
            metadata = dict(closure=name, order=run["config"]["order"], width=width,
                            seeds=list(SEEDS), reference=f"arcs30_n{width}_three_seed_mean")
            result["comparisons"].extend(gram_comparisons(run, mean, times, **metadata))
            result["scalar_comparisons"].extend(scalar_comparisons(run, mean, times, **metadata))
    for name, run in itertools.chain(runs.items(), ((f"arcs30_n{w}_mean", r) for w, r in means.items())):
        for layer, (panel, selected) in itertools.product(range(2), PANELS.items()):
            gram = run["gram"][:, layer, selected, selected]
            baseline = matrix_rms(gram - run["initial"][layer, selected, selected])
            norm = matrix_rms(gram)
            row = curve_summary(baseline, times, name=name, layer=layer + 1, panel=panel,
                                observable="G_minus_own_initial")
            row["current_gram_norm_curve"] = norm.tolist()
            row["relative_curve"] = [float(x / y) if y else None for x, y in zip(baseline, norm)]
            result["frozen_initial_baselines"].append(row)
    for kind, left, right in CONTROL_PAIRS + QUADRATURE_PAIRS:
        table = "numerical_controls" if (kind, left, right) in CONTROL_PAIRS else "quadrature_comparisons"
        metadata = dict(control_kind=kind, left=left, reference=right)
        result[table].extend(gram_comparisons(runs[left], runs[right], times, **metadata))
        result[table].extend(scalar_comparisons(runs[left], runs[right], times, **metadata))
    for width in WIDTHS:
        for first, second in itertools.combinations(SEEDS, 2):
            left, right = f"arcs30_n{width}_s{first}", f"arcs30_n{width}_s{second}"
            metadata = dict(width=width, left=left, reference=right)
            result["seed_diagnostics"].extend(gram_comparisons(runs[left], runs[right], times, **metadata))
            result["seed_diagnostics"].extend(scalar_comparisons(runs[left], runs[right], times, **metadata))
    result["width_diagnostics"] = gram_comparisons(means[2048], means[8192], times,
        left="arcs30_n2048_mean", reference="arcs30_n8192_mean") + scalar_comparisons(
        means[2048], means[8192], times, left="arcs30_n2048_mean", reference="arcs30_n8192_mean")
    result["settling"] = settling_checks(runs, result["comparisons"], times, target)
    previous = []
    try:
        previous, links = previous_evidence(output, target)
        result["previous_analyses"] = links
        cumulative = cumulative_rows(result["numerical_controls"], previous, "numerical_controls")
        cumulative_quad = cumulative_rows(result["quadrature_comparisons"], previous, "quadrature_comparisons")
        for rows in (cumulative, cumulative_quad):
            for row in rows:
                if row["maximum_stage"] is None:
                    row["maximum_stage"] = target
        result["cumulative_numerical_controls"] = cumulative
        result["cumulative_quadrature_comparisons"] = cumulative_quad
    except (OSError, ValueError, KeyError, TypeError) as error:
        result["provenance_errors"].append(str(error))
        cumulative = result["numerical_controls"]
    tested = [row for row in cumulative if row["observable"] in ("loss", "G", "DeltaG")]
    failures = [row for row in tested if row["maximum"] > .002]
    increases = [dict(target=target, name=row["name"], **inc) for row in result["runs"]
                 for inc in row["loss_increases"] if inc["substantial"]]
    for earlier in previous:
        increases.extend(dict(target=earlier["target"], name=row["name"], **inc)
            for row in earlier["runs"] for inc in row["loss_increases"] if inc["substantial"])
    numeric_pass = (not failures and not increases and not result["provenance_errors"] and len(tested) == 36)
    result["numerical_gates"] = dict(passed=numeric_pass, threshold=.002,
        expected_control_condition_count=36, control_condition_count=len(tested),
        failed_control_count=len(failures), failures=failures,
        substantial_loss_increases=increases, previous_stage_count=len(previous),
        maximum_witness=max(tested, key=lambda row: row["maximum"]) if tested else None,
        stage_pass=all(row["maximum"] <= .002 for row in result["numerical_controls"]
                       if row["observable"] in ("loss", "G", "DeltaG")),
        quadrature_blocks_computed_settling=False)
    if not numeric_pass:
        result["stop_recommended"] = "numerically_unresolved"
    elif result["settling"]["eligible"] and result["settling"]["passed"]:
        result["stop_recommended"] = "settled"
    result["counts"] = dict(runs=len(runs), loss_curves=len(result["loss_curves"]),
        gram_error_curves=len(result["comparisons"]), scalar_error_curves=len(result["scalar_comparisons"]),
        numerical_control_curves=len(result["numerical_controls"]),
        quadrature_curves=len(result["quadrature_comparisons"]),
        settling_conditions=result["settling"]["condition_count"])
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--target", type=int, required=True, choices=STAGES)
    args = parser.parse_args()
    print(json.dumps(analyse_stage(args.output, args.target), indent=2, allow_nan=False))
