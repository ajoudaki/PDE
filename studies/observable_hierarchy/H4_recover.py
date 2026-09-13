"""Read-only H3 correspondence and H4 foundation provenance; no trajectories."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    if not out.is_relative_to(ROOT / "data/generated/observable_hierarchy"):
        raise ValueError("output must belong to this study")
    out.mkdir(parents=True, exist_ok=False)
    mapping_path = STUDY / "H3_v2_promotion_mapping_v4.json"
    mapping = json.loads(mapping_path.read_text())
    manifest = json.loads((STUDY / "H3_v2_edition_v3_manifest.json").read_text())
    installed = {}
    for name, item in mapping["files"].items():
        actual = digest(ROOT / name)
        installed[name] = {"actual": actual, "reviewed": item["proposed_sha256"],
                           "matches": actual == item["proposed_sha256"]}
    dependencies = {}
    for name, expected in manifest["edition_hashes"].items():
        if name.startswith(("code/", "docs/")):
            actual = digest(ROOT / name)
            dependencies[name] = {"actual": actual, "reviewed": expected,
                                  "matches": actual == expected}
    section = (STUDY / "H3_v2_edition_v3_section.md").read_text()
    section_matches = (ROOT / "docs/global_nonlinear.md").read_text().count(section) == 1
    result = {"head": subprocess.check_output(["git", "rev-parse", "HEAD"],
                cwd=ROOT, text=True).strip(), "installed": installed,
        "dependencies": dependencies, "exact_h3_section_once": section_matches,
        "mapping_sha256": digest(mapping_path),
        "proposal_sha256": digest(STUDY / "H3_v2_promotion_proposal_v4.md"),
        "instructions": {name: digest(ROOT / name) for name in
            ("AGENTS.md", "RESEARCH_WORKFLOW.md")},
        "checker_sha256": digest(Path(__file__)),
        "scope": "Byte correspondence only; no scientific review or trajectory run."}
    result["pass"] = section_matches and all(v["matches"] for v in
        list(installed.values()) + list(dependencies.values()))
    (out / "correspondence.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"pass": result["pass"], "installed": len(installed),
                      "dependency_destinations": len(dependencies)}))
    if not result["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
