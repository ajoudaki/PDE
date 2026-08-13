from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def test_frozen_hashes_match_provenance():
    provenance = json.loads((HERE/"provenance_order7.json").read_text())
    mapping = {
        "source_sha256": HERE/"centered_connected.cpp",
        "raw_results_sha256": HERE/"frozen/results_order7.json",
        "reference_source_sha256": HERE/"centered_reference.py",
        "postprocess_source_sha256": HERE/"postprocess.py",
        "certificates_sha256": HERE/"certificates_order7.json",
    }
    for key, path in mapping.items():
        assert provenance[key] == sha256(path)

    # The binary is intentionally ignored: a clean checkout reconstructs it
    # from the frozen source and compile command.  When a local frozen binary
    # is present, still check its historical hash exactly.
    binary = HERE/"frozen/centered_connected"
    if binary.exists():
        assert provenance["binary_sha256"] == sha256(binary)
