"""Assemble a standalone proposed book; never modify the maintained edition."""
from pathlib import Path
import hashlib
import json
import shutil
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assemble(root, destination):
    root, destination = Path(root).resolve(), Path(destination).resolve()
    study = root / "studies/nonlinear_feature_learning_certificate_20261010"
    allowed = root / "data/generated/nonlinear_feature_learning_certificate_20261010"
    if not destination.is_relative_to(allowed) or destination.exists():
        raise ValueError("Use a new directory under this study's generated root")
    destination.mkdir(parents=True)
    for name in ("docs", "code"):
        shutil.copytree(root / name, destination / name,
                        ignore=shutil.ignore_patterns(".quarto", "__pycache__", "*.pyc"))
    chapter = destination / "docs/08b-trajectory-compression.qmd"
    original = chapter.read_text()
    marker = "## Assembly of the headline theorem {#sec-compression-assembly}"
    if original.count(marker) != 1:
        raise ValueError("Expected unique assembly heading")
    candidate = study / "PROMOTION_SECTION.qmd"
    chapter.write_text(original.replace(marker, candidate.read_text().rstrip() + "\n\n" + marker))
    packet = destination / "review_inputs"
    packet.mkdir()
    inputs = [
        "docs/index.qmd", "docs/notation.qmd", "docs/08b-trajectory-compression.qmd",
        "paper/compact.tex", "paper/compact_fitting.tex",
        "paper/feature_learning_theorem.tex", "paper/compact_feature_learning.tex",
        "studies/nonlinear_feature_learning_certificate_20261010/PROMOTION_SECTION.qmd",
        "studies/nonlinear_feature_learning_certificate_20261010/assemble_promotion.py",
    ]
    manifest = {}
    for relative in inputs:
        source = root / relative
        target = packet / source.name
        shutil.copyfile(source, target)
        manifest[target.name] = {"source": relative, "sha256": digest(target)}
    manifest["assembled_chapter"] = {
        "source": "docs/08b-trajectory-compression.qmd", "sha256": digest(chapter)}
    (packet / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    # Capture all maintained edition inputs, before any render creates outputs.
    edition = {str(p.relative_to(destination)): digest(p)
               for directory in (destination / "docs", destination / "code")
               for p in sorted(directory.rglob("*")) if p.is_file()}
    (destination / "edition_inputs.json").write_text(json.dumps(edition, indent=2) + "\n")
    print(destination)


if __name__ == "__main__":
    assemble(*sys.argv[1:])
