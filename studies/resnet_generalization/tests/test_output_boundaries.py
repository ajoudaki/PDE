"""Tiny routing/publication fixtures; no trajectories, analysis, or seals."""
import contextlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

import numpy as np

from studies.resnet_generalization import combine_references as combine
from studies.resnet_generalization.generalization_paths import GENERATED_ROOT, REPO_ROOT, require_output


class OutputBoundaryTests(unittest.TestCase):
    def run_main(self, inputs, output):
        with mock.patch.object(sys, 'argv', ['combine', *map(str, inputs), '--output', str(output)]), \
             contextlib.redirect_stdout(io.StringIO()):
            combine.main()

    def assert_before_inputs(self, inputs, output, error):
        with mock.patch.object(combine, 'load_raw') as load, mock.patch.object(Path, 'mkdir') as mkdir:
            with self.assertRaises(error):
                self.run_main(inputs, output)
            load.assert_not_called()
            mkdir.assert_not_called()

    def fixture(self, path):
        metadata = dict.fromkeys(('case_id case_sha256 registry_sha256 n depth duration dt sample_dt '
                                  'sigma_w A gamma activation X y m d pde_seal_sha256 dynamics_sha256').split(), None)
        values = np.arange(4., dtype=float).reshape(2, 2, 1)
        np.savez(path, times=np.array([0., 1.]), seeds=np.array([11, 12]), f=values,
                 grams=values[..., None], theta=values[..., None], metadata_json=json.dumps(metadata))

    def test_protected_outputs_rejected_before_inputs(self):
        for directory in (REPO_ROOT/'studies/resnet_generalization',
                          REPO_ROOT/'data/historical/studies/resnet_generalization',
                          REPO_ROOT/'data/generated/resnet_activation_controls',
                          REPO_ROOT/'data/generated/resnet_generalization_other'):
            with self.subTest(directory=directory):
                self.assert_before_inputs([Path('unread.npz')], directory/'unwritten.npz', ValueError)

    def test_own_generated_and_external_scratch_are_valid_without_writes(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(Path, 'mkdir') as mkdir:
            for path in (GENERATED_ROOT/'boundary-test-unwritten.npz', Path(tmp)/'out.npz'):
                self.assertEqual(require_output(path), path.resolve())
                self.assertEqual(combine.require_new_output(path, [Path(tmp)/'input.npz'])[0], path.resolve())
            mkdir.assert_not_called()

    def test_input_aliases_are_rejected_before_inputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root/'input.npz'
            source.write_bytes(b'unchanged fixture')
            symlink = root/'symlink.npz'
            symlink.symlink_to(source)
            hardlink = root/'hardlink.npz'
            os.link(source, hardlink)
            for output in (source, root/'sub/../input.npz', symlink, hardlink):
                with self.subTest(output=output):
                    self.assert_before_inputs([source], output, ValueError)
            self.assertEqual(source.read_bytes(), b'unchanged fixture')

    def test_existing_final_partial_and_dangling_links_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, suffix in (('final', ''), ('partial', '.partial')):
                output = root/f'{name}.npz'
                occupied = Path(str(output)+suffix)
                occupied.write_bytes(b'preserve')
                self.assert_before_inputs([root/'unread.npz'], output, FileExistsError)
                self.assertEqual(occupied.read_bytes(), b'preserve')
            for name, suffix in (('link-final', ''), ('link-partial', '.partial')):
                output = root/f'{name}.npz'
                occupied = Path(str(output)+suffix)
                occupied.symlink_to(root/'absent-target')
                # The shared guard rejects a linked final before the
                # combiner's existing-file check; both refuse pre-read.
                self.assert_before_inputs([root/'unread.npz'], output,
                                          ValueError if not suffix else FileExistsError)
                self.assertTrue(occupied.is_symlink())

    def test_tiny_scratch_merge_preserves_output_and_provenance_format(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, output = root/'input.npz', root/'fresh/combined.npz'
            self.fixture(source)
            self.run_main([source], output)
            with np.load(output, allow_pickle=False) as result:
                np.testing.assert_array_equal(result['f_mean'], [[1.], [2.]])
                np.testing.assert_allclose(result['f_sem'], [[1.], [1.]])
                np.testing.assert_array_equal(result['seeds'], [11, 12])
                metadata = json.loads(str(result['metadata_json']))
                self.assertEqual(metadata['sources'], [str(source)])
                self.assertEqual(metadata['source_sha256'], [combine.file_sha256(source)])
            self.assertFalse(output.with_suffix('.npz.partial').exists())

    def test_conflict_after_loading_is_rechecked_before_publication(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, output = root/'input.npz', root/'output.npz'
            self.fixture(source)
            original_load = combine.load_raw
            partial = output.with_suffix('.npz.partial')
            def load_and_introduce_partial(path):
                partial.write_bytes(b'preserve late partial')
                return original_load(path)
            with mock.patch.object(combine, 'load_raw', side_effect=load_and_introduce_partial):
                with self.assertRaises(FileExistsError):
                    self.run_main([source], output)
            self.assertEqual(partial.read_bytes(), b'preserve late partial')
            self.assertFalse(output.exists())

    def test_exclusive_partial_creation_does_not_truncate_a_late_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, output = root/'input.npz', root/'output.npz'
            self.fixture(source)
            partial = output.with_suffix('.npz.partial')
            original_mkdir = Path.mkdir
            def mkdir_and_introduce_partial(path, *args, **kwargs):
                original_mkdir(path, *args, **kwargs)
                partial.write_bytes(b'preserve exclusive partial')
            with mock.patch.object(Path, 'mkdir', mkdir_and_introduce_partial):
                with self.assertRaises(FileExistsError):
                    self.run_main([source], output)
            self.assertEqual(partial.read_bytes(), b'preserve exclusive partial')
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
