"""Predeclared final correspondence: 60 CPU s, 4 GiB, no solver runs.

Compare the current frozen candidate with the independently executed runtime,
account explicitly for two test-documentation changes, verify all frozen input
hashes and exact author/reproducer archives, and write an exact promotion map.
This is an author provenance check, not an independent scientific review.
"""
import ast
import hashlib
import json
from pathlib import Path
import resource
import time

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
EDITION = ROOT / "data/generated/observable_hierarchy/H4_candidate_v3"
EXECUTED = ROOT / "data/generated/observable_hierarchy/H4_author_edition_v1"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_semantics(text):
    tree = ast.parse(text)
    assert isinstance(tree.body[0], ast.Expr)
    assert isinstance(tree.body[0].value, ast.Constant)
    assert isinstance(tree.body[0].value.value, str)
    tree.body.pop(0)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "fail":
                # Both files use this only to explain the required scratch path.
                assert len(node.args) == 1 and isinstance(node.args[0], ast.Constant)
                assert "SCRATCH" in node.args[0].value
                node.args = [ast.Constant(value="scratch configuration failure")]
    return ast.dump(tree, include_attributes=False)


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    start = time.process_time()
    output = ROOT / "data/generated/observable_hierarchy/H4_final_correspondence_v3"
    output.mkdir(exist_ok=False)
    packet_path = STUDY / "H4_review_manifest_v3.json"
    packet = json.loads(packet_path.read_text())
    assert digest(packet_path) == "06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02"
    for row in packet["files"]:
        path = ROOT / row["path"]
        assert digest(path) == row["sha256"] and path.stat().st_size == row["bytes"]
    assert len(packet["files"]) == 271
    edition = json.loads((EDITION / "edition_manifest.json").read_text())
    original = json.loads((EXECUTED / "edition_manifest.json").read_text())
    changed_tests = {"code/tests/test_observable_laws.py", "code/tests/test_observable_horizon_validation.py"}
    runtime_correspondence = []
    for row in original["files"]:
        name = row["destination"]
        old, new = EXECUTED / name, EDITION / name
        assert digest(old) == row["destination_sha256"]
        identity = old.read_bytes() == new.read_bytes()
        if name in changed_tests:
            assert test_semantics(old.read_text()) == test_semantics(new.read_text())
            status = "test logic identical; module docstring and scratch failure text changed"
        else:
            assert identity
            status = "byte identical"
        runtime_correspondence.append(dict(path=name, executed_sha256=digest(old),
                                          final_sha256=digest(new), status=status))
    assert len(runtime_correspondence) == 25
    # Verify current destinations against the earlier untouched-base snapshot.
    bases = {row["destination"]: row["current_live_sha256"] for row in
             json.loads((STUDY / "H4_promotion_mapping_v2.json").read_text())["destinations"]}
    destinations = []
    for row in edition["files"]:
        assert digest(EDITION / row["destination"]) == row["destination_sha256"]
        assert digest(ROOT / row["source"]) == row["source_sha256"]
        if row["kind"] == "unchanged dependency":
            assert digest(ROOT / row["destination"]) == row["destination_sha256"]
            continue
        current = ROOT / row["destination"]
        current_hash = digest(current) if current.exists() else None
        assert current_hash == bases[row["destination"]]
        destinations.append(dict(row, current_live_sha256=current_hash,
                                 action="replace" if current.exists() else "add"))
    assert len(destinations) == 11
    mapping = dict(format="H4-proposed-promotion-mapping-v3",
                   status="candidate_pending_complete_reviews_and_user_approval",
                   edition=str(EDITION.relative_to(ROOT)),
                   review_manifest_sha256=digest(packet_path),
                   edition_manifest_sha256=digest(EDITION / "edition_manifest.json"),
                   destinations=destinations)
    mapping_path = STUDY / "H4_promotion_mapping_v3.json"
    with mapping_path.open("x") as handle:
        handle.write(json.dumps(mapping, indent=2) + "\n")
    # Full exact observations and checkpoints: no archive-derived input to solver.
    plan = json.loads((EDITION / "code/validation/observable_horizon_plan.json").read_text())
    author = ROOT / "data/generated/observable_hierarchy/H4_author_runs_v1"
    reproduced = EXECUTED / "data/established/H4_independent_runs_v1"
    comparisons = []
    for configuration in plan["configurations"]:
        name = configuration["id"]
        for filename in [f"observation_{i:02d}.json" for i in range(6)] + ["midpoint_restart.json", "final_restart.json"]:
            old, new = author / name / filename, reproduced / name / filename
            assert old.read_bytes() == new.read_bytes()
            comparisons.append(dict(configuration=name, filename=filename, sha256=digest(new)))
    assert len(comparisons) == 112
    record = dict(status="pass", cpu_seconds=time.process_time()-start,
                  script_sha256=digest(Path(__file__)), packet_files_verified=271,
                  review_manifest_sha256=digest(packet_path),
                  edition_manifest_sha256=digest(EDITION / "edition_manifest.json"),
                  reproduction_report_sha256=digest(STUDY / "H4_reproduction_v1.md"),
                  original_executed_manifest_sha256=digest(EXECUTED / "edition_manifest.json"),
                  runtime_and_test_correspondence=runtime_correspondence,
                  exact_observation_and_checkpoint_comparisons=comparisons,
                  promotion_mapping_sha256=digest(mapping_path),
                  live_bases_and_unchanged_dependencies_match=True,
                  note="Original empirical runtime, plan and analyzer are byte identical to v3. Two test module docstrings and scratch error text changed; test logic is identical. The final complete v3 guides and mathematics are separate frozen review inputs; this author identity check does not assert that the original reproducer read them or replaces a fresh review.")
    (output / "record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: v for k, v in record.items() if k not in ("runtime_and_test_correspondence", "exact_observation_and_checkpoint_comparisons")}))


if __name__ == "__main__":
    main()
