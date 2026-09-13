"""Predeclared static/package checks: 60 CPU s, 90 wall s, no trajectories.

Read only the named candidate, frozen packet and already assigned guides.
Execute the single new non-training public-API example. Preserve all inputs.
"""
import ast
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
EDITION = ROOT / "data/generated/observable_hierarchy/H4_candidate_v1"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    started = time.process_time()
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    output = ROOT / "data/generated/observable_hierarchy/H4_package_checks_v1"
    output.mkdir(exist_ok=False)
    manifest = json.loads((STUDY / "H4_review_manifest_v1.json").read_text())
    checks = []
    for row in manifest["files"]:
        assert digest(ROOT / row["path"]) == row["sha256"], row["path"]
    checks.append({"check": "full frozen packet hashes", "count": len(manifest["files"])})
    edition_manifest = json.loads((EDITION / "edition_manifest.json").read_text())
    for row in edition_manifest["files"]:
        assert digest(EDITION / row["destination"]) == row["destination_sha256"]
        if row["kind"] == "unchanged dependency":
            assert digest(ROOT / row["destination"]) == row["destination_sha256"]
    checks.append({"check": "assembled destinations and unchanged dependencies", "count": len(edition_manifest["files"])})
    code = sorted((EDITION / "code").rglob("*.py"))
    old_edition = ROOT / "data/generated/observable_hierarchy/H4_author_edition_v1"
    for path in code:
        ast.parse(path.read_text())
        assert path.read_bytes() == (old_edition / path.relative_to(EDITION)).read_bytes()
    checks.append({"check": "syntax and exact code correspondence to executed edition", "count": len(code)})
    chapter = (ROOT / "docs/global_nonlinear.md").read_bytes().rstrip() + b"\n\n" + (STUDY / "H4_proposed_section.md").read_bytes()
    assert chapter == (EDITION / "docs/global_nonlinear.md").read_bytes()
    guide = (ROOT / "code/README.md").read_bytes().rstrip() + b"\n\n" + (STUDY / "H4_code_guide.md").read_bytes()
    assert guide == (EDITION / "code/README.md").read_bytes()
    checks.append({"check": "exact chapter and guide append preservation"})
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[key] = "1"
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(EDITION / "code"))
    example = (STUDY / "H4_code_guide.md").read_text().split("```python\n", 1)[1].split("```", 1)[0]
    namespace = {}
    exec(compile(example, "new-guide-law-example", "exec"), namespace)
    checks.append({"check": "new public law example executed without initialization or training", "input_nodes": len(namespace["data"].labels)})
    result = {"checks": checks, "status": "pass", "cpu_seconds": time.process_time()-started,
              "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
              "budget": {"cpu_seconds": 60, "wall_seconds": 90, "trajectories": 0},
              "checker_sha256": digest(Path(__file__)), "python": sys.version,
              "review_manifest_sha256": digest(STUDY / "H4_review_manifest_v1.json")}
    (output / "record.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    run()
