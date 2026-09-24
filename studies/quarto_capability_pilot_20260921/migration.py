#!/usr/bin/env python3
"""Deterministic Markdown-to-Quarto migration for the PDE book.

The maintained Markdown is read-only.  This program converts complete chapters,
builds stable source-coordinate labels and cross-references, and records anything
that still needs semantic mathematical transcription.  It uses only the Python
standard library and never invokes a model or renderer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import posixpath
import re
import tempfile
from urllib.parse import unquote, urlsplit


HERE = Path(__file__).resolve().parent
DEFAULT_REPO = HERE.parents[1]
DEFAULT_OUTPUT = DEFAULT_REPO / "new_doc"
DEFAULT_STATE = HERE / "migration_state.json"

FORMAL_PREFIX = {
    "theorem": "thm",
    "lemma": "lem",
    "proposition": "prp",
    "corollary": "cor",
    "definition": "def",
    "conjecture": "cnj",
    "remark": "rem",
    "example": "exm",
    "exercise": "exr",
    "solution": "sol",
    "algorithm": "alg",
    "proof": "proof",
}

BOLD_LEAD_RE = re.compile(
    r"^(?P<indent>\s*)\*\*(?P<caption>[^*]+)\*\*(?P<body>.*?)(?P<newline>\r?\n)?$"
)
PLAIN_PROOF_RE = re.compile(
    r"^(?P<indent>\s*)Proof(?P<punct>[.:])(?:\s*(?P<body>.*?))(?P<newline>\r?\n)?$"
)
SYMBOLIC_STATEMENT_RE = re.compile(
    r"^(?P<indent>\s*)\((?P<number>[A-Z])\)\s+"
    r"(?P<body>[A-Z][a-z][^\r\n]*?)(?P<newline>\r?\n)?$"
)
NUMBERED_BOLD_RE = re.compile(
    r"^(?P<number>\d+|(?:[IVXLCDM]+|[A-Z]|\d+)"
    r"(?:[.](?:[IVXLCDM]+|[A-Z]|\d+)){1,})[.]\s+(?P<title>.+?)[.]?$"
)
HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)(?P<newline>\r?\n)?$")
FENCE_RE = re.compile(r"^\s*(?P<fence>`{3,}|~{3,})")
DISPLAY_OPEN_RE = re.compile(r"^(?P<indent>\s*)\\\[\s*(?P<newline>\r?\n)?$")
DISPLAY_CLOSE_RE = re.compile(
    r"^(?P<indent>\s*)\\\](?P<tail>[^\r\n]*)(?P<newline>\r?\n)?$"
)
HTML_ANCHOR_RE = re.compile(
    r'^\s*<a\s+id=["\'](?P<id>[^"\']+)["\']\s*></a>\s*(?P<newline>\r?\n)?$',
    re.IGNORECASE,
)
INTERNAL_LINK_RE = re.compile(r"(?P<image>!?)\[(?P<caption>[^\]]*)\]\((?P<destination>[^)]+)\)")
RAW_REFERENCE_RE = re.compile(
    r"\b(?P<kind>Section|Fragment|Theorem|Lemma|Proposition|Corollary|Equation)"
    r"(?P<plural>s?)\s+(?P<number>[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)*)"
    r"|\b(?P<lower_kind>section|fragment|theorem|lemma|proposition|corollary|equation)"
    r"(?P<lower_plural>s?)\s+(?P<lower_number>[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)*)",
)
SECTION_SYMBOL_RE = re.compile(
    r"(?P<marks>§{1,2})(?P<space>\s*)"
    r"(?P<body>[A-Z0-9]+(?:[.][A-Z0-9]+)*"
    r"(?:(?:\s*(?:,|–|—|--)\s*)[A-Z0-9]+(?:[.][A-Z0-9]+)*)*)"
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def file_key(path: str) -> str:
    stem = path[:-3] if path.endswith(".md") else path
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")


def output_name(path: str) -> str:
    if path == "docs/README.md":
        return "index.qmd"
    if path == "docs/NOTATION.md":
        return "notation.qmd"
    return Path(path).stem.replace("_", "-") + ".qmd"


def discover(repo: Path) -> list[str]:
    guide = repo / "docs/README.md"
    available = {p.relative_to(repo).as_posix() for p in (repo / "docs").glob("*.md")}
    order = ["docs/README.md"]
    if "docs/NOTATION.md" in available:
        order.append("docs/NOTATION.md")
    for destination in re.findall(r"\[[^\]]*\]\(([^)]+)\)", guide.read_text(encoding="utf-8")):
        parsed = urlsplit(destination.strip().strip("<>"))
        if parsed.scheme or not parsed.path:
            continue
        candidate = (guide.parent / unquote(parsed.path)).resolve()
        if candidate.is_relative_to(repo):
            name = candidate.relative_to(repo).as_posix()
            if name in available and name not in order:
                order.append(name)
    order.extend(sorted(available.difference(order)))
    return order


def github_slug(title: str) -> str:
    title = re.sub(r"\{#[^}]+\}\s*$", "", title)
    title = re.sub(r"[`*_]", "", title).lower()
    title = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE)
    title = re.sub(r"\s+", "-", title.strip())
    return re.sub(r"-+", "-", title)


def leading_number(title: str) -> str | None:
    plain = re.sub(r"[`*_]", "", title).strip()
    component = r"(?:[IVXLCDM]+|[A-Z](?:[A-Z]*\d+)|[A-Z]|\d+)"
    match = re.match(
        rf"(?P<number>{component}(?:[.]{component})*)"
        rf"(?:[.:]\s+|\s+-\s+|\s+)",
        plain,
    )
    return match.group("number") if match else None


def fence_mask(lines: list[str]) -> list[bool]:
    result: list[bool] = []
    active: str | None = None
    for line in lines:
        match = FENCE_RE.match(line)
        if active is None:
            result.append(bool(match))
            if match:
                active = match.group("fence")[0]
        else:
            result.append(True)
            if match and match.group("fence")[0] == active:
                active = None
    return result


def fenced_blocks(lines: list[str]) -> list[str]:
    """Return complete fenced blocks exactly as written, including delimiters."""
    blocks: list[str] = []
    active: str | None = None
    buffer: list[str] = []
    for line in lines:
        match = FENCE_RE.match(line)
        if active is None:
            if match:
                active = match.group("fence")[0]
                buffer = [line]
        else:
            buffer.append(line)
            if match and match.group("fence")[0] == active:
                blocks.append("".join(buffer))
                active = None
                buffer = []
    if active is not None:
        blocks.append("".join(buffer))
    return blocks


def mask_inline_code(text: str) -> str:
    """Replace inline-code contents with spaces while preserving line structure."""
    output: list[str] = []
    position = 0
    while position < len(text):
        if text[position] != "`":
            output.append(text[position])
            position += 1
            continue
        run = 1
        while position + run < len(text) and text[position + run] == "`":
            run += 1
        end = text.find("`" * run, position + run)
        if end < 0:
            output.append(text[position])
            position += 1
            continue
        chunk = text[position:end + run]
        output.append("".join("\n" if character == "\n" else " " for character in chunk))
        position = end + run
    return "".join(output)


def balanced_tag_spans(text: str) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    cursor = 0
    while True:
        start = text.find(r"\tag{", cursor)
        if start < 0:
            break
        depth = 1
        index = start + 5
        while index < len(text) and depth:
            if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
                depth += 1
            elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
                depth -= 1
            index += 1
        if depth:
            break
        spans.append((start, index, text[start + 5 : index - 1]))
        cursor = index
    return spans


def remove_spans(text: str, spans: list[tuple[int, int, str]]) -> str:
    for start, end, _ in reversed(spans):
        left = start
        if left and text[left - 1] == " " and (end == len(text) or text[end : end + 1] in {"", "\n"}):
            left -= 1
        text = text[:left] + text[end:]
    return text


def dollar_displays(lines: list[str]) -> list[tuple[str, str | None]]:
    """Extract generated dollar-delimited displays outside fenced code."""
    masked = fence_mask(lines)
    displays: list[tuple[str, str | None]] = []
    active = False
    buffer: list[str] = []
    for index, line in enumerate(lines):
        if masked[index]:
            continue
        if not active and re.fullmatch(r"\s*\$\$\s*(?:\r?\n)?", line):
            active = True
            buffer = []
            continue
        if active:
            closing = re.fullmatch(
                r"\s*\$\$(?:\s+\{#(?P<label>[a-z]+-[a-z0-9-]+)\})?\s*(?:\r?\n)?",
                line,
            )
            if closing:
                displays.append(("".join(buffer), closing.group("label")))
                active = False
                buffer = []
            else:
                buffer.append(line)
    return displays


def classify_formal_caption(caption: str) -> tuple[str, str] | None:
    """Recognize the book's explicit bold formal-statement captions."""
    text = caption.strip()
    if text.endswith("."):
        text = text[:-1].rstrip()
    # Some legacy statements carry a subsection coordinate before the type.
    text = re.sub(
        r"^(?:[IVXLCDM]+|[A-Z]|\d+)(?:[.](?:[IVXLCDM]+|[A-Z]|\d+)){1,}[.]\s+",
        "",
        text,
    )
    proof = re.match(r"^Proof(?:\s*:\s*|\s+)(?P<tail>.*)$|^Proof$", text, re.IGNORECASE)
    if proof:
        return "proof", (proof.groupdict().get("tail") or "").strip()
    kinds = "|".join(kind for kind in FORMAL_PREFIX if kind != "proof")
    leading = re.match(rf"^(?P<kind>{kinds})\b(?P<tail>.*)$", text, re.IGNORECASE)
    if leading:
        return leading.group("kind").lower(), leading.group("tail").strip()
    trailing = re.match(rf"^(?P<name>.+?)\s+(?P<kind>{kinds})$", text, re.IGNORECASE)
    if trailing:
        return trailing.group("kind").lower(), f"({trailing.group('name').strip()})"
    return None


def parse_formal_caption(kind: str, tail: str) -> tuple[str, str | None, str | None]:
    rest = tail.strip()
    if rest.endswith("."):
        rest = rest[:-1].rstrip()
    if kind == "proof":
        name = rest if rest else None
        return kind, None, name
    number = None
    name = None
    if rest and not rest.startswith("("):
        first, _, remainder = rest.partition(" ")
        if re.fullmatch(r"[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)*", first):
            number = first
            rest = remainder.strip()
    if rest.startswith("(") and rest.endswith(")"):
        name = rest[1:-1].strip() or None
    elif rest:
        name = rest
    if number and not any(character.isdigit() for character in number) and name is None:
        name = number
    return kind, number, name


