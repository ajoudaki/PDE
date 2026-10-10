# Promotion selection: matched frozen-top NTH storage

Date: 2026-10-10. Role: independent relevance and placement selector; not an
author or assembler of the submitted result. This is an **accept-for-assembly
decision**, not a scientific correctness verdict, completed promotion review,
or authorization to change maintained material.

## Decision and destination

**Accept for assembly; merge the three submitted arguments into one compact
section.** The result has distinct value as a quantitative cost theorem for a
precisely specified autonomous closure. Keep its deep-linear, short-time,
literal-array scope visible in both heading and statement.

The smallest suitable destination is **Part II, Chapter 7, “Observable
representations and autonomous closure,”** in
`docs/07-observable-closure.qmd`. Insert a new section titled **“Literal storage
of the frozen-top neural tangent hierarchy”**, with a descriptive identifier
such as `sec-frozen-top-nth-storage`, immediately after **“7. What unrestricted
fields can encode”** (`sec-docs-linear-dynamics-l1248`) and before **“6. Scope
and obstructions to stronger calculus claims”**
(`sec-docs-gaussian-calculus-l1749`). No new chapter, part, or shared notation
entry is needed. This placement continues the opening discussion of exactly
which representations an obstruction constrains, before the chapter turns to
other calculus and formal-jet obstructions.

Chapter 9, “Complete-trajectory compression,” may carry a short cross-reference
after its statement that the displayed sizes are sufficient rather than
optimal. Its headline theorem should not absorb this result: the new theorem
changes both the parameter regime and the promised horizon. Prepare and review
the book addition first. A later paper insertion should summarize or reproduce
the accepted result and identify the same scope, without treating it as a
fourth complete-trajectory compression construction.

## Distinct scientific value and duplication

The new content is a matched order/storage conclusion for the original ordered
neural tangent hierarchy (NTH): initialized ranks are copied, the highest rank
is frozen, and the retained ranks evolve with the closure's own residual. For
the specified correlated, two-hidden-layer identity-activation family,

\[
N_{\mathrm{literal}}
=\exp\!\bigl[\Theta_Y(\log m\,\log n)\bigr],
\qquad 4\mid m,\quad 4\le m\le\sqrt n,\quad d=m+1.
\]

Here `n` is width, `m` is training count, `d` is input dimension, `Y` is the
fixed positive label magnitude, and `N_literal` counts retained scalar entries
of the prescribed arrays. The optimization is over hierarchy order, at any
fixed positive success probability and any fixed positive multiple of the
actual independent dense-pair discrepancy. For `m` proportional to a fixed
positive power of `n`, the count is `exp(Theta((log n)^2))`. At fixed `m,d` it
is polynomial in width. The general-data local upper is also worth retaining:
it supplies sufficiency without a Gram-gap assumption, and makes the matched
claim more than a lower-bound example.

The inspected existing results do not duplicate this conclusion:

| Existing coverage | Why the candidate is distinct |
| --- | --- |
| Chapter 7, `thm-docs-linear-dynamics-l999`: bounded-contraction scalar/PDE nonclosure | An exact, state-universal obstruction for a restricted encoder class; it does not give approximation cost along these initialized trajectories. |
| Chapter 7, `sec-docs-linear-dynamics-l1248`: unrestricted trajectory-field encoding | Explains why representation restrictions matter, but supplies no initialized NTH order or retained-array bound. |
| Chapter 7, `sec-docs-gaussian-calculus-l3672` and its subsection 10.4 | A raw-square, random-readout, annealed formal-jet/Taylor obstruction with a different order of limits. It is neither the present deep-linear finite-width trajectory nor a growing-order NTH cost theorem. |
| Chapter 7, `sec-docs-gaussian-calculus-l5639` | Exact shallow identity closure for one input and a different initialization; it does not cover two trained hidden layers and growing correlated data. |
| Chapter 7, `sec-docs-global-nonlinear-l12084` | A finite-type nonlinear population approximation with no numerical resource rate; its state and reference system differ. |
| Chapter 9, `thm-compression-headline` and the paper headline | Sufficient storage for different constructions under fixed-data, small-label, complete-trajectory hypotheses; neither NTH optimality nor uniform growing-data bounds are asserted. |

The new result is not an information-theoretic lower bound. The linear
input-output map has structure that other encodings can exploit. Its value is
that an explicit familiar hierarchy can require far more retained entries
than the dense parameter state, despite geometric convergence in hierarchy
order. Do not market this as a lower bound on all compression, all tensor
representations, or nonlinear feature-learning models.

