"""Verify that the canonical report embeds every frozen scalar transition."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
REPORT = HERE / "ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md"
INDEPENDENT = HERE / "independent"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def embedded_formulas() -> dict[str, str]:
    text = REPORT.read_text()
    appendix = text[text.index("# Appendix A:") :]
    rows = re.findall(r"### `([^`]+)`\n\n```text\n([^\n]+)\n```", appendix)
    result = {
        name: formula.removeprefix(name + " = ") for name, formula in rows
    }
    if len(result) != len(rows):
        raise AssertionError("duplicate embedded transition name")
    return result


def expected_formulas() -> dict[str, str]:
    forward = json.loads((INDEPENDENT / "FROZEN_FORWARD_RECURRENCE.json").read_text())
    reverse = json.loads((INDEPENDENT / "FROZEN_REVERSE_RECURRENCE.json").read_text())
    moving = json.loads((INDEPENDENT / "FROZEN_MOVING_RECURRENCE.json").read_text())
    result = dict(forward["formatted"])
    result.update(reverse["formatted"])
    for group in moving["formatted"].values():
        result.update(group)
    return result


def verify() -> dict[str, object]:
    embedded = embedded_formulas()
    expected = expected_formulas()
    missing = sorted(set(expected) - set(embedded))
    extra = sorted(set(embedded) - set(expected))
    unequal = sorted(name for name in set(expected) & set(embedded) if expected[name] != embedded[name])
    text = REPORT.read_text()
    required_markers = [
        r"\boxed{7\;/\;8\;/\;4\;/\;4\;/\;3\;/\;3}",
        "C_H=2S_{5,H}+10AC+10Bm2+4M2+12Am3",
        r"\mu_{1,H}=\frac{4B_H^2-A_HC_H}{24A_H^5}",
        "does **not** realize the stronger one-forward/one-backward schematic",
        "top-down pass remains open",
    ]
    absent_markers = [marker for marker in required_markers if marker not in text]
    result = {
        "report": str(REPORT.relative_to(HERE.parent.parent.parent.parent)),
        "report_sha256": sha256(REPORT),
        "expected_transition_count": len(expected),
        "embedded_transition_count": len(embedded),
        "missing": missing,
        "extra": extra,
        "unequal": unequal,
        "absent_required_markers": absent_markers,
        "source_hashes": {
            name: sha256(INDEPENDENT / name)
            for name in (
                "FROZEN_FORWARD_RECURRENCE.json",
                "FROZEN_REVERSE_RECURRENCE.json",
                "FROZEN_MOVING_RECURRENCE.json",
            )
        },
    }
    if missing or extra or unequal or absent_markers:
        raise AssertionError(result)
    result["decision"] = "PASS: canonical report embeds every frozen transition literally"
    return result


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
