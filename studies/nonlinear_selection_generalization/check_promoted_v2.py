"""Check exact live correspondence to the approved C.4.10 edition.

Run from any directory with one fresh output directory under this study's
generated namespace. This performs no training and does not modify book files.
"""
from hashlib import sha256
import json
from pathlib import Path
import platform
import re
import subprocess
import sys


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]


def digest(data):
    return sha256(data).hexdigest()


def main():
    output = Path(sys.argv[1]).resolve()
    assert output.is_relative_to(
        ROOT / "data/generated/nonlinear_selection_generalization"
    )
    output.mkdir(parents=True, exist_ok=False)
    scientific_bytes = (STUDY / "scientific_manifest_v2.json").read_bytes()
    integration_bytes = (STUDY / "integration_manifest_v2.json").read_bytes()
    assert digest(scientific_bytes) == (
        "cb8b6827db6b24ba2c7c6bf00320cce82c66e687ae4ffe268b02a01bef3336c7"
    )
    assert digest(integration_bytes) == (
        "b5fcdf928d4bcc964f626a176bd129c84662c9a66a900501b1143c7b2fb25b9a"
    )
    scientific = json.loads(scientific_bytes)
    integration = json.loads(integration_bytes)
    for name, entry in scientific["files"].items():
        assert digest((STUDY / name).read_bytes()) == entry["sha256"], name
    for name, expected in scientific["assembly_unit_hashes"].items():
        assert digest((STUDY / name).read_bytes()) == expected, name
    reviews = {
        "scientific_review_v2_c.md":
            "8480318dc6bc5d98e7cbc35abd15d0884bd88b3310736cbc244ff4319d884507",
        "scientific_review_v2_d.md":
            "b26902b104bec3dd5dba1259a3071f24c9eae3142a19ba1119fd3f900040a92e",
        "integration_review_v2.md":
            "21ed7e7cdfb4a3ea3a07a2ddfd6dfde101daf269077a521adf2d75f7979ce715",
    }
    for name, expected in reviews.items():
        assert digest((STUDY / name).read_bytes()) == expected, name
    live_hashes = {}
    for name, expected in integration["edition_files"].items():
        live_hashes[name] = digest((ROOT / name).read_bytes())
        assert live_hashes[name] == expected, name

    chapter = (ROOT / "docs/global_nonlinear.md").read_bytes()
    candidate = (STUDY / "candidate_addition_v2.md").read_bytes()
    assert chapter.endswith(b"\n" + candidate)
    old = chapter[:-len(candidate)-1]
    assert digest(old) == scientific["source_slices"][
        "frozen_global_nonlinear_v2.md"
    ]["full_source_sha256"]
    guide = (ROOT / "docs/README.md").read_bytes()
    assert guide == (STUDY / "candidate_docs_README_v2.md").read_bytes()
    added = candidate.decode()
    assert added.startswith("#### C.4.10. Generalization during a finite added-data episode\n")
    assert "studies/" not in added and "data/generated" not in added
    labels = re.findall(r"\\tag\{([^}]+)\}", added)
    assert len(labels) == len(set(labels))
    assert not set(labels) & set(re.findall(r"\\tag\{([^}]+)\}", old.decode()))
    assert added.count(r"\[") == added.count(r"\]")
    assert added.count(r"\(") == added.count(r"\)")
    fragment = "global_nonlinear.md#c410-generalization-during-a-finite-added-data-episode"
    assert guide.decode().count(fragment) == 2
    heading_line = len(old.splitlines()) + 2
    assert chapter.decode().splitlines()[heading_line-1] == added.splitlines()[0]
    record = {
        "result": "PASS",
        "scope": "Exact live correspondence, unchanged dependencies/reviews, new labels and guide fragments",
        "python": platform.python_version(),
        "head_before_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "checker_sha256": digest(Path(__file__).read_bytes()),
        "scientific_manifest_sha256": digest(scientific_bytes),
        "integration_manifest_sha256": digest(integration_bytes),
        "live_files": live_hashes,
        "preserved_chapter_bytes": len(old),
        "new_section_bytes": len(candidate),
        "new_section_lines": len(candidate.splitlines()),
        "new_heading_line": heading_line,
        "unique_new_equation_labels": len(labels),
        "review_hashes": reviews,
        "limits": "Correspondence check only; frozen scientific and integration reviews supply proof audit. No experiments or whole-book re-audit.",
    }
    (output / "correspondence.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
