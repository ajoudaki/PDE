# NTH truncation lower bounds

## Book-promotion preparation (2026-10-10)

The user requested a compact, elegant promotion of the matching deep-linear
NTH storage result, followed by paper integration after book promotion.
The independent [selection](PROMOTION_SELECTION.md) accepts one section in
Part II, Chapter 7, with a Chapter 9 cross-reference. This is theory only.
The candidate must preserve the short-time, growing-data, fixed-label,
literal-array scope and include both necessity and sufficiency. No new
experiment or broader nonlinear claim is part of this promotion.

Write assignments for this continuation: this coordinating task owns
`PROMOTION_*`, `prepare_promotion.py`, the promotion paragraph here, and
`data/generated/nth_lower_bound_20261010/promotion_*`; the isolated assembler
`nth_compact_assembly` owns `PROMOTION_CANDIDATE_v1.qmd` until delivery.
The selector `nth_selector_current` owns its completed selection report.
All other study sources and concurrent paper/code work are preserved.

Current gate: **all pre-approval gates passed; awaiting approval of the
concrete reviewed addition.** No maintained book or paper file has been
changed by this promotion task. The final candidate is
[PROMOTION_CANDIDATE_v2.qmd](PROMOTION_CANDIDATE_v2.qmd), SHA-256
`e8c8cbd7474b9e0bbaded9100ce02474708339f9ac95cf606de7b93886616d23`.
It contains one main theorem, one general upper-bound corollary, and five
supporting lemmas, with shared estimates proved once. Its approximately
3,050 whitespace-separated words exclude no required proof dependency.
The existing compression fitting and dense-variability results have different
quantifiers; their conclusions are not silently reused on this growing-data,
fixed-label family. Paper adaptation remains downstream of book approval
and integration.

The exact destinations are one section in `docs/07-observable-closure.qmd`,
after the unrestricted-encoding discussion and before the calculus
obstructions; one descriptive theorem link near the opening of
`docs/08b-trajectory-compression.qmd`; and one entry in `docs/references.bib`.
No new chapter, maintained code, or empirical conclusion is proposed.

Completed gates and preserved evidence:

- Independent [placement selection](PROMOTION_SELECTION.md): accept.
- Two complete, independent scientific reviews:
  [A](PROMOTION_REVIEW_A_v1.md) and [B](PROMOTION_REVIEW_B_v1.md): PASS,
  with no required mathematical corrections. Both reviewers subsequently
  verified the exact wrapper-only v1-to-v2 correspondence. The
  [retained diff](PROMOTION_FORMAT_v1_v2.diff) moves six proof anchors
  outside Quarto proof divs; statements, proofs and references are unchanged.
- Independent final [integration review](PROMOTION_INTEGRATION_FINAL.md):
  PASS. It read all new content, checked the declared older context, and
  inspected representative PDF pages and actual link destinations.
  Earlier adverse integration reports remain preserved:
  [v1](PROMOTION_INTEGRATION_v1.md), [v2](PROMOTION_INTEGRATION_v2.md).
- Final standalone edition:
  `data/generated/nth_lower_bound_20261010/promotion_v4/`.
  Full HTML and PDF renders exited zero; the PDF's retained editable LaTeX
  is the exact compiled export. The three output records and commands are
  in `validation/builds.json`; the retained source is
  `data/generated/DTDL/docs/DTDL.tex` within that edition.
- Structural validation checked 93 library files. Final mechanical checks
  verified all 104 frozen source hashes, 18 HTML pages, 38 new targets,
  formal environments, the PDF pointer, and zero broken local links.
  Evidence is in `validation/final_checks.json` and `preservation.json`.
  Concurrently promoted Chapter 9 material is preserved unchanged.

The [final manifest](PROMOTION_MANIFEST_v4.json) records identities,
baseline/source hashes and placement. The [assembly script](prepare_promotion.py)
and [output validator](PROMOTION_VALIDATE.py) reproduce the assembly/checks;
run the latter with the standalone edition path. The neutral
[scientific](PROMOTION_REVIEW_ASSIGNMENT.md) and
[integration](PROMOTION_INTEGRATION_ASSIGNMENT.md) assignments and
supplementary algebra checks [A](PROMOTION_CHECK_A.py),
[B](PROMOTION_CHECK_B.py) remain study evidence, not promoted APIs.

