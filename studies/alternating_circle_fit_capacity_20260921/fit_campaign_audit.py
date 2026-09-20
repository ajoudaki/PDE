#!/usr/bin/env python3
"""Independent protocol/provenance audit of a completed, already replayed campaign."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time

import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def audit(root, replay_path, adjudications_path):
    started = time.monotonic()
    root = Path(root).resolve()
    repository = Path(__file__).resolve().parents[2]
    run = read(root / "run_record.json")
    replay = read(replay_path)
    checked = {a["attempt"]: a for a in replay["attempts"]}
    adjudications = read(adjudications_path)
    failures = []

    def require(condition, message):
        if not condition:
            failures.append(message)

    require(run["status"] == "complete", "campaign is not complete")
    jobs = run["jobs"]
    require(len({j["output"] for j in jobs}) == len(jobs), "duplicate output directory")
    require(set(checked) == {j["output"] for j in jobs}, "replay/job coverage mismatch")
    data = {}
    sources = {}
    frozen_protocol_sources = {}
    used_adjudications = []
    common = dict(adam_eps=1e-8, adam_lr1=.01, adam_lr2=.003, adam_steps=8000,
                  adam_switch=4000, export_reserve_seconds=5., fit_mse=.001,
                  lbfgs_history=50, lbfgs_max_eval=2000, lbfgs_max_iter=1000,
                  lbfgs_tolerance_change=1e-14, lbfgs_tolerance_grad=1e-12,
                  max_seconds=60., threads=1, circle_points=8192)
    for job in jobs:
        path = Path(job["output"])
        record = read(path / "record.json")
        config = record["config"]
        result = checked[str(path)]
        require(result["record_sha256"] == digest(path / "record.json"), f"stale replay: {path.name}")
        require(all(config[k] == v for k, v in common.items()), f"optimizer/time protocol mismatch: {path.name}")
        require(config["seed"] in (20260921, 20260922, 20260923), f"unauthorized seed: {path.name}")
        require(config["gain"] in ("primary", "rescue"), f"unauthorized gain: {path.name}")
        require(record["first_weight_gain"] == (1 if config["gain"] == "primary" else config["m"]/2),
                f"incorrect input gain: {path.name}")
        require(record["adam_steps_completed"] <= 8000 and record["lbfgs_evaluations"] <= 2000,
                f"optimizer cap exceeded: {path.name}")
        require(record["elapsed_seconds_before_final_record_write"] <= 60 and record["budget_respected"],
                f"attempt cap exceeded: {path.name}")
        require(job["supervisor_failure"] is None, f"supervisor failure: {path.name}")
        require(not record["environment"]["tf32"] and record["environment"]["deterministic_algorithms"],
                f"arithmetic policy mismatch: {path.name}")
        require(record["optimizer_coordinates"] == "W,middle,v=c/n for both models", f"coordinate mismatch: {path.name}")
        for key in ("config", "freeze"):
            provenance = record["provenance"]
            source_path = Path(provenance[key+"_path"])
            if key == "freeze" and source_path.resolve() == Path(__file__).resolve().parent / "README.md":
                # The README may receive an outcome summary after execution;
                # the exact frozen bytes remain in the flat protocol snapshot.
                snapshot = Path(__file__).resolve().parent / "PROTOCOL.md"
                if snapshot.exists():
                    source_path = snapshot
            require(digest(source_path) == provenance[key+"_sha256"], f"{key} hash mismatch: {path.name}")
            if key == "freeze":
                frozen_protocol_sources[provenance["freeze_path"]] = dict(
                    original_path=provenance["freeze_path"], verified_path=str(source_path),
                    sha256=provenance["freeze_sha256"])
        supplied_config = read(record["provenance"]["config_path"])
        require(all(config.get(k) == v for k, v in supplied_config.items())
                and set(config) == set(supplied_config) | set(common),
                f"saved config/default resolution differs: {path.name}")
        for name, expected in record["environment"]["source_sha256"].items():
            sources.setdefault(name, digest(repository / name))
            require(sources[name] == expected, f"source hash mismatch: {name}")
        for phase in ("initial", "best", "final"):
            with np.load(path / (phase+".npz"), allow_pickle=False) as arrays:
                require(all(arrays[k].dtype == np.float64 for k in arrays.files), f"non-float64 weights: {path.name}/{phase}")
        model_count = config["width"]**2+3*config["width"] if config["model"] == "network" else 3*config["width"]+15
        fixed_count = 0 if config["model"] == "network" else 8*config["width"]
        require(record["trainable_scalar_count"] == model_count, f"trainable count mismatch: {path.name}")
        require(record["frozen_feature_scalar_count"] == fixed_count, f"frozen count mismatch: {path.name}")
        if result["all_scored_states_within_tolerances"]:
            fit, mse = result["states"]["best"]["fit"], result["states"]["best"]["mse"]
        else:
            entry = adjudications.get(str(path), {})
            valid = (entry.get("resolved") and entry.get("stable_to_higher_precision")
                     and entry.get("record_sha256") == digest(path / "record.json"))
            require(valid, f"unresolved precision exception: {path.name}")
            if not valid:
                continue
            evidence = read(entry["evidencepath"])
            require(evidence["best_sha256"] == digest(path / "best.npz")
                    and evidence["dataset_sha256"] == digest(path / "dataset.npz"),
                    f"stale precision evidence: {path.name}")
            require(evidence["high_precision"]["fit"] == entry["fit"]
                    and evidence["low_precision"]["fit"] == entry["fit"], f"unstable precision fit: {path.name}")
            fit, mse = entry["fit"], entry["mse"]
            used_adjudications.append(str(path))
        data[str(path)] = dict(job=job, record=record, config=config, fit=fit, mse=mse)

    main = [a for a in data.values() if a["job"]["stage"] != "reproduction"]
    gates = []

    def group(model, width, samples):
        entries = [a for a in main if (a["config"]["model"], a["config"]["width"], a["config"]["m"]) == (model, width, samples)]
        canonical = [a for a in entries if a["config"]["gain"] == "primary"]
        rescue = [a for a in entries if a["config"]["gain"] == "rescue"]
        required_seeds = Counter((20260921, 20260922, 20260923))
        require(Counter(a["config"]["seed"] for a in canonical) == required_seeds, f"canonical seeds mismatch: {model}/{width}/{samples}")
        canonical_fits = sum(a["fit"] for a in canonical)
        require(Counter(a["config"]["seed"] for a in rescue) == (required_seeds if canonical_fits == 0 else Counter()),
                f"rescue gate mismatch: {model}/{width}/{samples}")
        result = dict(model=model, width=width, samples=samples, canonical_fits=canonical_fits,
                      all_fits=sum(a["fit"] for a in entries), attempted=len(entries), rescue_run=bool(rescue))
        gates.append(result)
        return result

    stage_a = [group("network", 55, m) for m in (30, 62, 126, 254)]
    candidates = [g["samples"] for g in stage_a if g["samples"] > 55 and not g["all_fits"]]
    selected = min(candidates) if candidates else None
    require(selected == run["selected_samples"], "conditional sample selection mismatch")
    if selected is not None:
        group("closure", 1024, selected)
        group("network", 105, selected)
    require(gates == run["gates"], "recorded gates differ from independent reconstruction")
    allowed = {("network", 55, m) for m in (30, 62, 126, 254)}
    if selected is not None:
        allowed |= {("closure", 1024, selected), ("network", 105, selected)}
    require(all((a["config"]["model"], a["config"]["width"], a["config"]["m"]) in allowed for a in main), "unregistered main comparison")

    reproductions = []
    expected_models = (("network", 55), ("closure", 1024), ("network", 105)) if selected is not None else (("network", 55),)
    for model, width in expected_models:
        candidates = [a for a in main if a["config"]["model"] == model and a["config"]["width"] == width
                      and a["config"]["m"] == (selected if selected is not None else 254)]
        best = min(candidates, key=lambda a: a["mse"])
        repeated = [a for a in data.values() if a["job"]["stage"] == "reproduction"
                    and a["config"]["model"] == model and a["config"]["width"] == width]
        require(len(repeated) == 1, f"reproduction count mismatch: {model}/{width}")
        if len(repeated) != 1:
            continue
        again = repeated[0]
        require(again["job"]["original_output"] == best["job"]["output"], f"wrong reproduction selection: {model}/{width}")
        require(again["config"] == best["config"], f"reproduction settings differ: {model}/{width}")
        difference = abs(again["mse"]-best["mse"])
        require(again["fit"] == best["fit"] and difference <= 1e-6, f"unstable reproduction: {model}/{width}")
        reproductions.append(dict(model=model, width=width, original=best["job"]["output"],
                                  reproduction=again["job"]["output"], same_config=True,
                                  same_fit=again["fit"] == best["fit"], mse_difference=difference))

    total_worker = sum(j["process_wall_seconds"] for j in jobs)
    require(abs(total_worker-run["spent_worker_seconds"]) < 1e-8, "worker timing sum mismatch")
    require(total_worker <= 2500 and len(jobs) <= 39, "overall campaign cap exceeded")
    intervals = sorted((a["record"]["started_unix_seconds"], a["record"]["started_unix_seconds"]+
                        a["record"]["elapsed_seconds_before_final_record_write"], a["config"]["device"]) for a in data.values())
    concurrency = max(sum(start <= t < stop for start, stop, device in intervals) for t, _, _ in intervals)
    require(concurrency <= 2, "more than two simultaneous training intervals")
    for i, (start, stop, device) in enumerate(intervals):
        require(not any(start < other_stop and other_start < stop and other_device == device
                        for other_start, other_stop, other_device in intervals[i+1:]), "overlapping training on one GPU")
    main_strict = all(checked[a["job"]["output"]]["all_scored_states_within_tolerances"]
                      for a in data.values() if a["config"]["m"] == selected)
    return dict(passed=not failures, failures=failures, attempts=len(jobs), selected_samples=selected,
                gates=gates, reproductions=reproductions, strict_replay_attempts=len(jobs)-len(used_adjudications),
                precision_adjudications=used_adjudications, main_comparison_all_strict_float64=main_strict,
                source_sha256=sources, frozen_protocol_sources=list(frozen_protocol_sources.values()),
                worker_seconds_sum=total_worker,
                maximum_attempt_seconds=max(a["record"]["elapsed_seconds_before_final_record_write"] for a in data.values()),
                maximum_training_concurrency=concurrency, automatic_precision_seconds=run.get("automatic_precision_seconds", 0),
                final_replay_elapsed_seconds=replay["elapsed_seconds"], audit_elapsed_seconds=time.monotonic()-started)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--replay", required=True, type=Path)
    parser.add_argument("--adjudications", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.root, args.replay, args.adjudications)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+"\n")
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit(0 if result["passed"] else 1)
