#!/usr/bin/env python3
"""Deterministic editorial adaptation of the established NTH section.

The sole proof input is the already compiled approved book section.  All
scientific statements and all six proof bodies are preserved; only the
declared notation, cross-references, local framing, and layout are changed.
Run from any directory.  No maintained paper/book file is written.
"""

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
SCRATCH = ROOT / "data/generated/nth_lower_bound_20261010/paper_adaptation"
SOURCE = ROOT / "data/generated/nth_lower_bound_20261010/promotion_v4/data/generated/DTDL/docs/DTDL.tex"


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


def math_blocks(text):
    return list(re.finditer(
        r"\\\(.*?\\\)|\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}",
        text, re.S))


def rename_math(body):
    # TeX commands are atomic: e.g. the w inside \\widetilde is untouched.
    mapping = {"w": "u", "u": r"\zeta", "Q": r"\Sigma"}
    tokens = re.findall(
        r"\\(?:begin|end|label|operatorname|text|mathrm|mathbb|mathscr)\{[^}]*\}"
        r"|\\rm\s+[A-Za-z]+|\\[A-Za-z]+|\\.|.", body, re.S)
    tokens = [mapping.get(token, token) for token in tokens]
    body = "".join(token + (" " if re.search(r"\\[A-Za-z]+$", token)
                          and i + 1 < len(tokens) and re.match(r"[A-Za-z]", tokens[i + 1])
                          else "") for i, token in enumerate(tokens))
    # The readout rename comes after the coefficient rename, so the resulting
    # w always denotes the manuscript's n-dimensional readout.
    body = body.replace("W^{(3)}", "w")
    body = body.replace(r"\mathcal L=", r"\mathcal L_{1/2}=")
    # The compiled book splits W^{(3)\\top} inside the superscript.
    body = body.replace(r"W^{(3)\top}", r"w^\top ")
    return body


def canonical_math(body):
    """Ignore only presentation tokens, including compiled line wrapping."""
    body = re.sub(r"\\label\{[^}]+\}", "", body)
    body = body.replace(r"\protect\phantomsection", "")
    body = body.replace(r"\allowbreak{}", "")
    body = body.replace(r"\begin{gathered}", "").replace(r"\end{gathered}", "")
    body = body.replace(r"\\", "")
    return re.sub(r"\s+", "", body)


full = SOURCE.read_text()
start = full.index(r"\section{Literal storage of a frozen-top neural tangent")
end = full.index(r"\section{", start + 10)
source = full[start:end].rstrip() + "\n"
text = source
labels = re.findall(r"\\label\{([^}]+)\}", source)
assert len(labels) == len(set(labels))


def target_label(label):
    if label == "sec-nth-storage":
        return "cp:nth:storage"
    if label == "sec-nth-storage-setup":
        return "cp:nth:setup"
    kind, suffix = label.split("-nth-storage-", 1)
    prefix = {"eq": "eq:", "proof": "proof:", "thm": "", "lem": "", "cor": ""}[kind]
    return "cp:nth:" + prefix + suffix


label_map = {label: target_label(label) for label in labels}
assert len(set(label_map.values())) == len(labels)
for old, new in sorted(label_map.items(), key=lambda pair: -len(pair[0])):
    text = text.replace(old, new)

text = re.sub(r"\\protect\\hypertarget\{[^}]+\}\{\}", "", text)
text = text.replace(r"\protect\phantomsection", r"\phantomsection")
text = text.replace(r"\allowbreak{}", "")
# Turn Pandoc's spelled-out numbered references into the paper's style.
text = re.sub(r"Equation~\\ref\{([^}]+)\}", lambda m: r"\eqref{" + m[1] + "}", text)
text = re.sub(r"(?:Theorem|Corollary|Lemma)~\\ref\{([^}]+)\}", lambda m: r"\Cref{" + m[1] + "}", text)
text = re.sub(
    r"\\\(.*?\\\)|\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}",
    lambda m: rename_math(m[0]), text, flags=re.S)

# p is the success probability only in the theorem and the final sentence of
# its proof.  The density p in the small-ball proof remains a local density.
theorem_start = text.index(r"\begin{theorem}")
theorem_end = text.index(r"\end{theorem}", theorem_start)
theorem = text[theorem_start:theorem_end]
theorem = theorem.replace("0<p<1", r"0<\pi<1").replace("S_n(p,A)", r"S_n(\pi,A)")
theorem = theorem.replace(r"\ge p", r"\ge\pi").replace(r"\(p,A\)", r"\(\pi,A\)")
text = text[:theorem_start] + theorem + text[theorem_end:]
text = once(text, r"eventually is below \(p\).", r"eventually is below \(\pi\).")

