"""Resource-amended activation continuation, GPU 0 only unless authorized.

Preserves every frozen scientific producer. The single explicitly interrupted
primary attempt may restart once in a fresh campaign; other failures never do.
The 33000-second integration budget includes that interruption. Resource
policy changes do not change physics, tolerances, seeds or scientific gates.
"""

import argparse
import copy
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

import finish_activation_circle_campaign as workflow
import run_activation_circle_campaign as launcher

FOLDER, REPOSITORY, GENERATED = workflow.FOLDER, workflow.REPOSITORY, workflow.GENERATED
read_json, write_json, sha256, require, stamp = (workflow.read_json, workflow.write_json,
    workflow.sha256, workflow.require, workflow.stamp)
SOURCE_NAMES = ("continue_activation_circle_campaign.py", "ACTIVATION_CIRCLE_EXECUTION_AMENDMENT.md",
                "activation_fast_engine.py", "activation_circle_fast_run.py", *workflow.SOURCES)
TERMINAL = {"complete", "failed"}
NOT_EXECUTED = {"pending", "cancelled_before_launch", "budget_skipped"}
MAX_ATTEMPTS = 113  # 112 declared trajectories plus one resource-interrupted attempt.


def stop_child(item, selected_signal):
    try:
        os.killpg(item["process"].pid, selected_signal)
    except ProcessLookupError:
        pass


def key(config):
    return config["case"], config["model"], config.get("order", 1), config["rtol"]


def resource_policy(path):
    value = read_json(path)
    require(isinstance(value, dict) and isinstance(value.get("allow_gpu1"), bool),
            "Resource policy requires boolean allow_gpu1")
    if value["allow_gpu1"]:
        require(isinstance(value.get("authorization"), str) and value["authorization"].strip(),
                "Enabling GPU 1 requires explicit user-authorization text recorded by the lead")
    return dict(allowed_devices=["cuda:0", "cuda:1"] if value["allow_gpu1"] else ["cuda:0"],
                contents=value, path=str(Path(path).resolve()), sha256=sha256(path))


def continuation_jobs(cases, old, release):
    require(old.get("status") == "interrupted", "Old primary must be finalized as interrupted by the lead")
    interrupted = release.get("terminated_gpu1", [])
    require(len(interrupted) == 1, "Exactly one externally interrupted attempt is authorized for restart")
    interrupted_path = str(Path(interrupted[0]["run"]).resolve())
    expected = launcher.build_jobs("primary", cases)
    require(len(old.get("jobs", [])) == 64, "Original schedule must retain all 64 logical configurations")
    originals = {key(job["config"]): job for job in old["jobs"]}
    require(len(originals) == 64 and set(originals) == {key(job["config"]) for job in expected},
            "Original primary schedule differs from frozen logical configurations")
    jobs, restart_count = [], 0
    for planned in expected:
        previous = originals[key(planned["config"])]
        require(previous["config"] == planned["config"], "Original primary controls differ from frozen schedule")
        require(previous["status"] in TERMINAL | NOT_EXECUTED, "Old primary still contains active/unfinalized workers")
        restart = str(Path(previous["run_directory"]).resolve()) == interrupted_path
        if restart:
            require(previous["status"] == "failed", "Externally interrupted attempt must be a recorded failure")
            require((Path(previous["run_directory"]) / "failure.json").is_file(), "Interrupted failure receipt is missing")
            failure = read_json(Path(previous["run_directory"]) / "failure.json")
            require(failure.get("external_interruption") is True,
                    "Restart exception requires the recorded external-interruption flag")
            require(not (Path(previous["run_directory"]) / "summary.json").exists(),
                    "A completed trajectory cannot use the external-interruption restart exception")
            restart_count += 1
        if previous["status"] in TERMINAL and not restart:
            directory = Path(previous["run_directory"])
            require((directory / "summary.json").is_file() or (directory / "failure.json").is_file(),
                    "Original terminal attempt lacks evidence")
            continue
        job = copy.deepcopy(planned)
        job["original_scheduled_device"] = job["config"]["device"]
        if restart:
            job["restart_of_external_interruption"] = interrupted_path
        jobs.append(job)
    require(restart_count == 1, "The authorized interrupted attempt was not found exactly once")
    return jobs, interrupted_path


