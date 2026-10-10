# Independent promotion selection

Date: 2026-10-10. Selector: `/root/promotion_selector`.

## Decision and destination

**Accept for assembly**, limited to one complementary section titled
**“Nonlinear feature learning preserved by compression”** in Part II,
*Observable closure and approximation theory*, Chapter 9,
*Complete-trajectory compression*, `docs/08b-trajectory-compression.qmd`.

Insert the complete section immediately after the Taylor construction and
its proof, before the existing `sec-compression-assembly` section (currently
line 4493). At that point the initialization/fitting lemma and all three
absolute approximation bounds are available. The existing headline theorem
can retain its present assumptions and its concluding assembly. No new
chapter, part, or parallel account in the learning chapters is warranted.

This is the relevance and placement gate only. It permits preparation of a
complete candidate; it is neither a proof-review verdict nor authorization
to change the established book. The paired complete reviews, integration
review, edition validation, and concrete-package approval remain separate.

## Distinct value and useful scope

Chapter 9 already establishes autonomous compression of complete prediction
trajectories. Its existing statements do not certify that those predictions
remain distinguishable from affine predictors or from training with the
coupled dense reference's initial tangent kernel. The proposed addition
answers that specific mechanism-preservation question in the same finite
network, initialization, metric, loss, and physical time as Chapter 9.

The proposed conclusions earn their place together:

| Conclusion | Scientific role and exact scope |
| --- | --- |
| Distance at least a positive fixed-problem constant times $t$ from every affine input predictor | Certifies input nonaffinity of each compressed predictor on its promised query domain. Frozen nonlinear features could also produce this property, so this conclusion alone is not a feature-learning certificate. |
| Distance at least a positive fixed-problem constant times $t^3$ from the coupled dense reference's frozen initial kernel predictor | Detects the effect of hidden learning in the compressed predictions. With the chapter's exactly zero initial readout, this comparator is precisely dense readout-only training with the initial hidden features fixed. |
| Dense training-feature displacement at least a positive fixed-problem constant times $t^2$ in every hidden layer | Supplies an internal certificate for the dense reference. The norm aggregates the training samples and neuron coordinates; it does not assert that every sample or every neuron moves. |
| First-layer dense feature increments have positive affine-projected squared size at least a constant times $t^4$ | Rules out an explanation based solely on an affine change of the first-layer feature map. The projection is on the unit sphere of the training-input span, averaged over neurons. |

Here $t$ is physical time and the constants are independent of width.
The claims hold with probability tending to one as width tends to infinity
for every separately fixed $0<t\le t_*$, where $t_*>0$ depends on the
fixed problem. These are early-time certificates. They neither assert
endpoint separation nor provide a uniform compressed-model lower bound for
arbitrary times tending to zero with width. They do not compare test risk,
matched-loss performance, or rates of fitting.

The final shortened argument is well matched to this role: it uses the
chapter's real fitting bounds, initialized Gaussian forward/reverse
conditioning, and an adjoint pairing of actual feature increments. Its
cubic coefficient is a sum of nonnegative hidden acceleration energies.
It does not require constructing a trained population flow or importing a
width-independent complex-time radius. Complete proof verification of these
steps belongs to the subsequent reviews.

## Existing coverage and duplication

The scoped search found closely related mechanisms, but no existing result
with the proposed compression conclusion and scope.

| Maintained passage inspected | Overlap | Reason to retain the proposed section |
| --- | --- | --- |
| Chapter 9, setup, fitting lemma, three approximation statements, and dense variability statement | Zero-readout dynamics, small-label fitting, vanishing prediction errors, and a positive-time comparison between independent dense runs | Dense-run variability is a different comparator; the existing lower bound does not establish separation from affine or frozen-kernel predictors. Reuse these existing results rather than repeat their proofs. |
| Chapter 1, “Sin-plus-cosine initialization and exact initial coefficient geometry” (`sec-docs-special-data-limits-l24007`) | Positive initial Grams and hidden coefficient energies, including a doubled label-direction kernel coefficient | This is a specific three-hidden-layer initialization calculation, expressly without a trajectory remainder. It cannot replace the proposed actual-time certificate. |
| Chapter 10, “Genuine nonlinear feature learning at every layer” (`sec-docs-global-nonlinear-l1531`) | Initial adjoint calculations, quadratic hidden motion, kernel change, and stronger later-time statements in its model | It concerns the separate one-input shifted-arctangent population construction. It does not cover the proposed fixed correlated dataset and compressed predictors. |
| Chapter 12, “Odd initial motion, endpoint obstructions and Gaussian normalization” (`sec-docs-special-data-limits-l17432`) | Positive hidden acceleration energies and adjoint sums for an odd activation and correlated pair | Its raw model, two binary labels, activation class, and population/feature-time scope differ. The proof mechanism is related, but the theorem is not a duplicate. |
| Chapter 15, “Early test-risk advantage over frozen features at matched training loss” (`sec-docs-global-nonlinear-l21578`) | A cubic departure from frozen features | It establishes a risk advantage for one two-hidden-layer tanh design and prescribed target, with a different finite readout initialization. The proposed section establishes a broader compression certificate with no risk advantage claim. |

These precedents should constrain the exposition: present the result as a
complement to trajectory compression, without claiming a first theorem of
hidden motion or a general advantage over kernel methods. A short contextual
cross-reference is sufficient; the new section should not re-explain those
other models.

## Local assumptions and assembly requirements

