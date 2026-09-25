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
DEFAULT_DECISIONS = HERE / "migration_decisions.json"
PRINT_FILTER = HERE / "pdf_breakable_tables.lua"
DEFAULT_MATH_BATCH_DIR = (
    DEFAULT_REPO / "data/generated/quarto_capability_pilot_20260921/math-transcription01"
)

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
        line_start = text.rfind("\n", 0, start) + 1
        next_newline = text.find("\n", end)
        line_end = len(text) if next_newline < 0 else next_newline
        # A tag on its own line is structural metadata, including that line's
        # newline.  Leaving an empty line inside ``$$ ... $$`` makes Pandoc
        # parse both delimiters as ordinary text instead of display math.
        if (
            not text[line_start:start].strip()
            and not text[end:line_end].strip()
        ):
            removal_end = line_end if next_newline < 0 else line_end + 1
            text = text[:line_start] + text[removal_end:]
            continue
        left = start
        if left and text[left - 1] == " " and (end == len(text) or text[end : end + 1] in {"", "\n"}):
            left -= 1
        text = text[:left] + text[end:]
    return text


def normalize_display_layout(payload: str) -> str:
    """Use an amsmath environment valid in numbered and unnumbered displays."""
    pattern = re.compile(r"\\begin\{split\}(?P<body>.*?)\\end\{split\}", re.DOTALL)
    return pattern.sub(
        lambda match: r"\begin{aligned}" + match.group("body") + r"\end{aligned}",
        payload,
    )


SCRIPT_ATOM = r"(?:\\[A-Za-z]+|[A-Za-z])"
SCRIPT_VALUE = r"(?:\{[^{}]*\}|\\[A-Za-z]+|[A-Za-z0-9])"
REPEATED_SUPERSCRIPT_RE = re.compile(
    SCRIPT_ATOM + r"\^" + SCRIPT_VALUE + r"(?:_" + SCRIPT_VALUE + r")?\^" + SCRIPT_VALUE
)
REPEATED_SUBSCRIPT_RE = re.compile(
    SCRIPT_ATOM + r"_" + SCRIPT_VALUE + r"(?:\^" + SCRIPT_VALUE + r")?_" + SCRIPT_VALUE
)
TRANSPOSE_AFTER_SUPERSCRIPT_RE = re.compile(
    r"(?P<atom>" + SCRIPT_ATOM + r"\^" + SCRIPT_VALUE
    + r"(?:_" + SCRIPT_VALUE + r")?)\^(?:T|\{T\})"
)


def normalize_math_atom_layout(payload: str) -> str:
    """Group an already-scripted atom before applying a transpose."""
    payload = re.sub(
        r"\\rm\s+([A-Za-z][A-Za-z0-9]*)",
        lambda match: r"\mathrm{" + match.group(1) + "}",
        payload,
    )
    payload = payload.replace(r"\backslash", r"\smallsetminus")
    payload = payload.replace(r"\setminus", r"\smallsetminus")
    return TRANSPOSE_AFTER_SUPERSCRIPT_RE.sub(
        lambda match: "{" + match.group("atom") + r"}^{\top}", payload
    )


INLINE_DOLLAR_RE = re.compile(r"(?<!\\)(?<!\$)\$(?!\$)(?P<body>[^$\r\n]*)\$(?!\$)")


def normalize_inline_dollar_boundaries(text: str) -> str:
    return INLINE_DOLLAR_RE.sub(
        lambda match: "$"
        + normalize_math_atom_layout(match.group("body").strip())
        + "$",
        text,
    )


def separate_markdown_headings(text: str) -> str:
    """Ensure every ATX heading starts a Markdown block outside fenced code."""
    lines = text.splitlines(keepends=True)
    masked = fence_mask(lines)
    output: list[str] = []
    for index, line in enumerate(lines):
        if not masked[index] and HEADING_RE.match(line) and output and output[-1].strip():
            output.append("\n")
        output.append(line)
    return "".join(output)


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
        self.reference_overrides: dict[tuple[str, int], list[dict]] = {}
        self.reference_override_uses: dict[int, int] = {}
        self.bibliography_by_link: dict[tuple[str, int, str], dict] = {}
        self.bibliography_uses: dict[str, int] = {}

    def configure_reference_overrides(self, overrides: list[dict]) -> None:
        """Validate the small set of references whose old text is ambiguous."""
        seen: set[tuple[str, int, str]] = set()
        for number, override in enumerate(overrides, 1):
            if not isinstance(override, dict):
                raise ValueError(f"reference override {number}: malformed record")
            source = override.get("source")
            line = override.get("line")
            old_text = override.get("text")
            target_ids = override.get("targets")
            style = override.get("style", "single")
            if (
                source not in self.by_path
                or not isinstance(line, int)
                or not 1 <= line <= len(self.by_path[source].lines)
                or not isinstance(old_text, str)
                or not old_text
                or not isinstance(target_ids, list)
                or not target_ids
                or len(set(target_ids)) != len(target_ids)
                or style not in {"single", "range"}
            ):
                raise ValueError(f"reference override {number}: invalid fields")
            key = (source, line, old_text)
            if key in seen:
                raise ValueError(f"reference override {number}: duplicate source reference")
            seen.add(key)
            source_line = self.by_path[source].lines[line - 1]
            if source_line.count(old_text) != 1:
                raise ValueError(
                    f"reference override {number}: source text is not unique on its line"
                )
            try:
                targets = [self.ids[target_id] for target_id in target_ids]
            except KeyError as error:
                raise ValueError(
                    f"reference override {number}: unknown target {error.args[0]}"
                ) from error
            if any(target.get("status") != "defined" for target in targets):
                raise ValueError(f"reference override {number}: target is not defined")
            if style == "single" and len(targets) != 1:
                raise ValueError(f"reference override {number}: single style needs one target")
            if style == "range" and len(targets) != 2:
                raise ValueError(f"reference override {number}: range style needs two targets")
            record = {
                "number": number,
                "source": source,
                "line": line,
                "text": old_text,
                "style": style,
                "targets": targets,
            }
            self.reference_overrides.setdefault((source, line), []).append(record)
            self.reference_override_uses[number] = 0

    def protect_reference_overrides(
        self, segment: str, source: str, line_number: int,
        references: list[dict],
    ) -> tuple[str, dict[str, str]]:
        """Temporarily protect reviewed links from the generic resolver."""
        restored: dict[str, str] = {}
        for override in self.reference_overrides.get((source, line_number), []):
            old_text = override["text"]
            if old_text not in segment:
                continue
            target_values = override["targets"]
            if override["style"] == "single":
                target = target_values[0]
                if target["kind"] == "eq":
                    replacement = f"([-@{target['id']}])"
                else:
                    destination = self.by_path[target["source"]].output + "#" + target["id"]
                    replacement = f"[{old_text}]({destination})"
                record_reference(
                    references, source, line_number, old_text, target,
                    "reviewed-reference", rendered=True,
                )
            else:
                match = re.fullmatch(
                    r"(?P<prefix>.*?)(?P<open1>\()?"
                    r"(?P<first>[A-Za-z0-9.]+)(?P<close1>\))?"
                    r"(?P<dash>\s*(?:–|—|--)\s*)"
                    r"(?P<open2>\()?(?P<last>[A-Za-z0-9.]+)"
                    r"(?P<close2>\))?",
                    old_text,
                )
                delimiters = (
                    bool(match and match.group("open1")),
                    bool(match and match.group("close1")),
                    bool(match and match.group("open2")),
                    bool(match and match.group("close2")),
                )
                if not match or delimiters not in {
                    (False, False, False, False),
                    (True, True, True, True),
                }:
                    raise ValueError(
                        f"{source}:{line_number}: malformed reviewed reference range"
                    )
                linked: list[str] = []
                for written, target in zip(
                    (match.group("first"), match.group("last")), target_values
                ):
                    if target["kind"] == "eq":
                        linked.append(f"([-@{target['id']}])")
                    else:
                        destination = (
                            self.by_path[target["source"]].output + "#" + target["id"]
                        )
                        linked.append(f"[{written}]({destination})")
                    record_reference(
                        references, source, line_number, written, target,
                        "reviewed-reference-range", rendered=True,
                    )
                replacement = (
                    match.group("prefix") + linked[0] + match.group("dash") + linked[1]
                )
            placeholder = f"\ue000reviewed-reference-{override['number']}\ue001"
            segment = segment.replace(old_text, placeholder, 1)
            restored[placeholder] = replacement
            self.reference_override_uses[override["number"]] += 1
        return segment, restored

    def verify_reference_overrides(self) -> None:
        invalid = {
            number: uses
            for number, uses in self.reference_override_uses.items()
            if uses != 1
        }
        if invalid:
            raise ValueError(f"reviewed references were not applied exactly once: {invalid}")

    def configure_bibliography(self, entries: list[dict]) -> None:
        """Validate exact paper-link citations and their BibTeX records."""
        keys: set[str] = set()
        for number, entry in enumerate(entries, 1):
            if not isinstance(entry, dict):
                raise ValueError(f"bibliography entry {number}: malformed record")
            source = entry.get("source")
            line = entry.get("line")
            destination = entry.get("destination")
            key = entry.get("key")
            bibtex = entry.get("bibtex")
            if (
                source not in self.by_path
                or not isinstance(line, int)
                or not 1 <= line <= len(self.by_path[source].lines)
                or not isinstance(destination, str)
                or not destination.startswith(("https://", "http://"))
                or not isinstance(key, str)
                or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_:-]*", key)
                or not isinstance(bibtex, str)
                or not re.match(rf"\s*@\w+\s*\{{{re.escape(key)}\s*,", bibtex)
            ):
                raise ValueError(f"bibliography entry {number}: invalid fields")
            lookup = (source, line, destination)
            if lookup in self.bibliography_by_link or key in keys:
                raise ValueError(f"bibliography entry {number}: duplicate link or key")
            if self.by_path[source].lines[line - 1].count(destination) != 1:
                raise ValueError(
                    f"bibliography entry {number}: link is not unique on its source line"
                )
            keys.add(key)
            self.bibliography_by_link[lookup] = entry
            self.bibliography_uses[key] = 0

    def cite_external_link(self, source: str, line: int, destination: str) -> str | None:
        entry = self.bibliography_by_link.get((source, line, destination))
        if entry is None:
            return None
        self.bibliography_uses[entry["key"]] += 1
        return entry["key"]

    def verify_bibliography(self) -> None:
        invalid = {key: uses for key, uses in self.bibliography_uses.items() if uses != 1}
        if invalid:
            raise ValueError(f"bibliography links were not cited exactly once: {invalid}")

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
        candidates = self.equation_reference_candidates(source, number)
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
                    target for target in candidates
                    if target["source"] == source
                    if parent["id"] in self.by_path[source].context_at(
                        target["range"]["start"]
                    )
                ]
                if len(scoped) == 1:
                    return scoped[0]
        local_exact = self.number_maps[source]["eq"].get(number, [])
        is_compound = bool(
            "." in number or "-" in number
            or re.search(r"[A-Za-z]", number) and re.search(r"\d", number)
        )
        if is_compound and local_exact:
            direct = self.resolve_number(
                source, "eq", number, line_number, allow_cross_kind=False
            )
            if direct:
                return direct
        matches = [target for target in candidates if target["source"] == source]
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
        # A fully qualified tag that occurs exactly once in another chapter
        # is a stable book-level coordinate.  Short suffixes never cross a
        # chapter boundary through this rule.
        if "." in number and len(candidates) == 1:
            return candidates[0]
        return None

    def equation_reference_candidates(self, source: str,
                                      number: str) -> list[dict]:
        """Return exact or locally abbreviated equation targets.

        A proof unit may define ``H40.E21`` and cite it locally as ``(E21)``.
        Exact local tags take precedence; otherwise suffix matches remain
        local and are disambiguated by outline context.  Only a fully
        qualified, globally unique exact tag may cross chapter boundaries.
        """
        exact = self.number_maps[source]["eq"].get(number, [])
        if exact:
            return exact
        suffix = "." + number
        local: dict[str, dict] = {}
        for targets in self.number_maps[source]["eq"].values():
            for target in targets:
                if target.get("number", "").endswith(suffix):
                    local[target["id"]] = target
        if local:
            return list(local.values())
        if "." in number:
            return self.global_numbers["eq"].get(number, [])
        return []


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
    start_column = 0
    content: list[str] = []
    for line_number, line in enumerate(document.lines, 1):
        if document.mask[line_number - 1]:
            continue
        if line_number in display_lines:
            closing = DISPLAY_CLOSE_RE.match(line)
            if not closing or not closing.group("tail").strip():
                continue
            tail_start = closing.start("tail")
            line = " " * tail_start + line[tail_start:]
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
                        "column": start_column,
                        "end_column": found + delimiter_length,
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
            start_column = found
            content = []
            position = found + delimiter_length
    if delimiter_length:
        raise ValueError(f"{document.path}: unclosed inline-code delimiter")
    return records


