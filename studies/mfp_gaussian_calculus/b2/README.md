# L=2 fixed-batch directional stage

This subtree began as the two-input stage.  Its array equations and executable
oracles now accept an arbitrary fixed batch size; the two-input channels remain
the primary named audit case.  The exact finite-width target is

```text
g_c = c^T f,              D_c = n grad(g_c).grad,
C_n,c = D_c^3 g_c,
```

with an arbitrary deterministic fixed-dimensional vector `c` and matching PSD
input Gram `Q0`, together with an independent exact-polynomial evaluator for the fully
contracted Gaussian normal form.  The maintained mathematical GNF
and response audit now pass the promotion gate under polynomial smoothness;
the reference evaluator alone is not a theorem.

Artifacts:

- `FINITE_WIDTH_DIRECTIONAL_PROGRAM.md`: derivation and fixed Tensor Program;
- `finite_width_directional.py`: direct contraction evaluator, the two extra
  frozen MSE response scalars, and the exact residual-dependent loss jet;
- `finite_width_jet.py`: independent order-three Taylor propagator;
- `raw_coordinate_jet_audit.py`: third-order multivariate differentiation of
  the original raw network, independent of both directional programs;
- `model.py`: fixed-batch initialization and the named two-input
  equal/opposite channels;
- `test_finite_width_directional.py`: seedwise equality and structural gates;
- `contracted_gnf_polynomial_reference.py`: independent exact Wick evaluator
  after all auxiliary Gaussian fields have been contracted;
- `test_contracted_gnf.py`: exact constant/linear controls, one-input
  reduction, and the accepted quadratic two-input campaign gate;
- `B2_GAUSSIAN_NORMAL_FORM.md`: closed generic-activation GNF;
- `B2_FINITE_WIDTH_AUDIT.md`: hostile finite-width/GNF audit and the complete
  arbitrary-label local MSE mapping.

The named channels are unnormalized:

```text
c_plus  = (1,  1)
c_minus = (1, -1)
```

For a frozen average-MSE label contraction use `c=y/B`.  For the exact
finite-width residual-dependent cubic loss jet, including the full NTK-cube
and both additional response terms, call `mse_loss_third_derivative` with
the unscaled label vector `y`.

Run:

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.b2.run_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.b2.raw_coordinate_jet_audit
```

Expected terminal line:

```text
PASS 12 fixed-batch checks
PASS 8 feature, 4 response, and 4 MSE independent raw-coordinate
third-jet checks; worst scaled error=1.239e-14
```
