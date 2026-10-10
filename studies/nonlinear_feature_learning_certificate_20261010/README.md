# Nonlinear feature-learning certificate for the compression setting

Date: 2026-10-10.

## Approved book promotion — integrated

The user requested the final compact-paper theorem and shortened proof as one
complementary section, **“Nonlinear feature learning preserved by compression,”**
in Chapter 9, *Complete-trajectory compression*. The independent
[selection report](PROMOTION_SELECTION.md) accepts this placement immediately
before the existing headline assembly. The user approved the exact reviewed
v3 package on 2026-10-10: “ok great, then I approve the promotion”.

The complete approved addition is [PROMOTION_SECTION.qmd](PROMOTION_SECTION.qmd).
It reuses the book's fitting lemma and the three absolute approximation
propositions, uses the canonical stored readout and explicit finite RMS
normalizations, and retains all local activity assumptions and early-time
qualifications. Only `paper/feature_learning_theorem.tex` and the final
`paper/compact_feature_learning.tex`, with their setup/fitting dependencies,
are source arguments; superseded study and long-paper proofs are excluded.
It is now incorporated in `docs/08b-trajectory-compression.qmd`, starting at
line 4493, under `sec-compression-nonlinear-learning`. The chapter is unchanged
outside this exact insertion; the paper and global notation are unchanged.

Promotion evidence is retained under
`data/generated/nonlinear_feature_learning_certificate_20261010/`:

- `promotion_v1/review_inputs/`: frozen complete mathematical review packet,
  neutral [assignment](PROMOTION_REVIEW_ASSIGNMENT.md), and input hashes;
- `promotion_v3/`: standalone full `docs/` and `code/` edition with the single
  insertion, assembled by [assemble_promotion.py](assemble_promotion.py);
- `promotion_v2/review_inputs/`: the same scientific text with ten blank lines
  added around five Quarto proof fences. `diff -B` against v1 is empty. The
  original v1 packet is unchanged;
- [check_promotion.py](check_promotion.py): insertion-preservation, frozen-input,
  full HTML local-target/fragment, identifier, and export checks;
- [integration assignment](PROMOTION_INTEGRATION_ASSIGNMENT.md): used by a
  fresh reviewer, separate from the selector and scientific reviewers.

Candidate v1 SHA-256:
`c04cc608c43cc0c402db40b1f0d4241e71a65eb9cd70bed5dcc18aff82fc307f`.
Formatting-corrected v2 SHA-256:
`6c9baf447fe55e2cfeeab935394e65e62f650673f2131196bcb15980daf87708`.
Final presentation v3 SHA-256:
`a6627f8f435d94714a2496bacd5842c810a893e17496168ee695ecdb44a57ed3`.
Relative to v2, v3 adds invisible TeX grouping around one norm interior to
prevent an inappropriate automatic line break, and removes a duplicate
“Equation” prefix before a native reference. Removing exactly these
typographic changes and blank lines reproduces v1 byte-for-byte linewise;
no scientific claim or proof step changed.

Two fresh complete mathematical promotion reviews,
[A](PROMOTION_MATH_REVIEW_A.md) and [B](PROMOTION_MATH_REVIEW_B.md), independently
read all 6,441 lines of the frozen packet and returned scientific PASS with
no required scientific corrections. Their original reports retain exact
hashes, read coverage, attacks, scope and isolation declarations. The
coordinator read both reports completely. They are reviews of v1's scientific
text; subsequent presentation-only repairs are assigned to the separate
integration reviewer, not silently included in their verdicts.

The fresh [integration review](PROMOTION_INTEGRATION_REVIEW.md) returned PASS
for the final v3 edition, with no required corrections. The reviewer checked
all new content, scoped older interfaces, actual HTML/LaTeX formal structures,
and every new-section PDF page. Its exact older read/unread coverage is
recorded; this is not a new whole-book proof audit. Browser-layout screenshots
were unavailable, so visual inspection used the PDF and HTML was checked as
actual markup, references and links. The coordinator read the complete report.

