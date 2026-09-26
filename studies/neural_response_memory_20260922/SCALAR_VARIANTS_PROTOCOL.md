# Controlled search for accurate scalar predictions

2026-09-25. Explicitly authorized by the user's request for theoretical and
empirical alternatives after the direct-point failure. Frozen before candidate
implementation or scientific runs. This is continuation of the same scalar
compression investigation, with distinct approximation families labelled below.

## Fixed experiment and decisions

Use width16, three hidden tanh layers, seed20260920, canonical mobilities
(n,1,1,n), normalized active circle angles10/125 degrees, labels+1/-1. Primary
passive angles are30,60,90 degrees, chosen before any candidate output is run.
They have zero training weight and never enter the residual, normalization,
clock, basis selection or training-gradient directions. All comparisons use
the same actual initialized matrices. Dense outputs are validation only;
no candidate coefficient is fitted to a future dense trajectory or test output.

Primary criterion: training RMS<=sqrt(.001), RMS over the three fitted passive
outputs <=.05 versus the fitted dense reference, and maximum passive error<=.10.
RMS>=.10 is a failed accuracy witness. Intermediate errors, failed integration
or resource caps are reported separately. Also compare common-time outputs,
record the entire training/point trajectory on a fixed temporal panel, and
report state dimension, fixed coefficient storage and all preparation/runtime
costs. A small final training loss is not itself a fidelity result.

H1: improving boundary treatment or choosing a different reduced basis restores
accurate passive predictions at a manageable scalar dimension. H0: missing
nonlinear correlations/basis motion remain too large. The previously failed
zero-tail K5 witness is retained as the reference failure, not deleted from the
record. This is a development comparison of a finite predeclared family, not
a statistical guarantee over random initializations/tasks.

## Candidate families

1. **Boundary approximations of the existing P1 tree hierarchy.** Test K=3 and5
   with (a) omitted connected factors frozen at exact initial contractions;
   (b) omitted factors approximated by their initial value plus their exact
   initialized residual/clock directional derivatives. The latter adds two
   residual accumulators u_a'=r_a and uses L-1 for the clock integral. Keep
   all factors of a generator term after boundary substitution; register
   exposed factors within K. Prune only structural exact zeros (frozen
   boundary contains A, or tangent boundary contains at least two A factors).
   No value-threshold pruning or clipping invented after seeing results.
   Frozen boundaries should recover exact initial retained velocities;
   tangent boundaries should also match initial second derivatives when
   residual RMS is nonzero. This does not assert long-time accuracy.

2. **Fixed response-basis Galerkin model of dense GF.** Test ranks4,8,12 and
   full-rank16 as an implementation control. Select each layer's basis solely
   from initial active responses, backward fields and initial response
   velocities, including the constant field, with deterministic rank completion.
   Normalize Q^T Q/n=I. Precompute initialized operator projections and cubic
   field-product tensors. Runtime evolves only modal response/readout vectors
   and reduced weight-update matrices; no population or neuronwise nonlinear
   evaluation. Use explicit projected products, not a claim of exact Galerkin
   integration of the entire composed vector field. Retain first-layer update
   coefficients too, allowing a terminal dense decoder from initial weights
   and fixed bases. Assess both internal passive outputs and this decoder's
   actual outputs. Full rank recovers the dense response lift and is not a
   compressed success. This family does not use a P-order history closure.

3. **Gradient flow of an initial polynomial output potential.** Whiten parameters
   by the canonical mobility. Initial gradient directions span rank<=2; enrich
   by H_i g_j to rank<=6, using only active inputs. Test (rank2,degree1),
   (rank2,degree2), (rank6,degree2), (rank6,degree3). Rank2/degree1 is the honest
   frozen-NTK control. Higher degrees have a changing positive semidefinite
   kernel and exact loss dissipation for their approximate potential. Compute
   coefficient jets analytically at initialization, not by fitting a dense
   trajectory. Runtime retains only z and fixed scalar polynomial tables.
   Save the fixed parameter basis separately for terminal decoding of
   theta0+D^(1/2)Qz; score both polynomial and decoded-network predictions.
   Quadratic/cubic enriched models should match initial dense passive velocities
   through second order. Their finite-time errors still depend on subspace
   leakage and polynomial remainder. This is a new approximation family, not
   a repaired proof for the old moment truncation.

The anchored recursive-factorization tail idea is a reserve theoretical design,
not an automatic additional run. Its split dependence needs a separate protocol
if the present bounded ladder is inconclusive. No seed/geometry/label tuning,
new cutoff search, fitted damping or future-reference coefficient calibration.

## Numerical validity and resource limits

Use float64 adaptive DOP853, horizon40, target MSE.001, rtol1e-7/atol1e-9.
Each fit has120s, state cap1e8 and a nonfinite-state stop. Each candidate's
preparation has180s and3GiB RSS; tree variants additionally cap live patterns
at12000, boundary patterns at50000 and retained terms at5000000. Any exceeded
limit is recorded and that cell stops, without a changed cap. Algebra checks
must pass before interpreting an experiment: initialized output/velocity,
passive independence, normalization, table-only runtime, and each family's
stated exact properties. Full rank is the response-basis oracle control.

Scientific phase budget:1800 summed process seconds, with at most three single-
thread CPU workers in parallel, and a hard30-minute elapsed campaign ceiling.
Each route owns its own cells/logs and enforces its caps; the root stops further
cells when the cumulative budget cannot accommodate them. Algebra development
checks have a separate300 CPU-second total budget. Report preparation failures
and negative cells; do not present only the winner.

Refine the best completed variant in each family at rtol1e-9/atol1e-11 once;
refine the dense reference once. If a family's best variant fails numerically,
its accuracy result remains inconclusive. Output changes must be<=.002.
No broader tolerance sweep. Rank16 agreement with dense must be<=1e-5.

## Predeclared validation branches

If at least one genuinely reduced candidate meets the primary accuracy gates,
select the smallest moving state among passing variants (ties: lower passive
RMS). If any passing variant also has a valid decoder, select within that
subset first. Valid decoder means actual decoded-network training RMS<=.05,
primary passive RMS<=.05 and maximum error<=.10; these are separate from the
internal-output gates. This selection clarification is frozen before any new
candidate fit. Test the selected variant on five additional passive angles0,150,210,270,330 degrees, with
unchanged scientific coefficients and controls. Selection uses the primary
panel only; report this new panel separately. For a parameter-decoder candidate,
also evaluate its decoded network on4096 circle angles; this is evaluation,
not training on a mesh. If its internal output and decoded network disagree,
report that gap rather than silently switching readouts.

If the selected variant has a valid whole-network decoder and passes the
additional panel, repeat that unchanged variant at width32 with the same seed
and task (one matched new dense reference). This checks whether success was
merely full-dimensional representation at width16. No hyperparameter changes
after this width check. Failure of the branch is retained alongside success
on the original width. Stop after these branches regardless of outcome.

## Evidence and ownership

New sources remain flat in this study; products use fresh
data/generated/neural_response_memory_20260922/scalar_variants01/ subdirectories.
Save initialization provenance, config/source hashes, original states,
coefficients, raw outputs, failures and summaries. Root owns shared protocol,
reference/analysis runner and report. tail_closure_design owns scalar_tail_engine.py;
spectral_scalar_design owns scalar_response_basis.py; kernel_scalar_design owns
scalar_polynomial_potential.py. Scoped implementation checks and separate
cross-checks do not constitute promotion. No maintained code/book changes.
