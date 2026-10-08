# Gate-continuation instrumentation: bounded static check

2026-10-07. This check was stopped when the user redirected the investigation
to full causal-system tests with more training samples. It records the static
inspection already completed; no further phase-3 test, experiment, or derivation
was undertaken after that instruction. The main checker launched no numerical
test. This is not a completed numerical instrumentation audit.

Allowed and inspected scientific inputs were `gate_continuation_experiment.py`,
the unchanged `dense_learning_experiment.py`, and
`PASSIVE_NONLINEARITY_DIAGNOSTICS.md`. No implementation file was modified.

The inspected SHA-256 values were:

| File | SHA-256 |
|---|---|
| `gate_continuation_experiment.py` | `2429f91d323f64491763f8aab62c932db20c00a417a09a34efca135059332ed1` |
| `dense_learning_experiment.py` | `58d566adc2898a49389c73d659147dd98d39b4eab0c24aaba444dbc91d8a7942` |
| `PASSIVE_NONLINEARITY_DIAGNOSTICS.md` | `09a4f20f43fbd152471d2ec40be9c00cc67a957a95fad5261dc13fb02a19eb8c` |

No implementation defect was identified in the completed static inspection.
The following findings delimit what the saved outputs mean.

## Predictor provenance and numerical quadrature

`simulate` constructs `initial_directions` from the zero-readout initialization,
computes the population clock constants, solves the autonomous cubic clock,
and evaluates both the 32-point and 64-point continuation predictions before
entering the dense-training loop. Consequently `prediction_autonomous` uses
initialization data, fixed labels, and its autonomous clock; it does not use
future dense states or a fit to their outputs.

The frozen direction uses the initial finite matrices, including the forward
and transpose products through the same initialized middle matrix. It is not
a newly sampled independent return. The coefficient arrays are therefore
initialization-only, but realization-dependent. The passive predictor combines
those finite-initialization defect coefficients with the population cubic
clock; it is not itself a deterministic exact population evaluation.

`population_constants` uses 160-point Gauss-Hermite quadrature for Gaussian
expectations. `continued_fields` uses Gauss-Legendre quadrature on the internal
coordinate interval from zero to the supplied clock value for the readout
integral. The saved 32-versus-64 discrepancy concerns the latter quadrature.
It does not check the Gaussian quadrature, the population-limit approximation,
the frozen displacement direction, or the cubic clock. Those accuracy claims
must not be inferred from a small saved `quadrature_error`.

All three compared autonomous outputs share the same geometric term and
clock. Their defect terms are, respectively, the finite linear-plus-cubic
polynomial, the product of the quadratic feature and cubic readout
polynomials, and full tanh evaluation along the frozen quadratic preactivation
displacement with its integrated readout. The polynomial-product control
retains its induced fifth-degree cross term. It is not a complete fifth-order
network expansion.

The source's built-in `self_test` checks initialized parameter accelerations,
the polynomial defect identity, and its finite cubic energy identity. The
main checker did not execute it before the task redirection. Merely having
these assertions in the source is not evidence that they passed in this audit.

## Measured-clock and projection outputs are diagnostics

Let \(s\in\{-1,1\}\) be the training-label sign and
\(u_a(t)=\int_0^t[y_a-f_a(\tau)]\,d\tau\) the companion deficits from the
dense run. `observe` uses the measured mode clock
\(u=(u_1+s u_2)/2\), and records the other accumulated mode
\((u_1-s u_2)/2\). The arrays under `prediction_measured_clock` are therefore
diagnostic evaluations at a measured coordinate. They are not the autonomous
predictions saved under `prediction_autonomous`.

For each layer and sample, `displacement_diagnostics` projects the actual
preactivation displacement onto that sample's initialized acceleration vector.
The coefficient is its empirical inner product with the direction divided by
the direction's squared empirical norm. The code uses zero when that norm
vanishes and reports zero cosine at a vanishing norm. These are reporting
conventions, not defined mathematical cosines in the degenerate cases.

The projected upper features apply tanh to the initialized preactivation plus
this observed projection. Their errors are then contracted with the actual
dense readout. Thus the projected arrays use both current dense displacement
and current readout. They measure how much output-relevant feature error
remains after allowing a separate fitted displacement coefficient for each
sample. They are not a predictive continuation or a single fitted common clock.
The module header calls them oracle diagnostics, consistent with their data
dependencies. A best Euclidean preactivation projection also need not minimize
the nonlinear, readout-weighted output error.

## Which discrepancy the saved splits reconstruct

Write \(\langle a,b\rangle_n=a^\top b/n\), and let
\(\widehat h_a,\widehat w\) denote the auxiliary continued features and
readout evaluated at the measured mode clock. Their raw output is
\(\widehat f_a=\langle\widehat w,\widehat h_a\rangle_n\).
The saved `error_split_f` uses the exact algebraic identity

\[
f_a-\widehat f_a
=\langle w,h_a-\widehat h_a\rangle_n
 +\langle w-\widehat w,\widehat h_a\rangle_n.
\]

This split concerns the raw auxiliary continuation. The final geometric-plus-
defect predictor is a different quantity. Let
\(\lambda=(2,1)/\sqrt5\),
\(\varepsilon=f_3-\lambda_1f_1-\lambda_2f_2\),
\(\widehat\varepsilon=\widehat f_3-\lambda_1\widehat f_1-
\lambda_2\widehat f_2\), and \(F(u)=\nu u+\kappa u^3\). The predictor is

\[
\widetilde f_3(u)=\frac{2+s}{\sqrt5}F(u)+\widehat\varepsilon(u).
\]

Accordingly, its complete error at the measured clock is

\[
f_3-\widetilde f_3(u)
=\left[\lambda_1f_1+\lambda_2f_2-rac{2+s}{\sqrt5}F(u)\right]
 +[\varepsilon-\widehat\varepsilon(u)].
\]

`error_split_defect` correctly decomposes the second bracket. The first
bracket must also be retained when reporting the full hybrid-predictor error.
At finite width it includes departures from training-mode symmetry as well
as disagreement with the cubic training curve. Applying the raw output split
to the hybrid predictor without this distinction would mislabel the error.

The source explicitly checks the raw and defect split identities through its
saved `identity_error`. This inspection did not independently evaluate those
identities on a numerical trajectory. No claim about the full campaign's
results, improvement from continuation, or all-time accuracy is made here.