The standalone edition is an exact insertion; all 104 frozen edition inputs
retain their hashes. The full HTML/PDF/editable-LaTeX render succeeded,
the complete link/fragment checks report no errors, and PDF integrity checks
pass. [PROMOTION_VALIDATION.md](PROMOTION_VALIDATION.md) records commands,
environment, hashes, presentation-only version changes, outputs and limitations.
The concrete preview is
`data/generated/nonlinear_feature_learning_certificate_20261010/promotion_preview/proposal-preview.pdf`.

Selection, paired complete scientific review, independent integration/
edition validation, user approval, and live correspondence gates are complete.
The live chapter is byte-for-byte identical to the approved assembled chapter,
with SHA-256
`5d068eaac00fe6b6ec8149e13d5320dc6c40f6935a7c2e467ab55e38abaf5bb8`.
All 104 live book/code inputs match the rendered v3 edition. A separate
read-only correspondence checker independently confirmed this agreement.
The edition checker was rerun successfully (18 HTML pages; no errors), and
the scoped Git whitespace check passed. No new scientific change or review
was needed. The integration and this approval record are committed together;
see the chapter's Git history for the integration commit. Generated editions
remain outside Git. Details and exclusions are in
[PROMOTION_VALIDATION.md](PROMOTION_VALIDATION.md).

## Current paper integration

The user subsequently requested one additional theorem and proof in the paper.
Its statement is `paper/feature_learning_theorem.tex`. Following the latest
compact-only shortening request, `compact.tex` uses
`paper/compact_feature_learning.tex` for the proof. The obsolete `main.tex`
still uses the unchanged longer `paper/feature_learning_proof.tex` and
`paper/feature_learning_initialization.tex`. The main compression theorem
and its rates are unchanged.

The additional theorem assumes nonaffine activations and excludes parallel
and antiparallel training inputs. It proves nonvanishing early-time gaps from
all affine predictors and from the dense reference's frozen initial NTK,
motion of every dense hidden layer, and motion of the nonlinear-in-input
part of its first-layer features. Activation values may remain unbounded.
Taylor's input-nonlinearity conclusion uses at most four extra deterministic
passive inputs declared at initialization without labels; its panel count
becomes at most `p+4`, with the same storage exponents.

The paper proof supersedes the earlier trained-population-flow dependency:
finite Gaussian conditioning at initialization gives joint empirical limits
with second moments, and a direct finite-width real-time bootstrap plus a
truncated bounded-multiplier estimate supplies the strong uniform remainder.
No trained population-flow theorem is imported. The source modules are
[INITIALIZATION_MODULE.md](INITIALIZATION_MODULE.md) and
[DIRECT_REMAINDER.md](DIRECT_REMAINDER.md); the typeset shared sources contain
the fully assembled argument. Earlier population-dependent notes below are
the history of the investigation, not additional paper dependencies.

### Original integration checks and compiled artifacts

Two fresh scoped adversarial reviews checked complementary parts of the
assembled proof: [input nonlinearity and increments](AUDIT_PAPER_INPUT.md)
and [initialization and dynamics](AUDIT_PAPER_DYNAMICS.md). Both found the
new arguments valid within their assigned scopes. Their union covers the
new certificate; the inherited compression approximation theorems remain
supplied inputs, not a fresh re-review of the entire manuscript. The Taylor
query set is now explicitly augmented in the theorem itself. After review,
the coordinator removed the redundant alternate transfer sentence invoking
a dense upper estimate: the displayed vanishing absolute errors suffice.
No mathematical assertion changed in that final cleanup.

Final shared-source SHA-256 values:

- theorem: `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f`;
- proof after that two-line deletion:
  `0a1daaa8085fb89bb4f7c8e0fb18ff729dee30011ece0c5d9f06bccb3fbcc13c`;
- initialization: `f132f884304c09f32759ec63baba5bc8be056944baf514200141e597399e9ff2`.

Both manuscripts compile with `latexmk -pdf -interaction=nonstopmode
-halt-on-error` in
`data/generated/nonlinear_feature_learning_certificate_20261010/paper_build_19s6aj/`.
The final logs contain no undefined references, multiply defined labels,
LaTeX warnings or overfull boxes. The theorem/proof pages were checked as
extracted text and rendered images. The shared proof adds approximately nine
pages: the compact copy is 58 pages and the complete manuscript 226 pages.
The resulting PDFs are copied to `paper/compact.pdf` and `paper/main.pdf`;
the pre-integration PDFs are preserved as `prior_compact.pdf` and
`prior_main.pdf` in that build folder. The compact notation inventory has
30 persistent symbols, adding only the frozen-kernel predictor.

