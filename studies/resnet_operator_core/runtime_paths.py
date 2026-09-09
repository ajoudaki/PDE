"""Separate source, selected read-only evidence, and newly generated outputs.

Environment overrides select a fresh run directory and, optionally, a different
input directory. Importing this module never creates a directory. Historical
archives are inputs only; no implicit fallback mixes them with a fresh run.
"""

from __future__ import annotations

import os
from pathlib import Path

STUDY_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = STUDY_ROOT.parents[1]


def output_root() -> Path:
    path = Path(os.environ.get(
        "PDE_OPERATOR_OUTPUT_ROOT",
        str(REPOSITORY_ROOT / "data" / "generated" / STUDY_ROOT.name),
    )).expanduser().resolve()
    protected = [REPOSITORY_ROOT / name for name in (
        "studies", "docs", "code", ".git", "data/historical", "data/runtime_cache",
        "data/original_backups",
    )]
    if path == REPOSITORY_ROOT or any(
        path == base or base in path.parents or path in base.parents
        for base in protected
    ):
        raise ValueError("Select a fresh output directory, not source or historical evidence.")
    return path


OUTPUT_ROOT = output_root()
INPUT_ROOT = Path(os.environ.get(
    "PDE_OPERATOR_INPUT_ROOT", str(OUTPUT_ROOT),
)).expanduser().resolve()
