"""Predeclared revision verification: 600 CPU s, 660 wall s, no trajectories.

Check exact insertion/preservation, all unchanged executable bytes, equation
tags and headings, then execute the actual complete documented test setup.
The two advertised discovery setups must be identical, so run it once.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
EDITION = ROOT / "data/generated/observable_hierarchy/H4_candidate_v2"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    output = ROOT / "data/generated/observable_hierarchy/H4_revision_checks_v2"
    output.mkdir(exist_ok=False)
    manifest = json.loads((EDITION / "edition_manifest.json").read_text())
    for row in manifest["files"]:
        assert digest(EDITION / row["destination"]) == row["destination_sha256"]
    old = ROOT / "data/generated/observable_hierarchy/H4_candidate_v1"
    unchanged = []
    for path in (EDITION / "code").rglob("*"):
        if path.suffix not in (".py", ".json"):
            continue
        assert path.read_bytes() == (old / path.relative_to(EDITION)).read_bytes()
        unchanged.append(str(path.relative_to(EDITION)))
    base = (ROOT / "docs/global_nonlinear.md").read_bytes()
    chapter = (EDITION / "docs/global_nonlinear.md").read_bytes()
    section = (STUDY / "H4_proposed_section_v2.md").read_bytes().rstrip()
    insertion = b"\n\n" + section
    assert chapter.count(insertion) == 1 and chapter.replace(insertion, b"", 1) == base
    start = chapter.index(b"##### C.4.7.10.")
    position = chapter.index(section)
    end = chapter.index(b"#### C.4.8.")
    assert start < position < end
    headers = [x for x in section.decode().splitlines() if x.startswith("#")]
    assert len(headers) == 5 and all(x.startswith("###### D.") for x in headers)
    tags = re.findall(r"\\tag\{([^}]+)\}", section.decode())
    assert len(tags) == len(set(tags)) == 79
    assert not any(x.startswith("**3.") and x.count("**") == 1 for x in section.decode().splitlines())
    guide = (EDITION / "code/README.md").read_text()
    recipes = re.findall(r"mkdir -p data/established\nobservable_test_scratch=.*?\n[^\n]*python -B -m unittest discover[^\n]*", guide)
    assert len(recipes) == 2 and recipes[0] == recipes[1]
    recipe = recipes[0] + "\n"
    (output / "executed_recipe.sh").write_text(recipe)
    environment = dict(os.environ)
    for key in ("H4_LAW_TEST_SCRATCH", "H4_VALIDATION_TEST_SCRATCH", "TMPDIR", "PYTHONPATH"):
        environment.pop(key, None)
    for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        environment[key] = "1"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    def cap():
        resource.setrlimit(resource.RLIMIT_CPU, (600, 600))
        resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    wall = time.monotonic()
    with (output / "recipe.log").open("xb") as log:
        completed = subprocess.run(["bash", "-eu", str(output / "executed_recipe.sh")],
                                   cwd=EDITION, env=environment, stdout=log, stderr=subprocess.STDOUT,
                                   timeout=660, preexec_fn=cap)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = {"status": "pass" if completed.returncode == 0 else "fail", "exit_code": completed.returncode,
              "command": ["bash", "-eu", str(output / "executed_recipe.sh")], "cwd": str(EDITION),
              "environment_scratch_initially_unset": True, "recipes_identical": True,
              "unchanged_executable_files": unchanged, "chapter_preservation": True,
              "part_D_start_line": chapter[:position].count(b"\n")+1,
              "part_D_end_before_C_4_8": True, "headers": headers, "tags": len(tags),
              "cpu_seconds": after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
              "wall_seconds": time.monotonic()-wall, "peak_rss_bytes": after.ru_maxrss*1024,
              "script_sha256": digest(Path(__file__)), "recipe_sha256": digest(output / "executed_recipe.sh"),
              "log_sha256": digest(output / "recipe.log"), "edition_manifest_sha256": digest(EDITION / "edition_manifest.json")}
    for row in manifest["files"]:
        assert digest(EDITION / row["destination"]) == row["destination_sha256"]
    (output / "record.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(run())