class Document:
    def __init__(self, path: str, text: str):
        self.path = path
        self.key = file_key(path)
        self.output = output_name(path)
        self.text = text
        self.lines = text.splitlines(keepends=True)
        self.mask = fence_mask(self.lines)
        self.targets: list[dict] = []
        self.headings: list[dict] = []
        self.displays: list[dict] = []
        self.formals: list[dict] = []
        self.statements: list[dict] = []
        self.anchors: list[dict] = []
        self.math_inventory: list[dict] = []
        self.pending_equations: list[dict] = []
        self.scan()
        self.math_inventory = legacy_math_inventory(self)
        self.pending_equations = pending_equations_from_inventory(
            self, self.math_inventory
        )
        self.targets.extend(self.pending_equations)

    def scan(self) -> None:
        structural: list[int] = []
        for index, line in enumerate(self.lines, 1):
            if self.mask[index - 1]:
                continue
            heading = HEADING_RE.match(line)
            if heading:
                title = re.sub(r"\s*\{#[^}]+\}\s*$", "", heading.group("title"))
                target = {
                    "id": f"sec-{self.key}-l{index}",
                    "kind": "sec",
                    "source": self.path,
                    "range": {"start": index, "end": index},
                    "name": title,
                    "number": leading_number(title),
                    "fragment": github_slug(title),
                    "level": len(heading.group("marks")),
                    "style": "markdown",
                    "status": "defined",
                }
                self.headings.append(target)
                self.targets.append(target)
                structural.append(index)

        for index, line in enumerate(self.lines, 1):
            if self.mask[index - 1]:
                continue
            bold = BOLD_LEAD_RE.match(line)
            if not bold or bold.group("indent"):
                continue
            numbered = NUMBERED_BOLD_RE.match(bold.group("caption").strip())
            if not numbered:
                continue
            title = numbered.group("title").rstrip(".")
            number = numbered.group("number")
            if number.isdigit():
                preceding_markdown = [
                    heading for heading in self.headings
                    if heading["style"] == "markdown"
                    and heading["range"]["start"] < index
                ]
                logical_level = (
                    preceding_markdown[-1]["level"] + 1
                    if preceding_markdown else 2
                )
            else:
                logical_level = min(6, len(number.split(".")) + 1)
            target = {
                "id": f"sec-{self.key}-l{index}",
                "kind": "sec",
                "source": self.path,
                "range": {"start": index, "end": index},
                "name": title,
                "number": number,
                "fragment": github_slug(number + "-" + title),
                "level": logical_level,
                "style": "bold",
                "status": "defined",
            }
            self.headings.append(target)
            self.targets.append(target)
            structural.append(index)

        self.headings.sort(key=lambda heading: heading["range"]["start"])
        headings_by_line = {heading["range"]["start"]: heading for heading in self.headings}
        for index, line in enumerate(self.lines, 1):
            if self.mask[index - 1]:
                continue
            match = HTML_ANCHOR_RE.match(line)
            if not match:
                continue
            following = next(
                (headings_by_line[line_number] for line_number in sorted(headings_by_line)
                 if line_number > index),
                None,
            )
            if following is not None:
                following.setdefault("aliases", []).append(match.group("id").lower())
                self.anchors.append({
                    "line": index,
                    "alias": match.group("id").lower(),
                    "target": following["id"],
                    "newline": match.group("newline") or "",
                })

        in_display = False
        start = 0
        buffer: list[str] = []
        for index, line in enumerate(self.lines, 1):
            if self.mask[index - 1]:
                continue
            if not in_display and DISPLAY_OPEN_RE.match(line):
                in_display, start, buffer = True, index, [line]
                continue
            if in_display:
                buffer.append(line)
                closing = DISPLAY_CLOSE_RE.match(line)
                if closing:
                    block = "".join(buffer)
                    tags = balanced_tag_spans(block)
                    record = {
                        "start": start,
                        "end": index,
                        "tags": tags,
                        "close_tail": closing.group("tail"),
                        "close_newline": closing.group("newline") or "",
                    }
                    if len(tags) == 1:
                        target = {
                            "id": f"eq-{self.key}-l{start}",
                            "kind": "eq",
                            "source": self.path,
                            "range": {"start": start, "end": index},
                            "name": tags[0][2],
                            "number": tags[0][2],
                            "status": "defined",
                        }
                        record["target"] = target
                        self.targets.append(target)
                    self.displays.append(record)
                    in_display, buffer = False, []

        for index, line in enumerate(self.lines, 1):
            if self.mask[index - 1]:
                continue
            match = BOLD_LEAD_RE.match(line)
            if not match:
                continue
            if match.group("indent"):
                continue
            classification = classify_formal_caption(match.group("caption"))
            if classification is None:
                continue
            kind, tail = classification
            kind, number, name = parse_formal_caption(kind, tail)
            prefix = FORMAL_PREFIX[kind]
            target = {
                "id": f"{prefix}-{self.key}-l{index}",
                "kind": prefix,
                "source": self.path,
                "range": {"start": index, "end": index},
                "name": name,
                "number": number,
                "status": "defined",
            }
            record = {
                "start": index,
                "kind": kind,
                "number": number,
                "name": name,
                "body": match.group("body").lstrip(),
                "newline": match.group("newline") or "",
                "target": target,
            }
            self.formals.append(record)
            self.targets.append(target)
            structural.append(index)

        existing_formal_starts = {formal["start"] for formal in self.formals}
        for index, line in enumerate(self.lines, 1):
            if self.mask[index - 1] or index in existing_formal_starts:
                continue
            match = PLAIN_PROOF_RE.match(line)
            if not match or match.group("indent"):
                continue
            target = {
                "id": f"proof-{self.key}-l{index}",
                "kind": "proof",
                "source": self.path,
                "range": {"start": index, "end": index},
                "name": None,
                "number": None,
                "status": "defined",
            }
            self.formals.append({
                "start": index,
                "kind": "proof",
                "number": None,
                "name": None,
                "body": match.group("body") or "",
                "newline": match.group("newline") or "",
                "target": target,
            })
            self.targets.append(target)
            structural.append(index)

        for index, line in enumerate(self.lines, 1):
            if self.mask[index - 1]:
                continue
            match = SYMBOLIC_STATEMENT_RE.match(line)
            if not match or match.group("indent"):
                continue
            target = {
                "id": f"stmt-{self.key}-l{index}",
                "kind": "stmt",
                "source": self.path,
                "range": {"start": index, "end": index},
                "name": f"Statement {match.group('number')}",
                "number": match.group("number"),
                "status": "defined",
            }
            self.statements.append({
                "line": index,
                "number": match.group("number"),
                "body": match.group("body"),
                "newline": match.group("newline") or "",
                "target": target,
            })
            self.targets.append(target)
            structural.append(index)

        structural = sorted(set(structural + [len(self.lines) + 1]))
        display_end_by_line = {
            line_number: display["end"]
            for display in self.displays
            for line_number in range(display["start"], display["end"] + 1)
        }
        for formal in self.formals:
            end = next(x for x in structural if x > formal["start"]) - 1
            if formal["kind"] == "proof":
                for line_number in range(formal["start"], end + 1):
                    if re.search(r"\\(?:black)?square|□|∎", self.lines[line_number - 1]):
                        end = display_end_by_line.get(line_number, line_number)
                        break
            while end > formal["start"] and not self.lines[end - 1].strip():
                end -= 1
            formal["end"] = end
            formal["target"]["range"]["end"] = end

    def context_at(self, line_number: int) -> tuple[str, ...]:
        stack: list[dict] = []
        for heading in self.headings:
            if heading["range"]["start"] > line_number:
                break
            while stack and stack[-1]["level"] >= heading["level"]:
                stack.pop()
            stack.append(heading)
        return tuple(heading["id"] for heading in stack)


