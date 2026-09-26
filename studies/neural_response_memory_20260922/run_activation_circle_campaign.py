"""Predeclared two-GPU activation-circle phases with cumulative integration budget.

No experiment is chosen from its result here. Conditional phases take explicit
selection rows. The single scheduler reserves integration wall time before
starting either worker and saves all child logs and lifecycle records.
"""

import argparse
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


TOTAL_BUDGET = 33000.
RESERVATION_GUARD = 35.
WATCHDOG_GRACE = 30.
TOLERANCES = (1.25e-5,3.125e-6,7.8125e-7)
FOLDER = Path(__file__).resolve().parent
REPOSITORY = FOLDER.parents[1]
CASES_PATH = FOLDER/"activation_circle_cases.json"
PROTOCOL_PATH = FOLDER/"ACTIVATION_CIRCLE_PROTOCOL.md"
RUNNER_PATH = FOLDER/"activation_circle_run.py"


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda:stream.read(1<<20),b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path,value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix+".tmp")
    temporary.write_text(json.dumps(value,indent=2)+"\n")
    temporary.replace(path)


def read_json_if_present(path):
    try:
        return json.loads(Path(path).read_text())
    except (FileNotFoundError,json.JSONDecodeError):
        return None


def prior_accounting(roots):
    """Count each run directory once; failed reservations remain conservative."""
    records = {}
    for raw_root in roots:
        root = Path(raw_root).resolve()
        if not root.is_dir():
            raise ValueError("missing prior root: "+str(root))
        campaign = read_json_if_present(root/"campaign.json")
        if campaign:
            if campaign.get("status") in ("running","starting"):
                raise ValueError("prior campaign is not finalized: "+str(root))
            for row in campaign.get("jobs",[]):
                if row.get("status") in ("pending","budget_skipped","cancelled_before_launch"):
                    continue
                path = Path(row["run_directory"]).resolve()
                records[str(path)] = dict(row)
        for path in root.rglob("summary.json"):
            summary = read_json_if_present(path)
            if not summary or summary.get("hidden_layers") != 3 or summary.get("activation") not in ("relu","gelu","selu","sigmoid"):
                continue
            directory = str(path.parent.resolve())
            config = read_json_if_present(path.parent/"config.json") or {}
            records.setdefault(directory,dict(run_directory=directory,config=config,status="complete"))
            records[directory]["charged_integration_seconds"] = summary["integration_with_observations_seconds"]
            records[directory]["summary"] = summary
    total = 0.
    for row in records.values():
        charge = row.get("charged_integration_seconds",row.get("reserved_integration_seconds"))
        if charge is None or not math.isfinite(charge) or charge < 0:
            raise ValueError("prior run has no valid integration accounting: "+row["run_directory"])
        total += charge
    return total,list(records.values())


def normalize_device(value):
    if value in (0,"0","cuda:0"):
        return "cuda:0"
    if value in (1,"1","cuda:1"):
        return "cuda:1"
    raise ValueError("activation campaign devices must be cuda:0 or cuda:1")


