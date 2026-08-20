#!/usr/bin/env python3
"""Run, analyze, and package the audit-fixed long-horizon extension."""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import itertools
import json
import os
import platform
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import matplotlib
import numpy as np

from dense_mup.analysis import analyze_directory
from dense_mup.experiment import config_hash, load_trace, run_trace


AXES = ("n", "depth", "seed", "sigma_w", "A", "gamma", "restart_time")


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else [value]


def _safe(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:g}".replace("-", "m").replace(".", "p")
    return str(value).replace("-", "m").replace(".", "p")


def source_hash(root: Path) -> str:
    digest = hashlib.sha256()
    files = sorted(
        [
            root / "run_all.py",
            *list((root / "src").rglob("*.py")),
            *list((root / "tests").rglob("*.py")),
        ]
    )
    for path in files:
        digest.update(str(path.relative_to(root)).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def expand_config(config: dict[str, Any], code_sha256: str) -> list[dict[str, Any]]:
    defaults = dict(config["defaults"])
    runs: list[dict[str, Any]] = []
    for group in config["groups"]:
        name = group["name"]
        group_base = {
            **defaults,
            **{
                key: value
                for key, value in group.items()
                if key not in ("name", "cases", *AXES, "seeds")
            },
        }
        cases = group.get("cases")
        if cases is not None:
            expanded_cases = [
                {**group_base, **case, "group": name} for case in cases
            ]
        else:
            axis_values = {}
            for axis in AXES:
                if axis == "seed":
                    value = group.get("seeds", group.get("seed", defaults[axis]))
                else:
                    value = group.get(axis, defaults[axis])
                axis_values[axis] = _as_list(value)
            expanded_cases = []
            for values in itertools.product(*(axis_values[x] for x in AXES)):
                case = dict(group_base)
                case.update(dict(zip(AXES, values)))
                case["group"] = name
                expanded_cases.append(case)

        for case in expanded_cases:
            case["n"] = int(case["n"])
            case["depth"] = int(case["depth"])
            case["seed"] = int(case["seed"])
            case["sigma_w"] = float(case["sigma_w"])
            case["A"] = float(case["A"])
            case["gamma"] = float(case["gamma"])
            case["restart_time"] = float(case.get("restart_time", 0.0))
            case["duration"] = float(case["duration"])
            case["dt"] = float(case["dt"])
            case["sample_dt"] = float(case["sample_dt"])
            case["orders"] = [int(x) for x in case["orders"]]
            case["control_order"] = bool(case.get("control_order", False))
            case["code_sha256"] = code_sha256
            identity = (
                f"{name}_n{case['n']}_L{case['depth']}_s{case['seed']}"
                f"_sw{_safe(case['sigma_w'])}_A{_safe(case['A'])}"
                f"_g{_safe(case['gamma'])}_r{_safe(case['restart_time'])}"
                f"_dt{_safe(case['dt'])}"
            )
            if any(x["id"] == identity for x in runs):
                identity = f"{identity}_v{len(runs):03d}"
            case["id"] = identity
            runs.append(case)
    return runs


def environment_record() -> dict[str, Any]:
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        np.show_config()
    return {
        "python": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "numpy": np.__version__,
        "matplotlib": matplotlib.__version__,
        "blas_configuration": stream.getvalue(),
        "float_type": "float64",
        "openblas_num_threads": os.environ.get("OPENBLAS_NUM_THREADS"),
        "omp_num_threads": os.environ.get("OMP_NUM_THREADS"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config", type=Path, default=ROOT / "config" / "protocol.json"
    )
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--only",
        action="append",
        help="Run only this group; may be supplied more than once.",
    )
    parser.add_argument("--skip-analysis", action="store_true")
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    code_sha256 = source_hash(ROOT)
    runs = expand_config(config, code_sha256)
    if args.only:
        selected = set(args.only)
        runs = [run for run in runs if run["group"] in selected]
    raw_dir = ROOT / "results" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, Any]] = []
    for index, run in enumerate(runs, start=1):
        path = raw_dir / f"{run['id']}.npz"
        expected_hash = config_hash(run)
        if path.exists() and not args.force:
            metadata, _ = load_trace(path)
            if metadata.get("config_sha256") == expected_hash:
                print(f"[{index:02d}/{len(runs):02d}] reuse {run['id']}")
                manifest.append(metadata)
                continue
        print(f"[{index:02d}/{len(runs):02d}] run   {run['id']}")
        metadata = run_trace(run, path, progress=print)
        manifest.append(metadata)

    metadata_dir = ROOT / "metadata"
    metadata_dir.mkdir(parents=True, exist_ok=True)
    (metadata_dir / "environment.json").write_text(
        json.dumps(environment_record(), indent=2), encoding="utf-8"
    )
    (metadata_dir / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    (metadata_dir / "source_sha256.txt").write_text(
        code_sha256 + "\n", encoding="utf-8"
    )

    if not args.skip_analysis:
        representative = next(
            (
                run["id"]
                for run in runs
                if run["group"] == config["representative"]["group"]
                and run["seed"] == config["representative"]["seed"]
            ),
            runs[0]["id"],
        )
        result = analyze_directory(
            raw_dir=raw_dir,
            processed_dir=ROOT / "results" / "processed",
            figures_dir=ROOT / "figures",
            protocol=config["plateau_protocol"],
            representative_id=representative,
            expected_manifest=manifest,
        )
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
