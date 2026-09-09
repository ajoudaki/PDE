#!/usr/bin/env python3
"""Run the frozen analyzer with one redundant-metadata compatibility fix."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
ANALYZER = ROOT / "analyze_generalization.py"
MANIFEST = ROOT / "protocol" / "FROZEN_DYNAMICS_MANIFEST.json"
AMENDMENT = ROOT / "protocol" / "POSTFREEZE_ANALYSIS_AMENDMENT.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    if sha256(ANALYZER) != manifest["files"]["analyze_generalization.py"]:
        raise RuntimeError("frozen analyzer hash mismatch")
    amendment = json.loads(AMENDMENT.read_text())
    if amendment["wrapper_sha256"] != sha256(Path(__file__)):
        raise RuntimeError("analysis-amendment wrapper hash mismatch")

    spec = importlib.util.spec_from_file_location("frozen_analyzer", ANALYZER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen analyzer")
    module = importlib.util.module_from_spec(spec)
    # Python 3.12's dataclass resolver expects the executing module to be
    # registered before decorators run.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    frozen_case_metadata = module._case_metadata

    def compatible_case_metadata(case):
        metadata = frozen_case_metadata(case)
        metadata.pop("m")
        metadata.pop("d")
        return metadata

    module._case_metadata = compatible_case_metadata

    frozen_metadata = module._metadata

    def compatible_metadata(path):
        metadata = frozen_metadata(path)
        if (
            "seed_ids" not in metadata
            and "seed_start" in metadata
            and "seeds" in metadata
            and "scientific_config_sha256" in metadata
        ):
            start = int(metadata["seed_start"])
            count = int(metadata["seeds"])
            metadata["seed_ids"] = list(range(start, start + count))
        return metadata

    module._metadata = compatible_metadata

    frozen_discover_dense = module.discover_dense_descriptors

    def compatible_discover_dense(results, cases, protocol, seal_hash, dynamics_hash):
        for key in ("screening_reference", "heldout_confirmation"):
            tier = protocol[key]
            if "seed_start" not in tier and "seed_blocks" in tier:
                tier["seed_start"] = int(tier["seed_blocks"][0][0])
        return frozen_discover_dense(
            results, cases, protocol, seal_hash, dynamics_hash
        )

    module.discover_dense_descriptors = compatible_discover_dense

    frozen_write_seal = module._write_processed_seal

    def amended_write_seal(**kwargs):
        frozen_write_seal(**kwargs)
        path = kwargs["results"] / "PROCESSED_STAGE_SEAL.json"
        record = json.loads(path.read_text())
        record["postfreeze_analysis_amendment_sha256"] = sha256(AMENDMENT)
        record["postfreeze_analysis_wrapper_sha256"] = sha256(Path(__file__))
        module._atomic_text(
            path,
            json.dumps(
                record, indent=2, sort_keys=True, allow_nan=False
            ) + "\n",
        )

    module._write_processed_seal = amended_write_seal
    args = module.parse_args()
    summary = module.run_analysis(args)
    print(
        json.dumps(
            {
                "summary": os.fspath(Path(args.output_dir) / "summary.json"),
                "broad_verdict": summary["broad_verdict"]["status"],
                "postfreeze_analysis_amendment": os.fspath(AMENDMENT),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