These are author results with scoped independent checks, not formal
verification or book promotion. No training experiment or Git commit was
performed. Other tasks' source and experiment changes were left untouched.

### Compact-only proof shortening

The subsequent request authorized shortening only this newly added theorem's
proof in the compact paper. The theorem source is unchanged. The only change
to the compact entrypoint is replacing `\input{feature_learning_proof}` with
`\input{compact_feature_learning}`. All preceding proof sources, the assembly,
the obsolete main manuscript and its longer proof sources remain unchanged.

The shorter argument replaces the full forward-acceleration analysis with a
scalar adjoint identity. Testing each layer's actual feature increment against
its initial backward response telescopes into a positive sum of hidden-block
acceleration energies. This proves layerwise feature motion and supplies the
label-contracted kernel increment needed for the cubic frozen-NTK gap. Only
the forward and backward Gaussian passes remain; the third pass, a full
matrix-valued kernel expansion, and unused expectation/uniform-integrability
claims disappear. The existing compact fitting lemma supplies the real bounds
and finite-query initial convergence, avoiding a repeated bootstrap. The
deterministic empirical second-moment limits and strong small-time remainder
are retained, including for unbounded activation values.

Supporting derivations are [SHORT_INITIALIZATION.md](SHORT_INITIALIZATION.md)
and [SHORT_ADJOINT.md](SHORT_ADJOINT.md). Two fresh scoped checks found no
required correction: [the proof audit](AUDIT_SHORT_PROOF.md) independently
checked the replacement argument, and [the preservation
audit](AUDIT_SHORT_PRESERVATION.md) compared it with the complete older proof
and theorem. They retain the preceding fitting result and stated compression
accuracy bounds as dependencies; this is not a fresh audit of the entire
compression paper or book promotion.

The proof source shrinks from 706 lines / 3,880 whitespace-delimited words
across the two old files to 335 lines / 1,891 words. The compiled compact paper
shrinks from **58 to 53 pages**, without layout changes. The proof starts on
page 48 and now ends on page 52 rather than page 57. All theorem conclusions,
probability quantifiers, activation qualifications and the four-input Taylor
augmentation are preserved.

The reviewed new proof has SHA-256
`71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1`.
The build and before-edit snapshots are in
`data/generated/nonlinear_feature_learning_certificate_20261010/short_proof_DLIOrk/`.
`latexmk -pdf -interaction=nonstopmode -halt-on-error` succeeds with no
LaTeX warnings, undefined references, multiply defined labels or overfull
boxes. Rendered proof pages were visually checked. The checked 53-page PDF is
copied to `paper/compact.pdf`. Byte comparisons against the before-edit
snapshot and hashes confirm that older paper content is unchanged. The Git
index was left untouched; no commit was requested or made.

### Requested rigorous re-audit

