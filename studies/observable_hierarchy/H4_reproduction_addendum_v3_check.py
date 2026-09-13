"""Bounded read/hash/static correspondence; imports no candidate modules."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import resource
import sys
import time


ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
OLD = ROOT / "data/generated/observable_hierarchy/H4_author_edition_v1"
NEW = ROOT / "data/generated/observable_hierarchy/H4_candidate_v3"
PREFIX = "H4_reproduction_addendum_v3_"


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def without_docstrings(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str):
                node.body.pop(0)
    return ast.dump(tree, include_attributes=False)


def run():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    cpu, wall = time.process_time(), time.monotonic()
    old_manifest = json.loads((OLD / "edition_manifest.json").read_text())
    new_manifest = json.loads((NEW / "edition_manifest.json").read_text())
    new_entries = {x["destination"]: x for x in new_manifest["files"]}
    original_report = STUDY / "H4_reproduction_v1.md"
    original_report_hash = "547c2b6658428a9a738670d900912c9b3e2aeaaf4e51085041e322998fad7ab4"
    assert digest(original_report) == original_report_hash
    run_root = OLD / "data/established/H4_independent_runs_v1"
    evidence_path = run_root / "reproduction_evidence_manifest.json"
    assert digest(evidence_path) == "c471d9899f413ff38a5e6594b807ad41a2368bf62b8846789ecdca7c9bb7c9eb"
    evidence = json.loads(evidence_path.read_text())
    assert digest(OLD / "edition_manifest.json") == evidence["edition_manifest_sha256"]
    original_outputs_verified = []
    for relative, expected in evidence["generated_files"].items():
        path = OLD / relative
        assert digest(path) == expected["sha256"] and path.stat().st_size == expected["bytes"]
        original_outputs_verified.append(relative)
    comparisons, diffs = [], []
    assert len(old_manifest["files"]) == 25
    for original in old_manifest["files"]:
        relative = original["destination"]
        old_path, new_path = OLD / relative, NEW / relative
        before, after = old_path.read_bytes(), new_path.read_bytes()
        old_hash, new_hash = digest(old_path), digest(new_path)
        assert old_hash == original["destination_sha256"] == evidence["input_hashes"][relative]
        assert new_hash == new_entries[relative]["destination_sha256"]
        row = dict(path=relative, original_sha256=old_hash, final_sha256=new_hash,
                   original_lines=len(before.splitlines()), final_lines=len(after.splitlines()),
                   byte_identical=before == after)
        if before != after:
            diff = "".join(difflib.unified_diff(before.decode().splitlines(True), after.decode().splitlines(True),
                fromfile="original/" + relative, tofile="final-v3/" + relative))
            diffs.append(diff)
            if relative.endswith(".py"):
                row["executable_ast_identical_after_removing_docstrings"] = (
                    without_docstrings(ast.parse(before)) == without_docstrings(ast.parse(after)))
        comparisons.append(row)
    guide = NEW / "code/README.md"
    text = guide.read_text()
    assert digest(guide) == new_entries["code/README.md"]["destination_sha256"]
    guide_lines = text.splitlines()
    setups = []
    for i, line in enumerate(guide_lines):
        if "-m unittest discover" in line:
            assert i >= 2
            assert guide_lines[i-2] == "mkdir -p data/established"
            assert guide_lines[i-1] == 'observable_test_scratch=$(mktemp -d "$PWD/data/established/observable_tests.XXXXXX")'
            required = ["PYTHONPATH=code", "PYTHONDONTWRITEBYTECODE=1", "OPENBLAS_NUM_THREADS=1",
                        "OMP_NUM_THREADS=1", "MKL_NUM_THREADS=1",
                        'H4_LAW_TEST_SCRATCH="$observable_test_scratch"',
                        'H4_VALIDATION_TEST_SCRATCH="$observable_test_scratch"',
                        'TMPDIR="$observable_test_scratch"', "python -B -m unittest discover -s code/tests"]
            assert all(part in line for part in required)
            setups.append(dict(start_line=i-1, command_line=i+1, lines=guide_lines[i-2:i+1],
                               required_settings_present=True))
    assert len(setups) == 3
    plan_path = NEW / "code/validation/observable_horizon_plan.json"
    plan = json.loads(plan_path.read_text())
    supervisor = json.loads((run_root / "supervisor.json").read_text())
    analysis_path = OLD / "data/established/H4_independent_analysis_v1/summary.json"
    analysis = json.loads(analysis_path.read_text())
    assert supervisor["plan_sha256"] == analysis["plan_sha256"] == digest(plan_path)
    assert supervisor["supervisor_sha256"] == digest(NEW / "code/scripts/run_observable_validation.py")
    assert supervisor["worker_sha256"] == digest(NEW / "code/scripts/validate_observable_horizon.py")
    assert analysis["postprocessor_sha256"] == digest(NEW / "code/scripts/analyze_observable_horizon.py")
    assert [x["id"] for x in supervisor["configurations"]] == [x["id"] for x in plan["configurations"]]
    worker_correspondence = []
    for config in plan["configurations"]:
        record = json.loads((run_root / config["id"] / "record.json").read_text())
        assert record["configuration"] == config
        assert record["plan_sha256"] == digest(plan_path)
        assert record["producer_sha256"] == digest(NEW / "code/scripts/validate_observable_horizon.py")
        assert all(source_hash == digest(NEW / "code/pde" / filename)
                   for filename, source_hash in record["source_hashes"].items())
        worker_correspondence.append(dict(id=config["id"], status=record["status"],
                                          all_recorded_runtime_hashes_match_final=True))
    identity_path = STUDY / "H4_review_manifest_v3.json"
    identity = json.loads(identity_path.read_text())
    # Restrict disclosure and examination of this manifest to identity metadata.
    identity_fields = {key: identity[key] for key in
                       ("format", "version", "candidate_version", "edition", "edition_path", "edition_manifest_sha256")
                       if key in identity}
    record = dict(format="H4-independent-reproduction-correspondence-check-v3",
        command=sys.argv, cwd=str(Path.cwd()), python=sys.version,
        original_report_sha256=original_report_hash,
        original_edition_manifest_sha256=digest(OLD / "edition_manifest.json"),
        original_evidence_manifest_sha256=digest(evidence_path),
        original_generated_files_verified=len(original_outputs_verified),
        final_edition_manifest_sha256=digest(NEW / "edition_manifest.json"),
        final_code_readme_sha256=digest(guide), final_code_readme_lines=len(guide_lines),
        final_review_manifest_sha256=digest(identity_path), final_review_identity=identity_fields,
        final_review_manifest_top_level_keys=list(identity),
        comparisons=comparisons, discovery_setups=setups,
        worker_correspondence=worker_correspondence,
        original_guide_absent=not (OLD / "code/README.md").exists(),
        original_instruction_hashes=evidence["instruction_hashes"],
        current_instruction_hashes={key:digest(Path(key)) for key in evidence["instruction_hashes"]},
        budget=dict(cpu_seconds=60, address_space_bytes=4*1024**3),
        no_tests_or_trajectories_executed=True, status="pass")
    record.update(cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
    with (STUDY / (PREFIX + "differences.diff")).open("x") as output:
        output.write("\n".join(diffs))
    with (STUDY / (PREFIX + "checks.json")).open("x") as output:
        json.dump(record, output, indent=2)
        output.write("\n")
    print(json.dumps({key:record[key] for key in ("status", "cpu_seconds", "wall_seconds", "peak_rss_bytes", "original_generated_files_verified", "final_review_identity", "final_review_manifest_top_level_keys")}))
    print(json.dumps([row for row in comparisons if not row["byte_identical"]]))
    print("\n".join(diffs))


if __name__ == "__main__":
    run()
