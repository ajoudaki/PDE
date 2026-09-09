#!/usr/bin/env python3
"""Atomic, capped sector runner for Campaign 5 Stage C."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import tempfile
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "stage_c_sector.cpp"
CHECKPOINTS = HERE / "checkpoints"
EXPECTED_SOURCE_SHA256 = (
    "f1912e81b2f25bdef04bcef9c490a0975757a64deda4cb55f74c7c50abfe64ce"
)
EXPECTED_BINARY_SHA256 = (
    "59d949b0808d92b946ec55a856764f43ed4ccbcc922c5849561c9ba73e175fbf"
)
STAGE_C_AUTHORIZED = False
CPU_CAP_SECONDS = 6 * 60 * 60
ADDRESS_CAP_BYTES = 4 * 1024**3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp",
                                     dir=path.parent)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(value, stream, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def validate_record(record: dict, sector: int, source_hash: str,
                    binary_hash: str) -> None:
    assert record["schema_version"] == 1
    assert record["order"] == 7
    assert record["w_hits"] == sector
    assert record["source_sha256"] == source_hash
    assert record["binary_sha256"] == binary_hash
    assert record["exit_status"] == 0
    assert isinstance(record["rho_coefficients"], list)
    assert all(isinstance(value, str) for value in record["rho_coefficients"])
    assert record["cpu_seconds"] >= 0


def capped_child() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (ADDRESS_CAP_BYTES,
                                            ADDRESS_CAP_BYTES))


def main() -> None:
    if not STAGE_C_AUTHORIZED:
        raise SystemExit(
            "Stage C is closed unauthorized: the final-source W-hit-zero "
            "pilot failed the frozen 1800-second completion gate. See "
            "provenance_stage_c_projection.json. Production is disabled."
        )
    parser = argparse.ArgumentParser()
    parser.add_argument("binary", type=Path)
    parser.add_argument("--single-sector", type=int)
    args = parser.parse_args()
    source_hash, binary_hash = sha256(SOURCE), sha256(args.binary)
    if EXPECTED_SOURCE_SHA256 != "TO_BE_FROZEN" and source_hash != EXPECTED_SOURCE_SHA256:
        raise SystemExit("source hash differs from the frozen Stage-C source")
    if EXPECTED_BINARY_SHA256 != "TO_BE_FROZEN" and binary_hash != EXPECTED_BINARY_SHA256:
        raise SystemExit("binary hash differs from the frozen Stage-C binary")

    sectors = [args.single_sector] if args.single_sector is not None else list(range(8))
    if any(sector is None or sector < 0 or sector > 7 for sector in sectors):
        raise SystemExit("invalid W-hit sector")

    consumed = 0.0
    for path in CHECKPOINTS.glob("stage_c_w*.json"):
        old = json.loads(path.read_text())
        if old.get("source_sha256") == source_hash and old.get("binary_sha256") == binary_hash:
            validate_record(old, old["w_hits"], source_hash, binary_hash)
            consumed += old["cpu_seconds"]

    for sector in sectors:
        path = CHECKPOINTS / f"stage_c_w{sector}.json"
        if path.exists():
            record = json.loads(path.read_text())
            if (record.get("source_sha256") == source_hash
                    and record.get("binary_sha256") == binary_hash):
                validate_record(record, sector, source_hash, binary_hash)
                continue
            raise SystemExit(f"stale checkpoint blocks sector {sector}: {path}")
        remaining = CPU_CAP_SECONDS - consumed
        if remaining <= 0:
            raise SystemExit("cumulative Stage-C CPU cap exhausted")

        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        start = time.monotonic()
        completed = subprocess.run(
            [str(args.binary), "7", "--w-hits", str(sector)],
            text=True, capture_output=True, timeout=remaining,
            preexec_fn=capped_child,
        )
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        cpu = ((after.ru_utime - before.ru_utime)
               + (after.ru_stime - before.ru_stime))
        consumed += cpu
        if completed.returncode != 0:
            raise SystemExit(
                f"sector {sector} failed with {completed.returncode}: "
                f"{completed.stderr[-2000:]}"
            )
        raw = json.loads(completed.stdout)
        if raw["w_hits"] != sector:
            raise SystemExit("compiler returned the wrong sector")
        record = {
            "schema_version": 1,
            "order": 7,
            "w_hits": sector,
            "source_sha256": source_hash,
            "binary_sha256": binary_hash,
            "rho_coefficients": raw["raw_rho"][7],
            "compiler_value_cache": raw["value_cache"],
            "compiler_terminal_cache": raw["wick_cache"],
            "compiler_base_evaluations": raw["base_evaluations"],
            "cpu_seconds": cpu,
            "wall_seconds": time.monotonic() - start,
            "stderr_tail": completed.stderr[-4000:],
            "address_cap_bytes": ADDRESS_CAP_BYTES,
            "cumulative_cpu_cap_seconds": CPU_CAP_SECONDS,
            "exit_status": completed.returncode,
        }
        validate_record(record, sector, source_hash, binary_hash)
        atomic_json(path, record)

    completed_records = []
    for sector in range(8):
        path = CHECKPOINTS / f"stage_c_w{sector}.json"
        if not path.exists():
            continue
        record = json.loads(path.read_text())
        if record.get("source_sha256") != source_hash or record.get("binary_sha256") != binary_hash:
            continue
        validate_record(record, sector, source_hash, binary_hash)
        completed_records.append(record)
    summary = {
        "schema_version": 1,
        "source_sha256": source_hash,
        "binary_sha256": binary_hash,
        "completed_sectors": [x["w_hits"] for x in completed_records],
        "cumulative_cpu_seconds": sum(x["cpu_seconds"] for x in completed_records),
        "all_sectors_complete": len(completed_records) == 8,
    }
    if summary["all_sectors_complete"]:
        width = max(len(x["rho_coefficients"]) for x in completed_records)
        coefficients = [0] * width
        for record in completed_records:
            for q, value in enumerate(record["rho_coefficients"]):
                coefficients[q] += int(value)
        summary["raw_J7_coefficients_ascending"] = [str(x) for x in coefficients]
    atomic_json(CHECKPOINTS / "stage_c_summary.json", summary)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
