"""Extract the reviewed book section and dry-run its exact source patch."""
from pathlib import Path
import difflib
import hashlib
import json
import subprocess
import sys

study = Path(__file__).resolve().parent
root = study.parents[1]
generated = root / 'data/generated' / study.name
run = generated / sys.argv[1]
baseline = generated / sys.argv[2]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, data):
    (run / name).write_text(json.dumps(data, indent=2) + '\n')


pdf = run / 'rendered_pdf/DTDL.pdf'
pages = (run / 'pdf_text.txt').read_text().split('\f')
starts = [i + 1 for i, page in enumerate(pages)
          if 'Fixed finite Gaussian derivative programs\n' in page]
ends = [i + 1 for i, page in enumerate(pages)
        if '7. Reusable finite calculus and forest factorization\n' in page]
assert len(starts) == len(ends) == 1, (starts, ends)
assert starts[0] < ends[0]
window = [max(1, starts[0] - 1), min(len(pages) - 1, ends[0] + 1)]
preview = run / 'mfp_book_preview.pdf'
assert not preview.exists()
subprocess.run(['qpdf', str(pdf), '--pages', str(pdf),
                f'{window[0]}-{window[1]}', '--', str(preview)], check=True)
save('preview_manifest.json', {
    'source': str(pdf.relative_to(root)), 'source_sha256': digest(pdf),
    'pages': window, 'section_boundary_pages': [starts[0], ends[0]],
    'preview': str(preview.relative_to(root)), 'preview_sha256': digest(preview),
    'purpose': 'Exact excerpt from the full rendered candidate with adjoining context.'})

changed = json.loads((run / 'changed_manifest.json').read_text())
patch = run / 'reviewed_changes.patch'
assert not patch.exists()
chunks = []
for name, expected in changed.items():
    old, new = baseline / 'edition' / name, run / 'edition' / name
    assert digest(new) == expected, name
    chunks.extend(difflib.unified_diff(
        old.read_text().splitlines(keepends=True) if old.exists() else [],
        new.read_text().splitlines(keepends=True),
        fromfile='a/' + name if old.exists() else '/dev/null', tofile='b/' + name))
patch.write_text(''.join(chunks))
command = ['patch', '--dry-run', '--batch', '--forward', '-p1',
           '-d', str(baseline / 'edition')]
result = subprocess.run(command, input=patch.read_text(), text=True, capture_output=True)
assert result.returncode == 0, result.stdout + result.stderr
save('patch_manifest.json', {
    'path': str(patch.relative_to(root)), 'sha256': digest(patch),
    'files': list(changed),
    'baseline_manifest_sha256': digest(baseline / 'candidate_manifest.json'),
    'changed_manifest_sha256': digest(run / 'changed_manifest.json'),
    'dry_run': {'command': command, 'stdin': str(patch.relative_to(root)),
                'exit_code': result.returncode, 'stdout': result.stdout,
                'stderr': result.stderr}})
print(json.dumps({'preview_pages': window, 'patch_files': len(changed),
                  'patch_bytes': patch.stat().st_size, 'dry_run': 'PASS'}, indent=2))