class Index:
    def __init__(self, documents: list[Document]):
        self.documents = documents
        self.by_path = {document.path: document for document in documents}
        self.targets = [target for document in documents for target in document.targets]
        self.ids = {target["id"]: target for target in self.targets}
        self.headings_by_id = {
            heading["id"]: heading
            for document in documents for heading in document.headings
        }
        if len(self.ids) != len(self.targets):
            raise ValueError("duplicate target ID")
        self.heading_fragments: dict[str, dict[str, list[dict]]] = {}
        self.number_maps: dict[str, dict[str, dict[str, list[dict]]]] = {}
        self.global_numbers: dict[str, dict[str, list[dict]]] = {
            "sec": {}, "thm": {}, "lem": {}, "prp": {}, "cor": {}, "eq": {},
            "stmt": {},
        }
        aliases: dict[str, set[str]] = {}
        for document in documents:
            fragments: dict[str, list[dict]] = {}
            numbers: dict[str, dict[str, list[dict]]] = {
                "sec": {}, "thm": {}, "lem": {}, "prp": {}, "cor": {}, "eq": {},
                "stmt": {},
            }
            for heading in document.headings:
                fragments.setdefault(heading["fragment"], []).append(heading)
                for alias in heading.get("aliases", []):
                    fragments.setdefault(alias, []).append(heading)
            for target in document.targets:
                number = target.get("number")
                if number and target["kind"] in numbers:
                    numbers[target["kind"]].setdefault(number, []).append(target)
                    self.global_numbers[target["kind"]].setdefault(number, []).append(target)
            self.heading_fragments[document.path] = fragments
            self.number_maps[document.path] = numbers
            names = {
                document.path,
                Path(document.path).stem.replace("_", " "),
                Path(document.output).stem.replace("-", " "),
            }
            if document.headings:
                names.add(re.sub(
                    r"^(?:[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)*)[.:]?\s+",
                    "",
                    document.headings[0]["name"],
                ))
            for name in names:
                normalized = re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
                if normalized and normalized != "readme":
                    variants = {
                        normalized,
                        re.sub(r"\band\b", " ", normalized),
                    }
                    for variant in variants:
                        variant = re.sub(r"\s+", " ", variant).strip()
                        if variant:
                            aliases.setdefault(variant, set()).add(document.path)
        guide = self.by_path.get("docs/README.md")
        if guide:
            for match in INTERNAL_LINK_RE.finditer(guide.text):
                parsed = urlsplit(match.group("destination").strip().strip("<>"))
                target_path = self.link_path(guide.path, match.group("destination"))
                if parsed.scheme or parsed.fragment or target_path not in self.by_path:
                    continue
                caption = re.sub(r"[`*_]", "", match.group("caption"))
                normalized = re.sub(r"[^a-z0-9]+", " ", caption.lower()).strip()
                if normalized:
                    aliases.setdefault(normalized, set()).add(target_path)
        self.chapter_aliases = {
            alias: next(iter(paths))
            for alias, paths in aliases.items()
            if len(paths) == 1
        }

    def resolve_link(self, source: str, destination: str) -> dict | None:
        parsed = urlsplit(destination.strip().strip("<>"))
        if parsed.scheme or not parsed.path and not parsed.fragment:
            return None
        target_path = self.link_path(source, destination)
        if target_path is None:
            return None
        document = self.by_path.get(target_path)
        if not document:
            return None
        if not parsed.fragment:
            return document.headings[0] if document.headings else None
        fragment = unquote(parsed.fragment).lower()
        matches = self.heading_fragments[target_path].get(fragment, [])
        return matches[0] if len(matches) == 1 else None

    def section_declares_kind(self, target: dict, kind: str) -> bool:
        if target.get("kind") != "sec":
            return False
        document = self.by_path[target["source"]]
        contained = [
            formal for formal in document.formals
            if formal["start"] > target["range"]["start"]
            and target["id"] in document.context_at(formal["start"])
        ]
        if not contained:
            return False
        first = min(contained, key=lambda formal: formal["start"])
        return first["target"]["kind"] == kind

    @staticmethod
    def link_path(source: str, destination: str) -> str | None:
        parsed = urlsplit(destination.strip().strip("<>"))
        if parsed.scheme:
            return None
        if not parsed.path:
            return source
        target_path = posixpath.normpath(
            posixpath.join(posixpath.dirname(source), unquote(parsed.path))
        )
        if target_path == ".." or target_path.startswith("../"):
            return None
        return target_path

    def qualified_chapter(self, prefix: str) -> str | None:
        normalized = re.sub(r"[^a-z0-9]+", " ", prefix.lower()).strip()
        matches = [
            (alias, path) for alias, path in self.chapter_aliases.items()
            if normalized.endswith(alias)
        ]
        if not matches:
            return None
        longest = max(len(alias) for alias, _ in matches)
        paths = {path for alias, path in matches if len(alias) == longest}
        return next(iter(paths)) if len(paths) == 1 else None

    def named_chapter(self, phrase: str) -> str | None:
        exact = self.qualified_chapter(phrase)
        if exact:
            return exact
        tokens = set(re.findall(r"[a-z0-9]+", phrase.lower()))
        tokens.difference_update({"and", "the", "book", "chapter", "section", "sections"})
        if len(tokens) < 2:
            return None
        scores: dict[str, int] = {}
        for alias, path in self.chapter_aliases.items():
            alias_tokens = set(alias.split()).difference({"and", "the"})
            score = len(tokens.intersection(alias_tokens))
            scores[path] = max(scores.get(path, 0), score)
        best = max(scores.values(), default=0)
        winners = [path for path, score in scores.items() if score == best]
        return winners[0] if best >= 2 and len(winners) == 1 else None

    def last_explicit_chapter(self, phrase: str) -> str | None:
        """Return the last literally named chapter in a bounded prose context."""
        normalized = re.sub(r"[^a-z0-9]+", " ", phrase.lower()).strip()
        matches: list[tuple[int, int, str]] = []
        for alias, path in self.chapter_aliases.items():
            if alias in {"book", "chapter", "guide", "readme"}:
                continue
            for occurrence in re.finditer(
                rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", normalized
            ):
                matches.append((occurrence.end(), len(alias), path))
        if not matches:
            return None
        last_end = max(end for end, _, _ in matches)
        longest = max(length for end, length, _ in matches if end == last_end)
        paths = {
            path for end, length, path in matches
            if end == last_end and length == longest
        }
        return next(iter(paths)) if len(paths) == 1 else None

    def preceding_named_chapter(self, prefix: str) -> str | None:
        """Resolve an explicit chapter phrase immediately governing a reference."""
        exact = self.qualified_chapter(prefix)
        if exact:
            return exact
        chapter_phrase = re.search(
            r"(?:in|from|of)\s+(?:the\s+)?"
            r"(?P<name>[A-Za-z0-9][A-Za-z0-9 /_-]*?)\s+"
            r"chapter(?:'s)?[,;:]?\s*$",
            prefix,
            re.IGNORECASE,
        )
        if chapter_phrase:
            return self.named_chapter(chapter_phrase.group("name"))
        if re.search(r"\bsame\s+chapter(?:'s)?\s*$", prefix, re.IGNORECASE):
            return self.last_explicit_chapter(prefix)
        return None

    def shared_context_depth(self, source: str, line_number: int,
                             target: dict) -> int:
        reference_context = self.by_path[source].context_at(line_number)
        target_context = self.by_path[target["source"]].context_at(
            target["range"]["start"]
        )
        if target["source"] != source:
            return 0
        depth = 0
        for left, right in zip(reference_context, target_context):
            if left != right:
                break
            depth += 1
        return depth

    def adjacent_outline_units(self, source: str, line_number: int,
                               target: dict) -> bool:
        if target["source"] != source:
            return False
        document = self.by_path[source]
        reference_context = document.context_at(line_number)
        target_context = document.context_at(target["range"]["start"])
        depth = self.shared_context_depth(source, line_number, target)
        if depth == 0 or depth >= len(reference_context) or depth >= len(target_context):
            return False
        reference_child = self.headings_by_id[reference_context[depth]]
        target_child = self.headings_by_id[target_context[depth]]
        if reference_child["level"] != target_child["level"]:
            return False
        parent = reference_context[:depth]
        siblings = [
            heading for heading in document.headings
            if heading["level"] == reference_child["level"]
            and document.context_at(heading["range"]["start"])[:-1] == parent
        ]
        positions = {heading["id"]: position for position, heading in enumerate(siblings)}
        return abs(
            positions.get(reference_child["id"], -1000000)
            - positions.get(target_child["id"], 1000000)
        ) == 1

    def resolve_scoped_section(self, source: str, number: str, line_number: int,
                               prefix: str, suffix: str = "") -> dict | None:
        chapter_suffix = re.match(
            r"\s+of\s+(?:the\s+)?(?P<name>[A-Za-z0-9][A-Za-z0-9 /_-]*?)"
            r"\s+chapter\b",
            suffix,
            re.IGNORECASE,
        )
        qualified = (
            self.named_chapter(chapter_suffix.group("name"))
            if chapter_suffix else (
                self.preceding_named_chapter(prefix)
            )
        )
        if qualified:
            matches = self.number_maps[qualified]["sec"].get(number, [])
            if len(matches) == 1:
                return matches[0]
            # A chapter-qualified plain number denotes its top-level section
            # when that level is unique.  This handles books whose later
            # proof fragments restart local numbering without guessing among
            # peers at the same depth.
            if matches:
                shallowest = min(target["level"] for target in matches)
                winners = [
                    target for target in matches if target["level"] == shallowest
                ]
                if len(winners) == 1:
                    return winners[0]
            return None

        qualifier = re.search(
            r"(?P<number>[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)+),?\s*$",
            prefix,
        )
        if qualifier:
            parent = self.resolve_number(
                source, "sec", qualifier.group("number"), line_number,
                allow_cross_kind=False,
            )
            if parent and parent["source"] == source:
                matches = self.number_maps[source]["sec"].get(number, [])
                scoped = [
                    target for target in matches
                    if parent["id"] in self.by_path[source].context_at(
                        target["range"]["start"]
                    )
                ]
                if len(scoped) == 1:
                    return scoped[0]
                parent_number = parent.get("number")
                if parent_number:
                    if number.startswith(parent_number.rsplit(".", 1)[-1] + "."):
                        expanded = parent_number.rsplit(".", 1)[0] + "." + number
                    elif "." not in number:
                        expanded = parent_number + "." + number
                    else:
                        expanded = ""
                    expanded_matches = [
                        target
                        for target in self.number_maps[source]["sec"].get(expanded, [])
                        if parent["id"] in self.by_path[source].context_at(
                            target["range"]["start"]
                        )
                    ]
                    if len(expanded_matches) == 1:
                        return expanded_matches[0]

        context = self.by_path[source].context_at(line_number)
        context_headings = [self.headings_by_id[target_id] for target_id in context]

        # Inside an explicitly named proof unit A, prose often abbreviates
        # A.3 as "section 3".  Plain-number bold subunits use the same local
        # convention.  Require a common immediate outline parent so the rule
        # cannot jump to another restarted numbering sequence.
        if number.isdigit():
            current_numbered = next(
                (
                    heading for heading in reversed(context_headings)
                    if heading.get("number")
                ),
                None,
            )
            lookup_number: str | None = None
            if current_numbered is not None:
                current_number = current_numbered["number"]
                if current_number.isdigit():
                    lookup_number = number
                elif "." in current_number:
                    coordinate_parent = current_number.rsplit(".", 1)[0]
                    proof_unit = any(
                        re.match(
                            rf"Proof unit\s+{re.escape(coordinate_parent)}(?:[.]|\b)",
                            ancestor["name"],
                            re.IGNORECASE,
                        )
                        for ancestor in context_headings
                        if ancestor["id"] != current_numbered["id"]
                    )
                    if proof_unit:
                        lookup_number = f"{coordinate_parent}.{number}"
                if lookup_number:
                    current_position = context.index(current_numbered["id"])
                    current_parent = context[:current_position]
                    local = [
                        target
                        for target in self.number_maps[source]["sec"].get(
                            lookup_number, []
                        )
                        if target["level"] == current_numbered["level"]
                        and self.by_path[source].context_at(
                            target["range"]["start"]
                        )[:-1] == current_parent
                    ]
                    if len(local) == 1:
                        return local[0]

        # Local proof and construction units sometimes restart coordinates such
        # as D.1, D.2, ... at the same Markdown level.  If the reference itself
        # lies inside D.k, the matching D.* run is stronger evidence than an
        # accidentally shared higher-level Markdown ancestor.  Select the
        # nearest same-level member of that coordinate series; ties stay
        # unresolved.
        if "." in number:
            coordinate_parent = number.rsplit(".", 1)[0]
            series_context = next(
                (
                    heading for heading in reversed(context_headings)
                    if heading.get("number")
                    and heading["number"].rsplit(".", 1)[0] == coordinate_parent
                ),
                None,
            )
            if series_context is not None:
                matches = [
                    target for target in self.number_maps[source]["sec"].get(number, [])
                    if target["level"] == series_context["level"]
                ]
                if matches:
                    distances = [
                        abs(
                            target["range"]["start"]
                            - series_context["range"]["start"]
                        )
                        for target in matches
                    ]
                    closest = min(distances)
                    winners = [
                        target for target, distance in zip(matches, distances)
                        if distance == closest
                    ]
                    if len(winners) == 1:
                        return winners[0]

        if number.count(".") >= 2:
            global_matches = self.global_numbers["sec"].get(number, [])
            if len(global_matches) == 1:
                return global_matches[0]

        target = self.resolve_number(
            source, "sec", number, line_number, allow_cross_kind=False
        )
        # resolve_number only crosses files for a globally unique coordinate.
        # That is a valid book-level reference and is part of the deterministic
        # uniqueness contract; repeated short numbers still remain unresolved.
        return target

    def resolve_number(self, source: str, kind: str, number: str,
                       line_number: int | None = None,
                       allow_cross_kind: bool = True) -> dict | None:
        matches = self.number_maps[source].get(kind, {}).get(number, [])
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1 and line_number is not None:
            # Reused proof-unit coordinates sit below the chapter's canonical
            # coordinate.  Outside a matching local X.k series, the unique
            # shallowest X.k is therefore the unqualified book destination.
            # resolve_scoped_section has already handled an active local
            # series and any explicit chapter/ancestor qualifier.
            if kind == "sec":
                shallowest = min(target["level"] for target in matches)
                winners = [target for target in matches if target["level"] == shallowest]
                if len(winners) == 1:
                    return winners[0]
            reference_context = self.by_path[source].context_at(line_number)

            def shared_depth(target: dict) -> int:
                target_context = self.by_path[source].context_at(target["range"]["start"])
                depth = 0
                for left, right in zip(reference_context, target_context):
                    if left != right:
                        break
                    depth += 1
                return depth

            scores = [shared_depth(target) for target in matches]
            best = max(scores, default=0)
            winners = [target for target, score in zip(matches, scores) if score == best]
            if best >= 2 and len(winners) == 1:
                return winners[0]
            by_distance = sorted(
                matches, key=lambda target: abs(target["range"]["start"] - line_number)
            )
            if (
                len(by_distance) >= 2
                and abs(by_distance[0]["range"]["start"] - line_number) * 2
                < abs(by_distance[1]["range"]["start"] - line_number)
            ):
                return by_distance[0]
        global_matches = self.global_numbers.get(kind, {}).get(number, [])
        if len(global_matches) == 1:
            return global_matches[0]
        if (
            kind == "sec"
            and len(global_matches) > 1
            and ("." in number or any(c.isalpha() for c in number))
        ):
            shallowest = min(target["level"] for target in global_matches)
            winners = [target for target in global_matches if target["level"] == shallowest]
            if len(winners) == 1:
                return winners[0]
        if kind != "sec" and allow_cross_kind:
            return self.resolve_number(source, "sec", number, line_number)
        return None

    def resolve_statement(self, source: str, number: str,
                          line_number: int) -> dict | None:
        matches = self.number_maps[source]["stmt"].get(number, [])
        scored = [
            (target, self.shared_context_depth(source, line_number, target))
            for target in matches
        ]
        best = max((score for _, score in scored), default=0)
        winners = [target for target, score in scored if score == best]
        return winners[0] if best >= 2 and len(winners) == 1 else None

    def resolve_qualified_equation(self, source: str, token: str,
                                   line_number: int) -> dict | None:
        """Resolve ``section.coordinate.tag`` when displays use a local tag."""
        direct = self.resolve_number(
            source, "eq", token, line_number, allow_cross_kind=False
        )
        if direct:
            return direct
        pieces = token.split(".")
        for split in range(len(pieces) - 1, 0, -1):
            section_number = ".".join(pieces[:split])
            local_tag = ".".join(pieces[split:])
            section = self.resolve_number(
                source, "sec", section_number, line_number,
                allow_cross_kind=False,
            )
            if not section or section["source"] != source:
                continue
            candidates = [
                target for target in self.number_maps[source]["eq"].get(local_tag, [])
                if section["id"] in self.by_path[source].context_at(
                    target["range"]["start"]
                )
            ]
            if len(candidates) == 1:
                return candidates[0]
        return None

    def resolve_bare_equation(self, source: str, number: str,
                              line_number: int, prefix: str = "") -> dict | None:
        """Resolve a parenthesized equation citation without global guessing.

        Compound legacy tags carry their own scope.  A simple local tag such
        as ``(2)`` or ``(F)`` must share a non-root outline ancestor with its
        target; otherwise a unique but remote reuse in another proof unit is
        not evidence of identity.
        """
        qualifier = re.search(
            r"(?P<number>[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)+),?\s*$",
            prefix,
        )
        if qualifier:
            parent = self.resolve_number(
                source, "sec", qualifier.group("number"), line_number,
                allow_cross_kind=False,
            )
            if parent and parent["source"] == source:
                scoped = [
                    target for target in self.number_maps[source]["eq"].get(number, [])
                    if parent["id"] in self.by_path[source].context_at(
                        target["range"]["start"]
                    )
                ]
                if len(scoped) == 1:
                    return scoped[0]
        if (
            "." in number or "-" in number
            or re.search(r"[A-Za-z]", number) and re.search(r"\d", number)
        ):
            return self.resolve_number(
                source, "eq", number, line_number, allow_cross_kind=False
            )
        matches = self.number_maps[source]["eq"].get(number, [])
        scoped = [
            (target, self.shared_context_depth(source, line_number, target))
            for target in matches
        ]
        best = max((depth for _, depth in scoped), default=0)
        winners = [target for target, depth in scoped if depth == best]
        if best >= 2 and len(winners) == 1:
            return winners[0]
        by_distance = sorted(
            winners, key=lambda target: abs(target["range"]["start"] - line_number)
        )
        if (
            best >= 2 and len(by_distance) >= 2
            and abs(by_distance[0]["range"]["start"] - line_number) * 2
            < abs(by_distance[1]["range"]["start"] - line_number)
        ):
            return by_distance[0]
        if len(winners) == 1 and self.adjacent_outline_units(
            source, line_number, winners[0]
        ):
            return winners[0]
        return None


