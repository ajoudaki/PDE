"""Validate an assembled edition without reading the live study or its history."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote


def sha(data):
    return hashlib.sha256(data).hexdigest()


def anchor(title):
    title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", title)
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--edition", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    edition = args.edition.resolve()
    output = args.output.resolve()
    assert not output.exists(), "fresh validation output required"
    output.mkdir(parents=True)
    manifest = json.loads((edition / "edition_manifest.json").read_text())
    for p, expected in manifest["supporting_files"].items():
        assert sha((edition / p).read_bytes()) == expected, p
    book = (edition / "docs/global_nonlinear.md").read_text()
    heading = "#### C.4.6. Trained data response at the fitted tanh reference"
    assert book.count(heading) == 1
    before, after = book.split(heading, 1)
    section = heading + after
    # Reverse the narrowly specified navigation change to check preservation.
    for edit in manifest["edits"]:
        if edit["path"] == "docs/global_nonlinear.md":
            assert before.count(edit["new"]) == 1
            before = before.replace(edit["new"], edit["old"])
    assert sha(before[:-1].encode()) == manifest["base_sha256"]["docs/global_nonlinear.md"]
    assert sha(section.encode()) == manifest["section_sha256"]
    guide = (edition / "docs/README.md").read_text()
    oldguide = guide
    for edit in reversed(manifest["edits"]):
        if edit["path"] == "docs/README.md":
            assert oldguide.count(edit["new"]) == 1
            oldguide = oldguide.replace(edit["new"], edit["old"])
    assert sha(oldguide.encode()) == manifest["base_sha256"]["docs/README.md"]
    # No mathematical assertion is accepted by these syntax checks alone.
    assert section.count(r"\[") == section.count(r"\]")
    assert section.count(r"\(") == section.count(r"\)")
    assert not re.search(r"studies/|data/generated/|R1_REVIEW|R1_PROOF|THEOREM\.md|PROPAGATOR\.md|WEIGHTED_SOURCE\.md|FINITE_CAPTURE\.md", section)
    assert sum(line.startswith("```") for line in section.splitlines()) % 2 == 0
    targets = []
    for source, text in [(edition / "docs/README.md", guide),
                         (edition / "docs/global_nonlinear.md", section)]:
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-z]+://", link):
                continue
            path, _, fragment = link.partition("#")
            dest = (source.parent / unquote(path)).resolve() if path else source
            assert dest.is_file(), str(dest)
            if fragment and dest.suffix == ".md":
                headings = [anchor(m.group(1)) for line in dest.read_text().splitlines()
                            if (m := re.match(r"#{1,6} (.*)", line))]
                assert unquote(fragment) in headings, (str(dest), fragment)
            targets.append(link)
    commands = [
        [sys.executable, "checks/identities.py", "--output", str(output / "identities")],
        [sys.executable, "checks/reference_certificate.py"],
    ]
    runs = []
    for index, command in enumerate(commands):
        result = subprocess.run(command, cwd=edition, capture_output=True, text=True)
        (output / f"check_{index}.stdout").write_text(result.stdout)
        (output / f"check_{index}.stderr").write_text(result.stderr)
        runs.append({"command": command, "cwd": str(edition), "exit_code": result.returncode})
        assert result.returncode == 0, runs[-1]
    report = {"checks": "PASS", "edition": str(edition),
              "edition_sha256": manifest["edition_sha256"],
              "section_sha256": manifest["section_sha256"],
              "exact_preservation": "base restored byte-for-byte outside selected edits",
              "local_links_checked": targets, "runs": runs,
              "python": sys.version,
              "scope": "Standalone structural, correspondence, algebra and constant checks; no training or whole-book reproof"}
    (output / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
