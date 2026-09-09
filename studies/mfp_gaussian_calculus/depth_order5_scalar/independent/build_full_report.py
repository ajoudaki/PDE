"""Build the self-contained report by appending frozen literal equations."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def equation_appendix(title: str, payload_path: Path, groups: list[str] | None = None) -> str:
    payload = json.loads(payload_path.read_text())
    formatted = payload["formatted"]
    lines = [f"# {title}", ""]
    if groups is None:
        groups_data = [("transition", formatted)]
    else:
        groups_data = [(group, formatted[group]) for group in groups]
    for group, values in groups_data:
        if groups is not None:
            lines.extend((f"## {group}", ""))
        for name, formula in values.items():
            lines.extend((f"### `{name}`", "", "```text", f"{name} = {formula}", "```", ""))
    return "\n".join(lines)


def build() -> tuple[Path, str]:
    pieces = [
        (ROOT / "FULL_SCALAR_RECURRENCE_PREAMBLE.md").read_text().rstrip(),
        equation_appendix(
            "Appendix A: frozen forward transition",
            ROOT / "FROZEN_FORWARD_RECURRENCE.json",
        ).rstrip(),
        equation_appendix(
            "Appendix B: frozen reverse transition",
            ROOT / "FROZEN_REVERSE_RECURRENCE.json",
        ).rstrip(),
        equation_appendix(
            "Appendix C: moving-gradient transitions",
            ROOT / "FROZEN_MOVING_RECURRENCE.json",
            ["feature2", "gradient2", "feature3", "gradient3"],
        ).rstrip(),
    ]
    target = ROOT / "FULL_SCALAR_RECURRENCE.md"
    target.write_text("\n\n".join(pieces) + "\n")
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT / "FULL_SCALAR_RECURRENCE.sha256").write_text(
        digest + "  " + target.name + "\n"
    )
    return target, digest


if __name__ == "__main__":
    path, digest = build()
    print(path)
    print(digest)
