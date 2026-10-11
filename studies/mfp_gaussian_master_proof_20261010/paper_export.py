"""Assemble the standalone MFP paper from maintained, promoted sources only.

Run from the repository root. Quarto is used only for this editorial export;
the delivered main.tex builds independently with latexmk/XeLaTeX.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "paper_MFP"
SCRATCH = ROOT / "data/generated/mfp_gaussian_master_proof_20261010/paper_export_20261011"
STUDY = ROOT / "studies/mfp_gaussian_master_proof_20261010"
DEST.mkdir(exist_ok=True)
SCRATCH.mkdir(parents=True, exist_ok=True)
manifest = {"source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
            "scope": "Editorial extraction of established book and code; no new mathematical claims.",
            "extracts": [], "copies": [], "editorial_changes": []}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def extract(path, start, end, role):
    source = ROOT / path
    lines = source.read_text().splitlines(keepends=True)
    result = "".join(lines[start - 1:end])
    manifest["extracts"].append({"source": path, "lines": [start, end], "role": role,
                                 "source_sha256": digest(source),
                                 "extract_sha256": hashlib.sha256(result.encode()).hexdigest()})
    return result

def replace(text, old, new, reason):
    assert text.count(old) == 1, (reason, text.count(old))
    manifest["editorial_changes"].append({"reason": reason, "before": old, "after": new})
    return text.replace(old, new)

mapping = json.loads((STUDY / "paper_code_mapping.json").read_text())
for entry in mapping:
    source, target = ROOT / entry["source"], ROOT / entry["destination"]
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    manifest["copies"].append({**entry, "source_sha256": digest(source), "byte_identical": True})
shutil.copyfile(ROOT / "docs/references.bib", DEST / "references.bib")
manifest["copies"].append({"source": "docs/references.bib", "destination": "paper_MFP/references.bib",
                           "source_sha256": digest(ROOT / "docs/references.bib"), "byte_identical": True})

prelude = extract("docs/02-gaussian-reuse.qmd", 15, 251, "Gaussian conditioning, moving directions and exact Gaussian moments")
main = extract("docs/02-gaussian-reuse.qmd", 252, 1293, "Complete master theorem, proofs, calculus, worked examples and implementation introduction")
foundation = extract("docs/12-three-sample-learning.qmd", 316, 684, "Complete bounded-program foundation and proofs")
guide = extract("code/MFP_CALCULUS.md", 1, 416, "Complete compiler guide")
manifest["extracts"].append({"source": "docs/notation.qmd", "source_sha256": digest(ROOT / "docs/notation.qmd"),
                            "role": "Canonical dimensions, forward model, data Gram and readout conventions used in editorial setup"})

# Heading changes preserve theorem titles inside fenced divisions.
prelude = re.sub(r"^### [1-4]\. ", "## ", prelude, flags=re.M)
prelude = "# Gaussian conditioning and finite calculations {#sec-preliminaries}\n\n" + prelude
main = main.replace("## Fixed finite Gaussian derivative programs", "# Fixed finite Gaussian derivative programs", 1)
main = re.sub(r"^### (.+\{#sec-[^\n]+)", r"## \1", main, flags=re.M)
foundation = re.sub(r"^### III\.F\. .*?(\{#sec-[^\n]+)", r"# Bounded-derivative Gaussian-program foundation \1", foundation, flags=re.M)
foundation = re.sub(r"^#### III\.F\.\d\. ", "## ", foundation, flags=re.M)
main = replace(main,
    "This lemma leaves intact the broader finite-second-moment roots and\n$C^1$ hypotheses of the older foundation. The smooth Gaussian theorem\nadds all finite scalar moments under its stronger assumptions; it does\nnot replace the lower-regularity specializations in\n[contained probability and continuity specializations](#sec-docs-global-nonlinear-l1840) or the distinct feature-ascent theorem\n@thm-docs-gaussian-calculus-l289.",
    "This lemma leaves intact the broader finite-second-moment roots and\n$C^1$ hypotheses of the bounded-derivative foundation in\n@sec-docs-special-data-limits-l3785. The smooth Gaussian theorem adds\nall finite scalar moments under its stronger assumptions. Its scope remains\nthe fixed Gaussian root laws and derivative language specified here.",
    "Replace comparisons to book results outside this paper by the included foundation and explicit scope.")
main = replace(main,
    "This is the general version of\n[derivatives along the gradient direction](#sec-docs-gaussian-calculus-l170) and the explicit finite MLP recurrence\nin [the finite MLP jet recurrence](#sec-docs-gaussian-calculus-l5338).",
    "This is the general version of\n[derivatives along the gradient direction](#sec-docs-gaussian-calculus-l170);\nthe neural applications below use this same finite recursion.",
    "Remove navigation to an optional later book recurrence.")
main = replace(main,
    "For neural applications fix $L,m,d$ and the canonical forward model",
    "For neural applications let $L$ be the hidden depth, $m$ the number of\nsamples, $d$ the input dimension and $n$ the hidden width. Fix $L,m,d$\nand data $x_a\\in\\mathbb R^d$, $y_a\\in\\mathbb R$, $1\\le a\\le m$.\nThe first weight matrix $W^{(1)}$ has shape $n\\times d$, hidden\nmatrices $W^{(\\ell)}$ have shape $n\\times n$ for $2\\le\\ell\\le L$,\nand the stored readout $W^{(L+1)}$ has length $n$. The data Gram is\n$G_{ab}=x_a^Tx_b/d$, without whitening or a nonsingularity requirement.\nUse the canonical forward model",
    "Supply canonical neural dimensions, data and Gram definitions locally.")
main = replace(main,
    "width-dependent small-readout law in [the notation contract](notation.qmd#sec-docs-notation-l70). With",
    "width-dependent small-readout law with stored entries $N(0,1/n^2)$. With",
    "State the compared readout law instead of linking outside the paper.")
main = replace(main,
    "The [MFP API guide](../code/MFP_CALCULUS.md) gives executable reuse,",
    "The compiler guide in @sec-compiler-guide (also supplied as\n`code/MFP_CALCULUS.md`) gives executable reuse,",
    "Point the implementation introduction to the included full guide.")
foundation = replace(foundation,
    " In the network application, the first-layer root is a Gaussian vector $w_0\\in\\mathbb R^d$ with covariance $I_d$; the three root preactivations are $u_i^T w_0$. Here $w_0=\\sqrt d V^{(1)}(0)$ in the isometric bottom coordinates of Part III.M.",
    "", "Omit the unrelated three-sample application aside with book-specific undefined coordinates.")

# Replace chapter-navigation links with numbered references to imported sections.
def local_links(text):
    text = re.sub(r"\[(?:Section )?III\.F\.\d\]\(12-three-sample-learning\.qmd#(sec-[^)]+)\)", r"@\1", text)
    text = re.sub(r"Sections @(sec-[\w-]+)–@(sec-[\w-]+)", r"Sections [-@\1]–[-@\2]", text)
    return re.sub(r"\]\(12-three-sample-learning\.qmd#", "](#", text)
main, foundation = local_links(main), local_links(foundation)
manifest["editorial_changes"].append({"reason": "Remove book heading prefixes and localize imported section links; preserve every theorem/equation identifier."})

guide = replace(guide, "../docs/02-gaussian-reuse.qmd#sec-mfp-finite-derivative-programs",
                "../main.pdf", "Local theorem link in the bundled Markdown guide.")
guide = replace(guide, "From the edition root:", "From the `paper_MFP/` root:", "Use the standalone execution root.")
guide = replace(guide, "data/established/mfp_kernel_jets_01", "build/kernel_jets_01", "Keep regenerated outputs in the standalone build directory.")
guide = replace(guide, "The directory must not exist.", "Create its parent first with `mkdir -p build`; the output directory itself must not exist.", "Make the fresh-output command self-contained.")
guide = replace(guide, "the default unhalved book loss", "the unhalved loss used in the general neural model", "Make the loss-clock comparison local.")
(DEST / "code/MFP_CALCULUS.md").write_text(guide)
for entry in manifest["copies"]:
    if entry["source"] == "code/MFP_CALCULUS.md":
        entry["byte_identical"] = False
        entry["note"] = "Only standalone links, execution root, generated-output path and local loss-reference wording adapted."

paper_guide = guide.replace("# Symbolic mean-field peeling calculus", "# The symbolic compiler: interface and examples {#sec-compiler-guide}", 1)
paper_guide = paper_guide.replace("[finite-program theorem](../main.pdf)", "[finite-program theorem](#sec-mfp-finite-derivative-programs)")
paper_guide = paper_guide.replace("](scripts/", "](code/scripts/")
# A two-column operation table reads better as a compact definition list on paper.
lines = paper_guide.splitlines()
start = lines.index("| Construction | Meaning |")
end = start + 2
while end < len(lines) and lines[end].startswith("|"):
    end += 1
operations = []
for row in lines[start + 2:end]:
    construction, meaning = row.strip("| ").split(" | ", 1)
    operations.extend([construction, ":   " + meaning, ""])
lines[start:end] = operations
paper_guide = "\n".join(lines) + "\n"
manifest["editorial_changes"].append({"reason": "Render the compiler's two-column operation table as a definition list; preserve all cells and executable examples."})

intro = r"""# Introduction {#sec-introduction}

