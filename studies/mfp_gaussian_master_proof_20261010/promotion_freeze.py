"""Freeze a neutral complete review packet beside an assembled edition."""
from pathlib import Path
import hashlib
import json
import shutil
import sys

study = Path(__file__).resolve().parent
root = study.parents[1]
run = root/'data/generated'/study.name/sys.argv[1]
edition = run/'edition'
packet = run/'review_packet'
packet.mkdir(exist_ok=False)
baseline = json.loads((run/'baseline_manifest.json').read_text())
mapping = json.loads((study/'promotion_code_mapping.json').read_text())
for name in ['promotion_theory.qmd','promotion_book_patches.json',
             'promotion_code_readme_patches.json','promotion_bibliography.bib',
             'promotion_assemble.py','promotion_code_mapping.json']:
    shutil.copyfile(study/name, packet/name)
if (study/'promotion_quarto_patches.json').exists():
    shutil.copyfile(study/'promotion_quarto_patches.json',packet/'promotion_quarto_patches.json')
for filename, start, end, target in [
    ('docs/02-gaussian-reuse.qmd',1,251,'dependency_chapter2_opening.qmd'),
    ('docs/02-gaussian-reuse.qmd',1035,1187,'dependency_chapter2_finite_jets.qmd'),
    ('docs/02-gaussian-reuse.qmd',3335,3410,'dependency_chapter2_specialization.qmd'),
    ('docs/12-three-sample-learning.qmd',316,684,'dependency_finite_gaussian_law.qmd')]:
    # Excerpts of the maintained baseline, not shifted candidate line numbers.
    source = root/filename
    assert hashlib.sha256(source.read_bytes()).hexdigest() == baseline[filename], filename
    lines = source.read_text().splitlines(True)
    (packet/target).write_text(''.join(lines[start-1:end]))
    (packet/(target+'.origin.json')).write_text(json.dumps({
        'source':filename,'lines':[start,end],
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()},indent=2)+'\n')
required = sorted(set(mapping.values()) | {
    'docs/index.qmd','docs/notation.qmd','docs/_quarto.yml','docs/references.bib',
    'code/README.md','code/pde/__init__.py','code/pde/gaussian_moments.py'})
authors = ['/root','/root/master_moment_proof','/root/calculus_rulebook',
           '/root/calculus_scalar','/root/calculus_oracles','/root/kernel_jet_finite_check',
           '/root/promotion_theory_author','/root/promotion_code_author',
           '/root/promotion_code_author/fixed_seed_semantics',
           '/root/promotion_math_layout','/root/promotion_small_layout']
sources = root/'data/generated'/study.name/'sources'
shutil.copyfile(sources/'non_gaussian_tp_main.txt',packet/'provenance_non_gaussian_tp_main.txt')
appendix = sources/'non_gaussian_tp_appendix.txt'
appendix_lines = appendix.read_text().split('\n')
assert appendix_lines[793].startswith('H      Technical Preliminaries')
assert appendix_lines[1707].startswith('K     Program Transformations')
(packet/'provenance_appendices_H_I_J.txt').write_text('\n'.join(appendix_lines[793:1707])+'\n')
(packet/'provenance_sources.json').write_text(json.dumps({
    'purpose':'Attribution only; the candidate proves its moment lemma internally.',
    'main_url':'https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf',
    'appendix_url':'https://papers.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Supplemental-Conference.zip',
    'appendix_text_lines':[794,1707],
    'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(sources.iterdir()) if p.is_file()}},indent=2)+'\n')
manifest = {'candidate_source_manifest':'../candidate_manifest.json',
            'changed_source_manifest':'../changed_manifest.json',
            'required_edition_reads':required,
            'authors_and_assemblers':authors,
            'selector':'/root/promotion_selector',
            'packet_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(packet.iterdir()) if p.is_file()}}
(packet/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(packet)
