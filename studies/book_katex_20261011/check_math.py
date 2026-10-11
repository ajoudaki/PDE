"""Check generated book math with the exact KaTeX JS used by its HTML."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess


class MathParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.formulas = []
        self.current = None
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "").split()
        if self.current is not None:
            self.depth += 1
        elif tag == "span" and "math" in classes:
            self.current = {"display": "display" in classes, "tex": ""}
            self.depth = 1

    def handle_endtag(self, tag):
        if self.current is not None:
            self.depth -= 1
            if not self.depth:
                self.formulas.append(self.current)
                self.current = None

    def handle_data(self, data):
        if self.current is not None:
            self.current["tex"] += data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_dir", type=Path)
    parser.add_argument("katex_js", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    formulas = []
    pages = sorted(args.html_dir.glob("*.html"))
    for page in pages:
        parsed = MathParser()
        parsed.feed(page.read_text())
        for index, formula in enumerate(parsed.formulas):
            text = formula["tex"].strip()
            if (text.startswith(r"\(") and text.endswith(r"\)")) or (
                text.startswith(r"\[") and text.endswith(r"\]")
            ):
                text = text[2:-2]
            formulas.append(dict(formula, tex=text, page=page.name, index=index))
    js = r"""
const fs = require('fs'), katex = require(process.argv[1]);
const formulas = JSON.parse(fs.readFileSync(0, 'utf8')), failures = [];
for (const r of formulas) {
  try { katex.renderToString(r.tex, {
    displayMode: r.display, throwOnError: true, strict: 'ignore'
  }); } catch(e) { failures.push({...r, error:e.message}); }
}
process.stdout.write(JSON.stringify({version:katex.version,
  count:formulas.length, failures}, null, 2));
"""
    result = subprocess.run(
        ["node", "-e", js, str(args.katex_js.resolve())],
        input=json.dumps(formulas), text=True, capture_output=True, check=True,
    )
    report = json.loads(result.stdout)
    report["pages"] = len(pages)
    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(f"KaTeX {report['version']}: {report['count']} formulas across "
          f"{len(pages)} pages; {len(report['failures'])} errors")
    raise SystemExit(bool(report["failures"]) or not formulas)
