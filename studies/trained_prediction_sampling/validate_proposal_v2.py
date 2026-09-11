"""Build and check a standalone proposed edition, never the live book.

Only the two proposed documents, notation, required Gaussian/finite-dynamics
excerpts, and self-contained deterministic check programs are assembled.
No checkout, Git index, worktree, or unrelated study is copied or changed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys

STUDY = Path(__file__).resolve().parent
REPOSITORY = STUDY.parents[1]
FROZEN = {
    "docs/global_nonlinear.md": "9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226",
    "docs/README.md": "5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a",
    "docs/NOTATION.md": "199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b",
    "docs/special_data_limits.md": "5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489",
    "docs/finite_dynamics.md": "a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a",
    "studies/trained_prediction_sampling/proposal_C4_8_v2.md": "98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928",
    "studies/trained_prediction_sampling/promotion_edits_v2.json": "50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c",
    "studies/trained_prediction_sampling/check_gaussian_calculus.py": "118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef",
    "studies/trained_prediction_sampling/check_sampling_hoeffding.py": "4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(output):
    namespace = (REPOSITORY / "data/generated/trained_prediction_sampling").resolve()
    output = output.resolve()
    assert namespace in output.parents, "Output must be study-owned generated data"
    output.mkdir(parents=True, exist_ok=False)
    actual = {path: digest(REPOSITORY / path) for path in FROZEN}
    assert actual == FROZEN, {path: actual[path] for path in actual if actual[path] != FROZEN[path]}
    edits = json.loads((STUDY / "promotion_edits_v2.json").read_text())
    candidate = (STUDY / "proposal_C4_8_v2.md").read_text()
    preserved = {}
    for name in ("docs/global_nonlinear.md", "docs/README.md"):
        original = (REPOSITORY / name).read_text()
        modified = original
        relevant = [edit for edit in edits["replacements"] if edit["path"] == name]
        for edit in relevant:
            assert modified.count(edit["old"]) == 1, (name, edit["old"])
            modified = modified.replace(edit["old"], edit["new"], 1)
        suffix = ""
        if name == edits["append"]["path"]:
            assert "### C.4.8." not in original
            suffix = "\n\n" + candidate
            modified += suffix
        restored = modified[:-len(suffix)] if suffix else modified
        for edit in reversed(relevant):
            assert restored.count(edit["new"]) == 1
            restored = restored.replace(edit["new"], edit["old"], 1)
        assert restored == original, "Unrelated bytes changed"
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(modified)
        preserved[name] = True
    (output / "docs/NOTATION.md").write_bytes((REPOSITORY / "docs/NOTATION.md").read_bytes())
    excerpts = {
        "docs/special_data_limits.md": (3785, 4286),
        "docs/finite_dynamics.md": (1, 227),
    }
    excerpt_manifest = {}
    for name, (first, last) in excerpts.items():
        lines = (REPOSITORY / name).read_text().splitlines(keepends=True)
        text = "".join(lines[first - 1:last])
        (output / name).write_text(text)
        excerpt_manifest[name] = {"source_lines": [first, last], "source_sha256": FROZEN[name],
                                  "excerpt_sha256": digest(output / name)}
    tags = re.findall(r"\\tag\{(C\.4\.8\.[^}]+)\}", candidate)
    refs = set(re.findall(r"\((C\.4\.8\.[PSR]\d+)\)", candidate))
    assert len(tags) == 88 and len(set(tags)) == 88
    assert refs <= set(tags)
    assert candidate.count(r"\[") == candidate.count(r"\]")
    assert candidate.count(r"\(") == candidate.count(r"\)")
    assert "studies/" not in candidate and "data/generated/" not in candidate
    allowed_commands = set("Delta Pi Pr Rightarrow Sigma alpha begin beta bigg bigl bigr cdot cdots chi choose delta dot downarrow ell end epsilon eta exp frac gamma ge hbox hspace in infty int lambda langle ldots le left lim limsup longrightarrow mapsto mathbb mathbf mathcal mathfrak mathscr max mid min mu ne notin nu operatorname otimes overline partial phi pi prod psi qquad quad rangle rho right rm sigma sim sqrt subset sum sup supset tag tanh tau text tfrac theta times to widehat widetilde xi zeta".split())
    commands_used = set(re.findall(r"\\([A-Za-z]+)", candidate))
    assert commands_used <= allowed_commands, sorted(commands_used - allowed_commands)
    assert r"\|v\|_{(n)}" not in candidate
    anchor = "c48-sampling-fluctuations-of-the-trained-prediction"
    assert "#### C.4.8. Sampling fluctuations of the trained prediction" in candidate
    assert "global_nonlinear.md#" + anchor in (output / "docs/README.md").read_text()
    # Independently execute copied checks in isolated Python mode. Their complete
    # inputs are literals plus standard-library code; no study/history is read.
    checks_dir = output / "verification/src"
    checks_dir.mkdir(parents=True)
    for name in ("check_gaussian_calculus.py", "check_sampling_hoeffding.py"):
        (checks_dir / name).write_bytes((STUDY / name).read_bytes())
    sampling_output = output / "data/generated/trained_prediction_sampling/statistical_checks/standalone"
    commands = [
        [sys.executable, "-I", str(checks_dir / "check_gaussian_calculus.py"),
         "--output", str(output / "verification/gaussian_report.json")],
        [sys.executable, "-I", str(checks_dir / "check_sampling_hoeffding.py"),
         "--output-dir", str(sampling_output)],
    ]
    outcomes = []
    clean_environment = dict(os.environ)
    clean_environment.pop("PYTHONPATH", None)
    for command in commands:
        result = subprocess.run(command, cwd=output, env=clean_environment,
                                text=True, capture_output=True, check=False)
        outcomes.append({"command": command, "cwd": str(output), "exit_code": result.returncode,
                         "stdout": result.stdout, "stderr": result.stderr})
        assert result.returncode == 0, outcomes[-1]
    assert json.loads((output / "verification/gaussian_report.json").read_text())["status"] == "PASS"
    sampling_report = json.loads((sampling_output / "report.json").read_text())
    assert sampling_report["total_checks_passed"] == 748 and sampling_report["status"] == "PASS"
    assert {path: digest(REPOSITORY / path) for path in FROZEN} == FROZEN
    report = {
        "status": "PASS", "python": platform.python_version(), "frozen_inputs": FROZEN,
        "generated_document_hashes": {name: digest(output / name) for name in
            ("docs/global_nonlinear.md", "docs/README.md", "docs/NOTATION.md")},
        "dependency_excerpts": excerpt_manifest, "preservation_inverse_check": preserved,
        "new_unique_tags": len(tags), "tex_control_words_checked": sorted(commands_used), "new_tag_references_resolved": len(refs),
        "new_navigation_anchor_resolved": anchor, "isolated_check_runs": outcomes,
        "limitation": "Validates the complete new addition, exact requested edits, necessary frozen dependencies and self-contained checks. It is not a whole-book proof, link, exporter or unrelated-code audit.",
    }
    (output / "validation_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "report": str(output / "validation_report.json"),
                      "documents": report["generated_document_hashes"]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    run(parser.parse_args().output)