After approval, recheck current dependencies, apply only the three accepted
insertions, verify exact correspondence to this edition, and record the
integration commit before adapting the paper. Do not overwrite whole live
chapters from an older frozen edition.

## Latest matching-size continuation

[MATCHING_RESULT.md](MATCHING_RESULT.md) now gives a matching upper for
the existing short-time deep-linear lower-bound family, with its complete
geometric source proof in
[UPPER_LOCAL_GEOMETRIC.md](UPPER_LOCAL_GEOMETRIC.md). Complete fresh scoped
reconstruction passed in [MATCHING_CHECK.md](MATCHING_CHECK.md). The two
requested editorial corrections have been applied: fixed success probability
is explicitly in `(0,1)`, and equation (7) of WORST_CASE_RESULT has its
TeX fraction repaired. No mathematical estimate changed. The earlier lower
and its checks remain as recorded below.

The new upper keeps the original frozen top, initial tensors, and own
residual. For every deterministic unit-input dataset with bounded labels
and `d<=n`, two hidden identity layers, canonical Gaussian mobilities and
zero readout, an explicit `q=O(log n)` gives whole-sphere error at most
`D_n/n`, with probability at least `1-4e/sqrt(n)-4 exp(-c_*n)`.
Here `D_n` is the actual iid dense-pair discrepancy on the same interval
`[0,1/32768]`. A direct small-ball proof supplies its needed lower bound;
an upper concentration rate is not used in place of actual variability.
Zero label-weighted input mean gives exact zero predictions in both models.

For the hard family `4|m`, `4<=m<=sqrt(n)`, `d=m+1`, fixed nonzero
label magnitude, the matching scale is
`exp(Theta(log m log n))`, hence `exp(Theta((log n)^2))` when `m` grows
as a fixed positive power of `n`. Both moving and total literal arrays
have that scale. This settles the current witness's local complexity,
not the broader nonlinear or longer-time worst case.

The separate searches did not close that broader question:

- [LOWER_ALTERNATIVE_SEARCH.md](LOWER_ALTERNATIVE_SEARCH.md) proves an
  exact one-driver own-clock transfer and an all-orders failure for an
  auxiliary smooth scalar gradient model. It does **not** realize that
  model as the canonical Gaussian network, so no stronger network lower
  is inferred.
- [UPPER_NONLINEAR_SCOPE.md](UPPER_NONLINEAR_SCOPE.md) gives an explicit
  sufficient-condition theorem involving the complete evolving source
  tensors. Its width-uniform hypothesis remains unverified for nonlinear
  Gaussian networks. The coordinate-growth diagnostics only reject two
  naive analytic-majorant arguments; they do not reject the upper itself.

Root read the complete new route files. These diagnostics remain
author-derived scoped results, not dependencies of the matching theorem.
No experiments, commits, promotion, or changes to shared paper/book/code.

## Previously checked lower bound

Date: 2026-10-10. Status: the latest joint width--sample lower bound is in
[WORST_CASE_RESULT.md](WORST_CASE_RESULT.md). Its source-to-error proof and
scope passed the complete internal check in
[WORST_CASE_CHECK.md](WORST_CASE_CHECK.md). This is not a promoted result.
No shared paper, book, or code was edited.

The separate [WORST_CASE_DENSE_CHECK.md](WORST_CASE_DENSE_CHECK.md)
reconstructs the Gaussian benchmark, uniform sample-range dependence, and
storage deduction. Its truncation-error premise is proved in the result
and checked by the complete report above. Root read all of these complete
derivations and reports; no scientific premise remains conditional on an
unverified other-study input.

For a full-rank correlated dataset with two label signs, fixed label
magnitude `0<eta<=1`, two hidden identity layers, and the canonical
feature-learning metric, matching actual dense-pair worst-time test
discrepancy requires literal frozen-top NTH array storage at least

\[
\exp\!\left[c_\eta\log m\,
\log\frac{n}{m+\log(en)}\right],\qquad
4\le m\le\sqrt n,\quad 4\mid m,\quad d=m+1.
\]

