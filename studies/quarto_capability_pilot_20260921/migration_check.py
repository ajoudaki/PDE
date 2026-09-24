#!/usr/bin/env python3
"""Bounded deterministic checks for linear Quarto migration packets.

This checker proves syntactic/source correspondence properties only.  In
particular, it does not decide whether a reference was assigned to the
scientifically correct target; that remains part of the complete audit.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import posixpath
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


TARGET_KINDS = {
    "sec", "thm", "lem", "prp", "cor", "def", "cnj", "rem", "exm",
    "exr", "sol", "alg", "eq", "proof", "assumption", "part", "eqpart",
    "fig", "tbl",
}
STATEMENT_KINDS = {"thm", "lem", "prp", "cor", "def", "cnj", "rem", "exm", "exr", "sol", "alg"}
EDIT_KINDS = {
    "label", "math-delimiter", "whitespace", "reference", "mermaid-fence",
    "equation-tag", "equation-label", "statement-open", "statement-close",
    "inline-transcription", "display-transcription",
}
ID_RE = re.compile(r"^(?P<kind>[a-z]+)-(?P<key>[a-z0-9-]+)-l(?P<line>[1-9][0-9]*)$")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+.*?(?:[ \t]+\{#([a-z][a-z0-9-]*)\})?[ \t]*$")
LABEL_RE = re.compile(r"\{#([a-z][a-z0-9-]*)\}")
NATIVE_REF_RE = re.compile(r"(?<![A-Za-z0-9_-])@([a-z][a-z0-9-]*)")
LINK_RE = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+\.qmd)#([a-z][a-z0-9-]*)\)")
OLD_LINK_RE = re.compile(r"\[([^\]\n]+)\]\([^)\n]+\)")
DOTTED_TAG_TOKEN = r"[A-Z]\.[0-9]+(?:\.[0-9]+)*(?:\.[A-Z][0-9]+)?"
ROMAN_TAG_TOKEN = r"[IVXLCDM]+\.[A-Z](?:\.[0-9]+)*"
TAG_TOKEN = rf"(?:[A-Z]+[0-9]+[A-Za-z0-9]*|{DOTTED_TAG_TOKEN}|{ROMAN_TAG_TOKEN}|[0-9]+(?:\.[0-9]+)*(?:[a-z])?)"
RAW_NUMBERED_REF_RE = re.compile(rf"(?<![A-Za-z0-9_.])(?:[A-Z]+[0-9]+[A-Za-z0-9]*|{DOTTED_TAG_TOKEN}|{ROMAN_TAG_TOKEN})(?![A-Za-z0-9_]|\.[A-Za-z0-9_])")
NUMBERED_CAPTION_RE = re.compile(rf"(?P<prefix>.*?,\s*)?(?:(?i:sections?)\s+)?{TAG_TOKEN}", re.S)
EQUATION_CAPTION_RE = re.compile(
    r"(?P<prefix>.*?,\s*)?(?:(?i:equations?|formulas?)\s+)?"
    rf"\((?P<number>{TAG_TOKEN})\)", re.S
)
EQUATION_TAG_RE = re.compile(rf"\\tag\{{{TAG_TOKEN}\}}")
THEOREM_MARKER_RE = re.compile(r"\*\*Theorem \((?P<title>[^\n]+)\)\.\*\* ")


def native_reference_text(old: str, target_id: str) -> str | None:
    """Convert only the reference identifier/noun, retaining a mixed caption prefix."""
    noun = r"(?i:equations?|formulas?)" if target_id.startswith("eq-") else r"(?i:sections?)"
    text = re.sub(rf"^{noun}\s+(?=\[)", "", old)
    if not target_id.startswith("eq-"):
        text = re.sub(r"^§{1,2}\s*", "", text)
    link = OLD_LINK_RE.fullmatch(text)
    caption = link.group(1) if link else text
    pattern = EQUATION_CAPTION_RE if target_id.startswith("eq-") else NUMBERED_CAPTION_RE
    match = pattern.fullmatch(caption)
    return (match.group("prefix") or "") + "@" + target_id if match else None


def equation_reference_number(old: str) -> str | None:
    text = re.sub(r"^(?i:equations?|formulas?)\s+(?=\[)", "", old)
    link = OLD_LINK_RE.fullmatch(text)
    match = EQUATION_CAPTION_RE.fullmatch(link.group(1) if link else text)
    return match.group("number") if match else None


class CheckFailure(Exception):
    """Raised for malformed top-level inputs that cannot be inspected further."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CheckFailure(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CheckFailure(f"cannot read JSON {path}: {exc}") from exc


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_excerpt(text: str, start: int, end: int) -> str:
    lines = text.splitlines(keepends=True)
    if start < 1 or end < start or end > len(lines):
        raise CheckFailure(f"packet range {start}:{end} is outside 1:{len(lines)}")
    return "".join(lines[start - 1 : end])


def apply_edits(original: str, edits: list[dict[str, Any]]) -> str:
    pieces: list[str] = []
    cursor = 0
    for index, edit in enumerate(edits):
        offset = edit["offset"]
        old = edit["old"]
        if offset < cursor:
            raise CheckFailure(f"edit {index} overlaps or is out of order")
        if offset > len(original) or not original.startswith(old, offset):
            raise CheckFailure(f"edit {index} old text does not match source at offset {offset}")
        pieces.extend((original[cursor:offset], edit["new"]))
        cursor = offset + len(old)
    pieces.append(original[cursor:])
    return "".join(pieces)


def _replayed_edit_positions(original: str, edits: list[dict[str, Any]]) -> list[int]:
    """Return each edit's start offset in the exact replayed candidate."""
    delta = 0
    positions: list[int] = []
    cursor = 0
    for index, edit in enumerate(edits):
        offset, old = edit["offset"], edit["old"]
        if offset < cursor or offset > len(original) or not original.startswith(old, offset):
            raise CheckFailure(f"edit {index} cannot be positioned in replay")
        positions.append(offset + delta)
        delta += len(edit["new"]) - len(old)
        cursor = offset + len(old)
    return positions


def _project_transcriptions(
    original: str, candidate: str, edits: list[dict[str, Any]]
) -> str:
    """Reverse only declared transcription replacements at replayed offsets."""
    positions = _replayed_edit_positions(original, edits)
    projected = candidate
    replacements = [
        (positions[index], edit["new"], edit["old"])
        for index, edit in enumerate(edits)
        if edit["kind"] in {"inline-transcription", "display-transcription"}
    ]
    for position, new, old in reversed(replacements):
        if not projected.startswith(new, position):
            raise CheckFailure("candidate transcription does not match its replayed replacement")
        projected = projected[:position] + old + projected[position + len(new):]
    return projected


