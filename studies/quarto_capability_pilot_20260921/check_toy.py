"""Check toy links and standalone TeX; exercise insertion and a missing reference."""
import argparse
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit

parser = argparse.ArgumentParser()
parser.add_argument("--quarto", type=Path, required=True)
parser.add_argument("--run-directory", type=Path, required=True)
args = parser.parse_args()
run = args.run_directory.resolve()
book = run / "book"
results = {}

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.duplicates = set(), [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            if a["id"] in self.ids:
                self.duplicates.append(a["id"])
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])

html = book / "_out-html"
pages = {p.resolve(): Page(p.read_text()) for p in html.glob("*.html")}
bad = []
for path, page in pages.items():
    for href in page.links:
        u = urlsplit(href)
        if u.scheme or u.netloc:
            continue
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if target.suffix != ".html":
            continue
        if target not in pages or (u.fragment and unquote(u.fragment) not in pages[target].ids):
            bad.append([path.name, href])
results["html"] = {"pages": len(pages), "broken_links": bad,
                   "duplicate_ids": {p.name: v.duplicates for p, v in pages.items() if v.duplicates}}

commands = []
def command(argv, cwd, logname, env=None):
    with (run / logname).open("w") as log:
        r = subprocess.run(argv, cwd=cwd, env=env, stdout=log,
                           stderr=subprocess.STDOUT, timeout=180)
    commands.append({"command": argv, "cwd": str(cwd), "exit_code": r.returncode})
    (run / "verification_commands.json").write_text(json.dumps(commands, indent=2) + "\n")
    return r.returncode

tex = next((book / "_out-latex").rglob("*.tex"))
text = tex.read_text()
results["live_tex_commands"] = {token: token in text for token in [
    r"\label{thm-seed}", r"\ref{thm-seed}", r"\label{eq-seed}", r"\ref{eq-seed}",
    r"\textcite{toy2026}", r"\autocite[7]{toy2026}", r"\printbibliography"]}

def compile_tex(name, content):
    dest = run / name
    dest.mkdir(exist_ok=False)
    (dest / "toy.tex").write_text(content)
    shutil.copyfile(book / "references.bib", dest / "references.bib")
    rc = command(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
                  "-no-shell-escape", "toy.tex"], dest, name + ".log")
    aux = (dest / "toy.aux").read_text() if (dest / "toy.aux").exists() else ""
    labels = {}
    for key in ["thm-seed", "thm-included", "eq-seed", "eq-balance"]:
        m = re.search(r"\\newlabel\{" + re.escape(key) + r"\}\{\{([^}]*)\}", aux)
        labels[key] = m.group(1) if m else None
    results[name] = {"exit_code": rc, "labels": labels}
    if rc == 0:
        command(["pdftotext", "-layout", "toy.pdf", "toy.txt"], dest, name + "-text.log")
    return dest

compile_tex("standalone", text)
insert = (r"\begin{theorem}[Inserted fixture]" + "\n"
          + r"\label{thm-inserted}An inserted test statement.\end{theorem}" + "\n"
          + r"\begin{equation}\label{eq-inserted}0=0\end{equation}" + "\n")
needle = r"\begin{equation}\protect\phantomsection\label{eq-seed}"
assert text.count(needle) == 1
compile_tex("standalone_inserted", text.replace(needle, insert + needle))
results["insertion_changes_numbers"] = all(
    results["standalone"]["labels"][key] is not None
    and results["standalone"]["labels"][key] != results["standalone_inserted"]["labels"][key]
    for key in ["thm-seed", "eq-seed"])

missing = run / "missing_reference"
missing.mkdir(exist_ok=False)
for name in json.loads((run / "source_hashes.json").read_text()):
    shutil.copyfile(book / name, missing / name)
with (missing / "second.qmd").open("a") as f:
    f.write("\nDeliberately missing reference: @thm-does-not-exist.\n")
env = dict(os.environ, XDG_CACHE_HOME=str(run / "cache"), XDG_CONFIG_HOME=str(run / "config"))
rc = command([str(args.quarto.resolve()), "render", "--to", "html"], missing,
             "missing-reference.log", env)
results["missing_reference"] = {"exit_code": rc,
    "diagnostic_lines": [x for x in (run / "missing-reference.log").read_text().splitlines()
                         if "WARN" in x or "does-not-exist" in x]}
rc = command([str(args.quarto.resolve()), "render", "--to", "html",
              "--fail-if-warnings", "--output-dir", "_strict"], missing,
             "missing-reference-strict.log", env)
results["missing_reference_strict"] = {"exit_code": rc,
    "diagnostic_lines": [x for x in (run / "missing-reference-strict.log").read_text().splitlines()
                         if "WARN" in x or "ERROR" in x or "does-not-exist" in x]}
(run / "verification.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2), flush=True)
core_pass = (len(pages) == 4 and not bad and not results["html"]["duplicate_ids"]
             and all(results["live_tex_commands"].values())
             and results["standalone"]["exit_code"] == 0
             and results["standalone_inserted"]["exit_code"] == 0
             and results["insertion_changes_numbers"])
raise SystemExit(0 if core_pass else 1)
