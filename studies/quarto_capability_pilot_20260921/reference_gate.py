"""Small toy gate: known reference diagnostics, HTML IDs and local HTML links.

This does not decide whether a valid destination is scientifically correct, or
whether prose contains a reference that was never converted to a link.
"""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.duplicates = set(), [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            key = attrs["id"]
            if key in self.ids:
                self.duplicates.append(key)
            self.ids.add(key)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])


def check(directory, logs):
    pages = {p.resolve(): Page(p.read_text()) for p in directory.rglob("*.html")}
    broken = []
    for path, page in pages.items():
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.suffix != ".html":
                continue
            if target not in pages or (url.fragment and unquote(url.fragment) not in pages[target].ids):
                broken.append([path.name, href])
    diagnostics = []
    pattern = r"Unable to resolve crossref|citation .+ not found|Duplicate identifier|undefined references|undefined citations"
    for log in logs:
        diagnostics.extend(line for line in log.read_text().splitlines()
                           if re.search(pattern, line, flags=re.IGNORECASE))
    duplicates = {p.name: page.duplicates for p, page in pages.items() if page.duplicates}
    return {"pass": bool(pages) and not (broken or diagnostics or duplicates),
            "pages": len(pages), "broken_links": broken,
            "duplicate_ids": duplicates, "diagnostics": diagnostics}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("logs", type=Path, nargs="*")
    args = parser.parse_args()
    result = check(args.directory, args.logs)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["pass"] else 1)
