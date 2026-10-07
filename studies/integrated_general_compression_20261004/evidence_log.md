# Evidence log: complete integrated-results audit

2026-10-07. Current author request: inspect the entire integrated result for
solidity and harmonization. Review artifacts only; theorem files preserved.

## Review Format Resolution

Author-owned research notes, processed at the author's request. Venue-neutral
unscored audit; no conference rules, acceptance recommendation or numeric
score inferred. Canonical-notation and rigorous-math instructions were read;
the paper-review workflow and severity rubric were applied. This is not
promotion into `docs/` or `paper/`.

## Inventory and frozen inputs

The primary submission is `RESULT.md`, not the historical supporting notes.
The study directory was inventoried by filename; historical reports were
not treated as fresh proof verification. The README describes the intended
single-document scientific contract. There is no main PDF to render.

- RESULT SHA-256: `5aae8d6de7d73cd3b2ddc081d3e45796438480878cc0dbf50f66ab0c66df8f23`.
- RESULT length: 13,187 lines.
- README SHA-256: `0496676ca320425c06eda1b0f07ef87467cd978a666686d8c2f344b73ca2f658`.
- Starting HEAD: `ae6000482eea61174a63c99ddf5393f8c631917d`.
- RESULT and README already had uncommitted changes. They were preserved;
  existing work in other studies and the shared Git index was not changed.

### Complete primary-input reading

Three scoped reviewers read frozen scientific inputs without earlier verdicts.
The lead read the common interfaces and decoder and reconciled cross-section
dependencies. Their union covers every line of RESULT:

| Reader/scope | Original lines read |
|---|---|
| Dense/source/Legendre | 1–2060; 3930–6602 |
| Harmonic | 1–1043; 2060–2606; 6603–7852; 8153–8256 |
| Setup/runtime | 561–938; 2790–3929; 8257–12948 |
| Lead common interfaces/decoder/audit | 1–1043; 2607–2790; 7853–8152; 12949–13187 |

The lead additionally inspected the specific source passages supporting M1;
the setup reviewer checked the decoder resource substitution independently.
This is complete read coverage and targeted reconstruction, not a claim
that four readers independently re-proved the whole document.

Scientific scope remained this study, maintained setup/notation, and the
user-authorized named decoder import. No arbitrary other-study search or
Git-history research was performed. Directly read decoder dependencies in
this audit include `SOURCE_SEED_EXACT_QUERY.md`,
`FULL_FINITE_SOURCE_PROBABILITY.md`, `TWO_GAP_CLOSURE_RESULT.md`, and
`WORD_COST_REFINEMENT.md`. These themselves refer to further finite-source,
precision and implementation proofs; this transitive chain was not fully
reconstructed. That limitation is M2, not a failed source retrieval.

## A. Critical theoretical dependencies

### Shared probabilistic source event

The source estimates at RESULT 3930–5085 support trained-carrier bounds and
complex domains used by all original approximation theorems. The audit
reconstructed the conditional downstream uses but identified missing
intermediate source-to-observable and trace identities at 4071–4074,
4116–4156 and 4448–4453. M1 is an unresolved substantiation concern, not a
demonstrated impossibility. The detailed caveat at 1581–1591 already records
that unresolved source obligations propagate downstream.

The finite-horizon domain supplies the required operator, readout, residual
and strip bounds. The Harmonic extension at 7582–7630 supplies them on disks
at every later real anchor. Its scalar variance inequality follows from
`sqrt(v_j) <= b + s sqrt(v_{j-1})` and the larger source-envelope recurrence.
Thus the setup proof does not add an unsupported *new* all-time hypothesis;
it still inherits M1 upstream.

A second targeted source reading recovered the direct-port trace and the
integrated forward/reverse traces underlying the principal scalar
coefficients. It also isolated the same-root residual-gradient trace as a
rank-one term to be placed in the vanishing remainder. No wrong principal
coefficient or counterexample was identified. This supports a local repair
of the scalar-trace exposition; it does not turn the unexpanded uniform
derivative graphs and nonlinear remainder into a freshly verified theorem.

