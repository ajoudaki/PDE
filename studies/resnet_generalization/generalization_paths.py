"""Source and evidence locations for the flat generalization study."""

from pathlib import Path
import sys

STUDY_ROOT = Path(__file__).resolve().parent
REPO_ROOT = STUDY_ROOT.parents[1]
GENERATED_ROOT = REPO_ROOT / "data/generated/resnet_generalization"
RESULTS = GENERATED_ROOT / "results/generalization"
HISTORICAL_RESULTS = REPO_ROOT / "data/historical/studies/resnet_generalization/results/generalization"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from studies._output_paths import reject_output_links


def evidence_root(results: Path) -> Path:
    """The root of logical results/generalization/... evidence labels."""
    return Path(results).resolve().parents[1]


def evidence_label(path: Path, results: Path) -> str:
    return Path(path).resolve().relative_to(evidence_root(results)).as_posix()


def evidence_path(label: str, results: Path) -> Path:
    relative = Path(label)
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in label.split("/")):
        raise ValueError(f"unsafe evidence label: {label!r}")
    root = evidence_root(results)
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"evidence label escapes its root: {label!r}")
    return path


def require_output(path: Path) -> Path:
    selected = path
    path = Path(path).resolve()
    if path.is_relative_to(REPO_ROOT) and not path.is_relative_to(GENERATED_ROOT):
        raise ValueError(f"fresh output must be under {GENERATED_ROOT} or external scratch: {path}")
    reject_output_links(selected)
    return path


def precheck_command(python: str, results: Path, output: Path) -> list[str]:
    return [python, str(STUDY_ROOT / "pde_precheck.py"), "--results-dir", str(results), "--output", str(output)]