LEGACY_BLOCK_MATH_SIGNAL_PATTERN = (
    r"<=|>=|->|=>|(?<![=!<>])=(?!=)|\|\||"
    r"[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9({]|"
    r"(?<=[A-Za-z0-9)}])\^(?=[A-Za-z0-9({-])|"
    r"\b(?:sqrt|sum|prod|integral|exp|log)\s*[_({]|[≤≥∞∑√⊗]"
)
LEGACY_BLOCK_MATH_SIGNAL_RE = re.compile(
    rf"(?:{LEGACY_BLOCK_MATH_SIGNAL_PATTERN})"
)

ASCII_MATH_ATOM_PATTERN = (
    r"(?:[A-Za-z](?:[0-9]+)?|"
    r"(?:alpha|beta|gamma|delta|epsilon|varepsilon|eta|theta|lambda|rho|"
    r"sigma|tau|phi|psi|xi|zeta|omega|ell|pi|infinity|Delta|Gamma|Phi|Pi|Theta|"
    r"Lambda|Omega)(?:[0-9]+)?|[0-9]+(?:[.][0-9]+)?)(?:')?"
)
ASCII_MATH_FUNCTION_PATTERN = (
    r"(?:[A-Za-z]|O|N|E|P|Var|Cov|Law|diag|atan|arctan|tanh|sin|cos|"
    r"exp|log|sqrt|H1|L2|Phi|Theta|Psi|phi|psi|beta|omega|lambda|"
    r"epsilon|varepsilon)"
)
ASCII_MATH_COMPARAND_PATTERN = (
    rf"(?:\|?{ASCII_MATH_ATOM_PATTERN}\|?|"
    rf"{ASCII_MATH_FUNCTION_PATTERN}(?:'{{1,3}})?\([^()\n]{{1,40}}\))"
)
ASCII_MATH_SIGNAL_PATTERN = (
    rf"(?<![A-Za-z0-9_])\({ASCII_MATH_ATOM_PATTERN}"
    rf"(?:\s*,\s*{ASCII_MATH_ATOM_PATTERN})+\)(?![A-Za-z0-9_])|"
    rf"(?<![A-Za-z0-9_])\[{ASCII_MATH_ATOM_PATTERN}"
    rf"(?:\s*,\s*{ASCII_MATH_ATOM_PATTERN})+\](?![A-Za-z0-9_])|"
    rf"(?<![A-Za-z0-9_])(?:{ASCII_MATH_ATOM_PATTERN}"
    rf"(?:\s*[+*/]\s*{ASCII_MATH_ATOM_PATTERN})+|"
    rf"{ASCII_MATH_ATOM_PATTERN}\s*-\s*{ASCII_MATH_ATOM_PATTERN})"
    rf"(?![A-Za-z0-9_])|"
    rf"(?<![A-Za-z0-9_]){ASCII_MATH_COMPARAND_PATTERN}\s*[<>]\s*"
    rf"{ASCII_MATH_COMPARAND_PATTERN}(?![A-Za-z0-9_])|"
    rf"(?<![A-Za-z0-9_]){ASCII_MATH_FUNCTION_PATTERN}(?:'{{1,3}})?"
    r"\([^()\n]{1,60}\)(?![A-Za-z0-9_])"
)

LEGACY_MATH_SIGNAL_RE = re.compile(
    rf"(?:{LEGACY_BLOCK_MATH_SIGNAL_PATTERN}|"
    r"[≤≥∞∑√⊗∈∉∋→↦⊥⊂⊆⊃⊇∂∇∀∃∧∨≠≈≡∝±∓·⋅∘×÷∫]|"
    r"[Α-Ωα-ωϕϑℓ]|"
    r"(?:[A-Za-zΑ-Ωα-ω][₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ]|"
    r"[A-Za-zΑ-Ωα-ω0-9][⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ᵀ])|"
    r"(?<!\\)\\[A-Za-z]+|"
    r"\b(?:L2|W1|W2|S1|C1)\b(?![.][0-9])|"
    r"\b(?:max|min|dist|span|rank|tr|det|argmax|argmin)\b\s*\(|"
    r"\bker\b\s+[A-Za-zΑ-Ωα-ω](?![A-Za-zΑ-Ωα-ω])|"
    rf"{ASCII_MATH_SIGNAL_PATTERN}|"
    r"\b(?:alpha|beta|gamma|delta|epsilon|varepsilon|eta|theta|lambda|rho|"
    r"sigma|tau|phi|psi|xi|zeta|pi|omega|chi|ell|Gamma|Delta|Phi|Pi|Theta|"
    r"Lambda|Omega)\b(?:'{1,3})?|"
    r"\b(?:Rtop|Ltop|Utop|Rbottom|Lbottom|Ubottom)\b)"
)


ASCII_SIGNAL_EXCLUSION_RE = re.compile(
    r"(?:C-H\d+|[A-Z]-[A-Z]\d*|[A-Z][0-9]+/[A-Z][0-9]+|"
    r"[A-Z]/[A-Z]|[0-9]+-[0-9]+)"
)


def legacy_math_signal_search(text: str) -> re.Match | None:
    for match in LEGACY_MATH_SIGNAL_RE.finditer(text):
        if ASCII_SIGNAL_EXCLUSION_RE.fullmatch(match.group(0)):
            continue
        if match.group(0) == "L2":
            before = text[max(0, match.start() - 48):match.start()]
            after = text[match.end():match.end() + 48]
            # ``L2`` is overloaded in the source: usually it denotes the
            # Hilbert space, but in a few fixed fragments it is a named layer
            # or resolvent.  These syntactic contexts uniquely identify the
            # latter and must remain ordinary identifiers.
            if (
                re.match(r"(?:-I|b\b|\s*=)", after)
                or before.endswith("|") and after.startswith("|")
                or re.search(r"(?:R\d|L\d|Rtop|Ltop)(?:\s*,\s*[A-Za-z0-9]+)*\s*,\s*$", before)
                or re.search(r"\bF\s+$", before)
                or re.match(
                    r"\s+arctangent\b|\s+natural-gate\b|\s+at\b|"
                    r"\s+on the nonlinear box\b|\s+assume\b",
                    after,
                )
            ):
                continue
        return match
    return None


def has_legacy_math_signal(text: str) -> bool:
    text = re.sub(r"!?\[[^\]]*\]\([^)]+\)", "", text)
    return legacy_math_signal_search(text) is not None


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
        if document.mask[line_number - 1]:
            residual.append("")
            continue
        if line_number in display_lines:
            closing = DISPLAY_CLOSE_RE.match(line)
            if not closing or not closing.group("tail").strip():
                residual.append("")
                continue
            # A display may close before prose on the same physical source
            # line.  Mask the delimiter but inventory that prose normally;
            # otherwise raw mathematics in the tail silently bypasses the
            # exact-span transcription pass.
            tail_start = closing.start("tail")
            line = " " * tail_start + line[tail_start:]
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
            # Indentation alone can also mean a prose continuation.  Preserve
            # the older conservative block classifier; the broader Unicode
            # detector below inventories newly exposed notation line by line.
            if LEGACY_BLOCK_MATH_SIGNAL_RE.search("".join(block_residual)):
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


MATH_FORM_CODE = {
    "inline-code": "inline",
    "indented-display": "display",
    "plain-line": "plain",
}


def indexed_math_records(documents: list[Document]) -> list[dict]:
    """Return the frozen math inventory with stable source-coordinate IDs."""
    records: list[dict] = []
    counters: dict[tuple[str, str, int], int] = {}
    for document in documents:
        for original in document.math_inventory:
            record = dict(original)
            key = (
                document.path,
                record["form"],
                record["line"],
            )
            counters[key] = counters.get(key, 0) + 1
            record["id"] = (
                f"math-{document.key}-l{record['line']}-"
                f"{MATH_FORM_CODE[record['form']]}-{counters[key]}"
            )
            records.append(record)
    if len({record["id"] for record in records}) != len(records):
        raise ValueError("duplicate mathematical-transcription ID")
    return records


def record_reserved_targets(document: Document, record: dict) -> list[dict]:
    return sorted(
        [
            target for target in document.pending_equations
            if record["form"] == target.get("form")
            and record["line"] <= target["range"]["start"]
            <= target["range"]["end"] <= record.get("end", record["line"])
        ],
        key=lambda target: target["range"]["start"],
    )


def display_parts(document: Document, record: dict) -> list[dict]:
    """Partition an indented block at reserved equation boundaries."""
    targets = record_reserved_targets(document, record)
    intervals: list[tuple[int, int, dict | None]] = []
    cursor = record["line"]
    for target in targets:
        start, end = target["range"]["start"], target["range"]["end"]
        if cursor < start:
            intervals.append((cursor, start - 1, None))
        intervals.append((start, end, target))
        cursor = end + 1
    if cursor <= record.get("end", record["line"]):
        intervals.append((cursor, record.get("end", record["line"]), None))
    if not intervals:
        intervals.append((record["line"], record.get("end", record["line"]), None))

    parts: list[dict] = []
    for start, end, target in intervals:
        text = "".join(document.lines[start - 1:end]).rstrip("\r\n")
        if not text.strip():
            continue
        parts.append({
            "part_id": len(parts) + 1,
            "line": start,
            "end": end,
            "text": text,
            "target_id": target["id"] if target else None,
            "legacy_number": target.get("number") if target else None,
        })
    if not parts:
        raise ValueError(f"{record['id']}: empty display partition")
    return parts


def compact_source_context(document: Document, record: dict) -> dict:
    start, end = record["line"], record.get("end", record["line"])
    before = "".join(document.lines[max(0, start - 3):start - 1])[-320:]
    after = "".join(document.lines[end:min(len(document.lines), end + 2)])[:320]
    container = "".join(document.lines[start - 1:end]).rstrip("\r\n")
    if len(container) > 1000 and record["form"] == "inline-code":
        needle = record["text"]
        position = container.find(needle)
        left = max(0, position - 400)
        right = min(len(container), position + len(needle) + 400)
        container = container[left:right]
    headings = {heading["id"]: heading for heading in document.headings}
    section = [
        headings[target_id]["name"]
        for target_id in document.context_at(start)
        if target_id in headings
    ]
    return {
        "section": section,
        "before": before,
        "container": container,
        "after": after,
    }


