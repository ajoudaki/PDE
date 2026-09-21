#!/usr/bin/env python3
"""Assemble the interactive radial fragment from checked, compressed predictions."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

STUDY = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mirror", type=Path)
    args = parser.parse_args()
    template = (STUDY / "radial_view.html").read_text()
    marker = "<!--RADIAL_PAYLOAD-->"
    assert template.count(marker) == 1
    payload = (args.data / "payload.gz.b64").read_text().strip()
    fragment = template.replace(marker, payload)
    assert len(fragment.encode()) < 1_000_000, "Inline visualization exceeds 1 MB"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(fragment)
    if args.mirror:
        args.mirror.parent.mkdir(parents=True, exist_ok=True)
        args.mirror.write_text(fragment)
    record = dict(
        fragment_bytes=len(fragment.encode()),
        template_sha256=hashlib.sha256(template.encode()).hexdigest(),
        payload_sha256=hashlib.sha256(payload.encode()).hexdigest(),
        fragment_sha256=hashlib.sha256(fragment.encode()).hexdigest(),
        output=str(args.output.resolve()),
        mirror=str(args.mirror.resolve()) if args.mirror else None,
    )
    (args.data / "viewer_build.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record))


if __name__ == "__main__":
    main()
