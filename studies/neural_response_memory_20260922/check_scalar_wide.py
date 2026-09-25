"""Independent algebraic and saved-data audit of the width-2048 campaign.

No dense or scalar research trajectory is integrated by this checker.
Small initializer identity tests use CPU algebra; GPU training is producer-owned.
"""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from check_scalar_long_time import (Audit, NAMES, digest, load_npz,
                                    independent_recenter, split_state,
                                    frozen_reference, scalar_rms, check_spatial)


def array_hash(*values):
    checksum = hashlib.sha256()
    for value in values:
        value = np.asarray(value)
        checksum.update(str(value.shape).encode())
        checksum.update(str(value.dtype).encode())
        checksum.update(value.tobytes(order="C"))
    return checksum.hexdigest()


def deterministic(audit):
    import scalar_aggregate_engine as legacy
    import scalar_circle_probe_engine as old_probe
    import scalar_wide_initialization as new

    rng = np.random.default_rng(294175)
    train = rng.normal(size=(3, 2))
    probes = rng.normal(size=(5, 2))
    for depth in (2, 3):
        for scale in (0., .3, 1.1):
            params = legacy.initialize_network(7, 2, depth=depth, seed=397)
            params = (*params[:-1], params[-1] * 7 * scale)
            source_copies = tuple(value.copy() for value in params)
            expected = old_probe.initialize_probe_coefficients(params, train, probes)
            actual = new.initialize_probe_coefficients(params, train, probes, batch_size=2)
            alternative = new.initialize_probe_coefficients(params, train, probes, batch_size=5)
            expected_train = legacy.initialize_coefficients(params, train)
            actual_train = new.initialize_coefficients(params, train, batch_size=1)
            prefix = f"initializer depth{depth} readout{scale}"
            for name in NAMES:
                magnitude = float(np.max(np.abs(expected[name])))
                audit.close(prefix + " legacy rectangular " + name, actual[name], expected[name],
                            atol=1e-11 + 1e-9 * magnitude, rtol=0)
                audit.close(prefix + " batch partition " + name, actual[name], alternative[name],
                            atol=1e-11, rtol=1e-10)
                audit.close(prefix + " legacy training " + name, actual_train[name], expected_train[name],
                            atol=1e-11, rtol=1e-9)
            for index, value in enumerate(params):
                audit.close(prefix + f" unchanged parameter block{index}", value, source_copies[index], atol=0, rtol=0)
            if scale == 0:
                audit.close(prefix + " zero-readout C", actual["C"], 0, atol=0, rtol=0)
                audit.check(prefix + " nonzero zero-readout Q", np.max(abs(actual["Q"])) > 1e-10)
            else:
                audit.check(prefix + " ordered Q stress", np.max(abs(expected["Q"] - expected["Q"].swapaxes(-1, -2))) > 1e-9)

    # Algebraic adapter checks stay on CPU and integrate no research trajectory.
    import torch
    from scalar_wide_dense import CanonicalDenseEngine
    from deep_circle_run import heun_trial, heun_interpolant

    torch.set_num_threads(1)
    params = legacy.initialize_network(6, 2, depth=3, seed=913)
    params = (*params[:-1], params[-1] + np.linspace(-.9, .4, 6))
    labels = np.array([1., -.7, .2])
    engine = CanonicalDenseEngine(params, train, labels, device="cpu")
    state = engine.initial_state()
    audit.check("dense adapter exact initialized arrays", array_hash(*params)
                == array_hash(*(value.numpy() for value in state.tensors())))
    audit.close("dense adapter predictions against NumPy", engine.predict(state, probes).numpy(),
                old_probe.forward_only(params, probes), atol=1e-13, rtol=1e-12)
    expected_first = legacy.network_rhs(params, train, labels)
    first, second, euler, candidate = heun_trial(engine, state, .013)
    expected_euler = tuple(value + .013 * velocity for value, velocity in zip(params, expected_first))
    expected_second = legacy.network_rhs(expected_euler, train, labels)
    for block, (one, two, predicted, actual) in enumerate(zip(first.tensors(), second.tensors(), euler.tensors(), candidate.tensors())):
        audit.close(f"dense adapter RHS block{block}", one.numpy(), expected_first[block], atol=1e-13, rtol=1e-12)
        audit.close(f"dense adapter second stage block{block}", two.numpy(), expected_second[block], atol=1e-13, rtol=1e-12)
        audit.close(f"dense adapter Euler block{block}", predicted.numpy(), expected_euler[block], atol=1e-13, rtol=1e-12)
        expected_heun = params[block] + .013 / 2 * (expected_first[block] + expected_second[block])
        audit.close(f"dense adapter Heun block{block}", actual.numpy(), expected_heun, atol=1e-13, rtol=1e-12)
    fraction = .371
    interior = heun_interpolant(state, first, second, .013, fraction)
    for block, actual in enumerate(interior.tensors()):
        expected = params[block] + .013 * (fraction - fraction ** 2 / 2) * expected_first[block]
        expected = expected + .013 * fraction ** 2 / 2 * expected_second[block]
        audit.close(f"dense adapter quadratic interpolant block{block}", actual.numpy(), expected, atol=1e-13, rtol=1e-12)