def remaining_jobs(jobs, completed):
    planned, finished = {key(job["config"]): job for job in jobs}, set()
    for campaign in completed:
        require(campaign.get("status") in ("complete", "interrupted"), "Completed root is not finalized")
        for job in campaign["jobs"]:
            identity = key(job["config"])
            require(identity in planned and job["status"] in TERMINAL | NOT_EXECUTED,
                    "Completed root has an unexpected configuration or active worker")
            controls = lambda cfg: {name:value for name,value in cfg.items() if name not in ("device", "execution_backend")}
            require(controls(job["config"]) == controls(planned[identity]["config"]), "Completed-root scientific controls differ")
            if job["status"] in TERMINAL:
                directory = Path(job["run_directory"])
                require(identity not in finished and any((directory/name).is_file() for name in ("summary.json", "failure.json")),
                        "Duplicate terminal configuration or missing terminal evidence")
                finished.add(identity)
    return [job for job in jobs if key(job["config"]) not in finished]


def logical_primary_complete(cases, old, continuation, interrupted_path, completed=()):
    expected = {key(job["config"]) for job in launcher.build_jobs("primary", cases)}
    finished = set()
    for campaign in (old, *completed, continuation):
        for job in campaign["jobs"]:
            if str(Path(job["run_directory"]).resolve()) == interrupted_path:
                continue
            if job["status"] in TERMINAL:
                directory = Path(job["run_directory"])
                require((directory / "summary.json").is_file() or (directory / "failure.json").is_file(),
                        "Logical terminal primary attempt lacks evidence")
                finished.add(key(job["config"]))
    require(finished == expected, "Not all 64 logical primary configurations have terminal attempts")
    return dict(logical_primary_configurations=64, finished_logical_configurations=len(finished),
                external_interruption_excluded_from_logical_completion=interrupted_path)


def choose_job(jobs, device, allowed):
    for job in jobs:
        if job["status"] != "pending":
            continue
        # With two authorized GPUs, keep the original opposite-GPU repeat plan.
        if job["config"]["phase"] == "repeat" and len(allowed) == 2 and job["config"]["device"] != device:
            continue
        return job
    return None


def repeat_runners(jobs, origins, prior):
    originals = {str(Path(job["run_directory"]).resolve()):job for job in prior}
    for job,origin in zip(jobs,origins):
        require(key(job["config"]) == key(origin["selection"]), "Repeat origin ordering differs")
        original = originals[str(Path(origin["original"]).resolve())]
        job["runner"] = original.get("runner","activation_circle_run.py")
        if job["runner"] == "activation_circle_fast_run.py":
            job["config"]["execution_backend"] = original["config"]["execution_backend"]


def reproduction_assessment(result):
    checks = result.get("checks", {})
    scientific = {name: passed for name, passed in checks.items() if name != "gpu_swapped"}
    available = bool(scientific)
    return dict(raw_checker_passed=result.get("passed") is True,
                cross_gpu_covered=checks.get("gpu_swapped") is True,
                numerical_reproduction_available=available,
                numerical_prefix_state_and_event_checks_passed=available and all(value is True for value in scientific.values()),
                excluded_from_numerical_check=["gpu_swapped"],
                statement="Same-GPU numerical reproduction does not establish the originally planned cross-GPU coverage")


