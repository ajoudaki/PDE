# Can Legendre history compression use polylogarithmic order?

## Current continuation: remove the readout-only tail

The user asks whether the previously proposed oblivious physical-time
variant can retain polylogarithmic order without freezing hidden layers.
This is a correction of the fitted continuation of the existing
`OBLIVIOUS_WINDOWS.md` construction, explicitly revisited by the user,
not a claim about reducing the order of the unchanged original method.
Its proved finite-horizon construction is retained. The repair
archives its completed memory factors and starts one fresh order-one
residual-clock memory block; physical weights in every layer continue
training. The completed result and proof are in `NO_FREEZE_TAIL.md`.
For each fixed admissible problem and confidence, eventually in width,
the order is O(log(en)^(5/2)), the all-time whole-sphere error is at most
Y/n, and the complete retained learned state is
n(d+1)+2(L-1)mn(q+1)+O(1). This includes the archived learned factors;
the initialized (L-1)n^2 mixers remain additional fixed storage.

The deterministic tail lemma is proved at an arbitrary bounded starting
network with a positive normalized feature-Gram gap, not by applying a
zero-readout initialization theorem at restart. Its exact velocity defect
is bounded by residual RMS times accumulated normalized parameter motion.
This closes a width-independent small-tail bootstrap, giving exponential
fitting and a uniform sphere prediction tail. A trigger at residual RMS
Y/n^2 reaches this regime eventually without changing the original label
condition. The existing growing-horizon first-stage parameter estimate
transfers the gap and bounds to that trigger. A deterministic rollover at
T=32(m/gamma)log(en) is also valid.

Prompt-only independent analysis reconstructed the tail mechanism and its
width-normalized constants. `NO_FREEZE_CHECK.md` is the subsequent fresh,
isolated full candidate/interface check, with verdict PASS in its stated
scope. Root read the entire report and reconstructed the calculation.
The frozen candidate checked was SHA-256
ed15f9dd811e9e4a84700ff15fa6d35de3f297bac6f6ee7a6a006c4381af34da;
only its status paragraph was updated after that check. The check uses the
existing first-stage theorem and does not claim fresh certification of its
entire probabilistic cavity/source proof.

This removes imposed freezing of physical layers, not the one-time memory
rollover. It is a hybrid online method, not the unchanged single-block
residual-clock equations or a completely switch-free smooth ODE. The
original model already slows down and fits; the repaired issue is its
all-time approximation guarantee. These are internally checked study
results, not promoted book material. No numerical run, paper edit, or
commit was made.

## Current continuation: sufficiency at n^(1/10+o(1))

The user now asks whether a subpolynomial factor above the necessary
one-tenth scale suffices for the unchanged method. This continues the
same study. The contract is still the full original activation/data
scope, unchanged residual clock and prefix, and all-time whole-sphere
accuracy relative to actual dense variability. The existing lower bound
is compatible with this target; it does not prove sufficiency.

Root investigates a finite-horizon fifth-power upper bound and its
all-time extension. A fresh scoped reader investigates terminal clock
geometry; a returning upper-bound reader investigates weighted tail
estimates. Inputs remain the current paper and this study. No new
experiment, paper edit, or commit is requested. A terminal history
obstruction alone will not be presented as a neural prediction
counterexample.

Outcome of this bounded continuation: **the all-time sufficiency question
remains open**, with a new proved finite-horizon upper result.

- `FINITE_HORIZON_FIFTH_POWER.md` proves, for every fixed finite physical
  horizon T and the full original activation/data scope, actual whole-sphere
  prediction error at most exp(C_T sqrt(log(en))) / q^5 once
  q >= exp(C_T sqrt(log(en))). Consequently
  q = ceil(n^(1/10) exp((log(en))^(3/4))) suffices on each fixed finite
  interval. C_T depends on T; this is not an all-time theorem.
- `FINITE_HORIZON_CHECK.md` is a fresh isolated check of that complete
  argument and its source interfaces. Root read the full report and
  reconstructed the proof. Its only requested wording correction was
  applied: the label vector is fixed with Y>0; entries may have either
  sign. The corrected candidate hash is
  82d4abed4cb5842b84c78204c1ad1708cd1603b451f108b7771bdc9f7c500268.
  The report records the pre-correction frozen hash and does not claim
  fresh certification of the entire imported cavity/source theorem.
