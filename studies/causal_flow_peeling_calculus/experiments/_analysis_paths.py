"""Preflight the files published by the local CSV analyzers."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from studies._output_paths import StudyPaths

_PATHS = StudyPaths(__file__)


def guard_outputs(outputs, inputs):
    protected = {Path(path).resolve() for path in inputs if path is not None}
    for path in outputs:
        if path is None:
            continue
        output = _PATHS.require_output(Path(path).absolute())
        if output in protected:
            raise ValueError(f"output aliases a consumed input or another output: {path}")
        protected.add(output)
