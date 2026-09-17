"""Fixed thirty-degree closure campaign using unchanged evolution and Grams."""
from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PLAN = HERE / "ARC30_20260914_PLAN.md"
PLAN_HASH = "b7e9cd1584e953a67144be4052adf39c26be74e6a11ab3fd51a13db05e5f9617"
GENERATED = ROOT / "data/generated/wide_network_closure_comparison/ARC30_20260914_v1"
SPEC = importlib.util.spec_from_file_location("arc30_inherited_grams", HERE / "GRAM_20260914_CLOSURE.py")
gram = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gram)
base, np = gram.base, gram.np
INHERITED_HASHES = gram.source_hashes()
ORIGINAL_ATOMIC = base.atomic_json
ORIGINAL_GRAM_OBSERVATION = gram.gram_observation
INITIALIZATION = {}
RUN_CAP, WORKER_CAP, GLOBAL_CAP = 600., 2400., 2400.


def configurations():
    menu = ((1, "", 1024, 512, "1/200", "primary"),
            (3, "", 1024, 512, "1/200", "primary"),
            (5, "", 1024, 512, "1/200", "primary"),
            (3, "_refined", 2048, 1024, "1/200", "quadrature_control"),
            (3, "_halfstep", 1024, 512, "1/400", "time_control"),
            (5, "_refined", 2048, 1024, "1/200", "quadrature_control"),
            (5, "_fine", 4096, 2048, "1/200", "quadrature_control"),
            (5, "_fine_halfstep", 4096, 2048, "1/400", "time_control"))
    return [dict(id=f"arcs30_N{order}{suffix}", case="arcs30", order=order,
                 initialization_nodes=q, population_nodes=p, step=h,
                 refined=q > 1024, kind=kind) for order, suffix, q, p, h, kind in menu]


def source_hashes():
    result = INHERITED_HASHES.copy()
    for path in (Path(__file__), PLAN, HERE / "ARC30_20260914_PREPARE.py"):
        if not path.exists():
            raise FileNotFoundError("Required frozen input source missing: " + str(path))
        result[str(path.relative_to(ROOT))] = base.digest(path)
    return result


def manifest(output):
    output = Path(output)
    if (output.is_symlink() or output.resolve().parent != GENERATED.parent.resolve()
            or not output.name.startswith("ARC30_")):
        raise ValueError("ARC30 closure output must be a direct ARC30_* child of this study's generated namespace")
    value = json.loads((output / "arc30_campaign.json").read_text())
    if base.digest(PLAN) != PLAN_HASH or value["plan_sha256"] != PLAN_HASH:
        raise ValueError("ARC30 campaign does not match the frozen plan")
    if value.get("closure_configs") != configurations():
        raise ValueError("ARC30 campaign closure configurations differ from the frozen menu")
    return value


def input_verification(output):
    manifest(output)
    arrays, _ = base.load_inputs(output)
    expected = {"times", "circle", "arcs30_inputs", "arcs30_labels", "arcs30_probabilities"}
    if set(arrays) != expected:
        raise ValueError("Unexpected ARC30 input keys")
    u, y, p = (arrays["arcs30_" + key] for key in ("inputs", "labels", "probabilities"))
    assert u.shape == (16, 2) and arrays["circle"].shape == (128, 2)
    np.testing.assert_array_equal(y, np.repeat([1., -1.], 8))
    np.testing.assert_array_equal(p, np.full(16, 1/16))
    np.testing.assert_allclose(np.sum(u*u, axis=1), 1, atol=2e-15, rtol=0)
    np.testing.assert_array_equal(u[8:], np.column_stack((-u[:8, 1], u[:8, 0])))
    angles = np.arctan2(u[:, 1], u[:, 0]) * 180 / np.pi
    np.testing.assert_allclose(angles[[0, 7, 8, 15]], [-30, 30, 60, 120], atol=2e-13, rtol=0)
    np.testing.assert_allclose(u[:8, 1] / (1 + u[:8, 0]),
                               (np.arange(8)*2-7)/7 * np.tan(np.pi/12), atol=2e-15, rtol=0)
    margin = y * (u[:, 0]-u[:, 1]) / np.sqrt(2)
    assert np.min(margin) > 0
    np.testing.assert_allclose(np.min(margin), np.sin(np.pi/12), atol=2e-15, rtol=0)
    np.testing.assert_array_equal(arrays["times"], np.asarray([float(t) for t in base.observation_times()]))
    return dict(status="passed", coordinate_angles_degrees=angles.tolist(),
                minimum_normalized_label_margin=float(np.min(margin)),
                input_sha256=base.digest(output / "inputs.npz"),
                input_metadata_sha256=base.digest(output / "inputs.json"))