def _line_number_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _line_bounds(text: str, offset: int) -> tuple[int, int]:
    start = text.rfind("\n", 0, offset) + 1
    end = text.find("\n", offset)
    return start, len(text) if end == -1 else end


def _line_offsets(text: str) -> list[int]:
    offsets = [0]
    offsets.extend(match.end() for match in re.finditer("\n", text))
    if offsets[-1] != len(text):
        offsets.append(len(text))
    return offsets


def _target_bounds_in_excerpt(
    original: str, packet_start: int, target: dict[str, Any]
) -> tuple[int, int] | None:
    offsets = _line_offsets(original)
    first = target["start"] - packet_start
    last = target["end"] - packet_start
    if first < 0 or last + 1 >= len(offsets):
        return None
    return offsets[first], offsets[last + 1]


def _equation_block(text: str) -> re.Match[str] | None:
    return re.fullmatch(rf"[ \t]*\\\[(?P<payload>.*?)\\\][ \t]*(?:\\tag\{{{TAG_TOKEN}\}})?[ \t]*(?:\n)?", text, re.S)


def _theorem_marker(text: str) -> re.Match[str] | None:
    return THEOREM_MARKER_RE.match(text)


def _indented_lines(text: str) -> list[str]:
    return text.splitlines()


def _indented_annotations(text: str) -> list[str]:
    """Return all terminal parenthesized source numbers in an ASCII block."""
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    return [
        match.group("number")
        for line in lines
        for match in [re.search(rf"\((?P<number>{TAG_TOKEN})\)\s*$", line)]
        if match is not None
    ]


def _indented_annotation(text: str) -> str | None:
    """Return the sole terminal parenthesized source number, if unique."""
    annotations = _indented_annotations(text)
    return annotations[0] if len(annotations) == 1 else None


def _complete_indented_block(text: str, offset: int, old: str) -> bool:
    """Check that an edit consumes one whole indented block in its source."""
    lines = _indented_lines(old)
    if not lines or any(not line.strip() or not line.startswith(("    ", "\t")) for line in lines):
        return False
    line_start, _ = _line_bounds(text, offset)
    if offset != line_start:
        return False
    before = text[:offset]
    after = text[offset + len(old):]
    previous = before[before.rfind("\n", 0, max(0, len(before) - 1)) + 1:]
    after = after.lstrip("\n")
    next_end = after.find("\n")
    following = after if next_end < 0 else after[:next_end]
    if previous.strip() and previous.startswith(("    ", "\t")):
        return False
    if following.strip() and following.startswith(("    ", "\t")):
        return False
    return True


def _raw_inline_splits_identifier(original: str, offset: int, old: str) -> bool:
    """Reject a raw span that starts or ends inside an alphabetic identifier."""
    content = old
    if content.startswith("$") and content.endswith("$"):
        content = content[1:-1]
    left_split = (
        bool(content) and content[0].isalpha() and offset > 0
        and original[offset - 1].isalpha()
    )
    right = offset + len(old)
    right_split = (
        bool(content) and content[-1].isalpha() and right < len(original)
        and original[right].isalpha()
    )
    return left_split or right_split


def _detached_derivative_prime(math: str) -> bool:
    """Reject atom\prime; derivative primes need an apostrophe or superscript."""
    return re.search(r"(?:[A-Za-z]|\\[A-Za-z]+)\\prime\b", math) is not None


_GREEK_NAME_RE = re.compile(
    r"(?<!\\)\b(?:alpha|beta|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|"
    r"iota|kappa|lambda|mu|nu|xi|omicron|pi|varpi|rho|varrho|sigma|varsigma|tau|"
    r"upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|"
    r"Phi|Psi|Omega)\b"
)
_ASCII_OPERATOR_RE = re.compile(r"(?<!\\)\b(?:sqrt|exp|sum|prod|log|tanh|cosh|clip)(?:\b\s*(?=[(^{])|(?=_))")
_DOUBLE_ESCAPED_TEX_RE = re.compile(r"\\\\(?:[A-Za-z]+|[^A-Za-z\s])")


def _retained_ascii_pseudo_math(math: str) -> str | None:
    """Find an unequivocal raw ASCII math token in a new transcription."""
    protected = re.sub(r"\\(?:text|operatorname)\{[^{}]*\}", " ", math)
    if "||" in protected:
        return "ASCII norm bars ||"
    if "<=" in protected or ">=" in protected:
        return "ASCII comparison operator"
    if _GREEK_NAME_RE.search(protected):
        return "unescaped Greek name"
    if _ASCII_OPERATOR_RE.search(protected):
        return "ASCII math operator"
    return None


def _double_escaped_tex(math: str) -> bool:
    return _DOUBLE_ESCAPED_TEX_RE.search(math) is not None


def _range_padding(old: str, new: str, native: str, original: str, offset: int) -> bool:
    """Allow one added space on either side only when it separates an original --."""
    left_ok = original[max(0, offset - 2):offset] == "--"
    right = offset + len(old)
    right_ok = original[right:right + 2] == "--"
    allowed = {native}
    if left_ok:
        allowed.add(" " + native)
    if right_ok:
        allowed.add(native + " ")
    if left_ok and right_ok:
        allowed.add(" " + native + " ")
    return new in allowed


def _equation_tag_replacement(original: str, offset: int, old: str) -> str:
    line_start, line_end = _line_bounds(original, offset)
    tag_only = (
        not original[line_start:offset].strip()
        and not original[offset + len(old):line_end].strip()
    )
    return "%" if tag_only else ""


