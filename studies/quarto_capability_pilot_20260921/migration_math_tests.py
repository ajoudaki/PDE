import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import migration_check as check


class MathPacketFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.study = root / "studies" / "pilot"
        self.frozen = root / "frozen" / "doc.md"
        self.study.mkdir(parents=True)
        self.frozen.parent.mkdir(parents=True)
        self.source = (
            "# Math\n\nSee Equation (3.5)--(3.6).\n\n"
            "\\[\nx+y \\tag{3.5}\n\\]\n\n"
            "\\[\nx-y \\tag{3.6}\n\\]\n\n"
            "**Theorem (Energy law).** The energy is constant.\n"
            "It stays finite.\n\nAfterward.\n"
        )
        self.frozen.write_text(self.source, encoding="utf-8")
        manifest = {"version": 1, "files": [{
            "source": "docs/doc.md", "key": "doc", "qmd": "doc.qmd",
            "sha256": hashlib.sha256(self.source.encode()).hexdigest(),
            "lines": len(self.source.splitlines()), "frozen": "frozen/doc.md",
        }]}
        self.targets = [
            {"id": "sec-doc-l1", "kind": "sec", "source": "docs/doc.md", "start": 1, "end": 1},
            {"id": "eq-doc-l5", "kind": "eq", "source": "docs/doc.md", "start": 5, "end": 7},
            {"id": "eq-doc-l9", "kind": "eq", "source": "docs/doc.md", "start": 9, "end": 11},
            {"id": "thm-doc-l13", "kind": "thm", "source": "docs/doc.md", "start": 13, "end": 14},
        ]
        marker = "**Theorem (Energy law).** "
        self.edits = [
            self.edit("# Math", len("# Math"), "", " {#sec-doc-l1}", "label", "sec-doc-l1"),
            self.edit("Equation (3.5)", 0, "Equation (3.5)", "@eq-doc-l5 ", "reference", "eq-doc-l5"),
            self.edit("(3.6)", 0, "(3.6)", " @eq-doc-l9", "reference", "eq-doc-l9"),
        ]
        for line, target in ((5, "eq-doc-l5"), (9, "eq-doc-l9")):
            block_start = self.line_offset(line)
            close = self.source.index(r"\]", block_start)
            tag = self.source.index(r"\tag", block_start)
            tag_text = r"\tag{3.5}" if line == 5 else r"\tag{3.6}"
            self.edits.extend([
                {"offset": block_start, "old": r"\[", "new": "$$", "kind": "math-delimiter"},
                {"offset": tag, "old": tag_text, "new": "", "kind": "equation-tag", "target": target},
                {"offset": close, "old": r"\]", "new": "$$", "kind": "math-delimiter"},
                {"offset": close + 2, "old": "", "new": f" {{#{target}}}", "kind": "equation-label", "target": target},
            ])
        theorem_start = self.source.index(marker)
        theorem_end = self.source.index("It stays finite.") + len("It stays finite.")
        self.edits.extend([
            {"offset": theorem_start, "old": marker,
             "new": "::: {#thm-doc-l13}\n## Energy law\n\n",
             "kind": "statement-open", "target": "thm-doc-l13"},
            {"offset": theorem_end, "old": "", "new": "\n\n:::",
             "kind": "statement-close", "target": "thm-doc-l13"},
        ])
        self.edits.sort(key=lambda item: item["offset"])
        self.write("sources.json", manifest)
        self.write("registry.json", [])
        self.write("progress.json", {"accepted": []})
        self.write("targets.json", self.targets)
        self.write_packet()

    def line_offset(self, line: int) -> int:
        return sum(len(part) for part in self.source.splitlines(keepends=True)[:line - 1])

    def edit(self, needle: str, adjustment: int, old: str, new: str, kind: str, target: str) -> dict:
        return {"offset": self.source.index(needle) + adjustment, "old": old, "new": new,
                "kind": kind, "target": target}

    def write(self, name: str, value, raw: bool = False) -> None:
        (self.study / name).write_text(value if raw else json.dumps(value), encoding="utf-8")

    def write_packet(self) -> None:
        self.edits.sort(key=lambda item: item["offset"])
        self.write("edits.json", self.edits)
        self.write("targets.json", self.targets)
        self.write("candidate.qmd", check.apply_edits(self.source, self.edits), raw=True)
        self.write("packet.json", {
            "id": "linear_005", "source": "docs/doc.md", "start": 1,
            "end": len(self.source.splitlines()), "candidate": "candidate.qmd",
            "edits": "edits.json", "targets": "targets.json", "sources": "sources.json",
            "registry": "registry.json", "progress": "progress.json",
        })

    def validate(self):
        return check.validate_packet(self.study / "packet.json", self.root)


class MigrationMathTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.fixture = MathPacketFixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_valid_tagged_equations_ranges_and_named_theorem(self):
        result = self.fixture.validate()
        self.assertTrue(result["ok"], result["errors"])

    def test_equation_target_requires_complete_original_tagged_display(self):
        target = next(item for item in self.fixture.targets if item["id"] == "eq-doc-l5")
        target["end"] = 6
        self.fixture.write_packet()
        result = self.fixture.validate()
        self.assertTrue(any("complete tagged display" in error for error in result["errors"]))

    def test_tag_and_label_must_be_exactly_paired(self):
        self.fixture.edits = [item for item in self.fixture.edits
                              if not (item["kind"] == "equation-label" and item["target"] == "eq-doc-l5")]
        self.fixture.write_packet()
        result = self.fixture.validate()
        self.assertTrue(any("exactly one equation-label" in error for error in result["errors"]))

    def test_tagged_display_cannot_be_left_without_equation_target(self):
        self.fixture.targets = [item for item in self.fixture.targets if item["id"] != "eq-doc-l5"]
        self.fixture.edits = [item for item in self.fixture.edits if item.get("target") != "eq-doc-l5"]
        self.fixture.write_packet()
        result = self.fixture.validate()
        self.assertTrue(any("lacks its unique equation target" in error for error in result["errors"]))

    def test_equation_reference_number_must_match_frozen_target_tag(self):
        reference = next(item for item in self.fixture.edits if item["old"] == "Equation (3.5)")
        reference["new"] = "@eq-doc-l9 "
        reference["target"] = "eq-doc-l9"
        self.fixture.write_packet()
        result = self.fixture.validate()
        self.assertTrue(any("reference number does not match target tag" in error for error in result["errors"]))

    def test_theorem_title_and_close_boundary_are_exact(self):
        opening = next(item for item in self.fixture.edits if item["kind"] == "statement-open")
        opening["new"] = opening["new"].replace("Energy law", "Changed title")
        closing = next(item for item in self.fixture.edits if item["kind"] == "statement-close")
        closing["offset"] = self.fixture.source.index("The energy is constant.") + len("The energy is constant.")
        self.fixture.write_packet()
        result = self.fixture.validate()
        self.assertTrue(any("exact original theorem title" in error for error in result["errors"]))
        self.assertTrue(any("theorem span end" in error for error in result["errors"]))

    def test_unconverted_numeric_section_prefix_is_rejected(self):
        self.fixture.source = self.fixture.source.replace("Afterward.", "See Section 2(a); $0.5$ is unchanged.")
        self.fixture.frozen.write_text(self.fixture.source, encoding="utf-8")
        manifest = json.loads((self.fixture.study / "sources.json").read_text(encoding="utf-8"))
        manifest["files"][0]["sha256"] = hashlib.sha256(self.fixture.source.encode()).hexdigest()
        self.fixture.write("sources.json", manifest)
        self.fixture.write_packet()
        result = self.fixture.validate()
        self.assertTrue(any("numeric section references" in error for error in result["errors"]))
        self.assertFalse(any("0.5" in error for error in result["errors"]))

    def test_unconverted_equation_reference_is_rejected(self):
        self.fixture.source = self.fixture.source.replace("Afterward.", "Afterward. See (3.6).")
        self.fixture.frozen.write_text(self.fixture.source, encoding="utf-8")
        manifest = json.loads((self.fixture.study / "sources.json").read_text(encoding="utf-8"))
        manifest["files"][0]["sha256"] = hashlib.sha256(self.fixture.source.encode()).hexdigest()
        self.fixture.write("sources.json", manifest)
        self.fixture.write_packet()
        result = self.fixture.validate()
        self.assertTrue(any("equation references" in error for error in result["errors"]))

    def test_inline_math_lookalikes_do_not_trigger_reference_scan(self):
        candidate = (
            "Inline $O(1)$, $1/(4m)$, $\\rho(0)$, and $W^{(2)}$ are math. "
            "The prose equation (1) remains a reference."
        )
        prose = check._reference_prose(candidate)
        self.assertEqual(check.RAW_NUMBERED_REF_RE.findall(prose), [])
        equation = check.EQUATION_CAPTION_RE.search(prose)
        self.assertIsNotNone(equation)
        self.assertEqual(equation.group("number"), "1")

    def test_tag_only_line_uses_comment_while_inline_tag_deletes(self):
        original = "\\[\nx+y\n  \\tag{3.5} \n\\]\n"
        target = {"id": "eq-doc-l1", "kind": "eq", "source": "docs/doc.md", "start": 1, "end": 4}
        tag_offset = original.index(r"\tag")
        edits = [{"offset": tag_offset, "old": r"\tag{3.5}", "new": "%",
                  "kind": "equation-tag", "target": target["id"]}]
        errors = []
        check.validate_edit_grammars(original, edits, {target["id"]: target}, 1, errors, "docs/doc.md")
        self.assertFalse(any("deletion/comment replacement" in error for error in errors), errors)
        self.assertEqual(check._normalized_source_displays(
            original, edits, {target["id"]: target}, 1, "docs/doc.md"
        ), ["\nx+y\n  % \n"])
        edits[0]["new"] = ""
        errors = []
        check.validate_edit_grammars(original, edits, {target["id"]: target}, 1, errors, "docs/doc.md")
        self.assertTrue(any("deletion/comment replacement" in error for error in errors))
        inline = "\\[\nx+y \\tag{3.5}\n\\]\n"
        self.assertEqual(check._equation_tag_replacement(inline, inline.index(r"\tag"), r"\tag{3.5}"), "")


