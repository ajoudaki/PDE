import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import migration_check as check


class PacketFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.study = root / "studies" / "pilot"
        self.frozen = root / "frozen" / "doc.md"
        self.study.mkdir(parents=True)
        self.frozen.parent.mkdir(parents=True)
        self.source = "# Intro\n\nSee C.4.5.\n\n\\[\nx+y\n\\]\n"
        self.full_source = self.source + "# Future\n"
        self.frozen.write_text(self.full_source, encoding="utf-8")
        manifest = {
            "version": 1,
            "files": [{
                "source": "docs/doc.md", "key": "doc", "qmd": "doc.qmd",
                "sha256": hashlib.sha256(self.full_source.encode()).hexdigest(),
                "lines": 8, "frozen": "frozen/doc.md",
            }],
        }
        self.write("sources.json", manifest)
        self.write("registry.json", [])
        self.write("progress.json", {"accepted": []})
        self.targets = [
            {"id": "sec-doc-l1", "kind": "sec", "source": "docs/doc.md", "start": 1, "end": 1},
            {"id": "sec-doc-l8", "kind": "sec", "source": "docs/doc.md", "start": 8, "end": 8},
        ]
        self.edits = [
            {"offset": 7, "old": "", "new": " {#sec-doc-l1}", "kind": "label", "target": "sec-doc-l1"},
            {"offset": self.source.index("C.4.5"), "old": "C.4.5", "new": "@sec-doc-l8", "kind": "reference", "target": "sec-doc-l8"},
            {"offset": self.source.index(r"\["), "old": r"\[", "new": "$$", "kind": "math-delimiter"},
            {"offset": self.source.index(r"\]"), "old": r"\]", "new": "$$", "kind": "math-delimiter"},
        ]
        self.edits.sort(key=lambda edit: edit["offset"])
        self.write("targets.json", self.targets)
        self.write("edits.json", self.edits)
        self.write("candidate.qmd", check.apply_edits(self.source, self.edits), raw=True)
        self.packet = {
            "id": "linear_001", "source": "docs/doc.md", "start": 1, "end": 7,
            "candidate": "candidate.qmd", "edits": "edits.json", "targets": "targets.json",
            "sources": "sources.json", "registry": "registry.json", "progress": "progress.json",
        }
        self.write("packet.json", self.packet)

    def write(self, name: str, value, raw: bool = False) -> None:
        text = value if raw else json.dumps(value)
        (self.study / name).write_text(text, encoding="utf-8")

    def validate(self):
        return check.validate_packet(self.study / "packet.json", self.root)


