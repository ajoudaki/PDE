"""Explicit fresh output and historical input roots; no compatibility mirror."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GENERATED_ROOT = REPO_ROOT / "data/generated/mfp_gaussian_calculus"
HISTORICAL_ROOT = REPO_ROOT / "data/historical/studies/mfp_gaussian_calculus"


def input_directory(relative: str, *, historical: bool = False) -> Path:
    return (HISTORICAL_ROOT if historical else GENERATED_ROOT) / relative


def require_output(path: Path) -> Path:
    path = Path(path).resolve()
    if path.is_relative_to(REPO_ROOT) and not path.is_relative_to(REPO_ROOT / "data/generated"):
        raise ValueError(f"fresh output must be generated data, not source/history: {path}")
    return path
