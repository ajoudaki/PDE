"""Independent CPU replay of completed frozen-campaign states, without training.

Uses only the maintained NumPy solver; neither ENGINE nor RUN is imported.
Every completed record is hash-checked and replayed on all 1440 saved circle
directions. Incomplete records are listed and their arrays are not read.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

# Establish the thread limit before NumPy or any BLAS library is imported.
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / "data/generated/closure_circle_spectral_mechanism"
sys.path.insert(0, str(ROOT / "code"))
from pde.observable_arithmetic import Arithmetic
from pde.observable_solver import State, DataLaw, _fields, predict, paired_observations

ARRAYS = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")
TOLERANCE = 1e-10


def sha(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while block := handle.read(1024*1024):
            result.update(block)
    return result.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def circle(count):
    angle = 2*np.pi*np.arange(count)/count
    return np.column_stack((np.cos(angle), np.sin(angle)))


def same(key, actual, expected, errors, exact=False):
    actual, expected = np.asarray(actual), np.asarray(expected)
    if actual.shape != expected.shape or not np.all(np.isfinite(actual)) or not np.all(np.isfinite(expected)):
        raise ValueError(f"{key}: invalid shape or nonfinite value")
    error = float(np.max(np.abs(actual-expected))) if actual.size else 0.0
    errors[key] = error
    if error > (0 if exact else TOLERANCE):
        raise ValueError(f"{key}: absolute discrepancy {error}")


def config_check(config):
    """Check the numeric protocol from PLAN rather than execute the producer."""
    control = config["control"]
    if control not in ("main", "fine", "half"):
        raise ValueError("undeclared control")
    expected = dict(Q=8192 if control == "fine" else 4096,
                    P=4096 if control == "fine" else 2048,
                    h=.01 if control == "half" else .02, t_min=100, t_max=600, obs_dt=10)
    if any(config[key] != value for key, value in expected.items()):
        raise ValueError("configuration differs from frozen numeric protocol")
    if config["order"] not in (1, 2, 3, 5) or config["order"] not in config["orders"]:
        raise ValueError("undeclared order")
    if config["id"] != f'{config["name"]}_N{config["order"]}_{control}':
        raise ValueError("configuration id mismatch")
    delta, rotation, amplitude = config["delta"], config["rotation"], config["amplitude"]
    if config["kind"] == "pair":
        angles, labels = rotation+delta*np.array([-.5, .5]), amplitude*np.array([-1, 1])
    elif config["kind"] == "triple":
        angles, labels = rotation+delta*np.array([-1, 0, 1]), np.array([1, -1, 1])
    elif config["kind"] == "quad":
        angles, labels = rotation+delta*np.array([-1.5, -.5, .5, 1.5]), np.array([-1, 1, -1, 1])
    else:
        raise ValueError("undeclared input family")
    if not np.array_equal(config["angles_degrees"], angles) or not np.array_equal(config["labels"], labels):
        raise ValueError("angles or labels differ from frozen case")


def replay(directory, config, record, source_hash):
    errors = {}
    with np.load(directory / "state.npz", allow_pickle=False) as archive:
        expected_keys = set(ARRAYS) | {"record_json", "data_inputs", "data_labels", "data_probabilities"}
        if set(archive.files) != expected_keys:
            raise ValueError("unexpected checkpoint fields")
        checkpoint = json.loads(str(archive["record_json"].item()))
        if set(checkpoint) != {"format", "metadata", "clock", "extra_metadata"}:
            raise ValueError("unexpected checkpoint record schema")
        if checkpoint["format"] != "closure-circle-torch-float64-v1":
            raise ValueError("unexpected checkpoint format")
        if checkpoint["extra_metadata"] != dict(config=config, source_sha256=source_hash):
            raise ValueError("checkpoint source or configuration mismatch")
        ar = Arithmetic()
        state = State(*(archive[key].copy() for key in ARRAYS), ar, checkpoint["metadata"]).validate()
        data = DataLaw(*(archive["data_"+key].copy() for key in ("inputs", "labels", "probabilities"))).validate(ar)
    metadata = state.metadata
    if any(metadata[key] != config[name] for key, name in
           (("hierarchy_order", "order"), ("initialization_nodes", "Q"), ("population_nodes", "P"))):
        raise ValueError("checkpoint initialization resolution differs")
    steps = checkpoint["clock"]["steps"]
    if not isinstance(steps, int) or steps < 0:
        raise ValueError("invalid checkpoint step count")
    clock_error = abs(checkpoint["clock"]["physical_time"]-steps*config["h"])
    if clock_error > 1e-7 or abs(steps*config["h"]-record["last_time"]) > 1e-10:
        raise ValueError("checkpoint physical clock differs from endpoint")
    angles = np.deg2rad(config["angles_degrees"])
    expected_inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    same("checkpoint_inputs", data.inputs, expected_inputs, errors, exact=True)
    same("checkpoint_labels", data.labels, config["labels"], errors, exact=True)
    same("checkpoint_weights", data.probabilities, np.ones(len(data.labels))/len(data.labels), errors, exact=True)
    dense = predict(state, circle(1440), block_size=256)
    train = predict(state, data.inputs, block_size=256)
    loss = float(data.probabilities @ ((train-data.labels)**2))
    current = _fields(state, data.inputs, backward=False)
    initial_state = state.dynamic_copy(state.g, np.zeros_like(state.c), state.D)
    initial = _fields(initial_state, data.inputs, backward=False)
    pairs = paired_observations(state, data, include_pairs=False)
    with np.load(directory / "observations.npz", allow_pickle=False) as observed:
        for key in observed.files:
            if not np.all(np.isfinite(observed[key])):
                raise ValueError(f"nonfinite observations: {key}")
        for key, value in (("train_inputs", data.inputs), ("labels", data.labels),
                           ("weights", data.probabilities), ("angles", angles)):
            same(key, observed[key], value, errors, exact=True)
        same("dense_predictions", dense, observed["dense_predictions"], errors)
        same("diagnostic_prediction", dense, observed["prediction"], errors)
        same("final_720_prediction", dense[::2], observed["predictions"][-1], errors)
        same("train_predictions", train, observed["train_predictions"][-1], errors)
        same("diagnostic_train_prediction", train, observed["train_prediction"], errors)
        same("record_loss", loss, record["final_loss"], errors)
        same("observation_loss", loss, observed["loss"][-1], errors)
        same("record_time", observed["times"][-1], record["last_time"], errors, exact=True)
        times = observed["times"]
        if not np.array_equal(times, np.arange(len(times))*config["obs_dt"]):
            raise ValueError("observation time grid differs from protocol")
        same("all_recorded_losses", observed["loss"],
             ((observed["train_predictions"]-data.labels)**2) @ data.probabilities, errors)
        for layer, population in ((1, state.p1), (2, state.p2)):
            for label, fields in (("current", current), ("initial", initial)):
                feature = fields[f"h{layer}"]
                gram = feature.T @ (population[:, None]*feature)
                same(f"hidden{layer}_gram_{label}", gram, observed[f"hidden{layer}_gram_{label}"], errors)
                if np.linalg.eigvalsh(gram).min() < -1e-8:
                    raise ValueError("invalid negative hidden Gram eigenvalue")
            same(f"hidden{layer}_motion_rms_training", pairs[f"rms{layer}"],
                 observed[f"hidden{layer}_motion_rms_training"], errors)
        same("singular_values_final", np.linalg.svd(state.M, compute_uv=False), observed["singular_values_final"], errors)
        same("singular_values_initial", np.linalg.svd(state.D, compute_uv=False), observed["singular_values_initial"], errors)
    return dict(id=config["id"], order=config["order"], Q=config["Q"], P=config["P"],
                dense_directions=1440, block_size=256, final_loss=loss,
                clock_accumulation_error=clock_error, max_absolute_error=max(errors.values()), errors=errors)


def verify(campaign, out):
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    signal.alarm(120)
    begun, cpu_begun = time.perf_counter(), time.process_time()
    campaign, out = campaign.resolve(), out.resolve()
    if campaign != GENERATED / "campaign_001" or not out.is_relative_to(GENERATED):
        raise ValueError("only the assigned campaign and study-owned outputs are allowed")
    if out == campaign or out.is_relative_to(campaign):
        raise ValueError("verification output must be separate from campaign inputs")
    out.mkdir(parents=True, exist_ok=False)
    manifest_path = campaign / "manifest.json"
    manifest = read_json(manifest_path)
    manifest_hash = sha(manifest_path)
    expected_sources = {str(HERE / name) for name in ("PLAN.md", "RUN.py", "ENGINE.py", "ENGINE_CHECK.py", "NTK.py", "NTK_CHECK.py")}
    expected_sources |= {str(ROOT / "code/pde" / name) for name in
                         ("observable_solver.py", "observable_initialization.py", "observable_words.py", "observable_arithmetic.py", "observable_fixed.py")}
    if set(manifest["sources"]) != expected_sources:
        raise ValueError("unexpected manifest source paths")
    report = dict(status="RUNNING", campaign=str(campaign), manifest_sha256=manifest_hash,
                  verification_source_sha256=sha(__file__), tolerance=TOLERANCE,
                  scientific_training=False, backend="maintained NumPy float64", threads=1,
                  hash_checked=[], numeric_replay=[], pending=[], incomplete=[], failures=[],
                  selection="all complete records in manifest order at scan time",
                  unread_scope="Other studies, incomplete-run arrays, and unlisted research sources were not read.",
                  code_audit=dict(pickle_disabled=True, run_imported=False, engine_imported=False,
                                  checkpoint_expected_keys_checked=True, checkpoint_data_and_config_checked=True,
                                  executable_checkpoint_content=False,
                                  note="RUN passes only study-produced archives to ENGINE.load_npz; the loader uses allow_pickle=False, JSON and explicit tensor fields. This verifier uses the maintained NumPy State instead."))
    for path, expected in manifest["sources"].items():
        if sha(path) != expected:
            report["failures"].append(dict(source=path, error="source hash mismatch"))
    source_hash = manifest["sources"][str(HERE / "ENGINE.py")]
    configs = manifest["configurations"]
    if len(configs) != 75 or len({c["id"] for c in configs}) != 75:
        raise ValueError("expected exactly 75 distinct planned configurations")
    # Snapshot record availability before any numerical replay, so a running
    # campaign cannot silently enlarge this verification's declared selection.
    records = []
    for config in configs:
        config_check(config)
        directory = campaign / config["id"]
        if not directory.is_relative_to(campaign) or "/" in config["id"]:
            raise ValueError("unsafe configuration path")
        record_path = directory / "record.json"
        if not record_path.exists():
            report["pending"].append(config["id"])
            continue
        record = read_json(record_path)
        if record["status"] != "complete":
            report["incomplete"].append(dict(id=config["id"], status=record["status"], stop_reason=record.get("stop_reason")))
            continue
        records.append((directory, config, record))
    for directory, config, record in records:
        try:
            if record["config"] != config or read_json(directory / "config.json") != config:
                raise ValueError("record/file/manifest configurations differ")
            if record["manifest_sha256"] != manifest_hash or record["source_sha256"] != source_hash:
                raise ValueError("record manifest or engine source hash differs")
            if set(record["outputs"]) != {"state.npz", "observations.npz", "config.json"}:
                raise ValueError("unexpected record output paths")
            for name, digest in record["outputs"].items():
                if sha(directory / name) != digest:
                    raise ValueError(f"output hash mismatch: {name}")
            report["hash_checked"].append(config["id"])
            if not report["failures"] or not any("source" in f for f in report["failures"]):
                report["numeric_replay"].append(replay(directory, config, record, source_hash))
        except Exception as error:
            report["failures"].append(dict(id=config["id"], error=repr(error)))
    replayed = {entry["id"] for entry in report["numeric_replay"]}
    required = [f"pair_d30_r45_N{n}_{control}" for n in (1, 2, 3, 5) for control in ("main", "fine")]
    required += [f"{name}_N{n}_{control}" for name in ("triple_d40", "quad_d30")
                 for n in (1, 3, 5) for control in ("main", "fine", "half")]
    report.update(status="FAIL" if report["failures"] else "PASS_ALL" if len(replayed) == 75 else "PASS_AVAILABLE",
                  completed_snapshot=len(records), verified_count=len(replayed), source_hash_count=len(expected_sources),
                  required_selection=required, required_pending=[name for name in required if name not in replayed],
                  maximum_absolute_error=max((entry["max_absolute_error"] for entry in report["numeric_replay"]), default=None),
                  wall_seconds=time.perf_counter()-begun, cpu_seconds=time.process_time()-cpu_begun)
    (out / "verification.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key: report[key] for key in ("status", "completed_snapshot", "verified_count", "source_hash_count",
                                                  "maximum_absolute_error", "wall_seconds", "cpu_seconds", "failures")}))
    if report["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    verify(args.campaign, args.out)