def replacement_for_link(caption: str, target: dict, index: Index) -> str:
    plain = re.sub(r"[`*_]", "", caption).strip()
    match = RAW_REFERENCE_RE.fullmatch(plain)
    if match:
        kind, plural, number = reference_parts(match)
        if (
            target["kind"] != "sec"
            and not plural
            and plausible_reference_number(kind, number)
        ):
            return "@" + target["id"]
    destination = index.by_path[target["source"]].output + "#" + target["id"]
    return f"[{caption}]({destination})"


def map_kind(word: str) -> str:
    return {
        "section": "sec", "fragment": "sec", "theorem": "thm", "lemma": "lem",
        "proposition": "prp", "corollary": "cor", "equation": "eq",
    }[word.lower()]


def reference_parts(match: re.Match) -> tuple[str, str, str]:
    kind = match.group("kind") or match.group("lower_kind")
    plural = match.group("plural") if match.group("kind") else match.group("lower_plural")
    number = match.group("number") or match.group("lower_number")
    return kind, plural, number


def plausible_reference_number(kind: str, number: str) -> bool:
    if any(character.isdigit() for character in number):
        return True
    if kind[0].isupper() and number.isupper():
        return bool(re.fullmatch(r"[A-Z]+(?:[.][A-Z]+)*", number))
    return False


def obvious_code_span(content: str) -> bool:
    value = content.strip()
    lower = value.lower()
    if (
        not value
        or "://" in value
        or value.startswith("--")
        or lower.startswith("pde.")
        or lower.endswith((".py", ".md", ".qmd", ".json", ".yaml", ".yml", ".toml",
                           ".csv", ".npy", ".npz", ".pt", ".sh"))
        or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*\(\)", value)
        or re.fullmatch(r"pde(?:[.][A-Za-z_][A-Za-z0-9_]*)+", value)
    ):
        return True
    return False


def math_candidate(content: str) -> bool:
    value = content.strip()
    if obvious_code_span(value):
        return False
    return True


def normalize_inline_math_spacing(text: str) -> str:
    text = re.sub(r"\\\([ \t]+", r"\(", text)
    return re.sub(r"[ \t]+\\\)", r"\)", text)


def mask_legacy_inline_math(line: str, active: bool) -> tuple[str, bool]:
    """Mask legacy inline TeX while retaining all other characters and newlines."""
    output: list[str] = []
    position = 0
    while position < len(line):
        delimiter = r"\)" if active else r"\("
        found = line.find(delimiter, position)
        if found < 0:
            chunk = line[position:]
            if active:
                output.append("".join("\n" if c == "\n" else " " for c in chunk))
            else:
                output.append(chunk)
            break
        chunk = line[position:found + 2]
        if active:
            output.append("".join("\n" if c == "\n" else " " for c in chunk))
        else:
            output.append(line[position:found])
            output.append("  ")
        active = not active
        position = found + 2
    return "".join(output), active


def mask_dollar_inline_math(line: str) -> str:
    pattern = re.compile(r"(?<!\\)\$(?!\$).*?(?<!\\)\$")
    return pattern.sub(
        lambda match: "".join("\n" if c == "\n" else " " for c in match.group(0)),
        line,
    )


def mask_legacy_inline_code(line: str, delimiter_length: int) -> tuple[str, int]:
    """Mask Markdown code spans, including spans continued onto later lines."""
    output: list[str] = []
    position = 0
    while position < len(line):
        if delimiter_length:
            delimiter = "`" * delimiter_length
            found = line.find(delimiter, position)
            if found < 0:
                output.append("".join("\n" if c == "\n" else " " for c in line[position:]))
                break
            chunk = line[position:found + delimiter_length]
            output.append("".join("\n" if c == "\n" else " " for c in chunk))
            delimiter_length = 0
            position = found + len(delimiter)
            continue
        found = line.find("`", position)
        if found < 0:
            output.append(line[position:])
            break
        output.append(line[position:found])
        run = 1
        while found + run < len(line) and line[found + run] == "`":
            run += 1
        output.append(" " * run)
        delimiter_length = run
        position = found + run
    return "".join(output), delimiter_length


def legacy_code_math_inventory(document: "Document", display_lines: set[int]) -> list[dict]:
    records: list[dict] = []
    delimiter_length = 0
    start_line = 0
    content: list[str] = []
    for line_number, line in enumerate(document.lines, 1):
        if document.mask[line_number - 1] or line_number in display_lines:
            continue
        position = 0
        while position < len(line):
            if delimiter_length:
                delimiter = "`" * delimiter_length
                found = line.find(delimiter, position)
                if found < 0:
                    content.append(line[position:])
                    break
                content.append(line[position:found])
                inside = "".join(content)
                if math_candidate(inside):
                    records.append({
                        "kind": "math",
                        "form": "inline-code",
                        "source": document.path,
                        "line": start_line,
                        "end": line_number,
                        "text": delimiter + inside + delimiter,
                        "reason": "legacy code-form math requires semantic transcription",
                    })
                position = found + delimiter_length
                delimiter_length = 0
                content = []
                continue
            found = line.find("`", position)
            if found < 0:
                break
            delimiter_length = 1
            while found + delimiter_length < len(line) and line[found + delimiter_length] == "`":
                delimiter_length += 1
            start_line = line_number
            content = []
            position = found + delimiter_length
    if delimiter_length:
        raise ValueError(f"{document.path}: unclosed inline-code delimiter")
    return records


def has_legacy_math_signal(text: str) -> bool:
    text = re.sub(r"!?\[[^\]]*\]\([^)]+\)", "", text)
    return bool(re.search(
        r"(?:<=|>=|->|=>|(?<![=!<>])=(?!=)|\|\||"
        r"[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9({]|"
        r"(?<=[A-Za-z0-9)}])\^(?=[A-Za-z0-9({-])|"
        r"\b(?:sqrt|sum|prod|integral|exp|log)\s*[_({]|[≤≥∞∑√⊗])",
        text,
    ))


def legacy_math_inventory(document: "Document") -> list[dict]:
    """Find non-TeX legacy formula spans without attempting to transcribe them."""
    display_lines = {
        line_number
        for display in document.displays
        for line_number in range(display["start"], display["end"] + 1)
    }
    records = legacy_code_math_inventory(document, display_lines)
    residual: list[str] = []
    inline_active = False
    code_delimiter_length = 0
    for line_number, line in enumerate(document.lines, 1):
        if document.mask[line_number - 1] or line_number in display_lines:
            residual.append("")
            continue
        outside_code, code_delimiter_length = mask_legacy_inline_code(
            line, code_delimiter_length
        )
        outside_math, inline_active = mask_legacy_inline_math(outside_code, inline_active)
        residual.append(mask_dollar_inline_math(outside_math))

    consumed: set[int] = set()
    line_number = 1
    while line_number <= len(document.lines):
        if (
            residual[line_number - 1]
            and re.match(r"^ {4,}\S", document.lines[line_number - 1])
        ):
            start = line_number
            block: list[str] = []
            block_residual: list[str] = []
            while line_number <= len(document.lines) and (
                re.match(r"^ {4,}", document.lines[line_number - 1])
                or not document.lines[line_number - 1].strip()
            ):
                block.append(document.lines[line_number - 1])
                block_residual.append(residual[line_number - 1])
                line_number += 1
            end = line_number - 1
            if has_legacy_math_signal("".join(block_residual)):
                consumed.update(range(start, end + 1))
                records.append({
                    "kind": "math",
                    "form": "indented-display",
                    "source": document.path,
                    "line": start,
                    "end": end,
                    "text": "".join(block).rstrip("\r\n"),
                    "reason": "legacy indented formula requires semantic transcription",
                })
            continue
        line_number += 1

    for line_number, line in enumerate(residual, 1):
        if line_number in consumed or not line.strip():
            continue
        if has_legacy_math_signal(line):
            records.append({
                "kind": "math",
                "form": "plain-line",
                "source": document.path,
                "line": line_number,
                "end": line_number,
                "text": document.lines[line_number - 1].rstrip("\r\n"),
                "reason": "legacy plain-text formula requires semantic transcription",
            })
    return add_aligned_formula_inventory(document, records, display_lines)


