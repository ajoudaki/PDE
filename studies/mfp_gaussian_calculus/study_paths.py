"""Explicit fresh output and historical input roots; no compatibility mirror."""

from pathlib import Path

from studies._output_paths import StudyPaths

REPO_ROOT = Path(__file__).resolve().parents[2]
GENERATED_ROOT = REPO_ROOT / "data/generated/mfp_gaussian_calculus"
HISTORICAL_ROOT = REPO_ROOT / "data/historical/studies/mfp_gaussian_calculus"
_PATHS = StudyPaths(__file__)


def input_directory(relative: str, *, historical: bool = False) -> Path:
    return (HISTORICAL_ROOT if historical else GENERATED_ROOT) / relative


def require_output(path: Path) -> Path:
    return _PATHS.require_output(path)


def guard_output_inputs(outputs, inputs):
    """Protect explicitly selected inputs as well as source/retained paths."""
    protected = {Path(path).resolve() for path in inputs}
    for path in outputs:
        output = require_output(path)
        if output in protected:
            raise ValueError(f"output aliases a consumed input or another output: {path}")
        protected.add(output)
