#!/usr/bin/env python3
"""Print an apply_patch patch for the reviewed width module's LaTeX port.

Only reads the scoped approved source. All transformations are typography,
cross-reference mapping, or the paper's explicitly stated readout notation.
"""
from pathlib import Path
import json
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "studies/headline_threefold_upgrade_20261011/PROMOTION_WIDTH.qmd"
TARGET = ROOT / "paper/compact_width.tex"

EXTERNAL = {
    "sec-compression-setup": "cp:setup",
    "eq-compression-legendre-size": "cp:legendre-size",
    "eq-compression-panel-size": "cp:panel-size",
    "eq-compression-dense-lower": "cp:eq-dense-lower",
    "eq-compression-source-families": "cp:source-families",
    "eq-compression-source-rms": "cp:source-rms",
    "eq-compression-initialization-event": "cp:eq-initialization-event",
    "eq-compression-src-basic": "cp:src-basic",
    "eq-compression-src-absorption-coefficients": "cp:src-absorption-coefficients",
    "eq-compression-src-allowance": "cp:src-allowance",
    "eq-compression-src-response-coefficients": "cp:src-response-coefficients",
    "eq-compression-src-uv": "cp:src-UV",
    "eq-compression-src-k": "cp:src-K",
    "eq-compression-src-retained": "cp:src-retained",
    "eq-compression-src-gradient-derivative": "cp:src-gradient-derivative",
    "eq-compression-src-vertical": "cp:src-vertical",
    "eq-compression-src-exact-remainders": "cp:src-exact-remainders",
    "eq-compression-src-remainder-bounds": "cp:src-remainder-bounds",
    "eq-compression-src-force-remainder": "cp:src-force-remainder",
    "eq-compression-src-traces": "cp:src-traces",
    "eq-compression-src-main-moment": "cp:src-main-moment",
    "lem-compression-src-powers": "cp:src-powers",
    "lem-compression-src-time-derivative": "cp:src-time-derivative",
    "lem-compression-src-gaussian": "cp:src-Gaussian",
    "lem-compression-derivative-transfer": "cp:derivative-transfer",
    "prp-compression-jets": "cp:jets",
    "prp-compression-selected": "cp:selected",
    "eq-compression-legendre-reconstruction": "cp:eq-legendre-reconstruction",
    "eq-compression-legendre-flow": "cp:eq-legendre-flow",
    "eq-compression-legendre-defect": "cp:eq-legendre-defect",
    "eq-compression-legendre-pointwise-defect": "cp:eq-legendre-pointwise-defect",
    "eq-compression-legendre-ledger": "cp:eq-legendre-ledger",
    "eq-compression-projection-growth": "cp:eq-projection-growth",
    "eq-compression-legendre-signed": "cp:eq-legendre-signed",
    "eq-compression-legendre-count": "cp:eq-legendre-count",
    "proof-compression-fit": "cp:fit",
    "proof-compression-innovation": "cp:innovation",
    "proof-compression-panel": "cp:panel",
    "proof-compression-source-whole-sphere-verification": "cp:src-whole-sphere-verification",
    "proof-compression-src-finite-working": "cp:src-finite-working",
    "proof-compression-src-gaussian": "cp:src-Gaussian",
    "proof-compression-src-local-lemma": "cp:src-local-lemma",
    "proof-compression-src-panel-working": "cp:src-panel-working",
    "sec-compression-every-noncentered-contraction": "cp:src-moments",
}
INTERNAL = {
    "sec-compression-polynomial-width": "cp:poly:width-section",
    "sec-compression-polynomial-source": "cp:poly:source-section",
    "sec-compression-polynomial-dense-lower": "cp:poly:dense-lower-section",
    "sec-compression-polynomial-legendre": "cp:poly:legendre-section",
    "sec-compression-polynomial-assembly": "cp:poly:assembly",
    "thm-compression-polynomial-width": "cp:poly:width",
    "lem-compression-polynomial-source": "cp:poly:source",
    "prp-compression-polynomial-dense-lower": "cp:poly:dense-lower",
    "prp-compression-polynomial-legendre": "cp:poly:legendre",
    "eq-compression-finite-smallball": "cp:poly:eq:finite-smallball",
}
source = SOURCE.read_text()
for anchor in re.findall(r"\{#(eq-compression-polynomial-[\w-]+)\}", source):
    INTERNAL[anchor] = "cp:poly:eq:" + anchor.removeprefix("eq-compression-polynomial-")
MAPPING = EXTERNAL | INTERNAL


def inline(text):
    text = text.replace(r"W^{(L+1)}", "w")
    text = re.sub(r"\[([^\]]+)\]\(#([\w-]+)\)",
                  lambda m: r"\hyperref[" + MAPPING[m[2]] + "]{" + m[1] + "}", text)
    text = re.sub(r"@([\w-]+)",
                  lambda m: (r"\eqref{" if m[1].startswith("eq-") else r"\Cref{")
                  + MAPPING[m[1]] + "}", text)
    text = re.sub(r"\*(complete|actual)\*", r"\\emph{\1}", text)
    return text


