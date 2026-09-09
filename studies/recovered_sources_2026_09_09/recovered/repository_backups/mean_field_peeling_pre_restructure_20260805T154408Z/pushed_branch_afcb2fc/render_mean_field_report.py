#!/usr/bin/env python3
"""Render the maintained Markdown report into a small LaTeX subset.

The source intentionally uses only headings, paragraphs, flat lists, bold
emphasis, quotes, inline LaTeX math, and display LaTeX math.  A tiny renderer
keeps the mathematical source untouched and avoids a dependency on Pandoc.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "MEAN_FIELD_PEELING_SELF_CONTAINED_REPORT.md"
TARGET = ROOT / "MEAN_FIELD_PEELING_SELF_CONTAINED_REPORT.body.tex"


def inline_markup(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)


def close_list(output: list[str], active: str | None) -> None:
    if active is not None:
        output.append(rf"\end{{{active}}}")
        output.append("")


def render(lines: list[str]) -> str:
    output: list[str] = []
    in_math = False
    in_quote = False
    active_list: str | None = None

    for position, raw in enumerate(lines):
        line = raw.rstrip("\n")

        if line.strip() == "$$":
            close_list(output, active_list)
            active_list = None
            if in_quote:
                output.extend([r"\end{quote}", ""])
                in_quote = False
            output.append(r"\[" if not in_math else r"\]")
            if in_math:
                output.append("")
            in_math = not in_math
            continue

        if in_math:
            output.append(line)
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            close_list(output, active_list)
            active_list = None
            if in_quote:
                output.extend([r"\end{quote}", ""])
                in_quote = False
            level = len(heading.group(1))
            title = inline_markup(heading.group(2))
            command = {1: "section", 2: "subsection", 3: "subsubsection"}[level]
            toc = {1: "section", 2: "subsection", 3: "subsubsection"}[level]
            output.append(rf"\{command}*{{{title}}}")
            output.append(rf"\addcontentsline{{toc}}{{{toc}}}{{{title}}}")
            output.append("")
            continue

        if line.startswith(">"):
            close_list(output, active_list)
            active_list = None
            if not in_quote:
                output.extend([r"\begin{quote}\itshape", ""])
                in_quote = True
            output.append(inline_markup(line[1:].lstrip()))
            continue
        elif in_quote:
            output.extend([r"\end{quote}", ""])
            in_quote = False

        bullet = re.match(r"^-\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if bullet or ordered:
            wanted = "itemize" if bullet else "enumerate"
            if active_list != wanted:
                close_list(output, active_list)
                active_list = wanted
                output.append(rf"\begin{{{active_list}}}")
            item = bullet.group(1) if bullet else ordered.group(1)
            output.append(r"\item " + inline_markup(item))
            continue

        if not line.strip():
            if active_list is not None:
                next_nonblank = ""
                for later in lines[position + 1 :]:
                    if later.strip():
                        next_nonblank = later.rstrip("\n")
                        break
                continues = (
                    active_list == "itemize"
                    and re.match(r"^-\s+(.+)$", next_nonblank)
                ) or (
                    active_list == "enumerate"
                    and re.match(r"^\d+\.\s+(.+)$", next_nonblank)
                )
                if continues:
                    continue
            close_list(output, active_list)
            active_list = None
            output.append("")
            continue

        output.append(inline_markup(line))

    close_list(output, active_list)
    if in_quote:
        output.append(r"\end{quote}")
    if in_math:
        raise ValueError("Unclosed display-math block")
    return "\n".join(output) + "\n"


def main() -> None:
    TARGET.write_text(render(SOURCE.read_text().splitlines(True)))


if __name__ == "__main__":
    main()
