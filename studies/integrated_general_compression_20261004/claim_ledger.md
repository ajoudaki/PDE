# Claim ledger: integrated-results audit

2026-10-07. Frozen target and exact read coverage are in
[evidence_log.md](evidence_log.md). Locations refer to that version.
Severity definitions distinguish a proof-completeness concern from a
counterexample. No novelty priority or optimality assessment was requested;
none is inferred from this scoped audit.

## 1. Dense upper and actual-trajectory lower variability

- **Claim/type:** Whole-sphere/all-time upper error of root-width order up to
  subpolynomial factors, and a transient root-width lower bound up to logs.
- **Evidence supplied:** Initialization/fitting, signed comparison, Gaussian
  concentration, initialized-Gram CLT, innovation lower inequality, and
  derivative-to-prediction conversion.
- **Plausibility:** Plausible.
- **Checked argument:** Initialization/fitting, signed energy, concentration,
  innovation and lower conversion were reconstructed. The small-confidence
  normal quantile and the positive-time witness are consistent.
- **Soundness:** Supported conditionally on the shared source event; M1
  prevents an unconditional certification of the full chain. The initialized
  fluctuation calculation does not itself need that event.
- **Adversarial boundary:** L1 is a genuine missing qualification: one sample
  permits identically zero dense discrepancy. The detailed theorem has the
  correct restriction; the canonical ratio table does not.
- **Cascades:** Both negligibility corollaries inherit the lower-bound scope.

## 2. Legendre forward, inverse and learned storage

- **Claim/type:** Every positive integer order has a decreasing error
  certificate; inverse prescriptions give the displayed learned-state size.
- **Evidence supplied:** Exact moment evolution, factor reconstruction,
  fitting, signed stability, history-tail estimate and small-order fallback.
- **Plausibility:** Highly plausible conditional deterministic statement.
- **Checked argument:** The construction, full/simple label distinction,
  all-order domain, absence of an exactness claim at order equal to width,
  and inverse formulas reconstruct coherently.
- **Soundness:** Conditional on source input, with minor flaw L7 in an
  intermediate power multiplication. The final sixth-power forward envelope
  and cubic learned-storage envelope are unchanged by that correction.
- **Cascades:** M1 affects unconditional approximation, not the deterministic
  moment identities or coordinate inventory. No new sample-power improvement
  is established by this audit.

## 3. Harmonic comparison, budget inversion and storage

- **Claim/type:** Signed readout cancellation yields the improved error
  amplification on the full original label interval; supplied budget can be
  inverted without adding a stochastic accuracy-dependent event.
- **Evidence supplied:** Source approximation, coordinate selection, metric,
  corrected optimizer, independent fitting, signed comparison and tail bridge.
- **Plausibility:** Highly plausible conditional deterministic statement.
- **Checked argument:** Selection support, exact source isometry, metric
  positivity, signed cancellation, hidden-Gram absorption, scalar integration,
  dimension-one branch, integer inversion and all-time analytic extension.
- **Soundness:** Supported at those conditional interfaces. Source recurrence
  validity remains under M1. L2 incorrectly equates exact moving/retained
  inventories; L8 overstates the finite-horizon bound's endpoint scope.
- **Cascades:** The quartic sample/gap retained-state power remains; equality
  of exact counts does not. No small-label substitution was used to advertise
  a reduced sample exponent.

## 4. Efficient Harmonic initialization and runtime

- **Claim/type:** Explicit near-quadratic and implicit near-linear setup at
  fixed structural parameters, with the existing retained-model accuracy.
- **Evidence supplied:** Signed numerical-defect stability, local Taylor
  continuation, real-value activation backend, streamed source construction,
  adaptive Gaussian sampling and factored increments.
- **Plausibility:** Highly plausible under the stated exact-real model.
- **Checked argument:** Euclidean source-image accuracy includes its extra
  width factor; sampler posterior handles both orientations, global adaptive
  interleaving and bounded stopping; a deterministic request cap replaces
  random realized rank. Finite operation counts yield the quoted log powers.
- **Soundness:** Conditional on source and runtime comparison. Original and
  late-time domains provide the downstream analytic hypotheses. This does
  not resolve M1's upstream source construction.
- **Cascades/limitations:** No conclusion about finite precision, practical
  width 1000–10000, or converting a supplied dense matrix in linear work.

## 5. Logarithmic decoder: accuracy and finite-word costs

- **Claim/type:** Independent-dense upper-scale comparison using six log
  powers plus log-log in retained words; explicit sufficient width and costs.
- **Evidence supplied:** Finite source probability, numerical source bridge,
  transcript generator, exact empirical query, median amplification, and
  word-level implementation.
- **Plausibility:** Plausible composed theorem; resource algebra highly
  plausible conditional on the finite implementation.
- **Checked argument:** Transcript-event union, need to amplify complete
  sources, common source/query precision requirement, numerical remainder
  absorption, and the modular-to-structural resource exponents. Nisan's
  invocation is valid at the finite-program interface described in the
  source note; hypotheses and scope are recorded in the evidence log.
- **Soundness:** M2 leaves the integrated document short of a self-contained
  construction. A full independent reconstruction of all finite-source and
  numerical backend dependencies was not performed. No source-independence
  claim is made for generated rows or ensemble members after replacement.
- **Localized flaws:** L3–L6 mix domains, confidence, storage units, ranking
  and coefficient qualifications. L8 omits the median ensemble's required
  lower bound. These admit local corrections with unchanged rates.
- **Cascades:** No negligible-actual-variability claim, logarithmic-time query
  claim, or fifth-power word/bit claim is supported.

## Severity triage

| Category | Concern | Rationale | Severity |
|---|---|---|---|
| Proof substantiation | M1 | The shared insertion event was not fully reconstructed. A second check recovers the principal scalar traces, but not the upstream control-uniform maps/remainder. | Unresolved completeness/coverage concern; not a demonstrated major or fatal logical flaw |
| Integration completeness | M2 | Finite implementation chain is summarized rather than included despite the self-containment promise. | Major completeness concern; imported conclusion not refuted |
| Scope | L1 | Missing two-sample restriction has an existing counterexample, but a local qualification repairs it. | Minor flaw |
| Storage/interface | L2–L6 | Exact inventory, domain, units, constants and ranking can be corrected without changing the theorems. | Minor points |
| Local proof/presentation | L7–L9 | Direct multiplication, endpoint wording, ensemble lower bound, TeX, and the recovered scalar-trace bridge admit localized repairs. | Minor flaws/points |

## Holistic analysis

No fatal flaw or counterexample to the principal correctly qualified
compression claims was found. The conditional contributions survive. The
stronger claim that one fully explicit, fully self-contained document closes
the entire chain is not supported by this audit. Passing execution tests
does not discharge either proof-completeness concern.
