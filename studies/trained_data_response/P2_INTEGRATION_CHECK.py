"""Independent read-only correspondence checks for the isolated review."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/trained_data_response'
SCRATCH = ROOT / 'data/generated/trained_data_response/p2_20260911_02/integration_review'
RUN = SCRATCH / 'standalone_run_01'
EDITION = RUN / 'edition/standalone'
sha = lambda b: hashlib.sha256(b).hexdigest()
manifest_bytes = (STUDY / 'P2_PROMOTION_MANIFEST.json').read_bytes()
assert sha(manifest_bytes) == '7ad4d1a5479153bc568c67706c1497ed28d5c64acace30ac0f43ef5f8334a73e'
manifest = json.loads(manifest_bytes)
ancillary = json.loads((STUDY / 'P2_EDITION_ANCILLARY.json').read_text())
hashes = {'P2_PROMOTION_MANIFEST.json': sha(manifest_bytes)}
for group, parent in [('inputs', STUDY), ('established_sha256', ROOT), ('instruction_sha256', ROOT)]:
    for name, expected in manifest[group].items():
        assert sha((parent / name).read_bytes()) == expected, name
        hashes[name] = expected
hashes['P2_INTEGRATION_REVIEW_ASSIGNMENT.md'] = sha((STUDY / 'P2_INTEGRATION_REVIEW_ASSIGNMENT.md').read_bytes())

section = (STUDY / 'P2_SECTION.md').read_text()
original = {name: (ROOT / name).read_text() for name in manifest['established_sha256']}
actual = {name: (EDITION / name).read_text() for name in original}
expected = dict(original)
replacements = []
for change in ancillary['replacements']:
    name, old, new = change['path'], change['old'], change['new']
    assert expected[name].count(old) == 1
    assert new not in expected[name]
    expected[name] = expected[name].replace(old, new)
    replacements.append({'id': change['id'], 'path': name, 'old_sha256': sha(old.encode()),
                         'new_sha256': sha(new.encode())})
expected['docs/global_nonlinear.md'] += '\n' + section
assert actual == expected
restored = dict(actual)
assert restored['docs/global_nonlinear.md'].endswith('\n' + section)
restored['docs/global_nonlinear.md'] = restored['docs/global_nonlinear.md'][:-len('\n' + section)]
for change in reversed(ancillary['replacements']):
    name, old, new = change['path'], change['old'], change['new']
    assert restored[name].count(new) == 1
    restored[name] = restored[name].replace(new, old)
assert restored == original
assert actual['docs/README.md'] == (STUDY / 'P2_PROPOSED_GUIDE.md').read_text()

def headings(text):
    seen = Counter()
    result = set()
    fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        if fenced or not re.match(r'^#{1,6} ', line):
            continue
        title = re.sub(r'^#{1,6} ', '', line).lower()
        slug = re.sub(r'[^\w\s-]', '', title).replace(' ', '-')
        count = seen[slug]
        seen[slug] += 1
        result.add(slug if not count else slug + '-' + str(count))
    return result

affected = []
for change in ancillary['replacements']:
    affected.extend((change['path'], url) for url in re.findall(r'\[[^\]]*\]\(([^)]+)\)', change['new']))
guide = [('docs/README.md', url) for url in re.findall(r'\[[^\]]*\]\(([^)]+)\)', actual['docs/README.md'])]
links = []
for source, url in affected + guide:
    parsed = urlsplit(url)
    if parsed.scheme:
        links.append({'source': source, 'target': url, 'status': 'external preserved, not retrieved'})
        continue
    if (source, url) == ('docs/README.md', '../code/README.md'):
        assert url in original[source]
        assert not (EDITION / 'code').exists()
        links.append({'source': source, 'target': url, 'status': 'explicit preexisting exclusion'})
        continue
    target = (EDITION / source).parent / parsed.path if parsed.path else EDITION / source
    target = target.resolve()
    assert target.is_relative_to(EDITION) and target.is_file()
    if parsed.fragment:
        assert parsed.fragment in headings(target.read_text()), (source, url)
    links.append({'source': source, 'target': url, 'status': 'resolved'})

all_files = sorted(p for p in EDITION.rglob('*') if p.is_file())
assert not any(p.is_symlink() for p in EDITION.rglob('*'))
assert not any(part in ('studies', '.git', '__pycache__') for p in all_files for part in p.relative_to(EDITION).parts)
assert len(list((EDITION / 'docs').glob('*.md'))) == 10
script_details = []
for name in ['P2_PROMOTION_TANGENT_CHECK.py', 'P2_PROMOTION_REFERENCE_CHECK.py', 'P2_PROMOTION_RADIAL_CHECK.py']:
    path = EDITION / 'validation' / name
    assert sha(path.read_bytes()) == manifest['inputs'][name]
    tree = ast.parse(path.read_text())
    imports = sorted({node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)} |
                     {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names})
    script_details.append({'name': name, 'sha256': sha(path.read_bytes()), 'imports': imports})
dependencies = (STUDY / 'P2_PROMOTION_DEPENDENCIES.md').read_text()
reference_code = dependencies.split('###### 5. Reproducible rational Gaussian certificate', 1)[1].split('```python\n', 1)[1].split('\n```', 1)[0]
assert reference_code + '\n' == (STUDY / 'P2_PROMOTION_REFERENCE_CHECK.py').read_text()
tags = re.findall(r'\\tag\s*\{([^{}]+)\}', section)
assert len(tags) == len(set(tags)) and all(t.startswith('C.4.7.') for t in tags)
old_tags = re.findall(r'\\tag\s*\{([^{}]+)\}', original['docs/global_nonlinear.md'])
actual_tags = re.findall(r'\\tag\s*\{([^{}]+)\}', actual['docs/global_nonlinear.md'])
assert actual_tags == old_tags + tags
result = dict(result='PASS', frozen_input_hashes=hashes,
              edition_hashes={name: sha(text.encode()) for name, text in actual.items()},
              exact_inverse_recovers_every_base=True, all_new_material_exact=True,
              section_start_line=actual['docs/global_nonlinear.md'].split(section)[0].count('\n') + 1,
              new_equation_tags=len(tags), original_equation_tags_unchanged=True,
              replacements=replacements, links=links, script_details=script_details,
              reference_script_exactly_matches_displayed_certificate=True,
              standalone_inventory=[str(p.relative_to(EDITION)) for p in all_files])
with (SCRATCH / 'independent_assembly_check.json').open('x') as f:
    json.dump(result, f, indent=2)
    f.write('\n')
print(json.dumps(result, indent=2))
