#!/usr/bin/env python3
"""Execute the frozen dense sealer past one eager-default orchestration bug.

The frozen ``seal_dense`` implementation evaluates ``tier["seed_start"]``
while constructing the unused default argument to ``dict.get``, even when
the tier already has the authoritative ``seed_blocks`` entry.  This wrapper
adds only that redundant key to the in-memory protocol object and then calls
the otherwise unchanged frozen sealer.

It does not read scientific arrays except through the frozen sealer's
predeclared schema/hash checks, and it does not modify any frozen source,
protocol, result archive, seed schedule, or decision rule.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "protocol" / "run_grid.py"
MANIFEST = ROOT / "protocol" / "FROZEN_DYNAMICS_MANIFEST.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    expected_runner = manifest["files"]["protocol/run_grid.py"]
    if sha256(RUNNER) != expected_runner:
        raise RuntimeError("frozen run_grid.py hash mismatch")
    spec = importlib.util.spec_from_file_location("frozen_run_grid", RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen run_grid.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for tier_name in ("screening_reference", "heldout_confirmation"):
        tier = module.PROTOCOL[tier_name]
        if "seed_start" in tier or "seed_blocks" not in tier:
            raise RuntimeError(
                f"{tier_name}: amendment precondition does not hold"
            )
        tier["seed_start"] = int(tier["seed_blocks"][0][0])
    module.seal_dense()


if __name__ == "__main__":
    main()
