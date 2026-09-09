# Direct Loewner experiments

This branch preserves the chronological direct numerical investigation.

- `protocol.md` and `direct_test_report.md` document the initial experiment,
  which failed because finite-width polynomial ascent can blow up and because
  the tested clock was not the correct common output clock.
- `corrected_clock_protocol.md` and `corrected_clock_report.md` document the
  corrected-clock experiment.
- `corrected_clock_bias_audit.md` supersedes its evidential interpretation:
  the resulting robust proxy has an (O(1)) local-coefficient bias and is not
  calibrated well enough for a target Loewner conclusion.

All generated arrays, logs, summaries, and frozen manifests are under
[`runs/`](runs/).  They remain useful negative-result and reproducibility
records.