def paragraph_context(document: Document, record: dict) -> tuple[tuple, dict]:
    """Share one bounded local paragraph among nearby batch items."""
    start, end = record["line"], record.get("end", record["line"])
    paragraph_start = start
    while paragraph_start > 1 and document.lines[paragraph_start - 2].strip():
        paragraph_start -= 1
    paragraph_end = end
    while paragraph_end < len(document.lines) and document.lines[paragraph_end].strip():
        paragraph_end += 1
    text = "".join(document.lines[paragraph_start - 1:paragraph_end]).rstrip("\r\n")
    bounded = len(text) > 700
    if bounded:
        paragraph_start = max(1, start - 1)
        paragraph_end = min(len(document.lines), end + 1)
        before = document.lines[paragraph_start - 1][-180:] if paragraph_start < start else ""
        after = document.lines[paragraph_end - 1][:180] if paragraph_end > end else ""
        if record["form"] == "inline-code":
            current = "".join(document.lines[start - 1:end]).rstrip("\r\n")
            position = current.find(record["text"])
            current = current[
                max(0, position - 220):min(len(current), position + len(record["text"]) + 220)
            ]
        else:
            current = "<candidate text supplied separately>"
        text = before + current + after
    if len(text) > 280:
        position = text.find(record["text"])
        if position >= 0:
            left = max(0, position - 100)
            right = min(len(text), position + len(record["text"]) + 100)
            text = text[left:right]
        else:
            text = text[:140] + " … " + text[-140:]
    headings = {heading["id"]: heading for heading in document.headings}
    section = [
        headings[target_id]["name"]
        for target_id in document.context_at(start)
        if target_id in headings
    ]
    key = (
        document.path,
        paragraph_start,
        paragraph_end,
        start if bounded else 0,
        end if bounded else 0,
    )
    return key, {
        "source": document.path,
        "line": paragraph_start,
        "end": paragraph_end,
        "section": section,
        "text": text,
    }


def json_schema_for_math_batch(kind: str, item_count: int) -> dict:
    base_item = {
        "type": "object",
        "additionalProperties": False,
    }
    if kind == "inline":
        base_item |= {
            "required": ["id", "latex"],
            "properties": {
                "id": {"type": "integer"},
                "latex": {"type": "string"},
            },
        }
    elif kind == "display":
        base_item |= {
            "required": ["id", "parts"],
            "properties": {
                "id": {"type": "integer"},
                "parts": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["part_id", "latex"],
                        "properties": {
                            "part_id": {"type": "integer"},
                            "latex": {"type": "string"},
                        },
                    },
                },
            },
        }
    elif kind == "plain":
        base_item |= {
            "required": ["id", "mode", "latex", "spans"],
            "properties": {
                "id": {"type": "integer"},
                "mode": {"type": "string", "enum": ["mixed", "display"]},
                "latex": {"type": "string"},
                "spans": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["source", "latex"],
                        "properties": {
                            "source": {"type": "string"},
                            "latex": {"type": "string"},
                        },
                    },
                },
            },
        }
    else:
        raise ValueError(f"unknown math batch kind {kind}")
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["batch", "items"],
        "properties": {
            "batch": {"type": "string"},
            "items": {
                "type": "array",
                "minItems": item_count,
                "maxItems": item_count,
                "items": base_item,
            },
        },
    }


MATH_BATCH_PROMPTS = {
    "inline": """Convert every item from exact legacy code-form mathematics to a faithful LaTeX payload. Use context only to identify notation. Preserve every operator, index, delimiter, constant, norm, derivative, quantifier, and distinction; do not simplify or repair the mathematics. Expand pseudo-LaTeX such as mathcal, Greek names, _(...), ^(...), sqrt, sum, tensor, and inequalities into standard LaTeX. Return one output item for every numeric id in the same order. Return payloads only: no $, \\(, \\[ , labels, tags, Markdown, prose, or commentary. Preserve the number of newline characters in each multiline input. Do not use tools. The required JSON schema is enforced.\n\nINPUT BATCH:\n""",
    "display": """Convert every exact legacy indented formula part to a faithful LaTeX display payload. Use context only to identify notation. Preserve every equation, operator, index, delimiter, constant, norm, derivative, quantifier, and line relation; do not simplify or repair the mathematics. Use aligned, gathered, cases, or text commands inside the payload when required. A non-null equation_number is metadata: omit that printed number from the LaTeX because the program attaches its target automatically. Return every numeric item id and every part_id once, in the supplied order. Return payloads only: no outer $, \\[, labels, tags, Markdown, explanations, or commentary. Do not use tools. The required JSON schema is enforced.\n\nINPUT BATCH:\n""",
    "plain": """Transcribe all mathematics in every exact source line while preserving its prose byte-for-byte outside the selected math. Context is explanatory only and must never be returned. For a line with a non-null reserved_equation_number, use mode display, put the complete formula in latex, omit the legacy terminal number, and leave spans empty. Otherwise use mode mixed with latex empty and return ordered, nonoverlapping spans: each source value must be an exact nonempty substring of the supplied text, and each latex value is only its faithful LaTeX replacement. Use mode display only when the entire unlabelled line is mathematical and contains no prose. Protected inline-code spans are handled by another batch: do not include or overlap them. Capture every raw mathematical expression, preserving all operators, indices, constants, norms, derivatives, quantifiers, and grouping; do not simplify or repair the mathematics. Return one item for every numeric id in the same order. No $, \\(, \\[, labels, tags, Markdown, explanations, or commentary. Do not use tools. The required JSON schema is enforced.\n\nINPUT BATCH:\n""",
}


PLAIN_SIGNAL_RE = LEGACY_MATH_SIGNAL_RE

PLAIN_SYNTAX_MASKS = [
    re.compile(r"`+[^`]*`+"),
    re.compile(r"\\\(.*?\\\)"),
    # Only mask a genuinely unclosed legacy inline-math span.  The earlier
    # broad expression also matched a closed ``\(...\)`` and consequently
    # hid every later token on that physical line from residual validation.
    re.compile(r"\\\((?:(?!\\\))[^\r\n])*$"),
    re.compile(r"\$[^$]*\$"),
    re.compile(r"!?\[[^\]]*\]\([^)]+\)"),
    re.compile(r"<[^>]+>"),
    # Prose such as "the explicit integral (C.4.7.N32)" is a reference,
    # not an untypeset integral expression.
    re.compile(r"\b(?:sum|product|integral)\s+\([A-Z0-9][A-Za-z0-9.]*\)"),
]

GREEK_PSEUDO_NAMES = {
    "alpha": r"\alpha", "beta": r"\beta", "gamma": r"\gamma",
    "delta": r"\delta", "epsilon": r"\epsilon", "eta": r"\eta",
    "theta": r"\theta", "lambda": r"\lambda", "rho": r"\rho",
    "sigma": r"\sigma", "tau": r"\tau", "phi": r"\phi",
    "psi": r"\psi", "xi": r"\xi", "zeta": r"\zeta", "pi": r"\pi",
    "omega": r"\omega", "Gamma": r"\Gamma", "Delta": r"\Delta",
    "Phi": r"\Phi", "Pi": r"\Pi", "Theta": r"\Theta",
    "Lambda": r"\Lambda", "Omega": r"\Omega",
    "Rtop": r"R_{\mathrm{top}}", "Ltop": r"L_{\mathrm{top}}",
    "Utop": r"U_{\mathrm{top}}",
    "Rbottom": r"R_{\mathrm{bottom}}", "Lbottom": r"L_{\mathrm{bottom}}",
    "Ubottom": r"U_{\mathrm{bottom}}",
}


def mask_plain_syntax(text: str, occupied: list[tuple[int, int]]) -> str:
    masked = list(text)
    intervals = list(occupied)
    for pattern in PLAIN_SYNTAX_MASKS:
        for match in pattern.finditer(text):
            intervals.append((match.start(), match.end()))
    # A single-dollar delimiter uses the same token to open and close.  Mask
    # complete pairs above, and protect a final unpaired opening delimiter
    # without mistaking the closing delimiter of ``$...$`` for another open.
    single_dollars = [
        match.start()
        for match in re.finditer(r"(?<![\\$])\$(?!\$)", text)
    ]
    if len(single_dollars) % 2:
        intervals.append((single_dollars[-1], len(text)))
    for left, right in intervals:
        masked[left:right] = " " * (right - left)
    return "".join(masked)


def legacy_fragment_to_latex(source: str) -> str:
    """Lexically normalize one already-delimited pseudo-math token."""
    text = source
    text = text.replace("<=", r"\le ").replace(">=", r"\ge ")
    text = text.replace("->", r"\to ").replace("=>", r"\Rightarrow ")
    text = text.replace("≤", r"\le ").replace("≥", r"\ge ")
    text = text.replace("∞", r"\infty ").replace("∑", r"\sum ")
    text = text.replace("√", r"\sqrt ").replace("⊗", r"\otimes ")
    text = text.replace("×", r"\times ")
    superscripts = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ᵀ", "0123456789+-T")
    subscripts = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
    text = re.sub(
        r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ᵀ]+",
        lambda match: "^{" + match.group(0).translate(superscripts).replace("T", r"\top") + "}",
        text,
    )
    text = re.sub(
        r"[₀₁₂₃₄₅₆₇₈₉]+",
        lambda match: "_{" + match.group(0).translate(subscripts) + "}",
        text,
    )
    text = re.sub(r"\bsqrt\(([^()]*)\)", r"\\sqrt{\1}", text)
    text = re.sub(r"\bexp\(", r"\\exp(", text)
    text = re.sub(r"\blog\(", r"\\log(", text)
    text = re.sub(r"\b(?:atan|arctan)\b", r"\\arctan", text)
    text = re.sub(r"\b(tanh|sin|cos)\b", lambda match: "\\" + match.group(1), text)
    text = re.sub(r"\b(Var|Cov|Law|diag)\b",
                  lambda match: r"\operatorname{" + match.group(1) + "}", text)
    text = re.sub(r"\bN(?=\s*\()", lambda _: r"\mathcal N", text)
    text = re.sub(r"\b([CLSW])-?infinity\b", r"\1^\\infty", text)
    text = re.sub(r"\binfinity\b", lambda _: r"\infty", text)
    text = re.sub(r"\bsum_", r"\\sum_", text)
    text = re.sub(r"\bprod_", r"\\prod_", text)
    text = re.sub(r"\bintegral_", r"\\int_", text)
    text = re.sub(r"\bmax_", r"\\max_", text)
    text = text.replace(" tensor ", r" \otimes ")
    text = re.sub(r"\bW([12])\b", r"W_{\1}", text)
    text = re.sub(r"\bC1,1\b", r"C^{1,1}", text)
    text = re.sub(r"\b([CLS])([0-9]+)\b", r"\1^{\2}", text)
    text = re.sub(r"\bH1(?=\s*\()", r"H^1", text)
    text = re.sub(r"\b(?:mathcal([A-Z])|([A-Z])cal)(?=_|\b)",
                  lambda match: r"\mathcal " + (match.group(1) or match.group(2)), text)
    text = re.sub(r"(?<![A-Za-z])chi(?![A-Za-z])", r"\\chi", text)
    text = re.sub(r"(?<![A-Za-z])ell(?![A-Za-z])", r"\\ell", text)
    text = re.sub(
        r"(?<![A-Za-z])([A-Za-z][A-Za-z0-9]*)_hat(?:_([A-Za-z0-9]+))?",
        lambda match: (
            r"\widehat{" + match.group(1) + "}"
            + ("_{" + match.group(2) + "}" if match.group(2) else "")
        ),
        text,
    )
    text = re.sub(
        r"(?<![A-Za-z])([A-Za-z][A-Za-z0-9]*)_dagger\b",
        lambda match: match.group(1) + r"^\dagger",
        text,
    )
    for name, replacement in GREEK_PSEUDO_NAMES.items():
        text = re.sub(
            rf"(?<![A-Za-z]){name}([0-9]+)(?![A-Za-z0-9])",
            lambda match, command=replacement: command + "_{" + match.group(1) + "}",
            text,
        )
        text = re.sub(
            rf"(?<![A-Za-z]){name}(?![A-Za-z])",
            lambda _: replacement,
            text,
        )
    while re.search(r"_\(([^()]*)\)", text):
        text = re.sub(r"_\(([^()]*)\)", r"_{\1}", text)
    while re.search(r"\^\(([^()]*)\)", text):
        # Parentheses in the legacy spelling distinguish layer labels such as
        # W^(2) from an ordinary scalar square.  Retaining them is the only
        # syntax-only conversion that cannot change the mathematics.
        text = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", text)
    # A comma can continue one subscript (U_l,N), but must not consume the
    # base of a following indexed symbol (x_1,x_2).
    text = re.sub(
        r"_([A-Za-z0-9*+-]+),([A-Za-z0-9*+-]+)(?!_)",
        r"_{\1,\2}",
        text,
    )
    text = re.sub(r"_([A-Za-z0-9*+-]+)", r"_{\1}", text)
    text = re.sub(r"\^(-?[A-Za-z0-9]+)", r"^{\1}", text)
    if text.count("||") >= 2:
        text = text.replace("||", r"\lVert ", 1).replace("||", r" \rVert", 1)
    return text.strip()


