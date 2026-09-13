"""Additional bounded static inspection; no candidate imports or executions."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import shlex
import sys
import time


ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
OLD = ROOT / "data/generated/observable_hierarchy/H4_author_edition_v1"
NEW = ROOT / "data/generated/observable_hierarchy/H4_candidate_v3"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(source):
    tree = ast.parse(source)
    messages = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str):
                node.body.pop(0)
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name) and node.func.value.id == "self"
                and node.func.attr == "fail" and len(node.args) == 1
                and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)):
            messages.append(dict(line=node.lineno, value=node.args[0].value))
            node.args[0].value = "<self.fail diagnostic string>"
    return ast.dump(tree, include_attributes=False), messages


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
    cpu, wall = time.process_time(), time.monotonic()
    checks = json.loads((STUDY / "H4_reproduction_addendum_v3_checks.json").read_text())
    changed = []
    for row in checks["comparisons"]:
        assert digest(OLD / row["path"]) == row["original_sha256"]
        assert digest(NEW / row["path"]) == row["final_sha256"]
        if row["byte_identical"]:
            continue
        a, old_messages = normalized((OLD / row["path"]).read_text())
        b, new_messages = normalized((NEW / row["path"]).read_text())
        assert a == b
        assert len(old_messages) == len(new_messages) == 1
        changed.append(dict(path=row["path"], ast_identical_except_docstrings_and_fail_messages=True,
                            original_fail_messages=old_messages, final_fail_messages=new_messages))
    identity_path = STUDY / "H4_review_manifest_v3.json"
    identity = json.loads(identity_path.read_text())
    assert identity["edition"] == str(NEW.relative_to(ROOT))
    allowed = {str(NEW / row["path"]): row["final_sha256"] for row in checks["comparisons"]}
    allowed[str(NEW / "code/README.md")] = checks["final_code_readme_sha256"]
    allowed[str(NEW / "edition_manifest.json")] = checks["final_edition_manifest_sha256"]
    bound = []
    # Identity metadata only: no assignment or scientific file content access.
    for entry in identity["files"]:
        path = Path(entry["path"])
        path = path if path.is_absolute() else ROOT / path
        if str(path) in allowed:
            assert entry["sha256"] == allowed[str(path)] == digest(path)
            assert entry["bytes"] == path.stat().st_size
            bound.append(str(path.relative_to(NEW)))
    guide = (NEW / "code/README.md").read_text().splitlines()
    producer_line = next((i+1, line) for i, line in enumerate(guide)
                         if line.startswith("python -B code/scripts/run_observable_validation.py")
                         and "--worker validate_observable_horizon.py" in line)
    analyzer_line = next((i+1, line) for i, line in enumerate(guide)
                         if line.startswith("python -B code/scripts/analyze_observable_horizon.py"))
    run_root = OLD / "data/established/H4_independent_runs_v1"
    original_producer = json.loads((run_root / "supervisor_command.json").read_text())["command"]
    original_producer = original_producer[original_producer.index("python"):]
    original_analyzer = json.loads((run_root / "analysis_commands.json").read_text())["commands"][0]["command"]
    def normalized_command(command):
        command = list(command)
        command[0] = "python"
        for option in ("--output-dir", "--runs", "--output"):
            if option in command:
                command[command.index(option)+1] = "<fresh run/analysis namespace>"
        return command
    assert normalized_command(shlex.split(producer_line[1])) == normalized_command(original_producer)
    assert normalized_command(shlex.split(analyzer_line[1])) == normalized_command(original_analyzer)
    assert digest(NEW / "edition_manifest.json") == checks["final_edition_manifest_sha256"]
    assert digest(NEW / "code/README.md") == checks["final_code_readme_sha256"]
    assert digest(identity_path) == checks["final_review_manifest_sha256"]
    record = dict(format="H4-independent-reproduction-correspondence-details-v3", command=sys.argv,
                  cwd=str(Path.cwd()), changed_tests=changed,
                  review_identity_bound_files=bound,
                  producer_guide_line=producer_line[0], producer_guide_command=producer_line[1],
                  analyzer_guide_line=analyzer_line[0], analyzer_guide_command=analyzer_line[1],
                  commands_correspond_after_fresh_namespace_substitution=True,
                  original_execution_had_explicit_thread_and_import_environment=True,
                  no_tests_or_trajectories_executed=True, final_inputs_unchanged=True,
                  cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024, status="pass")
    with (STUDY / "H4_reproduction_addendum_v3_details.json").open("x") as output:
        json.dump(record, output, indent=2)
        output.write("\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
