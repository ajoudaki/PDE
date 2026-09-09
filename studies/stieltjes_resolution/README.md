# Stieltjes resolution program

The exploratory program is complete.  Its locked target was the natural
uniform block-metric extension of the formal moment conjecture, and that
target is **disproved exactly**.

At \((\alpha,\beta)=(0,1)\), the same one-input quadratic network reduces to a
two-variable polynomial derivation.  Exact coefficients through order
thirteen produce a negative shifted \(3\times3\) Hankel quadratic form.  The
complete \(\beta=1\) jet is now also exact as a polynomial in \(\alpha\), and
the same determinant stays negative for every
\(0\leq\alpha\leq1/100\).  Hence strictly positive metrics
\((\alpha,1)\), \(0<\alpha\leq1/100\), are counterexamples: the result does not
depend on freezing a layer.  This resolves uniform block-metric U1/U2/U3
negatively, but not canonical \((1,1)\) V1--V3.
The same six-moment determinant has a unique positive root
\(\alpha_*=0.017519225541486\ldots\), and every other available leading gate
on \(\beta=1\) is coefficientwise positive.  This exactly classifies the
computed prefix, not the all-order family.  At the boundary, an exact scaling
identifies the formal counterexample with the conventional one-hidden-layer
raw-square model.  That shallow flow also has explicit Riccati
characteristics, so characteristic integrability survives the failure of
Stieltjes positivity.

As a bounded canonical successor, two exact recurrence implementations now
agree through $F^{(17)}(0)$.  Exact inversion supplies the first eight
canonical moments, and both newly decidable $4\times4$ matrices satisfy
$H_3\succ0$ and $H_3^+\succ0$.  This is an exact finite-order pass only;
canonical V1--V3 remain open.  The frozen branch stopped at order seventeen,
and no order-nineteen computation was attempted.

- [BLOCK_METRIC_RESOLUTION.md](BLOCK_METRIC_RESOLUTION.md) is the complete
  proof and scope statement.
- [block_metric_counterexample.py](block_metric_counterexample.py) regenerates
  the certificate with standard-library exact rational arithmetic.
- [BLOCK_METRIC_COUNTEREXAMPLE.json](BLOCK_METRIC_COUNTEREXAMPLE.json) retains
  the exact coefficients, minors, and polynomial witness.
- [test_block_metric_counterexample.py](test_block_metric_counterexample.py)
  checks regeneration and the independent Campaign-4 prefix.
- [POSITIVE_ALPHA_JET_DERIVATION.md](POSITIVE_ALPHA_JET_DERIVATION.md) proves
  the fixed-order Gaussian detransposition recurrence and lists the complete
  jet through order thirteen.
- [ALPHA_INTERVAL_CERTIFICATE.json](ALPHA_INTERVAL_CERTIFICATE.json) retains
  the degree-36 determinant numerator and the exact \(\varepsilon=1/100\)
  convexity/Bernstein certificate.
- [ALPHA_TRANSITION_CERTIFICATE.json](ALPHA_TRANSITION_CERTIFICATE.json) and
  [alpha_transition_certificate.py](alpha_transition_certificate.py) retain
  the unique positive root isolation and coefficient-positive audit of every
  other leading six-moment gate on \(\beta=1\).
- [SHALLOW_QUADRATIC_REDUCTION.md](SHALLOW_QUADRATIC_REDUCTION.md) and
  [SHALLOW_QUADRATIC_CERTIFICATE.json](SHALLOW_QUADRATIC_CERTIFICATE.json)
  give the conventional shallow rescaling, exact negative determinant,
  Riccati characteristics, and global-Gaussian scope boundary.
- [independent_qalpha_recurrence_audit.py](independent_qalpha_recurrence_audit.py)
  recomputes the complete jet directly over \(\mathbb Q[\alpha]\).
- [independent_scalar_determinant_audit.py](independent_scalar_determinant_audit.py)
  independently reconstructs the determinant numerator from 37 scalar
  inversions.
- [ALPHA_CONNECTED_COMPILER_AUDIT.md](ALPHA_CONNECTED_COMPILER_AUDIT.md)
  records algebraically distinct connected-forest overlap checks.
- [PROOF_CONTRACT.md](PROOF_CONTRACT.md) separates canonical V1--V3 from the
  selected uniform target U1--U3.
- [ROUTE_REGISTRY.md](ROUTE_REGISTRY.md) records the independent proof and
  falsification routes.
- [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) records claim-level consequences.
- [canonical_high_order/](canonical_high_order/) contains the frozen
  order-fifteen/order-seventeen successor, two-route exact recurrence audits,
  the new moments $\mu_6,\mu_7$, and complete ordinary/shifted $4\times4$
  Hankel certificates.
- [canonical_hidden_high_order/](canonical_hidden_high_order/) contracts the
  same exact recurrence against both hidden preactivation squared-RMS
  observables.  It retains nine first-hidden and eight second-hidden moment
  candidates, normalized literal-RMS readouts, two independent exact
  reconstructions, and every accessible Hankel principal minor.