def check_scalar_archive(audit, run, initial, probe):
    """Replay every passive segment independently; M may be four or eight."""
    record = json.loads((run / "result.json").read_text())
    arrays = load_npz(run / "trajectory.npz")
    prefix = run.parent.name + "/" + run.name
    m, count = len(initial["labels"]), len(probe["angles"])
    training_size = sum(m ** degree for degree in (1, 2, 3))
    expected_training = np.concatenate([initial[name].reshape(-1) for name in NAMES[:3]])
    anchors = {name: probe[name] for name in NAMES}
    audit.check(prefix + ": fresh time-zero origin", record["from_zero"] and arrays["times"][0] == 0)
    audit.check(prefix + ": finite saved trajectory", all(np.isfinite(value).all() for value in arrays.values()))
    audit.check(prefix + ": monotone saved times", np.all(np.diff(arrays["times"]) > 0))
    audit.check(prefix + ": scalar physical cap", float(arrays["time"]) <= 1e9)
    maximum_gap = scalar_rms(anchors["f"][-m:] - initial["f"])
    milestones = json.loads((run / "milestones.json").read_text())
    for segment, local_state in enumerate(arrays["segment_states"]):
        tag = prefix + f": segment{segment}"
        audit.close(tag + " original training anchor", arrays["segment_training"][segment], expected_training, atol=0, rtol=0)
        for index in np.flatnonzero(arrays["milestone_segments"] == segment):
            fields = split_state(arrays["milestone_states"][index], m)
            prediction = independent_recenter(anchors, fields)["f"]
            residual = fields["f"] - initial["labels"]
            kernel = fields["Theta"]
            checkpoint = milestones[index]
            audit.close(prefix + f": milestone{index} loss", checkpoint["loss"], np.mean(residual ** 2), atol=1e-12)
            audit.close(prefix + f": milestone{index} rate", checkpoint["effective_rate"], residual @ kernel @ residual / (residual @ residual), atol=2e-11)
            audit.close(prefix + f": milestone{index} circle", arrays["milestone_grids"][index], prediction[:count], atol=3e-7, rtol=2e-12)
        fields = split_state(local_state, m)
        anchors = independent_recenter(anchors, fields)
        maximum_gap = max(maximum_gap, scalar_rms(anchors["f"][-m:] - fields["f"]))
        expected_training = local_state[:training_size]
        if segment < len(arrays["segment_states"]) - 1:
            boundary = max(np.max(abs(fields["z"])) / 64,
                           np.max(abs(fields["I"])) / 64 ** 2,
                           np.max(abs(fields["J"])) / 64 ** 3)
            audit.close(tag + " recenter event", boundary, 1., atol=2e-9, rtol=0)
    saved_passive = load_npz(run / "passive_endpoint.npz")
    for name in NAMES:
        audit.close(prefix + ": passive replay " + name, saved_passive[name], anchors[name], atol=3e-7, rtol=2e-12)
    audit.close(prefix + ": unchanged original Q", saved_passive["Q"], probe["Q"], atol=0, rtol=0)
    audit.close(prefix + ": final training state", arrays["state"][:training_size], expected_training, atol=0, rtol=0)
    audit.close(prefix + ": zero final local integrals", arrays["state"][training_size:], 0, atol=0, rtol=0)
    audit.close(prefix + ": grid replay", arrays["grid"], anchors["f"][:count], atol=3e-7, rtol=2e-12)
    audit.close(prefix + ": off-grid replay", arrays["off_grid"], anchors["f"][count:count + 32], atol=3e-7, rtol=2e-12)
    audit.close(prefix + ": peak training-probe gap", record["training_probe_gap"], maximum_gap, atol=3e-7, rtol=1e-8)
    final_loss = float(np.mean((arrays["train_f"] - initial["labels"]) ** 2))
    audit.close(prefix + ": final loss", record["loss"], final_loss, atol=1e-12)
    audit.close(prefix + ": final time", record["time"], arrays["time"], atol=0, rtol=0)
    if record["status"] == "fitted":
        audit.close(prefix + ": fitting event", final_loss, 1e-6, atol=1e-12, rtol=0)
        audit.check(prefix + ": first saved crossing", np.all(arrays["losses"][:-1] > 1e-6))
    return arrays, record