PENDING_EQUATION_LABEL_RE = re.compile(
    r"\S[ \t]{2,}\((?P<tag>[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)\)\s*$"
)
INDENTED_EQUATION_LABEL_RE = re.compile(
    r"\S[ \t]+\((?P<tag>[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)\)\s*$"
)
RAW_FORMULA_LEAD_RE = re.compile(
    r"^\s*\S+\s*(?:=|<=|>=|<|>|≤|≥)"
)


def add_aligned_formula_inventory(document: "Document", records: list[dict],
                                  display_lines: set[int]) -> list[dict]:
    """Inventory high-confidence numbered formula lines missed by signal tests."""
    covered = {
        line_number
        for record in records
        for line_number in range(record["line"], record.get("end", record["line"]) + 1)
    }
    for line_number, line in enumerate(document.lines, 1):
        if (
            document.mask[line_number - 1]
            or line_number in display_lines
            or line_number in covered
        ):
            continue
        if PENDING_EQUATION_LABEL_RE.search(line.rstrip("\r\n")):
            records.append({
                "kind": "math",
                "form": "plain-line",
                "source": document.path,
                "line": line_number,
                "end": line_number,
                "text": line.rstrip("\r\n"),
                "reason": "aligned numbered formula requires semantic transcription",
            })
    return records


def pending_label_match(text: str, form: str) -> re.Match | None:
    strict = PENDING_EQUATION_LABEL_RE.search(text)
    if strict:
        return strict
    loose = INDENTED_EQUATION_LABEL_RE.search(text)
    if form == "indented-display":
        return loose
    if form == "plain-line" and RAW_FORMULA_LEAD_RE.match(text):
        return loose
    return None


def pending_equations_from_inventory(document: "Document",
                                     records: list[dict]) -> list[dict]:
    """Reserve targets for unmistakably labelled legacy formula blocks.

    A reservation does not define a Quarto equation or alter the source text.
    The later transcription pass must attach this exact ID to the converted
    display.  Requiring alignment whitespace before the terminal label rejects
    function arguments such as ``o_P(1)`` and prose such as ``Equation (2)``.
    """
    pending: list[dict] = []
    for record in records:
        if record["form"] not in {"indented-display", "plain-line"}:
            continue
        block_start = record["line"]
        block_end = record.get("end", block_start)
        label_lines: list[tuple[int, re.Match]] = []
        for line_number in range(block_start, block_end + 1):
            match = pending_label_match(
                document.lines[line_number - 1].rstrip("\r\n"), record["form"]
            )
            if match:
                label_lines.append((line_number, match))
        cursor = block_start
        for label_line, match in label_lines:
            # Blank lines separate independently numbered formulas inside one
            # Markdown indented block.  A preceding numbered line also ends
            # the previous formula even when no blank line is present.
            unit_start = cursor
            for line_number in range(cursor, label_line):
                if not document.lines[line_number - 1].strip():
                    unit_start = line_number + 1
            while unit_start < label_line and not document.lines[unit_start - 1].strip():
                unit_start += 1
            pending.append({
                "id": f"eq-{document.key}-l{unit_start}",
                "kind": "eq",
                "source": document.path,
                "range": {"start": unit_start, "end": label_line},
                "label_line": label_line,
                "name": match.group("tag"),
                "number": match.group("tag"),
                "form": record["form"],
                "status": "reserved",
            })
            cursor = label_line + 1
    return pending


def record_reference(references: list[dict], source: str, line_number: int,
                     text: str, target: dict, method: str,
                     rendered: bool) -> None:
    references.append({
        "source": source,
        "line": line_number,
        "text": text,
        "target": target["id"],
        "method": method,
        "target_status": target.get("status", "defined"),
        "rendered": rendered,
    })


