#!/usr/bin/env python3
"""Run the bounded double-graded sectors and merge the Campaign 1 jet JSON."""

from __future__ import annotations

import argparse
from collections import defaultdict
import copy
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time


EXPECTED_LOWER_SHA = (
    "9919b54fdddc496af5b4b439f525c0215ed0295d7130a0eb247e2416ce62ca18"
)
EXPECTED_PARENT_SHA = (
    "1931b628b25d2a7c018bc20a06d14aee6ee86ca702d8abcbec17e1ec719be260"
)
EXPECTED_F9 = 1_181_161_141_825_400_561_664


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def memory_limiter(byte_limit: int):
    def limit() -> None:
        resource.setrlimit(resource.RLIMIT_AS, (byte_limit, byte_limit))
    return limit


def run_order(
    binary: Path,
    root: str,
    order: int,
    deadline: float,
    byte_limit: int,
) -> tuple[list[int], list[dict]]:
    coefficients: defaultdict[int, int] = defaultdict(int)
    records = []
    total = (order + 1) * (order + 2) // 2
    completed = 0
    for w_hits in range(order + 1):
        for a_hits in range(order - w_hits + 1):
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("global Campaign 1 wall-clock cap reached")
            process = subprocess.run(
                [
                    str(binary), root, str(order),
                    str(w_hits), str(a_hits),
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=remaining,
                preexec_fn=memory_limiter(byte_limit),
            )
            record = json.loads(process.stdout)
            if record["parent_source_sha256"] != EXPECTED_PARENT_SHA:
                raise AssertionError("graded sector used an unexpected parent source")
            coefficients[record["lambda_degree"]] += int(record["value"])
            records.append(record)
            completed += 1
            print(json.dumps({
                "root": root,
                "order": order,
                "completed": completed,
                "total": total,
                "w_hits": w_hits,
                "a_hits": a_hits,
                "value": record["value"],
                "seconds": record["seconds"],
            }), flush=True)
    return [coefficients[degree] for degree in range(order + 1)], records


def jet_record(order: int, coefficients: list[int]) -> dict:
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return {
        "order": order,
        "lambda_coefficients": [str(value) for value in coefficients],
        "lambda_one": str(sum(coefficients)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--lower-result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-seconds", type=float, default=1200.0)
    parser.add_argument("--memory-bytes", type=int, default=4 * 1024**3)
    args = parser.parse_args()

    if sha256(args.lower_result) != EXPECTED_LOWER_SHA:
        raise AssertionError("lower-order input hash differs from frozen result")
    lower = json.loads(args.lower_result.read_text(encoding="utf-8"))
    start = time.monotonic()
    deadline = start + args.max_seconds

    f9, f_records = run_order(
        args.binary, "f", 9, deadline, args.memory_bytes
    )
    if sum(f9) != EXPECTED_F9:
        raise AssertionError(
            f"canonical F9 regression failed: {sum(f9)} != {EXPECTED_F9}"
        )
    q2_8, q2_records = run_order(
        args.binary, "q2", 8, deadline, args.memory_bytes
    )

    merged = copy.deepcopy(lower)
    merged["schema_version"] = 3
    lower_parent = merged.pop("parent_source_sha256")
    merged["provenance"] = {
        "lower_result_sha256": EXPECTED_LOWER_SHA,
        "lower_parent_source_sha256": lower_parent,
        "upper_graded_parent_source_sha256": EXPECTED_PARENT_SHA,
    }
    merged["graded_sector_source_sha256"] = sha256(
        Path(__file__).with_name("graded_sector.cpp")
    )
    merged["safety_caps"] = {"f": 9, "q1": 8, "q2": 8}
    merged["observables"]["f"]["max_order"] = 9
    merged["observables"]["f"]["jets"].extend([
        jet_record(8, [0]),
        jet_record(9, f9),
    ])
    merged["observables"]["q2"]["max_order"] = 8
    merged["observables"]["q2"]["jets"].extend([
        jet_record(7, [0]),
        jet_record(8, q2_8),
    ])

    # Exact Euler identity: D_lambda^8 Q1 = 8 lambda D_lambda^7 f.
    f7 = [
        int(value) for value in
        merged["observables"]["f"]["jets"][7]["lambda_coefficients"]
    ]
    q1_8 = [0] + [8 * value for value in f7]
    merged["observables"]["q1"]["max_order"] = 8
    merged["observables"]["q1"]["jets"].extend([
        jet_record(7, [0]),
        jet_record(8, q1_8),
    ])

    # Diagnostics copied from the frozen lower result describe only the lower
    # dense run.  Do not silently present them as resource data for the merged
    # upper-stage artifact.
    merged["lower_stage_diagnostics"] = {
        "observables": {
            root: {
                key: merged["observables"][root].pop(key)
                for key in ("seconds", "cache_before", "cache_after")
            }
            for root in ("f", "q1", "q2")
        },
        "cache": merged.pop("cache"),
        "misses_by_remaining_order": merged.pop("misses_by_remaining_order"),
    }
    merged["graded_run"] = {
        "wall_seconds": time.monotonic() - start,
        "memory_bytes_per_sector": args.memory_bytes,
        "wall_cap_seconds": args.max_seconds,
        "f9_sector_count": len(f_records),
        "q2_order8_sector_count": len(q2_records),
        "sector_records": f_records + q2_records,
    }
    merged["regression_gates_passed"] = True

    encoded = json.dumps(merged, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(encoded, encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "f9": str(sum(f9)),
        "q2_order8": str(sum(q2_8)),
        "wall_seconds": merged["graded_run"]["wall_seconds"],
    }), flush=True)


if __name__ == "__main__":
    main()
