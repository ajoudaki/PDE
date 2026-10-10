"""Check the frozen section and all local HTML targets in a rendered edition."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links = [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])


def check(stage):
    stage = Path(stage).resolve()
    packet = stage / "review_inputs"
    manifest = json.loads((packet / "manifest.json").read_text())
    errors = []
    for name, entry in manifest.items():
        source = stage / entry["source"] if name == "assembled_chapter" else packet / name
        if hashlib.sha256(source.read_bytes()).hexdigest() != entry["sha256"]:
            errors.append(f"Frozen input changed: {source}")
    chapter = stage / "docs/08b-trajectory-compression.qmd"
    text = chapter.read_text()
    candidate = (packet / "PROMOTION_SECTION.qmd").read_text().rstrip() + "\n\n"
    original = (packet / "08b-trajectory-compression.qmd").read_text()
    if text.count(candidate) != 1 or text.replace(candidate, "", 1) != original:
        errors.append("Assembly is not exactly the proposed insertion")
    output = stage / "data/generated/DTDL"
    pages = {p: Page(p.read_text()) for p in output.glob("*.html")}
    for path, page in pages.items():
        duplicate = [key for key, count in Counter(page.ids).items() if count > 1]
        if duplicate:
            errors.append(f"Duplicate HTML IDs in {path.name}: {duplicate}")
        for link in page.links:
            uri = urlsplit(link)
            if uri.scheme or uri.netloc or link.startswith(("javascript:", "mailto:")):
                continue
            target = (path.parent / unquote(uri.path)).resolve() if uri.path else path
            if target.is_dir():
                target /= "index.html"
            if not target.exists():
                errors.append(f"Missing local target: {path.name}: {link}")
            elif uri.fragment and target in pages and unquote(uri.fragment) not in pages[target].ids:
                errors.append(f"Missing HTML fragment: {path.name}: {link}")
        unresolved = re.findall(r"@(?:eq|thm|lem|prp|cor|sec|ch)-[A-Za-z0-9_-]+", path.read_text())
        if unresolved:
            errors.append(f"Unresolved rendered refs: {path.name}: {sorted(set(unresolved))}")
    if len(pages) != 18:
        errors.append(f"Expected 18 rendered book HTML pages, got {len(pages)}")
    for suffix in ("pdf", "tex"):
        if not (output / f"DTDL.{suffix}").is_file():
            errors.append(f"Missing complete edition DTDL.{suffix}")
    result = {"html_pages": len(pages), "errors": sorted(set(errors)),
              "candidate_sha256": manifest["PROMOTION_SECTION.qmd"]["sha256"]}
    print(json.dumps(result, indent=2))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check(sys.argv[1]))
