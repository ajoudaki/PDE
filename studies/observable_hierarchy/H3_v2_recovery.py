"""Read-only correspondence audit; writes only to a fresh requested run path."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    study = root / "studies/observable_hierarchy"
    args.output.mkdir(parents=True, exist_ok=False)
    chapter = (root / "docs/global_nonlinear.md").read_text()
    proposal = (study / "H2_proposed_section_v3.md").read_text()
    start = chapter.index("##### C.4.7.9.")
    end = chapter.index("#### C.4.8.", start)
    assert chapter[start:end].strip() == proposal.strip()
    dependencies = []
    for part in (study / "dependencies_v1.md").read_text().split("\nSource: `")[1:]:
        source, rest = part.split("`;", 1)
        scope, body = rest.split("\n\n", 1)
        body = body.rsplit("\n\n---", 1)[0].strip()
        assert body in (root / source).read_text(), scope
        dependencies.append(dict(source=source, scope=scope.strip(), lines=len(body.splitlines()),
                                 sha256=hashlib.sha256(body.encode()).hexdigest()))
    promotion = json.loads((study / "H2_promotion_record_v3.json").read_text())
    unchanged = ["code/pde/observable_closure.py", "code/tests/test_observable_closure.py", "code/README.md"]
    for path in unchanged:
        assert digest(root / path) == promotion["live_validation"]["final_hashes"][path]
    inputs = ["AGENTS.md", "RESEARCH_WORKFLOW.md", "docs/README.md", "docs/NOTATION.md",
              "docs/global_nonlinear.md", "docs/special_data_limits.md", *unchanged]
    inputs += ["studies/observable_hierarchy/" + name for name in
               ["H2_proposed_section_v3.md", "dependencies_v1.md", "H2_prototype_notes_v3.md",
                "H2_promotion_record_v3.json", "H3_assessment.md", "H3_portfolio_comparison.md",
                "H3_residual_feasibility.md", "H3_contract.md"]]
    result = dict(status="PASS", head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
                  theorem="Identical after stripping boundary whitespace", dependency_excerpts=dependencies,
                  unchanged_approved_paths=unchanged, hashes={path: digest(root / path) for path in inputs},
                  limitation="The live roadmap is intentionally revised; whole-chapter hashes may include unrelated later additions. This checks source correspondence, not a new scientific review.")
    (args.output / "recovery.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(dict(status=result["status"], dependency_excerpts=len(dependencies), output=str(args.output))))


if __name__ == "__main__":
    main()
