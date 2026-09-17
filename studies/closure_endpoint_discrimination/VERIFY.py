"""Read-only integrity and numerical checks for this study's saved campaign.

No training is performed. Default checks use hashes, fixtures, checkpoints'
wrapper histories, and independently recomputed trajectory identities. Explicit
--replay main/all additionally reloads endpoint parameters and predicts them.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / "data/generated/closure_endpoint_discrimination"
sys.path.insert(0, str(HERE))
from ANALYZE import load_inputs, validate_job


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def encoded_config(config):
    return hashlib.sha256(json.dumps(config, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def owned(path, base=None):
    path = Path(path)
    if not path.is_absolute():
        path = (base or ROOT) / path
    path = path.resolve()
    if not path.is_relative_to(GENERATED.resolve()):
        raise ValueError(f"path outside this study's generated products: {path}")
    return path


def read_json(path):
    return json.loads(Path(path).read_text())


def read_npz(path):
    with np.load(path, allow_pickle=False) as source:
        return {key: source[key].copy() for key in source.files}


def require(condition, message, failures):
    if not condition:
        failures.append(message)


def check_hash(path, expected, failures, label):
    try:
        actual = sha256(path)
        require(actual == expected, f"{label}: hash mismatch", failures)
        return dict(path=str(path), expected=expected, actual=actual, passed=actual == expected)
    except Exception as error:
        failures.append(f"{label}: {error}")
        return dict(path=str(path), expected=expected, passed=False, error=str(error))


def campaign_for(manifest_path, manifest):
    if "sources_sha256" in manifest:
        return manifest_path, manifest
    if "campaign_manifest" in manifest:
        path = owned(manifest["campaign_manifest"], manifest_path.parent)
        return path, read_json(path)
    for parent in manifest_path.parents:
        if not parent.is_relative_to(GENERATED):
            break
        candidate = parent / "manifest.json"
        if candidate.exists():
            content = read_json(candidate)
            if "sources_sha256" in content:
                return candidate, content
    raise ValueError("no frozen campaign manifest found")


def input_geometry(path, stage):
    inputs = load_inputs(path)
    centers = np.array([15, 35, 50, 75, 100, 170], dtype=np.float64)
    offsets = np.array([-4, -4 / 3, 4 / 3, 4])
    theta = np.deg2rad((centers[:, None] + offsets).reshape(-1))
    a, b, c = theta - np.deg2rad(17), theta + np.deg2rad(11), theta - np.deg2rad(23)
    mixed = .20 * np.cos(3*a) + .25 * np.sin(5*a) + .30 * np.cos(7*b) + .25 * np.sin(11*c)
    targets = [np.cos(a), np.cos(3*a), .60*np.cos(3*a)+.40*np.sin(5*a),
               .40*np.cos(3*a)+.35*np.sin(5*a)+.25*np.cos(7*b), mixed, np.sign(mixed)]
    errors = {"training_angles": float(np.max(np.abs(inputs["train_theta"] - theta))),
              "training_labels": float(np.max(np.abs(inputs["labels"] - targets[stage])))}
    for key in ("train", "circle", "dense"):
        directions = inputs[f"{key}_u"]
        angles = inputs[f"{key}_theta"]
        errors[key + "_direction"] = float(np.max(np.abs(directions - np.column_stack((np.cos(angles), np.sin(angles))))))
    return dict(passed=max(errors.values()) <= 1e-12, errors=errors)


def equation_evidence(checks):
    errors = {key: value for key, value in checks.items() if key not in ("passed", "device")}
    return checks.get("passed") is True and bool(errors) and all(
        isinstance(value, (int, float)) and np.isfinite(value) and 0 <= value <= 1e-10
        for value in errors.values())


def fixtures(campaign_path, campaign, overrides=None):
    paths = dict(network=GENERATED / "checks_network_001/final/check.json",
                 closure_wrapper=GENERATED / "closure_wrapper_check_66kh5obr/check_result.json",
                 closure_cpu=GENERATED / "closure_wrapper_check_66kh5obr/direct/record.json",
                 closure_gpu=campaign_path.parent / "stage_00/screen/cl_N3_screen/record.json")
    paths.update(overrides or {})
    failures, result = [], {}
    for kind, path in paths.items():
        try:
            path = owned(path, campaign_path.parent)
            value = read_json(path)
            passed = True
            if kind == "network":
                passed = (value.get("passed") is True and value.get("checkpoint_state_exact") is True
                          and value.get("initialization_hashes_match") is True
                          and value.get("tf32_disabled") is True
                          and value.get("source_hash") == campaign["sources_sha256"][str(HERE.relative_to(ROOT) / "NETWORK.py")]
                          and all(np.isfinite(error) and 0 <= error <= 1e-10 for error in value["errors"].values())
                          and value["errors"].get("serialized_history_restart") == 0)
            elif kind == "closure_wrapper":
                passed = value.get("passed") is True and value.get("resumed_state_and_history_bit_exact") is True
                direct, resumed = path.parent / "direct", path.parent / "resumed"
                for name in ("trajectories.npz", "final_restart.json", "final_wrapper.npz"):
                    passed = passed and sha256(direct / name) == sha256(resumed / name)
            else:
                checks = value.get("checks", {})
                expected_device = "cpu" if kind == "closure_cpu" else "cuda"
                passed = (value.get("status") == "complete" and equation_evidence(checks.get("equations", {}))
                          and str(checks["equations"].get("device", "")).startswith(expected_device)
                          and checks.get("restart_arrays_exact") is True
                          and 0 <= checks.get("dense_replay_max_error", float("inf")) <= 1e-10
                          and value.get("hashes", {}).get("runner") == campaign["sources_sha256"][str(HERE.relative_to(ROOT) / "CLOSURE.py")])
            require(passed, f"fixture {kind} failed", failures)
            result[kind] = dict(path=str(path), sha256=sha256(path), passed=bool(passed), evidence=value)
        except Exception as error:
            failures.append(f"fixture {kind}: {error}")
            result[kind] = dict(path=str(path), passed=False, error=str(error))
    return dict(passed=not failures, failures=failures, results=result)


def verify_job(name, directory, inputs_path, inputs, campaign, replay, device):
    failures, hashes = [], {}
    directory = owned(directory)
    record_path = directory / "record.json"
    record = read_json(record_path)
    config, checks = record["config"], record.get("checks", {})
    arrays = read_npz(directory / "trajectories.npz")
    require(record.get("status") == "complete", "worker status is not complete", failures)
    require(owned(config["inputs_path"]) == inputs_path, "configuration inputs differ from manifest", failures)
    require(config.get("h") in (.02, .01), "unplanned step size", failures)
    require(config.get("obs_dt") == 5 and 100 <= config.get("t_min", 0) <= config.get("t_max", 0) <= 1600,
            "unplanned observation grid or horizon", failures)
    validation = validate_job(arrays, record, inputs)
    require(validation["passed"], "saved trajectory numerical identities failed", failures)
    require(abs(float(arrays["times"][0])) < 1e-10, "history does not begin at time zero", failures)
    require(np.allclose(np.diff(arrays["times"]), 5, atol=1e-8, rtol=0), "history is not on the declared five-unit grid", failures)
    kind = config.get("kind")
    if kind == "network":
        expected_runner = campaign["sources_sha256"][str(HERE.relative_to(ROOT) / "NETWORK.py")]
        require(record.get("source_hash") == expected_runner, "network source hash differs from freeze", failures)
        require(record.get("inputs_hash") == sha256(inputs_path), "network input hash differs", failures)
        require(record.get("config_hash") == encoded_config(config), "network configuration hash differs", failures)
        require(config.get("width") in (4096, 8192) and config.get("seed") in (11, 29, 47), "unplanned network width or seed", failures)
        require(config.get("dtype") in ("float32", "float64"), "unplanned network precision", failures)
        require(config.get("dtype") != "float64" or config.get("width") == 4096, "float64 control exceeds declared width", failures)
        for flag in ("all_finite", "unit_uniform_probabilities", "checkpoint_state_exact", "tf32_disabled"):
            require(checks.get(flag) is True, f"network check missing or false: {flag}", failures)
        require(checks.get("checkpoint_prediction_replay_error") == 0, "network checkpoint replay is not exact", failures)
        for key in ("gram_symmetry_error", "rms_gram_error", "mse_recompute_error", "oddness_error", "max_loss_increase"):
            require(np.isfinite(checks.get(key, float("inf"))) and 0 <= checks.get(key, float("inf")) <= 1e-5,
                    f"network raw check failed or missing: {key}", failures)
        for name_out in ("state.pt", "trajectories.npz"):
            hashes[name_out] = check_hash(directory / name_out, record.get("output_hashes", {}).get(name_out), failures, name_out)
        initialization_hashes = record.get("initialization_hashes", {})
        require(set(initialization_hashes) == {"a", "b", "c"} and all(isinstance(v, str) and len(v) == 64 for v in initialization_hashes.values()),
                "missing pre-cast PCG64 block hashes", failures)
        if record.get("resume_from"):
            previous = owned(record["resume_from"])
            previous_record = read_json(previous.parent / "record.json")
            if previous.exists():
                hashes["resume_state"] = check_hash(previous, previous_record["output_hashes"]["state.pt"], failures, "resume state")
            else:
                from RETIRE import historical_evidence
                hashes["resume_state"] = historical_evidence(previous, previous_record["output_hashes"]["state.pt"])
            require(previous_record["initialization_hashes"] == initialization_hashes, "resume changed initialization hashes", failures)
    elif kind == "closure":
        recorded_hashes = record.get("hashes", {})
        source_paths = dict(runner=HERE / "CLOSURE.py", plan=HERE / "CAMPAIGN_PLAN.md",
                            solver=ROOT / "code/pde/observable_solver.py", initializer=ROOT / "code/pde/observable_initialization.py",
                            words=ROOT / "code/pde/observable_words.py")
        for key, path in source_paths.items():
            expected = campaign["sources_sha256"][str(path.relative_to(ROOT))]
            require(recorded_hashes.get(key) == expected, f"closure consumed {key} differs from freeze", failures)
        config_path = owned(record["config_path"])
        hashes["config"] = check_hash(config_path, recorded_hashes.get("config"), failures, "closure configuration")
        require(read_json(config_path) == config, "record and configuration file disagree", failures)
        require(recorded_hashes.get("inputs") == sha256(inputs_path), "closure input hash differs", failures)
        require(config.get("order") in (1, 3, 5), "unplanned closure order", failures)
        require((config.get("Q"), config.get("P")) in ((2048, 1024), (8192, 4096), (16384, 8192), (32768, 16384)),
                "unplanned closure integration grid", failures)
        require(equation_evidence(checks.get("equations", {})), "closure equation/autograd/Heun evidence failed", failures)
        require(checks.get("restart_arrays_exact") is True, "closure restart arrays are not exact", failures)
        for key in ("dense_replay_max_error", "oddness_max_error", "paired_movement_max_error",
                    "gram_symmetry_max_error", "rms_identity_max_error", "mse_identity_max_error"):
            require(np.isfinite(checks.get(key, float("inf"))) and 0 <= checks.get(key, float("inf")) <= 1e-10,
                    f"closure raw check failed or missing: {key}", failures)
        for name_out in ("trajectories.npz", "final_restart.json", "final_wrapper.npz"):
            hashes[name_out] = check_hash(directory / name_out, recorded_hashes.get(name_out), failures, name_out)
        wrapper = read_npz(directory / "final_wrapper.npz")
        for key in ("times", "predictions", "loss", "grams", "rms", "movement"):
            require(np.array_equal(wrapper[key], arrays[key]), f"wrapper and trajectory disagree: {key}", failures)
        require(json.loads(str(wrapper["config_json"])) == config, "wrapper configuration differs", failures)
        require(str(wrapper["inputs_sha256"]) == sha256(inputs_path), "wrapper input hash differs", failures)
        require(int(wrapper["train_count"]) == len(inputs["labels"]), "wrapper training count differs", failures)
        for key in ("initial_h1", "initial_h2"):
            require(wrapper[key].shape == (config["P"], len(inputs["labels"])) and np.all(np.isfinite(wrapper[key])),
                    f"invalid paired initialization array: {key}", failures)
        if record.get("resume_from"):
            previous = owned(record["resume_from"])
            hashes["resume_state"] = check_hash(previous, recorded_hashes.get("resume_state"), failures, "resume state")
            previous_wrapper = previous.with_name(previous.name.replace("_restart.json", "_wrapper.npz"))
            hashes["resume_wrapper"] = check_hash(previous_wrapper, recorded_hashes.get("resume_wrapper"), failures, "resume wrapper")
    else:
        failures.append("unknown job kind")
    require(np.isfinite(checks.get("gram_min_eigenvalue", float("nan"))) and checks.get("gram_min_eigenvalue", -1) >= -1e-5,
            "recorded Gram positivity check failed or missing", failures)
    replay_result = dict(performed=False, reason="explicit replay deferred")
    if replay:
        replay_result = replay_endpoint(directory, record, inputs, arrays, device)
        require(replay_result["passed"], "independent endpoint replay failed", failures)
    return dict(passed=not failures, failures=failures, directory=str(directory), record_sha256=sha256(record_path),
                kind=kind, config=config, last_time=record.get("last_time"), settled=record.get("settled"),
                initialization_hashes=record.get("initialization_hashes"), hashes=hashes,
                validation=validation, raw_checks=checks, replay=replay_result)


def replay_endpoint(directory, record, inputs, arrays, device):
    """Predict saved parameters using explicit formulas; never take a flow step."""
    began = time.monotonic()
    kind = record["config"]["kind"]
    if kind == "network":
        os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
        import torch
        torch.set_num_threads(1)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        torch.set_float32_matmul_precision("highest")
        torch.use_deterministic_algorithms(True)
        saved = torch.load(directory / "state.pt", map_location="cpu", weights_only=False)
        a, b, c = [saved[key].to(device) for key in ("a", "b", "c")]
        with torch.no_grad():
            u = torch.tensor(inputs["dense_u"].T, dtype=a.dtype, device=device)
            prediction = (c @ torch.tanh(b @ torch.tanh(a @ u)) / c.numel()).cpu().numpy()
        tolerance = 1e-5 if record["config"]["dtype"] == "float32" else 1e-10
        metadata_exact = (saved["config"] == record["config"] and saved["source_hash"] == record["source_hash"]
                          and saved["inputs_hash"] == record["inputs_hash"]
                          and saved["initialization_hashes"] == record["initialization_hashes"]
                          and saved["time"] == record["last_time"])
        del a, b, c, saved
        if str(device).startswith("cuda"):
            torch.cuda.synchronize(device)
            torch.cuda.empty_cache()
    else:
        sys.path.insert(0, str(ROOT / "code"))
        from pde.observable_solver import load_restart
        state, data = load_restart(directory / "final_restart.json")
        values = []
        for begin in range(0, len(inputs["dense_u"]), 128):
            u = inputs["dense_u"][begin:begin + 128]
            h1 = np.tanh(state.w @ u.T)
            coefficients = state.b1.T @ (state.p1[:, None] * h1)
            h2 = np.tanh(state.b2 @ (state.M @ coefficients))
            values.append(state.p2 @ (state.c[:, None] * h2))
        prediction = np.concatenate(values)
        metadata_exact = all(np.array_equal(getattr(data, key), inputs[other]) for key, other in
                             (("inputs", "train_u"), ("labels", "labels"), ("probabilities", "probabilities")))
        tolerance = 1e-10
    error = float(np.max(np.abs(prediction - arrays["dense_predictions"].reshape(-1))))
    return dict(performed=True, passed=bool(metadata_exact and np.isfinite(error) and error <= tolerance),
                max_error=error, tolerance=tolerance, checkpoint_metadata_exact=bool(metadata_exact),
                elapsed_seconds=time.monotonic() - began, device=device if kind == "network" else "cpu")


def verify(manifest_path, replay="none", device="cpu"):
    began = time.monotonic()
    manifest_path = owned(manifest_path)
    manifest = read_json(manifest_path)
    campaign_path, campaign = campaign_for(manifest_path, manifest)
    failures, source_checks, input_checks, jobs = [], {}, {}, {}
    for relative, expected in campaign["sources_sha256"].items():
        path = (ROOT / relative).resolve()
        if not (path.is_relative_to(HERE) or path.is_relative_to(ROOT / "code") or path.is_relative_to(ROOT / "docs")
                or path in (ROOT / "AGENTS.md", ROOT / "RESEARCH_WORKFLOW.md")):
            raise ValueError("frozen manifest points outside allowed input scope")
        source_checks[relative] = check_hash(path, expected, failures, "source " + relative)
    for relative, expected in campaign["inputs_sha256"].items():
        path = owned(relative, campaign_path.parent)
        check = check_hash(path, expected, failures, "input " + relative)
        geometry = input_geometry(path, int(path.parent.name.split("_")[-1]))
        require(geometry["passed"], "input geometry/labels differ: " + relative, failures)
        input_checks[relative] = dict(hash=check, geometry=geometry)
    fixture_result = fixtures(campaign_path, campaign, manifest.get("fixtures"))
    require(fixture_result["passed"], "preflight fixture evidence failed", failures)
    if manifest.get("jobs"):
        inputs_path = owned(manifest["inputs_path"], manifest_path.parent)
        inputs = load_inputs(inputs_path)
        frozen_input_paths = {owned(key, campaign_path.parent) for key in campaign["inputs_sha256"]}
        require(inputs_path in frozen_input_paths, "job input is absent from frozen campaign", failures)
        for name, value in manifest["jobs"].items():
            path = value if isinstance(value, str) else value["path"]
            is_main = str(name).endswith("_main") or str(name) in ("net_n8192_s11", "net_n8192_s29", "net_n8192_s47")
            try:
                jobs[str(name)] = verify_job(str(name), owned(path, manifest_path.parent), inputs_path, inputs,
                                            campaign, replay == "all" or (replay == "main" and is_main), device)
            except Exception as error:
                jobs[str(name)] = dict(passed=False, failures=[repr(error)], directory=str(path))
            require(jobs[str(name)]["passed"], f"job {name} failed verification", failures)
    groups = defaultdict(list)
    for name, job in jobs.items():
        if job.get("kind") == "network":
            config = job["config"]
            groups[(config["stage"], config["width"], config["seed"])].append((name, job))
    initialization_controls = []
    for key, members in groups.items():
        if len(members) > 1:
            same = all(item["initialization_hashes"] == members[0][1]["initialization_hashes"] for _, item in members)
            require(same, f"PCG64 initialization differs within control group {key}", failures)
            initialization_controls.append(dict(stage=key[0], width=key[1], seed=key[2],
                                                names=[name for name, _ in members], passed=same))
    if "pair" in manifest:
        selected = tuple(manifest["pair"])
        require(selected in ((1, 3), (3, 5)), "invalid confirmation pair", failures)
        required = [f"cl_N{n}_main" for n in (1, 3, 5)]
        required += [f"cl_N{n}_{role}" for n in selected for role in ("fine", "half")]
        required += ["net_n8192_s11", "net_n8192_s29", "net_n8192_s47", "net_n4096_s11",
                     "net_n8192_s11_half", "net_n4096_s11_double"]
        require(all(name in jobs for name in required), "confirmation manifest lacks required runs", failures)
        if "common_time" in manifest:
            require(all(abs(job.get("last_time", -1) - manifest["common_time"]) <= 1e-7 for job in jobs.values()),
                    "confirmation endpoints are not at common_time", failures)
    return dict(passed=not failures, failures=failures, manifest=str(manifest_path), manifest_sha256=sha256(manifest_path),
                campaign_manifest=str(campaign_path), campaign_manifest_sha256=sha256(campaign_path),
                verifier_source_sha256=sha256(__file__), sources=source_checks, inputs=input_checks,
                fixtures=fixture_result, jobs=jobs, initialization_controls=initialization_controls,
                independent_replay_mode=replay, elapsed_seconds=time.monotonic() - began,
                retention_helper_source_sha256=sha256(HERE / "RETIRE.py") if (HERE / "RETIRE.py").exists() else None,
                scope="Saved-data correctness only; settling and shape separation are separate analysis gates.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--replay", choices=("none", "main", "all"), default="none")
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args()
    out = owned(args.out)
    if out.exists():
        raise ValueError("verification output must be fresh")
    result = verify(args.manifest, args.replay, args.device)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps(dict(passed=result["passed"], failures=result["failures"], out=str(out),
                          elapsed_seconds=result["elapsed_seconds"])), flush=True)
    return 0 if result["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
