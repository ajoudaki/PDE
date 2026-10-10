"""Verify the reviewed package and current checkout before requesting approval.

Run only after the coordinator has read the complete integration report and
confirmed its verdict. This mechanical check cannot replace that reading.
"""
from pathlib import Path
import argparse
import datetime
import json
import re
from promotion_assemble import digest, inventory

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--integration-sha256', required=True)
parser.add_argument('--run', default='promotion_candidate_v6')
parser.add_argument('--integration-report', default='promotion_integration_review_v6.md')
args = parser.parse_args()
study = Path(__file__).resolve().parent
root = study.parents[1]
generated = root / 'data/generated' / study.name
run, prior = generated / args.run, generated / 'promotion_candidate_v3'
code_run = generated / 'promotion_candidate_v4'
baseline = json.loads((run / 'baseline_manifest.json').read_text())
assert inventory() == baseline, 'Concurrent maintained-source changes; inspect before approval'
candidate = json.loads((run / 'candidate_manifest.json').read_text())
changed = json.loads((run / 'changed_manifest.json').read_text())
assert len(changed) == 15
for name, value in candidate.items():
    assert digest(run / 'edition' / name) == value, name
packet = json.loads((run / 'review_packet/manifest.json').read_text())
patches = (json.loads((study / 'promotion_math_layout_patches_v1.json').read_text())
           + json.loads((study / 'promotion_small_layout_patches_v1.json').read_text()))
def nonlayout_tokens(text):
    text = text.replace('\\left.', '').replace('\\right.', '').replace('{}', '')
    text = re.sub(r'\\(?:begin|end)\{(?:aligned|gathered)\}', '', text)
    text = re.sub(r'\\(?:left|right|bigl|bigr|quad|qquad)\b', '', text)
    return re.sub(r'\s+', '', text.replace('\\,', '').replace('\\\\', '').replace('&', ''))
assert len(patches) == 13
for patch in patches:
    assert nonlayout_tokens(patch['old']) == nonlayout_tokens(patch['new'])
def restore_layout(text):
    for patch in reversed(patches):
        assert text.count(patch['new']) == 1
        text = text.replace(patch['new'], patch['old'], 1)
    return text
for name, value in packet['packet_sha256'].items():
    assert digest(run / 'review_packet' / name) == value, name
    if name == 'promotion_theory.qmd':
        assert restore_layout((run / 'review_packet' / name).read_text()) == (
            prior / 'review_packet' / name).read_text()
    else:
        assert digest(prior / 'review_packet' / name) == value, name
for name in packet['required_edition_reads']:
    assert digest(run / 'edition' / name) == digest(prior / 'edition' / name), name
assert restore_layout((run / 'edition/docs/02-gaussian-reuse.qmd').read_text()) == (
    prior / 'edition/docs/02-gaussian-reuse.qmd').read_text()
for name in changed:
    if name != 'docs/02-gaussian-reuse.qmd':
        assert digest(run / 'edition' / name) == digest(prior / 'edition' / name)
for name, value in candidate.items():
    if name.startswith('code/') or name == 'requirements.txt':
        assert digest(code_run / 'edition' / name) == value, name
scientific = json.loads((prior / 'scientific_gate_check.json').read_text())
assert scientific['result'] == 'PASS'
for review in scientific['checks']:
    assert digest(root / review['full_report']) == review['full_report_sha256']
    assert review['root_complete_read'] and review['reported_manifests_match']
integration = study / args.integration_report
assert digest(integration) == args.integration_sha256
validation = json.loads((code_run / 'code_validation/manifest.json').read_text())
assert all(command['exit_code'] == 0 for command in validation['commands'])
assert 'Ran 72 tests' in (code_run / 'code_validation/tests.log').read_text()
links = json.loads((run / 'html_links.json').read_text())
assert not links['errors']
layout = json.loads((run / 'math_layout_check/result.json').read_text())
assert layout['new_section_all_displays_typeset_and_fonts_loaded']
assert {row['viewport_width'] for row in layout['viewports']} == {1280, 1500}
assert all(row['display_count'] == 44 and not row['overflows'] and not row['math_errors']
           for row in layout['viewports'])
structure = json.loads((run / 'structural_validation.json').read_text())
assert structure['frozen_sources_unchanged'] == len(candidate)
for name, value in structure['pdf_and_latex'].items():
    assert digest(run / name) == value
for format in ('html', 'pdf', 'latex'):
    render = json.loads((run / f'render_logs/{format}.json').read_text())
    assert render['exit_code'] == 0
    for name, value in render['outputs'].items():
        assert digest(run / f'rendered_{format}' / name) == value, name
preview = json.loads((run / 'preview_manifest.json').read_text())
assert digest(root / preview['source']) == preview['source_sha256']
assert digest(root / preview['preview']) == preview['preview_sha256']
patch = json.loads((run / 'patch_manifest.json').read_text())
assert digest(root / patch['path']) == patch['sha256']
assert patch['dry_run']['exit_code'] == 0
report = {
    'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'current_maintained_sources_identical_to_baseline': len(baseline),
    'frozen_candidate_sources_verified': len(candidate),
    'identical_scientific_packet_inputs': len(packet['packet_sha256']) - 1,
    'theory_identical_after_reversing_13_reviewed_layout_patches': True,
    'identical_scientific_edition_reads': len(packet['required_edition_reads']),
    'identical_proposed_changes': len(changed) - 1,
    'chapter_identical_after_reversing_13_reviewed_layout_patches': True,
    'scientific_reports': scientific['checks'],
    'integration_report': str(integration.relative_to(root)),
    'integration_report_sha256': args.integration_sha256,
    'coordinator_complete_integration_read_confirmed_by_invocation': True,
    'source_manifest_sha256': digest(run / 'candidate_manifest.json'),
    'changed_manifest_sha256': digest(run / 'changed_manifest.json'),
    'all_three_render_archives_verified': True,
    'all_44_new_displays_fit_at_1280_and_1500': True,
    'standalone_code_commands': len(validation['commands']),
    'code_validation_evidence': str((code_run / 'code_validation').relative_to(root)),
    'all_code_and_requirements_identical_to_validation_run': True,
    'tests': 72, 'local_links_checked': links['checked_local_links'],
    'status': 'Technical checks complete; concrete-package user approval pending',
    'live_maintained_mutation_by_this_task': False}
(run / 'preapproval_check.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
