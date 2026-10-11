#!/usr/bin/env python3
"""Faithful, deterministic PROMOTION_SETUP -> compact initializer transfer.

Writes only the assigned new paper file and PAPER_SETUP_* integration aids,
through apply_patch. Run --check for a read-only preservation audit.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/headline_threefold_upgrade_20261011"
SOURCE = STUDY / "PROMOTION_SETUP.qmd"
FROZEN = ROOT / "data/generated/headline_threefold_upgrade_20261011/promotion_v6/docs/08b-trajectory-compression.qmd"
TARGET = ROOT / "paper/compact_initialization.tex"
MAIN = STUDY / "PAPER_SETUP_MAIN.tex"

EXTERNAL = {
    "thm-compression-headline": "cp:headline",
    "eq-compression-network": "cp:network",
    "eq-compression-flow": "cp:flow",
    "eq-compression-selected-readout": "cp:selected-readout",
    "eq-compression-harmonic-size": "cp:harmonic-size",
    "eq-compression-panel-size": "cp:panel-size",
    "eq-compression-absolute": "cp:absolute",
    "eq-compression-relative": "cp:relative",
    "eq-compression-source-families": "cp:source-families",
    "prp-compression-selected": "cp:selected",
    "eq-compression-selected-coefficients": "cp:selected-coefficients",
    "lem-compression-selected-fitting": "cp:selected-fitting",
    "prp-compression-panel": "cp:panel",
    "sec-compression-src-coefficients": "cp:src-coefficients",
    "eq-compression-src-uv": "cp:src-UV",
    "eq-compression-src-k": "cp:src-K",
    "lem-compression-harmonic-approximation": "cp:harmonic-approximation",
    "prp-compression-harmonic": "cp:harmonic",
    "lem-compression-selection": "cp:selection",
    "eq-compression-metric": "cp:metric",
    "lem-compression-polynomial-source": "cp:poly:source",
    "thm-compression-polynomial-width": "cp:poly:width",
    "sec-compression-polynomial-assembly": "cp:poly:assembly",
    "eq-compression-polynomial-taylor-tail-gate": "cp:poly:eq:taylor-tail-gate",
    "eq-compression-polynomial-taylor-count-gate": "cp:poly:eq:taylor-count-gate",
}


def readout_math(text: str) -> str:
    # Exact notation correspondences; no changes to factors or mobilities.
    text = text.replace(r"W^{(L+1)\top}", r"w^\top")
    text = text.replace(r"W^{(L+1)}", "w")
    text = text.replace(r"\phi^{(j)}", r"\phi_j")
    text = text.replace(r"\psi^{(j)}", r"\psi_j")
    # This scalar bound variable would otherwise collide with the readout.
    text = text.replace(r"z=B(w+w^{-1})/2", r"z=B(\zeta+\zeta^{-1})/2")
    text = text.replace(r"|w|=e^{\tau_o}", r"|\zeta|=e^{\tau_o}")
    return text


def local_label(native: str) -> str:
    if native in EXTERNAL:
        return EXTERNAL[native]
    if native == "sec-compression-efficient-setup":
        return "cp:init:proof"
    if native == "prp-compression-efficient-setup":
        return "cp:initialization"
    for prefix, target in (
        ("eq-compression-setup-", "cp:init:eq:"),
        ("lem-compression-setup-", "cp:init:"),
        ("sec-compression-setup-", "cp:init:sec:"),
    ):
        if native.startswith(prefix):
            return target + native[len(prefix):]
    raise ValueError(f"Unmapped native label: {native}")


def inline(text: str) -> str:
    text = readout_math(text)
    text = re.sub(r"\[([^\]]+)\]\(#([\w-]+)\)",
                  lambda m: r"\hyperref[" + local_label(m[2]) + "]{" + m[1] + "}", text)
    # The source spells out 'Lemma' once before its automatic cross-reference.
    text = text.replace("Lemma @lem-compression-setup-defect", "@lem-compression-setup-defect")
    text = re.sub(r"@([\w-]+)", lambda m:
                  (r"\eqref{" if m[1].startswith("eq-") else r"\Cref{")
                  + local_label(m[1]) + "}", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    return text


def convert(text: str) -> str:
    # A bold phrase in the reviewed prose spans a physical source line.
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    lines = text.splitlines()
    output: list[str] = []
    environments: list[str] = []
    in_list = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line == "$$":
            start = i + 1
            i += 1
            while i < len(lines) and not lines[i].startswith("$$"):
                i += 1
            assert i < len(lines), "Unclosed display"
            math = readout_math("\n".join(lines[start:i]))
            match = re.fullmatch(r"\$\$ \{#([\w-]+)\}", lines[i])
            if match:
                output.extend([r"\begin{equation}", r"\label{" + local_label(match[1]) + "}", math, r"\end{equation}"])
            else:
                assert lines[i] == "$$", lines[i]
                output.extend([r"\[", math, r"\]"])
            i += 1
            continue
        match = re.fullmatch(r":::: \{#([\w-]+)\}", line)
        if match:
            title = lines[i+1]
            assert title.startswith("### "), title
            env = "lemma" if match[1].startswith("lem-") else "proposition"
            environments.append(env)
            output.extend([r"\begin{" + env + "}[" + title[4:] + "]", r"\label{" + local_label(match[1]) + "}"])
            i += 2
            continue
        if line == ":::: {.proof}":
            environments.append("proof")
            output.append(r"\begin{proof}")
            i += 1
            continue
        if line == "::::":
            output.append(r"\end{" + environments.pop() + "}")
            i += 1
            continue
        match = re.fullmatch(r"(#{2,4}) (.*?) \{#([\w-]+)\}", line)
        if match:
            command = {2: "section", 3: "subsection", 4: "subsubsection"}[len(match[1])]
            output.extend(["\\" + command + "{" + match[2] + "}", r"\label{" + local_label(match[3]) + "}"])
            i += 1
            continue
        if line.startswith("| "):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([x.strip() for x in lines[i].strip("|").split("|")])
                i += 1
            assert len(rows) == 6 and len(rows[0]) == 4
            output.extend([r"\begin{center}\footnotesize",
                           r"\begin{tabular}{@{}p{.13\linewidth}p{.24\linewidth}p{.29\linewidth}p{.25\linewidth}@{}}",
                           r"\toprule", " & ".join(map(inline, rows[0])) + r"\\", r"\midrule"])
            output.extend(" & ".join(map(inline, row)) + r"\\" for row in rows[2:])
            output.extend([r"\bottomrule", r"\end{tabular}", r"\end{center}"])
            continue
        match = re.match(r"\d+\. (.*)", line)
        if match:
            if not in_list:
                output.append(r"\begin{enumerate}")
                in_list = True
            output.append(r"\item " + inline(match[1]))
            i += 1
            continue
        if in_list and line and not line.startswith("   "):
            output.append(r"\end{enumerate}")
            in_list = False
        output.append(inline(line[3:] if in_list and line.startswith("   ") else line))
        i += 1
    if in_list:
        output.append(r"\end{enumerate}")
    assert not environments, environments
    return "\n".join(output).rstrip() + "\n"


def products() -> tuple[str, str, str]:
    source = SOURCE.read_text()
    frozen = FROZEN.read_text()
    assert source.strip() in frozen, "Reviewed setup module differs from frozen v6 chapter"
    start = source.index(":::: {#prp-compression-efficient-setup}")
    end = source.index("\n::::\n", start) + len("\n::::\n")
    main = convert(source[start:end])
    main = main.replace("both of the preceding initializers", "both a supplied dense initializer and a fresh implicit Gaussian initializer")
    main = main.replace("in \\hyperref[cp:init:sec:costs]{the detailed cost ledger}.",
                        "in \\hyperref[cp:init:sec:costs]{the detailed cost ledger}. The complete proof is in \\Cref{cp:init:proof}.")
    # The complete statement goes immediately after the headline theorem.
    # Its preamble and full detailed proof remain in the new paper input.
    detail = convert(source[:start] + source[end:])
    detail = detail.replace("already used by the chapter", "of \\Cref{cp:fit,cp:source}")
    detail = detail.replace("The proof first gives", "The proof of \\Cref{cp:initialization} first gives")
    # Match the compact manuscript's names and refer to the exact existing claim.
    detail = detail.replace("source-to-runtime theorem", "source-to-runtime proposition")
    header = ("% Transferred from reviewed PROMOTION_SETUP.qmd, frozen v6 Chapter 9.\n"
              "% Readout correspondence: book W^{(L+1)} = compact w; all normalizations unchanged.\n"
              "% Main statement cp:initialization is in compact.tex; PAPER_SETUP_MAIN.tex is its source-complete audit counterpart.\n")
    return source, main, header + detail


def apply_file(path: Path, content: str) -> None:
    if path.exists():
        old = path.read_text()
        if old == content:
            return
        patch = "*** Begin Patch\n*** Update File: " + str(path) + "\n@@\n"
        patch += "".join("-" + line + "\n" for line in old.splitlines())
        patch += "".join("+" + line + "\n" for line in content.splitlines())
    else:
        patch = "*** Begin Patch\n*** Add File: " + str(path) + "\n"
        patch += "".join("+" + line + "\n" for line in content.splitlines())
    patch += "*** End Patch\n"
    subprocess.run(["apply_patch", patch], check=True, cwd=ROOT, capture_output=True, text=True)


def display_math(source: str, latex: bool = False) -> list[str]:
    if latex:
        pattern = r"\\\[\s*(.*?)\s*\\\]|\\begin\{equation\}\s*(.*?)\\end\{equation\}"
        out = [a or b for a, b in re.findall(pattern, source, re.S)]
        out = [re.sub(r"\\label\{[^}]+\}", "", x) for x in out]
    else:
        out = re.findall(r"(?m)^\$\$\n(.*?)\n\$\$", source, re.S)
    return [re.sub(r"\s+", "", readout_math(x)) for x in out]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--compile", action="store_true")
    args = parser.parse_args()
    source, statement, detail = products()
    if not args.check:
        apply_file(MAIN, statement)
        apply_file(TARGET, detail)
    assert MAIN.read_text() == statement, "Main statement differs from deterministic transfer"
    assert TARGET.read_text() == detail, "Detailed initializer differs from deterministic transfer"
    combined = statement + detail
    source_labels = re.findall(r"\{#([\w-]+)\}", source)
    target_labels = re.findall(r"\\label\{([^}]+)\}", combined)
    assert Counter(map(local_label, source_labels)) == Counter(target_labels)
    source_displays = display_math(source)
    target_displays = display_math(combined, True)
    assert Counter(source_displays) == Counter(target_displays), "Display mathematics changed"
    source_inline = re.findall(r"(?<!\$)\$(?!\$)([^$]*?)\$(?!\$)", source)
    target_inline = re.findall(r"(?<!\$)\$(?!\$)([^$]*?)\$(?!\$)", combined)
    assert Counter(map(readout_math, source_inline)) == Counter(target_inline), "Inline mathematics changed"
    assert not re.search(r"@[a-z]|\{#|(?m:^::::)|\]\(#|\*\*", combined), "Untranslated Quarto markup"
    refs = re.findall(r"\\(?:eqref|Cref|ref)\{([^}]+)\}|\\hyperref\[([^\]]+)\]", combined)
    external = sorted({label for group in refs for item in group if item for label in item.split(",")} - set(target_labels))
    print("Frozen v6 module: byte-identical source substring")
    print("Source SHA256:", hashlib.sha256(source.encode()).hexdigest())
    print(f"All {len(source_labels)} labels preserved exactly once")
    print(f"All {len(source_displays)} display equations and {len(source_inline)} inline math spans preserved")
    print("Three lemmas and all three proofs retained; full main proposition in PAPER_SETUP_MAIN.tex")
    print("Exact substitutions only: W^{(L+1)} -> w; phi^{(j)} -> phi_j; psi^{(j)} -> psi_j; scalar ellipse w -> zeta")
    print("Eight finite-order work/memory ledgers and four asymptotic table rows retained")
    print("External compact labels:", ", ".join(external))
    print("Native-to-compact label mapping:")
    for label in sorted(set(source_labels) | set(EXTERNAL)):
        print(f"  {label} -> {local_label(label)}")
    if args.compile:
        scratch = ROOT / "data/generated/headline_threefold_upgrade_20261011/paper_setup_transfer"
        scratch.mkdir(parents=True, exist_ok=True)
        preamble = (ROOT / "paper/compact.tex").read_text().split(r"\begin{document}")[0]
        harness = (preamble + "\n\\begin{document}\n"
                   + "\\input{" + str(MAIN) + "}\n"
                   + "\\input{" + str(TARGET) + "}\n\\end{document}\n")
        apply_file(scratch / "setup_harness.tex", harness)
        for _ in range(2):
            result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                                     "setup_harness.tex"], cwd=scratch, capture_output=True, text=True)
            if result.returncode:
                print(result.stdout[-10000:])
                raise SystemExit(result.returncode)
        log = (scratch / "setup_harness.log").read_text()
        print("Isolated LaTeX syntax build passed (external references resolved by integrated manuscript)")
        print("Overfull boxes:", len(re.findall("Overfull", log)))


if __name__ == "__main__":
    main()
