# Direct Loewner experiments

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

This branch preserves the chronological direct numerical investigation.

- `protocol.md` and `direct_test_report.md` document the initial experiment,
  which failed because finite-width polynomial ascent can blow up and because
  the tested clock was not the correct common output clock.
- `corrected_clock_protocol.md` and `corrected_clock_report.md` document the
  corrected-clock experiment.
- `corrected_clock_bias_audit.md` supersedes its evidential interpretation:
  the resulting robust proxy has an (O(1)) local-coefficient bias and is not
  calibrated well enough for a target Loewner conclusion.

Retained arrays, logs, summaries and frozen manifests are under repository
`data/historical/studies/stieltjes_direct_loewner/runs/`. Fresh producers use
`data/generated/stieltjes_direct_loewner/`; the corrected-clock producer writes
`runs/corrected_clock_run_20260814/`, also the finite-width jet consumer's
default input. Historical records retain their original paths and hashes.

`simulate_loewner.py` validates its `--output` as this study's generated tree
or external scratch, rejecting existing symlink/hardlink aliases before opening
its log. Related shared-helper tools use `--output-dir` and, when reading saved
products, explicit `--input-dir` or `--historical-inputs`. There is no implicit
historical fallback. This documents routing, not a fresh campaign validation.
