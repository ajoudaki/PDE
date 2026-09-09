#!/usr/bin/env python3
"""Build the durable Campaign-4 provenance record from frozen artifacts."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    descriptor, temporary = tempfile.mkstemp(
        prefix=path.name+".", suffix=".tmp", dir=path.parent
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


def main() -> None:
    result_path = HERE/"results_order9.json"
    certificate_path = HERE/"certificates_order9.json"
    budget_path = HERE/"production_budget.json"
    result = json.loads(result_path.read_text())
    budget = json.loads(budget_path.read_text())
    binary = HERE/"bin/sector_wrapper"
    provenance = {
        "schema_version": 1,
        "campaign": "two-independent-block metric, exact output order nine",
        "metric": "D_a + alpha D_u + beta D_W; alpha,beta >= 0",
        "working_directory": "/home/amir/Codes/PDE",
        "compiler": subprocess.run(
            ["g++", "--version"], check=True, text=True,
            stdout=subprocess.PIPE
        ).stdout.splitlines()[0],
        "compile_command": (
            "g++ -std=c++17 -O3 -DNDEBUG "
            "studies/mean_field_peeling/quadratic_compiler/campaign4/"
            "sector_wrapper.cpp -o studies/mean_field_peeling/"
            "quadratic_compiler/campaign4/bin/sector_wrapper"
        ),
        "production_command": (
            "python3 studies/mean_field_peeling/quadratic_compiler/campaign4/"
            "run_sectors.py --binary studies/mean_field_peeling/"
            "quadratic_compiler/campaign4/bin/sector_wrapper --sectors "
            "studies/mean_field_peeling/quadratic_compiler/campaign4/sectors "
            "--output studies/mean_field_peeling/quadratic_compiler/"
            "campaign4/results_order9.json --budget-ledger studies/"
            "mean_field_peeling/quadratic_compiler/campaign4/"
            "production_budget.json --max-seconds 1800 "
            "--memory-bytes 4294967296"
        ),
        "postprocess_command": (
            "python3 studies/mean_field_peeling/quadratic_compiler/"
            "campaign4/postprocess.py"
        ),
        "hashes": {
            "protocol_sha256": sha256(HERE/"PROTOCOL.md"),
            "results_report_sha256": sha256(HERE/"RESULTS.md"),
            "wrapper_source_sha256": sha256(HERE/"sector_wrapper.cpp"),
            "campaign1_graded_source_sha256": sha256(
                HERE.parent/"campaign1/graded_sector.cpp"
            ),
            "parent_sector_engine_sha256": result["source_identity"][
                "parent_sector_engine_sha256"
            ],
            "runner_sha256": sha256(HERE/"run_sectors.py"),
            "reference_source_sha256": sha256(HERE/"bivariate_reference.py"),
            "postprocessor_sha256": sha256(HERE/"postprocess.py"),
            "provenance_builder_sha256": sha256(Path(__file__)),
            "frozen_campaign1_result_sha256": sha256(
                HERE.parent/"campaign1/results_order9_q2_order8.json"
            ),
            "result_sha256": sha256(result_path),
            "certificate_sha256": sha256(certificate_path),
            "budget_ledger_sha256": sha256(budget_path),
            "binary_sha256_when_locally_present": (
                sha256(binary) if binary.exists() else
                result["source_identity"]["binary_sha256"]
            ),
        },
        "binary_policy": (
            "The binary is ignored by Git. Its historical hash is retained; "
            "clean-checkout tests compile the frozen source independently."
        ),
        "resource_precommit": {
            "per_sector_virtual_memory_bytes": 4*1024**3,
            "cumulative_production_wall_seconds": 1800,
            "target_order": 9,
            "forbidden": ["F11", "Q2", "other observables"],
        },
        "production_measurement": {
            "completed": True,
            "cumulative_wall_seconds": budget["cumulative_wall_seconds"],
            "sector_count": result["production"]["sector_count"],
            "atomic_sector_files": result["production"]["sector_count"],
            "per_sector_memory_cap_bytes": result["production"][
                "memory_bytes_per_sector"
            ],
            "measured_peak_rss": None,
            "peak_rss_note": (
                "RLIMIT_AS was enforced independently on every sector; peak "
                "resident memory was not separately measured."
            ),
        },
        "validation": {
            "all_125_atomic_sector_hashes_in_result_manifest": True,
            "checked_512_bit_arithmetic": True,
            "all_diagonal_coefficients_through_F9_match_campaign1": True,
            "canonical_point_through_F9_matches_accepted_jets": True,
            "independent_whole_forest_all_coefficients_through_F5": True,
            "independent_off_diagonal_points_through_F5": True,
            "feature_parity_through_order_8": True,
            "all_denominators_positive_including_origin": True,
            "mu0_through_mu3_coefficientwise_positive_off_origin": True,
            "ordinary_H1_coefficientwise_positive_off_origin": True,
            "shifted_H1_coefficientwise_positive_off_origin": True,
        },
        "primary_decision": {
            "status": "strictly_positive_except_at_degenerate_origin",
            "shifted_numerator_term_count": 169,
            "shifted_numerator_total_degree": 18,
            "zero_set_on_closed_quadrant": [[0, 0]],
        },
        "claim_limit": (
            "Exact finite-order formal-jet family certificate only; not an "
            "all-order Stieltjes theorem or global mean-field trajectory "
            "identification theorem."
        ),
    }
    atomic_json(HERE/"provenance_order9.json", provenance)


if __name__ == "__main__":
    main()