class MigrationCheckTests(unittest.TestCase):
    def test_native_numbered_reference_variants(self):
        for old, expected in [
            ('Section C.4', '@sec-x-l1'),
            ('section 1', '@sec-x-l1'),
            ('Sections 7.2', '@sec-x-l1'),
            ('§1', '@sec-x-l1'),
            ('§ 1', '@sec-x-l1'),
            ('§§1', '@sec-x-l1'),
            ('§§ 1', '@sec-x-l1'),
            ('III.F', '@sec-x-l1'),
            ('III.F.2', '@sec-x-l1'),
            ('Section C.4.6.T1', '@sec-x-l1'),
            ('Section C.4.6.P1', '@sec-x-l1'),
            ('10.2', '@sec-x-l1'),
            ('[Section C.5](old.md#heading)', '@sec-x-l1'),
            ('Section\n[C.4.7](old.md#heading)', '@sec-x-l1'),
            ('[Global nonlinear learning, Section C.4](old.md#heading)', 'Global nonlinear learning, @sec-x-l1')]:
            with self.subTest(old=old):
                self.assertEqual(check.native_reference_text(old, 'sec-x-l1'), expected)
        self.assertIsNone(check.native_reference_text('risk at time 40', 'sec-x-l1'))

    def test_hierarchical_letter_tags_are_scanned_and_parsed(self):
        self.assertEqual(
            check.RAW_NUMBERED_REF_RE.findall('See C.4.6.T1 and C.4.6.P1 and C.4.6.S21.'),
            ['C.4.6.T1', 'C.4.6.P1', 'C.4.6.S21'],
        )
        for tag in ('C.4.6.T1', 'C.4.6.P1', 'C.4.6.S21'):
            self.assertIsNotNone(check.EQUATION_TAG_RE.fullmatch(rf'\tag{{{tag}}}'))

    def test_dotted_family_descriptions_are_not_numeric_references(self):
        prose = "Families C.4.6.T, C.4.6.P, C.4.6.S and C.4.6.F are described here."
        self.assertEqual(check.RAW_NUMBERED_REF_RE.findall(prose), [])

    def test_roman_locator_forms_are_scanned_as_whole_tokens(self):
        prose = "See III.F and III.F.2, but preserve C.4.6.T as family prose."
        self.assertEqual(check.RAW_NUMBERED_REF_RE.findall(prose), ["III.F", "III.F.2"])

    def test_numbered_headings_are_not_prose_references(self):
        prose = check._reference_prose('### A.1. Title {#sec-doc-l1}\n\nSee A.1\n')
        self.assertEqual(check.RAW_NUMBERED_REF_RE.findall(prose), ['A.1'])

    def test_mermaid_only_fence_conversion(self):
        old = '```mermaid\nflowchart TD\nA --> B\n```\n'
        edit = dict(offset=0, old='```mermaid', new='```{mermaid}', kind='mermaid-fence')
        errors=[]
        check.validate_edit_grammars(old, [edit], {}, 1, errors)
        self.assertEqual(errors, [])
        edit['new'] += '\nA --> C'
        check.validate_edit_grammars(old, [edit], {}, 1, errors)
        self.assertTrue(errors)

    def test_native_reference_preserves_descriptive_prefix(self):
        target=dict(id='sec-doc-l8', kind='sec', source='docs/doc.md', start=8,end=8)
        old='[Global nonlinear learning, Section C.4](old.md)'
        edit=dict(offset=0,old=old,new='@sec-doc-l8',kind='reference',target='sec-doc-l8')
        errors=[]
        check.validate_edit_grammars(old,[edit],{'sec-doc-l8':target},1,errors)
        self.assertTrue(errors)

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.fixture = PacketFixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_valid_packet_and_reserved_inventory(self):
        result = self.fixture.validate()
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["inventory"]["defined"], ["sec-doc-l1"])
        self.assertEqual(result["inventory"]["reserved"], ["sec-doc-l8"])

    def test_content_corruption_is_rejected(self):
        candidate = (self.fixture.study / "candidate.qmd").read_text(encoding="utf-8")
        self.fixture.write("candidate.qmd", candidate.replace("x+y", "x-y"), raw=True)
        result = self.fixture.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("exact ordered edit replay" in error for error in result["errors"]))

    def test_wrong_deterministic_id_is_rejected(self):
        errors = []
        bad = [{"id": "sec-doc-l2", "kind": "sec", "source": "docs/doc.md", "start": 1, "end": 1}]
        manifest = {"docs/doc.md": {"key": "doc", "lines": 8}}
        check.validate_target_list(bad, "proposed", manifest, errors)
        self.assertTrue(any("sec-doc-l1" in error for error in errors))

    def test_section_span_and_out_of_bounds_are_rejected(self):
        for end in (2, 99):
            with self.subTest(end=end):
                errors = []
                target = dict(id="sec-doc-l1", kind="sec", source="docs/doc.md", start=1, end=end)
                check.validate_target_list([target], "proposed", {"docs/doc.md": {"key": "doc", "lines": 8}}, errors)
                self.assertTrue(errors)

    def test_noncanonical_relative_old_link_is_rejected(self):
        # The old link must be found even if its path contains .. components.
        self.fixture.source = self.fixture.source.replace('See C.4.5.', 'See C.4.5. [old](../docs/doc.md).')
        self.fixture.full_source = self.fixture.source + '# Future\n'
        self.fixture.frozen.write_text(self.fixture.full_source)
        manifest = json.loads((self.fixture.study / 'sources.json').read_text())
        manifest['files'][0]['sha256'] = hashlib.sha256(self.fixture.full_source.encode()).hexdigest()
        self.fixture.write('sources.json', manifest)
        for edit in self.fixture.edits:
            if edit['kind'] == 'math-delimiter':
                edit['offset'] = self.fixture.source.index(edit['old'])
        self.fixture.write('edits.json', self.fixture.edits)
        self.fixture.write('candidate.qmd', check.apply_edits(self.fixture.source, self.fixture.edits), raw=True)
        result = self.fixture.validate()
        self.assertTrue(any('unconverted internal-book' in error for error in result['errors']))

    def test_wrong_link_destination_is_rejected(self):
        ref = next(edit for edit in self.fixture.edits if edit["kind"] == "reference")
        ref.update(old="C.4.5", new="[C.4.5](wrong.qmd#sec-doc-l8)")
        self.fixture.write("edits.json", self.fixture.edits)
        self.fixture.write("candidate.qmd", check.apply_edits(self.fixture.source, self.fixture.edits), raw=True)
        result = self.fixture.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("destination" in error for error in result["errors"]))

    def test_existing_markdown_link_caption_can_be_preserved(self):
        old = "[shared notation](NOTATION.md)"
        target = {"id": "sec-doc-l8", "kind": "sec", "source": "docs/doc.md", "start": 8, "end": 8}
        edit = {
            "offset": 0, "old": old,
            "new": "[shared notation](doc.qmd#sec-doc-l8)",
            "kind": "reference", "target": "sec-doc-l8",
        }
        errors = []
        check.validate_edit_grammars(old, [edit], {target["id"]: target}, 1, errors, "docs/doc.md")
        self.assertEqual(errors, [])

    def test_collisions_and_crossing_ranges_are_rejected(self):
        registry = [{"id": "proof-doc-l1", "kind": "proof", "source": "docs/doc.md", "start": 1, "end": 5}]
        proposed = [
            {"id": "proof-doc-l4", "kind": "proof", "source": "docs/doc.md", "start": 4, "end": 7},
            {"id": "eq-doc-l3", "kind": "eq", "source": "docs/doc.md", "start": 3, "end": 6},
        ]
        errors = []
        check.validate_target_relations(registry, proposed, errors)
        self.assertTrue(any("same-kind" in error for error in errors))
        self.assertTrue(any("cross" in error for error in errors))

    def test_cross_kind_containment_is_valid(self):
        outer = [{"id": "proof-doc-l1", "kind": "proof", "source": "docs/doc.md", "start": 1, "end": 7}]
        inner = [{"id": "eq-doc-l5", "kind": "eq", "source": "docs/doc.md", "start": 5, "end": 7}]
        errors = []
        check.validate_target_relations(outer, inner, errors)
        self.assertEqual(errors, [])

    def test_edited_registry_after_acceptance_is_rejected(self):
        registry_hash = hashlib.sha256((self.fixture.study / "registry.json").read_bytes()).hexdigest()
        accepted_name = "accepted.qmd"
        self.fixture.write(accepted_name, "# Prior {#sec-doc-l1}\n", raw=True)
        accepted_hash = hashlib.sha256((self.fixture.study / accepted_name).read_bytes()).hexdigest()
        progress = {"accepted": [{
            "packet": "linear_000", "source": "docs/doc.md", "start": 1, "end": 1,
            "candidate": accepted_name, "candidate_sha256": accepted_hash,
            "registry_sha256": registry_hash,
        }]}
        self.fixture.write("progress.json", progress)
        self.fixture.write("registry.json", self.fixture.targets[:1])
        result = self.fixture.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("registry hash" in error for error in result["errors"]))

    def test_invalid_heading_boundary_is_rejected(self):
        edit = {"offset": 2, "old": "", "new": " {#sec-doc-l1}", "kind": "label", "target": "sec-doc-l1"}
        errors = []
        check.validate_edit_grammars(self.fixture.source, [edit], {t["id"]: t for t in self.fixture.targets}, 1, errors)
        self.assertTrue(any("end of an unlabeled ATX heading" in error for error in errors))

    def test_unknown_reference_is_rejected(self):
        ref = next(edit for edit in self.fixture.edits if edit["kind"] == "reference")
        ref.update(new="@sec-doc-l99", target="sec-doc-l99")
        self.fixture.write("edits.json", self.fixture.edits)
        self.fixture.write("candidate.qmd", check.apply_edits(self.fixture.source, self.fixture.edits), raw=True)
        result = self.fixture.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("unknown target" in error for error in result["errors"]))

    def test_missing_covered_heading_label_is_rejected(self):
        self.fixture.edits = [edit for edit in self.fixture.edits if edit["kind"] != "label"]
        self.fixture.write("edits.json", self.fixture.edits)
        self.fixture.write("candidate.qmd", check.apply_edits(self.fixture.source, self.fixture.edits), raw=True)
        result = self.fixture.validate()
        self.assertFalse(result["ok"])
        self.assertTrue(any("lacks its unique section label" in error for error in result["errors"]))

    def test_original_coordinates_survive_inserted_blank_line(self):
        self.fixture.packet["end"] = 8
        self.fixture.write("packet.json", self.fixture.packet)
        second_heading = self.fixture.full_source.index("# Future")
        self.fixture.edits.extend([
            {"offset": second_heading, "old": "", "new": "\n", "kind": "whitespace"},
            {"offset": second_heading + len("# Future"), "old": "", "new": " {#sec-doc-l8}", "kind": "label", "target": "sec-doc-l8"},
        ])
        self.fixture.edits.sort(key=lambda edit: edit["offset"])
        self.fixture.write("edits.json", self.fixture.edits)
        self.fixture.write("candidate.qmd", check.apply_edits(self.fixture.full_source, self.fixture.edits), raw=True)
        result = self.fixture.validate()
        self.assertTrue(result["ok"], result["errors"])


if __name__ == "__main__":
    unittest.main()
