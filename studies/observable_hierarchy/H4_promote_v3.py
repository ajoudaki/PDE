"""Apply the exact H4 v3 addition explicitly approved in this task.

Predeclared post-install checks: 600 cumulative CPU seconds, 660 wall seconds
per command, 4 GiB, one numerical thread. Run the 67 affected deterministic
tests, the public law example and three new/affected CLI help commands. No
research trajectory or repeated empirical campaign. Record failures and stop.
The short installation transaction holds the shared Git-writer lock; checks
run after releasing it. This script never stages or commits files.
"""
import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
OUTPUT = ROOT / "data/generated/observable_hierarchy/H4_promotion_checks_v3"
RECORD = STUDY / "H4_promotion_record_v3.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write_record(record):
    RECORD.write_text(json.dumps(record, indent=2) + "\n")


def install():
    common = Path(subprocess.check_output(["git", "rev-parse", "--git-common-dir"], cwd=ROOT, text=True).strip())
    common = common if common.is_absolute() else ROOT / common
    with (common / "pde-writer.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT, check=True)
        mapping_path = STUDY / "H4_promotion_mapping_v3_final.json"
        assert digest(mapping_path) == "3aac433611215b6af76e4d699c85b79bcf322a9643c15520e5b072441dedb5dd"
        proposal = STUDY / "H4_promotion_proposal_v3.md"
        assert digest(proposal) == "4480094b5001f3ead5f20adc79275901cc98349b2b8d8c9a7724c0860fee6bfb"
        mapping = read(mapping_path)
        packet_path = STUDY / "H4_review_manifest_v3.json"
        assert digest(packet_path) == mapping["review_manifest_sha256"]
        packet = read(packet_path)
        for entry in packet["files"]:
            path = ROOT / entry["path"]
            assert digest(path) == entry["sha256"] and path.stat().st_size == entry["bytes"]
        edition = ROOT / mapping["edition"]
        assert digest(edition / "edition_manifest.json") == mapping["edition_manifest_sha256"]
        full_mapping = read(edition / "edition_manifest.json")
        for row in full_mapping["files"]:
            assert digest(edition / row["destination"]) == row["destination_sha256"]
            assert digest(ROOT / row["source"]) == row["source_sha256"]
            if row["kind"] == "unchanged dependency":
                assert digest(ROOT / row["destination"]) == row["destination_sha256"]
        for report in mapping["review_reports"]:
            assert digest(ROOT / report["path"]) == report["sha256"]
        payloads = []
        for row in mapping["destinations"]:
            live = ROOT / row["destination"]
            assert (digest(live) if live.exists() else None) == row["current_live_sha256"]
            payloads.append((live, (edition / row["destination"]).read_bytes()))
        assert len(payloads) == 11 and not RECORD.exists() and not OUTPUT.exists()
        OUTPUT.mkdir(parents=True)
        record = dict(status="approved_preflight_passed", task="01a09bce-f91d-73c3-9127-0fbe5fb00386",
                      approval=dict(user_text="yes I approve", user_context_local_date="2026-09-14",
                                    scope="The exact eleven-file H4 v3 addition requested in the preceding assistant final response",
                                    proposal_sha256=digest(proposal), mapping_sha256=digest(mapping_path)),
                      recorded_utc=datetime.now(timezone.utc).isoformat(),
                      preinstallation_head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                      reviewed_manifest_sha256=digest(packet_path), verified_frozen_inputs=len(packet["files"]),
                      verified_edition_files=len(full_mapping["files"]), review_reports=mapping["review_reports"],
                      approved_destinations=mapping["destinations"], script_sha256=digest(Path(__file__)),
                      budget=dict(cpu_seconds=600, wall_seconds_per_command=660, address_space_bytes=4*1024**3,
                                  numerical_threads=1, research_trajectories=0),
                      checks=[], integration_commit=None)
        write_record(record)
        for live, content in payloads:
            live.write_bytes(content)
        for row in full_mapping["files"]:
            assert digest(ROOT / row["destination"]) == row["destination_sha256"]
        record["status"] = "installed_pending_checks"
        record["installed_files"] = [{"path": row["destination"], "sha256": digest(ROOT / row["destination"])} for row in full_mapping["files"]]
        write_record(record)
    print(json.dumps(dict(status=record["status"], installed=11, matched_edition_files=31)), flush=True)


def checks():
    record = read(RECORD)
    assert record["status"] == "installed_pending_checks"
    scratch = OUTPUT / "scratch"
    scratch.mkdir()
    env = dict(os.environ, PYTHONPATH=str(ROOT / "code"), PYTHONDONTWRITEBYTECODE="1",
               H4_LAW_TEST_SCRATCH=str(scratch), H4_VALIDATION_TEST_SCRATCH=str(scratch), TMPDIR=str(scratch))
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[key] = "1"
    guide = (ROOT / "code/README.md").read_text().split("## Observable computation through physical time 40", 1)[1]
    example = guide.split("```python\n", 1)[1].split("```", 1)[0]
    example_path = OUTPUT / "public_example.py"
    example_path.write_text(example)
    commands = [[sys.executable, "-B", "-m", "unittest", "discover", "-s", "code/tests", "-p", "test_observable*.py", "-v"],
                [sys.executable, "-B", str(example_path)]]
    commands += [[sys.executable, "-B", "code/scripts/" + name + ".py", "--help"] for name in
                 ("run_observable_validation", "validate_observable_horizon", "analyze_observable_horizon")]
    consumed = 0.0
    for index, command in enumerate(commands):
        allowance = int(600-consumed)
        assert allowance > 0
        def limits():
            resource.setrlimit(resource.RLIMIT_CPU, (allowance, allowance))
            resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        start = time.monotonic()
        log = OUTPUT / f"check_{index}.log"
        with log.open("x") as stream:
            try:
                result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT,
                                        preexec_fn=limits, timeout=660)
                code = result.returncode
            except subprocess.TimeoutExpired:
                code = None
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        cpu = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
        consumed += cpu
        row = dict(command=command, cwd=str(ROOT), exit_code=code, cpu_seconds=cpu,
                   wall_seconds=time.monotonic()-start, peak_child_rss_bytes=after.ru_maxrss*1024,
                   log=str(log.relative_to(ROOT)), log_sha256=digest(log))
        record["checks"].append(row)
        record["status"] = "checks_running" if code == 0 else "check_failed"
        record["check_cpu_seconds"] = consumed
        write_record(record)
        print(json.dumps(row), flush=True)
        if code != 0:
            raise RuntimeError("post-install check failed; original evidence retained")
    for row in record["installed_files"]:
        assert digest(ROOT / row["path"]) == row["sha256"]
    record["status"] = "installed_checks_passed_pending_commit"
    record["test_environment"] = {key: env[key] for key in env if key in
                                 ("PYTHONPATH", "PYTHONDONTWRITEBYTECODE", "TMPDIR", "H4_LAW_TEST_SCRATCH", "H4_VALIDATION_TEST_SCRATCH") or key.endswith("NUM_THREADS")}
    write_record(record)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("install", "checks"))
    args = parser.parse_args()
    install() if args.phase == "install" else checks()