old_opening = text[text.index("The preceding encoding obstruction"):text.index(r"\subsection{Model")]
new_opening = r"""Literal neural tangent hierarchy (NTH) arrays provide a separate benchmark
for how a prescribed representation affects storage. We study the ordered
hierarchy associated with Huang and Yau~\cite{huang2020nth}, with its highest
retained rank frozen, in the same feature-learning metric and zero-readout
initialization as \Cref{cp:setup}. On a correlated growing dataset, its
necessary and sufficient retained size is
\(\exp[\Theta(\log m\log n)]\) on a fixed short interval.

This section has its own assumptions and probability convention. The
fixed-data, small-label, Gram-gap and complete-trajectory hypotheses of
\Cref{cp:headline} are not imposed here; the result is an independent
benchmark, and gives no same-family storage separation from the preceding
compression constructions. No theorem for another parameterization or
readout initialization is transferred.

"""
text = once(text, old_opening, new_opening)
text = once(text,
    "The two hidden activations\nare identity. In canonical layer notation,",
    "We specialize \\eqref{cp:network} to two identity hidden activations\n"
    "and use its readout \\(w\\). Thus")
text = once(text,
    "book's full-MSE flow at physical time \\(t\\) equals this flow at time\n"
    "\\(2t\\). Thus the interval below becomes \\([0,T/2]\\) under full-MSE.",
    "full-MSE flow \\eqref{cp:flow} at physical time \\(t\\) equals this flow\n"
    "at time \\(2t\\). Throughout this section, \\(t\\) and dots refer to\n"
    "half-MSE physical time. Thus \\(T=2^{-15}\\) here corresponds to\n"
    "\\([0,T/2]=[0,2^{-16}]\\) in the paper's full-MSE time.")
text = once(text,
    "fixed data summaries and evolving prediction coefficient by",
    "fixed input second moment \\(\\Sigma\\in\\mathbb R^{d\\times d}\\),\n"
    "label-input mean \\(b\\in\\mathbb R^d\\), and prediction coefficient\n"
    "\\(u\\in\\mathbb R^d\\) by")
text = once(text,
    r"\end{gathered}}\end{equation} Here \(\|\Sigma\|_{\rm op}\le1\),",
    r"\end{gathered}}\end{equation} Here \(\Sigma\) is an input-space second moment," + "\n"
    r"distinct from the sample-space population Grams \(Q^{(\ell)}\) in" + "\n"
    r"\eqref{cp:data}. We have \(\|\Sigma\|_{\rm op}\le1\),")
text = once(text,
    "The fixed-data small-label hypotheses of the\ncomplete-trajectory compression theorem",
    "The fixed-data small-label hypotheses of\n\\Cref{cp:headline}")
text = once(text,
    "Its fitting and dense-variability theorems are not used,",
    "The preceding fitting and dense-variability theorems are not used,")

# Undo narrow-book display wraps that split a single factor or argument.
# Existing clean display rows remain: this is a layout-only transformation.
repairs = {
    r"(j\\+2)": "(j+2)",
    r"(k\\+2)": "(k+2)",
    r"(v,\\a_z": "(v,a_z",
    r"(\mathbf v;\\t)": r"(\mathbf v;t)",
    r"(\mathbf v,\\v_{a_1}": r"(\mathbf v,v_{a_1}",
    r"N_{\rm mov}\\+N_{\rm top}": r"N_{\rm mov}+N_{\rm top}",
    r"(2\kappa)\\+3]": r"(2\kappa)+3]",
}
repair_counts = {}
for old, new in repairs.items():
    repair_counts[old] = text.count(old)
    assert repair_counts[old] > 0, old
    text = text.replace(old, new)

text = text.replace(r"\begin{equation}\phantomsection", r"\begin{equation}")
# Give the final proof its actual target, without modifying its body.
text = once(text,
    r"\label{cp:nth:proof:main}{}" + "\n\n" + r"\begin{proof}",
    r"\label{cp:nth:proof:main}{}" + "\n\n"
    r"\begin{proof}[Proof of \Cref{cp:nth:matching,cp:nth:general-upper}]")
text = "% Established NTH benchmark; full statements and proofs are included below.\n" + text

counts = {name: (source.count(r"\begin{" + name + "}"), text.count(r"\begin{" + name + "}"))
          for name in ("theorem", "corollary", "lemma", "proof", "equation")}