Mean-field peeling (MFP) turns a specified finite computation on a Gaussian-initialized
neural network into a finite graph of multivariate Gaussian expectations.
The computation may include coordinate nonlinearities, products, sums,
normalized averages, named matrix and transpose calls, represented parameter
updates, and the derivatives admitted by the typed language below. Matrix
identity and every reuse are retained throughout the construction.

There are two mathematical operations. First, the product, chain and adjoint
rules express the requested network derivative exactly at each finite width.
Second, a Gaussian source-response recursion computes the limit of that
expression as width tends to infinity. For instance, the reused-matrix
observable with identity activation in @eq-mfp-reuse-square has expectation
$2+1/n$ at width $n$, while the Gaussian graph evaluates to its limit $2$.

The master statement is @thm-mfp-finite-derivative-program. Its program length,
hidden depth, sample count, derivative order and number of updates are fixed
before the width limit. It gives convergence of scalar observables in every
finite $L^p$, uniform moments and joint empirical laws. The initialization
normal form in @prp-mfp-initialization-normal-form has the additional literal
preactivation restriction stated there. The accompanying compiler makes the
construction inspectable and executable; its tests check implementation
identities rather than constituting a proof of the theorem.

This paper collects the established MFP material of *A Dynamical Theory of
Deep Learning*, together with the complete bounded-program foundation used
in its proof and the compiler guide. The raw-entry moment mechanism is
attributed to Golikov and Yang in @sec-mfp-uniform-moments. The presentation
does not claim a new general probabilistic program theorem. The accompanying
source map records the maintained book passages and the unchanged Python
sources used for this standalone edition.

