# Revised isolated certification: RESTART_RESPONSE_WINDOW.md

Verdict: **PASS — scoped local restart lemma and its stated conditional
nonaccumulation criterion. No outstanding corrections in this scope.**

Audited candidate: `/tmp/l3-two-sample-Un7kw9/RESTART_RESPONSE_WINDOW.md`.
Length: 764 lines. SHA-256:

```text
cf80b9703dbff418eb9f00bc794309e81a2f9443298acdafe797a0a50975be67
```

The revised candidate was independently read in full. This certification is
based on the mathematical argument in that candidate, including the amended
continuation statements, rather than acceptance of the reported edits.
The `solve-math-rigorously` instructions previously read in full were
applied. The dependency boundary remains `CONTRACT.md`, the permitted
source equations and coefficient-prefix moment/derivative-envelope
arguments of `NONLINEAR_RESPONSE_PERTURBATION.md`, and the formal source
definitions of `TWO_SAMPLE_SOURCE_BASELINE.md`. Their already-read content
was used; no additional dependency files, histories, or other reviews were
opened. No agents or experiments were used.

## Certified statement

The objects are the actual canonical capped finite source programs, with
their full retained history, formal derivatives at frozen coefficients and
covariances, and three separate coordinate populations. Fix finite
\(B,H_*\ge1\) and \(S\). At a reached mesh time \(u\), assume

\[
 \max_{i=1,2,3}\|\mathcal H_i(u)\|_2\le H_*,
\]

where the random envelopes are exactly (3)–(5), and assume the stated
primal bound \(B\) on the retained prefix and candidate future interval.
Then the explicit positive length \(d_*\) in (7) and constants in
(17), (19), (20), (31), and (36) certify the following conclusions for
available continuation nodes within that length and horizon:

\[
 |a^i_{kj}|\le A_i h_j\quad(j<k),\qquad
 \sum_{j\le k}|b^i_{kj}|\le M_i,\qquad i=2,3.
\]

These bounds include every old column. The coordinate fields have a common
subGaussian moment bound on the extended prefix, and its endpoint history
envelopes have the asserted finite \(L^2\) bound \(\Psi(B,H_*,S)\).
The estimates are independent of the auxiliary cap and the number of mesh
nodes. They allow unequal positive steps, singular source covariances,
\(\rho=-1\), either label choice, and the fixed amplitude \(e=0.1\).
Replacing appearances of \(e\) in the constants by 1 also gives the
stated uniformity for \(0<e\le1\).

## Proof recheck

The past-envelope hypothesis yields deterministic old coefficient bounds
(14) by the frozen response identities, Cauchy–Schwarz, and the primal
source-variance bounds. It also controls the actual old forcing with the
new coefficient row. In particular,

\[
 \frac1{h_j}\left|\sum_{r<m}a^2_{kr}D^{2,\zeta}_{r,j}\right|
 \le A_2\mathcal H_2(u),
 \qquad
 \sum_{j\le k}|J^{i,\mathrm{old}}_{k,j}|
 \le1+A_i\mathcal H_i(u).
\]

The old diagonal transpose derivative is included with its own step weight;
that weight cancels its single denominator. The argument never replaces
the new old-column coefficients by row \(m\), drops an old source, or
introduces independence between an old envelope and a new field.

The coefficient closure is causal in the order
\(a^2_k,a^3_k,b^3_k,b^2_k\). The first row uses only earlier bottom
backward rows; the second additionally uses the newly bounded \(a^2_k\).
For these forward outputs the current gates are bounded, so the current
unbounded multiplier in (22) is omitted. The top backward output uses
\(C_k\), which is already determined from earlier top fields. The middle
backward output uses \(q^2_k\) only after \(b^3_k\) has been bounded.
Thus the moment and derivative estimates require only rows available at
the corresponding stage, not the future coefficient conclusion.

