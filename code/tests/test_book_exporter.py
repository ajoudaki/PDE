"""Small safety/discovery tests; do not read or execute the live PDE project."""
from contextlib import redirect_stdout, redirect_stderr
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

# This is a standalone command, not part of the numerical pde package.
_exporter_path = Path(__file__).resolve().parents[1] / "tools/book_pdf/export_book.py"
_spec = importlib.util.spec_from_file_location("pde_book_exporter", _exporter_path)
exporter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(exporter)


class ExporterTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pde-export-test-", dir="/tmp")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / "source with spaces"
        (self.repo / "docs").mkdir(parents=True)
        (self.repo / "code").mkdir()
        self.put("docs/README.md", "# Introduction\n\n[Second](second.md)\n[First](first.md)\n")
        self.put("docs/NOTATION.md", "# Notation\n")
        self.put("docs/first.md", "# First\n")
        self.put("docs/second.md", "# Second\n")
        self.put("code/README.md", "# Implementation\n")

    def put(self, name, content):
        (self.repo / name).write_text(content)

    def test_guide_order_and_appendix(self):
        files, unlisted = exporter.discover(self.repo)
        self.assertEqual(files, [["docs/README.md", "Introduction"], ["docs/NOTATION.md", "Notation"],
                                 ["docs/second.md", "1"], ["docs/first.md", "2"], ["code/README.md", "Appendix"]])
        self.assertEqual(unlisted, [])

    def test_new_unlisted_chapter_is_not_silently_omitted(self):
        self.put("docs/new.md", "# New chapter\n")
        files, unlisted = exporter.discover(self.repo)
        self.assertEqual(unlisted, ["docs/new.md"])
        self.assertEqual(files[-2], ["docs/new.md", "3"])

    def test_snapshot_keeps_source_bytes_unchanged(self):
        work = self.root / "build"
        work.mkdir()
        files, _, payload = exporter.snapshot(self.repo, work)
        self.assertEqual(len(files), 5)
        for name, data in payload.items():
            self.assertEqual((self.repo / name).read_bytes(), data)
            self.assertEqual((work / "snapshot" / name).read_bytes(), data)

    def test_rejects_source_symlink_escape(self):
        external = self.root / "external.md"
        external.write_text("Not part of this project\n")
        (self.repo / "docs/escape.md").symlink_to(external)
        with self.assertRaisesRegex(ValueError, "symlink"):
            exporter.discover(self.repo)

    def test_rejects_output_inside_repo(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            exporter.validate_output(self.repo, self.repo / "book.pdf")

    def test_rejects_non_pdf_output(self):
        with self.assertRaisesRegex(ValueError, "end in"):
            exporter.validate_output(self.repo, self.root / "book.md")

    def test_rejects_unverified_converter_archive(self):
        archive = self.root / "pandoc.tar.gz"
        archive.write_bytes(b"not the verified release archive")
        with self.assertRaisesRegex(RuntimeError, "integrity"):
            exporter.install_private_converter(self.root, archive)
        self.assertFalse((self.root / "pandoc").exists())

    def test_installed_converter_must_match_pinned_version(self):
        with patch.object(exporter.shutil, "which", return_value="/usr/bin/pandoc"), \
             patch.object(exporter, "run", return_value="pandoc 2.0\n"):
            with self.assertRaisesRegex(RuntimeError, "requires Pandoc 3.6.4"):
                exporter.install_private_converter(self.root)

    def test_missing_converter_has_actionable_error(self):
        with patch.object(exporter.shutil, "which", return_value=None), \
             patch.object(exporter, "DEFAULT_ARCHIVE", self.root / "missing.tar.gz"):
            with self.assertRaisesRegex(RuntimeError, "--pandoc-archive"):
                exporter.install_private_converter(self.root)

    def test_atomic_copy_replaces_only_the_requested_file(self):
        incoming = self.root / "incoming"
        incoming.write_bytes(b"new PDF payload")
        destination = self.root / "output" / "book.pdf"
        exporter.atomic_copy(incoming, destination)
        incoming.write_bytes(b"updated PDF payload")
        exporter.atomic_copy(incoming, destination)
        self.assertEqual(destination.read_bytes(), b"updated PDF payload")
        self.assertEqual(list(destination.parent.iterdir()), [destination])

    def test_failed_conversion_preserves_previous_pdf_and_sources(self):
        destination = self.root / "book.pdf"
        destination.write_bytes(b"previous successful PDF")
        before = {p: p.read_bytes() for p in self.repo.rglob("*.md")}
        work = self.root / "failed-build"
        work.mkdir()
        # Inject a converter failure without installing or running any tools.
        with patch.object(exporter.tempfile, "mkdtemp", return_value=str(work)), \
             patch.object(exporter.shutil, "which", return_value="installed"), \
             patch.object(exporter, "install_private_converter"), \
             patch.object(exporter, "run", side_effect=RuntimeError("injected conversion failure")), \
             redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            result = exporter.main([str(destination), "--repo", str(self.repo)])
        self.assertEqual(result, 1)
        self.assertEqual(destination.read_bytes(), b"previous successful PDF")
        self.assertFalse(destination.with_suffix(".build.json").exists())
        self.assertTrue(work.is_dir())
        for path, data in before.items():
            self.assertEqual(path.read_bytes(), data)


if __name__ == "__main__":
    unittest.main()
