#!/usr/bin/env python3
"""Deterministically reorganize the migrated Quarto book into conceptual parts.

The input is the complete, linearly migrated book.  The manifest partitions each
scientific source exactly once.  This program moves those frozen chunks, adjusts
only Markdown heading depth, rewrites file-qualified internal links from stable
target IDs, and adds chapter wrappers.  It does not alter mathematical payloads.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
DEFAULT_MANIFEST = HERE / "book_reorganization.json"
DEFAULT_LOGICAL_ROOT = HERE.parents[1] / "new_doc"

ID_RE = re.compile(r"\{#([A-Za-z][A-Za-z0-9_.:-]*)")
HEADING_RE = re.compile(r"^(#{1,6})([ \t]+)(.*?)(\r?\n)?$")
FENCE_RE = re.compile(r"^[ \t]*(```+|~~~+)")
LINK_DEST_RE = re.compile(
    r"(?P<prefix>\]\()(?P<dest><?(?:#[A-Za-z][A-Za-z0-9_.:-]*|"
    r"(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.qmd"
    r"(?:#[A-Za-z][A-Za-z0-9_.:-]*)?)>?)(?=[ \t\)])"
)
ALL_LINK_RE = re.compile(r"\]\((?P<dest><?[^) \t]+>?)(?:[ \t]+[^)]*)?\)")
CROSSREF_RE = re.compile(
    r"(?<![A-Za-z0-9_.:-])@((?:eq|sec|thm|lem|lm|prop|prp|cor|def|proof|"
    r"fig|tbl|exr|sol|cnj|rem|stmt)-[A-Za-z0-9_-]+(?:[.:][A-Za-z0-9_-]+)*)"
)
BIB_KEY_RE = re.compile(r"^@[A-Za-z]+\{([^,]+),", re.MULTILINE)
CITATION_RE = re.compile(
    r"(?<![A-Za-z0-9_.:-])@([A-Za-z][A-Za-z0-9_-]*(?:[.:][A-Za-z0-9_-]+)*)"
)


class ReorganizationError(RuntimeError):
    pass


@dataclass(frozen=True)
class Chunk:
    key: str
    source: str
    start: str
    target: str
    text: str
    start_line: int
    end_line: int


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def heading_ids(lines: list[str], source: str) -> dict[str, int]:
    found: dict[str, int] = {}
    in_fence = False
    fence_char = ""
    for index, line in enumerate(lines):
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif marker == fence_char:
                in_fence = False
                fence_char = ""
            continue
        if in_fence or not HEADING_RE.match(line):
            continue
        ids = ID_RE.findall(line)
        for target_id in ids:
            if target_id in found:
                raise ReorganizationError(
                    f"duplicate heading boundary {target_id!r} in {source}"
                )
            found[target_id] = index
    return found


def partition_sources(source_dir: Path, manifest: dict) -> tuple[dict[str, Chunk], dict]:
    chunks: dict[str, Chunk] = {}
    source_state: dict[str, dict] = {}
    for source, entries in manifest["source_partitions"].items():
        path = source_dir / source
        if not path.is_file():
            raise ReorganizationError(f"missing source file: {path}")
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        lines = text.splitlines(keepends=True)
        boundaries = heading_ids(lines, source)
        starts: list[int] = []
        for position, entry in enumerate(entries):
            start = entry["start"]
            if position == 0 and start != "__start__":
                raise ReorganizationError(f"{source}: first partition must start at __start__")
            if start == "__start__":
                index = 0
            else:
                if start not in boundaries:
                    raise ReorganizationError(f"{source}: missing boundary {start}")
                index = boundaries[start]
            if starts and index <= starts[-1]:
                raise ReorganizationError(f"{source}: non-increasing partition {start}")
            starts.append(index)

        covered_lines = 0
        source_chunks = []
        for position, (entry, start_index) in enumerate(zip(entries, starts)):
            end_index = starts[position + 1] if position + 1 < len(starts) else len(lines)
            chunk_text = "".join(lines[start_index:end_index])
            key = f"{source}@{entry['start']}"
            if key in chunks:
                raise ReorganizationError(f"duplicate chunk key: {key}")
            chunk = Chunk(
                key=key,
                source=source,
                start=entry["start"],
                target=entry["target"],
                text=chunk_text,
                start_line=start_index + 1,
                end_line=end_index,
            )
            chunks[key] = chunk
            covered_lines += end_index - start_index
            source_chunks.append(
                {
                    "key": key,
                    "target": entry["target"],
                    "start_line": start_index + 1,
                    "end_line": end_index,
                    "sha256": sha256_text(chunk_text),
                }
            )
        if covered_lines != len(lines):
            raise ReorganizationError(
                f"{source}: partition covers {covered_lines}/{len(lines)} lines"
            )
        source_state[source] = {
            "bytes": len(raw),
            "lines": len(lines),
            "sha256": sha256_bytes(raw),
            "chunks": source_chunks,
        }
    return chunks, source_state


def iter_outside_fences(lines: Iterable[str]):
    in_fence = False
    fence_char = ""
    for line in lines:
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif marker == fence_char:
                in_fence = False
                fence_char = ""
            yield line, False
            continue
        yield line, not in_fence


def shift_chunk_headings(text: str) -> str:
    """Make the first heading a chapter section and preserve relative depth.

    Legacy source occasionally uses a shallower unlabelled heading inside a deep
    proof package.  Such a heading becomes a subsection of the chunk rather than
    escaping above its new section root.
    """

    lines = text.splitlines(keepends=True)
    root_level = None
    first_heading = True
    output: list[str] = []
    for line, active in iter_outside_fences(lines):
        match = HEADING_RE.match(line) if active else None
        if not match:
            output.append(line)
            continue
        level = len(match.group(1))
        if root_level is None:
            root_level = level
        if first_heading:
            new_level = 2
            first_heading = False
        elif level > root_level:
            new_level = min(6, 2 + level - root_level)
        else:
            new_level = 3
        newline = match.group(4) or ""
        output.append("#" * new_level + match.group(2) + match.group(3) + newline)
    if root_level is None:
        raise ReorganizationError("chunk contains no Markdown heading")
    return "".join(output)


def extract_ids(text: str) -> list[str]:
    return ID_RE.findall(text)


def first_heading_id(text: str, source: str) -> str:
    for line, active in iter_outside_fences(text.splitlines(keepends=True)):
        if active and HEADING_RE.match(line):
            ids = ID_RE.findall(line)
            if ids:
                return ids[0]
    raise ReorganizationError(f"{source}: no labelled root heading")


def architecture_block(chapters: list[dict], parts: list[dict]) -> str:
    by_id = {chapter["id"]: chapter for chapter in chapters}
    lines = [
        "## Book architecture {#sec-book-architecture}",
        "",
        "The established theory is organized by scientific responsibility: first the",
        "population dynamics that captures training, then autonomous approximation of",
        "that evolution, and finally the learning and prediction it produces.",
        "",
    ]
    for part in parts:
        lines.extend([f"### {part['title']}", ""])
        for chapter_id in part["chapters"]:
            chapter = by_id[chapter_id]
            lines.append(
                f"{chapter['number']}. [{chapter['title']}]"
                f"({chapter['file']}#{chapter['anchor']})"
            )
        lines.append("")
    lines.extend(
        [
            "The closing [strategic outlook](outlook.qmd#ch-strategic-outlook)",
            "records open objectives and dependencies. Stable identifiers preserve links",
            "to every moved theorem, equation, proof and source section.",
            "",
        ]
    )
    return "\n".join(lines)


def quarto_config(manifest: dict) -> str:
    chapter_by_id = {chapter["id"]: chapter for chapter in manifest["chapters"]}
    lines = [
        "project:",
        "  type: book",
        "",
        "book:",
        '  title: "PDE: population dynamics of deep learning"',
        "  chapters:",
        "    - index.qmd",
        "    - notation.qmd",
    ]
    for part in manifest["parts"]:
        lines.append(f'    - part: "{part["title"]}"')
        lines.append("      chapters:")
        for chapter_id in part["chapters"]:
            lines.append(f"        - {chapter_by_id[chapter_id]['file']}")
    lines.extend(
        [
            "    - outlook.qmd",
            "",
            "bibliography: references.bib",
            "",
            "number-sections: false",
            "crossref:",
            "  chapters: false",
            "",
            "classoption: enabledeprecatedfontcommands",
            "header-includes:",
            "  - \\usepackage{mathtools}",
            "  - \\usepackage{fvextra}",
            "  - \\RecustomVerbatimEnvironment{verbatim}{Verbatim}{breaklines=true,breakanywhere=true}",
            "  - \\AtBeginDocument{\\counterwithout{equation}{chapter}\\counterwithout{theorem}{section}\\counterwithout{lemma}{section}\\counterwithout{proposition}{section}\\counterwithout{corollary}{section}}",
            "format:",
            "  html: default",
            "  pdf:",
            "    pdf-engine: xelatex",
            "    keep-tex: true",
            "    latex-auto-install: false",
            "    latex-tinytex: false",
            "    filters:",
            "      - pdf_breakable_tables.lua",
            "  latex:",
            "    filters:",
            "      - pdf_breakable_tables.lua",
            "",
        ]
    )
    return "\n".join(lines)


def rewrite_links(
    text: str,
    current_file: str,
    id_to_file: dict[str, str],
    source_root_to_file: dict[str, str],
    output_files: set[str],
) -> tuple[str, int]:
    rewritten = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal rewritten
        original = match.group("dest")
        angled = original.startswith("<") and original.endswith(">")
        dest = original[1:-1] if angled else original
        new_dest = None
        if dest.startswith("#"):
            target_id = dest[1:]
            if target_id in id_to_file:
                new_dest = f"{id_to_file[target_id]}#{target_id}"
        else:
            base, marker, target_id = dest.partition("#")
            base_name = base.removeprefix("./")
            if base_name in source_root_to_file:
                if marker:
                    if target_id not in id_to_file:
                        raise ReorganizationError(
                            f"{current_file}: link has unknown target {target_id}: {dest}"
                        )
                    new_dest = f"{id_to_file[target_id]}#{target_id}"
                else:
                    new_dest = source_root_to_file[base_name]
            elif base_name in output_files:
                new_dest = dest
        if new_dest is None or new_dest == dest:
            return match.group(0)
        rewritten += 1
        if angled:
            new_dest = f"<{new_dest}>"
        return match.group("prefix") + new_dest

    output: list[str] = []
    for line, active in iter_outside_fences(text.splitlines(keepends=True)):
        output.append(LINK_DEST_RE.sub(replace, line) if active else line)
    return "".join(output), rewritten


def validate_output(
    output_dir: Path,
    logical_root: Path,
    old_ids: set[str],
    manifest: dict,
    expected_qmd: set[str],
) -> dict:
    qmd_files = {path.name for path in output_dir.glob("*.qmd")}
    if qmd_files != expected_qmd:
        raise ReorganizationError(
            f"output QMD set mismatch: missing={sorted(expected_qmd-qmd_files)}, "
            f"extra={sorted(qmd_files-expected_qmd)}"
        )

    id_locations: dict[str, list[str]] = {}
    texts: dict[str, str] = {}
    for name in sorted(qmd_files):
        text = (output_dir / name).read_text(encoding="utf-8")
        texts[name] = text
        for target_id in extract_ids(text):
            id_locations.setdefault(target_id, []).append(name)
    duplicates = {key: value for key, value in id_locations.items() if len(value) != 1}
    if duplicates:
        raise ReorganizationError(f"duplicate output IDs: {list(duplicates.items())[:10]}")
    missing_old = old_ids - set(id_locations)
    if missing_old:
        raise ReorganizationError(f"missing old IDs: {sorted(missing_old)[:20]}")

    internal_links = 0
    repository_links = 0
    for name, text in texts.items():
        for line, active in iter_outside_fences(text.splitlines(keepends=True)):
            if not active:
                continue
            for match in ALL_LINK_RE.finditer(line):
                dest = match.group("dest").strip("<>")
                if dest.startswith(("http://", "https://", "mailto:")):
                    continue
                if dest.startswith("#"):
                    target_file = name
                    target_id = dest[1:]
                else:
                    base, marker, target_id = dest.partition("#")
                    if base.endswith(".qmd"):
                        target_file = Path(base).name
                    elif base.startswith("../"):
                        # Generated candidates may live below data/generated, but
                        # repository links are authored for the final new_doc/
                        # location.  Validate against that logical location.
                        resolved = (logical_root / base).resolve()
                        if not resolved.exists():
                            raise ReorganizationError(f"{name}: broken repository link {dest}")
                        repository_links += 1
                        continue
                    else:
                        continue
                if target_file not in qmd_files:
                    raise ReorganizationError(f"{name}: missing linked QMD {dest}")
                if target_id and target_id not in extract_ids(texts[target_file]):
                    raise ReorganizationError(f"{name}: broken fragment {dest}")
                internal_links += 1

    missing_crossrefs = []
    for name, text in texts.items():
        for target_id in CROSSREF_RE.findall(text):
            if target_id not in id_locations:
                missing_crossrefs.append((name, target_id))
    if missing_crossrefs:
        raise ReorganizationError(f"missing cross-references: {missing_crossrefs[:20]}")

    bibliography = (output_dir / "references.bib").read_text(encoding="utf-8")
    bib_keys = set(BIB_KEY_RE.findall(bibliography))
    citation_keys = set()
    for text in texts.values():
        for key in CITATION_RE.findall(text):
            if not CROSSREF_RE.fullmatch("@" + key):
                citation_keys.add(key)
    missing_citations = citation_keys - bib_keys
    if missing_citations:
        raise ReorganizationError(f"missing bibliography keys: {sorted(missing_citations)}")

    chapter_files = {chapter["file"] for chapter in manifest["chapters"]}
    for name in chapter_files:
        if not texts[name].startswith("# "):
            raise ReorganizationError(f"{name}: missing chapter heading")

    return {
        "status": "pass",
        "qmd_files": len(qmd_files),
        "old_targets_preserved": len(old_ids),
        "new_targets": len(id_locations) - len(old_ids),
        "total_targets": len(id_locations),
        "internal_links": internal_links,
        "repository_links": repository_links,
        "cross_references": sum(len(CROSSREF_RE.findall(text)) for text in texts.values()),
        "citations": len(citation_keys),
    }


def build(
    source_dir: Path,
    output_dir: Path,
    logical_root: Path,
    manifest_path: Path,
    state_path: Path,
) -> None:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    logical_root = logical_root.resolve()
    manifest_path = manifest_path.resolve()
    state_path = state_path.resolve()
    if source_dir == output_dir:
        raise ReorganizationError("source and output directories must differ")
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ReorganizationError(f"output directory is not empty: {output_dir}")

    manifest = read_json(manifest_path)
    chapters = manifest["chapters"]
    chapter_by_id = {chapter["id"]: chapter for chapter in chapters}
    if len(chapter_by_id) != 14:
        raise ReorganizationError("manifest must define exactly fourteen chapters")
    part_chapters = [item for part in manifest["parts"] for item in part["chapters"]]
    if part_chapters != [chapter["id"] for chapter in chapters]:
        raise ReorganizationError("parts must contain the fourteen chapters once, in order")

    chunks, source_state = partition_sources(source_dir, manifest)
    manifest_chunk_keys = set(chunks)
    assembly_keys = []
    for chapter in chapters:
        assembly_keys.extend(chapter["chunks"])
    assembly_keys.extend(manifest["front_matter"]["index_chunks"])
    assembly_keys.extend(manifest["front_matter"]["outlook_chunks"])
    if set(assembly_keys) != manifest_chunk_keys or len(assembly_keys) != len(set(assembly_keys)):
        missing = manifest_chunk_keys - set(assembly_keys)
        extra = set(assembly_keys) - manifest_chunk_keys
        duplicates = sorted(key for key in set(assembly_keys) if assembly_keys.count(key) > 1)
        raise ReorganizationError(
            f"chunk assembly mismatch: missing={sorted(missing)}, extra={sorted(extra)}, "
            f"duplicates={duplicates}"
        )
    for key, chunk in chunks.items():
        destination = chunk.target
        if destination not in chapter_by_id and destination not in {"index", "outlook"}:
            raise ReorganizationError(f"{key}: unknown destination {destination}")
        if destination in chapter_by_id and key not in chapter_by_id[destination]["chunks"]:
            raise ReorganizationError(f"{key}: partition/assembly destination mismatch")

    notation_name = manifest["front_matter"]["notation_source"]
    notation_path = source_dir / notation_name
    if not notation_path.is_file():
        raise ReorganizationError(f"missing notation source: {notation_path}")

    destination_file = {chapter["id"]: chapter["file"] for chapter in chapters}
    destination_file.update({"index": "index.qmd", "outlook": "outlook.qmd"})
    id_to_file: dict[str, str] = {}
    old_ids: set[str] = set()
    for chunk in chunks.values():
        for target_id in extract_ids(chunk.text):
            if target_id in id_to_file:
                raise ReorganizationError(f"source target occurs twice: {target_id}")
            id_to_file[target_id] = destination_file[chunk.target]
            old_ids.add(target_id)
    notation_text = notation_path.read_text(encoding="utf-8")
    for target_id in extract_ids(notation_text):
        if target_id in id_to_file:
            raise ReorganizationError(f"source target occurs twice: {target_id}")
        id_to_file[target_id] = "notation.qmd"
        old_ids.add(target_id)

    for chapter in chapters:
        if chapter["anchor"] in id_to_file:
            raise ReorganizationError(f"new chapter anchor collides: {chapter['anchor']}")
        id_to_file[chapter["anchor"]] = chapter["file"]
    id_to_file["sec-book-architecture"] = "index.qmd"
    id_to_file["ch-strategic-outlook"] = "outlook.qmd"

    source_root_to_file = {}
    for source in manifest["source_partitions"]:
        root_id = first_heading_id((source_dir / source).read_text(encoding="utf-8"), source)
        source_root_to_file[source] = id_to_file[root_id]
    source_root_to_file[notation_name] = "notation.qmd"

    output_dir.mkdir(parents=True, exist_ok=True)
    generated: dict[str, str] = {}
    transformed_chunks: dict[str, str] = {}
    for key, chunk in chunks.items():
        transformed_chunks[key] = shift_chunk_headings(chunk.text)

    index_first, *index_rest = manifest["front_matter"]["index_chunks"]
    index_pieces = [chunks[index_first].text.rstrip(), architecture_block(chapters, manifest["parts"]).rstrip()]
    index_pieces.extend(chunks[key].text.rstrip() for key in index_rest)
    generated["index.qmd"] = "\n\n".join(index_pieces) + "\n"

    generated["notation.qmd"] = notation_text
    outlook_pieces = [
        "# Strategic outlook {#ch-strategic-outlook}\n\n"
        "This closing outlook preserves the established roadmap, scope boundaries and "
        "source-package map. Its stable links now lead to the reorganized chapters."
    ]
    outlook_pieces.extend(
        transformed_chunks[key].rstrip() for key in manifest["front_matter"]["outlook_chunks"]
    )
    generated["outlook.qmd"] = "\n\n".join(outlook_pieces) + "\n"

    for chapter in chapters:
        pieces = [
            f"# {chapter['number']}. {chapter['title']} {{#{chapter['anchor']}}}\n\n"
            f"{chapter['introduction']}"
        ]
        for key in chapter["chunks"]:
            chunk = chunks[key]
            pieces.append(
                f"<!-- moved verbatim from {chunk.source}:{chunk.start_line}-{chunk.end_line}; "
                f"only heading depth and internal link destinations may differ -->\n\n"
                f"{transformed_chunks[key].rstrip()}"
            )
        generated[chapter["file"]] = "\n\n".join(pieces) + "\n"

    expected_qmd = set(generated)
    output_files = expected_qmd | {"_quarto.yml", "references.bib", "pdf_breakable_tables.lua"}
    rewritten_total = 0
    for name, text in list(generated.items()):
        rewritten, count = rewrite_links(
            text, name, id_to_file, source_root_to_file, output_files
        )
        generated[name] = rewritten
        rewritten_total += count
        (output_dir / name).write_text(rewritten, encoding="utf-8")

    for support in ("references.bib", "pdf_breakable_tables.lua"):
        source = source_dir / support
        if not source.is_file():
            raise ReorganizationError(f"missing support file: {source}")
        shutil.copyfile(source, output_dir / support)
    (output_dir / "_quarto.yml").write_text(quarto_config(manifest), encoding="utf-8")

    checks = validate_output(output_dir, logical_root, old_ids, manifest, expected_qmd)
    checks["rewritten_internal_links"] = rewritten_total
    output_state = []
    for path in sorted(output_dir.iterdir()):
        if path.is_file():
            data = path.read_bytes()
            output_state.append(
                {"path": path.name, "bytes": len(data), "sha256": sha256_bytes(data)}
            )
    state = {
        "version": 1,
        "status": "pass",
        "manifest": {
            "path": str(manifest_path),
            "sha256": sha256_bytes(manifest_path.read_bytes()),
        },
        "source_directory": str(source_dir),
        "output_directory": str(output_dir),
        "logical_output_directory": str(logical_root),
        "sources": source_state,
        "notation": {
            "path": notation_name,
            "sha256": sha256_bytes(notation_path.read_bytes()),
        },
        "chunks": len(chunks),
        "checks": checks,
        "outputs": output_state,
    }
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "pass",
                "chapters": len(chapters),
                "parts": len(manifest["parts"]),
                "chunks": len(chunks),
                "old_targets_preserved": checks["old_targets_preserved"],
                "rewritten_internal_links": rewritten_total,
                "output": str(output_dir),
                "state": str(state_path),
            },
            indent=2,
        )
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build"])
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--logical-root", type=Path, default=DEFAULT_LOGICAL_ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--state", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        build(args.source, args.output, args.logical_root, args.manifest, args.state)
    except (OSError, ValueError, KeyError, ReorganizationError) as exc:
        print(f"reorganization: FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