def validate_edit_schema(edits: Any, errors: list[str]) -> list[dict[str, Any]]:
    if not isinstance(edits, list):
        errors.append("edits must be a JSON list")
        return []
    required = {"offset", "old", "new", "kind"}
    allowed = required | {"target"}
    valid: list[dict[str, Any]] = []
    for index, edit in enumerate(edits):
        if not isinstance(edit, dict):
            errors.append(f"edit {index} must be an object")
            continue
        missing = required - edit.keys()
        extra = edit.keys() - allowed
        if missing:
            errors.append(f"edit {index} missing fields: {sorted(missing)}")
        if extra:
            errors.append(f"edit {index} unsupported fields: {sorted(extra)}")
        if missing or extra:
            continue
        if not isinstance(edit["offset"], int) or isinstance(edit["offset"], bool) or edit["offset"] < 0:
            errors.append(f"edit {index} offset must be a nonnegative integer")
            continue
        if not isinstance(edit["old"], str) or not isinstance(edit["new"], str):
            errors.append(f"edit {index} old/new must be strings")
            continue
        if edit["kind"] not in EDIT_KINDS:
            errors.append(f"edit {index} has unsupported kind {edit['kind']!r}")
            continue
        if "target" in edit and not isinstance(edit["target"], str):
            errors.append(f"edit {index} target must be a string")
            continue
        valid.append(edit)
    return valid


def validate_target_list(value: Any, label: str, manifest: dict[str, dict[str, Any]], errors: list[str]) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        errors.append(f"{label} must be a JSON list")
        return []
    result: list[dict[str, Any]] = []
    required = {"id", "kind", "source", "start", "end"}
    for index, target in enumerate(value):
        where = f"{label}[{index}]"
        if not isinstance(target, dict) or set(target) != required:
            errors.append(f"{where} must have exactly {sorted(required)}")
            continue
        if any(not isinstance(target[name], str) for name in ("id", "kind", "source")):
            errors.append(f"{where} id/kind/source must be strings")
            continue
        if target["kind"] not in TARGET_KINDS:
            errors.append(f"{where} has unsupported kind {target['kind']!r}")
            continue
        entry = manifest.get(target["source"])
        if entry is None:
            errors.append(f"{where} names unknown source {target['source']!r}")
            continue
        if any(not isinstance(target[name], int) or isinstance(target[name], bool) for name in ("start", "end")):
            errors.append(f"{where} start/end must be integers")
            continue
        if not (1 <= target["start"] <= target["end"] <= entry["lines"]):
            errors.append(f"{where} range is outside source bounds")
            continue
        if target["kind"] == "sec" and target["start"] != target["end"]:
            errors.append(f"{where} section range must be its single heading line")
        expected = f"{target['kind']}-{entry['key']}-l{target['start']}"
        if target["id"] != expected:
            errors.append(f"{where} id must be {expected!r}")
        match = ID_RE.fullmatch(target["id"]) if isinstance(target["id"], str) else None
        if match is None:
            errors.append(f"{where} has malformed id")
        result.append(target)
    return result


def validate_target_relations(registry: list[dict[str, Any]], proposed: list[dict[str, Any]], errors: list[str]) -> None:
    seen_ids: dict[str, tuple[str, int, int, str]] = {}
    seen_objects: dict[tuple[str, str, int, int], str] = {}
    tagged = [("registry", t) for t in registry] + [("proposed", t) for t in proposed]
    for origin, target in tagged:
        signature = (target["source"], target["start"], target["end"], target["kind"])
        previous = seen_ids.get(target["id"])
        if previous is not None:
            errors.append(f"target id {target['id']!r} is reused ({previous} vs {signature})")
        else:
            seen_ids[target["id"]] = signature
        obj = (target["source"], target["kind"], target["start"], target["end"])
        if obj in seen_objects:
            errors.append(f"target object {obj} is duplicated as {seen_objects[obj]!r} and {target['id']!r}")
        else:
            seen_objects[obj] = target["id"]

    for pos, (origin_a, a) in enumerate(tagged):
        for origin_b, b in tagged[pos + 1 :]:
            if a["source"] != b["source"]:
                continue
            overlap = max(a["start"], b["start"]) <= min(a["end"], b["end"])
            if not overlap:
                continue
            same_span = a["start"] == b["start"] and a["end"] == b["end"]
            if a["kind"] == b["kind"]:
                errors.append(f"same-kind targets overlap: {a['id']} and {b['id']}")
                continue
            if same_span and a["kind"] in STATEMENT_KINDS and b["kind"] in STATEMENT_KINDS:
                errors.append(f"statement targets conflict on the same span: {a['id']} and {b['id']}")
                continue
            a_contains_b = a["start"] <= b["start"] and a["end"] >= b["end"]
            b_contains_a = b["start"] <= a["start"] and b["end"] >= a["end"]
            if not (a_contains_b or b_contains_a):
                errors.append(f"target intervals cross: {a['id']} and {b['id']}")


