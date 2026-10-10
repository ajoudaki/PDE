"""Check rendered book links/IDs and frozen-source structural preservation."""
from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            self.ids.append(values['id'])
        if tag == 'a' and 'href' in values:
            self.links.append(values['href'])
        if tag in ('img', 'script', 'iframe', 'source') and 'src' in values:
            self.links.append(values['src'])
        if tag == 'link' and 'href' in values:
            self.links.append(values['href'])


def check(root):
    errors = []
    pages = {}
    book = []
    for path in sorted(root.rglob('*.html')):
        if any(p in ('code', 'docs', 'site_libs') for p in path.relative_to(root).parts[:-1]):
            continue
        page = Page(path.read_text())
        pages[path.resolve()] = page
        book.append(path)
        duplicates = [key for key, n in Counter(page.ids).items() if n > 1]
        if duplicates:
            errors.append(f'{path.name}: duplicate IDs {duplicates}')
    checked = 0
    for path in book:
        for link in pages[path.resolve()].links:
            uri = urlsplit(link)
            if uri.scheme or uri.netloc or uri.path.startswith('/'):
                continue
            target = (path.parent / unquote(uri.path)).resolve() if uri.path else path.resolve()
            if target.is_dir():
                target = target / 'index.html'
            if not target.is_file():
                errors.append(f'{path.name}: missing {link}')
                continue
            checked += 1
            if uri.fragment and target.suffix == '.html':
                if target not in pages:
                    pages[target] = Page(target.read_text())
                if unquote(uri.fragment) not in pages[target].ids:
                    errors.append(f'{path.name}: missing fragment {link}')
            elif uri.fragment and target.suffix in ('.qmd', '.md'):
                text = target.read_text()
                # Explicit Quarto identifiers and ordinary Markdown heading slugs.
                ids = set(re.findall(r'\{#([^ }]+)', text))
                for heading in re.findall(r'^#+\s+(.+)$', text, re.M):
                    slug = re.sub(r'[^\w\s-]', '', heading.lower())
                    ids.add(re.sub(r'\s+', '-', slug.strip()))
                if unquote(uri.fragment) not in ids:
                    errors.append(f'{path.name}: missing source fragment {link}')
    result = {'book_html_pages':len(book), 'checked_local_links':checked,
              'errors':errors, 'scope':'Local rendered book href/src targets and fragments, page IDs; no external URL availability audit.'}
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--report', required=True, type=Path)
    args = parser.parse_args()
    report = check(args.output.resolve())
    args.report.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(bool(report['errors']))