The exact current terms \(L^3_k\) and
\(L^2_k+V^2_kb^3_{kk}G^2_k\) are present in the leading forcing
estimates (34)–(35). They are not assigned a short-window factor.
Finite iteration gives the remainder majorants (24), and their expected
values are controlled by (22): each contains just one old envelope, with
Hölder exponents \(2,6,6,6\). This uses only its assumed \(L^2\) norm.
The explicit \(K\) dominates these terms, and \(Kd\le1/2\) closes
all four rows with the stated margin.

The endpoint history estimate does not infer \(FE\in L^2\) from an
arbitrary \(F\in L^2\). After the coefficient closure, the full-origin
canonical derivative equations give an increasing pathwise envelope of
the form

\[
 C\left(1+S+\sum_{r<n}h_rQ^i_r\right)
 \exp\left\{\kappa S+\kappa e\sum_{r<n}h_rQ^i_r\right\},
\]

with \(C\) controlled by the displayed deterministic constants.
The diagonal contribution to the accumulated middle transpose derivatives
is bounded separately by 2; every later term carries the source step.
Weighted convexity and the established subGaussian coordinate moments
then give the \(L^2\) bound (36), and higher finite moments as needed.
This reasoning uses no random maximum of Gaussian coordinates, source-count
factor, ratio of adjacent steps, or division by the terminal zero step.

## Six corrections verified in the revised candidate

| Correction | Revised location | Verification |
| --- | --- | --- |
| Retained primal bound | Lines 597–601 | Uses \(B=\max\{B_{\rm past},2B_0\}\), with the alternative \(B_0\ge B_{\rm past}\), and explicitly distinguishes the reached state from its past. |
| Sufficient continuation length and mesh family | Lines 609–628 | Uses the doubled primal bound and minimum with the primal window; the covering count uses \(\delta_*\), and refinement must remain in the uniformly controlled family. |
| Exact nonlinear contribution wording | Lines 678–685 | Identifies (40) as the contribution of \(L^1_k\), without claiming to isolate every nonlinear dependence of the memory term. |
| Capped multiplier wording | Lines 744–749 | Uses \(g'(Z)\tau_R(q)\) and explicitly identifies \(g'(Z)q\) as the uncut version. |
| Spacing commands in (12) | Lines 198–199 | Both separators are valid `\quad` commands. |
| Current-return math delimiter | Line 558 | The stray backslash has been removed. |

For the prefix-only primal hypothesis, the independently checked sufficient
length is exactly

\[
 \delta_*=
 \min\left\{d_*(2\bar B,\bar H,S),
             \frac{\bar B}{100(2\bar B)^3}\right\}>0.
\]

The local primal first-exit argument supplies the future bound
\(2\bar B\); the retained prefix already lies in that bound. Where the
future primal bound \(\bar B\) is itself supplied, the original response
length \(d_*(\bar B,\bar H,S)\) applies. The covering count is valid
under the stated uniform hypotheses and maximum-step restriction within
the same mesh family. These amendments remove the auxiliary qualifications
identified in the first review.

## Boundary of the certification

Nonaccumulation is conditional on common primal and random-history bounds.
Finiteness at each separate restart, or the recursive certificate (37)
alone, does not imply a divergent sum of available window lengths.
The signed capped energy contribution (40), its absolute majorant (41),
and the weighted Euler-square term remain without the propagation estimate
needed for a global result. The Gaussian example (43) is a valid obstruction
to a general norm inequality, not an actual canonical-response
counterexample.

This PASS certifies the local finite-source estimate and its conditional
continuation criterion. It does not certify an uncut population limit,
unconditional global continuation, or the universal-activation two-sample
theorem. No further correction is required for the certified scope.

The original `RESTART_RESPONSE_WINDOW_REVIEW.md` is preserved. Its SHA-256
at this recheck is:

```text
d7be3a575d8fbb3676ffd0d21522f927f55e244525397be2fe43720be182eeb5
```
