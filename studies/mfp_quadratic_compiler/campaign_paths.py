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


def require_distinct_output(output: Path, inputs=()) -> Path:
    """Reject pre-existing input aliases, allowing deliberate output updates.

    This checks resolved names and existing file identity, not concurrent
    filesystem changes. Mutable checkpoints are not read-only inputs to
    their own update operation; separate exports must still avoid them.
    """
    output = Path(output).expanduser().absolute()
    for source in inputs:
        source = Path(source)
        if output.resolve() == source.resolve() or (
            output.exists() and source.exists() and output.samefile(source)
        ):
            raise ValueError(f"output aliases an input: {source}")
    return output


def require_new_output(output: Path, inputs=()) -> Path:
    """Refuse input aliases and occupied destinations before postprocessing.

    Callers create direct outputs exclusively or publish a unique temporary
    file. This is a pre-existing-alias guard, not a concurrent-adversary claim.
    """
    output = require_distinct_output(output, inputs)
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"refusing to overwrite existing output: {output}")
    return output
