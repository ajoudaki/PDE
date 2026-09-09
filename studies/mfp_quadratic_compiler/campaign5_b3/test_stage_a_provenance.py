from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_stage_a_durable_hashes_and_status():
    data = json.loads((HERE / "provenance_stage_a.json").read_text())
    assert data["protocol_sha256"] == sha256(HERE / "PROTOCOL.md")
    assert data["reference"]["source_sha256"] == sha256(HERE / "b3_reference.py")
    assert data["connected"]["source_sha256"] == sha256(HERE / "b3_connected.cpp")
    assert data["reference"]["raw_output_sha256"] == sha256(
        HERE / "frozen/stage_a_reference_order3.json"
    )
    assert data["connected"]["raw_output_sha256"] == sha256(
        HERE / "frozen/stage_a_connected_order3.json"
    )
    assert data["reference"]["peak_rss_kib"] < 2 * 1024 * 1024
    assert data["connected"]["peak_rss_kib"] < 2 * 1024 * 1024
    assert data["reference"]["wall_seconds"] < 600
    assert data["connected"]["wall_seconds"] < 600
    assert "Stage A passed" in data["classification"]
    assert "Stage C remains unauthorized" in data["next_branch"]


def test_stage_b_durable_hashes_caps_and_novelty():
    data = json.loads((HERE / "provenance_stage_b.json").read_text())
    assert data["protocol_sha256"] == sha256(HERE / "PROTOCOL.md")
    assert data["connected"]["source_sha256"] == sha256(HERE / "b3_connected.cpp")
    assert data["connected"]["raw_output_sha256"] == sha256(
        HERE / "frozen/stage_b_connected_order5.json"
    )
    assert data["connected"]["peak_rss_kib"] < 4 * 1024 * 1024
    assert data["connected"]["wall_seconds"] < 1800
    assert data["validation"]["scale_invariant_I_nonconstant"]
    assert len({data["validation"][key] for key in (
        "I_at_minus_half", "I_at_zero", "I_at_one"
    )}) == 3
    assert data["stage_c_status"].startswith("unauthorized")
