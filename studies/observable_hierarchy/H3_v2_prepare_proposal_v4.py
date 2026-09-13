"""Prepare exact proposed live-file bytes without applying them."""
import difflib
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
study = root/'studies/observable_hierarchy'
edition = root/'data/generated/observable_hierarchy/H3_v2_edition_v3'
sha = lambda data: hashlib.sha256(data).hexdigest()
prior = json.loads((study/'H3_v2_promotion_mapping_v3.json').read_text())
manifest = json.loads((edition/'review/manifest.json').read_text())
files, patch = {}, []
for relative, previous in prior['files'].items():
    live, proposed = root/relative, edition/relative
    old = live.read_bytes() if live.exists() else b''
    base = sha(old) if live.exists() else None
    assert base == previous['base_sha256'], relative
    new = proposed.read_bytes()
    assert sha(new) == manifest['edition_hashes'][relative]
    files[relative] = dict(action=previous['action'], base_sha256=base,
                           proposed_sha256=sha(new),
                           candidate_path=str(proposed.relative_to(root)))
    patch.extend(difflib.unified_diff(old.decode().splitlines(keepends=True),
        new.decode().splitlines(keepends=True),
        fromfile='a/'+relative if live.exists() else '/dev/null',
        tofile='b/'+relative))
patch_bytes = ''.join(patch).encode()
patch_path = study/'H3_v2_proposed_changes_v4.patch'
mapping_path = study/'H3_v2_promotion_mapping_v4.json'
assert not patch_path.exists() and not mapping_path.exists()
patch_path.write_bytes(patch_bytes)
mapping = dict(status='scientific reviews pass; final integration and approval pending',
    edition_manifest_sha256=sha((edition/'review/manifest.json').read_bytes()),
    files=files, patch_sha256=sha(patch_bytes))
mapping_path.write_text(json.dumps(mapping, indent=2)+'\n')
proposal = (study/'H3_v2_promotion_proposal_v3.md').read_text()
proposal = proposal.replace('H3_v2_edition_v2_section.md', 'H3_v2_edition_v3_section.md')
proposal = proposal.replace('H3_v2_proposed_changes_v3.patch', 'H3_v2_proposed_changes_v4.patch')
proposal = proposal.replace('H3_v2_promotion_mapping_v3.json', 'H3_v2_promotion_mapping_v4.json')
proposal = proposal.replace('Status: complete candidate and independent reproduction; final scientific and\nintegration outcomes are still pending. This draft is not promotion approval.',
    'Status: complete candidate, independent reproduction and two complete scientific\nreviews pass; final integration review is pending. This is not promotion approval.')
proposal = proposal.replace('Relevance selection accepts the addition beside H2. Two complete fresh\nscientific reviews and a separate complete fresh integration review of packet\nv3 are pending.',
    'Relevance selection accepts the addition beside H2. Both complete fresh\nscientific reviews of packet v3 pass without required corrections. A required\nintegration presentation correction displays one existing bound properly;\nall mathematics, code and execution inputs are preserved. A fresh complete\nintegration review of the corrected edition v3, packet v4, is pending.')
out = study/'H3_v2_promotion_proposal_v4.md'
assert not out.exists()
out.write_text(proposal)
print(json.dumps(dict(paths=len(files), patch_sha256=sha(patch_bytes),
                     edition_manifest_sha256=mapping['edition_manifest_sha256']), indent=2))