def build_jobs(phase,cases,selections=None,prior_runs=()):
    names = list(cases)
    if len(names) != 8:
        raise ValueError("frozen circle suite must contain eight activation/task combinations")
    expected_cases = {(activation,task) for activation in ("relu","gelu","selu","sigmoid")
                      for task in ("two_outliers_alternating","quadrant_alternating")}
    if {(row["activation"],row["task"]) for row in cases.values()} != expected_cases:
        raise ValueError("incomplete activation/task suite")
    if phase not in ("pilot","primary","refine","repeat"):
        raise ValueError("invalid campaign phase")
    if phase == "pilot":
        if selections is not None:
            raise ValueError("pilot does not accept selections")
        outliers = [name for name in names if cases[name]["task"] == "two_outliers_alternating"]
        rows = [dict(case=case,model=model,order=order,rtol=TOLERANCES[0])
                for case in outliers for model,order in (("dense",1),("moment",3))]
    elif phase == "primary":
        if selections is not None:
            raise ValueError("primary does not accept selections")
        rows = [dict(case=case,model=model,order=order,rtol=rtol)
                for case in names for rtol in TOLERANCES[:2]
                for model,order in (("dense",1),("moment",1),("moment",2),("moment",3))]
    else:
        if selections is None or not isinstance(selections,list):
            raise ValueError("refine/repeat require explicit JSON selection rows")
        rows = [dict(row) for row in selections]
        if phase == "refine" and len(rows) > 32:
            raise ValueError("at most thirty-two conditional refinements")
        if phase == "repeat":
            expected = {(case,model,order) for case in names
                        if cases[case]["task"] == "two_outliers_alternating"
                        for model,order in (("dense",1),("moment",3))}
            selected = {(row.get("case"),row.get("model"),row.get("order",row.get("P",1))) for row in rows}
            if len(rows) != 8 or selected != expected:
                raise ValueError("repeat requires all eight outlier-task activation/dense/P3 pairs")
    jobs,seen = [],set()
    for index,row in enumerate(rows):
        case,model = row["case"],row["model"]
        order = row.get("order",row.get("P",1))
        if case not in cases or model not in ("dense","moment") or order not in (1,2,3):
            raise ValueError("invalid case/model/order selection")
        if model == "dense":
            order = 1
        rtol = row.get("rtol",TOLERANCES[2] if phase == "refine" else None)
        if rtol not in TOLERANCES or (phase == "refine" and rtol != TOLERANCES[2]):
            raise ValueError("selection tolerance is not in the frozen phase")
        key = (case,model,order,rtol)
        if key in seen:
            raise ValueError("duplicate phase selection")
        seen.add(key)
        existing = [prior for prior in prior_runs if
                    (prior.get("config",{}).get("case"),prior.get("config",{}).get("model"),
                     prior.get("config",{}).get("order",1),prior.get("config",{}).get("rtol")) == key]
        if phase in ("pilot","primary","repeat") and any(prior.get("config",{}).get("phase") == phase for prior in existing):
            raise ValueError("phase configuration already executed; no unauthorized retry")
        if phase == "refine" and any(prior.get("config",{}).get("phase") == "refine" for prior in existing):
            raise ValueError("this model already received its conditional refinement")
        device = normalize_device(row.get("device",index%2))
        if phase == "repeat":
            originals = [prior for prior in prior_runs if
                         (prior.get("config",{}).get("case"),prior.get("config",{}).get("model"),
                          prior.get("config",{}).get("order",1)) == (case,model,order)
                         and prior.get("config",{}).get("phase") in ("primary","refine")]
            if not originals or rtol != min(prior["config"]["rtol"] for prior in originals):
                raise ValueError("repeat must use the finest executed original tolerance")
            original = next(prior for prior in reversed(originals) if prior["config"]["rtol"] == rtol)
            required_device = "cuda:1" if original["config"]["device"] == "cuda:0" else "cuda:0"
            if "device" in row and normalize_device(row["device"]) != required_device:
                raise ValueError("repeat device must swap the original GPU")
            device = required_device
        label = "dense" if model == "dense" else "P"+str(order)
        run_id = f"{index:02d}_{case}_{label}_rtol{rtol:.9g}"
        angles = [value*math.pi/180 for value in cases[case]["angles_degrees"]]
        config = dict(case=case,activation=cases[case]["activation"],task=cases[case]["task"],phase=phase,run_id=run_id,model=model,order=order,width=4096,
                      seed=20260920,inputs=[[math.cos(a),math.sin(a)] for a in angles],
                      labels=cases[case]["labels"],device=device,threads=1,rtol=rtol,atol=rtol/100,
                      initial_step=.05,max_step=2.,max_time=10000.,max_steps=30 if phase == "pilot" else 30000,
                      max_wall_seconds=30. if phase == "pilot" else 300.,target_loss=.001,
                      milestones=[] if phase == "pilot" else [.9,.5,.1,.03,.01,.003,.001],
                      observation_times=[] if phase == "pilot" else [10.,100.,1000.],
                      query_count=128 if phase == "pilot" else 8192,query_batch_size=128,
                      bisection_iterations=32,progress_seconds=30.,
                      source_case_definition=cases[case])
        jobs.append(dict(run_id=run_id,config=config,status="pending"))
    return jobs


