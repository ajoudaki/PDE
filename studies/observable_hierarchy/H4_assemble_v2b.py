"""Assemble only the named observable proposal and dependencies, without Git.

This creates a fresh standalone edition, not a checkout/worktree or repository
copy. Source/configuration remain in the study; output never overwrites a run.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parent.parent

MAINTAINED = [
    "code/pde/__init__.py", "code/pde/finite_network.py", "code/pde/gaussian_moments.py",
    "code/pde/observable_closure.py", "code/pde/observable_words.py",
    "code/pde/observable_fixed.py", "code/pde/observable_arithmetic.py",
    "code/pde/observable_compiler.py", "code/pde/observable_initialization.py",
    "code/pde/observable_solver.py", "code/scripts/validate_observable_solver.py",
    "code/scripts/analyze_observable_solver.py", "code/validation/observable_solver_plan.json",
    "code/tests/test_observable_compiler.py", "code/tests/test_observable_initialization.py",
    "code/tests/test_observable_solver.py", "code/tests/test_observable_validation.py",
]
PROPOSED = {
    "H4_laws.py": "code/pde/observable_laws.py",
    "H4_laws_tests_v2.py": "code/tests/test_observable_laws.py",
    "H4_validate.py": "code/scripts/validate_observable_horizon.py",
    "H4_run_validation.py": "code/scripts/run_observable_validation.py",
    "H4_validation_tests_v2.py": "code/tests/test_observable_horizon_validation.py",
    "H4_analyze.py": "code/scripts/analyze_observable_horizon.py",
    "H4_analysis_tests.py": "code/tests/test_observable_horizon_analysis.py",
    "H4_validation_plan.json": "code/validation/observable_horizon_plan.json",
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def assemble(output, *, code_only=False):
    output = Path(output).resolve()
    if output.exists():
        raise FileExistsError("standalone edition must be fresh")
    inputs = [(ROOT / path, path, "unchanged dependency") for path in MAINTAINED]
    inputs += [(STUDY / name, destination, "proposed") for name, destination in PROPOSED.items()]
    if not code_only:
        inputs += [(ROOT / name, name, "unchanged dependency") for name in
                   ("docs/NOTATION.md", "docs/finite_dynamics.md", "docs/special_data_limits.md")]
        inputs += [(STUDY / "H4_proposed_section_v2.md", "docs/global_nonlinear.md", "insert after C.4.7.10"),
                   (STUDY / "H4_code_readme_v2.md", "code/README.md", "complete proposed guide"),
                   (STUDY / "H4_docs_readme.md", "docs/README.md", "complete proposed guide")]
    if any(not source.is_file() for source, _, _ in inputs):
        raise FileNotFoundError("missing complete assembly input: " + str([str(s) for s, _, _ in inputs if not s.is_file()]))
    # Read/hash all inputs before creating an output tree.
    payloads, manifest = {}, []
    for source, destination, kind in inputs:
        content = source.read_bytes()
        if source.name == "H4_laws_tests_v2.py":
            content = content.replace(b"from H4_laws import", b"from pde.observable_laws import")
            transform = "canonical import rename only"
        elif kind == "insert after C.4.7.10":
            chapter = (ROOT / destination).read_bytes()
            marker = b"\n\n#### C.4.8. Sampling fluctuations of the trained prediction\n"
            if chapter.count(marker) != 1:
                raise ValueError("expected one established C.4.7.10 end boundary")
            position = chapter.index(marker)
            start = chapter.index(b"##### C.4.7.10. Finite numerical autonomous observable closure\n")
            if not start < position:
                raise ValueError("invalid established C.4.7.10 boundary order")
            insertion = b"\n\n" + content.rstrip()
            content = chapter[:position] + insertion + chapter[position:]
            assert content.replace(insertion, b"", 1) == chapter
            transform = "insert complete part D at C.4.7.10 end; preserve every existing chapter byte"
        elif kind == "append to current guide":
            content = (ROOT / destination).read_bytes().rstrip() + b"\n\n" + content
            transform = "append complete proposed guide"
        else:
            transform = "identity"
        payloads[destination] = content
        manifest.append(dict(source=str(source.relative_to(ROOT)), source_sha256=digest(source),
                             destination=destination, destination_sha256=hashlib.sha256(content).hexdigest(),
                             kind=kind, transform=transform))
    output.mkdir(parents=True)
    for destination, content in payloads.items():
        target = output / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    record = dict(format="H4-standalone-edition-v2b", code_only=code_only,
                  assembler_sha256=digest(__file__), output=str(output), files=manifest)
    (output / "edition_manifest.json").write_text(json.dumps(record, indent=2) + "\n")
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--code-only", action="store_true")
    args = parser.parse_args()
    record = assemble(args.output, code_only=args.code_only)
    print(json.dumps(dict(output=record["output"], code_only=record["code_only"], files=len(record["files"]))))