def convert_plain_segment(segment: str, source: str, line_number: int, index: Index,
                          references: list[dict], unresolved: list[dict],
                          prior_context: str = "") -> str:
    equation_map = index.number_maps[source]["eq"]

    section_number = re.compile(r"[A-Z0-9]+(?:[.][A-Z0-9]+)*")

    def section_symbol_replacement(match: re.Match) -> str:
        occurrences = list(section_number.finditer(match.group("body")))
        scope_prefix = prior_context + segment[:match.start()]
        targets = [
            index.resolve_scoped_section(
                source, occurrence.group(0), line_number, scope_prefix
            )
            for occurrence in occurrences
        ]
        if not occurrences or any(target is None for target in targets):
            unresolved.append({
                "kind": "reference", "source": source, "line": line_number,
                "text": match.group(0),
                "reason": "section-symbol shorthand needs an explicit scope",
            })
            return match.group(0)
        target_paths = {target["source"] for target in targets if target}
        if len(target_paths) != 1:
            unresolved.append({
                "kind": "reference", "source": source, "line": line_number,
                "text": match.group(0),
                "reason": "section-symbol endpoints do not share one chapter",
            })
            return match.group(0)

        body = match.group("body")
        converted: list[str] = []
        position = 0
        for occurrence, target in zip(occurrences, targets):
            assert target is not None
            converted.append(body[position:occurrence.start()])
            destination = index.by_path[target["source"]].output + "#" + target["id"]
            converted.append(f"[{occurrence.group(0)}]({destination})")
            record_reference(
                references, source, line_number, occurrence.group(0), target,
                "section-symbol", rendered=True,
            )
            position = occurrence.end()
        converted.append(body[position:])
        return match.group("marks") + match.group("space") + "".join(converted)

    segment = SECTION_SYMBOL_RE.sub(section_symbol_replacement, segment)

    multiple_reference = re.compile(
        r"\b(?P<word>Sections|Fragments|Theorems|Lemmas|Propositions|Corollaries|Equations)"
        r"\s+(?P<first>[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)*)"
        r"(?P<space1>\s*)(?P<join>–|—|--|\band\b|\bor\b|\bto\b)(?P<space2>\s*)"
        r"(?P<last>[A-Za-z0-9]+(?:[.][A-Za-z0-9]+)*)",
        re.IGNORECASE,
    )

    def multiple_replacement(match: re.Match) -> str:
        kind = {
            "sections": "sec", "fragments": "sec", "theorems": "thm", "lemmas": "lem",
            "propositions": "prp", "corollaries": "cor", "equations": "eq",
        }[match.group("word").lower()]
        first_number, last_number = match.group("first"), match.group("last")
        if not (
            (any(c.isdigit() for c in first_number) or first_number.isupper())
            and (any(c.isdigit() for c in last_number) or last_number.isupper())
        ):
            return match.group(0)
        scope_prefix = prior_context + segment[:match.start()]
        scope_suffix = segment[match.end():]
        if kind == "sec":
            first_target = index.resolve_scoped_section(
                source, first_number, line_number, scope_prefix, scope_suffix
            )
            last_target = index.resolve_scoped_section(
                source, last_number, line_number, scope_prefix, scope_suffix
            )
        else:
            first_target = index.resolve_number(source, kind, first_number, line_number)
            last_target = index.resolve_number(source, kind, last_number, line_number)
        if not first_target or not last_target:
            unresolved.append({
                "kind": "reference", "source": source, "line": line_number,
                "text": match.group(0),
                "reason": "one or both endpoints of the reference are ambiguous",
            })
            return match.group(0)
        if any(
            target.get("status") != "defined"
            for target in (first_target, last_target)
        ):
            for number, target in ((first_number, first_target), (last_number, last_target)):
                record_reference(
                    references, source, line_number, number, target,
                    "explicit-multiple", rendered=False,
                )
            return match.group(0)

        def endpoint(number: str, target: dict) -> str:
            if target["kind"] == kind and kind != "sec":
                value = f"[-@{target['id']}]"
                return f"({value})" if kind == "eq" else value
            destination = index.by_path[target["source"]].output + "#" + target["id"]
            return f"[{number}]({destination})"

        for number, target in ((first_number, first_target), (last_number, last_target)):
            record_reference(
                references, source, line_number, number, target,
                "explicit-multiple", rendered=True,
            )
        return (
            match.group("word") + " " + endpoint(first_number, first_target)
            + match.group("space1") + match.group("join") + match.group("space2")
            + endpoint(last_number, last_target)
        )

    segment = multiple_reference.sub(multiple_replacement, segment)

    bare_section_range = re.compile(
        r"(?<![A-Za-z0-9_.@-])"
        r"(?P<first>[A-Z][A-Z0-9]*(?:[.][A-Z0-9]+)+)"
        r"(?P<dash>–|—|--)"
        r"(?P<last>[A-Z][A-Z0-9]*(?:[.][A-Z0-9]+)+|[A-Z][A-Z0-9]*|\d+)"
        r"(?![A-Za-z0-9_.@-])"
    )

    def bare_section_range_replacement(match: re.Match) -> str:
        first = match.group("first")
        last_written = match.group("last")
        last = (
            last_written if "." in last_written
            else first.rsplit(".", 1)[0] + "." + last_written
        )
        # An equation namespace collision makes a bare coordinate semantic;
        # let the equation rule handle it or leave it unresolved.
        if (
            equation_map.get(first) or equation_map.get(last)
            or (
                re.search(r"[A-Za-z]", first.rsplit(".", 1)[-1])
                and equation_map.get(first.rsplit(".", 1)[-1])
            )
            or (
                re.search(r"[A-Za-z]", last.rsplit(".", 1)[-1])
                and equation_map.get(last.rsplit(".", 1)[-1])
            )
        ):
            return match.group(0)
        scope_prefix = prior_context + segment[:match.start()]
        scope_suffix = segment[match.end():]
        first_target = index.resolve_scoped_section(
            source, first, line_number, scope_prefix, scope_suffix
        )
        last_target = index.resolve_scoped_section(
            source, last, line_number, scope_prefix, scope_suffix
        )
        if not first_target or not last_target:
            unresolved.append({
                "kind": "reference", "source": source, "line": line_number,
                "text": match.group(0),
                "reason": "bare section range is absent or repeated in this chapter",
            })
            return match.group(0)
        if (
            first_target["source"] != last_target["source"]
            or (
                first_target["source"] == source
                and line_number in {
                    first_target["range"]["start"], last_target["range"]["start"]
                }
            )
        ):
            return match.group(0)
        target_document = index.by_path[first_target["source"]]
        first_destination = target_document.output + "#" + first_target["id"]
        last_destination = target_document.output + "#" + last_target["id"]
        record_reference(
            references, source, line_number, first, first_target,
            "bare-section-range", rendered=True,
        )
        record_reference(
            references, source, line_number, last_written, last_target,
            "bare-section-range", rendered=True,
        )
        return (
            f"[{first}]({first_destination}){match.group('dash')}"
            f"[{last_written}]({last_destination})"
        )

    segment = bare_section_range.sub(bare_section_range_replacement, segment)

    abbreviated_range = re.compile(
        r"(?<![A-Za-z0-9_.@-])"
        r"(?P<first>[A-Za-z0-9]+(?:[.][A-Za-z0-9-]+){2,})"
        r"(?P<dash>–|—|--)"
        r"(?P<last>[A-Za-z][A-Za-z0-9-]*)"
        r"(?![A-Za-z0-9_.@-])"
    )

    def range_replacement(match: re.Match) -> str:
        first = match.group("first")
        last = first.rsplit(".", 1)[0] + "." + match.group("last")
        if not re.search(r"[A-Za-z]", first.rsplit(".", 1)[-1]):
            return match.group(0)
        first_target = index.resolve_qualified_equation(source, first, line_number)
        last_target = index.resolve_qualified_equation(source, last, line_number)
        if not first_target or not last_target:
            return match.group(0)
        if any(
            target.get("status") != "defined"
            for target in (first_target, last_target)
        ):
            for text_value, target in (
                (first, first_target), (match.group("last"), last_target)
            ):
                record_reference(
                    references, source, line_number, text_value, target,
                    "bare-equation-token-range", rendered=False,
                )
            return match.group(0)
        for text_value, target in ((first, first_target), (match.group("last"), last_target)):
            record_reference(
                references, source, line_number, text_value, target,
                "bare-equation-token-range", rendered=True,
            )
        return (
            f"[-@{first_target['id']}]"
            f"{match.group('dash')}"
            f"[-@{last_target['id']}]"
        )

    segment = abbreviated_range.sub(range_replacement, segment)

    # Some long-form tags are cited as bare tokens rather than as ``(tag)``.
    # Match only compound tokens, outside explicit ``Section ...``-style
    # references, and require an actual indexed equation target before changing
    # anything.  Parenthesized tags are handled separately below so a legacy
    # formula's own trailing number can be protected.
    bare_token = re.compile(
        r"(?<![A-Za-z0-9_.(@-])"
        r"(?P<tag>[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)+)"
        r"(?![A-Za-z0-9_.@-])"
    )

    def token_replacement(match: re.Match) -> str:
        tag = match.group("tag")
        parts = tag.split(".")
        # Short bare tokens such as ``3.1``, ``D.4`` and ``III.F.2`` are also
        # used as section and fragment names throughout this book.  Without
        # parentheses they are not safely identifiable as equations.  The
        # long equation identifiers have at least three dotted components and
        # an alphabetic final component (for example ``C.4.6.T10``).
        if len(parts) < 3 or not re.search(r"[A-Za-z]", parts[-1]):
            return match.group(0)
        if not equation_map.get(tag):
            return match.group(0)
        prefix = segment[max(0, match.start() - 16):match.start()]
        if re.search(
            r"(?:Section|Fragment|Theorem|Lemma|Proposition|Corollary|Equation)s?\s+$",
            prefix,
            re.IGNORECASE,
        ):
            return match.group(0)
        target = index.resolve_number(
            source, "eq", tag, line_number, allow_cross_kind=False
        )
        if not target:
            return match.group(0)
        rendered = target.get("status") == "defined"
        record_reference(
            references, source, line_number, match.group(0), target,
            "bare-equation-token", rendered=rendered,
        )
        if not rendered:
            return match.group(0)
        return f"[-@{target['id']}]"

    segment = bare_token.sub(token_replacement, segment)

    def raw_replacement(match: re.Match) -> str:
        kind_word, plural, number = reference_parts(match)
        if plural or not plausible_reference_number(kind_word, number):
            return match.group(0)
        kind = map_kind(kind_word)
        if kind == "sec":
            target = index.resolve_scoped_section(
                source, number, line_number,
                prior_context + segment[:match.start()], segment[match.end():],
            )
        else:
            target = index.resolve_number(source, kind, number, line_number)
        if target and target["kind"] != kind:
            kind_name = {
                "thm": "theorem", "lem": "lemma", "prp": "proposition",
                "cor": "corollary", "eq": "equation",
            }.get(kind, "")
            same_local_unit = (
                target["source"] == source
                and index.shared_context_depth(source, line_number, target) >= 2
            )
            named_as_kind = bool(
                kind_name and kind_name in target.get("name", "").lower()
            )
            declared_as_kind = index.section_declares_kind(target, kind)
            if not same_local_unit and not named_as_kind and not declared_as_kind:
                target = None
        if not target:
            unresolved.append({
                "kind": "reference", "source": source, "line": line_number,
                "text": match.group(0), "reason": "number is absent or ambiguous in the book",
            })
            return match.group(0)
        method = "explicit-number" if target["kind"] == kind else "cross-kind-number"
        rendered = target.get("status") == "defined"
        record_reference(
            references, source, line_number, match.group(0), target,
            method, rendered=rendered,
        )
        if not rendered:
            return match.group(0)
        if target["kind"] == "sec" or target["kind"] != kind:
            destination = index.by_path[target["source"]].output + "#" + target["id"]
            return f"[{match.group(0)}]({destination})"
        return "@" + target["id"]

    segment = RAW_REFERENCE_RE.sub(raw_replacement, segment)

    # A parenthesized equation number may be a simple integer (``(3)``) as
    # well as a compound tag (``(H2.3)``).  Replacement is still conservative:
    # it occurs only outside code/math and only when this chapter has exactly
    # one display carrying that tag.
    bare = re.compile(
        r"(?<![A-Za-z0-9_^)}\]])\("
        r"(?P<tag>[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)"
        r"\)(?![A-Za-z0-9])"
    )

    def bare_replacement(match: re.Match) -> str:
        tag = match.group("tag")
        prefix = segment[:match.start()]
        suffix = segment[match.end():]
        # Parentheses inside raw sub/superscripts and the two endpoints of a
        # parenthesized range are mathematical syntax, not independent prose
        # citations.  They remain for the transcription pass.
        if re.search(r"[_^]\{?\s*$", prefix):
            return match.group(0)
        if (
            re.search(r"\)\s*(?:–|—|--)\s*$", prefix)
            or re.match(r"\s*(?:–|—|--)\s*\(", suffix)
        ):
            return match.group(0)
        # A legacy plain-text formula often carries its own number at the end
        # of the line.  Keep that number for the later transcription pass;
        # turning it into a reference to some earlier equation would corrupt
        # the prospective target.
        if any(
            target.get("label_line") == line_number
            for target in equation_map.get(tag, [])
        ):
            return match.group(0)
        if not suffix.strip() and has_legacy_math_signal(prefix):
            return match.group(0)
        statement = index.resolve_statement(source, tag, line_number)
        if statement:
            record_reference(
                references, source, line_number, match.group(0), statement,
                "named-statement", rendered=True,
            )
            destination = index.by_path[source].output + "#" + statement["id"]
            return f"[{match.group(0)}]({destination})"
        if not equation_map.get(tag):
            return match.group(0)
        target = index.resolve_bare_equation(source, tag, line_number, prefix)
        if not target:
            unresolved.append({
                "kind": "reference", "source": source, "line": line_number,
                "text": match.group(0),
                "reason": "parenthesized equation number lacks unique local outline scope",
            })
            return match.group(0)
        rendered = target.get("status") == "defined"
        record_reference(
            references, source, line_number, match.group(0), target,
            "bare-equation-number", rendered=rendered,
        )
        if not rendered:
            return match.group(0)
        return f"([-@{target['id']}])"

    return bare.sub(bare_replacement, segment)


def convert_prose_line(line: str, source: str, line_number: int, index: Index,
                       references: list[dict], citations: list[dict], unresolved: list[dict],
                       inline_math_state: list[bool] | None = None,
                       inline_code_state: list[int] | None = None,
                       prior_context: str = "") -> str:
    line = normalize_inline_math_spacing(line)
    math_state = inline_math_state if inline_math_state is not None else [False]
    code_state = inline_code_state if inline_code_state is not None else [0]
    output: list[str] = []
    plain: list[str] = []

    def flush() -> None:
        if plain:
            prior = (prior_context + "".join(output))[-240:]
            output.append(convert_plain_segment(
                "".join(plain), source, line_number, index, references,
                unresolved, prior_context=prior,
            ))
            plain.clear()

    position = 0
    while position < len(line):
        if code_state[0]:
            delimiter = "`" * code_state[0]
            end = line.find(delimiter, position)
            if end < 0:
                output.append(line[position:])
                break
            output.append(line[position:end + code_state[0]])
            position = end + code_state[0]
            code_state[0] = 0
            continue
        if math_state[0]:
            end = line.find(r"\)", position)
            if end < 0:
                output.append(line[position:])
                break
            output.append(line[position:end])
            output.append("$")
            math_state[0] = False
            position = end + 2
            continue
        if line[position] == "`":
            run = 1
            while position + run < len(line) and line[position + run] == "`":
                run += 1
            flush()
            output.append(line[position:position + run])
            code_state[0] = run
            position += run
            continue
        if line.startswith(r"\(", position):
            flush()
            output.append("$")
            math_state[0] = True
            position += 2
            continue
        if line.startswith(r"\)", position):
            flush()
            output.append("$")
            position += 2
            continue
        link = INTERNAL_LINK_RE.match(line, position)
        if link:
            flush()
            caption, destination = link.group("caption"), link.group("destination")
            converted_caption = normalize_inline_math_spacing(caption)
            converted_caption = converted_caption.replace(r"\(", "$").replace(r"\)", "$")
            parsed = urlsplit(destination.strip().strip("<>"))
            if parsed.scheme in {"http", "https"}:
                citations.append({
                    "source": source, "line": line_number, "text": caption,
                    "destination": destination, "status": "external-link",
                })
                output.append(f"{link.group('image')}[{converted_caption}]({destination})")
            else:
                target = index.resolve_link(source, destination)
                if target:
                    record_reference(
                        references, source, line_number, caption, target,
                        "markdown-link", rendered=True,
                    )
                    output.append(replacement_for_link(converted_caption, target, index))
                else:
                    target_path = index.link_path(source, destination)
                    if target_path in index.by_path:
                        unresolved.append({
                            "kind": "link", "source": source, "line": line_number,
                            "text": link.group(0),
                            "reason": "link points into a book chapter but its fragment did not resolve",
                        })
                    elif target_path:
                        references.append({
                            "source": source,
                            "line": line_number,
                            "text": caption,
                            "destination": destination,
                            "repository_path": target_path,
                            "method": "preserved-local-link",
                        })
                    output.append(f"{link.group('image')}[{converted_caption}]({destination})")
            position = link.end()
            continue
        plain.append(line[position])
        position += 1
    flush()
    return "".join(output)


