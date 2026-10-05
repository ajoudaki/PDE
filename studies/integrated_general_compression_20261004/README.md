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

The latest request is to integrate **only general** lower results into
the common theorem. This is done in
[RESULT.md](RESULT.md) §6 and
[SAMPLE_POLYNOMIAL_STATEMENT.md](SAMPLE_POLYNOMIAL_STATEMENT.md) §6.
The complete new statement is
[GENERAL_VARIABILITY_LOWER_RESULT.md](GENERAL_VARIABILITY_LOWER_RESULT.md).
For every fixed admissible dataset with \(m\ge2\), arbitrary nonzero
signed labels in the existing allowance, arbitrary fixed depth and the
same possibly unbounded analytic activation class, the common trajectory
norm is at least
\(c_{\phi,L,\delta}Y\sqrt\gamma/[\sqrt n\,\log(en)^{5/2}]\)
with any fixed eventual confidence. No orthogonality, centered covariance
gap or additional variance hypothesis is needed. The recurrence-based
label allowance is retained; the simpler beta cap makes its coefficient
particularly explicit.

The key new moment inequality is distribution-free:
\(\operatorname{tr}\operatorname{Cov}(H(y^\top H))
\ge\gamma^3q_L\|y\|^2/(16\mu_4)\).
Positive uncentered feature rank prevents every label-weighted feature
product from being deterministic. The initialized Gram CLT then supplies
onset variability. A rerun of the source proof for a finite query set
removes the spatial mesh factor from its complex-time radius. A
Chebyshev derivative inequality converts onset into an actual-prediction
lower bound, preserving the physical training timescale.

The unchanged compact model already has error smaller than this
lower scale. Legendre does too after multiplying the latest order by
\(\log(en)^{3/2}\); its moving-state exponent stays \(5/4+o(1)\).
For each fixed admissible task, both compression-error / actual-dense-
discrepancy ratios tend to zero in probability in the same all-time,
whole-sphere norm. This calibrates the compression against actual
variability, without relying solely on its upper bound.

Proofs: [GENERAL_INNOVATION_LOWER.md](GENERAL_INNOVATION_LOWER.md),
[GENERAL_ONSET_NONDEGENERACY.md](GENERAL_ONSET_NONDEGENERACY.md), and
[GENERAL_TRAJECTORY_LOWER_BRIDGE.md](GENERAL_TRAJECTORY_LOWER_BRIDGE.md).
The quantitative moment argument was reconstructed separately by two
scoped agents; the trajectory bridge has a separate
[internal check](GENERAL_TRAJECTORY_LOWER_BRIDGE_CHECK.md).
The coordinator owns the integration and final
[consistency check](GENERAL_VARIABILITY_LOWER_CHECK.md).
These are internal checks, not promotion reviews.

The lower witness is at a training input at a positive time that can
shrink with width; no general endpoint lower is proved. The upper and
lower width exponents agree, but sharp sample, conditioning and dimension
dependence remains open. One-sample deterministic exceptions and zero
labels are expressly excluded from the positive statement. Width
thresholds are not effective, and no joint growing-data limit is asserted.
No experiment, manuscript/book edit, or Git-index mutation was made.

The preceding, separately scoped endpoint investigation is retained in
[ENDPOINT_LOWER_RESULT.md](ENDPOINT_LOWER_RESULT.md). It contains actual
fixed-label fitted-endpoint results, beyond the earlier onset derivative:

- Two tanh hidden layers, general correlated training data spanning a
  proper input subspace: at any fixed orthogonal unseen query, the
  endpoint discrepancy is at least
  `c sqrt(y^T Q^(-1) y / n)` with a fixed positive probability.
  The existing integrated label allowance suffices. For labels in the
  weakest covariance direction, or all label directions on orthogonal
  data, its scale is `Y sqrt(m/(gamma n))`; a separate fixed-query upper
  bound matches these powers. Complete proof:
  [TANH_ENDPOINT_VARIABILITY_LOWER.md](TANH_ENDPOINT_VARIABILITY_LOWER.md).
- Arbitrary fixed depth with identity activations and `m<d` independent
  inputs: an exact conditional Gaussian endpoint law yields the
  full-sphere lower scale
  `sqrt((d-m) y^T Q^(-1) y / n)`. For the hardest label direction,
  matching endpoint upper/lower scales are
  `Y sqrt(m(d-m)/(gamma n))`, with an explicit width threshold.
  Complete proof:
  [LINEAR_ENDPOINT_VARIABILITY_LOWER.md](LINEAR_ENDPOINT_VARIABILITY_LOWER.md).
- A general initialized-onset-to-prediction bridge supplies actual
  positive-time lower bounds. On orthogonal data, arbitrary fixed depth
  and permitted odd activations, it gives
  `c gamma Y / (sqrt(m n) log(en)^(5/2))`.
  This is a transient near-root result, not an endpoint theorem:
  [ONSET_TO_TRAJECTORY_LOWER.md](ONSET_TO_TRAJECTORY_LOWER.md).

The tanh endpoint proof uses exactly frozen unused read-in columns, a
finite-network covariance gap obtained from cubic products of nonlinear
query responses, and the readout energy forced by interpolation. It does
not assume a population comparison or use an infinitesimal-label endpoint
approximation. The simpler independently derived identity--tanh endpoint
argument is retained in
[NONLINEAR_ENDPOINT_VARIABILITY_LOWER.md](NONLINEAR_ENDPOINT_VARIABILITY_LOWER.md).

Checks and exact source hashes are in
[ENDPOINT_LOWER_CHECK.md](ENDPOINT_LOWER_CHECK.md),
[TANH_ENDPOINT_VARIABILITY_LOWER_CHECK.md](TANH_ENDPOINT_VARIABILITY_LOWER_CHECK.md),
and
[LINEAR_ENDPOINT_VARIABILITY_LOWER_CHECK.md](LINEAR_ENDPOINT_VARIABILITY_LOWER_CHECK.md).
These are internal reconstructions, not promotion reviews.
The coordinator owns the tanh proof, synthesis and check assembly;
`merge_general_dense` authored the linear proof and reconstructed the
tanh proof, `merge_general_legendre` authored identity--tanh and checked
the synthesis, and `merge_unbounded_compressor` authored the onset bridge
and reconstructed the linear proof. No experiment was run.

Those endpoint lower bounds transfer to the common all-time norm because it contains
the endpoint and every positive time. They do not make endpoint upper
bounds time-uniform, or prove a universal positive lower bound for every
activation/data pair. Sharp nonlinear whole-sphere dimension dependence,
full-input-span nonlinear endpoint lower bounds, and the remaining
general upper-bound gap are still open. The user's preceding request
authorized this endpoint investigation. Its specialized results are not
presented as general parts of the latest integrated theorem.

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
