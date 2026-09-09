# Theory and moment reconstruction

This directory contains the exact derivative-to-moment calculations,
Stieltjes/Hankel certificates, atomic quadrature reconstruction, and analytic
bounds used by the authoritative
[`../CURRENT_RESEARCH_STATE.md`](../CURRENT_RESEARCH_STATE.md).

The principal current artifacts are:

- `certificates_order11.json`: exact audited coefficients of $K$, moments, and
  Hankel determinants; the raw derivative certificate is owned by the
  [`../../mean_field_peeling/quadratic_compiler/`](../../mean_field_peeling/quadratic_compiler/)
  study;
- `stieltjes_certificates.py`: exact rational certificate generator;
- `moment_reconstruction.py` and `reconstruction_order11.json`: Gaussian and
  zero-Radau atomic reconstructions;
- `exact_d13_threshold.py`: the exact order-thirteen threshold calculation.
- `variance_homotopy_boundary_audit.py` and `finite_variance_hankel_audit.py`:
  exact boundary, first-variation, and finite-variance certificates;
- `sector_total_nonnegativity.py` and `sector_real_rootedness.py`: exact
  all-minor and Sturm-isolation audits for the $6\times12$ sector matrix;
- `stieltjes_tests.html` and `stieltjes_reconstruction_audit.html`: the two
  interactive visual audits created during the investigation.

`../archive/EARLIER_REPORT.md` is retained as a superseded historical report. Some JSON
and provenance text files intentionally contain the old pre-consolidation
paths that were recorded when their computations ran.
