from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from campaign_paths import INPUT_ROOT, certificate_path, recorded_sector_path



def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def test_frozen_hashes_match_provenance():
    provenance = json.loads((INPUT_ROOT / "campaign3/provenance_order7.json").read_text())
    mapping = {
        "source_sha256": HERE/"centered_connected.cpp",
        "raw_results_sha256": INPUT_ROOT / "campaign3/frozen/results_order7.json",
        "reference_source_sha256": HERE/"centered_reference.py",
        "postprocess_source_sha256": HERE/"postprocess.py",
        "certificates_sha256": certificate_path("campaign3/certificates_order7.json"),
    }
    for key, path in mapping.items():
        assert provenance[key] == sha256(path)

    # The binary is intentionally ignored: a clean checkout reconstructs it
    # from the frozen source and compile command.  When a local frozen binary
    # is present, still check its historical hash exactly.
    binary = INPUT_ROOT / "campaign3/frozen/centered_connected"
    if binary.exists():
        assert provenance["binary_sha256"] == sha256(binary)
