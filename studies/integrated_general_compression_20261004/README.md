# General dense, Legendre, and autonomous-compressor comparison

Started 2026-10-04 at the user's explicit request for a **new study**.
The user expressly authorizes borrowing relevant proofs, notes and arguments
from all previous studies. That source-access authorization does not promote
their claims or remove the need to verify interfaces and corrections.

## Fixed research contract

The task is a merged general theorem for arbitrary fixed hidden depth
L>=2, finite sphere training data with positive limiting top-feature Gram
gap gamma, arbitrary signed fixed small labels, canonical Gaussian dense
initialization with exactly zero readout, and the original mean-loss
mobilities (n,1,...,1,n). Activations may differ across layers; they are real
on R, holomorphic on a common strip, and have bounded derivative there.
Their VALUES MAY BE UNBOUNDED. No orthogonality, special label pattern,
clipping, frozen features, or additional unproved response hypothesis may
replace this scope.

The three comparisons are separate: compact autonomous versus its realized
dense run, independent dense versus dense, and original residual-RMS-clock
Legendre closure versus its realized dense run. All use equal physical
time and the norm sup over t in [0,infinity], including fitted endpoints,
and every query on ||x||=sqrt(d). Target rate is strict C/sqrt(n), with
explicit data/activation/depth/dimension/confidence dependence. Near-root
is not silently identified with root. The general Legendre order target is
n^(1/4+o(1)); the special one-sixth theorem is unnecessary.

The compact retained-state target has depth-independent logarithmic power
3d+2, actual label RMS Y visible in its size coefficient, and full accounting
of moving state, fixed coefficients, metrics, data and caches. Legendre's
moving and fixed-mixer storage must be reported separately. Improve
constants separately when supported; do not force three equal prefactors.

The preceding conversation proposed numerical envelopes involving
beta_partial^(-62L), beta_partial^(124L), and beta_partial^(82Ld).
Those were explicitly labeled **conjectural benchmarks**, not proved
unbounded-activation constants. Their validity is an obligation here, not
an imported theorem. The same is true of the sharp unbounded source radii
and strict-root independent-dense bound. No prior chat assertion is a proof.

Supporting tasks are bounded: reuse or derive an easy initialized/early-time
dense lower calibration, then obtain epsilon/state corollaries algebraically.
Do not spend the main effort on special cases or endpoint lower bounds.
Do not start an experimental campaign. Do not edit the manuscript or book.

## Work and source ownership

Coordinator owns this README, the canonical merged statement and proof
assembly, deterministic general fitting/constants, and final checks.
Scoped agents own disjoint files for the general independent-dense bridge,
sharp unbounded analytic-source/runtime bridge, and general Legendre
constants transfer. Their source scopes and exact coverage will be recorded
with their reports. All source claims remain internally checked research
unless separately promoted by the established workflow.

Initial source chain: closure_sampling_20261003 (general analytic compressor,
unbounded extension, spherical/source/runtime refinements, integrated
variability notes) and dense_cutoff_population_rate_20261001 (general
small-label joint budgets, tracking and self-averaging). Other studies may
be used when they supply an actual needed proof, under the user's new
authorization. Avoid broad unrelated reading.

## Repository state and current status

Startup HEAD: 4dfa5c1ef2c5b920eda2bbc84316b189b97da92e. Index empty.
Preexisting tracked changes to paper/main.pdf and
studies/structured_full_rank_scalar_20260926/README.md are not ours.
Numerous existing untracked studies are preserved. No Git mutation.

## Results and current proof boundary

The latest comparison-coefficient refinement is
[SAMPLE_POLYNOMIAL_STATEMENT.md](SAMPLE_POLYNOMIAL_STATEMENT.md), checked
in [SAMPLE_POLYNOMIAL_CHECK.md](SAMPLE_POLYNOMIAL_CHECK.md).
It removes sample/gap factors from the dense-copy and Legendre exponential
width factors while retaining actual label dependence polynomially.
The new step preserves the negative residual-discrepancy square in
parameter energy; convexity then moves the remaining activity dependence
outside the exponential. The label condition, activation/depth/data
scope, original physical clock, all-query norm and source event are unchanged.
The dense rate remains near-root. Legendre still attains Y/sqrt(n)
with order n^(1/4+o(1)), now with polynomial data dependence in the
displayed order prefactors and a quarter-log inversion.

Complete derivations are DENSE_SAMPLE_EXPONENT_REFINEMENT.md and
LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md. The latter explicitly checks
that terminal projection tails control the absolute integrated physical
defect, as required by its new forced energy argument.
COMPACT_SAMPLE_EXPONENT_REFINEMENT.md improves the compact comparison's
displayed width cost and keeps Y explicit, but does not remove its
exponential data dependence. It identifies the limitation of the current
positive-coefficient comparison and a separate exponential source gate;
neither is an intrinsic model lower bound. The source probability
threshold remains unquantified. No experiment or manuscript edit was made.

