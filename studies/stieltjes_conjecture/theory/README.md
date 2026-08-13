# Theory and moment reconstruction

This directory contains the exact derivative-to-moment calculations,
Stieltjes/Hankel certificates, atomic quadrature reconstruction, and analytic
bounds used by the authoritative
[`../CURRENT_RESEARCH_STATE.md`](../CURRENT_RESEARCH_STATE.md).

The principal current artifacts are:

- `derivatives_order11.json` and `certificates_order11.json`: exact audited
  derivatives, coefficients of (K), moments, and Hankel determinants;
- `stieltjes_certificates.py`: exact rational certificate generator;
- `moment_reconstruction.py` and `reconstruction_order11.json`: Gaussian and
  zero-Radau atomic reconstructions;
- `exact_d13_threshold.py`: the exact order-thirteen threshold calculation.
- `stieltjes_tests.html` and `stieltjes_reconstruction_audit.html`: the two
  interactive visual audits created during the investigation.

`EARLIER_REPORT.md` is retained as a superseded historical report.  Some JSON
and provenance text files intentionally contain the old pre-consolidation
paths that were recorded when their computations ran.