def campaign_manifest(phase,prior_roots,selections_path):
    sources = ("run_activation_circle_campaign.py","activation_circle_run.py","activation_moment_engine.py",
               "deep_moment_engine.py","moment_engine.py",
               "ACTIVATION_CIRCLE_PROTOCOL.md","activation_circle_cases.json")
    head = subprocess.check_output(["git","-C",str(REPOSITORY),"rev-parse","HEAD"],text=True).strip()
    paths = [str((FOLDER/name).relative_to(REPOSITORY)) for name in sources]
    dirty = subprocess.check_output(["git","-C",str(REPOSITORY),"status","--porcelain=v1","--",*paths],text=True)
    return dict(phase=phase,created_utc=stamp(),cwd=str(Path.cwd().resolve()),git_head=head,
                scoped_git_status=dirty,source_sha256={name:sha256(FOLDER/name) for name in sources},
                prior_roots=[str(Path(path).resolve()) for path in prior_roots],
                selections_path=str(Path(selections_path).resolve()) if selections_path else None,
                selections_sha256=sha256(selections_path) if selections_path else None,
                python_executable=sys.executable,command=sys.argv,
                budget_seconds=TOTAL_BUDGET,reservation_guard_seconds=RESERVATION_GUARD,
                watchdog_grace_seconds=WATCHDOG_GRACE,
                accounting="sum completed integration wall; running reservations include a 35-second guard; 30-second integration watchdog grace; failed runs charge lifecycle duration or full reservation")