In particular, `m=4 floor(n^a/4)`, for fixed `0<a<=1/2`, gives
`exp(c_(eta,a) (log n)^2)`: a genuine superpolynomial width lower bound.
The nonfrozen literal arrays have the same headline lower bound. The
comparison uses one distinct passive query versus the larger whole-sphere
dense-pair discrepancy on the same fixed interval `[0,1/32768]`; failure
holds with probability tending to one, simultaneously over all orders
within the stated insufficient budget.

Essential limits: this is **not** `exp(cn)`, not superpolynomial at fixed
`m,d`, and not an information-theoretic lower bound on structured tensor
encodings. Identity is admitted by the NTH paper; both hidden feature
covariances change at a nonvanishing width scale, but the input--output
function class is linear. The normalization and zero readout are the
canonical feature-learning regime, not the native Huang--Yau NTK theorem.
Labels remain fixed as `m` grows, so the old compression theorem's extra
`Y=O(1/m)` hypothesis is not imposed or imported. Restoring that hypothesis
invalidates this derivation of the superpolynomial bound; it does not prove
that no other such bound is possible.

The separate fixed-data nonlinear growing-order direct-array lower bound
remains in [NONLINEAR_RESULT.md](NONLINEAR_RESULT.md). The general two-tanh
growing-order question and a fixed-data exponential-width obstruction
remain open.

The finite-time continuation is [FINITE_TIME_RESULT.md](FINITE_TIME_RESULT.md).
It compares worst error on every fixed `[0,T]` at one distinct passive query
against dense-pair error on that same query and window. The dense benchmark
sharpens to `C_T sqrt(log(n)/n)`. The existing nonlinear necessary storage
scale remains `exp(c log(n)/loglog(n))`: its original witness was already
early-time, not an endpoint discrepancy. A stronger storage exponent is not
claimed from the finite-horizon change.
The bounded continuation also records two proof-route diagnostics in
[FINITE_TIME_COEFFICIENT.md](FINITE_TIME_COEFFICIENT.md) and
[FINITE_TIME_REMAINDER.md](FINITE_TIME_REMAINDER.md): generic parameter
interpolation and absolute averaged-state majorants do not provide the
missing geometric scalar error lower bound. These are not optimality or
impossibility theorems for the actual NTH.
The new internally checked [FINITE_TIME_TANH.md](FINITE_TIME_TANH.md)
proves actual dense and original-NTH finite Taylor remainders for two tanh
layers and two orthogonal inputs, through order `O(log n)`. This closes a
remainder sub-bridge but not the full-coefficient noncancellation or
small-ball steps needed for a growing-order tanh lower bound.

## Question and scope

Current continuation (matching-size challenge): the user asks for a
substantially stronger worst-case lower, or a matching
`exp(O((log n)^2))` upper. The original frozen-top rule and its own residual
remain mandatory. A matching upper on the existing short-time deep-linear
witness is a useful resolved subproblem, not a universal nonlinear or
all-time upper. This distinction is fixed before the new derivations.
The active theoretical routes are root (actual dense-variability small-ball
bridge and synthesis), `nth_matching_upper` (uniform deep-linear
ordered-integral upper, `UPPER_LOCAL_GEOMETRIC.md`),
`nth_stronger_hard_case` (fresh prompt-only harder-witness search,
`LOWER_ALTERNATIVE_SEARCH.md`), and `nth_general_upper_scope`
(nonlinear upper conditions and verification,
`UPPER_NONLINEAR_SCOPE.md`). The latter routes have scoped scientific
inputs recorded in their files and do not exchange candidate approaches
before they are complete. No numerical experiments or Git writes.

Current continuation: the user explicitly asks for an existential worst-case
lower bound. One admitted activation and one nondegenerate dataset or explicitly
specified growing dataset family suffice; no uniform lower over all datasets
or activations is required. The target is superpolynomial or exponential
literal frozen-top NTH tensor storage in dense width, at actual dense-pair
finite-window prediction accuracy. The continuing parameterization is the
canonical feature-learning metric and zero readout; the native Huang--Yau
NTK metric/random-readout theorem is a distinct scope, not silently imported.
The requested end goal is
still the order/storage needed for dense-variability accuracy, not merely
formal correctness of fixed-order coefficients. The existing linear witness
does not establish a superpolynomial fixed-data bound. Labels and activation
remain fixed independently of width. A joint `(n,m)` lower must explicitly
state any growth of samples and dimension and whether it retains the earlier
sample-dependent small-label restriction; these cannot be hidden in constants.

