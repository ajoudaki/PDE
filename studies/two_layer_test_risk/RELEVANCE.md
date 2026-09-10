# Independent relevance and placement selection

Selector: `relevance_selector`, 2026-09-10. This is a relevance decision under
RESEARCH_WORKFLOW Part 2, step 1. It is not a correctness review, a paired
promotion audit, approval to change established material, or authorization
for further research. The selector did not author or assemble the result;
the declared authors/assembler are `root`, `cubic_derivation`,
`matching_remainder`, and `quadrature_check`.

## Decision

**NARROW — accept for assembly as one proof-only extension of
`docs/global_nonlinear.md`, immediately after C.3.** A suitable working title
is “C.4. A controlled local risk expansion at equal training loss.” Keep its
fixed two-hidden-layer tanh, three-angle, whole-circle contract explicit.
Do not present it as a signed test-risk improvement or a generalization
theorem. The complete signed theorem remains unqualified for promotion:
the exact coefficient's sign and nonvanishing are unresolved.

The partial result merits preparation now because it makes an additional
mathematical connection that the current book does not supply. It compares
the learned and frozen predictors on a continuous passive-input set after
matching their training losses, and controls the resulting risk error by a
fourth-order remainder on the actual population flow. Its coefficient is a
finite integral of initialization quantities, with both matrix responses
retained. That is a usable reduction of a trajectory question; it does not
require the future learned path as an input. A rigorous sign enclosure would
then settle the stated local comparison without another trajectory argument.

This recommendation is for assembling and independently reviewing that exact
partial theorem. It neither presumes that the source arguments will pass the
required reviews nor recommends immediate integration.

## Scientific value and duplication

The current reading guide explicitly identifies passive inputs and the
connection to out-of-sample risk as the next explanatory question
(`docs/README.md`, “Beyond fixed depth and a fixed dataset”). Its list of
established chapter roles contains no equal-training-loss risk expansion for
this nonlinear model. The following comparison isolates the increment.

| Current coverage | Proposed increment | Placement consequence |
|---|---|---|
| Global nonlinear C.1–C.2 construct the local strong flow and capture finite GF and every deterministic vanishing raw-GD mesh, including specified fixed probes. | The exact first-layer spanning identity and uniform angular continuity extend these probes to the whole circle and transfer their convergence to the specified integrated risk. | Use C.1–C.2 as existing premises, then prove the compact-input corollary in the new subsection. Do not restate the full width theorem. |
| C.3, including its weighted correction, supplies positive activation/response Grams, nonzero hidden onset, the changing training kernel, and persistent local nonaffinity. | The moving-versus-frozen predictor subtraction identifies its cubic coefficient, while matching loss produces a positive cubic clock shift and removes the leading training-speed contribution. | This is the main scientific increment. Refer to C.3 for the activity and Gram facts; do not reproduce an additional tanh strict-activity theorem. |
| Gaussian calculus Sections 1–3 and global nonlinear Section 3 provide the exact reused-matrix conditioning and source-response identities. Finite moving jets in Section 7.1 and Appendix E retain all trained blocks and moving residuals. | The scalar coefficient is explicitly reduced to initial lower/upper Gaussian moments, including the response-mean product, and to one teacher projection. The integral-equation bootstrap supplies a uniform positive-time remainder. | Include the concrete contraction and remainder proof. Do not promote a duplicate finite-jet method or identify finite jets with a population Taylor theorem. |
| Finite dynamics Sections 1–4 give exact raw gradients, kernel blocks, dissipation and width-independent norm control under their hypotheses. | Local inverse loss matching and risk convergence add a comparison observable. | Keep the new result near C.3, where its population hypotheses are discharged, rather than in the finite-dynamics foundation. |

In particular, the identity

\[
 p^\top(J_{\rm train}-\beta a_{\rm train})=0
\]

is scientifically informative even before the risk coefficient is signed.
It identifies the component eliminated by matching training progress and
shows why positive hidden energy alone cannot settle the test-risk question.
The additional teacher projection is the necessary discriminator. The
selection does not claim that this observation rules out every alternative
explanation or demonstrates beneficial feature learning.

## Exact useful scope

The assembled theorem should retain all of the following, together with
their full proofs and assumptions:

1. The canonical stored-weight model with two tanh hidden layers, no biases,
   Gaussian initialization variances `(1, 1/n, 1/n^2)`, unit multipliers and
   raw block mobilities `(n, 1, n)`, and the mean squared training loss.
   The normalized circle inputs have angles `0, pi/5, -pi/5`, labels
   `1, (1-sqrt(5))/4, (1-sqrt(5))/4`, and passive teacher `cos(3 alpha)`
   under uniform circle measure. The original rank-two input Gram is retained.
2. The actual locally constructed population flow and its frozen-feature
   readout comparison from the same limiting zero readout; the frozen
   residual remains dynamic. Establish the unique loss-matching clock and
   the shared positive interval explicitly from the local flow and frozen
   positive activation Gram.
3. The uniform cubic predictor comparison, the cubic clock shift, and the
   bound
   `|R(g_tau(t))-R(f_t)-chi t^3| <= M t^4` on a positive interval, for a
   finite fixed-model constant `M`. State that no numerical radius or width
   threshold has been evaluated.
4. The explicit initialization-only expressions for `J`, `beta`, and `chi`,
   including both trained hidden blocks, the readout correction and the
   reused-transpose mean-product term. Supply the singular-passive-slot
   justification and the uniform fixed-direction fourth-moment estimates
   used by the integral bootstrap. No inverse of the original input Gram
   or of a singular passive covariance is available.
