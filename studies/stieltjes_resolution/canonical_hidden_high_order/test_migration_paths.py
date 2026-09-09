"""Source-role routing and immutable digest gates; no recurrence or audit work."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from studies.stieltjes_resolution.canonical_hidden_high_order import hidden_moment_hankel_audit as audit


class SourceRoleTests(unittest.TestCase):
    def test_exact_legacy_current_and_basename_labels_bind_source_not_data(self):
        fixture = b'fixed source-role fixture'
        digest = hashlib.sha256(fixture).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            result_path = Path(tmp) / 'caller-selected-result.json'
            for filename in ('production_hidden_recurrence.py', 'independent_hidden_recurrence.py'):
                for label in (
                    filename,
                    f'studies/stieltjes_resolution/canonical_hidden_high_order/{filename}',
                    f'studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/{filename}',
                ):
                    for field in ('file', 'path'):
                        document = {'source': {field: label, 'sha256': digest}}
                        original = copy.deepcopy(document)
                        with self.subTest(label=label, field=field), mock.patch.object(
                            Path, 'read_bytes', autospec=True, return_value=fixture
                        ) as read:
                            result = audit.validate_source(document, result_path)
                        read.assert_called_once_with(audit.HERE / filename)
                        self.assertEqual(result, {'file': label, 'sha256': digest})
                        self.assertEqual(document, original)
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_unknown_or_traversing_labels_refuse_before_read(self):
        for label in ('unknown.py', '../production_hidden_recurrence.py',
                      'unrelated/production_hidden_recurrence.py',
                      str(audit.HERE / 'production_hidden_recurrence.py')):
            with self.subTest(label=label), mock.patch.object(Path, 'read_bytes') as read:
                with self.assertRaisesRegex(ValueError, 'unrecognized.*source label'):
                    audit.validate_source({'source': {'path': label, 'sha256': '0' * 64}}, Path('input.json'))
                read.assert_not_called()

    def test_wrong_digest_is_not_replaced_with_current_digest(self):
        document = {'source': {'file': 'production_hidden_recurrence.py', 'sha256': '0' * 64}}
        with mock.patch.object(Path, 'read_bytes', return_value=b'tiny source fixture'):
            with self.assertRaisesRegex(AssertionError, 'source hash mismatch'):
                audit.validate_source(document, Path('input.json'))
        self.assertEqual(document['source']['sha256'], '0' * 64)

    def test_actual_retained_records_reach_current_sources_and_keep_frozen_hash_failures(self):
        read_bytes = Path.read_bytes
        for result_path, filename in (
            (audit.PRODUCTION_RESULT, 'production_hidden_recurrence.py'),
            (audit.INDEPENDENT_RESULT, 'independent_hidden_recurrence.py'),
        ):
            document = json.loads(result_path.read_text())
            original = copy.deepcopy(document)
            with self.subTest(result=result_path.name), mock.patch.object(
                Path, 'read_bytes', autospec=True, side_effect=read_bytes
            ) as read:
                with self.assertRaisesRegex(AssertionError, 'source hash mismatch'):
                    audit.validate_source(document, result_path)
            read.assert_called_once_with(audit.HERE / filename)
            self.assertEqual(document, original)


if __name__ == '__main__':
    unittest.main()
