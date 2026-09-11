"""Freeze an integration-only revision without changing scientific inputs."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    previous = json.loads((BASE / "P1_MANIFEST.json").read_text())
    for name, value in previous["inputs"].items():
        assert sha((BASE / name).read_bytes()) == value["sha256"], name
    spec = importlib.util.spec_from_file_location("builder", BASE / "prepare_promotion.py")
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    for name, digest in (builder.EXPECTED | builder.SUPPORTING).items():
        assert sha((ROOT / name).read_bytes()) == digest, name
    build = (BASE / "prepare_promotion.py").read_text().replace("R1_CHECK_IDENTITIES.py", "P1_CHECK_IDENTITIES.py").replace("R1_REFERENCE_CERTIFICATE.py", "P1_REFERENCE_CERTIFICATE.py")
    assignment = (BASE / "P1_INTEGRATION_ASSIGNMENT.md").read_text()
    assignment = assignment.replace("P1_MANIFEST.json", "P1I2_MANIFEST.json").replace("P1_BUILD.py", "P1I2_BUILD.py").replace("P1_VALIDATE.py", "P1I2_VALIDATE.py")
    assignment = assignment.replace(
        "The build program may read the live base files only to verify their exact\ndeclared hashes and assemble a generated standalone edition; it does not\nmodify them. Read those already supplied bodies from the frozen packet.",
        "The build program may read only the exact live files listed in the manifest's\nbase_sha256 and structural_support_sha256 mappings, plus the frozen input\nfiles. It verifies every declared live hash before constructing the edition\nand rechecks them afterward. Structural support consists solely of unchanged\nlocal-link targets: those bodies are copied verbatim by the builder for\nstructural validation and are not mathematical dependencies of C.4.6.\nDo not open or scientifically review those additional bodies; record them\nas the unread structural complement. Read the complete supplied scientific\nbodies from the frozen packet. The builder modifies no established file."
    )
    outputs = {
        "P1I2_BUILD.py": build.encode(),
        "P1I2_VALIDATE.py": (BASE / "validate_edition.py").read_bytes(),
        "P1I2_ASSIGNMENT.md": assignment.encode(),
    }
    science_names = ["P1_SECTION.md", "P1_ANCILLARY.md", "P1_DEPENDENCIES.md",
                     "P1_INTEGRATION_BASE.md", "P1_CHECK_IDENTITIES.py",
                     "P1_REFERENCE_CERTIFICATE.py"]
    inputs = {name: previous["inputs"][name] for name in science_names}
    inputs.update({name: {"sha256": sha(data), "lines": len(data.splitlines())}
                   for name, data in outputs.items()})
    manifest = {
        "packet": "P1I2",
        "authors": previous["authors"], "assembler": previous["assembler"],
        "selector_instance": previous["selector_instance"],
        "inputs": inputs,
        "base_sha256": builder.EXPECTED,
        "structural_support_sha256": builder.SUPPORTING,
        "ancillary_edits": builder.EDITS,
        "scientific_input_contract": "The section, ancillary text, dependency proofs and deterministic mathematical checks have the exact displayed bytes; no scientific change is made by the assembly tooling.",
        "edition_sha256": {
            "docs/global_nonlinear.md": "3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf",
            "docs/README.md": "88757537ae600ebf79cf265288d6ca3034254caba236b4dcb055a21dd568c721",
        },
        "scope": "Complete canonical integration review with exact declared assembly reads and an explicit unread structural complement",
    }
    outputs["P1I2_MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    assert all(not (BASE / name).exists() for name in outputs)
    for name, data in outputs.items():
        (BASE / name).write_bytes(data)
    print(json.dumps({name: sha(data) for name, data in outputs.items()}, indent=2))


if __name__ == "__main__":
    main()
