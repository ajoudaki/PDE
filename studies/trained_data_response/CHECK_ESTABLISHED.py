"""Check exact approved incorporation and validate a fresh standalone edition.

Reads the eleven explicitly declared book/support files. Writes only to a fresh
directory in this study's generated namespace. Does not edit established files.
The frozen pre-promotion builder remains unchanged and expects the old edition;
this correspondence check works after the approved edition has been installed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
MANIFEST_SHA = "174bd123c8fd48cdc536925681f7eade0b5f37f3b3b1cebf53d7b383a0a5298f"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT,
                        help="live checkout, or the approved standalone draft")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    allowed = ROOT / "data/generated/trained_data_response"
    assert output.is_relative_to(allowed) and output != allowed
    assert not output.exists(), "use a fresh output directory"
    packet_bytes = (STUDY / "P1I2_MANIFEST.json").read_bytes()
    assert sha(packet_bytes) == MANIFEST_SHA
    packet = json.loads(packet_bytes)
    for path, record in packet["inputs"].items():
        data = (STUDY / path).read_bytes()
        assert sha(data) == record["sha256"], path
        assert len(data.splitlines()) == record["lines"], path
    expected = {**packet["base_sha256"],
                **packet["structural_support_sha256"],
                **packet["edition_sha256"]}
    live = {path: (source / path).read_bytes() for path in expected}
    for path, data in live.items():
        assert sha(data) == expected[path], f"Changed approved edition: {path}"
    output.mkdir(parents=True)
    edition = output / "edition"
    files = dict(live)
    for original, name in [("P1_CHECK_IDENTITIES.py", "identities.py"),
                           ("P1_REFERENCE_CERTIFICATE.py", "reference_certificate.py")]:
        files["checks/" + name] = (STUDY / original).read_bytes()
    for path, data in files.items():
        target = edition / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    edition_hashes = {path: sha(live[path]) for path in packet["base_sha256"]}
    manifest = {
        "section_sha256": packet["inputs"]["P1_SECTION.md"]["sha256"],
        "base_sha256": packet["base_sha256"],
        "structural_support_sha256": packet["structural_support_sha256"],
        "edits": packet["ancillary_edits"],
        "edition_sha256": edition_hashes,
        "supporting_files": {path: sha(data) for path, data in files.items()},
        "scope": "Exact approved edition copied from declared source files only",
    }
    (edition / "edition_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    command = [sys.executable, str(STUDY / "P1I2_VALIDATE.py"),
               "--edition", str(edition), "--output", str(output / "validation")]
    result = subprocess.run(command, capture_output=True, text=True)
    (output / "validate.stdout").write_text(result.stdout)
    (output / "validate.stderr").write_text(result.stderr)
    assert result.returncode == 0, f"Validator failed: {output / 'validate.stderr'}"
    for path, data in live.items():
        assert (source / path).read_bytes() == data, f"Concurrent change: {path}"
    for path, record in packet["inputs"].items():
        assert sha((STUDY / path).read_bytes()) == record["sha256"], path
    report = {
        "checks": "PASS", "source": str(source), "output": str(output),
        "manifest_sha256": MANIFEST_SHA,
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "source_sha256": {path: sha(data) for path, data in live.items()},
        "candidate_to_final": "Exact reviewed destination hashes; unchanged dependencies",
        "validation_command": command, "exit_code": result.returncode,
        "scope": "Correspondence and affected integration checks; no new scientific review",
    }
    (output / "correspondence.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