assert counts["theorem"] == (1, 1)
assert counts["corollary"] == (1, 1)
assert counts["lemma"] == (5, 5)
assert counts["proof"] == (6, 6)
assert all(a == b for a, b in counts.values())
new_labels = re.findall(r"\\label\{([^}]+)\}", text)
assert set(new_labels) == set(label_map.values())
assert len(new_labels) == len(set(new_labels))
refs = re.findall(r"\\(?:Cref|eqref|ref)\{([^}]+)\}", text)
refs = {ref for group in refs for ref in group.split(",")}
assert refs - set(new_labels) == {"cp:setup", "cp:network", "cp:flow", "cp:data", "cp:headline"}
assert "nth-storage" not in text
new_commands = set(re.findall(r"\\[A-Za-z]+", text)) - set(re.findall(r"\\[A-Za-z]+", source))
assert new_commands <= {r"\Sigma", r"\zeta", r"\pi", r"\Cref", r"\eqref", r"\cite"}, new_commands

# Proof correspondence is independent of paragraph replacements above:
# compare every proof body token-by-token after ONLY the advertised notation,
# reference and wrapping translations.  Named proof headings are ignored.
def proof_bodies(tex):
    return re.findall(r"\\begin\{proof\}(?:\[[^\n]*\])?(.*?)\\end\{proof\}", tex, re.S)


proof_checks = []
for index, (original, adapted) in enumerate(zip(proof_bodies(source), proof_bodies(text)), 1):
    expected = original
    for old, new in label_map.items():
        expected = expected.replace(old, new)
    expected = re.sub(r"Equation~\\ref\{([^}]+)\}", lambda m: r"\eqref{" + m[1] + "}", expected)
    expected = re.sub(r"(?:Theorem|Corollary|Lemma)~\\ref\{([^}]+)\}", lambda m: r"\Cref{" + m[1] + "}", expected)
    expected = re.sub(
        r"\\\(.*?\\\)|\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}",
        lambda m: rename_math(m[0]), expected, flags=re.S)
    expected = expected.replace(r"\(p\)", r"\(\pi\)") if index == 6 else expected
    expected = expected.replace(r"\protect\phantomsection", "")
    left, right = canonical_math(expected), canonical_math(adapted)
    assert left == right, f"Proof {index} changed beyond declared transformations"
    proof_checks.append({"proof": index, "identical_after_declared_transforms": True,
                         "canonical_sha256": digest(left)})

statement_checks = []
for environment in ("theorem", "corollary", "lemma"):
    pattern = r"\\begin\{" + environment + r"\}(.*?)\\end\{" + environment + r"\}"
    originals = re.findall(pattern, source, re.S)
    adapted_statements = re.findall(pattern, text, re.S)
    for index, (original, adapted) in enumerate(zip(originals, adapted_statements), 1):
        expected = original
        for old, new in label_map.items():
            expected = expected.replace(old, new)
        expected = re.sub(r"\\protect\\hypertarget\{[^}]+\}\{\}", "", expected)
        expected = re.sub(r"Equation~\\ref\{([^}]+)\}", lambda m: r"\eqref{" + m[1] + "}", expected)
        expected = re.sub(r"(?:Theorem|Corollary|Lemma)~\\ref\{([^}]+)\}", lambda m: r"\Cref{" + m[1] + "}", expected)
        expected = re.sub(
            r"\\\(.*?\\\)|\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}",
            lambda m: rename_math(m[0]), expected, flags=re.S)
        if environment == "theorem":
            expected = expected.replace("0<p<1", r"0<\pi<1").replace("S_n(p,A)", r"S_n(\pi,A)")
            expected = expected.replace(r"\ge p", r"\ge\pi").replace(r"\(p,A\)", r"\(\pi,A\)")
        expected = expected.replace(r"\protect\phantomsection", "")
        assert canonical_math(expected) == canonical_math(adapted), (environment, index)
        statement_checks.append({"environment": environment, "index": index,
                                 "identical_after_declared_transforms": True})

SCRATCH.mkdir(parents=True, exist_ok=True)
(STUDY / "PAPER_NTH.tex").write_text(text)
(SCRATCH / "source_section.tex").write_text(source)
report = {
    "source_file": str(SOURCE.relative_to(ROOT)),
    "source_section_lines": [full[:start].count("\n") + 1, full[:end].count("\n")],
    "source_section_sha256": digest(source),
    "output_sha256": digest(text),
    "counts": counts, "labels": label_map, "external_local_references": sorted(refs - set(new_labels)),
    "layout_repair_counts": repair_counts, "proof_correspondence": proof_checks,
    "statement_correspondence": statement_checks,
    "new_TeX_commands": sorted(new_commands),
    "scope": "Editorial adaptation only; no mathematical re-review or new claims",
}
(SCRATCH / "correspondence.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"output": str(STUDY / "PAPER_NTH.tex"), "lines": len(text.splitlines()),
                  "counts": counts, "proofs_preserved": len(proof_checks), "sha256": digest(text)}, indent=2))