def validate_edit_grammars(original: str, edits: list[dict[str, Any]], targets: dict[str, dict[str, Any]], packet_start: int, errors: list[str], packet_source: str | None = None) -> None:
    paired = {"equation-tag", "equation-label", "statement-open", "statement-close"}
    counts: dict[str, dict[str, int]] = {}
    for index, edit in enumerate(edits):
        kind, old, new, offset = edit["kind"], edit["old"], edit["new"], edit["offset"]
        target_id = edit.get("target")
        if kind in {"label", "reference"} | paired and not target_id:
            errors.append(f"edit {index} kind {kind} requires target")
            continue
        if kind not in {"label", "reference", "display-transcription"} | paired and target_id is not None:
            errors.append(f"edit {index} kind {kind} may not carry target")
        if target_id is not None and target_id not in targets:
            errors.append(f"edit {index} names unknown target {target_id!r}")
            continue
        target = targets.get(target_id)
        if kind in paired | {"display-transcription"} and target_id is not None:
            target_counts = counts.setdefault(target_id, {})
            target_counts[kind] = target_counts.get(kind, 0) + 1
        if kind == "math-delimiter":
            if (old, new) not in {(r"\[", "$$"), (r"\]", "$$"), (r"\(", "$"), (r"\)", "$")}:
                errors.append(f"edit {index} is not a permitted delimiter conversion")
        elif kind == "inline-transcription":
            code_span = old.startswith("`") or old.endswith("`")
            valid_code_span = code_span and old.startswith("`") and old.endswith("`") and old.count("`") == 2
            valid_plain = not code_span and bool(old.strip())
            valid_new = (
                new.startswith("$") and new.endswith("$")
                and not new.startswith("$$") and not new.endswith("$$")
                and bool(new[1:-1].strip()) and "\n\n" not in old
            )
            if not (valid_code_span or valid_plain) or not valid_new or "\n\n" in old:
                errors.append(f"edit {index} inline transcription must be a nonempty one-paragraph math span")
            elif valid_plain and _raw_inline_splits_identifier(original, offset, old):
                errors.append(f"edit {index} raw inline transcription splits an alphabetic identifier")
            if valid_new and _detached_derivative_prime(new[1:-1]):
                errors.append(f"edit {index} transcription detaches a derivative prime from its atom")
            if valid_new:
                pseudo = _retained_ascii_pseudo_math(new[1:-1])
                if pseudo is not None:
                    errors.append(f"edit {index} transcription retains {pseudo}")
                if _double_escaped_tex(new[1:-1]):
                    errors.append(f"edit {index} inline transcription contains double-escaped TeX")
        elif kind == "display-transcription":
            complete_indented = _complete_indented_block(original, offset, old)
            display = re.fullmatch(
                r"\$\$(?P<body>.*?)\$\$(?: \{#(?P<label>[a-z][a-z0-9-]*)\})?",
                new,
                re.S,
            )
            annotations = _indented_annotations(old)
            annotation = annotations[0] if len(annotations) == 1 else None
            label = None if display is None else display.group("label")
            if not complete_indented or display is None or not display.group("body").strip():
                errors.append(f"edit {index} display transcription must be a complete indented display")
            elif _detached_derivative_prime(display.group("body")):
                errors.append(f"edit {index} transcription detaches a derivative prime from its atom")
            if display is not None:
                pseudo = _retained_ascii_pseudo_math(display.group("body"))
                if pseudo is not None:
                    errors.append(f"edit {index} transcription retains {pseudo}")
            if len(annotations) > 1:
                errors.append(f"edit {index} indented display has unsupported multiple original equation annotations")
            if annotation is not None and target_id is None:
                errors.append(f"edit {index} numbered indented display requires an equation target")
            if annotation is None and target_id is not None:
                errors.append(f"edit {index} unnumbered indented display may not name an equation target")
            if target_id is not None:
                bounds = _target_bounds_in_excerpt(original, packet_start, target)
                if (target is None or target["kind"] != "eq"
                        or (packet_source is not None and target["source"] != packet_source)
                        or bounds is None
                        or bounds[0] != offset
                        or original[offset:bounds[1]] not in {old, old + "\n"}
                        or label != target_id):
                    errors.append(f"edit {index} display transcription target must match its complete source block and label")
        elif kind == "mermaid-fence":
            line_start, line_end = _line_bounds(original, offset)
            if old != '```mermaid' or new != '```{mermaid}' or offset != line_start or original[line_start:line_end] != old:
                errors.append(f"edit {index} must convert only an exact Mermaid opening fence")
        elif kind == "whitespace":
            if re.fullmatch(r"\n*", old) is None or re.fullmatch(r"\n+", new) is None:
                errors.append(f"edit {index} whitespace edits may only adjust LF blank lines and must retain a line break")
            left = original[:offset].rstrip("\n")
            right = original[offset + len(old):].lstrip("\n")
            if not (left.endswith((r"\[", r"\]")) or right.startswith((r"\[", r"\]"))):
                errors.append(f"edit {index} whitespace edit is not adjacent to a display delimiter")
        elif kind == "label":
            expected = f" {{#{target_id}}}"
            if old != "" or new != expected:
                errors.append(f"edit {index} label must insert exactly {expected!r}")
            line_start, line_end = _line_bounds(original, offset)
            line = original[line_start:line_end]
            if offset != line_end or not HEADING_RE.fullmatch(line) or LABEL_RE.search(line):
                errors.append(f"edit {index} label is not at the end of an unlabeled ATX heading")
            absolute_line = packet_start + _line_number_at(original, offset) - 1
            if target and (target["kind"] != "sec" or (packet_source is not None and target["source"] != packet_source) or target["start"] != absolute_line or target["end"] != absolute_line):
                errors.append(f"edit {index} label does not match its section source line")
        elif kind == "equation-tag":
            bounds = _target_bounds_in_excerpt(original, packet_start, target) if target else None
            if target is None or target["kind"] != "eq" or (packet_source is not None and target["source"] != packet_source):
                errors.append(f"edit {index} equation tag does not name an equation in the packet source")
            replacement = _equation_tag_replacement(original, offset, old)
            if new != replacement or EQUATION_TAG_RE.fullmatch(old) is None:
                errors.append(f"edit {index} equation tag must use the exact deletion/comment replacement")
            if bounds is None or not (bounds[0] <= offset and offset + len(old) <= bounds[1]):
                errors.append(f"edit {index} equation tag is outside its complete equation span")
        elif kind == "equation-label":
            bounds = _target_bounds_in_excerpt(original, packet_start, target) if target else None
            expected = f" {{#{target_id}}}"
            block = _equation_block(original[bounds[0]:bounds[1]]) if bounds else None
            closing = bounds[0] + block.end("payload") + len(r"\]") if bounds and block else None
            if target is None or target["kind"] != "eq" or (packet_source is not None and target["source"] != packet_source):
                errors.append(f"edit {index} equation label does not name an equation in the packet source")
            if old != "" or new != expected or closing != offset:
                errors.append(f"edit {index} equation label must follow its complete display closing delimiter")
        elif kind == "statement-open":
            marker = _theorem_marker(old)
            expected = None if marker is None else f"::: {{#{target_id}}}\n## {marker.group('title')}\n\n"
            line_start, _ = _line_bounds(original, offset)
            absolute_line = packet_start + _line_number_at(original, offset) - 1
            if target is None or target["kind"] != "thm" or (packet_source is not None and target["source"] != packet_source):
                errors.append(f"edit {index} statement open does not name a theorem in the packet source")
            if marker is None or marker.group(0) != old or new != expected:
                errors.append(f"edit {index} statement open must preserve the exact original theorem title")
            if target and (offset != line_start or absolute_line != target["start"]):
                errors.append(f"edit {index} statement open is not at the theorem span start")
        elif kind == "statement-close":
            line_start, line_end = _line_bounds(original, offset)
            absolute_line = packet_start + _line_number_at(original, offset) - 1
            if target is None or target["kind"] != "thm" or (packet_source is not None and target["source"] != packet_source):
                errors.append(f"edit {index} statement close does not name a theorem in the packet source")
            if old != "" or new != "\n\n:::" or offset != line_end or offset >= len(original) or original[offset] != "\n":
                errors.append(f"edit {index} statement close must precede the final statement line break")
            if target and (absolute_line != target["end"] or line_start == line_end):
                errors.append(f"edit {index} statement close is not at the theorem span end")
        elif kind == "reference":
            native = native_reference_text(old, target_id)
            if native is not None and _range_padding(old, new, native, original, offset):
                pass
            elif new == f"@{target_id}":
                errors.append(f"edit {index} native reference must preserve any descriptive prefix")
            else:
                match = LINK_RE.fullmatch(new)
                old_match = OLD_LINK_RE.fullmatch(old)
                old_caption = old_match.group(1) if old_match else old
                if native is not None:
                    errors.append(f"edit {index} numbered reference must use native @ID syntax")
                if match is None or match.group(1) != old_caption or match.group(3) != target_id:
                    errors.append(f"edit {index} descriptive link must preserve its caption and target ID")

    packet_end = packet_start + len(original.splitlines()) - 1
    for target_id, target in targets.items():
        if packet_source is not None and target["source"] != packet_source:
            continue
        if not (packet_start <= target["start"] <= target["end"] <= packet_end):
            continue
        target_counts = counts.get(target_id, {})
        if target["kind"] == "eq":
            bounds = _target_bounds_in_excerpt(original, packet_start, target)
            span = original[bounds[0]:bounds[1]] if bounds is not None else ""
            required = (("display-transcription",) if _complete_indented_block(span, 0, span)
                        else ("equation-tag", "equation-label"))
        else:
            required = ("statement-open", "statement-close") if target["kind"] == "thm" else ()
        for kind in required:
            if target_counts.get(kind, 0) != 1:
                errors.append(f"covered {target['kind']} target {target_id!r} requires exactly one {kind} edit")
    for display in re.finditer(re.escape(r"\[") + r"(.*?)" + re.escape(r"\]"), original, re.S):
        if EQUATION_TAG_RE.search(display.group(1)) is None:
            continue
        start_line = packet_start + _line_number_at(original, display.start()) - 1
        end_line = packet_start + _line_number_at(original, display.end() - 1) - 1
        matches = [
            target for target in targets.values()
            if target["kind"] == "eq" and (packet_source is None or target["source"] == packet_source)
            and target["start"] == start_line and target["end"] == end_line
        ]
        if len(matches) != 1:
            errors.append(f"tagged display at {packet_source or '<packet>'}:{start_line}-{end_line} lacks its unique equation target")