class MigrationTranscriptionTests(unittest.TestCase):
    def _case(self):
        original = "# Math\n\nText `x+y`.\n\n    x+y = z. (T1)\n\nSee (T1).\n"
        target = {
            "id": "eq-doc-l5", "kind": "eq", "source": "docs/doc.md",
            "start": 5, "end": 5,
        }
        inline_offset = original.index("`x+y`")
        display_offset = original.index("    x+y")
        reference_offset = original.rindex("(T1)")
        edits = [
            {"offset": inline_offset, "old": "`x+y`", "new": "$x+y$", "kind": "inline-transcription"},
            {"offset": display_offset, "old": "    x+y = z. (T1)",
             "new": "$$\nx+y=z.\n$$ {#eq-doc-l5}", "kind": "display-transcription", "target": "eq-doc-l5"},
            {"offset": reference_offset, "old": "(T1)", "new": "@eq-doc-l5", "kind": "reference", "target": "eq-doc-l5"},
        ]
        return original, target, edits

    def test_valid_inline_and_numbered_display_transcription(self):
        original, target, edits = self._case()
        errors = []
        check.validate_edit_grammars(original, edits, {target["id"]: target}, 1, errors, "docs/doc.md")
        self.assertEqual(errors, [])
        candidate = check.apply_edits(original, edits)
        self.assertEqual(
            check._project_transcriptions(original, candidate, edits),
            original.replace("See (T1)", "See @eq-doc-l5"),
        )

    def test_unmarked_formula_mutation_is_rejected_by_projection(self):
        original, target, edits = self._case()
        candidate = check.apply_edits(original, edits).replace("x+y=z.", "x-y=z.")
        with self.assertRaises(check.CheckFailure):
            check._project_transcriptions(original, candidate, edits)

    def test_incomplete_indented_code_block_target_is_rejected(self):
        original = "Before.\n    x+y = z.\n    q=1. (T1)\nAfter.\n"
        target = {"id": "eq-doc-l2", "kind": "eq", "source": "docs/doc.md", "start": 2, "end": 3}
        edit = {"offset": original.index("    x+y"), "old": "    x+y = z.",
                "new": "$$\nx+y=z.\n$$", "kind": "display-transcription"}
        errors = []
        check.validate_edit_grammars(original, [edit], {target["id"]: target}, 1, errors, "docs/doc.md")
        self.assertTrue(any("complete indented display" in error for error in errors), errors)

    def test_raw_inline_transcription_cannot_split_alphabetic_identifier(self):
        for original, old in (("reco$n$struction", "$n$"), ("$L$ipschitz", "$L$")):
            with self.subTest(original=original):
                offset = original.index(old)
                edit = {"offset": offset, "old": old, "new": old,
                        "kind": "inline-transcription"}
                errors = []
                check.validate_edit_grammars(original, [edit], {}, 1, errors, "docs/doc.md")
                self.assertTrue(any("splits an alphabetic identifier" in error for error in errors), errors)

    def test_complete_inline_spans_and_code_spans_remain_valid(self):
        cases = [
            ("Use x_i and (x).", "x_i"),
            ("Use `reconstruction`.", "`reconstruction`"),
        ]
        for original, old in cases:
            with self.subTest(old=old):
                offset = original.index(old)
                content = old[1:-1] if old.startswith("`") else old
                edit = {"offset": offset, "old": old, "new": f"${content}$",
                        "kind": "inline-transcription"}
                errors = []
                check.validate_edit_grammars(original, [edit], {}, 1, errors, "docs/doc.md")
                self.assertEqual(errors, [])

    def test_derivative_prime_must_be_apostrophe_or_superscript(self):
        for content in (r"\phi\prime", r"f\prime"):
            edit = {"offset": 0, "old": "phi", "new": f"${content}$",
                    "kind": "inline-transcription"}
            errors = []
            check.validate_edit_grammars("phi", [edit], {}, 1, errors, "docs/doc.md")
            self.assertTrue(any("detaches a derivative prime" in error for error in errors), errors)

        for content in (r"\phi'", r"\phi^\prime", r"\phi^{\prime}", r"\prime"):
            edit = {"offset": 0, "old": "phi", "new": f"${content}$",
                    "kind": "inline-transcription"}
            errors = []
            check.validate_edit_grammars("phi", [edit], {}, 1, errors, "docs/doc.md")
            self.assertEqual(errors, [])

    def test_transcription_rejects_unequivocal_ascii_pseudo_math(self):
        for content in (
            r"||Delta delta||2+C||Delta H^1||2",
            r"prod_k(...)<=exp(sum_k(...))",
            r"sqrt(x)",
            r"tanh(x)",
            r"clip_R(x)",
        ):
            with self.subTest(content=content):
                edit = {"offset": 0, "old": "x", "new": f"${content}$",
                        "kind": "inline-transcription"}
                errors = []
                check.validate_edit_grammars("x", [edit], {}, 1, errors, "docs/doc.md")
                self.assertTrue(any("transcription retains" in error for error in errors), errors)

    def test_transcription_allows_latex_and_descriptive_ascii(self):
        for content in (r"\|\Delta x\|^2 + C", r"\operatorname{exp}(x)", r"\operatorname{clip}_R(x)", r"\text{Delta sum}", "x+y"):
            with self.subTest(content=content):
                edit = {"offset": 0, "old": "x", "new": f"${content}$",
                        "kind": "inline-transcription"}
                errors = []
                check.validate_edit_grammars("x", [edit], {}, 1, errors, "docs/doc.md")
                self.assertEqual(errors, [])

    def test_inline_transcription_rejects_double_escaped_tex(self):
        for content in (r"\\Delta x", r"\\|x\\|"):
            edit = {"offset": 0, "old": "x", "new": f"${content}$",
                    "kind": "inline-transcription"}
            errors = []
            check.validate_edit_grammars("x", [edit], {}, 1, errors, "docs/doc.md")
            self.assertTrue(any("double-escaped TeX" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
