"""Freeze a presentation-corrected edition's neutral integration inputs."""
import hashlib
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
start = time.process_time()
root = Path(__file__).resolve().parents[2]
study = root / 'studies/observable_hierarchy'
old = root / 'data/generated/observable_hierarchy/H3_v2_edition_v2'
new = root / 'data/generated/observable_hierarchy/H3_v2_edition_v3'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
old_manifest = json.loads((old/'review/manifest.json').read_text())
new_manifest = json.loads((new/'review/manifest.json').read_text())
before = 'sup_t e_N<=CT exp[C(1+s)T]((1+s)epsilon_N+tau(s)).'
after = r'''\[
\sup_{t} e_N\le CT\,\exp\!\bigl(C(1+s)T\bigr)
\bigl((1+s)\epsilon_N+\tau(s)\bigr).
\]'''
changed = []
for relative, digest in old_manifest['edition_hashes'].items():
    assert sha(old/relative) == digest
    assert sha(new/relative) == new_manifest['edition_hashes'][relative]
    if (old/relative).read_bytes() != (new/relative).read_bytes():
        a, b = (old/relative).read_text(), (new/relative).read_text()
        assert a.count(before) == b.count(after) == 1
        assert a.replace(before, after) == b
        changed.append(relative)
assert sorted(changed) == ['docs/global_nonlinear.md', 'review/proposed_section.md']
import markdown
rendered = markdown.markdown(after)
assert '<a ' not in rendered and 'epsilon_N' in rendered and 'tau(s)' in rendered
base_manifest = json.loads((study/'H3_v2_integration_manifest_v3.json').read_text())
for relative, item in base_manifest['base_files'].items():
    assert sha(root/relative) == item['sha256'] == sha(root/item['source'])
manifest = {
    'role': 'complete neutral integration packet; no prior verdicts',
    'edition_root': str(new.relative_to(root)),
    'edition_manifest_sha256': sha(new/'review/manifest.json'),
    'reproduced_edition_root': str(old.relative_to(root)),
    'reproduced_edition_manifest_sha256': sha(old/'review/manifest.json'),
    'evidence_manifest': 'studies/observable_hierarchy/H3_v2_evidence_v3.json',
    'evidence_manifest_sha256': sha(study/'H3_v2_evidence_v3.json'),
    'base_files': base_manifest['base_files'],
    'presentation_correspondence': {
        'changed_files': changed, 'before': before, 'after': after,
        'other_25_files_byte_identical': True,
        'verification_source': str(Path(__file__).relative_to(root)),
        'verification_source_sha256': sha(Path(__file__)),
    },
}
path = study/'H3_v2_integration_manifest_v4.json'
assert not path.exists()
path.write_text(json.dumps(manifest, indent=2)+'\n')
assignment = (study/'H3_v2_integration_assignment_v3.md').read_text()
assignment = assignment.replace('packet v3, edition v2', 'packet v4, edition v3')
assignment = assignment.replace('H3_v2_edition_v2/', 'H3_v2_edition_v3/')
assignment = assignment.replace('H3_v2_integration_manifest_v3.json', 'H3_v2_integration_manifest_v4.json')
assignment = assignment.replace('H3_v2_integration_v3.md', 'H3_v2_integration_v4.md')
assignment = assignment.replace('H3_v2_integration_v3/', 'H3_v2_integration_v4/')
assignment += '''
The execution evidence was produced by the separate frozen edition v2,
whose complete `review/manifest.json` and all 27 listed edition files are
also inputs. The v4 integration manifest names both roots explicitly.
Verify correspondence: all implementations, tests, guides, dependencies and
the exact executed plan are byte-identical; only the rendering of one bound
in the section and full chapter differs. Both complete versions of that
bound and the exact static correspondence source are supplied. Inspect this
source in full. Read the complete new edition; the byte-identical older
bodies need no duplicate scientific reading. Read the differing old bound
and verify its meaning is preserved. Execution logs must remain attributed
to their actual v2 source; they are not a new v3 execution. No old human
review or reproduction report is an input. Check mathematical rendering as
well as link syntax throughout the new section. All other scope, complete
read requirements and budgets above remain in force.
'''
assignment_path = study/'H3_v2_integration_assignment_v4.md'
assert not assignment_path.exists()
assignment_path.write_text(assignment)
result = dict(changed_files=changed, other_files_identical=25,
              no_accidental_bound_link=True, markdown_version=markdown.__version__,
              cpu_seconds=time.process_time()-start,
              edition_manifest_sha256=sha(new/'review/manifest.json'),
              integration_manifest_sha256=sha(path),
              assignment_sha256=sha(assignment_path))
scratch = root/'data/generated/observable_hierarchy/H3_v2_presentation_check_v4'
scratch.mkdir(exist_ok=False)
(scratch/'result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