## Exact scope to retain in the assembled statement

1. Two hidden identity layers; independent Gaussian first/hidden matrices;
   exactly zero stored readout; block mobilities `(n,1,n)`. All three blocks
   train, but the predictor remains linear in its input. State the half-MSE
   loss explicitly. The book's usual unhalved MSE changes physical time by a
   factor of two; the source interval must not silently be reused after that
   change.
2. The interval is exactly `0 <= t <= 2^-15` in the source's half-MSE time.
   There is no all-time, fitted-endpoint, arbitrary-horizon, raw-GD, or
   nonlinear-activation claim.
3. The upper allows deterministic data varying with width, `d <= n`, input
   norms at most one, and labels of magnitude at most one. For
   `b = m^-1 sum_a y_a v_a`, the error is bounded by
   `64 ||b||_2 1024^-q`. A deterministic order proportional to `log n` gives
   error at most `D_n/n`, with the probability and zero-`b` convention in the
   submitted matching theorem. The anti-concentration event is for each
   deterministic dataset, not simultaneously for every dataset.
4. The lower uses the displayed correlated dataset, three-quarters positive
   and one-quarter negative labels of fixed magnitude `0 < Y <= 1`,
   `4 | m`, and `d=m+1`. Its Gram gap is positive and uniform. Its exclusion
   of insufficient orders is simultaneous, including initialization-dependent
   order choices subject to a deterministic budget. The fixed success
   probability and comparison factor belong in the meaning of “optimal.”
5. Define `E_n(q)` and `D_n` on the same whole-sphere domain and interval in
   the matched statement. The lower's single passive query already bounds
   that larger error from below. Define the independent dense copy, rather
   than replacing its realized discrepancy by a concentration-rate proxy.
6. Count moving ranks and frozen coefficients separately, including the
   finitely many coordinate-query arrays used to decode arbitrary later
   inputs by linearity. State the data cost and exclude coefficient-generation
   work, initialization peak memory, arithmetic precision, and integration
   error from retained real-coordinate storage.

Use the book's canonical `W^(1), W^(2), W^(3)` notation in the setup, with
the exact local aliases `B=W^(1)/sqrt(n)`, `W=W^(2)`, and
`c=W^(3)/sqrt(n)` for the proof. Use `Y` for the fixed label magnitude
(equal here to label RMS), rather than introducing a potentially misleading
training-step symbol. Define the ordered tensor recursion explicitly and do
not assume symmetry of its input slots.

## Legitimate reuse and assumptions that prevent reuse

The source model can reuse the book's forward normalization and mobility
conventions by the preceding explicit specialization. Chapter 9's exactly-zero
readout is also the same initialization choice. This reuses notation and
model formulas, not Chapter 9's hypotheses or conclusions.

The fully inspected scalar lemma `lem-compression-derivative-transfer`
in `docs/08b-trajectory-compression.qmd` is a legitimate optional reusable
tool for transferring an initial **first** derivative to positive-time
discrepancy. Its assumptions are only scalar holomorphy and a bound on a
parameter-two Bernstein ellipse. The submitted uniform complex disk contains
that ellipse for the stated short real interval, and its bound retains the
factor `||b||_2`. Thus the lemma could replace the elementary second-derivative
transfer used for the sufficient-storage comparison, after showing the
containment and selecting its truncation degree. Doing so adds a forward
chapter reference and changes quantitative bookkeeping without changing the
headline scale; retaining the submitted brief Taylor remainder argument is
likely more economical. This scalar lemma does **not** by itself replace the
arbitrary-derivative Chebyshev estimate needed for the lower bound.

No other inspected established lemma is an adequate substitute for the new
proof obligations. In particular:

- `prp-compression-dense-lower` inherits the fixed-data and small-label setup.
  The new hard family has `gamma=1/2`, `Y` fixed, and growing `m`; it does not
  satisfy `Y <= gamma beta^(-30L)/m`. Neither the book nor paper version may
  supply the required uniform discrepancy estimate by citation.
- The selected-source compiler and Taylor panel construction use a different
  reduced state and dynamics. Their initialization-only provenance does not
  identify their equations with frozen-top NTH. The source compiler statement
  and panel proof opening were inspected for this interface comparison; their
  unread proof remainder is not claimed as a dependency.
- The bounded-contraction, formal-jet, and shallow closure results use
  different quantifiers, architectures, or initializations. None can replace
  the present all-order coefficient lower bound or own-residual comparison.

