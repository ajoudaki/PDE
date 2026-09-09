"""Separate source, selected read-only evidence, and newly generated outputs.

Environment overrides select a fresh run directory and, optionally, a different
input directory. Importing this module never creates a directory. Historical
archives are inputs only; no implicit fallback mixes them with a fresh run.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

STUDY_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = STUDY_ROOT.parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))
from studies._output_paths import reject_output_links


def output_root() -> Path:
    selected = Path(os.environ.get(
        "PDE_OPERATOR_OUTPUT_ROOT",
        str(REPOSITORY_ROOT / "data" / "generated" / STUDY_ROOT.name),
    )).expanduser().absolute()
    path = selected.resolve()
    protected = [REPOSITORY_ROOT / name for name in (
        "studies", "docs", "code", ".git", "data/historical", "data/runtime_cache",
        "data/original_backups",
    )]
    if path == REPOSITORY_ROOT or any(
        path == base or base in path.parents or path in base.parents
        for base in protected
    ):
        raise ValueError("Select a fresh output directory, not source or historical evidence.")
    reject_output_links(selected)
    return path


OUTPUT_ROOT = output_root()
INPUT_ROOT = Path(os.environ.get(
    "PDE_OPERATOR_INPUT_ROOT", str(OUTPUT_ROOT),
)).expanduser().resolve()


def require_new_archive(path: Path, inputs=()) -> tuple[Path, Path]:
    """Check the concrete archive and partial before constructing a trajectory."""
    path = Path(path).expanduser().absolute()
    partial = path.with_suffix(path.suffix + ".partial")
    for target in (path, partial):
        reject_output_links(target)
        for source in inputs:
            source = Path(source)
            if target.resolve() == source.resolve() or (
                target.exists() and source.exists() and target.samefile(source)
            ):
                raise ValueError(f"output aliases a consumed input: {source}")
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"refusing to overwrite archive or partial: {target}")
    return path, partial
