# Fixed-depth extension

This directory contains the exact finite-width control program for arbitrary
hidden depth `H >= 1` and fixed batch size `B >= 1`.

- [`EXACT_FIXED_DEPTH_PROGRAM.md`](./EXACT_FIXED_DEPTH_PROGRAM.md) states the
  model, forward/reverse ordinary-series recursion, normalization, audit
  evidence, and current proof boundary.
- [`finite_width_jet.py`](./finite_width_jet.py) implements the full nonlinear
  feature-ascent ODE through order three.
- [`raw_coordinate_jet_audit.py`](./raw_coordinate_jet_audit.py) independently
  differentiates the original raw network through third order for tiny exact
  checks.
- [`audit_h1_control.py`](./audit_h1_control.py) reproduces the independent
  generic-activation `H=1` Gaussian-quadrature/finite-width control.
- [`audit_h3_nonlinear.py`](./audit_h3_nonlinear.py) reproduces the
  independent nonlinear `H=3`, `B=1` finite-width campaign.
- [`test_exact_depth_program.py`](./test_exact_depth_program.py) contains the
  seedwise specialization, singular-Gram, depth, batch, and homogeneity gates.
- [`DEPTH_B1_GAUSSIAN_RECURSION.md`](./DEPTH_B1_GAUSSIAN_RECURSION.md) is a
  separate analytic one-sample recurrence, including the preferred fully
  contracted one-dimensional-atom form.
- [`gnf_audit_reference.py`](./gnf_audit_reference.py) is an independently
  derived scalar contraction, and
  [`test_gnf_audit_reference.py`](./test_gnf_audit_reference.py) cross-checks
  it through `H=4` against the four-Gaussian proof IR.
- [`DEPTH_B1_HOSTILE_AUDIT.md`](./DEPTH_B1_HOSTILE_AUDIT.md) records the
  response, parity, normalization, reduction, probability, and nonclaim
  ledger.
- [`DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md`](./DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md)
  is the audited joint recursion for arbitrary separately fixed \(H,B\).
- [`DEPTH_FIXED_BATCH_HOSTILE_AUDIT.md`](./DEPTH_FIXED_BATCH_HOSTILE_AUDIT.md)
  independently checks its matrix chronology, parity closure, terminal
  contractions, literal atom bound, probability bridge, and MSE map.
- [`FIXED_H_FIXED_B_GNF_TEMPLATE.md`](./FIXED_H_FIXED_B_GNF_TEMPLATE.md) is
  the separately written matrix-lift derivation used as an additional
  orientation/response witness.
- [`fixed_batch_polynomial_reference.py`](./fixed_batch_polynomial_reference.py)
  and [`audit_h3_b2_joint_nonlinear.py`](./audit_h3_b2_joint_nonlinear.py)
  provide exact polynomial and independent finite-width joint gates.

The deterministic analytic evaluator is `gnf_recursion.py`; its
`test_gnf_recursion.py` gates cover the base depth, the accepted \(H=2\)
normal form, and the deep-linear family.

Run the deterministic audit with

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.depth.run_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.depth.run_fixed_batch_gates
```

Current executable status: **accepted finite-width control**.

Current analytic status: **proved for arbitrary separately fixed \(H,B\)
under the polynomially-smooth activation envelope**.  The \(B=1\) recurrence
has an independent scalar contraction through \(H=4\), while the joint
recursion has exact reductions on both axes and a genuinely nonlinear
\(H=3,B=2\) audit.  Regimes with \(H=H(n)\) or \(B=B(n)\), uniform error
bounds, flat-expansion complexity, and fixed-positive-time convergence remain
separate obligations.
