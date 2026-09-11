# Internal proof and deterministic checks

Coordinator: `/root`, 2026-09-11. This records internal checks, not the
independent promotion reviews. Established book/code files have not been edited.

## Frozen analytic inputs checked

The coordinator read every line of the following reports and checked the
arguments against the complete established sources used by the study:

| File | SHA256 | Outcome |
|---|---|---|
| route_source_response.md | 51eac24d314a529af831194c09efc8552e6c2be823396571ae09acf710c9f17c | Fixed-order source tensors and singular Gaussian expectation calculus checked |
| route_source_second_phase.md | b3c45efde1fc4b22e16b0f49ebf8c0fadf0efdd8146b4dc0400c9fbc6631002e | Uniform finite-program first and mixed second output responses checked |
| route_slab_audit.md | 3434adc3727e693d514d03911f1d08a2015c62e41e5645a5065ff8143fb3596c | Complete separate reconstruction checked |
| route_slab_kernel_addendum.md | 84678ecf58eea56a578dfa7488850224d29f6ba75b9743fd3e4ebef899df81dc | Moment absorption and Borel first-kernel passage checked |
| route_replacement.md | aa085a7a7269f4f2b2c711e0bbeaee430d8a3cff33333d10df9de22b72ffb1d1 | Conditional replacement/Hoeffding theorem, including L2 strengthening, checked |

The first-round weak-topology and integrated-forcing reports were also read
completely. Their surviving tangent-propagation hypotheses remain explicitly
conditional; they are not inputs to the successful source-output route. The
new result does not infer an ambient raw-L2 tangent from finite moments.

## Specific reconstruction

1. In each finite program the derivative exists chronologically before a
   uniform estimate is sought. Every forward covariance, reverse covariance,
   residual, alpha coefficient and beta coefficient is differentiated. The
   source-coordinate derivatives alone do not suffice.
2. Full absolute source-tensor sums control covariance contractions against
   covariance entry suprema. Repeated source indices are included. No product
   of quadrature masses is assigned to repeated upper source derivatives.
3. The lower increment since a time-block boundary has each fixed source
   tensor bounded by its physical duration in every fixed finite Lp. This
   follows by differentiating its time-weighted sum of actual updates.
4. The unknown part of a reverse covariance derivative has at least one new
   source index. Its contraction annihilates the old-boundary expression.
   Subtraction leaves the small lower increment tensor. For alpha the same
   argument uses its third source tensor and sums its row index as well.
5. Lower explicit response forcing carries physical time weights. Its random
   integrating factor has all fixed moments from the actual Gaussian-source
   bound. Coefficient derivatives are deterministic; their norm E contributes
   C ell E. Old response norms enter additively and do not multiply E.
6. Forward covariance and F-row responses consequently cost C ell E plus
   known history. The upper explicit recurrence uses the proved base F density,
   yielding the same estimate for reverse covariance, beta, residual and D.
   Thus one fixed short physical interval absorbs E, independently of steps.
7. Only finitely many moment orders enter this deterministic absorption.
   Higher fixed moments are obtained after E is known, with no further
   absorption. The second-response unknown linear system is identical; its
   other terms are controlled first-response products. Orders 5/3/1 suffice
   for base/first/second source tensors.
8. The actual atom derivative follows from uniform quadratic contamination
   bounds and actual value completion. Finite-sum centering and direction
   formulas pass through jointly continuous atom kernels. This avoids the
   invalid inference that any bounded TV functional has an atom integral
   representation for nonatomic laws.
9. The second bound survives as a rectangular inequality on actual values.
   No continuous Borel Hessian is asserted. Common finite quantization contracts
   the variation norm and preserves probability rectangles.
10. The statistical proof separately controls bias, higher Hoeffding orders,
    and convergence of the first projection to the actual influence. No
    empirical total-variation convergence is used. Bounded cutoffs supported
    inside the analytic neighborhood and exponential finite-test concentration
    justify both probability and mean-square exceptional-event removal.
11. The width-first bridge uses C.4.7 only on good empirical laws. Actual
    finite GF exists for every finite sample by direct finite-time parameter
    bounds. Bounded-Lipschitz tests cost at most twice the bad-law probability;
    no width limit is assumed there.

