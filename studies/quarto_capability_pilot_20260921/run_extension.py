"""Bounded extra fixture, negative reference gate and source-movement tests."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

sys.dont_write_bytecode = True
from reference_gate import check

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--quarto", type=Path, required=True)
parser.add_argument("--run-directory", type=Path, required=True)
args = parser.parse_args()
source = Path(__file__).resolve().parent
run = args.run_directory.resolve()
book = run / "book"
book.mkdir(parents=True, exist_ok=False)
quarto = str(args.quarto.resolve())
env = dict(os.environ, XDG_CACHE_HOME=str(run / "cache"), XDG_CONFIG_HOME=str(run / "config"))
commands, results = [], {}


def command(argv, cwd, name):
    start = time.monotonic()
    with (run / (name + ".log")).open("w") as log:
        result = subprocess.run(argv, cwd=cwd, env=env, stdout=log,
                                stderr=subprocess.STDOUT, timeout=180)
    commands.append({"command": argv, "cwd": str(cwd), "exit_code": result.returncode,
                     "seconds": round(time.monotonic() - start, 2)})
    (run / "commands.json").write_text(json.dumps(commands, indent=2) + "\n")
    print(name, result.returncode, flush=True)
    return result.returncode


names = ["index.qmd", "first.qmd", "second.qmd", "references.qmd", "_included.md",
         "references.bib", "extra_advanced.qmd", "extra_appendix.qmd", "extra_references.bib",
         "extra_figure.tex"]
for name in names:
    shutil.copyfile(source / name, book / name)
config = (source / "_quarto.yml").read_text()
config = config.replace("        - second.qmd", "        - second.qmd\n        - extra_advanced.qmd")
config = config.replace("bibliography: references.bib", "  appendices:\n    - extra_appendix.qmd\nbibliography: [references.bib, extra_references.bib]\nnumber-depth: 4\nlink-citations: true")
config = config.replace("    cite-method: biblatex", "    cite-method: biblatex\n    biblio-style: authoryear")
(book / "_quarto.yml").write_text(config)
names += ["_quarto.yml"]
(run / "source_hashes.json").write_text(json.dumps({n: hashlib.sha256((book/n).read_bytes()).hexdigest()
                                                  for n in names}, indent=2) + "\n")
assert command(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape", "extra_figure.tex"], book, "figure") == 0
assert command(["pdftoppm", "-png", "-singlefile", "-r", "100", "extra_figure.pdf", "extra_figure"], book, "figure-png") == 0
names += ["extra_figure.png"]
results["renders"] = {}
for fmt in ["html", "pdf", "latex"]:
    argv = [quarto, "render", "--to", fmt, "--output-dir", "_out-" + fmt]
    if fmt == "latex":
        argv += ["-M", "cite-method:biblatex", "-M", "biblio-style:authoryear"]
    results["renders"][fmt] = command(argv, book, fmt)
results["reference_gate"] = check(book / "_out-html", [run / "html.log"])

# Export must remain compilable with its ordinary bibliography and image assets.
tex_path = next((book / "_out-latex").rglob("Artificial-*.tex"))
tex = tex_path.read_text()
standalone = run / "standalone"
standalone.mkdir()
shutil.copyfile(tex_path, standalone / "toy.tex")
for name in ["references.bib", "extra_references.bib", "extra_figure.png"]:
    shutil.copyfile(book / name, standalone / name)
results["standalone"] = command(["latexmk", "-xelatex", "-interaction=nonstopmode",
    "-halt-on-error", "-no-shell-escape", "toy.tex"], standalone, "standalone")
if results["standalone"] == 0:
    command(["pdftotext", "-layout", "toy.pdf", "toy.txt"], standalone, "standalone-text")
results["live_tex_tokens"] = {t: t in tex for t in [r"\ref{sec-leaf}", r"\ref{fig-extra-curve}",
    r"\ref{alg-toy-update}", r"\label{eq-representative-long}", r"\newcommand{\toyE}",
    r"\autocites", r"\printbibliography"]}


def copy_fixture(name):
    dest = run / name
    dest.mkdir()
    for filename in names:
        shutil.copyfile(book / filename, dest / filename)
    return dest


# Positive mechanical update: insert earlier objects and move one included theorem.
moved = copy_fixture("source_moved")
first = (moved / "first.qmd").read_text()
insertion = "\n::: {#thm-extra-insertion}\n## Inserted test\nZero equals zero.\n:::\n\n$$\n0=0\n$$ {#eq-extra-insertion}\n"
first = first.replace("\n", "\n" + insertion, 1).replace("{{< include _included.md >}}", "")
(moved / "first.qmd").write_text(first)
with (moved / "second.qmd").open("a") as f:
    f.write("\n{{< include _included.md >}}\n")
results["source_moved_render"] = command([quarto, "render", "--to", "html", "--output-dir", "_html"], moved, "source-moved")
results["source_moved_gate"] = check(moved / "_html", [run / "source-moved.log"])
before = (book / "_out-html" / "second.html").read_text()
after = (moved / "_html" / "second.html").read_text()


def ref_html(text, key):
    return re.findall(r'<a[^>]*href="([^"]*#' + re.escape(key) + r')"[^>]*>(.*?)</a>', text, re.S)


results["source_reference_updates"] = {key: {"before": ref_html(before, key), "after": ref_html(after, key)}
                                       for key in ["thm-seed", "eq-seed", "thm-included"]}

# Deliberate failures: absent target types/citation, duplicate ID and broken link.
broken = copy_fixture("negative")
with (broken / "extra_advanced.qmd").open("a") as f:
    f.write("\nMissing @thm-missing-test, @eq-missing-test, @sec-missing-test; [@missingbibtest].\n\n"
            "[]{#duplicate-test}\n\n[]{#duplicate-test}\n\n[Missing local link](first.qmd#missing-anchor-test).\n")
results["negative_render"] = command([quarto, "render", "--to", "html", "--output-dir", "_html"], broken, "negative")
results["negative_gate"] = check(broken / "_html", [run / "negative.log"])
negative_text = json.dumps(results["negative_gate"])
results["negative_cases_detected"] = {key: key in negative_text for key in [
    "thm-missing-test", "eq-missing-test", "sec-missing-test", "missingbibtest", "duplicate-test", "missing-anchor-test"]}
(run / "verification.json").write_text(json.dumps(results, indent=2) + "\n")
updates = results["source_reference_updates"]
success = (all(v == 0 for v in results["renders"].values())
           and results["reference_gate"]["pass"] and results["standalone"] == 0
           and all(results["live_tex_tokens"].values()) and results["source_moved_render"] == 0
           and results["source_moved_gate"]["pass"]
           and all(v["before"] and v["after"] and v["before"] != v["after"] for v in updates.values())
           and not results["negative_gate"]["pass"] and all(results["negative_cases_detected"].values()))
print(json.dumps({"core_pass": success, "evidence": str(run)}, indent=2), flush=True)
raise SystemExit(0 if success else 1)