def _display_payloads(text: str, opener: str, closer: str) -> list[str]:
    pattern = re.compile(re.escape(opener) + r"(.*?)" + re.escape(closer), re.DOTALL)
    return [match.group(1) for match in pattern.finditer(text)]


def _normalized_source_displays(
    original: str, edits: list[dict[str, Any]], targets: dict[str, dict[str, Any]],
    packet_start: int, packet_source: str,
) -> list[str]:
    valid: list[dict[str, Any]] = []
    for edit in edits:
        target = targets.get(edit.get("target"))
        if edit["kind"] != "equation-tag" or target is None or target["kind"] != "eq":
            continue
        bounds = _target_bounds_in_excerpt(original, packet_start, target)
        if (target["source"] == packet_source and bounds is not None
                and edit["new"] == _equation_tag_replacement(original, edit["offset"], edit["old"])
                and EQUATION_TAG_RE.fullmatch(edit["old"])
                and bounds[0] <= edit["offset"] and edit["offset"] + len(edit["old"]) <= bounds[1]):
            valid.append(edit)
    return _display_payloads(apply_edits(original, sorted(valid, key=lambda item: item["offset"])), r"\[", r"\]")


def validate_math_target_sources(
    targets: list[dict[str, Any]], manifest: dict[str, dict[str, Any]], repo_root: Path,
    errors: list[str],
) -> dict[str, str]:
    """Validate equation/theorem spans against the complete frozen sources."""
    cache: dict[str, list[str]] = {}
    equation_numbers: dict[str, str] = {}
    for target in targets:
        if target["kind"] not in {"eq", "thm"}:
            continue
        source = target["source"]
        if source not in cache:
            cache[source] = (repo_root / manifest[source]["frozen"]).read_text(encoding="utf-8").splitlines(keepends=True)
        lines = cache[source]
        span = "".join(lines[target["start"] - 1:target["end"]])
        if target["kind"] == "eq":
            block = _equation_block(span)
            tags = [] if block is None else EQUATION_TAG_RE.findall(block.group("payload"))
            if block is not None:
                if len(tags) != 1:
                    errors.append(f"equation target {target['id']!r} must span one complete tagged display")
                else:
                    equation_numbers[target["id"]] = tags[0][5:-1]
            else:
                indented = _complete_indented_block(span, 0, span)
                annotations = _indented_annotations(span)
                annotation = annotations[0] if len(annotations) == 1 else None
                if len(annotations) > 1:
                    errors.append(f"equation target {target['id']!r} has unsupported multiple original equation annotations")
                elif not indented or annotation is None:
                    if span.lstrip().startswith(r"\["):
                        errors.append(f"equation target {target['id']!r} must span one complete tagged display")
                    else:
                        errors.append(f"equation target {target['id']!r} must span one complete indented numbered block")
                else:
                    equation_numbers[target["id"]] = annotation
        else:
            marker = _theorem_marker(span)
            final_line = lines[target["end"] - 1].rstrip("\r\n")
            if marker is None or marker.start() != 0:
                errors.append(f"theorem target {target['id']!r} must begin at its exact named marker")
            if not final_line.strip():
                errors.append(f"theorem target {target['id']!r} ends on a blank line")
    return equation_numbers


def _candidate_headings(candidate: str, targets: dict[str, dict[str, Any]]) -> list[str]:
    """Return structural headings, excluding exact theorem-title metadata."""
    lines = candidate.splitlines()
    result: list[str] = []
    in_fence = False
    for index, line in enumerate(lines):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.fullmatch(line)
        if not match:
            continue
        generated = False
        if index and line.startswith("## "):
            div = re.fullmatch(r"::: \{#([a-z][a-z0-9-]*)\}", lines[index - 1])
            target = targets.get(div.group(1)) if div else None
            generated = target is not None and target["kind"] in STATEMENT_KINDS
        if not generated:
            result.append(re.sub(r"[ \t]+\{#[a-z][a-z0-9-]*\}[ \t]*$", "", line))
    return result


def _reference_prose(text: str) -> str:
    text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    text = re.sub(r"(?<![\\$])\$(?!\$).*?(?<!\\)\$(?!\$)", "", text, flags=re.S)
    return "\n".join("" if HEADING_RE.fullmatch(line) else line for line in text.splitlines())