def transform(document: Document, index: Index, references: list[dict], citations: list[dict],
              unresolved: list[dict]) -> str:
    unresolved.extend(document.math_inventory)
    replacements: dict[int, str] = {}
    after: dict[int, list[str]] = {}
    display_lines: set[int] = set()
    formal_starts = {formal["start"] for formal in document.formals}

    for heading in document.headings:
        line_number = heading["range"]["start"]
        if heading["style"] == "bold":
            if line_number not in formal_starts:
                converted_line = convert_prose_line(
                    document.lines[line_number - 1], document.path, line_number, index,
                    references, citations, unresolved,
                )
                replacements[line_number] = f"[]{{#{heading['id']}}}\n\n" + converted_line
            continue
        line = document.lines[line_number - 1]
        match = HEADING_RE.match(line)
        assert match
        title = re.sub(r"\s*\{#[^}]+\}\s*$", "", match.group("title"))
        title = convert_prose_line(
            title, document.path, line_number, index, references, citations, unresolved
        )
        replacements[line_number] = (
            f"{match.group('marks')} {title} {{#{heading['id']}}}{match.group('newline') or ''}"
        )

    for anchor in document.anchors:
        replacements[anchor["line"]] = anchor["newline"]

    for statement in document.statements:
        line_number = statement["line"]
        body = convert_prose_line(
            statement["body"], document.path, line_number, index,
            references, citations, unresolved,
        )
        replacements[line_number] = (
            f"[]{{#{statement['target']['id']}}}\n\n"
            f"({statement['number']}) {body}{statement['newline']}"
        )

    for display in document.displays:
        start, end = display["start"], display["end"]
        display_lines.update(range(start, end + 1))
        indent = re.match(r"^\s*", document.lines[start - 1]).group(0)
        needs_blank_before = start > 1 and bool(document.lines[start - 2].strip())
        replacements[start] = ("\n" if needs_blank_before else "") + indent + "$$\n"
        payload = "".join(document.lines[start:end - 1])
        tags = balanced_tag_spans(payload)
        payload = remove_spans(payload, tags)
        payload_lines = payload.splitlines(keepends=True)
        for offset, content in enumerate(payload_lines, start + 1):
            replacements[offset] = content
        target = display.get("target")
        closing = indent + "$$" + (f" {{#{target['id']}}}" if target else "") + "\n"
        if display["close_tail"]:
            closing += "\n"
            closing += convert_prose_line(
                display["close_tail"].lstrip() + display["close_newline"],
                document.path,
                end,
                index,
                references,
                citations,
                unresolved,
            )
        elif end == len(document.lines) or document.lines[end].strip():
            closing += "\n"
        replacements[end] = closing
        if len(tags) > 1:
            unresolved.append({
                "kind": "equation", "source": document.path, "line": start,
                "reason": "display contains multiple equation tags",
            })

    for formal in document.formals:
        target = formal["target"]
        section = next(
            (
                heading for heading in document.headings
                if heading["style"] == "bold" and heading["range"]["start"] == formal["start"]
            ),
            None,
        )
        prefix = f"[]{{#{section['id']}}}\n\n" if section else ""
        if formal["kind"] == "proof":
            opening = prefix + f"[]{{#{target['id']}}}\n\n::: {{.proof}}\n"
            if formal["name"]:
                name = convert_prose_line(
                    formal["name"], document.path, formal["start"], index,
                    references, citations, unresolved,
                )
                opening += f"## {name}\n\n"
        else:
            opening = prefix + f"::: {{#{target['id']}}}\n"
            if formal["name"]:
                name = convert_prose_line(
                    formal["name"], document.path, formal["start"], index,
                    references, citations, unresolved,
                )
                opening += f"## {name}\n\n"
        body = formal["body"]
        if body:
            opening += convert_prose_line(
                body + formal["newline"], document.path, formal["start"], index,
                references, citations, unresolved,
            )
        replacements[formal["start"]] = opening
        after.setdefault(formal["end"], []).append("\n:::\n")

    converted: list[str] = []
    inline_math_state = [False]
    inline_code_state = [0]
    paragraph_context = ""
    for line_number, line in enumerate(document.lines, 1):
        if line_number in replacements:
            converted.append(replacements[line_number])
            paragraph_context = ""
        elif document.mask[line_number - 1] or line_number in display_lines:
            converted.append(line)
            paragraph_context = ""
        else:
            converted.append(convert_prose_line(
                line, document.path, line_number, index, references, citations, unresolved,
                inline_math_state, inline_code_state, paragraph_context,
            ))
            if line.strip():
                paragraph_context = (paragraph_context + line)[-240:]
            else:
                paragraph_context = ""
        converted.extend(after.get(line_number, []))
        if after.get(line_number):
            paragraph_context = ""
    if inline_math_state[0]:
        raise ValueError(f"{document.path}: unclosed inline math delimiter")
    if inline_code_state[0]:
        raise ValueError(f"{document.path}: unclosed inline-code delimiter")
    return "".join(converted)


def validate(documents: list[Document], outputs: dict[str, str], index: Index,
             references: list[dict], unresolved: list[dict]) -> dict:
    labels: list[str] = []
    errors: list[str] = []
    for document in documents:
        output = outputs[document.path]
        labels.extend(re.findall(r"\{#([a-z]+-[a-z0-9-]+)\}", output))
        output_lines = output.splitlines(keepends=True)
        if fenced_blocks(document.lines) != fenced_blocks(output_lines):
            errors.append(f"{document.path}: fenced-code blocks changed")
        actual_displays = dollar_displays(output_lines)
        expected_displays = []
        for display in document.displays:
            payload = "".join(document.lines[display["start"]:display["end"] - 1])
            expected_displays.append((
                remove_spans(payload, balanced_tag_spans(payload)),
                display.get("target", {}).get("id"),
            ))
        if actual_displays != expected_displays:
            errors.append(f"{document.path}: display-math payload or label changed")
        masked = fence_mask(output_lines)
        prose = "".join(line if not masked[i] else "\n" for i, line in enumerate(output_lines))
        prose_without_code = mask_inline_code(prose)
        if re.search(r"(?m)^\s*\\[\[\]]\s*$", prose):
            errors.append(f"{document.path}: standalone legacy display delimiter remains")
        if re.search(r"\\[()]", prose_without_code):
            errors.append(f"{document.path}: legacy inline math delimiter remains")
        if balanced_tag_spans(prose):
            errors.append(f"{document.path}: equation tag remains")
        for target in document.targets:
            if target.get("status") == "reserved":
                start, end = target["range"]["start"], target["range"]["end"]
                containing = [
                    record for record in document.math_inventory
                    if record["form"] == target.get("form")
                    and record["line"] <= start <= end
                    <= record.get("end", record["line"])
                ]
                label_line = target.get("label_line", end)
                label_match = pending_label_match(
                    document.lines[label_line - 1].rstrip("\r\n"),
                    target.get("form", ""),
                )
                if len(containing) != 1 or not label_match:
                    errors.append(
                        f"{document.path}: reserved target {target['id']} lacks math inventory"
                    )
                elif label_match.group("tag") != target.get("number"):
                    errors.append(
                        f"{document.path}: reserved target {target['id']} changed number"
                    )
                if output.count("{#" + target["id"] + "}"):
                    errors.append(
                        f"{document.path}: reserved target {target['id']} was defined early"
                    )
                continue
            if output.count("{#" + target["id"] + "}") != 1:
                errors.append(f"{document.path}: target {target['id']} is not defined exactly once")
    duplicates = sorted({label for label in labels if labels.count(label) > 1})
    if duplicates:
        errors.append("duplicate labels: " + ", ".join(duplicates[:10]))
    defined = set(labels)
    referenced: set[str] = set()
    for output in outputs.values():
        referenced.update(re.findall(r"(?<![A-Za-z0-9_-])@([a-z]+-[a-z0-9-]+)", output))
        referenced.update(re.findall(r"\.qmd#([a-z]+-[a-z0-9-]+)", output))
    missing = sorted(referenced.difference(defined))
    if missing:
        errors.append("undefined references: " + ", ".join(missing[:10]))
    for reference in references:
        target_id = reference.get("target")
        if target_id is None:
            continue
        target = index.ids.get(target_id)
        if target is None:
            errors.append(f"reference records absent target {target_id}")
            continue
        expected_rendered = target.get("status") == "defined"
        if reference.get("rendered") != expected_rendered:
            errors.append(
                f"reference to {target_id} has inconsistent rendered status"
            )
    return {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "labels": len(labels),
        "references": len(referenced),
        "unresolved": len(unresolved),
    }


def quarto_config(documents: list[Document]) -> str:
    chapters = "\n".join(f"    - {document.output}" for document in documents)
    return (
        "project:\n  type: book\n\n"
        "book:\n  title: \"PDE: population dynamics of deep learning\"\n"
        "  chapters:\n" + chapters + "\n\n"
        "number-sections: false\n"
        "crossref:\n  chapters: true\n\n"
        "format:\n  html: default\n  pdf: default\n"
    )