def convert():
    lines = source.splitlines()
    out = ["% Complete port of PROMOTION_WIDTH.qmd; all auxiliary symbols are local.",
           "% Book readout W^{(L+1)} is the compact paper's w."]
    stack = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith(":::: {#"):
            anchor = re.fullmatch(r":::: \{#([\w-]+)\}", line)[1]
            kind = {"thm": "theorem", "lem": "lemma", "prp": "proposition"}[anchor[:3]]
            i += 1
            while not lines[i].strip():
                i += 1
            title = lines[i].removeprefix("### ")
            out.extend([r"\begin{" + kind + "}[" + title + "]",
                        r"\label{" + MAPPING[anchor] + "}"])
            stack.append(kind)
        elif line == ":::: {.proof}":
            stack.append("proof")
            out.append(r"\begin{proof}")
        elif line == "::::":
            out.append(r"\end{" + stack.pop() + "}")
        elif line.startswith("##"):
            match = re.fullmatch(r"(#{2,3}) (.*?) \{#([\w-]+)\}", line)
            assert match, line
            level = "section" if len(match[1]) == 2 else "subsection"
            out.extend(["\\" + level + "{" + match[2] + "}",
                        r"\label{" + MAPPING[match[3]] + "}"])
        elif line == "$$":
            math = []
            i += 1
            while not lines[i].startswith("$$"):
                math.append(inline(lines[i]))
                i += 1
            end = re.fullmatch(r"\$\$(?: \{#([\w-]+)\})?", lines[i])
            assert end, lines[i]
            if end[1]:
                out.extend([r"\begin{equation}", *math,
                            r"\label{" + MAPPING[end[1]] + "}", r"\end{equation}"])
            else:
                out.extend([r"\[", *math, r"\]"])
        elif line.startswith("| "):
            table = []
            while i < len(lines) and lines[i].startswith("|"):
                table.append(lines[i])
                i += 1
            i -= 1
            out.extend([r"\begin{center}\small",
                        r"\begin{tabular}{@{}p{0.57\linewidth}p{0.39\linewidth}@{}}",
                        r"\toprule"])
            for j, row in enumerate(table):
                if j == 1:
                    out.append(r"\midrule")
                else:
                    cells = [inline(c.strip()) for c in row.strip("|").split("|")]
                    out.append(" & ".join(cells) + r"\\")
            out.extend([r"\bottomrule", r"\end{tabular}\end{center}"])
        else:
            out.append(inline(line))
        i += 1
    assert not stack
    result = "\n".join(out) + "\n"
    # Keep the paper's global C reserved for activation/depth constants.
    result = result.replace(r"\left[C\beta^L", r"\left[c_{\rm wid}\beta^L")
    result = result.replace(' \\right]^C\n', ' \\right]^{c_{\\rm wid}}\n')
    result = result.replace("with one absolute finite numerical $C$.",
                            "with one absolute finite numerical constant $c_{\\rm wid}$, local to this theorem.")
    return result


if __name__ == "__main__":
    if "--check" in sys.argv:
        target = TARGET.read_text()
        book = (ROOT / "data/generated/headline_threefold_upgrade_20261011/"
                "promotion_v6/docs/08b-trajectory-compression.qmd").read_text()
        approved = book.split("## Polynomial sufficient widths for Legendre and Taylor", 1)[1]
        approved = "## Polynomial sufficient widths for Legendre and Taylor" + approved.split(
            "## One selected nonlinear dynamics for both source constructions", 1)[0]
        assert source.strip() == approved.strip(), "Promotion module differs from approved v6."

        def mathnorm(value):
            value = value.replace(r"W^{(L+1)}", "w")
            value = value.replace(r"c_{\rm wid}", "C")
            value = value.replace("^{C}", "^C")
            value = re.sub(r"\\(?:begin|end)\{gathered\}", "", value)
            value = value.replace(r"\\", "")
            return re.sub(r"\\(?:quad|qquad)|\s+", "", value)

        body = mathnorm(target)
        chunks = [a or b for a, b in re.findall(r"\$\$(.*?)\$\$|\$([^$]+)\$", source, re.S)]
        missing_math = [value for value in chunks if mathnorm(value) not in body]
        assert not missing_math, missing_math
        labels = set(re.findall(r"\\label\{([^}]+)\}", target))
        assert labels == set(INTERNAL.values()), (labels, set(INTERNAL.values()))
        refs = set(re.findall(r"\\(?:eqref|Cref)\{([^}]+)\}|\\hyperref\[([^]]+)\]", target))
        refs = {a or b for a, b in refs}
        compact_files = [ROOT / "paper/compact.tex"]
        compact_files += [ROOT / "paper" / (name + ".tex") for name in re.findall(
            r"\\input\{([^}]+)\}", compact_files[0].read_text())]
        all_labels = set().union(*(set(re.findall(r"\\label\{([^}]+)\}", p.read_text()))
                                   for p in compact_files if p.exists())) | labels
        print(json.dumps({
            "approved_v6_source_exact": True,
            "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "target_sha256": hashlib.sha256(target.encode()).hexdigest(),
            "preserved_math_chunks": len(chunks),
            "preserved_internal_anchors": len(labels),
            "external_mapping_count": len(EXTERNAL),
            "unresolved_references": sorted(refs - all_labels),
            "target_lines": len(target.splitlines()),
        }, indent=2))
    elif "--mapping" in sys.argv:
        print(json.dumps({"external": EXTERNAL, "internal": INTERNAL}, indent=2, sort_keys=True))
    else:
        result = convert()
        print("*** Begin Patch")
        print("*** Add File: " + str(TARGET))
        print("\n".join("+" + line for line in result.splitlines()))
        print("*** End Patch")
