# Minimal dictionary closures with hidden feature learning

This new study investigates the user's explicitly requested weaker closures,
with smaller dictionaries than canonical p=1. It is not an exact reduction
or an approximation theorem for the full p=1 trajectory.

## Contract

Use two tanh hidden layers, inputs x in sqrt(2) S1, physical time, unhalved
probability-weighted square loss, initial w=g~N(0,I2), and zero population
readout. Retain the same gradient metric and actual transpose/scalar reverse
action. The authorized change is to retain fewer initialized dictionary
features, with their exact Gaussian contractions and eta=1/4096 normalization.
Any selected input direction is fixed before evolution. No future path enters
the coefficients. No simulations, network limits, or promotion are planned.

Scientific inputs: established docs/NOTATION.md, docs/observable_p1.md,
docs/global_nonlinear.md finite Gaussian source rule and C.4.7.10.B/C.1/C.3.
The established reading guide and required skills were read in this task;
their hashes were checked unchanged. No other study is a research input.

## Results and evidence

The complete argument is [minimal_closures.md](minimal_closures.md).

- A scalar dictionary on each side, selected from the matched initialized
  forward probes, gives a nontrivial closure with scalar M. Its exact
  initialization and physical gradient equations are in Sections 1--2.
- Both hidden activations move and loss converges exponentially for the
  explicit balanced reflected opposite-label pair in Section 4, including
  non-antipodal inputs. The fixed-direction model covers an entire family;
  selecting the direction from the data covers every distinct balanced
  opposite-label pair. This is a changed closure, not canonical p=1.
- The scalar model's initial upper Gram is positive definite for any finite
  input list whose selected projections are nonzero and distinct up to sign.
  For distinct non-antipodal inputs all but finitely many directions qualify.
  This guarantees initial descent, not eventual fitting for arbitrary data.
- A fixed scalar probe can also yield a stationary nonfitting trajectory on
  compatible data. Section 5 preserves this limitation, including a case
  exactly representable by the same closure at another state.
- A (2,2) forward-only dictionary uses 2D/2D characteristic grids and has
  positive definite initial upper Gram for all distinct non-antipodal input
  lists, without selecting a direction from the data (Section 6).
- (1,1) is the smallest positive dictionary size in this factorized
  architecture. Its generic grids are 2D/1D; a scalar lower mark does not
  remove the two-dimensional Gaussian initial weights (Section 7).

Status: **internally checked by the author**, with analytic scope/edge-case
audit in [validation.md](validation.md). No independent review, experiments,
network approximation claim, or promotion. Relevant source and artifact
hashes are in [manifest.sha256](manifest.sha256).

## Reproduction, limitations, and ownership

Reproduce by following the complete derivations from the established sources
listed above. The check is analytic; there is no simulation to rerun. From
the repository root, `sha256sum -c studies/minimal_feature_closure_20260917/manifest.sha256`
checks the exact input/artifact snapshot (later shared-source edits may
legitimately change its outcome).

Open: long-time fitting for arbitrary data in either smaller closure;
quantitative comparison with canonical p=1; numerical grid accuracy and cost.
No global optimum over all conceivable compressed architectures is claimed.
The current construction and explanation request is complete. Further research
or implementation requires a new user direction; these gaps do not authorize
a numerical campaign.

Owner and checker: current primary agent only. Study-owned flat files only;
no edits to established material, staging, or commits.