def observe(state, data, circle, row):
    if not INITIALIZATION:
        INITIALIZATION.update({key: base.array_hash(getattr(state, key))
                               for key in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")})
        if not (np.array_equal(state.w, state.g) and np.array_equal(state.M, state.D)
                and np.array_equal(state.c, np.zeros_like(state.c))):
            raise AssertionError("Fresh closure initialization contract failed")
    return ORIGINAL_GRAM_OBSERVATION(state, data, circle, row)


def record_json(path, value):
    if path.name == "record.json" and path.parent.parent.name == "closure":
        value.update(format="arc30-20260914-closure-v1", plan_sha256=PLAN_HASH,
                     initialization_array_sha256=INITIALIZATION.copy(),
                     original_comparison_status="not_applicable_changed_training_data",
                     original_comparison_scope="New thirty-degree inputs; no historical scalar trajectory replay.",
                     archive_input_provenance_scope="New fixed ARC30 inputs from the frozen study-owned preparation source.")
        step = Fraction(value["configuration"]["step"])
        value["steps_requested"] = int(Fraction(40) / step)
        value["steps_completed_at_last_observation"] = int(Fraction(str(value.get("last_time", "0"))) / step)
        value["fixed_marks_verified"] = (value.get("fixed_signature_initial") == value["fixed_signature_final"]
                                           if "fixed_signature_final" in value else None)
    return ORIGINAL_ATOMIC(path, value)


def no_replay(output, config, directory, shared):
    return dict(status="not_applicable_changed_training_data", reason="New thirty-degree input law.")


def install_wrappers():
    """Change only inputs, menus, observations, provenance and resource limits."""
    base.PLAN = PLAN
    base.atomic_json = record_json
    gram.PLAN, gram.manifest, gram.source_hashes = PLAN, manifest, source_hashes
    gram.configurations, gram.replay_check = configurations, no_replay
    gram.RUN_CAP, gram.WORKER_CAP, gram.GLOBAL_CAP = RUN_CAP, WORKER_CAP, GLOBAL_CAP


def verification(output):
    # The inherited fixture uses non-initial states, so verify before installing observe.
    result = gram.verification()
    result.update(input_validation=input_verification(output), source_hashes=source_hashes(),
                  scope="Deterministic fixtures and supplied inputs only; no scientific initialization or evolution.")
    return result


def run_configuration(output, config):
    shared = manifest(output)
    if shared.get("experiment_started_epoch") is None:
        raise ValueError("Shared scientific start clock has not been set")
    input_verification(output)
    INITIALIZATION.clear()
    gram.gram_observation = observe
    try:
        return gram.run_configuration(output, config)
    finally:
        gram.gram_observation = ORIGINAL_GRAM_OBSERVATION


def run_campaign(output):
    shared = manifest(output)
    if shared.get("experiment_started_epoch") is None:
        raise ValueError("Shared scientific start clock has not been set")
    path = output / "closure_campaign.json"
    if path.exists():
        raise FileExistsError("Refusing to replace an earlier closure campaign")
    ORIGINAL_ATOMIC(output / "closure_verification.json", verification(output))
    start = time.time()
    campaign = dict(status="running", maximum_runs=8, configurations=configurations(),
                    source_hashes=source_hashes(), run_wall_cap=RUN_CAP, worker_wall_cap=WORKER_CAP,
                    global_wall_cap=GLOBAL_CAP, output_cap_bytes=gram.OUTPUT_CAP,
                    numerical_threads=1, command=sys.argv, runs=[])
    ORIGINAL_ATOMIC(path, campaign)
    worker_seconds = 0.
    for config in configurations():
        remaining = min(WORKER_CAP-worker_seconds, gram.global_remaining(shared, start))
        if remaining <= 0 or gram.output_bytes(output) >= gram.OUTPUT_CAP:
            campaign["runs"].append(dict(id=config["id"], status="unstarted_budget"))
            continue
        directory = output / "closure" / config["id"]
        directory.mkdir(parents=True, exist_ok=False)
        command = [sys.executable, "-B", str(Path(__file__).resolve()), "--output", str(output),
                   "--worker-id", config["id"]]
        launched, stop_reason = time.time(), None
        with (directory / "worker.log").open("xb") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, cwd=ROOT)
            while process.poll() is None:
                if time.time()-launched >= min(RUN_CAP, remaining):
                    stop_reason = "wall_budget"
                elif gram.output_bytes(output) >= gram.OUTPUT_CAP:
                    stop_reason = "output_budget"
                if stop_reason:
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
                    break
                time.sleep(.25)
        elapsed = time.time()-launched
        worker_seconds += elapsed
        record_path = directory / "record.json"
        record = json.loads(record_path.read_text()) if record_path.exists() else dict(configuration=config)
        if stop_reason or process.returncode != 0:
            record.update(status="stopped" if stop_reason else "failure", worker_exit_code=process.returncode,
                          stop_reason=stop_reason, supervisor_wall_seconds=elapsed)
            progress_path = directory / "gram_progress.json"
            if progress_path.exists():
                progress = json.loads(progress_path.read_text())
                record.update(gram_completed_observations=progress["completed_rows"], gram_shape=progress["shape"],
                              gram_sha256=base.digest(directory / "gram.npy"), gram=progress)
            ORIGINAL_ATOMIC(record_path, record)
        campaign["runs"].append(dict(id=config["id"], status=record.get("status", "failure"),
                                     returncode=process.returncode, wall_seconds=elapsed, command=command))
        campaign.update(worker_wall_seconds=worker_seconds, wall_seconds=time.time()-start)
        ORIGINAL_ATOMIC(path, campaign)
        print(json.dumps(campaign["runs"][-1]), flush=True)
    campaign.update(status="complete" if all(r["status"] == "complete" for r in campaign["runs"]) else "incomplete",
                    worker_wall_seconds=worker_seconds, wall_seconds=time.time()-start,
                    total_output_bytes=gram.output_bytes(output))
    ORIGINAL_ATOMIC(path, campaign)
    return 0 if campaign["status"] == "complete" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--run", action="store_true")
    action.add_argument("--verify-only", action="store_true")
    action.add_argument("--worker-id", choices=[c["id"] for c in configurations()])
    args = parser.parse_args()
    install_wrappers()
    output = args.output.resolve()
    if args.verify_only:
        print(json.dumps(verification(output), indent=2), flush=True)
        return 0
    if args.worker_id:
        return run_configuration(output, next(c for c in configurations() if c["id"] == args.worker_id))
    return run_campaign(output)


if __name__ == "__main__":
    raise SystemExit(main())