The preliminary calculations are in @sec-preliminaries. The typed language,
Gaussian evaluation, complete proof, derivative rules and worked neural
examples follow in @sec-mfp-finite-derivative-programs. The executable
interface is in @sec-compiler-guide. Appendix
[-@sec-docs-special-data-limits-l3785] supplies the bounded-derivative foundation,
including singular query Grams and causal scalar feedback.

Throughout, $N(0,K)$ denotes the centered multivariate Gaussian law with
positive semidefinite covariance $K$, including singular laws. For finite
vectors, pairings are divided by $n$ when explicitly displayed that way;
the Frobenius matrix pairing is $\langle A,B\rangle_F=\operatorname{tr}(A^TB)$.
The empirical law of a same-type tuple $v^1,\ldots,v^k$ is
$n^{-1}\sum_i\delta_{(v^1_i,\ldots,v^k_i)}$.
The distance $\mathcal W_2$ is the quadratic Wasserstein distance, that is,
the infimum of $(\mathbb E\|X-Y\|_2^2)^{1/2}$ over couplings of the two laws.

"""
meta = r"""---
title: "Mean-Field Peeling"
subtitle: "A Gaussian Calculus for Fixed Finite Neural Derivative Programs"
author: "Amir Joudaki"
date: "2026-10-11"
abstract: |
  We present a constructive Gaussian calculus for fixed finite derivative computations
  of Gaussian-initialized deep neural networks. A typed language specifies coordinate
  operations, normalized contractions, matrix and transpose reuse, represented updates,
  and finite derivatives and flow jets. Exact finite-width differentiation compiles these
  operations into primitive programs. A causal Gaussian source-response recursion then
  identifies their infinite-width scalar limits, with convergence in every finite
  Lp and uniform moment bounds. Singular covariance is allowed without identifying
  distinct formal source variables. A restricted initialization subclass admits a
  reduction to moments of products of activation derivatives. We include the complete
  proofs, worked reuse and moving-flow examples, symbolic geometry and label-dependent
  feature-kernel jets, and a documented Python compiler with its executable examples
  and tests. Depth, data dimensions, derivative order and update count are fixed;
  no positive-time reconstruction or growing-order guarantee is asserted.
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
number-sections: true
toc: true
toc-depth: 2
colorlinks: true
bibliography: references.bib
cite-method: natbib
biblio-style: plainnat
crossref:
  chapters: false
format:
  latex:
    keep-tex: true
header-includes:
  - \usepackage{mathtools}
  - \usepackage{fvextra}
  - \RecustomVerbatimEnvironment{verbatim}{Verbatim}{breaklines=true,breakanywhere=true,fontsize=\small}
  - \RecustomVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\},breaklines=true,breakanywhere=true,fontsize=\small}
  - \allowdisplaybreaks[1]
  - \setlength{\emergencystretch}{3em}
---

"""
bundle = r"""
# Source bundle and reproduction {#sec-source-bundle}

The standalone directory supplies `main.tex`, `references.bib`, a `Makefile`,
and the accompanying `code/` tree. The native LaTeX source compiles with
XeLaTeX, BibTeX and `latexmk`; Quarto is not needed to build this paper.
From the paper directory, run `make pdf`. The output is `main.pdf`.
Install the Python dependency with `python -m pip install -r requirements.txt`
in an environment of your choice, then run `make check` for the copied test suite.

The symbolic implementation is in `code/pde/mfp_compiler.py` and
`code/pde/mfp_expr.py`; the independent finite-array interpreter is in
`code/pde/mfp_finite.py`. The package initialization, finite-network module
and exact Gaussian-moment module are included to preserve the established
import closure. Three `code/scripts/example_mfp_*.py` files implement the
worked calculations, and four `code/tests/test_mfp_*.py` files supply the
established checks. All Python sources and the dependency pin are copied
byte for byte from the maintained package. `SOURCE_MAP.json` records the
source hashes, manuscript extraction ranges and editorial adaptations.

"""
qmd = meta + intro + prelude + "\n" + main + "\n" + paper_guide + bundle + "\n\\appendix\n\n" + foundation
(SCRATCH / "main.qmd").write_text(qmd)
shutil.copyfile(DEST / "references.bib", SCRATCH / "references.bib")
(DEST / "SOURCE_MAP.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print(SCRATCH / "main.qmd")