def _next_coordinate(source: str, end: int, ordered: list[dict[str, Any]]) -> tuple[str, int]:
    index = next((i for i, entry in enumerate(ordered) if entry["source"] == source), -1)
    if index < 0:
        raise CheckFailure(f"progress names source absent from manifest: {source!r}")
    if end < ordered[index]["lines"]:
        return source, end + 1
    if index + 1 >= len(ordered):
        raise CheckFailure("accepted prefix already reaches the end of the manifest")
    return ordered[index + 1]["source"], 1


def validate_progress(
    value: Any,
    ordered_manifest: list[dict[str, Any]],
    packet_dir: Path,
    registry_path: Path,
    errors: list[str],
) -> tuple[list[dict[str, Any]], tuple[str, int]]:
    if not isinstance(value, dict) or set(value) != {"accepted"} or not isinstance(value["accepted"], list):
        errors.append("progress must be an object with exactly one accepted list")
        return [], (ordered_manifest[0]["source"], 1)
    accepted: list[dict[str, Any]] = []
    expected = (ordered_manifest[0]["source"], 1)
    required = {"packet", "source", "start", "end", "candidate", "candidate_sha256"}
    for index, item in enumerate(value["accepted"]):
        where = f"progress.accepted[{index}]"
        if not isinstance(item, dict) or not (required <= set(item) <= required | {"registry_sha256"}):
            errors.append(f"{where} has invalid fields")
            continue
        if not re.fullmatch(r"linear_[0-9]{3}", item.get("packet", "")):
            errors.append(f"{where} has invalid packet id")
        if (item.get("source"), item.get("start")) != expected:
            errors.append(f"{where} breaks accepted-prefix continuity; expected {expected[0]}:{expected[1]}")
        entry = next((entry for entry in ordered_manifest if entry["source"] == item.get("source")), None)
        if entry is None or not isinstance(item.get("start"), int) or not isinstance(item.get("end"), int) or not (1 <= item["start"] <= item["end"] <= entry["lines"]):
            errors.append(f"{where} has invalid source range")
            continue
        candidate_name = item.get("candidate")
        if not isinstance(candidate_name, str) or Path(candidate_name).is_absolute():
            errors.append(f"{where} candidate must be a relative path")
        else:
            candidate_path = packet_dir / candidate_name
            try:
                if sha256(candidate_path) != item.get("candidate_sha256"):
                    errors.append(f"{where} accepted candidate hash mismatch")
            except OSError as exc:
                errors.append(f"{where} accepted candidate is unreadable: {exc}")
        accepted.append(item)
        try:
            expected = _next_coordinate(item["source"], item["end"], ordered_manifest)
        except CheckFailure as exc:
            if index != len(value["accepted"]) - 1:
                errors.append(str(exc))
    if accepted and "registry_sha256" in accepted[-1]:
        try:
            if sha256(registry_path) != accepted[-1]["registry_sha256"]:
                errors.append("registry hash differs from the latest accepted receipt")
        except OSError as exc:
            errors.append(f"registry is unreadable: {exc}")
    return accepted, expected