`paper/compact.tex` contains the overlapping setup/headline and includes its
proof components from other files. Those included files were outside this
selection's allowed input set and were not read. No paper-only result is
approved as a hidden book dependency. If assembly needs a result absent from
the maintained book, its complete statement and proof must enter the frozen
book candidate; a paper label or input directive is insufficient.

## Compact assembly and maintenance cost

Use one setup, one matched-storage theorem with a general-data upper clause,
and one proof organized around the following genuinely necessary arguments:

1. Polynomial leaf counting, zero-readout parity, and the common local
   analytic bound.
2. Ordered-integral reconstruction with each system's own residual, followed
   by contraction and the geometric tail bound.
3. The hard family's nonzero omitted derivative, its transfer to a real
   interval, and the growing-dimension dense-pair upper concentration bound.
4. The elementary product-chi-square small-ball estimate for the upper
   comparison, then the moving/frozen storage count.

These arguments overlap substantially across the three submissions. Prove
their shared estimates once. Keep conservative numerical constants private to
the proof except for the declared horizon; the statement can use explicit
existential constants where that does not weaken quantifiers. A short remark
can record the hidden-feature motion certificate and distinguish linear
prediction from frozen features. No experiment, API, figure, or maintained
code is needed for this theorem-only addition.

Maintenance cost is moderate: most of the proof is new, so an elegant headline
cannot be made self-contained by citing the paper's compression theorem.
The all-order real-time transfer and the uniform Gaussian concentration step
must retain complete justifications or precise maintained dependencies. Do
not import the three full research reports, their internal-check narrative,
repeated boundary lists, or exploratory future routes. A single consolidated
section is proportionate; a new chapter is not.

The section's introduction and a final short scope paragraph should suffice to
prevent misleading comparison with the complete-trajectory constructions.
The paper's future treatment can be a scoped proposition after its compression
theorem or in its comparison discussion, but must preserve the different
label/growth/horizon assumptions. A claim that the present lower bound proves
those constructions superior on the same growing-data problem is unsupported
by the inspected results.

## Coverage, input identity, and remaining gates

Read in full: `AGENTS.md`; `RESEARCH_WORKFLOW.md` Part 2 and its shared-write
paragraph; the promotion skill module; the notation skill and neural-network
reference; all three assigned scientific reports; `docs/index.qmd`,
`docs/notation.qmd`, `docs/_quarto.yml`; and `paper/compact.tex`.

Chapter 7 coverage: all headings; lines 1–118, 345–555, 752–800,
1161–1292, 1571–1612, 1918–1962, 2463–2502, 3162–3210, and
3700–3750. Chapter 9 coverage: all headings; lines 1–225, 2922–3010,
3977–4025, and 4354–4417. These ranges include the full scalar
derivative-transfer lemma/proof and the setup/headline used for the assumption
comparison. The other chapters, the unread complements of these two chapters,
paper input files, study history, linked internal-check reports, other
studies, and `old_docs/` were not read. Embedded status statements in the
assigned reports were not treated as review evidence.

SHA-256 identities at selection:

```text
74cc2f091e4106bbd12d9ecb51ff5049f2b889e613647b148b83188dd76c63f4  MATCHING_RESULT.md
8b4f03bd580adbc078a1f9bb6030101954cb0341e987a22bfcd904d7e7815e50  WORST_CASE_RESULT.md
6cbdc29a429fb7e27d9688f6a6951a5751e62cd8bf490ff8560b9ff786de9733  UPPER_LOCAL_GEOMETRIC.md
8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68  docs/index.qmd
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023  docs/notation.qmd
e8312b9a53ebe0dbff35b93c55f8f8f5f49bd8c3bf633bd44c8bdd2b086f55e7  docs/_quarto.yml
6872261310c15149868c44300a687d201e75e023e8d792c463c8d85318bf80cf  docs/07-observable-closure.qmd
4aeaa51c0da24b65acf8b26edb4c4437dbb5dee14a3f336034de7c787faa6571  docs/08b-trajectory-compression.qmd
5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21  paper/compact.tex
```

No independent scientific audit, code audit, empirical reproduction, or book
build was performed in this selection. The complete canonical candidate,
two fresh complete adversarial reviews, rendered standalone edition,
independent integration review, and approval of the concrete reviewed package
remain the applicable promotion gates. Only this study-owned selection report
was written; no maintained source or Git index was changed.
