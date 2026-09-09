"""Private plain-text fixtures only; never compile or read maintained reports."""
from contextlib import contextmanager, redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from . import build_report as report


@contextmanager
def layout():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        inputs = root / 'inputs'
        inputs.mkdir()
        sources = (inputs / 'first.md', inputs / 'second.md')
        tex = inputs / 'wrapper.tex'
        for path in (*sources, tex):
            path.write_text('Private plain text fixture.\n')
        output = root / 'fresh'
        build = output / 'build'
        markdown = build / 'markdown'
        with mock.patch.multiple(report, SOURCES=sources, REPORT_TEX=tex,
                                 OUTPUT_DIR=output, BUILD_DIR=build, MARKDOWN_DIR=markdown,
                                 REPORT_PDF=output / 'wrapper.pdf'):
            yield root, sources, tex


class ReportPathTests(unittest.TestCase):
    def assert_refused_before_work(self, entry=report.main):
        with mock.patch.object(report.shutil, 'rmtree', side_effect=AssertionError('deletion reached')) as delete, \
             mock.patch.object(Path, 'read_text', side_effect=AssertionError('source reading reached')) as read, \
             mock.patch.object(report, 'run', side_effect=AssertionError('compiler reached')) as run:
            with self.assertRaises(ValueError):
                entry()
            delete.assert_not_called()
            read.assert_not_called()
            run.assert_not_called()

    def test_publication_preserves_all_maintained_inputs(self):
        for index in range(3):
            for kind in ('same', 'symlink', 'hardlink'):
                with self.subTest(input=index, kind=kind), layout() as (_root, sources, tex):
                    source = (*sources, tex)[index]
                    report.OUTPUT_DIR.mkdir()
                    destination = report.REPORT_PDF
                    if kind == 'same':
                        destination = source
                    elif kind == 'symlink':
                        destination.symlink_to(source)
                    else:
                        destination.hardlink_to(source)
                    with mock.patch.object(report, 'REPORT_PDF', destination):
                        self.assert_refused_before_work()
                    self.assertEqual(source.read_text(), 'Private plain text fixture.\n')

    def test_publication_preserves_intermediate_markdown_and_tex_even_before_creation(self):
        for leaf in ('first.pdf.md', 'second.pdf.md', 'markdown_math_defs.tex'):
            for existing in (False, True):
                with self.subTest(leaf=leaf, existing=existing), layout():
                    intermediate = report.MARKDOWN_DIR / leaf
                    if existing:
                        intermediate.parent.mkdir(parents=True)
                        intermediate.write_text('Private intermediate input.\n')
                    with mock.patch.object(report, 'REPORT_PDF', intermediate):
                        self.assert_refused_before_work()
                    if existing:
                        self.assertEqual(intermediate.read_text(), 'Private intermediate input.\n')

    def test_intermediate_aliases_refuse_in_main_and_direct_callables(self):
        for entry in (report.main, report.protect_markdown, report.compile_report):
            for leaf in ('first.pdf.md', 'markdown_math_defs.tex'):
                with self.subTest(entry=entry.__name__, leaf=leaf), layout() as (_root, sources, _tex):
                    report.MARKDOWN_DIR.mkdir(parents=True)
                    (report.MARKDOWN_DIR / leaf).symlink_to(sources[1])
                    self.assert_refused_before_work(entry)
                    self.assertEqual(sources[1].read_text(), 'Private plain text fixture.\n')

    def test_rebuild_cannot_delete_a_source_or_follow_parent_alias(self):
        with layout() as (root, sources, _tex):
            with mock.patch.object(report, 'BUILD_DIR', sources[0].parent):
                self.assert_refused_before_work()
            (root / 'linked-output').symlink_to(sources[0].parent, target_is_directory=True)
            with mock.patch.object(report, 'OUTPUT_DIR', root / 'linked-output'):
                self.assert_refused_before_work()

    def test_valid_plain_text_pipeline_preserves_sources_and_intermediates(self):
        with layout() as (_root, sources, tex):
            before = {path: path.read_bytes() for path in (*sources, tex)}
            report.MARKDOWN_DIR.mkdir(parents=True)
            (report.BUILD_DIR / 'old-build-placeholder').write_text('old private build')

            def fake_compile():
                for source in sources:
                    self.assertEqual((report.MARKDOWN_DIR / (source.stem + '.pdf.md')).read_bytes(), before[source])
                built = report.BUILD_DIR / report.REPORT_PDF.name
                built.write_bytes(b'private mock PDF output\n')
                return built

            with mock.patch.object(report, 'compile_report', side_effect=fake_compile) as compiler, \
                 mock.patch.object(report, 'verify_pdf') as verify, redirect_stdout(io.StringIO()):
                report.main()
            compiler.assert_called_once()
            verify.assert_called_once()
            self.assertEqual(before, {path: path.read_bytes() for path in (*sources, tex)})
            self.assertEqual(report.REPORT_PDF.read_bytes(), b'private mock PDF output\n')
            self.assertTrue((report.MARKDOWN_DIR / 'markdown_math_defs.tex').is_file())


if __name__ == '__main__':
    unittest.main()
