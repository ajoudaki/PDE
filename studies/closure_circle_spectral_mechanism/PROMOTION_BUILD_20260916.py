"""Assemble Package C's exact proposed edition without editing live docs.

Only standard-library text/hash operations; no scientific runtime or data.
The output must be a fresh directory in this study's generated namespace.
"""
import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / "data/generated/closure_circle_spectral_mechanism"
PREFIX = "PROMOTION_"
SUFFIX = "_20260916"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    if not out.is_relative_to(GENERATED.resolve()):
        raise ValueError("output must belong to this study's generated namespace")
    manifest = json.loads((HERE / f"{PREFIX}MANIFEST{SUFFIX}.json").read_text())
    for filename, expected in manifest["frozen_inputs"].items():
        actual = sha((HERE / filename).read_bytes())
        if actual != expected:
            raise ValueError(f"frozen input changed: {filename}")
    base = (HERE / f"{PREFIX}BASE_CHAPTER{SUFFIX}.md").read_text()
    insertion = (HERE / f"{PREFIX}INSERTION{SUFFIX}.md").read_text().strip()
    anchor = manifest["insertion_after"]
    if base.count(anchor) != 1:
        raise ValueError("insertion anchor is not unique")
    if any(f"\\tag{{H3.CS{k}}}" in base for k in range(1, 11)):
        raise ValueError("proposed equation tag already exists")
    final = base.replace(anchor, anchor + "\n\n" + insertion, 1)
    # Reversing this exact insertion must recover every original byte.
    if final.replace(anchor + "\n\n" + insertion, anchor, 1) != base:
        raise AssertionError("unchanged chapter preservation failed")
    out.mkdir(parents=True, exist_ok=False)
    docs = out / "docs"
    docs.mkdir()
    outputs = {
        "docs/global_nonlinear.md": final,
        "docs/README.md": (HERE / f"{PREFIX}DOCS_GUIDE{SUFFIX}.md").read_text(),
        "docs/NOTATION.md": (HERE / f"{PREFIX}NOTATION{SUFFIX}.md").read_text(),
    }
    for rel, value in outputs.items():
        (out / rel).write_text(value)
    start = len(base.split(anchor)[0].splitlines()) + len(anchor.splitlines()) + 2
    report = {
        "frozen_manifest_sha256": sha((HERE / f"{PREFIX}MANIFEST{SUFFIX}.json").read_bytes()),
        "chapter_base_sha256": sha(base.encode()),
        "edition_sha256": {rel: sha(value.encode()) for rel, value in outputs.items()},
        "inserted_lines": len(insertion.splitlines()),
        "first_inserted_line": start,
        "only_change": "one insertion after (H3.N2); original chapter bytes preserved",
        "guide_changes": False,
        "new_code_or_empirical_claims": False,
        "validation": "all frozen hashes, unique anchor, new tags, inverse insertion verified",
        "scope": "target chapter and full guides; no studies/history imports; unchanged guide links to other book chapters are outside this minimal edition",
    }
    (out / "assembly.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
