#!/usr/bin/env python3
"""Checkpointed exact sector runner for Campaign 4."""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import tempfile
import time


HERE = Path(__file__).resolve().parent
PARENT_SHA = "1931b628b25d2a7c018bc20a06d14aee6ee86ca702d8abcbec17e1ec719be260"
FROZEN_CAMPAIGN1_SHA = "02215aa7c18f3550a19f34b89734b6bf5b66a2825e8aa5bc103517767982ee1a"
CANONICAL = {
    1: 111,
    3: 1_685_184,
    5: 77_400_633_120,
    7: 7_315_868_433_079_296,
    9: 1_181_161_141_825_400_561_664,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def limiter(byte_limit: int):
    def set_limit() -> None:
        resource.setrlimit(resource.RLIMIT_AS, (byte_limit, byte_limit))
    return set_limit


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=path.name + ".", suffix=".tmp", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def sector_path(directory: Path, order: int, w_hits: int,
                a_hits: int) -> Path:
    return directory / f"k{order}_w{w_hits}_a{a_hits}.json"


def validate_record(record: dict, order: int, w_hits: int,
                    a_hits: int) -> None:
    expected = {
        "root": "f", "order": order,
        "w_hits": w_hits, "a_hits": a_hits,
    }
    for key, value in expected.items():
        if record.get(key) != value:
            raise ArithmeticError(f"sector record {key} mismatch")
    if record.get("parent_source_sha256") != PARENT_SHA:
        raise ArithmeticError("sector parent source mismatch")
    if int(record.get("lambda_degree")) != order-a_hits:
        raise ArithmeticError("sector diagonal degree mismatch")
    campaign = record.get("campaign4")
    if campaign is not None:
        if int(campaign.get("alpha_power")) != order-w_hits-a_hits:
            raise ArithmeticError("sector alpha-power metadata mismatch")
        if int(campaign.get("beta_power")) != w_hits:
            raise ArithmeticError("sector beta-power metadata mismatch")
    int(record["value"])


def frozen_diagonal(path: Path) -> dict[int, list[int]]:
    if sha256(path) != FROZEN_CAMPAIGN1_SHA:
        raise ArithmeticError("frozen Campaign-1 result hash mismatch")
    raw = json.loads(path.read_text())
    output = {}
    for record in raw["observables"]["f"]["jets"]:
        order = int(record["order"])
        output[order] = [int(value) for value in record["lambda_coefficients"]]
    return output


def compile_result(sector_directory: Path, diagonal_path: Path,
                   binary: Path) -> dict:
    expected = frozen_diagonal(diagonal_path)
    jets = []
    sectors = []
    for order in range(10):
        if order % 2 == 0:
            jets.append({"order": order, "monomials": []})
            continue
        monomials = []
        diagonal = defaultdict(int)
        total = 0
        for w_hits in range(order+1):
            for a_hits in range(order-w_hits+1):
                path = sector_path(sector_directory, order, w_hits, a_hits)
                if not path.exists():
                    raise FileNotFoundError(f"missing exact sector {path}")
                record = json.loads(path.read_text())
                validate_record(record, order, w_hits, a_hits)
                value = int(record["value"])
                alpha_power = order-w_hits-a_hits
                beta_power = w_hits
                if value:
                    monomials.append({
                        "alpha_power": alpha_power,
                        "beta_power": beta_power,
                        "value": str(value),
                        "w_hits": w_hits,
                        "a_hits": a_hits,
                    })
                diagonal[alpha_power+beta_power] += value
                total += value
                sectors.append({
                    "path": str(path), "sha256": sha256(path),
                    "order": order, "w_hits": w_hits, "a_hits": a_hits,
                    "alpha_power": alpha_power, "beta_power": beta_power,
                    "value": str(value), "seconds": record["seconds"],
                    "value_cache": record["value_cache"],
                    "wick_cache": record["wick_cache"],
                    "wick_subproblem_cache": record["wick_subproblem_cache"],
                })
        diagonal_coefficients = [
            diagonal[degree] for degree in range(order+1)
        ]
        while len(diagonal_coefficients) > 1 and not diagonal_coefficients[-1]:
            diagonal_coefficients.pop()
        if diagonal_coefficients != expected[order]:
            raise ArithmeticError(
                f"order-{order} frozen diagonal coefficient mismatch"
            )
        if total != CANONICAL[order]:
            raise ArithmeticError(f"order-{order} canonical point mismatch")
        jets.append({
            "order": order,
            "monomials": sorted(monomials,
                                key=lambda z: (z["alpha_power"],
                                               z["beta_power"])),
            "diagonal_lambda_coefficients": [
                str(value) for value in diagonal_coefficients
            ],
            "canonical_alpha1_beta1": str(total),
        })
    return {
        "schema_version": 1,
        "metric": "D_a + alpha D_u + beta D_W",
        "orders": list(range(10)),
        "jets": jets,
        "sector_manifest": sectors,
        "source_identity": {
            "wrapper_sha256": sha256(HERE/"sector_wrapper.cpp"),
            "campaign1_graded_source_sha256": sha256(
                HERE.parent/"campaign1/graded_sector.cpp"
            ),
            "parent_sector_engine_sha256": PARENT_SHA,
            "runner_sha256": sha256(Path(__file__)),
            "binary_sha256": sha256(binary),
            "frozen_campaign1_input_sha256": FROZEN_CAMPAIGN1_SHA,
        },
        "all_diagonal_and_canonical_gates_passed": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--sectors", type=Path,
                        default=HERE/"sectors")
    parser.add_argument("--diagonal", type=Path,
                        default=HERE.parent/"campaign1/results_order9_q2_order8.json")
    parser.add_argument("--output", type=Path,
                        default=HERE/"results_order9.json")
    parser.add_argument("--max-seconds", type=float, default=1800.0)
    parser.add_argument("--memory-bytes", type=int, default=4*1024**3)
    parser.add_argument("--budget-ledger", type=Path,
                        default=HERE/"production_budget.json")
    args = parser.parse_args()

    # Refuse to launch production if the diagonal source is not frozen.
    frozen_diagonal(args.diagonal)
    prior_wall = 0.0
    prior_invocations = []
    if args.budget_ledger.exists():
        ledger = json.loads(args.budget_ledger.read_text())
        prior_wall = float(ledger["cumulative_wall_seconds"])
        prior_invocations = list(ledger.get("invocations", []))
    remaining_budget = args.max_seconds-prior_wall
    if remaining_budget <= 0:
        raise TimeoutError("Campaign-4 cumulative wall cap was already exhausted")
    start = time.monotonic()
    deadline = start + remaining_budget
    executed = 0
    reused = 0
    def write_budget(status: str) -> tuple[float, float]:
        invocation = time.monotonic()-start
        cumulative = prior_wall+invocation
        atomic_json(args.budget_ledger, {
            "schema_version": 1,
            "hard_cap_seconds": args.max_seconds,
            "cumulative_wall_seconds": cumulative,
            "invocations": prior_invocations + [{
                "wall_seconds": invocation,
                "sectors_executed": executed,
                "sectors_reused": reused,
                "status": status,
            }],
        })
        return invocation, cumulative

    try:
        for order in (1, 3, 5, 7, 9):
            for w_hits in range(order+1):
                for a_hits in range(order-w_hits+1):
                    path = sector_path(args.sectors, order, w_hits, a_hits)
                    if path.exists():
                        record = json.loads(path.read_text())
                        validate_record(record, order, w_hits, a_hits)
                        reused += 1
                        continue
                    remaining = deadline-time.monotonic()
                    if remaining <= 0:
                        raise TimeoutError(
                            "Campaign-4 cumulative wall cap reached"
                        )
                    process = subprocess.run(
                        [str(args.binary), "f", str(order),
                         str(w_hits), str(a_hits)],
                        check=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, text=True, timeout=remaining,
                        preexec_fn=limiter(args.memory_bytes),
                    )
                    record = json.loads(process.stdout)
                    validate_record(record, order, w_hits, a_hits)
                    record["campaign4"] = {
                        "alpha_power": order-w_hits-a_hits,
                        "beta_power": w_hits,
                        "atomic_sector_schema": 1,
                    }
                    atomic_json(path, record)
                    executed += 1
                    write_budget("active_checkpoint")
                    print(json.dumps({
                        "completed": str(path), "seconds": record["seconds"],
                        "remaining_global_seconds": deadline-time.monotonic(),
                    }), flush=True)
    except BaseException:
        write_budget("failed_or_inconclusive")
        raise

    invocation_wall, cumulative_wall = write_budget("completed")
    result = compile_result(args.sectors, args.diagonal, args.binary)
    result["production"] = {
        "wall_seconds_this_invocation": invocation_wall,
        "cumulative_wall_seconds": cumulative_wall,
        "max_seconds": args.max_seconds,
        "memory_bytes_per_sector": args.memory_bytes,
        "sectors_executed": executed,
        "sectors_reused": reused,
        "sector_count": len(result["sector_manifest"]),
        "budget_ledger": str(args.budget_ledger),
        "budget_ledger_sha256": sha256(args.budget_ledger),
    }
    atomic_json(args.output, result)
    print(json.dumps({
        "result": str(args.output), "sha256": sha256(args.output),
        "wall_seconds": result["production"]["wall_seconds_this_invocation"],
        "sector_count": len(result["sector_manifest"]),
    }), flush=True)


if __name__ == "__main__":
    main()
