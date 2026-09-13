"""Bounded post-reproduction correspondence: 60 CPU s/90 wall s, no trajectories.

Preserve all original input/output bytes. Complete the independently executed
code edition with the six reviewed document files, as new paths only; its
original code-only manifest remains unchanged. Compare existing observations.
"""
import hashlib
import json
from pathlib import Path
import resource
import time

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
BASE = ROOT / "data/generated/observable_hierarchy"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    started = time.process_time()
    output = BASE / "H4_reproduction_correspondence_v1"
    output.mkdir(exist_ok=False)
    old, complete = BASE / "H4_author_edition_v1", BASE / "H4_candidate_v1"
    runs = old / "data/established/H4_independent_runs_v1"
    original = json.loads((old / "edition_manifest.json").read_text())
    full = json.loads((complete / "edition_manifest.json").read_text())
    for row in original["files"]:
        assert digest(old / row["destination"]) == row["destination_sha256"]
        assert (old / row["destination"]).read_bytes() == (complete / row["destination"]).read_bytes()
    inventory = json.loads((runs / "reproduction_evidence_manifest.json").read_text())
    for name, row in inventory["generated_files"].items():
        path = old / name
        assert path.stat().st_size == row["bytes"] and digest(path) == row["sha256"], name
    added = []
    for row in full["files"]:
        target = old / row["destination"]
        if target.exists():
            assert digest(target) == row["destination_sha256"]
            continue
        assert row["destination"].startswith("docs/") or row["destination"] == "code/README.md"
        content = (complete / row["destination"]).read_bytes()
        assert hashlib.sha256(content).hexdigest() == row["destination_sha256"]
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(content)
        added.append({"path": row["destination"], "sha256": digest(target)})
    assert len(added) == 6
    comparisons = []
    plan = json.loads((old / "code/validation/observable_horizon_plan.json").read_text())
    for config in plan["configurations"]:
        name = config["id"]
        author = BASE / "H4_author_runs_v1" / name
        independent = runs / name
        a, b = (json.loads((p / "record.json").read_text()) for p in (author, independent))
        assert a["configuration"] == b["configuration"] == config
        files = [x["exact_json"] for x in a["observations"]] + ["midpoint_restart.json", "final_restart.json"]
        row = {"id": name, "exact_files": []}
        for filename in files:
            left, right = author / filename, independent / filename
            assert left.read_bytes() == right.read_bytes(), (name, filename)
            row["exact_files"].append({"name": filename, "sha256": digest(left), "byte_identical": True})
        comparisons.append(row)
    saved_checker = runs / "check_saved_observations.py"
    source_copy = STUDY / "H4_reproduction_checker_v1.py"
    with source_copy.open("xb") as stream:
        stream.write(saved_checker.read_bytes())
    result = {"status": "pass", "cpu_seconds": time.process_time()-started,
              "script_sha256": digest(Path(__file__)), "added_documents": added,
              "original_code_manifest_sha256": digest(old / "edition_manifest.json"),
              "full_edition_manifest_sha256": digest(complete / "edition_manifest.json"),
              "reproduction_report_sha256": digest(STUDY / "H4_reproduction_v1.md"),
              "reproduction_inventory_sha256": digest(runs / "reproduction_evidence_manifest.json"),
              "checker_flat_copy_sha256": digest(source_copy), "comparisons": comparisons,
              "note": "Documentation was added only after the isolated code reproduction report was frozen; no executed input or evidence file changed. This supplies full-document correspondence, not another trajectory run."}
    (output / "record.json").write_text(json.dumps(result, indent=2)+"\n")
    (old / "documentation_assembly_v1.json").write_text(json.dumps({"format": "H4-post-reproduction-documentation-assembly-v1", "added": added, "record": str((output / "record.json").relative_to(ROOT))}, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "exact_comparisons": sum(len(x["exact_files"]) for x in comparisons), "added_documents": len(added), "cpu_seconds": result["cpu_seconds"]}))


if __name__ == "__main__":
    run()
