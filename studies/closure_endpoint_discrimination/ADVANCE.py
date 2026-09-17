#!/usr/bin/env python3
"""Prepare and collect stage-5 continuations; never launch scientific workers.

Examples (all paths belong to this study):
  ADVANCE.py --campaign C --collect confirmation finest --out C/initial.json
  ADVANCE.py --campaign C --previous C/initial.json --time 700 --profile common_0700
  ADVANCE.py --campaign C --previous C/initial.json --merge common_0700 --out C/t0700.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / "data/generated/closure_endpoint_discrimination"
sys.path.insert(0, str(HERE))
import PREPARE


def owned(path):
    path = Path(path).resolve()
    if not path.is_relative_to(GENERATED):
        raise ValueError("path must belong to this study's generated directory: " + str(path))
    return path


def sha(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1048576), b""):
            result.update(chunk)
    return result.hexdigest()


def read_json(path):
    return json.loads(owned(path).read_text())


def write_fresh(path, value):
    path = owned(path)
    if not path.parent.is_dir():
        raise FileNotFoundError(path.parent)
    with path.open("x") as handle:
        json.dump(value, handle, indent=2, allow_nan=False)
        handle.write("\n")


def action_record(action, inputs):
    return dict(action=action, created_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                command=[sys.executable, *sys.argv], cwd=str(Path.cwd()),
                sources_sha256={str(HERE/name): sha(HERE/name) for name in
                                ("ADVANCE.py", "PREPARE.py", "BATCH.py", "CAMPAIGN_PLAN.md")},
                input_sha256={str(owned(path)): sha(path) for path in inputs})


def endpoint(path, stage=5):
    """Validate completeness without interpreting or recomputing a trajectory."""
    path = owned(path)
    record_path = path/"record.json"
    record = read_json(record_path)
    if record.get("status") != "complete":
        raise ValueError("producer is not complete: " + str(record_path))
    config = record["config"]
    if config.get("stage") != stage:
        raise ValueError("producer belongs to another stage: " + str(record_path))
    kind = config.get("kind")
    if kind == "network":
        required = ("state.pt", "trajectories.npz")
    elif kind == "closure":
        required = ("final_restart.json", "final_wrapper.npz", "trajectories.npz")
    else:
        raise ValueError("unrecognized producer kind: " + str(kind))
    for name in required:
        if not (path/name).is_file():
            raise FileNotFoundError(path/name)
    now = record.get("last_time", record.get("final_time"))
    if now is None or not math.isfinite(float(now)) or not 0 <= float(now) <= 1600:
        raise ValueError("invalid producer endpoint time")
    return dict(path=str(path), time=float(now), settled=bool(record.get("settled")),
                record_sha256=sha(record_path), config=config)


def batch_directory(campaign, stage, profile):
    base = campaign/f"stage_{stage:02d}"
    path = owned(profile if Path(profile).is_absolute() else base/profile)
    if path.parent != base:
        raise ValueError("profile must be directly inside the selected stage")
    return path


def completed_batch(campaign, stage, profile):
    folder = batch_directory(campaign, stage, profile)
    report_path, jobs_path = folder/"batch.json", folder/"jobs.json"
    report, spec = read_json(report_path), read_json(jobs_path)
    if report.get("complete") is not True or report.get("reason") is not None or report.get("pending"):
        raise ValueError("dispatcher batch is not fully complete: " + str(folder))
    if report.get("jobs_file_sha256") != sha(jobs_path):
        raise ValueError("batch jobs differ from the consumed job specification")
    if spec.get("stage") != stage:
        raise ValueError("batch stage differs")
    expected = {job["name"]: job for job in spec["jobs"]}
    results = report["results"]
    if len(expected) != len(spec["jobs"]) or len(results) != len(expected):
        raise ValueError("duplicate jobs or incomplete result count")
    actual_names = [result["name"] for result in results]
    if len(set(actual_names)) != len(actual_names) or set(actual_names) != set(expected):
        raise ValueError("result names do not equal scheduled job names")
    collected = {}
    for result in results:
        if (result.get("exit_code") != 0 or result.get("producer_status") != "complete"
                or result.get("interrupted", False)):
            raise ValueError("unsuccessful or interrupted producer: " + result["name"])
        path = owned(result["out"])
        if path != owned(expected[result["name"]]["out"]) or path.parent != folder:
            raise ValueError("result output does not match its scheduled destination")
        collected[result["name"]] = endpoint(path, stage)
    return collected, [report_path, jobs_path]


def common_time(endpoints):
    times = [value["time"] for value in endpoints.values()]
    if not times:
        raise ValueError("no endpoints collected")
    return times[0] if max(times)-min(times) <= 1e-8 else None


def previous_manifest(path, stage):
    previous = read_json(path)
    if previous.get("stage") != stage or previous.get("pair") != [1, 3]:
        raise ValueError("previous manifest must describe stage 5 and pair [1,3]")
    if not isinstance(previous.get("jobs"), dict) or not previous["jobs"]:
        raise ValueError("previous manifest lacks its role-to-output mapping")
    if not isinstance(previous.get("minimum_common_time"), (int, float)):
        raise ValueError("previous manifest lacks the frozen initial timing requirement")
    ends = {role: endpoint(path, stage) for role, path in previous["jobs"].items()}
    return previous, ends


def collect(campaign, stage, profiles, output, previous_path=None):
    if owned(output).exists():
        raise FileExistsError(output)
    inputs, batches = [], []
    if previous_path is None:
        previous, endpoints = None, {}
    else:
        previous, endpoints = previous_manifest(previous_path, stage)
        inputs.append(owned(previous_path))
    updated = {}
    for profile in profiles:
        records, paths = completed_batch(campaign, stage, profile)
        for role, value in records.items():
            if role in updated:
                raise ValueError("role occurs in two newly collected batches: " + role)
            if previous is None and role in endpoints:
                raise ValueError("role occurs twice in initial collection: " + role)
            if previous is not None:
                if role not in endpoints:
                    raise ValueError("continuation introduced an unrecognized role: " + role)
                if value["time"] <= endpoints[role]["time"]:
                    raise ValueError("continuation did not advance role " + role)
            updated[role] = value
        inputs.extend(paths)
        batches.append(str(paths[0]))
    endpoints.update(updated)
    if previous is None:
        # Only initial collection establishes this requirement. Merges preserve it.
        minimum = max(value["time"] for value in endpoints.values()) + 100
        initial_times = {role: value["time"] for role, value in endpoints.items()}
        rounds = 0
    else:
        minimum = previous["minimum_common_time"]
        initial_times = previous["initial_stop_times"]
        rounds = int(previous.get("continuation_rounds", 0))+1
    result = dict(stage=stage, pair=[1, 3], campaign=str(campaign),
                  inputs_path=str(campaign/f"stage_{stage:02d}"/"inputs.npz"),
                  jobs={role: value["path"] for role, value in endpoints.items()},
                  endpoints={role: {k: v for k, v in value.items() if k != "config"}
                             for role, value in endpoints.items()},
                  minimum_common_time=minimum, initial_stop_times=initial_times,
                  common_time=common_time(endpoints), continuation_rounds=rounds,
                  collected_batches=batches,
                  provenance=action_record("merge" if previous else "initial_collect", inputs))
    if previous is not None:
        result["previous_manifest"] = str(owned(previous_path))
    write_fresh(output, result)
    print(json.dumps(dict(manifest=str(owned(output)), roles=len(endpoints),
                          common_time=result["common_time"], minimum_common_time=minimum)), flush=True)
    return result


def job_priority(job):
    config = read_json(job["config_path"])
    if job["device"] == "cpu":
        # BATCH picks CPU jobs independently of the preceding GPU entries.
        cost = float(config.get("P", 0))/float(config["h"])
        return (1, -cost, -int(config.get("P", 0)), job["name"])
    if config["kind"] == "network":
        if config.get("dtype") == "float64":
            return (0, 0, 0, job["name"])
        if config.get("width") == 8192 and float(config["h"]) < .02:
            return (0, 1, 0, job["name"])
        return (0, 2, -int(config["width"])/float(config["h"]), job["name"])
    return (0, 3, -int(config["P"])*int(config["order"])/float(config["h"]), job["name"])


def advance(campaign, stage, previous_path, target_time, profile):
    previous, endpoints = previous_manifest(previous_path, stage)
    target_time = float(target_time)
    if not math.isfinite(target_time) or target_time > 1600:
        raise ValueError("common endpoint must be finite and at most 1600")
    if target_time < previous["minimum_common_time"]-1e-8:
        raise ValueError("common endpoint precedes the frozen initial timing requirement")
    latest = max(value["time"] for value in endpoints.values())
    if target_time <= latest:
        raise ValueError("next endpoint must advance every role")
    if previous.get("continuation_rounds", 0) and abs(target_time-latest-100) > 1e-8:
        raise ValueError("subsequent common continuations must advance by 100")
    folder = batch_directory(campaign, stage, profile)
    if folder.exists():
        raise FileExistsError("continuation profile must be fresh: " + str(folder))
    # This call changes only clocks/devices in fresh job configurations, exactly
    # as the maintained study preparation helper specifies; it launches nothing.
    PREPARE.continuation(campaign, stage, folder.name, owned(previous_path), target_time)
    jobs_path = folder/"jobs.json"
    spec = read_json(jobs_path)
    before = sha(jobs_path)
    spec["jobs"] = sorted(spec["jobs"], key=job_priority)
    spec["queue_policy"] = "float64 network, 8192 half-step network, other GPU jobs; CPU descending P/h"
    jobs_path.write_text(json.dumps(spec, indent=2, allow_nan=False)+"\n")
    action = action_record("prepare_continuation", [owned(previous_path)])
    action.update(target_time=target_time, profile=folder.name, jobs_before_reordering_sha256=before,
                  jobs_sha256=sha(jobs_path), queue=[job["name"] for job in spec["jobs"]],
                  configurations_sha256={job["name"]: sha(job["config_path"]) for job in spec["jobs"]},
                  physics_changed=False, launched_workers=False)
    write_fresh(folder/"advance_action.json", action)
    print(json.dumps(dict(jobs=str(jobs_path), queue=action["queue"], launched_workers=False)), flush=True)
    return spec


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign", required=True)
    parser.add_argument("--stage", type=int, default=5)
    parser.add_argument("--stage5", action="store_true", help="explicit alias for the stage-5 default")
    operation = parser.add_mutually_exclusive_group()
    operation.add_argument("--collect", nargs="+", metavar="PROFILE")
    operation.add_argument("--merge", nargs="+", metavar="PROFILE")
    parser.add_argument("--previous")
    parser.add_argument("--time", type=float)
    parser.add_argument("--profile")
    parser.add_argument("--out", "--output", dest="out")
    args = parser.parse_args()
    if args.stage != 5:
        parser.error("this helper is scoped to stage 5")
    campaign = owned(args.campaign)
    if args.collect:
        if not args.out or args.previous:
            parser.error("initial --collect requires --out and does not accept --previous")
        collect(campaign, args.stage, args.collect, args.out)
    elif args.merge:
        if not args.out or not args.previous:
            parser.error("--merge requires --previous and --out")
        collect(campaign, args.stage, args.merge, args.out, args.previous)
    else:
        if not args.previous or args.time is None or not args.profile:
            parser.error("continuation preparation requires --previous, --time and --profile")
        advance(campaign, args.stage, args.previous, args.time, args.profile)


if __name__ == "__main__":
    main()
