"""Freeze exact-byte hashes for Route S before any cross-route comparison."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[4]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    artifact_names = [
        f"H{depth}_{suffix}"
        for depth in (3, 4)
        for suffix in (
            "LAYER_TAGGED_ABC.cse.txt",
            "LAYER_TAGGED_COEFFICIENTS.json",
            "UNIT_ABC.cse.txt",
            "UNIT_COEFFICIENTS.json",
            "ARTIFACT_STATS.json",
        )
    ]
    local_source_names = [
        "ROUTE_S_CONTRACT.md",
        "EVIDENCE_LEDGER.md",
        "depth_population_jet.py",
        "generate_frozen_artifacts.py",
        "test_depth_population_jet.py",
    ]
    dependency_paths = [
        PROJECT / "studies/mean_field_peeling/generic_first_stieltjes/order5/compiler/factored_expression.py",
        PROJECT / "studies/mean_field_peeling/generic_first_stieltjes/order5/compiler/population_jet.py",
        PROJECT / "studies/mean_field_peeling/generic_first_stieltjes/order5/compiler/coefficient_map.py",
    ]
    stats = {
        str(depth): json.loads((HERE / f"H{depth}_ARTIFACT_STATS.json").read_text())
        for depth in (3, 4)
    }
    manifest = {
        "schema": "route-s-primary-freeze-v1",
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "frozen_before_cross_route_formula_inspection": True,
        "scope": "H=3,4; B=1; ordinary derivatives through five",
        "normal_forms": {
            "arbitrary_forward_variance": "layer tags retained; Q0 explicit",
            "unit_gram": "all layer atoms identified; Q0=M_200000=1",
        },
        "artifacts": {
            name: {"sha256": sha256(HERE / name), "bytes": (HERE / name).stat().st_size}
            for name in artifact_names
        },
        "local_sources": {
            name: sha256(HERE / name) for name in local_source_names
        },
        "dependencies": {
            str(path.relative_to(PROJECT)): sha256(path) for path in dependency_paths
        },
        "term_counts": {
            depth: {
                "tagged": record["tagged_term_counts"],
                "unit": record["unit_term_counts"],
            }
            for depth, record in stats.items()
        },
        "dag_node_counts": {
            depth: {
                "tagged": record["tagged_dag_node_counts"],
                "unit": record["unit_dag_node_counts"],
            }
            for depth, record in stats.items()
        },
        "pre_freeze_audits": {
            "H2_tagged_atomwise_difference_counts_ABC": [0, 0, 0],
            "H2_unit_atomwise_difference_counts_ABC": [0, 0, 0],
            "parity_H3_H4": True,
            "terminal_maximum_derivative_ABC": [1, 3, 5],
            "polynomial_controls_recorded_in_stats": True,
        },
    }
    manifest_path = HERE / "PRIMARY_FREEZE_MANIFEST.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    digest = sha256(manifest_path)
    (HERE / "PRIMARY_FREEZE_SHA256.txt").write_text(
        f"{digest}  {manifest_path.name}\n", encoding="utf-8"
    )
    print(digest)


if __name__ == "__main__":
    main()