def launch(args):
    cases = json.loads(CASES_PATH.read_text())
    selections = json.loads(Path(args.selections).read_text()) if args.selections else None
    prior_charge,prior_runs = prior_accounting(args.prior_roots)
    jobs = build_jobs(args.phase,cases,selections,prior_runs)
    if len(prior_runs)+len(jobs) > 112:
        raise ValueError("campaign would exceed the frozen 112-trajectory ceiling")
    out = Path(args.out).resolve()
    out.mkdir(parents=True,exist_ok=False)
    for name in ("configs","logs","runs"):
        (out/name).mkdir()
    manifest = campaign_manifest(args.phase,args.prior_roots,args.selections)
    write_json(out/"manifest.json",manifest)
    campaign = dict(manifest,status="running",prior_integration_seconds=prior_charge,
                    jobs=jobs,started_utc=stamp(),charged_integration_seconds=0.)
    for job in jobs:
        job["run_directory"] = str(out/"runs"/job["run_id"])
        job["config_path"] = str(out/"configs"/(job["run_id"]+".json"))
        job["log_path"] = str(out/"logs"/(job["run_id"]+".log"))
        write_json(job["config_path"],job["config"])
        job["config_sha256"] = sha256(job["config_path"])
    environment = dict(os.environ)
    for name in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS","BLIS_NUM_THREADS"):
        environment[name] = "1"
    environment["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
    active = {}
    charged = 0.

    def persist():
        campaign.update(charged_integration_seconds=charged,
                        total_with_prior_integration_seconds=prior_charge+charged,
                        active_reserved_integration_seconds=sum(item["job"]["reserved_integration_seconds"] for item in active.values()),
                        updated_utc=stamp())
        write_json(out/"campaign.json",campaign)

    def finish(device):
        nonlocal charged
        item = active.pop(device)
        process,job = item["process"],item["job"]
        code = process.wait()
        item["log"].close()
        lifecycle = read_json_if_present(Path(job["run_directory"])/"lifecycle.json") or {}
        summary = read_json_if_present(Path(job["run_directory"])/"summary.json")
        if summary:
            cost = summary["integration_with_observations_seconds"]
        elif "integration_with_observations_seconds" in lifecycle:
            cost = lifecycle["integration_with_observations_seconds"]
        elif "integration_start_monotonic" in lifecycle:
            cost = time.monotonic()-lifecycle["integration_start_monotonic"]
        elif (Path(job["run_directory"])/"manifest.json").exists():
            cost = job["reserved_integration_seconds"]
        else:
            cost = 0.
        charged += cost
        job.update(exit_code=code,ended_utc=stamp(),subprocess_wall_seconds=time.monotonic()-item["start"],
                   charged_integration_seconds=cost,status="complete" if code == 0 and summary and summary.get("status") != "failed" else "failed",
                   log_sha256=sha256(job["log_path"]))
        if summary:
            job["summary_status"] = summary["status"]
            job["summary_sha256"] = sha256(Path(job["run_directory"])/"summary.json")
        if job["status"] == "failed":
            failure_path = Path(job["run_directory"])/"launcher_failure.json"
            failure_path.parent.mkdir(parents=True,exist_ok=True)
            write_json(failure_path,{key:job[key] for key in job if key != "config"})
            if not (failure_path.parent/"config.json").exists():
                write_json(failure_path.parent/"config.json",job["config"])
            if not (failure_path.parent/"failure.json").exists():
                write_json(failure_path.parent/"failure.json",dict(status="failed",reason="launcher child failed",
                           exit_code=code,watchdog_reason=job.get("watchdog_reason"),
                           config_sha256=job["config_sha256"],source_sha256=manifest["source_sha256"]))
        print(json.dumps(dict(event="child_complete",run_id=job["run_id"],exit_code=code,
                              charged_seconds=cost,total_with_prior=prior_charge+charged)),flush=True)

    persist()
    try:
        while any(job["status"] == "pending" for job in jobs) or active:
            for device in ("cuda:0","cuda:1"):
                if device in active:
                    continue
                job = next((row for row in jobs if row["status"] == "pending" and row["config"]["device"] == device),None)
                if job is None:
                    continue
                reserved = sum(item["job"]["reserved_integration_seconds"] for item in active.values())
                available = TOTAL_BUDGET-prior_charge-charged-reserved
                cap = job["config"]["max_wall_seconds"]
                if available < cap+RESERVATION_GUARD:
                    if not active:
                        for row in jobs:
                            if row["status"] == "pending":
                                row.update(status="budget_skipped",skip_reason="next complete run reservation exceeds remaining budget")
                    continue
                job.update(status="running",reserved_integration_seconds=cap+RESERVATION_GUARD,started_utc=stamp())
                write_json(job["config_path"],job["config"])
                job["config_sha256"] = sha256(job["config_path"])
                command = [sys.executable,str(RUNNER_PATH),"--config",job["config_path"],"--out",job["run_directory"]]
                log = Path(job["log_path"]).open("wb")
                try:
                    process = subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,cwd=REPOSITORY,
                                               env=environment,start_new_session=True)
                except OSError as exc:
                    log.close()
                    job.update(status="failed",exit_code=None,charged_integration_seconds=0.,launch_error=str(exc),ended_utc=stamp())
                    failure_directory = Path(job["run_directory"])
                    failure_directory.mkdir(parents=True,exist_ok=True)
                    write_json(failure_directory/"config.json",job["config"])
                    write_json(failure_directory/"failure.json",dict(status="failed",reason="subprocess launch failed",
                               message=str(exc),config_sha256=job["config_sha256"],source_sha256=manifest["source_sha256"]))
                    continue
                job["pid"] = process.pid
                active[device] = dict(process=process,job=job,log=log,start=time.monotonic())
                print(json.dumps(dict(event="child_started",run_id=job["run_id"],device=device,pid=process.pid,
                                      integration_cap_seconds=cap)),flush=True)
            for device,item in list(active.items()):
                if item["process"].poll() is not None:
                    finish(device)
                    continue
                lifecycle = read_json_if_present(Path(item["job"]["run_directory"])/"lifecycle.json") or {}
                if lifecycle.get("status") == "integrating":
                    elapsed = time.monotonic()-lifecycle["integration_start_monotonic"]
                    if elapsed >= item["job"]["config"]["max_wall_seconds"]+WATCHDOG_GRACE:
                        item["job"]["watchdog_reason"] = "integration cap plus reserved final-step grace exhausted"
                        os.killpg(item["process"].pid,signal.SIGKILL)
            persist()
            if active:
                time.sleep(.2)
        campaign["status"] = "complete"
    except BaseException:
        campaign["status"] = "interrupted"
        for item in active.values():
            if item["process"].poll() is None:
                os.killpg(item["process"].pid,signal.SIGKILL)
        for device in list(active):
            finish(device)
        for job in jobs:
            if job["status"] == "pending":
                job["status"] = "cancelled_before_launch"
        raise
    finally:
        campaign["ended_utc"] = stamp()
        persist()
    return campaign


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--phase",choices=("pilot","primary","refine","repeat"),required=True)
    result.add_argument("--out",required=True)
    result.add_argument("--selections")
    result.add_argument("--prior-roots",nargs="*",default=[])
    return result


if __name__ == "__main__":
    launch(parser().parse_args())
