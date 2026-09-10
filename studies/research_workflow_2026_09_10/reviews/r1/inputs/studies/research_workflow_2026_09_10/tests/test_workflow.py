"""Mechanical gate tests; fixtures are synthetic, never scientific reviews."""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


REPO = Path(__file__).absolute().parents[3]
SOURCE = Path(os.environ.get("STUDY_WORKFLOW_SOURCE", REPO / "studies/_workflow.py"))
if "STUDY_WORKFLOW_SOURCE" not in os.environ and not SOURCE.exists():
    SOURCE = Path(__file__).absolute().parents[1] / "implementation/study_workflow.py"
spec = importlib.util.spec_from_file_location("study_workflow", SOURCE)
wf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wf)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        area = REPO / "data/generated/research_workflow_2026_09_10"
        area.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="workflow-test-", dir=area))
        for name in ("studies", "data"):
            (self.root / name).mkdir()
        (self.root / "README.md").write_text("Fixture repository\n")
        self.study = self.root / "studies/demo"
        self.package = self.study / "promotion/example"
        self.round = self.package / "rounds/r1"

    def tearDown(self):
        for path in self.root.rglob("*"):
            if not path.is_symlink() and path.is_dir():
                path.chmod(0o755)
        shutil.rmtree(self.root)

    def cli(self, *args, success=True):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            result = wf.main(list(args), root=self.root)
        self.assertEqual(result, 0 if success else 1, output.getvalue())
        return output.getvalue()

    def start(self):
        self.cli("start", "demo", "--question", "Can this fixture pass?", "--owner", "owner")

    def freeze(self, components="theory", authors=("author-one",)):
        args = ["freeze", "demo", "example", "r1", "--components", components]
        for author in authors:
            args += ["--author-session", author]
        self.cli(*args)

    def packet(self, components="theory", authors=("author-one",)):
        self.start()
        for name in ("candidate", "dependencies"):
            (self.package / name).mkdir(parents=True)
        (self.package / "candidate/result.md").write_text("Synthetic proof fixture: 1 + 1 = 2.\n")
        (self.package / "dependencies/definition.md").write_text("Usual integer addition.\n")
        self.freeze(components, authors)

    def json(self, name, value=None):
        path = self.round / name
        if value is not None:
            path.write_bytes(wf.encoded(value))
        return json.loads(path.read_text())

    def evidence(self, name, content):
        (self.round / name).write_text(content)
        return {"path": name, "sha256": wf.digest(content.encode())}

    def complete(self, components="theory", authors=("author-one",)):
        self.packet(components, authors)
        bound = {"schema": 1, "input_digest": self.json("inputs/INPUTS.json")["input_digest"]}
        selection = dict(bound, reviewer_session="selector", decision="accept", nonduplicate=True,
                         relevant=True, useful=True, reason="Synthetic selection fixture.",
                         report=self.evidence("selection.md", "Synthetic selector: fixture is relevant to gate testing.\n"))
        self.json("selection.json", selection)
        for label in ("A", "B"):
            review = dict(bound, reviewer_session="reviewer-" + label, full_input_read=True,
                          isolated=True, verdict="clean", unresolved=[],
                          completion_evidence="Synthetic complete read coverage; no actual scientific review claimed.",
                          report=self.evidence("report_" + label + ".md", f"Synthetic reviewer {label}: read candidate/result.md line 1 and dependencies/definition.md line 1 completely; no commands needed for this synthetic assertion.\n"))
            self.json("review_" + label + ".json", review)
        if set(components.split(",")) & {"code", "empirical"}:
            command = [sys.executable, "-c", "assert 2 + 2 == 4; print('1 fixture assertion passed')"]
            result = subprocess.run(command, cwd=self.root, capture_output=True, text=True, check=True)
            log_path = self.root / "data/generated/demo/run/validation.log"
            log_path.parent.mkdir(parents=True)
            log_path.write_text(result.stdout)
            log = {"path": log_path.relative_to(self.root).as_posix(), "sha256": wf.digest(result.stdout.encode())}
            kinds = (["tests"] if "code" in components else []) + (["reproduction"] if "empirical" in components else [])
            self.json("validation.json", dict(bound, checks=[dict(kind=kind, command=shlex.join(command),
                      result="pass", exit_code=result.returncode, summary=result.stdout.strip(), log=log) for kind in kinds]))

    def check(self, success=True):
        return self.cli("check", "demo", "--package", "example", "--round", "r1", success=success)

    def test_fresh_start_status_and_standalone(self):
        self.start()
        self.assertEqual({p.name for p in self.study.iterdir()}, set(wf.RECORDS))
        self.assertIn("MECHANICAL READINESS ONLY", self.cli("check", "demo"))
        self.assertIn("owner: owner", self.cli("status", "demo"))
        installed = self.root / "studies/_workflow.py"
        shutil.copyfile(SOURCE, installed)
        result = subprocess.run([sys.executable, str(installed), "check", "demo"], cwd=self.root,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_duplicate_adopt_preserves_every_existing_byte(self):
        self.start()
        self.cli("start", "demo", "--question", "Other", "--owner", "other", success=False)
        (self.study / "CLAIMS.md").write_bytes(b"old record\x00\xff")
        (self.study / "STATE.md").unlink()
        original = {p.name: p.read_bytes() for p in self.study.iterdir()}
        self.cli("adopt", "demo", "--question", "Other", "--owner", "other")
        for name, content in original.items():
            self.assertEqual((self.study / name).read_bytes(), content)
        self.assertTrue((self.study / "STATE.md").exists())

    def test_unsafe_names_roots_and_namespaces(self):
        for name in ("../escape", "/absolute", "a/b", "a\\b", "a..b", "Upper", "x__y"):
            self.cli("start", name, "--question", "q", "--owner", "o", success=False)
        with self.assertRaises(wf.WorkflowError):
            wf.repository(Path("/"))
        alias = self.root / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(wf.WorkflowError):
            wf.repository(alias)
        alias.unlink()
        self.start()
        info = json.loads((self.study / "STUDY.json").read_text())
        info["data_path"] = "data/generated/another"
        (self.study / "STUDY.json").write_bytes(wf.encoded(info))
        self.cli("check", "demo", success=False)

    def test_symlink_and_hardlink_records_and_sources(self):
        self.packet()
        for use_symlink in (True, False):
            source = self.package / "candidate/result.md"
            alias = self.package / "candidate/alias.md"
            alias.symlink_to(source) if use_symlink else os.link(source, alias)
            self.check(success=False)
            self.cli("freeze", "demo", "example", "r2", "--author-session", "author", success=False)
            alias.unlink()
        record = self.study / "STATE.md"
        record.unlink()
        record.symlink_to(self.study / "README.md")
        self.cli("check", "demo", success=False)

    def test_freeze_never_overwrites_and_detects_changes(self):
        self.complete()
        before = (self.round / "inputs/INPUTS.json").read_bytes()
        self.cli("freeze", "demo", "example", "r1", "--author-session", "author", success=False)
        self.assertEqual((self.round / "inputs/INPUTS.json").read_bytes(), before)
        self.check()
        source = self.package / "candidate/result.md"
        source.write_text("Changed source\n")
        self.assertIn("current candidate", self.check(success=False))
        source.write_bytes((self.round / "inputs/candidate/result.md").read_bytes())
        frozen = self.round / "inputs/candidate/result.md"
        frozen.chmod(0o644)
        frozen.write_text("Changed frozen file\n")
        self.assertIn("frozen files differ", self.check(success=False))

    def test_every_review_gate_and_hash_binding(self):
        self.complete(authors=("author-one", "author-two"))
        self.check()
        cases = {"selection.json": {"decision": "reject", "nonduplicate": False, "relevant": False,
                                      "useful": False, "reason": "", "reviewer_session": "author-two"},
                 "review_A.json": {"full_input_read": False, "isolated": False, "verdict": "revise",
                                   "unresolved": ["gap"], "completion_evidence": "", "input_digest": "stale",
                                   "reviewer_session": "author-two"},
                 "review_B.json": {"reviewer_session": "reviewer-A"}}
        for name, mutations in cases.items():
            original = self.json(name)
            for field, bad in mutations.items():
                with self.subTest(name=name, field=field):
                    self.json(name, dict(original, **{field: bad}))
                    self.check(success=False)
            self.json(name, original)
            content = (self.round / name).read_bytes()
            (self.round / name).unlink()
            self.check(success=False)
            (self.round / name).write_bytes(content)
        report = self.round / "report_A.md"
        report.write_text("Changed report\n")
        self.check(success=False)

    def test_report_containment_and_duplicate_reports(self):
        self.complete()
        original = self.json("review_B.json")
        for path in ("../report_A.md", "/etc/passwd", "inputs/candidate/result.md"):
            self.json("review_B.json", dict(original, report={"path": path, "sha256": "bad"}))
            self.check(success=False)
        self.json("review_B.json", dict(original, report=self.json("review_A.json")["report"]))
        self.check(success=False)

    def test_extra_source_frozen_files_and_hash_matching_aliases(self):
        self.complete()
        for folder in (self.package / "candidate", self.round / "inputs/candidate"):
            folder.chmod(0o755)
            extra = folder / "extra.md"
            extra.write_text("unlisted file")
            self.check(success=False)
            extra.unlink()
        report = self.round / "report_A.md"
        backup = self.round / "report_backup.md"
        report.rename(backup)
        for symlink in (True, False):
            report.symlink_to(backup) if symlink else os.link(backup, report)
            self.check(success=False)
            report.unlink()
        backup.rename(report)
        self.check()

    def test_code_empirical_actual_logs_and_required_receipts(self):
        self.complete("theory,code,empirical")
        self.assertIn("MECHANICAL READINESS ONLY", self.check())
        original = self.json("validation.json")
        for bad in ([], original["checks"][:1], [dict(original["checks"][0], exit_code=1)]):
            self.json("validation.json", dict(original, checks=bad))
            self.check(success=False)
        self.json("validation.json", original)
        other = self.root / "data/generated/another/run/validation.log"
        other.parent.mkdir(parents=True)
        shutil.copyfile(self.root / original["checks"][0]["log"]["path"], other)
        bad_log = dict(original["checks"][0]["log"], path=other.relative_to(self.root).as_posix())
        self.json("validation.json", dict(original, checks=[dict(check, log=bad_log) for check in original["checks"]]))
        self.check(success=False)
        self.json("validation.json", original)
        (self.root / original["checks"][0]["log"]["path"]).write_text("Changed log")
        self.check(success=False)

    def test_code_component_empty_candidate_and_transaction_cleanup(self):
        self.packet()
        candidate = self.package / "candidate/result.md"
        candidate.unlink()
        self.cli("freeze", "demo", "example", "r2", "--author-session", "author", success=False)
        (self.package / "candidate/program.py").write_text("print(1)\n")
        self.cli("freeze", "demo", "example", "r2", "--author-session", "author", success=False)
        with mock.patch.object(wf, "write_new", side_effect=OSError("simulated write failure")):
            self.cli("freeze", "demo", "example", "r2", "--author-session", "author", "--components", "code", success=False)
        self.assertFalse((self.package / "rounds/r2").exists())


if __name__ == "__main__":
    unittest.main()
