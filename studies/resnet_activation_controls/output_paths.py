"""Output boundaries only; no changes to frozen scientific authorization."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from studies._output_paths import StudyPaths

PATHS = StudyPaths(__file__)
require_output = PATHS.require_output


def require_raw_output(path: Path, inputs=()) -> Path:
    """Guard the final and deterministic partial before any raw run starts."""
    output = require_output(path)
    partial = output.with_suffix(output.suffix + ".partial")
    require_output(partial)
    for selected in inputs:
        if selected is None:
            continue
        source = Path(selected).resolve()
        for target in (output, partial):
            if target == source or (target.exists() and source.exists() and target.samefile(source)):
                raise ValueError(f"raw output aliases an input: {selected}")
    if partial.exists():
        raise FileExistsError(f"stale partial blocks raw output: {partial}")
    return output
