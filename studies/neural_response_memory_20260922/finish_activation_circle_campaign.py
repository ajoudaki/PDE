"""Execute only the already frozen activation campaign's remaining stages.

The lead launches this coordinator. It waits for all 64 primary attempts,
analyzes, conditionally refines once, analyzes again, repeats the eight declared
pairs, and replays saved states with one independent checker process per GPU.
No result changes tolerances, budgets, cases or the frozen producer sources.
"""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

import run_activation_circle_campaign as launcher


FOLDER = Path(__file__).resolve().parent
REPOSITORY = FOLDER.parents[1]
GENERATED = REPOSITORY / "data/generated/neural_response_memory_20260922"
SOURCES = (
    "finish_activation_circle_campaign.py", "run_activation_circle_campaign.py",
    "activation_circle_run.py", "activation_moment_engine.py", "deep_moment_engine.py",
    "moment_engine.py", "analyze_activation_circle.py", "analyze_deep_circle.py",
    "check_activation_circle.py", "ACTIVATION_CIRCLE_PROTOCOL.md", "activation_circle_cases.json",
)
TERMINAL_ATTEMPTS = {"complete", "failed"}
NOT_EXECUTED = {"pending", "budget_skipped", "cancelled_before_launch"}


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def write_json(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def primary_complete(campaign, root, cases):
    """A complete campaign must contain every planned terminal attempt once."""
    status = campaign.get("status")
    if status in ("running", "starting"):
        return False
    require(status == "complete", "Primary campaign did not complete: " + str(status))
    expected = {job["run_id"]: job["config"] for job in launcher.build_jobs("primary", cases)}
    jobs = campaign.get("jobs", [])
    require(len(jobs) == 64 and len({job["run_id"] for job in jobs}) == 64,
            "Primary campaign must contain 64 unique scheduled attempts")
    require(set(expected) == {job["run_id"] for job in jobs}, "Primary schedule differs from frozen cases")
    for job in jobs:
        require(job["config"] == expected[job["run_id"]], "Primary config differs from frozen schedule")
        require(job["status"] in TERMINAL_ATTEMPTS, "Primary attempt was not finished: " + job["run_id"])
        directory = Path(job["run_directory"]).resolve()
        require(directory == (Path(root) / "runs" / job["run_id"]).resolve(), "Primary attempt path mismatch")
        require((directory / "config.json").is_file(), "Finished primary attempt lacks config")
        require(read_json(directory / "config.json") == job["config"], "Primary saved config differs from scheduled config")
        require((directory / "summary.json").is_file() or (directory / "failure.json").is_file(),
                "Finished primary attempt lacks summary/failure receipt")
    return True


def refinement_selections(metrics, cases):
    require(metrics.get("primary_schedule_complete") is True and
            metrics.get("finished_primary_attempts") == 64 and
            metrics.get("refinement_decisions_provisional") is False,
            "Refinement decisions require all 64 finished primary attempts")
    selected, seen = [], set()
    for request in metrics["required_refinements"]:
        case, model = request["case"], request["model"]
        require(case in cases and model in ("dense", "P1", "P2", "P3"), "Invalid refinement identity")
        require(request.get("conditional_run_available") is True and
                request.get("action") == "one_predeclared_refinement" and
                request["requested_rtol"] == launcher.TOLERANCES[2] and
                request["requested_atol"] == launcher.TOLERANCES[2] / 100,
                "Refinement request is not the single predeclared third tolerance")
        require((case, model) not in seen, "Duplicate refinement request")
        seen.add((case, model))
        selected.append(dict(case=case, model="dense" if model == "dense" else "moment",
                             order=1 if model == "dense" else int(model[1:]), rtol=launcher.TOLERANCES[2]))
    require(len(selected) <= 32, "Too many conditional refinements")
    require(all(model == "dense" or (case, "dense") in seen for case, model in seen),
            "Frozen analyzer omitted a required paired dense refinement")
    return selected


def repeat_selections(cases, prior_runs):
    """Match the launcher's finest attempted resolution, including failed attempts."""
    prior_runs = [row for row in prior_runs if row.get("status") not in NOT_EXECUTED]
    selected, origins = [], []
    for case, literal in cases.items():
        if literal["task"] != "two_outliers_alternating":
            continue
        for model, order in (("dense", 1), ("moment", 3)):
            originals = [row for row in prior_runs if
                         row.get("status") not in NOT_EXECUTED and
                         (row.get("config", {}).get("case"), row.get("config", {}).get("model"),
                          row.get("config", {}).get("order", 1)) == (case, model, order) and
                         row["config"].get("phase") in ("primary", "refine")]
            require(originals, "No executed original for repetition: " + case + "/" + model)
            finest = min(row["config"]["rtol"] for row in originals)
            original = next(row for row in reversed(originals) if row["config"]["rtol"] == finest)
            selected.append(dict(case=case, model=model, order=order, rtol=finest))
            origins.append(dict(selection=selected[-1], original=original["run_directory"],
                                original_status=original["status"], original_device=original["config"]["device"],
                                repeated_device="cuda:1" if original["config"]["device"] == "cuda:0" else "cuda:0"))
    require(len(selected) == 8, "Repetition requires exactly eight declared outlier pairs")
    launcher.build_jobs("repeat", cases, selected, prior_runs)
    return selected, origins


def replay_batches(campaign_roots):
    """Balance observation panels without consulting scientific performance."""
    runs, excluded, seen = [], [], set()
    for root in campaign_roots:
        campaign = read_json(Path(root) / "campaign.json")
        require(campaign.get("status") == "complete", "Replay requires a finalized campaign")
        for job in campaign["jobs"]:
            directory = Path(job["run_directory"]).resolve()
            if directory in seen:
                continue
            seen.add(directory)
            summary_path = directory / "summary.json"
            if summary_path.is_file():
                try:
                    summary = read_json(summary_path)
                    if summary.get("status") != "failed":
                        query_count = summary.get("query_count", 8192)
                        require(isinstance(query_count, int) and query_count > 0, "Invalid replay query count")
                        weight = max(1, len(summary.get("observations", []))) * query_count
                        runs.append(dict(path=str(directory), weight=weight, summary_sha256=sha256(summary_path)))
                        continue
                except (OSError, ValueError, TypeError, AttributeError) as error:
                    # The independent checker preserves per-run exceptions. A
                    # malformed summary must not prevent healthy run replay.
                    runs.append(dict(path=str(directory), weight=12 * 8192,
                                     summary_parse_error=type(error).__name__ + ": " + str(error)))
                    continue
            excluded.append(dict(path=str(directory), campaign_status=job["status"],
                                 reason="No successful saved trajectory summary; failed/skipped attempt preserved"))
    batches, weights = [[], []], [0, 0]
    for row in sorted(runs, key=lambda row: (-row["weight"], row["path"])):
        index = min(range(2), key=lambda i: (weights[i], i))
        batches[index].append(row)
        weights[index] += row["weight"]
    return batches, weights, excluded


def destinations(args):
    base = Path(args.primary_root).resolve().parent
    return dict(finish=Path(args.out).resolve(), primary=Path(args.primary_root).resolve(),
                pilot=Path(args.pilot_root).resolve(), analysis_primary=base / "activation_circle_analysis_primary01",
                refine=base / "activation_circle_refine01", analysis_final=base / "activation_circle_analysis_final01",
                repeat=base / "activation_circle_repeat01", audit=base / "activation_circle_audit01")


def reproduction_path(audit, index, selection):
    model = "dense" if selection["model"] == "dense" else "P" + str(selection["order"])
    return Path(audit) / f"reproduction_{index:02d}_{selection['case']}_{model}_01.json"


def reproduction_plan(origins, repeated_jobs, audit):
    plan = []
    for index, origin in enumerate(origins):
        selection = origin["selection"]
        matching = [job for job in repeated_jobs if all(job["config"][key] == value for key, value in selection.items())]
        require(len(matching) == 1, "Repetition must map to exactly one scheduled attempt")
        job = matching[0]
        output = reproduction_path(audit, index, selection)
        plan.append(dict(original=origin["original"], repeated=job["run_directory"],
                         repeated_status=job["status"], selection=selection, output=str(output),
                         command=[sys.executable, str(FOLDER / "check_activation_circle.py"), "reproduction",
                                  origin["original"], job["run_directory"], "--output", str(output)]))
    require(len(plan) == 8, "Exactly eight reproduction audit pairs are required")
    return plan


def run(args):
    paths = destinations(args)
    cases = read_json(FOLDER / "activation_circle_cases.json")
    require(0 < args.poll_seconds <= 60, "Polling interval must lie in (0,60] seconds")
    for name in ("finish", "analysis_primary", "refine", "analysis_final", "repeat"):
        require(not paths[name].exists(), "Output must be fresh: " + str(paths[name]))
    for index in (0, 1):
        require(not (paths["audit"] / f"replay_gpu{index}_01.json").exists(), "Replay evidence already exists")
    pairs = [dict(case=case, model=model, order=order) for case, literal in cases.items()
             if literal["task"] == "two_outliers_alternating" for model, order in (("dense", 1), ("moment", 3))]
    for index, selection in enumerate(pairs):
        output = reproduction_path(paths["audit"], index, selection)
        require(not output.exists() and not output.with_suffix(".failure.json").exists(), "Reproduction evidence already exists")
    require(paths["primary"].is_dir() and paths["pilot"].is_dir(), "Primary and pilot roots must exist")
    pilot = read_json(paths["pilot"] / "campaign.json")
    require(pilot.get("status") == "complete", "Pilots must be finalized")
    paths["finish"].mkdir(parents=True, exist_ok=False)
    (paths["finish"] / "logs").mkdir()
    frozen = {name: sha256(FOLDER / name) for name in SOURCES}
    receipt = dict(status="waiting_for_primary", created_utc=stamp(), pid=os.getpid(),
                   source_sha256=frozen, command=sys.argv, python_executable=sys.executable,
                   paths={name: str(value) for name, value in paths.items()}, stages=[],
                   scope="Frozen orchestration and saved-state audit; no scientific verdict or new branch")
    environment = dict(os.environ)
    environment.update({name: "1" for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                       "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS", "PYTHONDONTWRITEBYTECODE")})
    environment["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
    active = []

    def persist():
        receipt["updated_utc"] = stamp()
        write_json(paths["finish"] / "workflow_receipt.json", receipt)

    def check_sources():
        require(all(sha256(FOLDER / name) == expected for name, expected in frozen.items()),
                "A frozen orchestration/analysis/producer source changed")

    def start_stage(name, command, expected_output):
        check_sources()
        require(not Path(expected_output).exists(), "Stage output must be fresh: " + str(expected_output))
        log_path = paths["finish"] / "logs" / (name + ".log")
        row = dict(name=name, status="starting", command=list(map(str, command)),
                   expected_output=str(expected_output), log_path=str(log_path), started_utc=stamp())
        receipt["stages"].append(row)
        persist()
        log = log_path.open("xb")
        try:
            process = subprocess.Popen(row["command"], stdout=log, stderr=subprocess.STDOUT,
                                       cwd=REPOSITORY, env=environment, start_new_session=True)
        except BaseException:
            log.close()
            row.update(status="launch_failed", ended_utc=stamp(), traceback=traceback.format_exc())
            persist()
            raise
        item = dict(process=process, log=log, row=row, start=time.monotonic())
        active.append(item)
        row.update(status="running", pid=process.pid)
        persist()
        print(json.dumps(dict(event="stage_started", name=name, pid=process.pid)), flush=True)
        return item

    def finish_stage(item):
        code = item["process"].wait()
        item["log"].close()
        active.remove(item)
        row = item["row"]
        output = Path(row["expected_output"])
        row.update(exit_code=code, duration_seconds=time.monotonic() - item["start"], ended_utc=stamp(),
                   status="complete" if code == 0 and output.exists() else "failed",
                   log_sha256=sha256(row["log_path"]))
        if output.is_file():
            row["output_sha256"] = sha256(output)
        persist()
        print(json.dumps(dict(event="stage_finished", name=row["name"], status=row["status"])), flush=True)
        return row["status"] == "complete"

    def execute(name, command, expected_output):
        item = start_stage(name, command, expected_output)
        while item["process"].poll() is None:
            time.sleep(min(args.poll_seconds, 5.))
        require(finish_stage(item), "Orchestration stage failed: " + name)
        check_sources()

    def analyze(name, roots, out):
        execute(name, [sys.executable, str(FOLDER / "analyze_activation_circle.py"),
                       "--runs", *map(str, roots), "--out", str(out)], out)
        metrics_path = out / "metrics_summary.json"
        require(metrics_path.is_file(), "Analysis did not produce metrics_summary.json")
        receipt[name] = dict(metrics_path=str(metrics_path), metrics_sha256=sha256(metrics_path))
        return read_json(metrics_path)

    def campaign(phase, selection_path, out, prior_roots):
        execute(phase, [sys.executable, str(FOLDER / "run_activation_circle_campaign.py"),
                       "--phase", phase, "--selections", str(selection_path), "--out", str(out),
                       "--prior-roots", *map(str, prior_roots)], out)
        value = read_json(out / "campaign.json")
        require(value.get("status") == "complete", "Campaign failed to finalize: " + phase)
        require(all(job["status"] in TERMINAL_ATTEMPTS | {"budget_skipped"} for job in value["jobs"]),
                "Campaign contains unfinished jobs: " + phase)
        receipt[phase] = dict(campaign_sha256=sha256(out / "campaign.json"),
                             statuses={status: sum(job["status"] == status for job in value["jobs"])
                                       for status in sorted({job["status"] for job in value["jobs"]})},
                             total_with_prior_integration_seconds=value["total_with_prior_integration_seconds"])
        return value

    started = time.monotonic()
    persist()
    try:
        while True:
            primary = read_json(paths["primary"] / "campaign.json")
            if primary_complete(primary, paths["primary"], cases):
                break
            receipt["primary_snapshot"] = dict(status=primary.get("status"),
                finished=sum(job["status"] in TERMINAL_ATTEMPTS for job in primary.get("jobs", [])))
            persist()
            time.sleep(args.poll_seconds)
        check_sources()
        for previous in (pilot, primary):
            require(previous.get("source_sha256"), "A previous campaign lacks frozen source hashes")
            require(all(frozen.get(name) == digest for name, digest in previous["source_sha256"].items()),
                    "Previous campaign sources differ from the frozen continuation sources")
        receipt.update(status="executing_remaining_stages", primary_campaign_sha256=sha256(paths["primary"] / "campaign.json"))
        persist()
        prior_roots = [paths["pilot"], paths["primary"]]
        science_roots = [paths["primary"]]
        metrics = analyze("analysis_primary", science_roots, paths["analysis_primary"])
        selections = refinement_selections(metrics, cases)
        selection_path = paths["finish"] / "refine_selections.json"
        write_json(selection_path, selections)
        receipt["refinement_selection"] = dict(path=str(selection_path), sha256=sha256(selection_path),
                                               count=len(selections), requests=metrics["required_refinements"])
        if selections:
            campaign("refine", selection_path, paths["refine"], prior_roots)
            prior_roots.append(paths["refine"])
            science_roots.append(paths["refine"])
        else:
            receipt["refine"] = dict(status="not_requested", reason="Frozen analyzer requested no conditional third tolerance")
        final_metrics = analyze("analysis_final", science_roots, paths["analysis_final"])
        receipt["remaining_refinement_requests_not_executed"] = final_metrics.get("required_refinements", [])
        # This is the final science analysis. A residual request is recorded and
        # never starts a second refinement, retries a failure, or rescues a cap.
        prior_charge, prior_runs = launcher.prior_accounting(prior_roots)
        repeats, origins = repeat_selections(cases, prior_runs)
        repeat_path = paths["finish"] / "repeat_selections.json"
        write_json(repeat_path, repeats)
        receipt["repetition_selection"] = dict(path=str(repeat_path), sha256=sha256(repeat_path),
                                               origins=origins, prior_integration_seconds=prior_charge)
        repeat_campaign = campaign("repeat", repeat_path, paths["repeat"], prior_roots)
        prior_roots.append(paths["repeat"])
        total_charge, all_attempts = launcher.prior_accounting(prior_roots)
        require(total_charge <= launcher.TOTAL_BUDGET and len(all_attempts) <= 112,
                "Final campaign accounting exceeds a frozen bound")
        receipt["final_accounting"] = dict(integration_seconds=total_charge, executed_attempts=len(all_attempts))
        # Pilots are included only in this independent saved-state replay.
        batches, weights, excluded = replay_batches(prior_roots)
        receipt["replay_plan"] = dict(batches=batches, estimated_panel_weights=weights, excluded=excluded)
        paths["audit"].mkdir(parents=True, exist_ok=True)
        workers = []
        for index, batch in enumerate(batches):
            output = paths["audit"] / f"replay_gpu{index}_01.json"
            command = [sys.executable, str(FOLDER / "check_activation_circle.py"), "replay",
                       *[row["path"] for row in batch], "--device", f"cuda:{index}", "--output", str(output)]
            workers.append(start_stage(f"replay_gpu{index}", command, output))
        while any(item["process"].poll() is None for item in workers):
            time.sleep(min(args.poll_seconds, 5.))
        worker_success = [finish_stage(item) for item in workers]
        require(all(worker_success), "An independent replay subprocess failed; existing evidence is preserved")
        check_sources()
        audit_failures = []
        for index, batch in enumerate(batches):
            output = paths["audit"] / f"replay_gpu{index}_01.json"
            records = read_json(output)
            require(isinstance(records, list) and len(records) == len(batch), "Incomplete replay worker inventory")
            require({str(Path(row["run"]).resolve()) for row in records} == {row["path"] for row in batch},
                    "Replay worker returned the wrong saved-run inventory")
            audit_failures.extend(row for row in records if row.get("passed") is not True)
        receipt["reproduction_plan"] = reproduction_plan(origins, repeat_campaign["jobs"], paths["audit"])
        reproduction_results = []
        for index, pair in enumerate(receipt["reproduction_plan"]):
            item = start_stage(f"reproduction_{index:02d}", pair["command"], pair["output"])
            while item["process"].poll() is None:
                time.sleep(min(args.poll_seconds, 5.))
            completed = finish_stage(item)
            check_sources()
            try:
                require(completed, "Checker exited unsuccessfully or produced no reproduction evidence")
                result = read_json(pair["output"])
                require(isinstance(result, dict) and "passed" in result, "Invalid reproduction checker output")
            except (OSError, ValueError, TypeError) as error:
                # A failed/missing original or repetition remains a failed audit
                # record. The other seven comparisons are independent checks.
                result = dict(original=pair["original"], repeated=pair["repeated"], passed=False,
                              failures=["reproduction_checker_failed_or_unavailable"],
                              error=type(error).__name__ + ": " + str(error), command=pair["command"],
                              exit_code=item["row"].get("exit_code"), log_path=item["row"]["log_path"],
                              receipt_source="finish coordinator; original checker evidence preserved")
                failure_output = Path(pair["output"]).with_suffix(".failure.json")
                require(not failure_output.exists(), "Reproduction failure receipt already exists")
                write_json(failure_output, result)
                result["failure_receipt"] = str(failure_output)
            reproduction_results.append(dict(output=pair["output"], **result))
        receipt["reproduction_results"] = reproduction_results
        reproduction_failures = [row for row in reproduction_results if row.get("passed") is not True]
        receipt.update(status="complete" if not audit_failures else "complete_with_audit_failures",
                       replay_failures=audit_failures, replayed_run_count=sum(map(len, batches)),
                       reproduction_failures=reproduction_failures,
                       finished_utc=stamp(), duration_seconds=time.monotonic() - started)
        if reproduction_failures:
            receipt["status"] = "complete_with_audit_failures"
        persist()
        return receipt
    except BaseException as error:
        receipt.update(status="orchestration_failed", error_type=type(error).__name__, error=str(error),
                       traceback=traceback.format_exc(), finished_utc=stamp(), duration_seconds=time.monotonic() - started)
        # SIGINT lets an active frozen launcher terminate and account for its
        # own children. This coordinator does not send SIGKILL to training jobs.
        for item in list(active):
            if item["process"].poll() is None:
                try:
                    os.killpg(item["process"].pid, signal.SIGINT)
                except ProcessLookupError:
                    pass
            finish_stage(item)
        persist()
        raise


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--out", required=True)
    result.add_argument("--primary-root", default=str(GENERATED / "activation_circle_primary01"))
    result.add_argument("--pilot-root", default=str(GENERATED / "activation_circle_pilot01"))
    result.add_argument("--poll-seconds", type=float, default=15.)
    return result


def termination_requested(signum, frame):
    raise KeyboardInterrupt("Termination signal " + str(signum) + " received")


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, termination_requested)
    run(parser().parse_args())
