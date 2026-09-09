"""Protect selected recurrence inputs before downstream audit work."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from studies._output_paths import StudyPaths

_PATHS = StudyPaths(__file__)


def guard_output(output, inputs):
    if output is None:
        return
    selected = _PATHS.require_output(Path(output).absolute())
    if selected in {Path(path).resolve() for path in inputs}:
        raise ValueError(f"output aliases a consumed input: {output}")
