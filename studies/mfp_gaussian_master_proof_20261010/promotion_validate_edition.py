"""Check final standalone renders, exact source preservation and formal targets."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json
import re
import subprocess
import sys

study = Path(__file__).resolve().parent
generated = study.parents[1]/'data/generated'/study.name
run = generated/sys.argv[1]
edition = run/'edition'
baseline = generated/(sys.argv[2] if len(sys.argv) > 2 else 'promotion_baseline_v1')/'edition'
packet = run/'review_packet'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

sources = json.loads((run/'candidate_manifest.json').read_text())
for name, expected in sources.items():
    assert digest(edition/name) == expected, name
frozen = json.loads((packet/'manifest.json').read_text())['packet_sha256']
for name, expected in frozen.items():
    assert digest(packet/name) == expected, name

chapter = 'docs/02-gaussian-reuse.qmd'
old = (baseline/chapter).read_text()
new = (edition/chapter).read_text()
theory = (packet/'promotion_theory.qmd').read_text().rstrip()+'\n\n'
assert new.count(theory) == 1
restored = new.replace(theory, '', 1)
for patch in reversed(json.loads((packet/'promotion_book_patches.json').read_text())):
    assert restored.count(patch['new']) == 1
    restored = restored.replace(patch['new'], patch['old'], 1)
assert restored == old, 'Unlisted chapter changes'
quarto = (edition/'docs/_quarto.yml').read_text()
for patch in reversed(json.loads((packet/'promotion_quarto_patches.json').read_text())):
    assert quarto.count(patch['new']) == patch.get('count', 1)
    quarto = quarto.replace(patch['new'], patch['old'], patch.get('count', 1))
assert quarto == (baseline/'docs/_quarto.yml').read_text()

class Ids(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.nodes = {}
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.nodes[attrs['id']] = {'tag':tag, 'class':attrs.get('class', '')}

html = Ids((run/'rendered_html/02-gaussian-reuse.html').read_text()).nodes
old_ids = set(re.findall(r'\{#([^ }]+)', old))
new_ids = set(re.findall(r'\{#([^ }]+)', theory))
assert old_ids <= html.keys(), old_ids-html.keys()
assert new_ids <= html.keys(), new_ids-html.keys()
formal = {name:html[name] for name in sorted(new_ids)
          if name.startswith(('thm-', 'lem-', 'prp-', 'def-', 'proof-'))}
for name, value in formal.items():
    if not name.startswith('proof-'):
        assert 'theorem' in value['class'], (name, value)

for fmt in ('html', 'pdf', 'latex'):
    assert json.loads((run/f'render_logs/{fmt}.json').read_text())['exit_code'] == 0
    log = (run/f'render_logs/{fmt}.log').read_text()
    assert not re.search(r'undefined (?:references|citations)|Unable to resolve|WARNING.*(?:ref|cit)', log, re.I), fmt
assert not json.loads((run/'html_links.json').read_text())['errors']
pdf = run/'rendered_pdf/DTDL.pdf'
check = subprocess.run(['qpdf', '--check', str(pdf)], capture_output=True, text=True)
assert check.returncode == 0, check.stdout+check.stderr
subprocess.run(['pdftotext', '-layout', str(pdf), str(run/'pdf_text.txt')], check=True)
text = (run/'pdf_text.txt').read_text()
section = text[text.index('Fixed finite Gaussian derivative programs\n'):]
section = section[:section.index('7. Reusable finite calculus and forest factorization')]
assert 'Definition 0.0.1' not in section
assert 'Definition 1 (Finite Gaussian program)' in section
assert not re.search(r'Section\s*\.', section)
latex = run/'rendered_latex/book-latex/DTDL.tex'
assert latex.is_file() and latex.stat().st_size > 100000
for name in new_ids:
    assert name in latex.read_text(), name
report = {'frozen_sources_unchanged':len(sources), 'frozen_packet_unchanged':len(frozen),
          'old_chapter_ids_preserved':len(old_ids), 'new_ids_present':len(new_ids),
          'chapter_exact_restoration':True, 'quarto_only_declared_counter_patch':True,
          'formal_html_nodes':formal, 'pdf_qpdf_output':check.stdout+check.stderr,
          'pdf_and_latex':{str(p.relative_to(run)):digest(p) for p in (pdf, latex)},
          'pdf_new_section_references_and_definition_checked':True}
(run/'structural_validation.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
