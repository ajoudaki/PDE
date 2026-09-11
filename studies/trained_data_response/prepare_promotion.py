"""Assemble the proposed edition in a fresh generated directory only.

The actual established files are read-only inputs. This is not an installer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
EXPECTED = {
    "docs/global_nonlinear.md": "d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1",
    "docs/README.md": "7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e",
    "docs/NOTATION.md": "199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b",
    "docs/finite_dynamics.md": "a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a",
    "docs/special_data_limits.md": "5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489",
}

EDITS = [
    {
        "path": "docs/global_nonlinear.md",
        "old": "Sections C.4.1–C.4.4 prove a local quantitative statement about the actual nonlinear\nlearning algorithm. The separate fixed-accuracy extension is in C.4.5. The proof retains the Gaussian matrix action and its\nadjoint and permits every training law on the compact observation space.",
        "new": "Sections C.4.1–C.4.4 prove a local quantitative statement about the actual nonlinear\nlearning algorithm. The separate fixed-accuracy extension is in C.4.5.\nSection C.4.6 identifies actual finite-GF data derivatives at that fitted\nreference on each fixed horizon and bounds the population homogeneous\npropagator uniformly in time. The local theorem retains the Gaussian matrix\naction and its adjoint and permits every training law on the compact\nobservation space.",
    },
    {
        "path": "docs/README.md",
        "old": "with early paired hidden activity; it does not construct global perturbed-law population dynamics. |",
        "new": "with early paired hidden activity; it does not construct global perturbed-law population dynamics. At that fitted reference, a separate response theorem captures actual finite-GF data derivatives on each fixed horizon and the whole circle, with uniformly bounded population homogeneous propagation and total-variation forcing control. |",
    },
    {
        "path": "docs/README.md",
        "old": "that feature learning outperforms frozen or linear models.\nA global input-population theorem",
        "new": "that feature learning outperforms frozen or linear models. Section C.4.6\nseparately captures actual finite-GF data derivatives at this trained reference\non each fixed horizon, with a population homogeneous propagator bounded\nuniformly in time. Its total-variation forcing bound gives response control\nlinear in the horizon; it constructs neither nonlinear changed-law population\nflows nor a finite-contamination remainder.\nA global input-population theorem",
    },
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def assemble(section_path, output):
    section = section_path.read_bytes()
    if not section.startswith(b"#### C.4.6."):
        raise ValueError("canonical section must start at C.4.6")
    sources = {p: (ROOT / p).read_bytes() for p in EXPECTED}
    for p, data in sources.items():
        assert sha(data) == EXPECTED[p], f"Changed dependency: {p}"
    assert not output.exists(), "use a fresh output directory"
    output.mkdir(parents=True)
    result = {p: data.decode() for p, data in sources.items()}
    for edit in EDITS:
        assert result[edit["path"]].count(edit["old"]) == 1, edit["path"]
        result[edit["path"]] = result[edit["path"]].replace(edit["old"], edit["new"])
    result["docs/global_nonlinear.md"] += "\n" + section.decode().rstrip() + "\n"
    for p, content in result.items():
        dest = output / p
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)
    # Complete local link targets, without importing tools, history or Git.
    for p in (ROOT / "docs").glob("*.md"):
        dest = output / "docs" / p.name
        if not dest.exists():
            dest.write_bytes(p.read_bytes())
    (output / "code").mkdir()
    (output / "code/README.md").write_bytes((ROOT / "code/README.md").read_bytes())
    checks = output / "checks"
    checks.mkdir()
    for original, name in [("R1_CHECK_IDENTITIES.py", "identities.py"),
                           ("R1_REFERENCE_CERTIFICATE.py", "reference_certificate.py")]:
        (checks / name).write_bytes((BASE / original).read_bytes())
    manifest = {
        "section_sha256": sha(section),
        "base_sha256": EXPECTED,
        "edits": EDITS,
        "edition_sha256": {p: sha((output / p).read_bytes()) for p in result},
        "supporting_files": {str(p.relative_to(output)): sha(p.read_bytes())
                             for p in sorted(output.rglob("*")) if p.is_file()},
        "scope": "Standalone proposed edition; no established files written",
    }
    (output / "edition_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for p, data in sources.items():
        assert (ROOT / p).read_bytes() == data, f"Concurrent dependency change: {p}"
    print(json.dumps(manifest["edition_sha256"], indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--section", type=Path, default=BASE / "CANONICAL_SECTION.md")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    target = args.output.resolve()
    allowed = ROOT / "data/generated/trained_data_response"
    assert target.is_relative_to(allowed), "output must belong to this study's generated namespace"
    assemble(args.section.resolve(), target)
