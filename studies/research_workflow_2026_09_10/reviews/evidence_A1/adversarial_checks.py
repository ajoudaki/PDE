"""Bounded independent mechanical attacks; no scientific conclusions or Git access."""

import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from unittest import mock

ROOT = Path(__file__).parents[4]
AREA = Path(__file__).parent
spec = importlib.util.spec_from_file_location("frozen_helper", ROOT / "studies/_workflow.py")
wf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wf)
spec = importlib.util.spec_from_file_location("frozen_tests", ROOT / "studies/research_workflow_2026_09_10/tests/test_workflow.py")
supplied = importlib.util.module_from_spec(spec)
spec.loader.exec_module(supplied)


@contextlib.contextmanager
def fixture(components="theory"):
    case = supplied.WorkflowTests()
    case.setUp()
    # Explicitly do not consult any Git metadata in independent attacks.
    with mock.patch.object(supplied.wf, "baseline", return_value=None):
        case.complete(components)
    try:
        yield case
    finally:
        case.tearDown()


def call(case):
    output = io.StringIO()
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
        result = wf.main(["check", "demo", "--package", "example", "--round", "r1"], root=case.root)
    return result, output.getvalue().strip()


def reject(label, mutate):
    with fixture() as case:
        mutate(case)
        result, output = call(case)
        assert result == 1, (label, result, output)
        print("REJECTED", label, "=>", output)


def write_json(case, path, obj):
    (case.round / path).write_bytes(wf.encoded(obj))


def alter_manifest(case, mutation, rebind=False):
    path = case.round / "inputs/INPUTS.json"
    value = json.loads(path.read_text())
    mutation(value)
    if rebind:
        value["input_digest"] = wf.digest(wf.canonical({k: v for k, v in value.items() if k != "input_digest"}))
    path.chmod(0o644)
    path.write_bytes(wf.encoded(value))


reject("duplicate JSON key", lambda c: (c.round / "review_A.json").write_text('{"schema":1,"schema":1}'))
reject("boolean masquerading as schema", lambda c: write_json(c, "review_A.json", dict(c.json("review_A.json"), schema=True)))
reject("review identity padded to evade author collision", lambda c: write_json(c, "review_A.json", dict(c.json("review_A.json"), reviewer_session=" author-one")))
reject("review identity collides with selector", lambda c: write_json(c, "review_A.json", dict(c.json("review_A.json"), reviewer_session="selector")))
reject("distinct paths but copied report bytes", lambda c: (c.round / "report_B.md").write_bytes((c.round / "report_A.md").read_bytes()) or None)
reject("missing frozen input manifest", lambda c: (c.round / "inputs").chmod(0o755) or (c.round / "inputs/INPUTS.json").unlink())
reject("manifest author edit without rehash", lambda c: alter_manifest(c, lambda m: m.update(author_sessions=["changed-author"])))
reject("manifest omitted dependency even with recomputed digest", lambda c: alter_manifest(c, lambda m: m["files"].pop("dependencies/definition.md"), True))
reject("manifest invalid line count even with recomputed digest", lambda c: alter_manifest(c, lambda m: m["files"]["candidate/result.md"].update(lines=True), True))
reject("stale selection after valid manifest identity change", lambda c: alter_manifest(c, lambda m: m.update(author_sessions=["changed-author"]), True))

with fixture() as c:
    # Match the new hash as well, so this tests duplicate report identity rather than staleness.
    content = (c.round / "report_A.md").read_bytes()
    (c.round / "report_B.md").write_bytes(content)
    value = c.json("review_B.json")
    value["report"]["sha256"] = hashlib.sha256(content).hexdigest()
    write_json(c, "review_B.json", value)
    result, output = call(c)
    assert result == 1 and "distinct full reports" in output
    print("REJECTED duplicate report under distinct path with correct hash =>", output)

with fixture() as c:
    empty = c.package / "candidate/empty"
    empty.mkdir()
    (empty / "outside").symlink_to(c.root / "data", target_is_directory=True)
    result, output = call(c)
    assert result == 1 and "symlink forbidden" in output
    print("REJECTED symlink directory in otherwise empty subtree =>", output)

with fixture() as c:
    fifo = c.package / "candidate/special"
    os.mkfifo(fifo)
    result, output = call(c)
    assert result == 1 and "special file forbidden" in output
    fifo.unlink()
    print("REJECTED FIFO without opening/blocking =>", output)

with fixture("code,empirical") as c:
    value = c.json("validation.json")
    value["checks"][0]["exit_code"] = False
    write_json(c, "validation.json", value)
    result, output = call(c)
    assert result == 1 and "validation failed" in output
    print("REJECTED false boolean exit status =>", output)

with fixture("code") as c:
    value = c.json("validation.json")
    log = c.root / value["checks"][0]["log"]["path"]
    alias = log.with_name("alias.log")
    os.link(log, alias)
    result, output = call(c)
    assert result == 1 and "hardlink alias forbidden" in output
    print("REJECTED same-namespace hash-matching hardlinked log =>", output)

with fixture() as c:
    # Demonstrate an expressly documented limit, not a scientific endorsement.
    (c.round / "REVIEW_PROMPT.md").write_text("Changed prompt; synthetic limit probe only.\n")
    result, output = call(c)
    assert result == 0
    print("DOCUMENTED/COORDINATOR LIMIT: prompt bytes are not bound by the helper manifest; check returned 0")

with fixture() as c:
    info = json.loads((c.study / "STUDY.json").read_text())
    info["lifecycle"] = "promoted"
    (c.study / "STUDY.json").write_bytes(wf.encoded(info))
    output = io.StringIO()
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
        result = wf.main(["check", "demo"], root=c.root)
    assert result == 0 and "MECHANICAL READINESS ONLY" in output.getvalue()
    print("DOCUMENTED LIMIT: administrative promoted label is allowed, never scientific acceptance")

print("ALL 17 INDEPENDENT ATTACK/LIMIT CASES COMPLETED")