These checks establish the finite-program estimate and the conditional
statistical lemma internally for their stated scopes. The coordinator then
read the complete canonical source lemma (796 lines, hash
`1550a69ad330544eb4d3a284617b939a9e62e2542cfa4704216537dcbe8c55ac`)
and canonical sampling lemma (363 lines, hash
`21fda6fda72e5846f9ed91eb389bee150de717cb8dd364628b69367e3126bc03`),
and wrote and checked the complete actual-law/finite-width passage.
The assembled full theorem, including the selector's two notation/consistency
suggestions, is internally checked at candidate hash
`53ef8e1c31795ecd1ae8400c9ed8183cc8f1a86a2e71c74a0d736b7eb2b33456`.
Its claim includes A--C and the bounded-extension mean-square strengthening.
The complete selector report was read and its relevant scientific inputs
rehashed. Fresh paired adversarial and separate integration reviews remain
required; no promotion acceptance is inferred from the internal checks.

## Deterministic algebra check

Command, from the repository root:

```
python studies/trained_prediction_sampling/check_gaussian_calculus.py --output data/generated/trained_prediction_sampling/gaussian_checks_01/report.json
```

Observed exit status 0, PASS, six exact polynomial identities, Python 3.10.12.
Source hash `118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef`.
The independent oracle substitutes `(G0+s G1,G0+t G1)` and integrates monomials
using independent scalar Gaussian moments. It verifies both first derivatives
and the mixed second covariance formula, including the singular line s=t.
The complete output is `data/generated/trained_prediction_sampling/gaussian_checks_01/report.json`.
It checks algebraic factors only; it is not evidence replacing the neural proof.
An optional symbolic-library availability check found SymPy absent; the actual
completed check uses only the Python standard library and exact rational values.

The statistical contributor ran the separate exact-enumeration check source
`check_sampling_hoeffding.py`, hash
`4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a`.
The coordinator read its entire implementation. It passed 748 exact assertions
with all four nonconstant Hoeffding orders nonzero, including orthogonality,
every double-replacement identity, and the exact three-term scaled remainder
identity. Original report:
`data/generated/trained_prediction_sampling/statistical_checks/exact_hoeffding_20260911T212903_125941Z/report.json`,
hash `528abe5481c10583ee50266aae543977ab614dc7b9ea054d7ab573e57c062847`.

Both checks were independently executed again by the coordinator's standalone
validation, using identical source bytes copied into the minimal proposed
edition and Python isolated mode with no repository imports. The command was
`python studies/trained_prediction_sampling/validate_proposal.py --output data/generated/trained_prediction_sampling/standalone_v1`.
It exited 0 and reported PASS. Its source is persisted in the study; its full
report is `data/generated/trained_prediction_sampling/standalone_v1/validation_report.json`,
hash `311eacfb64da57d0dbd86cbbd322d2187cb0d42a44ea627957311deae93d8225`.
This additionally verifies all 88 new tags/references, the new navigation link,
and exact inverse preservation of all existing book/guide bytes outside the
specified edits. Unchanged base hashes were checked before and after.

No training run, random simulation, parameter sweep, or finite-width experiment
was performed. All proof sources and check code remain in the flat study folder;
generated reports are reproducible from those sources.

## Corrected edition and review provenance

The full version-1 paired reports and integration report have now been read and
their provenance verified. The integration objections supersede any suggestion
that version 1 was ready for promotion. Their exact resolutions and report/input
hashes are preserved in [review_resolution.md](review_resolution.md).

The coordinator checked each version-2 edit against the frozen original. The
finite-GF existence paragraph now uses explicit ordinary Euclidean/Frobenius
norms and retains the full factor `2|r|` in the middle update. Its first-row
bound uses the operator norm of the initialized action plus the Frobenius norm
of the learned middle increment. Gronwall first bounds the readout, integration
then bounds the middle increment and first-row field on any finite horizon.
The three textual corrections repair a TeX control word, heading placement,
and stale local section references. No source-response or statistical estimate
was changed. Complete fresh version-2 reviews are pending.

Version-2 standalone validation was run from the repository root:

```
python studies/trained_prediction_sampling/validate_proposal_v2.py --output data/generated/trained_prediction_sampling/standalone_v2
```

Observed exit 0, PASS. The full output report hash is
`a43fbd60d00c8891c62d289d1f3c1846722192781c1dde3118b40c7cf2483ec9`.
The candidate hash is
`98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928`.
The exact checks and limitations are as recorded above and in the resolution
record, with an added TeX-control-word whitelist and explicit heading-depth
check. Established scientific/process inputs were unchanged after validation.
