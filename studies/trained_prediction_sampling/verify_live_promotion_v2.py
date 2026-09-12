"""Verify the approved C.4.8 edition after integration; never edit the book."""
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
ROOT = STUDY.parents[1]
BASE = {
    "docs/global_nonlinear.md": "9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226",
    "docs/README.md": "5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a",
}
FINAL = {
    "docs/global_nonlinear.md": "bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05",
    "docs/README.md": "5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f",
}
DEPENDENCIES = {
    "AGENTS.md": "7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba",
    "RESEARCH_WORKFLOW.md": "8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12",
    "docs/NOTATION.md": "199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b",
    "docs/special_data_limits.md": "5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489",
    "docs/finite_dynamics.md": "a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a",
}
FROZEN_STUDY = {
    "proposal_C4_8_v2.md": "98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928",
    "promotion_edits_v2.json": "50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c",
    "review_packet_v2.md": "4eb8fb821a7e87d6819afc1c2fd7e1716e09b7bd2333d83509ca5a02802fb996",
    "integration_packet_v2.md": "b6ede822df001807c55ac017c7986de4f541a8fcb1e1fb1f7292d601fa477a4c",
    "review_v2_A.md": "32371cdd2fa0e8b26c1d1ac3a7e9f23fca7cabbf0277152d6edc66d336e5fa8e",
    "review_v2_B.md": "f6f6f2c492ea25fd27115174f4174abc372e873afbb57a8ba210aea104a93a98",
    "integration_v2.md": "0dad4e3f95c1c1918083886227c5c3306ea43168fe263c6d6901aff910456511",
    "check_gaussian_calculus.py": "118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef",
    "check_sampling_hoeffding.py": "4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def checked_files():
    values = {name: sha((ROOT / name).read_bytes()) for name in DEPENDENCIES}
    assert values == DEPENDENCIES, "A frozen dependency changed"
    study = {name: sha((STUDY / name).read_bytes()) for name in FROZEN_STUDY}
    assert study == FROZEN_STUDY, "A reviewed input changed"
    final = {name: sha((ROOT / name).read_bytes()) for name in FINAL}
    assert final == FINAL, "Live documents differ from the approved edition"
    return {"dependencies": values, "reviewed_study_inputs": study, "live": final}


def run(output):
    namespace = (ROOT / "data/generated/trained_prediction_sampling").resolve()
    output = output.resolve()
    assert namespace in output.parents, "Output must be study-owned generated data"
    output.mkdir(parents=True, exist_ok=False)
    before = checked_files()
    candidate = (STUDY / "proposal_C4_8_v2.md").read_bytes()
    edits = json.loads((STUDY / "promotion_edits_v2.json").read_bytes())
    correspondence = {}
    for name in FINAL:
        live = (ROOT / name).read_bytes()
        restored = live
        for edition in ("standalone_v2", "integration_v2_edition"):
            frozen = namespace / edition / name
            assert live == frozen.read_bytes(), (name, edition)
        if name == edits["append"]["path"]:
            suffix = b"\n\n" + candidate
            assert restored.endswith(suffix)
            assert b"".join(live.splitlines(keepends=True)[11439:12991]) == candidate
            restored = restored[:-len(suffix)]
        replacements = [e for e in edits["replacements"] if e["path"] == name]
        for edit in reversed(replacements):
            old, new = edit["old"].encode(), edit["new"].encode()
            assert restored.count(new) == 1
            restored = restored.replace(new, old, 1)
        assert sha(restored) == BASE[name], "Unapproved old bytes changed"
        correspondence[name] = {
            "final_sha256": sha(live), "restored_original_sha256": sha(restored),
            "exact_reviewed_edition_match": True, "summary_replacements": len(replacements),
        }
    text = candidate.decode()
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    expected = {f"C.4.8.{kind}{i}" for kind, count in (("P", 20), ("S", 43), ("R", 25))
                for i in range(1, count + 1)}
    assert len(tags) == 88 and set(tags) == expected
    refs = set(re.findall(r"\((C\.4\.8\.[PSR]\d+)\)", text))
    assert refs <= expected
    live_chapter = (ROOT / "docs/global_nonlinear.md").read_text()
    assert all(live_chapter.count("\\tag{" + tag + "}") == 1 for tag in tags)
    assert text.splitlines()[0] == "#### C.4.8. Sampling fluctuations of the trained prediction"
    anchor = "global_nonlinear.md#c48-sampling-fluctuations-of-the-trained-prediction"
    assert anchor in (ROOT / "docs/README.md").read_text()
    assert "studies/" not in text and "data/generated/" not in text
    assert text.count(r"\[") == text.count(r"\]")
    assert text.count(r"\(") == text.count(r"\)")
    sources = output / "verification/src"
    sources.mkdir(parents=True)
    for name in ("check_gaussian_calculus.py", "check_sampling_hoeffding.py"):
        (sources / name).write_bytes((STUDY / name).read_bytes())
    sampling = output / "data/generated/trained_prediction_sampling/statistical_checks/live"
    commands = [
        [sys.executable, "-I", str(sources / "check_gaussian_calculus.py"),
         "--output", str(output / "verification/gaussian_report.json")],
        [sys.executable, "-I", str(sources / "check_sampling_hoeffding.py"),
         "--output-dir", str(sampling)],
    ]
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    runs = []
    for command in commands:
        result = subprocess.run(command, cwd=output, env=env, text=True, capture_output=True)
        runs.append({"command": command, "cwd": str(output), "exit_code": result.returncode,
                     "stdout": result.stdout, "stderr": result.stderr})
        assert result.returncode == 0, runs[-1]
    gaussian = output / "verification/gaussian_report.json"
    sampling_report = sampling / "report.json"
    assert json.loads(gaussian.read_text())["status"] == "PASS"
    stats = json.loads(sampling_report.read_text())
    assert stats["status"] == "PASS" and stats["total_checks_passed"] == 748
    assert checked_files() == before
    report = {
        "status": "PASS", "python": platform.python_version(), "inputs": before,
        "correspondence": correspondence,
        "candidate_to_live": {"candidate_lines": [1, 1552], "live_lines": [11440, 12991]},
        "unique_new_tags": len(tags), "explicit_tag_references": len(refs), "navigation": anchor,
        "isolated_checks": runs,
        "result_hashes": {str(p.relative_to(output)): sha(p.read_bytes()) for p in (gaussian, sampling_report)},
        "limitation": "Exact approved addition and affected algebra/integration checks only; not a new whole-book proof, exporter or unrelated-code audit.",
    }
    (output / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "report": str(output / "report.json"),
                      "live_hashes": FINAL, "new_tags": len(tags), "sampling_checks": 748}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    run(parser.parse_args().output)
