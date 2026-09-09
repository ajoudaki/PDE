"""Read retained campaign evidence separately from newly computed outputs.

PDE_QUADRATIC_INPUT_ROOT selects a complete evidence tree relative to this study;
PDE_QUADRATIC_OUTPUT_ROOT selects the corresponding fresh generated tree. No
directories are created on import and historical provenance is never renewed.
"""

import os
from pathlib import Path

STUDY_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = STUDY_ROOT.parents[1]
HISTORICAL_ROOT = REPOSITORY_ROOT / "data/historical/studies" / STUDY_ROOT.name
INPUT_ROOT = Path(os.environ.get("PDE_QUADRATIC_INPUT_ROOT", str(HISTORICAL_ROOT))).resolve()
OUTPUT_ROOT = Path(os.environ.get(
    "PDE_QUADRATIC_OUTPUT_ROOT",
    str(REPOSITORY_ROOT / "data/generated" / STUDY_ROOT.name),
)).resolve()

for protected in (REPOSITORY_ROOT / name for name in (
    "studies", "docs", "code", ".git", "data/historical", "data/original_backups",
    "data/runtime_cache",
)):
    if (OUTPUT_ROOT == protected or protected in OUTPUT_ROOT.parents
            or OUTPUT_ROOT in protected.parents):
        raise ValueError("Campaign output must not replace source or retained evidence.")


def recorded_sector_path(recorded: str) -> Path:
    """Resolve an old sector label without changing the frozen manifest bytes."""
    path = Path(recorded)
    prefixes = ("studies/mfp_quadratic_compiler/",
                "studies/mean_field_peeling/quadratic_compiler/")
    label = path.as_posix()
    if path.is_absolute():
        try:
            label = path.relative_to(REPOSITORY_ROOT).as_posix()
        except ValueError:
            return path
    for prefix in prefixes:
        if label.startswith(prefix):
            return INPUT_ROOT / label[len(prefix):]
    return path if path.is_absolute() else REPOSITORY_ROOT / path


def certificate_path(relative: str) -> Path:
    """Fixed certificates are source artifacts; an explicit replay selects new ones."""
    base = INPUT_ROOT if "PDE_QUADRATIC_INPUT_ROOT" in os.environ else STUDY_ROOT
    return base / relative