def validate_packet(packet_path: Path, repo_root: Path | None = None) -> dict[str, Any]:
    errors: list[str] = []
    packet_dir = packet_path.resolve().parent
    repo_root = repo_root or Path(__file__).resolve().parents[2]
    packet = load_json(packet_path)
    required_packet = {"id", "source", "start", "end", "candidate", "edits", "targets", "sources", "registry", "progress"}
    if not isinstance(packet, dict) or set(packet) != required_packet:
        raise CheckFailure(f"packet must have exactly {sorted(required_packet)}")
    if not isinstance(packet["id"], str) or not re.fullmatch(r"linear_[0-9]{3}", packet["id"]):
        errors.append("packet id must have form linear_NNN")
    if any(not isinstance(packet[name], str) for name in ("source", "candidate", "edits", "targets", "sources", "registry", "progress")):
        raise CheckFailure("packet path/source fields must be strings")
    for name in ("candidate", "edits", "targets", "sources", "registry", "progress"):
        path = Path(packet[name])
        if path.is_absolute() or ".." in path.parts:
            errors.append(f"packet {name} path must stay relative to the packet directory")
    if any(not isinstance(packet[name], int) or isinstance(packet[name], bool) for name in ("start", "end")):
        raise CheckFailure("packet start/end must be integers")

    sources_path = packet_dir / packet["sources"]
    sources_doc = load_json(sources_path)
    if not isinstance(sources_doc, dict) or sources_doc.get("version") != 1 or not isinstance(sources_doc.get("files"), list):
        raise CheckFailure("source manifest must be version 1 with a files list")
    manifest: dict[str, dict[str, Any]] = {}
    ordered_manifest: list[dict[str, Any]] = []
    for index, entry in enumerate(sources_doc["files"]):
        needed = {"source", "key", "qmd", "sha256", "lines", "frozen"}
        if not isinstance(entry, dict) or not needed <= entry.keys():
            errors.append(f"manifest entry {index} is malformed")
            continue
        if any(not isinstance(entry[name], str) for name in ("source", "key", "qmd", "sha256", "frozen")) or not isinstance(entry["lines"], int):
            errors.append(f"manifest entry {index} has invalid field types")
            continue
        source_path = PurePosixPath(entry["source"])
        frozen_path = PurePosixPath(entry["frozen"])
        if source_path.is_absolute() or ".." in source_path.parts or frozen_path.is_absolute() or ".." in frozen_path.parts:
            errors.append(f"manifest entry {index} source/frozen paths must be bounded relative paths")
            continue
        if entry["lines"] < 1:
            errors.append(f"manifest entry {index} must describe a nonempty full source")
        if entry["source"] in manifest:
            errors.append(f"manifest source {entry['source']!r} is duplicated")
        manifest[entry["source"]] = entry
        ordered_manifest.append(entry)
        frozen = repo_root / entry["frozen"]
        try:
            actual_hash = sha256(frozen)
            actual_lines = len(frozen.read_text(encoding="utf-8").splitlines())
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read frozen source {entry['frozen']}: {exc}")
            continue
        if actual_hash != entry["sha256"]:
            errors.append(f"frozen hash mismatch for {entry['source']}")
        if actual_lines != entry["lines"]:
            errors.append(f"frozen line-count mismatch for {entry['source']}")

    source_entry = manifest.get(packet["source"])
    if source_entry is None:
        raise CheckFailure(f"packet source {packet['source']!r} is absent from manifest")
    frozen_path = repo_root / source_entry["frozen"]
    frozen_text = frozen_path.read_text(encoding="utf-8")
    original = source_excerpt(frozen_text, packet["start"], packet["end"])

    registry_path = packet_dir / packet["registry"]
    registry_raw = load_json(registry_path)
    accepted, expected_coordinate = validate_progress(
        load_json(packet_dir / packet["progress"]), ordered_manifest, packet_dir, registry_path, errors
    )
    if (packet["source"], packet["start"]) != expected_coordinate:
        errors.append(
            f"packet breaks accepted-prefix continuity; expected {expected_coordinate[0]}:{expected_coordinate[1]}"
        )
    proposed_raw = load_json(packet_dir / packet["targets"])
    registry = validate_target_list(registry_raw, "registry", manifest, errors)
    proposed = validate_target_list(proposed_raw, "proposed", manifest, errors)
    validate_target_relations(registry, proposed, errors)
    combined = registry + proposed
    by_id = {target["id"]: target for target in combined}
    equation_numbers = validate_math_target_sources(combined, manifest, repo_root, errors)

    edits_raw = load_json(packet_dir / packet["edits"])
    edits = validate_edit_schema(edits_raw, errors)
    candidate_path = packet_dir / packet["candidate"]
    try:
        candidate = candidate_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise CheckFailure(f"cannot read candidate {candidate_path}: {exc}") from exc
    if len(edits) == len(edits_raw) if isinstance(edits_raw, list) else False:
        try:
            replayed = apply_edits(original, edits)
            if replayed != candidate:
                errors.append("candidate does not equal exact ordered edit replay")
        except CheckFailure as exc:
            errors.append(str(exc))
    validate_edit_grammars(original, edits, by_id, packet["start"], errors, packet["source"])
    try:
        projected_candidate = _project_transcriptions(original, candidate, edits)
    except CheckFailure as exc:
        projected_candidate = candidate
        errors.append(str(exc))

    # Headings are unchanged except for the one permitted terminal label.
    source_headings = []
    in_fence = False
    for line in original.splitlines(keepends=True):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and HEADING_RE.fullmatch(line.rstrip("\r\n")):
            source_headings.append(line.rstrip("\r\n"))
    candidate_headings = _candidate_headings(projected_candidate, by_id)
    if source_headings != candidate_headings:
        errors.append("heading text, levels, or order changed")

    # The only mathematical payload change allowed is delimiter spelling.
    if _normalized_source_displays(original, edits, by_id, packet["start"], packet["source"]) != _display_payloads(projected_candidate, "$$", "$$"):
        errors.append("display-math payloads or order changed")
    if original.count(r"\[") != original.count(r"\]") or candidate.count("$$") % 2:
        errors.append("unbalanced display delimiters")
    without_displays = re.sub(r'\$\$.*?\$\$', '', projected_candidate, flags=re.S)
    inline_payloads = re.findall(r'(?<![\\$])\$(?!\$)(.*?)(?<!\\)\$(?!\$)', without_displays, flags=re.S)
    if _display_payloads(original, r"\(", r"\)") != inline_payloads:
        errors.append('inline-math payloads or order changed')
    # Fenced diagrams/code and ordinary code spans are immutable apart from the
    # explicitly allowed opening-fence spelling. This also protects code-form math.
    source_fences = re.findall(r'^```(?:\{mermaid\}|mermaid)?[^\n]*\n(.*?)^```\s*$', original, re.M|re.S)
    new_fences = re.findall(r'^```(?:\{mermaid\}|mermaid)?[^\n]*\n(.*?)^```\s*$', projected_candidate, re.M|re.S)
    if source_fences != new_fences:
        errors.append('fenced block contents changed')
    strip_fences = lambda text: re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M|re.S)
    source_inline_code = re.findall(r'`([^`\n]+)`', strip_fences(original))
    candidate_inline_code = re.findall(r'`([^`\n]+)`', strip_fences(projected_candidate))
    if source_inline_code != candidate_inline_code:
        errors.append('inline code contents changed')

    # Validate section coordinates against frozen headings, including reservations.
    frozen_cache: dict[str, list[str]] = {}
    for target in combined:
        if target["kind"] != "sec":
            continue
        source = target["source"]
        if source not in frozen_cache:
            frozen_cache[source] = (repo_root / manifest[source]["frozen"]).read_text(encoding="utf-8").splitlines()
        if not HEADING_RE.fullmatch(frozen_cache[source][target["start"] - 1]):
            errors.append(f"section target {target['id']!r} does not point to a frozen ATX heading")

    emitted: dict[str, tuple[str, int]] = {}
    for accepted_item in accepted:
        accepted_path = packet_dir / accepted_item["candidate"]
        try:
            accepted_text = accepted_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for line in accepted_text.splitlines():
            for label in LABEL_RE.findall(line):
                if label in emitted:
                    errors.append(f"label {label!r} is emitted more than once across accepted/current candidates")
                target = by_id.get(label)
                if target is None:
                    errors.append(f"accepted candidate emits unknown label {label!r}")
                    continue
                emitted[label] = (target["source"], target["start"])
                if not (target["source"] == accepted_item["source"] and accepted_item["start"] <= target["start"] <= target["end"] <= accepted_item["end"]):
                    errors.append(f"accepted label {label!r} is outside its accepted original span")

    label_edit_kinds = {"label", "equation-label", "statement-open", "display-transcription"}
    current_label_locations = {
        edit["target"]: packet["start"] + _line_number_at(original, edit["offset"]) - 1
        for edit in edits if edit["kind"] in label_edit_kinds and edit.get("target") in by_id
    }
    for line in candidate.splitlines():
        for label in LABEL_RE.findall(line):
            if label in emitted:
                errors.append(f"label {label!r} is emitted more than once across accepted/current candidates")
            target = by_id.get(label)
            if target is None:
                errors.append(f"emitted label {label!r} is not registered or proposed")
                continue
            original_line = current_label_locations.get(label)
            emitted[label] = (packet["source"], original_line or packet["start"])
            if original_line is None:
                errors.append(f"emitted label {label!r} has no corresponding label edit")
            elif not (target["source"] == packet["source"] and target["start"] <= original_line <= target["end"]):
                errors.append(f"emitted label {label!r} is outside its original source location")
            if target["kind"] == "sec" and not HEADING_RE.fullmatch(line):
                errors.append(f"section label {label!r} is not on an ATX heading")
            if target["kind"] == "eq" and not line.rstrip().endswith(f"{{#{label}}}"):
                errors.append(f"equation label {label!r} is not immediately after its display delimiter")
            if target["kind"] in STATEMENT_KINDS and line != f"::: {{#{label}}}":
                errors.append(f"statement label {label!r} is not on its native div opener")

    covered = [(item["source"], item["start"], item["end"]) for item in accepted]
    covered.append((packet["source"], packet["start"], packet["end"]))
    for target in combined:
        is_covered = any(source == target["source"] and start <= target["start"] <= target["end"] <= end for source, start, end in covered)
        if is_covered and target["id"] not in emitted:
            errors.append(f"covered target {target['id']!r} is not defined")

    in_fence = False
    for local_line, line in enumerate(original.splitlines(), start=packet["start"]):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not HEADING_RE.fullmatch(line):
            continue
        expected_sections = [
            target for target in combined
            if target["kind"] == "sec" and target["source"] == packet["source"]
            and target["start"] == local_line and target["end"] == local_line
        ]
        if len(expected_sections) != 1 or expected_sections[0]["id"] not in emitted:
            errors.append(f"frozen heading at {packet['source']}:{local_line} lacks its unique section label")

    references: list[dict[str, str]] = []
    for match in NATIVE_REF_RE.finditer(candidate):
        target_id = match.group(1)
        references.append({"id": target_id, "form": "native"})
        if target_id not in by_id:
            errors.append(f"native reference names unknown target {target_id!r}")
    qmd_for_source = {source: entry["qmd"] for source, entry in manifest.items()}
    for match in LINK_RE.finditer(candidate):
        destination, target_id = match.group(2), match.group(3)
        references.append({"id": target_id, "form": "link", "destination": destination})
        target = by_id.get(target_id)
        if target is None:
            errors.append(f"link names unknown target {target_id!r}")
        elif destination != qmd_for_source[target["source"]]:
            errors.append(f"link to {target_id!r} has destination {destination!r}, expected {qmd_for_source[target['source']]!r}")
    prose = _reference_prose(candidate)
    remaining_raw = sorted(set(RAW_NUMBERED_REF_RE.findall(prose)))
    if remaining_raw:
        errors.append(f"unconverted numbered references remain: {remaining_raw}")
    remaining_sections = sorted(set(re.findall(
        rf"\bSections?\s+(?:[A-Z]\.)?[0-9]+(?:\.[0-9]+)*(?:\([a-z0-9]+\))?", prose
    )))
    if remaining_sections:
        errors.append(f"unconverted numeric section references remain: {remaining_sections}")
    remaining_equations = sorted(set(re.findall(
        rf"(?:(?:Equations?|Formulas?)\s+)?\({TAG_TOKEN}\)", prose,
    )))
    if remaining_equations:
        errors.append(f"unconverted equation references remain: {remaining_equations}")
    if re.search(r'\bSections?\s+@sec-', candidate):
        errors.append('duplicated section noun before native reference')
    if re.search(r'\b(?:Equations?|Formulas?)\s+@eq-', candidate):
        errors.append('duplicated equation noun before native reference')
    for match in re.finditer(r"\[[^\]\n]+\]\(([^)\s]+\.md(?:#[^)\s]+)?)\)", candidate):
        raw_destination = match.group(1).split("#", 1)[0]
        resolved = posixpath.normpath(str(PurePosixPath(packet["source"]).parent / raw_destination))
        if resolved in manifest:
            errors.append(f"unconverted internal-book Markdown link remains: {match.group(1)!r}")

    # Validate link edit destinations now that manifest mappings are available.
    for index, edit in enumerate(edits):
        if edit["kind"] != "reference":
            continue
        target_id = edit.get("target")
        target = by_id.get(target_id)
        native = native_reference_text(edit["old"], target_id) if target_id else None
        if target and target["kind"] == "eq" and native is not None:
            number = equation_reference_number(edit["old"])
            if number != equation_numbers.get(target_id):
                errors.append(f"edit {index} equation reference number does not match target tag")
        if native is not None and _range_padding(edit["old"], edit["new"], native, original, edit["offset"]):
            continue
        match = LINK_RE.fullmatch(edit["new"])
        if match and target and match.group(2) != qmd_for_source[target["source"]]:
            errors.append(f"edit {index} link destination does not match target source")

    defined = sorted(emitted)
    reserved = sorted(target["id"] for target in combined if target["id"] not in emitted)
    diff = "".join(difflib.unified_diff(original.splitlines(keepends=True), candidate.splitlines(keepends=True), fromfile=f"{packet['source']}:{packet['start']}-{packet['end']}", tofile=packet["candidate"]))
    return {
        "ok": not errors,
        "packet": packet["id"],
        "errors": errors,
        "inventory": {
            "registry": len(registry),
            "proposed": len(proposed),
            "defined": defined,
            "reserved": reserved,
            "references": references,
        },
        "limitations": [
            "Mechanical checks do not establish that a reference points to the semantically correct scientific object.",
            "Supported edits include section/equation labels, tagged equations, named theorem wrappers, delimiters, display whitespace, references and native Mermaid opening fences.",
        ],
        "_diff": diff,
    }


def _write_output(directory: Path, result: dict[str, Any]) -> None:
    if directory.exists():
        raise CheckFailure(f"output directory already exists: {directory}")
    directory.mkdir(parents=True)
    (directory / "raw.diff").write_text(result.get("_diff", ""), encoding="utf-8")
    persisted = {key: value for key, value in result.items() if key != "_diff"}
    (directory / "verification.json").write_text(json.dumps(persisted, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="packet JSON path")
    parser.add_argument("--output", type=Path, help="fresh directory for raw.diff and verification.json")
    args = parser.parse_args(argv)
    try:
        result = validate_packet(args.packet)
        if args.output is not None:
            _write_output(args.output, result)
    except CheckFailure as exc:
        result = {"ok": False, "errors": [str(exc)]}
        if args.output is not None:
            try:
                _write_output(args.output, result)
            except CheckFailure as output_exc:
                result["errors"].append(str(output_exc))
    public = {key: value for key, value in result.items() if key != "_diff"}
    print(json.dumps(public, indent=2, sort_keys=True))
    return 0 if public.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
