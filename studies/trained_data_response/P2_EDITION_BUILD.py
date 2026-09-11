#!/usr/bin/env python3
"""Assemble and verify a frozen, docs-only proposed C.4.7 edition.

This script never edits established files.  The required --output is a fresh
directory below data/generated/trained_data_response.  The proposed book is
written under OUTPUT/standalone/docs; OUTPUT/validation.json records the exact
inputs, replacement effects, rollback, preservation and link checks.

Optional promotion-manifest contract::

    {"inputs": {"P2_SECTION.md": "<sha256>", ...},
     "established_sha256": {"docs/global_nonlinear.md": "<sha256>", ...},
     "authors": ["..."]}

All ``inputs`` are flat files in this study; a manifest cannot name itself.
Validation scripts are deliberately left to the separate supervisor runner.
Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/trained_data_response"
ANCILLARY = STUDY / "P2_EDITION_ANCILLARY.json"
BASE_DOCS = {
    "docs/README.md",
    "docs/NOTATION.md",
    "docs/global_nonlinear.md",
    "docs/finite_dynamics.md",
    "docs/special_data_limits.md",
}
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
TAG = re.compile(r"\\tag\s*\{([^{}]+)\}")
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")
DEFINITION = re.compile(r"^ {0,3}\[[^]\n]+\]:\s*(<[^>]+>|\S+)", re.MULTILINE)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value


def checked_file(path: Path, expected: str) -> bytes:
    require(isinstance(expected, str) and SHA256.fullmatch(expected) is not None,
            f"Invalid expected SHA-256 for {path}")
    require(path.is_file() and not path.is_symlink(), f"Missing or symlinked input: {path}")
    value = path.read_bytes()
    require(digest(value) == expected, f"Frozen source hash mismatch: {path}")
    return value


def relative_input(name: str, parent: Path, *, flat: bool) -> Path:
    require(isinstance(name, str) and bool(name), "Input names must be nonempty strings")
    rel = Path(name)
    require(not rel.is_absolute() and ".." not in rel.parts,
            f"Input path must remain inside its source directory: {name}")
    if flat:
        require(len(rel.parts) == 1 and rel.name == name, f"Study input must be flat: {name}")
    path = parent / rel
    require(path.resolve().is_relative_to(parent.resolve()), f"Escaping input path: {name}")
    return path


def without_fences(source: str) -> str:
    """Mask fenced code while preserving line positions for metadata checks."""
    lines = []
    fence = None
    for line in source.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\n"))
        if fence is None and marker:
            fence = marker.group(1)
            lines.append("\n" if line.endswith("\n") else "")
        elif fence is not None:
            if (marker and marker.group(1)[0] == fence[0]
                    and len(marker.group(1)) >= len(fence)
                    and not marker.group(2).strip()):
                fence = None
            lines.append("\n" if line.endswith("\n") else "")
        else:
            lines.append(line)
    require(fence is None, "Unclosed Markdown code fence")
    return "".join(lines)


def anchors(source: str) -> set[str]:
    """GitHub-style anchors for ATX headings, including duplicate suffixes."""
    found = set()
    counts: Counter[str] = Counter()
    for line in without_fences(source).splitlines():
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"<[^>]*>", "", match.group(1)).lower()
        title = re.sub(r"[^\w\-\s]", "", title, flags=re.UNICODE)
        slug = re.sub(r"\s", "-", title)
        suffix = counts[slug]
        counts[slug] += 1
        found.add(slug if suffix == 0 else f"{slug}-{suffix}")
    found.update(re.findall(r"\b(?:id|name)=[\"']([^\"']+)[\"']", source))
    return found


def markdown_links(source: str) -> list[str]:
    masked = without_fences(source)
    return [m.group(1).strip("<>") for pattern in (LINK, DEFINITION)
            for m in pattern.finditer(masked)]


def validate_section(section: str, chapter: str, spec: dict) -> dict:
    title = spec["title"]
    require(section.startswith(title + "\n"), f"Section must start with {title!r}")
    require(section.count(title) == 1 and title not in chapter,
            "New section title must occur exactly once and not exist in the base chapter")
    require(section.endswith("\n") and "\r" not in section,
            "Section must use LF line endings and have a final newline")
    require(not re.search(r"(?i)(?:\bstudies[/\\]|\bdata[/\\]generated[/\\]|"
                          r"P2_[\w.-]+\.(?:md|py|json)\b|/home/|file://|codex://)", section),
            "Section contains a study, generated-file or machine-local dependency")
    visible = without_fences(section)
    tags = TAG.findall(visible)
    require(bool(tags), "Section must contain explicitly namespaced equation tags")
    require(len(tags) == len(set(tags)), "Duplicate equation tag in new section")
    require(all(tag.startswith("C.4.7.") for tag in tags),
            "Every new equation tag must use the C.4.7 namespace")
    require(not (set(tags) & set(TAG.findall(chapter))),
            "A new equation tag already occurs in the base chapter")
    display = None
    display_count = 0
    for match in re.finditer(r"\\\[|\\\]|\$\$", visible):
        token = match.group()
        if token == r"\[":
            require(display is None, "Nested or mismatched display delimiter")
            display = token
        elif token == r"\]":
            require(display == r"\[", "Unmatched closing display delimiter")
            display = None
            display_count += 1
        elif display == "$$":
            display = None
            display_count += 1
        else:
            require(display is None, "Mixed display delimiters")
            display = "$$"
    require(display is None, "Unclosed display delimiter")
    require(spec["fragment"] in anchors(section), "New section fragment does not resolve")
    return {"heading": title, "fragment": spec["fragment"],
            "equation_tags": tags, "balanced_display_count": display_count,
            "no_study_dependencies": True}


def link_check(source_name: str, target: str, docs: dict[str, str],
               exclusions: set[tuple[str, str]]) -> dict:
    result = {"source": source_name, "target": target}
    url = urlsplit(target)
    if url.scheme in {"http", "https", "mailto"} or url.netloc:
        return dict(result, status="external-url-not-fetched")
    require(not url.scheme, f"Unsupported local-link scheme: {source_name}: {target}")
    if (source_name, target) in exclusions:
        return dict(result, status="preserved-preexisting-outside-docs-exclusion")
    path = unquote(url.path)
    require(not path.startswith("/"), f"Absolute local link: {source_name}: {target}")
    resolved = (ROOT / source_name).parent / path if path else ROOT / source_name
    resolved = resolved.resolve()
    require(resolved.is_relative_to(ROOT / "docs"),
            f"Link escapes standalone docs: {source_name}: {target}")
    relative = resolved.relative_to(ROOT).as_posix()
    require(relative in docs, f"Missing standalone link target: {source_name}: {target}")
    if url.fragment:
        require(unquote(url.fragment) in anchors(docs[relative]),
                f"Missing heading fragment: {source_name}: {target}")
    return dict(result, status="resolved", destination=relative,
                fragment=unquote(url.fragment) or None)


def validate_manifest(path: Path | None, source_hashes: dict[str, str]) -> dict | None:
    if path is None:
        return None
    require(path.resolve().parent == STUDY, "Manifest must be a flat file in this study")
    require(path.is_file() and not path.is_symlink(), "Manifest is missing or symlinked")
    manifest = read_json(path)
    inputs = manifest.get("inputs")
    established = manifest.get("established_sha256")
    require(isinstance(inputs, dict) and isinstance(established, dict),
            "Manifest requires inputs and established_sha256 objects")
    require(path.name not in inputs, "Manifest cannot include its own hash")
    required = {"P2_SECTION.md", ANCILLARY.name, Path(__file__).name}
    require(required <= set(inputs), f"Manifest missing assembly inputs: {sorted(required - set(inputs))}")
    require(BASE_DOCS <= set(established), "Manifest must freeze all five scientific base docs")
    for name, expected in inputs.items():
        checked_file(relative_input(name, STUDY, flat=True), expected)
    for name, expected in established.items():
        require(name.startswith("docs/"), "This docs-only builder accepts only docs/ established inputs")
        checked_file(relative_input(name, ROOT, flat=False), expected)
        if name in source_hashes:
            require(expected == source_hashes[name], f"Manifest/ancillary source disagreement: {name}")
    return {"source": path.relative_to(ROOT).as_posix(), "sha256": digest(path.read_bytes()),
            "inputs": inputs, "established_sha256": established,
            "authors": manifest.get("authors", []), "all_named_hashes_verified": True}


def build(output: Path, manifest_path: Path | None) -> dict:
    require(output.resolve().is_relative_to(GENERATED.resolve())
            and output.resolve() != GENERATED.resolve(),
            f"--output must be a fresh descendant of {GENERATED}")
    require(not output.exists() and not output.is_symlink(), "--output must not already exist")
    ancillary_bytes = ANCILLARY.read_bytes()
    builder_bytes = Path(__file__).read_bytes()
    config = json.loads(ancillary_bytes.decode("utf-8"))
    require(config.get("schema_version") == 1, "Unsupported ancillary schema")
    frozen = config["copied_docs_sha256"]
    require(set(config["scientific_base_sha256"]) == BASE_DOCS,
            "Ancillary must freeze exactly the five scientific base documents")
    for name, expected in config["scientific_base_sha256"].items():
        require(frozen.get(name) == expected, f"Inconsistent base hash: {name}")
    for name, expected in config["instruction_sha256"].items():
        require(name in {"AGENTS.md", "RESEARCH_WORKFLOW.md"}, "Unexpected shared instruction input")
        checked_file(ROOT / name, expected)
    actual_names = {p.relative_to(ROOT).as_posix() for p in (ROOT / "docs").rglob("*.md")}
    require(actual_names == set(frozen), "Frozen docs inventory differs from the current Markdown inventory")
    original = {}
    for name, expected in frozen.items():
        require(name.startswith("docs/") and name.endswith(".md"), "Only docs Markdown files may be copied")
        original[name] = checked_file(relative_input(name, ROOT, flat=False), expected)
    manifest = validate_manifest(manifest_path, frozen)
    spec = config["section"]
    require(spec["source"] == "P2_SECTION.md" and spec["destination"] == "docs/global_nonlinear.md",
            "Unexpected section source or destination")
    section_path = STUDY / spec["source"]
    require(section_path.is_file() and not section_path.is_symlink(), "P2_SECTION.md is missing or symlinked")
    section_bytes = section_path.read_bytes()
    if manifest is not None:
        require(digest(section_bytes) == manifest["inputs"][spec["source"]],
                "Section changed after manifest validation")
    section = section_bytes.decode("utf-8")
    chapter_name = spec["destination"]
    texts = {name: data.decode("utf-8") for name, data in original.items()}
    section_validation = validate_section(section, texts[chapter_name], spec)
    effects = []
    replacements = config["replacements"]
    require(len({change["id"] for change in replacements}) == len(replacements),
            "Replacement identifiers must be unique")
    for change in replacements:
        name, old, new = change["path"], change["old"], change["new"]
        require(name in {chapter_name, "docs/README.md"}, "Unexpected navigation destination")
        require(old and new and old != new and texts[name].count(old) == 1,
                f"Old navigation text is not unique: {change['id']}")
        require(new not in texts[name], f"New navigation text already exists: {change['id']}")
        line = texts[name][:texts[name].index(old)].count("\n") + 1
        texts[name] = texts[name].replace(old, new, 1)
        effects.append({"id": change["id"], "path": name, "line_before_change": line,
                        "old_sha256": digest(old.encode()), "new_sha256": digest(new.encode()),
                        "exact_old_match_count": 1})
    require(spec["append_separator"] == "\n", "Append separator must be one newline")
    require(texts[chapter_name].endswith("\n"), "Base chapter needs a final newline")
    append = spec["append_separator"] + section
    texts[chapter_name] += append
    require(texts[chapter_name].count(spec["title"]) == 1, "Assembled section title is not unique")
    restored = dict(texts)
    require(restored[chapter_name].endswith(append), "Appended section suffix mismatch")
    restored[chapter_name] = restored[chapter_name][:-len(append)]
    for change in reversed(replacements):
        name, old, new = change["path"], change["old"], change["new"]
        require(restored[name].count(new) == 1, f"Reverse replacement is ambiguous: {change['id']}")
        restored[name] = restored[name].replace(new, old, 1)
    require(all(restored[name].encode("utf-8") == data for name, data in original.items()),
            "Exact rollback failed to recover all base documents")
    exclusions = {(item["source"], item["target"])
                  for item in config["allowed_preexisting_external_doc_links"]}
    baseline_links = {(name, target) for name, text in
                      ((name, data.decode("utf-8")) for name, data in original.items())
                      for target in markdown_links(text)}
    require(exclusions <= baseline_links, "A claimed preexisting link exclusion does not exist")
    affected = [(change["path"], target) for change in replacements
                for target in markdown_links(change["new"])]
    affected.extend((chapter_name, target) for target in markdown_links(section))
    affected_checks = [link_check(name, target, texts, set()) for name, target in affected]
    guide_checks = [link_check("docs/README.md", target, texts, exclusions)
                    for target in markdown_links(texts["docs/README.md"])]
    unchanged = sorted(set(original) - {chapter_name, "docs/README.md"})
    require(all(texts[name].encode("utf-8") == original[name] for name in unchanged),
            "A copied document outside the two declared edits changed")
    output.mkdir(parents=True, exist_ok=False)
    standalone = output / "standalone"
    for name, text in texts.items():
        destination = standalone / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(text.encode("utf-8"))
    written_hashes = {name: digest((standalone / name).read_bytes()) for name in sorted(texts)}
    require(all(written_hashes[name] == digest(texts[name].encode("utf-8")) for name in texts),
            "Written edition differs from the validated assembly")
    for name, expected in frozen.items():
        checked_file(ROOT / name, expected)
    require(section_path.read_bytes() == section_bytes, "Section changed during assembly")
    require(ANCILLARY.read_bytes() == ancillary_bytes, "Ancillary changed during assembly")
    require(Path(__file__).read_bytes() == builder_bytes, "Builder changed during assembly")
    for name, expected in config["instruction_sha256"].items():
        checked_file(ROOT / name, expected)
    if manifest_path is not None:
        require(validate_manifest(manifest_path, frozen) == manifest,
                "Manifest or a named input changed during assembly")
    report = {
        "schema_version": 1, "status": "PASS", "scope": "docs-only C.4.7 edition assembly",
        "edition": "standalone/docs", "command": [sys.executable, *sys.argv],
        "python_version": sys.version, "source_root": str(ROOT),
        "inputs": {"P2_SECTION.md": digest(section_bytes),
                   ANCILLARY.name: digest(ancillary_bytes),
                   Path(__file__).name: digest(builder_bytes)},
        "instruction_sha256": config["instruction_sha256"],
        "scientific_base_sha256": config["scientific_base_sha256"],
        "copied_docs_sha256": frozen, "edition_docs_sha256": written_hashes,
        "manifest": manifest, "navigation_replacements": effects,
        "section_checks": section_validation,
        "preservation": {"unchanged_documents": unchanged, "all_exactly_preserved": True,
                         "rollback_all_base_hashes_recovered": True,
                         "rollback_recipe": "Remove the exact newline-plus-P2_SECTION.md suffix; reverse the JSON replacements in reverse order.",
                         "original_sources_unchanged_at_completion": True},
        "affected_links_and_fragments": affected_checks,
        "readme_links_and_fragments": guide_checks,
        "scoped_exclusions": config["allowed_preexisting_external_doc_links"],
        "limitations": ["No mathematical proof audit is performed by this assembly script.",
                        "Only affected-section links and all README links/fragments are checked; older chapter links and proofs are not re-audited.",
                        "External web URLs are preserved without fetching.",
                        "No maintained code, study files, Git metadata, training, empirical reproduction or deterministic math checks are included or executed.",
                        "The supervisor runs separately frozen deterministic checks in standalone/validation."]}
    (output / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                             encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="Fresh directory inside data/generated/trained_data_response")
    parser.add_argument("--manifest", type=Path,
                        help="Optional frozen P2_PROMOTION_MANIFEST.json in this study")
    args = parser.parse_args()
    try:
        report = build(args.output.absolute(), args.manifest.absolute() if args.manifest else None)
    except (ValueError, OSError, UnicodeError, KeyError, TypeError) as error:
        print(f"P2 edition assembly failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"status": report["status"], "edition": str(args.output / "standalone/docs"),
                      "report": str(args.output / "validation.json"),
                      "copied_docs": len(report["copied_docs_sha256"]),
                      "navigation_replacements": len(report["navigation_replacements"])},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