The latest bounded routes were: root, correlated growing-sample construction
and synthesis; `worst_analytic_witness`, its source/physical-time proof after
a separate fresh analytic search; `worst_smooth_witness`, fresh smooth
nonanalytic activation search; `nth_native_scope`, primary-source scope and
admissibility check. The latter three started without inherited research
discussion. Allowed inputs and subsequent same-study source additions are
recorded in their route files. The completed source reconstruction is
[WORST_GROWING_SAMPLE_ROUTE.md](WORST_GROWING_SAMPLE_ROUTE.md); its dense
concentration premise is proved in the assembled result, not assumed there.
The smooth nonanalytic route is recorded as open, with its exact failed
bridge, in [WORST_SMOOTH_ROUTE.md](WORST_SMOOTH_ROUTE.md).
[NATIVE_SCOPE_CHECK.md](NATIVE_SCOPE_CHECK.md) verifies the official
activation/data assumptions and explains why native NTK and canonical
feature-learning conclusions cannot be interchanged. Its published upper
bound is a source report, not a newly self-contained imported theorem.
No experiments, commits, or paper edits.

Root investigates general-data estimates and synthesizes; `tanh_nth_lower`
owns `TANH_LOWER_ROUTE.md`, `tanh_nth_upper` owns `TANH_UPPER_ROUTE.md`, and
`tanh_nth_generic` owns `TANH_GENERIC_ROUTE.md`. These are separate initial
routes with scoped scientific inputs recorded in their artifacts. No new
experiments, paper edits, or commits are authorized or being performed.

Prove a rigorous obstruction or necessary truncation-order/storage bound for
the frozen-top neural tangent hierarchy when it approximates canonical
feature-learning gradient flow at dense-versus-dense trajectory precision.
Distinguish this specific hierarchy from arbitrary compressed dynamics, and
distinguish shallow/linear comparison models from the maintained theorem's
deep nonlinear setting. No numerical experiments or shared-paper edits.

This is a new lower-bound investigation. Inputs are the maintained book's
notation/setup and external primary definitions of NTH. No other study's
research is imported. Huang–Yau's ICML 2020 paper is used for the definition
of the frozen-top hierarchy, not as an unverified stochastic theorem.

## Ownership and routes

- Root: synthesis, deep/multisample route, README and RESULT.
- `nth_lower_scalar`: prompt-only shallow scalar linear route;
  `SCALAR_ROUTE.md`.
- `nth_lower_nonlinear`: shallow tanh route and deep initial-jet test;
  `NONLINEAR_ROUTE.md`. Additional allowed input: the first 150 lines of
  `docs/08b-trajectory-compression.qmd` for exact normalization.
- `nth_lower_analytic_check`: dimension-free complex-time and
  derivative-to-real-interval estimates; `ANALYTIC_ROUTE.md`. Its fresh
  `sup_lemma` helper checked the scalar analytic inequality.
- `nth_lower_scalar` additionally checks the assembled deep argument in
  `DEEP_CHECK.md`, after its independent scalar candidate was frozen.
- In the same-investigation strengthening, `nth_lower_scalar` owns
  `STRONGER_SOURCE.md`; `nth_lower_analytic_check` owns
  `POLYNOMIAL_UPPER.md`; and `nth_lower_nonlinear` owns
  `STRONG_NONLINEAR_SEARCH.md`. Root owns the authoritative synthesis.

All agents may read required skills/shared process instructions. Generated
scratch, if needed, belongs to `data/generated/nth_lower_bound_20261010/`.
No commits or changes to unrelated dirty work are authorized by this task.

## Results and exact limitations

The new growing-order result is [NONLINEAR_RESULT.md](NONLINEAR_RESULT.md).
It uses the original frozen-top NTH with its own residual, canonical
Gaussian initialization, two trained hidden layers, and one fixed genuinely
nonlinear first activation from the family \(z+\varepsilon\sin z\);
the second activation is the identity. For almost every fixed
\(\varepsilon\in[1/8,1/4]\), fixed labels \((\eta,0)\) with
\(0<\eta\le10^{-62}\), and two orthogonal inputs, matching actual dense-run
variability requires order at least \(c_\eta\log n/\log\log n\) along
\(n_k=\lceil e^k\rceil\). The necessary literal-array size is
\(\exp(c_\eta\log n/\log\log n)\), ruling out every fixed-power polylog
budget, but not establishing an \(\Omega(n)\) bound. The lower concerns
actual physical predictions, not just initialized derivatives.
It does not settle two tanh layers, all correlated inputs, or arbitrary
implicit encodings. A prescribed parameter such as \(\varepsilon=1/4\)
has not been certified.

