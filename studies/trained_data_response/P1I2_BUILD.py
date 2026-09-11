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

# Unchanged link targets are structural support, not additional scientific
# dependencies of C.4.6. Pin every byte read by the standalone assembler.
SUPPORTING = {
    "docs/arctan_limits.md": "19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead",
    "docs/continuous_depth.md": "12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d",
    "docs/finite_optimization_and_controls.md": "80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628",
    "docs/gaussian_calculus.md": "d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e",
    "docs/linear_dynamics.md": "8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d",
    "code/README.md": "00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774",
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
    support = {p: (ROOT / p).read_bytes() for p in SUPPORTING}
    for p, data in support.items():
        assert sha(data) == SUPPORTING[p], f"Changed structural link target: {p}"
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
    for p, data in support.items():
        dest = output / p
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    checks = output / "checks"
    checks.mkdir()
    for original, name in [("P1_CHECK_IDENTITIES.py", "identities.py"),
                           ("P1_REFERENCE_CERTIFICATE.py", "reference_certificate.py")]:
        (checks / name).write_bytes((BASE / original).read_bytes())
    manifest = {
        "section_sha256": sha(section),
        "base_sha256": EXPECTED,
        "structural_support_sha256": SUPPORTING,
        "edits": EDITS,
        "edition_sha256": {p: sha((output / p).read_bytes()) for p in result},
        "supporting_files": {str(p.relative_to(output)): sha(p.read_bytes())
                             for p in sorted(output.rglob("*")) if p.is_file()},
        "scope": "Standalone proposed edition; no established files written",
    }
    (output / "edition_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for p, data in sources.items():
        assert (ROOT / p).read_bytes() == data, f"Concurrent dependency change: {p}"
    for p, data in support.items():
        assert (ROOT / p).read_bytes() == data, f"Concurrent structural support change: {p}"
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
