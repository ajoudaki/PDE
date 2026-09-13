"""Run a predeclared observable-solver validation plan serially on Linux.

Install beside validate_observable_solver.py in code/scripts. An optional
--worker selects another worker with the same --plan/--id/--output protocol.
Without that option the existing H3 worker and behavior are unchanged.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import selectors
import signal
import subprocess
import sys
import time

import psutil


MAX_PLAN_BYTES = 1024 * 1024
MAX_RECORD_BYTES = 4 * 1024 * 1024
MAX_LOG_BYTES = 256 * 1024
POLL_SECONDS = 0.05
THREAD_VARIABLES = (
    "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS",
)


def _read_json(path, limit):
    with Path(path).open("rb") as stream:
        payload = stream.read(limit + 1)
    if len(payload) > limit:
        raise ValueError("JSON file exceeds the supervisor's byte allowance")
    return json.loads(payload), hashlib.sha256(payload).hexdigest()


def _positive(value, label, *, integer=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(label + " must be a positive finite number")
    if not math.isfinite(value) or value <= 0 or (integer and not isinstance(value, int)):
        raise ValueError(label + " must be a positive " + ("integer" if integer else "finite number"))
    return value


def _validate_plan(plan):
    budget, configurations = plan["budget"], plan["configurations"]
    maximum = _positive(budget["maximum_configurations"], "maximum_configurations", integer=True)
    if not isinstance(configurations, list) or not 0 < len(configurations) <= maximum:
        raise ValueError("configuration count must be positive and within the declared maximum")
    for key in ("cpu_seconds_per_configuration", "rss_bytes_per_process"):
        _positive(budget[key], key, integer=True)
    for key in ("wall_seconds_per_configuration", "total_cpu_seconds"):
        _positive(budget[key], key)
    if budget["threads_per_process"] != 1 or budget["parallel_trajectory_processes"] != 1:
        raise ValueError("this runner requires one numerical thread and one serial worker")
    names = [configuration["id"] for configuration in configurations]
    if any(not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", name) for name in names):
        raise ValueError("configuration IDs must be safe directory names of at most 80 characters")
    if len(set(names)) != len(names):
        raise ValueError("configuration IDs must be unique")


def _children_cpu():
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    return usage.ru_utime + usage.ru_stime


def _kill(process):
    # A separate session lets interruption also clean up accidental descendants.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def _monitor(process, log_path, budget, consumed_cpu, started):
    observer = psutil.Process(process.pid)
    sampled_rss, sampled_cpu, seen_bytes, saved_bytes = 0, 0.0, 0, 0
    stopped = None
    with log_path.open("xb") as log, selectors.DefaultSelector() as selector:
        os.set_blocking(process.stdout.fileno(), False)
        selector.register(process.stdout, selectors.EVENT_READ)

        def drain():
            nonlocal seen_bytes, saved_bytes
            # One bounded read per iteration keeps resource checks responsive
            # even if the worker continuously floods stdout/stderr.
            try:
                block = os.read(process.stdout.fileno(), 65536)
            except BlockingIOError:
                return False
            if not block:
                if selector.get_map():
                    selector.unregister(process.stdout)
                return False
            seen_bytes += len(block)
            retained = block[:max(0, MAX_LOG_BYTES - saved_bytes)]
            log.write(retained)
            saved_bytes += len(retained)
            return True

        try:
            while process.poll() is None:
                try:
                    sampled_rss = max(sampled_rss, observer.memory_info().rss)
                    usage = observer.cpu_times()
                    sampled_cpu = max(sampled_cpu, usage.user + usage.system)
                except (psutil.NoSuchProcess, psutil.ZombieProcess):
                    pass
                if sampled_rss > budget["rss_bytes_per_process"]:
                    stopped = "rss_budget"
                elif time.monotonic() - started >= budget["wall_seconds_per_configuration"]:
                    stopped = "wall_budget"
                elif sampled_cpu >= budget["cpu_seconds_per_configuration"]:
                    stopped = "cpu_budget"
                elif consumed_cpu + sampled_cpu >= budget["total_cpu_seconds"]:
                    stopped = "total_cpu_budget"
                if stopped:
                    _kill(process)
                    break
                if selector.select(POLL_SECONDS):
                    drain()
        except KeyboardInterrupt:
            stopped = "supervisor_interrupted"
            _kill(process)
        finally:
            # Also reap on unexpected I/O/monitoring exceptions; no child is
            # allowed to outlive the runner after it leaves this block.
            if process.poll() is None:
                _kill(process)
            process.wait()
            _kill(process)
            # The terminated process can leave a finite pipe backlog. The read
            # count bounds cleanup even if a descendant held the pipe open.
            for _ in range(16):
                if not drain():
                    break
            process.stdout.close()
    return dict(exit_code=process.returncode, stopped=stopped,
                sampled_peak_rss=sampled_rss, sampled_cpu_seconds=sampled_cpu,
                wall_seconds=time.monotonic() - started,
                log_bytes_observed=seen_bytes, log_bytes_saved=saved_bytes,
                log_truncated=seen_bytes > saved_bytes)


def _record_summary(path, configuration, plan_hash):
    try:
        record, record_hash = _read_json(path, MAX_RECORD_BYTES)
        if record.get("id") != configuration["id"] or record.get("configuration") != configuration:
            raise ValueError("worker record does not match its configuration")
        if record.get("plan_sha256") != plan_hash:
            raise ValueError("worker record does not match the plan hash")
        cpu = record.get("total_seconds", {}).get("cpu", 0)
        peak_rss = record.get("peak_rss_bytes", 0)
        for value in (cpu, peak_rss):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError("worker resource counters must be finite and nonnegative")
        status = record.get("status")
        if status not in ("running", "failure", "operational_pass"):
            raise ValueError("unrecognized worker status")
        return dict(worker_status=status, record_sha256=record_hash,
                    worker_reported_cpu_seconds=cpu, worker_reported_peak_rss=peak_rss)
    except (OSError, ValueError, TypeError, AttributeError, RecursionError) as exc:
        return dict(worker_status="invalid_or_missing_record", record_error=str(exc)[:512],
                    worker_reported_cpu_seconds=0, worker_reported_peak_rss=0)


def _checkpoint(output, result):
    path = output / "supervisor.json"
    temporary = output / "supervisor.json.tmp"
    temporary.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def _emit(entry):
    # Worker text is kept in capped logs. Parent stdout has one small JSON line
    # per declared configuration, including budget skips.
    fields = ("id", "status", "stopped", "cpu_seconds", "wall_seconds", "sampled_peak_rss")
    print(json.dumps({key: entry[key] for key in fields if key in entry}), flush=True)


def run(plan_path, output_dir, *, worker=None):
    """Execute precisely the listed configurations; return 0 only if all pass."""
    if sys.platform != "linux":
        raise RuntimeError("the validation resource monitor requires Linux")
    plan_path, output = Path(plan_path).resolve(), Path(output_dir).resolve()
    plan, plan_hash = _read_json(plan_path, MAX_PLAN_BYTES)
    _validate_plan(plan)
    here = Path(__file__).resolve().parent
    selected = Path("validate_observable_solver.py") if worker is None else Path(worker)
    worker = (selected if selected.is_absolute() else here / selected).resolve()
    code_root = here.parent
    if not worker.is_file():
        raise FileNotFoundError("selected validation worker is not a file: " + str(worker))
    environment = dict(os.environ)
    environment.update({name: "1" for name in THREAD_VARIABLES})
    environment.update(OMP_DYNAMIC="FALSE", MKL_DYNAMIC="FALSE", PYTHONDONTWRITEBYTECODE="1")
    environment["PYTHONPATH"] = str(code_root) + (os.pathsep + environment["PYTHONPATH"] if environment.get("PYTHONPATH") else "")
    output.mkdir(parents=True, exist_ok=False)
    budget = plan["budget"]
    result = dict(format="observable-validation-supervisor-v1", status="running",
                  plan_sha256=plan_hash, supervisor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  worker_sha256=hashlib.sha256(worker.read_bytes()).hexdigest(),
                  worker=str(worker),
                  plan=str(plan_path), output_dir=str(output), budget=budget,
                  log_limit_bytes_per_configuration=MAX_LOG_BYTES, poll_seconds=POLL_SECONDS,
                  cpu_accounting="Maximum of reaped-child OS CPU, sampled CPU and worker-reported CPU; includes interpreter startup. Parent CPU is separate.",
                  resource_enforcement="Worker RLIMIT_CPU plus sampled CPU/wall/RSS/total CPU stops; sampling can overshoot. Worker artifacts are retained; only parent logs and metadata are capped.",
                  total_cpu_seconds=0.0, configurations=[])
    parent_started = time.process_time()
    _checkpoint(output, result)
    interrupted = False
    try:
        for configuration in plan["configurations"]:
            name = configuration["id"]
            if result["total_cpu_seconds"] >= budget["total_cpu_seconds"]:
                entry = dict(id=name, status="not_run_total_budget")
            else:
                command = [sys.executable, "-B", str(worker), "--plan", str(plan_path),
                           "--id", name, "--output", str(output / name)]
                entry = dict(id=name, command=command, status="failure")
                before_cpu = _children_cpu()
                launched = time.monotonic()
                process = None
                try:
                    process = subprocess.Popen(command, env=environment, stdout=subprocess.PIPE,
                                               stderr=subprocess.STDOUT, start_new_session=True)
                    entry.update(_monitor(process, output / (name + ".log"), budget, result["total_cpu_seconds"], launched))
                except (Exception, KeyboardInterrupt) as exc:
                    if process is not None:
                        _kill(process)
                        process.wait()
                        if process.stdout is not None:
                            process.stdout.close()
                    entry.update(exit_code=process.returncode if process is not None else None,
                                 stopped="supervisor_interrupted" if isinstance(exc, KeyboardInterrupt) else "supervisor_error",
                                 supervisor_error=str(exc)[:512],
                                 sampled_peak_rss=0, sampled_cpu_seconds=0,
                                 wall_seconds=time.monotonic() - launched)
                entry["reaped_cpu_seconds"] = max(0.0, _children_cpu() - before_cpu)
                entry.update(_record_summary(output / name / "record.json", configuration, plan_hash))
                entry["cpu_seconds"] = max(entry["reaped_cpu_seconds"], entry["sampled_cpu_seconds"],
                                            entry["worker_reported_cpu_seconds"])
                result["total_cpu_seconds"] += entry["cpu_seconds"]
                if entry["stopped"] is None:
                    if max(entry["sampled_peak_rss"], entry["worker_reported_peak_rss"]) > budget["rss_bytes_per_process"]:
                        entry["stopped"] = "rss_budget_after_exit"
                    elif entry["wall_seconds"] >= budget["wall_seconds_per_configuration"]:
                        entry["stopped"] = "wall_budget_after_exit"
                    elif entry["cpu_seconds"] >= budget["cpu_seconds_per_configuration"]:
                        entry["stopped"] = "cpu_budget_after_exit"
                    elif result["total_cpu_seconds"] >= budget["total_cpu_seconds"]:
                        entry["stopped"] = "total_cpu_budget_after_exit"
                if entry["exit_code"] == 0 and entry["stopped"] is None and entry["worker_status"] == "operational_pass":
                    entry["status"] = "operational_pass"
                interrupted = entry["stopped"] == "supervisor_interrupted"
            result["configurations"].append(entry)
            _checkpoint(output, result)
            _emit(entry)
            if interrupted:
                break
    except KeyboardInterrupt:
        interrupted = True
    if interrupted:
        recorded = {entry["id"] for entry in result["configurations"]}
        for configuration in plan["configurations"]:
            if configuration["id"] not in recorded:
                entry = dict(id=configuration["id"], status="not_run_interrupted")
                result["configurations"].append(entry)
                _emit(entry)
    result["status"] = "interrupted" if interrupted else ("operational_pass" if all(
        entry["status"] == "operational_pass" for entry in result["configurations"]) else "failure")
    result["parent_cpu_seconds"] = time.process_time() - parent_started
    _checkpoint(output, result)
    return 130 if interrupted else int(result["status"] != "operational_pass")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True, help="predeclared JSON validation plan")
    parser.add_argument("--output-dir", type=Path, required=True, help="fresh directory for records and capped logs")
    parser.add_argument("--worker", type=Path,
                        help="worker filename relative to this script, or absolute path; default validate_observable_solver.py")
    args = parser.parse_args(argv)

    def interrupted(signum, frame):
        raise KeyboardInterrupt

    previous = signal.signal(signal.SIGTERM, interrupted)
    try:
        return run(args.plan, args.output_dir, worker=args.worker)
    finally:
        signal.signal(signal.SIGTERM, previous)


if __name__ == "__main__":
    raise SystemExit(main())
