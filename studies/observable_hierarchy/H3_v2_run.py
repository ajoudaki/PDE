"""Budget supervisor for the predeclared author validation plan."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import psutil


def run(plan_path, output):
    plan = json.loads(plan_path.read_text())
    output.mkdir(parents=True, exist_ok=False)
    budget = plan["budget"]
    environment = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
    records, consumed_cpu = [], 0.
    here = Path(__file__).resolve().parent
    for config in plan["configurations"]:
        if consumed_cpu >= budget["total_cpu_seconds"]:
            records.append(dict(id=config["id"], status="not_run_total_budget"))
            continue
        directory = output/config["id"]
        cmd = [sys.executable, "-B", str(here/"H3_v2_candidate_loader.py"), str(here/"H3_v2_validate.py"),
               "--plan", str(plan_path), "--id", config["id"], "--output", str(directory)]
        wall = time.monotonic()
        with (output/(config["id"]+".log")).open("w") as log:
            process = subprocess.Popen(cmd, env=environment, stdout=log, stderr=subprocess.STDOUT)
            observer = psutil.Process(process.pid)
            maximum_rss, worker_cpu, stopped = 0, 0., None
            while process.poll() is None:
                try:
                    maximum_rss = max(maximum_rss, observer.memory_info().rss)
                    usage = observer.cpu_times()
                    worker_cpu = usage.user+usage.system
                except psutil.NoSuchProcess:
                    break
                if maximum_rss > budget["rss_bytes_per_process"]:
                    stopped = "rss_budget"
                elif time.monotonic()-wall > budget["wall_seconds_per_configuration"]:
                    stopped = "wall_budget"
                elif consumed_cpu+worker_cpu > budget["total_cpu_seconds"]:
                    stopped = "total_cpu_budget"
                if stopped:
                    process.kill()
                    break
                time.sleep(.1)
            code = process.wait()
        record_path = directory/"record.json"
        worker_record = json.loads(record_path.read_text()) if record_path.exists() else {}
        actual_cpu = max(worker_cpu, worker_record.get("total_seconds", {}).get("cpu", 0))
        consumed_cpu += actual_cpu
        entry = dict(id=config["id"], exit_code=code, stopped=stopped, sampled_peak_rss=maximum_rss,
                     cpu_seconds=actual_cpu, wall_seconds=time.monotonic()-wall,
                     status=worker_record.get("status", "failure_before_record"), command=cmd)
        if code != 0 or stopped:
            entry["status"] = "failure"
        records.append(entry)
        result = dict(plan_sha256=hashlib.sha256(plan_path.read_bytes()).hexdigest(),
                      supervisor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      total_cpu_seconds=consumed_cpu, configurations=records)
        (output/"supervisor.json").write_text(json.dumps(result, indent=2)+"\n")
        print(json.dumps({k: entry[k] for k in ("id", "status", "cpu_seconds", "wall_seconds", "sampled_peak_rss")}), flush=True)
    return int(any(x["status"] == "failure" for x in records))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.plan.resolve(), args.output.resolve()))
