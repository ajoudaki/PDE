# Mathematical review of the main-paper exposition

Reviewer: independent exposition-accuracy agent, 2026-09-06.

## Source reading completed

Read in full: `GF_RESULT.md`, `GENERAL_POPULATION_GF_PROOF.md`,
`GENERAL_DEPTH_RESPONSE_PROOF.md`, and `REVIEW_RECORD.md`.
This review concerns fidelity of the forthcoming exposition to those audited
proofs; it is not a fresh claim of proof-assistant verification or priority.

## Indispensable mathematical content for the main paper

1. Give the concrete stored network and learning-rate scaling. The readout
   remains the stored rescaled vector. Every population middle map must be
   retained together with its actual adjoint: independently redrawing a
   backward map would alter the model.
2. Explain why a fixed number of training steps is insufficient. The target
   interval contains roughly `T*/eta_n` steps, and this tends to infinity.
   A fixed coarse mesh is an intermediate proof construction, not a constraint
   imposed on the actual training step or a trajectory-dependent model.
3. RMS fields and matrix operator norms stay bounded for a positive time by
   finite-depth growth inequalities. This alone does not make the vector field
   Lipschitz in mean square: the derivative-of-activation difference multiplies
   an unbounded reference backward field.
4. The response estimate controls scalar marginal subGaussian tails uniformly
   in time and coarse mesh. It does **not** control the exponential moment of
   the maximum over a time path or over neurons. The proof controls weighted
   time sums, using Jensen without time independence.
5. One historical backward-slot perturbation enters with `Delta omega_b`.
   Retaining that factor gives a total effect proportional to elapsed time,
   rather than to the number of steps. The finite-depth coupled response bounds
   close because their zero-time constants can be chosen bottom-up for forward
   responses and top-down for backward responses, before shrinking the time.
6. Cutoffs create an error coefficient linear in the cutoff. At each backward
   layer, bounded matrices and bounded activation derivatives propagate the
   previous error; the new cutoff error is added. There is no cutoff raised to
   the depth.
7. Gronwall amplification grows like `exp(C R T*)`, while the discarded tail
   decays like `exp(-c R^2)`. This comparison is the decisive quantitative
   mechanism. It supplies Cauchy population Euler paths, uniqueness, and
   stability of actual GD against a finite coarse computation.
8. The oracle uses deterministic population residuals and contractions in a
   fixed finite Gaussian program, but shares initial arrays with actual GD.
   Its finite rank parameter reconstruction has vanishing fixed-mesh defects.
   Comparisons happen either in common population spaces or at the same finite
   width, never as an operator-norm distance from an n-by-n matrix to a limiting
   operator.
9. Send width to infinity at fixed cutoff and coarse mesh, then shrink the
   coarse mesh, then remove the cutoff. This proves every `eta_n -> 0`, with no
   relation to a power of width.

## Scope and wording constraints

- The result is local in mathematical terminology: one fixed positive physical
  time interval survives the limit. It is not an all-finite-horizons theorem.
- Depth, dataset size, and input dimension are fixed in the convergence claim.
  Under the normalized loss and uniform input/root/loss bounds, the existence
  time can be independent of dataset size, dimension and Gram eigenvalues;
  this is not uniform convergence for growing data or dimension.
- The activation class is C1 with bounded globally Lipschitz derivative;
  activation values may grow linearly. ReLU is outside this class. The proof
  first treats bounded second derivative and then uses uniform mollification.
- Initialization groups are independent. First-weight scalar entries are iid
  centered subGaussian; middle matrices remain iid Gaussian with variance
  `sigma_ell^2/n`; the stored readout can have any iid subGaussian law, including
  noncentered or nonvanishing laws. Degenerate scales and zero learning
  multipliers are allowed for existence.
- General separable losses require common bounds and Lipschitz constants for
  their first derivatives on bounded prediction intervals. Their coefficients
  are frozen only inside the response calculation, not in the actual flow.
- Uniqueness is for a common initial field/operator state. Only the constructed
  reference flow requires the tail estimate; a competing strong solution needs
  only the preliminary norm bound.
- An autonomous population state consists of finitely many fields and maps but
  infinitely many scalar degrees of freedom. No finite scalar closure follows.
- Strict nonzero feature activity is a separate two-hidden-layer result under
  stronger initialization, geometry, label, scale, and nonaffinity conditions.
  It must not be asserted at arbitrary depth by this existence theorem.
- The parameter scaling, fixed-step Gaussian limits, and operator formulation
  have precedents; the claimed proof contribution here is the mesh-uniform
  estimate and joint positive-time width/GD comparison.

## Appendix review, first draft

Read `gf_exposition/appendix.tex` in full. Its substantive claims and estimates
faithfully reproduce the audited proof, including the explicit noncircular cap
selection, marginal-versus-pathwise tail distinction, finite-width proxy
consistency, and uniqueness against a competitor without assumed tails. No
new mathematical gap found in this exposition.

Corrections sent to the author:

- Remove the stray comma after `(f_{b,s}-y_b)` in the accumulated middle
  operator formula.
- Repair the TeX typo `\\!left[` to `\\!\\left[` in the hidden-velocity formula.
- The generic algebra templates in the localization subsection omit layer
  superscripts on `W,H,Z,phi`. They are mathematically intelligible, but adding
  the layer superscripts would comply literally with the user's canonical
  notation instruction.

## Main-paper review

Read `gf_exposition/main.tex` in full and checked its compiled PDF text.
The compiled document has 10 pages: nine exposition pages, with references
beginning on page nine and continuing on page ten. Visually inspected the
rendered page six; all equations and the explicit sensitivity statement fit
and are legible.

**Substantive verdict: PASS.** The main-paper scope agrees with the source
theorem and appendix. The prose conveys the mathematical mechanism rather
than only listing lemmas: concrete feature transport; the second-moment
product obstruction; correlated Gaussian matrix reuse; the `Delta omega_b`
pulse; marginal tails from weighted time sums; additive depth propagation of
cutoff errors; and the fixed-coarse computation that removes any width/step
coupling. No essential insight is hidden entirely in the appendix. Technical
operator construction and sensitivity-cap bookkeeping are appropriately
delegated there.

Small required precision corrections sent to the author:

1. State `2 <= ell <= L` next to the hidden-preactivation derivative on page
   four, to avoid an apparent layer-zero activation at `ell=1`.
2. Rephrase the theorem opening that parameter trajectories ``have the
   population limit'' as convergence in the subsequently specified observable
   sense. The existing later disclaimer is correct, but the opening should
   not suggest an operator-norm limit between different widths.
3. The main paper promises exact finite updates in the appendix. The first
   appendix draft displays the accumulated middle update but omits exact
   finite first-weight/readout updates. Add them once or narrow that promise.

## Final verification of repairs

Rechecked the revised main paper and the affected appendix passages. The main
theorem now explicitly states convergence in the listed observable senses, and
the hidden derivative is restricted to `2 <= ell <= L`. The appendix now gives
the exact first-weight, first-preactivation, middle-weight and readout finite
updates, with the correct factors of `2`, `eta_n`, `n`, the input normalization,
and the dataset weights. Both TeX typos were repaired. The localization
templates now carry explicit layer superscripts; the unrelated numerical
norm bounds no longer use bare lowercase field names.

**Final verdict: PASS, with no required mathematical or scope correction
remaining.** The user-requested core mechanisms are conveyed in the main text,
and the appendix contains their detailed derivation. This review found no
conditional source claim silently promoted to a proved assertion, no
depth-uniform or all-time overclaim, and no inappropriate independence or
cross-width operator-convergence assertion.
