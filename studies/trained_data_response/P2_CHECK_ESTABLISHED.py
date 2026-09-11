#!/usr/bin/env python3
"""Verify the approved P2 live edition and rerun frozen supplied-state checks.

Administrative byte correspondence and deterministic algebra only: this is not
a mathematical review, training run, or authorization to change established files.
All writes go to the required fresh study-generated output directory.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import traceback


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parent.parent
GENERATED = ROOT / "data/generated/trained_data_response"
MANIFEST_SHA = "7ad4d1a5479153bc568c67706c1497ed28d5c64acace30ac0f43ef5f8334a73e"
P1_MANIFEST_SHA = "f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d"
APPROVED = {
    "docs/global_nonlinear.md": "9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226",
    "docs/README.md": "5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a",
}
SCRIPTS = ["P2_PROMOTION_TANGENT_CHECK.py", "P2_PROMOTION_REFERENCE_CHECK.py",
           "P2_PROMOTION_RADIAL_CHECK.py"]
CONTROLS = dict(PYTHONPATH="", PYTHONDONTWRITEBYTECODE="1",
                OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", OMP_THREAD_LIMIT="1",
                MKL_NUM_THREADS="1", BLIS_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1",
                VECLIB_MAXIMUM_THREADS="1")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def json_write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def checked(path, expected, report):
    require(path.is_file() and not path.is_symlink(), f"Missing/symlinked input: {path}")
    data = path.read_bytes()
    actual = sha(data)
    report["input_hashes"][path.relative_to(ROOT).as_posix()] = actual
    require(actual == expected, f"Hash mismatch: {path}; expected {expected}, found {actual}")
    return data


def flat_input(name):
    require(isinstance(name, str) and Path(name).name == name and name not in {".", ".."},
            f"Nonflat study input: {name}")
    return STUDY / name


def verify(output, report):
    manifest_path = STUDY / "P2_PROMOTION_MANIFEST.json"
    manifest = json.loads(checked(manifest_path, MANIFEST_SHA, report))
    require(len(manifest["inputs"]) == 10, "Expected exactly ten frozen P2 inputs")
    inputs = {name: checked(flat_input(name), expected, report)
              for name, expected in manifest["inputs"].items()}
    ancillary = json.loads(inputs["P2_EDITION_ANCILLARY.json"])
    frozen = manifest["established_sha256"]
    require(len(frozen) == 10 and frozen == ancillary["copied_docs_sha256"],
            "Frozen document inventories disagree")
    require(manifest["instruction_sha256"] == ancillary["instruction_sha256"]
            and set(manifest["instruction_sha256"]) == {"AGENTS.md", "RESEARCH_WORKFLOW.md"},
            "Frozen instruction inventories disagree")
    for name, expected in manifest["instruction_sha256"].items():
        checked(ROOT / name, expected, report)
    for name, expected in ancillary["scientific_base_sha256"].items():
        require(frozen.get(name) == expected, f"Scientific base hash disagreement: {name}")
    actual_names = {p.relative_to(ROOT).as_posix() for p in (ROOT / "docs").rglob("*.md")}
    require(actual_names == set(frozen), "Live docs inventory changed")
    live = {}
    for name, base_sha in frozen.items():
        require(name.startswith("docs/") and name.endswith(".md")
                and ".." not in Path(name).parts, f"Unexpected docs path: {name}")
        live[name] = checked(ROOT / name, APPROVED.get(name, base_sha), report)
    require(live["docs/README.md"] == inputs["P2_PROPOSED_GUIDE.md"],
            "Live guide differs from frozen proposed guide")
    report["live_docs_sha256"] = {name: sha(data) for name, data in live.items()}

    spec = ancillary["section"]
    chapter = "docs/global_nonlinear.md"
    require(spec["source"] == "P2_SECTION.md" and spec["destination"] == chapter
            and spec["append_separator"] == "\n", "Unexpected append specification")
    append = b"\n" + inputs["P2_SECTION.md"]
    require(live[chapter].endswith(append), "Exact newline-plus-section suffix missing")
    restored = dict(live)
    restored[chapter] = restored[chapter][:-len(append)]
    changes = ancillary["replacements"]
    require(len(changes) == 7 and len({c["id"] for c in changes}) == 7,
            "Expected seven distinct ancillary replacements")
    report["reversed_replacements"] = []
    for change in reversed(changes):
        name, old, new = change["path"], change["old"].encode(), change["new"].encode()
        require(name in APPROVED and old and new and old != new, "Unexpected replacement")
        require(restored[name].count(new) == 1, f"Ambiguous reverse replacement: {change['id']}")
        restored[name] = restored[name].replace(new, old, 1)
        require(restored[name].count(old) == 1, f"Ambiguous restored text: {change['id']}")
        report["reversed_replacements"].append(dict(id=change["id"], path=name,
                                                    old_sha256=sha(old), new_sha256=sha(new)))
    report["restored_base_sha256"] = {name: sha(data) for name, data in restored.items()}
    require(report["restored_base_sha256"] == frozen, "Exact reversal failed to restore frozen base")

    pattern = (r"<!-- BEGIN ([^:]+):(\d+)-(\d+); SHA256 ([0-9a-f]+) -->\n"
               r"(.*?)\n<!-- END CANONICAL DEPENDENCY -->")
    report["dependency_excerpts"] = []
    for match in re.finditer(pattern, inputs["P2_PROMOTION_DEPENDENCIES.md"].decode(), re.S):
        name, first, last, expected, body = match.groups()
        require(name in restored and sha(restored[name]) == expected, f"Dependency base mismatch: {name}")
        lines = restored[name].decode().splitlines(keepends=True)
        require(1 <= int(first) <= int(last) <= len(lines), f"Invalid dependency interval: {name}")
        require(body == "".join(lines[int(first)-1:int(last)]), f"Dependency excerpt mismatch: {name}")
        report["dependency_excerpts"].append(dict(path=name, first=int(first), last=int(last),
                                                  base_sha256=expected, excerpt_sha256=sha(body.encode())))
    require(len(report["dependency_excerpts"]) == 7, "Expected all seven dependency excerpts")

    p1 = json.loads(checked(STUDY / "P1_MANIFEST.json", P1_MANIFEST_SHA, report))
    p1_hashes = {}
    p1_section = None
    for name, metadata in p1["inputs"].items():
        data = checked(flat_input(name), metadata["sha256"], report)
        p1_hashes[name] = sha(data)
        if name == "P1_SECTION.md":
            p1_section = data
    require(p1_section and restored[chapter].count(p1_section) == 1
            and restored[chapter].endswith(p1_section), "Frozen P1 section not exactly preserved in restored base")
    report["p1_preservation"] = dict(manifest_sha256=P1_MANIFEST_SHA, input_sha256=p1_hashes,
                                      exact_section_count=1, section_is_restored_chapter_suffix=True)

    # Import only the frozen builder's pure structural helpers; never call build().
    sys.dont_write_bytecode = True
    module_spec = importlib.util.spec_from_file_location("p2_frozen_edition_builder", STUDY / "P2_EDITION_BUILD.py")
    builder = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(builder)
    texts = {name: data.decode() for name, data in live.items()}
    base_texts = {name: data.decode() for name, data in restored.items()}
    section = inputs["P2_SECTION.md"].decode()
    report["section_checks"] = builder.validate_section(section, base_texts[chapter], spec)
    require(texts[chapter].count(spec["title"]) == 1, "Live section title is not unique")
    exclusions = {(item["source"], item["target"])
                  for item in ancillary["allowed_preexisting_external_doc_links"]}
    require(exclusions == {("docs/README.md", "../code/README.md")}, "Unexpected excluded link")
    baseline_links = {(name, target) for name, text in base_texts.items()
                      for target in builder.markdown_links(text)}
    require(exclusions <= baseline_links, "Excluded link was not present in frozen base")
    require((ROOT / "code/README.md").is_file(), "Existing implementation-guide target is missing")
    report["excluded_live_target"] = dict(source="docs/README.md", target="../code/README.md",
                                           actual_target="code/README.md", exists=True,
                                           copied_to_standalone=False, contents_read=False)
    affected = [(change["path"], target) for change in changes
                for target in builder.markdown_links(change["new"])]
    affected += [(chapter, target) for target in builder.markdown_links(section)]
    report["affected_links_and_fragments"] = [builder.link_check(name, target, texts, set())
                                              for name, target in affected]
    report["readme_links_and_fragments"] = [builder.link_check("docs/README.md", target, texts, exclusions)
                                            for target in builder.markdown_links(texts["docs/README.md"])]

    standalone = output / "standalone"
    for name, data in live.items():
        destination = standalone / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    checks = standalone / "validation"
    checks.mkdir()
    for name in SCRIPTS:
        (checks / name).write_bytes(inputs[name])
    initial_files = {p.relative_to(standalone).as_posix() for p in standalone.rglob("*") if p.is_file()}
    require(initial_files == set(live) | {"validation/" + name for name in SCRIPTS},
            "Standalone input inventory must be exactly ten docs and three frozen scripts")
    report["standalone_input_sha256"] = {name: sha((standalone / name).read_bytes())
                                          for name in sorted(initial_files)}
    env = dict(os.environ, **CONTROLS)
    data = standalone / "data/generated/trained_data_response/checks"
    commands = [
        ("tangent", [sys.executable, "-B", SCRIPTS[0], "--output", str(data / "tangent")]),
        ("reference", [sys.executable, "-B", SCRIPTS[1]]),
        ("radial", [sys.executable, "-B", SCRIPTS[2], "--output", str(data / "radial")]),
    ]
    for label, command in commands:
        record = dict(label=label, command=command, cwd=str(checks), environment=CONTROLS,
                      started_utc=datetime.now(timezone.utc).isoformat())
        report["commands"].append(record)
        json_write(output / "validation.json", report)
        try:
            run = subprocess.run(command, cwd=checks, env=env, capture_output=True, timeout=180)
            stdout, stderr = run.stdout, run.stderr
            record["exit"] = run.returncode
        except subprocess.TimeoutExpired as error:
            stdout, stderr = error.stdout or b"", error.stderr or b""
            record.update(exit=None, failure="Timed out after 180 seconds")
        (output / (label + ".stdout.log")).write_bytes(stdout)
        (output / (label + ".stderr.log")).write_bytes(stderr)
        record.update(stdout_sha256=sha(stdout), stderr_sha256=sha(stderr),
                      finished_utc=datetime.now(timezone.utc).isoformat())
        if record["exit"] != 0:
            report["failures"].append(dict(label=label, exit=record["exit"], failure=record.get("failure")))
        json_write(output / "validation.json", report)

    require(not any(p.name in {"studies", ".git", "__pycache__"}
                    or p.is_symlink() or p.suffix == ".pyc" for p in standalone.rglob("*")),
            "Standalone contains forbidden study, Git, symlink or bytecode artifacts")
    for name, expected in report["standalone_input_sha256"].items():
        require(sha((standalone / name).read_bytes()) == expected, f"Standalone input changed: {name}")
    for name, expected in dict(report["input_hashes"]).items():
        checked(ROOT / name, expected, report)
    require(sha(Path(__file__).read_bytes()) == report["checker_sha256"], "Checker changed during execution")
    require(not report["failures"], "One or more deterministic checks failed; see retained logs")
    report["preservation"] = dict(unchanged_docs=sorted(set(frozen) - set(APPROVED)),
                                  restored_all_ten_base_hashes=True,
                                  frozen_inputs_and_live_docs_rechecked_at_completion=True,
                                  standalone_inputs_unchanged=True)
    report["status"] = "PASS"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.absolute()
    require(output.resolve().is_relative_to(GENERATED.resolve())
            and output.resolve() != GENERATED.resolve(), "Output must descend from this study's generated directory")
    require(not output.exists() and not output.is_symlink(), "Output must be fresh")
    output.mkdir(parents=True, exist_ok=False)
    report = dict(status="RUNNING", scope="administrative live-file correspondence and supplied-state algebra only",
                  command=[sys.executable, *sys.argv], cwd=str(Path.cwd()), source_root=str(ROOT),
                  checker_sha256=sha(Path(__file__).read_bytes()),
                  started_utc=datetime.now(timezone.utc).isoformat(),
                  environment=dict(python=sys.version, executable=sys.executable, platform=platform.platform(),
                                   machine=platform.machine(), numpy=importlib.metadata.version("numpy"),
                                   scipy=importlib.metadata.version("scipy"), subprocess_overrides=CONTROLS),
                  input_hashes={}, commands=[], failures=[],
                  read_scope=dict(full_code=["P2_EDITION_BUILD.py", "P2_PROMOTION_CHECK.py", *SCRIPTS],
                                  correspondence_only=["P2_SECTION.md", "P2_PROPOSED_GUIDE.md",
                                                       "P2_PROMOTION_DEPENDENCIES.md", "P1_SECTION.md", "ten live docs"],
                                  hash_only="All other P1 manifest inputs and P2_PROMOTION_RECIPE.md",
                                  no_scientific_review=True),
                  limitations=["No new scientific-review verdict, training, sweep or empirical reproduction.",
                               "Only affected-section and full guide links/fragments are checked; older chapter links/proofs are not re-audited.",
                               "External URLs are not fetched; the preserved code-guide link is checked for existence only."])
    try:
        verify(output, report)
    except BaseException as error:
        report["status"] = "FAIL"
        report["failures"].append(dict(type=type(error).__name__, message=str(error)))
        (output / "failure.log").write_text(traceback.format_exc(), encoding="utf-8")
    finally:
        report["finished_utc"] = datetime.now(timezone.utc).isoformat()
        report["output_sha256"] = {p.relative_to(output).as_posix(): sha(p.read_bytes())
                                   for p in sorted(output.rglob("*"))
                                   if p.is_file() and p.name not in {"validation.json", "SHA256SUMS.json"}}
        json_write(output / "validation.json", report)
        json_write(output / "SHA256SUMS.json", dict(report["output_sha256"],
                                                    **{"validation.json": sha((output / "validation.json").read_bytes())}))
    print(json.dumps(dict(status=report["status"], report=str(output / "validation.json"),
                         report_sha256=sha((output / "validation.json").read_bytes()),
                         failures=report["failures"]), ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
