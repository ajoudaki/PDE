"""Build a typeset snapshot without changing any repository source.

All generated files and PDF-only formatting live in the private build directory.
"""
from pathlib import Path
import collections
import argparse
import hashlib
import json
import posixpath
import re
import subprocess

parser = argparse.ArgumentParser(description="Internal PDF-only rendering helper")
parser.add_argument("build_directory", type=Path)
args = parser.parse_args()
ROOT = args.build_directory.resolve()
config = json.loads((ROOT / "build-config.json").read_text())
PANDOC = ROOT / "pandoc"
FILES = config["files"]

def visit(node, fn):
    if isinstance(node, list):
        return [visit(x, fn) for x in node]
    if isinstance(node, dict):
        node = {k: visit(v, fn) for k, v in node.items()}
        return fn(node)
    return node

def tex_escape(text):
    replacements = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
                    "$": r"\$", "&": r"\&", "#": r"\#", "%": r"\%",
                    "_": r"\_", "^": r"\textasciicircum{}", "~": r"\textasciitilde{}"}
    return "".join(replacements.get(x, x) for x in text)

def wrap_long_integer_tuple(body):
    """Reflow a literal integer tuple assignment without altering any token."""
    match = re.fullmatch(r"([^=\n]+)\s*=\s*\(\s*([+\-\d,\s]+)\s*\)([.;,]?)", body.strip())
    if not match:
        return body
    lhs, literal, punctuation = match.groups()
    values = [x.strip() for x in literal.split(",")]
    if any(not re.fullmatch(r"[+-]?\d+", x) for x in values):
        return body
    if len(",".join(values)) <= 90:
        return body
    rows, row = [], []
    for value in values:
        if row and len(",".join(row + [value])) > 48:
            rows.append(",".join(row) + ",")
            row = []
        row.append(value)
    rows.append(",".join(row))
    lines = ["&(" + rows[0]] + [r"&\quad " + x for x in rows[1:]]
    lines[-1] += ")" + punctuation
    return (r"\begin{gathered}" + "\n" + lhs.strip() + r"={}\\" + "\n"
            + r"\begin{aligned}" + "\n" + "\\\\\n".join(lines) + "\n"
            + r"\end{aligned}" + "\n" + r"\end{gathered}")

