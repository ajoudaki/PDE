"""Path-only owning-study checks; no legacy engines or attempts."""
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from studies.stieltjes_hybrid_campaign.breadth_panel.successive_paths import (
    GENERATED_PANEL, REPO, parse_analysis_paths, require_output,
)


class OutputBoundaryTests(unittest.TestCase):
    def test_source_history_and_foreign_generated_are_rejected_without_writes(self):
        for target in (REPO/'studies/stieltjes_hybrid_campaign',
                       REPO/'data/historical/studies/stieltjes_hybrid_campaign',
                       REPO/'data/generated/resnet_activation_controls',
                       REPO/'data/generated/stieltjes_hybrid_campaign_other',
                       REPO/'data/generated'):
            with self.subTest(target=target), mock.patch.object(Path, 'mkdir') as mkdir:
                with self.assertRaises(ValueError):
                    require_output(target)
                with self.assertRaises(ValueError):
                    parse_analysis_paths('successive_n4096', ['--output-dir', str(target)])
                mkdir.assert_not_called()

    def test_own_study_and_scratch_remain_valid_without_writes(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(Path, 'mkdir') as mkdir:
            for target in (GENERATED_PANEL/'successive_n4096', GENERATED_PANEL.parent/'other-output', Path(tmp)/'fresh'):
                self.assertEqual(require_output(target), target.resolve())
                self.assertEqual(parse_analysis_paths('successive_n4096', ['--output-dir', str(target)]).output_dir,
                                 target.resolve())
            mkdir.assert_not_called()


if __name__ == '__main__':
    unittest.main()
