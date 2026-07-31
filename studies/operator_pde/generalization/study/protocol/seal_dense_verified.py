#!/usr/bin/env python3
"""Verify the historical dense-seal amendment, then execute it unchanged."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
AMENDMENT = ROOT / "protocol" / "POSTFREEZE_EXECUTION_AMENDMENT.json"
WRAPPER = ROOT / "protocol" / "seal_dense_postfreeze_amendment.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    record = json.loads(AMENDMENT.read_text())
    if record["wrapper"] != "protocol/seal_dense_postfreeze_amendment.py":
        raise RuntimeError("unexpected dense-seal amendment wrapper")
    if record["wrapper_sha256"] != sha256(WRAPPER):
        raise RuntimeError("dense-seal amendment wrapper hash mismatch")
    subprocess.run([sys.executable, str(WRAPPER)], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
