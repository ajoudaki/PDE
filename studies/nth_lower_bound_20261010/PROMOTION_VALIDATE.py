"""Check the frozen NTH proposed edition after its full HTML/PDF build."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import subprocess
import sys

w = Path(sys.argv[1]).resolve()
out = w / 'data/generated/DTDL'
manifest = json.loads((w / 'manifest.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
expected = {r['path']: r['sha256'] for r in manifest['original_library']}
expected.update({r['path']: r['sha256'] for r in manifest['changed']})
assert all(sha(w / p) == h for p, h in expected.items())
candidate = (w / 'candidate.qmd').read_text()
assert candidate in (w / 'docs/07-observable-closure.qmd').read_text()
ids = re.findall(r'\{#([\w-]+)', candidate)

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links = [], []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])

pages = {p.resolve(): Page(p) for p in out.glob('*.html')}
errors = []
for path, page in pages.items():
    if len(page.ids) != len(set(page.ids)):
        errors.append([path.name, 'duplicate HTML ID'])
    for link in page.links:
        u = urlsplit(link)
        if u.scheme or u.netloc or u.path.startswith('/'):
            continue
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if not target.exists():
            errors.append([path.name, link, 'missing local file'])
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append([path.name, link, 'missing HTML fragment'])
assert len(pages) == 18
assert set(ids) <= set(pages[(out / '07-observable-closure.html').resolve()].ids)
assert not errors, errors

tex = (out / 'docs/DTDL.tex').read_text()
assert all(('\\label{' + i + '}') in tex for i in ids)
start = tex.index('\\section{Literal storage of a frozen-top')
end = tex.index('\\section{', start + 1)
region = tex[start:end]
environments = {'theorem': 1, 'lemma': 5, 'corollary': 1, 'proof': 6}
for env, count in environments.items():
    assert region.count('\\begin{' + env + '}') == count, env
    assert region.count('\\end{' + env + '}') == count, env
assert 'is established in \\hyperref[thm-nth-storage-matching]{its storage theorem}' in re.sub(r'\s+', ' ', tex)
pdf = subprocess.check_output(['pdftotext', '-layout', str(out / 'DTDL.pdf'), '-'], text=True)
flat = re.sub(r'\s+', ' ', pdf)
assert 'is established in its storage theorem' in flat
assert 'is established in Section .' not in flat
builds = json.loads((w / 'validation/builds.json').read_text())
assert {r['format'] for r in builds} == {'html', 'pdf', 'editable-latex'}
assert all(r['exit_code'] == 0 for r in builds)
result = {'status': 'PASS', 'frozen_files': len(expected), 'html_pages': len(pages),
          'new_ids': len(ids), 'broken_links': errors, 'formal_environments': environments,
          'pdf_pointer': 'descriptive theorem link verified',
          'pdf_sha256': sha(out / 'DTDL.pdf'), 'tex_sha256': sha(out / 'docs/DTDL.tex')}
(w / 'validation/final_checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
