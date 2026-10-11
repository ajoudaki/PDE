"""Stage the compression proposal without editing the maintained book.

This copies only the established documentation and its linked code resources,
not the checkout or Git metadata. All scientific additions live in the two
study-owned QMD fragments; this script performs exact, checked integration.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import shutil


STUDY = Path(__file__).resolve().parent
REPO = STUDY.parent.parent
CHAPTER = "08b-trajectory-compression.qmd"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected one unchanged integration anchor: {old[:90]!r}")
    return text.replace(old, new, 1)


def integrate(text: str, width: str, setup: str) -> str:
    text = replace_once(
        text,
        "systems and do not assert a population limit, a raw-GD approximation, a\n"
        "finite-precision guarantee, or efficient preprocessing. The selected\n"
        "constructions also attain absolute error $Y/n$. Their theoretical compilers\n"
        "use initialization derivatives; empirical rollout-based implementations have\n"
        "a different setup contract.",
        "systems and do not assert a population limit, a raw-GD approximation,\n"
        "or a finite-precision guarantee. The selected constructions also attain\n"
        "absolute error $Y/n$. The quantitative refinement below gives polynomial\n"
        "sufficient widths for Legendre and Taylor. A separate computational theorem\n"
        "gives efficient exact-real initialization: near-quadratic work for a supplied\n"
        "dense realization and near-linear work for a fresh Gaussian reference sampled\n"
        "implicitly, for both Harmonic and Taylor. The original initialized-jet\n"
        "compiler remains an alternative without a work bound.",
    )
    text = replace_once(
        text,
        "All other constants are defined in the statement or proof using them.",
        "All other constants are defined in the statement or proof using them.\n"
        "The initialization cost theorem states its own fixed-parameter big-O\n"
        "convention; its computational constants are not the storage constant $C$.",
    )
    text = replace_once(
        text,
        "may depend on every fixed problem parameter, including the positive $Y$,\n"
        "and is not proved polynomial or practically small. No simultaneous event\n"
        "over infinitely many independently initialized widths, uniform growing-data\n"
        "limit, or uniform limit as $Y\\downarrow0$ is asserted. For a ratio below,",
        "may depend on every fixed problem parameter, including the positive $Y$.\n"
        "Unless the quantitative refinement @thm-compression-polynomial-width is\n"
        "invoked, its size is not proved polynomial; in particular Harmonic retains\n"
        "the eventual qualification. Polynomial sufficient widths need not be\n"
        "practically small. Each probability bound concerns the stated deterministic\n"
        "data and labels at one individual width, not one event simultaneous over\n"
        "all datasets, labels, or infinitely many independent initializations.\n"
        "No unrestricted growing-data limit is asserted. For a ratio below,",
    )
    text = replace_once(
        text,
        "storage orders. The theoretical initializers use the dense initialization,\n"
        "training data, and finitely many initialization derivatives; no later trained\n"
        "weight or dense training trajectory is an input. Subsequent evolution is an\n"
        "autonomous nonlinear system with the retained state.",
        "storage orders. One theoretical initialization uses only the dense\n"
        "initialization, training data, and finitely many initialization derivatives;\n"
        "it takes no later trained state or trajectory sample as an input. The\n"
        "alternative efficient initializers in @prp-compression-efficient-setup\n"
        "compute disposable numerical continuations from the same initial data.\n"
        "For every alternative, subsequent compressed evolution is an autonomous\n"
        "nonlinear system with the stated retained state.",
    )
    text = replace_once(
        text,
        "These are sufficient sizes, not optimality claims.",
        "For Legendre and Taylor, @thm-compression-polynomial-width strengthens\n"
        "the sufficient-width qualification while preserving these storage formulas\n"
        "and the complete-trajectory comparison. It does not quantify the separate\n"
        "nonlinear-feature-learning certificates or Harmonic's width threshold.\n\n"
        "These are sufficient sizes, not optimality claims.",
    )
    text = replace_once(
        text,
        "Coordinate counts do not bound precision or\npreprocessing time.",
        "Coordinate counts alone do not bound precision or preprocessing time;\n"
        "@prp-compression-efficient-setup supplies separate arithmetic and peak-memory\n"
        "bounds, but no finite-precision theorem.",
    )
    text = replace_once(
        text,
        "these statements concern exact arithmetic and do not assert efficient\n"
        "preprocessing or empirical performance.",
        "the original storage argument is supplemented by quantitative width and\n"
        "efficient-setup results below. All computational statements concern their\n"
        "specified exact-real primitives, not empirical performance.",
    )
    text = replace_once(
        text,
        "its initial arrays; the separate compiler below will establish their\n"
        "initialization-only provenance for the two methods.",
        "its initial arrays. The next compiler establishes initialization-jet\n"
        "provenance; @prp-compression-efficient-setup supplies separate efficient\n"
        "rollout implementations of the same source-to-runtime interface.",
    )
    text = replace_once(
        text,
        "The preceding constructions provide the stated retained counts and\n"
        "initialization-only provenance. Here we verify the probabilistic comparison,",
        "The preceding constructions provide the stated retained counts and the\n"
        "initialized-jet provenance alternative; the efficient alternatives have\n"
        "their own execution proofs. Here we verify the original asymptotic\n"
        "comparison. @thm-compression-polynomial-width gives its separate quantitative\n"
        "strengthening for Legendre and Taylor. The reference is actual dense\n"
        "variability. In the following original probabilistic comparison,",
    )
    text = replace_once(
        text,
        "In the following original probabilistic comparison,\n"
        "whose reference is actual dense variability rather than an upper bound.",
        "The following proof does not compare against a dense upper certificate.",
    )
    text = replace_once(
        text,
        "## One selected nonlinear dynamics for both source constructions "
        "{#sec-compression-selected-section}",
        width.rstrip() + "\n\n## One selected nonlinear dynamics for both source "
        "constructions {#sec-compression-selected-section}",
    )
    return replace_once(
        text,
        "## Nonlinear feature learning preserved by compression "
        "{#sec-compression-nonlinear-learning}",
        setup.rstrip() + "\n\n## Nonlinear feature learning preserved by compression "
        "{#sec-compression-nonlinear-learning}",
    )


def check_links(docs: Path) -> dict:
    locations: dict[str, list[str]] = {}
    references: set[str] = set()
    section_references: set[str] = set()
    section_headings: set[str] = set()
    for path in sorted(docs.glob("*.qmd")):
        body = path.read_text()
        for label in re.findall(r"\{#([\w.-]+)", body):
            locations.setdefault(label, []).append(path.name)
        references.update(label.rstrip(".") for label in re.findall(
            r"(?<!\w)@((?:sec|eq|thm|lem|prp|cor|def|rem|fig|tbl)-[\w.-]+)", body))
        references.update(re.findall(r"\]\(#([\w.-]+)\)", body))
        section_references.update(label.rstrip(".") for label in re.findall(
            r"(?<!\w)@(sec-[\w.-]+)", body))
        section_headings.update(re.findall(r"^#+[^\n]*\{#(sec-[\w.-]+)\}", body, re.M))
        if re.search(r"(?<!\w)@proof-", body):
            raise ValueError(f"Proof anchors require Markdown links, not citation syntax: {path}")
    duplicates = {key: files for key, files in locations.items() if len(files) > 1}
    missing = sorted(references - locations.keys())
    return {"duplicate_identifiers": duplicates, "missing_crossreferences": missing,
            "nonheading_section_crossreferences": sorted(section_references - section_headings)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="Fresh study-owned generated directory")
    args = parser.parse_args()
    destination = args.destination.resolve()
    generated = (REPO / "data/generated/headline_threefold_upgrade_20261011").resolve()
    if not destination.is_relative_to(generated) or destination == generated:
        raise ValueError("Destination must be a fresh child of this study's generated namespace")
    if destination.exists():
        raise FileExistsError(destination)
    fragments = [STUDY / "PROMOTION_WIDTH.qmd", STUDY / "PROMOTION_SETUP.qmd"]
    original = (REPO / "docs" / CHAPTER).read_text()
    candidate = integrate(original, *(path.read_text() for path in fragments))
    if any(re.search(r"(?<!\w)@sec-", path.read_text()) for path in fragments):
        raise ValueError("New section links need descriptive anchor text in this unnumbered book")
    if re.search(r"studies/|paper/compact|\.md\)", "\n".join(path.read_text() for path in fragments)):
        raise ValueError("Candidate fragments must not depend on study/paper Markdown files")
    destination.mkdir(parents=True)
    for name in ("docs", "code"):
        shutil.copytree(REPO / name, destination / name,
                        ignore=shutil.ignore_patterns(".*", "__pycache__", "*.pyc"))
    (destination / "docs" / CHAPTER).write_text(candidate)
    (destination / "chapter.diff").write_text("".join(difflib.unified_diff(
        original.splitlines(keepends=True), candidate.splitlines(keepends=True),
        fromfile=f"established/docs/{CHAPTER}", tofile=f"proposed/docs/{CHAPTER}")))
    manifest = {str(path.relative_to(REPO)): digest(path)
                for root in (REPO / "docs", REPO / "code")
                for path in sorted(root.rglob("*"))
                if path.is_file() and not any(part.startswith(".") or part == "__pycache__"
                                              for part in path.relative_to(root).parts)
                and path.suffix != ".pyc"}
    manifest.update({str(path.relative_to(REPO)): digest(path)
                     for path in [Path(__file__), *fragments]})
    manifest["proposed/docs/" + CHAPTER] = digest(destination / "docs" / CHAPTER)
    (destination / "inputs.sha256.json").write_text(json.dumps(manifest, indent=2) + "\n")
    findings = check_links(destination / "docs")
    (destination / "structural_check.json").write_text(json.dumps(findings, indent=2) + "\n")
    print(json.dumps({"destination": str(destination), **findings}, indent=2))
    if any(findings.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