Retain Chapter 9's fixed-data, fixed-depth, full mean-squared loss,
mobilities $(n,1,\ldots,1,n)$, independent Gaussian hidden initialization,
exactly zero stored readout, analytic strip assumptions, positive feature
Gram gap, and positive small-label condition. Add **only within the new
section** that every activation is nonaffine and

\[
|x_a^\top x_b|<d\qquad(a\ne b).
\]

This allows correlated and rank-deficient input Grams. Since the chapter
already has at least two training examples, the strict condition implies
that the input dimension and the dimension of the training-input span are
at least two. It excludes identical and antipodal training inputs. It must
not become a new assumption of the broader compression theorem.

For Taylor, append at most four deterministic passive witness inputs before
initialization. They may depend on the fixed training problem and carry no
training labels or update terms. The statement must use the augmented panel
and replace $p$ by at most $p+4$ in the existing storage bound. This does
not change the width orders; it does change the panel on which the claim is
made. The witnesses require no future trained state, so this is not an
oracle assumption. No efficient witness-finding claim is needed.

Assembly should preserve the following distinctions explicitly:

- The frozen-kernel comparator belongs to the coupled dense reference;
  it is not the compressed model's own initial tangent kernel.
- Hidden-feature and nonlinear-increment lower bounds concern dense
  variables. Compression transfers prediction gaps, not a neuron-by-neuron
  identification of compressed state with the dense hidden layers.
- The new positive constants may depend on the entire fixed problem.
  They are not the chapter's special activation/depth-only constant $C$,
  and need not be uniform as labels shrink, samples approach parallelism,
  or depth varies.
- The transfer uses the proved absolute error tending to zero for each
  method: `prp-compression-legendre`, `prp-compression-harmonic`, and
  `prp-compression-panel`. The headline relative-error ratio by itself is
  not the needed absolute comparison.
- Use the book's $W^{(L+1)}$ and $\phi^{(\ell)}$, with explicit
  correspondence to the paper's $w$ and $\phi_\ell$. Keep finite RMS
  normalizations and pairings explicit as required by `docs/notation.qmd`;
  do not import the paper's local normalized-norm aliases as a new dialect.

## Proportion and maintenance cost

The selected source is one 62-line theorem/explanation file plus the final
335-line proof file. A single section containing the theorem, its local
supporting lemmas, and complete proofs is proportionate to the 4537-line
chapter and closes an identifiable gap in its interpretation. Reuse the
existing fitting lemma and compression propositions by stable native
cross-references. Do not duplicate the fitting, analytic-source, compiler,
or storage proofs.

Maintenance cost is moderate and confined to mathematical prose and
cross-references. No new code API, experiment, data archive, global notation
entry, or literature dependency is necessary for the proposed scope.
Future changes to the initialization, mobility, loss, query contract, or
compression errors would require checking this section as a dependent
result. No scientific gap identified at this relevance gate warrants a
new research program before assembly.

## Independence, sources, and read coverage

I did not author or assemble the proposed result and have not read prior
audit reports, study history, other reviewers' findings, or `old_docs/`.
No other study's scientific contents were read. Repository status and a
filename-discovery command exposed path metadata only. I made no book,
paper, index, or Git changes; this report is the sole output.

The required rigorous-math skill, canonical-notation skill and its neural
reference, root `AGENTS.md`, and both parts of `RESEARCH_WORKFLOW.md` were
read. Scientific coverage was:

- Complete: `paper/feature_learning_theorem.tex` (1–62),
  `paper/compact_feature_learning.tex` (1–335), `paper/compact.tex`
  (1–298), `paper/compact_fitting.tex` (1–241), `docs/index.qmd`
  (1–260), and `docs/notation.qmd` (1–98).
- Chapter 9: lines 1–511, 2400–2435, 2922–3004, 4250–4269,
  4354–4378, and 4490–4537; headings and scoped keyword matches across
  the complete file. The remaining proof bodies were not audited.
- Duplicate-coverage excerpts located by scoped searches in maintained
  `.qmd` files: `docs/01-training-geometry.qmd` 2500–2720;
  `docs/09-trainability.qmd` 5410–5755;
  `docs/11-shape-and-depth.qmd` 3685–3945;
  `docs/14-generalization.qmd` 3474–3640 and 4040–4090.
  Other book material was limited to keyword hits, not read as proof
  dependencies. This is not a whole-book absence or correctness audit.

The searches targeted nonlinear feature activity, hidden acceleration,
frozen features/kernels, NTK certificates, and nonlinear increments. All
selected source-file reads were completed; truncated tool output relevant
to the selected coverage was reread.

Observed HEAD before the report: `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`.
The working tree already contained unrelated modifications; the index was
empty. The evaluated source identities are:

```text
f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f  paper/feature_learning_theorem.tex
71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1  paper/compact_feature_learning.tex
5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21  paper/compact.tex
6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f  paper/compact_fitting.tex
8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68  docs/index.qmd
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023  docs/notation.qmd
4aeaa51c0da24b65acf8b26edb4c4437dbb5dee14a3f336034de7c787faa6571  docs/08b-trajectory-compression.qmd
ea3b9bf0d19ed2c1023f234737b58e9cb83fc641caf2f7e5ee5b249d30618711  docs/01-training-geometry.qmd
2bd293017b66125c00f3ed338117affcc4d21977b707229091cc80e6c722e477  docs/09-trainability.qmd
81014ee297553b03fa17669b9e30840723f7334b4dbbf4d9f85b11ef5760c3d8  docs/11-shape-and-depth.qmd
2d1cddf57aea48ca596b2b2b3072e3fee5bc42f84223f6951cfe5cb8b396b766  docs/14-generalization.qmd
```