def check_dense_archive(audit, run, initial, probe, initialization, initial_features=None):
    record = json.loads((run / "result.json").read_text())
    config = json.loads((run / "config.json").read_text())
    arrays = load_npz(run / "trajectory.npz")
    prefix = run.parent.name + "/" + run.name
    width = int(initialization["width"])
    audit.check(prefix + ": actual width 2048", record["width"] == config["width"] == width == 2048)
    audit.check(prefix + ": GPU-only research trajectory", record["device"].startswith("cuda:") and config["device"].startswith("cuda"))
    audit.check(prefix + ": float64 and deterministic execution", record["dtype"] == "float64"
                and record["deterministic_algorithms"] and not record["tf32"])
    audit.check(prefix + ": identical initialized parameters", record["initialization_hash"] == initialization["initialization_hash"])
    audit.check(prefix + ": trajectory hash", digest(run / "trajectory.npz") == record["trajectory_sha256"])
    audit.check(prefix + ": config hash", digest(run / "config.json") == record["effective_config_sha256"])
    audit.check(prefix + ": canonical dense solver controls", config["initial_step"] == .05
                and config["max_step"] == 2. and config["target_loss"] == 1e-6
                and config["atol"] == config["rtol"] / 100)
    audit.close(prefix + ": canonical training inputs", arrays["train_inputs"], initial["inputs"], atol=0, rtol=0)
    audit.close(prefix + ": canonical labels", arrays["train_labels"], initial["labels"], atol=0, rtol=0)
    audit.close(prefix + ": grid angles", arrays["grid_angles"], probe["angles"], atol=0, rtol=0)
    audit.close(prefix + ": off-grid angles", arrays["off_grid_angles"], probe["off_angles"], atol=0, rtol=0)
    audit.check(prefix + ": all saved numeric arrays finite", all(np.isfinite(value).all() for value in arrays.values()))
    params = tuple(arrays[name] for name in ("w", "W2", "W3", "c"))
    audit.check(prefix + ": full dense parameter shapes", tuple(value.shape for value in params)
                == ((width, 2), (width, width), (width, width), (width,)))
    audit.close(prefix + ": flat full dense state", arrays["flatstate"],
                np.concatenate([value.reshape(-1) for value in params]), atol=0, rtol=0)
    # Independent NumPy endpoint evaluation, without training or GPU work.
    values = probe["probe_inputs"].T
    final_features = []
    for matrix in params[:-1]:
        values = np.tanh(matrix @ values)
        final_features.append(values[:, -len(initial["labels"]):].copy())
    prediction = params[-1] @ values / width
    ngrid, m = len(probe["angles"]), len(initial["labels"])
    audit.close(prefix + ": independent dense grid", arrays["grid"], prediction[:ngrid], atol=2e-10, rtol=2e-11)
    audit.close(prefix + ": independent dense off-grid", arrays["off_grid"], prediction[ngrid:ngrid + 32], atol=2e-10, rtol=2e-11)
    audit.close(prefix + ": independent dense training outputs", arrays["train_f"], prediction[-m:], atol=2e-11, rtol=2e-11)
    measured_loss = np.mean((prediction[-m:] - initial["labels"]) ** 2)
    audit.close(prefix + ": independently evaluated training loss", record["training_mse"], measured_loss, atol=2e-13, rtol=2e-10)
    audit.check(prefix + ": accepted step error bounds", np.all(arrays["local_error_ratios"] <= 1)
                and np.all(arrays["local_error_ratios"] >= 0))
    audit.check(prefix + ": accepted trace sizes", len(arrays["times"]) == record["accepted"] + 1
                == len(arrays["losses"]) == len(arrays["accepted_steps"]) + 1)
    audit.close(prefix + ": accepted time increments", np.diff(arrays["times"]), arrays["accepted_steps"], atol=2e-12, rtol=2e-12)
    audit.check(prefix + ": positive steps within ceiling", np.all(arrays["accepted_steps"] > 0) and np.max(arrays["accepted_steps"], initial=0) <= 2.)
    audit.check(prefix + ": physical and step caps", record["time"] <= 2048 and record["accepted"] <= 100000)
    audit.check(prefix + ": resource caps", record["peak_cuda_allocated_bytes"] < 12 * 1024 ** 3
                and record["peak_process_rss_bytes"] < 8 * 1024 ** 3)
    audit.close(prefix + ": initial training loss", arrays["losses"][0], np.mean((initial["f"] - initial["labels"]) ** 2), atol=2e-12)
    if record["status"] == "fitted":
        bracket = record["crossing_bracket"]
        audit.check(prefix + ": downward event bracket", bracket["left_loss"] > 1e-6 >= bracket["right_loss"]
                    and bracket["left_time"] <= record["time"] <= bracket["right_time"])
        audit.close(prefix + ": fitted endpoint", measured_loss, 1e-6, atol=2e-12, rtol=0)
        audit.check(prefix + ": first saved downward event", np.all(arrays["losses"][:-1] > 1e-6))
    if initial_features is not None:
        record["audit_feature_movement"] = []
        for layer, (before, after) in enumerate(zip(initial_features, final_features), 1):
            magnitude = scalar_rms(before)
            movement = scalar_rms(after - before)
            record["audit_feature_movement"].append({"layer": layer, "initial_rms": magnitude,
                                                     "movement_rms": movement,
                                                     "relative_movement": movement / magnitude})
    return {key: arrays[key] for key in ("grid", "off_grid", "train_f", "time", "times", "losses")}, record


