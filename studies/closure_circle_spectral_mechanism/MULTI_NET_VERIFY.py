"""Independent NumPy replay and identity audit of all 48 saved networks.

No trainer is imported and no optimization is performed. A single BLAS thread,
180 CPU-second hard cap, and exactly indices 0,10,...,1430 for every endpoint.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CASES = ("triple_d20", "triple_d40", "triple_d60", "quad_d15", "quad_d30", "quad_d45")
DATA_KEYS = ("name", "kind", "delta", "rotation", "amplitude", "angles_degrees", "labels")


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(8*1024*1024), b""):
            h.update(part)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def initialized_digest(width, seed, dtype):
    """Independent reproduction of maintained initializer's declared draw order."""
    rng = np.random.default_rng(seed)
    h = hashlib.sha256()
    for shape, scale in (((width,2),1.), ((width,width),np.sqrt(width)), ((width,),width)):
        array = np.asarray(rng.standard_normal(shape)/scale, dtype=dtype)
        h.update(array.tobytes())
    return h.hexdigest()


def predict(arrays, theta):
    W, V, c = arrays
    u = np.stack((np.cos(theta), np.sin(theta)))
    return c @ np.tanh(V @ np.tanh(W @ u))/len(c)


def run(campaign, output):
    resource.setrlimit(resource.RLIMIT_CPU, (180,180))
    cpu0, wall0 = time.process_time(), time.monotonic()
    require(output.is_relative_to(campaign) and output != campaign, "fresh campaign child required")
    output.mkdir(exist_ok=False)
    manifest = read(campaign/"manifest.json")
    manifest_hash = digest(campaign/"manifest.json")
    require(manifest_hash == (campaign/"manifest.sha256").read_text().strip(), "frozen manifest digest")
    batch = read(campaign/"main_batch.json")
    require(batch["exit_codes"] == [0,0] and not batch["missing"] and batch["stop_reason"] is None,
            "campaign workers did not complete")
    configs = manifest["configs"]
    expected = {(case,n,s,"main") for case in CASES for n in (1024,4096) for s in (1729,2718,3141)}
    expected |= {(case,4096,1729,"half") for case in CASES}
    expected |= {(case,1024,1729,"precision") for case in CASES}
    actual = {(c["name"],c["width"],c["seed"],c["variant"]) for c in configs}
    require(actual == expected and len(configs) == 48 and len({c["id"] for c in configs}) == 48,
            "fixed 48-job design mismatch")
    require(set(batch["completed"]) == {c["id"] for c in configs}, "batch completion set mismatch")
    sources = {}
    for relative, expected_hash in {**manifest["source_hashes"], **manifest["input_hashes"]}.items():
        live = (ROOT/relative).resolve()
        entry = manifest["archived_sources"][relative]
        archived = (campaign/entry["path"]).resolve()
        require(archived.is_relative_to(campaign/"source_archive") and entry["sha256"] == expected_hash,
                "invalid archive identity: "+relative)
        require(digest(live) == expected_hash, "live producer mismatch: "+relative)
        require(digest(archived) == expected_hash, "archived producer mismatch: "+relative)
        sources[relative] = dict(sha256=expected_hash, live_verified=True, archive_verified=True)
    original_data = {}
    for case in CASES:
        path = ROOT/"data/generated/closure_circle_spectral_mechanism/campaign_001"/f"{case}_N1_main/config.json"
        original_data[case] = read(path)
    theta = 2*np.pi*np.arange(1440)/1440
    indices = np.arange(0,1440,10)
    rows, replay, initial_hashes = [], {}, {}
    for cfg in configs:
        name, width = cfg["id"], cfg["width"]
        directory = campaign/name
        record = read(directory/"record.json")
        require(record["status"] == "complete", name+": incomplete")
        require(cfg == read(directory/"config.json") == record["config"], name+": config identity")
        require(record["source_hashes"] == manifest["source_hashes"], name+": producer identity")
        require(record["input_hashes"] == manifest["input_hashes"] and record["manifest_sha256"] == manifest_hash,
                name+": frozen manifest/input identity")
        require(name == f"{cfg['name']}_n{width}_s{cfg['seed']}_{cfg['variant']}", name+": id")
        require(all(cfg[k] == original_data[cfg["name"]][k] for k in DATA_KEYS), name+": original closure data")
        require(digest(ROOT/cfg["closure_config_path"]) == cfg["closure_config_sha256"]
                == manifest["input_hashes"][cfg["closure_config_path"]], name+": closure config source digest")
        require(cfg["dtype"] == ("float64" if cfg["variant"] == "precision" else "float32")
                and cfg["h"] == (.01 if cfg["variant"] == "half" else .02)
                and cfg["retain_state"] is True, name+": numerics/retention")
        require(record["environment"]["tf32"] is False, name+": TF32 unexpectedly enabled")
        hashes = {}
        require(set(record["outputs"]) >= {"config.json", "observations.npz", "state.npz"}, name+": missing outputs")
        for filename, expected_hash in record["outputs"].items():
            path = (directory/filename).resolve()
            require(path.is_relative_to(directory.resolve()) and digest(path) == expected_hash, name+": output hash "+filename)
            hashes[filename] = expected_hash
        with np.load(directory/"observations.npz", allow_pickle=False) as archive:
            saved = {k:archive[k] for k in archive.files}
        require(all(np.all(np.isfinite(v)) for v in saved.values()), name+": observation finiteness")
        require(np.array_equal(saved["theta"],theta), name+": dense angles")
        require(saved["dense_predictions"].shape == saved["common_T100"].shape == (1440,), name+": dense shape")
        require(np.array_equal(saved["times"],10.*np.arange(13)), name+": fixed clock")
        require(saved["predictions"].shape == (13,512)
                and saved["train_predictions"].shape == (13,len(cfg["labels"]))
                and saved["loss"].shape == (13,), name+": observation shapes")
        if "stop_theta" in saved:
            require(np.array_equal(saved["stop_theta"],2*np.pi*np.arange(512)/512), name+": stop angles")
        if "motion_theta" in saved:
            require(np.array_equal(saved["motion_theta"],2*np.pi*np.arange(128)/128), name+": motion angles")
        size = len(cfg["labels"])
        for k in ("gram1_initial", "gram2_initial", "gram1_final", "gram2_final"):
            gram = saved[k]
            require(gram.shape == (size,size), name+": Gram shape")
            require(np.max(abs(gram-gram.T)) <= 1e-6
                    and np.linalg.eigvalsh((gram+gram.T)/2).min() >= -1e-6, name+": Gram symmetry/PSD")
        loss = np.mean((saved["train_predictions"]-np.asarray(cfg["labels"]))**2,axis=1)
        require(np.allclose(loss,saved["loss"],rtol=0,atol=1e-14), name+": reconstructed loss")
        require(float(np.max(np.diff(loss))) <= 1e-6 and record["checks"]["max_loss_increase"] <= 1e-6,
                name+": recorded loss monotonicity")
        require(record["final_time"] == 120 and record["final_loss"] == saved["loss"][-1]
                and record["stop_reason"] == "fixed_T120", name+": endpoint/stopping")
        panel = saved["predictions"]
        drift1, drift2 = float(np.max(abs(panel[10]-panel[8]))), float(np.max(abs(panel[12]-panel[10])))
        threshold = .002*max(1.,float(np.max(abs(panel[-1]))))
        settled = bool(loss[-1] <= 1e-6 and max(drift1,drift2) <= threshold)
        require(record["settled"] == settled, name+": settling diagnostic")
        for key,value in (("settled_drift_80_100",drift1),("settled_drift_100_120",drift2),("settled_tolerance",threshold)):
            if key in record["checks"]:
                require(abs(record["checks"][key]-value) <= 1e-14, name+": "+key+" mismatch")
        tol = 1e-10 if cfg["dtype"] == "float64" else 2e-5
        require(record["checks"]["disk_replay"] <= tol, name+": producer disk replay")
        oddness = {k:float(np.max(abs(saved[k][:720]+saved[k][720:])))
                   for k in ("dense_predictions", "common_T100")}
        oddness["all_stop_observations"] = float(np.max(abs(panel[:,:256]+panel[:,256:])))
        require(max(oddness.values()) <= tol, name+": oddness")
        initial_key = width,cfg["seed"],cfg["dtype"]
        if initial_key not in initial_hashes:
            initial_hashes[initial_key] = initialized_digest(*initial_key)
        require(initial_hashes[initial_key] == record["initial_weight_sha256"], name+": initialization digest")
        before = time.process_time()
        with np.load(directory/"state.npz", allow_pickle=False) as archive:
            require(set(archive.files) == {"W","V","c"}, name+": state keys")
            stored = tuple(archive[k] for k in ("W","V","c"))
        require(tuple(a.shape for a in stored) == ((width,2),(width,width),(width,)), name+": state shape")
        require(all(a.dtype == np.dtype(cfg["dtype"]) and np.all(np.isfinite(a)) for a in stored),
                name+": state dtype/finiteness")
        arrays = tuple(np.asarray(a,dtype=np.float64) for a in stored)
        del stored
        actual_output = predict(arrays, theta[indices])
        error = float(np.max(abs(actual_output-saved["dense_predictions"][indices])))
        train_output = predict(arrays, np.deg2rad(cfg["angles_degrees"]))
        train_error = float(np.max(abs(train_output-saved["train_predictions"][-1])))
        require(np.all(np.isfinite(actual_output)) and max(error,train_error) <= tol, name+": independent NumPy replay")
        replay[name] = actual_output
        rows.append(dict(id=name, all_output_hashes_verified=True, output_hashes=hashes,
            configuration_data_identity=True, initialization_digest_verified=True,
            all_observation_arrays_finite=True, all_retained_parameters_finite=True,
            observation_shapes={k:list(v.shape) for k,v in saved.items()}, loss_reconstructed=True,
            final_loss=float(loss[-1]), T100_loss=float(loss[10]), settled=settled,
            settling_drift_80_100=drift1, settling_drift_100_120=drift2, settling_tolerance=threshold,
            oddness=oddness, replay_tolerance=tol, independent_cpu_replay_max_abs_error=error,
            independent_train_replay_max_abs_error=train_error,
            state_load_and_replay_cpu_seconds=time.process_time()-before))
        del arrays, saved
    np.savez_compressed(output/"independent_replay.npz", indices=indices, **replay)
    result = dict(passed=True, configs_checked=48, retained_states_checked=48,
        manifest_sha256=digest(campaign/"manifest.json"), verifier_sha256=digest(__file__),
        source_checks=sources, rows=rows, replay_indices=indices.tolist(),
        maximum_cpu_replay_error=max(r["independent_cpu_replay_max_abs_error"] for r in rows),
        maximum_train_replay_error=max(r["independent_train_replay_max_abs_error"] for r in rows),
        maximum_oddness=max(max(r["oddness"].values()) for r in rows),
        settled_count=sum(r["settled"] for r in rows),
        independent_replay_sha256=digest(output/"independent_replay.npz"),
        cpu_seconds=time.process_time()-cpu0, wall_seconds=time.monotonic()-wall0,
        cpu_cap_seconds=180,
        limitations=["All48 final parameter arrays were scanned, with independent replay on the fixed144-angle subset of the exact1440 dense grid.",
            "Training observations and clocks were audited; training was not rerun, intermediate parameter states were not retained, and T100 states cannot be independently replayed.",
            "A passed verifier certifies saved-state/configuration consistency, not closure accuracy, equilibrium, or infinite-width convergence."],
        environment=dict(numpy=np.__version__,threads={k:os.environ[k] for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")}),
        command=[sys.executable,*sys.argv])
    require(result["cpu_seconds"] < 180, "CPU budget exceeded")
    (output/"verification.json").write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:result[k] for k in ("passed","configs_checked","retained_states_checked","maximum_cpu_replay_error","settled_count","cpu_seconds","wall_seconds")}))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.campaign.resolve(),args.output.resolve())
