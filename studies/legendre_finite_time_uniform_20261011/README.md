# Finite-time Legendre compression uniform in width

Started 2026-10-11. This is a new theoretical investigation requested by the
user, not a modification of the paper or established book.

## Contract

Extend the actual autonomous, original residual-clock Legendre closure to
arbitrary fixed depth, finite training data, and the compact paper's layerwise
strip-analytic activations with bounded derivatives (activation values may be
unbounded). Labels are arbitrary fixed finite values, with no small-label cap.
The desired comparison is the supremum over physical time in every prescribed
finite interval [0,T] and over the input sphere, against the same-initialization
canonical dense gradient flow, with zero readout and Gaussian hidden weights.
The target is an error C_T/q^2, or an explicitly identified weaker rate if that
cannot be proved, with constants and sufficient order independent of width.
Confidence dependence must be stated. No vanishing width floor, width-first
limit, oracle history, clipping of the actual dynamics, changed clock, or
width-dependent initialization cap may be substituted for that target.

The request to extend the previously identified theorem authorizes the relevant
proofs and corrections in response_memory_width_uniform_20260927 as scientific
inputs. The paper's compact setup and Legendre construction specify the current
model. Established docs/ are also available. No other study is imported.

## Work and evidence

Root owns synthesis and this README. Separate scoped routes will investigate
finite-time stability/energy, Gaussian-tail control, and adversarial obstructions.
All routes use fresh contexts and explicitly bounded inputs. No experiments,
paper edits, book edits, or Git mutations are authorized by this study.

## Current mathematical status

The requested general nonlinear prediction-tracking theorem remains **open**.
No counterexample to the specified Gaussian prediction claim was found. The
earlier one-input, two-hidden-tanh-layer theorem is an input, not evidence that
all its hypotheses can be removed.

- [ENERGY_ROUTE.md](ENERGY_ROUTE.md) proves finite-time existence, bounded
  physical parameters, accumulated absolute velocity defect at most C_T/q, and
  total positive loss variation at most C_T/q. These hold without small labels,
  at arbitrary fixed depth and data size, for unbounded-value bounded-slope
  activations, with one sufficient order independent of width and one Gaussian
  confidence event independent of order. The full constants and exact unchanged
  construction are given there. Root reconstructed the energy argument and read
  the complete fresh isolated [ENERGY_CHECK.md](ENERGY_CHECK.md): PASS for these
  partial claims and the affine boundary case. Its explicit Gaussian-law and
  confidence-range clarification was incorporated and rechecked; the accepted
  proof hash is
  `0b51956f9782c02fff67476929f87078c9115af1819a9b25d92a5ecfd082886d`.
  This is internal checking, not promotion or a check of an unproved tracking claim.
- [ADVERSARIAL_ROUTE.md](ADVERSARIAL_ROUTE.md) proves exact readout/clock bounds
  and Gaussian examples distinguishing diverging carrier maxima or curvature
  rates from failure of compression. These are proof-route diagnostics, not
  counterexamples to the prediction target. Root read and reconstructed them.
- [GAUSSIAN_ROUTE.md](GAUSSIAN_ROUTE.md) derives a conditional all-width bound
  C q^-2 sqrt(log(e+q)) exp(C sqrt(log(e+q))) from uniform Gaussian-type RMS
  cutoff tails for the actual finite dense backward carriers. Root read and
  reconstructed its conditional comparison. The required probability estimate
  for those trained carriers remains unproved, and the exact q^-2 exponent is
  not established even by that conditional estimate. Population-only tails or
  qualitative width floors do not satisfy this missing premise. A weighted
  Gaussian derivative route and a comparison at equal values of each system's
  own clock are recorded only as unfinished proposals.

The energy result does not compare predictions with dense training. The two
remaining bridges are uniform backward-history regularity and uniform stability
of the actual approximation error. Ordinary operator/RMS bounds do not supply
either product estimate. The affine-activation q^-2 boundary case is recorded,
but was already implicit in the older finite-time theorem and is not a new
general nonlinear extension.

The general nonlinear claim is not falsified by either the energy or adversarial
route. In particular, large Gaussian coordinate maxima are not a counterexample:
the adversarial note includes an actual Gaussian trajectory with diverging maxima
and identically zero compression error. The unresolved comparison must exploit
the actual error/source structure rather than simply substitute a maximum norm.

No training experiments were run and no paper, established book, implementation,
or Git index was changed. A limited external literature search was exploratory;
no external theorem was imported to fill the remaining gap.

Startup HEAD: ef8362764b4eb8144d7af8d6f8db080fdaaf82ca. Existing unrelated
modified and untracked artifacts were observed and will be preserved.
