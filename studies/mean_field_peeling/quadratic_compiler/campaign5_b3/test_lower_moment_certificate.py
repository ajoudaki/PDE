"""Recompute and audit the post-hoc exact lower-moment certificate."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess


HERE = Path(__file__).resolve().parent


def test_lower_moment_certificate_recomputes_exactly() -> None:
    completed = subprocess.run(
        ["python3", str(HERE / "postprocess_lower_moments.py")],
        check=True,
        text=True,
        capture_output=True,
    )
    computed = json.loads(completed.stdout)
    frozen = json.loads((HERE / "certificates_lower_moments.json").read_text())
    assert computed == frozen
    assert all(
        piece["distinct_real_root_count"] == 0
        and piece["left_sign"] == 1
        and piece["right_sign"] == 1
        for pieces in computed["sturm_certificates"].values()
        for piece in pieces
    )
    conclusions = computed["conclusions"]
    assert conclusions["mu0_positive_on_full_domain"]
    assert conclusions["mu1_positive_on_full_domain"]
    assert not conclusions["mu2_available"]
    assert not conclusions["ordinary_H1_available"]

