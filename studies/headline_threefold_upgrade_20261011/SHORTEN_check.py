"""Freeze and check the paper-only shortening, without touching the Git index."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
BASE = "aa28e4693eecb93e6770db404878e959f5161fdf"
ENTRY = "main.tex"
BASE_ENTRY = "compact.tex"
OWN = {"compact_width.tex", "compact_initialization.tex"}
ADDED = {"compact_figures.tex"}
OUTPUT = ROOT / "data/generated/headline_threefold_upgrade_20261011"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def baseline(name):
    return subprocess.check_output(["git", "show", BASE + ":" + name], cwd=ROOT)


def check():
    sources = {}

    def visit(name):
        if name in sources:
            return
        path = ROOT / "paper" / name
        sources[name] = path.read_text()
        for child in re.findall(r"\\input\{([^}]+)\}", sources[name]):
            visit(child if child.endswith(".tex") else child + ".tex")

    visit(ENTRY)
    unchanged = {
        name: (ROOT / "paper" / name).read_bytes() == baseline("paper/" + name)
        for name in sources if name not in OWN | ADDED and name != ENTRY
    }
    main_original = baseline("paper/" + BASE_ENTRY).decode()
    feature_input = "\\input{feature_learning_theorem}\n\n"
    initializer = "\\begin{proposition}[Efficient initialization]"
    assert main_original.count(feature_input) == main_original.count(initializer) == 1
    main_reordered = main_original.replace(feature_input, "").replace(
        initializer,
        feature_input + "\\subsection{Efficient initialization}\n\n" + initializer,
        1,
    )
    def figure_editorial(text):
        text = text.replace(
            "\\usepackage{booktabs,array,longtable,enumitem,microtype}\n",
            "\\usepackage{booktabs,array,longtable,enumitem,microtype}\n"
            "\\usepackage{graphicx,caption}\n",
        ).replace(
            "fresh Gaussian reference sampled implicitly. It makes no empirical or\n"
            "finite-precision claim.",
            "fresh Gaussian reference sampled implicitly. The guarantees are exact-real,\n"
            "not finite-precision. A final figure collection provides earlier numerical\n"
            "illustrations, separately from the theorems.",
        ).replace(
            "The following is the complete persistent notation. A row with several entries\n"
            "counts each entry separately; layer and sample indices do not create new\n"
            "objects. The two uses of $\\delta$ are counted separately.",
            "The following is the complete persistent notation.",
        )
        start = text.index("\\begin{tabular}")
        stop = text.index("\\end{tabular}", start)
        table = text[start:stop]
        table = table.replace(
            "p{0.24\\linewidth}p{0.65\\linewidth}r",
            "p{0.28\\linewidth}p{0.66\\linewidth}",
        ).replace("Symbols&Meaning&Count", "Symbols&Meaning")
        table = table.replace("\\midrule\n&&30\\\\\n", "")
        table = re.sub(r"&[0-9]+(?=\\\\)", "", table)
        text = text[:start] + table + text[stop:]
        return text.replace(
            "\\Cref{cp:initialization}. Every dependency is supplied below; the older\n"
            "decoder and empirical material remain outside this manuscript.",
            "\\Cref{cp:initialization}. Every dependency is supplied below. The older\n"
            "decoder theory remains outside this manuscript; earlier numerical figures\n"
            "are collected separately at the end.",
        ).replace(
            "\\bibliography{references}\n\n",
            "\\bibliography{references}\n\n\\input{compact_figures}\n\n",
        )

    main_for_preservation = sources[ENTRY]
    if "\\section{Introduction}\n\\label{cp:introduction}" in main_for_preservation:
        intro_start = main_for_preservation.index("\\section{Introduction}")
        setup_start = main_for_preservation.index("\\section{Setup and main results}")
        main_for_preservation = (
            main_for_preservation[:intro_start] + main_for_preservation[setup_start:]
        ).replace("\\section{Setup and main results}",
                  "\\section{Setup and the headline theorem}", 1)
        related_start = main_for_preservation.index("\\section{Related work and discussion}")
        roadmap_start = main_for_preservation.index("\\paragraph{Proof roadmap.}")
        main_for_preservation = (
            main_for_preservation[:related_start] + main_for_preservation[roadmap_start:]
        ).replace("\\paragraph{Proof roadmap.}", "\\paragraph{Proof architecture.}", 1)
    unchanged[ENTRY + " mathematics (allowing approved framing and figure editorial)"] = (
        main_for_preservation in (
            main_original, main_reordered, figure_editorial(main_reordered)
        )
    )
    for name in ("docs/08b-trajectory-compression.qmd", "docs/notation.qmd"):
        unchanged[name] = (ROOT / name).read_bytes() == baseline(name)
    old_bib = baseline("paper/references.bib").decode()
    nth_start = old_bib.index("@misc{huang2020nth,")
    nth_stop = old_bib.index("\n}\n", nth_start) + 3
    nth_published = """@inproceedings{huang2020nth,
  author = {Huang, Jiaoyang and Yau, Horng-Tzer},
  title = {Dynamics of Deep Neural Networks and Neural Tangent Hierarchy},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning},
  series = {Proceedings of Machine Learning Research},
  volume = {119},
  pages = {4542--4551},
  publisher = {PMLR},
  year = {2020},
  url = {https://proceedings.mlr.press/v119/huang20l.html}
}
"""
    bib = (ROOT / "paper/references.bib").read_text()
    unchanged["references.bib (allowing verified NTH publication metadata)"] = bib in (
        old_bib, old_bib[:nth_start] + nth_published + old_bib[nth_stop:]
    )
    text = "\n".join(sources.values())
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    references = []
    for group in re.findall(r"\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}", text):
        references.extend(part.strip() for part in group.split(","))
    references.extend(re.findall(r"\\hyperref\[([^]]+)\]", text))
    citations = {
        key.strip() for group in re.findall(r"\\cite\{([^}]+)\}", text)
        for key in group.split(",")
    }
    bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib))
    result = {
        "baseline_commit": BASE,
        "unchanged_public_theorem_and_older_sources": unchanged,
        "duplicate_labels": sorted({s for s in labels if labels.count(s) > 1}),
        "missing_references": sorted(set(references) - set(labels)),
        "missing_citations": sorted(citations - bib_keys),
        "source_sha256": {name: digest(ROOT / "paper" / name) for name in sources},
        "new_module_lines": {name: len(sources[name].splitlines()) for name in OWN},
        "baseline_module_lines": {
            name: len(baseline("paper/" + name).splitlines()) for name in OWN},
    }
    assert all(unchanged.values()), result
    assert not result["duplicate_labels"] and not result["missing_references"], result
    assert not result["missing_citations"], result
    return sources, result


if __name__ == "__main__":
    sources, result = check()
    if len(sys.argv) > 1:
        dest = Path(sys.argv[1]).resolve()
        assert dest.is_relative_to(OUTPUT) and not dest.exists()
        (dest / "paper").mkdir(parents=True)
        (dest / "baseline").mkdir()
        (dest / "docs").mkdir()
        for name in [*sources, "references.bib"]:
            shutil.copy2(ROOT / "paper" / name, dest / "paper" / name)
        for name in [*(name for name in sources if name not in ADDED), "references.bib"]:
            original_name = BASE_ENTRY if name == ENTRY else name
            (dest / "baseline" / name).write_bytes(baseline("paper/" + original_name))
        if "compact_figures.tex" in sources:
            (dest / "paper/figures").mkdir()
            for figure in (ROOT / "paper/figures").glob("*.pdf"):
                shutil.copy2(figure, dest / "paper/figures" / figure.name)
        for name in ("index.qmd", "notation.qmd"):
            shutil.copy2(ROOT / "docs" / name, dest / "docs" / name)
        (dest / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
