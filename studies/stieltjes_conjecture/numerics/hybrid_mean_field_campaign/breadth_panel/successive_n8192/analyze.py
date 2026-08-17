#!/usr/bin/env python3
"""Analyze n=8192 with the exact retained n=4096 analysis implementation.

The n=4096 analysis source is hash-checked and transformed in memory only at
the four width-specific contracts.  This keeps the original runner and its
retained manifest hashes untouched while preventing the two analyses from
drifting in their estimands, bootstrap, proxy evaluation, or reporting.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import types


HERE = Path(__file__).resolve().parent
BASE_ANALYZER = HERE.parent / "successive_n4096" / "analyze.py"
EXPECTED_BASE_SHA256 = "731eeddbf362aebd89991a9dd83f8fe5db324ffc6764d9c44326d1df8fc34dd8"
TRANSFORM = (
    ("n4096", "n8192", 4),
    ("n=4096", "n=8192", 3),
    ("== 4096", "== 8192", 1),
    ("[2048, 4096]", "[2048, 4096, 8192]", 1),
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def load_analyzer() -> types.ModuleType:
    source_bytes = BASE_ANALYZER.read_bytes()
    actual_sha256 = sha256_bytes(source_bytes)
    if actual_sha256 != EXPECTED_BASE_SHA256:
        raise RuntimeError(
            "n=4096 analysis source changed; refusing an unreviewed n=8192 transform: "
            f"{actual_sha256} != {EXPECTED_BASE_SHA256}"
        )
    source = source_bytes.decode("utf-8")
    for old, new, expected_count in TRANSFORM:
        actual_count = source.count(old)
        if actual_count != expected_count:
            raise RuntimeError(
                f"unexpected transform count for {old!r}: "
                f"{actual_count} != {expected_count}"
            )
        source = source.replace(old, new)

    module_name = "breadth_successive_n8192_transformed_analysis"
    module = types.ModuleType(module_name)
    module.__file__ = str(Path(__file__).resolve())
    sys.modules[module_name] = module
    exec(compile(source, str(Path(__file__).resolve()), "exec"), module.__dict__)
    return module


def main() -> int:
    return int(load_analyzer().main())


if __name__ == "__main__":
    raise SystemExit(main())
