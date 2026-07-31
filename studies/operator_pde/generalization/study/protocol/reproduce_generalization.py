#!/usr/bin/env python3
"""One-command reproduction of the frozen sparse generalization study."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(arguments: list[str], env: dict[str, str]) -> None:
    print("+", " ".join(arguments), flush=True)
    subprocess.run(arguments, cwd=ROOT, env=env, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parallel-pde", type=int, default=3)
    parser.add_argument("--parallel-dense", type=int, default=2)
    parser.add_argument("--dense-workers", type=int, default=4)
    parser.add_argument("--bootstrap-replicates", type=int, default=2000)
    args = parser.parse_args()
    env = os.environ.copy()
    env["PYTHONPATH"] = os.fspath(ROOT / "src")
    env["OPENBLAS_NUM_THREADS"] = "1"
    env["OMP_NUM_THREADS"] = "1"
    env["MPLCONFIGDIR"] = os.path.join(
        tempfile.gettempdir(), "dense-mup-matplotlib"
    )

    run(
        [PYTHON, "-m", "unittest", "discover", "-s", "tests", "-v"],
        env,
    )
    for mode in (
        "pde-primary",
        "pde-scramble",
        "pde-continue",
        "pde-audits",
    ):
        run(
            [
                PYTHON,
                "protocol/run_grid.py",
                mode,
                "--parallel-jobs",
                str(args.parallel_pde),
            ],
            env,
        )
    run([PYTHON, "pde_precheck.py"], env)
    decision = json.loads(
        (
            ROOT
            / "results"
            / "generalization"
            / "pde_numerical_decision.json"
        ).read_text()
    )
    fallback = decision["r256_required"]
    if fallback:
        run(
            [
                PYTHON,
                "protocol/run_grid.py",
                "pde-r256",
                "--parallel-jobs",
                str(args.parallel_pde),
                "--case-ids",
                *fallback,
            ],
            env,
        )
    run([PYTHON, "protocol/run_grid.py", "seal-pde"], env)
    for mode in ("dense-screen", "dense-confirm", "dense-depth"):
        run(
            [
                PYTHON,
                "protocol/run_grid.py",
                mode,
                "--parallel-jobs",
                str(args.parallel_dense),
                "--dense-workers",
                str(args.dense_workers),
            ],
            env,
        )
    run([PYTHON, "protocol/run_grid.py", "seal-dense"], env)
    run(
        [
            PYTHON,
            "analyze_generalization.py",
            "--bootstrap-replicates",
            str(args.bootstrap_replicates),
        ],
        env,
    )
    if args.bootstrap_replicates == 2000:
        run([PYTHON, "verify_study.py", "evidence"], env)
    else:
        print(
            "Noncanonical bootstrap count used; full frozen-evidence "
            "verification intentionally skipped.",
            flush=True,
        )


if __name__ == "__main__":
    main()
