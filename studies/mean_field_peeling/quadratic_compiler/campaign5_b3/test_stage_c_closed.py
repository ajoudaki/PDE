"""The failed projection gate must make Stage-C production fail closed."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess


HERE = Path(__file__).resolve().parent


def test_projection_is_terminally_unauthorized() -> None:
    provenance = json.loads(
        (HERE / "provenance_stage_c_projection.json").read_text()
    )
    assert provenance["status"] == "failed_closed_unauthorized"
    assert not provenance["authorization_conditions"]["stage_c_authorized"]
    assert not provenance["fresh_final_source_pilots"][0][
        "completed_order_seven"
    ]


def test_runner_refuses_to_launch_any_binary() -> None:
    completed = subprocess.run(
        ["python3", str(HERE / "run_stage_c.py"), "/does/not/exist"],
        text=True,
        capture_output=True,
    )
    assert completed.returncode != 0
    assert "closed unauthorized" in completed.stderr