def mechanical_plain_supplements(text: str,
                                   occupied: list[tuple[int, int]]) -> list[dict]:
    """Cover only residual tokens selected by the deterministic signal lexer."""
    intervals = list(occupied)
    additions: list[dict] = []
    for _ in range(256):
        residual = mask_plain_syntax(text, intervals)
        signal = legacy_math_signal_search(residual)
        if signal is None:
            break
        left, right = signal.span()
        bare_named_symbol = signal.group(0).rstrip("'") in {
            *GREEK_PSEUDO_NAMES,
            "chi", "ell",
        }
        if not bare_named_symbol:
            while left > 0 and not residual[left - 1].isspace() and residual[left - 1] not in ";:":
                left -= 1
            while right < len(residual) and not residual[right].isspace() and residual[right] not in ";:":
                right += 1
        while left < right and residual[left] in ".,":
            left += 1
        while right > left and residual[right - 1] in ".,":
            right -= 1
        # Do not pull a prose compound prefix into mathematics (for example,
        # ``radius-1/4`` or ``non-1/c``).  A leading minus with no alphabetic
        # prefix remains part of the formula, as in ``-1<rho<1``.
        compound = re.match(r"[A-Za-z]{2,}-(?=[0-9.])", residual[left:right])
        if compound:
            left += compound.end()
        suffix = re.match(
            r"(?:L2|W1|W2|S1|C1|[0-9]+(?:/[0-9]+)?)(?=-[A-Za-z])",
            residual[left:right],
        )
        if suffix:
            right = left + suffix.end()
        # Token expansion may meet prose punctuation adjacent to a formula.
        # Retain balanced mathematical delimiters, but leave unmatched prose
        # parentheses/brackets outside the generated math span.
        while left < right and residual[left] in "([" and (
            residual[left:right].count(residual[left])
            > residual[left:right].count({"(": ")", "[": "]"}[residual[left]])
        ):
            left += 1
        while right > left and residual[right - 1] in ")]" and (
            residual[left:right].count(residual[right - 1])
            > residual[left:right].count({")": "(", "]": "["}[residual[right - 1]])
        ):
            right -= 1
        if left >= right:
            raise ValueError("residual math lexer produced an empty span")
        source = text[left:right]
        additions.append({
            "source": source,
            "latex": validate_latex_payload(
                legacy_fragment_to_latex(source), "mechanical supplement"
            ),
            "method": "mechanical-supplement",
            "_position": left,
        })
        intervals.append((left, right))
    else:
        raise ValueError("residual math lexer did not terminate")
    if legacy_math_signal_search(mask_plain_syntax(text, intervals)):
        raise ValueError("residual math signal remains after mechanical supplements")
    return additions


def normalized_plain_spans(source_item: dict, returned_spans: list,
                           identity: str,
                           reference_intervals: list[tuple[int, int]]) -> tuple[list[dict], dict]:
    """Keep exact model spans and supplement only lexer-decidable omissions."""
    text = source_item["text"]
    protected: list[tuple[int, int]] = list(reference_intervals)
    cursor = 0
    for item in source_item.get("protected_inline_code", []):
        position = text.find(item["text"], cursor)
        if position < 0:
            raise ValueError(f"{identity}: protected inline source is absent")
        protected.append((position, position + len(item["text"])))
        cursor = position + len(item["text"])

    accepted: list[dict] = []
    occupied = list(protected)
    cursor = 0
    discarded_absent = 0
    discarded_overlap = 0
    for number, span in enumerate(returned_spans, 1):
        source = span.get("source")
        if not isinstance(source, str) or not source or "\n" in source:
            discarded_absent += 1
            continue
        candidates: list[int] = []
        position = text.find(source, cursor)
        while position >= 0:
            candidates.append(position)
            position = text.find(source, position + 1)
        # Short variables are often repeated inside nearby prose words.  A
        # returned ``v`` in "variances v", for example, belongs at the
        # standalone occurrence.  Prefer token boundaries whenever one exists;
        # retain the legacy fallback only for genuinely run-together source
        # such as "at most8^L".
        bounded = [
            position for position in candidates
            if not (
                source[0].isalnum()
                and position > 0
                and (text[position - 1].isalnum() or text[position - 1] == "_")
            )
            and not (
                source[-1].isalnum()
                and position + len(source) < len(text)
                and (
                    text[position + len(source)].isalnum()
                    or text[position + len(source)] == "_"
                )
            )
        ]
        position = (bounded or candidates or [-1])[0]
        if position < 0:
            discarded_absent += 1
            continue
        end = position + len(source)
        if any(position < right and left < end for left, right in occupied):
            discarded_overlap += 1
            continue
        accepted.append({
            "source": source,
            "latex": validate_latex_payload(
                span.get("latex"), f"{identity}/span-{number}"
            ),
            "method": "model",
            "_position": position,
        })
        occupied.append((position, end))
        cursor = end
    supplements = mechanical_plain_supplements(text, occupied)
    accepted.extend(supplements)

    # Re-sort by exact occurrence so application remains deterministic even
    # when the model returned otherwise-valid spans out of source order.
    ordered: list[tuple[int, dict]] = [
        (span["_position"], span) for span in accepted
    ]
    ordered.sort(key=lambda item: item[0])
    for previous, current in zip(ordered, ordered[1:]):
        previous_end = previous[0] + len(previous[1]["source"])
        if current[0] < previous_end:
            raise ValueError(f"{identity}: normalized spans overlap")
    normalized = [
        {
            "start": position,
            "end": position + len(span["source"]),
            **{key: value for key, value in span.items() if key != "_position"},
        }
        for position, span in ordered
    ]
    return normalized, {
        "discarded_absent": discarded_absent,
        "discarded_overlap": discarded_overlap,
        "mechanical_supplements": len(supplements),
    }


def reference_intervals_from_documents(
    documents: list["Document"],
    reference_overrides: list[dict] | None = None,
) -> dict[tuple[str, int], list[tuple[int, int]]]:
    """Locate deterministic references before mathematical transcription."""
    index = Index(documents)
    references: list[dict] = []
    citations: list[dict] = []
    unresolved: list[dict] = []
    for document in documents:
        transform(document, index, references, citations, unresolved)
    by_path = {document.path: document for document in documents}
    grouped: dict[tuple[str, int], list[dict]] = {}
    for reference in references:
        if not reference.get("target"):
            continue
        grouped.setdefault((reference["source"], reference["line"]), []).append(reference)
    result: dict[tuple[str, int], list[tuple[int, int]]] = {}
    for key, records in grouped.items():
        source, line_number = key
        line = by_path[source].lines[line_number - 1].rstrip("\r\n")
        cursor = 0
        intervals: list[tuple[int, int]] = []
        for record in records:
            text = record.get("text")
            if not isinstance(text, str) or not text:
                continue
            candidates: list[int] = []
            needle = text
            interval_offset = 0
            interval_length = len(text)
            if record.get("method") == "parenthesized-equation-range":
                needle = "(" + text + ")"
                interval_length = len(needle)
            position = line.find(needle)
            while position >= 0:
                candidates.append(position)
                position = line.find(needle, position + 1)
            if record.get("method") == "bare-equation-number" and text.startswith("("):
                tag = text[1:-1]
                filtered: list[int] = []
                for position in candidates:
                    prefix = line[:position]
                    if re.search(r"[_^]\{?\s*$", prefix):
                        continue
                    target = index.resolve_bare_equation(source, tag, line_number, prefix)
                    if target and target["id"] == record.get("target"):
                        filtered.append(position)
                candidates = filtered
            unused = [
                position for position in candidates
                if not any(position < right and left < position + interval_length
                           for left, right in intervals)
            ]
            later = [position for position in unused if position >= cursor]
            position = later[0] if later else (unused[0] if unused else -1)
            if position < 0:
                continue
            intervals.append((
                position + interval_offset,
                position + interval_offset + interval_length,
            ))
            cursor = position + interval_length
        if intervals:
            result[key] = intervals
    # Reviewed overrides may point to equations that are still reserved at
    # this pre-transcription stage.  Their exact frozen text is nevertheless
    # a protected reference interval and must not be consumed as mathematics.
    for override in reference_overrides or []:
        source = override.get("source")
        line_number = override.get("line")
        text = override.get("text")
        if (
            source not in by_path
            or not isinstance(line_number, int)
            or not 1 <= line_number <= len(by_path[source].lines)
            or not isinstance(text, str)
            or not text
        ):
            continue
        line = by_path[source].lines[line_number - 1].rstrip("\r\n")
        intervals = result.setdefault((source, line_number), [])
        for match in re.finditer(re.escape(text), line):
            interval = match.span()
            if interval not in intervals:
                intervals.append(interval)
        intervals.sort()
    return result


def baseline_reference_intervals(source_records: list[dict]) -> dict[tuple[str, int], list[tuple[int, int]]]:
    """Locate deterministic pre-transcription references in their source lines."""
    paths = [record["path"] for record in source_records]
    documents = [
        Document(path, (DEFAULT_REPO / path).read_text(encoding="utf-8"))
        for path in paths
    ]
    expected_hashes = {record["path"]: record["sha256"] for record in source_records}
    actual_hashes = {
        document.path: sha256(document.text.encode("utf-8"))
        for document in documents
    }
    if expected_hashes != actual_hashes:
        raise ValueError("prepared batches do not match current sources")
    return reference_intervals_from_documents(documents)


