"""Freeze/check the authorized paper transfer and unchanged headline contract."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
BASE = "ef8362764b4eb8144d7af8d6f8db080fdaaf82ca"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inputs():
    files = {}
    def visit(name):
        path = ROOT / "paper" / name
        if name in files:
            return
        body = path.read_text()
        files[name] = body
        for child in re.findall(r"\\input\{([^}]+)\}", body):
            visit(child if child.endswith(".tex") else child + ".tex")
    visit("compact.tex")
    return files

def math_block(body, label):
    pos = body.index("\\label{" + label + "}")
    starts = list(re.finditer(r"\\begin\{(equation|align|gather)\}", body[:pos]))
    start = starts[-1]
    end = body.index("\\end{" + start[1] + "}", pos)
    return re.sub(r"\s+", "", body[start.start():end])

def check():
    files = inputs()
    text = "\n".join(files.values())
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    refs = []
    for group in re.findall(r"\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}", text):
        refs.extend(group.split(","))
    refs.extend(re.findall(r"\\hyperref\[([^]]+)\]", text))
    duplicate = sorted({label for label in labels if labels.count(label) > 1})
    missing = sorted(set(refs) - set(labels))
    old = subprocess.check_output(["git", "show", BASE + ":paper/compact.tex"], cwd=ROOT, text=True)
    preserved = {}
    for label in ["cp:network", "cp:backward", "cp:flow", "cp:data", "cp:labels",
                  "cp:norm", "cp:relative", "cp:legendre-size", "cp:harmonic-size",
                  "cp:panel-size", "cp:absolute"]:
        preserved[label] = math_block(old, label) == math_block(files["compact.tex"], label)
    unchanged = {}
    for name, body in files.items():
        if name in {"compact.tex", "compact_foundations.tex", "compact_selected.tex",
                    "compact_width.tex", "compact_initialization.tex"}:
            continue
        original = subprocess.check_output(["git", "show", BASE + ":paper/" + name], cwd=ROOT)
        unchanged[name] = original == (ROOT / "paper" / name).read_bytes()
    theorem_end = files["compact.tex"].index("\\end{theorem}", files["compact.tex"].index("\\label{cp:headline}"))
    proposition_next = files["compact.tex"][theorem_end + len("\\end{theorem}"):].lstrip().startswith("\\begin{proposition}[Efficient initialization]")
    old_notation = old[old.index("\\paragraph{What must be remembered.}"):old.index("\\begin{theorem}[Compression")]
    notation = files["compact.tex"][files["compact.tex"].index("\\paragraph{What must be remembered.}"):files["compact.tex"].index("\\begin{theorem}[Compression")]
    book = ROOT / "docs/08b-trajectory-compression.qmd"
    approved = ROOT / "data/generated/headline_threefold_upgrade_20261011/promotion_v6/docs/08b-trajectory-compression.qmd"
    approved_text = approved.read_text()
    final_book_text = approved_text.replace(
        "from here through the end of this proof are private to this argument;\n"
        "the subsequent constructions use only the proposition's stated bounds.",
        "from here through the end of this proof are local to this argument.\n"
        "The quantitative width and initialization proofs explicitly recall the\n"
        "coefficient recurrences they additionally use; other constructions use\n"
        "the proposition's stated bounds.")
    final_book_text = final_book_text.replace(
        "We now compare the stronger working estimates with the statement, so no\n"
        "coefficient from this proof is needed by a later construction.  The working\n"
        "whole-sphere time radius is",
        "We now compare the stronger working estimates with the public statement.\n"
        "The quantitative width and initialization proofs explicitly recall the\n"
        "coefficient recurrences they additionally use. The working whole-sphere\n"
        "time radius is")
    result = {"baseline_commit": BASE, "preserved_equations": preserved,
              "unchanged_dependencies": unchanged, "notation_inventory_unchanged": old_notation == notation,
              "initialization_proposition_immediately_after_theorem": proposition_next,
              "duplicate_labels": duplicate, "missing_references": missing,
              "book_equals_approved_plus_two_locality_clarifications": book.read_text() == final_book_text,
              "book_sha256": sha(book),
              "source_sha256": {name: sha(ROOT / "paper" / name) for name in files}}
    assert all(preserved.values()) and all(unchanged.values()) and old_notation == notation
    assert proposition_next and not duplicate and not missing and result["book_equals_approved_plus_two_locality_clarifications"], result
    return files, result

if __name__ == "__main__":
    files, result = check()
    if len(sys.argv) > 1:
        dest = Path(sys.argv[1]).resolve()
        allowed = ROOT / "data/generated/headline_threefold_upgrade_20261011"
        assert dest.is_relative_to(allowed) and not dest.exists()
        (dest / "paper").mkdir(parents=True)
        for name in [*files, "references.bib"]:
            shutil.copy2(ROOT / "paper" / name, dest / "paper" / name)
        (dest / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
        (dest / "docs").mkdir()
        for name in ["08b-trajectory-compression.qmd", "index.qmd", "notation.qmd", "_quarto.yml"]:
            shutil.copy2(ROOT / "docs" / name, dest / "docs" / name)
        diff = subprocess.check_output(["git", "diff", BASE, "--", "paper/compact.tex",
                                       "paper/compact_foundations.tex", "paper/compact_selected.tex"], cwd=ROOT)
        (dest / "integration.diff").write_bytes(diff)
    print(json.dumps(result, indent=2))