5. The two training normalization identities and the conditional implication
   from either rigorous strict sign of `chi` to the corresponding local risk
   inequality. State directly that cubic is the first possible term and that
   `chi=0` is not excluded.
6. The whole-circle prediction/risk capture and the exact finite-width
   boundary: retain the actual small random initial readout, assert finite
   matching only on fixed `[delta,T]` with `delta>0`, and transfer a sign
   only conditionally on its population proof. Preserve the in-probability,
   local-horizon, every-vanishing-GD-step scope without a width rate or a
   claim uniform down to zero time at finite width.

These assumptions are concrete and compatible with the repository's main
mechanism: both hidden blocks train, the data remain correlated and rank
deficient, and the same Gaussian connector is used in both directions.
Tanh boundedness and smoothness, zero limiting readout, fixed geometry and
fixed teacher are substantive restrictions. Do not broaden the theorem to
arbitrary datasets, activations, teachers, depths, horizons, or initialization
regimes during assembly; that would require new scientific work.

## Material to retain only in the study

- The approximate positive coefficient, resolution table, campaign-specific
  quadrature driver and generated arrays. QUADRATURE reports a last relative
  change of about 1.69 percent against a 1 percent trigger and no error
  enclosure. Its numerical conclusion is explicitly inconclusive. Passing
  contraction identities does not supply integration accuracy.
- Duplicate proofs of positive hidden displacement, activation nonaffinity,
  kernel activity and the finite moving-flow jet algorithm. The relevant
  facts are already maintained in C.3 and the calculus chapter. A short
  hypothesis check for this witness is sufficient in the candidate.
- Research chronology, author check records, alternative notation layers and
  unexecuted future plans. They are useful provenance, not theorem premises.

In particular, a displayed numerical value must not quietly serve as a
nonzero example in the proposed theorem. Neither `chi>0` nor `chi!=0` has
been supplied by the stated sources.

## Maintenance cost and smallest destination

One C.4 subsection is the smallest suitable destination. Its proofs can
reuse the maintained C.1–C.3 flow, Gaussian identities and positivity results;
the new material should contain the passive-circle argument, the fixed
initial moment estimates, the integral remainder bootstrap, the explicit
coefficient contraction, and the clock/risk calculation. A separate chapter
would fragment closely dependent local theory. A code module is not justified
by this scope: there is no maintained reusable numerical contract or certified
integrator being proposed.

The maintenance cost is moderate if the two author proofs are combined into
one notation-consistent argument and their duplicated setup is removed. It
would be excessive if all four source reports, their empirical recipes and
the already-established strict-activity argument were copied into the book.
The finite expectation formula is intrinsic to this theorem's usefulness;
reducing the addition to an unspecified coefficient and an `O(t^4)` statement
would leave too little distinct content.

Use the canonical layer-indexed readout/operator notation and a single name
for each coefficient. In particular, the two source meanings of `J` and
the pairs `gamma/beta`, `C_Delta/chi` must be reconciled. Avoid plain `Delta`
for the risk difference because NOTATION reserves it for a proof mesh;
writing the difference of the two risk functionals is sufficient. The guide
needs at most one precise addition to the existing global-nonlinear row,
describing a local equal-loss expansion with unresolved sign. Its statement
that a generalization theorem is not established should remain accurate.

The named gap for the full desired theorem is a rigorous nonzero signed
bound on the exact `chi`, including propagated Gaussian and angular
integration errors if numerical certification is used. This report does
not reopen the stopped computation or request a new proof search.

## Coverage and independence record

Read in full: root AGENTS and both workflow parts; RESULT,
CUBIC_DERIVATION, MATCHING_AND_REMAINDER and QUADRATURE; docs README and
NOTATION; global nonlinear Sections 3.1–3.4 and complete C.1–C.3 including
the weighted correction; finite dynamics introduction and Sections 1–4;
Gaussian calculus introduction and Sections 1–3, Section 7.1, and Appendix E
including E.1. Truncated tool output was repaired by bounded rereads.
Chapter heading/text searches were used only to locate the relevant coverage.

Required skills read in full: `solve-math-rigorously/SKILL.md` and
`investigate-conjectures/SKILL.md`, with research-contract, evidence-ledger
and adversarial-audit references. No external result was imported.

Unread complement: other study reports/history and reviewers' findings;
unrelated chapters and the remaining sections of the three inspected
scientific chapters; implementation code, tests and numerical producer/arrays.
This was the assigned placement assessment, so no code audit or empirical
reproduction was performed. No maintained API was used or changed. No Git
operation was performed. The only write is this report.

The input hashes observed for this selection are:

| Input | SHA-256 |
|---|---|
| AGENTS.md | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| RESEARCH_WORKFLOW.md | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| docs/README.md | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| docs/gaussian_calculus.md | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| docs/finite_dynamics.md | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| RESULT.md | `845374726a1a378c3edd922a0e3b9ffc86e60c91cc191013deea96f11f815139` |
| CUBIC_DERIVATION.md | `3f46c878a77dd046c876d5195950f6262b3db06a025cb756518643f4c97ca495` |
| MATCHING_AND_REMAINDER.md | `ebefcae59267dd14a71d4e93e3a287126471f178a42646fe60b5abd45894157d` |
| QUADRATURE.md | `54bcd350546353dca2282bdb2418768d0c153be62c84f9df0990927481d3a266` |