The proof combines the exact omitted-jet and fixed-parameter sublevel
arguments in [NONLINEAR_WITNESS.md](NONLINEAR_WITNESS.md), the self-contained
Gaussian forest estimate in [INITIAL_JET_MOMENTS.md](INITIAL_JET_MOMENTS.md),
and the geometric-order real remainder in
[SINE_REMAINDER.md](SINE_REMAINDER.md). The latter uses a finite Taylor
polynomial only as a proof device: no continuation closure or replacement
algorithm is introduced. [SINE_DENSE_VARIABILITY.md](SINE_DENSE_VARIABILITY.md)
proves a deliberately nonsharp polynomial decay of the actual whole-circle,
complete-trajectory dense-pair discrepancy, sufficient for the ratio lower
bound. Checks are recorded in [ASSEMBLY_CHECK.md](ASSEMBLY_CHECK.md),
[SINE_CHECK.md](SINE_CHECK.md), and the remainder file. Earlier cube-root
order estimates are valid but superseded
by the geometric-order/Chebyshev sharpening in the main result.

Two further routes remain diagnostics only:
[AVERAGED_UPPER.md](AVERAGED_UPPER.md) proves an averaged-versus-empirical
Taylor distinction and records exact high-order identities;
[GAUSSIAN_TAIL_LOWER.md](GAUSSIAN_TAIL_LOWER.md) isolates a first-layer
Gaussian sector for tanh but does not close its full-network cancellation
or actual-error transfer. Neither is reported as a tanh storage theorem.
The author assignments for this continuation are: root, assembled result
and dense-pair estimate; averaged-upper agent, real remainder and jet check;
Gaussian-tail agent, initialized moments and assembly check; generic agent,
fixed-parameter transfer and dense/remainder check. These are same-study
internal checks, not independent promotion reviews.

The general-input tanh result is [TANH_RESULT.md](TANH_RESULT.md). For two
hidden tanh layers, arbitrary fixed input configurations with positive final
feature-Gram gap, and fixed labels satisfying `0<Y<=gamma/(64m)`, it proves
an unconditional whole-sphere, whole-trajectory two-sided error estimate for
orders two and three. Its lower error is `c Y^3 (gamma/m)^8>0`; its upper
error is `7300 Y^3 (m/gamma)^3`. A sufficient width is explicitly
`247808 (m/gamma)^4 log(10m^2/delta)`. Complete proofs are in
[TANH_LOWER_ROUTE.md](TANH_LOWER_ROUTE.md) and Section 4 of
[TANH_UPPER_ROUTE.md](TANH_UPPER_ROUTE.md), with the scoped internal check
[TANH_CHECK.md](TANH_CHECK.md). This does not determine a growing order or
storage at dense-variability precision. The conditional high-order criterion
and the coordinate-analytic obstruction are not substitutes for that theorem.

The bounded follow-up [TANH_HIGH_ORDER_ROUTE.md](TANH_HIGH_ORDER_ROUTE.md)
derives an indefinite curvature contribution at the next source order, so
the fourth-order positivity proof does not directly iterate. The missing
bridge is still a cancellation-resistant bound for actual prediction error
at growing order, including the hierarchy's own residual feedback. No new
storage exponent follows from that diagnostic.

The earlier linear-witness storage argument is [RESULT.md](RESULT.md), with the fully explicit analytic
dependency in [ANALYTIC_ROUTE.md](ANALYTIC_ROUTE.md). There is an admissible
canonical two-hidden-layer, two-sample, two-dimensional linear-activation
instance (`gamma=1`, `beta=10`, fixed small nonzero label) such that matching
any constant multiple of the actual dense-pair complete-trajectory discrepancy
with positive fixed success probability requires `q >= c_eta log(n)`.
The positive constant is explicit in
[STRONGER_SOURCE.md](STRONGER_SOURCE.md). For literal tensor arrays this gives
a necessary retained size `n^(alpha_eta-o(1))`, with `alpha_eta>0` explicit.
At fixed label eta=10^(-62), `alpha_eta` is approximately 0.0019649183.
The source invariant retains the trained second matrix and improves the
previous omitted-derivative bound by a factorial. The earlier
`log(n)/loglog(n)` order estimate is superseded as the headline bound.

