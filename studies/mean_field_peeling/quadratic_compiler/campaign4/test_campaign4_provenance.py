from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_frozen_hashes_match_provenance():
    provenance = json.loads((HERE/"provenance_order9.json").read_text())
    hashes = provenance["hashes"]
    mapping = {
        "protocol_sha256": HERE/"PROTOCOL.md",
        "results_report_sha256": HERE/"RESULTS.md",
        "wrapper_source_sha256": HERE/"sector_wrapper.cpp",
        "campaign1_graded_source_sha256": (
            HERE.parent/"campaign1/graded_sector.cpp"
        ),
        "runner_sha256": HERE/"run_sectors.py",
        "reference_source_sha256": HERE/"bivariate_reference.py",
        "postprocessor_sha256": HERE/"postprocess.py",
        "provenance_builder_sha256": HERE/"make_provenance.py",
        "frozen_campaign1_result_sha256": (
            HERE.parent/"campaign1/results_order9_q2_order8.json"
        ),
        "result_sha256": HERE/"results_order9.json",
        "certificate_sha256": HERE/"certificates_order9.json",
        "budget_ledger_sha256": HERE/"production_budget.json",
    }
    for key, path in mapping.items():
        assert hashes[key] == sha256(path)

    binary = HERE/"bin/sector_wrapper"
    if binary.exists():
        assert hashes["binary_sha256_when_locally_present"] == sha256(binary)


def test_denominator_origin_and_resource_limits_are_explicit():
    provenance = json.loads((HERE/"provenance_order9.json").read_text())
    assert provenance["validation"][
        "all_denominators_positive_including_origin"
    ] is True
    assert provenance["production_measurement"][
        "cumulative_wall_seconds"
    ] <= provenance["resource_precommit"][
        "cumulative_production_wall_seconds"
    ]
    assert provenance["production_measurement"]["sector_count"] == 125

