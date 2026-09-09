"""Guard-only fixtures: no raw decoding, fit, recurrence or seal generation."""
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from .depth_order5.primary import generate_frozen_artifacts as archived
from .depth_order5_scalar.multi_observable.audit import postprocess_h3_sine_regression as post
from .depth_order5_scalar.multi_observable.audit import run_h3_curvature_extension as curvature


class SelectedRawAliasTests(unittest.TestCase):
    def test_each_named_output_refuses_all_input_alias_forms_before_hash_or_science(self):
        for target, leaf in (
            (post, 'H3_NORMALIZED_SINE_RESULT.json'),
            (curvature, 'H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RAW.npz'),
            (curvature, 'H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RESULT.json'),
        ):
            for kind in ('same', 'symlink', 'hardlink', 'input-symlink'):
                with self.subTest(module=target.__name__, leaf=leaf, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    fresh = root / 'fresh'
                    fresh.mkdir()
                    output, raw = fresh / leaf, root / 'selected.npz'
                    if kind in ('same', 'input-symlink'):
                        output.write_bytes(b'untouched private raw placeholder')
                        if kind == 'same':
                            raw = output
                        else:
                            raw.symlink_to(output)
                    else:
                        raw.write_bytes(b'untouched private raw placeholder')
                        if kind == 'symlink':
                            output.symlink_to(raw)
                        else:
                            output.hardlink_to(raw)
                    before = raw.read_bytes()
                    with mock.patch.object(target, 'digest', side_effect=AssertionError('hash work reached')) as digest, \
                         mock.patch.object(target.np, 'load', side_effect=AssertionError('raw decoding reached')) as load, \
                         mock.patch.object(target, 'compile_numeric', side_effect=AssertionError('science reached')) as compile_numeric:
                        with self.assertRaises(ValueError):
                            target.run(raw, fresh)
                        digest.assert_not_called()
                        load.assert_not_called()
                        compile_numeric.assert_not_called()
                    self.assertEqual(raw.read_bytes(), before)

    def test_disjoint_input_keeps_original_digest_failure(self):
        for target in (post, curvature):
            with self.subTest(module=target.__name__), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                raw = root / 'selected.npz'
                raw.write_bytes(b'not the frozen raw bytes')
                with mock.patch.object(target.np, 'load', side_effect=AssertionError('raw decoding reached')) as load:
                    with self.assertRaises(RuntimeError):
                        target.run(raw, root / 'fresh')
                    load.assert_not_called()
                self.assertEqual(raw.read_bytes(), b'not the frozen raw bytes')
                self.assertFalse((root / 'fresh').exists())

    def test_archived_writer_refuses_before_temporary_or_expansion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            retained = root / 'retained-input.json'
            retained.write_bytes(b'untouched retained fixture')
            destination = root / 'H3_UNIT_COEFFICIENTS.json'
            destination.with_suffix('.json.tmp').symlink_to(retained)
            with mock.patch.object(Path, 'open', side_effect=AssertionError('file open reached')), \
                 mock.patch.object(archived, 'expand_coefficient_map', side_effect=AssertionError('expansion reached')) as expand:
                with self.assertRaisesRegex(RuntimeError, 'archive-only'):
                    archived.write_coefficient_json(destination, 3, 'private fixture', {})
                expand.assert_not_called()
            self.assertEqual(retained.read_bytes(), b'untouched retained fixture')
            self.assertFalse(destination.exists())
            self.assertTrue(callable(archived.sha256))
            self.assertTrue(callable(archived.compile_depth))


if __name__ == '__main__':
    unittest.main()