Start with [RESULT.md](RESULT.md) for the assembled scope, numerical
definition map, three separate comparisons, probability qualifications,
onset calibration, and accuracy/storage consequences.

For the user's requested low-notation statement, see
[SIMPLE_EXPLICIT_STATEMENT.md](SIMPLE_EXPLICIT_STATEMENT.md). It replaces
the long numerical recurrences by conservative explicit powers of one
activation envelope and one data/depth coefficient. The common sufficient
label cap is `Y <= (gamma/m) beta^(-30L)`; the exact recurrence allowances
remain available in RESULT.md. Its finite-envelope derivations are
`SIMPLE_CONSTANTS_SOURCE_CHECK.md`, `SIMPLE_CONSTANTS_DENSE_CHECK.md`, and
`SIMPLE_CONSTANTS_LEGENDRE_CHECK.md`. The dense-copy coefficient retains
an explicit factor Y by integrating the initially zero readout difference.
The strict dense-copy rate and effective stochastic width threshold remain
open; the simpler statement does not remove those limitations.
Its confidence audit explicitly includes the unquantified threshold
`n >= N_0(delta)` in the Legendre applicability condition and compact
width inequality. At fixed width, the order/error/storage formulas remain
unchanged; the numerical compact threshold alone supplies no certified
confidence. Source moment order is proof-only and does not enter storage.

The requested general strict-root three-comparison theorem is **not yet
proved**. In particular the inherited general independent-dense theorem
has a subpolynomial width loss; its strict-root replacement cannot be
obtained by substituting constants from the compression proof. The actual
remaining issue is the transported mixed response, not a restriction to
tanh, two layers, orthogonal data, or bounded activation values.

- `GENERAL_EXPLICIT_FITTING.md` and `GENERAL_EXPLICIT_FITTING_CHECK.md`:
  checked explicit dense initialization, fitting, global convergence and
  sphere endpoint tail. Values may be unbounded; no forward normalization
  is assumed. Exact moment constants give the label cap, with the simpler
  sufficient envelope `Y <= (gamma/m) beta_partial^(-5L)`.
- `GENERAL_EXPLICIT_CLOSURE_FITTING.md` and
  `GENERAL_EXPLICIT_CLOSURE_FITTING_CHECK.md`: checked explicit fitting
  and convergence for **every** original RMS-clock Legendre order. The
  approximate energy estimate closes the readout bound despite the
  non-gradient reconstruction defect. A sufficient simplified cap is
  `Y <= (gamma/m) beta_partial^(-10L)`.
- `GENERAL_LEGENDRE_TRANSFER.md`: full general inherited same-width
  comparison, explicit near-quarter order schedule, and numerical
  deterministic tracking interface. The new closure fitter supplies its
  physical constants; the trained carrier probability event is a distinct
  input supplied by the source argument.
- `EXPLICIT_LEGENDRE_COMPARISON.md` and its `_CHECK.md`: checked numerical
  assembly and concrete order giving error `Y/sqrt(n)` in the full norm,
  with `q_n=n^(1/4+o(1))`. Fixed initialized mixers remain quadratic.
- `UNBOUNDED_COMPRESSOR_BRIDGE.md`: new samplewise joint-budget and sharp
  complex-source bridge. It preserves the `3d+2` storage logarithmic
  exponent and actual `Y^4` leading storage dependence, with numerical
  recurrences. `UNBOUNDED_COMPRESSOR_BRIDGE_CHECK.md` checks source §§1–12.
  Section 13 adds a fully numerical deterministic comparison and explicit
  deterministic width/error trade; its separate check is
  `UNBOUNDED_COMPARISON_CHECK.md`. The probability proof still gives an
  eventual, unquantified stochastic width threshold.
- `EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md` and its `_CHECK.md`: exact autonomous corrected
  optimizer, explicit small-label fitting and sphere endpoint tail for
  unbounded activations; independent reconstruction passes.
- `GENERAL_DENSE_COMPARISON.md`: corrected audit and new mixed-response
  calculations. Existing source estimates do control instantaneous
  cross-query responses. The adjoint training projections have backward
  damping. The full transported neuronwise mixed moments, valid Gaussian
  localization and query increments remain open. This is not evidence of
  a slower-rate counterexample. Equations (37)–(44) give a numerical
  all-time whole-sphere near-root bound with all multiplicative constants
  specified by finite recurrences.
- `EARLY_VARIABILITY_AND_STORAGE.md`: proved general initialized Gram
  fluctuation recursion and onset derivative calibration; exact storage
  algebra with separate comparison constants. It explicitly does not turn
  an onset derivative into a fixed-label endpoint lower bound, or a
  requested comparison shape into an established theorem.

Checks here are internal reconstructions, not promotion reviews. No
manuscript, maintained-book, earlier-study, or Git-index changes were made.