def comparison_reference(first, second, first_record, second_record, discrepancy):
    count = min(len(first["grid"]), len(second["grid"]))
    change = scalar_rms(first["grid"][::len(first["grid"]) // count]
                        - second["grid"][::len(second["grid"]) // count])
    delta = abs(float(first["time"] - second["time"])) / max(1., float(second["time"]))
    probe_gap = max(first_record.get("training_probe_gap", 0), second_record.get("training_probe_gap", 0))
    fitted = first_record["status"] == second_record["status"] == "fitted"
    return {"numerical_change": change, "time_relative_change": delta, "training_probe_gap": probe_gap,
            "passed": bool(fitted and change <= .002 and change <= .1 * max(discrepancy, 1e-6)
                           and delta <= .001 and probe_gap <= 1e-4)}


def saved_data(audit, campaign, source, reproduction=None, reproduction_source=None):
    import scalar_aggregate_engine as legacy

    folders = sorted(path for path in source.iterdir() if path.is_dir() and (path / "initialization.json").exists())
    cases = json.loads((Path(__file__).resolve().parent / "deep_circle_cases.json").read_text())
    audit.check("four declared initializations", len(folders) == 4)
    observed_configurations = set()
    feature_movements = []
    for folder in folders:
        name = folder.name
        target = campaign / name
        initialization = json.loads((folder / "initialization.json").read_text())
        config = json.loads((folder / "configuration.json").read_text())
        initial, probe = load_npz(folder / "initial_coefficients.npz"), load_npz(folder / "probe_coefficients.npz")
        m, ngrid = len(initial["labels"]), len(probe["angles"])
        observed_configurations.add((config["case"], config["seed"]))
        case = cases[config["case"]]
        angles = np.deg2rad(case["angles_degrees"])
        audit.close(name + ": literal original training inputs", initial["inputs"],
                    np.column_stack((np.cos(angles), np.sin(angles))), atol=0, rtol=0)
        audit.close(name + ": literal original labels", initial["labels"], case["labels"], atol=0, rtol=0)
        audit.check(name + ": width and architecture", config["width"] == 2048 and config["hidden_layers"] == 3)
        audit.check(name + ": initializer memory/time caps", initialization["peak_rss_bytes"] < 8 * 1024 ** 3 and initialization["seconds"] <= 601)
        params = legacy.initialize_network(2048, 2, depth=3, seed=config["seed"])
        audit.check(name + ": exact NumPy initialized parameter hash", array_hash(*params) == initialization["initialization_hash"])
        base = legacy.network_fields(params, initial["inputs"])
        initial_features = tuple(value.copy() for value in base["h"])
        audit.close(name + ": independent initialized f", initial["f"], base["f"], atol=1e-12, rtol=1e-10)
        audit.close(name + ": independent initialized kernel", initial["Theta"], base["Theta"], atol=1e-12, rtol=1e-10)
        del params, base
        for source_name, expected_hash in initialization["sources"].items():
            audit.check(name + ": frozen source " + source_name, digest(folder / "sources" / source_name) == expected_hash)
        for key in NAMES:
            audit.check(name + ": coefficient hash " + key, array_hash(probe[key]) == initialization["coefficient_hashes"][key])
            audit.close(name + ": training-probe initialized identity " + key, initial[key], probe[key][-m:], atol=0, rtol=0)
            audit.check(name + ": finite initialized coefficient " + key, np.isfinite(probe[key]).all())
        audit.check(name + ": exact stored kernel symmetry", np.array_equal(initial["Theta"], initial["Theta"].T))
        first_hard = config["case"] == "quadrant_alternating" and config["seed"] == 20260920
        if first_hard:
            oracle = load_npz(folder / "initialization_oracle.npz")
            points = np.vstack((np.array([[1., 0.], [np.cos(np.pi / 7), np.sin(np.pi / 7)]]), initial["inputs"][:2]))
            audit.close(name + ": predeclared legacy comparison points", oracle["points"], points, atol=0, rtol=0)
            for key in NAMES:
                expected, actual = oracle["reference_" + key], oracle["optimized_" + key]
                bound = 1e-11 + 1e-9 * np.max(abs(expected))
                difference = float(np.max(abs(actual - expected)))
                audit.check(name + ": width2048 legacy initializer " + key, difference <= bound)
                audit.close(name + ": legacy comparison metric " + key, initialization["initialization_oracle"][key]["maximum_difference"], difference)
        summary = json.loads((target / "summary.json").read_text())
        families = {}
        for model in ("dense", "order4"):
            paths = sorted((path for path in target.glob(model + "_resolution*") if path.is_dir()),
                           key=lambda p: int(p.name.split("resolution")[-1]))
            families[model] = []
            for run in paths:
                if not (run / "result.json").exists():
                    continue
                if model == "dense":
                    data, record = check_dense_archive(audit, run, initial, probe, initialization, initial_features)
                else:
                    data, record = check_scalar_archive(audit, run, initial, probe)
                level = int(run.name.split("resolution")[-1])
                tolerance = ((1.25e-5, 3.125e-6, 7.8125e-7) if model == "dense"
                             else (1e-7, 1e-9, 1e-11))[level]
                audit.check(name + ": declared " + run.name + " tolerance", record["rtol"] == tolerance
                            and record["atol"] == tolerance / 100)
                families[model].append((data, record))
            audit.check(name + ": both primary " + model + " resolutions", len(families[model]) >= 2)
        dense, scalar = families["dense"][-1][0], families["order4"][-1][0]
        feature_movements.append({"configuration": name, "dense_time": float(dense["time"]),
                                  "layers": families["dense"][-1][1]["audit_feature_movement"]})
        discrepancy = scalar_rms(scalar["grid"] - dense["grid"])
        all_gates = True
        for model, runs in families.items():
            expected = comparison_reference(runs[-2][0], runs[-1][0], runs[-2][1], runs[-1][1], discrepancy)
            all_gates = all_gates and expected["passed"]
            for key in ("numerical_change", "time_relative_change", "training_probe_gap"):
                audit.close(name + ": " + model + " gate " + key, summary["gates"][model][key], expected[key], atol=2e-11)
            audit.check(name + ": " + model + " gate scoring", summary["gates"][model]["passed"] == expected["passed"])
            if len(runs) == 3:
                trigger = comparison_reference(runs[0][0], runs[1][0], runs[0][1], runs[1][1], discrepancy)
                audit.check(name + ": declared conditional refinement trigger " + model, not trigger["passed"])
        check_spatial(audit, name + "/order4", scalar, probe, dense, summary["spatial"], target / "order4_fourier.npz")
        all_gates = all_gates and summary["spatial"]["quadrature_pass"] and summary["spatial"]["fourier_pass"]
        if first_hard:
            audit.check(name + ": independent reproduction present", reproduction is not None)
            if reproduction is not None:
                repeated_source = reproduction_source if reproduction_source else reproduction / "source"
                repeat_initial = load_npz(repeated_source / "initial_coefficients.npz")
                repeat_probe = load_npz(repeated_source / "probe_coefficients.npz")
                for key in NAMES:
                    audit.close(name + ": independently repeated initializer " + key, repeat_initial[key], initial[key], atol=0, rtol=0)
                    audit.close(name + ": independently repeated passive initializer " + key, repeat_probe[key], probe[key], atol=0, rtol=0)
                repeat_metadata = json.loads((repeated_source / "initialization.json").read_text())
                for model in ("dense", "order4"):
                    run = reproduction / model
                    if model == "dense":
                        other, record = check_dense_archive(audit, run, repeat_initial, repeat_probe, repeat_metadata,
                                                           initial_features)
                    else:
                        other, record = check_scalar_archive(audit, run, repeat_initial, repeat_probe)
                    expected = comparison_reference(families[model][-1][0], other, families[model][-1][1], record, discrepancy)
                    all_gates = all_gates and expected["passed"]
                    for key in ("numerical_change", "time_relative_change", "training_probe_gap"):
                        audit.close(name + ": reproduced " + model + " " + key, summary["reproduction"][model][key], expected[key], atol=2e-11)
                    audit.check(name + ": reproduction gate " + model, summary["reproduction"][model]["passed"] == expected["passed"])
        fitted = all(runs[-1][1]["status"] == "fitted" for runs in families.values())
        verdict = ("no_matched_endpoint" if not fitted else "reproduction_pending" if first_hard and reproduction is None
                   else "numerically_inconclusive" if not all_gates else "agreement" if discrepancy <= .1
                   else "adverse" if discrepancy > .2 else "inconclusive")
        audit.check(name + ": independent complete verdict", summary["verdict"] == verdict)
        baseline = load_npz(target / "order2_spectral.npz")
        reference = frozen_reference(initial, probe, float(baseline["time"]))
        audit.close(name + ": frozen-kernel training outputs", baseline["train_f"], reference["train_f"], atol=2e-11)
        audit.close(name + ": frozen-kernel integrated residual", baseline["z"], reference["z"], atol=3e-7)
        audit.close(name + ": frozen-kernel integral identity", initial["f"] + initial["Theta"] @ baseline["z"], reference["train_f"], atol=3e-8)
        audit.close(name + ": frozen-kernel circle readout", baseline["grid"], reference["probe"][:ngrid], atol=3e-8)
        audit.close(name + ": frozen-kernel off-grid readout", baseline["off_grid"], reference["probe"][ngrid:ngrid + 32], atol=3e-8)
        audit.close(name + ": frozen-kernel endpoint loss", summary["order2"]["loss"], reference["loss"], atol=1e-12)
        check_spatial(audit, name + "/order2", baseline, probe, dense, summary["order2"]["spatial"], target / "order2_fourier.npz")
    audit.check("exact preregistered case/seed set", observed_configurations
                == {(case, seed) for case in ("equal_mixed_odd", "quadrant_alternating") for seed in (20260920, 20260927)})
    audit.feature_movements = feature_movements


def budget_audit(audit, campaign, source, reproduction, reproduction_source, pilot):
    """Disjoint recorded work; sum worker durations conservatively despite overlap."""
    primary = {}
    launched_initializations = set()
    for lane in ("dense", "scalar"):
        receipt = json.loads((campaign / (lane + "_launch.json")).read_text())
        durations = sum(item["seconds"] for item in receipt["records"])
        audit.close("budget " + lane + " launch receipt sum", receipt["active_seconds"], durations, atol=1e-10)
        audit.check("budget " + lane + " successful subprocesses", all(item["exit_code"] == 0 for item in receipt["records"]))
        primary[lane + "_launches"] = float(receipt["active_seconds"])
        for item in receipt["records"]:
            command = item["command"]
            if "prepare" in command:
                launched_initializations.add(Path(command[command.index("--output") + 1]).resolve())
    other_initializations = []
    for folder in sorted(source.iterdir()):
        path = folder / "initialization.json"
        if path.exists() and folder.resolve() not in launched_initializations:
            record = json.loads(path.read_text())
            other_initializations.append(record["seconds"])
    primary["initializations_outside_launch_receipts"] = float(sum(other_initializations))
    pilot_record = json.loads((pilot / "result.json").read_text())
    audit.check("pilot protocol identity", pilot_record["width"] == 2048 and pilot_record["case"] == "quadrant_alternating"
                and pilot_record["seed"] == 20260920 and pilot_record["device"].startswith("cuda:")
                and pilot_record["rtol"] == 1.25e-5 and pilot_record["phase"] == "pilot")
    audit.check("pilot bounded feasibility only", pilot_record["accepted"] == 40
                and pilot_record["max_steps"] == 40 and pilot_record["max_wall_seconds"] == 90
                and pilot_record["status"] == "max_steps" and not pilot_record["scientific_validity"])
    audit.check("pilot resource bounds", pilot_record["integration_seconds"] < 90
                and pilot_record["peak_cuda_allocated_bytes"] < 12 * 1024 ** 3
                and pilot_record["peak_process_rss_bytes"] < 8 * 1024 ** 3)
    audit.check("pilot saved trajectory hash", digest(pilot / "trajectory.npz") == pilot_record["trajectory_sha256"])
    primary["pilot_work"] = pilot_record["total_work_seconds"]
    repeat_initial = json.loads((reproduction_source / "initialization.json").read_text())
    repeat_dense = json.loads((reproduction / "dense" / "result.json").read_text())
    repeat_scalar = json.loads((reproduction / "order4" / "result.json").read_text())
    primary["reproduction_initialization"] = repeat_initial["seconds"]
    primary["reproduction_dense_work"] = repeat_dense["total_work_seconds"]
    primary["reproduction_scalar_work"] = repeat_scalar["seconds"]
    audit.check("reproduction per-run limits", repeat_initial["seconds"] <= 600
                and repeat_dense["integration_seconds"] <= 900 and repeat_scalar["seconds"] <= 240)
    subtotal = sum(primary.values())
    audit.check("recorded disjoint active work within 7200 seconds", subtotal < 7200)
    audit.budget = {"components_seconds": primary, "recorded_active_work_subtotal_seconds": subtotal,
                    "note": "Primary launch receipts include subprocess overhead and three initializations. Other components use in-process timings; their process startup and separate scoring are not included. Simultaneous lanes are added, not treated as elapsed campaign wall time."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--campaign", type=Path)
    parser.add_argument("--reproduction", type=Path)
    parser.add_argument("--reproduction-source", type=Path)
    parser.add_argument("--pilot", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit = Audit()
    deterministic(audit)
    if args.campaign:
        saved_data(audit, args.campaign.resolve(), args.source.resolve(),
                   args.reproduction.resolve() if args.reproduction else None,
                   args.reproduction_source.resolve() if args.reproduction_source else None)
        if args.pilot:
            budget_audit(audit, args.campaign.resolve(), args.source.resolve(), args.reproduction.resolve(),
                         args.reproduction_source.resolve(), args.pilot.resolve())
    result = audit.result()
    if hasattr(audit, "feature_movements"):
        result["dense_feature_movements"] = audit.feature_movements
    if hasattr(audit, "budget"):
        result["budget_accounting"] = audit.budget
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("status", "checks", "failures")}, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
