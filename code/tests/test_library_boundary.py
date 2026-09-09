"""Small structural-check fixtures, independent of the research tree."""

from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest


spec = importlib.util.spec_from_file_location(
    "library_checker", Path(__file__).resolve().parents[1] / "tools" / "check_library.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class LibraryBoundaryTests(unittest.TestCase):
    def check_fixture(self, markdown="", module="", setup=None):
        with tempfile.TemporaryDirectory(prefix="pde-library-test-") as name:
            root = Path(name)
            (root / "docs").mkdir()
            (root / "code" / "pde").mkdir(parents=True)
            (root / "docs" / "page.md").write_text(markdown)
            (root / "code" / "pde" / "__init__.py").write_text(module)
            if setup is not None:
                setup(root)
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                result = checker.main(root)
            return result, err.getvalue()

    def test_missing_inline_and_reference_links(self):
        for markdown in ("[missing](no.md)", "[missing][p]\n\n[p]: no.md"):
            self.assertEqual(self.check_fixture(markdown)[0], 1)

    def test_valid_links_and_math_lookalikes(self):
        text = "[same](page.md)\n[ref]: page.md\n\\[v[mu](s,x)\\]\n"
        self.assertEqual(self.check_fixture(text)[0], 0)

    def test_missing_modules_and_undeclared_imports(self):
        for module in ("import pde.missing", "from .missing import value", "import unavailable_package"):
            self.assertEqual(self.check_fixture(module=module)[0], 1)

    def test_existing_relative_module(self):
        def setup(root):
            (root / "code" / "pde" / "helper.py").write_text("value = 1\n")
        self.assertEqual(self.check_fixture(module="from .helper import value", setup=setup)[0], 0)

    def test_dangling_symlink_rejected_without_reading(self):
        def setup(root):
            (root / "docs" / "link.md").symlink_to(root / "absent.md")
        result, error = self.check_fixture(setup=setup)
        self.assertEqual(result, 1)
        self.assertIn("symbolic link", error)


if __name__ == "__main__":
    unittest.main()