There is a complementary full-trajectory upper bound on **the same witness**:
[POLYNOMIAL_UPPER.md](POLYNOMIAL_UPPER.md) proves
`E_n(q) <= 24576 eta (128 eta)^(q-1)`. An explicit `q=O_eta(log n)` makes
`E_n(q)<=D_n/n` with probability tending to one, using at most
`C_eta n^(5 log(2)/log(1/(128 eta)))` retained coordinates. For the existing
label range eta<=10^(-62), this exponent is less than 1/20. Thus even an
Omega(n) retained-array lower bound is false **on this witness**. These counts
exclude coefficient-generation work and initialization peak memory.

Both bounds use the whole sphere and the entire fitted trajectory, with the
closure's own residual. The lower bound also holds for two fixed passive
unseen queries, without their labels. Neither is a claim about arbitrary tensor
encodings, implicit implementations, or different closures. The witness uses
identity activations, not general tanh or the source's native NTK scaling.
The fixed-data superpolynomial and exponential-width lower-bound questions
across the full activation/data class remain open; the growing-data
superpolynomial result above is a distinct, now closed case.
[STRONG_NONLINEAR_SEARCH.md](STRONG_NONLINEAR_SEARCH.md)
records a bounded source-singularity route and its exact unresolved bridges;
it does not establish a canonical prediction or storage lower bound.

[SCALAR_ROUTE.md](SCALAR_ROUTE.md) separately gives a simpler exact shallow
one-sample illustration, including an exact constant-state alternative closure.
[NONLINEAR_ROUTE.md](NONLINEAR_ROUTE.md) is the superseded special-input
predecessor to the general-data tanh bound. Its early-time remainder coefficient
`1/6` is erroneous; the corrected `1/3` proof and constants are in
TANH_LOWER_ROUTE. That auxiliary result does not prove a growing-order bound;
its deep complete-trajectory dense-pair rate is not established in that route.
Root read both complete auxiliary arguments and checked their algebra; only
the assembled linear deep result is used in the headline storage conclusion.

## Contract and check record

Initialization coefficients must be obtained from the actual initialized
dense system. Frozen-top NTH copies tensors through rank q and freezes rank q.
The primary obstruction should concern predictions at physical times, not
merely mismatched derivatives or mismatched residual clocks. A lower bound
for a particular tensor-array representation is not an information-theoretic
storage lower bound.

The root reconstructed the deep coefficient and all-time concentration proof,
read the complete analytic dependency, and checked the model against the first
150 lines of maintained `docs/08b-trajectory-compression.qmd`. The scoped
consistency report is [DEEP_CHECK.md](DEEP_CHECK.md). Analytic helper provenance,
explicit constants and deterministic arithmetic checks are recorded in the
analytic route. These are internal checks, not independent promotion reviews.
No numerical research experiment was run. The only external scientific input
was the NTH definition in Huang--Yau's ICML 2020 equation (15); no stochastic
theorem from that source was imported. The strengthened proofs are reproduced
by following RESULT, ANALYTIC_ROUTE, STRONGER_SOURCE, and POLYNOMIAL_UPPER;
there are no generated-data dependencies. Root read all three new route files
completely and reconstructed their mathematical claims and scope. The stronger
nonlinear route remains a diagnostic, not a canonical complexity conclusion.
The complete additional upper-bound check is
[SAME_STUDY_CHECK.md](SAME_STUDY_CHECK.md); its requested synthesis correction
is resolved. This is a scoped same-study check, not an isolated promotion
review. Root read its complete report.

All unrelated dirty paths were preserved. No commit or push was requested or
performed. The same-investigation strengthening is confined to the proofs
above. There are no numerical campaigns, depth sweeps, or optimal-encoding
lower-bound claims. The paper and maintained book remain unchanged.
