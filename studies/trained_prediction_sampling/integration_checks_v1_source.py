"""Integration integrity checks; no scientific reads beyond the frozen packet."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import platform
import re

ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/trained_prediction_sampling'
SCRATCH = ROOT / 'data/generated/trained_prediction_sampling/integration_v1'
FRESH = ROOT / 'data/generated/trained_prediction_sampling/integration_v1_edition'
FROZEN = ROOT / 'data/generated/trained_prediction_sampling/standalone_v1'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
edits = json.loads((STUDY / 'promotion_edits.json').read_text())
proposal = (STUDY / 'proposal_C4_8.md').read_bytes()
text = proposal.decode()
results = {}
for name in ('docs/global_nonlinear.md', 'docs/README.md'):
    original = (ROOT / name).read_bytes()
    fresh = (FRESH / name).read_bytes()
    assembled = (FROZEN / name).read_bytes()
    assert fresh == assembled
    relevant = [edit for edit in edits['replacements'] if edit['path'] == name]
    restored = fresh
    if name == edits['append']['path']:
        assert restored.endswith(b'\n\n' + proposal)
        restored = restored[:-len(proposal)-2]
        assert b''.join(assembled.splitlines(keepends=True)[11439:12974]) == proposal
    for edit in reversed(relevant):
        new, old = edit['new'].encode(), edit['old'].encode()
        assert restored.count(new) == 1
        restored = restored.replace(new, old, 1)
    assert restored == original
    results[name] = {'fresh_equals_frozen': True, 'byte_inverse_equals_live': True,
                     'sha256': sha(FRESH / name), 'replacement_count': len(relevant)}
assert (FRESH / 'docs/NOTATION.md').read_bytes() == (ROOT / 'docs/NOTATION.md').read_bytes()
assert (FRESH / 'docs/NOTATION.md').read_bytes() == (FROZEN / 'docs/NOTATION.md').read_bytes()
tags = re.findall(r'\\tag\{(C\.4\.8\.[^}]+)\}', text)
assert len(tags) == len(set(tags)) == 88
# Read other bytes here only to extract tag metadata, not their scientific bodies.
all_tags = Counter(re.findall(r'\\tag\{([^}]+)\}', (FRESH / 'docs/global_nonlinear.md').read_text()))
assert all(all_tags[tag] == 1 for tag in tags)
new_refs = set(re.findall(r'\((C\.4\.8\.[PSR]\d+)\)', text))
assert new_refs <= set(tags)
named_older_refs = sorted(set(re.findall(r'C\.4\.[67]\.[A-Za-z]+[A-Za-z0-9-]*', text)))
assert all(ref in all_tags for ref in named_older_refs)
head = text.splitlines()[0].lstrip('# ').lower()
anchor = re.sub(r'[^\w\- ]', '', head).replace(' ', '-')
assert anchor == 'c48-sampling-fluctuations-of-the-trained-prediction'
assert ('global_nonlinear.md#' + anchor) in (FRESH / 'docs/README.md').read_text()
assert 'studies/' not in text and 'data/generated/' not in text
commands = sorted(set(re.findall(r'\\([A-Za-z]+)', text)))
hash_paths = [
    ROOT / 'AGENTS.md', ROOT / 'RESEARCH_WORKFLOW.md',
    STUDY / 'integration_packet_v1.md', STUDY / 'proposal_C4_8.md',
    STUDY / 'promotion_edits.json', STUDY / 'validate_proposal.py',
    STUDY / 'check_gaussian_calculus.py', STUDY / 'check_sampling_hoeffding.py',
    *[ROOT / f'docs/{n}.md' for n in ('global_nonlinear','README','NOTATION','finite_dynamics')],
    *[FROZEN / f'docs/{n}.md' for n in ('global_nonlinear','README','NOTATION')],
    *[FRESH / f'docs/{n}.md' for n in ('global_nonlinear','README','NOTATION','finite_dynamics','special_data_limits')],
    FRESH / 'validation_report.json', FRESH / 'verification/gaussian_report.json',
    FRESH / 'data/generated/trained_prediction_sampling/statistical_checks/standalone/report.json',
]
report = {'status': 'PASS for byte/tag/anchor checks only',
          'time_utc': datetime.now(timezone.utc).isoformat(),
          'python': platform.python_version(), 'platform': platform.platform(),
          'cwd': str(Path.cwd()), 'preservation': results,
          'proposal_byte_match_with_exact_assembled_range': True,
          'new_unique_tags': len(tags), 'explicit_new_references': len(new_refs),
          'explicit_older_references_resolved': named_older_refs,
          'new_anchor': anchor, 'latex_control_words': commands,
          'known_required_corrections': {
              '1178': 'Undefined control word \\ler; use \\le r.',
              '1': 'C.4.8 has h3 depth but preceding C.4.7 is h4.',
              '916,1020,1475': 'Inherited local numbering 3,4,6 is discontinuous.',
              '922': 'Reference to Section 2 has no locally numbered Section 2 here.',
              '1481-1501': 'New finite RMS norm abbreviations conflict with unchanged notation contract.',
              '1486-1488': 'Norm bound on full middle update omits factor 2 and residual integral.',
          },
          'hashes': {str(p.relative_to(ROOT)): sha(p) for p in hash_paths}}
(SCRATCH / 'independent_checks.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in ('hashes','latex_control_words')}, indent=2))
print('LATEX CONTROL WORDS:', ', '.join(commands))