The user then requested a fresh rigorous audit of the new theorem and its
shortened proof. The [coordinator's detailed re-audit](REAUDIT.md) rechecks
every conclusion, the full fitting dependency, the Gaussian row-law argument,
strong small-time probability quantifiers and the compression transfer.
It includes a separate finite-width derivative reconstruction of the cubic
coefficient. No mathematical error or required correction was found in the
audited scope. The prior three compression accuracy theorems are supplied
inputs, not themselves re-audited in this round.

A fresh scoped review of initialization and nonaffinity is retained in
[REAUDIT_INITIALIZATION.md](REAUDIT_INITIALIZATION.md). The audit records
reviewer provenance explicitly: a separate dynamics review was stopped after
accidental exposure to earlier verdict summaries and is not counted as an
independent audit; its [disclosure](REAUDIT_DYNAMICS.md) is preserved. The
coordinator completed the dynamics checks directly. No paper source or PDF
was changed, no experiment was run and no Git operation was performed.

## Question and scope

Determine whether the assumptions shared by the paper's Legendre, Harmonic,
and Taylor compression theorems imply both of the following for the coupled
dense gradient flow:

1. hidden representations move at a nonvanishing width-asymptotic scale,
   preferably in every hidden layer; and
2. the trained predictor separates quantitatively from the frozen-initial-
   tangent-kernel trajectory.

The canonical system is the paper's width-`n`, fixed-depth dense network with
Gaussian initialization, zero readout, mean-square loss, mobilities
`(n,1,...,1,n)`, fixed sphere data, analytic activations with bounded strip
derivatives (values may be unbounded), positive top population feature-Gram
gap, fixed nonzero labels, and the paper's small-label condition. The target is
a finite positive-time lower bound in probability as `n` tends to infinity;
mere nonzero finite-width motion does not certify a feature-learning regime.
The investigation also asks for the strongest useful consequences for the
compression paper. The latest user request authorizes the paper theorem and
proof addition described above. No experiment, book promotion or Git operation
is part of this integration.

This is a new study because it asks for a mechanism certificate not supplied by
the trajectory-compression theorem. Permitted scientific inputs are the current
paper, the maintained `docs/` notation and reading guide, and this study's own
artifacts. Other studies are not inputs.

## Claim ladder and falsifiers

- Exact: derive the first nonzero time derivatives of hidden features and of
  the difference from the same-initialization frozen-kernel flow.
- Universal theorem: decide whether the paper's present assumptions force
  positive limiting coefficients.
- Corrected theorem: if the universal statement is false, identify the weakest
  explicit nondegeneracy condition under which the derivative lower bounds and
  analytic remainder estimates yield actual positive-time feature movement and
  frozen-kernel separation.
- Strong extension: decide whether every hidden layer can be certified rather
  than only one layer.

An admissible affine activation falsifies a universal input-nonlinearity claim.
A data/activation/label symmetry that makes a limiting hidden-force coefficient
zero falsifies a universal nonvanishing feature-motion claim. A positive initial
derivative without a width-uniform time remainder is not sufficient evidence.

## Result and status

The universal claim is false. An antipodal two-sample problem with equal
labels and analytic, nonaffine activations has a positive top feature-Gram gap,
yet every hidden layer has vanishing width-limit motion over the complete
training trajectory and the dense predictor converges uniformly in time to
its frozen-initial-kernel trajectory. Thus the failure is not caused merely by
allowing affine or constant activations.

The study also proves an exact finite-width identity: the label-direction
cubic departure from the frozen-kernel trajectory equals one third of the
sample count times the squared initial hidden acceleration. This identifies
the extra response nondegeneracy that a valid positive theorem would need;
the current feature-Gram gap does not imply it.

- [Complete result and proof](RESULT.md)
- [Fresh reconstruction and adversarial check](CHECK.md)

Status: author-derived and internally reconstructed. No independent review or
promotion has been performed.

## Corrected compatible-data result

If compatibility is strengthened to exclude parallel and antiparallel
training inputs, and every activation is analytic and nonaffine, the negative
example is excluded and a positive arbitrary-fixed-depth theorem holds.
Every hidden parameter block and every hidden layer's joint training-feature
tuple has positive order-\(t^2\) motion; the dense prediction separates from
its frozen initial kernel at order \(t^3\); and every activation retains a
positive best-affine-fit error on a common initial interval. Gaussian
second-moment normalization fixes scale but is not the source of positivity.

- [Compatible-data theorem and proof](COMPATIBLE_RESULT.md)
- [Internal reconstruction and boundary checks](COMPATIBLE_CHECK.md)

The result is author-derived. Fresh scoped independent checks have now
examined initialization activity and fixed-time transfer. They found and
repaired the unjustified smooth-\(L^2\) assertion; the theorem uses strong
directional expansions instead. The source population theorem is maintained
book material and was not independently re-proved by those scoped checks.
No promotion has been performed.

- [Initialization/adjoint audit](AUDIT_ACTIVITY.md)
- [Fixed-time and normalization audit](AUDIT_TIME.md)
- [Independent label-superposition derivation](LABEL_SUPERPOSITION.md)
- [Compression consequences and recommended paper insertion](COMPRESSION_CONSEQUENCE.md)

The new consequence is unchanged-storage compression with vanishing error
but nonvanishing separation from the dense reference's frozen initial kernel.
It also preserves a strict early-time training-MSE improvement over that
kernel and a nonzero label-superposition defect. The latter rules out any
single label-linear predictor approximating both the original labels and
their halves, not all possible label-dependent kernels. The activity conditions
are attached to this corollary, not imposed on the broader compression theorem.
At that stage, self-contained paper integration would have required the
local population proof module. The direct finite-width argument in the
current paper integration removes that dependency entirely.

## Input nonlinearity versus deep linear feature learning

The latest continuation distinguishes moving-kernel feature learning from
genuine non-affinity in the raw input. The initial population prediction
velocity is non-affine for every nonzero label vector under the same
nonparallel-input and nonaffine bounded-derivative activation assumptions.
The proof uses positive monomial kernels after removing affine components;
their Gram matrices approach the identity at high degree. It applies to
unbounded activation values and does not impose nonlinear target labels.

A width-uniform real first-order remainder transfers this to a fixed early
time. Four deterministic passive inputs suffice to witness the separation
from every affine predictor. Legendre and Harmonic already cover them;
Taylor may append at most four predeclared passive inputs, changing `p` to
at most `p+4` and preserving its `log(n)^3` storage exponent. Combining with
the prior feature-learning certificate gives simultaneous separation from
deep linear predictors and frozen-initial-kernel dynamics. This does not
assert that the nonlinear component of every hidden feature moves.

- [Complete combined statement and new proof](INPUT_NONLINEARITY_RESULT.md)
- [Independent prompt-only input-kernel derivation](INPUT_KERNEL_LEMMA.md)

Status: author-derived with independent scoped derivations and checks. The
fresh reports `AUDIT_INPUT_KERNEL.md` and `AUDIT_INPUT_TIME.md` found no
substantive defect in their respective kernel/witness and time/transfer
components. Their explicit m>=2 qualification, event-intersection wording,
and logarithmic-exponent clarification were incorporated. The coordinator
read both reports completely and rechecked the displayed derivations. The
inherited local-population feature-learning dependency remains separately
identified; these are not full promotion audits of that dependency.

### The nonlinear part of the features actually changes

The supplemental [nonlinear feature-increment proof](NONLINEAR_FEATURE_INCREMENT.md)
rules out a frozen nonlinear feature component merely accompanied by an
affine-in-input first-layer change. After removing the best affine increment
separately for every first-layer neuron, the average squared feature increment
is bounded below by a positive constant times t^4 at every sufficiently small
fixed positive time, with probability tending to one as width grows.

Its elementary lemma says that phi'(g dot v)(r dot v) cannot be affine on a
sphere of dimension at least one when g and r are nonzero and phi is analytic
nonaffine. The proof works on the span of the training inputs, so it adds no
input-rank assumption. Scoped agent `nonlinear_feature_increment` independently
proved the lemma and product-L2 positivity, then checked the strong-time and
Wasserstein-2 transfer. The maintained local theorem uses the uniform path
norm as that transfer requires. Only fixed positive times are claimed.

This strengthens first-layer activity, not every layer's nonlinear-increment
claim. It does not identify dense features with compressed internal coordinates
or establish nonaffinity of the output difference from the frozen kernel.
The compressed prediction separations themselves remain those in
`INPUT_NONLINEARITY_RESULT.md`, including the four-input Taylor qualification.

No paper changes, experiments, book promotion or commits were made in that
earlier continuation. Its proposed next step was a short joint
nonlinearity/feature-learning corollary with the complete supporting proof
dependencies in its appendix; the latest user request now authorizes it.

Coordinator's final source check on 2026-10-10 used these SHA-256 versions:
`INPUT_NONLINEARITY_RESULT.md`:
`95bc820696553dbdae88693c2c01b246a279e35c8c839d3459a4f332e114e5bf`;
`NONLINEAR_FEATURE_INCREMENT.md`:
`f622b9f254f282c2f9d3534b23c5186eaa4992b953e86ee66908a2920f182bb2`.
The check comprised algebraic reconstruction, the independent scoped reports
described above, and a scoped whitespace check; no numerical experiment was
used as proof evidence.
