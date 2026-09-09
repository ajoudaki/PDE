"""Dependency-free shared-guard checks; tiny files, no campaign execution."""
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from studies._output_paths import REPO_ROOT, StudyPaths


class SharedOutputPathsTests(unittest.TestCase):
    def setUp(self):
        self.paths = StudyPaths(__file__)

    def test_validation_accepts_own_tree_and_scratch_without_creating_them(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(Path, 'mkdir') as mkdir:
            for path in (self.paths.generated/'unwritten', Path(tmp)/'unwritten'):
                self.assertEqual(self.paths.require_output(path), path.resolve())
            mkdir.assert_not_called()

    def test_validation_refuses_source_history_and_other_generated_trees(self):
        with mock.patch.object(Path, 'mkdir') as mkdir:
            for path in (REPO_ROOT/'studies/stieltjes_finite_width', self.paths.historical,
                         REPO_ROOT/'data/generated/another_study', REPO_ROOT/'data/generated',
                         REPO_ROOT/'data/generated/stieltjes_finite_width_other'):
                with self.subTest(path=path), self.assertRaises(ValueError):
                    self.paths.require_output(path)
            mkdir.assert_not_called()

    def test_existing_child_hardlink_is_rejected_before_truncating_consumer(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            retained = root/'input'
            retained.write_bytes(b'retained input')
            output = root/'output'
            (output/'nested').mkdir(parents=True)
            alias = output/'nested/run.log'
            os.link(retained, alias)
            with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaisesRegex(ValueError, 'hardlink'):
                checked = self.paths.require_output(output)
                (checked/'nested/run.log').write_text('must never truncate')
            mkdir.assert_not_called()
            self.assertEqual(retained.read_bytes(), b'retained input')
            self.assertEqual(alias.read_bytes(), b'retained input')

    def test_hardlinked_leaf_is_rejected_too(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            retained = root/'input'
            retained.write_bytes(b'unchanged')
            alias = root/'output'
            os.link(retained, alias)
            with self.assertRaisesRegex(ValueError, 'hardlink'):
                self.paths.require_output(alias)
            self.assertEqual(retained.read_bytes(), b'unchanged')

    def test_symlink_children_roots_and_components_are_rejected(self):
        for kind in ('file', 'directory', 'dangling', 'root', 'component'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                output = root/'output'
                output.mkdir()
                target = root/'target'
                if kind in ('directory', 'root', 'component'):
                    target.mkdir()
                elif kind == 'file':
                    target.write_bytes(b'unchanged')
                link = output/'link'
                link.symlink_to(target)
                selected = link/'child' if kind == 'component' else link if kind == 'root' else output
                with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaisesRegex(ValueError, 'symlink'):
                    self.paths.require_output(selected)
                mkdir.assert_not_called()
                self.assertTrue(link.is_symlink())
                if kind == 'file':
                    self.assertEqual(target.read_bytes(), b'unchanged')
                if kind == 'dangling':
                    self.assertFalse(target.exists())

    def test_ordinary_existing_products_remain_usable(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)/'output'
            (output/'nested').mkdir(parents=True)
            product = output/'nested/run.log'
            product.write_text('old generated product')
            self.assertEqual(self.paths.require_output(output), output)
            self.assertEqual(self.paths.require_output(product), product)
            self.assertEqual(product.read_text(), 'old generated product')


if __name__ == '__main__':
    unittest.main()
