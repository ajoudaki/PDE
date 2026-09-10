"""Read-only structural audit of the frozen proof-only edition."""
from pathlib import Path
import difflib
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "packet"
EDITION = ROOT / "edition"

def sha(data):
    return hashlib.sha256(data).hexdigest()

manifest = json.loads((ROOT / "manifest.json").read_text())
result = {"input_hashes": {}, "checks": {}}
for group, mapping in ((PACKET, manifest["packet_sha256"]),
                       (EDITION, manifest["edition_sha256"])):
    for rel, expected in mapping.items():
        path = group / rel
        actual = sha(path.read_bytes())
        assert actual == expected, (path, actual, expected)
        result["input_hashes"][str(path.relative_to(ROOT))] = actual
for rel in ("manifest.json", "validation.json"):
    result["input_hashes"][rel] = sha((ROOT / rel).read_bytes())
result["checks"]["all_packet_and_edition_hashes_match_manifest"] = True

actual_files = sorted(str(p.relative_to(EDITION)) for p in EDITION.rglob("*") if p.is_file())
assert actual_files == sorted(manifest["edition_sha256"])
assert not any(p.is_symlink() for p in EDITION.rglob("*"))
result["checks"]["edition_exact_file_inventory_no_symlinks"] = actual_files
changed = sorted(rel for rel, expected in manifest["copied_sources_sha256"].items()
                 if sha((EDITION / rel).read_bytes()) != expected)
assert changed == ["docs/README.md", "docs/global_nonlinear.md"]
result["checks"]["only_changed_source_paths"] = changed

candidate = (PACKET / "candidate.md").read_bytes()
global_bytes = (EDITION / "docs/global_nonlinear.md").read_bytes()
assert global_bytes.endswith(candidate)
before_candidate = global_bytes[:-len(candidate)]
prefix_matches = [i for i in range(5)
                  if sha(before_candidate[:len(before_candidate)-i]) == manifest["copied_sources_sha256"]["docs/global_nonlinear.md"]]
assert len(prefix_matches) == 1, prefix_matches
separator_bytes = prefix_matches[0]
old_global = before_candidate[:len(before_candidate)-separator_bytes]
assert before_candidate[len(old_global):] == b"\n"
result["checks"]["global_assembly"] = {
    "old_prefix_sha256": sha(old_global), "old_prefix_bytes": len(old_global),
    "separator_hex": before_candidate[len(old_global):].hex(),
    "candidate_exact_suffix": True, "candidate_bytes": len(candidate),
    "new_first_line": global_bytes[:len(before_candidate)].count(b"\n") + 1,
    "new_last_line": global_bytes.count(b"\n"),
}

guide_before = (PACKET / "docs_README_before.md").read_bytes()
guide_after = (PACKET / "docs_README_after.md").read_bytes()
assert sha(guide_before) == manifest["copied_sources_sha256"]["docs/README.md"]
assert guide_after == (EDITION / "docs/README.md").read_bytes()
old_lines = guide_before.decode().splitlines(keepends=True)
new_lines = guide_after.decode().splitlines(keepends=True)
assert len(old_lines) == len(new_lines)
guide_changes = [(i + 1, old, new) for i, (old, new) in enumerate(zip(old_lines, new_lines)) if old != new]
assert len(guide_changes) == 1
sentence = " A fixed two-hidden-layer tanh design also admits a controlled cubic test-risk expansion at equal training loss; the coefficient's sign and nonvanishing remain open."
assert guide_changes[0][2] == guide_changes[0][1].replace(" |\n", sentence + " |\n")
result["checks"]["guide_exactly_one_appended_sentence"] = {"line": guide_changes[0][0], "sentence": sentence.strip()}
(ROOT / "integration_scratch/guide.diff").write_text("".join(difflib.unified_diff(old_lines, new_lines, fromfile="packet/docs_README_before.md", tofile="edition/docs/README.md")))
assert (PACKET / "NOTATION.md").read_bytes() == (EDITION / "docs/NOTATION.md").read_bytes()
result["checks"]["notation_packet_equals_edition"] = True

dependencies = (PACKET / "dependencies.md").read_text()
dep_chunks = re.split(r"<!-- Exact source lines (\d+)--(\d+); original section numbering\. -->\n\n", dependencies)
edition_lines = global_bytes.decode().splitlines(keepends=True)
coverage = []
for i in range(1, len(dep_chunks), 3):
    first, last = int(dep_chunks[i]), int(dep_chunks[i + 1])
    frozen = "".join(edition_lines[first-1:last])
    copied = dep_chunks[i+2]
    assert copied.startswith(frozen), (first, last)
    assert not copied[len(frozen):].strip(), (first, last, copied[len(frozen):])
    coverage.append({"first_line": first, "last_line": last, "sha256": sha(frozen.encode()), "exact_copy": True})
result["checks"]["dependency_excerpts_equal_edition"] = coverage

candidate_text = candidate.decode()
tags = re.findall(r"\\tag\{(C4\.\d+)\}", candidate_text)
assert tags == [f"C4.{i}" for i in range(1, 32)]
refs = set(re.findall(r"C4\.\d+", candidate_text))
assert refs == set(tags)
assert global_bytes.count(b"### C.4. A controlled local risk expansion at equal training loss") == 1
for tag in tags:
    assert global_bytes.decode().count("\\tag{" + tag + "}") == 1
result["checks"]["unique_ordered_C4_equation_tags_all_refs_resolve"] = tags
assert not re.search(r"studies/|data/generated/|promotion_v1|review|verdict|\.git", candidate_text, flags=re.I)
result["checks"]["new_material_no_study_or_review_dependency"] = True

command = [sys.executable, "-B", "code/tools/check_library.py"]
check = subprocess.run(command, cwd=EDITION, text=True, capture_output=True, check=False)
assert check.returncode == 0, check.stderr
result["checks"]["independent_boundary_run"] = {"command": command, "cwd": str(EDITION), "returncode": check.returncode, "stdout": check.stdout, "stderr": check.stderr}
output = ROOT / "integration_scratch/check_results.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result["checks"], indent=2))