For that local reconstruction only, let \(\Phi(t,s)\) be the zero-source
cavity parameter propagator, \(H_a=D_\Theta h_a^{(j-1)}\), and
\(R_a=D_\Theta\delta_a^{(j+1)}\). The incoming/outgoing roots are
\(y_i,x_i\). The three principal same-root contractions are
\[
x_i^\top(D_e\delta_a^{(j+1)})x_i h_{a,i},\qquad
-\int\frac2m\sum_b r_bh_{b,i}
x_i^\top R_a\Phi(t,s)R_b^\top x_i\,ds,
\]
\[
-\int\frac2m\sum_b r_b\delta_{b,i}
y_i^\top H_a\Phi(t,s)H_b^\top y_i\,ds.
\]
After the conditional Gaussian trace replacement, the displayed series at
4400–4416 bounds the backward integrated trace by
\(T_0+576e^3D_*^3\mathcal B S^4/\eta^3\). The direct and learned-column
terms are exactly those used in \(D_0,D_1\). The forward contributions are
\(8sf_*^2S^2U_i\), \(sH_{j-1}^2S^2U_i\), and \(sS^2U_i\), bounded by
\(C_FS^2U_i\). All coefficients here are the document's locally defined
source coefficients, not new assumptions. The residual-gradient map gives
a fixed-rank normalized trace of order
\(n^{-1+1/1000}\operatorname{polylog}n\), and hence belongs to the
vanishing remainder. This establishes L9 as a minor omitted bridge,
conditional on the upstream insertion event; it narrows rather than closes M1.

### Logarithmic finite construction

The current exact-query source note supplies a common source/query tolerance
schedule, includes the full two-orientation correction, and distinguishes
fixed-query marginal transfer from a simultaneous code-set event. The word
note declares word-RAM primitives and the additional tiny-label RMS gate.
These are substantive qualifications missing in full detail from RESULT.
The finite source probability note is itself a composition with explicit
map and remainder dependencies; it is not a substitute for reading every
transitive proof. M2 limits the single-document/full-audit assertion.

### Nisan finite-space block generator

Primary source consulted on 2026-10-07:
[Nisan, Pseudorandom Generators for Space-Bounded Computation](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf),
block model and Lemma 3, with the recursive generator/hash construction.
The primary text was retrieved; screenshot requests did not yield a usable
render, so no visual inspection is claimed.

The theorem bounds state between blocks, permits unrestricted finite block
transitions, and supplies exponentially small error when block length
dominates state and recursion depth. The decoder's one-pass transcript-event
verifier fits after padding: running sums fit the stated state, transcript
length pays for the union, and `log n` bounds depth. Noise is fixed first,
then averaged. The outer test keeps counters between member blocks; the
whole member computation is inside a transition. Thus the cited use is valid
at the declared finite-program interface. It does not certify that program's
scientific coupling. Independence of generated blocks is neither needed nor
asserted. The integrated text should state these hypotheses explicitly.

## B. Empirical baselines and methodology

No empirical superiority claim was audited; none is established by the
provided small algebra tests. Setup scaling does not demonstrate practical
speedup over dense training or a necessity for inverse-polynomial Euler steps.
No dataset-dependent experiment or external empirical baseline was required.

## C. Missing citations/baselines

No literature-priority or missing-baseline allegation is made. The concerns
are the integrated document's proof completeness and consistency with its
own detailed assumptions, not an unsupported novelty claim.

## Finding provenance and checks

- M1: direct source-section reading plus scoped source reconstruction.
- M2: integrated finite-decoder proof compared with the specifically cited
  construction and word-cost sources; no claim that unavailable evidence
  establishes falsity.
- L1: compare canonical ratio statements with 925–934 and the explicit
  one-sample counterexample at 5927–5945.
- L2: compare headline equality with exact moving count and fixed inventory
  at 2529–2550; decoder inventory at 2726–2729.
- L3–L6: compare common interface prose with decoder-specific conditions,
  coefficients, unit conventions, and the permitted dimension-one case.
- L7: direct multiplication in 6557–6563. The extra prefactor contributes
  one sample/gap power; the final sixth-power bound is supported.
- L8: direct finite/all-time comparison, malformed TeX, and the elementary
  median tail `2^(-J)` combined with the external-code union.
- L9: second, narrowly scoped source reconstruction and the contractions
  displayed above; the principal coefficients and their series sums check.

All execution commands and versions appear in [code_audit.md](code_audit.md).
All three checks exited zero. A broad `git diff --stat` could not read an
unrelated migration file; the study-scoped read succeeded. No permission
change or inspection of that unrelated content was attempted. No full TeX
render or neural experiment was performed.

## Disposition

The report is [review.md](review.md), with supporting
[claim_ledger.md](claim_ledger.md) and [code_audit.md](code_audit.md).
Only these four audit artifacts were added. The identified corrections have
not been applied to RESULT or README. No commit was requested or made.
