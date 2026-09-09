"""Build the single-file report containing both complete arithmetic DAGs."""

from __future__ import annotations

from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
ORDER5 = HERE.parent
UNIT_BEGIN = "<!-- BEGIN EMBEDDED UNIT ARTIFACT -->\n```text\n"
UNIT_END = "```\n<!-- END EMBEDDED UNIT ARTIFACT -->"
SEPARATED_BEGIN = "<!-- BEGIN EMBEDDED LAYER-SEPARATED ARTIFACT -->\n```text\n"
SEPARATED_END = "```\n<!-- END EMBEDDED LAYER-SEPARATED ARTIFACT -->"


def embedded_payload(text: str, begin: str, end: str) -> str:
    return text.split(begin, 1)[1].split(end, 1)[0]


def main() -> None:
    body = (ORDER5 / "PRIMARY_GAUSSIAN_NORMAL_FORM.md").read_text().rstrip()
    unit_path = HERE / "UNIT_GRAM_ABC_NORMAL_FORM.txt"
    separated_path = HERE / "LAYER_SEPARATED_ABC_NORMAL_FORM.txt"
    unit = unit_path.read_text()
    separated = separated_path.read_text()
    appendix = f"""

## Appendix A. Complete unit-Gram arithmetic DAG

This appendix is part of the formula.  It is repeated here so the report is
self-contained.  Every assignment is deterministic and dependency first.

{UNIT_BEGIN}{unit}{UNIT_END}

## Appendix B. Complete layer-separated arbitrary-variance arithmetic DAG

Here `Q0` is the first forward Gram,
`X_nu` is evaluated at `N(0,Q0)`, `Q1=X_200000`, and `Y_nu` is evaluated at
`N(0,Q1)`.  Thus `Q2=Y_200000` remains explicit.

{SEPARATED_BEGIN}{separated}{SEPARATED_END}
"""
    report_path = ORDER5 / "H2_B1_ORDER5_SELF_CONTAINED.md"
    report = body + appendix
    assert embedded_payload(report, UNIT_BEGIN, UNIT_END) == unit
    assert embedded_payload(report, SEPARATED_BEGIN, SEPARATED_END) == separated
    report_path.write_text(report)
    manifest = {
        "embedded_byte_equality": {
            "unit_gram": True,
            "layer_separated": True,
        },
        "sha256": {
            "report": hashlib.sha256(report_path.read_bytes()).hexdigest(),
            "unit_gram": hashlib.sha256(unit_path.read_bytes()).hexdigest(),
            "layer_separated": hashlib.sha256(separated_path.read_bytes()).hexdigest(),
        },
    }
    (ORDER5 / "SELF_CONTAINED_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