def self_test() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        (root / "docs").mkdir()
        (root / "code").mkdir()
        (root / "docs/README.md").write_text(
            "# Guide\n\n[Theory](chapter.md) and [code](../code/README.md).\n",
            encoding="utf-8",
        )
        (root / "docs/chapter.md").write_text("# Theory\n", encoding="utf-8")
        (root / "code/README.md").write_text("# Code guide\n", encoding="utf-8")
        assert discover(root) == ["docs/README.md", "docs/chapter.md"]

    source_a = """# Guide\n\nSee [the result](chapter.md#1-result) and Section 1.\nThe qualified chapter §§C.1–C.2 are also linked.\nSection B.1 of the repeated chapter is qualified.\nThe ambiguous A.1–A.2 remains.\n\nIn *hierarchy*,\nSections G.1 and G.2 are qualified across a line break.\nThe same chapter's\nSection G.1 is qualified by the retained paragraph context.\n"""
    source_b = r"""# Chapter

## 1. Result

\[
x^2=1. \tag{C.1.T1}
\]

**Theorem 1.1 (sample).** The claim uses (C.1.T1).

**Proof.** Immediate.

The bare token C.1.T1 denotes the same display.

\[
y=2. \tag{2}
\]

Use (2), while preserving the raw symbols V^(2) and
C(s)=s+o(s). (R0)

## C.1 First coordinate

## C.2 Second coordinate

The local range C.1–C.2 and symbols §§C.1–C.2 are links.

    z = 3.                  (R1)

    w = 4. (R2)

The pending formulas are (R1) and (R2).
The raw syntax W^{(R2)} and range (R1)–(R2) stay intact.

## A.1 Chapter first

## A.2 Chapter second

(F) Every sample satisfies the named statement.

By (F), the named statement is reusable.

## C.4 Qualified equation parent

\[
r=5. \tag{R5}
\]

\[
r=7. \tag{R7}
\]

The qualified range C.4.R5–R7 uses local equation tags.

## III.V Parent

### III.V.3 First relative child

### III.V.6 Last relative child

Under Section III.V, V.3–V.6 is a relative section range.
""" + "\n"
    source_c = """# Repeated\n\n## A.1 First\n\n## A.2 Second\n\n## A.1 Again\n\nThe locally scoped A.1–A.2 may resolve.\n\n## B.1 Earlier unit\n\nThe remote (F) remains unresolved.\n\nProof. The literal proof marker is converted.\n\n## B.2 Intervening unit\n\nNo symbolic target is defined here.\n\n## C.1 Later unit\n\n    q = 5. (F)\n\n## D.1 Early first\n\n## D.2 Early second\n\n## D.3 Early third\n\nThe same-run D.1–D.2 resolves backward.\n\n## E.1 Separator\n\n## D.1 Later first\n\n## D.2 Later second\n"""
    source_d = """# Hierarchy\n\n## G.1 Canonical first\n\n## G.2 Canonical second\n\n## H.1 Unrelated unit\n\nThe canonical G.1–G.2 resolves at the shallowest unique level.\n\n### G.1 Nested first\n\n### G.2 Nested second\n"""
    source_e = """# Local numbering\n\n## Proof unit A. Local argument\n\n### A.1 First local section\n\n### A.2 Second local section\n\nSection 1 abbreviates A.1 inside proof unit A.\n\n## Z.1 Bold container\n\n**1. First bold unit**\n\n**2. Second bold unit**\n\nThe estimate of §1 applies here.\n\n## 4. Canonical numeric section\n\n### 4. Nested numeric section\n\n## H.1 Unrelated unit\n\nSection 4 chooses the unique shallowest coordinate.\n"""
    docs = [
        Document("docs/README.md", source_a),
        Document("docs/chapter.md", source_b),
        Document("docs/repeated.md", source_c),
        Document("docs/hierarchy.md", source_d),
        Document("docs/local.md", source_e),
    ]
    idx = Index(docs)
    refs: list[dict] = []
    cites: list[dict] = []
    unresolved: list[dict] = []
    outputs = {d.path: transform(d, idx, refs, cites, unresolved) for d in docs}
    checks = validate(docs, outputs, idx, refs, unresolved)
    assert checks["status"] == "pass", checks
    chapter = outputs["docs/chapter.md"]
    guide = outputs["docs/README.md"]
    assert "$$ {#eq-docs-chapter-l5}" in chapter
    assert r"\tag" not in chapter
    assert "::: {#thm-docs-chapter-l9}" in chapter
    assert "::: {.proof}" in chapter
    assert "bare token [-@eq-docs-chapter-l5]" in chapter
    assert "Use ([-@eq-docs-chapter-l15])" in chapter
    assert "V^(2)" in chapter
    assert "C(s)=s+o(s). (R0)" in chapter
    assert "[the result](chapter.qmd#sec-docs-chapter-l3)" in guide
    c1 = idx.number_maps["docs/chapter.md"]["sec"]["C.1"][0]
    c2 = idx.number_maps["docs/chapter.md"]["sec"]["C.2"][0]
    assert f"[C.1](chapter.qmd#{c1['id']})–[C.2](chapter.qmd#{c2['id']})" in chapter
    assert f"§§[C.1](chapter.qmd#{c1['id']})–[C.2](chapter.qmd#{c2['id']})" in chapter
    assert f"chapter §§[C.1](chapter.qmd#{c1['id']})–[C.2](chapter.qmd#{c2['id']})" in guide
    b1 = idx.number_maps["docs/repeated.md"]["sec"]["B.1"][0]
    assert f"[Section B.1](repeated.qmd#{b1['id']}) of the repeated chapter" in guide
    pending = [
        target for target in idx.targets
        if target.get("status") == "reserved"
        and target["source"] == "docs/chapter.md"
    ]
    assert {target["number"] for target in pending} == {"R0", "R1", "R2"}
    assert len({target["id"] for target in pending}) == 3
    assert "z = 3.                  (R1)" in chapter
    assert "w = 4. (R2)" in chapter
    assert "The pending formulas are (R1) and (R2)." in chapter
    assert "W^{(R2)} and range (R1)–(R2) stay intact" in chapter
    for target in pending:
        if target["number"] == "R0":
            continue
        assert any(
            reference.get("target") == target["id"]
            and reference.get("rendered") is False
            for reference in refs
        )
    repeated = outputs["docs/repeated.md"]
    assert "The ambiguous A.1–A.2 remains." in guide
    assert "The remote (F) remains unresolved." in repeated
    assert not any(
        reference.get("source") == "docs/repeated.md"
        and reference.get("text") == "(F)"
        for reference in refs
    )
    assert any(
        record.get("source") == "docs/README.md"
        and record.get("text") == "A.1–A.2"
        and record.get("reason") == "bare section range is absent or repeated in this chapter"
        for record in unresolved
    )
    statement = idx.number_maps["docs/chapter.md"]["stmt"]["F"][0]
    assert f"[]{{#{statement['id']}}}" in chapter
    assert f"[(F)](chapter.qmd#{statement['id']})" in chapter
    r5 = idx.number_maps["docs/chapter.md"]["eq"]["R5"][0]
    r7 = idx.number_maps["docs/chapter.md"]["eq"]["R7"][0]
    assert f"qualified range [-@{r5['id']}]–[-@{r7['id']}]" in chapter
    relative_v3 = idx.number_maps["docs/chapter.md"]["sec"]["III.V.3"][0]
    relative_v6 = idx.number_maps["docs/chapter.md"]["sec"]["III.V.6"][0]
    assert (
        f"[V.3](chapter.qmd#{relative_v3['id']})"
        f"–[V.6](chapter.qmd#{relative_v6['id']}) is a relative section range"
    ) in chapter
    assert "::: {.proof}\nThe literal proof marker is converted." in repeated
    early_d1, later_d1 = idx.number_maps["docs/repeated.md"]["sec"]["D.1"]
    early_d2, later_d2 = idx.number_maps["docs/repeated.md"]["sec"]["D.2"]
    assert early_d1["range"]["start"] < later_d1["range"]["start"]
    assert early_d2["range"]["start"] < later_d2["range"]["start"]
    assert (
        f"same-run [D.1](repeated.qmd#{early_d1['id']})"
        f"–[D.2](repeated.qmd#{early_d2['id']}) resolves backward"
    ) in repeated
    hierarchy = outputs["docs/hierarchy.md"]
    canonical_g1, nested_g1 = idx.number_maps["docs/hierarchy.md"]["sec"]["G.1"]
    canonical_g2, nested_g2 = idx.number_maps["docs/hierarchy.md"]["sec"]["G.2"]
    assert canonical_g1["level"] < nested_g1["level"]
    assert canonical_g2["level"] < nested_g2["level"]
    assert (
        f"canonical [G.1](hierarchy.qmd#{canonical_g1['id']})"
        f"–[G.2](hierarchy.qmd#{canonical_g2['id']}) resolves"
    ) in hierarchy
    assert (
        f"Sections [G.1](hierarchy.qmd#{canonical_g1['id']}) and "
        f"[G.2](hierarchy.qmd#{canonical_g2['id']}) are qualified"
    ) in guide
    assert (
        f"[Section G.1](hierarchy.qmd#{canonical_g1['id']}) is qualified"
    ) in guide
    local = outputs["docs/local.md"]
    local_a1 = idx.number_maps["docs/local.md"]["sec"]["A.1"][0]
    bold_one = next(
        target for target in idx.number_maps["docs/local.md"]["sec"]["1"]
        if target["style"] == "bold"
    )
    canonical_four = min(
        idx.number_maps["docs/local.md"]["sec"]["4"],
        key=lambda target: target["level"],
    )
    assert f"[Section 1](local.qmd#{local_a1['id']}) abbreviates A.1" in local
    assert f"§[1](local.qmd#{bold_one['id']}) applies" in local
    assert (
        f"[Section 4](local.qmd#{canonical_four['id']}) chooses the unique shallowest"
    ) in local
    print("self-test: PASS")


def build(repo: Path, output: Path, state_path: Path) -> dict:
    paths = discover(repo)
    payload = {path: (repo / path).read_bytes() for path in paths}
    documents = [Document(path, payload[path].decode("utf-8")) for path in paths]
    index = Index(documents)
    references: list[dict] = []
    citations: list[dict] = []
    unresolved: list[dict] = []
    outputs = {
        document.path: transform(document, index, references, citations, unresolved)
        for document in documents
    }
    checks = validate(documents, outputs, index, references, unresolved)
    output_by_source = {
        document.path: output / document.output for document in documents
    }
    for reference in references:
        if reference.get("method") != "preserved-local-link":
            continue
        repository_target = (repo / reference["repository_path"]).resolve()
        parsed = urlsplit(reference["destination"].strip().strip("<>"))
        generated_target = (
            output_by_source[reference["source"]].parent / unquote(parsed.path)
        ).resolve()
        if not repository_target.is_file():
            checks["errors"].append(
                f"missing repository link target: {reference['source']}:{reference['line']} "
                f"-> {reference['destination']}"
            )
        elif generated_target != repository_target:
            checks["errors"].append(
                f"generated relative link changes destination: "
                f"{reference['source']}:{reference['line']} -> {reference['destination']}"
            )
    if checks["errors"]:
        checks["status"] = "fail"
    if checks["status"] != "pass":
        raise RuntimeError("; ".join(checks["errors"]))
    if any((repo / path).read_bytes() != data for path, data in payload.items()):
        raise RuntimeError("book sources changed during migration; retry")

    output.mkdir(parents=True, exist_ok=True)
    for document in documents:
        atomic_write(output / document.output, outputs[document.path].encode("utf-8"))
    atomic_write(output / "_quarto.yml", quarto_config(documents).encode("utf-8"))

    state = {
        "schema": 1,
        "source": [
            {"path": path, "sha256": sha256(payload[path]), "lines": len(payload[path].splitlines())}
            for path in paths
        ],
        "targets": index.targets,
        "references": references,
        "citations": citations,
        "chapters": [
            {
                "source": document.path,
                "output": document.output,
                "sha256": sha256(outputs[document.path].encode("utf-8")),
                "status": "generated",
            }
            for document in documents
        ],
        "unresolved": unresolved,
        "checks": checks,
    }
    atomic_write(state_path, (json.dumps(state, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return state


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("self-test")
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    build_parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    build_parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    args = parser.parse_args(argv)
    if args.command == "self-test":
        self_test()
        return 0
    state = build(args.repo.resolve(), args.output.resolve(), args.state.resolve())
    target_status = {
        status: sum(target.get("status") == status for target in state["targets"])
        for status in ("defined", "reserved")
    }
    reference_status = {
        "rendered": sum(reference.get("rendered") is True for reference in state["references"]),
        "reserved": sum(
            reference.get("target_status") == "reserved"
            for reference in state["references"]
        ),
        "preserved_local": sum(
            reference.get("method") == "preserved-local-link"
            for reference in state["references"]
        ),
    }
    unresolved_status = {
        kind: sum(record.get("kind") == kind for record in state["unresolved"])
        for kind in ("math", "reference", "link", "equation")
    }
    print(json.dumps({
        "chapters": len(state["chapters"]),
        "targets": target_status,
        "references": reference_status,
        "citations": len(state["citations"]),
        "unresolved": unresolved_status,
        "checks": state["checks"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
