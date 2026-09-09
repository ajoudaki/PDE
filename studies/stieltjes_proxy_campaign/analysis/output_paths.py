"""Output-only checks shared by the analysis CLI and its callable writer."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
GENERATED_ROOT = REPO_ROOT / "data/generated/stieltjes_proxy_campaign"


def require_output(path: str | Path) -> Path:
    output = Path(path).resolve()
    if output.is_relative_to(REPO_ROOT) and not output.is_relative_to(GENERATED_ROOT):
        raise ValueError(f"fresh output must be under {GENERATED_ROOT} or external scratch: {output}")
    return output


def require_new_output(path: str | Path) -> tuple[Path, Path]:
    selected = Path(path)
    output = require_output(selected)
    temporary = output.with_suffix(output.suffix + ".tmp")
    for candidate in (selected, output, temporary):
        if candidate.exists() or candidate.is_symlink():
            raise FileExistsError(f"refusing to overwrite analysis result or temporary: {candidate}")
    return output, temporary
