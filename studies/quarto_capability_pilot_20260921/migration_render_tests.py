"""Focused controls for prefix assembly and the partial reference gate."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from check_linear_render import check
from render_linear import assemble


class RenderGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.run = Path(self.temp.name)
        self.inputs = self.run / 'inputs'
        self.inputs.mkdir()
        self.page = self.run / 'book/_out-html/index.html'
        self.page.parent.mkdir(parents=True)
        self.put('linear_001_packet.json', dict(sources='sources.json', candidate='candidate.qmd', registry='registry.json', targets='targets.json'))
        self.put('sources.json', dict(files=[dict(source='a.md', qmd='index.qmd'), dict(source='b.md', qmd='future.qmd')]))
        self.put('registry.json', [])
        self.targets = [dict(id='sec-a-l1', source='a.md', kind='sec', start=1, end=1),
                        dict(id='sec-b-l1', source='b.md', kind='sec', start=1, end=1)]
        self.put('targets.json', self.targets)
        (self.inputs / 'candidate.qmd').write_text('# A {#sec-a-l1}\n\n@sec-b-l1; [B](future.qmd#sec-b-l1).\n')
        self.html = '<h1 id="sec-a-l1">A</h1><span class="quarto-unresolved-ref">?sec-b-l1</span><a href="future.qmd#sec-b-l1">B</a>'
        self.page.write_text(self.html)
        for fmt in ('html', 'pdf', 'latex'):
            (self.run / (fmt + '.log')).write_text('WARN: Unable to resolve crossref @sec-b-l1\n')
        (self.run / 'commands.json').write_text(json.dumps([dict(exit_code=0)] * 3))

    def put(self, name, obj):
        (self.inputs / name).write_text(json.dumps(obj))

    def accepted(self):
        return check(self.run)['pass_partial']

    def test_exact_future_reservation_passes(self):
        self.assertTrue(self.accepted())

    def test_unknown_native_reference_fails(self):
        self.page.write_text(self.html.replace('?sec-b-l1', '?sec-wrong-l1'))
        self.assertFalse(self.accepted())

    def test_registered_but_unreferenced_native_warning_fails(self):
        self.put('targets.json', self.targets + [dict(id='sec-b-l8', source='b.md', kind='sec', start=8, end=8)])
        (self.run / 'pdf.log').write_text('WARN: Unable to resolve crossref @sec-b-l8\n')
        self.assertFalse(self.accepted())

    def test_wrong_future_link_fails(self):
        self.page.write_text(self.html.replace('future.qmd#sec-b-l1', 'future.qmd#sec-wrong-l1'))
        self.assertFalse(self.accepted())

    def test_future_html_rewrite_passes(self):
        self.page.write_text(self.html.replace('future.qmd#', 'future.html#'))
        self.assertTrue(self.accepted())

    def test_registered_but_unreferenced_future_link_fails(self):
        self.put('targets.json', self.targets + [dict(id='sec-b-l8', source='b.md', kind='sec', start=8, end=8)])
        self.page.write_text(self.html + '<a href="future.qmd#sec-b-l8">unused</a>')
        self.assertFalse(self.accepted())

    def test_missing_defined_label_fails(self):
        self.page.write_text(self.html.replace('id="sec-a-l1"', 'id="elsewhere"'))
        self.assertFalse(self.accepted())

    def test_duplicate_defined_label_fails(self):
        self.page.write_text(self.html + '<p id="sec-a-l1">duplicate</p>')
        self.assertFalse(self.accepted())

    def test_missing_citation_fails(self):
        (self.run / 'latex.log').write_text('[WARNING] Citeproc: citation unknown not found\n')
        self.assertFalse(self.accepted())

    def test_unregistered_missing_file_warning_fails(self):
        (self.run / 'html.log').write_text('WARN: Unable to resolve link target: wrong.qmd\n')
        self.assertFalse(self.accepted())

    def test_broken_local_fragment_fails(self):
        self.page.write_text(self.html + '<a href="#missing">missing</a>')
        self.assertFalse(self.accepted())


class AssemblyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        (self.base / 'linear_001.qmd').write_text('first\n')
        (self.base / 'linear_002.qmd').write_text('second\n')
        digest = hashlib.sha256((self.base / 'linear_001.qmd').read_bytes()).hexdigest()
        self.progress = dict(accepted=[dict(packet='linear_001', source='docs/README.md',
                                                   start=1, end=2, candidate='linear_001.qmd',
                                                   candidate_sha256=digest)])
        (self.base / 'progress.json').write_text(json.dumps(self.progress))
        (self.base / 'sources.json').write_text(json.dumps(dict(files=[
            dict(source='docs/README.md', qmd='index.qmd', lines=2),
            dict(source='docs/NOTATION.md', qmd='notation.qmd', lines=2)])))
        self.packet = dict(id='linear_002', source='docs/NOTATION.md', start=1, end=2,
                           sources='sources.json',
                           candidate='linear_002.qmd', progress='progress.json')
        (self.base / 'linear_002_packet.json').write_text(json.dumps(self.packet))

    def test_assembles_verified_contiguous_prefix(self):
        _, pieces, source = assemble(self.base / 'linear_002_packet.json')
        self.assertEqual(source, b'first\nsecond\n')
        self.assertEqual([(p['qmd'], p['start'], p['end']) for p in pieces],
                         [('index.qmd', 1, 2), ('notation.qmd', 1, 2)])

    def test_rejects_gap_before_current_packet(self):
        self.packet['start'] = 4
        (self.base / 'linear_002_packet.json').write_text(json.dumps(self.packet))
        with self.assertRaisesRegex(ValueError, 'does not continue'):
            assemble(self.base / 'linear_002_packet.json')

    def test_rejects_changed_accepted_candidate(self):
        (self.base / 'linear_001.qmd').write_text('changed\n')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            assemble(self.base / 'linear_002_packet.json')

    def test_rejects_skipped_source(self):
        self.packet['source'] = 'wrong.md'
        (self.base / 'linear_002_packet.json').write_text(json.dumps(self.packet))
        with self.assertRaisesRegex(ValueError, 'does not continue'):
            assemble(self.base / 'linear_002_packet.json')

    def test_same_chapter_continuation(self):
        manifest = dict(files=[dict(source='docs/README.md', qmd='index.qmd', lines=4)])
        (self.base / 'sources.json').write_text(json.dumps(manifest))
        self.packet.update(source='docs/README.md', start=3, end=4)
        (self.base / 'linear_002_packet.json').write_text(json.dumps(self.packet))
        _, pieces, content = assemble(self.base / 'linear_002_packet.json')
        self.assertEqual(content, b'first\nsecond\n')
        self.assertEqual([p['qmd'] for p in pieces], ['index.qmd', 'index.qmd'])


if __name__ == '__main__':
    unittest.main()