- `TENTH_POWER_UPPER_ROUTE.md` proves a stronger all-time dense-history
  estimate (q^(-7/2), up to logarithms, for its signed matrix cross tail),
  but does not transfer it to the actual closure's all-time predictions.
  `SCALAR_CLOCK_REGULARITY_LOSS.md` proves that the proposed smoothness
  assumptions alone cannot give a fifth-power signed bound, even with
  the correct prefix and an exact forward/backward derivative relation.
- `ENDPOINT_GEOMETRY_ROUTE.md` derives admissible dense neural endpoint
  terms whose tensor survives the sample sum and the instantaneous
  output Jacobian. It does not prove a full-history primitive asymptotic
  or a compressed-output lower bound. In particular it does not disprove
  the requested one-tenth sufficiency theorem.

The remaining bottleneck is the actual prediction response in a late-time
residual-clock boundary layer. The finite-horizon proof removes the need
to bound high derivatives of the closure on regular clock segments; its
constants cannot be substituted at T proportional to log(n). The existing
general sufficient order remains n^(1/4+o(1)); the independently checked
necessary one-tenth scale below is unchanged. New results are study-level
internal findings, not promoted book material. The paper was not edited;
no experiments or commits were made.

## 2026-10-10 continuation: an order below n^(1/10)

The user now asks whether an order strictly below `n^(1/10)` suffices for
the same original method. This is a continuation of the same order-versus-
accuracy investigation, not a change of model. The target remains actual
dense-variability accuracy in the all-time, whole-sphere norm, with fixed
problem parameters and the original full activation/data scope. A power
strictly smaller than `1/10` is the main interpretation; any distinction
between this, `o(n^(1/10))`, and a small constant times `n^(1/10)` must be
made explicit in the conclusion. The earlier necessary `n^(1/20-o(1))`
order does not itself settle this request.

The bounded proof routes are: root's exact cross-projection algebra and
uniform Legendre estimates; `legendre_sharper_upper` on primitive-forcing
stability and a sharper sufficient rate; `legendre_bulk_obstruction` on
an actual stronger prediction obstruction; `identity_dense_tight_upper`
on the identity example's dense fluctuation without logarithmic loss.
The three delegated contexts started fresh with explicitly scoped current-
paper/this-study inputs. Cross-pollination began only after the first two
returned concrete formulas. No new experiment, paper edit, or commit is
authorized. New substantial arguments and their checks will be recorded
in this same flat study. A classical Legendre interior asymptotic was also
checked against the primary NIST DLMF, §18.15, equation 18.15.4_5; the
needed specialization can be proved from the paper's integral formula.

This continuation is now resolved against a strictly smaller power:
[FIFTH_POWER_RESULT.md](FIFTH_POWER_RESULT.md) is the current sharpest
result of this investigation. The old valid onset lower bound was
strengthened from \(q^{-10}\) to \(q^{-5}\) for actual predictions,
uniformly in width and order, on the same admissible identity-activation
example. The dense upper bound is sharpened to
\(O_{\mathbb P}(n^{-1/2})\) on that example without a carrier-source
theorem. Consequently every \(q=o(n^{1/10})\) fails even constant-factor
comparison with actual dense variability; vanishing relative error
requires \(q/n^{1/10}\to\infty\). Constant-factor sufficiency at
\(q=c_0n^{1/10}\), including \(c_0<1\), remains open, as does the best
general sufficient exponent. No positive theorem with the requested
smaller exponent is claimed.

Evidence: the complete prediction proof is SHARPER_OBSTRUCTION_ROUTE.md
(SHA-256 578b46258b1f5a1116b62630a0da7434f17bd1976e24a445b324120298b30e8b);
the no-log dense proof is IDENTITY_DENSE_UPPER.md
(94ccc7e639a376f54dd7dea89d5158a2a7f94efcb29fed06e1e2be1c931152e0).
Root reconstructed both and read all check reports. FIFTH_POWER_AUDIT.md
is a fresh scoped full-chain PASS. FIFTH_POWER_TRANSFER_CHECK.md is a
separate nonauthor transfer check with reused context.
CROSS_TAIL_IDENTITIES.md and CROSS_TAIL_CHECK.md contain the exact scalar
algebra and its independent verification. Their one wording clarification
was applied: the scalar lower implication requires a nondegenerate
interval, not a bound at every endpoint.