class Controller:
    def __init__(self, args):
        self.args = args
        self.out = Path(args.out).resolve()
        self.base = Path(args.primary_root).resolve().parent
        require(args.generation >= 2, "Continuation generation must be at least 2")
        suffix = f"{args.generation:02d}"
        self.completed_roots = [Path(root).resolve() for root in args.completed_roots]
        require(len(set(self.completed_roots)) == len(self.completed_roots), "Duplicate completed roots")
        require(set(self.completed_roots) == {self.base/f"activation_circle_primary_continuation{index:02d}"
                for index in range(1,args.generation-1)}, "Completed roots must include exactly the previous continuation generations")
        self.paths = dict(primary=Path(args.primary_root).resolve(), pilot=Path(args.pilot_root).resolve(),
            continuation=self.base/f"activation_circle_primary_continuation{args.generation-1:02d}",
            analysis_primary=self.base/("activation_circle_analysis_primary"+suffix),
            refine=self.base/("activation_circle_refine"+suffix), analysis_final=self.base/("activation_circle_analysis_final"+suffix),
            repeat=self.base/("activation_circle_repeat"+suffix), audit=self.base/("activation_circle_audit"+suffix))
        require(not self.out.exists(), "Finish directory must be fresh")
        require(all(not self.paths[name].exists() for name in ("continuation", "analysis_primary", "refine", "analysis_final", "repeat", "audit")),
                "A continuation-stage output already exists; no overwrite or silent retry")
        require(0 < args.poll_seconds <= 60, "Polling interval must lie in (0,60]")
        self.out.mkdir(parents=True, exist_ok=False)
        (self.out/"logs").mkdir()
        self.policy_path = Path(args.resource_policy).resolve() if args.resource_policy else self.out/"resource_policy.json"
        if args.resource_policy:
            require(self.policy_path.exists(), "Explicit resource policy file must exist")
        else:
            write_json(self.policy_path, dict(allow_gpu1=False, authorization="User requested keeping GPU 1 free until further authorization"))
        self.frozen = {name: sha256(FOLDER/name) for name in SOURCE_NAMES}
        self.environment = dict(os.environ)
        self.environment.update({name:"1" for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS", "PYTHONDONTWRITEBYTECODE")})
        self.environment["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
        self.receipt = dict(status="waiting_for_old_primary_finalization", pid=os.getpid(), created_utc=stamp(),
            command=sys.argv, python_executable=sys.executable, source_sha256=self.frozen,
            paths={name:str(path) for name,path in self.paths.items()}, resource_policy_path=str(self.policy_path),
            completed_roots=list(map(str,self.completed_roots)), fast_moment_runner=args.fast_moment_runner,
            stages=[], resource_policy_history=[], maximum_attempts=MAX_ATTEMPTS, integration_budget_seconds=launcher.TOTAL_BUDGET,
            scope="User-directed resource amendment; scientific model and numerical protocol unchanged")
        self.children = []
        self.started = time.monotonic()
        self.persist()

    def persist(self):
        self.receipt.update(updated_utc=stamp(), elapsed_seconds=time.monotonic()-self.started)
        write_json(self.out/"workflow_receipt.json", self.receipt)

    def check_sources(self):
        require(all(sha256(FOLDER/name) == digest for name,digest in self.frozen.items()), "Frozen continuation dependency changed")

    def policy(self):
        policy = resource_policy(self.policy_path)
        history = self.receipt["resource_policy_history"]
        if not history or history[-1]["sha256"] != policy["sha256"]:
            history.append(dict(observed_utc=stamp(), **policy))
            self.persist()
        return policy

    def start(self, name, command, log_path=None):
        self.check_sources()
        path = Path(log_path) if log_path else self.out/"logs"/(name+".log")
        require(not path.exists(), "Subprocess log must be fresh")
        row = dict(name=name, command=list(map(str,command)), status="starting", started_utc=stamp(), log_path=str(path))
        self.receipt["stages"].append(row)
        self.persist()
        log = path.open("xb")
        try:
            process = subprocess.Popen(row["command"],stdout=log,stderr=subprocess.STDOUT,cwd=REPOSITORY,
                                       env=self.environment,start_new_session=True)
        except BaseException:
            log.close(); row.update(status="launch_failed", traceback=traceback.format_exc()); self.persist(); raise
        item = dict(process=process, log=log, row=row, start=time.monotonic())
        self.children.append(item)
        row.update(status="running", pid=process.pid)
        self.persist()
        return item

    def finish(self, item):
        code = item["process"].wait(); item["log"].close(); self.children.remove(item)
        item["row"].update(status="complete" if code==0 else "failed", exit_code=code,
            ended_utc=stamp(), duration_seconds=time.monotonic()-item["start"], log_sha256=sha256(item["row"]["log_path"]))
        self.persist()
        return code

    def execute(self, name, command, output, tolerate_failure=False):
        require(not Path(output).exists(), "Stage output must be fresh: "+str(output))
        item = self.start(name,command)
        while item["process"].poll() is None:
            time.sleep(min(self.args.poll_seconds, 2.))
        code = self.finish(item)
        self.check_sources()
        if not tolerate_failure:
            require(code==0 and Path(output).exists(), "Orchestration stage failed: "+name)
        return code, item["row"]

    def campaign(self, phase, jobs, out, prior_roots, selections_path=None):
        prior_charge, prior_runs = launcher.prior_accounting(prior_roots)
        require(len(prior_runs)+len(jobs)<=MAX_ATTEMPTS, "Resource-amended 113-attempt ceiling exceeded")
        require(not out.exists(), "Campaign output must be fresh")
        out.mkdir(parents=True,exist_ok=False)
        for child in ("configs","logs","runs"): (out/child).mkdir()
        manifest = launcher.campaign_manifest(phase,prior_roots,selections_path)
        # Preserve exactly the original seven scientific source hashes; the
        # controller/resource amendment is separate provenance, never substituted.
        require(set(manifest["source_sha256"]) == set(read_json(self.paths["primary"]/"manifest.json")["source_sha256"]),
                "Frozen seven-source campaign manifest changed")
        manifest.update(execution_controller=dict(path=str(Path(__file__).resolve()), sha256=self.frozen[Path(__file__).name],
            dependency_sha256=self.frozen), resource_override=dict(default_device="cuda:0", policy_path=str(self.policy_path),
            authority_receipt=str(Path(self.args.release_receipt).resolve()), authority_sha256=sha256(self.args.release_receipt),
            maximum_attempts=MAX_ATTEMPTS, scientific_controls_changed=False))
        write_json(out/"manifest.json",manifest)
        value = dict(manifest,status="running",jobs=jobs,prior_integration_seconds=prior_charge,
            charged_integration_seconds=0.,started_utc=stamp())
        charged = 0.; active = {}
        for job in jobs:
            runner = job.setdefault("runner", "activation_circle_fast_run.py" if self.args.fast_moment_runner and
                                    job["config"]["model"] == "moment" and phase != "repeat" else "activation_circle_run.py")
            require(runner in ("activation_circle_run.py", "activation_circle_fast_run.py"), "Unrecognized runner")
            if runner == "activation_circle_fast_run.py": job["config"].setdefault("execution_backend", "batched_graphs")
            job["runner_sha256"] = self.frozen[runner]
            job.update(run_directory=str(out/"runs"/job["run_id"]),config_path=str(out/"configs"/(job["run_id"]+".json")),
                       log_path=str(out/"logs"/(job["run_id"]+".log")))
            write_json(job["config_path"],job["config"])
        def persist():
            value.update(charged_integration_seconds=charged,total_with_prior_integration_seconds=prior_charge+charged,
                active_reserved_integration_seconds=sum(item["job"]["reserved_integration_seconds"] for item in active.values()),updated_utc=stamp())
            write_json(out/"campaign.json",value)
        def finish_job(device):
            nonlocal charged
            item=active.pop(device);job=item["job"];code=self.finish(item)
            directory=Path(job["run_directory"])
            lifecycle=launcher.read_json_if_present(directory/"lifecycle.json") or {}
            summary=launcher.read_json_if_present(directory/"summary.json")
            if summary: cost=summary["integration_with_observations_seconds"]
            elif "integration_with_observations_seconds" in lifecycle: cost=lifecycle["integration_with_observations_seconds"]
            elif "integration_start_monotonic" in lifecycle: cost=time.monotonic()-lifecycle["integration_start_monotonic"]
            elif (directory/"manifest.json").exists(): cost=job["reserved_integration_seconds"]
            else: cost=0.
            require(cost>=0, "Invalid integration charge")
            charged+=cost
            job.update(status="complete" if code==0 and summary and summary.get("status")!="failed" else "failed",
                exit_code=code,charged_integration_seconds=cost,ended_utc=stamp(),
                subprocess_wall_seconds=time.monotonic()-item["start"],log_sha256=sha256(job["log_path"]))
            if summary: job.update(summary_status=summary["status"],summary_sha256=sha256(directory/"summary.json"))
            if job["status"]=="failed":
                directory.mkdir(parents=True,exist_ok=True)
                if not (directory/"config.json").exists(): write_json(directory/"config.json",job["config"])
                if not (directory/"failure.json").exists():
                    write_json(directory/"failure.json",dict(status="failed",reason=job.get("termination_reason","continuation worker failed"),
                        exit_code=code,charged_integration_seconds=cost,execution_controller=manifest["execution_controller"]))
                write_json(directory/"continuation_launcher_failure.json",{k:v for k,v in job.items() if k!="config"})
            persist()
        persist()
        try:
            while any(job["status"]=="pending" for job in jobs) or active:
                policy=self.policy();allowed=policy["allowed_devices"]
                for device,item in list(active.items()):
                    if item["process"].poll() is not None:
                        finish_job(device);continue
                    if device not in allowed and not item["job"].get("termination_reason"):
                        item["job"]["termination_reason"]="Resource policy withdrew this GPU; no automatic restart"
                        stop_child(item,signal.SIGTERM)
                    lifecycle=launcher.read_json_if_present(Path(item["job"]["run_directory"])/"lifecycle.json") or {}
                    if lifecycle.get("status")=="integrating" and time.monotonic()-lifecycle["integration_start_monotonic"]>=item["job"]["config"]["max_wall_seconds"]+launcher.WATCHDOG_GRACE:
                        item["job"]["termination_reason"]="Integration cap plus reserved watchdog grace exhausted"
                        stop_child(item,signal.SIGKILL)
                for device in allowed:
                    if device in active: continue
                    job=choose_job(jobs,device,allowed)
                    if job is None: continue
                    available=launcher.TOTAL_BUDGET-prior_charge-charged-sum(item["job"]["reserved_integration_seconds"] for item in active.values())
                    cap=job["config"]["max_wall_seconds"]
                    if available<cap+launcher.RESERVATION_GUARD:
                        if not active:
                            for pending in jobs:
                                if pending["status"]=="pending":pending.update(status="budget_skipped",skip_reason="Remaining integration budget cannot reserve a complete run")
                        continue
                    self.check_sources()
                    assignment_policy=self.policy()
                    if device not in assignment_policy["allowed_devices"]:
                        continue
                    original_device=job["config"]["device"]
                    job["config"]["device"]=device
                    job.update(status="running",started_utc=stamp(),reserved_integration_seconds=cap+launcher.RESERVATION_GUARD,
                        resource_assignment=dict(requested_device=original_device,actual_device=device,policy=assignment_policy,
                            cross_gpu_repetition_planned=(device==original_device) if phase=="repeat" else None))
                    write_json(job["config_path"],job["config"]);job["config_sha256"]=sha256(job["config_path"])
                    command=[sys.executable,str(FOLDER/job["runner"]),"--config",job["config_path"],"--out",job["run_directory"]]
                    try:
                        item=self.start(phase+"_"+job["run_id"],command,job["log_path"])
                    except OSError as error:
                        directory=Path(job["run_directory"]);directory.mkdir(parents=True,exist_ok=True)
                        write_json(directory/"config.json",job["config"])
                        write_json(directory/"failure.json",dict(status="failed",reason="subprocess launch failed",message=str(error)))
                        job.update(status="failed",charged_integration_seconds=0.,launch_error=str(error));persist();continue
                    item["job"]=job;job["pid"]=item["process"].pid;active[device]=item;persist()
                persist()
                if active:time.sleep(.2)
            value["status"]="complete"
        except BaseException:
            value["status"]="interrupted"
            for item in active.values():
                if item["process"].poll() is None:
                    try:os.killpg(item["process"].pid,signal.SIGTERM)
                    except ProcessLookupError:pass
            for device in list(active):finish_job(device)
            for job in jobs:
                if job["status"]=="pending":job["status"]="cancelled_before_launch"
            raise
        finally:
            value["ended_utc"]=stamp();persist()
        require(prior_charge+charged<=launcher.TOTAL_BUDGET, "Integration budget exceeded")
        return value

    def analyze(self, name, roots, out):
        self.execute(name,[sys.executable,str(FOLDER/"analyze_activation_circle.py"),"--runs",*map(str,roots),"--out",str(out)],out)
        result=read_json(out/"metrics_summary.json")
        self.receipt[name]=dict(path=str(out),metrics_sha256=sha256(out/"metrics_summary.json"));self.persist()
        return result

    def audit(self, roots, origins, repeated_jobs):
        out=self.paths["audit"];out.mkdir(parents=True,exist_ok=False)
        runs=[];excluded=[];seen=set()
        for root in roots:
            campaign=read_json(root/"campaign.json")
            require(campaign["status"] in ("complete","interrupted"),"Audit requires finalized campaigns")
            for job in campaign["jobs"]:
                directory=Path(job["run_directory"]).resolve()
                if directory in seen:continue
                seen.add(directory);summary_path=directory/"summary.json"
                if not summary_path.exists():
                    excluded.append(dict(path=str(directory),status=job["status"],reason="No completed saved-state summary"));continue
                try:
                    summary=read_json(summary_path)
                    if summary.get("status")=="failed":
                        excluded.append(dict(path=str(directory),status="failed"));continue
                    query_count=summary.get("query_count",8192)
                    require(isinstance(query_count,int) and not isinstance(query_count,bool) and query_count>0,"Invalid replay query count")
                    weight=max(1,len(summary.get("observations",[])))*query_count
                except (OSError,ValueError,TypeError,AttributeError):weight=12*8192
                runs.append(dict(path=str(directory),weight=weight))
        runs.sort(key=lambda row:(-row["weight"],row["path"]))
        batches=[runs[i:i+4] for i in range(0,len(runs),4)]
        self.receipt["replay_plan"]=dict(batches=batches,excluded=excluded);self.persist()
        pending=list(enumerate(batches));active={};records=[]
        while pending or active:
            policy=self.policy();allowed=policy["allowed_devices"]
            for device,item in list(active.items()):
                if item["process"].poll() is None:
                    if device not in allowed:
                        stop_child(item,signal.SIGTERM)
                    continue
                code=self.finish(item);active.pop(device)
                output=item["output"]
                if code==0 and output.exists():
                    batch_result=read_json(output)
                    require(isinstance(batch_result,list) and len(batch_result)==len(item["batch"]) and {str(Path(row["run"]).resolve()) for row in batch_result}=={row["path"] for row in item["batch"]},"Replay output inventory differs")
                else:
                    batch_result=[dict(run=row["path"],passed=False,failures=["replay_subprocess_failed"],exit_code=code,log_path=item["row"]["log_path"]) for row in item["batch"]]
                    failure_output=output.with_suffix(".failure.json");require(not failure_output.exists(),"Replay failure evidence already exists");write_json(failure_output,batch_result)
                records.extend(batch_result)
            for device in allowed:
                if device in active or not pending:continue
                if device not in self.policy()["allowed_devices"]:continue
                index,batch=pending.pop(0);output=out/f"replay_batch_{index:03d}.json"
                item=self.start(f"replay_batch_{index:03d}",[sys.executable,str(FOLDER/"check_activation_circle.py"),"replay",*[row["path"] for row in batch],"--device",device,"--output",str(output)])
                item.update(output=output,batch=batch);active[device]=item
            if active:time.sleep(.5)
        self.receipt["replay_results"]=records
        plan=workflow.reproduction_plan(origins,repeated_jobs,out)
        self.receipt["reproduction_plan"]=plan;self.persist()
        reproductions=[]
        for index,pair in enumerate(plan):
            code,stage=self.execute(f"reproduction_{index:02d}",pair["command"],pair["output"],tolerate_failure=True)
            try:
                require(code==0,"Reproduction checker did not complete")
                result=read_json(pair["output"])
                require(isinstance(result,dict) and "passed" in result,"Malformed reproduction result")
            except (OSError,ValueError,TypeError) as error:
                result=dict(original=pair["original"],repeated=pair["repeated"],passed=False,
                    failures=["reproduction_unavailable"],error=str(error),exit_code=code,log_path=stage["log_path"])
                failure_output=Path(pair["output"]).with_suffix(".failure.json")
                require(not failure_output.exists(),"Reproduction failure evidence already exists");write_json(failure_output,result)
            reproductions.append(dict(output=pair["output"],raw_result=result,resource_amended_assessment=reproduction_assessment(result)))
        self.receipt["reproduction_results"]=reproductions
        self.receipt["cross_gpu_reproduction_coverage_count"]=sum(row["resource_amended_assessment"]["cross_gpu_covered"] for row in reproductions)
        self.receipt["numerical_reproduction_pass_count"]=sum(row["resource_amended_assessment"]["numerical_prefix_state_and_event_checks_passed"] for row in reproductions)
        failures=any(row.get("passed") is not True for row in records) or any(not row["resource_amended_assessment"]["numerical_prefix_state_and_event_checks_passed"] for row in reproductions)
        self.receipt["status"]="complete_with_audit_failures" if failures else "complete_resource_amended"
        self.persist()

    def run(self):
        cases=read_json(FOLDER/"activation_circle_cases.json")
        release=read_json(self.args.release_receipt)
        while True:
            old=read_json(self.paths["primary"]/"campaign.json")
            if old.get("status")=="interrupted":break
            require(old.get("status") in ("running","starting"),"Unexpected old primary finalization status")
            self.policy();time.sleep(self.args.poll_seconds)
        pilot=read_json(self.paths["pilot"]/"campaign.json")
        require(pilot["status"]=="complete","Pilots are not finalized")
        completed=[read_json(root/"campaign.json") for root in self.completed_roots]
        for previous in (old,pilot,*completed):
            require(all(self.frozen.get(name)==digest for name,digest in previous["source_sha256"].items()),"Frozen source hashes differ from original campaign")
        jobs,interrupted=continuation_jobs(cases,old,release)
        jobs=remaining_jobs(jobs,completed)
        prior_roots=[self.paths["pilot"],self.paths["primary"],*self.completed_roots]
        charge,attempts=launcher.prior_accounting(prior_roots)
        self.receipt.update(status="continuing_primary_on_authorized_resources",release_receipt_sha256=sha256(self.args.release_receipt),
            interrupted_run=interrupted,prior_integration_seconds=charge,prior_attempt_count=len(attempts),
            old_primary_campaign_sha256=sha256(self.paths["primary"]/"campaign.json"));self.persist()
        continuation=self.campaign("primary",jobs,self.paths["continuation"],prior_roots)
        self.receipt["primary_completion"]=logical_primary_complete(cases,old,continuation,interrupted,completed)
        prior_roots.append(self.paths["continuation"])
        science_roots=[self.paths["primary"],*self.completed_roots,self.paths["continuation"]]
        metrics=self.analyze("analysis_primary",science_roots,self.paths["analysis_primary"])
        selections=workflow.refinement_selections(metrics,cases)
        selection_path=self.out/"refine_selections.json";write_json(selection_path,selections)
        self.receipt["refinement_selection"]=dict(path=str(selection_path),sha256=sha256(selection_path),requests=metrics["required_refinements"])
        if selections:
            _,prior=launcher.prior_accounting(prior_roots)
            refined_jobs=launcher.build_jobs("refine",cases,selections,prior)
            self.campaign("refine",refined_jobs,self.paths["refine"],prior_roots,selection_path)
            prior_roots.append(self.paths["refine"]);science_roots.append(self.paths["refine"])
        final=self.analyze("analysis_final",science_roots,self.paths["analysis_final"])
        self.receipt["remaining_refinement_requests_not_executed"]=final.get("required_refinements",[])
        _,prior=launcher.prior_accounting(prior_roots)
        repeat_selections,origins=workflow.repeat_selections(cases,prior)
        repeat_path=self.out/"repeat_selections.json";write_json(repeat_path,repeat_selections)
        repeat_jobs=launcher.build_jobs("repeat",cases,repeat_selections,prior)
        repeat_runners(repeat_jobs,origins,prior)
        repeated=self.campaign("repeat",repeat_jobs,self.paths["repeat"],prior_roots,repeat_path)
        self.receipt["repetition_origins"]=origins;prior_roots.append(self.paths["repeat"])
        total,all_attempts=launcher.prior_accounting(prior_roots)
        require(total<=launcher.TOTAL_BUDGET and len(all_attempts)<=MAX_ATTEMPTS,"Final resource-amended budget exceeded")
        self.receipt["final_accounting"]=dict(integration_seconds=total,executed_attempts=len(all_attempts),maximum_attempts=MAX_ATTEMPTS)
        self.audit(prior_roots,origins,repeated["jobs"])
        self.receipt.update(finished_utc=stamp());self.persist()
        return self.receipt

    def abort(self, error):
        self.receipt.update(status="orchestration_failed",error_type=type(error).__name__,error=str(error),traceback=traceback.format_exc())
        for item in list(self.children):
            if item["process"].poll() is None:
                try:os.killpg(item["process"].pid,signal.SIGTERM)
                except ProcessLookupError:pass
            self.finish(item)
        self.persist()


def parser():
    result=argparse.ArgumentParser(description=__doc__)
    result.add_argument("--out",required=True)
    result.add_argument("--primary-root",default=str(GENERATED/"activation_circle_primary01"))
    result.add_argument("--pilot-root",default=str(GENERATED/"activation_circle_pilot01"))
    result.add_argument("--release-receipt",default=str(GENERATED/"activation_circle_finish01/user_gpu_release01.json"))
    result.add_argument("--resource-policy")
    result.add_argument("--completed-roots",nargs="*",default=[])
    result.add_argument("--generation",type=int,default=2)
    result.add_argument("--fast-moment-runner",action="store_true")
    result.add_argument("--poll-seconds",type=float,default=15.)
    return result


if __name__=="__main__":
    signal.signal(signal.SIGTERM,workflow.termination_requested)
    controller=Controller(parser().parse_args())
    try:controller.run()
    except BaseException as error:
        controller.abort(error)
        raise
