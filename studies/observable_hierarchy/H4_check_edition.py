"""Bounded deterministic checking of a fresh H4 standalone code edition.

Predeclared: 600 combined child CPU seconds, 660 wall seconds per check;
one numerical thread; tests and the book's exact rational constant program
only, no H4 or finite-network training trajectories. Old evidence is preserved.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[2]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def children_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime


def run(edition, output):
    edition, output = Path(edition).resolve(), Path(output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    scratch = output / "scratch"
    scratch.mkdir()
    sources = sorted((edition / "code").rglob("*.py"))
    hashes = {str(p.relative_to(edition)): digest(p) for p in sources}
    chapter = (ROOT / "docs/global_nonlinear.md").read_text()
    unit = chapter.split("###### 5. Reproducible rational Gaussian certificate", 1)[1].split("##### C.4.5.2.", 1)[0]
    certificate = unit.split("```python\n", 1)[1].split("```", 1)[0]
    certificate_path = output / "reference_certificate.py"
    certificate_path.write_text(certificate)
    environment = dict(os.environ)
    environment.update(PYTHONPATH=str(edition / "code"), PYTHONDONTWRITEBYTECODE="1",
                       TMPDIR=str(scratch), H4_LAW_TEST_SCRATCH=str(scratch), H4_VALIDATION_TEST_SCRATCH=str(scratch))
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        environment[key] = "1"
    commands = [
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "code/tests", "-p", "test_observable*.py", "-v"],
        [sys.executable, "-B", str(certificate_path)],
    ]
    result = dict(format="H4-deterministic-edition-check-v1", edition=str(edition),
                  input_hashes=hashes, checker_sha256=digest(__file__),
                  certificate_source="docs/global_nonlinear.md C.4.5.1.5 complete Python block",
                  certificate_sha256=digest(certificate_path), python=sys.version, platform=platform.platform(),
                  environment={k:environment[k] for k in environment if k.startswith("H4_") or k in
                               ("PYTHONPATH", "TMPDIR", "PYTHONDONTWRITEBYTECODE", "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                  commands=[], budget=dict(total_cpu_seconds=600, wall_seconds_per_command=660))
    before = children_cpu()
    for index, command in enumerate(commands):
        used = children_cpu()-before
        if used >= 600:
            result["commands"].append(dict(command=command, status="not_run_cpu_budget"))
            break
        remaining = max(1, int(600-used))
        def cap():
            resource.setrlimit(resource.RLIMIT_CPU, (remaining, remaining))
        started = time.monotonic()
        cpu = children_cpu()
        with (output / ("check_"+str(index)+".log")).open("xb") as log:
            try:
                process = subprocess.run(command, cwd=edition, env=environment, stdout=log, stderr=subprocess.STDOUT,
                                         timeout=660, preexec_fn=cap)
                status, exit_code = "complete", process.returncode
            except subprocess.TimeoutExpired:
                status, exit_code = "wall_budget", None
        result["commands"].append(dict(command=command, cwd=str(edition), status=status, exit_code=exit_code,
                                        cpu_seconds=children_cpu()-cpu, wall_seconds=time.monotonic()-started,
                                        log="check_"+str(index)+".log"))
    result["input_hashes_unchanged"] = hashes == {str(p.relative_to(edition)): digest(p) for p in sources}
    result["child_cpu_seconds"] = children_cpu()-before
    result["peak_child_rss_bytes"] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss*1024
    result["status"] = "pass" if (result["input_hashes_unchanged"] and len(result["commands"]) == len(commands)
                                    and all(r.get("exit_code") == 0 for r in result["commands"])) else "failure"
    result["outputs"] = {p.name:digest(p) for p in output.iterdir() if p.is_file()}
    (output / "record.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("status", "child_cpu_seconds", "peak_child_rss_bytes", "commands")}))
    return int(result["status"] != "pass")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    raise SystemExit(run(args.edition, args.output))