def prepare_math_batches(repo: Path, batch_dir: Path) -> dict:
    paths = discover(repo)
    payload = {path: (repo / path).read_bytes() for path in paths}
    documents = [Document(path, payload[path].decode("utf-8")) for path in paths]
    by_path = {document.path: document for document in documents}
    records = indexed_math_records(documents)
    inline_by_location: dict[tuple[str, int], list[dict]] = {}
    for record in records:
        if record["form"] == "inline-code":
            for line in range(record["line"], record.get("end", record["line"]) + 1):
                inline_by_location.setdefault((record["source"], line), []).append(record)

    grouped = {
        "inline": [record for record in records if record["form"] == "inline-code"],
        "display": [record for record in records if record["form"] == "indented-display"],
        "plain": [record for record in records if record["form"] == "plain-line"],
    }
    midpoint = len(grouped["plain"]) // 2
    specifications = [
        ("inline", "inline", grouped["inline"]),
        ("display", "display", grouped["display"]),
        ("plain-1", "plain", grouped["plain"][:midpoint]),
        ("plain-2", "plain", grouped["plain"][midpoint:]),
    ]
    batch_dir.mkdir(parents=True, exist_ok=True)
    manifest_batches: list[dict] = []
    for name, kind, selected in specifications:
        items: list[dict] = []
        contexts: list[dict] = []
        context_ids: dict[tuple, int] = {}
        for numeric_id, record in enumerate(selected, 1):
            document = by_path[record["source"]]
            context_key, context = paragraph_context(document, record)
            if context_key not in context_ids:
                context_ids[context_key] = len(contexts) + 1
                contexts.append({"id": context_ids[context_key], **context})
            item = {
                "id": numeric_id,
                "source_id": record["id"],
                "source": record["source"],
                "line": record["line"],
                "end": record.get("end", record["line"]),
                "context_id": context_ids[context_key],
                "text": record["text"],
            }
            if kind == "inline":
                item["column"] = record["column"]
                item["end_column"] = record["end_column"]
            elif kind == "display":
                item["parts"] = display_parts(document, record)
            else:
                reserved = record_reserved_targets(document, record)
                if len(reserved) > 1:
                    raise ValueError(f"{record['id']}: multiple targets on one plain line")
                item["reserved_target"] = (
                    {
                        "id": reserved[0]["id"],
                        "legacy_number": reserved[0]["number"],
                    }
                    if reserved else None
                )
                item["protected_inline_code"] = [
                    {"source_id": other["id"], "text": other["text"]}
                    for other in inline_by_location.get((record["source"], record["line"]), [])
                ]
            items.append(item)
        batch = {
            "schema": 1,
            "batch": name,
            "kind": kind,
            "source": [
                {"path": path, "sha256": sha256(payload[path])}
                for path in paths
            ],
            "contexts": contexts,
            "items": items,
        }
        batch_bytes = json.dumps(
            batch, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
        chapter_numbers = {path: number for number, path in enumerate(paths, 1)}
        model_items: list[dict] = []
        for item in items:
            model_item = {
                "id": item["id"],
                "at": [
                    chapter_numbers[item["source"]], item["line"], item["end"]
                ],
                "context_id": item["context_id"],
                "text": item["text"],
            }
            if kind == "inline":
                model_item["columns"] = [item["column"], item["end_column"]]
            elif kind == "display":
                model_item["parts"] = [
                    {
                        "part_id": part["part_id"],
                        "text": part["text"],
                        "equation_number": part["legacy_number"],
                    }
                    for part in item["parts"]
                ]
            else:
                model_item["reserved_equation_number"] = (
                    item["reserved_target"]["legacy_number"]
                    if item["reserved_target"] else None
                )
                model_item["protected_inline_code"] = [
                    protected["text"] for protected in item["protected_inline_code"]
                ]
            model_items.append(model_item)
        model_batch = {
            "batch": name,
            "kind": kind,
            "chapters": [path for path in paths],
            "contexts": [
                {
                    "id": context["id"],
                    "section": context["section"],
                    "text": context["text"],
                }
                for context in contexts
            ],
            "items": model_items,
        }
        schema_bytes = (
            json.dumps(json_schema_for_math_batch(kind, len(items)), indent=2) + "\n"
        ).encode("utf-8")
        prompt_header = (
            MATH_BATCH_PROMPTS[kind]
            + f"The items array must contain exactly {len(items)} entries. "
              "An empty, partial, summarized, sampled, or truncated array is invalid.\n\n"
        )
        prompt_bytes = prompt_header.encode("utf-8") + json.dumps(
            model_batch, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8") + b"\n"
        atomic_write(batch_dir / f"{name}.json", batch_bytes + b"\n")
        atomic_write(batch_dir / f"{name}.schema.json", schema_bytes)
        atomic_write(batch_dir / f"{name}.prompt.txt", prompt_bytes)
        manifest_batches.append({
            "name": name,
            "kind": kind,
            "items": len(items),
            "input": f"{name}.json",
            "input_sha256": sha256(batch_bytes + b"\n"),
            "prompt": f"{name}.prompt.txt",
            "prompt_sha256": sha256(prompt_bytes),
            "schema": f"{name}.schema.json",
            "schema_sha256": sha256(schema_bytes),
            "response": f"{name}.response.json",
        })
    manifest = {
        "schema": 1,
        "model": "gpt-5.6-terra",
        "reasoning_effort": "medium",
        "source": [
            {"path": path, "sha256": sha256(payload[path])}
            for path in paths
        ],
        "records": len(records),
        "batches": manifest_batches,
    }
    atomic_write(
        batch_dir / "manifest.json",
        (json.dumps(manifest, indent=2) + "\n").encode("utf-8"),
    )
    return manifest


def validate_latex_payload(latex: object, identity: str) -> str:
    if not isinstance(latex, str) or not latex.strip():
        raise ValueError(f"{identity}: empty LaTeX payload")
    if "`" in latex or "$" in latex:
        raise ValueError(f"{identity}: payload contains Markdown math delimiters")
    if re.search(r"\\(?:tag|label)\s*\{|\\[\[\]]", latex):
        raise ValueError(f"{identity}: payload contains a model-owned label or delimiter")
    if re.search(
        r"[_^]\\(?:mathcal|mathrm|mathbf|mathbb|mathsf|mathtt|mathit|"
        r"operatorname|text|boldsymbol|overline|underline|sqrt|frac)\s*\{",
        latex,
    ):
        raise ValueError(
            f"{identity}: command-valued subscript or superscript lacks an outer group"
        )
    if REPEATED_SUPERSCRIPT_RE.search(latex) or REPEATED_SUBSCRIPT_RE.search(latex):
        raise ValueError(f"{identity}: one mathematical atom carries a repeated script")
    depth = 0
    normalized: list[str] = []
    for position, character in enumerate(latex):
        escaped = position > 0 and latex[position - 1] == "\\"
        if character == "{" and not escaped:
            depth += 1
        elif character == "}" and not escaped:
            if depth:
                depth -= 1
            else:
                # A raw pseudo-math set delimiter is commonly returned as an
                # unmatched TeX brace when its opening half lies in adjacent
                # source context.  Escaping only an otherwise-unmatched close
                # preserves it as a printed delimiter without guessing content.
                normalized.append("\\")
        normalized.append(character)
    if depth:
        # Terra occasionally drops only the terminal braces of subscripts,
        # superscripts, or command arguments.  Closing the still-open groups is
        # the unique syntax-preserving normalization; no payload text changes.
        normalized.append("}" * depth)
    return "".join(normalized).strip()


def preserve_display_terminal_punctuation(source: str, latex: str) -> str:
    """Carry the frozen formula's final punctuation across transcription."""
    source_tail = source.rstrip()
    source_tail = re.sub(
        r"\s*\([A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*\)\s*$", "", source_tail
    ).rstrip()
    punctuation = source_tail[-1] if source_tail and source_tail[-1] in ".,;:" else ""

    closing = re.search(r"(\\end\{(?:aligned|gathered|cases|split)\})\s*$", latex)
    if closing:
        body = latex[:closing.start()].rstrip()
        body = re.sub(r"[.,;:]$", "", body).rstrip()
        return body + punctuation + closing.group(1)
    body = re.sub(r"[.,;:]$", "", latex.rstrip()).rstrip()
    return body + punctuation


def ingest_math_responses(batch_dir: Path, decisions_path: Path) -> dict:
    manifest = json.loads((batch_dir / "manifest.json").read_text(encoding="utf-8"))
    protected_references = baseline_reference_intervals(manifest["source"])
    decisions: list[dict] = []
    receipts: list[dict] = []
    normalization = {
        "discarded_absent": 0,
        "discarded_overlap": 0,
        "mechanical_supplements": 0,
    }
    for batch_record in manifest["batches"]:
        name, kind = batch_record["name"], batch_record["kind"]
        batch_bytes = (batch_dir / batch_record["input"]).read_bytes()
        if sha256(batch_bytes) != batch_record["input_sha256"]:
            raise ValueError(f"{name}: batch input hash changed")
        batch = json.loads(batch_bytes)
        response_path = batch_dir / batch_record["response"]
        response_bytes = response_path.read_bytes()
        response = json.loads(response_bytes)
        if response.get("batch") != name or not isinstance(response.get("items"), list):
            raise ValueError(f"{name}: malformed response envelope")
        expected_ids = list(range(1, len(batch["items"]) + 1))
        actual_ids = [item.get("id") for item in response["items"]]
        if actual_ids != expected_ids:
            raise ValueError(f"{name}: response IDs are incomplete, duplicated, or reordered")
        for source_item, result in zip(batch["items"], response["items"]):
            identity = source_item["source_id"]
            if kind == "inline":
                decision = {
                    "id": identity,
                    "form": "inline-code",
                    "latex": validate_latex_payload(result.get("latex"), identity),
                }
            elif kind == "display":
                expected_parts = source_item["parts"]
                returned_parts = result.get("parts")
                if not isinstance(returned_parts, list):
                    raise ValueError(f"{identity}: missing display parts")
                if [part.get("part_id") for part in returned_parts] != [
                    part["part_id"] for part in expected_parts
                ]:
                    raise ValueError(f"{identity}: display parts are incomplete or reordered")
                decision = {
                    "id": identity,
                    "form": "indented-display",
                    "parts": [
                        {
                            "part_id": returned["part_id"],
                            "latex": preserve_display_terminal_punctuation(
                                expected["text"],
                                validate_latex_payload(
                                    returned.get("latex"),
                                    f"{identity}/part-{returned['part_id']}",
                                ),
                            ),
                        }
                        for expected, returned in zip(expected_parts, returned_parts)
                    ],
                }
            else:
                mode = result.get("mode")
                latex = result.get("latex")
                spans = result.get("spans")
                if mode not in {"mixed", "display"} or not isinstance(spans, list):
                    raise ValueError(f"{identity}: malformed plain-line decision")
                if source_item["reserved_target"] and mode != "display":
                    raise ValueError(f"{identity}: reserved equation was not returned as display")
                if mode == "display":
                    if spans:
                        raise ValueError(f"{identity}: display decision has span edits")
                    clean_latex = preserve_display_terminal_punctuation(
                        source_item["text"], validate_latex_payload(latex, identity)
                    )
                    clean_spans: list[dict] = []
                else:
                    if latex != "":
                        raise ValueError(f"{identity}: mixed decision needs empty latex")
                    clean_latex = ""
                    clean_spans, span_stats = normalized_plain_spans(
                        source_item, spans, identity,
                        protected_references.get(
                            (source_item["source"], source_item["line"]), []
                        ),
                    )
                    for key in normalization:
                        normalization[key] += span_stats[key]
                decision = {
                    "id": identity,
                    "form": "plain-line",
                    "mode": mode,
                    "latex": clean_latex,
                    "spans": clean_spans,
                }
            decisions.append(decision)
        receipts.append({
            "name": name,
            "kind": kind,
            "items": len(batch["items"]),
            "input_sha256": batch_record["input_sha256"],
            "prompt_sha256": batch_record["prompt_sha256"],
            "response_sha256": sha256(response_bytes),
        })
    if len({decision["id"] for decision in decisions}) != len(decisions):
        raise ValueError("duplicate decisions across batches")
    if len(decisions) != manifest["records"]:
        raise ValueError("not every prepared math record has a decision")
    payload = {
        "schema": 1,
        "model": manifest["model"],
        "reasoning_effort": manifest["reasoning_effort"],
        "source": manifest["source"],
        "batches": receipts,
        "normalization": normalization,
        "items": decisions,
    }
    atomic_write(
        decisions_path,
        (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
    )
    return payload


def format_transcribed_display(latex: str, target_id: str | None) -> tuple[str, str]:
    payload = normalize_display_layout(
        normalize_math_atom_layout(latex.strip() + "\n")
    )
    closing = "$$" + (f" {{#{target_id}}}" if target_id else "")
    return f"\n$$\n{payload}{closing}\n\n", payload


class MathTranscriptions:
    """Validated semantic replacements applied over frozen source coordinates."""

    def __init__(self, documents: list[Document], decisions_path: Path):
        raw = decisions_path.read_bytes()
        payload = json.loads(raw)
        if payload.get("schema") != 1 or not isinstance(payload.get("items"), list):
            raise ValueError("unsupported math-decision file")
        source_hashes = {item["path"]: item["sha256"] for item in payload.get("source", [])}
        actual_hashes = {
            document.path: sha256(document.text.encode("utf-8"))
            for document in documents
        }
        if source_hashes != actual_hashes:
            raise ValueError("math decisions do not match the current frozen book sources")
        reference_overrides = payload.get("reference_overrides", [])
        if not isinstance(reference_overrides, list):
            raise ValueError("reference_overrides must be a list")
        self.reference_overrides = reference_overrides
        bibliography = payload.get("bibliography", [])
        if not isinstance(bibliography, list):
            raise ValueError("bibliography must be a list")
        self.bibliography = bibliography

        records = indexed_math_records(documents)
        reference_intervals = reference_intervals_from_documents(
            documents, reference_overrides
        )
        decision_map = {item.get("id"): item for item in payload["items"]}
        if len(decision_map) != len(payload["items"]):
            raise ValueError("duplicate mathematical decisions")
        if set(decision_map) != {record["id"] for record in records}:
            raise ValueError("mathematical decisions are incomplete or stale")
        by_path = {document.path: document for document in documents}
        records_by_path: dict[str, list[dict]] = {}
        for record in records:
            records_by_path.setdefault(record["source"], []).append(record)
        record_by_id = {record["id"]: record for record in records}

        reviewed_blocks_by_path: dict[str, list[dict]] = {}
        reviewed_ids: set[str] = set()
        for number, block in enumerate(payload.get("reviewed_blocks", []), 1):
            if not isinstance(block, dict):
                raise ValueError(f"reviewed block {number}: malformed record")
            path = block.get("source")
            start, end = block.get("start"), block.get("end")
            covered = block.get("covered_ids")
            if (
                path not in by_path
                or not isinstance(start, int)
                or not isinstance(end, int)
                or not 1 <= start <= end <= len(by_path[path].lines)
                or not isinstance(covered, list)
                or not covered
                or len(set(covered)) != len(covered)
            ):
                raise ValueError(f"reviewed block {number}: invalid coordinates or IDs")
            exact = "".join(by_path[path].lines[start - 1:end])
            if exact != block.get("text"):
                raise ValueError(f"reviewed block {number}: frozen source text mismatch")
            for identity in covered:
                record = record_by_id.get(identity)
                if record is None or record["source"] != path:
                    raise ValueError(f"reviewed block {number}: unknown covered ID {identity}")
                record_start = record["line"]
                # Indented-display end coordinates are the first line after
                # the mathematical payload; allow that boundary only.
                record_last = record.get("end", record_start)
                if record["form"] == "indented-display":
                    record_last -= 1
                if record_start < start or record_last > end:
                    raise ValueError(
                        f"reviewed block {number}: {identity} is outside its source range"
                    )
                if identity in reviewed_ids:
                    raise ValueError(f"reviewed block {number}: duplicate covered ID {identity}")
                reviewed_ids.add(identity)
            latex = validate_latex_payload(
                block.get("latex"), f"reviewed block {number}"
            )
            target_id = block.get("target")
            if target_id is not None and not any(
                target["id"] == target_id
                and target["source"] == path
                and start <= target.get("label_line", target["range"]["start"]) <= end
                for target in by_path[path].pending_equations
            ):
                raise ValueError(f"reviewed block {number}: invalid reserved target")
            reviewed_blocks_by_path.setdefault(path, []).append({
                **block,
                "latex": latex,
            })

        self.lines: dict[str, list[str]] = {}
        self.blocks: dict[str, list[dict]] = {}
        self.displays: dict[str, list[dict]] = {}
        self.applied_ids: list[str] = []
        defined_reserved: set[str] = set()

        for path, document in by_path.items():
            line_offsets = [0]
            for line in document.lines:
                line_offsets.append(line_offsets[-1] + len(line))
            interval_edits: list[tuple[int, int, str, str]] = []
            block_edits: list[dict] = []
            expected_displays: list[dict] = []
            path_records = records_by_path.get(path, [])
            inline_intervals: list[tuple[int, int, str]] = []

            for order, block in enumerate(
                sorted(reviewed_blocks_by_path.get(path, []), key=lambda item: item["start"])
            ):
                rendered, expected = format_transcribed_display(
                    block["latex"], block.get("target")
                )
                block_edits.append({
                    "start": block["start"], "end": block["end"],
                    "text": rendered, "ids": list(block["covered_ids"]),
                })
                expected_displays.append({
                    "start": block["start"], "order": -1000 + order,
                    "payload": expected, "target": block.get("target"),
                })
                if block.get("target"):
                    defined_reserved.add(block["target"])
                self.applied_ids.extend(block["covered_ids"])

            for record in path_records:
                if record["id"] in reviewed_ids:
                    continue
                if record["form"] != "inline-code":
                    continue
                decision = decision_map[record["id"]]
                if decision.get("form") != record["form"]:
                    raise ValueError(f"{record['id']}: decision form mismatch")
                start = line_offsets[record["line"] - 1] + record["column"]
                end = line_offsets[record["end"] - 1] + record["end_column"]
                if document.text[start:end] != record["text"]:
                    raise ValueError(f"{record['id']}: exact inline source mismatch")
                latex = validate_latex_payload(decision.get("latex"), record["id"])
                newlines = record["text"].count("\n")
                latex = " ".join(latex.splitlines()) + ("\n" * newlines)
                replacement = r"\(" + latex + r"\)"
                interval_edits.append((start, end, replacement, record["id"]))
                inline_intervals.append((start, end, record["id"]))
                self.applied_ids.append(record["id"])

            for record in path_records:
                if record["id"] in reviewed_ids:
                    continue
                if record["form"] != "plain-line":
                    continue
                decision = decision_map[record["id"]]
                if decision.get("form") != record["form"]:
                    raise ValueError(f"{record['id']}: decision form mismatch")
                line = document.lines[record["line"] - 1]
                source_line = line.rstrip("\r\n")
                if source_line != record["text"]:
                    raise ValueError(f"{record['id']}: exact plain-line source mismatch")
                targets = record_reserved_targets(document, record)
                if decision.get("mode") == "display":
                    if any(
                        line_offsets[record["line"] - 1] < right
                        and left < line_offsets[record["line"]]
                        for left, right, _ in inline_intervals
                    ):
                        raise ValueError(
                            f"{record['id']}: whole-line display overlaps protected inline code"
                        )
                    if len(targets) > 1:
                        raise ValueError(f"{record['id']}: multiple reserved plain-line targets")
                    latex = validate_latex_payload(decision.get("latex"), record["id"])
                    target_id = targets[0]["id"] if targets else None
                    rendered, expected = format_transcribed_display(latex, target_id)
                    block_edits.append({
                        "start": record["line"], "end": record["line"],
                        "text": rendered, "ids": [record["id"]],
                    })
                    expected_displays.append({
                        "start": record["line"], "order": 0,
                        "payload": expected, "target": target_id,
                    })
                    if target_id:
                        defined_reserved.add(target_id)
                elif decision.get("mode") == "mixed":
                    if targets:
                        raise ValueError(f"{record['id']}: reserved equation is not a display")
                    spans = decision.get("spans")
                    if not isinstance(spans, list):
                        raise ValueError(f"{record['id']}: malformed mixed-line spans")
                    cursor = 0
                    covered: list[tuple[int, int]] = []
                    for number, span in enumerate(spans, 1):
                        source = span.get("source")
                        if not isinstance(source, str) or not source or "\n" in source:
                            raise ValueError(f"{record['id']}/span-{number}: invalid source")
                        position = span.get("start")
                        span_end = span.get("end")
                        if (
                            not isinstance(position, int)
                            or not isinstance(span_end, int)
                            or position < cursor
                            or span_end != position + len(source)
                            or source_line[position:span_end] != source
                        ):
                            raise ValueError(
                                f"{record['id']}/span-{number}: exact source coordinates mismatch"
                            )
                        absolute_start = line_offsets[record["line"] - 1] + position
                        absolute_end = line_offsets[record["line"] - 1] + span_end
                        if any(
                            position < right and left < span_end
                            for left, right in reference_intervals.get(
                                (record["source"], record["line"]), []
                            )
                        ):
                            raise ValueError(
                                f"{record['id']}/span-{number}: overlaps a resolvable reference"
                            )
                        if any(
                            absolute_start < right and left < absolute_end
                            for left, right, _ in inline_intervals
                        ):
                            raise ValueError(
                                f"{record['id']}/span-{number}: overlaps protected inline code"
                            )
                        latex = validate_latex_payload(
                            span.get("latex"), f"{record['id']}/span-{number}"
                        )
                        interval_edits.append((
                            absolute_start, absolute_end, r"\(" + latex + r"\)",
                            f"{record['id']}/span-{number}",
                        ))
                        covered.append((position, span_end))
                        cursor = span_end
                    local_occupied = list(covered)
                    local_occupied.extend(reference_intervals.get(
                        (record["source"], record["line"]), []
                    ))
                    for left, right, _ in inline_intervals:
                        line_start = line_offsets[record["line"] - 1]
                        if line_start <= left and right <= line_offsets[record["line"]]:
                            local_left, local_right = left - line_start, right - line_start
                            local_occupied.append((local_left, local_right))
                    if legacy_math_signal_search(mask_plain_syntax(source_line, local_occupied)):
                        raise ValueError(f"{record['id']}: raw math signal remains outside spans")
                else:
                    raise ValueError(f"{record['id']}: unknown plain-line mode")
                self.applied_ids.append(record["id"])

            for record in path_records:
                if record["id"] in reviewed_ids:
                    continue
                if record["form"] != "indented-display":
                    continue
                decision = decision_map[record["id"]]
                if decision.get("form") != record["form"]:
                    raise ValueError(f"{record['id']}: decision form mismatch")
                parts = display_parts(document, record)
                returned = decision.get("parts")
                if not isinstance(returned, list) or [part.get("part_id") for part in returned] != [
                    part["part_id"] for part in parts
                ]:
                    raise ValueError(f"{record['id']}: display parts mismatch")
                rendered_parts: list[str] = []
                for order, (part, result) in enumerate(zip(parts, returned)):
                    exact = "".join(document.lines[part["line"] - 1:part["end"]]).rstrip("\r\n")
                    if exact != part["text"]:
                        raise ValueError(f"{record['id']}/part-{part['part_id']}: source changed")
                    latex = validate_latex_payload(
                        result.get("latex"), f"{record['id']}/part-{part['part_id']}"
                    )
                    rendered, expected = format_transcribed_display(latex, part["target_id"])
                    rendered_parts.append(rendered)
                    expected_displays.append({
                        "start": part["line"], "order": order,
                        "payload": expected, "target": part["target_id"],
                    })
                    if part["target_id"]:
                        defined_reserved.add(part["target_id"])
                block_edits.append({
                    "start": record["line"],
                    "end": record.get("end", record["line"]),
                    "text": "".join(rendered_parts),
                    "ids": [record["id"]],
                })
                self.applied_ids.append(record["id"])

            interval_edits.sort(key=lambda item: (item[0], item[1]))
            for previous, current in zip(interval_edits, interval_edits[1:]):
                if current[0] < previous[1]:
                    raise ValueError(
                        f"overlapping exact edits: {previous[3]} and {current[3]}"
                    )
            converted_text = document.text
            for start, end, replacement, _ in reversed(interval_edits):
                converted_text = converted_text[:start] + replacement + converted_text[end:]
            converted_lines = converted_text.splitlines(keepends=True)
            if len(converted_lines) != len(document.lines):
                raise ValueError(f"{path}: inline transcription changed source line count")

            occupied: set[int] = set()
            for block in sorted(block_edits, key=lambda item: item["start"]):
                lines = set(range(block["start"], block["end"] + 1))
                if occupied.intersection(lines):
                    raise ValueError(f"{path}:{block['start']}: overlapping display blocks")
                if any(document.mask[line - 1] for line in lines):
                    raise ValueError(f"{path}:{block['start']}: display overlaps fenced code")
                occupied.update(lines)
            self.lines[path] = converted_lines
            self.blocks[path] = sorted(block_edits, key=lambda item: item["start"])
            self.displays[path] = sorted(
                expected_displays, key=lambda item: (item["start"], item["order"])
            )

        reserved = {
            target["id"]
            for document in documents for target in document.pending_equations
        }
        if defined_reserved != reserved:
            missing = sorted(reserved.difference(defined_reserved))
            extra = sorted(defined_reserved.difference(reserved))
            raise ValueError(
                f"reserved equation activation mismatch; missing={missing[:5]}, extra={extra[:5]}"
            )
        if set(self.applied_ids) != {record["id"] for record in records}:
            raise ValueError("not every mathematical candidate was applied exactly once")
        for document in documents:
            for target in document.pending_equations:
                target["status"] = "defined"
                target["transcribed"] = True
        self.summary = {
            "decisions": len(records),
            "inline_code": sum(record["form"] == "inline-code" for record in records),
            "indented_display": sum(
                record["form"] == "indented-display" for record in records
            ),
            "plain_line": sum(record["form"] == "plain-line" for record in records),
            "activated_equations": len(reserved),
            "decision_sha256": sha256(raw),
            "model": payload.get("model"),
            "reasoning_effort": payload.get("reasoning_effort"),
            "normalization": payload.get("normalization", {}),
            "reviewed_corrections": payload.get("review", {}),
            "reviewed_blocks": len(payload.get("reviewed_blocks", [])),
            "reviewed_references": len(reference_overrides),
            "bibliography_entries": len(bibliography),
            "exact_source_match": True,
            "prose_outside_spans_unchanged": True,
        }

    def source_lines(self, document: Document) -> list[str]:
        return self.lines[document.path]

    def block_edits(self, document: Document) -> list[dict]:
        return self.blocks[document.path]

    def expected_displays(self, document: Document) -> list[dict]:
        return self.displays[document.path]


def record_reference(references: list[dict], source: str, line_number: int,
                     text: str, target: dict, method: str,
                     rendered: bool, group_rendered: bool | None = None) -> None:
    record = {
        "source": source,
        "line": line_number,
        "text": text,
        "target": target["id"],
        "method": method,
        "target_status": target.get("status", "defined"),
        "rendered": rendered,
    }
    if group_rendered is not None:
        record["group_rendered"] = group_rendered
    references.append(record)


def convert_plain_segment(segment: str, source: str, line_number: int, index: Index,
                          references: list[dict], unresolved: list[dict],
                          prior_context: str = "") -> str:
    segment, reviewed_references = index.protect_reference_overrides(
        segment, source, line_number, references
    )
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
            group_rendered = False
            for number, target in ((first_number, first_target), (last_number, last_target)):
                record_reference(
                    references, source, line_number, number, target,
                    "explicit-multiple", rendered=False,
                    group_rendered=group_rendered,
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
                "explicit-multiple", rendered=True, group_rendered=True,
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
            group_rendered = False
            for text_value, target in (
                (first, first_target), (match.group("last"), last_target)
            ):
                record_reference(
                    references, source, line_number, text_value, target,
                    "bare-equation-token-range", rendered=False,
                    group_rendered=group_rendered,
                )
            return match.group(0)
        for text_value, target in ((first, first_target), (match.group("last"), last_target)):
            record_reference(
                references, source, line_number, text_value, target,
                "bare-equation-token-range", rendered=True, group_rendered=True,
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

    # Convert parenthesized equation ranges before the single-number rule.
    # The latter intentionally ignores range endpoints, since converting one
    # endpoint without the other would leave a misleading half-reference.
    parenthesized_equation_range = re.compile(
        r"(?<![A-Za-z0-9_^')}\]])\("
        r"(?P<first>[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)"
        r"\)(?P<space1>\s*)(?P<dash>–|—|--)(?P<space2>\s*)\("
        r"(?P<last>[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)"
        r"\)(?![A-Za-z0-9])"
    )

    def parenthesized_range_replacement(match: re.Match) -> str:
        first_number = match.group("first")
        last_number = match.group("last")
        first_map = index.equation_reference_candidates(source, first_number)
        last_map = index.equation_reference_candidates(source, last_number)
        # A syntactically similar prose range is not an equation citation
        # unless both endpoints are actual equation tags in this chapter.
        if not first_map or not last_map:
            return match.group(0)
        if any(
            target.get("label_line") == line_number
            for target in first_map + last_map
        ):
            return match.group(0)
        prefix = segment[:match.start()]
        first_target = index.resolve_bare_equation(
            source, first_number, line_number, prefix
        )
        last_target = index.resolve_bare_equation(
            source, last_number, line_number, prefix
        )
        if not first_target or not last_target:
            unresolved.append({
                "kind": "reference", "source": source, "line": line_number,
                "text": match.group(0),
                "reason": "parenthesized equation range lacks unique local outline scope",
            })
            return match.group(0)
        rendered = all(
            target.get("status") == "defined"
            for target in (first_target, last_target)
        )
        for number, target in (
            (first_number, first_target), (last_number, last_target)
        ):
            record_reference(
                references, source, line_number, number, target,
                "parenthesized-equation-range", rendered=rendered,
                group_rendered=rendered,
            )
        if not rendered:
            return match.group(0)
        return (
            f"([-@{first_target['id']}])"
            + match.group("space1") + match.group("dash") + match.group("space2")
            + f"([-@{last_target['id']}])"
        )

    segment = parenthesized_equation_range.sub(
        parenthesized_range_replacement, segment
    )

    # A parenthesized equation number may be a simple integer (``(3)``) as
    # well as a compound tag (``(H2.3)``).  Replacement is still conservative:
    # it occurs only outside code/math and only when this chapter has exactly
    # one display carrying that tag.
    bare = re.compile(
        r"(?<![A-Za-z0-9_^')}\]])\("
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
        if not index.equation_reference_candidates(source, tag):
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

    segment = bare.sub(bare_replacement, segment)
    for placeholder, replacement in reviewed_references.items():
        segment = segment.replace(placeholder, replacement)
    return segment


def convert_prose_line(line: str, source: str, line_number: int, index: Index,
                       references: list[dict], citations: list[dict], unresolved: list[dict],
                       inline_math_state: list[bool] | None = None,
                       inline_code_state: list[int] | None = None,
                       prior_context: str = "") -> str:
    line = normalize_inline_math_spacing(line)
    math_state = inline_math_state if inline_math_state is not None else [False]
    if len(math_state) == 1:
        math_state.append(False)
    code_state = inline_code_state if inline_code_state is not None else [0]
    output: list[str] = []
    plain: list[str] = []

    def flush() -> None:
        if plain:
            prior = (prior_context + "".join(output))[-240:]
            plain_text = normalize_inline_dollar_boundaries("".join(plain))
            converted_plain = convert_plain_segment(
                plain_text, source, line_number, index, references,
                unresolved, prior_context=prior,
            )
            output.append(converted_plain.replace("∎", r"$\blacksquare$"))
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
                fragment = line[position:]
                if fragment.endswith("\r\n"):
                    fragment = fragment[:-2]
                elif fragment.endswith("\n") or fragment.endswith("\r"):
                    fragment = fragment[:-1]
                if fragment:
                    if math_state[1]:
                        output.append(" ")
                    output.append(normalize_math_atom_layout(fragment))
                math_state[1] = True
                break
            fragment = line[position:end]
            if fragment:
                if math_state[1]:
                    output.append(" ")
                output.append(normalize_math_atom_layout(fragment))
            output.append("$")
            math_state[0] = False
            math_state[1] = False
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
            math_state[1] = False
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
                citation_key = index.cite_external_link(
                    source, line_number, destination
                )
                citation = {
                    "source": source, "line": line_number, "text": caption,
                    "destination": destination, "status": "external-link",
                }
                if citation_key:
                    citation["key"] = citation_key
                    citation["status"] = "bibliography"
                citations.append(citation)
                rendered_link = f"{link.group('image')}[{converted_caption}]({destination})"
                if citation_key:
                    rendered_link += f" [@{citation_key}]"
                output.append(rendered_link)
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
              unresolved: list[dict],
              transcriptions: MathTranscriptions | None = None) -> str:
    if transcriptions is None:
        unresolved.extend(document.math_inventory)
    source_lines = (
        transcriptions.source_lines(document) if transcriptions is not None else document.lines
    )
    replacements: dict[int, str] = {}
    after: dict[int, list[str]] = {}
    display_lines: set[int] = set()
    formal_starts = {formal["start"] for formal in document.formals}

    for heading in document.headings:
        line_number = heading["range"]["start"]
        if heading["style"] == "bold":
            if line_number not in formal_starts:
                converted_line = convert_prose_line(
                    source_lines[line_number - 1], document.path, line_number, index,
                    references, citations, unresolved,
                )
                replacements[line_number] = f"[]{{#{heading['id']}}}\n\n" + converted_line
            continue
        line = source_lines[line_number - 1]
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
        statement_match = SYMBOLIC_STATEMENT_RE.match(source_lines[line_number - 1])
        if not statement_match:
            raise ValueError(f"{document.path}:{line_number}: transcribed statement changed syntax")
        body = convert_prose_line(
            statement_match.group("body"), document.path, line_number, index,
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
        payload = "".join(source_lines[start:end - 1])
        tags = balanced_tag_spans(payload)
        payload = normalize_display_layout(
            normalize_math_atom_layout(remove_spans(payload, tags))
        )
        # Write the normalized payload once and suppress every original
        # interior line.  Removing a tag-only line changes the payload's line
        # count, so positional line-by-line replacement would otherwise leak
        # the old tag line back into the output.
        for line_number in range(start + 1, end):
            replacements[line_number] = ""
        if start + 1 < end:
            replacements[start + 1] = payload
        target = display.get("target")
        closing = indent + "$$" + (f" {{#{target['id']}}}" if target else "") + "\n"
        converted_close = DISPLAY_CLOSE_RE.match(source_lines[end - 1])
        close_tail = (
            converted_close.group("tail")
            if converted_close is not None
            else display["close_tail"]
        )
        if close_tail:
            closing += "\n"
            closing += convert_prose_line(
                close_tail.lstrip() + display["close_newline"],
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
        source_line = source_lines[formal["start"] - 1]
        if formal["kind"] == "proof":
            plain_proof_match = PLAIN_PROOF_RE.match(source_line)
            formal_match = plain_proof_match or BOLD_LEAD_RE.match(source_line)
        else:
            plain_proof_match = None
            formal_match = BOLD_LEAD_RE.match(source_line)
        if not formal_match:
            raise ValueError(
                f"{document.path}:{formal['start']}: transcribed formal changed syntax"
            )
        body = formal_match.group("body") or ""
        if plain_proof_match is None:
            body = body.lstrip()
        if body:
            opening += convert_prose_line(
                body + formal["newline"], document.path, formal["start"], index,
                references, citations, unresolved,
            )
        replacements[formal["start"]] = opening
        after.setdefault(formal["end"], []).append("\n:::\n")

    if transcriptions is not None:
        for block in transcriptions.block_edits(document):
            lines = range(block["start"], block["end"] + 1)
            if any(line in display_lines for line in lines):
                raise ValueError(
                    f"{document.path}:{block['start']}: transcription overlaps existing display"
                )
            if block["start"] in replacements:
                raise ValueError(
                    f"{document.path}:{block['start']}: display transcription overlaps structure"
                )
            replacements[block["start"]] = block["text"]
            for line in range(block["start"] + 1, block["end"] + 1):
                if line in replacements:
                    raise ValueError(
                        f"{document.path}:{line}: display transcription overlaps structure"
                    )
                replacements[line] = ""

    converted: list[str] = []
    inline_math_state = [False]
    inline_code_state = [0]
    paragraph_context = ""
    for line_number, line in enumerate(source_lines, 1):
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
    return separate_markdown_headings("".join(converted))


def validate(documents: list[Document], outputs: dict[str, str], index: Index,
             references: list[dict], unresolved: list[dict],
             transcriptions: MathTranscriptions | None = None) -> dict:
    labels: list[str] = []
    errors: list[str] = []
    for document in documents:
        output = outputs[document.path]
        labels.extend(re.findall(r"\{#([a-z]+-[a-z0-9-]+)\}", output))
        output_lines = output.splitlines(keepends=True)
        if fenced_blocks(document.lines) != fenced_blocks(output_lines):
            errors.append(f"{document.path}: fenced-code blocks changed")
        actual_displays = dollar_displays(output_lines)
        if any(
            any(not line.strip() for line in payload.splitlines())
            for payload, _label in actual_displays
        ):
            errors.append(
                f"{document.path}: blank line inside dollar display prevents Quarto parsing"
            )
        if any(
            normalize_display_layout(payload) != payload
            for payload, _label in actual_displays
        ):
            errors.append(
                f"{document.path}: split environment has multiple alignment columns"
            )
        if any(
            REPEATED_SUPERSCRIPT_RE.search(payload)
            or REPEATED_SUBSCRIPT_RE.search(payload)
            for payload, _label in actual_displays
        ):
            errors.append(f"{document.path}: display math contains a repeated script")
        expected_records: list[dict] = []
        for display in document.displays:
            payload = "".join(document.lines[display["start"]:display["end"] - 1])
            expected_records.append({
                "start": display["start"],
                "order": 0,
                "payload": normalize_display_layout(
                    normalize_math_atom_layout(
                        remove_spans(payload, balanced_tag_spans(payload))
                    )
                ),
                "target": display.get("target", {}).get("id"),
            })
        if transcriptions is not None:
            expected_records.extend(transcriptions.expected_displays(document))
        expected_records.sort(key=lambda item: (item["start"], item["order"]))
        expected_displays = [
            (item["payload"], item["target"]) for item in expected_records
        ]
        if actual_displays != expected_displays:
            errors.append(f"{document.path}: display-math payload or label changed")
        masked = fence_mask(output_lines)
        prose = "".join(line if not masked[i] else "\n" for i, line in enumerate(output_lines))
        prose_without_code = mask_inline_code(prose)
        if re.search(r"(?m)^\s*\\[\[\]]\s*$", prose):
            errors.append(f"{document.path}: standalone legacy display delimiter remains")
        if re.search(r"(?<!\\)\\[()]", prose_without_code):
            errors.append(f"{document.path}: legacy inline math delimiter remains")
        in_dollar_display = False
        for line in prose_without_code.splitlines(keepends=True):
            if not in_dollar_display and re.fullmatch(r"\s*\$\$\s*(?:\r?\n)?", line):
                in_dollar_display = True
                continue
            if in_dollar_display:
                if re.fullmatch(
                    r"\s*\$\$(?:\s+\{#[a-z]+-[a-z0-9-]+\})?\s*(?:\r?\n)?",
                    line,
                ):
                    in_dollar_display = False
                continue
            dollar_markers = list(
                re.finditer(r"(?<!\\)(?<!\$)\$(?!\$)", line)
            )
            if len(dollar_markers) % 2:
                errors.append(
                    f"{document.path}: inline dollar math crosses a physical line"
                )
                break
            for opening, closing in zip(dollar_markers[::2], dollar_markers[1::2]):
                payload = line[opening.end():closing.start()]
                if payload != payload.strip():
                    errors.append(
                        f"{document.path}: inline dollar math has boundary whitespace"
                    )
                    break
                if (
                    REPEATED_SUPERSCRIPT_RE.search(payload)
                    or REPEATED_SUBSCRIPT_RE.search(payload)
                ):
                    errors.append(
                        f"{document.path}: inline math contains a repeated script"
                    )
                    break
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
        expected_rendered = (
            target.get("status") == "defined"
            and reference.get("group_rendered", True)
        )
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
        "math_transcriptions": (
            len(transcriptions.applied_ids) if transcriptions is not None else 0
        ),
    }


def quarto_config(documents: list[Document], has_bibliography: bool = False) -> str:
    chapters = "\n".join(f"    - {document.output}" for document in documents)
    bibliography = "bibliography: references.bib\n\n" if has_bibliography else ""
    return (
        "project:\n  type: book\n\n"
        "book:\n  title: \"PDE: population dynamics of deep learning\"\n"
        "  chapters:\n" + chapters + "\n\n"
        + bibliography
        +
        "number-sections: false\n"
        "crossref:\n  chapters: false\n\n"
        "classoption: enabledeprecatedfontcommands\n"
        "header-includes:\n  - \\usepackage{mathtools}\n"
        "  - \\usepackage{fvextra}\n"
        "  - \\RecustomVerbatimEnvironment{verbatim}{Verbatim}"
        "{breaklines=true,breakanywhere=true}\n"
        "  - \\AtBeginDocument{\\counterwithout{equation}{chapter}"
        "\\counterwithout{theorem}{section}\\counterwithout{lemma}{section}"
        "\\counterwithout{proposition}{section}\\counterwithout{corollary}{section}}\n"
        "format:\n"
        "  html: default\n"
        "  pdf:\n"
        "    pdf-engine: xelatex\n"
        "    keep-tex: true\n"
        "    latex-auto-install: false\n"
        "    latex-tinytex: false\n"
        "    filters:\n"
        "      - pdf_breakable_tables.lua\n"
        "  latex:\n"
        "    filters:\n"
        "      - pdf_breakable_tables.lua\n"
    )


def self_test() -> None:
    tag_only = "x=1.\n\\tag{T1}\n"
    assert remove_spans(tag_only, balanced_tag_spans(tag_only)) == "x=1.\n"
    multi_alignment = r"\begin{split}a&=b,&c&=d\\e&=f,&g&=h\end{split}"
    normalized_alignment = normalize_display_layout(multi_alignment)
    assert normalized_alignment.startswith(r"\begin{aligned}")
    assert normalized_alignment.endswith(r"\end{aligned}")
    assert normalize_display_layout(r"\begin{split}a&=b\\c&=d\end{split}") == (
        r"\begin{aligned}a&=b\\c&=d\end{aligned}"
    )
    assert normalize_math_atom_layout(r"W^{(\ell)}_n^T v") == (
        r"{W^{(\ell)}_n}^{\top} v"
    )
    assert normalize_math_atom_layout(r"c_{\rm primal,\psi}") == (
        r"c_{\mathrm{primal},\psi}"
    )
    assert normalize_math_atom_layout(r"j\backslash q") == r"j\smallsetminus q"
    assert normalize_inline_dollar_boundaries("Use $ x+y $ now.") == (
        "Use $x+y$ now."
    )
    assert separate_markdown_headings("Paragraph.\n### Heading\n") == (
        "Paragraph.\n\n### Heading\n"
    )
    assert separate_markdown_headings("```text\n### literal\n```\n") == (
        "```text\n### literal\n```\n"
    )
    try:
        validate_latex_payload(r"\lVert v\rVert_\mathcal{V}", "test")
    except ValueError as error:
        assert "lacks an outer group" in str(error)
    else:
        raise AssertionError("ungrouped command-valued subscript was accepted")
    assert (
        validate_latex_payload(r"\lVert v\rVert_{\mathcal{V}}", "test")
        == r"\lVert v\rVert_{\mathcal{V}}"
    )
    try:
        validate_latex_payload(r"x^{a}_i^{b}", "test")
    except ValueError as error:
        assert "repeated script" in str(error)
    else:
        raise AssertionError("repeated superscript was accepted")
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

    s = 8. (RM)

A mixed range (R5)–(RM) stays intact until both endpoints are defined.

## III.V Parent

### III.V.3 First relative child

### III.V.6 Last relative child

Under Section III.V, V.3–V.6 is a relative section range.

The scalar derivative m'(2) is not a reference to the display.
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
    multiline_math_state = [False]
    multiline_code_state = [0]
    multiline_inline = convert_prose_line(
        "Use \\(x+y\n", "docs/chapter.md", 1, idx, refs, cites, unresolved,
        multiline_math_state, multiline_code_state,
    ) + convert_prose_line(
        "=z\\) now.\n", "docs/chapter.md", 2, idx, refs, cites, unresolved,
        multiline_math_state, multiline_code_state,
    )
    assert multiline_inline == "Use $x+y =z$ now.\n"
    assert not multiline_math_state[0]
    closing_line_state = [False]
    closing_line_code = [0]
    closing_line_inline = convert_prose_line(
        "Use \\(x+\n", "docs/chapter.md", 1, idx, refs, cites, unresolved,
        closing_line_state, closing_line_code,
    ) + convert_prose_line(
        "y\n", "docs/chapter.md", 2, idx, refs, cites, unresolved,
        closing_line_state, closing_line_code,
    ) + convert_prose_line(
        "\\) now.\n", "docs/chapter.md", 3, idx, refs, cites, unresolved,
        closing_line_state, closing_line_code,
    )
    assert closing_line_inline == "Use $x+ y$ now.\n"
    assert not closing_line_state[0]
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
    assert "derivative m'(2) is not a reference" in chapter
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
    assert {target["number"] for target in pending} == {"R0", "R1", "R2", "RM"}
    assert len({target["id"] for target in pending}) == 4
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
    assert "A mixed range (R5)–(RM) stays intact" in chapter
    rm = next(target for target in pending if target["number"] == "RM")
    mixed_range = [
        reference for reference in refs
        if reference.get("method") == "parenthesized-equation-range"
        and reference.get("target") in {r5["id"], rm["id"]}
        and reference.get("group_rendered") is False
    ]
    assert len(mixed_range) == 2
    assert all(
        reference.get("rendered") is False
        and reference.get("group_rendered") is False
        for reference in mixed_range
    )
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


def build(repo: Path, output: Path, state_path: Path,
          decisions_path: Path | None = None) -> dict:
    paths = discover(repo)
    payload = {path: (repo / path).read_bytes() for path in paths}
    print_filter = PRINT_FILTER.read_bytes()
    documents = [Document(path, payload[path].decode("utf-8")) for path in paths]
    transcriptions = (
        MathTranscriptions(documents, decisions_path) if decisions_path is not None else None
    )
    index = Index(documents)
    if transcriptions is not None:
        index.configure_reference_overrides(transcriptions.reference_overrides)
        index.configure_bibliography(transcriptions.bibliography)
    references: list[dict] = []
    citations: list[dict] = []
    unresolved: list[dict] = []
    outputs = {
        document.path: transform(
            document, index, references, citations, unresolved, transcriptions
        )
        for document in documents
    }
    index.verify_reference_overrides()
    index.verify_bibliography()
    checks = validate(
        documents, outputs, index, references, unresolved, transcriptions
    )
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
    if PRINT_FILTER.read_bytes() != print_filter:
        raise RuntimeError("print filter changed during migration; retry")

    output.mkdir(parents=True, exist_ok=True)
    for document in documents:
        atomic_write(output / document.output, outputs[document.path].encode("utf-8"))
    bibliography_entries = transcriptions.bibliography if transcriptions is not None else []
    if bibliography_entries:
        bibliography_text = "\n\n".join(
            entry["bibtex"].strip() for entry in bibliography_entries
        ) + "\n"
        atomic_write(output / "references.bib", bibliography_text.encode("utf-8"))
    atomic_write(
        output / "_quarto.yml",
        quarto_config(documents, bool(bibliography_entries)).encode("utf-8"),
    )
    atomic_write(output / PRINT_FILTER.name, print_filter)

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
        "support": [
            {
                "source": PRINT_FILTER.relative_to(repo).as_posix(),
                "output": PRINT_FILTER.name,
                "sha256": sha256(print_filter),
            }
        ],
        "unresolved": unresolved,
        "checks": checks,
    }
    if transcriptions is not None:
        state["math_transcription"] = transcriptions.summary
    atomic_write(state_path, (json.dumps(state, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return state


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("self-test")
    prepare_parser = subparsers.add_parser("prepare-math")
    prepare_parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    prepare_parser.add_argument("--batch-dir", type=Path, default=DEFAULT_MATH_BATCH_DIR)
    ingest_parser = subparsers.add_parser("ingest-math")
    ingest_parser.add_argument("--batch-dir", type=Path, default=DEFAULT_MATH_BATCH_DIR)
    ingest_parser.add_argument("--decisions", type=Path, default=DEFAULT_DECISIONS)
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    build_parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    build_parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    build_parser.add_argument("--decisions", type=Path)
    args = parser.parse_args(argv)
    if args.command == "self-test":
        self_test()
        return 0
    if args.command == "prepare-math":
        manifest = prepare_math_batches(args.repo.resolve(), args.batch_dir.resolve())
        print(json.dumps({
            "records": manifest["records"],
            "batches": [
                {"name": batch["name"], "items": batch["items"]}
                for batch in manifest["batches"]
            ],
            "batch_dir": str(args.batch_dir.resolve()),
        }, indent=2))
        return 0
    if args.command == "ingest-math":
        payload = ingest_math_responses(
            args.batch_dir.resolve(), args.decisions.resolve()
        )
        print(json.dumps({
            "decisions": len(payload["items"]),
            "batches": len(payload["batches"]),
            "output": str(args.decisions.resolve()),
        }, indent=2))
        return 0
    state = build(
        args.repo.resolve(), args.output.resolve(), args.state.resolve(),
        args.decisions.resolve() if args.decisions else None,
    )
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
