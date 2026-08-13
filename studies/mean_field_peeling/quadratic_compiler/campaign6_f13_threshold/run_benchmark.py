#!/usr/bin/env python3
"""Run one Campaign 6 benchmark with frozen resource/provenance recording."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent
MEMORY_BYTES = 4 * 1024**3
CPU_SECONDS = 900
WALL_SECONDS = 900


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("executable", type=Path)
    parser.add_argument("args", nargs="*")
    ns = parser.parse_args()

    executable = ns.executable.resolve()
    command = [
        "prlimit",
        f"--as={MEMORY_BYTES}",
        f"--cpu={CPU_SECONDS}",
        "--",
        str(executable),
        *ns.args,
    ]
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    timed_out = False
    try:
        proc = subprocess.run(
            command,
            cwd=HERE,
            text=True,
            capture_output=True,
            timeout=WALL_SECONDS,
            check=False,
        )
        returncode = proc.returncode
        stdout = proc.stdout
        stderr = proc.stderr
    except subprocess.TimeoutExpired as error:
        timed_out = True
        returncode = None
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
    wall = time.monotonic() - start
    after = resource.getrusage(resource.RUSAGE_CHILDREN)

    record = {
        "name": ns.name,
        "command": command,
        "executable_sha256": sha256(executable),
        "wall_seconds": wall,
        "user_cpu_seconds": after.ru_utime - before.ru_utime,
        "system_cpu_seconds": after.ru_stime - before.ru_stime,
        "peak_rss_kib": after.ru_maxrss,
        "returncode": returncode,
        "timed_out": timed_out,
        "stdout": stdout,
        "stderr": stderr,
        "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "limits": {
            "address_space_bytes": MEMORY_BYTES,
            "cpu_seconds": CPU_SECONDS,
            "wall_seconds": WALL_SECONDS,
        },
    }
    output = HERE / f"{ns.name}.benchmark.json"
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(output)
    if timed_out or returncode != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