SHARPER_UPPER_ROUTE.md preserves a new proved primitive-forcing stability
lemma but does not establish a sharper general sufficient spectral power.
This separates the positive proof tool from an unproved compression
guarantee. The q-dependent-history regularity, terminal residual-clock
behavior, and nonlinear-only scope remain genuine open questions for
that upper route. No new run, paper edit, or commit was performed.
All new findings are internally checked study results, not promoted
book material.

## Active continuation: the unchanged residual-clock method

The user now specifically asks for the original equations: initial clock
one, residual-RMS clock speed, constant forward/zero backward prefix, and
the original all-time updates. Changing the clock, prefix, basis, tail,
or adding compiled directions is not an answer to this continuation.
The user reports strong empirical support; no new experiment is authorized
or required by this proof request. The physical-time variant below remains
a separately checked result and is not substituted for this target.

Current bounded routes: root reconstructs the original observable-level
defect and checks the actual implementation's clock conventions; a reader
investigates prediction-level cancellations; a reader investigates whether
the known prefix approximation issue produces an actual neural-prediction
obstruction. Prior history-tail obstructions alone do not settle this.
Only a proved original-method guarantee or an actual counterexample can
resolve the theorem; otherwise report the exact gap. Scope, source boundary,
state counts, and prohibition on paper edits/experiments remain unchanged.

Additional direct current-paper inputs for this continuation are the
`LegendreCompression` implementation in
`paper/figures/capture_trajectory.py` (to identify its clock and prefix),
the relevant description in `paper/README.md`, and the dense upper
certificate and its complete relevant proof in
`paper/integrated_appendix.tex`. These are current paper inputs, not an
authorization to follow its links to other studies. The upper certificate
is required to compare an error lower bound with actual dense variability;
the dense lower bound alone would not justify that implication.

`ORIGINAL_OUTPUT_ANALYSIS.md` now contains a complete actual
prediction counterexample for the unchanged method, including a remainder
uniform in width and order. `ORIGINAL_METHOD_RESULT.md` closes the actual
dense-variability comparison and separates that result from the incomplete
tanh coefficient calculation in `ORIGINAL_POSITIVE_ROUTE.md`. Two bounded
separate checks passed: `ORIGINAL_OUTPUT_REMAINDER_CHECK.md` and
`ORIGINAL_OUTPUT_COEFFICIENT_CHECK.md`, both tied to candidate SHA-256
`6bf9c51316b5425eb0cb9288a0859b24e6f08d5adcf6155e21bf2dbfad967320`.
Root read both reports and reconstructed the calculation. These readers
reused their earlier contexts but did not author this candidate and were
not supplied each other's findings. The second checked the relative-error
implication using the authorized dense upper certificate. No change to
the paper or experiments was made; no commit was requested or performed.

Current claim status:

- **Falsified over the full original scope:** subpolynomial order for the
  unchanged residual-clock, unit-prefix method at dense-variability accuracy.
  The proof uses an admissible identity-activation example and an actual
  `c q^(-10)` prediction discrepancy. This supersedes the earlier status
  of a mere history-approximation concern; it does not contradict the
  separate modified-method positive result.
- **Proved, internally checked:** the new onset lower bound, and failure
  of constant-factor comparison to actual dense variability for
  `q=n^(o(1))`, using the paper's existing dense upper theorem. The
  ordinary fitting and upper certificates remain imported current-paper
  results, not new restrictions or newly re-certified source theorems.
- **Open for a nonlinear-only restriction such as tanh:** the fifth-order
  coefficient is nonzero but its uniform remainder has not been proved.
  No numerical result was inspected sufficiently to change its empirical
  status. No further branch is needed to settle the full-scope question.

## Question and contract

User asks whether the Legendre argument can yield q = polylog(n), reducing
moving state from n^(5/4+o(1)) to n^(1+o(1)). This is a new theoretical
investigation, not an edit of the paper or a numerical campaign. Inputs are
the user-assigned current paper's compact proof: compact.tex,
compact_legendre.tex, compact_fitting.tex, compact_foundations.tex and, only
where relevant, compact_selected.tex. Other studies and historical versions
are not inputs. The maintained book's setup/notation are contextual guides.

Preserve the canonical Gaussian initialization, block-mobility gradient flow,
fixed depth and data, positive feature-Gram gap, unbounded-value strip-analytic
activation class, fixed small-label condition, full sphere and all physical
times including fitted limits, and initialization-only information. The
reference is the coupled dense run; error should remain negligible relative
to independent dense-run variability. Counts distinguish moving state
n(d+1)+1+2(L-1)mnq from (L-1)n^2 fixed mixers. No bit, setup-time or total
subquadratic-storage conclusion is inferred from a moving-state result.