documents = []
targets = {}
manifest = {}
counts = collections.Counter()
equations = []
for filename, chapter in FILES:
    source = ROOT / "snapshot" / filename
    raw = source.read_bytes()
    manifest[filename] = {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    ast = json.loads(subprocess.check_output([
        str(PANDOC), "--from=markdown+tex_math_single_backslash-superscript-subscript", "--to=json", str(source)
    ]))
    namespace = filename.replace("/", "-").replace(".md", "").lower()
    def name_target(node):
        if node.get("t") in ("Span", "Div") and node["c"][0][0]:
            old = node["c"][0][0]
            new = namespace + "--" + old
            node["c"][0][0] = new
            targets[filename + "#" + old] = new
        if node.get("t") == "Header":
            old = node["c"][1][0]
            new = namespace + "--" + old
            node["c"][1][0] = new
            targets[filename + "#" + old] = new
            if node["c"][0] == 1:
                targets.setdefault(filename, new)
                if chapter.isdigit():
                    node["c"][2] = [{"t": "Str", "c": chapter + "."}, {"t": "Space"}] + node["c"][2]
                if chapter == "Appendix":
                    node["c"][2] = [{"t": "Str", "c": "Appendix."}, {"t": "Space"}] + node["c"][2]
        if node.get("t") in ("RawBlock", "RawInline") and node["c"][0] == "html":
            match = re.fullmatch(r'\s*<a\s+(?:id|name)=[\"\']([^\"\']+)[\"\']\s*>\s*(?:</a>\s*)?', node["c"][1])
            if match:
                old = match[1]
                new = namespace + "--" + old
                targets[filename + "#" + old] = new
                return {"t": node["t"], "c": ["latex", r"\phantomsection\label{" + new + "}"]}
            if node["c"][1].strip() == "</a>":
                return {"t": node["t"], "c": ["latex", ""]}
        return node
    ast = visit(ast, name_target)
    documents.append((filename, ast))

all_blocks = []
unresolved = []
for filename, ast in documents:
    def transform(node):
        kind = node.get("t")
        counts[kind] += 1
        if kind == "Math":
            # Group the existing layer-indexed matrix before its transpose.
            # Two source occurrences otherwise have invalid double superscripts.
            node["c"][1] = node["c"][1].replace(r"W^{(\ell)}_n^T", r"(W^{(\ell)}_n)^T")
        if kind == "Link":
            target = node["c"][2][0]
            if not re.match(r"^[a-zA-Z]+:", target):
                base, sep, anchor = target.partition("#")
                dest = posixpath.normpath(posixpath.join(posixpath.dirname(filename), base)) if base else filename
                key = dest + ("#" + anchor if sep else "")
                if key in targets:
                    node["c"][2][0] = "#" + targets[key]
                else:
                    unresolved.append({"from": filename, "target": target})
        if kind == "Math" and node["c"][0]["t"] == "DisplayMath":
            body = node["c"][1]
            tags = re.findall(r"\\tag\*?\{([^{}]*)\}", body)
            if len(tags) > 1:
                raise ValueError((filename, "Multiple equation tags", body))
            body = re.sub(r"\\tag\*?\{([^{}]*)\}", "", body).strip()
            body = body.replace(r"\begin{split}", r"\begin{aligned}").replace(r"\end{split}", r"\end{aligned}")
            body = wrap_long_integer_tuple(body)
            tag = tags[0] if tags else ""
            eid = "E" + str(len(equations) + 1)
            equations.append({"id": eid, "source": filename, "body": body, "tag": tag})
            return {"t": "RawInline", "c": ["latex", "\\ExportDisplay{" + eid + "}{\n" + body + "\n}{" + tag + "}"]}
        if kind == "Code":
            value = node["c"][1]
            escaped = "".join(tex_escape(ch) + (r"\allowbreak{}" if ch in "_/,:=+-" else "") for ch in value)
            return {"t": "RawInline", "c": ["latex", r"{\small\texttt{" + escaped + "}}"]}
        if kind == "Str" and len(node["c"]) >= 12 and re.search(r"[_^]|~N", node["c"]):
            escaped = "".join(tex_escape(ch) + (r"\allowbreak{}" if ch in "_/,:=+-)" else "") for ch in node["c"])
            return {"t": "RawInline", "c": ["latex", escaped]}
        if kind == "Table":
            columns = node["c"][2]
            if len(columns) == 2:
                weights = [.28, .72]
            elif len(columns) == 3:
                weights = [.24, .38, .38]
            else:
                weights = [1 / len(columns)] * len(columns)
            for spec, weight in zip(columns, weights):
                spec[1] = {"t": "ColWidth", "c": weight}
        return node
    ast = visit(ast, transform)
    all_blocks.extend(ast["blocks"])

if unresolved:
    raise ValueError("Unresolved book links: " + repr(unresolved))

out = {"pandoc-api-version": documents[0][1]["pandoc-api-version"], "meta": {}, "blocks": all_blocks}
(ROOT / "book.json").write_text(json.dumps(out), encoding="utf-8")
(ROOT / "source-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
(ROOT / "equation-index.json").write_text(json.dumps(equations, indent=2) + "\n")
(ROOT / "coverage.json").write_text(json.dumps({"files": [x[0] for x in FILES], "ast_counts": dict(counts), "display_equations": len(equations), "link_targets": len(targets), "unresolved_links": unresolved}, indent=2) + "\n")
subprocess.run([
    str(PANDOC), str(ROOT / "book.json"), "--from=json", "--to=latex", "--standalone",
    "--top-level-division=chapter", "--toc", "--toc-depth=2", "--no-highlight",
    "--metadata=title:Deep Neural Network Learning Dynamics",
    "--metadata=author:Project PDE", "--metadata=date:" + config["date"],
    "--variable=documentclass:scrreprt", "--variable=classoption:oneside", "--variable=classoption:open=any",
    "--variable=classoption:enabledeprecatedfontcommands",
    "--variable=fontsize:11pt", "--variable=papersize:a4",
    "--variable=geometry:top=23mm,bottom=23mm,left=22mm,right=22mm,headheight=15pt,headsep=7mm,footskip=11mm",
    "--variable=mainfont:TeX Gyre Pagella", "--variable=sansfont:TeX Gyre Heros",
    "--variable=monofont:DejaVu Sans Mono", "--variable=monofontoptions:Scale=0.83",
    "--variable=mathfont:TeX Gyre Pagella Math", "--variable=colorlinks:true",
    "--variable=linkcolor:ExportBlue", "--variable=urlcolor:ExportBlue", "--variable=toccolor:black",
    "--include-in-header=" + str(ROOT / "layout.tex"), "--output=" + str(ROOT / "book.tex")
], check=True)
print(json.dumps({"source_files": len(FILES), "display_equations": len(equations), "internal_targets": len(targets), "unresolved_links": unresolved}, indent=2))