First assess the exact published residual-clock, constant-prefix construction.
Any change of clock, prefix, history basis or tail handling must be labeled
as a modified Legendre construction, not a proof of the unchanged scheme.
No stored future trajectory, oracle forcing, hidden dense learned matrices,
or scope weakening is allowed. New theory and bounded independent analysis
are authorized; experiments, paper changes and commits are not requested.

## Work and check plan

- Lead: reconstruct the exact projection-error/stability chain and test whether
  physical-time analyticity can supply a usable sharper source estimate.
- Scoped fresh reader: analyze the current clock/prefix for genuine regularity
  obstructions; distinguish an approximation obstruction from a prediction
  lower bound.
- Scoped fresh reader: investigate a minimally modified Legendre realization
  with an analytic temporal basis and explicit finite retained state.

Stop this bounded assessment at a proved improvement or an explicit remaining
bridge; do not claim that a source approximation alone proves runtime accuracy.
Scientific notes and any review stay in this flat folder. Generated scratch,
if needed, belongs in data/generated/legendre_analytic_history_20261009/.
The paper and existing concurrent changes remain untouched.

## Clarified contract (current)

The user explicitly excludes data-adapted bases or data-dependent coefficient
compilation: the target is the oblivious Legendre temporal-memory method,
not another initialized response-subspace method. Ordinary training-gradient
and online response evaluations are still the original model's operation.
Prescribed temporal bases and their schedules may use the stated problem
parameters, but must not be chosen from a dataset's response directions or
dense trajectory. The investigation now continues under this stricter
contract, without editing the paper.

`RESULT.md` records a mathematically valid candidate using a fixed,
initialization-compiled response subspace, but that candidate is **outside
the clarified target** and is not the answer to the user's question.
`SOURCE_CHECK.md` and any accompanying independent check concern validity
of that separate candidate only, not its admissibility under this contract.
`CLOCK_ANALYSIS.md` remains relevant to the unchanged online scheme.

## Current online candidate

`OBLIVIOUS_WINDOWS.md` now contains the data-oblivious temporal construction,
including a final single-growing-interval version with one order q. Its
only learned hidden arrays are online Legendre moments, not adapted
directions. A Volterra contraction defines initialization without an
artificial prefix. An exact quadratic projection defect and signed comparison
give polylogarithmic order; a prescribed readout-only tail gives exact fitting
and full-trajectory sphere accuracy. The basis and schedule use only theorem
qualification parameters. This is a finite-state evolution with a regular
zero-time branch and deterministic hybrid tail switch, not an assertion of a
globally locally-Lipschitz vector field at every clock state.

Root reconstructed and checked the new bridge and assembled the global
single-interval corollary. Two separate readers checked its runtime and
source/parameter interfaces: `OBLIVIOUS_RUNTIME_CHECK.md` and
`OBLIVIOUS_SOURCE_CHECK.md` both passed the frozen mathematical candidate
`7cd8051dda86a6bc7bee09cd46ab51ddce1fb8d21f7891f97148e34cc6137298`.
Their contexts were reused from the earlier different-candidate checks;
they did not author this construction or read one another's reports. Root
accepted their arguments after checking the source matches and incorporated
the requested wording clarifications (eventual probability qualifier and
explicit dense operator margin). The imported source probability theorem
was not independently re-proved in this bounded investigation.

Status: **internally checked, not promoted**. The final single-interval
version has q = O(log(en)^(5/2)) and exactly
`n(d+1)+2(L-1)mnq+1` learned coordinates. Its all-time full-sphere error is
eventually at most `Y/n`, hence negligible relative to the paper's actual
dense-variability lower bound. The original activation class, fixed depth,
general data, positive gap and label cap are unchanged. The fixed dense
mixers remain quadratic; no numerical step-size, runtime-speed or practical
threshold claim is made. The later `ORIGINAL_METHOD_RESULT.md` now rules
out this smaller order for the unchanged residual-clock equations over the
full original activation/data scope, without contradicting this modified
construction.

`OBLIVIOUS_RESULT.md` is an auxiliary small-positive-prefix variant, not
the chosen zero-prefix construction. `ANALYTIC_VARIANT.md` contains other
exploratory routes and is not the final result. No paper or experiment
changes and no commit were requested or performed. The current continuation
reports the unchanged-method obstruction above; paper integration would
require a subsequent user request.
